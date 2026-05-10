#!/usr/bin/env python3
"""Pick 2 unposted backlog papers matching the 한미암 (cancer multiomics) filter.

Reads wiki/sources/*.md frontmatter, scores each by tag/kind/year/journal,
filters out already-posted slugs (from wiki/_meta/slack-posted.json),
and outputs JSON of the top 2 picks to stdout.

Output schema:
  {
    "date": "YYYY-MM-DD",
    "selected": [
      {"slug": "...", "score": <int>, "path": "wiki/sources/<slug>.md", "meta": {...}},
      ...
    ]
  }
"""
import datetime
import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
SOURCES = REPO / "wiki/sources"
POSTED = REPO / "wiki/_meta/slack-posted.json"

# Tier 1 — phosphoproteome × drug response / kinase × targeted therapy
TIER1 = {"phosphoproteomics", "ptm", "kinase-signaling", "ppqtl",
         "ptm-anchor", "ptmanchor", "phospho", "ptm-correction"}
# Tier 2 — proteogenomics + WGS + neoantigen + immunotherapy resistance
TIER2 = {"cancer-proteomics", "neoantigen", "neoantigen-discovery",
         "resistance", "resistance-framework", "immune-evasion",
         "immunotherapy", "translational-oncology", "clinical-translation",
         "proteomics", "multiomics-identification",
         "bcell-neoantigen"}
# Tier 3 — adjacent
TIER3 = {"tls", "tls-biology", "b-cells", "immunology",
         "multiomics-proteomics-ptm-identification"}

# paper_kind boost
KIND_BOOST = {
    "proteogenomic": 6,
    "clinical-trial": 5,
    "trial": 4,
    "translational": 4,
    "research": 1,
    "review": 0,
    "computational": 1,
    "mechanistic": 2,
    "cohort-study": 3,
}

# High-impact journals (lowercase substring match)
HIGH_IMPACT = [
    "nature medicine", "nature cancer", "cancer cell", "cancer discovery",
    "nature reviews cancer", "cell", "nature", "science",
    "lancet oncology", "lancet",
    "new england journal of medicine", "n engl j med",
    "nature communications", "nat commun",
    "cell reports medicine", "molecular cell", "immunity",
    "journal of clinical oncology", "j clin oncol",
    "annals of oncology", "ann oncol",
    "clinical cancer research", "jama oncology",
    "science translational medicine", "sci transl med",
    "signal transduction and targeted therapy",
    "molecular & cellular proteomics", "mol cell proteomics",
    "nature biotechnology", "nat biotechnol",
]

# Exclude predatory / low-tier
JOURNAL_EXCLUDE = ["mdpi", "scientific reports", "plos one", "iscience",
                   "cancers (basel)", "biomedicines",
                   "international journal of molecular sciences"]


def parse_frontmatter(text):
    """Tiny YAML frontmatter parser (handles the wiki's specific format)."""
    if not text.startswith("---"):
        return None
    end = text.find("\n---\n", 4)
    if end < 0:
        end = text.find("\n---\r\n", 4)
    if end < 0:
        return None
    fm = text[4:end]

    out = {}
    cur_key = None
    cur_list = None
    for raw in fm.split("\n"):
        line = raw.rstrip()
        if not line:
            continue
        # list item
        m = re.match(r"^\s+-\s*(.*)$", line)
        if m and cur_list is not None:
            val = m.group(1).strip().strip('"').strip("'")
            if val:
                cur_list.append(val)
            continue
        # key: value
        m = re.match(r"^([A-Za-z_][A-Za-z0-9_]*):\s*(.*)$", line)
        if m:
            cur_key = m.group(1)
            val = m.group(2).strip()
            if val == "":
                cur_list = []
                out[cur_key] = cur_list
            else:
                cur_list = None
                out[cur_key] = val.strip('"').strip("'")
    return out


def journal_score(journal: str) -> int:
    if not journal:
        return 0
    j = journal.lower()
    for ex in JOURNAL_EXCLUDE:
        if ex in j:
            return -10
    for hi in HIGH_IMPACT:
        if hi in j:
            return 3
    return 1


def score_paper(meta: dict) -> int:
    if not meta:
        return -100
    tags = set()
    for k in ("tags", "themes"):
        v = meta.get(k)
        if isinstance(v, list):
            tags.update(t.lower() for t in v)
    topic = meta.get("topic", "")
    if topic:
        tags.add(topic.lower())
    extras = meta.get("extra_topics")
    if isinstance(extras, list):
        tags.update(t.lower() for t in extras)

    s = 0
    if tags & TIER1:
        s += 12
    if tags & TIER2:
        s += 5
    if tags & TIER3:
        s += 2

    kind = meta.get("paper_kind", "").strip()
    s += KIND_BOOST.get(kind, 0)

    s += journal_score(meta.get("journal", ""))

    try:
        year = int(str(meta.get("year", "0")).strip())
        s += max(0, year - 2020)  # 2021→1, 2026→6
    except Exception:
        pass

    # Need at least one Tier1 or Tier2 hit
    if not (tags & (TIER1 | TIER2)):
        s -= 100

    return s


def load_posted() -> set:
    if POSTED.exists():
        try:
            return set(json.loads(POSTED.read_text()).get("slugs", []))
        except Exception:
            return set()
    return set()


def main():
    posted = load_posted()
    candidates = []
    for p in sorted(SOURCES.glob("*.md")):
        if p.stem in posted:
            continue
        if p.stem == "index":
            continue
        try:
            text = p.read_text(encoding="utf-8")
        except Exception:
            continue
        meta = parse_frontmatter(text)
        if not meta:
            continue
        s = score_paper(meta)
        if s < 5:
            continue
        candidates.append({
            "slug": p.stem,
            "score": s,
            "path": str(p.relative_to(REPO)),
            "meta": meta,
        })

    # Sort by score desc, then year desc as tiebreaker
    candidates.sort(
        key=lambda c: (-c["score"],
                       -int(str(c["meta"].get("year") or 0).split(".")[0])
                       if str(c["meta"].get("year") or "").strip().split(".")[0].isdigit() else 0)
    )

    selected = candidates[:2]

    out = {
        "date": datetime.date.today().isoformat(),
        "total_candidates": len(candidates),
        "selected": selected,
    }
    json.dump(out, sys.stdout, indent=2, ensure_ascii=False)
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()
