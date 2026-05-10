---
title: "Proteogenomic Landscape of Breast Cancer Tumorigenesis and Targeted Therapy."
authors:
  - "Krug"
  - "Jaehnig"
  - "Satpathy"
year: "2020"
journal: "Cell"
doi: "10.1016/j.cell.2020.10.036"
pmid: "33212010"
pmcid: "PMC8077737"
paper_kind: resource
cancer_types:
  - breast-cancer
modalities:
  - proteogenomics
  - phosphoproteomics
  - acetylproteomics
pdf: "raw/inbox/papers/krug-2020-proteogenomic-landscape-breast-cancer-tumorigenesis.pdf"
topic: bcell-neoantigen
tags:
  - "source"
  - "bcell-neoantigen"
  - "neoantigen"
  - "b-cells"
  - "tls"
  - "immunology"
  - "pmid-33212010"
themes:
  - "neoantigen-discovery"
  - "tls-biology"
  - "clinical-translation"
---
# Proteogenomic Landscape of Breast Cancer Tumorigenesis and Targeted Therapy.

_Cell, 2020._ PMID: [33212010](https://pubmed.ncbi.nlm.nih.gov/33212010/).

DOI: [10.1016/j.cell.2020.10.036](https://doi.org/10.1016/j.cell.2020.10.036)

## Summary

The integration of mass spectrometry-based proteomics with next-generation DNA and RNA sequencing profiles tumors more comprehensively. Here this "proteogenomics" approach was applied to 122 treatment-naive primary breast cancers accrued to preserve post-translational modifications, including protein phosphorylation and acetylation. Proteogenomics challenged standard breast cancer diagnoses, provided detailed analysis of the ERBB2 amplicon, defined tumor subsets that could benefit from immune checkpoint therapy, and allowed more accurate assessment of Rb status for prediction of CDK4/6 inhibitor responsiveness. Phosphoproteomics profiles uncovered novel associations between tumor suppressor loss and targetable kinases. Acetylproteome analysis highlighted acetylation on key nuclear proteins involved in the DNA damage response and revealed cross-talk between cytoplasmic and mitochondrial acetylation and metabolism. Our results underscore the potential of proteogenomics for clinical investigation of breast cancer through more accurate annotation of targetable pathways and biological features of this remarkably heterogeneous malignancy.

## Key Points

- **122 treatment-naive primary breast cancers**를 “PTM 보존 프로토콜”로 수집해 proteome/phosphoproteome/acetylome을 포함한 proteogenomics로 분석한다.
- Proteogenomics 관점에서 **표준 진단/아형 분류(예: ERBB2/HER2)**를 재점검하고, ERBB2 amplicon의 protein-level 해석을 상세히 제시한다.
- **Rb status**를 proteomics 기반으로 더 정확히 평가해 CDK4/6 inhibitor 반응성 추정의 근거를 제공한다고 주장한다.
- Phosphoproteomics로 **tumor suppressor loss ↔ targetable kinase** 연관을 제시하며, “유전→kinase signaling” 연결의 대표 예시로 활용 가능하다.

## Multi-Omics Identification Extraction

- Cohort / scope: 122 treatment-naive primary breast cancers profiled in the CPTAC-style breast cancer proteogenomic landscape.
- Proteome: 10,107 proteins after filtering for the analysis dataset; Spectrum Mill protein grouping reports aggregate protein-level FDR < 0.01% (1/10,633).
- Phosphoproteome: 38,968 phosphorylation sites in the analysis dataset; VM-site polishing yielded 63,416 phosphosites, with 70% fully localized.
- Acetylome: 9,869 acetylation sites in the analysis dataset; VM-site polishing yielded 18,392 acetylsites, with 99% fully localized to lysine.
- MS method: TMT-10 multiplexing with a common reference; high-pH reversed-phase fractionation; Fe3+-NTA/IMAC phosphopeptide enrichment; anti-acetyl-lysine antibody enrichment for acetylpeptides.
- Instrument / platform: LC-MS/MS on Orbitrap Fusion Lumos; methods materials also list Q Exactive Plus and Orbitrap Fusion Lumos, with the main MS section describing Orbitrap Fusion Lumos acquisition.
- Software / search: Spectrum Mill, QUILTS patient-specific database search, TMT reporter-ion quantification, two-component normalization, VM-site polishing.
- Extraction evidence: local PDF reports 10,107 proteins, 38,968 phosphorylation sites, and 9,869 acetylation sites in the filtered dataset; STAR Methods report TMT-10 design, enrichment methods, Orbitrap Fusion Lumos, 63,416 phosphosites, and 18,392 acetylsites.
- Interpretation note: the atlas should separate filtered analysis-feature counts from the larger VM-site-polished identification totals.

## Cancer Multiomics Project Relevance

- Cancer Multiomics의 “WGS-인산화단백체 통합 기반 반응/내성 모델”에서, **유전 이벤트(amplicon/TS loss) → phospho-signaling 기능 상태**로 이어지는 feature 설계의 레퍼런스다.
- 임상적 의사결정 포인트(HER2, CDK4/6 등)를 proteogenomics로 재정의하는 흐름은, Cancer Multiomics에서 **genome-first 가설을 protein/PTM evidence로 보정**하는 논리로 재사용 가능하다.

## Connections

- [Multiomics Proteomics PTM Identification](../topics/multiomics-proteomics-ptm-identification.md)

- [Bcell Neoantigen Topic Hub](../topics/b-cell-neoantigen-human-cancer.md)
- [Bcell Neoantigen Anchor](../analyses/b-cell-neoantigen-proposal-anchor.md)
- [Cancer Multiomics Literature Monitor](../topics/cancer-multiomics-literature.md)
- [Krug 2020 - Breast Cancer Proteogenomics (PTM-preserved; HER2/Rb/kinase)](../analyses/cancer-multiomics-literature/krug-2020-proteogenomic-landscape-breast-cancer-tumorigenesis.md)

## Sources

- Local PDF: `raw/inbox/papers/krug-2020-proteogenomic-landscape-breast-cancer-tumorigenesis.pdf`
- PubMed: <https://pubmed.ncbi.nlm.nih.gov/33212010/>
- DOI: <https://doi.org/10.1016/j.cell.2020.10.036>
- PMC: <https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8077737/>
