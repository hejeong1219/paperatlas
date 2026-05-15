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
batch_ingest_status: pdf-text-extracted
batch_ingested_on: 2026-05-13
---
# Deciphering the dark cancer phosphoproteome using machine-learned co-regulation of phosphosites

Pan-cancer machine-learning study that uses tumor phosphoproteomics to infer co-regulated phosphosite structure and expand kinase-substrate annotation into the dark phosphoproteome.

## Batch PDF Ingest Status

- Status: `pdf-text-extracted` on 2026-05-13.
- Local PDF: `raw/inbox/papers/jiang-2025-dark-cancer-phosphoproteome-coregulation.pdf`.
- Extracted text length: 71,835 characters.
- Scope note: automated local-PDF text ingest for the 100-paper drug-response/phospho-global batch; not yet a manual full-text deep-dive.
- Evidence boundary: downstream scientific claims should use this page only after source-specific Key Points are manually promoted or rechecked against the local PDF.
- High-signal PDF snippets:
  - Article https://doi.org/10.1038/s41467-025-57993-2 Deciphering the dark cancer phosphoproteome using machine-learned co-regulation of phosphosites Received: 7 July 2024 Wen Jiang1,2, Eric J.
  - Cantley 6,7 & Accepted: 10 March 2025 Bing Zhang 1,2 Published online: 20 March 2025 Check for updates Mass spectrometry-based phosphoproteomics offers a comprehensive view of 1234567890():,; 1234567890():,; protein phosphorylation, yet our limited knowledge about the regulation and function of most phosphosites hampers the e...
  - To address this challenge, we integrate machine learning with phosphoproteomic data from 1195 tumor specimens spanning 11 cancer types to construct CoPheeMap, a network that maps the co-regulation of 26,280 phosphosites.
  - By incorporating network features from CoPheeMap into a second machine learning model, namely CoPheeKSA, we achieve superior performance in predicting kinase-substrate associations.
  - CoPheeKSA uncovers 24,015 associations between 9399 phosphosites and 104 serine/ threonine kinases, shedding light on many unannotated phosphosites and understudied kinases.

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

- [Cancer Multiomics Literature Monitor](../topics/cancer-multiomics-literature.md)
- Cancer Multiomics 요약: [Jiang 2025 - Dark Cancer Phosphoproteome](../analyses/cancer-multiomics-literature/jiang-2025-dark-cancer-phosphoproteome.md)
- [ptmanchor Manuscript Anchor](../analyses/ptmanchor-manuscript-anchor.md)
- [PTM Correction and Kinase Signaling in Cancer Proteomics](../topics/ptm-correction-and-kinase-signaling-in-cancer-proteomics.md)
- [Pan-Cancer](../cancers/pan-cancer.md)
- [Comprehensive evaluation of phosphoproteomic-based kinase activity inference](./muller-dott-2025-phosphoproteomic-kinase-activity-inference.md)

## Sources

- PDF: [jiang-2025-dark-cancer-phosphoproteome-coregulation.pdf](../../raw/inbox/papers/jiang-2025-dark-cancer-phosphoproteome-coregulation.pdf)
- Article: <https://www.nature.com/articles/s41467-025-57993-2>
