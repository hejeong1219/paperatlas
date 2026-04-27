#!/usr/bin/env python3
"""For source pages whose body still says 'Abstract pending', search PubMed by
title to find PMID, then fetch abstract + DOI/journal/year, and patch the
page (placeholder -> abstract; frontmatter gains pmid/doi/journal if missing).
"""
import json
import re
import sys
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

NCBI = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
UA = "llm-wiki/0.1"
PLACEHOLDER = "_Abstract pending — see source PDF or external link for full content._"


def http_get(url, timeout=30):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def title_from_page(text):
    m = re.search(r'^title:\s*"?([^"\n]+)"?', text, re.MULTILINE)
    if m:
        return m.group(1).strip().rstrip('"').strip()
    m = re.search(r"^# (.+)$", text, re.MULTILINE)
    if m:
        return m.group(1).strip()
    return None


def slug_year_author(slug):
    m = re.match(r"^([a-z]+)-(\d{4})-", slug)
    if m:
        return m.group(1), int(m.group(2))
    return None, None


def title_keywords(title, n=4):
    skipwords = {"a","an","the","of","in","on","and","for","to","by","with","from","as","via","is","are","be","at","or","into","vs","versus","this","that","their","its","but","novel","new","human","study","analysis"}
    words = re.findall(r"[a-zA-Z][a-zA-Z\-]{3,}", title.lower())
    words = [w for w in words if w not in skipwords]
    words.sort(key=lambda w: -len(w))
    return words[:n]


def search_pmid(title, year, author):
    kws = title_keywords(title, n=4)
    queries = []
    if kws:
        queries.append(f"{author}[Author] AND {year}[PDAT] AND {kws[0]}[Title]")
    queries.append(f"{author}[Author] AND {year}[PDAT]")
    if kws:
        queries.append(f"{author}[Author] AND {kws[0]}[Title]")
    title_words = set(re.findall(r"[a-zA-Z]{4,}", title.lower()))
    for q in queries:
        url = f"{NCBI}/esearch.fcgi?db=pubmed&retmode=json&retmax=10&term=" + urllib.parse.quote(q)
        try:
            data = http_get(url, timeout=20)
            ids = json.loads(data).get("esearchresult", {}).get("idlist", [])
            if not ids: continue
            # validate by efetch
            efetch_url = f"{NCBI}/efetch.fcgi?db=pubmed&id={','.join(ids[:10])}&retmode=xml"
            xml = http_get(efetch_url, timeout=30)
            root = ET.fromstring(xml)
            for art in root.findall(".//PubmedArticle"):
                pmid_el = art.find(".//PMID")
                if pmid_el is None: continue
                pmid = pmid_el.text
                # author check
                first_au = art.find(".//AuthorList/Author/LastName")
                if first_au is None or not first_au.text: continue
                au_norm = re.sub(r"[^a-z]", "", first_au.text.lower())
                if not (au_norm.startswith(author[:6]) or author.startswith(au_norm[:6])):
                    continue
                # year check
                ye = art.find(".//Journal/JournalIssue/PubDate/Year")
                yr = ye.text if ye is not None else ""
                if not yr:
                    md = art.find(".//Journal/JournalIssue/PubDate/MedlineDate")
                    if md is not None:
                        m2 = re.search(r"\d{4}", md.text or "")
                        if m2: yr = m2.group(0)
                try:
                    if abs(int(yr) - year) > 1: continue
                except Exception:
                    pass
                # title overlap
                t_el = art.find(".//ArticleTitle")
                cand_title = "".join(t_el.itertext()).lower() if t_el is not None else ""
                cand_words = set(re.findall(r"[a-zA-Z]{4,}", cand_title))
                if len(title_words & cand_words) < 3: continue
                return pmid, art
        except Exception:
            pass
        time.sleep(0.2)
    return None, None


def extract_meta(art):
    meta = {"abstract": "", "doi": None, "journal": None, "year": None, "pmcid": None}
    parts = []
    for ab in art.findall(".//Abstract/AbstractText"):
        label = ab.attrib.get("Label")
        text = "".join(ab.itertext()).strip()
        if not text: continue
        parts.append(f"**{label}**: {text}" if label else text)
    meta["abstract"] = "\n\n".join(parts)
    j = art.find(".//Journal/Title")
    meta["journal"] = j.text if j is not None else None
    ye = art.find(".//Journal/JournalIssue/PubDate/Year")
    meta["year"] = ye.text if ye is not None else None
    for aid in art.findall(".//ArticleIdList/ArticleId"):
        if aid.attrib.get("IdType") == "doi": meta["doi"] = aid.text
        elif aid.attrib.get("IdType") == "pmc": meta["pmcid"] = aid.text
    return meta


def patch_page(text, pmid, meta):
    # Replace placeholder with abstract
    if meta["abstract"] and PLACEHOLDER in text:
        text = text.replace(PLACEHOLDER, meta["abstract"])
    # Frontmatter: add pmid/doi/journal/year if missing
    fm_end = text.find("\n---", 4)
    if fm_end < 0: return text
    fm = text[4:fm_end]
    body = text[fm_end:]
    additions = []
    if "pmid:" not in fm and pmid:
        additions.append(f'pmid: "{pmid}"')
    if "doi:" not in fm and meta.get("doi"):
        additions.append(f'doi: "{meta["doi"]}"')
    if "journal:" not in fm and meta.get("journal"):
        additions.append(f'journal: "{meta["journal"]}"')
    if "pmcid:" not in fm and meta.get("pmcid"):
        additions.append(f'pmcid: "{meta["pmcid"]}"')
    if additions:
        fm = fm.rstrip() + "\n" + "\n".join(additions) + "\n"
    return "---\n" + fm + body


def main():
    sources = Path("wiki/sources")
    targets = []
    for f in sources.glob("*.md"):
        if f.stem == "index": continue
        text = f.read_text()
        if PLACEHOLDER not in text: continue
        title = title_from_page(text)
        author, year = slug_year_author(f.stem)
        if not (title and author and year): continue
        targets.append((f, title, author, year))
    print(f"Pages needing backfill: {len(targets)}", file=sys.stderr)
    updated = 0
    for i, (f, title, author, year) in enumerate(targets):
        if i and i % 10 == 0:
            print(f"  [{i}/{len(targets)}] updated={updated}", file=sys.stderr)
        pmid, art = search_pmid(title, year, author)
        if not pmid:
            time.sleep(0.2)
            continue
        meta = extract_meta(art)
        text = f.read_text()
        new_text = patch_page(text, pmid, meta)
        if new_text != text:
            f.write_text(new_text)
            updated += 1
        time.sleep(0.3)
    print(f"\nBackfilled {updated}/{len(targets)} pages", file=sys.stderr)


if __name__ == "__main__":
    main()
