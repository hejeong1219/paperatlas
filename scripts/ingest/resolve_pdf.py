#!/usr/bin/env python3
"""Resolve a paper's PDF via PubMed -> DOI/PMCID -> publisher API.

Pipeline:
  1) title -> PubMed esearch (author + year + key terms) -> PMID
  2) Validate PMID by checking author last name + year match
  3) DOI/PMCID lookup -> Europe PMC, Unpaywall, doi-direct, Elsevier, Springer
"""
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path


NCBI_BASE = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
UNPAYWALL_EMAIL = os.environ.get("UNPAYWALL_EMAIL", "omics259259@gmail.com")
ELSEVIER_KEY = os.environ.get("ELSEVIER_KEY", "25b29b9a49f64f62ddf2d796377e8ebe")
SPRINGER_KEY = os.environ.get("SPRINGER_KEY", "b3ff5134cc702630bf31b6311f9aace3")

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"


def http_get(url, headers=None, timeout=30):
    h = {"User-Agent": UA, "Accept": "*/*"}
    if headers:
        h.update(headers)
    req = urllib.request.Request(url, headers=h)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read(), r.headers.get("Content-Type", ""), r.geturl()


def title_keywords(title, n=3):
    skipwords = {"a", "an", "the", "of", "in", "on", "and", "for", "to", "by", "with",
                 "from", "as", "via", "is", "are", "be", "at", "or", "into", "vs",
                 "versus", "this", "that", "their", "its", "but", "novel", "new", "human",
                 "study", "studies", "analysis", "based"}
    words = re.findall(r"[a-zA-Z][a-zA-Z\-]{3,}", title.lower())
    words = [w for w in words if w not in skipwords]
    # Prefer longer/more specific words
    words.sort(key=lambda w: -len(w))
    return words[:n]


def pubmed_search_pmid(title, year, first_author):
    """Author+year-anchored search; verify with title overlap. Tries multiple
    query forms from strict to loose."""
    kws = title_keywords(title, n=4)
    one_kw = kws[0] if kws else ""
    two_kw_and = " AND ".join(kws[:2]) if len(kws) >= 2 else (kws[0] if kws else "")
    queries = []
    if kws:
        queries.append(f'{first_author}[Author] AND {year}[PDAT] AND {one_kw}[Title]')
    queries.append(f'{first_author}[Author] AND {year}[PDAT]')
    if two_kw_and:
        queries.append(f'{first_author}[Author] AND ({two_kw_and})')
    if kws:
        queries.append(f'{first_author}[Author] AND {kws[0]}[Title]')
    for q in queries:
        url = f"{NCBI_BASE}/esearch.fcgi?db=pubmed&retmode=json&retmax=20&term=" + urllib.parse.quote(q)
        try:
            data, _, _ = http_get(url)
            j = json.loads(data)
            ids = j.get("esearchresult", {}).get("idlist", [])
            if ids:
                pmid = validate_pmid_match(ids, title, year, first_author)
                if pmid:
                    return pmid
        except Exception:
            pass
    return None


def validate_pmid_match(pmids, title, year, first_author):
    """Pick a PMID whose record matches author last name + year."""
    if not pmids:
        return None
    url = f"{NCBI_BASE}/efetch.fcgi?db=pubmed&id=" + ",".join(pmids[:10]) + "&retmode=xml"
    try:
        data, _, _ = http_get(url, timeout=30)
        root = ET.fromstring(data)
        title_words = set(re.findall(r"[a-zA-Z]{4,}", title.lower()))
        for art in root.findall(".//PubmedArticle"):
            pmid_el = art.find(".//PMID")
            if pmid_el is None: continue
            pmid = pmid_el.text
            # Year
            yr = ""
            ye = art.find(".//Journal/JournalIssue/PubDate/Year")
            if ye is not None:
                yr = ye.text
            else:
                md = art.find(".//Journal/JournalIssue/PubDate/MedlineDate")
                if md is not None:
                    m = re.search(r"\d{4}", md.text or "")
                    if m: yr = m.group(0)
            try:
                year_diff = abs(int(yr) - int(year))
            except Exception:
                year_diff = 99
            if year_diff > 1:
                continue
            # First author last name
            first_au = art.find(".//AuthorList/Author/LastName")
            if first_au is None or not first_au.text:
                continue
            au_last = re.sub(r"[^a-z]", "", first_au.text.lower())
            req_last = re.sub(r"[^a-z]", "", first_author.lower())
            if au_last != req_last and not (au_last.startswith(req_last[:6]) or req_last.startswith(au_last[:6])):
                continue
            # Title overlap
            t_el = art.find(".//ArticleTitle")
            if t_el is None: continue
            cand_title = "".join(t_el.itertext()).lower()
            cand_words = set(re.findall(r"[a-zA-Z]{4,}", cand_title))
            overlap = len(title_words & cand_words)
            if overlap < min(3, max(2, len(title_words) // 4)):
                continue
            return pmid
    except Exception:
        return None
    return None


def pubmed_meta(pmid):
    url = f"{NCBI_BASE}/esummary.fcgi?db=pubmed&retmode=json&id={pmid}"
    meta = {"pmid": pmid, "doi": None, "pmcid": None, "journal": None, "title": None, "year": None}
    try:
        data, _, _ = http_get(url)
        j = json.loads(data)
        rec = j.get("result", {}).get(pmid, {})
        meta["title"] = rec.get("title")
        meta["journal"] = rec.get("fulljournalname") or rec.get("source")
        meta["year"] = rec.get("pubdate", "")[:4]
        for aid in rec.get("articleids", []):
            if aid.get("idtype") == "doi":
                meta["doi"] = aid.get("value")
            elif aid.get("idtype") == "pmc":
                meta["pmcid"] = aid.get("value")
    except Exception:
        pass
    return meta


def try_save_pdf(data, out_path):
    if not data or len(data) < 5000:
        return False
    if data[:4] != b"%PDF":
        return False
    out_path.write_bytes(data)
    return True


def try_europepmc(pmcid, out_path):
    if not pmcid: return False, "no pmcid"
    url = f"https://europepmc.org/backend/ptpmcrender.fcgi?accid={pmcid}&blobtype=pdf"
    try:
        data, ctype, _ = http_get(url, timeout=60)
        if try_save_pdf(data, out_path):
            return True, url
        return False, f"europepmc not-pdf ({ctype})"
    except Exception as e:
        return False, f"europepmc err: {e}"


def try_unpaywall(doi, out_path):
    if not doi: return False, "no doi"
    api = f"https://api.unpaywall.org/v2/{urllib.parse.quote(doi)}?email={UNPAYWALL_EMAIL}"
    try:
        data, _, _ = http_get(api, timeout=30)
        j = json.loads(data)
        oa = j.get("best_oa_location") or {}
        pdf_url = oa.get("url_for_pdf") or oa.get("url")
        if not pdf_url:
            for loc in j.get("oa_locations") or []:
                if loc.get("url_for_pdf"):
                    pdf_url = loc["url_for_pdf"]; break
        if not pdf_url: return False, "unpaywall no oa"
        try:
            pdata, ctype, _ = http_get(pdf_url, timeout=60)
            if try_save_pdf(pdata, out_path):
                return True, pdf_url
            return False, f"unpaywall url not-pdf ({ctype})"
        except Exception as e:
            return False, f"unpaywall fetch err: {e}"
    except Exception as e:
        return False, f"unpaywall api err: {e}"


def try_elsevier(doi, out_path):
    if not doi: return False, "no doi"
    url = f"https://api.elsevier.com/content/article/doi/{urllib.parse.quote(doi)}"
    headers = {"X-ELS-APIKey": ELSEVIER_KEY, "Accept": "application/pdf"}
    try:
        data, ctype, _ = http_get(url, headers=headers, timeout=60)
        if try_save_pdf(data, out_path):
            return True, url
        return False, f"elsevier not-pdf ({ctype})"
    except Exception as e:
        return False, f"elsevier err: {e}"


def try_springer(doi, out_path):
    if not doi: return False, "no doi"
    url = f"https://api.springernature.com/article/pdf/{urllib.parse.quote(doi)}?api_key={SPRINGER_KEY}"
    try:
        data, ctype, _ = http_get(url, timeout=60)
        if try_save_pdf(data, out_path):
            return True, url
    except Exception:
        pass
    meta_url = f"https://api.springernature.com/meta/v2/json?q=doi:{urllib.parse.quote(doi)}&api_key={SPRINGER_KEY}"
    try:
        data, _, _ = http_get(meta_url, timeout=30)
        j = json.loads(data)
        records = j.get("records") or []
        if not records: return False, "springer no record"
        urls = records[0].get("url") or []
        for u in urls:
            if u.get("format") == "pdf":
                try:
                    pdata, ctype, _ = http_get(u["value"], timeout=60)
                    if try_save_pdf(pdata, out_path):
                        return True, u["value"]
                except Exception:
                    pass
        return False, "springer no pdf url"
    except Exception as e:
        return False, f"springer err: {e}"


def try_doi_direct(doi, journal, out_path):
    if not doi: return False, "no doi"
    # Springer Nature
    m = re.match(r"^10\.1038/(.+)$", doi)
    if m:
        for url in [
            f"https://www.nature.com/articles/{m.group(1)}.pdf",
            f"https://www.nature.com/articles/{m.group(1)}",
        ]:
            try:
                data, ctype, _ = http_get(url, timeout=60)
                if try_save_pdf(data, out_path):
                    return True, url
            except Exception: pass
    # BMC / Springer Open
    m = re.match(r"^10\.1186/(.+)$", doi)
    if m:
        try:
            data, _, _ = http_get(f"https://doi.org/{doi}", timeout=30)
            # BMC redirects; just try direct PDF guess via doi resolution
        except Exception: pass
    # eLife
    m = re.match(r"^10\.7554/eLife\.(.+)$", doi)
    if m:
        url = f"https://elifesciences.org/articles/{m.group(1).split('.')[0]}.pdf"
        try:
            data, _, _ = http_get(url, timeout=60)
            if try_save_pdf(data, out_path):
                return True, url
        except Exception: pass
    return False, "doi-direct no match"


def try_biorxiv(doi, title, year, out_path):
    """bioRxiv/medRxiv search by title."""
    if not title or len(title) < 20: return False, "no title"
    # Search bioRxiv API
    try:
        import urllib.parse as up
        clean = re.sub(r"[^a-zA-Z0-9 ]", " ", title)
        clean = re.sub(r"\s+", " ", clean).strip()[:120]
        url = f"https://api.biorxiv.org/details/biorxiv/{up.quote(clean)}/{year or 0}/{(year or 0) + 1}/0"
        # bioRxiv has different API — just try preprint dois
    except Exception:
        pass
    return False, "biorxiv n/a"


def try_europepmc_xml(pmcid, out_path):
    """Try Europe PMC full-text XML render to PDF (some content not in PMC PDF)."""
    if not pmcid: return False, "no pmcid"
    # Try the open-access render
    urls = [
        f"https://europepmc.org/articles/{pmcid}?pdf=render",
        f"https://europepmc.org/api/get/{pmcid}/fullTextPDF",
    ]
    for url in urls:
        try:
            data, _, _ = http_get(url, timeout=60)
            if try_save_pdf(data, out_path):
                return True, url
        except Exception:
            continue
    return False, "europepmc-xml no pdf"


def resolve_and_download(ref, out_dir: Path):
    result = {
        "slug": ref["slug"],
        "pmid": None, "pmcid": None, "doi": None, "journal": None,
        "downloaded": False, "pdf_path": None, "tried": [], "via": None,
    }
    out_path = out_dir / (ref["slug"] + ".pdf")
    if out_path.exists() and out_path.stat().st_size > 5000:
        result["downloaded"] = True
        result["pdf_path"] = str(out_path)
        result["via"] = "already-on-disk"
        return result
    pmid = pubmed_search_pmid(ref["title"], ref["year"], ref["first_author_last"])
    if pmid:
        result["pmid"] = pmid
        meta = pubmed_meta(pmid)
        result["doi"] = meta.get("doi")
        result["pmcid"] = meta.get("pmcid")
        result["journal"] = meta.get("journal")
    chain = [
        ("europepmc", lambda: try_europepmc(result["pmcid"], out_path)),
        ("europepmc-xml", lambda: try_europepmc_xml(result["pmcid"], out_path)),
        ("unpaywall", lambda: try_unpaywall(result["doi"], out_path)),
        ("doi-direct", lambda: try_doi_direct(result["doi"], result["journal"], out_path)),
        ("elsevier", lambda: try_elsevier(result["doi"], out_path)),
        ("springer", lambda: try_springer(result["doi"], out_path)),
    ]
    for name, fn in chain:
        try:
            ok, msg = fn()
            result["tried"].append({"src": name, "ok": ok, "msg": msg})
            if ok:
                result["downloaded"] = True
                result["pdf_path"] = str(out_path)
                result["via"] = name + ": " + msg
                return result
        except Exception as e:
            result["tried"].append({"src": name, "ok": False, "msg": f"exc: {e}"})
    return result


def main():
    if len(sys.argv) < 3:
        print("usage: resolve_pdf.py <unmatched.json> <output_dir>")
        sys.exit(1)
    refs_path = Path(sys.argv[1])
    out_dir = Path(sys.argv[2])
    out_dir.mkdir(parents=True, exist_ok=True)
    refs = json.loads(refs_path.read_text())
    results = []
    for i, ref in enumerate(refs):
        print(f"[{i+1}/{len(refs)}] {ref['slug'][:60]}", file=sys.stderr)
        try:
            res = resolve_and_download(ref, out_dir)
        except Exception as e:
            res = {"slug": ref["slug"], "downloaded": False, "tried": [], "via": None, "exc": str(e)}
        status = "OK" if res.get("downloaded") else "PEND"
        print(f"   {status} pmid={res.get('pmid')} doi={res.get('doi')} via={res.get('via')}", file=sys.stderr)
        results.append(res)
        time.sleep(0.3)
    out_json = refs_path.parent / (refs_path.stem + "_resolved.json")
    out_json.write_text(json.dumps(results, indent=2))
    ok = sum(1 for r in results if r.get("downloaded"))
    print(f"\nDownloaded {ok}/{len(results)} PDFs", file=sys.stderr)
    print(f"Wrote {out_json}", file=sys.stderr)


if __name__ == "__main__":
    main()
