---
title: A comprehensive proteogenomic pipeline for neoantigen discovery to advance personalized cancer immunotherapy
authors:
  - "Huber"
year: 2025
journal: "Nature Biotechnology"
doi: "10.1038/s41587-024-02420-y"
url: "https://www.nature.com/articles/s41587-024-02420-y"
pdf: "raw/inbox/papers/huber-2025-comprehensive-proteogenomic-pipeline-neoantigen-discovery.pdf"
paper_kind: computational
cancer_types:
  - pan-cancer
modalities:
  - proteogenomics
  - immunopeptidomics
  - neoantigen-discovery
themes:
  - neoantigen
  - pipeline
  - personalized-therapy
tags:
  - source
  - neoantigen
  - pipeline
  - immunopeptidomics
  - personalized-therapy
topic: ptmanchor
extra_topics:
  - "bcell-neoantigen"
---
# A comprehensive proteogenomic pipeline for neoantigen discovery to advance personalized cancer immunotherapy

NeoDisc is an end-to-end proteogenomic workflow that integrates immunopeptidomics, genomics, transcriptomics, and prioritization logic to improve clinical neoantigen discovery and vaccine design.

## Key Points

- Introduces `NeoDisc`, a clinical proteogenomic pipeline that combines immunopeptidomics with genomic and transcriptomic analysis.
- Expands candidate discovery beyond canonical neoantigens to include viral, tumor-specific, and noncanonical antigens.
- Reports improved prioritization of immunogenic neoantigens compared with recent baseline pipelines.
- Supports both rule-based and machine-learning ranking strategies for personalized antigen discovery.

## What the Pipeline Takes In (as described)

- Matched germline–tumor sequencing (`WES`; `WGS` is supported by the software but was not implemented in the study examples).
- Bulk `RNA-seq` for expression, inflammation context, and additional evidence (including use of unmapped reads for viral detection).
- Immunopeptidomics MS data (`HLA-I` and `HLA-II`; mentions `DDA` and `DIA` acquisition).

## How NeoDisc Decides (PDF-backed details)

- Variant confidence is handled via an ensemble approach: four variant callers are applied; variants called by only one caller are treated as low-confidence, whereas variants supported by ≥2 callers are treated as high-confidence.
  - Low- and high-confidence variants can be included in the personalized proteome used for immunopeptidomics search.
  - Only high-confidence variants are used for in silico neoantigen prediction in the default settings.
- HLA typing is derived from germline and tumor `WES` plus `RNA-seq` data.
- Antigen processing and presentation machinery (APPM) defects and HLA LOH are explicitly identified and surfaced as “failure modes” that impact neoantigen interpretation.
- HLA-I ranking: supports both rule-based ranking and an ML ranking model trained on a public immunogenicity dataset.
- HLA-II ranking: described as rule-based; the text notes a lack of sufficient public immunogenicity data for robust ML at HLA-II scale.

## Worked Example (CESC-1; numbers in main text)

- The paper illustrates prioritization on a cervical adenocarcinoma case (`CESC-1`) with 393 actionable coding mutations.
- From a predicted peptide pool, 66 HLA-I minimal-epitope candidates were selected for T-cell screening, and 11/66 were reported immunogenic by IFNγ ELISpot.
- Re-ranking with the NeoDisc ML model placed 6 immunogenic peptides within the top 10.
- The text also reports that immunopeptidomics can directly detect (and help re-rank) confirmed immunogenic neoantigens in this case.

## Practical Relevance (why it matters here)

- This paper is a concrete “end-to-end” reference for connecting genomics/RNA evidence to HLA-bound peptide evidence, while keeping APPM/HLA-LOH failure modes visible.
- It is especially useful for Cancer Multiomics and B-cell/TLS tracks because it makes the upstream “antigen quality” assumptions auditable before downstream immune-architecture interpretation.

## Relevance

- This is one of the most directly useful papers for a practical neoantigen pipeline layer in this wiki.
- It provides a concrete reference architecture for integrating raw sequencing and HLA-bound peptide evidence.
- It is especially relevant for linking downstream B-cell and TLS biology to upstream antigen selection quality.

## Connections

- [Cancer Multiomics Proteogenomic Atlas](../topics/cancer-multiomics-literature.md)
- Cancer Multiomics 요약: [Huber 2025 - NeoDisc Proteogenomic Neoantigen Pipeline](../analyses/cancer-multiomics-literature/huber-2025-neodisc-neoantigen-pipeline.md)
- [B-Cell Neoantigen Proposal Anchor](../analyses/b-cell-neoantigen-proposal-anchor.md)
- [B-Cell Neoantigen Research Map](../topics/b-cell-neoantigen-human-cancer.md)
- [Neoantigen Discovery Pipelines](../concepts/neoantigen-discovery-pipelines.md)
- [B-Cell Neoantigen Pipeline in Human Cancer](../analyses/b-cell-neoantigen-pipeline-human-cancer-corpus.md)
- [Identification of non-canonical peptides with moPepGen](./zhu-2025-identification-of-non-canonical-peptides.md)
- [Systematic discovery of neoepitope-HLA pairs for neoantigens shared among patients and tumor types](./gurung-2024-systematic-discovery-of-neoepitope-hla.md)

## Sources

- PDF: [huber-2025-comprehensive-proteogenomic-pipeline-neoantigen-discovery.pdf](../../raw/inbox/papers/huber-2025-comprehensive-proteogenomic-pipeline-neoantigen-discovery.pdf)
- Article: <https://www.nature.com/articles/s41587-024-02420-y>
