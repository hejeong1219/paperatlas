---
title: Neoantigen Discovery and Prioritization
tags:
  - neoantigen
  - prioritization
  - pipeline
  - research-axis
---

# Neoantigen Discovery and Prioritization

This axis covers how candidate neoantigens are generated, filtered, ranked, and validated before any biological or clinical interpretation.

## Key Points

- “Neoantigen” can mean multiple antigen classes; keeping the class explicit reduces false comparisons across papers (HLA-I vs HLA-II, mutation-derived vs noncanonical, predicted vs MS-observed).
- Discovery is usually the easy step; the main bottlenecks are (i) **presentation evidence** and (ii) **immunogenicity/effector relevance** in the actual tumor context.
- Proteogenomics and immunopeptidomics do not replace prediction pipelines; they change the confidence model by providing direct HLA-bound peptide evidence and revealing antigen-processing/presentation defects.
- The wiki should preserve the paper’s reporting unit and evidence type:
  - `predicted_only` (genomics/RNA-based)
  - `ms_observed` (immunopeptidomics evidence)
  - `validated_immunogenic` (T-cell assays such as ELISpot/tetramer/TCR readouts)

## Standard Definitions (avoid term drift)

- **Candidate generation**: the full set of possible peptides (SNV/indel, splice junction, fusion, frameshift, noncoding ORFs, viral, etc.).
- **Prioritization**: ranking a candidate list using features (binding rank, expression, clonality, cleavage/processing, similarity to self, etc.).
- **Validation**: evidence that a candidate is (a) presented on HLA and/or (b) immunogenic.
- **HLA class**:
  - `HLA-I` candidates are often shorter minimal epitopes and often use different presentation and processing assumptions.
  - `HLA-II` candidates are longer and can be ranked differently; some pipelines use separate heuristics for HLA-II.
- **Noncanonical**: peptides from non-protein-coding transcripts/alternative ORFs; should not be merged into “mutation-derived” without an explicit label.

## What to Extract from PDFs (minimum)

- Which **antigen classes** are in scope (HLA-I/HLA-II; mutation-derived/noncanonical/viral; private/shared)?
- What **evidence** is used (WES/WGS, RNA, MS immunopeptidomics, T-cell assays)?
- How does the pipeline treat **HLA typing** uncertainty and HLA LOH / APPM defects?
- Where does the paper’s “success” claim come from (ranking metrics, clinical response association, prospective vaccine outcomes)?

## Key Questions

- How broad should candidate generation be?
- What role should immunopeptidomics play in validation?
- How do we move from private to shared neoantigen strategies?

## Relevant Papers

- [A comprehensive proteogenomic pipeline for neoantigen discovery to advance personalized cancer immunotherapy](../sources/huber-2025-comprehensive-proteogenomic-pipeline-neoantigen-discovery.md)
- [Identification of non-canonical peptides with moPepGen](../sources/zhu-2025-identification-of-non-canonical-peptides.md)
- [Systematic discovery of neoepitope-HLA pairs for neoantigens shared among patients and tumor types](../sources/gurung-2024-systematic-discovery-of-neoepitope-hla.md)

## Connections

- [Clinical Translation of Neoantigen Research](./clinical-translation-of-neoantigen-research.md)
- [B-Cell Neoantigen Research Map](../syntheses/b-cell-neoantigen-research-map.md)
- [Neoantigen Discovery Pipelines](./neoantigen-discovery-pipelines.md)
