---
title: "Thymic health and immunotherapy outcomes in patients with cancer"
authors:
  - "Bernatz"
  - "Prudente"
  - "Pai"
  - "Attermann"
  - "Di Federico"
year: 2026
journal: "Nature"
doi: "10.1093/nar/gkad1025"
pmid: "41851467"
pmcid: "PMC10767911"
pdf: "raw/inbox/papers/bernatz-2026-thymic-health-immunotherapy-outcomes-patients-cancer.pdf"
paper_kind: research
cancer_types:
  - "breast-cancer"
  - "non-small-cell-lung-cancer"
  - "small-cell-lung-cancer"
  - "melanoma"
  - "renal-cell-carcinoma"
  - "pan-cancer"
themes:
  - "clinical-translation"
  - "immunotherapy"
  - "tcr-t"
topic: b-cell-neoantigen-human-cancer
discovery_method: topic-sweep-2026-05-25
tags:
  - "b-cell-neoantigen-human-cancer"
  - "clinical-translation"
  - "immunotherapy"
  - "nature-2026"
  - "tcr-t"
  - "topic-sweep"
batch_ingest_status: topic-sweep-stub
batch_ingested_on: 2026-05-25
---

# Thymic health and immunotherapy outcomes in patients with cancer

_Nature, 2026._ [10.1093/nar/gkad1025](https://doi.org/10.1093/nar/gkad1025) · [PubMed 41851467](https://pubmed.ncbi.nlm.nih.gov/41851467/) · [PMC PMC10767911](https://pmc.ncbi.nlm.nih.gov/articles/PMC10767911/)

## Summary

본 연구는 routine CT 영상에서 deep-learning self-supervised foundation model로 thymic health score(0–100)를 정량화하여 ICI 치료 환자 3,476명(pan-cancer cohort)에서 면역치료 효과와의 연관을 평가했습니다. NSCLC에서 thymic health가 높을수록 progression과 all-cause mortality 위험이 감소했으며, 이 연관은 PD-L1과 TMB 수준을 보정한 뒤에도 유지되었습니다. 전향적 TRACERx lung cancer 연구(n=464)에서 thymic health는 TCR diversity와 T cell receptor excision circles(TRECs), immune signalling pathway와 양의 상관을 보였고, melanoma·breast·renal cancer로 확장하여 pan-cancer 관련성을 보였습니다. 이로써 tumor-centric biomarker를 넘어선 host 면역 능력(thymic functionality)을 새로운 tumor-agnostic 결정 인자로 제시합니다.

## Key Points

- Training set 5,674명, evaluation set 3,940명(Harvard-NSCLC 1,218 + Harvard-PAN 2,258 + TRACERx 464)으로 ICI 치료 pan-cancer 코호트에 deep learning 기반 thymic health 정량 모델을 적용했다.
- Harvard-NSCLC 코호트에서 thymic health 상승이 progression과 all-cause mortality 위험 감소와 연관되었고, PD-L1과 TMB 층에 무관하게 유지되었다.
- TRACERx prospective cohort(n=464)에서 thymic health가 TCR diversity, TRECs, immune-system signaling pathway와 양의 상관을 보여 흉선 활동의 영상적 proxy로 검증되었다.
- melanoma, breast cancer, renal cell carcinoma 분석으로 thymic health의 pan-cancer 관련성이 확인되어, 종양 종류에 의존하지 않는 host-side biomarker임을 시사한다.
- 임상적 함의: patient stratification, treatment timing, immune-rejuvenating 전략(예: thymic regeneration) 개발에 영향 가능하지만, retrospective 영상 분석 위주이므로 prospective 검증이 추가로 필요하다.

## 한미암 활용 가능성

한미암 위암 cohort에서 ICI/항암화학 반응 예측 모델을 구축할 때 tumor multiomics만이 아니라 baseline CT 기반 thymic health score 같은 host immune competence proxy를 함께 변수로 통합해보는 접근을 검토해볼 수 있겠고, TCR-seq 데이터가 확보될 경우 thymic health와 TCR diversity·neoantigen-reactive TCR clone 수의 상관을 위암 환자에서 재현할 수 있는지 시사적 가설로 참고할 만합니다.

## Topic Sweep Ingest Status

- Status: `topic-sweep-stub` (2026-05-25)
- Topic: `b-cell-neoantigen-human-cancer`
- Local PDF: `raw/inbox/papers/bernatz-2026-thymic-health-immunotherapy-outcomes-patients-cancer.pdf`
- Download path: `europepmc-xml: https://europepmc.org/articles/PMC13102699?pdf=render`
- Extracted text length: 30013 characters
- Scope note: automated topic-sweep batch ingest; not yet a manual full-text deep-dive.

## Abstract (PubMed)

Although immunotherapy has revolutionized cancer treatment, many patients still experience limited benefit, highlighting the urgent need for improved biomarkers1. Although immunotherapy is founded on unleashing T cells2, most existing biomarkers remain tumour-centric and mainly overlook host immune competence. The thymus is a key immune organ that is crucial for T cell maturation, and we hypothesized that thymic functionality is associated with immunotherapy outcomes3. Here we show that thymic health, a radiographic measure of thymic functionality, is strongly associated with immunotherapy outcomes across several cancer types. Using a deep-learning framework applied to routine computed tomography images, we quantified thymic health in a pan-cancer cohort of 3,476 patients receiving immune checkpoint inhibitors. In patients with non-small cell lung cancer, higher thymic health was associated with reduced risks of progression and all-cause mortality. These associations remained significant across clinically relevant levels of programmed death ligand 1 (PD-L1) and tumour mutation burden. In the prospective TRACERx lung cancer study, thymic health was positively associated with T cell receptor diversity and T cell receptor excision circles, and correlated with immune-system signalling pathways, supporting radiographic thymic health as a proxy for thymic activity and adaptive immune competence. Analysis across patients with melanoma, breast cancer or renal cancer demonstrated pan-cancer relevance. Together, these findings identify thymic health as a previously unrecognized, tumour-agnostic determinant of immunotherapy efficacy, with potential implications for patient stratification, treatment timing and the development of immune-rejuvenating strategies in precision immuno-oncology.

## High-signal PDF head

```
Article

Thymic health and immunotherapy
outcomes in patients with cancer

https://doi.org/10.1038/s41586-026-10243-x                      Simon Bernatz1,2,3,4,15, Vasco Prudente1,2,3,15, Suraj Pai1,2,3,15, Asbjørn K. Attermann1,5,6,7,15,
                                                                Alessandro Di Federico8, Andrew Rowan9, Selvaraju Veeriah9,10,11, Lars Dyrskjøt5,6,
Received: 13 January 2025
                                                                Leonard Nürnberg1,2,3, Joao V. Alessi8, Patrick A. Ott8, Elad Sharon8, Allan Hackshaw12,
Accepted: 5 February 2026                                       Nicholas McGranahan10,13, Christopher Abbosh10, Raymond H. Mak1,2, Danielle Bitterman1,2,
                                                                Mark Awad8, Biagio Ricciuti8, Charles Swanton9,10,11,16, Mariam Jamal-Hanjani10,11,14,16,
Published online: 18 March 2026
                                                                Nicolai J. Birkbak5,6,7,16 & Hugo J. W. L. Aerts1,2,3,16 ✉
Open access

    Check for updates
                                                                Although immunotherapy has revolutionized cancer treatment, many patients still
                                                                experience limited benefit, highlighting the urgent need for improved biomarkers1.
                                                                Although immunotherapy is founded on unleashing T cells2, most existing
         
```

## Sources

- Local PDF: `raw/inbox/papers/bernatz-2026-thymic-health-immunotherapy-outcomes-patients-cancer.pdf`
- DOI: <https://doi.org/10.1093/nar/gkad1025>
- PubMed: <https://pubmed.ncbi.nlm.nih.gov/41851467/>
- PMC: <https://pmc.ncbi.nlm.nih.gov/articles/PMC10767911/>
