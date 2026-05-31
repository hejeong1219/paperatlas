---
title: "IGHG1+ malignant epithelial Cell-myCAF crosstalk via MIF-CD74/APP-CD74 drives early brain metastasis in NSCLC: Delineated via primary tumor-brain metastasis single-cell and spatial transcriptomics"
authors:
  - "Yang"
  - "Yang"
  - "Zhao"
  - "Wen"
  - "Wu"
year: 2026
journal: "Cancer letters"
doi: "10.1016/j.canlet.2026.218451"
pmid: "41881335"
pdf: "raw/inbox/papers/yang-2026-ighg-malignant-epithelial-cell-mycaf-crosstalk.pdf"
paper_kind: research
cancer_types:
  - "non-small-cell-lung-cancer"
  - "small-cell-lung-cancer"
themes:
  - "clinical-translation"
  - "single-cell"
  - "spatial-omics"
  - "treatment-response"
topic: cancer-multiomics-literature
discovery_method: topic-sweep-2026-05-25
tags:
  - "cancer-lett-2026"
  - "cancer-multiomics-literature"
  - "clinical-translation"
  - "single-cell"
  - "spatial-omics"
  - "topic-sweep"
  - "treatment-response"
batch_ingest_status: topic-sweep-stub
batch_ingested_on: 2026-05-25
cm_axis: response
---

# IGHG1+ malignant epithelial Cell-myCAF crosstalk via MIF-CD74/APP-CD74 drives early brain metastasis in NSCLC: Delineated via primary tumor-brain metastasis single-cell and spatial transcriptomics

_Cancer Lett, 2026._ [10.1016/j.canlet.2026.218451](https://doi.org/10.1016/j.canlet.2026.218451) · [PubMed 41881335](https://pubmed.ncbi.nlm.nih.gov/41881335/)

## Summary

NSCLC 53명(stage I-IV)의 FFPE 시료(정상 폐, 뇌전이 동반/비동반 원발 종양 PTBrM/PTNBrM, 뇌전이 BrM, 정상 뇌)에 대해 snRNA-seq, GeoMx DSP, CosMx SMI를 통합한 spatial multi-omics 연구입니다. snRNA-seq에서 IGHG1+ malignant epithelial cell (MEC)이 PTBrM 상피의 terminal differentiation 상태로 EMT pathway에 enrichment되었으며 NL→PTBrM 섭동 점수 0.596 vs NL→PTNBrM 0.000 (P=0.002)으로 특이 반응을 보였습니다. Spatial transcriptomics에서 IGHG1+ MEC가 PTBrM의 invasive front에 위치하고 myCAF와 r=0.900으로 강하게 co-localize하며, MIF-CD74/APP-CD74 axis를 통해 양방향 상호작용함을 확인했습니다. (참고: 본 stub의 full_text 추출본은 다른 저자 동명 ESCC 논문이 끼어 있어 본 요약은 abstract에 의존합니다.)

## Key Points

- 53명 NSCLC paraffin 시료 코호트로 정상 폐·PTBrM·PTNBrM·BrM·정상 뇌의 다섯 조직 타입을 single-nucleus RNA-seq + GeoMx DSP + CosMx SMI로 통합 프로파일링했습니다.
- IGHG1+ MEC는 PTBrM 상피의 terminal differentiation 상태로 EMT pathway에 enrich되며, Augur 분석에서 NL→PTBrM과 NL→PTNBrM 간 perturbation 점수 차이가 통계적으로 유의(0.596 vs 0.000, P=0.002)했습니다.
- Spatial transcriptomics에서 IGHG1+ MEC와 myCAF가 PTBrM 변연부에서 강하게 co-localize (r=0.900)하며, MIF-CD74·APP-CD74 axis를 통한 양방향 신호 전달이 in vitro·임상에서 검증되었습니다.
- 종양 변연부의 high CD74 발현은 뇌전이의 독립적 예측인자였으며 AUC=0.776, HR=5.495로 brain metastasis-free survival 단축(37 vs 60 months, P<0.0001)과 연관되었습니다.
- CD74를 표적으로 한 doxorubicin과 milatuzumab은 in vivo에서 EMT 억제 경향을 보여, MIF-CD74 axis가 NSCLC 뇌전이 예방의 잠재적 표적임을 시사합니다. 단, 본 stub의 full_text 추출은 부분적으로 다른 논문이 섞여 있어 abstract 기반 한계가 있습니다.

## 한미암 활용 가능성

치료반응 예측 측면에서, 본 연구의 spatial niche(invasive front, IGHG1+ MEC-myCAF) 정의 + ligand-receptor (MIF-CD74/APP-CD74) inference + CD74 high를 통한 위험 분류 워크플로는 위암에서 림프절 전이·복막 전이 예측 마커를 spatial transcriptomics로 정의할 때 참고할 수 있겠습니다. 또한 CD74 high가 HR=5.495 수준의 강한 위험 분류력을 보였다는 점은 위암 단백체에서 발견 가능한 CAF-tumor 상호작용 마커의 임상적 활용 가능성을 검토해 볼 만합니다.

## Topic Sweep Ingest Status

- Status: `topic-sweep-stub` (2026-05-25)
- Topic: `cancer-multiomics-literature`
- Local PDF: `raw/inbox/papers/yang-2026-ighg-malignant-epithelial-cell-mycaf-crosstalk.pdf`
- Download path: `elsevier: https://api.elsevier.com/content/article/doi/10.1016/j.ijbiomac.2026.152654`
- Extracted text length: 30013 characters
- Scope note: automated topic-sweep batch ingest; not yet a manual full-text deep-dive.

## Abstract (PubMed)

To investigate the mechanisms of early brain metastasis in non-small cell lung cancer (NSCLC) using spatial multi-omics technology, develop predictive models, and identify potential therapeutic targets. A retrospective analysis was conducted on paraffin samples from 53 NSCLC patients (stages I-IV), including normal lung tissue (NL), primary tumors with/without brain metastasis (PTNBrM/PTBrM), brain metastases (BrM), and normal brain tissue. Integrated single-nucleus RNA sequencing, GeoMx DSP, and CosMx SMI. Augur, pseudo-time, and space communication analysis identified key cells and molecules. ROC and survival analysis evaluated predictive performance. Potential preventive targets screened from the Therapeutic Target Database. snRNA-seq revealed that IGHG1+ malignant epithelial cell (MEC) represent the terminal differentiation state of PTBrM epithelium, showing significant enrichment in EMT pathways. These cells uniquely responded to biological perturbations (NL→PTBrM vs NL→PTNBrM, 0.596 vs 0.000, P = 0.002). Spatial transcriptomics further indicated that IGHG1+ MEC predominantly localized at the invasive front of PTBrM, co-localizing with myofibroblastic cancer-associated fibroblast (myCAF; r = 0.900). Multi-omics demonstrated bidirectional interactions between IGHG1+ MEC and myCAF at PTBrM margins via MIF-CD74/APP-CD74 axes, which were also validated both clinically and in vitro. High CD74 at margins was an independent predictor of brain metastasis (AUC = 0.776; HR = 5.495), linked to shorter brain metastasis-free survival (37 vs 60 months, P < 0.0001). In vivo studies confirmed that the candidate drugs targeting CD74, doxorubicin and milatuzumab, have a tendency to inhibit EMT. IGHG1+ MEC collaborate with myCAF to shape a pro-metastatic microenvironment, with the MIF-CD74/APP-CD74 interaction network serving as a driver of NSCLC brain metastasis. CD74-targeting therapies show promising clinical potential.

## High-signal PDF head

```
Journal Pre-proof


Single-cell and spatial transcriptomics reveal SPRR2A+
epithelial-MMP1+ fibroblast interactions as key drivers of
Esophageal Squamous Cell Carcinoma progression


Wenjie Yang, Yue Chen, Fujue Wang, Wenqi Chen, Xiang Xiao,
Rong Ma, Deying Kang

PII:                   S0141-8130(26)02581-X
DOI:                   https://doi.org/10.1016/j.ijbiomac.2026.152654
Reference:             BIOMAC 152654

To appear in:          International Journal of Biological Macromolecules

Received date:         1 December 2025
Revised date:          17 May 2026
Accepted date:         20 May 2026


Please cite this article as: W. Yang, Y. Chen, F. Wang, et al., Single-cell and spatial
transcriptomics reveal SPRR2A+ epithelial-MMP1+ fibroblast interactions as key drivers
of Esophageal Squamous Cell Carcinoma progression, International Journal of Biological
Macromolecules (2024), https://doi.org/10.1016/j.ijbiomac.2026.152654


This is a PDF of an article that has undergone enhancements after acceptance, such as
the addition of a cover page and metadata, and formatting for readability. This version
will undergo additional copyediting, typesetting and review before it is published in
its final form. As such, this version is no longer the Accepted Manuscript, but it is
not yet the definitive Version of Record; we are providing this early version to give
early visibility of the article. Please note that Elsevier’s sharing policy for the Published
Journal Article applies to this versi
```

## Sources

- Local PDF: `raw/inbox/papers/yang-2026-ighg-malignant-epithelial-cell-mycaf-crosstalk.pdf`
- DOI: <https://doi.org/10.1016/j.canlet.2026.218451>
- PubMed: <https://pubmed.ncbi.nlm.nih.gov/41881335/>

