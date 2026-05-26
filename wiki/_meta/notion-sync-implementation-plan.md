# Notion → Wiki Sync 자동화 — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Notion "참고 논문 및 아이디어" DB(`344302d9-c598-8188-8a05-d5041134fb3d`) 하위 페이지를 daily cron으로 fetch → Claude로 한미암 프로젝트 Tier 판단 → Tier 1/2 논문은 PDF 다운로드 + `wiki/sources/` stub MD 생성, Tier 0/3은 state만 마킹.

**Architecture:** 5개 파일의 단방향 파이프 — `fetch_notion_pages.py` (Notion SDK) → `/tmp/notion_candidates_<date>.json` → `sync_papers.py` (per-candidate orchestrator) → `claude -p` (Tier judge) + `pdf_resolver.py` (DOI-first chain + ezproxy fallback) → wiki/sources/<slug>.md + raw/inbox/papers/<slug>.pdf + `wiki/_meta/notion-synced.json`. 기존 daily_digest cron과 별도 디렉토리(`scripts/notion_sync/`)·state·cron entry.

**Tech Stack:** Python 3 (anaconda3), `notion-client` SDK, `claude` CLI, 기존 `scripts/ingest/resolve_pdf.py` + `ezproxy_download.py` 라이브러리 호출, KU EZproxy 쿠키(`.cookies/oca.cookies.txt`), bash cron wrapper.

**Spec reference:** [notion-sync-automation-spec.md](notion-sync-automation-spec.md) (Tier 정책·data flow·schema 정의)

**Test approach:** Repo에 `tests/` 디렉토리 없음 — `pytest` 단위 테스트 대신 **smoke test via DRY_RUN/LIMIT** 사용. 각 step 작성 직후 실제 데이터(또는 mock JSON)로 1회 실행해 동작 확인. 기존 `scripts/daily_digest/run.sh`와 동일한 검증 패턴.

---

## File Structure

```
scripts/notion_sync/                          (NEW directory)
├── __init__.py                               (NEW, empty — Python package marker)
├── fetch_notion_pages.py                     (NEW, ~250 lines) — Notion SDK → candidates JSON
├── pdf_resolver.py                           (NEW, ~80 lines)  — DOI-first PDF wrapper
├── sync_papers.py                            (NEW, ~250 lines) — per-candidate orchestrator
├── prompt.md                                 (NEW, ~80 lines)  — Claude Tier judge prompt
├── run.sh                                    (NEW, ~120 lines) — cron orchestrator
└── cron_entry.sh                             (NEW, ~50 lines)  — cron env wrapper

wiki/_meta/notion-synced.json                 (NEW, runtime state — JSON, atomic flush)
logs/notion-sync-<date>.log                   (NEW, runtime log — git-ignored)
```

**Responsibility split:**
- `fetch_notion_pages.py` — Notion API + 3-way dedup (state/slug/DOI). Stdout = candidate JSON.
- `pdf_resolver.py` — Library only. Wraps `resolve_and_download` + DOI-direct chain + ezproxy fallback.
- `sync_papers.py` — 각 candidate per-paper: claude judge 호출, PDF resolve, stub MD write, incremental state flush.
- `prompt.md` — Claude 판단용 1-편당 1-호출 프롬프트. JSON output only.
- `run.sh` — git pull → fetch → sync → commit → push. STAGE/DRY_RUN/LIMIT/ONLY_PAGE_ID env vars.
- `cron_entry.sh` — conda load, PATH, GIT_SSH_COMMAND, ~/.paperatlas.env 로드. `run.sh` 호출.

---

## Task 0: Environment Setup

**Files:** None (env + system check)

- [ ] **Step 0.1: Install notion-client SDK**

Run: `/home/hejeong/anaconda3/bin/pip install notion-client`
Expected: `Successfully installed notion-client-X.Y.Z`

- [ ] **Step 0.2: Verify NOTION_API_KEY available**

User action prerequisite (not in plan execution scope):
1. https://www.notion.so/profile/integrations 에서 internal integration 생성 (예: "wiki-sync")
2. 부모 페이지 `344302d9-c598-8188-8a05-d5041134fb3d`에 integration 명시적 공유 ("Connections" → integration 추가)
3. integration token (`secret_...` 또는 `ntn_...`)을 `~/.paperatlas.env`에 `export NOTION_API_KEY=...` 형식으로 추가
4. `chmod 600 ~/.paperatlas.env` 확인

Run (확인): `grep -c NOTION_API_KEY ~/.paperatlas.env`
Expected: `1` (한 줄 존재). 없으면 사용자에게 위 절차 안내 후 일시 정지.

- [ ] **Step 0.3: Verify KU cookies exist**

Run: `ls -la /home/hejeong/Dropbox/llm-wiki/.cookies/oca.cookies.txt`
Expected: 파일 존재, 비어있지 않음 (다운로드 fallback에 사용됨).
파일 없으면 ezproxy step은 skip되고 OA chain만 시도됨 — 치명적이지 않으나 paywall paper PDF는 manual queue로 빠짐.

- [ ] **Step 0.4: Verify claude CLI on PATH**

Run: `which claude && claude --version 2>&1 | head -1`
Expected: claude binary 경로 + 버전 출력.

---

## Task 1: pdf_resolver.py — DOI-first PDF wrapper

**Files:**
- Create: `scripts/notion_sync/__init__.py` (empty)
- Create: `scripts/notion_sync/pdf_resolver.py`

기존 `scripts/ingest/resolve_pdf.py`는 title→PubMed PMID 검색에 의존해 DOI는 있지만 PMID 없는 2026 preprint나 비-PubMed 저널은 OA chain이 실행되지 않음. 본 wrapper가 DOI-first 흐름 보장 + KU ezproxy fallback.

- [ ] **Step 1.1: Create empty __init__.py**

```bash
mkdir -p scripts/notion_sync
touch scripts/notion_sync/__init__.py
```

- [ ] **Step 1.2: Write pdf_resolver.py**

Create `scripts/notion_sync/pdf_resolver.py`:

```python
#!/usr/bin/env python3
"""DOI-first PDF wrapper for Notion-sync flow.

Wraps scripts/ingest/resolve_pdf.py (which requires PMID via title search)
with a DOI-seeded fallback chain, then KU EZproxy fallback. Returns the
same shape as resolve_and_download() with `tried` listing every attempt.
"""
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
INGEST = REPO / "scripts/ingest"
sys.path.insert(0, str(INGEST))

from resolve_pdf import (  # noqa: E402
    resolve_and_download,
    try_unpaywall,
    try_doi_direct,
    try_elsevier,
    try_springer,
)
from ezproxy_download import (  # noqa: E402
    load_cookies,
    make_opener,
    try_ezproxy_pdf,
)


def resolve_with_doi(ref, out_dir):
    """Resolve PDF for a DOI-only ref (PMID may not exist).

    ref keys (required): slug, title, year, first_author_last, doi
    ref keys (optional): pmcid, journal

    Returns dict shaped like resolve_and_download() output:
      {slug, pmid, pmcid, doi, journal, downloaded, pdf_path, tried, via}
    """
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / (ref["slug"] + ".pdf")

    # 1) Existing resolve_and_download — handles already-on-disk + PMID hit case.
    result = resolve_and_download(ref, out_dir)
    if result.get("downloaded"):
        return result

    # 2) PMID lookup may have failed, but ref["doi"] is known — seed manual chain.
    doi = ref["doi"]
    journal = result.get("journal") or ref.get("journal")
    fallback_chain = [
        ("unpaywall-doi", lambda: try_unpaywall(doi, out_path)),
        ("doi-direct-doi", lambda: try_doi_direct(doi, journal, out_path)),
        ("elsevier-doi", lambda: try_elsevier(doi, out_path)),
        ("springer-doi", lambda: try_springer(doi, out_path)),
    ]
    for name, fn in fallback_chain:
        try:
            ok, msg = fn()
        except Exception as e:
            ok, msg = False, f"exc: {e}"
        result["tried"].append({"src": name, "ok": ok, "msg": msg})
        if ok and out_path.exists() and out_path.stat().st_size > 5000:
            result["downloaded"] = True
            result["pdf_path"] = str(out_path)
            result["via"] = f"{name}: {msg}"
            return result

    # 3) KU EZproxy fallback (if cookies present).
    cookies = REPO / ".cookies/oca.cookies.txt"
    if cookies.exists():
        try:
            opener = make_opener(load_cookies(cookies))
            ok, info = try_ezproxy_pdf(opener, doi, out_path)
        except Exception as e:
            ok, info = False, f"ezproxy exc: {e}"
        result["tried"].append({"src": "ezproxy", "ok": ok, "msg": info})
        if ok and out_path.exists() and out_path.stat().st_size > 5000:
            result["downloaded"] = True
            result["pdf_path"] = str(out_path)
            result["via"] = f"ezproxy: {info}"
    else:
        result["tried"].append({"src": "ezproxy", "ok": False, "msg": "no cookies file"})

    return result


if __name__ == "__main__":
    # Smoke test: usage: pdf_resolver.py <doi> <slug> <first_author_last> <year> <title> <out_dir>
    import json
    if len(sys.argv) != 7:
        print("usage: pdf_resolver.py <doi> <slug> <first_author> <year> <title> <out_dir>",
              file=sys.stderr)
        sys.exit(1)
    ref = {
        "doi": sys.argv[1],
        "slug": sys.argv[2],
        "first_author_last": sys.argv[3],
        "year": int(sys.argv[4]),
        "title": sys.argv[5],
    }
    r = resolve_with_doi(ref, Path(sys.argv[6]))
    json.dump(r, sys.stdout, indent=2, default=str)
    sys.stdout.write("\n")
```

- [ ] **Step 1.3: Smoke test pdf_resolver with an OA-known DOI**

OA paper DOI (`10.1101/2024.01.01.000000` 같은 bioRxiv는 항상 OA — 단, 진짜 DOI가 아니면 실패함. 기존 wiki에서 한 편 가져오기).

```bash
DOI=$(grep -h '^doi:' wiki/sources/*.md 2>/dev/null | grep -v '^doi: ""$' | head -1 | sed 's/^doi: *//; s/^"//; s/"$//')
echo "Testing with DOI: $DOI"
python3 scripts/notion_sync/pdf_resolver.py \
    "$DOI" "smoke-test-resolver" "smoke" 2024 "Smoke test title" /tmp
```

Expected: JSON 출력에서 `tried` 배열이 여러 source 시도(`europepmc`, `unpaywall`, ...) 보여줘야 함. `downloaded: true` 또는 모든 source 실패 모두 OK — 라이브러리 호출 자체가 끊김 없이 실행되는지만 검증.

- [ ] **Step 1.4: Commit Task 1**

```bash
git add scripts/notion_sync/__init__.py scripts/notion_sync/pdf_resolver.py
git commit -m "Notion sync: add DOI-first PDF resolver wrapper

Wraps scripts/ingest/resolve_pdf.py with DOI-seeded fallback chain
+ KU EZproxy fallback for papers without PMID (preprints, non-PubMed
journals). Same return shape as resolve_and_download().

Co-Authored-By: Claude Opus 4.7 <noreply@anthropic.com>"
```

---

## Task 2: fetch_notion_pages.py — Notion → candidates JSON

**Files:**
- Create: `scripts/notion_sync/fetch_notion_pages.py`

Notion 부모 페이지(`344302d9-c598-8188-8a05-d5041134fb3d`)의 child page 모두 enumerate → DOI/title/authors/year/journal 추출 → 3-way dedup (state + slug + DOI) → candidate JSON으로 stdout.

- [ ] **Step 2.1: Write fetch_notion_pages.py — imports + constants**

Create `scripts/notion_sync/fetch_notion_pages.py` with this block first:

```python
#!/usr/bin/env python3
"""Fetch Notion '참고 논문 및 아이디어' child pages → candidates JSON.

Stdout: JSON with {date, parent_page_id, synced_count, fetched_total,
                   after_dedup, skipped, candidates: [...]}
Stderr: progress log.

Env vars:
  NOTION_API_KEY    required
  LIMIT             optional, cap on candidates emitted
  ONLY_PAGE_ID      optional, restrict to one page (debug)
"""
import argparse
import datetime
import json
import os
import re
import sys
from pathlib import Path

try:
    from notion_client import Client
except ImportError:
    print("ERROR: notion-client not installed. Run: pip install notion-client",
          file=sys.stderr)
    sys.exit(1)

REPO = Path(__file__).resolve().parents[2]
PARENT_PAGE_ID = "344302d9-c598-8188-8a05-d5041134fb3d"
STATE_PATH = REPO / "wiki/_meta/notion-synced.json"
WIKI_SOURCES = REPO / "wiki/sources"

DOI_RE = re.compile(r"10\.\d{4,9}/[^\s\"<>)]+")
```

- [ ] **Step 2.2: Add state helpers + dedup helpers**

Append to `fetch_notion_pages.py`:

```python
def load_state():
    if not STATE_PATH.exists():
        return {"last_run": None, "synced": [], "history": []}
    return json.loads(STATE_PATH.read_text())


def synced_page_ids(state):
    return {e["page_id"] for e in state.get("synced", []) if e.get("page_id")}


def slug_exists(slug):
    return (WIKI_SOURCES / f"{slug}.md").exists()


def doi_already_in_wiki(doi):
    """grep wiki/sources/*.md for matching `doi:` frontmatter line."""
    if not doi:
        return False
    pat = re.compile(r'^doi:\s*"?' + re.escape(doi.lower()) + r'"?\s*$',
                     re.IGNORECASE | re.MULTILINE)
    for md in WIKI_SOURCES.glob("*.md"):
        try:
            text = md.read_text(errors="ignore")
        except Exception:
            continue
        if pat.search(text):
            return True
    return False
```

- [ ] **Step 2.3: Add Notion page parser**

Append to `fetch_notion_pages.py`:

```python
def block_to_text(block):
    """Render a Notion block to plain markdown (best-effort)."""
    btype = block.get("type")
    if not btype:
        return ""
    payload = block.get(btype, {})
    rich = payload.get("rich_text", [])
    text = "".join(rt.get("plain_text", "") for rt in rich)
    if btype == "heading_1":
        return f"# {text}"
    if btype == "heading_2":
        return f"## {text}"
    if btype == "heading_3":
        return f"### {text}"
    if btype == "bulleted_list_item":
        return f"- {text}"
    if btype == "numbered_list_item":
        return f"1. {text}"
    if btype == "quote":
        return f"> {text}"
    if btype == "code":
        lang = payload.get("language", "")
        return f"```{lang}\n{text}\n```"
    if btype == "paragraph":
        return text
    return text  # divider, image, etc. — best-effort fall-through


def fetch_page_body(notion, page_id):
    """Concatenate all child blocks of a page into markdown-ish text."""
    parts = []
    cursor = None
    while True:
        resp = notion.blocks.children.list(block_id=page_id, start_cursor=cursor)
        for blk in resp.get("results", []):
            line = block_to_text(blk)
            if line:
                parts.append(line)
        if not resp.get("has_more"):
            break
        cursor = resp.get("next_cursor")
    return "\n\n".join(parts)


def extract_property_value(prop):
    """Notion property → plain str (handles title, rich_text, url, select, ...)."""
    if not prop:
        return ""
    ptype = prop.get("type")
    if ptype == "title":
        return "".join(t.get("plain_text", "") for t in prop.get("title", []))
    if ptype == "rich_text":
        return "".join(t.get("plain_text", "") for t in prop.get("rich_text", []))
    if ptype == "url":
        return prop.get("url") or ""
    if ptype == "select":
        sel = prop.get("select") or {}
        return sel.get("name", "")
    if ptype == "number":
        return prop.get("number")
    if ptype == "multi_select":
        return [s.get("name", "") for s in prop.get("multi_select", [])]
    return ""


def find_doi(properties, body_text):
    """Look for DOI in properties first, then body text."""
    for key, prop in properties.items():
        if "doi" in key.lower():
            val = extract_property_value(prop)
            if isinstance(val, str) and val:
                m = DOI_RE.search(val)
                if m:
                    return m.group(0).rstrip(".,;)")
    m = DOI_RE.search(body_text or "")
    return m.group(0).rstrip(".,;)") if m else None


def find_url(properties):
    for key, prop in properties.items():
        if "url" in key.lower() or "link" in key.lower():
            val = extract_property_value(prop)
            if isinstance(val, str) and val.startswith("http"):
                return val
    return ""
```

- [ ] **Step 2.4: Add slug builder + parser orchestration**

Append to `fetch_notion_pages.py`:

```python
def make_slug(first_author_last, year, title):
    """authoryear-firstwords-of-title kebab. Mirror existing wiki slug convention."""
    base = re.sub(r"[^a-z0-9\s-]", "", (title or "").lower())
    words = base.split()[:6]
    slug = f"{first_author_last}-{year}-" + "-".join(words)
    return re.sub(r"-+", "-", slug).strip("-")


def parse_title_for_author_year(notion_title):
    """Best-effort: Notion title is freeform user text like
    'Xu et al. 2026 — Chinese HER2-low BC proteogenomics + lactylome'.
    Extract first author surname + year. Falls back to defaults on no match."""
    title = notion_title or ""
    yr_m = re.search(r"\b(19|20)\d{2}\b", title)
    year = int(yr_m.group(0)) if yr_m else 0
    name_m = re.match(r"^\s*([A-Za-zÀ-ſ][A-Za-zÀ-ſ\-']*)", title)
    first_author_last = (name_m.group(1) if name_m else "unknown").lower()
    first_author_last = re.sub(r"[^a-z]", "", first_author_last) or "unknown"
    return first_author_last, year


def parse_notion_page(notion, page):
    """Page payload → candidate dict (or None if no DOI)."""
    page_id = page["id"]
    properties = page.get("properties", {})

    # Notion stores child page name as a 'title' property — find it.
    title_text = ""
    for prop in properties.values():
        if prop.get("type") == "title":
            title_text = "".join(t.get("plain_text", "") for t in prop.get("title", []))
            break

    body = fetch_page_body(notion, page_id)
    doi = find_doi(properties, body)
    if not doi:
        return None  # caller logs warning

    first_author_last, year = parse_title_for_author_year(title_text)
    if not year:
        # Final fallback: this year
        year = datetime.date.today().year

    slug = make_slug(first_author_last, year, title_text)

    return {
        "page_id": page_id,
        "title": title_text,
        "doi": doi,
        "first_author_last": first_author_last,
        "year": year,
        "journal": "",   # left blank; deep-dive will fill
        "slug_candidate": slug,
        "notion_url": page.get("url", ""),
        "notion_body": body,
    }
```

- [ ] **Step 2.5: Add main() and dedup loop**

Append to `fetch_notion_pages.py`:

```python
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--parent", default=PARENT_PAGE_ID,
                    help="Notion parent page ID (default: 참고 논문 및 아이디어 root)")
    args = ap.parse_args()

    token = os.environ.get("NOTION_API_KEY")
    if not token:
        print("ERROR: NOTION_API_KEY not set", file=sys.stderr)
        sys.exit(1)

    only = os.environ.get("ONLY_PAGE_ID")
    limit = int(os.environ.get("LIMIT", "0"))

    notion = Client(auth=token)
    state = load_state()
    synced_ids = synced_page_ids(state)

    # Enumerate child pages of parent.
    children = []
    cursor = None
    while True:
        resp = notion.blocks.children.list(block_id=args.parent, start_cursor=cursor)
        for blk in resp.get("results", []):
            if blk.get("type") == "child_page":
                children.append(blk["id"])
        if not resp.get("has_more"):
            break
        cursor = resp.get("next_cursor")

    print(f"[fetch] parent has {len(children)} child pages", file=sys.stderr)

    skipped = {"already_synced": 0, "slug_collision": 0, "doi_collision": 0,
               "no_doi": 0, "filter": 0}
    candidates = []

    for page_id in children:
        if only and page_id != only:
            skipped["filter"] += 1
            continue
        if page_id in synced_ids:
            skipped["already_synced"] += 1
            continue
        try:
            page = notion.pages.retrieve(page_id=page_id)
        except Exception as e:
            print(f"  {page_id}: retrieve failed: {e}", file=sys.stderr)
            continue
        cand = parse_notion_page(notion, page)
        if cand is None:
            print(f"  {page_id}: DOI missing — skip", file=sys.stderr)
            skipped["no_doi"] += 1
            continue
        if slug_exists(cand["slug_candidate"]):
            print(f"  {page_id}: slug {cand['slug_candidate']} exists — skip",
                  file=sys.stderr)
            skipped["slug_collision"] += 1
            continue
        if doi_already_in_wiki(cand["doi"]):
            print(f"  {page_id}: DOI {cand['doi']} already in wiki — skip",
                  file=sys.stderr)
            skipped["doi_collision"] += 1
            continue
        candidates.append(cand)
        if limit and len(candidates) >= limit:
            print(f"[fetch] LIMIT={limit} reached", file=sys.stderr)
            break

    out = {
        "date": datetime.date.today().isoformat(),
        "parent_page_id": args.parent,
        "synced_count": len(synced_ids),
        "fetched_total": len(children),
        "after_dedup": len(candidates),
        "skipped": skipped,
        "candidates": candidates,
    }
    json.dump(out, sys.stdout, ensure_ascii=False, indent=2)
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()
```

- [ ] **Step 2.6: Smoke test (dry — env var unset path)**

Run: `python3 scripts/notion_sync/fetch_notion_pages.py 2>&1 | head -5`
Expected: `ERROR: NOTION_API_KEY not set` then exit 1 (env var unset path).

- [ ] **Step 2.7: Smoke test (real Notion fetch with LIMIT=1)**

Requires Step 0.2 done (NOTION_API_KEY available + parent page shared with integration).

```bash
source ~/.paperatlas.env
LIMIT=1 python3 scripts/notion_sync/fetch_notion_pages.py > /tmp/notion_smoke.json 2>/tmp/notion_smoke.stderr
echo "--- stderr ---"; cat /tmp/notion_smoke.stderr
echo "--- candidates ---"
python3 -c "import json; d=json.load(open('/tmp/notion_smoke.json')); print('fetched_total:', d['fetched_total']); print('after_dedup:', d['after_dedup']); print('first cand:', d['candidates'][0]['title'] if d['candidates'] else 'NONE')"
```

Expected:
- stderr: `[fetch] parent has N child pages` 라인 + `LIMIT=1 reached` 라인
- stdout JSON에 candidates[0]에 page_id/title/doi/slug_candidate/notion_body 키 존재
- `notion_body`에 노션 4-섹션 (논문 정보 / 한 줄 요약 / 과제 관련성 / 주요 결과) 텍스트가 평문 markdown으로 들어가야 함

만약 `fetched_total: 0`이면 integration이 부모 페이지에 공유 안 됨 → user 안내.

- [ ] **Step 2.8: Commit Task 2**

```bash
git add scripts/notion_sync/fetch_notion_pages.py
git commit -m "Notion sync: add fetch_notion_pages.py with 3-way dedup

Enumerates child pages of '참고 논문 및 아이디어' DB, extracts DOI/title/
year/notion-body, applies state/slug/DOI dedup, emits candidates JSON.

Co-Authored-By: Claude Opus 4.7 <noreply@anthropic.com>"
```

---

## Task 3: prompt.md — Claude Tier judge prompt

**Files:**
- Create: `scripts/notion_sync/prompt.md`

Claude CLI는 per-paper 1회 호출 — Tier 판단만 책임. PDF 다운로드/MD write는 Python.

- [ ] **Step 3.1: Write prompt.md**

Create `scripts/notion_sync/prompt.md`:

```markdown
# Per-paper Tier Judgment Prompt

You receive ONE Notion page candidate (title, journal, year, DOI, notion_body).
Your ONLY job: emit strict JSON for the user's Cancer Multiomics ("한미암")
project Tier classification.

The criteria are in your system prompt
(`wiki/_meta/han-mi-am-project-context.md`). Do NOT search externally.
Do NOT call tools. Do NOT write files. Output ONE line of JSON only.

## Tier Definitions (from system prompt)

- **Tier 1** — Phospho × drug resistance × cancer, ppQTL, kinase × targeted therapy
- **Tier 2** — pQTL/proteogenomics × WGS, neoantigen, CPTAC, basket trial, AI drug response
- **Tier 3** — WGS SV, noncoding driver, tumor heterogeneity, PTM crosstalk methods, multi-omics cohort
- **Tier 0** — animal/cell-line only, non-cancer, abstract-only, off-topic

## Output Schema (strict)

```json
{"tier": 1, "reason": "<one-sentence justification grounded in the title/notion_body>", "paper_kind": "translational"}
```

Allowed `paper_kind` values (controlled vocab from
`wiki/_meta/paper-frontmatter-schema.md`):
`trial | translational | mechanistic | computational | review | resource`

If `paper_kind` cannot be inferred from title/notion_body, default to
`computational`.

## Rules (from feedback_paper_relevance_writing.md — STRICT)

- Tier 판단은 system prompt(한미암 context) 기준만 사용. 외부 지식·웹 검색 금지.
- 뇌피셜 금지. "이렇게 쓸 수 있을 것 같다"식 추론 금지.
- 평가어("최고", "ROI 최고", "step-change", "credible follow-up", "white space") 사용 금지.
- `reason`은 노션 메모 본문에 명시된 사실에 기반한 한 문장으로만.
- 노션 메모의 "과제 관련성 (한미암)" 섹션 문장을 그대로 옮기지 말 것 — 사용자 본인의 사전 추론이지 논문 본문이 아님.

## Output Format Rules

- 응답은 **JSON 한 줄만**. 설명 문장·markdown fence·prefix/suffix 텍스트 금지.
- JSON 파싱 실패하면 Python에서 exit 2 → 그 candidate는 다음 cron에서 재시도됨.

## Input

다음 줄부터 candidate JSON이 stdin으로 들어옴. 그 candidate만 보고 위 schema에 맞춰 한 줄 응답해라.

---
```

- [ ] **Step 3.2: Commit Task 3**

```bash
git add scripts/notion_sync/prompt.md
git commit -m "Notion sync: add Claude Tier judge prompt (strict JSON output)

Co-Authored-By: Claude Opus 4.7 <noreply@anthropic.com>"
```

---

## Task 4: sync_papers.py — per-candidate orchestrator

**Files:**
- Create: `scripts/notion_sync/sync_papers.py`

각 candidate 1편씩 처리: claude judge → Tier 0/3 marking 또는 Tier 1/2 PDF+MD. **Incremental state flush** — 다음 candidate 처리 전 disk reflect.

- [ ] **Step 4.1: Write sync_papers.py — imports + state I/O**

Create `scripts/notion_sync/sync_papers.py`:

```python
#!/usr/bin/env python3
"""Per-candidate orchestrator for Notion → wiki sync.

Reads candidates JSON from arg1, runs claude Tier judge per candidate,
downloads PDF for Tier 1/2, writes stub MD for Tier 1/2, marks Tier 0/3
in state only. Incremental flush after each candidate.

Env vars:
  LIMIT             optional, cap on candidates processed
  ONLY_PAGE_ID      optional, restrict to one page (debug)
  DRY_RUN           optional, skip claude/PDF/MD writes (state untouched)
"""
import datetime
import json
import os
import re
import subprocess
import sys
import tempfile
import traceback
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(Path(__file__).resolve().parent))
import pdf_resolver  # noqa: E402

STATE_PATH = REPO / "wiki/_meta/notion-synced.json"
LOG_PATH = REPO / "wiki/_meta/log.md"
SOURCES_DIR = REPO / "wiki/sources"
PDF_DIR = REPO / "raw/inbox/papers"
CTX_PATH = REPO / "wiki/_meta/han-mi-am-project-context.md"
PROMPT_PATH = REPO / "scripts/notion_sync/prompt.md"


def now_iso():
    return datetime.datetime.now().astimezone().isoformat(timespec="seconds")


def load_state():
    if not STATE_PATH.exists():
        return {"last_run": None, "synced": [], "history": []}
    return json.loads(STATE_PATH.read_text())


def flush_state(state):
    """Atomic write — write to tmp then rename."""
    STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    tmp = STATE_PATH.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(state, ensure_ascii=False, indent=2))
    tmp.replace(STATE_PATH)


def append_state_entry(state, entry):
    state.setdefault("synced", []).append(entry)
    state["last_run"] = now_iso()
    flush_state(state)
```

- [ ] **Step 4.2: Add claude judge invocation + JSON parser**

Append to `sync_papers.py`:

```python
def run_claude_judge(cand):
    """Invoke claude CLI per-candidate. Returns parsed JSON dict."""
    if not PROMPT_PATH.exists():
        raise FileNotFoundError(PROMPT_PATH)
    if not CTX_PATH.exists():
        raise FileNotFoundError(CTX_PATH)

    prompt = PROMPT_PATH.read_text()
    ctx = CTX_PATH.read_text()

    # Pass candidate as stdin (the prompt expects it after "---" line).
    cand_for_judge = {
        "page_id": cand["page_id"],
        "title": cand["title"],
        "doi": cand["doi"],
        "year": cand["year"],
        "journal": cand.get("journal", ""),
        "notion_body": cand["notion_body"],
    }
    full_prompt = prompt + "\n\n" + json.dumps(cand_for_judge, ensure_ascii=False)

    proc = subprocess.run(
        ["claude", "-p", full_prompt,
         "--append-system-prompt", ctx,
         "--allowed-tools", "Read"],
        capture_output=True,
        text=True,
        timeout=180,
    )
    if proc.returncode != 0:
        raise RuntimeError(f"claude exit {proc.returncode}: {proc.stderr[:500]}")

    out = proc.stdout.strip()
    # Strip code fences if claude wrapped anyway.
    out = re.sub(r"^```(?:json)?\s*", "", out)
    out = re.sub(r"\s*```$", "", out)
    # Take first valid JSON object line.
    for line in out.splitlines():
        line = line.strip()
        if line.startswith("{") and line.endswith("}"):
            return json.loads(line)
    # Fallback: parse the whole stripped output.
    return json.loads(out)
```

- [ ] **Step 4.3: Add stub MD writer**

Append to `sync_papers.py`:

```python
def yaml_quote(s):
    """Quote a string for safe YAML scalar embedding."""
    if s is None:
        return '""'
    s = str(s).replace('"', '\\"')
    return f'"{s}"'


def write_stub_md(cand, judgment, pdf_status, pdf_path, pdf_attempts):
    """Write wiki/sources/<slug>.md stub. Only called for Tier 1/2."""
    slug = cand["slug_candidate"]
    out_path = SOURCES_DIR / f"{slug}.md"
    out_path.parent.mkdir(parents=True, exist_ok=True)

    today = datetime.date.today().isoformat()
    paper_kind = judgment.get("paper_kind", "computational")
    tier = judgment["tier"]

    fm_lines = [
        "---",
        f"title: {yaml_quote(cand['title'])}",
        "authors:",
        f"  - {yaml_quote(cand['first_author_last'].capitalize())}",
        f"year: {cand['year']}",
        f"journal: {yaml_quote(cand.get('journal') or '')}",
        f"doi: {yaml_quote(cand['doi'])}",
        f"url: {yaml_quote('https://doi.org/' + cand['doi'])}",
    ]
    if pdf_status == "downloaded" and pdf_path:
        rel = str(Path(pdf_path).relative_to(REPO))
        fm_lines.append(f"pdf: {yaml_quote(rel)}")
    elif pdf_status in ("manual", "pending"):
        fm_lines.append(f"pdf_status: {pdf_status}")
        if pdf_attempts:
            fm_lines.append("pdf_attempts:")
            for a in pdf_attempts:
                fm_lines.append(f"  - src: {yaml_quote(a['src'])}")
                fm_lines.append(f"    ok: {str(a['ok']).lower()}")
                fm_lines.append(f"    msg: {yaml_quote(a['msg'])}")

    fm_lines += [
        f"paper_kind: {paper_kind}",
        "cancer_types: []",
        "modalities: []",
        "themes:",
        "  - cancer-multiomics",
        "tags:",
        "  - source",
        "  - cancer-multiomics",
        "  - notion-sync",
        f"  - tier-{tier}",
        "topic: cancer-multiomics-literature",
        f"notion_url: {yaml_quote(cand['notion_url'])}",
        f"notion_page_id: {yaml_quote(cand['page_id'])}",
        "ingest_via: notion-sync-cron",
        f"ingest_date: {today}",
        "---",
        "",
    ]

    # Indent notion_body as blockquote.
    quoted_body = "\n".join(
        ("> " + line if line.strip() else ">")
        for line in cand["notion_body"].splitlines()
    )

    if pdf_status == "downloaded":
        local_pdf_line = f"- Local PDF: `{Path(pdf_path).relative_to(REPO)}`"
    else:
        local_pdf_line = "- Local PDF: pending (manual queue) — `pdf_attempts` frontmatter 참고"

    body_lines = [
        f"# {cand['title']}",
        "",
        f"_{cand.get('journal') or '<journal pending>'}, {cand['year']}._ "
        f"DOI: [{cand['doi']}](https://doi.org/{cand['doi']})",
        "",
        "## Summary",
        "",
        "_Awaiting deep-dive._",
        "",
        "## Key Points",
        "",
        "- _Awaiting deep-dive._",
        "",
        "## Methods",
        "",
        "- _Awaiting deep-dive._",
        "",
        "## Cancer Multiomics Project Relevance",
        "",
        "_Awaiting deep-dive._ (자동화는 Tier 분류만 수행; 적용 시나리오는 사용자 정독 후 작성. "
        "노션 메모의 '과제 관련성' 섹션을 여기로 복사 금지.)",
        "",
        "## Notion Notes",
        "",
        f"_사용자 노션 메모 (출처: [{cand['notion_url']}]({cand['notion_url']})):_",
        "",
        quoted_body,
        "",
        "## Connections",
        "",
        "- [Cancer Multiomics Proteogenomic Atlas](../topics/cancer-multiomics-literature.md)",
        "",
        "## Sources",
        "",
        local_pdf_line,
        f"- Notion: {cand['notion_url']}",
        f"- DOI: <https://doi.org/{cand['doi']}>",
        "",
    ]

    out_path.write_text("\n".join(fm_lines + body_lines))
    return out_path
```

- [ ] **Step 4.4: Add log appender + main loop**

Append to `sync_papers.py`:

```python
def append_log_md(summary):
    """One-line entry in wiki/_meta/log.md."""
    date = datetime.date.today().isoformat()
    line = (
        f"- {date} — Notion sync: {summary['after_dedup']} candidates, "
        f"Tier 1/2={summary['tier_1']+summary['tier_2']}, "
        f"Tier 0/3 skipped={summary['tier_0_skipped']+summary['tier_3_skipped']}, "
        f"PDF downloaded={summary['pdf_downloaded']}, manual={summary['pdf_manual']}"
    )
    with open(LOG_PATH, "a") as f:
        f.write(line + "\n")


def main():
    if len(sys.argv) < 2:
        print("usage: sync_papers.py <candidates.json>", file=sys.stderr)
        sys.exit(1)
    candidates_path = Path(sys.argv[1])
    if not candidates_path.exists():
        print(f"ERROR: {candidates_path} not found", file=sys.stderr)
        sys.exit(1)

    data = json.loads(candidates_path.read_text())
    candidates = data.get("candidates", [])
    only = os.environ.get("ONLY_PAGE_ID")
    limit = int(os.environ.get("LIMIT", "0"))
    dry_run = os.environ.get("DRY_RUN") == "1"

    state = load_state()
    summary = {
        "date": datetime.date.today().isoformat(),
        "candidates_fetched": len(candidates),
        "tier_1": 0, "tier_2": 0,
        "tier_3_skipped": 0, "tier_0_skipped": 0,
        "pdf_downloaded": 0, "pdf_manual": 0,
        "errors": 0,
    }

    processed = 0
    for cand in candidates:
        if only and cand["page_id"] != only:
            continue
        if limit and processed >= limit:
            print(f"[sync] LIMIT={limit} reached", file=sys.stderr)
            break
        processed += 1

        print(f"[sync] {cand['page_id'][:8]} — {cand['title'][:60]}",
              file=sys.stderr)

        try:
            if dry_run:
                print("  [DRY_RUN] skipping claude/PDF/MD", file=sys.stderr)
                continue

            judgment = run_claude_judge(cand)
            tier = int(judgment["tier"])
            reason = judgment.get("reason", "")
            paper_kind = judgment.get("paper_kind", "computational")
            print(f"  Tier {tier}: {reason[:80]}", file=sys.stderr)

            entry_base = {
                "page_id": cand["page_id"],
                "synced_at": now_iso(),
                "tier": tier,
                "tier_reason": reason,
                "paper_kind": paper_kind,
                "doi": cand["doi"],
            }

            if tier in (0, 3):
                entry = {**entry_base, "skipped": True}
                append_state_entry(state, entry)
                summary[f"tier_{tier}_skipped"] += 1
                continue

            # Tier 1/2 → PDF + stub MD
            pdf_result = pdf_resolver.resolve_with_doi(cand, PDF_DIR)
            if pdf_result.get("downloaded"):
                pdf_status = "downloaded"
                pdf_path = pdf_result["pdf_path"]
                summary["pdf_downloaded"] += 1
            else:
                pdf_status = "manual"
                pdf_path = None
                summary["pdf_manual"] += 1
            pdf_attempts = pdf_result.get("tried", [])

            md_path = write_stub_md(cand, judgment, pdf_status, pdf_path, pdf_attempts)
            print(f"  Wrote stub: {md_path.relative_to(REPO)}", file=sys.stderr)

            entry = {
                **entry_base,
                "slug": cand["slug_candidate"],
                "pdf_status": pdf_status,
                "pdf_via": pdf_result.get("via"),
            }
            if pdf_status == "manual":
                entry["pdf_attempts"] = pdf_attempts
            append_state_entry(state, entry)
            summary[f"tier_{tier}"] += 1

        except Exception as e:
            print(f"  ERROR: {e}", file=sys.stderr)
            traceback.print_exc(file=sys.stderr)
            summary["errors"] += 1
            # Do NOT flush state for this candidate — next cron retries.

    # History entry + log.md (only if not dry_run, so state stays untouched).
    if not dry_run:
        state.setdefault("history", []).append(summary)
        flush_state(state)
        try:
            append_log_md(summary)
        except Exception as e:
            print(f"WARN: log.md append failed: {e}", file=sys.stderr)

    json.dump(summary, sys.stdout, ensure_ascii=False, indent=2)
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()
```

- [ ] **Step 4.5: Smoke test with DRY_RUN against fixture**

Build a minimal fixture (no Notion call needed):

```bash
cat > /tmp/notion_fixture.json <<'EOF'
{
  "date": "2026-05-14",
  "parent_page_id": "344302d9-c598-8188-8a05-d5041134fb3d",
  "synced_count": 0,
  "fetched_total": 1,
  "after_dedup": 1,
  "skipped": {"already_synced": 0, "slug_collision": 0, "doi_collision": 0, "no_doi": 0, "filter": 0},
  "candidates": [
    {
      "page_id": "test-page-0001",
      "title": "Smoke 2026 — Fixture for sync_papers DRY_RUN",
      "doi": "10.9999/fixture",
      "first_author_last": "smoke",
      "year": 2026,
      "journal": "",
      "slug_candidate": "smoke-2026-fixture-sync-papers-dry-run",
      "notion_url": "https://www.notion.so/test-page-0001",
      "notion_body": "## 논문 정보\nSmoke fixture\n## 한 줄 요약\nFixture\n## 과제 관련성 (한미암)\nN/A\n## 주요 결과\nN/A"
    }
  ]
}
EOF

DRY_RUN=1 python3 scripts/notion_sync/sync_papers.py /tmp/notion_fixture.json
```

Expected:
- stderr: `[sync] test-pag — Smoke 2026 ...` 그리고 `[DRY_RUN] skipping...`
- stdout: summary JSON with `tier_1: 0, ..., errors: 0`
- Wiki/sources/, state file 모두 변경 없음

- [ ] **Step 4.6: Smoke test write_stub_md isolated**

Quick check that write_stub_md generates valid frontmatter:

```bash
python3 - <<'EOF'
import sys, json
sys.path.insert(0, "scripts/notion_sync")
from sync_papers import write_stub_md
cand = {
    "page_id": "test-0001",
    "title": "Smoke 2026 — Stub MD generation test",
    "doi": "10.9999/fixture",
    "first_author_last": "smoke",
    "year": 2026,
    "journal": "Test Journal",
    "slug_candidate": "smoke-2026-stub-md-generation-test",
    "notion_url": "https://www.notion.so/test-0001",
    "notion_body": "## 논문 정보\n저자: Smoke et al.\n## 한 줄 요약\nfixture only"
}
judgment = {"tier": 1, "reason": "fixture", "paper_kind": "computational"}
p = write_stub_md(cand, judgment, "manual", None,
                  [{"src": "europepmc", "ok": False, "msg": "no PMID"}])
print("Wrote:", p)
print(p.read_text())
EOF
```

Expected: valid markdown출력. Frontmatter section에 `tier-1`, `notion-sync` tag, `pdf_status: manual`, `pdf_attempts:` list 포함. 검토 후:

```bash
rm wiki/sources/smoke-2026-stub-md-generation-test.md
```

- [ ] **Step 4.7: Commit Task 4**

```bash
git add scripts/notion_sync/sync_papers.py
git commit -m "Notion sync: add sync_papers.py per-candidate orchestrator

Runs claude Tier judge per candidate, handles Tier 0/3 skip path and
Tier 1/2 PDF+stub-MD path. Incremental state flush, partial-failure
isolated per candidate via try/except.

Co-Authored-By: Claude Opus 4.7 <noreply@anthropic.com>"
```

---

## Task 5: run.sh — cron orchestrator

**Files:**
- Create: `scripts/notion_sync/run.sh`

기존 `scripts/daily_digest/run.sh`와 평행한 구조. 5단계 (pull → fetch → sync → commit → push).

- [ ] **Step 5.1: Write run.sh**

Create `scripts/notion_sync/run.sh`:

```bash
#!/usr/bin/env bash
# Notion → Wiki sync — runs daily via cron.
#
# Stages:
#   1) git pull --rebase --autostash
#   2) python fetch_notion_pages.py → /tmp/notion_candidates_<date>.json
#   3) python sync_papers.py → wiki/sources/, raw/inbox/papers/, state
#   4) git add + commit
#   5) git push
#
# Env vars:
#   DRY_RUN=1         fetch only, skip claude/PDF/MD writes
#   LIMIT=N           cap candidates processed
#   ONLY_PAGE_ID=...  single-page debug mode

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
cd "$REPO_ROOT"

LOG_DIR="$REPO_ROOT/logs"
mkdir -p "$LOG_DIR"
TODAY="$(date +%F)"
LOG_FILE="$LOG_DIR/notion-sync-$TODAY.log"

exec > >(tee -a "$LOG_FILE") 2>&1

echo "================================================================"
echo "Notion sync run @ $(date -Iseconds)"
echo "Repo: $REPO_ROOT"
echo "DRY_RUN=${DRY_RUN:-0} LIMIT=${LIMIT:-0} ONLY_PAGE_ID=${ONLY_PAGE_ID:-}"
echo "================================================================"

# [1/5] sync latest wiki
echo "[1/5] Pulling latest wiki..."
git pull --quiet --rebase --autostash origin main || {
    echo "WARN: rebase pull failed; trying merge"
    git pull --quiet --no-rebase origin main || echo "WARN: pull still failed; continuing"
}

# [2/5] fetch candidates from Notion
echo "[2/5] Fetching Notion candidates..."
CANDIDATES_JSON="/tmp/notion_candidates_$TODAY.json"
set +e
python3 "$SCRIPT_DIR/fetch_notion_pages.py" > "$CANDIDATES_JSON" 2> "$LOG_DIR/notion-fetch-$TODAY.stderr"
FETCH_RC=$?
set -e
cat "$LOG_DIR/notion-fetch-$TODAY.stderr"
if [ "$FETCH_RC" -ne 0 ]; then
    echo "ERROR: fetch_notion_pages exited $FETCH_RC"
    exit 2
fi
CAND_COUNT=$(python3 -c "import json; print(len(json.load(open('$CANDIDATES_JSON'))['candidates']))" 2>/dev/null || echo 0)
echo "    Candidates after dedup: $CAND_COUNT"

if [ "$CAND_COUNT" -eq 0 ]; then
    echo "    Nothing to sync. Exiting."
    exit 0
fi

# [3/5] per-candidate sync
echo "[3/5] Syncing candidates..."
DRY_RUN="${DRY_RUN:-0}" LIMIT="${LIMIT:-0}" ONLY_PAGE_ID="${ONLY_PAGE_ID:-}" \
    python3 "$SCRIPT_DIR/sync_papers.py" "$CANDIDATES_JSON" || {
        echo "ERROR: sync_papers exited $?"
        exit 3
    }

if [ "${DRY_RUN:-0}" = "1" ]; then
    echo "[DRY_RUN=1] Stopping before commit/push."
    exit 0
fi

# [4/5] commit
echo "[4/5] Committing wiki changes..."
git add wiki/sources/ wiki/_meta/notion-synced.json wiki/_meta/log.md raw/inbox/papers/ 2>/dev/null || true
if ! git diff --cached --quiet; then
    git -c user.email="notion-sync-bot@noreply" -c user.name="notion-sync-bot" \
        commit -m "Notion sync: $TODAY ($CAND_COUNT candidates)" --quiet
    echo "    Committed."
else
    echo "    No changes to commit."
fi

# [5/5] push
echo "[5/5] Pushing..."
git push --quiet origin main || echo "WARN: push failed; will retry next run"

echo "================================================================"
echo "Done @ $(date -Iseconds)"
echo "================================================================"
```

- [ ] **Step 5.2: chmod +x and DRY_RUN smoke test**

```bash
chmod +x scripts/notion_sync/run.sh
source ~/.paperatlas.env
DRY_RUN=1 LIMIT=1 bash scripts/notion_sync/run.sh 2>&1 | tail -30
```

Expected:
- `[1/5] Pulling latest wiki...` 단계 OK
- `[2/5] Fetching Notion candidates...` 후 candidates JSON 생성, `Candidates after dedup: N`
- `[3/5] Syncing candidates...` 후 `[DRY_RUN] skipping...` 라인
- `[DRY_RUN=1] Stopping before commit/push.` 라인으로 종료, exit 0
- `git status` 확인: untracked 파일 없음 (state·MD·PDF 변경 없음)

- [ ] **Step 5.3: Commit Task 5**

```bash
git add scripts/notion_sync/run.sh
git commit -m "Notion sync: add run.sh cron orchestrator

5-stage pipeline (pull → fetch → sync → commit → push). DRY_RUN/LIMIT/
ONLY_PAGE_ID env-var driven, mirrors daily_digest/run.sh patterns.

Co-Authored-By: Claude Opus 4.7 <noreply@anthropic.com>"
```

---

## Task 6: cron_entry.sh — env wrapper

**Files:**
- Create: `scripts/notion_sync/cron_entry.sh`

Cron의 minimal env에서 conda·PATH·SSH key·NOTION_API_KEY 로드.

- [ ] **Step 6.1: Write cron_entry.sh**

Create `scripts/notion_sync/cron_entry.sh`:

```bash
#!/usr/bin/env bash
# Cron wrapper — loads conda + PATH + SSH key + NOTION_API_KEY, then calls run.sh.
#
# Install (daily 09:00 KST — separate entry from daily_digest):
#   crontab -e
#   0 9 * * * /home/hejeong/Dropbox/llm-wiki/scripts/notion_sync/cron_entry.sh >> /home/hejeong/Dropbox/llm-wiki/logs/notion-sync-cron-wrapper.log 2>&1

set -o pipefail
# Do NOT enable `set -u` — conda.sh references unset vars (matches daily_digest pattern).

# 1. Conda (so python3 + notion-client work)
for p in "$HOME/anaconda3" "$HOME/miniconda3" "$HOME/miniforge3" "/opt/anaconda3" "/opt/miniconda3" "/opt/conda"; do
    if [ -f "$p/etc/profile.d/conda.sh" ]; then
        echo "[cron_entry] sourcing conda from $p" >&2
        # shellcheck disable=SC1091
        source "$p/etc/profile.d/conda.sh"
        conda activate base 2>/dev/null || true
        break
    fi
done

# 2. PATH — claude CLI typically in ~/.local/bin or /usr/local/bin
export PATH="$HOME/.local/bin:/usr/local/bin:/usr/bin:/bin:$PATH"

# 3. SSH key for git push
export GIT_SSH_COMMAND="ssh -i $HOME/.ssh/id_ed25519 -o StrictHostKeyChecking=no"

# 4. Load NOTION_API_KEY (+ any other secrets) from ~/.paperatlas.env
if [ -f "$HOME/.paperatlas.env" ]; then
    # shellcheck disable=SC1091
    source "$HOME/.paperatlas.env"
fi

# 5. Run
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
cd "$REPO_ROOT" || exit 1

echo "[cron_entry] launching run.sh from $REPO_ROOT" >&2

DRY_RUN="${DRY_RUN:-0}" LIMIT="${LIMIT:-0}" ONLY_PAGE_ID="${ONLY_PAGE_ID:-}" \
    bash "$SCRIPT_DIR/run.sh"
```

- [ ] **Step 6.2: chmod +x and smoke test (DRY_RUN, no env)**

Cron-like minimal env simulation:

```bash
chmod +x scripts/notion_sync/cron_entry.sh
env -i HOME="$HOME" DRY_RUN=1 LIMIT=1 bash scripts/notion_sync/cron_entry.sh 2>&1 | tail -20
```

Expected:
- `[cron_entry] sourcing conda from /home/hejeong/anaconda3` 라인
- `[cron_entry] launching run.sh from /home/hejeong/Dropbox/llm-wiki` 라인
- run.sh의 `[1/5]` ... `[DRY_RUN=1] Stopping before commit/push.` 정상 흐름

만약 NOTION_API_KEY 없어 fetch_notion_pages가 exit 1하면 `[2/5]` 단계 실패 — `.paperatlas.env`에 키가 있는지 확인.

- [ ] **Step 6.3: Commit Task 6**

```bash
git add scripts/notion_sync/cron_entry.sh
git commit -m "Notion sync: add cron_entry.sh wrapper

Loads conda + PATH + GIT_SSH_COMMAND + ~/.paperatlas.env (for
NOTION_API_KEY) before invoking run.sh. Mirrors daily_digest pattern.

Co-Authored-By: Claude Opus 4.7 <noreply@anthropic.com>"
```

---

## Task 7: Initial backlog dry run + small real run

**Files:** None (operational)

상태: 모든 스크립트 작성 완료. 노션 전체 백로그 (~50편)를 점진 처리.

- [ ] **Step 7.1: Full DRY_RUN — verify dedup + fetch shape**

```bash
source ~/.paperatlas.env
DRY_RUN=1 bash scripts/notion_sync/run.sh 2>&1 | tail -40
```

Expected:
- `Candidates after dedup: N` (보통 30~50, 첫 실행은 백로그 다)
- skipped 분포 (already_synced=0, slug_collision=?, doi_collision=?, no_doi=?)
- 모든 candidate에 대해 `[DRY_RUN] skipping...`
- 종료 후 git status 깨끗

확인 포인트:
1. `cat /tmp/notion_candidates_$(date +%F).json | python3 -c "import json,sys; d=json.load(sys.stdin); [print(c['page_id'][:8], c['title'][:60], c['doi']) for c in d['candidates'][:10]]"`
2. DOI 없는 페이지 수가 비정상적으로 많으면 노션에 DOI property/본문 정리 필요

- [ ] **Step 7.2: Real LIMIT=2 run on backlog**

```bash
LIMIT=2 bash scripts/notion_sync/run.sh 2>&1 | tail -50
```

Expected:
- 2개 candidate 처리. 각 candidate별 stderr 라인:
  - `[sync] <8-char id> — <title>`
  - `  Tier <n>: <reason>`
  - (Tier 1/2면) `  Wrote stub: wiki/sources/...md`
- 4/5 단계: `Committed.`
- 5/5: push 성공 또는 WARN
- `git log --oneline -5` 에 새 커밋 보임
- `cat wiki/_meta/notion-synced.json | python3 -m json.tool | head -40` 으로 state 점검 — `synced` 배열에 2개 entry

검증 체크리스트:
```bash
# State 일관성
jq '.synced | length' wiki/_meta/notion-synced.json
# wiki/sources에 생성된 새 파일 (Tier 1/2만)
git log -1 --name-only | grep wiki/sources/
# PDF 다운로드 결과
ls -la raw/inbox/papers/ | tail -10
```

- [ ] **Step 7.3: 결과 검토 + 사용자 확인 게이트**

생성된 새 wiki/sources/*.md 페이지 1편 정독:
- Frontmatter: `tier-N`, `paper_kind`, `doi`, `notion_url` OK?
- Body: "Awaiting deep-dive" placeholder만 있어야 함 (자동화는 본문 추론 안 함)
- "Notion Notes" 섹션에 노션 4-섹션이 blockquote로 들어가야 함
- "Cancer Multiomics Project Relevance" 섹션은 placeholder만 — 노션 "과제 관련성" 텍스트가 여기 복사돼있으면 BUG

문제 있으면 PR 형태로 분리 수정. OK면 다음 step.

- [ ] **Step 7.4: 백로그 전량 처리**

```bash
bash scripts/notion_sync/run.sh 2>&1 | tail -50
```

LIMIT 제거. 백로그 잔여분 모두 처리. 대용량이면 (50편 처리에 ~30분) `nohup`으로 백그라운드 실행 권장:

```bash
nohup bash scripts/notion_sync/run.sh > /tmp/notion-bulk.log 2>&1 &
tail -f /tmp/notion-bulk.log
```

- [ ] **Step 7.5: 사후 검증**

```bash
# State 합계
jq '.history[-1]' wiki/_meta/notion-synced.json
# Tier 분포
jq '.synced | group_by(.tier) | map({tier: .[0].tier, n: length})' wiki/_meta/notion-synced.json
# PDF 다운로드율
jq '.synced | map(select(.pdf_status)) | group_by(.pdf_status) | map({status: .[0].pdf_status, n: length})' wiki/_meta/notion-synced.json
```

- Tier 0/3 비율이 70% 초과면 prompt.md 또는 한미암 context 보강 필요
- pdf_manual > pdf_downloaded이면 KU 쿠키 갱신 + retry

---

## Task 8: Cron registration

**Files:** None (crontab 수정)

- [ ] **Step 8.1: 현재 crontab 확인**

Run: `crontab -l`
Expected: 기존 daily_digest entry(`50 9 * * 3 STAGE=compose ...`, `59 9 * * 3 STAGE=post ...`) 보임. 기존 entry 손대지 말 것.

- [ ] **Step 8.2: 새 entry 추가**

`crontab -e`로 다음 한 줄 추가 (시간은 daily_digest와 충돌 없도록 09:00 KST, daily_digest는 09:50 시작):

```
# Notion → Wiki sync (daily 09:00 KST — separate from daily_digest)
0 9 * * * /home/hejeong/Dropbox/llm-wiki/scripts/notion_sync/cron_entry.sh >> /home/hejeong/Dropbox/llm-wiki/logs/notion-sync-cron-wrapper.log 2>&1
```

저장 후 확인:
```bash
crontab -l | grep notion-sync
```

- [ ] **Step 8.3: 다음날 cron 실행 확인**

다음날 09:01 에:
```bash
tail -50 logs/notion-sync-cron-wrapper.log
tail -50 logs/notion-sync-$(date +%F).log
```

기대 결과:
- `[cron_entry] launching run.sh ...` 라인
- 백로그 다 처리한 상태면 `Candidates after dedup: 0` → exit 0 (정상)
- 새 노션 추가분이 있으면 정상 처리 라인

---

## Implementation Order & Dependencies

```
Task 0 (env setup)  →  Task 1 (pdf_resolver)  →  Task 2 (fetch_notion_pages)
                                                          ↓
                                              Task 3 (prompt.md)
                                                          ↓
                                              Task 4 (sync_papers)
                                                          ↓
                                              Task 5 (run.sh)  →  Task 6 (cron_entry.sh)
                                                          ↓
                                              Task 7 (backlog)  →  Task 8 (cron register)
```

각 task는 단독으로 commit 가능. Task 1/2/3/4는 mock fixture로 smoke test 가능하므로 NOTION_API_KEY 없어도 진행 가능. Task 7부터 실제 Notion 호출 필요.

---

## Out of scope (re-affirmed from spec)

- 노션 페이지 수정 감지 (once-only 정책)
- 노션 4-섹션 본문 → wiki Summary/Methods 자동 변환 (source-grounding rule 위반)
- Slack/이메일 알림 (cron log 파일로 충분)
- Tier 3 페이지의 stub MD 생성 (사용자 결정 2026-05-14 — state marking only)
- 사용자 deep-read 자동화 (manual)
