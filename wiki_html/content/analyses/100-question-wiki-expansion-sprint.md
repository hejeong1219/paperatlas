---
title: 100-Question Wiki Expansion Sprint
tags:
  - question-bank
  - wiki-expansion
  - ingest-planning
  - cancer-multiomics
---

# 100-Question Wiki Expansion Sprint

질문 100개를 순차적으로 답하면서, 답변 가치가 있는 내용을 source/topic/concept/analysis/synthesis 페이지로 누적하고 이후 high-impact PDF 확보와 ingest로 이어가기 위한 운영 페이지.

## Key Points

- 사용자가 질문하면 먼저 `wiki/_meta/index.md`와 관련 topic/source page를 읽고, 답은 **로컬 PDF, 로컬 보충자료, 유지된 wiki page**에 근거해 작성한다.
- 답변이 durable value를 만들면 `wiki/analyses/` 또는 `wiki/syntheses/`에 저장하고, 관련 source/topic/concept page도 보강한다.
- 새 과학적 주장, 수치, 논문별 비교표, interactive data는 웹으로 채우지 않는다. 웹은 후보 발견, DOI/메타데이터 확인, PDF 확보 같은 운영 작업에만 쓴다.
- 이미 존재하는 100문항 은행을 출발점으로 삼고, 실제 질문이 들어오면 “답변 → 위키 반영 → 다음 질문/논문 gap 기록”으로 진행한다.
- 100문항 후에는 남은 gap을 기준으로 high-impact journal PDF를 추가 확보하고, `raw/inbox/papers/` → `wiki/sources/` → topic/analysis/synthesis 순서로 ingest한다.

## Current Question Banks

- [Four-Topic Question Expansion Map](topic-question-expansion-map.md): B-cell neoantigen, immunotherapy resistance, PTM identification atlas, Cancer Multiomics monitor의 4개 축별 질문 은행.
- [PTM Correction and Kinase Signaling Question Bank](ptm-correction-kinase-signaling-question-bank.md): protein abundance correction, kinase inference, phosphoproteomics 해석 질문 100개.
- [Cancer Multiomics Corpus Queue (Target=100)](cancer-multiomics-corpus-queue.md): high-impact multiomics/proteogenomics 코퍼스 선정, PDF 확보, source ingest, Cancer Multiomics brief 상태 추적.

## Sprint Protocol

1. 질문을 받으면 `wiki/_meta/index.md`를 먼저 확인한다.
2. `./bin/qmd search "<핵심어>"`로 관련 markdown page를 찾는다.
3. 관련 source page와 topic/concept/analysis page를 연다.
4. 답변에 필요한 수치/claim이 source page에 부족하면 해당 로컬 PDF 또는 supplement를 다시 읽는다.
5. 답변에는 근거가 되는 wiki/source page를 명시하고, 관찰/추론/불확실성을 분리한다.
6. durable value가 있으면 아래 중 하나 이상을 업데이트한다.
   - source page: 논문별 핵심 claim, 방법, 수치, caveat
   - concept page: 반복 개념, 정의 차이, 해석 원칙
   - topic hub: 관련 논문 묶음, 표준 체크리스트, navigation
   - analysis/synthesis: 질문 답변이 누적되는 비교표, 모델, 논지
7. `wiki/_meta/index.md`와 `wiki/_meta/log.md`를 갱신한다.
8. 새 논문이 필요하면 `cancer-multiomics-corpus-queue.md` 또는 `next-download-candidates.md`에 gap과 후보를 먼저 기록한 뒤 PDF 확보를 진행한다.

## Batch Plan

### Batch 1: Questions 1-25

목표: 현재 ingest된 논문만으로 답할 수 있는 질문을 우선 처리한다.

- Cancer Multiomics 100-paper queue에서 `needs-brief` 상태인 논문을 답변 근거로 승격한다.
- source page에 이미 충분한 수치가 있는 논문부터 Cancer Multiomics brief를 만든다.
- 질문마다 최소 하나의 source page와 하나의 topic/concept/analysis page를 업데이트한다.

### Batch 2: Questions 26-50

목표: 논문 간 정의 차이와 해석 tension을 정리한다.

- neoantigen evidence tier, antigen presentation defect, PTM correction, kinase inference, subtype/response endpoint 정의를 표준화한다.
- 반복되는 caveat는 concept page로 올리고 source page에는 짧게 링크한다.
- 비교표가 필요한 질문은 `wiki/analyses/`에 누적 테이블로 관리한다.

### Batch 3: Questions 51-75

목표: manuscript/proposal에 바로 쓸 수 있는 synthesis를 만든다.

- B-cell/TLS/neoantigen, immune resistance, PTM signaling, Cancer Multiomics를 연결하는 cross-topic synthesis를 만든다.
- 표준 그림/슬라이드가 될 수 있는 causal map, evidence matrix, taxonomy를 우선한다.
- 같은 claim을 여러 페이지에 복제하지 않고 canonical concept 또는 synthesis page로 모은다.

### Batch 4: Questions 76-100

목표: 남은 gap을 PDF acquisition list로 전환한다.

- 답변 과정에서 “로컬 evidence 부족”으로 표시된 claim을 모은다.
- high-impact 저널 논문 후보를 discovery-only web search 또는 bibliographic tooling으로 찾되, 과학적 내용은 PDF 확보 후만 기록한다.
- 다운로드된 PDF는 `raw/inbox/papers/`에 두고 source page basename을 안정적으로 정한다.
- 확보 실패, paywall, publisher correction, supplement missing은 queue에 명시한다.

## High-Impact PDF Sweep Rules

- 우선순위는 질문 답변 중 생긴 gap이 결정한다. “좋아 보이는 논문”보다 “현재 위키의 빈 링크를 메우는 논문”을 먼저 받는다.
- Cancer Multiomics와 직접 연결되는 논문은 다음 조건을 선호한다.
  - human cancer cohort 또는 clinical response/resistance context
  - WGS/WES/RNA-seq와 proteome/phosphoproteome/acetylome/immunopeptidome/spatial layer 중 둘 이상 통합
  - raw data 또는 processed data availability가 명시됨
  - therapeutic target, biomarker, subtype, resistance mechanism 중 하나 이상을 재사용 가능하게 제시
- Methods-only, review, benchmark, tool paper는 quantitative corpus row로 부풀리지 않고 context/source note로 분리한다.
- PDF 확보 후 source page deep-dive 전에는 scientific claim을 확정하지 않는다.

## Immediate Next Queue

- `needs-brief` source pages 중 PDF-backed full ingest가 이미 끝난 항목부터 Cancer Multiomics brief로 승격한다.
- `needs-deep-dive` expansion batch 36편은 질문과 직접 연결되는 순서로만 깊게 읽는다.
- blocked/manual_pending 항목은 high-impact sweep 때 대체 경로(PMC, publisher page, user-provided PDF, supplement)를 확인한다.
- 질문 답변 중 새로 발견되는 gap은 이 페이지가 아니라 관련 corpus queue 또는 topic question bank에 기록한다.

## Connections

- [Four-Topic Question Expansion Map](topic-question-expansion-map.md)
- [PTM Correction and Kinase Signaling Question Bank](ptm-correction-kinase-signaling-question-bank.md)
- [Cancer Multiomics Corpus Queue (Target=100)](cancer-multiomics-corpus-queue.md)
- [Cancer Multiomics Literature Monitor](../topics/cancer-multiomics-literature.md)

## Sources

- Maintained local wiki pages and source pages listed in `wiki/_meta/index.md`.
- Local PDFs and supplements under `raw/`.
