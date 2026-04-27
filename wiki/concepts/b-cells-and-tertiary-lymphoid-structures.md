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

### 💡 Short answer (manuscript-ready)

**Yes — TLS maturity outperforms density**, because density is a *structural* readout but maturity is a *functional* readout: a mature TLS = a functioning ectopic germinal center making **somatically hypermutated, class-switched, antigen-specific B cells** that feed both plasma-cell-derived antibody and CD4-help to local CD8 T cells. Density alone counts the cells; maturity counts the *functioning unit*. The convergence of melanoma (Helmink 2020, Cabrita 2020) and sarcoma (Italiano 2022, Petitprez 2020) cohorts on the same ranking is therefore not a coincidence — it is the same biology surfacing through different tumor microenvironments. **For the B-cell neoantigen proposal**: the immune-context input should be a *functional* score (mature-TLS flag + B-cell transcriptomic signature + somatic hypermutation evidence), not a *structural* count.

### Mechanistic model — why maturity is the right axis

A working causal chain that the above papers collectively support:

```
Tumor antigen presence
        │
        ▼
B-cell aggregation (driven by CXCL13)        ← TLS density measures this
        │
        ▼
Germinal-center formation                     ← mature TLS marker (CD21⁺ FDC + CD23⁺ GC)
   • somatic hypermutation
   • class switching (IgG, IgA)
   • affinity maturation against tumor antigens
        │
        ▼
Plasma cell + memory B cell output            ← functional readout
   • antibody → ADCC/ADCP
   • CD4-help → tumor-specific CD8 expansion
        │
        ▼
ICB response amplification                    ← clinical observable
```

**TLS density** captures the second arrow only (cells aggregating). **TLS maturity** captures arrows 2–4 (the entire functional cascade). This explains why density alone is necessary but not sufficient: an aggregate without GC formation produces no antigen-specific antibody and contributes little to the cycle.

### Why the cross-paper convergence is not coincidence

Same conclusion across very different tumor microenvironments (melanoma = high TMB, hot; sarcoma = low TMB, cold; NSCLC = mixed) means the predictive variable is **upstream of tumor-type biology** — i.e., it is a property of the immune cycle itself, not a tumor-intrinsic factor. This makes mature TLS the right *generic* immune-context biomarker and makes the proposal's reliance on it portable across cancer types.

### Apparent contradictions and how the model resolves them

- **Helmink 2020 baseline P = 0.132 vs on-treatment P < 0.001.** Resolved by the model: at baseline, mature TLS may exist but the GC reaction is not active; ICB releases the brake on T-cell help → GC reaction accelerates → on-treatment density tracks responder status. Density at the right time is informative, density at the wrong time is not.
- **TCGA-KIRC: B-cell signature *not* prognostic (Helmink 2020 Extended Data).** Resolved by the model: ccRCC has tumor-cell-intrinsic immune evasion (HIF/VHL biology) that overrides immune contexture. The model predicts mature-TLS predictive value should hold *only when tumor-intrinsic immune evasion is not dominant* — which is a testable prediction.
- **PDAC TLS-induction (Amisaki 2025) shows benefit.** Consistent with the model: PDAC is normally cold; inducing mature TLS via IL-33/ILC2 supplies the missing GC reaction.

### What the model predicts (testable hypotheses for the manuscript Future Work)

1. **HCC/PDAC/prostate**: a quantified mature-TLS score (CD21⁺ + CD23⁺ + somatic hypermutation evidence in BCR-seq) will outperform PD-L1 or TMB for ICB stratification — *prediction*: AUC for mature-TLS score ≥ 0.75, vs PD-L1 ≈ 0.55 in cold tumors.
2. **TLS-induction therapy** (anti-CD40 agonist + CXCL13 ± IL-21) in TLS-low tumors will convert non-responders to responders at a rate proportional to *de-novo* GC formation (mature TLS gain on biopsy), not to total CD20 density change.
3. **BCR-Ag pairing in mature TLS** will recover **tumor-neoantigen-specific BCRs at higher frequency than self-reactive BCRs**, formalizing the "functional unit" claim. If this fails (most BCRs are self-reactive), the entire model is wrong and TLS maturity is a self-reactive Treg-rich structure — a pivotal alternative hypothesis.
4. **Single-cell mature-TLS deconvolution**: scRNA + scBCR will show that mature-TLS-rich tumors carry a distinct "active GC" B-cell state (high SHM, AID expression, IGHG+) that immature-TLS tumors lack, even at matched CD20 density.

### What this changes in the B-cell neoantigen proposal

- **Inputs to the proposal's scoring framework**: replace "TLS density score" with a three-part functional vector:
  - structural (CD21⁺ + CD23⁺ + MECA79⁺ mIF)
  - transcriptomic (Cabrita 9-gene or Meylan signature)
  - clonal (BCR-seq somatic hypermutation index)
- **Tumor-type prioritization**: predictive value is highest where tumor-intrinsic immune-evasion is moderate (melanoma, sarcoma, NSCLC), lower where it dominates (ccRCC, MSI-CRC). The proposal should rank cancers by predicted *informativeness of TLS score* and prioritize accordingly.
- **Failure mode to design around**: if BCR-Ag pairing study shows mature TLS BCRs are mostly self-reactive, the proposal's premise needs updating — define this as a go/no-go decision in the proposal's milestones.

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
