---
title: Resistance-State Subtyping in Refractory Gastric Cancer
tags:
  - analysis
  - question-chain
  - refractory-gastric-cancer
  - cancer-multiomics
  - phosphoproteomics
  - research-question
themes:
  - wgs
  - phosphoproteomics
  - immune-state
  - treatment-resistance
  - resistance-state-subtype
  - response-prediction
date: 2026-05-25
status: draft
---

# Resistance-State Subtyping in Refractory Gastric Cancer

This page records a dataset-specific LLM-wiki expansion chain: starting from the cancer multiomics literature gap, narrowing through a WGS-phosphoproteome refractory gastric cancer cohort, and ending in a research-article-level question rather than a generic literature summary.

## Key Points

- The distinctive use of LLM-wiki here is not asking "What is the cancer multiomics gap?" in the abstract. The question is constrained by a refractory gastric cancer WGS-proteome/phosphoproteome cohort: neoantigen/immune features, treatment resistance, and planned clinical response.
- Existing wiki pages already cover the general field map and 50-question sprint. This page therefore preserves the **question chain** that converts those compiled facts into a dataset-specific research question.
- The working hypothesis is that phosphoproteomic signaling may be the functional layer between genomic alterations, immune state, and resistance-associated therapeutic vulnerability.
- The current pivot is from conventional **molecular subtype** discovery to **resistance-state subtype** discovery: in a refractory cohort, the key question is not only what intrinsic tumor class a sample belongs to, but what state of therapeutic escape it occupies.
- The current gastric cancer IC1/IC2 result should be framed as a first analyzable version of the larger project, not as the whole project.

## Anchor Question

> Can phosphoproteomic signaling serve as the functional layer that connects genomic alterations, tumor immune state, and treatment resistance in advanced cancer?

Cohort-specific version:

> Can WGS-integrated phosphoproteomic profiling define resistance-state subtypes that are distinct from conventional molecular subtypes in advanced gastric cancer?

Korean working version:

> 진행성 위암 치료 실패 환자군에서 전장유전체-인산화단백체 통합 분석은 기존 molecular subtype과 구별되는 resistance-state subtype을 정의할 수 있는가?

## Use Pattern

The general LLM-wiki workflow is source-bounded compilation:

1. ingest papers,
2. create source pages,
3. connect concepts and topics,
4. synthesize overviews.

The added research-use step here is a **dataset-fit filter**:

1. What has the field already shown?
2. What gap remains?
3. Which gap matches the cohort data layers?
4. Which current result is the first analyzable version?
5. What question can become a research article figure spine?

In short:

> literature map -> gap -> cohort data fit -> current IC1/IC2 interpretation -> research article question

## Question Chain

### Q1. What have cancer proteogenomics studies already solved?

Ask LLM-wiki:

> In cancer proteogenomics and multiomics studies, what have previous studies already shown about linking genomic alterations, proteome/phosphoproteome states, therapeutic vulnerabilities, and tumor immunity?

Wiki-derived answer:

- CPTAC-style studies have already shown that mutation, CNA, RNA, protein, phosphosite, and immune features can refine tumor subtypes and nominate therapeutic vulnerabilities.
- The strongest recurring lesson is that genomic alteration alone is often insufficient: protein abundance, phosphosite activity, kinase inference, or immune-proteomic state can change the interpretation of a driver event.
- Existing local examples include driver-to-phosphosite interpretation in LUAD and HNSCC, phosphoproteome-heavy subtype definition in Korean NSCLC, pan-cancer tumor-immunity proteogenomics, and response-labeled phosphoproteomic resistance cohorts.

Why this matters for this cohort:

- The project should not claim novelty merely from "multiomics." The field already does multiomics subtype discovery.
- The stronger niche is **WGS-integrated phosphoproteomic resistance interpretation**, especially when linked to response or immune state.

### Q2. What gap remains after those studies?

Ask LLM-wiki:

> What research gaps remain in connecting phosphoproteomic signaling states to treatment resistance and tumor immune states?

Wiki-derived answer:

- Many studies are baseline atlases; fewer directly profile primary or acquired resistance.
- Many studies map genomic drivers to expression or protein states; fewer treat phosphoproteomic signaling as the central functional state for response.
- Tumor immunity is often represented by transcriptomic or deconvolution signatures; fewer studies explicitly connect kinase/phosphoproteomic state to immune-evasion programs.
- Neoantigen prediction and immune visibility are often analyzed separately from kinase signaling and treatment-response modeling.
- Clinical translation often stops at subtype or actionability rather than a response-prediction model.

Cohort gap statement:

> The gap is not simply "more omics are needed." The gap is whether phosphoproteomic signaling can functionally connect WGS alterations, immune state, and treatment resistance in patient cohorts.

### Q2b. Is the missing object a new molecular subtype, or a resistance-state subtype?

Ask LLM-wiki:

> Existing cancer multiomics studies often define molecular subtypes. In a refractory or treatment-failed cohort, what would make a subtype a resistance-state subtype rather than another intrinsic molecular subtype?

Working distinction:

| Classification object | Main question | Typical evidence | Limitation for this cohort |
| --- | --- | --- | --- |
| Molecular subtype | What biological class does this tumor belong to? | mutation, CNA, RNA/protein program, lineage, immune or metabolic phenotype | May describe baseline biology without proving relation to treatment failure |
| Therapeutic vulnerability subtype | What target or pathway might be actionable? | drug target abundance, kinase activity, pathway enrichment, drug-matching | May nominate actionability without explaining why current treatment failed |
| Resistance-state subtype | What state of therapeutic escape does this tumor occupy now? | refractory cohort context, signaling state, immune state, genomic constraints, response/survival association | Requires clinical-response linkage and careful distinction from baseline subtype |

Candidate claim:

> In a treatment-failed cohort, IC1/IC2 should not be treated only as a new gastric cancer taxonomy. The stronger question is whether they represent different resistance states: an immune-visible but exhausted state versus a kinase-driven immune-quiet state.

Why this is a better gap:

- Pan-cancer and disease-specific proteogenomic studies already show that multiomics can refine molecular subtype.
- Several studies also connect phosphoproteomics to therapeutic vulnerability.
- What remains less settled is whether multiomics can classify **how refractory tumors are resisting treatment**, especially when immune state and kinase activity diverge.
- This is directly testable because the project is built around refractory/failed treatment context plus WGS, proteome/phosphoproteome, neoantigen/immune features, and clinical response.

### Q2c. Should the cohort model resistance versus non-resistance, or heterogeneity inside resistance?

Ask LLM-wiki:

> In a refractory or treatment-failed cancer cohort, is it more informative to model resistant versus non-resistant tumors, or to decompose the resistant cohort into distinct resistance states? What evidence would support an intra-resistance subtype analysis?

Wiki-derived answer:

- A simple resistant-versus-sensitive contrast is strongest when a cohort has a matched treatment, a fixed endpoint, and comparable sampling time.
- The project cohort is closer to a refractory cohort with mixed prior treatments and multiple possible escape routes. In this setting, the first question may not be "who is resistant?" because most samples already share treatment-failed context.
- The more useful question is whether the refractory population contains separable **resistance states** that differ by immune visibility, effector dysfunction, kinase activity, genome instability, and drug actionability.
- Local response-oriented source pages already suggest this shift: some resistance cohorts have genomic mechanisms for only a subset of patients, while proteome/phosphoproteome features explain additional response or non-response structure.
- Therefore, resistance should be treated as a heterogeneous phenotype rather than a single binary label.

Working analysis frame:

| Binary resistance model | Intra-resistance state model |
| --- | --- |
| Compares resistant vs sensitive/non-resistant tumors | Compares different refractory tumors to each other |
| Best for one treatment class with clear response labels | Better for mixed treatment-failed cohorts |
| Asks whether a feature predicts response | Asks what kind of escape state the tumor occupies |
| Risks collapsing multiple mechanisms into one resistant group | Can separate immune-exhausted, kinase-driven, genome-instability, or stromal/immune-excluded states |

Cohort-specific interpretation:

> The current gastric cancer cohort should first be asked whether IC1/IC2 represent different states **within** treatment failure, before forcing a resistant-versus-non-resistant classifier.

Candidate resistance-state axes:

- immune-visible/exhausted state,
- kinase-driven immune-quiet state,
- genome-instability or CIN-associated state,
- neoantigen-high but presentation-disconnected state,
- stromal/ECM or immune-access-limited state,
- drug-actionable phosphoproteomic state without an obvious genomic driver.

Analysis implication:

- First, define robust intra-refractory states using proteome/phosphoproteome and immune features.
- Second, test whether these states align with treatment class, RECIST, PFS/OS, or WGS features.
- Third, if enough clinical labels exist, compare the state model against a simpler resistant-versus-non-resistant or response/non-response model.

### Q3. Which gap is testable in this project?

Ask LLM-wiki:

> Given a project with WGS, proteome, phosphoproteome, neoantigen prediction, and planned clinical response data, which cancer multiomics research gaps are directly testable?

Cohort-testable layers:

- WGS alteration -> proteome/phosphoproteome functional state
- CIN/WGD/SV/CNA -> kinase or immune phenotype
- phosphosite/kinase activity -> drug actionability
- proteomic immune state -> response or resistance
- HLA/neoantigen features -> immune visibility
- feature blocks -> AI response prediction model

Less directly testable without additional data:

- spatial immune exclusion,
- single-cell-level TME architecture,
- direct TCR recognition of predicted neoantigens,
- causal validation of every candidate kinase or antigen.

### Q4. How does the current gastric cancer analysis fit?

Ask LLM-wiki:

> In the current advanced gastric cancer proteome/phosphoproteome cohort, what is the first analyzable version of the larger WGS-phosphoproteome resistance question?

Current interpretation:

- IC1: antigen-presentation high, HLA class I / MHC-I APP high, dendritic-cell signature high, exhaustion present. This may represent an **immune-visible but exhausted resistance-state candidate**.
- IC2: PI3K/AKT/mTOR/CDK/MAPK signaling high, kinase inhibitor actionability enriched, immune-quiet. This may represent a **kinase-driven immune-quiet resistance-state candidate**.

Caution:

- IC1/IC2 are not yet proven resistance states without RECIST, PFS, OS, treatment class, and WGS integration.
- The current result is best described as **candidate immune-signaling states** that can later be tested against clinical response and WGS-derived genomic features.
- The central analysis should therefore test whether IC1/IC2 explain resistance beyond known gastric cancer subtype labels, tumor purity, treatment class, and broad immune infiltration.

### Q5. What variables translate the review framework into cohort features?

Ask LLM-wiki:

> What measurable features should represent immune visibility, immune access, effector dysfunction, and kinase-driven resistance using WGS, proteome, and phosphoproteome data?

Draft feature map:

| Review concept | Cohort measurable feature candidates |
| --- | --- |
| Immune visibility | HLA-A/B/C, B2M, TAP1/2, antigen-presentation score, HLA type, HLA LOH if available, neoantigen burden |
| Immune access | CAF/stromal protein signatures, ECM remodeling, TGF-beta pathway, angiogenesis/vascular markers; spatial exclusion remains limited |
| Effector dysfunction | exhaustion signatures, PD-1/PD-L1 axis if measurable, Treg/myeloid/TAM markers, hypoxia/lactate/metabolic hostility, TLS-related proteins if available |
| Kinase-driven resistance | phosphosite DE analysis, protein-aware phosphosite correction, inferred kinase activity, PI3K/AKT/mTOR/MAPK/CDK activity, drug-target matching |
| Genome instability | CIN index, WGD, CNA/SV burden, mutational signatures, response-ppQTL candidates |

### Q6. What research article does this become?

Ask LLM-wiki:

> How can the WGS/proteome/phosphoproteome project be structured as a research article rather than a clustering report?

Candidate figure spine:

1. Cohort and data layers: WGS, proteome, phosphoproteome, clinical-response plan.
2. Existing-subtype comparison: show whether IC1/IC2 recapitulate or diverge from known gastric cancer molecular subtype labels.
3. Resistance-state definition: IC1 immune-visible/exhausted vs IC2 kinase-driven/immune-quiet.
4. Functional support: phosphosite/kinase activity, immune visibility, exhaustion, antigen-presentation, and actionability features.
5. Clinical and genomic validation: RECIST/PFS/OS, treatment class, WGS features, CIN/WGD, HLA/neoantigen, ppQTL.

Central hypothesis:

> In advanced gastric cancer refractory to standard treatment, proteome/phosphoproteome-derived IC1/IC2 clusters represent candidate resistance-state subtypes rather than ordinary molecular subtypes.

Testable predictions:

- IC1/IC2 should show coherent immune-signaling differences after controlling for tumor purity and major clinicopathologic factors.
- IC1/IC2 should not be fully explained by existing gastric cancer molecular subtype categories.
- IC1 should carry immune visibility plus exhaustion/suppression features rather than simple immune-hot responsiveness.
- IC2 should carry kinase actionability with reduced immune visibility or immune activation.
- When clinical response data are available, IC1/IC2 should associate with response pattern, PFS/OS, or treatment-class-specific failure.

## Working Chain

The current chain is:

1. **First question**: What has cancer multiomics already explained?
2. **Gap question**: What remains unresolved about phosphoproteomic signaling, resistance, and immune state?
3. **Dataset-fit question**: Which gap can the project cohort actually test?
4. **Endpoint-pivot question**: Should the analysis force resistant versus non-resistant labels, or decompose the refractory cohort into multiple resistance states?
5. **Subtype-pivot question**: Are we finding another molecular subtype, or a resistance-state subtype?
6. **Current-result question**: What does IC1/IC2 represent within that gap?
7. **Research-article question**: Can WGS-integrated phosphoproteomics define resistance-state subtypes in refractory gastric cancer?

The point is that the LLM-wiki answer is not the endpoint. Each answer is used to narrow the next question.

## Evidence-Bounded Question Chain

This chain separates three layers: **established evidence**, **unresolved possibility**, and **next question**.

### Chain 1. From Molecular Subtype to Resistance State

**Q1. Are multiomics subtypes already well established?**

**Answer.** Multiomics subtypes are already well established because pan-cancer and disease-specific proteogenomic studies use genome, RNA, proteome, phosphoproteome, immune, and clinical layers to refine tumor classification ([Chen 2019](../sources/chen-2019-pan-cancer-molecular-subtypes-proteomic-characterization.md); [Zhang 2022](../sources/zhang-2022-proteogenomic-characterization-2002-human-cancers.md); [Song 2024](../sources/song-2024-proteogenomic-analysis-reveals-non-small-cell.md)). In Korean NSCLC, phosphoproteome features contributed 80% of subtype features, showing that phosphorylation can be a primary stratification layer rather than a downstream annotation ([Song 2024](../sources/song-2024-proteogenomic-analysis-reveals-non-small-cell.md); [Cancer Multiomics 50Q Q9](cancer-multiomics-50q-sprint-2026-05.md)). In Taiwanese gastric cancer, proteogenomics defined tumor proteome clusters, immune clusters, anatomy-linked kinase states, carcinogen clusters, microbiome-linked states, and CDK4 actionability hypotheses ([Chang 2026](../sources/chang-2026-integrative-proteogenomics-gastric-cancer-taiwan.md); [Cancer Multiomics 50Q Q5/Q10](cancer-multiomics-50q-sprint-2026-05.md)).

**Unresolved possibility.** These subtype maps do not by themselves prove that a cluster is a **resistance-state subtype**, because many source cohorts are treatment-naive, prognostic, or subtype-discovery cohorts rather than refractory-state cohorts with direct treatment failure labels ([Petralia 2024](../sources/petralia-2024-pan-cancer-proteogenomics-characterization-tumor-immunity.md); [Drug Response POC](drug-response-poc-global-phospho-somatic-snv.md)).

**Next question.** If ordinary molecular subtype discovery is already established, what additional evidence is required to call a subtype a resistance-state subtype ([Drug Response POC](drug-response-poc-global-phospho-somatic-snv.md); [Cancer Resistance Convergence Framework](../syntheses/resistance-convergence-framework.md))?

### Chain 2. From Resistant-vs-Sensitive to Intra-Resistance Heterogeneity

**Q2. Is resistant-versus-sensitive classification the right first model for a refractory cohort?**

**Answer.** Resistant-versus-sensitive classification is strongest when one treatment class, one sampling time, and one response endpoint are clearly defined ([Drug Response POC](drug-response-poc-global-phospho-somatic-snv.md)). Several response-labeled proteogenomic studies use fixed treatment settings such as neoadjuvant chemotherapy in TNBC, cisplatin-based therapy in MIBC, chemoradiation in cervical cancer, sunitinib in ccRCC, or anti-HER2 neoadjuvant therapy in breast cancer ([Lee 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md); [Holt 2025](../sources/holt-2025-proteogenomic-characterization-unveils-biomarkers-associated.md); [Sambath 2026](../sources/sambath-2026-integrated-genomic-proteomic-cervical-cancer-chemoradiation-resistance.md); [Zhang 2023](../sources/zhang-2023-proteogenomics-clear-cell-renal-response-tyrosine-kinase-inhibitor.md); [Jaehnig 2025](../sources/jaehnig-2025-proteogenomic-analysis-calgb-40601-alliance.md)). A mixed refractory gastric cancer cohort differs from those designs because prior treatment histories can contain multiple drug classes and multiple escape routes ([Drug Response POC](drug-response-poc-global-phospho-somatic-snv.md); [Project Context](../_meta/han-mi-am-project-context.md)).

**Unresolved possibility.** In a mixed refractory cohort, the scientifically useful object may be **heterogeneity inside resistance** rather than a binary resistant-versus-non-resistant label, because the resistant group can contain immune-exhausted, kinase-driven, genome-instability, antigen-presentation, and stromal/access-limited states ([Petralia 2024](../sources/petralia-2024-pan-cancer-proteogenomics-characterization-tumor-immunity.md); [Huang 2021](../sources/huang-2021-proteogenomic-insights-biology-treatment-hpv-negative.md); [Cao 2021](../sources/cao-2021-proteogenomic-characterization-pancreatic-ductal-adenocarcinoma.md); [Drug Response POC](drug-response-poc-global-phospho-somatic-snv.md)).

**Next question.** Can proteome/phosphoproteome and immune features decompose refractory gastric cancer into resistance states before clinical response labels are fully modeled ([Song 2024](../sources/song-2024-proteogenomic-analysis-reveals-non-small-cell.md); [Petralia 2024](../sources/petralia-2024-pan-cancer-proteogenomics-characterization-tumor-immunity.md))?

### Chain 3. From Genomic Resistance to Functional Resistance State

**Q3. Are genomic alterations enough to explain therapy resistance?**

**Answer.** Genomic alterations explain only part of resistance because first-line osimertinib acquired-resistance analysis found candidate plasma ctDNA mechanisms in 38/109 patients and no detectable candidate mechanism in 71/109 patients ([Chmielecki 2023](../sources/chmielecki-2023-acquired-resistance-first-line-osimertinib.md); [Drug Response POC](drug-response-poc-global-phospho-somatic-snv.md)). Copy-number and structural layers also matter because cervical chemoradiation resistance involved EGFR amplification, STK11 structural deletion, chromothripsis, DNA repair pathway activation, and phosphorylation changes ([Sambath 2026](../sources/sambath-2026-integrated-genomic-proteomic-cervical-cancer-chemoradiation-resistance.md); [Cancer Multiomics 50Q Q3](cancer-multiomics-50q-sprint-2026-05.md)). Somatic SNV-only analysis can miss CNA/SV-driven or protein-only effects because local response templates repeatedly note that copy-number, structural, protein, and phosphosite layers alter treatment interpretation ([Drug Response POC](drug-response-poc-global-phospho-somatic-snv.md); [Chen 2023](../sources/chen-2023-global-impact-somatic-structural-variation-cancer-proteome.md); [Chen 2026](../sources/chen-2026-global-impact-germline-structural-variation-cancer-proteome.md)).

**Unresolved possibility.** A refractory tumor may lack a clean drug-specific genomic resistance mechanism but still occupy a functional resistance state defined by protein abundance, phosphosite activity, kinase activity, immune state, and pathway rewiring ([Gillette 2020](../sources/gillette-2020-proteogenomic-characterization-reveals-therapeutic-vulnerabilities.md); [Huang 2021](../sources/huang-2021-proteogenomic-insights-biology-treatment-hpv-negative.md); [Drug Response POC](drug-response-poc-global-phospho-somatic-snv.md)).

**Next question.** For samples without an obvious WGS-defined resistance mechanism, can phosphoproteomic signaling identify a resistance state or drug-actionable vulnerability ([Drug Response POC](drug-response-poc-global-phospho-somatic-snv.md); [Kinase Inference Under PTM Correction](../syntheses/kinase-activity-inference-under-ptm-correction.md))?

### Chain 4. From Immune Hot/Cold to Immune-Signaling Resistance States

**Q4. Is a single immune-hot versus immune-cold score enough?**

**Answer.** A single immune score is not enough because Petralia 2024 separates `CD8+/IFNG+`, `CD8-/IFNG+`, and `CD8-/IFNG-` states, including a state with strong IFNG signaling but low CD8/B-cell infiltration ([Petralia 2024](../sources/petralia-2024-pan-cancer-proteogenomics-characterization-tumor-immunity.md)). The `CD8+/IFNG+` state predicted atezolizumab PFS benefit in OAK but not docetaxel benefit, showing that immune subtype can be treatment-class-specific rather than a generic prognosis marker ([Petralia 2024](../sources/petralia-2024-pan-cancer-proteogenomics-characterization-tumor-immunity.md); [Drug Response POC](drug-response-poc-global-phospho-somatic-snv.md)). HNSCC proteogenomics showed immune-cold tumors can reflect antigen-presentation regulator copy-number deletion and APM failure rather than simple antigen-source absence ([Huang 2021](../sources/huang-2021-proteogenomic-insights-biology-treatment-hpv-negative.md); [Drug Response POC](drug-response-poc-global-phospho-somatic-snv.md)).

**Unresolved possibility.** IC1 could represent an immune-visible but exhausted resistance state rather than a simple immune-hot or immune-responsive state, because antigen-presentation-high and exhaustion/suppression-high states can coexist in existing immune proteogenomic frameworks ([Petralia 2024](../sources/petralia-2024-pan-cancer-proteogenomics-characterization-tumor-immunity.md); [Cancer Resistance Convergence Framework](../syntheses/resistance-convergence-framework.md)).

**Next question.** Does IC1 show immune visibility together with effector dysfunction or suppressive features, and does this pattern differ from ordinary immune-hot molecular subtype labels ([Petralia 2024](../sources/petralia-2024-pan-cancer-proteogenomics-characterization-tumor-immunity.md); [Cancer Resistance Convergence Framework](../syntheses/resistance-convergence-framework.md))?

### Chain 5. From Kinase Activity to Immune-Quiet Resistance

**Q5. Can phosphoproteomic kinase activity define a resistance state that genomics alone misses?**

**Answer.** Phosphoproteomic kinase activity can add functional information because Korean NSCLC subtype features were mostly phosphoproteome-derived, and a hypoxic PI3K-Akt/CSNK2A1-GSK3B/SLK-LRRFIP1 subtype had poor-prognosis biology ([Song 2024](../sources/song-2024-proteogenomic-analysis-reveals-non-small-cell.md); [Cancer Multiomics 50Q Q9](cancer-multiomics-50q-sprint-2026-05.md)). Multiple drug-response templates show that protein/phosphosite activity can outperform or refine mutation-only interpretation, including GSK3B-S9 in MIBC, phospho-Rb in HNSCC/LSCC, and mTOR/MAPK/CDK activity in ccRCC sunitinib response ([Holt 2025](../sources/holt-2025-proteogenomic-characterization-unveils-biomarkers-associated.md); [Huang 2021](../sources/huang-2021-proteogenomic-insights-biology-treatment-hpv-negative.md); [Satpathy 2021](../sources/satpathy-2021-proteogenomic-portrait-lung-squamous-cell.md); [Zhang 2023](../sources/zhang-2023-proteogenomics-clear-cell-renal-response-tyrosine-kinase-inhibitor.md); [Drug Response POC](drug-response-poc-global-phospho-somatic-snv.md)). Protein-aware phosphosite correction is necessary because raw phosphosite increases can reflect protein abundance changes, and correction can change kinase calls ([PTM Correction Concept](../concepts/ptm-correction-confounding-foundations.md); [Kinase Inference Under PTM Correction](../syntheses/kinase-activity-inference-under-ptm-correction.md)).

**Unresolved possibility.** IC2 could represent a kinase-driven immune-quiet resistance state if PI3K/AKT/mTOR, MAPK, CDK, or related kinase activities remain after protein correction and are not fully explained by tumor purity, stromal content, or existing molecular subtype ([Song 2024](../sources/song-2024-proteogenomic-analysis-reveals-non-small-cell.md); [Drug Response POC](drug-response-poc-global-phospho-somatic-snv.md); [Kinase Inference Under PTM Correction](../syntheses/kinase-activity-inference-under-ptm-correction.md)).

**Next question.** Does IC2 retain kinase-driven actionability after protein-aware phosphosite correction and adjustment for purity, treatment class, and known gastric cancer molecular subtype labels ([PTM Correction Concept](../concepts/ptm-correction-confounding-foundations.md); [Chang 2026](../sources/chang-2026-integrative-proteogenomics-gastric-cancer-taiwan.md); [Drug Response POC](drug-response-poc-global-phospho-somatic-snv.md))?

### Chain 6. From Plausible State to Testable Article Claim

**Q6. What would make the resistance-state subtype claim defensible?**

**Answer.** A defensible resistance-state subtype claim needs evidence that IC1/IC2 are not fully explained by known molecular subtype labels, tumor purity, broad immune infiltration, treatment class, or batch effects ([Drug Response POC](drug-response-poc-global-phospho-somatic-snv.md); [Song 2024](../sources/song-2024-proteogenomic-analysis-reveals-non-small-cell.md); [Petralia 2024](../sources/petralia-2024-pan-cancer-proteogenomics-characterization-tumor-immunity.md)). A defensible claim also needs a model ladder that compares clinical/technical covariates, WGS features, proteome features, and phosphoproteome/kinase features rather than claiming multiomics value from clustering alone ([Drug Response POC](drug-response-poc-global-phospho-somatic-snv.md)). A defensible claim should mark each conclusion as observational, predictive, or perturbation-supported because many proteogenomic subtype papers generate therapeutic hypotheses without direct prospective response validation ([Drug Response POC](drug-response-poc-global-phospho-somatic-snv.md); [Petralia 2024](../sources/petralia-2024-pan-cancer-proteogenomics-characterization-tumor-immunity.md); [Chang 2026](../sources/chang-2026-integrative-proteogenomics-gastric-cancer-taiwan.md)).

**Unresolved possibility.** The central hypothesis is plausible but not yet proven: refractory gastric cancer may contain immune-visible/exhausted and kinase-driven/immune-quiet resistance-state subtypes that are more informative than a resistant-versus-non-resistant binary model ([Petralia 2024](../sources/petralia-2024-pan-cancer-proteogenomics-characterization-tumor-immunity.md); [Song 2024](../sources/song-2024-proteogenomic-analysis-reveals-non-small-cell.md); [Drug Response POC](drug-response-poc-global-phospho-somatic-snv.md)).

**Next question.** Can IC1/IC2 be validated against RECIST, PFS/OS, treatment class, WGS features, HLA/neoantigen presentation, and protein-corrected kinase activity in a way that distinguishes resistance-state subtype from ordinary molecular subtype ([Drug Response POC](drug-response-poc-global-phospho-somatic-snv.md); [Cancer Multiomics 50Q Q6/Q9](cancer-multiomics-50q-sprint-2026-05.md); [Project Context](../_meta/han-mi-am-project-context.md))?

## Connections

- [Cancer Multiomics Literature Monitor](../topics/cancer-multiomics-literature.md)
- [Cancer Multiomics Literature 50-Question Sprint](cancer-multiomics-50q-sprint-2026-05.md)
- [Drug Response Proof-of-Concept with Global Proteome, Phosphoproteome, and Somatic SNV](drug-response-poc-global-phospho-somatic-snv.md)
- [Cancer Resistance Manuscript Anchor](cancer-resistance-manuscript-anchor.md)
- [Cancer Resistance Convergence Framework](../syntheses/resistance-convergence-framework.md)
- [Project Context](../_meta/han-mi-am-project-context.md)

## Sources

- [Cancer Multiomics Literature Monitor](../topics/cancer-multiomics-literature.md)
- [Cancer Multiomics Literature 50-Question Sprint](cancer-multiomics-50q-sprint-2026-05.md)
- [Drug Response Proof-of-Concept with Global Proteome, Phosphoproteome, and Somatic SNV](drug-response-poc-global-phospho-somatic-snv.md)
- [Cancer Resistance Manuscript Anchor](cancer-resistance-manuscript-anchor.md)
- [Pan-cancer proteogenomics characterization of tumor immunity](../sources/petralia-2024-pan-cancer-proteogenomics-characterization-tumor-immunity.md)
- [Proteogenomic analysis reveals non-small cell lung cancer subtypes predicting chromosome instability, and tumor microenvironment](../sources/song-2024-proteogenomic-analysis-reveals-non-small-cell.md)
- [Proteogenomic Characterization Reveals Subtype-Specific Therapeutic Potential for HER2-Low Breast Cancer](../sources/xu-2026-proteogenomic-characterization-reveals-subtype-specific-therapeutic.md)
- [Integrated genomic and proteomic profiling reveals insights into chemoradiation resistance in cervical cancer](../sources/sambath-2026-integrated-genomic-proteomic-cervical-cancer-chemoradiation-resistance.md)
- [Proteogenomics of clear cell renal cell carcinoma response to tyrosine kinase inhibitor](../sources/zhang-2023-proteogenomics-clear-cell-renal-response-tyrosine-kinase-inhibitor.md)
- [Integrative proteogenomics maps multifactorial aetiology, progression and therapeutic vulnerabilities in gastric cancer](../sources/chang-2026-integrative-proteogenomics-gastric-cancer-taiwan.md)

## Open Questions

- When eCRF arrives, should IC1/IC2 be tested first against RECIST or survival endpoints?
- Should WGS integration prioritize CIN/WGD, actionable CNA/SV, HLA/neoantigen, or ppQTL as the first validation layer?
- Is IC1 better interpreted as immune-responsive potential, exhausted resistance, or simply an antigen-presentation-high baseline phenotype?
- Does IC2's kinase actionability remain after controlling for tumor purity, stromal content, and treatment class?
- Which known gastric cancer molecular subtype labels must IC1/IC2 be compared against before claiming resistance-state subtype status?
- What minimum clinical evidence is required to call a cluster a resistance-state subtype rather than a refractory-cohort-associated molecular subtype?
- Are treatment classes too heterogeneous for a binary resistance model, and if so, which intra-resistance axes should be defined first?
