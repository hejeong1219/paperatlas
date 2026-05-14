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
| 3 | WGS SV, noncoding driver, tumor heterogeneity, PTM crosstalk methods, multi-omics cohort | Stub MD + Notion Notes 캡처 (**PDF 다운로드 skip**) |
| 0 | 동물·세포주 only, 비암 질환, abstract only | state에만 마킹 + skip |

---

## 디렉토리 구조

```
scripts/notion_sync/                           # 신규
├── fetch_notion_pages.py                      # Notion API → candidates JSON
├── prompt.md                                  # Claude relevance judge + stub writer
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
  │         · wiki/sources/<slug>.md 존재 시 dedup (slug-only)
  ├─ [3/5] claude -p "$(cat prompt.md)" --append-system-prompt "$(cat han-mi-am-project-context.md)" --allowed-tools "Read,Write,Edit,Bash"
  │         · 각 candidate 마다:
  │           a) Tier 1-3 판단
  │           b) Tier 0 → state JSON에만 마킹
  │           c) Tier 1/2 → Bash로 PDF 다운로드 (resolve_pdf → ezproxy fallback) → stub MD Write
  │           d) Tier 3 → stub MD Write (PDF skip)
  │         · wiki/_meta/notion-synced.json 갱신
  │         · wiki/_meta/log.md 엔트리 append
  ├─ [4/5] git add wiki/sources/ wiki/_meta/notion-synced.json wiki/_meta/log.md
  └─ [5/5] git commit + push
```

---

## fetch_notion_pages.py 출력 schema

```json
{
  "date": "2026-05-14",
  "parent_page_id": "344302d9-c598-8188-8a05-d5041134fb3d",
  "synced_count": 27,
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

---

## prompt.md 골격

Claude CLI가 받는 instruction. 핵심:

1. `/tmp/notion_candidates_<date>.json` Read
2. 각 candidate마다:
   - **Tier 판단**: system prompt(`han-mi-am-project-context.md`)의 Tier 1-3 기준 적용. 1-2문장 reasoning을 state에 기록.
   - **Tier 0**: state JSON에 `{page_id, tier: 0, reason}` 추가, skip
   - **Tier 1/2**: Bash로 `python scripts/ingest/resolve_pdf.py` 시도 → 실패 시 `ezproxy_download.py` fallback. PDF 결과 무관 stub MD 생성. PDF 실패 시 `pdf_status: manual`.
   - **Tier 3**: PDF skip. stub MD 생성, `pdf_status: skipped_tier3`.
3. **Stub MD 구조** (Write):
   ```markdown
   ---
   title: "<full title>"
   authors: [<first>, ...]
   year: <int>
   journal: "<journal>"
   doi: "<doi>"
   url: "https://doi.org/<doi>"
   paper_kind: <auto-classify>
   topic: cancer-multiomics-literature
   tags: [source, cancer-multiomics, notion-sync, tier-<n>]
   notion_url: <url>
   notion_page_id: <page_id>
   pdf_status: <pending|manual|skipped_tier3>
   ingest_via: notion-sync-cron
   ingest_date: <YYYY-MM-DD>
   ---

   # <Title>

   _<journal>, <year>._ DOI: [<doi>](https://doi.org/<doi>)

   ## Summary

   _Awaiting deep-dive._

   ## Key Points

   - _Awaiting deep-dive._

   ## Methods

   - _Awaiting deep-dive._

   ## Cancer Multiomics Project Relevance

   - _Awaiting deep-dive._ (자동화는 Tier 분류만 수행; 실제 적용 시나리오는 사용자 정독 후 작성)

   ## Notion Notes

   _사용자 노션 메모 (출처: <notion_url>):_

   > <notion_body 전체 인용, blockquote 형식>

   ## Connections

   - [Cancer Multiomics Literature Monitor](../topics/cancer-multiomics-literature.md)

   ## Sources

   - Local PDF: `raw/inbox/papers/<slug>.pdf` (<pdf_status>)
   - Notion: <notion_url>
   - DOI: <https://doi.org/<doi>>
   ```
4. wiki/_meta/notion-synced.json 갱신 (Edit)
5. wiki/_meta/log.md에 한 줄 append (Edit)

**Strict rules** (feedback_paper_relevance_writing.md):
- Notion Notes는 인용만, 추가 narrative 금지
- Summary/Key Points는 절대 본문 추론으로 채우지 말 것 — placeholder 유지
- 평가어 ("최고", "ROI 최고", "step-change", "credible") 사용 금지
- 여러 논문 인위적 묶음 narrative 금지 (Connections는 단일 hub link만)

---

## State file schema

`wiki/_meta/notion-synced.json`:

```json
{
  "last_run": "2026-05-14T09:00:23+09:00",
  "synced": [
    {
      "page_id": "35e302d9-c598-815f-8c4d-e8aecdfd83a9",
      "synced_at": "2026-05-14T09:00:23+09:00",
      "slug": "xu-2026-her2-low-breast-proteogenomics-lactylome",
      "tier": 2,
      "tier_reason": "Chinese HER2-low BC proteogenomics + lactylome, Tier 2 (proteogenomics + cancer subtype)",
      "pdf_status": "downloaded",
      "doi": "10.xxxx/..."
    },
    {
      "page_id": "350302d9-c598-8161-b259-ef033859244a",
      "synced_at": "2026-05-14T09:00:23+09:00",
      "tier": 0,
      "tier_reason": "Nextflow pipeline review only, no human cancer data — Tier 0",
      "skipped": true
    }
  ],
  "history": [
    {
      "date": "2026-05-14",
      "candidates_fetched": 23,
      "tier_1": 2,
      "tier_2": 8,
      "tier_3": 5,
      "tier_0_skipped": 8,
      "pdf_downloaded": 7,
      "pdf_manual": 3
    }
  ]
}
```

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
4. **Tier 분포 sanity check**: history 배열 마지막 엔트리에서 `tier_0_skipped > candidates_fetched * 0.7`이면 alert (Tier 판단이 과도하게 보수적인지 의심)
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
