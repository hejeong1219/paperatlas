---
title: "scComm: a contrastive learning framework for deciphering cell-cell communications at single-cell resolution"
authors:
  - "Jin"
  - "Tang"
  - "Li"
  - "Zhang"
  - "Xie"
year: 2026
journal: "Genome biology"
doi: "10.6084/m9.figshare.31615864"
pmid: "41877186"
pmcid: "PMC13134144"
pdf: "raw/inbox/papers/jin-2026-sccomm-contrastive-learning-framework-deciphering-cell.pdf"
paper_kind: research
cancer_types:
  - "colorectal-cancer"
  - "hepatocellular-carcinoma"
themes:
  - "immunotherapy"
  - "tls-biology"
topic: b-cell-neoantigen-human-cancer
discovery_method: topic-sweep-2026-05-25
tags:
  - "b-cell-neoantigen-human-cancer"
  - "genome-biol-2026"
  - "immunotherapy"
  - "tls-biology"
  - "topic-sweep"
batch_ingest_status: topic-sweep-stub
batch_ingested_on: 2026-05-25
---

# scComm: a contrastive learning framework for deciphering cell-cell communications at single-cell resolution

_Genome Biol, 2026._ [10.6084/m9.figshare.31615864](https://doi.org/10.6084/m9.figshare.31615864) · [PubMed 41877186](https://pubmed.ncbi.nlm.nih.gov/41877186/) · [PMC PMC13134144](https://pmc.ncbi.nlm.nih.gov/articles/PMC13134144/)

## Summary

본 연구는 supervised contrastive learning을 활용하여 single-cell 수준에서 cell-cell communication(CCC)을 추론하는 computational framework scComm을 제안합니다. 기존 cluster-aggregated 방법이 within-cluster heterogeneity를 무시하는 한계를 극복하며, simulation에서 최대 95% 정확도를 달성했습니다. colorectal cancer scRNA-seq에 적용하여 PD-1 blockade 반응과 tertiary lymphoid structures(TLS) 관련 CCC를 식별했고, liver cancer에서는 3개의 novel tumor subtype과 angiogenesis-promoting neutrophil subtype을 발견하여 기존 방법으로는 놓치는 high-resolution biological insight를 제공함을 보였습니다.

## Key Points

- scComm은 supervised contrastive learning으로 ligand-receptor pair selection과 cell-cell communication을 single-cell 해상도로 추론하는 framework이다.
- benchmark simulation에서 기존 CCC inference 방법을 능가하며 최대 95% 정확도를 달성하여 within-cluster heterogeneity를 효과적으로 다룬다.
- colorectal cancer scRNA-seq 분석에서 PD-1 blockade 반응성과 TLS 형성에 연관된 cell-cell communication network를 식별했다.
- liver cancer 데이터에 적용하여 3개의 novel tumor subtype과 angiogenesis를 촉진하는 neutrophil subtype을 발견, 각 subtype 고유의 tumor microenvironment 특징을 묘사했다.
- 한계: deep learning 모델 특성상 학습 데이터·label 품질에 의존하며, 새로운 cancer type에서 generalization 검증이 추가로 필요하다.

## 한미암 활용 가능성

한미암 위암 scRNA-seq/spatial 데이터에서 TLS 형성·B cell-T cell 상호작용·면역치료 반응 관련 ligand-receptor 신호를 single-cell 수준으로 해부하는 분석 도구로 검토해볼 만하며, 기존 cluster-aggregated 방법보다 within-subtype heterogeneity를 더 잘 보존한다는 점에서 위암 TME의 subtype별 communication map을 그릴 때 참고할 수 있겠습니다.

## Topic Sweep Ingest Status

- Status: `topic-sweep-stub` (2026-05-25)
- Topic: `b-cell-neoantigen-human-cancer`
- Local PDF: `raw/inbox/papers/jin-2026-sccomm-contrastive-learning-framework-deciphering-cell.pdf`
- Download path: `europepmc-xml: https://europepmc.org/articles/PMC13134144?pdf=render`
- Extracted text length: 30013 characters
- Scope note: automated topic-sweep batch ingest; not yet a manual full-text deep-dive.

## Abstract (PubMed)

Cell-cell communication regulates complex biological processes in multicellular systems. Existing scRNA-seq-based methods typically aggregate gene expression by clusters, overlooking within-cluster heterogeneity. We present scComm, a computational framework that infers cell-cell communications between individual cells using supervised contrastive learning. In simulations, scComm outperforms other methods and achieves up to 95% accuracy. Applied to colorectal cancer, it reveals cell-cell communications linked to PD-1 blockade response and tertiary lymphoid structures. In liver cancer, it identifies three novel tumor subtypes and angiogenesis-promoting neutrophil subtypes that have unique tumor microenvironments. scComm enables high-resolution cell-cell communication analysis, uncovering biological insights missed by existing approaches.

## High-signal PDF head

```
Jin et al. Genome Biology   (2026) 27:149                                                                                                         Genome Biology
https://doi.org/10.1186/s13059-026-04043-9




    METHODOLOGY                                                                                                                                        Open Access

scComm: a contrastive learning framework
for deciphering cell–cell communications
at single‑cell resolution
Zijie Jin1,2†, Zongli Tang1,2†, Xinyi Li1†, Kuangen Zhang3, Zhengwei Xie2,4* and Ning Zhang1,2,3,4*


†
 Zijie Jin, Zongli Tang and Xinyi Li
contributed equally to this work.
                                         Abstract
*Correspondence:                         Cell–cell communication regulates complex biological processes in multicellular
xiezhengwei@hsc.pku.edu.cn;              systems. Existing scRNA-seq-based methods typically aggregate gene expression
zhangning@bjmu.edu.cn                    by clusters, overlooking within-cluster heterogeneity. We present scComm, a compu-
1
  Department of Immunology,              tational framework that infers cell–cell communications between individual cells using
School of Basic Medical Sciences,        supervised contrastive learning. In simulations, scComm outperforms other methods
Health Science Center, Peking
University, Beijing 100191, China        and achieves up to 95% accuracy. Applied to colorectal cancer, it reveals cell–cell com-
2
  Peking Univers
```

## Sources

- Local PDF: `raw/inbox/papers/jin-2026-sccomm-contrastive-learning-framework-deciphering-cell.pdf`
- DOI: <https://doi.org/10.6084/m9.figshare.31615864>
- PubMed: <https://pubmed.ncbi.nlm.nih.gov/41877186/>
- PMC: <https://pmc.ncbi.nlm.nih.gov/articles/PMC13134144/>
