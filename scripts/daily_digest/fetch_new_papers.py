#!/usr/bin/env python3
"""Phase B — search PubMed for new 한미암-relevant papers, download full PDFs,
extract text, and emit a JSON of candidates ready for LLM relevance judgment.

Steps:
  1. PubMed esearch with the proteogenomics × drug response × cancer query,
     restricted to recent Entrez date window (default last 7 days).
  2. PubMed efetch → metadata (title, journal, year, doi, authors, pmcid).
  3. Filter out PMIDs already in wiki/sources/*.md or wiki/_meta/slack-posted.json.
  4. For each remaining candidate:
       - Try resolve_pdf.resolve_and_download() (EuropePMC, Unpaywall,
         doi-direct, Elsevier, Springer).
       - Fall back to ezproxy_download (Korea Univ proxy) if those fail.
       - Skip if no PDF obtained or text < 1000 chars.
  5. pdftotext extract; emit `{candidates: [...]}` JSON to stdout.

Output schema (each candidate):
  {
    pmid, slug, title, authors[], year, journal, doi, pmcid,
    pdf_path,         # relative to repo root
    full_text,        # truncated to ~30K chars by extract_pdf_text
    download_via      # which source the PDF came from
  }

Empty candidates list = no NEW papers obtained today; orchestrator should
fall back to backlog (Phase A select_papers.py).
"""
import argparse
import datetime
import json
import os
import re
import sys
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
INGEST = REPO / "scripts/ingest"
sys.path.insert(0, str(INGEST))

# Reuse existing infra
from resolve_pdf import resolve_and_download  # noqa: E402
from extract_pdf_text import extract as pdf_extract  # noqa: E402

NCBI = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"

# Default query — proteogenomics × drug response × cancer × human
# Tier 1 (phospho × resistance) gets boosted via OR with tighter terms.
DEFAULT_QUERY = (
    "((phosphoproteomic*[All] OR proteogenomic*[All] OR ppQTL[All] OR pQTL[All]) "
    "AND (drug response[All] OR drug resistance[All] OR chemoresistance[All] "
    "OR treatment response[All] OR therapy resistance[All] "
    "OR targeted therapy[All] OR immunotherapy[MeSH] "
    "OR kinase inhibitor[All] OR neoantigen*[All]) "
    "AND (cancer[MeSH Terms] OR neoplasm*[MeSH Terms] OR tumor*[All]) "
    "AND humans[Filter] "
    "AND English[lang])"
)

SKIP_TITLE_WORDS = {
    "a", "an", "the", "of", "in", "on", "and", "for", "to", "by", "with",
    "from", "as", "via", "is", "are", "be", "at", "or", "into", "novel",
    "new", "human", "study", "based", "using", "between",
}


def http_get_json(url, timeout=60):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read())


def http_get_bytes(url, timeout=120):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def esearch(query, days, retmax):
    """Return list of PMIDs matching query within last `days` Entrez days."""
    full_query = f"{query} AND (\"last {days} days\"[EDat])"
    url = NCBI + "/esearch.fcgi?" + urllib.parse.urlencode({
        "db": "pubmed",
        "term": full_query,
        "retmax": retmax,
        "retmode": "json",
        "sort": "date",
    })
    print(f"[esearch] window=last {days} days, retmax={retmax}", file=sys.stderr)
    data = http_get_json(url)
    pmids = data.get("esearchresult", {}).get("idlist", [])
    print(f"[esearch] got {len(pmids)} PMIDs", file=sys.stderr)
    return pmids


def efetch_metadata(pmids):
    """Return dict pmid -> metadata."""
    if not pmids:
        return {}
    url = NCBI + "/efetch.fcgi?" + urllib.parse.urlencode({
        "db": "pubmed",
        "id": ",".join(pmids),
        "retmode": "xml",
    })
    xml_bytes = http_get_bytes(url)
    return parse_pubmed_xml(xml_bytes)


def parse_pubmed_xml(xml_bytes):
    out = {}
    root = ET.fromstring(xml_bytes)
    for art in root.findall(".//PubmedArticle"):
        pmid_el = art.find(".//PMID")
        if pmid_el is None:
            continue
        pmid = pmid_el.text

        title_el = art.find(".//ArticleTitle")
        title = "".join(title_el.itertext()).strip() if title_el is not None else ""

        journal_el = art.find(".//Journal/Title")
        journal = (journal_el.text or "").strip() if journal_el is not None else ""

        year = ""
        for path in (".//ArticleDate/Year", ".//PubDate/Year", ".//PubDate/MedlineDate"):
            el = art.find(path)
            if el is not None and el.text:
                m = re.search(r"\b(20\d{2}|19\d{2})\b", el.text)
                if m:
                    year = m.group(1)
                    break

        doi = ""
        pmcid = ""
        for aid in art.findall(".//ArticleId"):
            it = (aid.get("IdType") or "").lower()
            if it == "doi":
                doi = (aid.text or "").strip()
            elif it == "pmc":
                pmcid = (aid.text or "").strip()

        authors = []
        for a in art.findall(".//Author"):
            ln = a.findtext("LastName", "")
            if ln:
                authors.append(ln)

        out[pmid] = {
            "pmid": pmid,
            "title": title,
            "journal": journal,
            "year": year,
            "doi": doi,
            "pmcid": pmcid,
            "authors": authors,
        }
    return out


def make_slug(meta):
    first = (meta["authors"][0] if meta.get("authors") else "unknown").lower()
    first = re.sub(r"[^a-z]", "", first) or "unknown"
    year = meta.get("year") or "ny"
    title = meta.get("title", "").lower()
    words = re.findall(r"[a-z]+", title)
    kw = [w for w in words if w not in SKIP_TITLE_WORDS and len(w) > 2][:6]
    slug = f"{first}-{year}-" + "-".join(kw)
    return slug[:120]


def known_pmids():
    pmids = set()
    for p in (REPO / "wiki/sources").glob("*.md"):
        try:
            head = p.read_text(encoding="utf-8")[:2000]
        except Exception:
            continue
        m = re.search(r'^pmid:\s*"?(\d+)"?', head, re.MULTILINE)
        if m:
            pmids.add(m.group(1))
    return pmids


def posted_pmids():
    f = REPO / "wiki/_meta/slack-posted.json"
    if not f.exists():
        return set()
    try:
        return set(str(x) for x in json.loads(f.read_text()).get("pmids", []))
    except Exception:
        return set()


def try_ezproxy(doi, out_path):
    """Fallback: invoke ezproxy_download.py functions."""
    cookies = REPO / ".cookies/oca.cookies.txt"
    if not cookies.exists():
        return False, "no cookies file"
    try:
        sys.path.insert(0, str(INGEST))
        from ezproxy_download import (
            load_cookies, make_opener, try_ezproxy_pdf,
        )
        cj = load_cookies(cookies)
        opener = make_opener(cj)
        ok, info = try_ezproxy_pdf(opener, doi, out_path)
        return ok, info
    except Exception as e:
        return False, f"ezproxy exc: {e}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--days", type=int, default=int(os.environ.get("DIGEST_DAYS", "7")),
                    help="Entrez date window in days (default 7)")
    ap.add_argument("--retmax", type=int, default=30,
                    help="Max PMIDs to fetch from esearch (default 30)")
    ap.add_argument("--max-candidates", type=int, default=8,
                    help="Cap on candidates with full text passed to LLM (default 8)")
    args = ap.parse_args()

    pdf_dir = REPO / "raw/inbox/papers"
    pdf_dir.mkdir(parents=True, exist_ok=True)

    pmids = esearch(DEFAULT_QUERY, args.days, args.retmax)

    known = known_pmids()
    posted = posted_pmids()
    print(f"[filter] wiki has {len(known)} PMIDs, posted log has {len(posted)}",
          file=sys.stderr)

    fresh = [p for p in pmids if p not in known and p not in posted]
    print(f"[filter] fresh PMIDs: {len(fresh)}", file=sys.stderr)

    if not fresh:
        json.dump({
            "date": datetime.date.today().isoformat(),
            "query": DEFAULT_QUERY,
            "days": args.days,
            "candidates": [],
            "note": "No new PMIDs in window after filtering.",
        }, sys.stdout, ensure_ascii=False, indent=2)
        return

    metas = efetch_metadata(fresh)
    print(f"[efetch] got metadata for {len(metas)} PMIDs", file=sys.stderr)

    candidates = []
    for pmid in fresh:
        if len(candidates) >= args.max_candidates:
            break
        m = metas.get(pmid)
        if not m or not m.get("doi"):
            print(f"  {pmid}: no DOI in metadata, skip", file=sys.stderr)
            continue

        slug = make_slug(m)
        first_last = re.sub(r"[^a-z]", "", (m["authors"][0] if m["authors"] else "").lower())
        ref = {
            "slug": slug,
            "title": m["title"],
            "year": m["year"],
            "first_author_last": first_last,
            "pmid": pmid,
            "doi": m["doi"],
            "pmcid": m["pmcid"],
        }

        out_path = pdf_dir / f"{slug}.pdf"
        print(f"  {pmid} ({slug[:50]}...): trying OA sources", file=sys.stderr)
        try:
            result = resolve_and_download(ref, pdf_dir)
        except Exception as e:
            result = {"downloaded": False, "tried": [], "exc": str(e)}

        via = None
        if result.get("downloaded") and out_path.exists() and out_path.stat().st_size > 5000:
            via = result.get("via", "oa")
        else:
            # ezproxy fallback
            print(f"    OA failed, trying ezproxy", file=sys.stderr)
            ok, info = try_ezproxy(m["doi"], out_path)
            if ok and out_path.exists() and out_path.stat().st_size > 5000:
                via = f"ezproxy: {info[:60]}"

        if not via:
            print(f"    no PDF obtained, skip", file=sys.stderr)
            continue

        # Extract text
        try:
            text = pdf_extract(out_path)
        except Exception as e:
            print(f"    extract err: {e}", file=sys.stderr)
            continue

        if len(text.strip()) < 1000:
            print(f"    extracted text too short ({len(text)} chars), skip", file=sys.stderr)
            continue

        candidates.append({
            "pmid": pmid,
            "slug": slug,
            "title": m["title"],
            "authors": m["authors"][:5],
            "year": m["year"],
            "journal": m["journal"],
            "doi": m["doi"],
            "pmcid": m["pmcid"],
            "pdf_path": str(out_path.relative_to(REPO)),
            "download_via": via,
            "full_text": text,
        })
        print(f"    OK ({len(text)} chars, via {via[:30]})", file=sys.stderr)

    json.dump({
        "date": datetime.date.today().isoformat(),
        "query": DEFAULT_QUERY,
        "days": args.days,
        "esearch_count": len(pmids),
        "after_filter": len(fresh),
        "candidates": candidates,
    }, sys.stdout, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    main()
