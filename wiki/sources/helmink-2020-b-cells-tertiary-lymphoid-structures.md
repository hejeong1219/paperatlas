---
title: "B cells and tertiary lymphoid structures promote immunotherapy response."
authors:
  - "Helmink"
  - "Reddy"
  - "Gao"
year: "2020"
journal: "Nature"
doi: "10.1038/s41586-019-1922-8"
pmid: "31942075"
pmcid: "PMC8762581"
paper_kind: research
pdf: "raw/inbox/papers/helmink-2020-b-cells-tertiary-lymphoid-structures.pdf"
topic: bcell-neoantigen
extra_topics:
  - "resistance"
tags:
  - "bcell-neoantigen"
  - "neoantigen"
  - "b-cells"
  - "tls"
  - "immunology"
  - "pmid-31942075"
themes:
  - "neoantigen-discovery"
  - "tls-biology"
  - "clinical-translation"
---
# B cells and tertiary lymphoid structures promote immunotherapy response

_Nature 577:549–555, 2020._ PMID: [31942075](https://pubmed.ncbi.nlm.nih.gov/31942075/) · DOI: [10.1038/s41586-019-1922-8](https://doi.org/10.1038/s41586-019-1922-8)

## Summary

Landmark paper that shifted ICB-response biology from a T-cell-only frame to one where B cells inside tertiary lymphoid structures (TLS) are the strongest tumor-side correlate of response. Using bulk RNA-seq on a neoadjuvant melanoma ICB trial (NCT02519322), the authors found that B-cell genes — not T-cell genes — top the differentially expressed list between responders and non-responders. The signal reproduces in two independent cohorts (a second neoadjuvant melanoma trial, OpACIN-neo, and a pre-surgical RCC ICB trial), in TCGA-SKCM survival data, and in scRNA-seq of an unrelated metastatic melanoma cohort. Histology shows the responder B cells are not scattered: they are organized into mature secondary-follicle-like TLS containing CD21⁺ follicular dendritic cells and CD23⁺ germinal-center B cells, co-localized with CD4⁺/CD8⁺/FOXP3⁺ T cells. BCR-seq and scRNA-seq add a functional layer — responders show clonally expanded, switched memory and plasma-cell-like B-cell states, suggesting an active germinal-center reaction at the tumor. Together the paper reframes B cells as an organized, prognostically meaningful, and likely mechanistic component of ICB response.

## Key Points

- B-cell-related genes (`MZB1`, `JCHAIN`, `IGLL5`, `FCRL5`, `POU2AF1`) top the differentially expressed gene list at baseline in melanoma responders vs non-responders (P < 0.001), surpassing canonical T-cell or interferon markers.
- MCP-counter B-lineage scores predicted ICB response in melanoma (OR 2.6, P = 0.02; OR 2.9, P = 0.03 across pooled neoadjuvant melanoma cohorts) and in RCC (OR 61.2, P = 0.05) in univariable analyses; multivariable significance is lost, suggesting B cells act with other immune subsets rather than alone.
- TLS density and CD20⁺ B-cell density in tumor were significantly higher in responders, especially on-treatment (CD20 P = 0.0008; TLS density P = 0.001; TLS:tumor ratio P = 0.002), echoing the known on-treatment-biopsy advantage over baseline biopsy for predicting ICB benefit.
- Architectural mapping showed responder TLS are mature: CD21⁺ follicular dendritic cells, CD23⁺ germinal-center B cells, MECA79⁺ high endothelial venules, and surrounding CD4⁺/CD8⁺/FOXP3⁺ T-cell rings — a structure that resembles a secondary lymphoid follicle inside the tumor.
- BCR repertoire (TRUST analysis on bulk RNA-seq) shows higher IgH/IgL clonal counts (P = 0.001/0.004) and higher BCR diversity (P = 0.002/0.0008) in responders — i.e., responders are not just B-cell rich, they carry an active humoral response.
- scRNA-seq of an independent metastatic-melanoma ICB cohort (1,760 B cells, 32 patients) recovered four B-cell states: switched activated IgD⁻ (G1), plasma cells (G2), unswitched IgD⁺ (G3), and a second switched activated IgD⁻ subset (G4); responder tumors enrich for the switched/plasma states (G1, G2), validating mass-cytometry findings.
- TCGA-SKCM (n = 136, stage III non-recurrent) shows that B-cell-low tumors carry HR 1.7 for death (P = 0.05), generalizing the link beyond the ICB trial cohorts to a broader prognostic role.
- The paper does not show B-cell depletion experiments in patients — causality is inferred, not proven; this is the central caveat for therapeutic claims.

## Methods

Neoadjuvant ipi+nivo or nivo melanoma trial (NCT02519322) with paired baseline and on-treatment biopsies; primary discovery via bulk RNA-seq plus targeted Nanostring DSP. Validation across an independent neoadjuvant melanoma trial (OpACIN-neo), a pre-surgical RCC ICB trial (NCT02210117, three arms including PD1+CTLA4 and PD1+bev), TCGA-SKCM and TCGA-KIRC RNA-seq, multiplex IHC and IF for CD20/CD21/CD23/CD4/CD8/FOXP3/MECA79, mass cytometry of TILs, BCR-seq via TRUST on bulk RNA-seq, and scRNA-seq from an unrelated melanoma ICB cohort.

## Limitations

- Cohort sizes are small for each individual trial (≤ ~20 patients per arm), so multivariable analyses lose power and individual B-cell sub-state associations with response are under-powered.
- Sampling is biased toward melanoma; RCC adds a second tumor type but the broader pan-cancer claim depends on TCGA bulk transcriptomics, which cannot resolve TLS architecture.
- TLS quantification by 2D histology underestimates 3D structure and varies by tumor region — single-section bias likely.
- Causality between TLS and response is inferred from correlation; B-cell depletion (e.g., anti-CD20) was not performed in patients.
- Switched memory / plasma-cell associations are phenotypic — antigen specificity (which tumor antigens these B cells recognize) is not demonstrated, leaving the link to neoantigens implicit.
- Patients on the ICB trials had stage III/IV disease — the role of TLS may differ in earlier-stage disease where adaptive immunity is less constrained.

## Relevance to anchors

- Direct cornerstone for the [B-Cell Neoantigen Proposal Anchor](../analyses/b-cell-neoantigen-proposal-anchor.md): establishes that the B-cell axis is not optional but a leading correlate of ICB benefit, justifying the proposal's core premise that B-cell-relevant antigen interpretation is under-built.
- Connects to the [Cancer Resistance Manuscript Anchor](../analyses/cancer-resistance-manuscript-anchor.md) under the "effector function" axis: TLS-poor tumors fail ICB even when other axes (visibility, access) are intact, supporting the convergence framework.
- Reinforces TLS as a *structural* immune-context biomarker (not just B-cell density), matching the topic's argument that organization, not just abundance, predicts response.
- Sets up later spatial/scRNA TLS work (Wang 2025 gastric, Li 2025 head-and-neck, Amisaki 2025 pancreatic) as mechanistic extensions of this melanoma/RCC observation into other tumor types.

## Open Questions

- Are the responder-enriched switched memory / plasma-cell B-cell clones tumor-antigen-specific, and if so against neoantigens or self-antigens? BCR-Ag pairing in patient samples remains scarce.
- Does anti-CD20 (rituximab) abrogate ICB benefit in melanoma patients with TLS? A natural experiment exists in lymphoma-coincident melanoma cases that has not been reported.
- What induces TLS formation under ICB — is it ICB-driven *de novo* neogenesis or pre-existing follicles becoming activated?
- Can a clinically usable TLS score (mIF or transcriptomic) outperform PD-L1 + TMB for ICB selection across tumor types?
- How do mature vs immature TLS differ functionally, and is maturity (CD21⁺/CD23⁺ presence) a better predictor than density alone?

## Connections

- [B-Cell Neoantigen Research Map](../topics/b-cell-neoantigen-human-cancer.md)
- [B-Cell and TLS Context for Neoantigen Research](../concepts/b-cell-and-tls-context-for-neoantigen-research.md)
- [B-Cell Neoantigen Proposal Anchor](../analyses/b-cell-neoantigen-proposal-anchor.md)
- [Italiano 2022 — Pembrolizumab in Soft-Tissue Sarcoma TLS](./italiano-2022-pembrolizumab-soft-tissue-sarcomas-tls.md)
- [Cabrita 2020 — TLS in Melanoma (companion landmark)](https://doi.org/10.1038/s41586-019-1914-8)

## Sources

- Local PDF: `raw/inbox/papers/helmink-2020-b-cells-tertiary-lymphoid-structures.pdf`
- PubMed: <https://pubmed.ncbi.nlm.nih.gov/31942075/>
- DOI: <https://doi.org/10.1038/s41586-019-1922-8>
