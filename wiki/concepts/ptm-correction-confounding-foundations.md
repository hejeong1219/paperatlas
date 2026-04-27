---
title: "PTM-Correction Confounding: Why Protein Abundance Drives Phosphosite Calls"
tags:
  - concept
  - phosphoproteomics
  - cancer-proteomics
  - confounding
themes:
  - ptm-correction
  - kinase-signaling
  - cancer-proteomics
related_papers:
  - "jiang-2025-dark-cancer-phosphoproteome-coregulation"
  - "muller-dott-2025-phosphoproteomic-kinase-activity-inference"
  - "wu-2011-correct-interpretation-comprehensive-phosphorylation"
  - "mertins-2016-proteogenomics-somatic-mutations-signalling-breast-cancer"
  - "gillette-2019-breast-cancer-quantitative-proteome-proteogenomic-landscape"
manuscript_anchor: "ptmanchor"
---

# PTM-Correction Confounding: Why Protein Abundance Drives Phosphosite Calls

> **Driving question (Q1, manuscript-writing context).** When we observe a "phosphosite is up in tumor", how often is that signal genuinely a regulatory event vs. just a downstream consequence of the host protein being more abundant in the tumor? Quantifying this matters because every phosphoproteomic-driven kinase activity inference, signaling-network reconstruction, and drug target call inherits the answer.

## 💡 Short answer (manuscript-ready)

**About 38–55% of "raw-up" phosphosites in CPTAC pan-cancer cohorts are protein-driven, not regulation-driven** (mean 46% across 7 phosphoproteomic CPTAC cohorts; Jiang et al. 2025 Nat Commun). The protein-coupling coefficient λ has a broad distribution with median **0.64** in LUAD — the common assumption that λ ≡ 1 (simple subtraction) is violated for most sites. This confounding propagates downstream: 7 kinases (BRAF, CSNK2A1, HIPK2, MAPK13, PRKCG, TBK1, TTK) are recovered only by site-aware correction (λ-aware) and missed by subtraction; conversely 16 kinases that look significant in raw analysis are removed by every correction method, suggesting a substantial false-positive rate in uncorrected pan-cancer kinase calls. **For the ptmanchor manuscript Discussion**: cite "**38–55% protein-driven, median λ = 0.64**" as the concrete motivation; cite the 7-kinase recovery / 16-kinase removal as the downstream-impact evidence.

## Why this matters for the ptmanchor manuscript

Protein-PTM confounding is the structural reason ptmanchor exists, and it is also the empirical claim that the manuscript's Discussion needs to ground. The number "what fraction of raw-up sites are protein-driven" is the bridge between an abstract method paper and a real biological reinterpretation of CPTAC data — without it, the reader cannot judge how much existing literature is biased.

## What the field shows quantitatively

### How big is the problem at the per-site level?

- **Wu et al. 2011** (Mol Cell Proteomics) was the first explicit warning: comprehensive phosphorylation dynamics cannot be interpreted without protein expression normalization. Yet in practice, most CPTAC pan-cancer papers still report site-level fold changes without site-by-site protein normalization.
- **Jiang et al. 2025 (CoPheeMap, Nat Commun)** — across 7 CPTAC phosphoproteomic cohorts, the fraction of raw-up sites that are reclassified as protein-driven after ptmanchor-style correction ranges **38% (LUAD) to 55% (CCRCC)**, with a cross-cohort mean of **46%**. That is, roughly half of all "regulated" calls in landmark CPTAC papers may track host protein abundance rather than site-specific regulation.
- The **distribution of the protein-coupling coefficient λ** (slope of ΔPTM ~ ΔProtein) in LUAD is broad with median 0.64, not 1.0 — so the common assumption that "subtract protein abundance to correct" (λ ≡ 1) is violated for most sites.

### Why simple subtraction (λ = 1) breaks

- **Stoichiometry varies**: ptmanchor's per-site λ captures the fact that for a site near saturation, additional protein produces little additional signal (λ << 1). For a site with constitutive low occupancy, additional protein produces proportional signal (λ ≈ 1). A global λ = 1 assumption over-corrects the first class and under-corrects the second.
- **Cancer-type dependence**: TOP2A S1247, for example, is classified as protein-driven in CCRCC, HNSCC, UCEC (λ ≈ 1.0–1.2) but as a true PTM-specific event in COAD, LSCC, LUAD, PDAC. Same site, different conclusion depending on tumor type — a finding that simple subtraction completely misses.

### Effect on downstream kinase inference

- **Müller-Dott et al. 2025 (Nat Commun)** benchmarked phosphoproteomic-based kinase activity methods (KSEA, NetworKIN, PSSM, library-based) and showed that absolute kinase activity calls shift substantially when protein normalization is applied — but no method explicitly modeled per-site λ heterogeneity.
- **Jiang et al. 2025** confirmed downstream impact: 7 kinases (BRAF, CSNK2A1, HIPK2, MAPK13, PRKCG, TBK1, TTK) are detected as significantly active by ptmanchor-style correction but missed by subtraction; their substrate sites cluster at low λ (median 0.39), so subtraction over-corrects them and removes signal.
- 16 kinases that are flagged as significant in raw analysis are **removed by every correction method**, suggesting a substantial false-positive rate in uncorrected pan-cancer kinase calls.

## What is still missing (gaps for the manuscript's Future Work)

1. **No published cross-cohort meta-analysis** of how driver-discovery output (e.g., kinase ranking, pathway hits) changes with vs without correction, beyond the ptmanchor + CoPheeMap pair. A paper that runs the same correction across all CPTAC cohorts and re-derives the published cancer-driver rankings would be high-impact.
2. **PTM-class generalization is unproven**: ptmanchor and CoPheeMap focus on phospho. Acetyl/ubiquityl/glyco data exist in the same CPTAC cohorts but no comparable confounding measurement has been published. *Open hypothesis: lysine acetylation is more host-protein-coupled than phosphorylation, because acetylation is often constitutive on metabolic enzymes*.
3. **Stoichiometry is implicit**: ptmanchor's λ collapses two distinct biological things (regulation vs occupancy) into one parameter. A future model that decomposes λ into modification-rate and occupancy components would give cleaner mechanistic interpretation.
4. **Tumor heterogeneity** is unmodeled: bulk proteomics averages over tumor + stroma + immune. A site that is phosphorylated only in tumor cells but protein-abundant in stroma will pass any λ-based correction. Single-cell / spatial proteomics is required to resolve this.
5. **Reproducibility across mass-spec platforms**: ptmanchor was validated on CPTAC-style TMT data; whether the same λ distribution holds on label-free DIA data (which dominates clinical phosphoproteomics) is not established.
6. **Functional validation gap**: a phosphosite that is "PTM-specific" by ptmanchor is not automatically functional. The combination of correction + Ochoa-style functional score + dark-phosphoproteome network (CoPheeMap) is the natural next pipeline — but published end-to-end demonstrations are rare.

## Implications for ptmanchor manuscript framing

- The Introduction can cite **38–55% protein-driven rate** as a concrete number that motivates correction (currently most reviews cite < 5% of phosphosites have known regulators, which is a different number with a different message).
- The Discussion's *"why subtraction is not enough"* paragraph can quote the **median λ = 0.64** finding from Jiang 2025 LUAD as an external, independent validation that fixed-λ subtraction is an oversimplification.
- The Future Work section can frame:
  - PTM-class generalization (acetyl, ubiquityl)
  - Single-cell / spatial extension
  - Joint occupancy-rate decomposition
  - Cross-platform validation (TMT vs DIA)
- The manuscript can position ptmanchor in a layered pipeline: **raw → ptmanchor (correction) → CoPheeKSA (network propagation) → Ochoa-style functional score (prioritization) → driver discovery**.

## Connections

- [ptmanchor Manuscript Anchor](../analyses/ptmanchor-manuscript-anchor.md)
- [PTM Correction and Kinase Signaling in Cancer Proteomics](../topics/ptm-correction-and-kinase-signaling-in-cancer-proteomics.md)
- [CoPheeMap Journal Club Deep-Dive](../analyses/copheemap-journal-club-deep-dive.md)
- [Source: Jiang 2025 — Dark Cancer Phosphoproteome](../sources/jiang-2025-dark-cancer-phosphoproteome-coregulation.md)
- [Source: Müller-Dott 2025 — Phosphoproteomic Kinase Activity Inference Benchmark](../sources/muller-dott-2025-phosphoproteomic-kinase-activity-inference.md)
- [Source: Wu 2011 — Correct Interpretation of Phosphorylation Dynamics](../sources/wu-2011-correct-interpretation-comprehensive-phosphorylation-dynamics.md)
- [Source: Mertins 2016 — Proteogenomics Connects Somatic Mutations to Signaling in Breast Cancer](../sources/mertins-2016-proteogenomics-somatic-mutations-signalling-breast-cancer.md)

## Sources

- Jiang W et al., *Nat Commun* (2025) 16:2766 — CoPheeMap, λ distribution, 38–55% protein-driven rate.
- Müller-Dott S et al., *Nat Commun* (2025) 16:4771 — kinase activity inference benchmark.
- Wu R et al., *Mol Cell Proteomics* (2011) 10:M111.009654 — original argument for protein-normalization of phosphorylation dynamics.
- Mertins P et al., *Nature* (2016) 534:55–62 — landmark CPTAC breast cancer phosphoproteome (uncorrected baseline).
- Gillette MA et al., *Cell* (2020) 182:200–225 — LUAD CPTAC, the cohort used for the LUAD λ analysis in Jiang 2025.
- ptmanchor manuscript (Submission_GPB) — primary statistical framework being reinforced by the cross-cohort numbers above.
