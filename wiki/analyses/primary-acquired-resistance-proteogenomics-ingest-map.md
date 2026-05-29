---
title: Primary and Acquired Resistance Proteogenomics Ingest Map
tags:
  - analysis
  - ingest-map
  - primary-resistance
  - acquired-resistance
  - proteogenomics
  - phosphoproteomics
  - presentation-prep
themes:
  - treatment-resistance
  - longitudinal-sampling
  - pre-post
  - drug-response
  - resistance-state
status: draft
date: 2026-05-26
---

# Primary and Acquired Resistance Proteogenomics Ingest Map

This page reframes the drug-response/proteogenomics corpus around a presentation-ready LLM-wiki operating rule: preserve question-answer chains as reusable context, then split them into durable wiki nodes by research context rather than by chat turn. The current biological question produced by that rule is: what data are required to distinguish primary resistance, acquired resistance, and static refractory resistance states?

## LLM-Wiki Operating Rule

**Rule:** Do not store a whole chat as one note. Split discussion into context-specific question nodes.

For this project, each durable node should preserve four things:

- the question that triggered the discussion,
- the data condition needed to answer it,
- the local papers or source pages that support or limit the answer,
- the next question created by the gap.

The goal is to make the wiki remember the research process. When a new chat starts, the agent should not need the whole background again; it can reopen the relevant question node and continue from the saved context.

**Applied here:** questions about treatment resistance were split into separate nodes for primary resistance, acquired resistance, static refractory state, and baseline atlas evidence. This made the hidden gap visible: many papers can describe a resistant state, but fewer can prove when the resistance emerged.

## Key Points

- The next ingest work should not simply collect "resistance papers." Each paper should be tagged by what it can prove about timing: primary resistance, acquired resistance, refractory-state heterogeneity, or baseline functional vulnerability.
- Static resistant samples can support a **resistance-state** interpretation, but they cannot by themselves prove **acquired resistance**. Acquired resistance needs paired pre/post or serial treatment-exposure data.
- Primary resistance is best supported by pre-treatment samples with fixed response labels such as pCR/non-pCR, RECIST responder/non-responder, RCB, or early progression.
- Proteogenomics and multiomics matter because WGS/WES often leaves a large unexplained fraction: CNA/SV, protein abundance, phosphoproteome/kinase activity, immune visibility, immune access, and effector dysfunction can carry the functional resistance state.

## Presentation Anchor

Working Korean question:

> 1차내성과 2차내성을 구분하려면 resistant patient sample만으로 충분한가, 아니면 어떤 pre/post multiomics 데이터 구조가 필요한가?

Working English title:

> From Static Resistant Tumors to Longitudinal Resistance States: Data Requirements for Distinguishing Primary and Acquired Cancer Therapy Resistance

## Classification Logic

| Interpretation type | Minimum data structure | What can be interpreted | What cannot be interpreted |
| --- | --- | --- | --- |
| Primary resistance | Pre-treatment sample + response label | Baseline features associated with non-response | Whether the feature was selected by therapy |
| Acquired resistance | Same-patient pre-treatment + progression/post-resistance sample, ideally serial ctDNA/on-treatment | Therapy-associated clonal or state change | Causality without functional validation |
| Static refractory state | Post-treatment or treatment-failed sample only | Resistance-state subtype or current escape state | Whether the state existed before treatment |
| Baseline atlas blueprint | Treatment-naive atlas without direct response endpoint | Feature design for target, pathway, immune, and kinase interpretation | Direct predictive resistance interpretation |

## Question Chain for Ingest

### Q1. What kind of resistance timing does the paper actually observe?

Ask per paper:

- Does it sample before therapy, after therapy, or both?
- Is the response endpoint fixed and comparable across patients?
- Is "resistant" a non-responder label, a progression label, a refractory cohort label, or a model-system phenotype?

Decision:

- Pre-treatment + response label -> primary-resistance evidence.
- Paired pre/post or serial ctDNA/progression -> acquired-resistance evidence.
- Post-treatment only -> refractory-state evidence.
- Treatment-naive atlas -> feature-design evidence.

### Q2. Is the paper proving mechanism, subtype, or data requirement?

Ask per paper:

- Is the strongest interpretation a driver mechanism, a predictive classifier, a patient subtype, or a missing-data lesson?
- Does the paper distinguish genomic alteration from protein/phosphosite functional state?
- Does it show that WGS/WES alone is insufficient?

This prevents overinterpretation. A paper can be excellent for the presentation even if it is not a perfect resistance cohort, as long as it shows why one data layer is necessary.

### Q3. What layer explains the unexplained fraction?

Ask per paper:

- Genomic layer: SNV, CNA, SV, mutational signature, HLA loss, neoantigen change.
- Protein layer: target abundance, pathway abundance, subtype program.
- Phosphoproteome layer: kinase activation, bypass signaling, protein-corrected phosphosite state.
- Immune layer: visibility, access, effector dysfunction.
- Spatial/single-cell layer: exclusion, lineage switch, ecosystem remodeling.

The durable synthesis question is:

> When genomic escape is incomplete or absent, which functional layer makes the resistance state visible?

## Current Local Evidence Buckets

### A. Primary-Resistance / Baseline Non-Response Papers

These are the cleanest papers for "1차내성은 pre-treatment + response label로 묻는다."

| Paper | Local status | Timing / endpoint | Use in presentation |
| --- | --- | --- | --- |
| [Lee 2026 TNBC](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md) | core-ingested | Baseline TNBC multiomics with pCR/non-pCR; paired post-treatment protein subset | Primary non-response model plus limited post-treatment residual-state discussion |
| [Anurag 2022 TNBC](../sources/anurag-2022-proteogenomic-markers-chemotherapy-resistance-response.md) | core-ingested | Pretreatment biopsy with pCR/RCB | Why WES/RNA/proteome/phosphoproteome should be compared block by block |
| [Holt 2025 MIBC](../sources/holt-2025-proteogenomic-characterization-unveils-biomarkers-associated.md) | core-ingested | Cisplatin-based chemotherapy response labels | DDR mutation alone is insufficient; protein DNA-repair/G2M and phosphosite state refine response |
| [Jaehnig 2025 HER2+ Breast](../sources/jaehnig-2025-proteogenomic-analysis-calgb-40601-alliance.md) | core-ingested | Pretreatment anti-HER2 trial biopsies with pCR/non-pCR | Target-status QC ladder: ERBB2 CN/RNA/protein/phospho before calling resistance |
| [Zhang 2023 ccRCC Sunitinib](../analyses/cancer-multiomics-literature/zhang-2023-proteogenomics-clear-cell-renal-response-tyrosine-kinase-inhibitor.md) | core-ingested analysis page | Therapy-specific response cohort | TKI response is better interpreted through pathway/kinase/TME state than target abundance alone |
| [Sambath 2026 Cervical CCRT](../sources/sambath-2026-integrated-genomic-proteomic-cervical-cancer-chemoradiation-resistance.md) | core-ingested | CCRT sensitive/resistant labels | CNA/SV plus protein/phospho convergence around DNA repair and STX3 validation |

### B. Acquired-Resistance / Longitudinal or Post-Progression Papers

These are the key papers for "2차내성은 pre/post 또는 serial data가 필요하다."

| Paper | Local status | Timing / endpoint | Use in presentation |
| --- | --- | --- | --- |
| [Chmielecki 2023 FLAURA osimertinib resistance](../sources/chmielecki-2023-acquired-resistance-first-line-osimertinib.md) | context-ingested | Baseline tissue plus paired plasma ctDNA at acquired resistance | SNV/ctDNA mechanisms explain only a subset; motivates non-genetic proteome/phospho layers |
| [Hsu 2025 osimertinib DTP phosphoproteomics](../sources/hsu-2025-phosphoproteomics-osimertinib-tolerant-persister-cells-reveals.md) | core-ingested | Model-system drug-tolerant persister and recovery time course | Shows why on-treatment/adaptive phosphoproteome can be different from baseline or progression |
| [Memon 2024 acquired PD-(L)1 resistance in NSCLC](../analyses/cancer-multiomics-literature/memon-2024-clinical-molecular-features-acquired-resistance.md) | analysis page | Acquired resistance after checkpoint blockade | Immune-inflamed but dysfunctional resistance-state framing |
| [Yaeger 2023 KRASG12C-EGFR acquired resistance](../sources/yaeger-2023-molecular-characterization-acquired-resistance-krasg12c-egfr.md) | full-text-read; evidence-checked | Patient serial ctDNA acquired resistance after KRASG12C-EGFR therapy | Strong time-axis evidence; motivates broad phosphoproteome/immune readout but does not provide it |
| [Wei 2026 longitudinal melanoma resistant ecosystem](../sources/wei-2026-longitudinal-multi-omic-atlas-reveals-emergence.md) | source page listed | Longitudinal multi-omic resistant melanoma atlas | High-priority deep-dive candidate for spatial/immune acquired resistance |
| [Solanki 2026 KRASG12C acquired resistance](../sources/solanki-2026-ras-gtp-inhibition-overcomes-acquired-resistance.md) | full-text-read; evidence-checked | Preclinical acquired-resistance models after KRASG12C inhibitor pressure | Mechanistic example: WES-positive RAS reactivation, WES-negative RTK/RAS-GTP persistence, and EMT/cell-cycle/DDR switching |

### C. Static Refractory / Resistance-State Papers

These support the careful interpretation: "이런 데이터는 acquired mechanism보다 resistance-state subtype을 말한다."

| Paper / page | Local status | Timing / endpoint | Use in presentation |
| --- | --- | --- | --- |
| [Resistance-State Subtyping in Refractory Gastric Cancer](resistance-state-subtyping-refractory-gastric-cancer.md) | draft analysis | Refractory/treatment-failed framing | Main local question chain: IC1/IC2 as candidate resistance states, not proven acquired mechanisms |
| [Cancer Resistance Convergence Framework](../syntheses/resistance-convergence-framework.md) | synthesis | Cross-therapy resistance framework | Visibility / access / effector dysfunction axes for immune resistance-state annotation |
| [Petralia 2024 Pan-Cancer Tumor Immunity](../sources/petralia-2024-pan-cancer-proteogenomics-characterization-tumor-immunity.md) | context-ingested | Treatment-naive pan-cancer immunity | Immune subtype and kinase hypothesis blueprint, not direct acquired resistance |
| [Song 2024 Korean NSCLC](../sources/song-2024-proteogenomic-analysis-reveals-non-small-cell.md) | core-ingested | Surgical cohort with adjuvant benefit signal | Subtype-treatment interaction rather than direct pre/post resistance mechanism |

### D. Baseline Atlas / Feature-Design Papers

These should be used as design logic, not as direct resistance proof.

| Paper | Local status | Main use |
| --- | --- | --- |
| [Gillette 2020 LUAD](../sources/gillette-2020-proteogenomic-characterization-reveals-therapeutic-vulnerabilities.md) | core-ingested | Driver-to-phosphosite ladder; STK11 immune-cold proteome signal |
| [Huang 2021 HNSCC](../sources/huang-2021-proteogenomic-insights-biology-treatment-hpv-negative.md) | core-ingested | EGFR ligand/activity and immune-hot/cold interpretation |
| [Satpathy 2021 LSCC](../sources/satpathy-2021-proteogenomic-portrait-lung-squamous-cell.md) | core-ingested | Target alteration -> protein -> ligand/bypass -> phospho/kinase QC ladder |
| [Krug 2020 Breast](../sources/krug-2020-proteogenomic-landscape-breast-cancer-tumorigenesis.md) | core-ingested | HER2/Rb/CDK4/6 functional target-status logic |
| [Li 2023 Pan-Cancer Driver-to-Functional-State](../analyses/cancer-multiomics-literature/li-2023-pan-cancer-driver-functional-states.md) | core-briefed | Why genomic drivers must be translated into protein/phosphoprotein states |

## Priority Deep-Dive Queue

The next ingest/deep-dive pass should prioritize papers that fill the acquired-resistance and longitudinal gap, because the current local corpus is already stronger for baseline primary resistance.

| Priority | Basename / page | Why next |
| --- | --- | --- |
| 1 | [wei-2026-longitudinal-multi-omic-atlas-reveals-emergence](../sources/wei-2026-longitudinal-multi-omic-atlas-reveals-emergence.md) | Directly matches longitudinal multi-omic resistant ecosystem framing; likely useful for pre/post + spatial/immune resistance story |
| 2 | [solanki-2026-ras-gtp-inhibition-overcomes-acquired-resistance](../sources/solanki-2026-ras-gtp-inhibition-overcomes-acquired-resistance.md) | Full-text evidence-checked preclinical acquired-resistance model: WES-positive RAS reactivation, WES-negative RTK/RAS-GTP signaling, and EMT/cell-cycle/DDR dependency switching. Useful mechanistic support, not direct patient pre/post proof. |
| 3 | [memon-2024-clinical-molecular-features-acquired-resistance](../analyses/cancer-multiomics-literature/memon-2024-clinical-molecular-features-acquired-resistance.md) | Checkpoint acquired resistance; needed for immune-axis comparison |
| 4 | [yaeger-2023-molecular-characterization-acquired-resistance-krasg12c-egfr](../sources/yaeger-2023-molecular-characterization-acquired-resistance-krasg12c-egfr.md) | Full-text evidence-checked patient serial ctDNA example: acquired alterations are often low-frequency, while KRASG12C amplification tracks progression and drug-pressure fitness. Strong timing evidence; broad phosphoproteomics remains missing. |
| 5 | [jin-2026-deciphering-mediated-phosphorylated-alterations-cancer-related](../sources/jin-2026-deciphering-mediated-phosphorylated-alterations-cancer-related.md) | Gastric cisplatin-resistance phosphoproteome; relevance depends on whether patient/pre-post data exist |
| 6 | [sakai-2026-postn-cafs-chemoradiotherapy-resistance-rectal-cancer](../sources/sakai-2026-postn-cafs-chemoradiotherapy-resistance-rectal-cancer.md) | Spatial/single-cell chemoradiotherapy resistance; useful for immune-access and stromal barrier axis |

## Slide Spine from the Ingest Map

1. Start with the negative control question: "resistant sample 하나로 acquired resistance를 말할 수 있는가?"
2. Define primary resistance, acquired resistance, and refractory resistance state by sampling time.
3. Show the four evidence buckets above as the LLM-wiki graph: primary / acquired / refractory / atlas blueprint.
4. Use primary-resistance papers to show why pre-treatment response labels are powerful.
5. Use acquired-resistance papers to show why same-patient pre/post or serial data are required.
6. Use WGS-only gaps to introduce proteome, phosphoproteome, immune, and spatial layers.
7. End with the review question: "What data architecture turns a resistant tumor from a static label into a mechanistic resistance timeline?"

## Connections

- [Drug Response Proof-of-Concept with Global Proteome, Phosphoproteome, and Somatic SNV](drug-response-poc-global-phospho-somatic-snv.md)
- [Resistance-State Subtyping in Refractory Gastric Cancer](resistance-state-subtyping-refractory-gastric-cancer.md)
- [Drug Response Phospho-Global Proteomics Corpus Queue](drug-response-phospho-global-100-corpus-queue.md)
- [Cancer Multiomics Proteogenomic Atlas](../topics/cancer-multiomics-literature.md)
- [Cancer Resistance Convergence Framework](../syntheses/resistance-convergence-framework.md)

## Sources

- Local source and analysis pages linked in the tables above.
- This page is a planning/synthesis map. Scientific interpretations should be promoted only after the linked local source pages are full-text-read or explicitly marked as source-backed.

## Actual LLM-Wiki Run: From Broad Question to Research Question

This section records the actual use of the wiki as a reasoning device, not a presentation outline.

### Operating Rule Used in This Run

**Rule: evidence boundary before synthesis.**

Before accepting an answer from a paper or a chat discussion, translate the question into the specific interpretation it would allow. Then check whether the local wiki/source evidence has the data structure needed for that interpretation.

For each question, record:

1. the interpretation the question is trying to make,
2. the data structure required to support that interpretation,
3. which local papers satisfy it,
4. which papers are useful but insufficient,
5. the next question created by the insufficiency.

This is different from simple paper summarization. The wiki is used to prevent a broad word like "resistance" from collapsing several different interpretations into one.

### Step 1. Starting Question

> Can proteogenomics or multiomics explain cancer therapy resistance?

Interpretation being attempted:

> Multiomic molecular features can explain why tumors resist therapy.

Wiki check:

- Local response-labeled proteogenomic papers support parts of this interpretation: Lee 2026 TNBC, Anurag 2022 TNBC, Holt 2025 MIBC, Jaehnig 2025 HER2+ breast, Zhang 2023 ccRCC, and Sambath 2026 cervical cancer.
- But the interpretation is too broad because "resistance" is used for baseline non-response, acquired progression, refractory treatment-failed state, and model-system tolerance.

Next question created:

> What kind of resistance is each paper actually able to support?

### Step 2. Resistance Timing Check

> Is the paper about primary resistance, acquired resistance, or a static resistant state?

Interpretation types found in the wiki:

| Interpretation type | Required evidence | Current wiki support |
| --- | --- | --- |
| Primary resistance | Pre-treatment sample + fixed response endpoint | Stronger support: Lee 2026, Anurag 2022, Holt 2025, Jaehnig 2025, Zhang 2023, Sambath 2026 |
| Acquired resistance | Same-patient pre/post or serial progression data | Partial support: Chmielecki 2023, Memon 2024, Yaeger 2023, Hsu 2025 model time course; needs more deep-dive |
| Static refractory state | Treatment-failed sample or refractory cohort | Supported as state description, not timing proof: refractory gastric cancer IC1/IC2 analysis |
| Baseline vulnerability | Treatment-naive atlas with functional omics | Useful for feature design: Gillette 2020, Huang 2021, Satpathy 2021, Krug 2020, Li 2023 |

Conclusion from this check:

> The current local corpus is stronger for primary resistance and functional vulnerability design than for direct acquired-resistance proteogenomics. Therefore, a review question that says it can solve acquired resistance broadly would currently overreach.

Next question created:

> If acquired-resistance evidence is incomplete, what research question is still supported by the current wiki?

### Step 3. Data-Requirement Question as a Filter

> What data are needed to distinguish primary resistance from acquired resistance?

Interpretation being attempted:

> Resistance timing can be inferred from sampling design.

Wiki-derived answer:

- Primary resistance can be studied with pre-treatment molecular data and response labels.
- Acquired resistance requires paired pre/post, progression biopsy, or serial ctDNA/multiomics from the same patient.
- Static refractory data can define resistance states but cannot prove that the state was acquired after treatment.

Important result:

> This data-structure answer is not the final research question. It is a filter that tells which interpretations are supported and which must be softened.

Next question created:

> Once unsupported acquired-resistance interpretations are filtered out, what remains as the strongest cross-paper gap?

### Step 4. Gap Check Across Papers

> What remains unexplained after genomic alteration analysis?

Interpretation being attempted:

> WGS/WES or ctDNA mechanisms do not fully explain therapy resistance; functional omics may reveal the missing state.

Local evidence pattern:

- Chmielecki 2023 motivates the gap: in first-line osimertinib acquired resistance, a large fraction lacks detectable candidate plasma genomic mechanisms.
- Anurag 2022 and Holt 2025 show that mutation status alone can miss response biology, while protein/phosphosite pathways clarify non-response.
- Jaehnig 2025 and Krug 2020 show that clinical target status must be rechecked through CN/RNA/protein/phospho functional target status.
- Zhang 2023 and Sambath 2026 show that CNA/SV plus proteome/phosphoproteome can converge on response or resistance pathways.
- The refractory gastric cancer analysis suggests that proteome/phosphoproteome may separate immune-visible/exhausted and kinase-driven/immune-quiet states, but this should be called candidate resistance-state subtyping until clinical timing/response labels are added.

Gap statement produced by the wiki:

> Many studies can nominate molecular features of non-response or resistant states, but fewer connect same-patient resistance timing with WGS, proteome, phosphoproteome, and immune state. The unresolved space is not simply "more omics"; it is whether functional omics can define the resistance state left unexplained by genomic mechanisms.

Next question created:

> Which functional layers should define this genome-unexplained resistance state?

### Step 5. Functional-Layer Check

> If WGS does not explain resistance, where should the next explanatory layer be sought?

Interpretation being attempted:

> Phosphoproteomic signaling and immune state are plausible functional axes for genome-unexplained resistance.

Wiki support:

- Phosphoproteome/kinase activity appears repeatedly as a response-relevant layer: GRK2/AURKB in Lee 2026, PTM-SEA/KSEA signals in Anurag 2022 and Zhang 2023, GSK3B-S9 in Holt 2025, DNA repair phosphorylation in Sambath 2026, and target/bypass phosphosite logic in Gillette/Huang/Satpathy/Krug.
- Immune state appears as a second recurring axis: immune/IFN response in TNBC, immune-hot/cold NSCLC and LSCC states, pan-cancer tumor-immunity proteogenomics, and the resistance convergence framework's visibility/access/effector dysfunction axes.
- The refractory gastric cancer IC1/IC2 framing provides a candidate local endpoint: immune-visible/exhausted versus kinase-driven/immune-quiet resistance-state candidates.

Conclusion from this check:

> The strongest current research direction is not just to ask whether proteogenomics predicts resistance. It is to ask whether phosphoproteomic signaling and immune-state features define genome-unexplained resistance states, while keeping primary/acquired timing interpretation bounded by sampling design.

## Current Research Question Reached

After applying the evidence-boundary rule to the current wiki, the working research question is:

> Can phosphoproteomic signaling and immune-state profiling define genome-unexplained resistance states in cancer therapy, while distinguishing what can be interpreted for primary resistance, acquired resistance, and static refractory cohorts based on sampling design?

A shorter version for manuscript development:

> Can phosphoproteomic and immune-state features explain therapy-resistant cancer states beyond genomic alterations?

A cohort-facing version for the refractory gastric cancer project:

> In treatment-failed gastric cancer, can WGS-integrated proteome/phosphoproteome profiling separate immune-visible/exhausted and kinase-driven/immune-quiet resistance-state subtypes that are not reducible to conventional molecular subtype labels?

## Hypothesis Produced by This Wiki Run

> Cancer therapy resistance should be treated as a timed and layered state rather than a single label. Genomic alterations explain some resistance mechanisms, but the genome-unexplained fraction may be organized by phosphoproteomic signaling and immune-state axes. In static refractory cohorts this should be framed as resistance-state subtyping; in paired pre/post cohorts it can be tested as acquired-resistance evolution.

## Immediate Next Wiki Actions

- Deep-dive longitudinal/acquired-resistance papers first, because that is the current weakest evidence bucket.
- Promote or correct source pages for Wei 2026 and Memon 2024 next; Solanki 2026 and Yaeger 2023 are now evidence-checked.
- For each new paper, add an evidence-boundary note: primary resistance, acquired resistance, static refractory state, or baseline feature design.
- Update the refractory gastric cancer page only with interpretations that its sampling design can actually support.

## Update After Solanki 2026 Deep-Dive

Solanki 2026 changes the evidence balance in a specific way.

It does **not** fill the patient-paired longitudinal gap, because the resistance evidence is mainly preclinical cell-line/xenograft/PDX rather than same-patient clinical pre/post biopsies. However, it strongly supports the mechanistic part of the emerging hypothesis:

> Acquired resistance can split into WES-positive genomic RAS reactivation, WES-negative RTK/RAS-GTP signaling persistence, and RAS-independent EMT/cell-cycle/DDR dependency switching.

This strengthens the working research question by showing that genome-unexplained resistance is not merely "unknown." It can be decomposed by functional assays and phosphoproteomic/kinase layers.

Revised interpretation:

- The wiki still needs more **patient longitudinal** acquired-resistance papers.
- But the functional-omics hypothesis is stronger: phosphoproteomics can classify resistance states even when WES does not reveal a causal alteration.
- Therefore the review should distinguish two levels of evidence:
  - patient timing evidence: paired pre/post or serial clinical samples;
  - mechanistic functional evidence: model systems with WES/RNA/proteome/phosphoproteome and perturbation validation.

Revised working question:

> Across patient longitudinal studies and mechanistic resistance models, can phosphoproteomic and immune-state features organize genome-unexplained therapy resistance into functional resistance states beyond WGS/WES alterations?

## Update After Yaeger 2023 Deep-Dive

Yaeger 2023 complements Solanki 2026 by filling the opposite side of the evidence structure.

- Yaeger provides **patient time-axis evidence**: serial ctDNA from patients receiving KRASG12C-EGFR combination therapy and progression tissue in a KRASG12C-amplified case.
- It does **not** provide broad proteome/phosphoproteome evidence. Its functional-state observations are based on targeted pathway assays, IHC, western blot, and model systems.
- Therefore it supports the sampling-design part of the argument more strongly than the phosphoproteomics part.

The combined lesson from Yaeger + Solanki is now clearer:

| Evidence need | Stronger current example | What it proves | What remains missing |
| --- | --- | --- | --- |
| Patient timing of acquired resistance | Yaeger 2023 | Serial ctDNA can track emergence and decay of acquired resistance alterations under drug pressure | Broad proteome/phosphoproteome patient readout |
| Functional decomposition of WES-negative resistance | Solanki 2026 | WES-negative acquired-resistance models can be split by RTK/RAS-GTP/phosphoproteomic and EMT/cell-cycle/DDR states | Same-patient clinical pre/post validation |

This refines the review question again:

> The most interesting gap is the missing intersection: patient longitudinal acquired-resistance sampling with broad functional omics, especially phosphoproteomic and immune-state profiling.
