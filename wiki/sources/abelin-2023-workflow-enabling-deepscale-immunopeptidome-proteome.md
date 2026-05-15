---
title: "Workflow enabling deepscale immunopeptidome, proteome, ubiquitylome, phosphoproteome, and acetylome analyses of sample-limited tissues."
authors:
  - "Abelin"
  - "Bergstrom"
  - "Rivera"
year: "2023"
journal: "Nature communications"
doi: "10.1038/s41467-023-37547-0"
pmid: "37012232"
pmcid: "PMC10070353"
paper_kind: proteogenomic
pdf: "raw/inbox/papers/abelin-2023-workflow-enabling-deepscale-immunopeptidome-proteome.pdf"
topic: ptmanchor
tags:
  - "ptmanchor"
  - "proteomics"
  - "ptm"
  - "phosphoproteomics"
  - "cancer-proteomics"
  - "pmid-37012232"
themes:
  - "ptm-correction"
  - "kinase-signaling"
  - "cancer-proteomics"
batch_ingest_status: pdf-text-extracted
batch_ingested_on: 2026-05-13
---
# Workflow enabling deepscale immunopeptidome, proteome, ubiquitylome, phosphoproteome, and acetylome analyses of sample-limited tissues.

_Nature communications, 2023._ PMID: [37012232](https://pubmed.ncbi.nlm.nih.gov/37012232/).

DOI: [10.1038/s41467-023-37547-0](https://doi.org/10.1038/s41467-023-37547-0)

## Summary

Serial multi-omic analysis of proteome, phosphoproteome, and acetylome provides insights into changes in protein expression, cell signaling, cross-talk and epigenetic pathways involved in disease pathology and treatment. However, ubiquitylome and HLA peptidome data collection used to understand protein degradation and antigen presentation have not together been serialized, and instead require separate samples for parallel processing using distinct protocols. Here we present MONTE, a highly sensitive multi-omic native tissue enrichment workflow, that enables serial, deep-scale analysis of HLA-I and HLA-II immunopeptidome, ubiquitylome, proteome, phosphoproteome, and acetylome from the same tissue sample. We demonstrate that the depth of coverage and quantitative precision of each 'ome is not compromised by serialization, and the addition of HLA immunopeptidomics enables the identification of peptides derived from cancer/testis antigens and patient specific neoantigens. We evaluate the technical feasibility of the MONTE workflow using a small cohort of patient lung adenocarcinoma tumors.

## Batch PDF Ingest Status

- Status: `pdf-text-extracted` on 2026-05-13.
- Local PDF: `raw/inbox/papers/abelin-2023-workflow-enabling-deepscale-immunopeptidome-proteome.pdf`.
- Extracted text length: 38,731 characters.
- Scope note: automated local-PDF text ingest for the 100-paper drug-response/phospho-global batch; not yet a manual full-text deep-dive.
- Evidence boundary: downstream scientific claims should use this page only after source-specific Key Points are manually promoted or rechecked against the local PDF.
- High-signal PDF snippets:
  - Carr 1 Serial multi-omic analysis of proteome, phosphoproteome, and acetylome provides insights into changes in protein expression, cell signaling, cross-talk and epigenetic pathways involved in disease pathology and treatment.
  - Here we present MONTE, a highly sensitive multi-omic native tissue enrichment workﬂow, that enables serial, deep-scale analysis of HLA-I and HLA-II immunopeptidome, ubiquitylome, proteome, phosphoproteome, and acetylome from the same tissue sample.
  - Mass spectrometry–based proteomics is a standing the molecular pathways driving disease progression.
  - These proven technology for parallel analyses that involve the characteriza- investigations routinely leverage deep-scale, multi-omic characteriza- tion of cell surface immunopeptidomes along with intracellular tions to broadly survey diverse biological pathways, such as cell sig- proteins and their post-translational modiﬁca...
  - Therefore, workﬂows that ﬂow-throughs of the UbiFast enrichment step containing unlabeled, facilitate a shift from parallel to serial multi-omic data collection are non-K-ɛ-GG peptides are further processed for deep-scale and highly advantageous for large-scale discovery efforts in patient cohorts, as multiplexed measurement ...

## Key Points

- MONTE is a serial sample-limited tissue workflow, not a large patient atlas; it is useful for the interactive atlas mainly as a methods/platform reference for simultaneous proteome, phosphoproteome, acetylome, ubiquitylome, and immunopeptidome acquisition.
- The paper demonstrates that sequential HLA-I/HLA-II immunopeptidome capture can be combined with downstream UbiFast, proteome, phosphoproteome, and acetylome workflows without losing the main PTM readouts.
- The LUAD demonstration and PDX validation make this a strong source for PTM method and instrument metadata, while cohort-scale biological conclusions should be treated cautiously because the workflow validation uses small sample sets.

## Multi-Omics Identification Extraction

This section was added for the interactive atlas on recent multi-omics proteomics/PTM identification scale. Values are taken from the local PDF and preserve the paper's own reporting unit.

- Cohort/scope: MONTE workflow validation using patient lung adenocarcinoma tissues and PDX material; included as a workflow/method paper rather than a population-scale tumor cohort.
- Proteome: PDX validation reports 9,402 proteins identified and quantified in the UbiFast flow-through experiment.
- Phosphoproteome: PDX validation reports 28,523 phosphorylation sites identified and quantified; LUAD MONTE comparison reports 26,681 phosphosites / 6,745 phosphoproteins in the no-HLA branch and 22,339 phosphosites / 6,235 phosphoproteins in the HLA-flow-through branch.
- Acetylome: PDX validation reports 6,294 lysine acetylation sites identified and quantified; LUAD MONTE comparison reports 3,702 internal K-acetylsites in the no-HLA branch and 5,380 internal K-acetylsites in the HLA-flow-through branch.
- MS method: MONTE serial HLA-I/HLA-II immunopeptidome capture followed by UbiFast K-e-GG, proteome, AssayMAP IMAC phosphopeptide enrichment, and PTMScan acetyl-lysine enrichment; TMTpro/TMT multiplexing; Spectrum Mill database search and TMT quantification.
- Instrument/platform: Orbitrap Exploris 480 LC-MS/MS platform is reported for the workflow runs.
- Extraction evidence: local PDF Results and Methods report the PDX 9,402 protein / 28,523 phosphosite / 6,294 acetylsite validation counts and LUAD branch-specific phosphosite and acetylsite counts.
- Interpretation note: Use as a methods point for serialized multi-omics depth and instrument design, not as a direct comparison to tumor-cohort CPTAC-style atlases.


## Connections

- [Ptmanchor Topic Hub](../topics/ptm-correction-and-kinase-signaling-in-cancer-proteomics.md)
- [Ptmanchor Anchor](../analyses/ptmanchor-manuscript-anchor.md)
- [Multiomics Proteomics PTM Identification](../topics/multiomics-proteomics-ptm-identification.md)

## Sources

- Local PDF: `raw/inbox/papers/abelin-2023-workflow-enabling-deepscale-immunopeptidome-proteome.pdf`
- PubMed: <https://pubmed.ncbi.nlm.nih.gov/37012232/>
- DOI: <https://doi.org/10.1038/s41467-023-37547-0>
- PMC: <https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10070353/>
