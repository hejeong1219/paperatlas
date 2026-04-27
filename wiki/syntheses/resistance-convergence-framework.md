---
title: "Cancer-Resistance Convergence Framework: Does Visibility / Access / Effector Dysfunction Hold Across Therapy Classes?"
tags:
  - synthesis
  - resistance
  - immune-evasion
  - convergence
themes:
  - resistance-framework
  - convergence
  - translational-oncology
manuscript_anchor: "resistance"
---

# Cancer-Resistance Convergence Framework

> **Driving question (Q35, manuscript-writing context).** The user's resistance review proposes that diverse therapy classes (checkpoint blockade, CAR-T, bispecific antibodies, ADCs, EGFR/KRAS-targeted therapy, endocrine therapy, PARP inhibitors) converge on **three immune-evasion axes — visibility, access, effector dysfunction**. Is the convergence claim empirically supported across *all* listed therapy classes, or is it strong for some and weak for others, and where does the framework most need additional evidence?

## 💡 Short answer (manuscript-ready)

**The three-axis convergence holds with high confidence for checkpoint blockade, CAR-T, BsAb, and targeted therapy (EGFR/KRAS) — moderate confidence for endocrine and ADC — and is genuinely under-tested for PARP.** The framework's strength is that the same three failure modes recur regardless of how a therapy *engages* the tumor (peptide-MHC, surface-protein, chemical, or hormonal); its weakness is that the *weight* of each axis varies enormously by therapy class, and the review must say so explicitly to avoid a "everything is convergence" critique.

## Mechanistic model — why convergence holds

The model is that every cancer therapy ultimately depends on, or is followed by, an immune step:

```
            Therapy            ◄─ different "engagement modes"
                 │
        ┌────────┼────────┐
        ▼        ▼        ▼
    Visibility  Access  Function   ◄─ shared downstream bottlenecks
        │        │        │
        ▼        ▼        ▼
              Outcome
```

- **Checkpoint blockade** depends on all three axes simultaneously — most exposed to convergence.
- **CAR-T / BsAb** bypass MHC restriction → less constrained by visibility, but still constrained by access and effector function (T-cell exhaustion, TME suppression).
- **ADC** is target-expression dependent → visibility (target expression loss) is the dominant axis.
- **Targeted therapy** (EGFR, KRAS) primarily kills tumor cells, but the *resistant clones that emerge* alter all three axes (EMT, MHC-I down, exclusion-prone TME) — convergence is on the *post-resistance* state, not on the primary mechanism.
- **Endocrine** therapy is unique: ESR1-mutant resistance disrupts T-cell surveillance (visibility/function axis link via direct ER-MHC regulation in tumor cells).
- **PARP inhibitors** drive cGAS-STING activation as their *immune* mechanism; reversion or BRCA1/2 secondary mutations silence STING signaling — visibility-axis loss.

## Per-class evidence audit

| Therapy class | Visibility | Access | Effector dysfunction | Convergence strength |
|---|---|---|---|---|
| **Checkpoint blockade** | HLA loss / B2M / JAK1-2 (Zaretsky 2016, Shin 2017) | TGF-β stromal exclusion (Mariathasan 2018) | Exhausted T cells, MDSC, TLS-poor | **Strong** — review's central case |
| **CAR-T (CD19)** | CD19 mutation / loss (Orlando 2018, Sotillo 2015) | Trafficking barriers (Labanieh 2023) | T-cell exhaustion, persistence loss (Sterner 2021) | **Strong** |
| **Bispecific (CD20×CD3)** | CD20 antigen modulation | Same TME barriers as CAR-T | T-cell exhaustion (Falchi 2023) | **Strong** (parallels CAR-T) |
| **ADC (T-DXd)** | HER2 expression loss (Chen 2026) | Less reported | cGAS-STING activation in responders (Oh 2024) | **Moderate** — visibility dominant |
| **EGFR-TKI (osimertinib)** | C797S, MET amp; cold TME with low MHC | Stromal exclusion in resistance (Han 2023) | EGFR-mutant NSCLC poor ICB response (Lai 2022, Lou 2016) | **Strong** at the post-resistance state |
| **KRAS G12Ci (sotorasib)** | KRAS amp / mutant emergence (Xue 2020, Tsai 2022) | Microenvironmental remodeling (Manabe 2022) | STK11/KEAP1-driven cold (Skoulidis 2018, 2024) | **Strong** at post-resistance state |
| **Endocrine (AI / fulvestrant)** | ESR1 LBD mutations disrupt T-cell surveillance (Lopez 2025) | Less studied | Limited direct data | **Moderate** — visibility/function link emerging |
| **PARP inhibitor** | BRCA reversion silences cGAS-STING; junctional neopeptides (Pettitt 2020) | Less studied | CD8⁺ T-cell recruitment in BRCA-deficient cancer (Pantelidou 2019) | **Under-tested** — visibility evidence emerging, access/function gap |

## Where the framework is strong

- **Mechanism-matched intervention table (Table 1 of the review)** is the cleanest test of convergence: the same intervention logic (restore antigenicity / remodel TME / reverse suppression) maps onto multiple therapy-class failures, supporting the framework as a *clinical action layer*, not just a conceptual framing.
- **CAR-T ↔ BsAb parallel** (Orlando 2018 CD19 loss vs Falchi 2023 CD20 loss) is the cleanest cross-class evidence — two different therapy modalities converge on the *same* visibility-axis failure when targeting B-lineage antigens. This is a clean example to anchor the review.
- **EGFR + KRAS post-resistance immune phenotype** is doubly converged: both produce a cold TME with low MHC-I and elevated exclusion markers, despite different oncogenic drivers (Sequist 2011, Lou 2016, Skoulidis 2018). The convergence here is downstream of *therapy + selection*, not of the original oncogene — which is a subtle but important distinction the review needs to make explicit.

## Where the framework is weak / under-tested

1. **PARP-resistance immune phenotype is largely speculative.** The review claims BRCA reversion silences cGAS-STING and disables visibility, but the *human-cohort evidence* is thin (mostly preclinical: Pantelidou 2019, Farkkila 2020). The review must either soften this claim or qualify it as a working hypothesis.
2. **Endocrine resistance and access/function axes** — almost all evidence is on the visibility axis (ESR1 → MHC-I / T-cell surveillance). Whether endocrine-resistant tumors also have stromal exclusion or exhausted effectors is largely unstudied. *This is the most important new study the user could propose in Future Work.*
3. **ADC + access** — almost no data on whether HER2-low or HER2-loss tumors also have stromal access barriers. The review currently rests on visibility (target loss) for ADC convergence.
4. **The framework risks being too inclusive.** If every therapy resistance maps to one or more axes, "convergence" loses falsifiability. The review needs a clear *anti-convergent* counterexample to maintain rigor — e.g., is there a therapy whose resistance is *not* explainable by these three axes? (Candidate: hormone-receptor-positive breast cancer driven by purely cell-autonomous CDK4/6 escape with intact immune contexture — needs explicit discussion.)
5. **Effector function vs access overlap.** Several papers (TGF-β, gut microbiota, stromal CAFs) blur the line between "physical access" and "functional state". The review should provide an operational distinction (mechanical/spatial = access; biochemical/exhaustion = function), otherwise the axes are not orthogonal.

## Apparent contradictions and how the model resolves them

- **CAR-T MHC bypass vs framework requiring visibility.** Resolved: CAR-T does bypass *T-cell* visibility (no MHC required) but inherits the surface-target-visibility axis (CD19 expression). The "visibility" axis is therefore better defined as *target visibility* (MHC-presented neoantigen *or* surface tumor antigen), not strictly MHC-I. The review should clarify this generalization explicitly.
- **PARP inhibitor benefit despite "cold" tumor (Farkkila 2020).** Resolved: PARP-induced DNA damage activates cGAS-STING, *creating* visibility transiently, then BRCA reversion silences it again. PARP is a case where the framework operates as a temporal cycle, not a static state.
- **Targeted therapy works without immune system in early phases (e.g., osimertinib first months).** Resolved: convergence claim is about the *resistant state*, not the initial response. The review must say "post-resistance immune-evasion convergence", not "resistance is fundamentally an immune problem".

## Testable predictions that follow from the model

1. **Cross-class biomarker portability**: a single mature-TLS-+-MHC-I-functional score should retain prognostic value for ICB, post-osimertinib salvage immunotherapy, and post-CAR-T relapse. Failure to do so on any one axis would falsify convergence.
2. **Mechanism-matched salvage trials**: visibility-axis failure (HLA loss) → neoantigen vaccine / TCR-T. Access failure → anti-VEGF / TGF-β / stromal targeting. Function failure → dual ICI / metabolic / engineered effector. The review's Table 1 implicitly proposes this; a prospective umbrella trial (e.g., PRECISION-IO) testing axis-stratified salvage would be the cleanest framework validation.
3. **Endocrine-resistance immune-context expansion**: scRNA + spatial profiling of ESR1-mutant breast cancer should reveal both visibility *and* access/function defects, not just visibility. If only visibility is present, the framework holds; if all three present, the framework gains evidence; if none, it loses.
4. **PARP-failure cohort BCR-seq + cGAS-STING readout**: human BRCA-reversion ovarian cancer biopsies should show reduced STING activation. A clean human-cohort dataset on this would resolve the framework's largest current gap.

## Implications for the resistance review manuscript

- **Frame convergence per axis weight, not as binary**: replace "all therapies converge on three axes" with "all therapies *touch* the three axes, but with class-specific weighting (Table)".
- **Open Discussion paragraph**: explicitly acknowledge PARP's under-tested status as the framework's largest gap; propose the BRCA-reversion + STING readout study as the natural next experiment.
- **Counterexample handling**: add a paragraph on "would the framework be falsifiable?" — propose hormone-receptor-positive breast cancer with intact immune contexture as the closest counterexample currently available.
- **Cross-modality biomarker prediction**: argue that the convergence claim, if true, predicts a *class-portable* immune-context biomarker — propose a prospective multi-class cohort study to test this. This is a high-impact future direction.

## Connections

- [Cancer Resistance Manuscript Anchor](../analyses/cancer-resistance-manuscript-anchor.md)
- [Immunotherapy Resistance and Immune Evasion](../topics/immunotherapy-resistance-and-immune-evasion.md)
- [MHC-I Loss and Interferon Pathway Defects in Checkpoint Resistance](../concepts/mhc-i-loss-and-interferon-pathway-defects-in-checkpoint-resistance.md)
- [TGF-Beta and Immune Exclusion](../concepts/tgf-beta-and-immune-exclusion.md)
- [Stromal and Myeloid Barriers to Immunotherapy](../concepts/stromal-and-myeloid-barriers-to-immunotherapy.md)
- [Antigen Loss, Lineage Switch, and Target Escape](../concepts/antigen-loss-lineage-switch-and-target-escape.md)
- [STK11-KEAP1-Related Immunotherapy Resistance in Lung Cancer](../concepts/stk11-keap1-related-immunotherapy-resistance-in-lung-cancer.md)
- [KRAS G12C Resistance and Ecosystem Remodeling](../concepts/kras-g12c-resistance-and-ecosystem-remodeling.md)
- [ESR1 Mutations and Endocrine Resistance in Breast Cancer](../concepts/esr1-mutations-and-endocrine-resistance-in-breast-cancer.md)

## Sources

- Mariathasan 2018 (Nature) — TGF-β + T-cell exclusion (urothelial cancer)
- Zaretsky 2016 (NEJM) — acquired PD-1 resistance via JAK1/2/B2M
- Shin 2017 (Cancer Discov) — primary PD-1 resistance via JAK1/2
- Orlando 2018 (Nat Med) — CD19 antigen loss in CAR-T relapse
- Falchi 2023 (Blood) — bispecific antibody resistance in B-NHL
- Skoulidis 2018, 2024 — STK11/KEAP1 + KRAS lung cancer immune-cold biology
- Lopez 2025 (Breast Cancer Res) — ESR1 + T-cell surveillance disruption
- Pantelidou 2019 (Cancer Discov) — PARP + STING + CD8 recruitment (preclinical)
- Pettitt 2020 (Cancer Discov) — BRCA1/2 reversion + neoantigen prediction
- ptmanchor manuscript Table 1 — mechanism-matched intervention logic source
