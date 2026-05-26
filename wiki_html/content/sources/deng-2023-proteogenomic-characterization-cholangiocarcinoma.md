---
title: "Proteogenomic characterization of cholangiocarcinoma."
year: 2023
journal: "Hepatology (Baltimore, Md.)"
doi: "10.1002/hep.32624"
pmid: "35716043"
pmcid: "PMC9869950"
paper_kind: proteogenomic
pdf: "raw/inbox/papers/deng-2023-proteogenomic-characterization-cholangiocarcinoma.pdf"
topic: multiomics-proteomics-ptm-identification
tags:
  - "multiomics-proteomics-ptm-identification"
  - "proteomics"
  - "phosphoproteomics"
  - "acetylomics"
  - "cancer-proteomics"
  - "mass-spectrometry"
themes:
  - "multiomics-identification"
  - "proteome-scale"
  - "ptm-proteomics"
  - "ms-methodology"
batch_ingest_status: pdf-text-extracted
batch_ingested_on: 2026-05-13
---
# Proteogenomic characterization of cholangiocarcinoma.

_Hepatology (Baltimore, Md.), 2023._ PMID: [35716043](https://pubmed.ncbi.nlm.nih.gov/35716043/).

DOI: [10.1002/hep.32624](https://doi.org/10.1002/hep.32624)

## Summary

Cholangiocarcinoma (CCA) is a highly heterogeneous cancer with limited understanding and few effective therapeutic approaches. We aimed at providing a proteogenomic CCA characterization to inform biological processes and treatment vulnerabilities. Integrative genomic analysis with functional validation uncovered biological perturbations downstream of driver events including DPCR1 , RBM47 mutations, SH3BGRL2 copy number alterations, and FGFR2 fusions in CCA. Proteomic clustering identified three subtypes with distinct clinical outcomes, molecular features, and potential therapeutics. Phosphoproteomics characterized targetable kinases in CCA, suggesting strategies for effective treatment with CDK and MAPK inhibitors. Patients with CCA with HBV infection showed increased antigen processing and presentation (APC) and T cell infiltration, conferring a favorable prognosis compared with those without HBV infection. The characterization of extrahepatic CCA recommended the feasible application of vascular endothelial-derived growth factor inhibitors. Multiomics profiling presented distinctive molecular characteristics of the large bile duct and the small bile duct of intrahepatic CCA. The immune landscape further revealed diverse tumor immune microenvironments, suggesting immune subtypes C1 and C5 might benefit from immune checkpoint therapy. TCN1 was identified as a potential CCA prognostic biomarker, promoting cell growth by enhancing vitamin B12 metabolism. We characterized the proteogenomic landscape of 217 CCAs with 197 paired normal adjacent tissues and identified their subtypes and potential therapeutic targets. The multiomics analyses with other databases and some functional validations have indicated strategies regarding the clinical, biological, and therapeutic approaches to the management of CCA.

## Multi-Omics Identification Extraction

- Cohort/scope: 217 cholangiocarcinomas with 197 paired adjacent normal tissues; FFPE samples profiled by WES, RNA-seq, proteomics, and phosphoproteomics.
- Proteome: 14,994 proteins identified; 6,875 proteins retained after filtering for downstream analysis.
- Phosphoproteome: 40,682 phosphopeptides identified, covering 32,219 high-confidence phosphosites from 8,398 phosphoproteins; 3,398 phosphosites retained after filtering for downstream analysis.
- Acetylome: not reported as a separate acetylome layer in the local PDF.
- MS method: FFPE proteome and phosphoproteome profiling; phosphoproteomic layer used for KSEA and kinase/substrate interpretation.
- Instrument/platform: not named in the extractable main PDF text; supplementary methods or data records should be checked before using an instrument label in the public plot.
- Extraction evidence: local PDF Results reports 14,994 proteins, 40,682 phosphopeptides, 32,219 phosphosites, 8,398 phosphoproteins, and filtered analysis sets of 6,875 proteins and 3,398 phosphosites.
- Interpretation note: show both raw identified and filtered analysis counts where the interactive allows it; use raw identified counts for scale comparison and filtered counts for analysis-depth caveats.

## Batch PDF Ingest Status

- Status: `pdf-text-extracted` on 2026-05-13.
- Local PDF: `raw/inbox/papers/deng-2023-proteogenomic-characterization-cholangiocarcinoma.pdf`.
- Extracted text length: 23,636 characters.
- Scope note: automated local-PDF text ingest for the 100-paper drug-response/phospho-global batch; not yet a manual full-text deep-dive.
- Evidence boundary: downstream scientific claims should use this page only after source-specific Key Points are manually promoted or rechecked against the local PDF.
- High-signal PDF snippets:
  - Received: 08 January 2022 | Revised: 15 June 2022 | Accepted: 15 June 2022 DOI: 10.1002/hep.32624 ORIGINAL ARTICLE Proteogenomic characterization of cholangiocarcinoma Mengjie Deng1 | Peng Ran1 | Lingli Chen2 | Yunzhi Wang1 | Zixiang Yu2 | Ke Cai1 | Jinwen Feng1 | Zhaoyu Qin1 | Yanan Yin1 | Subei Tan1 | Yang Liu1 | Chen Xu2 |...
  - We aimed at providing a proteogenomic CCA characterization Transplantation, Liver Cancer Institute, Zhong- shan Hospital, Fudan University, and Key to inform biological processes and treatment vulnerabilities.
  - Proteomic clustering identified three subtypes China.
  - Phosphoproteomics characterized targetable kinases in CCA, Jian‐Yuan Zhao, Institute for Development and Regenerative Cardiovascular Medicine, MOE‐ suggesting strategies for effective treatment with CDK and MAPK inhibitors.
  - The characterization of extrahepatic CCA recommended the feasible application of vascular endo- Jian Zhou, Department of Liver Surgery and Transplantation, Liver Cancer Institute, Zhong- thelial‐derived growth factor inhibitors.

## Key Points

- Proteomic clustering identifies three CCA subtypes with survival and therapeutic differences.
- Phosphoproteomics supports kinase-activity interpretation and subtype-specific therapeutic hypotheses.
- The source is suitable for the quantitative atlas as a large patient-cohort proteome/phosphoproteome study, but not an acetylome study.

## Cancer Multiomics Project Relevance

- Cancer Multiomics 과제의 핵심인 **WES/WGS 이벤트를 단백체·인산화단백체 기능 상태(kinase/pathway)로 번역**하는 대표적인 대규모 환자 코호트 proteogenomics 레퍼런스다.
- CCA라는 특정 암종이 Cancer Multiomics 코호트와 다르더라도, “(1) WES 기반 driver/SCNA → (2) protein/phosphoprotein cis-effect/functional state → (3) subtype/therapy hypothesis”의 분석 구성은 재사용 가능하다.
- 면역 관련 feature(항원제시/침윤 등)와 phosphoproteome 기반 kinase 해석을 함께 두는 구조라, “WGS + phosphoproteomics로 치료반응/내성 feature를 설명”하려는 과제 방향과 직접 맞닿는다.

## Open Questions

- Which exact LC-MS/MS instrument and enrichment workflow are listed in the supplementary methods?

## Connections

- [Multiomics Proteomics PTM Identification](../topics/multiomics-proteomics-ptm-identification.md)
- [Cancer Multiomics Literature Monitor](../topics/cancer-multiomics-literature.md)

## Sources

- Local PDF: `raw/inbox/papers/deng-2023-proteogenomic-characterization-cholangiocarcinoma.pdf`
- PubMed: <https://pubmed.ncbi.nlm.nih.gov/35716043/>
- DOI: <https://doi.org/10.1002/hep.32624>
- PMC: <https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9869950/>
