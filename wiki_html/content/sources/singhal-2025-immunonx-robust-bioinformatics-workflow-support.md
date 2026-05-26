---
title: "ImmunoNX: a robust bioinformatics workflow to support personalized neoantigen vaccine trials."
authors:
  - "Singhal"
  - "Schmidt"
  - "Kiwala"
year: 2025
journal: "ArXiv"
doi: "10.1101/080903"
pmid: "41415611"
pmcid: "PMC6450397"
paper_kind: clinical-trial
pdf: "raw/inbox/papers/singhal-2025-immunonx-robust-bioinformatics-workflow-support.pdf"
topic: bcell-neoantigen
tags:
  - "bcell-neoantigen"
  - "neoantigen"
  - "b-cells"
  - "tls"
  - "immunology"
  - "pmid-41415611"
themes:
  - "neoantigen-discovery"
  - "tls-biology"
  - "clinical-translation"
---
# ImmunoNX: a robust bioinformatics workflow to support personalized neoantigen vaccine trials.

_ArXiv, 2025._ PMID: [41415611](https://pubmed.ncbi.nlm.nih.gov/41415611/).

DOI: [10.1101/080903](https://doi.org/10.1101/080903)

## Summary

Personalized neoantigen vaccines represent a promising immunotherapy approach that harnesses tumor-specific antigens to stimulate anti-tumor immune responses. However, the design of these vaccines requires sophisticated computational workflows to predict and prioritize neoantigen candidates from patient sequencing data, coupled with rigorous review to ensure candidate quality. While numerous computational tools exist for neoantigen prediction, to our knowledge, there are no established protocols detailing the complete process from raw sequencing data through systematic candidate selection. Here, we present ImmunoNX (Immunogenomics Neoantigen eXplorer), an end-to-end protocol for neoantigen prediction and vaccine design that has supported over 185 patients across 11 clinical trials. The workflow integrates tumor DNA/RNA and matched normal DNA sequencing data through a computational pipeline built with Workflow Definition Language (WDL) and executed via Cromwell on Google Cloud Platform. ImmunoNX employs consensus-based variant calling, in-silico HLA typing, and pVACtools for neoantigen prediction. Additionally, we describe a two-stage immunogenomics review process with prioritization of neoantigen candidates, enabled by pVACview, followed by manual assessment of variants using the Integrative Genomics Viewer (IGV). This workflow enables vaccine design in under three months. We demonstrate the protocol using the HCC1395 breast cancer cell line dataset, identifying 78 high-confidence neoantigen candidates from 322 initial predictions. Although demonstrated here for vaccine development, this workflow can be adapted for diverse neoantigen therapies and experiments. Therefore, this protocol provides the research community with a reproducible, version-controlled framework for designing personalized neoantigen vaccines, supported by detailed documentation, example datasets, and open-source code.

## Key Points

_Awaiting deep-dive — automated abstract is in the Summary section above. The paper-specific Key Points, Methods, Limitations, and Open Questions will appear here once the full PDF has been read._


## Connections

- [Bcell Neoantigen Topic Hub](../topics/b-cell-neoantigen-human-cancer.md)
- [Bcell Neoantigen Anchor](../analyses/b-cell-neoantigen-proposal-anchor.md)

## Sources

- Local PDF: pending acquisition
- PubMed: <https://pubmed.ncbi.nlm.nih.gov/41415611/>
- DOI: <https://doi.org/10.1101/080903>
- PMC: <https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6450397/>
