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

# paper_kind values that mean the paper's main contribution is a NEW analysis
# tool / model / pipeline / benchmark. 청중이 임상·기초 교수진이라 method-only
# 논문은 의미 없음 → backlog 후보에서 완전 제외. review도 제외 (사용자 요청:
# 한미암 슬랙은 리서치 아티클만 올림).
EXCLUDED_KIND = {"computational", "methods/tool", "software", "method",
                 "tool", "benchmark", "pipeline", "review"}

# 최근 N년 이내 논문만 후보 — 청중에 너무 오래된 클래식은 의미 낮음.
RECENT_YEARS = 5

# 위암 키워드 — title/tags/themes에 매칭되면 위암 boost 가산.
GASTRIC_RE = re.compile(r"\bgastric\b|\bstomach\b", re.IGNORECASE)

# scRNA / spatial transcriptomics 가 main contribution 인 논문 — 한미암 코호트는
# bulk proteomics/phospho/WGS/RNA 중심이고 scRNA/spatial 데이터 생산 계획이 없어
# 청중 활용성이 낮음 → 큰 감점 (완전 제외하진 않되 다른 후보가 있으면 밀려나도록).
SCRNA_SPATIAL_RE = re.compile(
    r"\bsingle.cell\b|\bsingle.nucleus\b|\bspatial transcriptomic|\bscRNA",
    re.IGNORECASE,
)

# Key Points placeholder 패턴 — 아직 deep-dive 안 된 논문은 활용 line 부실해질
# 위험이 커서 후보에서 제외. 구 포맷("_To be filled", "_Awaiting deep-dive")과
# batch-ingest 자동생성 포맷("_Key claims to be filled in from full text. This page
# was created automatically as a placeholder._") 둘 다 잡아야 함.
KP_PLACEHOLDER_RE = re.compile(
    r"_to be filled|_awaiting deep.dive|awaiting deep.dive"
    r"|to be filled in from full text|created automatically as a placeholder"
    r"|key claims to be filled",
    re.IGNORECASE)

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

    # 위암 우선순위 — 한미암 과제의 핵심 암종. title/tags/themes에 gastric/stomach
    # 매칭되면 큰 가산점으로 같은 tier 안에서 위암 논문이 먼저 선택되도록.
    title = meta.get("title") or ""
    gastric_hit = bool(GASTRIC_RE.search(title)) or any(
        ("gastric" in t) or ("stomach" in t) for t in tags
    )
    if gastric_hit:
        s += 20

    # scRNA / spatial main contribution → 한미암 modality 비매치 → deprioritize.
    # 같은 위암 논문이라도 scRNA만으로 main contribution이면 코호트에 적용 불가.
    scrna_hit = bool(SCRNA_SPATIAL_RE.search(title)) or any(
        ("single-cell" in t) or ("scrna" in t) or
        ("spatial-transcriptomic" in t) or ("single-nucleus" in t)
        for t in tags
    )
    if scrna_hit:
        s -= 15

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
    skipped_pending = 0
    skipped_no_keypoints = 0
    skipped_method_kind = 0
    skipped_old_year = 0
    cutoff_year = datetime.date.today().year - RECENT_YEARS
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
        # HARD FILTER: method/tool/software/review papers are dropped from the
        # backlog — 청중이 임상·기초 교수진이라 분석 툴 자체가 contribution인 논문이나
        # 리뷰는 슬랙에 올리지 않음.
        kind = (meta.get("paper_kind") or "").strip().lower()
        if kind in EXCLUDED_KIND:
            skipped_method_kind += 1
            continue
        # HARD FILTER: 5년 이내 논문만. 너무 오래된 클래식은 청중이 이미 알고 있을
        # 가능성이 높고 신선도가 떨어짐.
        try:
            year = int(str(meta.get("year") or 0).split(".")[0])
        except Exception:
            year = 0
        if year and year < cutoff_year:
            skipped_old_year += 1
            continue
        # HARD FILTER: skip papers where the user has not yet finished
        # full-PDF-based analysis. Posting these would violate the
        # "no abstract-only judgment" rule.
        if str(meta.get("pdf_status", "")).strip().lower() == "pending":
            skipped_pending += 1
            continue
        # Extra safety: require a non-placeholder Key Points section.
        # Placeholders: "_To be filled after local PDF...", "_Awaiting deep-dive...".
        body = text[text.find("\n---\n", 4) + 5:] if text.startswith("---") else text
        if "## Key Points" in body:
            kp_idx = body.find("## Key Points")
            kp_block = body[kp_idx:kp_idx + 800]
            if KP_PLACEHOLDER_RE.search(kp_block):
                skipped_no_keypoints += 1
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
        "skipped_pending_pdf": skipped_pending,
        "skipped_placeholder_keypoints": skipped_no_keypoints,
        "skipped_method_kind": skipped_method_kind,
        "skipped_old_year": skipped_old_year,
        "cutoff_year": cutoff_year,
        "selected": selected,
    }
    json.dump(out, sys.stdout, indent=2, ensure_ascii=False)
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()
