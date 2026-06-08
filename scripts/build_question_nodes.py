#!/usr/bin/env python3
"""
sprint md(### Q + **A.** + **Cited**) -> 그래프 질문 노드 자동 생성.

interactives/llm-wiki-all.html 의 `const DATA={nodes,links}` 에서
- 논문/허브 노드와 기존 cancer-multiomics 질문(Q1~Q57)은 그대로 보존하고
- SPRINTS 에 등록된 sprint md 를 파싱해 질문 노드(type:"q") + 근거 링크(kind:"qp") 를 주입한다.

멱등: 각 sprint 의 id_prefix 로 시작하는 질문 노드/링크를 먼저 제거 후 재생성하므로
sprint md 를 고치고 다시 실행하면 그래프가 항상 위키와 일치한다(따로 놀지 않음).

재직렬화는 json.dumps(separators=(", ", ": "), ensure_ascii=False) 로,
원본 DATA 문자열과 바이트 단위로 동일한 스타일이라 기존 노드는 한 글자도 바뀌지 않는다.
"""
import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
GRAPH = REPO / "interactives" / "llm-wiki-all.html"
BASE = "https://hejeong1219.github.io/paperatlas"

# 그래프에 자동 주입할 sprint 세트. 새 sprint 추가 시 여기에 한 줄.
# cancer-multiomics(Q1~Q57)는 그래프에 수기 정리분(Q51~57 포함)이 있어 보존 대상이라 넣지 않는다.
SPRINTS = [
    {
        "file": "wiki/analyses/bcell-neoantigen-50q-sprint-2026-05.md",
        "id_prefix": "BN",          # 노드 id: BN1..BN50 (기존 Q*/sources/* 와 충돌 없음)
        "label_prefix": "N",        # 그래프 표시 라벨: N1..N50 (Neoantigen)
        "anchor": "DOM::neoantigen",  # 끌어당길 허브
    },
]


def extract_data(html: str):
    """`const DATA=` 뒤의 최상위 {..} 를 brace-match 로 잘라 (start, end, obj) 반환."""
    i = html.index("const DATA=")
    depth = 0
    start = end = -1
    in_str = False
    esc = False
    k = i + len("const DATA=")
    while k < len(html):
        c = html[k]
        if in_str:
            if esc:
                esc = False
            elif c == "\\":
                esc = True
            elif c == '"':
                in_str = False
        else:
            if c == '"':
                in_str = True
            elif c == "{":
                if depth == 0:
                    start = k
                depth += 1
            elif c == "}":
                depth -= 1
                if depth == 0:
                    end = k
                    break
        k += 1
    return start, end, json.loads(html[start:end + 1])


_LINK_RE = re.compile(r"\[([^\]]+)\]\(\.\./([a-z]+)/([^)]+?)\.md\)")
_BOLD_RE = re.compile(r"\*\*([^*]+?)\*\*")


def md_to_html(text: str) -> str:
    """답변 markdown -> 그래프 answer HTML (cancer-multiomics 기존 노드와 동일 규칙)."""
    text = text.strip()
    if text.startswith("**A.**"):
        text = text[len("**A.**"):].strip()
    # [label](../dir/slug.md) -> <a href="BASE/dir/slug" target="_blank">label</a>
    text = _LINK_RE.sub(
        lambda m: f'<a href="{BASE}/{m.group(2)}/{m.group(3)}" target="_blank">{m.group(1)}</a>',
        text,
    )
    # **bold** -> <b>bold</b>
    text = _BOLD_RE.sub(r"<b>\1</b>", text)
    return text


def parse_cited(cited_md: str):
    """**Cited** 라인 -> (라벨 리스트, cites[{label,url}], sources 슬러그 리스트). sources 만."""
    labels, cites, slugs = [], [], []
    for m in re.finditer(r"\[([^\]]+)\]\(\.\./sources/([^)]+?)\.md\)", cited_md or ""):
        label, slug = m.group(1), m.group(2)
        labels.append(label)
        cites.append({"label": label, "url": f"{BASE}/sources/{slug}"})
        slugs.append(slug)
    return labels, cites, slugs


_SEC_RE = re.compile(r"^##\s+Section\s+([A-Z])\s+[—-]\s+(.+?)\s*\(Q", re.UNICODE)
_Q_RE = re.compile(r"^###\s+Q(\d+)\.\s+(.+?)\s*$")


def parse_sprint(path: Path):
    """sprint md -> 질문 dict 리스트."""
    sec = secname = None
    questions = []
    for line in path.read_text(encoding="utf-8").splitlines():
        m = _SEC_RE.match(line)
        if m:
            sec, secname = m.group(1), m.group(2).strip()
            continue
        m = _Q_RE.match(line)
        if m:
            questions.append({
                "n": int(m.group(1)), "title": m.group(2).strip(),
                "sec": sec, "secname": secname, "answer_md": None, "cited_md": None,
            })
            continue
        if not questions:
            continue
        if line.startswith("**A.**"):
            questions[-1]["answer_md"] = line
        elif line.startswith("**Cited**"):
            questions[-1]["cited_md"] = line.split(":", 1)[1] if ":" in line else ""
    return questions


def build():
    html = GRAPH.read_text(encoding="utf-8")
    start, end, D = extract_data(html)
    paper_ids = {n["id"] for n in D["nodes"] if n.get("type") == "paper"}
    before_q = sum(1 for n in D["nodes"] if n.get("type") == "q")

    report = []
    for sp in SPRINTS:
        pre = sp["id_prefix"]
        # 멱등 제거
        D["nodes"] = [n for n in D["nodes"]
                      if not (n.get("type") == "q" and str(n.get("id", "")).startswith(pre))]
        D["links"] = [l for l in D["links"]
                      if not (str(l.get("s", "")).startswith(pre) or str(l.get("t", "")).startswith(pre))]

        questions = parse_sprint(REPO / sp["file"])
        added_n = added_l = miss_ans = 0
        missing_papers = set()
        for q in questions:
            if not q["answer_md"]:
                miss_ans += 1
                continue
            labels, cites, slugs = parse_cited(q["cited_md"])
            node = {
                "id": f"{pre}{q['n']}",
                "type": "q",
                "label": f"{sp['label_prefix']}{q['n']}",
                "title": q["title"],
                "sec": q["sec"],
                "secname": q["secname"],
                "color": "#444444",
                "cited": labels,
                "anchor": sp["anchor"],
                "answer": md_to_html(q["answer_md"]),
                "cites": cites,
            }
            D["nodes"].append(node)
            added_n += 1
            for slug in slugs:
                pid = f"sources/{slug}"
                if pid in paper_ids:
                    D["links"].append({"s": node["id"], "t": pid, "kind": "qp"})
                    added_l += 1
                else:
                    missing_papers.add(slug)
        report.append((sp["file"], added_n, added_l, miss_ans, missing_papers))

    after_q = sum(1 for n in D["nodes"] if n.get("type") == "q")
    new_data = json.dumps(D, ensure_ascii=False, separators=(", ", ": "))
    out = html[:start] + new_data + html[end + 1:]
    # 타이틀 패널/범례의 "내 질문 N개" 정적 텍스트도 질문 수에 맞춰 갱신(라벨이 그래프와 따로 놀지 않게)
    out = re.sub(r"내 질문 \d+개", f"내 질문 {after_q}개", out)
    GRAPH.write_text(out, encoding="utf-8")

    print(f"질문 노드: {before_q} -> {after_q}")
    for f, an, al, ma, mp in report:
        print(f"  {f}: +{an} 질문, +{al} 근거링크, 답없음 {ma}")
        if mp:
            print(f"    그래프에 없는 근거 논문(링크 생략): {sorted(mp)}")


if __name__ == "__main__":
    build()
