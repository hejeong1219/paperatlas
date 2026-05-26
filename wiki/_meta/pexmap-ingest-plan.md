# PEXMap (Awasthi 2026) Ingest Plan

**Slug**: `awasthi-2026-pexmap-proteogenomic-exon-isoform-mapping`

## 사전 확인

- **논문**: Awasthi, Verma, Pandit. "PEXMap: A proteogenomic method for exon and isoform level mapping of mass spectrometry derived peptides." bioRxiv, posted 2026-05-04.
- **DOI**: `10.64898/2026.04.29.721330` (openRxiv prefix, bioRxiv Systems Biology)
- **Source URL**: https://www.biorxiv.org/content/10.64898/2026.04.29.721330v1.abstract
- **License**: CC BY-NC-ND 4.0
- **PDF**: 이미 `raw/inbox/papers/awasthi-2026-pexmap-proteogenomic-exon-isoform-mapping.pdf` 에 저장됨 (1.7 MB, 23 페이지). 직접 다운로드 (Chrome UA + Mac Referer 헤더로 우회).
- **중복 확인**: `wiki/sources/` 및 `wiki/topics/cancer-multiomics-literature.md` 에 `PEXMap`/`peptide exon mapp`/`k-mer.*proteogenomic` 매치 없음 — 신규 ingest.
- **핵심 요지 (Crossref abstract)**: k-mer 기반 proteogenomic framework로 MS/MS peptide를 gene/transcript/exon/exon-junction 수준으로 정확 매핑. PeptideAtlas로 검증, 간/췌장/암 proteome에 적용해 tissue-specific isoform 발현을 확인. GitHub 공개.

## Phase 1 — PDF 본문 분석

1. `extract_pdf_text.py` 또는 `pdftotext` 로 PDF → 텍스트 추출.
2. 핵심 추출 대상:
   - Abstract 풀 텍스트
   - PEXMap 알고리즘 핵심 (k-mer 길이=8, exon-resolved isoform DB 구성)
   - 벤치마크/검증 결과 (PeptideAtlas concordance 수치)
   - Liver / Pancreas / Cancer proteome 적용 결과
   - 한계 / 향후 작업
   - Data Availability (GitHub repo URL, dataset accession)
   - Methods 핵심 표/그림 번호

## Phase 2 — `wiki/sources/<slug>.md` 생성

`paper-frontmatter-schema.md` + Jiang 2025 페이지 스타일을 따른다.

### Frontmatter (제안)

```yaml
title: "PEXMap: A proteogenomic method for exon and isoform level mapping of mass spectrometry derived peptides"
authors:
  - "Deepanshi Awasthi"
  - "Paras Verma"
  - "Shashi Bhushan Pandit"
year: 2026
journal: "bioRxiv"
doi: "10.64898/2026.04.29.721330"
url: "https://www.biorxiv.org/content/10.64898/2026.04.29.721330v1"
pdf: "raw/inbox/papers/awasthi-2026-pexmap-proteogenomic-exon-isoform-mapping.pdf"
paper_kind: computational
cancer_types:
  - pan-cancer
modalities:
  - proteogenomics
  - mass-spectrometry
themes:
  - proteogenomics
  - alternative-splicing
  - isoform-resolution
  - peptide-mapping
topic: cancer-multiomics-literature
tags:
  - source
  - cancer-multiomics
  - proteogenomics
  - alternative-splicing
  - tool
```

### 본문 섹션

- `# Title`
- `_bioRxiv (preprint), 2026._ DOI: ... · 한 줄 인용`
- `## Summary` — 5-8 줄, PEXMap 동기와 결과
- `## Key Points` — 알고리즘 핵심, 검증 지표, 적용 결과, 한계, 공개 데이터
- `## Methods` — k-mer 매칭 로직, reference DB 구성, isoform mapping rule
- `## Cancer Multiomics Project Relevance` — 한미암 인산화단백체/neoantigen 파이프라인에 미치는 함의
- `## Slack 메시지 초안` — 교수진 공유용 짧은 포맷 (선택)
- `## Connections` — Jiang 2025, NeoFlow (Wen 2020), NeoDisc (Huber 2025), Chong 2022 등 인접 페이지 링크
- `## Sources` — raw PDF + 외부 링크

## Phase 3 — 위키 허브/메타 갱신

1. `wiki/topics/cancer-multiomics-literature.md`:
   - **Section 1 (WGS와 Proteogenomics 통합 기반)** 끝에 추가 — PEXMap은 splice-isoform-aware peptide annotation tool 이므로 통합 기반 섹션에 적합.
   - 또는 **Section 3 (면역회피와 Neoantigen)** — NeoFlow/NeoDisc와 같은 proteogenomic pipeline tool로 묶을 수도 있음. **결정 필요**: Section 1 vs Section 3 어디에 둘지.
2. `wiki/analyses/cancer-multiomics-corpus-queue.md`:
   - Corpus 카운트 +1 (현재 카운트 확인 필요).
3. `wiki/_meta/index.md`:
   - sources 카테고리에 페이지 추가.
4. `wiki/_meta/log.md`:
   - `## [2026-05-11] ingest | Awasthi 2026 PEXMap` 항목 추가.

## Phase 4 — Notion 하위 페이지 생성

부모: `344302d9-c598-8188-8a05-d5041134fb3d` (참고 논문 및 아이디어).

**Title**: `Awasthi 2026 — PEXMap: k-mer 기반 proteogenomic exon/isoform peptide mapper`

**본문 (Tran 2026 페이지 스타일에 맞춤)**:

```markdown
## 논문 정보
- Title: PEXMap: A proteogenomic method for exon and isoform level mapping of mass spectrometry derived peptides
- Authors: Deepanshi Awasthi, Paras Verma, Shashi Bhushan Pandit
- Journal / preprint server: bioRxiv (2026-05-04)
- Identifier: 10.64898/2026.04.29.721330
- Code: [PEXMap GitHub](TBD — PDF에서 확인)
- llm-wiki stem: awasthi-2026-pexmap-proteogenomic-exon-isoform-mapping

## 한 줄 요약
(PDF Abstract 정독 후 1-2줄로 정리)

## 과제 관련성 (한미암)
- 한미암 proteogenomic 파이프라인에서 MS/MS peptide → exon/isoform 매핑 정확도 향상에 직접 활용 가능.
- Alternative splicing isoform 단백질을 distinguish 해야 하는 neoantigen 후보 발굴(특히 splice-junction neoantigen)에 잠재 활용.
- Tissue-specific isoform 분석(간/췌장 예시)이 폐암 코호트의 driver isoform proteomic feature 발견 설계로 확장 가능.
- 한계: peptide DB의 reference annotation 일관성에 의존 — 한미암 데이터에서 isoform DB 사전 정의가 필요.

## 핵심 결과
(PDF 본문에서 수치 포함 5-7 bullet 추출)

## 한미암에서 바로 가져올 포인트
- PDF 정독 후 작성. 가설: splice-aware peptide annotation을 한미암 proteogenomic 파이프라인의 후처리 모듈로 도입.

## 주의점
- bioRxiv preprint (peer review 전).
- k-mer 8-mer 매칭이라 short peptide 또는 high-similarity isoform 간 매핑 ambiguity 존재 가능.
- Cancer proteome 적용은 demonstration 수준, 대규모 임상 코호트 검증은 없음.
```

## Phase 5 — 검증 및 마무리

- 새 wiki 페이지 frontmatter 스키마 lint
- Notion 페이지 생성 후 ID 기록
- corpus-queue 카운트 vs 실제 일치 확인
- `wiki/_meta/log.md` 커밋용 차이 정리

## 결정이 필요한 항목 (사용자 승인 요청)

1. **Topic hub 배치 위치**: Section 1 (Proteogenomics 통합 기반) 또는 Section 3 (Neoantigen 파이프라인) 또는 둘 다? 추천: **Section 1**, "tool" 태그로 명시.
2. **Notion 제목 포맷**: 기존 페이지들은 "Tran et al. 2026 — Phoenix: ..." 패턴. 위 제안 그대로 진행 OK?
3. **Slack 메시지 초안**을 wiki 페이지에 포함할지 (다른 페이지처럼). 옵션: 포함 / 생략 / 별도 분석.
4. **Discovery 메타데이터**: `discovery_method: user-slack-share` 같이 출처 표기 추가할지 (Section 6 expansion 페이지들은 frontmatter에 `discovery_method`/`related_to_seeds` 있음).
