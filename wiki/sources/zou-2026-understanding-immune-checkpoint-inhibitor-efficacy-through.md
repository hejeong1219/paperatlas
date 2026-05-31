---
title: "Understanding immune checkpoint inhibitor efficacy through spatial decoding of the lung cancer tumor immune microenvironment"
authors:
  - "Zou"
  - "Minna"
year: 2026
journal: "The Journal of clinical investigation"
doi: "10.1001/jama.2024.10613"
pmid: "42138084"
pmcid: "PMC11337070"
pdf: "raw/inbox/papers/zou-2026-understanding-immune-checkpoint-inhibitor-efficacy-through.pdf"
paper_kind: research
cancer_types:
  - "non-small-cell-lung-cancer"
  - "small-cell-lung-cancer"
themes:
  - "clinical-translation"
  - "drug-resistance"
  - "immunotherapy"
  - "spatial-omics"
  - "treatment-response"
topic: cancer-multiomics-literature
discovery_method: topic-sweep-2026-05-25
tags:
  - "cancer-multiomics-literature"
  - "clinical-translation"
  - "drug-resistance"
  - "immunotherapy"
  - "j-clin-invest-2026"
  - "spatial-omics"
  - "topic-sweep"
  - "treatment-response"
batch_ingest_status: topic-sweep-stub
batch_ingested_on: 2026-05-25
cm_axis: response
---

# Understanding immune checkpoint inhibitor efficacy through spatial decoding of the lung cancer tumor immune microenvironment

_J Clin Invest, 2026._ [10.1001/jama.2024.10613](https://doi.org/10.1001/jama.2024.10613) · [PubMed 42138084](https://pubmed.ncbi.nlm.nih.gov/42138084/) · [PMC PMC11337070](https://pmc.ncbi.nlm.nih.gov/articles/PMC11337070/)

## Summary

JCI에 발표된 Isomoto 등의 NSCLC multiplex IHC 연구에 대한 commentary로, 103명의 metastatic NSCLC 환자(81명이 ICI 치료 받음)의 pretreatment 시료를 bespoke multiplex IHC + computational tissue segmentation으로 분석한 결과를 정리합니다. CD8+ TIL의 tumor nest proximity, tissue residence·proliferation marker는 ICI 효능과 연관된 반면, CD206+ M2-like TAM과 FAP+ CAF는 worse outcome과 상관함을 보고합니다. 특히 EGFR-mutant NSCLC에서 CD73 upregulation을 포함한 3-variable spatial composite가 PD-L1보다 ICI 효능 예측력에서 substantial하게 우세했고, intratumoral stromal CD8+ TIL density는 multivariable analysis에서 독립적 예측력이 없었습니다. 이는 spatial proteomic profiling이 NSCLC에서 actionable·mechanistic한 치료 가설 생성 플랫폼임을 강조합니다.

## Key Points

- Isomoto et al.은 103명 metastatic NSCLC(81명 ICI 치료)의 pretreatment 시료를 multiplex IHC + computational tissue segmentation으로 공간 프로파일링했습니다.
- CD8+ TIL의 tumor nest proximity와 tissue residence·proliferation marker는 ICI 효능과 양의 상관, CD206+ M2-like TAM과 FAP+ CAF는 음의 상관을 보였습니다.
- EGFR-mutant NSCLC에서 CD73 upregulation을 포함한 3-variable spatial composite는 PD-L1 단독 대비 substantial하게 우수한 ICI 효능 예측력을 보였습니다.
- Intratumoral stromal CD8+ TIL density는 표준 immunohistochemical 정량과 AI H&E scoring에서 통상 활용되지만, multivariable analysis에서 독립적 ICI 효능 예측력이 없었으며 이는 bulk TIL assessment의 임상적 utility 불일치를 spatial mechanism으로 설명합니다.
- Monkman et al.의 multiplex immunofluorescence + deep learning 연구가 본 결과를 검증하며, tumor nest proximity 관계(aggregate TIL density가 아니라)가 ICI PFS >24개월 예측의 핵심 단위임을 확인했습니다.

## 한미암 활용 가능성

치료반응 예측 측면에서, NSCLC에서 PD-L1보다 우수한 3-variable spatial composite (CD73 + 추가 spatial feature)가 도출된 사례는 위암 ICI 반응 예측에서 단일 마커(PD-L1, MSI 등)를 넘어선 multiplex IHC·spatial proteomic composite biomarker 개발을 검토해 볼 만합니다. 또한 tumor nest proximity, CD8+ TIL residency·proliferation, CD206+ M2 TAM 같은 spatial feature engineering 접근은 위암 multiplex IHC 데이터에서 ICI 효능 예측 모형 설계 시 참고할 수 있겠습니다.

## Topic Sweep Ingest Status

- Status: `topic-sweep-stub` (2026-05-25)
- Topic: `cancer-multiomics-literature`
- Local PDF: `raw/inbox/papers/zou-2026-understanding-immune-checkpoint-inhibitor-efficacy-through.pdf`
- Download path: `europepmc-xml: https://europepmc.org/articles/PMC13178642?pdf=render`
- Extracted text length: 26696 characters
- Scope note: automated topic-sweep batch ingest; not yet a manual full-text deep-dive.

## Abstract (PubMed)

Immune checkpoint inhibitors (ICIs) have improved patient outcomes substantially in non-small cell lung cancer (NSCLC). Despite considerable effort, our understanding of the features that predict for immunotherapy response and resistance in patients remains incomplete. In this issue of the JCI, Isomoto and colleagues utilized a multiplex IHC platform to profile the spatial organization of the lung cancer tumor immune microenvironment, enabling the identification of spatial immune features that correlate with immunotherapy efficacy. This study enhances our knowledge of the spatial organization of features impacting ICI efficacy by identifying a three-variable spatial composite - including CD73 upregulation in EGFR-mutant NSCLC - that substantially outperforms PD-L1 expression in predicting immunotherapy efficacy. Moreover, it establishes spatial proteomic profiling as a platform for generating therapeutic hypotheses that are actionable and mechanistic in NSCLC.

## High-signal PDF head

```
The Journal of Clinical Investigation                                                                                                                               CO M M E N TA RY



Understanding immune checkpoint inhibitor efficacy
through spatial decoding of the lung cancer tumor
immune microenvironment
Tao Zou1,2,3,4 and John D. Minna1,2,4,5
Hamon Center for Therapeutic Oncology Research, 2Department of Internal Medicine, 3Department of Immunology, 4Harold C. Simmons Comprehensive Cancer Center, and 5Department of Pharmacology,
1


University of Texas Southwestern Medical Center, Dallas, Texas, USA.


                                                                                                                                   and proliferation in TILs were associated
                                                                                                                                   with ICI efficacy, while CD206+ M2-like
             Immune checkpoint inhibitors (ICIs) have improved patient outcomes                                                    tumor-associated macrophages (TAMs)
             substantially in non–small cell lung cancer (NSCLC). Despite considerable                                             and fibroblast activation protein+ (FAP+)
             effort, our understanding of the features that predict for immunotherapy                                              cancer-associated fibroblasts (CAFs) cor-
             response and res
```

## Sources

- Local PDF: `raw/inbox/papers/zou-2026-understanding-immune-checkpoint-inhibitor-efficacy-through.pdf`
- DOI: <https://doi.org/10.1001/jama.2024.10613>
- PubMed: <https://pubmed.ncbi.nlm.nih.gov/42138084/>
- PMC: <https://pmc.ncbi.nlm.nih.gov/articles/PMC11337070/>
