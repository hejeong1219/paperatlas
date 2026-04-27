---
title: "Neoantigen load and HLA-class I expression identify a subgroup of tumors with a T-cell-inflamed phenotype and favorable prognosis in HR-proficient HGSC"
authors:
  - "Matsushita"
  - "Hasegawa"
  - "Oda"
year: 2020
journal: "Journal for ImmunoTherapy of Cancer"
doi: "10.1136/jitc-2019-000375"
pmid: "32461346"
pmcid: "PMC7254153"
paper_kind: research
pdf_status: pending
topic: bcell-neoantigen
extra_topics:
  - "resistance"
tags:
  - "bcell-neoantigen"
  - "neoantigen"
  - "hla-class-i"
  - "ovarian-cancer"
  - "hr-proficient"
  - "parp-resistance"
  - "pmid-32461346"
themes:
  - "neoantigen-discovery"
  - "antigen-presentation"
  - "ici-stratification"
---
# Matsushita 2020 — Neoantigen × HLA-class I stratifies HR-proficient HGSC

_J Immunother Cancer 8:e000375, 2020._ PMID: [32461346](https://pubmed.ncbi.nlm.nih.gov/32461346/) · DOI: [10.1136/jitc-2019-000375](https://doi.org/10.1136/jitc-2019-000375) · PMC: [PMC7254153](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7254153/)

## Summary

This is a small but conceptually important study (n=80) that uses two independent layers of tumor immunogenicity — **predicted neoantigen load (neoAg)** and **HLA-class I protein expression** — to identify a clinically meaningful subgroup of high-grade serous ovarian carcinoma (HGSC) where checkpoint blockade is rational *despite* the tumor being homologous-recombination (HR) proficient. The main finding is that 40% of HR-proficient HGSC still carry above-median neoAg load, and the joint neoAg-high + HLA-high subset has the longest progression-free survival (PFS, p=0.0087) and a transcriptomic profile dominated by effector memory CD8 / TH1 / interferon-γ programs. Strikingly, this T-cell-inflamed phenotype within HR-proficient tumors was *cleaner* (PFS p=0.0015) than the same phenotype in HR-deficient tumors — suggesting that when an HR-proficient tumor manages to be immunogenic, it does so without the HRD-driven mutational background "noise" and may be a stronger ICB candidate than HRD tumors with similar surface markers. The implication is a clinically actionable two-axis biomarker: HR status defines who gets PARP inhibitor benefit; neoAg×HLA defines who, *among the HR-proficient PARPi-failure population*, should still be tried on ICB.

## Key Points

- **Cohort**: 80 HGSC patients with paired WES + RNA-seq + methylation arrays for BRCA1/RAD51C silencing; HR-proficient n=46, HR-deficient n=34.
- **Neoantigen load is lower in HR-proficient tumors as expected**, but **40% of HR-proficient still exceed cohort median** — i.e., HRD is not the only path to immunogenicity in HGSC.
- **Joint biomarker (neoAg-high + HLA-class I-high)** stratifies HR-proficient HGSC for PFS at p=0.0087 — single-marker stratification is weaker, supporting the two-axis design.
- **GSEA**: the neoAg-high HLA-high HR-proficient subset is enriched for effector-memory CD8, TH1, IFN-γ response, and immune-related gene programs, validating that the genomic biomarker maps onto an actual T-cell-inflamed transcriptomic phenotype.
- **HR-proficient T-cell-inflamed > HR-deficient T-cell-inflamed in PFS (p=0.0015)** — counterintuitive finding; suggests HRD's mutational burden may be a *non-specific* burden where many neoAg are non-immunogenic, while HR-proficient immunogenic tumors are immunogenic for a more focused reason.
- **Translational implication**: the population most likely to benefit from ICB in HGSC is a *minority* of HR-proficient tumors (40% × HLA-high subset), not the entire HR-proficient population — refining the indication for trials like NRG-GY004 / KEYNOTE-100 follow-ups.
- **PARP-axis complement**: this paper does not test PARPi benefit; it offers ICB as the alternative pathway for HR-proficient PARPi-resistant disease.

## Methods

80 HGSC samples; whole-exome sequencing for mutation calling and neoantigen prediction (likely netMHCpan-class pipeline); RNA-seq for HLA-class I expression and immune deconvolution; methylation arrays for BRCA1/RAD51C promoter methylation to refine HR-proficient/deficient classification beyond germline/somatic BRCA mutation. Survival analyses (PFS) compared subgroups split by neoAg load and HLA-class I expression. GSEA on RNA-seq for immune signatures.

## Limitations

- **Single-cohort, n=80** — the four-quadrant subgroups (HR×neoAg×HLA) are necessarily small (HR-proficient + neoAg-high + HLA-high is likely ~10–15 patients). Survival p-values are stable but effect-size estimates are wide.
- **No prospective ICB validation** — the paper proposes ICB as a hypothesis for the neoAg-high HLA-high HR-proficient subset; it does not test it. Prospective ICB stratification in this subgroup remains to be done.
- **Predicted neoantigens, not validated**: relies on in-silico HLA binding prediction; immunogenicity is inferred from RNA-seq T-cell-inflammation signatures, not from BCR-Ag or TCR-Ag pairing.
- **HLA-class I quantification by RNA-seq** — protein-level HLA expression matters more (LOH, post-transcriptional regulation), but the cohort was scored at transcriptomic level. mIF-based HLA-I scoring would tighten the biomarker.
- **No B-cell readout** — given that ovarian cancer often has TLS-rich tumors (Kasikova 2024), the absence of B-cell or TLS analysis here leaves a layer of immune context unmeasured.

## Relevance to anchors

- **B-cell neoantigen proposal** ([anchor](../analyses/b-cell-neoantigen-proposal-anchor.md)): provides a clean precedent for **two-axis immunogenicity scoring** (neoAg × HLA) in a tumor type where the proposal aims to extend with B-cell context. The natural next paper is "neoAg × HLA × **mature TLS**" three-axis scoring in HGSC, which this paper sets up but does not execute.
- **Cancer resistance manuscript** ([anchor](../analyses/cancer-resistance-manuscript-anchor.md)): directly informs the "PARP resistance immune evasion" axis — argues that HR-proficient HGSC, often considered ICB-cold, has a treatable immunogenic minority. Reinforces the convergence framework's claim that "immune visibility" is the actionable axis even when the primary therapy class (PARPi) fails for HR-proficient tumors.
- **Concept link**: closely related to [MHC-I Loss and Interferon Pathway Defects in Checkpoint Resistance](../concepts/mhc-i-loss-and-interferon-pathway-defects-in-checkpoint-resistance.md) — Matsushita is the converse (HLA-class I *intact* selects the responders), Zaretsky 2016/Shin 2017 are the converse (HLA loss explains acquired/primary resistance).

## Open Questions

- Does the same neoAg × HLA score predict ICB response prospectively in HR-proficient HGSC, or is it only prognostic in untreated/standard-of-care patients?
- Does adding **mature-TLS density** as a third axis (Helmink 2020, Kasikova 2024 ovarian-specific) improve stratification beyond two axes, or is it redundant with the IFN-γ signature?
- Why is the HR-proficient T-cell-inflamed subgroup *cleaner* than the HR-deficient one — is HRD generating non-immunogenic neoAg "noise", or does HRD-associated TME suppression mute response despite mutational burden?
- Does **HLA-LOH at the protein level** (not just RNA expression) account for the patients in the neoAg-high HLA-low quadrant who do *not* show the T-cell-inflamed phenotype?
- Is the 40% HR-proficient + neoAg-high subset enriched for any particular oncogenic driver (TP53 mutation pattern, MYC amplification, CCNE1) that could be used as a more accessible clinical biomarker?
- Can this stratification be reproduced in larger HGSC cohorts (TCGA-OV, AOCS) using public proteogenomic data, ideally combined with ptmanchor-corrected phosphosite signals to refine the IFN-γ-pathway readout?

## Connections

- [B-Cell Neoantigen Research Map](../topics/b-cell-neoantigen-human-cancer.md)
- [B-Cell Neoantigen Proposal Anchor](../analyses/b-cell-neoantigen-proposal-anchor.md)
- [Cancer Resistance Manuscript Anchor](../analyses/cancer-resistance-manuscript-anchor.md)
- [MHC-I Loss and Interferon Pathway Defects in Checkpoint Resistance](../concepts/mhc-i-loss-and-interferon-pathway-defects-in-checkpoint-resistance.md)
- [Kasikova 2024 — TLS and B Cells in Ovarian Cancer](./kasikova-2024-tertiary-lymphoid-structures-b-cells.md)
- [Helmink 2020 — B Cells + TLS Promote ICB Response](./helmink-2020-b-cells-tertiary-lymphoid-structures.md)

## Sources

- PubMed: <https://pubmed.ncbi.nlm.nih.gov/32461346/>
- DOI: <https://doi.org/10.1136/jitc-2019-000375>
- PMC: <https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7254153/>
- Local PDF: pending acquisition (BMJ paywall + PMC anti-bot blocked automated download; obtain manually via [oca.korea.ac.kr/link.n2s?url=https://doi.org/10.1136/jitc-2019-000375](https://oca.korea.ac.kr/link.n2s?url=https://doi.org/10.1136/jitc-2019-000375))
