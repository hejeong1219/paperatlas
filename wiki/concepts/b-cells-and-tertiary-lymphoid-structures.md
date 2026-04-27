---
title: B Cells and Tertiary Lymphoid Structures
tags:
  - b-cells
  - tls
  - tumor-microenvironment
  - cancer
---

# B Cells and Tertiary Lymphoid Structures

B cells and TLS represent a major layer of intratumoral immune organization that can shape antigen presentation, plasma-cell differentiation, T-cell function, and response to immunotherapy.

## Key Points

- Mature TLS are generally associated with more organized local antitumor immunity.
- B-cell states inside TLS can influence the quality and persistence of intratumoral T-cell responses.
- Spatial organization matters: the same immune cell types can imply different biology depending on whether they form mature TLS.
- For translational cancer studies, antigen quality and local immune architecture should be interpreted together.
- Later checkpoint studies in melanoma, sarcoma, and neoadjuvant lung cancer suggest that TLS maturity and plasma-cell or memory-B-cell features can enrich for treatment benefit, not just prognosis.
- The advanced NSCLC literature now also suggests that TLS-related transcriptomic programs may retain predictive value in metastatic chemoimmunotherapy cohorts, not only in resection specimens.

## TLS Maturity vs TLS Density — which predicts ICB response?

> **Driving question (Q19, manuscript writing context).** When TLS density is measured by simple CD20⁺ counting, the predictive value for ICB response is inconsistent across cohorts. Is TLS *maturity* (germinal-center-like architecture: CD21⁺ follicular dendritic cells + CD23⁺ germinal-center B cells + MECA79⁺ high endothelial venules) the variable that actually correlates with response, and how should this be used in B-cell neoantigen proposal scoring?

### Where evidence converges (maturity matters more than density)

- **Helmink 2020 (melanoma + RCC, Nature)** — total CD20⁺ B-cell density was higher in responders but not statistically significant at baseline (P = 0.132). The *on-treatment* CD20 density (P = 0.0008) and the **TLS-to-tumor area ratio** (P = 0.002) were stronger. Architectural mIF showed the responder-associated TLS were **mature secondary-follicle-like** structures with CD21⁺/CD23⁺ germinal centers and MECA79⁺ high endothelial venules — i.e., the responder signal is the *organized* fraction, not the *raw count*.
- **Italiano 2022 PEMBROSARC (Nat Med)** — soft-tissue sarcoma is generally ICB-cold (RR ≈ 5%); pre-selecting on TLS-positive tumors lifted ORR to **30%** (vs 5% historical). TLS positivity here was scored by H&E + IHC architecture (mature follicle, GC presence) rather than density — a real-world example of TLS maturity functioning as a patient-selection biomarker.
- **Sun 2022 (J Immunother Cancer)** — resectable NSCLC neoadjuvant chemoimmunotherapy: both TLS abundance *and* maturation (defined by germinal-center markers) tracked with major pathologic response, with maturation giving cleaner separation.
- **Petitprez 2020 (Nature, soft-tissue sarcoma TLS classifier)** — sarcoma immune classes B and E (TLS-rich + B-cell-rich + GC-positive) had highest ICB benefit, formalizing the TLS-maturity → benefit link in a transcriptomic classifier.
- **Cabrita 2020 (Nature, melanoma companion paper)** — independent melanoma cohorts confirmed TLS + memory-B-cell + plasmablast signature as the strongest correlate of ICB benefit.

### Where evidence is mixed (density-only papers)

- Several earlier reviews counted CD20⁺ B cells without scoring architecture and reported either non-significant or contradictory associations. The current synthesis is that **density without maturation modifies the signal**: density is necessary but not sufficient.
- TLS density measured by 2D histology under-samples 3D structure, biasing studies that use a single section.

### Quantitative summary (for manuscript Discussion)

| Study | Tumor type | TLS density alone | TLS maturity / GC presence |
|---|---|---|---|
| Helmink 2020 | Melanoma | P = 0.132 baseline / P < 0.001 on-treatment | Mature TLS strongly associated |
| Italiano 2022 | Sarcoma | TLS density screening | TLS-positive ORR 30% vs ~5% |
| Sun 2022 | NSCLC | density correlated | maturation cleaner separation |
| Petitprez 2020 | Sarcoma | classes A/C/D less benefit | classes B/E (TLS+GC) most benefit |

### Gaps for future research (Future Work bullets)

1. **No standardized TLS-maturity score** — every cohort defines maturity differently (CD23 + CD21 + MECA79 vs follicular morphology vs transcriptomic signature). A consensus score, ideally on mIF or transcriptomics, is the obvious next deliverable for the field.
2. **mIF-based maturity scoring** has not been validated against transcriptomic TLS signatures (e.g., Cabrita-12-gene, Meylan-9-gene) on the same cohort — the two approaches may capture overlapping but distinct biology.
3. **Mature-TLS-induction therapy** (anti-CD40 agonist, IL-21, intratumoral CXCL13, anti-LTβR) is preclinically supported but clinically untested in patients selected for TLS-low → TLS-high conversion. This is the obvious translational gap.
4. **Spatial topology** of mature TLS within tumors (peritumoral, intratumoral, invasive margin) likely modifies functional impact, but no large-cohort spatial study has reported this systematically.
5. **Tumor-type generalization** — most maturity-vs-density evidence is from melanoma, sarcoma, NSCLC. PDAC, HCC, and prostate cancer (immune-cold tumors) need their own maturity-vs-density evaluation. Amisaki 2025 (PDAC, IL-33-induced TLS) is one early data point but more is needed.
6. **B-cell neoantigen specificity within mature TLS** — whether the antibodies produced in mature germinal centers are tumor-antigen-specific is still poorly characterized in human samples. BCR-Ag pairing studies in mature-TLS cohorts are the obvious next experiment.

### Implication for the B-cell neoantigen proposal

For the proposal's scoring framework, **TLS density alone should not be the immune-context input** — the better input is a binary or graded mature-TLS flag combined with B-cell-derived transcriptomic markers (Cabrita's 9-gene, plus MZB1/JCHAIN/IGLL5 from Helmink). This doubles down on the proposal's claim that "B cells in tumor" is meaningful only when paired with structural context.

## Connections

- [Tertiary lymphoid structures and B cells determine clinically relevant T cell phenotypes in ovarian cancer](../sources/kasikova-2024-tertiary-lymphoid-structures-b-cells.md)
- [Single-cell and spatial transcriptome analyses reveal tertiary lymphoid structures linked to tumour progression and immunotherapy response in nasopharyngeal carcinoma](../sources/liu-2024-single-cell-and-spatial-transcriptome.md)
- [Mature tertiary lymphoid structures evoke intra-tumoral T and B cell responses via progenitor exhausted CD4+ T cells in head and neck cancer](../sources/li-2025-mature-tertiary-lymphoid-structures-headneck.md)
- [B cells and tertiary lymphoid structures in cancer therapy response](../sources/hegoburu-2025-b-cells-and-tertiary-structures.md)
- [B cells and tertiary lymphoid structures promote immunotherapy response](../sources/helmink-2020-b-cells-tls-immunotherapy-response.md)
- [Pembrolizumab in soft-tissue sarcomas with tertiary lymphoid structures: a phase 2 PEMBROSARC trial cohort](../sources/italiano-2022-pembrolizumab-soft-tissue-sarcomas-tls.md)
- [Maturation and abundance of tertiary lymphoid structures are associated with the efficacy of neoadjuvant chemoimmunotherapy in resectable non-small cell lung cancer](../sources/sun-2022-tls-neoadjuvant-chemoimmunotherapy-resectable-nsclc.md)
- [Tertiary lymphoid structures gene signature predicts response to immunotherapy plus chemotherapy in advanced non-small cell lung cancer](../sources/du-2025-tls-gene-signature-advanced-nsclc.md)

## Sources

- [Tertiary lymphoid structures and B cells determine clinically relevant T cell phenotypes in ovarian cancer](../sources/kasikova-2024-tertiary-lymphoid-structures-b-cells.md)
- [Single-cell and spatial transcriptome analyses reveal tertiary lymphoid structures linked to tumour progression and immunotherapy response in nasopharyngeal carcinoma](../sources/liu-2024-single-cell-and-spatial-transcriptome.md)
- [Mature tertiary lymphoid structures evoke intra-tumoral T and B cell responses via progenitor exhausted CD4+ T cells in head and neck cancer](../sources/li-2025-mature-tertiary-lymphoid-structures-headneck.md)
- [B cells and tertiary lymphoid structures in cancer therapy response](../sources/hegoburu-2025-b-cells-and-tertiary-structures.md)
- [B cells and tertiary lymphoid structures promote immunotherapy response](../sources/helmink-2020-b-cells-tls-immunotherapy-response.md)
- [Pembrolizumab in soft-tissue sarcomas with tertiary lymphoid structures: a phase 2 PEMBROSARC trial cohort](../sources/italiano-2022-pembrolizumab-soft-tissue-sarcomas-tls.md)
- [Maturation and abundance of tertiary lymphoid structures are associated with the efficacy of neoadjuvant chemoimmunotherapy in resectable non-small cell lung cancer](../sources/sun-2022-tls-neoadjuvant-chemoimmunotherapy-resectable-nsclc.md)
- [Tertiary lymphoid structures gene signature predicts response to immunotherapy plus chemotherapy in advanced non-small cell lung cancer](../sources/du-2025-tls-gene-signature-advanced-nsclc.md)
