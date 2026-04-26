---
title: Deciphering the dark cancer phosphoproteome using machine-learned co-regulation of phosphosites
authors:
  - "Jiang"
year: 2025
journal: "Nature Communications"
doi: "10.1038/s41467-025-57993-2"
url: "https://www.nature.com/articles/s41467-025-57993-2"
pdf: "raw/inbox/papers/jiang-2025-dark-cancer-phosphoproteome-coregulation.pdf"
paper_kind: computational
cancer_types:
  - pan-cancer
modalities:
  - phosphoproteomics
  - machine-learning
  - kinase-activity-inference
themes:
  - dark-phosphoproteome
  - co-regulation
  - kinase-substrate-association
  - cptac
tags:
  - source
  - phosphoproteomics
  - machine-learning
  - kinase-inference
  - pan-cancer
topic: ptmanchor
---
# Deciphering the dark cancer phosphoproteome using machine-learned co-regulation of phosphosites

Pan-cancer machine-learning study that uses tumor phosphoproteomics to infer co-regulated phosphosite structure and expand kinase-substrate annotation into the dark phosphoproteome.

## Key Points

- Integrates phosphoproteomic data from 1,195 tumor specimens across 11 cancer types to build `CoPheeMap`, a large phosphosite co-regulation network.
- Uses network-derived features in `CoPheeKSA` to improve kinase-substrate association prediction beyond conventional motif- or annotation-limited approaches.
- Predicts tens of thousands of kinase-substrate associations spanning many understudied phosphosites and kinases, addressing the sparse-annotation problem directly.
- Positions dark phosphoproteome interpretation as a network-learning problem rather than a purely motif-matching problem.
- Highlights how broader phosphosite annotation can expose dysregulated signaling programs and therapeutic kinase targets in human cancer.

## Relevance

- Strongly relevant to the ptmanchor manuscript because it addresses the downstream interpretability bottleneck that appears after site-level signal correction.
- Useful for arguing that improved site-level quantification should be paired with richer network-level inference if the goal is to recover biologically meaningful kinase regulation.
- Complements formal kinase-activity benchmarking by expanding the substrate universe that those methods can draw from.

## Connections

- [ptmanchor Manuscript Anchor](../analyses/ptmanchor-manuscript-anchor.md)
- [PTM Correction and Kinase Signaling in Cancer Proteomics](../topics/ptm-correction-and-kinase-signaling-in-cancer-proteomics.md)
- [Pan-Cancer](../cancers/pan-cancer.md)
- [Comprehensive evaluation of phosphoproteomic-based kinase activity inference](./muller-dott-2025-phosphoproteomic-kinase-activity-inference.md)

## Sources

- PDF: [jiang-2025-dark-cancer-phosphoproteome-coregulation.pdf](../../raw/inbox/papers/jiang-2025-dark-cancer-phosphoproteome-coregulation.pdf)
- Article: <https://www.nature.com/articles/s41467-025-57993-2>
