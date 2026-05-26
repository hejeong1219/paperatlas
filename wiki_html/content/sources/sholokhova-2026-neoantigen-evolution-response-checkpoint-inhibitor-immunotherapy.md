---
title: "Neoantigen evolution and response to checkpoint inhibitor immunotherapy in colorectal cancer"
authors:
  - "Sholokhova"
  - "Kaveh"
  - "Bozic"
year: 2026
journal: "Nature communications"
doi: "10.5281/zenodo.6607134"
pmid: "41904118"
pmcid: "PMC7056644"
pdf: "raw/inbox/papers/sholokhova-2026-neoantigen-evolution-response-checkpoint-inhibitor-immunotherapy.pdf"
paper_kind: trial
cancer_types:
  - "colorectal-cancer"
  - "leukemia"
themes:
  - "clinical-translation"
  - "immunotherapy"
  - "neoantigen-discovery"
topic: b-cell-neoantigen-human-cancer
discovery_method: topic-sweep-2026-05-25
tags:
  - "b-cell-neoantigen-human-cancer"
  - "clinical-translation"
  - "immunotherapy"
  - "nat-commun-2026"
  - "neoantigen-discovery"
  - "topic-sweep"
batch_ingest_status: topic-sweep-stub
batch_ingested_on: 2026-05-25
---

# Neoantigen evolution and response to checkpoint inhibitor immunotherapy in colorectal cancer

_Nat Commun, 2026._ [10.5281/zenodo.6607134](https://doi.org/10.5281/zenodo.6607134) · [PubMed 41904118](https://pubmed.ncbi.nlm.nih.gov/41904118/) · [PMC PMC7056644](https://pmc.ncbi.nlm.nih.gov/articles/PMC7056644/)

## Summary

본 연구는 stochastic branching-process 기반으로 colorectal cancer(CRC) 종양의 neoantigen 진화를 simulate하고 각 neoantigen에 immunogenicity label을 부여하여 in-silico tumor의 pre-treatment mutational landscape를 생성합니다. 이어 임상시험 데이터로 매개변수화된 tumor-immune dynamical systems 모델로 checkpoint-blockade 치료 반응을 simulate하여 mutational landscape의 heterogeneity와 결과 간 관계를 정량화했습니다. 결과적으로 강한 clonal neoantigen 1개의 존재가 성공적 반응에 결정적이며, 반응 동역학에 기여하는 모든 neoantigen 중 minimal neoantigen quality가 durable response의 가장 강력한 예측인자임을 시사합니다.

## Key Points

- stochastic branching-process로 growing tumor 안에서 neoantigen 진화를 simulate하고 각 neoantigen에 predicted immunogenicity label을 부여하여 in-silico CRC tumor 코호트의 mutational landscape를 생성했다.
- 임상시험 데이터로 parameterize된 tumor-immune dynamical systems 모델을 CPI 치료에 적용하여 mutational landscape heterogeneity와 outcome 간 정량 관계를 도출했다.
- "강한 clonal neoantigen 1개"의 존재 여부가 성공적 반응에 결정적인 요인으로 나타나, subclonal mutation 다수보다 clonal high-quality neoantigen이 더 중요함을 시사한다.
- minimal neoantigen quality(반응 동역학에 기여하는 모든 neoantigen 중 가장 낮은 품질)가 durable response의 가장 강력한 예측인자로 식별되었다.
- limitation: 시뮬레이션·dynamical model 중심으로 실제 환자 cohort에서의 직접 검증은 후속 작업이 필요하며, MSI-H vs MSS subtype 간 차이를 모델 가정 안에서 어떻게 다룰지가 핵심이다.

## 한미암 활용 가능성

한미암 위암 cohort에서 neoantigen prediction 결과를 clonal vs subclonal로 분리하고 "strong clonal neoantigen 1개" 보유 여부와 minimal neoantigen quality 같은 simulation-derived 변수를 ICI 반응 예측 모델 변수로 시범 도입해 검토해볼 만하며, 위암 MSI-H subtype에서 clonal high-quality neoantigen 기여도를 정량화하는 모델링 framework로 참고할 수 있겠습니다.

## Topic Sweep Ingest Status

- Status: `topic-sweep-stub` (2026-05-25)
- Topic: `b-cell-neoantigen-human-cancer`
- Local PDF: `raw/inbox/papers/sholokhova-2026-neoantigen-evolution-response-checkpoint-inhibitor-immunotherapy.pdf`
- Download path: `unpaywall: https://www.nature.com/articles/s41467-026-71135-2_reference.pdf`
- Extracted text length: 30013 characters
- Scope note: automated topic-sweep batch ingest; not yet a manual full-text deep-dive.

## Abstract (PubMed)

Checkpoint-blockade immunotherapy enables the immune system to recognize tumor cells that were previously invisible due to immune escape, but these therapies lead to heterogeneous patient outcomes. Focusing on colorectal cancer, in which two subtypes have markedly different responses to immunotherapy, we query the relationship between a tumor's mutagenic landscape and therapeutic outcomes. First, we model neoantigen evolution in growing tumors using a stochastic branching-process model and label each neoantigen by its predicted immunogenicity, giving each in-silico tumor a unique pre-treatment mutational landscape. Next, we use a dynamical systems model of tumor-immune interactions under checkpoint-blockade therapy, parameterized using clinical trial data, to simulate immunotherapy. We relate therapeutic outcomes to the heterogeneity of tumor mutational landscape, finding that a strong clonal neoantigen appears crucial for a successful response. Additionally, the minimal neoantigen quality across all neoantigens contributing to response dynamics is one of the strongest predictors of durable response.

## High-signal PDF head

```
ARTICLE IN PRESS




Nature Communications                                                                                   https://doi.org/10.1038/s41467-026-71135-2


Article in Press

Neoantigen evolution and response to checkpoint
inhibitor immunotherapy in colorectal cancer

Received: 23 October 2025                            Alanna Sholokhova, Kamran Kaveh & Ivana Bozic
Accepted: 13 March 2026
                                                     We are providing an unedited version of this manuscript to give early access to its
Cite this article as: Sholokhova, A.,
                                                                                                      S
                                                     findings. Before final publication, the manuscript will undergo further editing. Please
Kaveh, K., Bozic, I. Neoantigen                                                              ES
                                                     note there may be errors present which affect the content, and all legal disclaimers
                                                     apply.
evolution and response to
checkpoint inhibitor immunotherapy
in colorectal cancer. Nat Commun
                                                                                   PR
                                                       If this paper is publishing under a Transparent Peer Review model then Peer
                                                     Review reports wi
```

## Sources

- Local PDF: `raw/inbox/papers/sholokhova-2026-neoantigen-evolution-response-checkpoint-inhibitor-immunotherapy.pdf`
- DOI: <https://doi.org/10.5281/zenodo.6607134>
- PubMed: <https://pubmed.ncbi.nlm.nih.gov/41904118/>
- PMC: <https://pmc.ncbi.nlm.nih.gov/articles/PMC7056644/>
