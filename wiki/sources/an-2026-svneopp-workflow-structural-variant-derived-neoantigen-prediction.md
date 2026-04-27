---
title: "SVNeoPP: A Workflow for Structural-Variant-Derived Neoantigen Prediction and Prioritization Using Multi-Omics Data."
authors:
  - "An"
  - "Tan"
  - "Liu"
year: 2026
journal: "Biology"
doi: "10.26508/lsa.202402977"
pmid: "41892252"
pmcid: "PMC11772497"
paper_kind: research
pdf: "raw/inbox/papers/an-2026-svneopp-workflow-structural-variant-derived-neoantigen-prediction.pdf"
topic: bcell-neoantigen
tags:
  - "bcell-neoantigen"
  - "neoantigen"
  - "b-cells"
  - "tls"
  - "immunology"
  - "pmid-41892252"
themes:
  - "neoantigen-discovery"
  - "tls-biology"
  - "clinical-translation"
---
# SVNeoPP: A Workflow for Structural-Variant-Derived Neoantigen Prediction and Prioritization Using Multi-Omics Data.

_Biology, 2026._ PMID: [41892252](https://pubmed.ncbi.nlm.nih.gov/41892252/).

DOI: [10.26508/lsa.202402977](https://doi.org/10.26508/lsa.202402977)

## Summary

**BACKGROUND**: Tumor neoantigens are key targets for personalized vaccines and T-cell therapies, yet most pipelines focus on neoantigens derived from SNV/small indel and often yield a limited number of high-quality candidates. SVs are prevalent in tumors and can generate novel chimeric sequences and neopeptides, making them a promising additional source of neoantigens. However, SV-derived neoantigen prediction remains challenging due to breakpoint uncertainty, isoform-dependent coding inference, and limited integration of multi-dimensional evidence and reproducibility.

**METHODS**: We developed SVNeoPP (Structural Variant Neoantigen Prediction and Prioritization), an end-to-end workflow for SV-derived neoantigen analysis. SVNeoPP takes WGS and RNA-seq as inputs, performs SV calling and annotation, and reconstructs altered transcripts and coding sequences in a traceable, isoform-aware manner to generate candidate peptides. Candidates are prescreened by integrating antigen-processing features with HLA binding prediction, and then hierarchically filtered and prioritized based on transcript expression, LC-MS/MS proteomics evidence, immunogenicity predictions, and sequence similarity to experimentally validated neoantigen databases. SVNeoPP is implemented in Snakemake to enable modular extension, checkpoint-based restarts, and end-to-end reproducibility.

**RESULTS**: Using a hepatocellular carcinoma (HCC) multi-omics dataset as a proof of concept, we demonstrated the performance of SVNeoPP and obtained a high-priority shortlist of candidate peptides. Compared with other methods, SVNeoPP substantially expanded the candidate search space for SV-derived neoantigens and showed more favorable distributions of antigen-processing and HLA binding features.

**CONCLUSIONS**: SVNeoPP provides a reusable, traceable, and interpretable multi-dimensional evidence-driven framework for SV-derived neoantigens. As a complementary module to SNV/small-indel pipelines, it broadens the neoantigen candidate repertoire and generates ranked candidates with interpretable evidence to facilitate downstream prioritization and decision-making.

## Key Points

_Awaiting deep-dive — automated abstract is in the Summary section above. The paper-specific Key Points, Methods, Limitations, and Open Questions will appear here once the full PDF has been read._


## Connections

- [Bcell Neoantigen Topic Hub](../topics/b-cell-neoantigen-human-cancer.md)
- [Bcell Neoantigen Anchor](../analyses/b-cell-neoantigen-proposal-anchor.md)

## Sources

- Local PDF: pending acquisition
- PubMed: <https://pubmed.ncbi.nlm.nih.gov/41892252/>
- DOI: <https://doi.org/10.26508/lsa.202402977>
- PMC: <https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11772497/>
