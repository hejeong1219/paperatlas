---
title: "Pan-cancer proteogenomics expands the landscape of therapeutic targets"
authors:
  - "Savage"
  - "Yi"
  - "Lei"
  - "Wen"
  - "Zhang"
year: 2024
journal: "Cell"
doi: "10.1016/j.cell.2024.05.039"
pmid: "38917788"
pmcid: "PMC12010439"
paper_kind: proteogenomic
cancer_types:
  - "BRCA"
  - "CCRCC"
  - "COAD"
  - "GBM"
  - "HNSCC"
  - "LUAD"
  - "LSCC"
  - "OV"
  - "PDAC"
  - "UCEC"
modalities:
  - "proteogenomics"
  - "proteomics"
  - "phosphoproteomics"
  - "genomics"
  - "transcriptomics"
themes:
  - "therapeutic-target-discovery"
  - "druggability"
  - "synthetic-lethality"
  - "neoantigen-discovery"
tags:
  - "cancer-multiomics"
  - "local-pdf-ingest"
extra_topics:
  - "cancer-multiomics"
pdf: "raw/inbox/papers/savage-2024-pan-cancer-proteogenomics-expands-landscape-therapeutic.pdf"
batch_ingest_status: pdf-text-extracted
batch_ingested_on: 2026-05-13
---
# Pan-cancer proteogenomics expands the landscape of therapeutic targets

## Summary

This study integrates harmonized CPTAC pan-cancer proteogenomics (10 cancer types; 1,043 tumors) to map the abundance and regulation of a curated set of druggable proteins and to prioritize therapeutic opportunities that are invisible or unreliable at the mRNA level. The workflow combines tumor proteomics/phosphoproteomics with additional public resources (e.g., genetic screens and drug response data) to nominate druggable dependencies and synthetic-lethal opportunities, and extends the target landscape to peptide targets (candidate “public” neoantigens such as mutant KRAS peptides and shared tumor-associated antigens), with results organized into a companion web portal.

## Batch PDF Ingest Status

- Status: `pdf-text-extracted` on 2026-05-13.
- Local PDF: `raw/inbox/papers/savage-2024-pan-cancer-proteogenomics-expands-landscape-therapeutic.pdf`.
- Extracted text length: 24,831 characters.
- Scope note: automated local-PDF text ingest for the 100-paper drug-response/phospho-global batch; not yet a manual full-text deep-dive.
- Evidence boundary: downstream scientific claims should use this page only after source-specific Key Points are manually promoted or rechecked against the local PDF.
- High-signal PDF snippets:
  - Pan-cancer proteogenomics expands the landscape of therapeutic targets Sara R.
  - We integrate CPTAC proteogenomics data from 1,043 patients across 10 cancer types with additional public datasets to identify potential therapeutic targets.
  - Integration of proteomic data from tumors and genetic screen data from cell lines identifies protein overexpression- or hyperactivation-driven druggable dependencies, enabling accurate predictions of effective drug targets.
  - Proteogenomic identification of synthetic lethality provides a strategy to target tumor suppressor gene loss.
  - Combining proteogenomic analysis and MHC binding prediction prioritizes mutant KRAS peptides as promising “public” neoantigens.

## Key Points

- Dataset: harmonized CPTAC proteogenomics spanning 10 cancer cohorts (BRCA, CCRCC, COAD, GBM, HNSCC, LUAD, LSCC, OV, PDAC, UCEC), totaling 1,043 tumors (plus matched normals).
- Scope: a tiered set of 2,863 “druggable” proteins is assembled and profiled; proteomics covers most but not all druggable targets, and measured protein abundance spans orders of magnitude.
- mRNA→protein mismatch: gene-wise mRNA–protein correlations vary widely across cohorts; secreted proteins and other biology can drive weak correlations, motivating protein-level target selection rather than transcript-only heuristics.
- Target nomination logic: integrates protein abundance and phospho-activation signals with external functional evidence (e.g., cell-line genetic screens and drug response) to prioritize “overexpression/hyperactivation-driven” dependencies.
- Tumor-suppressor loss strategy: uses proteogenomic patterns around loss-of-function events to propose synthetic-lethal target strategies (targeting vulnerabilities induced by TSG loss).
- Antigen targets: combines proteogenomic context with MHC binding prediction to prioritize candidate shared (“public”) neoantigens (including mutant KRAS peptides) and nominates shared tumor-associated antigens with experimental follow-up.
- Reproducibility/availability (as stated in PDF): raw proteomics are available via CPTAC / PDC; genomics/transcriptomics via GDC; processed data via LinkedOmicsKB; results summarized in a dedicated targets portal.

## Cancer Multiomics Project Relevance

- Cancer Multiomics 과제의 “WGS 이벤트 → functional state(단백체/인산화단백체) → 약물표적” 스토리라인을, **CPTAC pan-cancer 기반의 실제 분석 틀**로 제시한다.
- 특히 “mRNA로는 잘 안 보이는 표적/신호”를 protein/phosphoprotein 상태로 해석하는 설계(타깃 후보 우선순위, synthetic lethality, 항원 후보 포함)는 과제의 예측·내성 해석 프레임을 보강한다.

## Connections

- [Cancer Multiomics Proteogenomic Atlas](../topics/cancer-multiomics-literature.md)
- [Multiomics Proteomics PTM Identification](../topics/multiomics-proteomics-ptm-identification.md)
- [PTM Correction and Kinase Signaling in Cancer Proteomics](../topics/ptm-correction-and-kinase-signaling-in-cancer-proteomics.md)

## Sources

- Local PDF: `raw/inbox/papers/savage-2024-pan-cancer-proteogenomics-expands-landscape-therapeutic.pdf`
