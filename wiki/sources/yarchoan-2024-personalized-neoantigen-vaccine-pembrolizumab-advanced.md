---
title: "Personalized neoantigen vaccine and pembrolizumab in advanced hepatocellular carcinoma: a phase 1/2 trial"
authors:
  - "Yarchoan"
  - "Gane"
  - "Marron"
year: "2024"
journal: "Nature medicine"
doi: "10.1038/s41591-024-02894-y"
pmid: "38584166"
pmcid: "PMC11031401"
paper_kind: clinical-trial
pdf: "raw/inbox/papers/yarchoan-2024-personalized-neoantigen-vaccine-pembrolizumab-advanced.pdf"
topic: bcell-neoantigen
extra_topics:
  - "resistance"
tags:
  - "bcell-neoantigen"
  - "neoantigen"
  - "vaccine"
  - "pembrolizumab"
  - "hepatocellular-carcinoma"
  - "pmid-38584166"
themes:
  - "neoantigen-discovery"
  - "clinical-translation"
  - "vaccine-trial"
---
# Personalized neoantigen vaccine and pembrolizumab in advanced HCC (GT-30 trial)

_Nature Medicine 30:1044–1053, 2024 — phase 1/2 trial._ PMID: [38584166](https://pubmed.ncbi.nlm.nih.gov/38584166/) · DOI: [10.1038/s41591-024-02894-y](https://doi.org/10.1038/s41591-024-02894-y) · ClinicalTrials.gov: [NCT04251117](https://clinicaltrials.gov/study/NCT04251117)

## Summary

GT-30 is a 36-patient single-arm phase 1/2 trial in advanced HCC that previously progressed on a multi-tyrosine-kinase inhibitor. The intervention is GNOS-PV02, a personalized DNA-plasmid vaccine encoding up to 40 patient-specific neoantigens, co-formulated with a plasmid-IL-12 adjuvant (`pIL12`), delivered intradermally with electroporation, on top of standard-dose pembrolizumab. The trial demonstrates that personalized neoantigen vaccination is feasible at scale (every patient got their own product), is safe (no DLT, no grade ≥3 TRAE — only injection-site reactions in 41.6%), and produces tumor-side biology consistent with on-target T-cell activity (vaccine-specific CD4⁺ and CD8⁺ T cells in 19/22 patients by ELISpot, TCRβ tracking shows vaccine-induced clones expanding into tumor, and TCR-CDR cloning confirms neoantigen reactivity of expanded intratumoral clones). The headline efficacy signal is an ORR of 30.6% (11/36, 3 CR) — about 2× the historical 12–18% pembrolizumab monotherapy benchmark in HCC — with response correlating to neoantigen count in the vaccine. Importantly, this is a single-arm trial, so the response delta vs. pembrolizumab alone is suggestive, not definitive.

## Key Points

- **Patient population**: 36 advanced HCC patients, all post-mTKI (91.6% lenvatinib), Child-Pugh A, BCLC stage B (50%) or C (50%); etiology mixed (HBV 22.2%, HCV 33.3%, non-viral 41.7%).
- **Vaccine platform**: GNOS-PV02 = DNA plasmid encoding up to 40 personalized MANAs (mutation-associated neoantigens) selected from patient WES + RNA-seq + germline DNA; co-administered with `pIL12` (DNA plasmid encoding IL-12) for local cytokine adjuvant; delivered ID + electroporation.
- **Primary endpoint (safety/immunogenicity)**: no DLT, no grade ≥3 TRAE, only local injection-site reactions (15/36, 41.6%); 19/22 evaluable patients (86.4%) developed neoantigen-specific T-cell responses by ELISpot.
- **Efficacy (secondary)**: ORR 30.6% (11/36) including 3 complete responses (8.3%) by RECIST 1.1; the ORR is roughly double historical pembrolizumab monotherapy benchmarks in HCC (12–18%) but the trial is single-arm.
- **Dose-response**: clinical response was associated with the **number of neoantigens encoded** in the vaccine, suggesting a "more antigens, more chance of finding immunogenic ones" effect rather than a single dominant epitope.
- **Mechanism evidence**: vaccine-specific T cells are CD4⁺ AND CD8⁺, proliferative (Ki-67) and cytolytic (granzyme B); TCRβ bulk + scTCR sequencing show post-vaccination clones expanding in blood AND infiltrating tumor; CDR3 cloning of intratumoral clones confirms neoantigen reactivity in vitro — closing the loop between vaccine input and tumor effector output.
- **Vaccine production logistics**: all 36 patients had their personalized vaccine product ready at the time they were eligible to start second-line therapy → addresses a long-standing operational concern about whether personalized vaccines can keep up with the second-line decision window.

## Methods

Single-arm, open-label, multicenter phase 1/2; primary endpoints safety + immunogenicity, secondary endpoints efficacy (RECIST 1.1) + feasibility. Neoantigen prediction from WES (tumor + germline) + RNA-seq using the Geneos pipeline. Immunogenicity by IFN-γ ELISpot pre/post vaccination. Mechanism by multi-parametric flow + CyTOF + bulk TCRβ + scRNA/scTCR seq + CDR3 cloning of expanded TILs into Jurkat reporter cells stimulated with predicted neoantigen peptides.

## Limitations

- **Single-arm**: no randomized control vs pembrolizumab alone — the ORR comparison is to historical benchmarks, which is hypothesis-generating but not definitive.
- **Small cohort** (n = 36) and heterogeneous etiology (HBV/HCV/non-viral mixed); subgroup signal interpretation is under-powered.
- **HCC-specific**: low-TMB, immune-cold context — translation to TMB-low cold tumors of other origins (PDAC, prostate) is not tested here.
- **Neoantigen dose-response is correlative**: more encoded neoantigens correlated with response, but encoding ≠ presentation — the paper does not show that responders had more *presented* (HLA-bound) neoantigens.
- **No B-cell readout**: despite the topic relevance, the paper focuses on T-cell readouts and does not measure tumor-side B-cell or TLS responses, leaving open whether the vaccine engages humoral / TLS biology.
- **mTKI prior treatment** may have shaped the immune microenvironment in ways that influence vaccine response (lenvatinib is known to remodel TME), making the framework not directly portable to first-line settings.

## Relevance to anchors

- Direct evidence for the [B-Cell Neoantigen Proposal Anchor](../analyses/b-cell-neoantigen-proposal-anchor.md): demonstrates a feasible end-to-end pipeline (WES + RNA-seq → vaccine production within the second-line window → on-target T-cell expansion in tumor) that the proposal aims to extend on the **B-cell side**.
- Relevant to the [Cancer Resistance Manuscript Anchor](../analyses/cancer-resistance-manuscript-anchor.md) under "immune visibility loss" axis: HCC is a paradigmatic low-TMB, T-cell-cold tumor, and a vaccine targeting up to 40 neoantigens is exactly the "restore antigenicity" intervention proposed in the convergence framework.
- Sets a benchmark for vaccine + ICI combinations: ORR 30.6% in TKI-refractory advanced HCC, with safety profile suitable for combination, supports continuing this class of trial in other immune-cold tumor types.

## Open Questions

- Does the same DNA + pIL12 + ICI platform reproduce in randomized trials, and is the ORR doubling stable?
- Are responders enriched for vaccines with **specific** neoantigen properties (e.g., clonality, expression level, predicted MHC-I binding strength) beyond raw count?
- Why does CD4 vaccine-specific response track CD8? Is HCC's HLA-II expression supporting CD4 effector activity directly, or is CD4 helping prime/maintain CD8?
- Does the vaccine engage tumor B-cells / TLS at all, and if so, do humoral responses to encoded neoantigens contribute to control or epitope spreading?
- How portable is the workflow to other low-TMB tumors (PDAC, prostate), and does the same dose-response (more antigens = better) hold there?

## Connections

- [B-Cell Neoantigen Research Map](../topics/b-cell-neoantigen-human-cancer.md)
- [B-Cell Neoantigen Proposal Anchor](../analyses/b-cell-neoantigen-proposal-anchor.md)
- [Clinical Translation of Neoantigen Research](../concepts/clinical-translation-of-neoantigen-research.md)
- [Saxena 2025 — Atezolizumab + Personalized Neoantigen Vaccine in Urothelial Cancer (sister-trial design)](./atezolizumab-2025-personalized-neoantigen-vaccination-urothelial-cancer.md)
- [Borgers 2025 — Personalized Autologous Neoantigen-Specific Therapy](./borgers-2025-personalized-autologous-neoantigen-specific-therapy.md)

## Sources

- Local PDF: `raw/inbox/papers/yarchoan-2024-personalized-neoantigen-vaccine-pembrolizumab-advanced.pdf`
- PubMed: <https://pubmed.ncbi.nlm.nih.gov/38584166/>
- DOI: <https://doi.org/10.1038/s41591-024-02894-y>
- PMC: <https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11031401/>
