#!/usr/bin/env python3
"""
워크플로우가 생성한 답(/tmp/qfill/out/<prefix>_<batch>.json)을 위키 sprint md로 변환.

각 세트(PB/PE/TN/TR/TP/TM)마다 wiki/analyses/<slug>-answered-2026-06.md 를 생성한다.
형식은 기존 sprint와 동일(### Q + **A.** + **Cited**)이라 scripts/build_question_nodes.py 가
그대로 파싱해 그래프 질문 노드로 반영할 수 있다 → 위키 페이지와 그래프가 같은 소스에서 나온다.
"""
import json
import glob
import re
from pathlib import Path
from collections import defaultdict

REPO = Path(__file__).resolve().parent.parent
OUT = REPO / "outputs/qfill/out"
QUESTIONS = json.load(open(REPO / "outputs/qfill/questions.json", encoding="utf-8"))
SRC_IDX = {s["slug"]: s for s in json.load(open(REPO / "outputs/qfill/sources_index.json", encoding="utf-8"))}
SOURCE_SLUGS = {p.stem for p in (REPO / "wiki/sources").glob("*.md")}

SETS = {
    "PB": dict(title="PTM Correction & Kinase Signaling — Question Bank (Answered)",
               slug="ptm-correction-question-bank-answered", secname="PTM correction & kinase inference",
               tags=["question-bank", "ptm-correction", "answered"]),
    "PE": dict(title="PTM Correction & Kinase Signaling — Expansion Bank (Answered)",
               slug="ptm-correction-expansion-bank-answered", secname="PTM confounding & coupling models",
               tags=["question-bank", "ptm-correction", "answered"]),
    "TN": dict(title="B-Cell Neoantigen Research Map — Topic Questions (Answered)",
               slug="bcell-neoantigen-topic-answered", secname="Neoantigen discovery & B-cell biology",
               tags=["question-bank", "bcell-neoantigen", "answered"]),
    "TR": dict(title="Immunotherapy Resistance & Immune Evasion — Topic Questions (Answered)",
               slug="immunotherapy-resistance-topic-answered", secname="Immunotherapy resistance & immune evasion",
               tags=["question-bank", "resistance", "answered"]),
    "TP": dict(title="Multiomics Proteomics PTM Identification — Topic Questions (Answered)",
               slug="multiomics-ptm-topic-answered", secname="PTM identification methods",
               tags=["question-bank", "ptm", "answered"]),
    "TM": dict(title="Cancer Multiomics Proteogenomic Atlas — Topic Questions (Answered)",
               slug="cancer-multiomics-topic-answered", secname="Cancer multiomics integration",
               tags=["question-bank", "cancer-multiomics", "answered"]),
}


def label_of(slug):
    s = SRC_IDX.get(slug)
    if s and s.get("authors") and s.get("year"):
        return f"{s['authors'][0]} {s['year']}"
    return slug


def load_answers():
    """qid -> {answer, cites}."""
    ans = {}
    for f in sorted(OUT.glob("*.json")):
        prefix = f.stem.split("_")[0]
        try:
            data = json.load(open(f, encoding="utf-8"))
        except Exception as e:
            print(f"  !! {f.name} JSON 파싱 실패: {e}")
            continue
        for item in data:
            ans[f"{prefix}{item['n']}"] = item
    return ans


def build():
    answers = load_answers()
    q_by_prefix = defaultdict(list)
    for q in QUESTIONS:
        q_by_prefix[q["prefix"]].append(q)

    stats = []
    for prefix, meta in SETS.items():
        qs = sorted(q_by_prefix[prefix], key=lambda q: q["n"])
        lines = ["---", f'title: "{meta["title"]}"', "tags:"]
        lines += [f"  - {t}" for t in meta["tags"]]
        lines += ["date: 2026-06-08", "status: answered-2026-06", "---", "",
                  f"# {meta['title']}", "",
                  "위키 확장 질문에 로컬 `wiki/sources/` 논문 근거로 답을 단 sprint. "
                  "답·근거는 그래프(`interactives/llm-wiki-all.html`)에 질문 노드로 자동 반영된다.", "",
                  f"## Section A — {meta['secname']} (Q1-{len(qs)})", ""]
        answered = cited_total = bad = 0
        for q in qs:
            a = answers.get(q["qid"])
            lines.append(f"### Q{q['n']}. {q['text']}")
            if not a:
                bad += 1
                lines.append("**A.** (답 생성 실패 — 재처리 필요)")
                lines.append("")
                continue
            answered += 1
            lines.append(f"**A.** {a['answer'].strip()}")
            cites = [c for c in a.get("cites", []) if c in SOURCE_SLUGS]
            cited_total += len(cites)
            if cites:
                lines.append("")
                lines.append("**Cited**: " + ", ".join(f"[{label_of(c)}](../sources/{c}.md)" for c in cites))
            lines.append("")
        path = REPO / "wiki/analyses" / f"{meta['slug']}.md"
        path.write_text("\n".join(lines), encoding="utf-8")
        stats.append((prefix, len(qs), answered, cited_total, bad, path.name))

    print(f"{'set':4} {'질문':>4} {'답':>4} {'근거':>5} {'실패':>4}  파일")
    for prefix, n, a, c, b, fn in stats:
        print(f"{prefix:4} {n:4d} {a:4d} {c:5d} {b:4d}  {fn}")
    print(f"\n총 답: {sum(s[2] for s in stats)} / {sum(s[1] for s in stats)} 질문, 근거링크 {sum(s[3] for s in stats)}, 실패 {sum(s[4] for s in stats)}")


if __name__ == "__main__":
    build()
