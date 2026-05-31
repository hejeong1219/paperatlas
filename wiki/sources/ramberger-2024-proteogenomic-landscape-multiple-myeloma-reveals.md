---
title: "The proteogenomic landscape of multiple myeloma reveals insights into disease biology and therapeutic opportunities."
year: 2024
journal: "Nature cancer"
doi: "10.1038/s43018-024-00784-3"
pmid: "38942927"
pmcid: "PMC11358022"
paper_kind: proteogenomic
pdf: "raw/inbox/papers/ramberger-2024-proteogenomic-landscape-multiple-myeloma-reveals.pdf"
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
cm_axis: phospho
---
# The proteogenomic landscape of multiple myeloma reveals insights into disease biology and therapeutic opportunities.

_Nature cancer, 2024._ PMID: [38942927](https://pubmed.ncbi.nlm.nih.gov/38942927/).

DOI: [10.1038/s43018-024-00784-3](https://doi.org/10.1038/s43018-024-00784-3)

## Summary

Multiple myeloma (MM) is a plasma cell malignancy of the bone marrow. Despite therapeutic advances, MM remains incurable, and better risk stratification as well as new therapies are therefore highly needed. The proteome of MM has not been systematically assessed before and holds the potential to uncover insight into disease biology and improved prognostication in addition to genetic and transcriptomic studies. Here we provide a comprehensive multiomics analysis including deep tandem mass tag-based quantitative global (phospho)proteomics, RNA sequencing, and nanopore DNA sequencing of 138 primary patient-derived plasma cell malignancies encompassing treatment-naive MM, plasma cell leukemia and the premalignancy monoclonal gammopathy of undetermined significance, as well as healthy controls. We found that the (phospho)proteome of malignant plasma cells are highly deregulated as compared with healthy plasma cells and is both defined by chromosomal alterations as well as posttranscriptional regulation. A prognostic protein signature was identified that is associated with aggressive disease independent of established risk factors in MM. Integration with functional genetics and single-cell RNA sequencing revealed general and genetic subtype-specific deregulated proteins and pathways in plasma cell malignancies that include potential targets for (immuno)therapies. Our study demonstrates the potential of proteogenomics in cancer and provides an easily accessible resource for investigating protein regulation and new therapeutic approaches in MM.

## Multi-Omics Identification Extraction

- Cohort/scope: 138 primary patient-derived plasma cell malignancy samples, including treatment-naive multiple myeloma, plasma cell leukemia, MGUS, and healthy controls.
- Proteome: over 10,000 proteins identified; 8,336 proteins quantified in at least half of the samples.
- Phosphoproteome: over 50,000 phosphopeptides identified; 25,131 phosphopeptides quantified in at least half of the samples.
- Acetylome: not reported as a separate acetylome layer in the local PDF.
- MS method: TMTpro 16-plex global proteomics and phosphoproteomics; high-pH peptide fractionation; immobilized metal affinity chromatography phosphopeptide enrichment; MaxQuant search and TMT processing.
- Instrument/platform: Q Exactive HF-X for TMT global proteome and phosphoproteome acquisition; Q Exactive Plus and DIA-NN are also used for separate label-free/DIA cell-line follow-up experiments.
- Extraction evidence: local PDF reports over 10,000 proteins and 50,000 phosphopeptides identified, with 8,336 proteins and 25,131 phosphopeptides quantified in at least half of samples; Methods report TMTpro 16-plex, IMAC enrichment, Q Exactive HF-X, and MaxQuant.
- Interpretation note: use 10,000+ and 50,000+ as identification-scale values only if the visualization can show approximate values; use 8,336 and 25,131 for quantified comparison.

## Batch PDF Ingest Status

- Status: `pdf-text-extracted` on 2026-05-13.
- Local PDF: `raw/inbox/papers/ramberger-2024-proteogenomic-landscape-multiple-myeloma-reveals.pdf`.
- Extracted text length: 131,573 characters.
- Scope note: automated local-PDF text ingest for the 100-paper drug-response/phospho-global batch; not yet a manual full-text deep-dive.
- Evidence boundary: downstream scientific claims should use this page only after source-specific Key Points are manually promoted or rechecked against the local PDF.
- High-signal PDF snippets:
  - nature cancer Resource https://doi.org/10.1038/s43018-024-00784-3 The proteogenomic landscape of multiple myeloma reveals insights into disease biology and therapeutic opportunities Received: 21 December 2022 A list of authors and their affiliations appears at the end of the paper Accepted: 15 May 2024 Published online: 28 Ju...
  - Here we provide a comprehensive multiomics analysis including deep tandem mass tag-based quantitative global (phospho)proteomics, RNA sequencing, and nanopore DNA sequencing of 138 primary patient-derived plasma cell malignancies encompassing treatment-naive MM, plasma cell leukemia and the premalignancy monoclonal gammopathy...
  - Our study demonstrates the potential of proteogenomics in cancer and provides an easily accessible resource for investigating protein regulation and new therapeutic approaches in MM.
  - The introduction of effective Primary genetic events define the cytogenetic subgroups of MM2 and therapies including thalidomide analogs, proteasome inhibitors and are associated with a distinct gene expression profile3,4.
  - Compensation effects of CNAs from RNA to protein levels gain or amplification of chromosome 1q and mutations in NRAS, KRAS, were especially observed for ribosomal, spliceosome and proteasome TP53, TENT5C (FAM46C) and DIS3 (refs.

## Key Points

- The paper provides a TMT-based proteogenomic and phosphoproteomic atlas of plasma cell malignancies.
- Phosphoproteomic pathway clustering identifies a high-risk subgroup independent of genetic lesions.
- The paper is a proteome/phosphoproteome study, not an acetylome study.

## Open Questions

- Should the interactive display the approximate identified counts (`>10,000`, `>50,000`) or only the exact quantified-in-half counts?

## Cancer Multiomics Project Relevance

- Cancer Multiomics 과제의 “WGS/구조변이·CNA 축”과 “phosphoproteome/kinase signaling 축”을 연결할 때, **nanopore whole-genome DNA sequencing 기반 CNV + TMT phosphoproteomics 통합**이라는 설계 자체가 직접 참고가 된다.
- 코호트 내 고위험군을 genetic lesion과 독립적으로 phosphoproteomic pathway clustering으로 분리한 사례는, Cancer Multiomics에서 “genome feature가 약할 때”도 기능 상태 기반 분류가 가능한지 검증하는 레퍼런스로 유용하다.

## Connections

- [Multiomics Proteomics PTM Identification](../topics/multiomics-proteomics-ptm-identification.md)
- [Cancer Multiomics Proteogenomic Atlas](../topics/cancer-multiomics-literature.md)
- [Cancer Multiomics brief: Ramsberger 2024](../analyses/cancer-multiomics-literature/ramberger-2024-proteogenomic-landscape-multiple-myeloma-reveals.md)

## Sources

- Local PDF: `raw/inbox/papers/ramberger-2024-proteogenomic-landscape-multiple-myeloma-reveals.pdf`
- PubMed: <https://pubmed.ncbi.nlm.nih.gov/38942927/>
- DOI: <https://doi.org/10.1038/s43018-024-00784-3>
- PMC: <https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11358022/>
