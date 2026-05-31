---
title: "Sensitive neoantigen discovery by real-time mutanome-guided immunopeptidomics"
authors:
  - "Shapiro"
  - "Huber"
  - "Michaux"
  - "Bassani-Sternberg"
year: 2025
journal: "Nature Communications"
doi: "10.1038/s41467-025-62647-4"
pmid: "40775223"
paper_kind: methods
cancer_types:
  - "uveal melanoma (example application)"
modalities:
  - "WES"
  - "RNA-seq"
  - "immunopeptidomics"
  - "real-time MS acquisition"
themes:
  - "neoantigen-discovery"
  - "immunopeptidomics-workflow"
  - "real-time-search"
  - "targeted-acquisition"
tags:
  - "cancer-multiomics"
  - "local-pdf-ingest"
extra_topics:
  - "cancer-multiomics"
pdf: "raw/inbox/papers/shapiro-2025-sensitive-neoantigen-discovery-real-time-mutanome-guided.pdf"
topic: bcell-neoantigen

---
# Sensitive neoantigen discovery by real-time mutanome-guided immunopeptidomics

## Summary

NeoDiscMS extends the NeoDisc clinical antigen discovery pipeline to enable real-time, NGS-guided immunopeptidomics acquisitions that preserve global depth while increasing sensitivity for prioritized candidate neoantigens and tumor antigens. The method combines (1) a targeted real-time search branch (triggering high-sensitivity scans when a precursor matches an inclusion list and retention-time window) and (2) a discovery branch using wider isolation windows and chimeric-spectrum deconvolution to retain global peptide coverage. The paper includes concrete data/code availability for clinical-style deployments.

## Key Points

- Pipeline context: NeoDiscMS is integrated into NeoDisc and targets end-to-end clinical antigen discovery (NGS → candidate list → immunopeptidomics acquisition → identification/prioritization).
- Acquisition design: a 3-second cycle partitions time across MS1, a targeted branch (real-time search on scouting scans; triggers high-sensitivity scans), and a discovery branch (DDA) for global coverage.
- Discovery-branch boost: uses wider isolation windows (e.g., 3.2 Th) and chimeric-spectrum deconvolution (MSFragger DDA+ mode) to recover identifications from co-isolated precursors.
- Reported sensitivity gain: tumor-associated antigen detection improves “up to ~20%” compared to a gold-standard acquisition scheme (as stated in the PDF).
- Example clinical application: in an uveal melanoma case with three lesions, NeoDiscMS identifies 14,797 / 16,033 / 11,968 unique peptides per lesion (numbers as reported in the PDF text).
- Data availability (as stated in PDF): PRIDE/ProteomeXchange deposit `PXD059824` for raw files/RTS tables/PSMs; WES/RNA-seq for lesions deposited to EGA `EGAD50000001422`.
- Code availability (as stated in PDF): NeoDiscMS is integrated within NeoDisc and is available via the NeoDisc site.

## Cancer Multiomics Project Relevance

- Cancer Multiomics 과제에서 “WGS 기반 neoantigen 후보”를 실제 검증 후보로 좁힐 때, **NGS-guided immunopeptidomics**를 임상 TAT 제약 안에 넣는 acquisition 설계(reference)가 된다.
- WGS-only prediction 대비, “측정 기반(자연 제시 peptide)” 확인 루틴을 어디에 붙일지(샘플량, sensitivity vs depth trade-off)를 구체화하는 데 유용하다.

## Connections

- [Cancer Multiomics Proteogenomic Atlas](../topics/cancer-multiomics-literature.md)
- [B-Cell Neoantigen Research Map](../topics/b-cell-neoantigen-human-cancer.md)

## Sources

- Local PDF: `raw/inbox/papers/shapiro-2025-sensitive-neoantigen-discovery-real-time-mutanome-guided.pdf`
