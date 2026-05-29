---
title: Cancer Multiomics Resistance Gap Decision Matrix
tags:
  - analysis
  - gap-decision
  - cancer-multiomics
  - treatment-resistance
  - presentation
themes:
  - research-question-development
  - acquired-resistance
  - proteomics
  - phosphoproteomics
  - validation
date: 2026-05-28
---

# Cancer Multiomics Resistance Gap Decision Matrix

This page decides which research gap should become the center of the presentation and which data limitations should remain supporting context.

## Key Points

- The strongest current research gap is the **functional identity gap of resistance-associated protein/phosphosite programs**: the field has not clearly resolved which protein, phosphosite, kinase, or immune-state programs represent true resistance biology, which are baseline subtype/context markers, and which are merely refractory-state features.
- The other gaps are real, but they are better used as supporting questions rather than separate final research questions.
- The longitudinal data issue should be presented only as one methodological reason this biological question remains hard, not as the research gap itself.
- The presentation should not say "let's integrate many evidence layers to find biomarkers." It should say: **the field has not yet clarified whether resistance-associated protein/phosphosite signals reflect shared functional resistance states, drug-specific escape programs, baseline non-response biology, or post-treatment refractory states.**

## Gap Status

| Gap candidate | Did the wiki find an answer? | Current answer | Role in presentation |
| --- | --- | --- | --- |
| Functional identity gap | Yes, strongest | It remains unclear which resistance-associated protein/phosphosite programs are true functional resistance states versus baseline subtype, drug-context, immune/stromal, or refractory-state signals. | Main research gap |
| Timing ambiguity | Yes | Baseline, adaptive, acquired, and refractory settings can produce different marker meanings, but the field often discusses them under the broad label of resistance biomarkers. | Supporting reason the functional identity gap persists |
| Longitudinal data limitation | Yes | Baseline response-labeled proteogenomics is available for primary resistance; serial acquired-resistance evidence often exists in genomic/ctDNA studies or model systems; same-patient patient-level longitudinal proteome/phosphoproteome evidence remains sparse. | Methodological limitation, not the main research gap |
| Readout gap | Partly | Protein abundance and phosphosite/kinase activity can represent different biology, but many papers still require careful separation of raw phosphosite, protein-corrected phosphosite, and inferred kinase activity. | Supporting gap that helps define the classification criteria |
| Drug-context gap | Not fully answered yet | The corpus contains chemotherapy, TKI, HER2/ADC, immunotherapy, chemoradiation, and model-system examples, but the current wiki has not yet completed a full drug-class comparison of shared versus drug-specific protein/phosphosite resistance axes. | Future expansion or backup slide |
| Compartment gap | Partly | Bulk proteomics can mix tumor-intrinsic, immune, and stromal signals. The prior resistance review's visibility/access/effector dysfunction frame helps interpret this, but the current corpus is not yet fully separated by tumor versus microenvironment evidence. | Bridge to user's previous cancer resistance review |
| Validation gap | Partly | Many papers support same-cohort association or baseline response markers; fewer provide independent validation, perturbation, organoid/PDX, PRM/IHC, or patient longitudinal recurrence/progression validation for the same marker. | Supporting gap and next table to build |

## Main Research Gap Chosen

Presentation-ready research gap:

> 항암제 내성 proteogenomics 문헌에서는 다양한 protein/phosphosite marker가 보고되지만, 이 신호들이 실제 내성의 기능적 상태를 정의하는지, baseline subtype/context를 반영하는지, 약물별 escape program인지, 또는 refractory tumor의 단면인지는 아직 명확히 정리되지 않았다.

Supporting data limitation:

> 특히 therapy-emergent acquired resistance의 기능적 상태를 밝히려면 시간축 있는 functional-omics evidence가 도움이 되지만, 이것은 research gap 자체가 아니라 그 질문을 어렵게 만드는 방법론적 조건이다.

Why this is the best main gap:

1. It asks what the field has not biologically resolved, not merely what data are missing.
2. It directly follows from the user's first concern: before discovering resistance biomarkers, define what kind of resistance biology is being measured.
3. It avoids the generic "multiomics evidence layer" story.
4. It makes protein/phosphosite data meaningful because they are treated as functional-state readouts, not just additional omics layers.
5. It can be approached through a review-style classification framework and later tested in user-owned or public cohorts.

## Supporting Gaps

## Data Structure as a Sub-Question

Data structure is not the research gap. It is a sub-question used to decide which analysis can answer which part of the research gap.

Main research gap:

> Protein/phosphosite programs are reported in cancer therapy resistance, but it remains unclear what functional resistance state they represent.

Data sub-question:

> Given a dataset's sampling design, what kind of resistance-state analysis is actually possible?

| Data structure | Analysis possible | Research question it can answer | What it cannot answer alone |
| --- | --- | --- | --- |
| Pre-treatment sample + response label | Baseline association, predictor discovery, primary non-response marker analysis | Which baseline protein/phosphosite states are associated with poor response? | Whether the state emerged after treatment |
| Same-patient pre/post or progression sample | Treatment-associated change, gained/lost protein/phosphosite state, acquired-resistance trajectory | Which functional states appear, disappear, or are selected under therapy? | Causality without functional validation |
| Serial time-course model | Adaptive tolerance dynamics, kinase rewiring, reversibility analysis | Which signaling states appear early under drug pressure? | Patient generality without clinical validation |
| Resistant vs non-resistant snapshot | Resistant-state subtype comparison | What molecular states distinguish current resistant tumors? | Timing of emergence |
| Refractory-only cohort | Resistance-state heterogeneity, subtype discovery | Are there distinct refractory functional states? | Whether the state is primary, acquired, or therapy-selected |
| Multi-omics with immune/spatial layer | Tumor-intrinsic vs immune/stromal decomposition | Is the resistance state driven by tumor signaling, immune access, or effector dysfunction? | Temporal origin unless longitudinally sampled |

How to say this in the presentation:

> 데이터 구조를 본 이유는 "데이터가 부족하다"고 말하려는 것이 아니라, 어떤 데이터가 있을 때 어떤 분석과 어떤 내성 해석이 가능한지 구분하기 위해서였다.

### 1. Readout Gap

Question:

> If a resistance-associated signal is found, is it a protein abundance marker, a phosphosite marker, or a kinase-activity state?

Use:

> This supports the main gap because longitudinal data must track not only whether a marker exists, but what molecular unit is changing under treatment pressure.

### 2. Drug-Context Gap

Question:

> Are protein/phosphosite resistance axes shared across drug classes, or drug-class specific?

Use:

> This is important but too large for the main presentation. It can be presented as a next expansion after timing and readout are clarified.

### 3. Compartment Gap

Question:

> Is the resistance-associated proteomic signal tumor-intrinsic, immune/stromal, or mixed?

Use:

> This connects to the user's previous resistance review: resistance can converge through visibility, access, and effector dysfunction, but bulk proteomics may not separate those compartments cleanly.

### 4. Validation Gap

Question:

> What evidence is needed to move from a response-associated feature to a robust resistance biomarker?

Use:

> This becomes the next table: same cohort, independent cohort, perturbation, organoid/PDX, IHC/PRM, or patient longitudinal validation.

## Research Question Chosen

Main research question:

> 항암제 내성에서 보고되는 protein/phosphosite 신호들은 어떤 기능적 resistance state를 반영하며, 이 신호들이 baseline subtype, therapy-emergent escape, adaptive tolerance, refractory state 중 무엇에 해당하는지 어떻게 구분할 수 있는가?

Shorter presentation version:

> 항암제 내성 protein/phosphosite marker는 실제 내성 상태를 보여주는가, 아니면 baseline subtype이나 refractory state를 반영하는가?

More review-like English version:

> What functional resistance states are captured by protein and phosphosite programs in cancer therapy resistance, and how can these be distinguished from baseline subtype and refractory-state signals?

## How the Other Gaps Fit Under the Main Question

| Sub-question | How it supports the main question |
| --- | --- |
| Pre/post or snapshot? | Determines whether timing of resistance can be inferred |
| Protein or phosphosite? | Determines whether the marker reflects abundance, signaling, or kinase state |
| Drug-specific or shared? | Determines whether the marker can generalize across treatment classes |
| Tumor-intrinsic or immune/stromal? | Determines what biological compartment the marker represents |
| Association or validation? | Determines whether the marker remains a candidate or becomes stronger evidence |

## Slide Use

This page can become one decision slide after the question-chain slides.

Slide message:

> 발표의 중심은 "데이터가 부족하다"가 아니라, protein/phosphosite marker가 실제 어떤 기능적 내성 상태를 반영하는지 아직 명확하지 않다는 연구 gap이다. 데이터 구조는 이 질문을 풀기 위한 방법 조건으로만 배치한다.

## Connections

- [Cancer Multiomics Resistance Biomarker Evidence Boundary Map](./cancer-multiomics-resistance-biomarker-evidence-boundary-map.md)
- [Cancer Multiomics Resistance Biomarker Question Chain](./cancer-multiomics-resistance-biomarker-question-chain.md)
- [Primary and Acquired Resistance Proteogenomics Ingest Map](./primary-acquired-resistance-proteogenomics-ingest-map.md)
- [Cancer Multiomics Presentation Storyline](./cancer-multiomics-presentation-storyline.md)
- [My LLM-Wiki Use Rules](./my-llm-wiki-use-rules.md)
