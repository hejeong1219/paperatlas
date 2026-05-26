---
title: "The Proteogenomics of Prostate Cancer Radioresistance."
year: 2024
journal: "Cancer research communications"
doi: "10.1158/2767-9764.CRC-24-0292"
pmid: "39166898"
pmcid: "PMC11411600"
paper_kind: proteogenomic
pdf: "raw/inbox/papers/haas-2024-proteogenomics-prostate-cancer-radioresistance.pdf"
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
# The Proteogenomics of Prostate Cancer Radioresistance.

_Cancer research communications, 2024._ PMID: [39166898](https://pubmed.ncbi.nlm.nih.gov/39166898/).

DOI: [10.1158/2767-9764.CRC-24-0292](https://doi.org/10.1158/2767-9764.CRC-24-0292)

## Summary

Prostate cancer is frequently treated with radiotherapy. Unfortunately, aggressive radioresistant relapses can arise, and the molecular underpinnings of radioresistance are unknown. Modern clinical radiotherapy is evolving to deliver higher doses of radiation in fewer fractions (hypofractionation). We therefore analyzed genomic, transcriptomic, and proteomic data to characterize prostate cancer radioresistance in cells treated with both conventionally fractionated and hypofractionated radiotherapy. Independent of fractionation schedule, resistance to radiotherapy involved massive genomic instability and abrogation of DNA mismatch repair. Specific prostate cancer driver genes were modulated at the RNA and protein levels, with distinct protein subcellular responses to radiotherapy. Conventional fractionation led to a far more aggressive biomolecular response than hypofractionation. Testing preclinical candidates identified in cell lines, we revealed POLQ (DNA Polymerase Theta) as a radiosensitizer. POLQ-modulated radioresistance in model systems and was predictive of it in large patient cohorts. The molecular response to radiation is highly multimodal and sheds light on prostate cancer lethality. Radiation is standard of care in prostate cancer. Yet, we have little understanding of its failure. We demonstrate a new paradigm that radioresistance is fractionation specific and identified POLQ as a radioresistance modulator.

## Multi-Omics Identification Extraction

- Extraction status: PDF downloaded; this study is primarily WES + RNA-seq + (subcellular) shotgun proteomics (no dedicated phosphoproteome layer identified in the extractable PDF text).
- Data layers (as described in Methods/abstract): whole-exome sequencing (WES), RNA-seq, miRNA profiling (NanoString), and proteomics with subcellular fractionation.
- Proteomics platform cues: Easy nLC 1000 coupled to a Thermo Q Exactive HF, data-dependent acquisition (top-25), long gradient (reported ~265 min).
- Open question: does any supplementary dataset report global phosphoproteomics or PTM enrichment beyond total-proteome shotgun MS?

## Batch PDF Ingest Status

- Status: `pdf-text-extracted` on 2026-05-13.
- Local PDF: `raw/inbox/papers/haas-2024-proteogenomics-prostate-cancer-radioresistance.pdf`.
- Extracted text length: 44,788 characters.
- Scope note: automated local-PDF text ingest for the 100-paper drug-response/phospho-global batch; not yet a manual full-text deep-dive.
- Evidence boundary: downstream scientific claims should use this page only after source-specific Key Points are manually promoted or rechecked against the local PDF.
- High-signal PDF snippets:
  - RESEARCH ARTICLE https://doi.org/10.1158/2767-9764.CRC-24-0292 OPEN ACCESS Downloaded from http://aacrjournals.org/cancerrescommun/article-pdf/4/9/2463/3498698/crc-24-0292.pdf by Korea University Medical Library user on 09 May 2026 The Proteogenomics of Prostate Cancer Radioresistance Roni Haas1,2,3,4, Gavin Frame5,6, Shahbaz...
  - Testing preclinical candidates identified in nings of radioresistance are unknown.
  - evolving to deliver higher doses of radiation in fewer fractions (hypo- POLQ-modulated radioresistance in model systems and was predictive of it fractionation).
  - The molecular response to radiation is highly teomic data to characterize prostate cancer radioresistance in cells treated multimodal and sheds light on prostate cancer lethality.
  - Independent of fractionation schedule, resistance to radiotherapy involved Significance: Radiation is standard of care in prostate cancer.

## Key Points

- Radiotherapy resistance can differ by fractionation schedule: conventional fractionation (CF) and hypofractionation (HF) generate distinct molecular response patterns.
- Across schedules, resistant states show widespread genomic instability and abrogation of DNA mismatch repair, linking DNA maintenance programs to radiorecurrence risk.
- Integrative multi-omic profiling nominates POLQ (DNA polymerase theta) as a radiosensitizer; genetic/pharmacologic POLQ suppression re-sensitizes resistant models.
- Subcellular fractionation proteomics provides a mechanistic layer for how radiation alters protein localization/compartmental responses beyond RNA-level effects.

## Cancer Multiomics Project Relevance

- Cancer Multiomics 과제의 “치료 내성/반응 예측” 축에서, **WES(유전적 불안정/수선 결함) + proteome 변화**를 함께 놓고 모델링하는 설계(특히 schedule-dependent phenotype 분리)가 참고가 된다.
- 본 논문은 phosphoproteomics 중심은 아니지만, Cancer Multiomics 코호트에서 인산화단백체를 추가할 경우 “(WGS/WES) 변이·불안정성 지표 → kinase signaling/기능상태 → 치료 내성” 연결 가설을 세우는 비교 기준을 제공한다.

## Open Questions

- Does the paper report total identified counts or only filtered quantified/analysis features?
- Are acetylome values directly measured, absent, or only mentioned as a search modification?
- Are method and instrument details in main Methods or supplementary methods?

## Connections

- [Multiomics Proteomics PTM Identification](../topics/multiomics-proteomics-ptm-identification.md)
- [Cancer Multiomics Proteogenomic Atlas](../topics/cancer-multiomics-literature.md)

## Sources

- Local PDF: `raw/inbox/papers/haas-2024-proteogenomics-prostate-cancer-radioresistance.pdf`
- PubMed: <https://pubmed.ncbi.nlm.nih.gov/39166898/>
- DOI: <https://doi.org/10.1158/2767-9764.CRC-24-0292>
- PMC: <https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11411600/>
