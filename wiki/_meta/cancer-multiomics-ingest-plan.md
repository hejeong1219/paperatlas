# Cancer Multiomics — Notion 참고논문 Ingest Plan

**Scope**: Notion "참고 논문 및 아이디어" 페이지 (`344302d9-c598-8188-8a05-d5041134fb3d`) 하위 27개 논문 중 `wiki/sources/`에 없는 것만 ingest. 추가로 각 신규 논문의 관련 논문(citation graph)도 발굴해 큐에 적재.

**Project tag**: `cancer-multiomics-literature` (기존 토픽 허브 활용)

---

## Phase 0 — Discovery (완료)

### 노션 측
- 27개 paper 서브페이지 + 1개 "old" placeholder (스킵)
- 각 서브페이지에 DOI가 거의 항상 본문에 노출 (정규식 `10\.\d{4,9}/\S+`)
- DrugCLIP 같이 fragmented 링크는 `href` 속성에서 재조립 필요
- 일부 페이지에 `wiki path` 또는 `llm-wiki stem` 힌트 존재 → dedup 보조

### 위키 측 (재사용 가능 자산)
- `wiki/topics/cancer-multiomics-literature.md` — 100편 모니터 허브 (이미 존재)
- `wiki/analyses/cancer-multiomics-corpus-queue.md` — 큐 (이미 존재, 카운트 갱신 필요)
- `wiki/analyses/cancer-multiomics-literature/` — Slack-ready brief (13편 기존)
- `wiki/_meta/paper-frontmatter-schema.md` — frontmatter 스펙
- `./bin/qmd search "<terms>" -c llm-wiki` — 중복 탐지

### Ingest scripts (재사용 가능)
| 스크립트 | 역할 | 입력 | 출력 |
|---|---|---|---|
| `resolve_pdf.py` | title→PMID→DOI→PDF (PMID-first) | unmatched.json | resolved.json + PDF |
| `ku_download.py` | KU 캠퍼스 IP 쿠키로 PDF | wiki/sources/*.md (`pdf_status: pending`) | raw/inbox/papers/ |
| `ezproxy_download.py` | KU EZproxy 쿠키로 PDF | 동일 | 동일 |
| `fetch_abstract.py` | PMID → PubMed 메타+abstract | resolved.json | meta.json |
| `generate_source_pages.py` | meta.json → wiki stub | meta.json | wiki/sources/*.md |
| `expand_topic.py` | PubMed keyword 검색 | --topic name | expansion.json |
| `ingest_expansion.py` | expansion → 페이지+PDF | expansion.json | sources + PDFs |

### 갭 (해결 필요)
1. **DOI-first 흐름 부재** → 노션은 PMID 없이 DOI만 있는 경우 多. resolve_pdf.py는 title→PubMed search → PMID 의존이라 2026 preprint나 비-PubMed 저널은 실패율 ↑
2. **citation graph 부재** → expand_topic.py는 하드코딩 PubMed 쿼리만. OpenAlex/Semantic Scholar 미연동
3. **`cancer-multiomics-literature` topic이 generate_source_pages.py의 `--topic` 옵션에 미등록** (옵션은 `ptmanchor`/`resistance`/`bcell-neoantigen` 셋만)

---

## Phase 1 — Notion DOI 추출 + 위키 dedup

**산출물**: `/tmp/wiki_work/cancer_multiomics_seed.json`

```json
[
  {
    "notion_id": "347302d9-...",
    "notion_url": "https://www.notion.so/...",
    "title_full": "ProteinAligner: ...",
    "first_author_last": "zhang",
    "year": 2026,
    "journal": "Cell Reports Methods",
    "doi": "10.1016/j.crmeth.2026.101407",
    "slug_candidate": "zhang-2026-proteinaligner-tri-modal-contrastive-plm",
    "wiki_hint": "wiki/protein-ai/zhang-2026-...",
    "in_wiki": false
  },
  ...
]
```

**Steps**:
1. 27개 서브페이지를 mcp__notion__notion-fetch로 순회 → DOI/title/authors/year/journal 추출
2. 각 후보의 `slug_candidate`를 `firstauthor-year-five-key-words` 규칙으로 생성
3. Dedup:
   - `wiki/sources/<author>-<year>-*.md` glob 매치
   - `./bin/qmd search "<title 핵심 키워드>"` 결과 매치
   - 노션의 `wiki path` 힌트와 교차 검증
4. `in_wiki: true`는 제외, `false`만 신규 후보로 통과

**Anti-pattern guards**:
- DOI 정규식이 잘못 잘리면 안 됨 → fragmented 링크는 a 태그 href를 우선 사용
- "Zhang 2026"이 두 편 (ProteinAligner, Multi-Embed, Spatial EcoTyper)이라 author-year 단순 매치는 false negative 위험. 키워드까지 봐야 함

**Verification**: seed.json의 신규 후보 수와 노션 27편에서 in_wiki=true 제외한 수가 일치

---

## Phase 2 — Stub source 페이지 생성

**산출물**: `wiki/sources/<slug>.md` (신규 후보 1편당 1개)

**Frontmatter (canonical)**:
```yaml
---
title: "<full title>"
authors:
  - "<First Author>"
  - "..."
year: 2026
journal: "<journal>"
doi: "10.xxxx/..."
url: "https://doi.org/10.xxxx/..."
paper_kind: <computational|translational|review|...>
cancer_types:
  - <pan-cancer or specific>
modalities:
  - <multi-omics|spatial-transcriptomics|...>
themes:
  - cancer-multiomics
  - <paper-specific theme>
tags:
  - source
  - cancer-multiomics
  - <slug-keyword>
topic: cancer-multiomics-literature
pdf_status: pending
notion_url: https://www.notion.so/...
---
```

**본문 (minimal)**:
```markdown
# <Title>

_<journal>, <year>._ DOI: [10.xxxx/...](https://doi.org/10.xxxx/...)

## Summary

_Awaiting deep-dive._ Notion 메모: <한줄요약 from Notion>

## Key Points

- _PDF ingest 후 보강 예정._

## Connections

- [Cancer Multiomics Proteogenomic Atlas](../topics/cancer-multiomics-literature.md)
- <기타 관련 concept hub>

## Sources

- Local PDF: `raw/inbox/papers/<slug>.pdf` (pending)
- Notion: <notion_url>
- DOI: <https://doi.org/10.xxxx/...>
```

**Why stub-first**: KU/ezproxy 다운로더가 `wiki/sources/*.md`를 입력으로 스캔하므로, 페이지가 먼저 있어야 다운로드가 된다.

**Anti-pattern guards**:
- `--topic` 미등록 옵션은 generate_source_pages.py에 안 통하므로 **이 단계는 스크립트가 아닌 직접 작성** 또는 generate_source_pages.py 확장 후 실행
- `firstauthor-year-five-key-words` 규칙 엄수 (PDF/MD 동일 basename)

---

## Phase 3 — PDF 자동 다운로드

**Input**: 사용자가 KU 쿠키 파일 제공 (`/.cookies/oca.cookies.txt`)
**Tool**: `python scripts/ingest/ku_download.py --cookies <path> --workers 4`

**Steps**:
1. 사용자가 KU 도서관 로그인 → 브라우저 확장으로 cookies.txt export
2. `ku_download.py` 실행 → wiki/sources/ 스캔 → DOI 추출 → KU IP로 PDF 시도
3. 실패 케이스 (preprint, OA 저널, KU 미구독)는 fallback chain:
   - bioRxiv DOI (`10.1101/...`) → `https://www.biorxiv.org/content/{doi}.full.pdf`
   - Unpaywall API → OA URL
   - 수동 다운로드 큐로 분류 (`pdf_status: manual`)

**Verification**:
```bash
# 다운로드 성공 카운트
grep -l "pdf:" wiki/sources/*.md | xargs grep -l "topic: cancer-multiomics-literature" | wc -l
# 페이지에 pdf path 등록되어 있고 raw/inbox/papers/<slug>.pdf 실존 확인
```

---

## Phase 4 — Deep-read + 본문 채우기 (on-demand)

PDF 확보된 논문 단위로 사용자 우선순위에 따라 진행. 27편 일괄 X.

**Steps per paper**:
1. `raw/inbox/papers/<slug>.pdf` Read
2. Abstract, Methods, Key figures 정독
3. wiki/sources/<slug>.md의 Summary/Key Points/Connections 채움
4. 필요시 `wiki/analyses/cancer-multiomics-literature/<slug>.md` Slack-ready brief 추가
5. 기존 concept 페이지 (b-cells-and-tertiary-lymphoid-structures, 등) 보강

**Anti-pattern guards**:
- PDF 본문 없이 abstract만 있는 단계에서 가짜 Key Points 만들지 않기 → `_Awaiting deep-dive_` 유지
- 노션 한국어 메모는 출처 표기 후 인용

---

## Phase 5 — 관련 논문 디스커버리

**현재 코드 한계**: citation graph 미구현. 두 가지 옵션:

### Option A — `expand_topic.py`에 `cancer-multiomics` 토픽 추가 (권장 fallback)
- 하드코딩 PubMed 쿼리에 cancer-multiomics keyword 셋 추가
- 장점: 기존 검증된 파이프라인 (`expand → ingest_expansion`) 재사용
- 단점: 노션 27편의 citation graph는 활용 X (키워드 기반 발견)

### Option B — 신규 스크립트 `scripts/ingest/find_related_via_openalex.py` (권장 메인)
- 입력: `cancer_multiomics_seed.json`의 DOI 리스트
- 동작:
  ```python
  for doi in seeds:
      r = httpx.get(f"https://api.openalex.org/works/doi:{doi}")
      related = r.json()["related_works"]   # 약 20개 OpenAlex ID
      cited = r.json()["referenced_works"]  # 참고문헌
      # 각 ID의 메타 가져와 cancer/multiomics keyword 필터
  ```
- 출력: `expansion.json` 형식 (기존 ingest_expansion.py 호환)
- 장점: API key 불필요, 노션 시드 기반 정확한 관련성
- 단점: ~100줄 신규 코드

**권장**: B를 메인, A를 보조로. B 결과가 부실하면 A로 키워드 검색 보강.

**[2026-05-10 결정]**: Option B (OpenAlex 시드기반) 단독 채택.

**Anti-pattern guards**:
- OpenAlex API rate limit (10 req/s 권장) 준수
- 관련도 필터 없으면 cancer-irrelevant 논문 대량 유입 위험 → MeSH/title 키워드 필터 필수

---

## Phase 6 — 허브/index/log/QMD 갱신

**Edits**:
1. `wiki/topics/cancer-multiomics-literature.md` — 신규 페이지 링크 추가
2. `wiki/analyses/cancer-multiomics-corpus-queue.md` — 카운트/상태 갱신
3. `wiki/_meta/index.md` — "Cancer Multiomics Literature" 섹션 또는 그룹별 항목 추가
4. `wiki/_meta/log.md` — `## [YYYY-MM-DD] cancer-multiomics | Notion 참고논문 N편 ingest` 엔트리

**Log format** (실제 사례 기반):
```markdown
## [2026-05-10] cancer-multiomics | Notion 참고논문 N편 ingest + 관련논문 M편 큐 적재

- Notion 페이지 344302d9 → wiki/sources/ N편 stub 생성 (모두 cancer-multiomics-literature 토픽).
- ku_download.py로 X편 PDF 확보, Y편은 manual queue.
- OpenAlex 시드 기반 관련논문 M편 → wiki/analyses/cancer-multiomics-corpus-queue.md 추가.
- topic hub + corpus-queue 카운트 갱신.
```

**QMD reindex**: `./bin/qmd embed` (필요 시)

**Verification**:
- `grep -c "cancer-multiomics-literature" wiki/sources/*.md` 와 hub 페이지 링크 수 일치
- `wiki/_meta/log.md`의 마지막 엔트리가 오늘 날짜 + 정확한 카운트 포함

---

## 실행 순서 요약

1. Phase 1 (~5min): 노션 27편 fetch + dedup → seed.json
2. Phase 2 (~10-20min): N편 stub 페이지 작성
3. **사용자 액션**: KU 쿠키 export (`/.cookies/oca.cookies.txt`)
4. Phase 3 (~10min): ku_download.py 실행
5. Phase 5 (~30min): OpenAlex related works 디스커버리 (Option B 스크립트 작성 + 실행)
6. Phase 6 (~5min): 허브/index/log 갱신
7. Phase 4: 사용자 우선순위 논문부터 on-demand deep-read

**병렬화**: Phase 2와 Phase 5는 독립적이므로 동시 진행 가능.
