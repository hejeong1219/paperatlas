#!/usr/bin/env python3
"""Discover related papers for a list of seed DOIs via OpenAlex.

Pipeline:
  1. For each seed DOI, fetch the OpenAlex Work record.
  2. Collect both `referenced_works` (papers it cites) and `related_works`
     (OpenAlex's similarity neighbors).
  3. Resolve each candidate's metadata (title, authors, year, doi, abstract,
     concepts, primary_topic).
  4. Score candidates: in-degree across seeds + cancer/multiomics keyword hit.
  5. Dedup against existing wiki/sources/ (filename glob `<lastname>-<year>-*.md`).
  6. Output a ranked JSON queue + a Markdown review report.

OpenAlex API: free, no key required. Use `mailto=` for the polite pool
(higher rate limits, ~100k/day).

Usage:
  python scripts/ingest/find_related_via_openalex.py \\
      --seed-json /tmp/wiki_work/cancer_multiomics_seed.json \\
      --out-json /tmp/wiki_work/openalex_related.json \\
      --out-report /tmp/wiki_work/openalex_related_report.md \\
      --max-related-per-seed 25 \\
      --max-referenced-per-seed 60
"""
import argparse
import json
import re
import sys
import time
import urllib.parse
import urllib.request
from collections import defaultdict
from pathlib import Path

UA = "llm-wiki-cancer-multiomics-ingest/1.0"
MAILTO = "omics259259@gmail.com"
OA_BASE = "https://api.openalex.org"

# Cancer/multiomics relevance keywords. Hit any → relevant=True.
CANCER_KEYWORDS = [
    "cancer", "tumor", "tumour", "tumoral", "oncology", "oncologic",
    "neoplasm", "carcinoma", "sarcoma", "leukemia", "leukaemia", "lymphoma",
    "melanoma", "glioma", "glioblastoma", "metastasis", "metastatic",
    "malignant", "malignancy", "hepatocellular", "pancreatic", "colorectal",
    "lung adenocarcinoma", "breast cancer", "prostate", "ovarian",
    "renal cell carcinoma", "ccrcc", "hcc", "pdac", "luad", "lusc",
    "neoantigen", "immunopeptidomics", "checkpoint", "immunotherapy",
    "tumor microenvironment", "tme", "tertiary lymphoid", "tls",
]
MULTIOMICS_KEYWORDS = [
    "proteogenomic", "proteogenomics", "multi-omic", "multiomic",
    "multi-modal", "multimodal", "phosphoproteom", "acetylom",
    "ubiquitylom", "glycoprotein", "spatial transcriptom",
    "spatial multiomic", "spatial proteom", "single-cell",
    "scrna", "scatac", "cite-seq", "pathology", "histology",
    "immunopeptidom", "ms-based proteom", "tmt", "dia-ms",
    "phospho-tmt", "ptm", "post-translational",
]


def http_get_json(url, timeout=30, retries=3):
    last_err = None
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return json.loads(r.read().decode("utf-8", errors="ignore"))
        except Exception as e:
            last_err = e
            time.sleep(0.5 * (attempt + 1))
    raise RuntimeError(f"HTTP failed after {retries} retries: {url[:80]} :: {last_err}")


def add_mailto(url):
    sep = "&" if "?" in url else "?"
    return f"{url}{sep}mailto={urllib.parse.quote(MAILTO)}"


def normalize_doi(doi):
    if not doi:
        return None
    d = doi.strip().lower()
    d = d.replace("https://doi.org/", "").replace("http://doi.org/", "").replace("doi:", "")
    d = d.strip().rstrip("/.")
    return d if d.startswith("10.") else None


def fetch_work_by_doi(doi):
    nd = normalize_doi(doi)
    if not nd:
        return None
    url = add_mailto(f"{OA_BASE}/works/doi:{urllib.parse.quote(nd, safe='/')}")
    try:
        return http_get_json(url)
    except Exception as e:
        print(f"  WARN  {nd[:60]}  {e}", file=sys.stderr)
        return None


def fetch_works_by_ids(oa_ids, batch=25):
    """Fetch up to N OpenAlex works by ID using the filter endpoint."""
    out = {}
    short_ids = [i.replace("https://openalex.org/", "") for i in oa_ids]
    for i in range(0, len(short_ids), batch):
        chunk = short_ids[i:i+batch]
        flt = "openalex_id:" + "|".join(chunk)
        url = add_mailto(f"{OA_BASE}/works?filter={urllib.parse.quote(flt)}&per-page={batch}&select=id,doi,title,publication_year,authorships,primary_location,abstract_inverted_index,concepts,primary_topic,cited_by_count")
        try:
            r = http_get_json(url)
            for w in r.get("results", []):
                out[w.get("id")] = w
        except Exception as e:
            print(f"  WARN batch {i}-{i+batch}: {e}", file=sys.stderr)
        time.sleep(0.1)
    return out


def reconstruct_abstract(inverted_index):
    if not inverted_index:
        return ""
    pos = []
    for word, idxs in inverted_index.items():
        for ix in idxs:
            pos.append((ix, word))
    pos.sort()
    return " ".join(w for _, w in pos)[:1500]


def is_cancer_multiomics_relevant(work):
    blob = " ".join([
        (work.get("title") or "").lower(),
        reconstruct_abstract(work.get("abstract_inverted_index")).lower(),
        " ".join((c.get("display_name") or "").lower() for c in (work.get("concepts") or [])),
        ((work.get("primary_topic") or {}).get("display_name") or "").lower(),
        ((work.get("primary_topic") or {}).get("subfield") or {}).get("display_name", "").lower() if isinstance(work.get("primary_topic"), dict) else "",
    ])
    has_cancer = any(k in blob for k in CANCER_KEYWORDS)
    has_omics = any(k in blob for k in MULTIOMICS_KEYWORDS)
    return has_cancer or has_omics, has_cancer, has_omics


def author_lastname(authorships):
    if not authorships:
        return None
    a0 = authorships[0]
    name = (a0.get("author") or {}).get("display_name") or ""
    if not name:
        return None
    return name.split()[-1].lower().replace("'", "").replace("-", "")


def slug_for(work):
    last = author_lastname(work.get("authorships"))
    yr = work.get("publication_year")
    title = (work.get("title") or "").lower()
    title = re.sub(r"[^a-z0-9 ]+", " ", title)
    parts = [w for w in title.split() if len(w) > 2 and w not in {
        "the", "and", "for", "with", "from", "into", "onto", "this", "that",
        "are", "was", "were", "but", "not", "via",
    }]
    five = "-".join(parts[:5])
    if not last or not yr or not five:
        return None
    return f"{last}-{yr}-{five}"


def build_existing_index(sources_dir):
    """Build (lastname, year) → list of slugs map for fast dedup."""
    idx = defaultdict(list)
    for f in Path(sources_dir).glob("*.md"):
        m = re.match(r"^([a-z][a-z0-9]+)-(\d{4})-", f.stem)
        if m:
            idx[(m.group(1), int(m.group(2)))].append(f.stem)
    return idx


def is_in_wiki(work, existing_idx):
    last = author_lastname(work.get("authorships"))
    yr = work.get("publication_year")
    if not last or not yr:
        return False, None
    cands = existing_idx.get((last, yr), [])
    if not cands:
        return False, None
    title_blob = (work.get("title") or "").lower()
    title_words = set(re.findall(r"[a-z]{4,}", title_blob))
    for c in cands:
        slug_words = set(re.findall(r"[a-z]{4,}", c))
        overlap = len(title_words & slug_words)
        if overlap >= 3:
            return True, c
    return (len(cands) > 0), cands[0] if cands else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--seed-json", required=True, help="Path to cancer_multiomics_seed.json")
    ap.add_argument("--out-json", required=True)
    ap.add_argument("--out-report", required=True)
    ap.add_argument("--max-related-per-seed", type=int, default=25)
    ap.add_argument("--max-referenced-per-seed", type=int, default=60)
    ap.add_argument("--top-n", type=int, default=80, help="Top-N candidates to include in report")
    args = ap.parse_args()

    seed = json.loads(Path(args.seed_json).read_text())
    seed_dois = []
    for s in seed:
        d = s.get("doi")
        if d and isinstance(d, str) and d.startswith("10."):
            seed_dois.append((d, s.get("slug_candidate"), s.get("title_full")))
    print(f"Seed DOIs (Crossref-format): {len(seed_dois)} / {len(seed)} total seeds", file=sys.stderr)

    existing_idx = build_existing_index("wiki/sources")
    print(f"Existing wiki sources indexed: {sum(len(v) for v in existing_idx.values())}", file=sys.stderr)

    # 1. Fetch each seed work
    seed_works = {}  # doi -> work
    for d, slug, title in seed_dois:
        w = fetch_work_by_doi(d)
        if w:
            seed_works[d] = w
            print(f"  seed OK   {d[:55]}  cited_by={w.get('cited_by_count')} "
                  f"refs={len(w.get('referenced_works') or [])} related={len(w.get('related_works') or [])}",
                  file=sys.stderr)
        else:
            print(f"  seed MISS {d[:55]}", file=sys.stderr)
        time.sleep(0.15)

    # 2. Collect candidate IDs with provenance (which seeds reference/relate to them)
    cand_provenance = defaultdict(lambda: {"referenced_by": [], "related_to": []})
    for d, w in seed_works.items():
        seed_slug = next((s for dd, s, t in seed_dois if dd == d), d)
        for ref in (w.get("referenced_works") or [])[:args.max_referenced_per_seed]:
            cand_provenance[ref]["referenced_by"].append(seed_slug)
        for rel in (w.get("related_works") or [])[:args.max_related_per_seed]:
            cand_provenance[rel]["related_to"].append(seed_slug)
    print(f"Unique candidate OpenAlex IDs: {len(cand_provenance)}", file=sys.stderr)

    # 3. Fetch metadata for all candidate IDs (also exclude seed works themselves)
    seed_oa_ids = {w.get("id") for w in seed_works.values() if w.get("id")}
    candidate_ids = [cid for cid in cand_provenance.keys() if cid not in seed_oa_ids]
    print(f"Fetching metadata for {len(candidate_ids)} candidates...", file=sys.stderr)
    cand_meta = fetch_works_by_ids(candidate_ids)
    print(f"Resolved {len(cand_meta)} / {len(candidate_ids)} candidate works", file=sys.stderr)

    # 4. Filter + score
    scored = []
    for oa_id, work in cand_meta.items():
        prov = cand_provenance[oa_id]
        relevant, has_cancer, has_omics = is_cancer_multiomics_relevant(work)
        if not relevant:
            continue
        in_wiki, existing_slug = is_in_wiki(work, existing_idx)
        if in_wiki:
            continue
        # score: weighted by cross-seed support + cancer+omics + cited_by
        score = (
            2 * len(set(prov["referenced_by"])) +
            1 * len(set(prov["related_to"])) +
            (3 if has_cancer and has_omics else 0) +
            (1 if has_cancer else 0) +
            (1 if has_omics else 0) +
            min(5, (work.get("cited_by_count") or 0) // 50)
        )
        doi_short = (work.get("doi") or "").replace("https://doi.org/", "")
        scored.append({
            "openalex_id": oa_id,
            "doi": doi_short,
            "title": work.get("title"),
            "year": work.get("publication_year"),
            "first_author_last": author_lastname(work.get("authorships")),
            "slug_candidate": slug_for(work),
            "journal": ((work.get("primary_location") or {}).get("source") or {}).get("display_name"),
            "cited_by_count": work.get("cited_by_count"),
            "primary_topic": ((work.get("primary_topic") or {}).get("display_name")) if work.get("primary_topic") else None,
            "concepts_top3": [c.get("display_name") for c in (work.get("concepts") or [])[:3]],
            "abstract": reconstruct_abstract(work.get("abstract_inverted_index"))[:600],
            "referenced_by_seeds": list(set(prov["referenced_by"])),
            "related_to_seeds": list(set(prov["related_to"])),
            "has_cancer_keyword": has_cancer,
            "has_multiomics_keyword": has_omics,
            "score": score,
        })

    scored.sort(key=lambda x: (-x["score"], -(x["cited_by_count"] or 0)))

    # 5. Write JSON queue + Markdown report
    Path(args.out_json).write_text(json.dumps(scored, indent=2, ensure_ascii=False))

    lines = [
        "# OpenAlex Related Papers — Cancer Multiomics seeds",
        "",
        f"- Seeds: {len(seed_works)} OpenAlex works resolved out of {len(seed_dois)} DOIs",
        f"- Unique candidates surfaced: {len(cand_provenance)}",
        f"- Resolved candidate metadata: {len(cand_meta)}",
        f"- After cancer/multiomics filter + dedup: **{len(scored)}**",
        f"- Showing top {min(args.top_n, len(scored))} by score",
        "",
        "Filter: cancer keywords OR multiomics keywords in title/abstract/concepts.",
        "Score: 2× referenced_by seeds + 1× related_to seeds + cancer+omics bonus + cited_by tier.",
        "",
        "| # | Score | Year | First Author | Title | Journal | Cited | Cancer | Omics | Seed support |",
        "|---|---|---|---|---|---|---|---|---|---|",
    ]
    for i, c in enumerate(scored[:args.top_n], 1):
        seeds = (c["referenced_by_seeds"] + c["related_to_seeds"])
        seed_blob = ", ".join(sorted(set(s.split("-")[0] for s in seeds))[:4])
        lines.append(
            f"| {i} | {c['score']} | {c['year']} | {c['first_author_last']} | "
            f"[{(c['title'] or '')[:80]}](https://doi.org/{c['doi']}) | "
            f"{(c['journal'] or '')[:40]} | {c['cited_by_count']} | "
            f"{'Y' if c['has_cancer_keyword'] else ''} | "
            f"{'Y' if c['has_multiomics_keyword'] else ''} | "
            f"{seed_blob} |"
        )
    Path(args.out_report).write_text("\n".join(lines) + "\n")
    print(f"\nWrote {args.out_json} and {args.out_report}", file=sys.stderr)
    print(f"Top-{min(args.top_n, len(scored))} candidates ready for review", file=sys.stderr)


if __name__ == "__main__":
    main()
