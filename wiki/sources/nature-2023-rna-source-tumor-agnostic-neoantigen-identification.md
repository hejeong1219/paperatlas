---
title: Proteogenomic analysis reveals RNA as a source for tumor-agnostic neoantigen identification
authors:
  - "Tretter"
year: 2023
journal: "Nature Communications"
doi: "10.1038/s41467-023-39570-7"
url: "https://www.nature.com/articles/s41467-023-39570-7"
pdf: "raw/inbox/papers/nature-2023-rna-source-tumor-agnostic-neoantigen-identification.pdf"
paper_kind: translational
cancer_types:
  - pan-cancer
modalities:
  - proteogenomics
  - neoantigen-discovery
  - immunopeptidomics
themes:
  - neoantigen
  - rna-derived-antigens
  - immunogenicity
  - tumor-agnostic
tags:
  - source
  - neoantigen
  - proteogenomics
  - immunopeptidomics
  - pan-cancer
topic: ptmanchor
extra_topics:
  - "bcell-neoantigen"
---
# Proteogenomic analysis reveals RNA as a source for tumor-agnostic neoantigen identification

Pan-cancer proteogenomic and immunopeptidomic study showing that RNA-derived events are a major source of candidate neoantigens across human tumors.

## Key Points

- Profiles 32 patients across 25 tumor types with DNA and RNA sequencing, HLA immunopeptidomics, and downstream immunogenicity testing.
- Uses an optimized pipeline that integrates RNA-seq and Prosit-assisted rescoring to broaden neoantigen discovery beyond DNA-only coding variants.
- Reports that many detected neoantigen candidates arise from RNA-derived events, including non-canonical and RNA-processing-related sources.
- Narrows a broad candidate space to 32 validated potential neoantigen candidates after peptide-level and immunogenicity-focused filtering.
- Connects immunogenic neoantigen detection with stronger T-cell infiltration, making this relevant for immune-context-aware prioritization rather than sequence-only ranking.

## Relevance

- Highly relevant to the B-cell neoantigen proposal because it strengthens the upstream discovery stack for multi-cancer neoantigen identification in real human tumors.
- Supports a pipeline architecture where transcriptomic and non-canonical antigen generation should be treated as first-class input layers rather than optional add-ons.
- Useful as a bridge paper between proteogenomic antigen discovery and later interpretation within TLS or B-cell-rich immune contexts.

## 한미암 활용 가능성

- 확인된 neoantigen 후보 90개 중 79개가 DNA에 없이 RNA 변이에서만 유래했고, 면역원성이 확인된 21개가 전부 RNA 기원(20개는 RNA 단독)이라는 결과는, WGS 변이만으로 신생항원 후보를 산정하는 파이프라인의 사각지대를 구체적 숫자로 보여줍니다.
- 검증 순서 제안(스펙트럼 검증 → GTEx 10,269개 정상조직 샘플 prevalence 확인 → 면역원성 평가)은, 한미암 신생항원 후보 우선순위 산정에서 어떤 필터를 어느 단계에 둘지 정할 때 참고할 만한 구조입니다. 저자들은 GTEx가 주로 mRNA 기반이라 intron 영역을 다루지 못한다는 점을 들어 환자 liquid biopsy total RNA-seq 병행을 제안합니다.
- 면역원성이 확인·검증된 후보 수가 TME의 CD3+/CD8+ Teff 침윤 빈도와 더 강하게 상관한 반면, RNA 변이의 총량 자체는 생존과 상관하지 않았습니다. 후보 개수를 단독 지표로 쓰기보다 면역 침윤 지표와 교차 확인하는 방향을 시사합니다.
- 코호트 한계: 32명/25개 암종의 이질적 pan-cancer 구성이며 위암 특이 코호트가 아닙니다. 면역원성 검증은 in vitro(acDC/ELISpot) 단계입니다.
- Slack 디지스트 게시: 2026-09-23.

## Connections

- [B-Cell Neoantigen Proposal Anchor](../analyses/b-cell-neoantigen-proposal-anchor.md)
- [B-Cell Neoantigen Research Map](../topics/b-cell-neoantigen-human-cancer.md)
- [Neoantigen Discovery Pipelines](../concepts/neoantigen-discovery-pipelines.md)
- [Identification of non-canonical peptides with moPepGen](./zhu-2025-identification-of-non-canonical-peptides.md)
- [A comprehensive proteogenomic pipeline for neoantigen discovery to advance personalized cancer immunotherapy](./huber-2025-comprehensive-proteogenomic-pipeline-neoantigen-discovery.md)

## Sources

- PDF: [nature-2023-rna-source-tumor-agnostic-neoantigen-identification.pdf](../../raw/inbox/papers/nature-2023-rna-source-tumor-agnostic-neoantigen-identification.pdf)
- Article: <https://www.nature.com/articles/s41467-023-39570-7>
