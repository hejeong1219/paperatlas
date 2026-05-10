---
title: "Proteogenomic analysis reveals non-small cell lung cancer subtypes predicting chromosome instability, and tumor microenvironment"
year: 2024
journal: "Nature Communications"
doi: "10.1038/s41467-024-54434-4"
pmid: "39580524"
pmcid: "PMC11585665"
paper_kind: resource
cancer_types:
  - non-small-cell-lung-cancer
modalities:
  - proteogenomics
  - phosphoproteomics
  - acetylproteomics
  - whole-exome-sequencing
  - neoantigen-analysis
themes:
  - molecular-subtypes
  - wgd
  - pi3k-akt
  - tumor-microenvironment
  - adjuvant-therapy
tags:
  - source
  - cancer-multiomics
  - non-small-cell-lung-cancer
  - proteogenomics
  - phosphoproteomics
  - acetylproteomics
  - pmid-39580524
pdf: "raw/inbox/papers/song-2024-proteogenomic-analysis-reveals-non-small-cell.pdf"
---
# Proteogenomic analysis reveals non-small cell lung cancer subtypes predicting chromosome instability, and tumor microenvironment

_Nature Communications, 2024._ PMID: [39580524](https://pubmed.ncbi.nlm.nih.gov/39580524/).

DOI: [10.1038/s41467-024-54434-4](https://doi.org/10.1038/s41467-024-54434-4)

## Summary

Korean NSCLC cohort multi-omics study that defines five molecular subtypes (beyond LUAD/LSCC histology) and links them to chromosome instability (including WGD), signaling programs (including PI3K–Akt), tumor microenvironment composition, and prognosis; includes a replication cohort from prior multi-omics studies.

## Multi-Omics Identification Extraction

- Cohort/scope: 229 Korean NSCLC tumors (surgery 2010–2019; Asan Medical Center, Seoul) + 462-patient replication cohort from prior multi-omics studies.
- Genomics: WES for 228 tumors (normal-adjacent matched plus a small set of tumor-only); WGD/chromosome-instability analyses.
- Transcriptome: bulk RNA-seq for 205 tumors and 85 matched normal-adjacent tissues (as reported in the main PDF text).
- Proteome/PTM: TMT-based proteomics; reports 10,788 proteins, 40,738 phosphosites, and 5,975 acetylation sites observed in ≥30% of samples.
- Immunology: tumor microenvironment characterization plus neoantigen-load comparisons across subtypes (pipeline details should be verified in Methods/Supplement before reuse).

## Key Points

- Defines five “multi-omics subtypes” that cut across LUAD/LSCC histology, including a PI3K–Akt–upregulated subtype associated with metastasis and poor survival.
- Reports proliferative subtypes that associate strongly with whole-genome doubling (WGD) events, framing chromosome instability as a proteogenomic subtype axis.
- Uses proteome, phosphoproteome, and acetylproteome layers (TMT) at cohort scale, enabling kinase/signaling interpretation beyond RNA.
- Compares tumor microenvironment composition and neoantigen load across subtypes and relates “immune-hot” states to prognosis and adjuvant-therapy efficacy signals.

## Cancer Multiomics Project Relevance

- 한국인(NSCLC) 대규모 코호트에서 **WES + proteome + phosphoproteome(+acetylome)**를 함께 써서 “형태학(LUAD/LSCC)보다 기능적 subtype이 예후/치료 맥락을 더 잘 분리할 수 있음”을 보여주는 레퍼런스다.
- Cancer Multiomics 과제의 “WGS(또는 WES)만으로 설명되지 않는 반응성 차이”를 **phosphoproteome/kinase network**와 면역 feature(neoantigen/침윤)로 보완하는 분석 구성에 직접 참고 가능하다.

## Open Questions

- Neoantigen-load 계산(사용한 HLA typing/variant calling/prediction 도구)이 무엇인지 Methods/Supplement에서 확인 필요.

## Connections

- [Cancer Multiomics Literature Monitor](../topics/cancer-multiomics-literature.md)
- [PTM Correction and Kinase Signaling in Cancer Proteomics](../topics/ptm-correction-and-kinase-signaling-in-cancer-proteomics.md)

## Sources

- Local PDF: `raw/inbox/papers/song-2024-proteogenomic-analysis-reveals-non-small-cell.pdf`
- PubMed: <https://pubmed.ncbi.nlm.nih.gov/39580524/>
- DOI: <https://doi.org/10.1038/s41467-024-54434-4>
- PMC: <https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11585665/>
