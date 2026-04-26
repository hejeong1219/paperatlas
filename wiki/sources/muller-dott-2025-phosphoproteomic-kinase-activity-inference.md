---
title: Comprehensive evaluation of phosphoproteomic-based kinase activity inference
authors:
  - "Muller-Dott"
year: 2025
journal: "Nature Communications"
doi: "10.1038/s41467-025-59779-y"
url: "https://www.nature.com/articles/s41467-025-59779-y"
pdf: "raw/inbox/papers/muller-dott-2025-phosphoproteomic-kinase-activity-inference.pdf"
paper_kind: computational
cancer_types:
  - pan-cancer
modalities:
  - phosphoproteomics
  - kinase-activity-inference
  - multi-omics
themes:
  - benchmark
  - kinase-signaling
  - cptac
  - library-selection
tags:
  - source
  - phosphoproteomics
  - kinase-inference
  - benchmark
  - pan-cancer
topic: ptmanchor
---
# Comprehensive evaluation of phosphoproteomic-based kinase activity inference

Benchmarking study that compares kinase-activity inference methods and substrate libraries using both perturbation data and human tumor multi-omic cohorts.

## Key Points

- Introduces `benchmarKIN`, an R package and evaluation framework for comparing kinase activity inference methods across phosphoproteomics settings.
- Uses complementary benchmarking strategies: perturbation experiments and tumor-based benchmarking grounded in CPTAC and related multi-omics cancer datasets.
- Shows that inference algorithm choice matters less than substrate-library choice, with curated kinase-substrate resources generally performing better.
- Finds that adding predicted targets, such as NetworKIN-derived interactions, can improve performance in tumor-based evaluations by expanding otherwise sparse coverage.
- Provides a practical framework for deciding which kinase activity inference strategy is credible enough to use in downstream biological interpretation.

## Relevance

- Directly relevant to the ptmanchor manuscript because its central translational claim is that better PTM correction should improve kinase activity inference.
- Useful as an external benchmark reference for evaluating whether protein-aware correction changes inferred kinase states in more biologically credible ways.
- Strong fit for pan-cancer phosphoproteomics work because it explicitly leverages human tumor cohorts rather than remaining a purely cell-line benchmark.

## Connections

- [ptmanchor Manuscript Anchor](../analyses/ptmanchor-manuscript-anchor.md)
- [PTM Correction and Kinase Signaling in Cancer Proteomics](../topics/ptm-correction-and-kinase-signaling-in-cancer-proteomics.md)
- [Pan-Cancer](../cancers/pan-cancer.md)
- [Deciphering the dark cancer phosphoproteome using machine-learned co-regulation of phosphosites](./jiang-2025-dark-cancer-phosphoproteome-coregulation.md)

## Sources

- PDF: [muller-dott-2025-phosphoproteomic-kinase-activity-inference.pdf](../../raw/inbox/papers/muller-dott-2025-phosphoproteomic-kinase-activity-inference.pdf)
- Article: <https://www.nature.com/articles/s41467-025-59779-y>
