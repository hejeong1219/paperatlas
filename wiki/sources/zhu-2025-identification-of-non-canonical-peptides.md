---
title: Identification of non-canonical peptides with moPepGen
authors:
  - "Zhu"
year: 2025
journal: "Nature Biotechnology"
doi: "10.1038/s41587-025-02701-0"
url: "https://www.nature.com/articles/s41587-025-02701-0"
pdf: "raw/inbox/papers/zhu-2025-identification-of-non-canonical-peptides.pdf"
paper_kind: computational
cancer_types:
  - pan-cancer
modalities:
  - proteogenomics
  - neoantigen-discovery
themes:
  - neoantigen
  - pipeline
  - noncanonical-peptides
tags:
  - source
  - neoantigen
  - noncanonical-peptides
  - pipeline
  - proteogenomics
topic: ptmanchor
extra_topics:
  - "bcell-neoantigen"
---
# Identification of non-canonical peptides with moPepGen

moPepGen is a graph-based algorithm for enumerating non-canonical peptides from complex genomic and transcriptomic inputs, extending the search space for cancer neoantigen discovery.

## Key Points

- Presents `moPepGen`, a graph-based method that generates non-canonical peptide candidates in linear time.
- Handles multiple technologies and data types, including variants, noncoding ORFs, fusions, and circular RNAs.
- Highlights how standard proteogenomic workflows miss substantial noncanonical peptide space in human cancers.
- Strengthens the computational front end for neoantigen discovery before immunogenicity prioritization.

## Relevance

- Useful when the wiki needs a broader neoantigen candidate generation stage than exome-only pipelines provide.
- Complements NeoDisc by improving the peptide universe that can later be prioritized or experimentally validated.

## Connections

- [B-Cell Neoantigen Proposal Anchor](../analyses/b-cell-neoantigen-proposal-anchor.md)
- [B-Cell Neoantigen Research Map](../topics/b-cell-neoantigen-human-cancer.md)
- [Neoantigen Discovery Pipelines](../concepts/neoantigen-discovery-pipelines.md)
- [A comprehensive proteogenomic pipeline for neoantigen discovery to advance personalized cancer immunotherapy](./huber-2025-comprehensive-proteogenomic-pipeline-neoantigen-discovery.md)
- [B-Cell Neoantigen Pipeline in Human Cancer](../analyses/b-cell-neoantigen-pipeline-human-cancer-corpus.md)

## Sources

- PDF: [zhu-2025-identification-of-non-canonical-peptides.pdf](../../raw/inbox/papers/zhu-2025-identification-of-non-canonical-peptides.pdf)
- Article: <https://www.nature.com/articles/s41587-025-02701-0>

## 함께 인용된 논문

위키 분석·합성 페이지에서 이 논문과 함께 인용된 논문들 (co-citation).

- [[gurung-2024-systematic-discovery-of-neoepitope-hla|Gurung 2024]]
- [[huber-2025-comprehensive-proteogenomic-pipeline-neoantigen-discovery|Huber 2025]]
- [[borgers-2025-personalized-autologous-neoantigen-specific-therapy|Borgers 2025]]
- [[hegoburu-2025-b-cells-and-tertiary-structures|Hegoburu 2025]]
- [[kasikova-2024-tertiary-lymphoid-structures-b-cells|Kasikova 2024]]
- [[li-2025-mature-tertiary-lymphoid-structures-headneck|Li 2025]]
- [[liu-2024-single-cell-and-spatial-transcriptome|Liu 2024]]
- [[rappaport-2024-shared-neoantigen-vaccine-checkpoint-blockade|Rappaport 2024]]
- [[yarchoan-2024-personalized-neoantigen-vaccine-and-pembrolizumab|Yarchoan 2024]]
