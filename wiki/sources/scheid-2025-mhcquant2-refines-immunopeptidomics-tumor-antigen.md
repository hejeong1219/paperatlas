---
title: "MHCquant2 refines immunopeptidomics tumor antigen discovery"
authors:
  - "Scheid"
  - "Lemke"
  - "Walz"
  - "Nahnsen"
year: 2025
journal: "Genome Biology"
doi: "10.1186/s13059-025-03763-8"
pmid: "40983925"
paper_kind: software
modalities:
  - "immunopeptidomics"
  - "Nextflow (nf-core)"
  - "OpenMS"
  - "DeepLC"
  - "MS2PIP"
themes:
  - "immunopeptidomics-workflow"
  - "pipeline-standardization"
  - "neoantigen-discovery"
tags:
  - "cancer-multiomics"
  - "local-pdf-ingest"
extra_topics:
  - "cancer-multiomics"
pdf: "raw/inbox/papers/scheid-2025-mhcquant2-refines-immunopeptidomics-tumor-antigen.pdf"
topic: bcell-neoantigen

---
# MHCquant2 refines immunopeptidomics tumor antigen discovery

## Summary

MHCquant2 is an open-source, nf-core integrated Nextflow pipeline for scalable immunopeptidomics identification and quantification with an emphasis on reproducibility and high sensitivity. It combines OpenMS-based processing with peptide-property predictors (DeepLC, MS2PIP) and rescoring to improve peptide identifications and to standardize large-scale HLA peptide datasets. The work also builds and applies a large benign immunopeptidome reference to refine tumor-associated antigen definition and to support discovery of tumor-exclusive antigens and low-abundance neoepitopes.

## Key Points

- Workflow: modular Nextflow DSL2 pipeline integrated into nf-core, designed for reproducible immunopeptidomics processing across platforms and infrastructures.
- Sensitivity claim (as stated in PDF): integrates OpenMS, DeepLC, and MS2PIP, improving peptide identifications by up to ~27% across diverse MS platforms.
- Reference resource: introduces a novel benign immunopeptidomics dataset (`benignMHCquant2`, n=92) and merges it with existing benign datasets into a comprehensive benign reference.
- Benign reference scale (as stated in PDF): comprehensive benign reference includes 420 HLA class I samples (213,462 unique binders) and 415 HLA class II samples (423,438 peptides); `benignMHCquant2` contributes substantial new binders/peptides to this reference.
- Tumor antigen refinement: uses the expanded benign reference to filter putative TAAs and to prioritize tumor-exclusive peptides; re-analyses published AML/CLL/OvCa and melanoma datasets to demonstrate impact.
- Data availability (as stated in PDF): the dataset generated in the study is deposited to PRIDE under `PXD058436`.
- Code availability (as stated in PDF): pipeline is available via nf-core/GitHub and archived on Zenodo (versioned release cited in the PDF).

## Cancer Multiomics Project Relevance

- Cancer Multiomics 과제에서 “WGS 기반 neoantigen 후보”를 immunopeptidomics로 확인/정량하는 경우, **재현 가능한 표준 파이프라인(nf-core)** 레퍼런스로 바로 사용할 수 있다.
- “benign reference로 TAA를 정의/필터링”하는 프레임은, 한국인 코호트에서 on-target/off-tumor 리스크를 더 보수적으로 관리하려는 논리의 기반이 된다.

## Connections

- [Cancer Multiomics Proteogenomic Atlas](../topics/cancer-multiomics-literature.md)
- [B-Cell Neoantigen Research Map](../topics/b-cell-neoantigen-human-cancer.md)

## Sources

- Local PDF: `raw/inbox/papers/scheid-2025-mhcquant2-refines-immunopeptidomics-tumor-antigen.pdf`
