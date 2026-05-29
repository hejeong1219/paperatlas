---
title: Cancer Multiomics Resistance Biomarker Evidence Boundary Map
tags:
  - analysis
  - evidence-boundary
  - cancer-multiomics
  - treatment-resistance
  - biomarkers
  - proteomics
  - phosphoproteomics
themes:
  - resistance-biomarkers
  - primary-resistance
  - acquired-resistance
  - refractory-state
  - validation-tier
date: 2026-05-28
---

# Cancer Multiomics Resistance Biomarker Evidence Boundary Map

This page is the second durable LLM-Wiki question expansion for the Cancer Multiomics resistance biomarker thread. It asks a presentation-friendly question: **given the data structure in each paper, how far can we go in interpreting each protein or phosphosite marker?**

## Key Points

- The next useful step is not to ask whether proteomics or phosphoproteomics can find resistance biomarkers in general. The useful step is to sort each candidate signal by the kind of evidence behind it.
- A baseline response-labeled protein or phosphosite signal is usually a **primary resistance / baseline non-response marker**, not automatically an acquired-resistance marker.
- Same-patient pre/post, progression, or serial data are required before a signal can be interpreted as **therapy-emergent acquired resistance**.
- Post-treatment or refractory-only datasets can still be valuable, but they should be framed as **resistance-state** or **refractory-state** biomarkers unless emergence is directly observed.
- The current local wiki is strong enough to support a review-style evidence-boundary framework. It is not yet strong enough to say that the field has a complete patient-level longitudinal proteome/phosphoproteome map of acquired resistance across drug classes.

## Starting Question

> In response-labeled cancer proteogenomics papers, which reported protein/phosphosite markers are baseline non-response markers, and which ones have evidence of therapy-emergent change?

This question follows from [Cancer Multiomics Resistance Biomarker Question Chain](./cancer-multiomics-resistance-biomarker-question-chain.md). It treats `pre/post data structure` as one test inside a larger question: **what does the evidence actually allow us to say?**

## Evidence Categories

| Evidence category | Minimum data needed | Careful wording | Wording to avoid |
| --- | --- | --- | --- |
| Baseline primary resistance marker | Pre-treatment sample plus response endpoint | "Baseline feature associated with non-response" | "Acquired resistance mechanism" |
| Therapy-emergent acquired-resistance marker | Same-patient pre/post, progression sample, or serial time course | "Feature gained, lost, or selected under therapy" | "Emergent" from post-only samples |
| Adaptive tolerance marker | Early on-treatment or model-system time course under drug pressure | "Drug-tolerant/adaptive state marker" | Patient-level acquired resistance without patient validation |
| Refractory-state marker | Treatment-failed or refractory sample without matched baseline | "Current resistant-state feature" | Timing of emergence |
| Feature-design atlas signal | Treatment-naive atlas without response endpoint | "Candidate readout for target/pathway/immune state" | Direct predictive biomarker |

## Paper-Level Evidence Map

| Local page | Sampling / endpoint | Best-supported interpretation | Protein/phosphosite role | Gap created |
| --- | --- | --- | --- | --- |
| [Lee 2026 TNBC](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md) | Baseline TNBC multiomics with pCR/non-pCR; paired post-treatment protein subset | Baseline non-response marker plus limited residual-state comparison | Estrogen protein signature, GRK2 PTM-SEA, ITGB8 status, AURKB-related treatment logic | Does the same protein/phosphosite state emerge after therapy in the same patient, or was it present at baseline? |
| [Anurag 2022 TNBC](../sources/anurag-2022-proteogenomic-markers-chemotherapy-resistance-response.md) | Pretreatment biopsy with pCR/RCB endpoint | Baseline chemotherapy response marker | Proteome metabolism/OXPHOS and phosphoproteome kinase targets separate response-associated programs | Strong baseline evidence, but not an acquired-resistance time course |
| [Holt 2025 MIBC](../sources/holt-2025-proteogenomic-characterization-unveils-biomarkers-associated.md) | Cisplatin-based response-labeled cohort | Baseline chemoresistance marker | DDR mutation status is insufficient; protein DNA-repair/G2M and GSK3B-S9-like phosphosite state refine response | Phosphosite state needs timing and protein-correction qualification before emergence is inferred |
| [Jaehnig 2025 HER2+ Breast](../sources/jaehnig-2025-proteogenomic-analysis-calgb-40601-alliance.md) | Pretreatment anti-HER2 trial biopsies with pCR/non-pCR | Baseline anti-HER2 non-response marker and target-status QC marker | ERBB2 copy/RNA/protein/phospho ladder separates false target status from confirmed HER2+ resistance state | Need pre/post anti-HER2 data to distinguish baseline bypass state from therapy-selected state |
| [Zhang 2023 ccRCC Sunitinib](../analyses/cancer-multiomics-literature/zhang-2023-proteogenomics-clear-cell-renal-response-tyrosine-kinase-inhibitor.md) | Therapy-specific response cohort | Baseline TKI response marker | Pathway/kinase/TME state can be more informative than target abundance alone | Still mainly response-labeled baseline logic, not longitudinal acquired resistance |
| [Sambath 2026 Cervical CCRT](../sources/sambath-2026-integrated-genomic-proteomic-cervical-cancer-chemoradiation-resistance.md) | CCRT sensitive/resistant labels with proteome/phosphoproteome subset | Baseline chemoradiation resistance marker | DNA repair pathway convergence across genomic, protein, and phosphosite layers | Proteome discovery size is small; timing remains response-label rather than same-patient emergence |
| [Hsu 2025 Osimertinib DTP](../sources/hsu-2025-phosphoproteomics-osimertinib-tolerant-persister-cells-reveals.md) | Model-system drug-tolerant persister and recovery time course | Adaptive tolerance phosphoproteomic marker | Time-resolved phosphoproteome exposes CDK1/YAP/mTOR-like adaptive signaling | Strong time-course logic, but model-system rather than patient pre/post proof |
| [Chmielecki 2023 FLAURA](../sources/chmielecki-2023-acquired-resistance-first-line-osimertinib.md) | Baseline tissue plus paired plasma ctDNA at acquired resistance | Acquired genomic-resistance context | Shows a large unexplained fraction after ctDNA mechanism check; motivates functional omics | Lacks patient proteome/phosphoproteome layer for the unexplained acquired-resistance fraction |
| [Yaeger 2023 KRASG12C-EGFR](../sources/yaeger-2023-molecular-characterization-acquired-resistance-krasg12c-egfr.md) | Serial ctDNA/progression acquired-resistance evidence | Strong acquired-resistance timing example | Time axis is strong, but functional phosphoproteome/proteome readout is missing | Ideal design gap: pair serial genomic tracking with proteome/phosphoproteome state |
| [Memon 2024 PD-(L)1 NSCLC](./cancer-multiomics-literature/memon-2024-clinical-molecular-features-acquired-resistance.md) | Acquired resistance after checkpoint blockade | Acquired immune-resistance state | Immune-inflamed but dysfunctional resistance framing | Need protein/phosphosite or spatial functional readouts to make this a proteogenomic biomarker story |
| [Resistance-State Subtyping in Refractory Gastric Cancer](./resistance-state-subtyping-refractory-gastric-cancer.md) | Refractory/treatment-failed framing | Refractory-state subtype marker | IC1/IC2 can be discussed as resistant-state heterogeneity | Do not infer acquired emergence without baseline or serial samples |

## What This Page Changes

The question chain now separates three different tasks:

1. **Literature review task:** classify published resistance proteogenomics papers by timing, molecular unit, endpoint, and validation strength.
2. **Data-design task:** define what pre/post or time-course data would be needed to upgrade a baseline or refractory marker into an acquired-resistance marker.
3. **Analysis task:** if user-owned data exist, test whether protein/phosphosite features add interpretable signal after clinical and genomic blocks, while labeling the result according to the sampling design.

## Graph Capture Use

For the presentation, this page should be captured as a question-specific Obsidian subgraph, not as a standalone table only.

Suggested graph view:

- Center node: `Cancer Multiomics Resistance Biomarker Evidence Boundary Map`
- Baseline marker cluster: Lee 2026, Anurag 2022, Holt 2025, Jaehnig 2025, Zhang 2023, Sambath 2026
- Acquired/adaptive cluster: Chmielecki 2023, Yaeger 2023, Memon 2024, Hsu 2025
- Bridge node: `Primary and Acquired Resistance Proteogenomics Ingest Map`
- Interpretation node: `PTM Correction and Kinase Signaling in Cancer Proteomics`

Slide caption:

> 같은 "resistance biomarker"라도 치료 전부터 보이는 marker인지, 치료 후 새로 생긴 marker인지, adaptive tolerance marker인지, refractory-state marker인지 먼저 구분해야 한다.

## Emerging Research Gap

The gap is not simply "we need more evidence layers." The sharper gap is:

> Response-labeled baseline proteogenomics can nominate primary resistance markers, and serial genomics can establish acquired-resistance timing, but same-patient longitudinal patient proteome/phosphoproteome data that connect therapy-emergent timing to functional protein or kinase-state biomarkers remain sparse.

## Next Question

> Which candidate markers in the local corpus have stronger follow-up evidence: independent cohort, perturbation experiment, organoid/PDX, IHC/PRM, or patient longitudinal recurrence?

This should become the next durable page only if it is expanded into a table. A good slug would be:

`cancer-multiomics-resistance-biomarker-validation-tiers.md`

## Connections

- [Cancer Multiomics Resistance Biomarker Question Chain](./cancer-multiomics-resistance-biomarker-question-chain.md)
- [Cancer Multiomics Presentation Storyline](./cancer-multiomics-presentation-storyline.md)
- [Primary and Acquired Resistance Proteogenomics Ingest Map](./primary-acquired-resistance-proteogenomics-ingest-map.md)
- [Drug Response Proof-of-Concept with Global Proteome, Phosphoproteome, and Somatic SNV](./drug-response-poc-global-phospho-somatic-snv.md)
- [PTM Correction and Kinase Signaling in Cancer Proteomics](../topics/ptm-correction-and-kinase-signaling-in-cancer-proteomics.md)

## Sources

- Local wiki source and analysis pages linked in the evidence map.
- This page is an analysis layer. Marker-level interpretations should remain bounded by the linked source pages and their stated sampling designs.
