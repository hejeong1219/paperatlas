#!/usr/bin/env python3
"""End-to-end ingest of an expansion candidate set.

Reads /tmp/wiki_work/{topic}_expansion.json, picks top N by relevance score,
generates source pages, downloads PDFs in parallel, and updates anchor + topic.
"""
import argparse
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from resolve_pdf import resolve_and_download  # noqa
from generate_source_pages import build_page  # noqa


HIGH_IMPACT_JOURNALS = {
    # tier 1 (top biomedical/oncology)
    "nature": 5, "science": 5, "cell": 5, "lancet": 5, "lancet oncology": 5,
    "new england journal of medicine": 5, "n engl j med": 5,
    "nature medicine": 5, "nature cancer": 5, "cancer cell": 5,
    "cancer discovery": 5, "nature reviews cancer": 5,
    # tier 2 (high-impact specialty)
    "nature communications": 4, "nat commun": 4,
    "cell reports": 4, "cell reports medicine": 4,
    "cell metabolism": 4, "molecular cell": 4, "immunity": 4,
    "journal of clinical oncology": 4, "j clin oncol": 4,
    "annals of oncology": 4, "ann oncol": 4,
    "clinical cancer research": 4, "clin cancer res": 4,
    "jama oncology": 4, "jama": 4,
    "blood": 4, "leukemia": 4, "gastroenterology": 4, "gut": 4,
    "hepatology": 4, "circulation": 4, "european urology": 4,
    "european journal of cancer": 4, "eur j cancer": 4,
    "nature biotechnology": 4, "nat biotechnol": 4,
    "nature genetics": 4, "nat genet": 4,
    "molecular cancer": 4, "mol cancer": 4,
    "signal transduction and targeted therapy": 4,
    "journal for immunotherapy of cancer": 4,
    "science translational medicine": 4, "sci transl med": 4,
    # tier 3 (good journals)
    "cancer research": 3, "cancer res": 3,
    "molecular & cellular proteomics": 3, "mol cell proteomics": 3,
    "elife": 3, "embo journal": 3, "embo j": 3,
    "embo molecular medicine": 3,
    "journal of clinical investigation": 3, "j clin invest": 3,
    "nucleic acids research": 3, "nucleic acids res": 3,
    "bioinformatics": 3, "genome biology": 3, "genome biol": 3,
    "genome research": 3, "genome res": 3,
    "british journal of cancer": 3, "br j cancer": 3,
    "oncogene": 3, "oncotarget": 2,
    "trends in cancer": 3, "trends in immunology": 3,
    "trends in molecular medicine": 3, "trends in genetics": 3,
    "current opinion in immunology": 3, "current opinion in genetics": 3,
    "annual review of cancer biology": 3, "annual review of immunology": 3,
}

EXCLUDE_JOURNALS_CONTAINS = ["mdpi", "scientific reports", "scientific report",
                              "plos one", "iscience", "cancers (basel)",
                              "biomedicines", "international journal of molecular sciences"]


def journal_score(journal):
    if not journal: return 0
    j = journal.lower().strip()
    for ex in EXCLUDE_JOURNALS_CONTAINS:
        if ex in j: return -1
    return HIGH_IMPACT_JOURNALS.get(j, 1)


def relevance_score(meta):
    j_score = journal_score(meta.get("journal") or "")
    if j_score < 0: return -1
    try:
        year = int(meta.get("year") or 0)
    except Exception:
        year = 0
    year_score = max(0, year - 2014)  # 2015 -> 1, 2026 -> 12
    return j_score * 10 + year_score


def already_ingested_slugs(out_dir):
    return {p.stem for p in out_dir.glob("*.md") if p.stem != "index"}


def select_top_n(candidates, n, exclude_slugs):
    scored = []
    for c in candidates:
        if c["slug"] in exclude_slugs:
            continue
        s = relevance_score(c)
        if s < 0: continue
        scored.append((s, c))
    scored.sort(key=lambda x: -x[0])
    return [c for _, c in scored[:n]]


def to_ref_struct(meta):
    """Convert meta dict (from expansion) to the same struct used by generate_source_pages."""
    title = meta.get("title", "")
    year = meta.get("year", "")
    authors = meta.get("authors") or []
    first = authors[0] if authors else "unknown"
    return {
        "slug": meta["slug"],
        "title": title,
        "year": year,
        "first_author_last": re.sub(r"[^a-z]", "", first.lower()),
        "authors_raw": ", ".join(authors[:5]),
        "journal": meta.get("journal", ""),
        "rest": "",
        "block": "",
        "pmid": meta.get("pmid"),
        "doi": meta.get("doi"),
        "pmcid": meta.get("pmcid"),
        "meta": meta,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--topic", required=True, choices=["bcell-neoantigen", "ptmanchor", "resistance"])
    ap.add_argument("--input", default=None, help="alternate expansion JSON path; defaults to /tmp/wiki_work/{topic}_expansion.json")
    ap.add_argument("--target", type=int, default=150)
    ap.add_argument("--current", type=int, required=True, help="current source count for topic")
    ap.add_argument("--workers", type=int, default=8)
    args = ap.parse_args()

    exp_path = Path(args.input) if args.input else Path(f"/tmp/wiki_work/{args.topic}_expansion.json")
    candidates = json.loads(exp_path.read_text())["accepted"]
    out_dir = Path("wiki/sources")
    pdf_dir = Path("raw/inbox/papers")
    pdf_dir.mkdir(parents=True, exist_ok=True)

    needed = max(0, args.target - args.current)
    print(f"Topic={args.topic} target={args.target} current={args.current} needed={needed}", file=sys.stderr)

    existing_slugs_set = already_ingested_slugs(out_dir)
    selected = select_top_n(candidates, needed + 50, existing_slugs_set)
    print(f"Selected {len(selected)} top-scored candidates", file=sys.stderr)

    # Generate skeleton pages
    new_pages = []
    for meta in selected:
        ref = to_ref_struct(meta)
        page = out_dir / f"{ref['slug']}.md"
        if page.exists(): continue
        has_pdf = (pdf_dir / f"{ref['slug']}.pdf").exists() and (pdf_dir / f"{ref['slug']}.pdf").stat().st_size > 5000
        page.write_text(build_page(ref, args.topic, pdf_dir, has_pdf))
        new_pages.append(ref)
    print(f"Generated {len(new_pages)} new source pages", file=sys.stderr)

    # Download PDFs in parallel
    def _resolve(ref):
        try:
            return resolve_and_download(ref, pdf_dir)
        except Exception as e:
            return {"slug": ref["slug"], "downloaded": False, "tried": [], "via": None, "exc": str(e)}

    ok_count = 0
    if new_pages:
        with ThreadPoolExecutor(max_workers=args.workers) as ex:
            futures = {ex.submit(_resolve, r): r for r in new_pages}
            for i, fut in enumerate(as_completed(futures)):
                res = fut.result()
                if res.get("downloaded"): ok_count += 1
                if i % 10 == 0:
                    print(f"  [{i+1}/{len(new_pages)}] ok={ok_count}", file=sys.stderr)
    print(f"Downloaded {ok_count}/{len(new_pages)} PDFs", file=sys.stderr)

    # Update has_pdf in any new page that just got downloaded
    for ref in new_pages:
        page = out_dir / f"{ref['slug']}.md"
        pdf = pdf_dir / f"{ref['slug']}.pdf"
        if pdf.exists() and pdf.stat().st_size > 5000:
            text = page.read_text()
            if "pdf_status: pending" in text:
                text = text.replace("pdf_status: pending",
                                    f'pdf: "raw/inbox/papers/{ref["slug"]}.pdf"')
                page.write_text(text)


if __name__ == "__main__":
    main()
