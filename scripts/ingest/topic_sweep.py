#!/usr/bin/env python3
"""Topic-specific PubMed sweep with journal allowlist + 90-day window + dedup.

Usage:
  python3 topic_sweep.py --topic bcell-neoantigen --days 90 --cap 30
  python3 topic_sweep.py --topic cancer-multiomics --days 90 --cap 30

For each topic, runs multiple esearch queries, fetches metadata, filters by:
  - last N days (Entrez date)
  - journal allowlist (high-impact + mid-tier)
  - not already in wiki/sources/ by PMID or slug
  - has DOI
Then downloads PDF (OA → EZproxy), extracts text (>1000 chars), emits JSON.
"""
import argparse
import datetime
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
INGEST = REPO / "scripts/ingest"
sys.path.insert(0, str(INGEST))

from resolve_pdf import resolve_and_download  # noqa: E402
from extract_pdf_text import extract as pdf_extract  # noqa: E402

NCBI = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"

# High-impact + mid-tier journal allowlist (case-insensitive substring match).
# Per user request 2026-05-24: include J Immunother Cancer, Clin Cancer Res, Mol Oncol etc.
JOURNAL_ALLOWLIST = [
    # Nature family
    "nature medicine", "nat med",
    "nature cancer", "nat cancer",
    "nature communications", "nat commun",
    "nature biotechnology", "nat biotechnol",
    "nature genetics", "nat genet",
    "nature methods", "nat methods",
    "nature cell biology", "nat cell biol",
    "nature reviews cancer", "nat rev cancer",
    "nature reviews clinical oncology", "nat rev clin oncol",
    "nature reviews drug discovery", "nat rev drug discov",
    "nature reviews molecular cell biology", "nat rev mol cell biol",
    "nature structural & molecular biology", "nat struct mol biol",
    "nature aging", "nat aging",
    "nature microbiology", "nat microbiol",
    "nature immunology", "nat immunol",
    "nature",  # parent journal — keep last to match after specific
    # Cell family
    "cancer cell",
    "molecular cell", "mol cell",
    "cell metabolism", "cell metab",
    "cell stem cell",
    "cell host & microbe", "cell host microbe",
    "cell reports medicine", "cell rep med",
    "cell genomics", "cell genom",
    "cell reports", "cell rep",
    "cell death and differentiation", "cell death differ",
    "cell research",
    "immunity",
    "cell",
    # Science family
    "science translational medicine", "sci transl med",
    "science advances", "sci adv",
    "science immunology", "sci immunol",
    "science signaling", "sci signal",
    "science",
    # Oncology specialty
    "cancer discovery",
    "cancer research", "cancer res",
    "clinical cancer research", "clin cancer res",
    "journal of clinical oncology", "j clin oncol",
    "jama oncology", "jama oncol",
    "lancet oncology", "lancet oncol",
    "new england journal of medicine", "n engl j med", "nejm",
    "annals of oncology", "ann oncol",
    "jnci", "journal of the national cancer institute",
    "cancer immunology research", "cancer immunol res",
    "molecular cancer", "mol cancer",
    "molecular cancer therapeutics", "mol cancer ther",
    "molecular oncology", "mol oncol",
    "british journal of cancer", "br j cancer",
    "oncogene",
    "esmo open",
    "cancer letters", "cancer lett",
    "journal of thoracic oncology", "j thorac oncol",
    "jto clinical and research reports", "jto clin res rep",
    "journal for immunotherapy of cancer", "j immunother cancer", "jitc",
    "signal transduction and targeted therapy",
    "lancet",
    # Hematology
    "blood",
    "leukemia",
    "blood cancer journal", "blood cancer j",
    "haematologica",
    # Proteomics
    "molecular & cellular proteomics", "mol cell proteomics", "mcp",
    "journal of proteome research", "j proteome res",
    # General high quality
    "genome biology", "genome biol",
    "genome medicine", "genome med",
    "elife",
    "embo journal", "embo j",
    "embo molecular medicine", "embo mol med",
    "embo reports", "embo rep",
    "molecular systems biology", "mol syst biol",
    "advanced science", "adv sci",
    "gut",
    "gastroenterology",
    "hepatology",
    "jhep reports", "jhep rep",
    "journal of hepatology", "j hepatol",
    "clinical and translational medicine", "clin transl med",
    "european journal of cancer", "eur j cancer",
    "journal of clinical investigation", "j clin invest",
]


TOPIC_QUERIES = {
    "bcell-neoantigen": [
        # Neoantigen × cancer × human
        '((neoantigen*[All] OR neoepitope*[All] OR immunopeptidom*[All]) '
        'AND (cancer[MeSH Terms] OR neoplasm*[MeSH Terms] OR tumor*[Title/Abstract]) '
        'AND humans[Filter] AND English[lang])',
        # TLS / tumor-infiltrating B cells
        '(("tertiary lymphoid structure"[All] OR "tertiary lymphoid structures"[All] '
        'OR "tumor-infiltrating B"[Title/Abstract] OR "tumor infiltrating B cell"[Title/Abstract] '
        'OR "intratumoral B cell"[Title/Abstract] OR "intratumoural B cell"[Title/Abstract]) '
        'AND (cancer[MeSH Terms] OR tumor*[Title/Abstract] OR tumour*[Title/Abstract]) '
        'AND humans[Filter] AND English[lang])',
        # Cryptic / non-canonical antigens
        '((cryptic peptide*[All] OR "non-canonical"[Title] OR noncanonical[Title] '
        'OR "noncoding ORF"[All] OR "alternative ORF"[All]) '
        'AND (immunopeptidom*[All] OR proteogenom*[All] OR HLA[All] OR MHC[All] OR neoantigen*[All]) '
        'AND cancer[MeSH Terms] AND humans[Filter])',
        # Personalized vaccine / TCR-T
        '(("neoantigen vaccine"[All] OR "personalized cancer vaccine"[All] '
        'OR "personalised cancer vaccine"[All] OR "TCR-T"[All] '
        'OR "neoantigen-specific T cell"[Title/Abstract] OR "antigen-specific T cell receptor"[Title/Abstract]) '
        'AND cancer[MeSH Terms] AND humans[Filter] AND English[lang])',
        # Antibody response in cancer
        '(("antibody response"[Title/Abstract] OR "B cell response"[Title/Abstract] '
        'OR "humoral immunity"[Title/Abstract] OR "tumor reactive antibody"[Title/Abstract]) '
        'AND (cancer[MeSH Terms] OR tumor*[Title/Abstract]) '
        'AND humans[Filter] AND English[lang])',
    ],
    "cancer-multiomics": [
        # Phospho/proteogenomic × drug response / molecular subtype (from fetch_new_papers DEFAULT_QUERY)
        '(((phosphoproteomic*[All] OR proteogenomic*[All] OR ppQTL[All] OR pQTL[All]) '
        'AND (drug response[All] OR drug resistance[All] OR chemoresistance[All] '
        'OR treatment response[All] OR therapy resistance[All] '
        'OR targeted therapy[All] OR immunotherapy[MeSH] OR kinase inhibitor[All] '
        'OR neoantigen*[All] OR pan-cancer[All] OR "pan cancer"[All] '
        'OR molecular subtyp*[All] OR proteogenomic subtyp*[All] '
        'OR molecular stratification[All] OR molecular taxonomy[All] '
        'OR molecular landscape[All] OR molecular characteriz*[All] '
        'OR proteogenomic characteriz*[All] OR proteogenomic landscape[All] '
        'OR tumor agnostic[All] OR therapeutic vulnerabilit*[All] OR precision oncology[All]) '
        'AND (cancer[MeSH Terms] OR neoplasm*[MeSH Terms] OR tumor*[All]) '
        'AND humans[Filter] AND English[lang])',
        # CPTAC / large-scale multiomic
        '(("CPTAC"[All] OR "ICGC-ARGO"[All] OR "pan-cancer multi-omic"[All] '
        'OR "pan-cancer proteogenomic"[All]) AND humans[Filter])',
        # Spatial multi-omics in cancer
        '(("spatial proteomic*"[Title/Abstract] OR "spatial multi-omic*"[Title/Abstract] '
        'OR "spatial transcriptomic*"[Title]) '
        'AND cancer[MeSH Terms] AND humans[Filter])',
        # Multi-omic kinase signaling / kinase inhibitor response
        '((kinase[Title] AND (signaling[Title] OR network[Title] OR inference[Title] OR activity[Title])) '
        'AND (cancer OR tumor) AND (phosphoproteom* OR proteome OR multi-omic) AND humans[Filter])',
        # Acquired/primary resistance × multi-omic
        '(("acquired resistance"[Title/Abstract] OR "primary resistance"[Title/Abstract] '
        'OR "resistance mechanism"[Title/Abstract]) '
        'AND (multi-omic*[All] OR proteogenom*[All] OR phosphoproteom*[All]) '
        'AND cancer[MeSH Terms] AND humans[Filter])',
    ],
}


SKIP_TITLE_WORDS = {
    "a", "an", "the", "of", "in", "on", "and", "for", "to", "by", "with",
    "from", "as", "via", "is", "are", "be", "at", "or", "into", "novel",
    "new", "human", "study", "based", "using", "between", "this", "that",
}

# Preclinical-only filter — skip if mouse/xenograft only and no human signal
EXCLUDE_PRECLINICAL_RE = re.compile(
    r"\b(xenograft|pdx|murine|mouse|mice|zebrafish|drosophila|in vitro only)\b",
    re.IGNORECASE,
)
INCLUDE_HUMAN_RE = re.compile(
    r"\b(human|clinical|patient|cohort|biopsy|trial|phase [0-9I]|specimen|resection)\b",
    re.IGNORECASE,
)


def http_get(url, timeout=60):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def normalize_journal(j: str) -> str:
    j = j.lower()
    j = re.sub(r"\s*\([^)]*\)\s*", " ", j)   # strip "(New York, N.Y.)" etc.
    j = re.sub(r"[.,;:]", " ", j)              # strip punctuation
    j = re.sub(r"^the\s+", "", j)              # strip leading "The "
    j = re.sub(r"\s+", " ", j).strip()
    return j


def journal_passes(journal: str) -> bool:
    """Match allowlist with startswith + word boundary; single-word entries require exact match.

    This prevents 'cell' from matching 'cell cycle' or 'international journal of biological sciences'
    from matching the bare 'science' entry.
    """
    if not journal:
        return False
    n = normalize_journal(journal)
    for allowed in JOURNAL_ALLOWLIST:
        # Single-word allowlist entries (Nature, Cell, Science, Lancet, Blood, Gut, ...)
        # require an exact match on the normalized journal name.
        if " " not in allowed:
            if n == allowed:
                return True
        else:
            if n == allowed or n.startswith(allowed + " "):
                return True
    return False


def esearch(query, days, retmax=200):
    full = f"{query} AND (\"last {days} days\"[EDat])"
    url = NCBI + "/esearch.fcgi?" + urllib.parse.urlencode({
        "db": "pubmed", "term": full, "retmax": retmax,
        "retmode": "json", "sort": "date",
    })
    try:
        data = json.loads(http_get(url))
        return data.get("esearchresult", {}).get("idlist", [])
    except Exception as e:
        print(f"[esearch err] {e}", file=sys.stderr)
        return []


def efetch_metadata(pmids, chunk=100):
    out = {}
    if not pmids:
        return out
    for i in range(0, len(pmids), chunk):
        ids = pmids[i:i + chunk]
        url = NCBI + "/efetch.fcgi?" + urllib.parse.urlencode({
            "db": "pubmed", "id": ",".join(ids), "retmode": "xml",
        })
        try:
            xml = http_get(url, timeout=120)
        except Exception as e:
            print(f"[efetch err] {e}", file=sys.stderr)
            continue
        out.update(parse_pubmed_xml(xml))
        time.sleep(0.3)
    return out


def parse_pubmed_xml(xml_bytes):
    out = {}
    root = ET.fromstring(xml_bytes)
    for art in root.findall(".//PubmedArticle"):
        pid = art.find(".//PMID")
        if pid is None:
            continue
        pmid = pid.text
        t = art.find(".//ArticleTitle")
        title = "".join(t.itertext()).strip() if t is not None else ""
        jrn = art.find(".//Journal/Title")
        journal = (jrn.text or "").strip() if jrn is not None else ""
        year = ""
        for path in (".//ArticleDate/Year", ".//PubDate/Year", ".//PubDate/MedlineDate"):
            el = art.find(path)
            if el is not None and el.text:
                m = re.search(r"\b(20\d{2})\b", el.text)
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
        abst_parts = []
        for ab in art.findall(".//Abstract/AbstractText"):
            lab = ab.attrib.get("Label")
            txt = "".join(ab.itertext())
            abst_parts.append(f"**{lab}**: {txt}" if lab else txt)
        out[pmid] = {
            "pmid": pmid, "title": title, "journal": journal, "year": year,
            "doi": doi, "pmcid": pmcid, "authors": authors,
            "abstract": "\n\n".join(abst_parts).strip(),
        }
    return out


def make_slug(meta):
    first = (meta["authors"][0] if meta.get("authors") else "unknown").lower()
    first = re.sub(r"[^a-z]", "", first) or "unknown"
    year = meta.get("year") or "ny"
    title = (meta.get("title") or "").lower()
    words = re.findall(r"[a-z]+", title)
    kw = [w for w in words if w not in SKIP_TITLE_WORDS and len(w) > 2][:6]
    slug = f"{first}-{year}-" + "-".join(kw)
    return slug[:120]


def known_pmids_and_slugs():
    pmids = set()
    slugs = set()
    for p in (REPO / "wiki/sources").glob("*.md"):
        slugs.add(p.stem)
        try:
            head = p.read_text(encoding="utf-8")[:3000]
        except Exception:
            continue
        m = re.search(r'^pmid:\s*"?(\d+)"?', head, re.MULTILINE)
        if m:
            pmids.add(m.group(1))
    # Also dedup against raw/inbox/papers/ slugs (in case PDF exists but no source page yet)
    for p in (REPO / "raw/inbox/papers").glob("*.pdf"):
        slugs.add(p.stem)
    return pmids, slugs


def posted_pmids():
    f = REPO / "wiki/_meta/slack-posted.json"
    if not f.exists():
        return set()
    try:
        return set(str(x) for x in json.loads(f.read_text()).get("pmids", []))
    except Exception:
        return set()


def is_preclinical_only(meta):
    text = (meta.get("title", "") + " " + meta.get("abstract", "")).lower()
    if EXCLUDE_PRECLINICAL_RE.search(text) and not INCLUDE_HUMAN_RE.search(text):
        return True
    return False


def try_ezproxy(doi, out_path):
    cookies = REPO / ".cookies/oca.cookies.txt"
    if not cookies.exists():
        return False, "no cookies"
    try:
        sys.path.insert(0, str(INGEST))
        from ezproxy_download import load_cookies, make_opener, try_ezproxy_pdf
        cj = load_cookies(cookies)
        opener = make_opener(cj)
        return try_ezproxy_pdf(opener, doi, out_path)
    except Exception as e:
        return False, f"ezproxy exc: {e}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--topic", required=True, choices=list(TOPIC_QUERIES.keys()))
    ap.add_argument("--days", type=int, default=90)
    ap.add_argument("--retmax", type=int, default=200,
                    help="PubMed esearch retmax per query")
    ap.add_argument("--cap", type=int, default=30,
                    help="Max candidates with successful PDF + text to emit")
    ap.add_argument("--scan-cap", type=int, default=120,
                    help="Max candidates to try downloading before stopping")
    ap.add_argument("--out", default=None,
                    help="Output JSON path (default /tmp/wiki_work/<topic>_sweep.json)")
    ap.add_argument("--dry-run", action="store_true",
                    help="Skip PDF download; emit metadata-only JSON for review.")
    args = ap.parse_args()

    out_path = Path(args.out or f"/tmp/wiki_work/{args.topic}_sweep.json")
    out_path.parent.mkdir(parents=True, exist_ok=True)

    print(f"[topic_sweep] topic={args.topic} days={args.days} cap={args.cap}",
          file=sys.stderr)

    # Phase 1: collect PMIDs from all topic queries
    seen = set()
    for q in TOPIC_QUERIES[args.topic]:
        ids = esearch(q, args.days, args.retmax)
        print(f"  query → {len(ids)} PMIDs", file=sys.stderr)
        for x in ids:
            seen.add(x)
        time.sleep(0.4)
    pmids = list(seen)
    print(f"[total unique PMIDs] {len(pmids)}", file=sys.stderr)

    # Phase 2: efetch metadata
    metas = efetch_metadata(pmids)
    print(f"[metadata fetched] {len(metas)}", file=sys.stderr)

    # Phase 3: filter
    known_p, known_s = known_pmids_and_slugs()
    posted = posted_pmids()
    print(f"[filter] known PMIDs={len(known_p)} known slugs={len(known_s)} posted={len(posted)}",
          file=sys.stderr)

    accepted_meta = []
    reasons = {"no_doi": 0, "journal_fail": 0, "duplicate_pmid": 0,
               "duplicate_slug": 0, "preclinical": 0}
    for pmid in pmids:
        m = metas.get(pmid)
        if not m:
            continue
        if not m.get("doi"):
            reasons["no_doi"] += 1
            continue
        if pmid in known_p or pmid in posted:
            reasons["duplicate_pmid"] += 1
            continue
        if not journal_passes(m.get("journal", "")):
            reasons["journal_fail"] += 1
            continue
        slug = make_slug(m)
        if slug in known_s:
            reasons["duplicate_slug"] += 1
            continue
        if is_preclinical_only(m):
            reasons["preclinical"] += 1
            continue
        m["slug"] = slug
        accepted_meta.append(m)

    print(f"[filter accepted] {len(accepted_meta)} of {len(metas)}", file=sys.stderr)
    for k, v in reasons.items():
        print(f"  rejected {k}: {v}", file=sys.stderr)

    if args.dry_run:
        out = {
            "topic": args.topic,
            "date": datetime.date.today().isoformat(),
            "days": args.days,
            "total_pmids": len(pmids),
            "metadata_fetched": len(metas),
            "filter_reasons": reasons,
            "accepted_metadata_only": [
                {k: v for k, v in m.items() if k != "abstract"} | {"abstract_len": len(m.get("abstract", ""))}
                for m in accepted_meta
            ],
        }
        out_path.write_text(json.dumps(out, ensure_ascii=False, indent=2))
        print(f"[dry-run] wrote metadata to {out_path}", file=sys.stderr)
        return

    # Phase 4: download PDFs, extract text, cap at args.cap successful
    pdf_dir = REPO / "raw/inbox/papers"
    pdf_dir.mkdir(parents=True, exist_ok=True)

    candidates = []
    tried = 0
    for m in accepted_meta:
        if len(candidates) >= args.cap:
            break
        if tried >= args.scan_cap:
            print(f"[scan-cap reached at {tried}]", file=sys.stderr)
            break
        tried += 1
        slug = m["slug"]
        pmid = m["pmid"]
        doi = m["doi"]
        out_pdf = pdf_dir / f"{slug}.pdf"

        first_last = re.sub(r"[^a-z]", "", (m["authors"][0] if m["authors"] else "").lower())
        ref = {
            "slug": slug, "title": m["title"], "year": m["year"],
            "first_author_last": first_last, "pmid": pmid, "doi": doi,
            "pmcid": m.get("pmcid", ""),
        }

        print(f"  [{tried}/{args.scan_cap}] {pmid} ({slug[:60]})", file=sys.stderr)
        try:
            result = resolve_and_download(ref, pdf_dir)
        except Exception as e:
            result = {"downloaded": False, "exc": str(e)}

        via = None
        if result.get("downloaded") and out_pdf.exists() and out_pdf.stat().st_size > 5000:
            via = result.get("via", "oa")
        else:
            ok, info = try_ezproxy(doi, out_pdf)
            if ok and out_pdf.exists() and out_pdf.stat().st_size > 5000:
                via = f"ezproxy: {(info or '')[:60]}"

        if not via:
            print(f"    no PDF (tried OA + ezproxy)", file=sys.stderr)
            continue

        try:
            text = pdf_extract(out_pdf)
        except Exception as e:
            print(f"    extract err: {e}", file=sys.stderr)
            continue

        if len(text.strip()) < 1000:
            print(f"    text too short ({len(text)})", file=sys.stderr)
            continue

        candidates.append({
            "pmid": pmid, "slug": slug, "title": m["title"],
            "authors": m["authors"][:5], "year": m["year"], "journal": m["journal"],
            "doi": doi, "pmcid": m.get("pmcid", ""),
            "pdf_path": str(out_pdf.relative_to(REPO)),
            "download_via": via,
            "abstract": m.get("abstract", ""),
            "full_text": text,
        })
        print(f"    OK ({len(text)} chars via {via[:30]})", file=sys.stderr)

    out = {
        "topic": args.topic,
        "date": datetime.date.today().isoformat(),
        "days": args.days,
        "tried": tried,
        "successful": len(candidates),
        "candidates": candidates,
    }
    out_path.write_text(json.dumps(out, ensure_ascii=False, indent=2))
    print(f"[done] {len(candidates)} candidates → {out_path}", file=sys.stderr)


if __name__ == "__main__":
    main()
