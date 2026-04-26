#!/usr/bin/env python3
"""Fetch full PubMed metadata + abstract via efetch xml for a list of PMIDs.

Reads <unmatched_resolved.json> with pmid/doi/etc and fetches abstract text
into the same record. Writes back as <stem>_meta.json.
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
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"


def fetch_xml(pmids):
    if not pmids:
        return ""
    url = f"{NCBI}/efetch.fcgi?db=pubmed&id=" + ",".join(pmids) + "&retmode=xml"
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read().decode("utf-8", errors="ignore")


def parse_abstracts(xml_text):
    """Return dict pmid -> {abstract, mesh, authors, journal, year, title, doi}"""
    out = {}
    root = ET.fromstring(xml_text)
    for art in root.findall(".//PubmedArticle"):
        pmid_el = art.find(".//PMID")
        if pmid_el is None:
            continue
        pmid = pmid_el.text
        title_el = art.find(".//ArticleTitle")
        title = "".join(title_el.itertext()) if title_el is not None else ""
        abst_parts = []
        for ab in art.findall(".//Abstract/AbstractText"):
            label = ab.attrib.get("Label")
            text = "".join(ab.itertext())
            if label:
                abst_parts.append(f"**{label}**: {text}")
            else:
                abst_parts.append(text)
        abstract = "\n\n".join(abst_parts).strip()
        journal_el = art.find(".//Journal/Title")
        journal = journal_el.text if journal_el is not None else ""
        year = ""
        ye = art.find(".//Journal/JournalIssue/PubDate/Year")
        if ye is not None:
            year = ye.text
        else:
            md = art.find(".//Journal/JournalIssue/PubDate/MedlineDate")
            if md is not None:
                m = re.search(r"\d{4}", md.text or "")
                if m:
                    year = m.group(0)
        authors = []
        for au in art.findall(".//AuthorList/Author"):
            ln = au.find("LastName")
            fn = au.find("ForeName") or au.find("Initials")
            if ln is not None:
                authors.append((ln.text or "") + (" " + (fn.text or "") if fn is not None else ""))
        mesh = []
        for mh in art.findall(".//MeshHeadingList/MeshHeading/DescriptorName"):
            if mh.text:
                mesh.append(mh.text)
        kws = []
        for kw in art.findall(".//KeywordList/Keyword"):
            if kw.text:
                kws.append(kw.text)
        doi = None
        for aid in art.findall(".//ArticleIdList/ArticleId"):
            if aid.attrib.get("IdType") == "doi":
                doi = aid.text
        out[pmid] = {
            "title": title,
            "abstract": abstract,
            "journal": journal,
            "year": year,
            "authors": authors,
            "mesh": mesh,
            "keywords": kws,
            "doi": doi,
        }
    return out


def main():
    if len(sys.argv) < 2:
        print("usage: fetch_abstract.py <resolved.json>")
        sys.exit(1)
    src = Path(sys.argv[1])
    refs = json.loads(src.read_text())
    pmids = [r["pmid"] for r in refs if r.get("pmid")]
    # Batch efetch (max 200 at once)
    metas = {}
    for i in range(0, len(pmids), 100):
        batch = pmids[i:i+100]
        try:
            xml = fetch_xml(batch)
            metas.update(parse_abstracts(xml))
        except Exception as e:
            print(f"  efetch err: {e}", file=sys.stderr)
        time.sleep(0.5)
    print(f"Fetched abstracts for {len(metas)}/{len(pmids)} PMIDs", file=sys.stderr)
    for r in refs:
        if r.get("pmid") and r["pmid"] in metas:
            r["meta"] = metas[r["pmid"]]
    out = src.parent / (src.stem.replace("_resolved", "") + "_meta.json")
    out.write_text(json.dumps(refs, indent=2, ensure_ascii=False))
    print(f"Wrote {out}", file=sys.stderr)


if __name__ == "__main__":
    main()
