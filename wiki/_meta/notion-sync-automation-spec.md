# Notion → Wiki Sync 자동화 Spec

**Created**: 2026-05-14
**Purpose**: Notion "참고 논문 및 아이디어" DB(`344302d9-c598-8188-8a05-d5041134fb3d`) 하위 페이지를 daily cron으로 자동 ingest.
**Related**: [Cancer Multiomics Ingest Plan](cancer-multiomics-ingest-plan.md) — 기존 manual Phase 1-6의 cron-automated 확장판. [Han-mi-am Project Context](han-mi-am-project-context.md) — Tier 1-3 기준.

---

## 사용자 합의 (브레인스토밍 결과)

1. **Trigger**: Daily cron, 기존 daily_digest와 **완전 분리** (디렉토리/state/cron entry 별도)
2. **Filter**: LLM 관련성 판단 — han-mi-am-project-context.md의 Tier 1-3 기준
3. **Ingest 깊이**: Stub frontmatter + PDF 다운로드 + Notion 4-섹션 본문을 `## Notion Notes` 섹션에 캡처(출처 표기). Summary/Key Points/Methods는 `_Awaiting deep-dive._` placeholder
4. **State**: page_id 기반 once-only. `wiki/_meta/notion-synced.json`

---

## Tier 처리 정책

| Tier | 정의 (han-mi-am-project-context.md) | 자동화 동작 |
|---|---|---|
| 1 | Phospho × drug resistance × cancer, ppQTL, kinase × targeted therapy | Stub MD + PDF 다운로드 + Notion Notes 캡처 |
| 2 | pQTL/proteogenomics × WGS, neoantigen, CPTAC, basket trial, AI drug response | Stub MD + PDF 다운로드 + Notion Notes 캡처 |
| 3 | WGS SV, noncoding driver, tumor heterogeneity, PTM crosstalk methods, multi-omics cohort | state에만 마킹 + skip (사용자 결정 2026-05-14) |
| 0 | 동물·세포주 only, 비암 질환, abstract only | state에만 마킹 + skip |

---

## 디렉토리 구조

```
scripts/notion_sync/                           # 신규
├── fetch_notion_pages.py                      # Notion API → candidates JSON (DOI 이중 dedup)
├── sync_papers.py                             # per-candidate orchestrator (claude judge + PDF + MD + incremental state)
├── pdf_resolver.py                            # DOI-first wrapper (resolve_pdf + ezproxy library import)
├── prompt.md                                  # Claude relevance judge 프롬프트 (per-paper)
└── run.sh                                     # cron orchestrator

wiki/_meta/notion-synced.json                  # 신규 state file
wiki/_meta/log.md                              # 기존 append-only log
wiki/sources/<slug>.md                         # 신규 stub pages
raw/inbox/papers/<slug>.pdf                    # 신규 PDF (Tier 1/2만)
logs/notion-sync-<date>.log                    # 신규 cron log
```

---

## Data flow

```
cron (daily)
  ↓
scripts/notion_sync/run.sh
  ├─ [1/5] git pull --rebase --autostash
  ├─ [2/5] python fetch_notion_pages.py > /tmp/notion_candidates_<date>.json
  │         · notion-synced.json 로드해 처리된 page_id 제외
  │         · 노션 부모 페이지 fetch → 자식 페이지 enumerate
  │         · 각 자식 fetch → DOI/title/authors/year/journal/notion_body 추출
  │         · DOI 없으면 skip + warn
  │         · Dedup (이중 체크):
  │             (a) wiki/sources/<slug>.md 존재 시 skip
  │             (b) wiki/sources/*.md 에서 `doi: "<doi>"` 매칭되면 skip
  │             — author-year 충돌(Zhang 2026 다편) 대비
  │         · env vars: LIMIT (처리 cap), ONLY_PAGE_ID (단일 page 디버그)
  ├─ [3/5] python sync_papers.py /tmp/notion_candidates_<date>.json
  │         · 각 candidate iterate (개별 try/except — 부분 실패 격리):
  │             1) claude -p로 1편 Tier 판단 호출
  │                (input: candidate JSON + han-mi-am-project-context.md;
  │                 output: {tier, reason, paper_kind})
  │             2) Tier 0 또는 Tier 3 → state에 {page_id, tier, reason, skipped:true} append, skip
  │             3) Tier 1/2 → PDF 다운로드 시도 (아래 PDF resolver 참고)
  │             4) Tier 1/2만 stub MD 생성 (Write)
  │             5) state JSON에 entry append (incremental flush — 다음 candidate 처리 전에 디스크 반영)
  │         · 마지막에 wiki/_meta/log.md 엔트리 append (한 줄)
  ├─ [4/5] git add wiki/sources/ wiki/_meta/notion-synced.json wiki/_meta/log.md raw/inbox/papers/
  └─ [5/5] git commit + push
```

**왜 [3/5]가 sync_papers.py로 wrapping되는가**:
- Per-candidate incremental state flush가 idempotency 보장 (중간 크래시해도 처리분만큼은 영구화)
- claude CLI는 1편 단위로 호출 (per-paper relevance judge만 LLM에 위임; PDF 다운로드/MD write는 Python이 담당)
- 부분 실패(특정 candidate에서 timeout)가 다른 candidate에 전염 안 됨

---

## fetch_notion_pages.py

**입력**: 없음 (Notion parent page ID는 코드 상수). 환경 변수: `NOTION_API_KEY` (필수), `LIMIT` (선택), `ONLY_PAGE_ID` (선택).

**구현**:
- Notion 공식 Python SDK `notion-client` 사용 (`pip install notion-client`). Notion integration token (`secret_...`) 발급 후 부모 페이지에 명시적 공유 필요.
- mcp__notion__notion-fetch는 Claude CLI에서만 호출 가능 — Python 스크립트는 SDK 사용.

**Dedup (이중 체크)**:
1. **State 체크**: `notion-synced.json`의 `synced[]`에 page_id가 있으면 skip
2. **Slug 체크**: `wiki/sources/<slug_candidate>.md` 존재하면 skip
3. **DOI 체크**: `wiki/sources/*.md` 전체 grep으로 `doi: "<doi>"` 또는 `doi: <doi>` 매칭되는 파일 있으면 skip
   - 이유: 슬러그 규칙이 변경되거나 같은 author-year 다른 키워드 조합(예: "Zhang 2026" 3편)으로 slug가 충돌 회피되어 다르게 생성될 수 있음. DOI는 unique identifier.

**출력 schema**:

```json
{
  "date": "2026-05-14",
  "parent_page_id": "344302d9-c598-8188-8a05-d5041134fb3d",
  "synced_count": 27,
  "fetched_total": 50,
  "after_dedup": 23,
  "skipped": {"already_synced": 27, "slug_collision": 0, "doi_collision": 0, "no_doi": 0},
  "candidates": [
    {
      "page_id": "35e302d9-c598-815f-8c4d-e8aecdfd83a9",
      "title": "Xu et al. 2026 — 중국인 HER2-low BC proteogenomics + lactylome",
      "doi": "10.xxxx/...",
      "first_author_last": "xu",
      "year": 2026,
      "journal": "Cancer Cell",
      "slug_candidate": "xu-2026-her2-low-breast-proteogenomics-lactylome",
      "notion_url": "https://www.notion.so/35e302d9...",
      "notion_body": "## 논문 정보\n...\n## 한 줄 요약\n...\n## 과제 관련성 (한미암)\n...\n## 주요 결과\n..."
    }
  ]
}
```

**DOI 추출 규칙**:
1. 우선 노션 페이지 properties에서 DOI 필드 확인 (해당 DB에 DOI property 있을 수 있음)
2. 없으면 본문 텍스트에서 정규식 `10\.\d{4,9}/[^\s<>"]+` 매칭 (첫 번째)
3. fragmented 링크(`href` 속성)도 시도
4. 그래도 없으면 candidate에서 제외 + log warning. state에는 마킹 안 함 (사용자가 노션에 DOI 추가 후 재실행 가능)

---

## pdf_resolver.py — DOI-first PDF wrapper

`scripts/ingest/resolve_pdf.py`는 title→PubMed PMID 검색에 의존 — DOI는 있지만 PMID 없는 2026 preprint나 비-PubMed 저널에서는 OA chain 자체가 실행되지 않음 (`result["doi"]`가 None 유지). 본 wrapper가 DOI-first 흐름 보장:

```python
# scripts/notion_sync/pdf_resolver.py (개요)
import sys
from pathlib import Path
REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO / "scripts/ingest"))
from resolve_pdf import (
    resolve_and_download, try_europepmc, try_unpaywall,
    try_doi_direct, try_elsevier, try_springer,
)
from ezproxy_download import load_cookies, make_opener, try_ezproxy_pdf

def resolve_with_doi(ref, out_dir):
    """ref: {slug, title, year, first_author_last, doi (required), pmcid (optional)}"""
    # 1) 기존 resolve_and_download 시도 (PMID hit하면 그대로)
    result = resolve_and_download(ref, out_dir)
    if result["downloaded"]:
        return result

    # 2) PMID 실패해도 ref["doi"]는 있음 → manual chain with seeded DOI
    out_path = out_dir / (ref["slug"] + ".pdf")
    for name, fn in [
        ("unpaywall-doi", lambda: try_unpaywall(ref["doi"], out_path)),
        ("doi-direct-doi", lambda: try_doi_direct(ref["doi"], result.get("journal"), out_path)),
        ("elsevier-doi", lambda: try_elsevier(ref["doi"], out_path)),
        ("springer-doi", lambda: try_springer(ref["doi"], out_path)),
    ]:
        ok, msg = fn()
        result["tried"].append({"src": name, "ok": ok, "msg": msg})
        if ok:
            result["downloaded"] = True
            result["pdf_path"] = str(out_path)
            result["via"] = f"{name}: {msg}"
            return result

    # 3) KU ezproxy fallback
    cookies = REPO / ".cookies/oca.cookies.txt"
    if cookies.exists():
        opener = make_opener(load_cookies(cookies))
        ok, info = try_ezproxy_pdf(opener, ref["doi"], out_path)
        result["tried"].append({"src": "ezproxy", "ok": ok, "msg": info})
        if ok:
            result["downloaded"] = True
            result["pdf_path"] = str(out_path)
            result["via"] = f"ezproxy: {info}"

    return result
```

`result["tried"]`는 stub frontmatter의 `pdf_attempts:` 필드에 그대로 보존됨 (사용자 진단용).

---

## sync_papers.py — per-candidate orchestrator

```python
# 의사 코드
candidates = json.load(open(sys.argv[1]))["candidates"]
state = load_state("wiki/_meta/notion-synced.json")
limit = int(os.environ.get("LIMIT", "0")) or len(candidates)
only = os.environ.get("ONLY_PAGE_ID")

for cand in candidates[:limit]:
    if only and cand["page_id"] != only:
        continue
    try:
        # 1) Claude 1회 호출 — Tier 판단만 (사이드이펙트 없음)
        judgment = run_claude_judge(cand)
        # judgment = {"tier": 1|2|3|0, "reason": "...", "paper_kind": "..."}

        # 2) Tier 0 또는 Tier 3 → state만 마킹, skip (stub MD/PDF 없음)
        if judgment["tier"] in (0, 3):
            entry = {"page_id": cand["page_id"], "tier": judgment["tier"],
                     "tier_reason": judgment["reason"], "skipped": True,
                     "synced_at": now()}
            append_state_entry_and_flush(state, entry)   # ← incremental flush
            continue

        # 3) Tier 1/2 → PDF 다운로드 시도
        pdf_result = pdf_resolver.resolve_with_doi(cand, Path("raw/inbox/papers"))
        if pdf_result["downloaded"]:
            pdf_status = "downloaded"
            pdf_path = pdf_result["pdf_path"]
        else:
            pdf_status = "manual"
            pdf_path = None
        pdf_attempts = pdf_result["tried"]

        # 4) Stub MD write (Tier 1/2만)
        write_stub_md(cand, judgment, pdf_status, pdf_path, pdf_attempts)

        # 5) Incremental state flush (CRITICAL — 부분실패 safe)
        entry = {"page_id": cand["page_id"], "tier": judgment["tier"],
                 "tier_reason": judgment["reason"],
                 "slug": cand["slug_candidate"], "doi": cand["doi"],
                 "pdf_status": pdf_status, "synced_at": now()}
        append_state_entry_and_flush(state, entry)
    except Exception as e:
        log_error(cand["page_id"], e)
        # 다음 candidate로 — 부분실패 격리

write_history_entry(state)
append_to_log_md(state)
```

---

## prompt.md — per-paper Tier judgment

`run_claude_judge()`가 candidate 1편마다 `claude -p` 호출. **출력만 책임, 사이드이펙트 없음**:

- system prompt: `wiki/_meta/han-mi-am-project-context.md` (via `--append-system-prompt`)
- user prompt: `prompt.md` + candidate 1편 (title, journal, year, doi, notion_body)
- 응답은 strict JSON 한 줄:
  ```json
  {"tier": 1, "reason": "<한 문장 Tier 근거>", "paper_kind": "computational"}
  ```
- `paper_kind`: controlled vocab만 — `trial | translational | mechanistic | computational | review | resource`. notion_body로 추정 가능한 카테고리만 사용 (PDF 정독 없음). 추정 불가시 `computational` default.

**Strict rules** (feedback_paper_relevance_writing.md):
- Tier 판단은 system prompt 기준만 사용 — 외부 지식 적용 금지
- 노션의 "과제 관련성 (한미암)" 섹션 문장을 wiki Project Relevance 섹션으로 **절대 복사 금지** (사용자 본인 추론이지 논문 본문이 아님)
- Wiki Project Relevance는 항상 `_Awaiting deep-dive._` placeholder 유지
- Summary/Key Points/Methods 모두 placeholder
- 평가어 ("최고", "ROI 최고", "step-change", "credible") 사용 금지

---

## Stub MD 구조

**적용 대상**: Tier 1/2만 stub MD 생성. Tier 0/3은 state에만 마킹 (wiki 파일 생성 없음).

**공통 frontmatter** (paper-frontmatter-schema.md 준수):

```yaml
---
title: "<full title>"
authors:
  - "<First Author>"
year: <int>
journal: "<journal>"
doi: "<doi>"
url: "https://doi.org/<doi>"
paper_kind: <trial|translational|mechanistic|computational|review|resource>
cancer_types: []           # deep-dive 시 채움
modalities: []             # deep-dive 시 채움
themes:
  - cancer-multiomics
tags:
  - source
  - cancer-multiomics
  - notion-sync
  - tier-<n>
topic: cancer-multiomics-literature
notion_url: "<url>"
notion_page_id: "<page_id>"
ingest_via: notion-sync-cron
ingest_date: <YYYY-MM-DD>
---
```

**PDF 필드** (Tier 1/2 stub MD에 추가):
- 다운로드 성공: `pdf: "raw/inbox/papers/<slug>.pdf"`, **`pdf_status` 필드 생략** (기존 ezproxy_download.py 동작과 일관)
- 다운로드 실패: `pdf_status: manual`, `pdf_attempts:` 리스트로 시도 내역 보존
- 다운로드 pending (예: dry-run 또는 future re-attempt): `pdf_status: pending` (정확히 이 문자열 — ku/ezproxy_download.py가 이걸로 스캔)

**본문 (Tier 1/2)**:

```markdown
# <Title>

_<journal>, <year>._ DOI: [<doi>](https://doi.org/<doi>)

## Summary

_Awaiting deep-dive._

## Key Points

- _Awaiting deep-dive._

## Methods

- _Awaiting deep-dive._

## Cancer Multiomics Project Relevance

_Awaiting deep-dive._ (자동화는 Tier 분류만 수행; 적용 시나리오는 사용자 정독 후 작성. **노션 메모의 "과제 관련성" 섹션을 여기로 복사 금지**)

## Notion Notes

_사용자 노션 메모 (출처: [<notion_url>](<notion_url>)):_

> <notion_body 전체 인용, blockquote 형식>

## Connections

- [Cancer Multiomics Literature Monitor](../topics/cancer-multiomics-literature.md)

## Sources

<다운로드 성공:>
- Local PDF: `raw/inbox/papers/<slug>.pdf`
<다운로드 실패:>
- Local PDF: pending (manual queue) — `pdf_attempts` frontmatter 참고

- Notion: <notion_url>
- DOI: <https://doi.org/<doi>>
```

---

## State file schema

`wiki/_meta/notion-synced.json` — **incremental flush** (매 candidate 처리 후 disk write):

```json
{
  "last_run": "2026-05-14T09:00:23+09:00",
  "synced": [
    {
      "page_id": "35e302d9-c598-815f-8c4d-e8aecdfd83a9",
      "synced_at": "2026-05-14T09:00:23+09:00",
      "slug": "xu-2026-her2-low-breast-proteogenomics-lactylome",
      "tier": 2,
      "tier_reason": "Chinese HER2-low BC proteogenomics + lactylome — Tier 2 (proteogenomics + WGS, basket-trial enabling)",
      "paper_kind": "translational",
      "pdf_status": "downloaded",
      "pdf_via": "ezproxy: ...",
      "doi": "10.xxxx/..."
    },
    {
      "page_id": "...",
      "synced_at": "2026-05-14T09:00:25+09:00",
      "slug": "lee-2026-korean-tnbc-nac-resistance-proteogenomics",
      "tier": 1,
      "tier_reason": "Korean TNBC NAC resistance proteogenomics — Tier 1 (phospho × drug resistance × human cancer)",
      "paper_kind": "translational",
      "pdf_status": "manual",
      "pdf_attempts": [
        {"src": "europepmc", "ok": false, "msg": "europepmc not-pdf (text/html)"},
        {"src": "unpaywall-doi", "ok": false, "msg": "unpaywall no oa"},
        {"src": "ezproxy", "ok": false, "msg": "ezproxy fetch err: HTTP 403"}
      ],
      "doi": "10.xxxx/..."
    },
    {
      "page_id": "350302d9-c598-8161-b259-ef033859244a",
      "synced_at": "2026-05-14T09:00:30+09:00",
      "tier": 0,
      "tier_reason": "Nextflow pipeline reproducibility review only, no human cancer data — Tier 0",
      "skipped": true
    },
    {
      "page_id": "351302d9-c598-8000-aaaa-bbbbccccdddd",
      "synced_at": "2026-05-14T09:00:32+09:00",
      "tier": 3,
      "tier_reason": "WGS SV review, supportive but not core — Tier 3",
      "skipped": true
    }
  ],
  "history": [
    {
      "date": "2026-05-14",
      "candidates_fetched": 23,
      "tier_1": 2, "tier_2": 8,
      "tier_3_skipped": 5, "tier_0_skipped": 8,
      "pdf_downloaded": 7, "pdf_manual": 3,
      "errors": 0
    }
  ]
}
```

**Flush 정책**:
- 매 candidate 처리 직후 (Tier 0 마킹 또는 stub MD write 직후) 전체 JSON을 임시 파일에 쓰고 atomic rename으로 교체
- Claude judge가 중간에 timeout / Python이 SIGTERM 받아도 이미 처리된 candidate는 영구화
- 다음 cron 실행 시 `synced[].page_id`에 있는 건 fetch_notion_pages.py가 자연 skip → idempotent

---

## Error handling

| 상황 | 처리 |
|---|---|
| `NOTION_API_KEY` 미설정 | exit 1, 사람 개입 필요 |
| Notion API rate limit | 1초 backoff + 3회 retry, 그래도 실패하면 exit 1 |
| 페이지에 DOI 없음 | candidates 제외, log warning ("page_id … : DOI missing") |
| Slug 중복 (wiki/sources/ 기존) | state에 `dedup_existing: true` 마킹, MD 안 건드림 |
| 모든 PDF source 실패 | stub MD는 생성, `pdf_status: manual` |
| KU 쿠키 만료/없음 | ezproxy skip, fallback chain만 시도 |
| Claude CLI exit non-zero | exit 2, 다음날 cron이 재시도 (state 기반 idempotent) |
| state JSON 손상 | exit 1, 사람 개입 (백업: git history) |

---

## Verification

1. **DRY_RUN**: `DRY_RUN=1 bash scripts/notion_sync/run.sh` → fetch JSON만 emit, Claude 호출 skip
2. **단일 페이지 테스트**: `ONLY_PAGE_ID=<id> bash run.sh` → 한 페이지만 처리
3. **State integrity**: `jq '.synced | length' wiki/_meta/notion-synced.json` ≥ `grep -l "ingest_via: notion-sync-cron" wiki/sources/*.md | wc -l`
4. **Tier 분포 sanity check**: history 배열 마지막 엔트리에서 `(tier_0_skipped + tier_3_skipped) > candidates_fetched * 0.7`이면 alert (Tier 판단이 과도하게 보수적인지 의심)
5. **PDF 실패율**: `pdf_manual / (pdf_downloaded + pdf_manual) > 0.5` 이면 KU 쿠키 점검 권유

---

## 초기 backlog 처리

첫 실행 시 noton-synced.json이 비어있어 노션의 모든 ~50편이 candidate로 잡힘. 안전 모드:

```bash
LIMIT=5 bash scripts/notion_sync/run.sh   # 처음 5편만 처리
```

사용자가 결과 검토 후 정상이면 `LIMIT` 제거하고 전체 처리. 이후 cron 등록.

---

## Cron entry (사용자 별도 등록)

```cron
# Notion → Wiki sync (daily 09:00 KST, daily_digest 10:00 이전)
0 9 * * * /home/hejeong/Dropbox/llm-wiki/scripts/notion_sync/run.sh >/dev/null 2>&1
```

(daily_digest의 `cron_entry.sh`와 별도 entry — 본 spec 합의사항)

---

## 사용자 액션 (구현 후 1회성)

1. `NOTION_API_KEY` 환경변수 설정 (Notion integration 생성 → 부모 페이지에 공유 → token을 `~/.paperatlas.env`에 추가)
2. 첫 실행은 `LIMIT=5` 안전 모드로 백로그 점진 처리
3. 결과 정상 확인 후 crontab 등록
4. KU 쿠키는 기존 daily_digest용 파일(`.cookies/oca.cookies.txt`) 공유 (별도 갱신 불필요)

---

## Out of scope

- 노션 페이지 수정 감지/재처리 (Once-only 정책)
- 노션 4-섹션 본문을 wiki Summary/Key Points로 자동 변환 (source-grounding rule 위반)
- Slack/이메일 알림 (cron 로그 파일로 충분)
- 관련 논문 citation graph 확장 (`find_related_via_openalex.py`의 역할)
- 사용자 deep-read (사용자 manual)
