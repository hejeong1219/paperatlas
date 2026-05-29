---
title: Cancer Multiomics Final Presentation Brief
tags:
  - analysis
  - presentation
  - cancer-multiomics
  - llm-wiki
  - research-question
themes:
  - layer-to-state
  - functional-resistance-state
  - proteogenomics
  - phosphoproteomics
date: 2026-05-28
status: presentation-ready
---

# Cancer Multiomics Final Presentation Brief

This is the presentation-ready version of the Cancer Multiomics LLM-Wiki storyline. It fixes the final research-question chain, slide logic, and capture targets.

## Final Direction

The presentation should not center on "more multiomics evidence layers" or "data are insufficient." The main thought movement is:

> **Layer 중심 질문에서 state 중심 질문으로 이동했다.**

Starting question:

> Cancer multiomics로 항암제 내성 marker를 더 잘 찾을 수 있을까?

Problem found through the wiki:

> Omics layer가 많아져도, 그 marker가 어떤 tumor/resistance state를 읽고 있는지 모르면 연구질문이 선명해지지 않는다.

Final research question:

> **Cancer multiomics readout을 이용해 유전체 변이만으로 설명되지 않는 항암제 내성을 functional resistance state로 재분류할 수 있는가?**

More specific version:

> **Proteome/phosphoproteome readout은 항암제 내성 종양을 immune-evasion state, kinase/adaptive-signaling state, DNA-repair/stress state, stromal/access-limited state 같은 functional resistance states로 구분할 수 있는가?**

## Hypothesis

Presentation hypothesis:

> **항암제 내성은 단일 resistance marker가 아니라, cancer multiomics readout으로 구분되는 여러 functional resistance states의 조합으로 설명될 수 있다.**

Operational hypothesis:

> Proteome은 pathway abundance, immune/stromal context, target abundance를 읽고, phosphoproteome은 kinase activity와 adaptive signaling을 읽는다. 따라서 WGS/RNA만으로 설명되지 않는 내성 종양을 proteome/phosphoproteome readout으로 functional state별로 재분류할 수 있다.

## My LLM-Wiki Rule

Use a simple rule name on the slide:

> **Layer를 모으지 말고, State를 물어보기**

Rule explanation:

1. 논문이 어떤 omics layer를 썼는지 먼저 모은다.
2. 그 다음 "이 layer는 어떤 tumor state를 읽는가?"로 질문을 바꾼다.
3. 같은 resistance marker라도 layer, timing, readout, validation에 따라 다른 state로 분류한다.
4. 답이 아니라 다음 질문을 위키 노드로 남긴다.

One-sentence presentation version:

> 저는 LLM-Wiki를 논문 요약 도구가 아니라, 여러 omics layer를 모은 뒤 그 layer들이 실제로 어떤 내성 상태를 읽고 있는지 묻는 도구로 사용했습니다.

## Question-Derivation Chain

| Step | Question asked | Wiki nodes expanded | What changed | Next question |
| --- | --- | --- | --- | --- |
| Q0 | Cancer multiomics로 항암제 내성 marker를 찾을 수 있을까? | [Cancer Multiomics Proteogenomic Atlas](../topics/cancer-multiomics-literature.md), corpus queues | Layer가 많다는 것만으로는 연구질문이 되지 않았다 | 각 layer는 무엇을 읽고 있나? |
| Q1 | 각 omics layer는 내성의 어떤 측면을 읽는가? | [PTM Correction and Kinase Signaling](../topics/ptm-correction-and-kinase-signaling-in-cancer-proteomics.md), [Drug Response POC](./drug-response-poc-global-phospho-somatic-snv.md) | WGS, proteome, phosphoproteome이 서로 다른 readout임을 분리했다 | layer보다 state가 중요한가? |
| Q2 | 항암제 내성을 functional state로 볼 수 있을까? | [Cancer-Resistance Convergence Framework](../syntheses/resistance-convergence-framework.md), immune-evasion topic | 기존 resistance thought-chain이 immune-evasion state 후보를 제공했다 | immune-evasion 말고 다른 state도 있나? |
| Q3 | Proteome/phosphoproteome은 어떤 state를 읽는가? | PTM/kinase topic, drug-response papers | Proteome은 abundance/context, phosphoproteome은 kinase/adaptive signaling을 읽는다는 축이 생겼다 | 내성 state 후보를 어떻게 나눌까? |
| Q4 | Resistance marker는 언제 생긴 state를 반영하나? | [Primary and Acquired Resistance Proteogenomics Ingest Map](./primary-acquired-resistance-proteogenomics-ingest-map.md), [Evidence Boundary Map](./cancer-multiomics-resistance-biomarker-evidence-boundary-map.md) | baseline, adaptive, acquired, refractory 해석이 달라짐을 알았다 | 어떤 데이터 구조에서 어떤 분석이 가능한가? |
| Q5 | 어떤 데이터가 있으면 어떤 state 분석이 가능한가? | [Gap Decision Matrix](./cancer-multiomics-resistance-gap-decision-matrix.md) | 데이터 부족이 결론이 아니라, state 해석을 위한 analysis-design 질문이 되었다 | 최종 가설을 어떻게 말할까? |
| Q6 | 최종 질문은 무엇인가? | this brief | "marker 발굴"에서 "functional resistance-state 재분류"로 이동했다 | PPT 구성으로 전환 |

## Functional State Map

| Functional state candidate | Main readout | Related wiki basis | Why it matters |
| --- | --- | --- | --- |
| Immune-evasion state | HLA/B2M/antigen presentation, immune proteins, IFN axis, T cell/TME features | Cancer resistance convergence framework; immunotherapy resistance topic | 기존 resistance review의 thought-chain을 cancer multiomics 질문으로 연결한다 |
| Kinase/adaptive-signaling state | phosphosite, kinase activity, pathway rewiring | PTM/kinase topic; Hsu 2025; response phosphoproteomics papers | phosphoproteome이 단순 layer가 아니라 functional signaling state를 읽는 이유 |
| DNA-repair/stress-response state | DDR protein/phosphosite, damage response, chromothripsis/CNA context | Holt 2025, Sambath 2026, TNBC response papers | chemotherapy/CCRT resistance에서 반복되는 functional axis |
| Stromal/access-limited state | CAF/ECM/TGF-beta/vascular or spatial-exclusion features | resistance convergence framework; spatial/immune multiomics pages | bulk proteomics에서 tumor-intrinsic vs TME signal이 섞이는 문제와 연결 |
| Refractory mixed state | resistant-only or treatment-failed cohort features | refractory gastric state page; ingest map | acquired mechanism이 아니라 current resistant-state heterogeneity로 해석해야 함 |

## Resistance Definitions To Use

This should appear early in the talk as the reason why the initial "resistance marker" question was too broad.

| Resistance definition | What it means | Minimum useful data | What analysis it allows |
| --- | --- | --- | --- |
| Primary resistance / baseline non-response | 치료 전부터 반응하지 않을 가능성이 높은 상태 | Pre-treatment sample + response endpoint | baseline predictor, primary non-response state, pre-existing functional context |
| Acquired resistance | 처음에는 반응했지만 치료 후 progression/resistance가 생긴 상태 | Same-patient pre/post, progression biopsy, or serial data | treatment-associated change, gained/lost state, resistant trajectory |
| Adaptive tolerance | 치료 압력 아래 early/reversible하게 생기는 drug-tolerant state | On-treatment or model-system time course | early kinase rewiring, adaptive signaling, reversible tolerance program |
| Refractory state | 이미 여러 치료 후 실패한 현재 상태 | Refractory-only or treatment-failed cohort | resistant-state heterogeneity, functional subtype discovery |
| Response-associated marker | 반응/비반응과 통계적으로 연결된 feature | Response-labeled cohort | candidate marker; requires additional evidence before mechanism wording |

Presentation sentence:

> 내성 정의를 먼저 나눈 이유는 이 분류 자체가 결론이라서가 아니라, 같은 protein/phosphosite signal이라도 primary marker, acquired state, adaptive tolerance, refractory state 중 무엇을 말하는지 달라지기 때문이다.

## PoC Design: What Data To Collect And What To Try

This can be used for the final "next step" slide. It does not need to dominate the talk, but it makes the research question actionable.

### Minimal PoC Dataset

Minimum local/user data needed:

- WGS or WES: SNV/indel, CNA, SV if available, TMB/neoantigen/HLA-related features if available.
- Global proteome: protein abundance, pathway/module scores, target abundance, immune/stromal proteins.
- Phosphoproteome: phosphosite abundance, protein-corrected phosphosite signal if matched protein exists, kinase/pathway activity inference.
- Clinical label: response/non-response, refractory status, progression, or treatment line.
- Optional but valuable: paired pre/post, on-treatment, or progression samples.

### PoC Analyses By Data Type

| Available data | Analysis to try | What it can test |
| --- | --- | --- |
| WGS + proteome | Genomic alteration to protein abundance concordance | Does a genomic event translate into protein-level functional state? |
| Proteome + phosphoproteome | Protein abundance vs phosphosite / kinase activity comparison | Is signaling activity independent of total protein abundance? |
| WGS + phosphoproteome | Genomic alteration vs kinase activity discordance | Are there genome-unexplained kinase/adaptive states? |
| WGS + proteome immune features | Predicted immune visibility vs antigen-presentation protein state | Does genomic antigenicity match actual presentation machinery? |
| Response label + proteome/phosphoproteome | Resistant-state feature comparison | Which functional states are enriched in non-response or refractory samples? |
| Pre/post or serial samples if available | State transition analysis | Which functional states emerge, disappear, or persist under treatment pressure? |

### Candidate State Features

| State | Candidate feature set |
| --- | --- |
| Immune-evasion state | HLA-A/B/C, B2M, TAP1/2, antigen processing/presentation proteins, IFN/JAK-STAT proteins or phosphosites, immune checkpoint proteins if measured |
| Kinase/adaptive-signaling state | kinase substrate enrichment, phosphosite modules, RTK/MAPK/PI3K/mTOR/CDK activity features |
| DNA-repair/stress state | ATM/ATR/BRCA/RAD/CHK/WEE1-related protein and phosphosite features, replication stress markers |
| Stromal/access-limited state | ECM/CAF/TGF-beta/angiogenesis proteins, spatial markers if available |
| Refractory mixed state | unsupervised proteome/phosphoproteome clusters in treatment-failed samples, then annotate by the feature sets above |

### Practical PoC Question

> WGS, proteome, and phosphoproteome are available but RNA-seq is not. Can we still identify genome-unexplained resistance states by checking whether genomic alteration, protein abundance, and kinase/phosphosite activity agree or disagree?

This keeps the PoC aligned with the user's actual data constraints.

## Slide Plan

### Slide 1. Title

Message:

> Cancer Multiomics LLM-Wiki를 통해 질문이 "어떤 layer가 marker를 잘 찾는가?"에서 "각 layer는 어떤 내성 상태를 읽는가?"로 이동했다.

Visual:

- title + small local graph or topic hub screenshot.

### Slide 2. Why Wiki

Message:

> 논문을 많이 모으는 것만으로는 연구질문이 생기지 않았다. Layer를 모으면 WGS/RNA/proteome/phosphoproteome이 쌓이지만, 그 layer가 읽는 state가 무엇인지가 남았다.

Capture:

- [Cancer Multiomics Proteogenomic Atlas](../topics/cancer-multiomics-literature.md)

### Slide 3. My LLM-Wiki Rule

Message:

> 나의 규칙: **Layer를 모으지 말고, State를 물어보기.**

Capture:

- [My LLM-Wiki Use Rules](./my-llm-wiki-use-rules.md)

### Slide 4. First Question: Marker?

Message:

> 처음 질문은 "multiomics로 내성 marker를 찾을 수 있을까?"였지만, 이 질문은 너무 넓었다.

Capture:

- [Cancer Multiomics Resistance Biomarker Question Chain](./cancer-multiomics-resistance-biomarker-question-chain.md)

### Slide 5. Reframing: Layer -> State

Message:

> WGS, proteome, phosphoproteome은 같은 종류의 evidence layer가 아니라 서로 다른 tumor state readout이다.

Visual:

- simple three-column diagram:
  - WGS: alteration / visibility
  - Proteome: abundance / pathway / immune context
  - Phosphoproteome: kinase / adaptive signaling

### Slide 6. Sub-Thought Chain: Immune-Evasion State

Message:

> 기존 cancer resistance thought-chain은 내성 state 후보 중 하나를 제공했다: immune visibility, access, effector dysfunction.

Capture:

- [Cancer-Resistance Convergence Framework](../syntheses/resistance-convergence-framework.md)

### Slide 7. Sub-Thought Chain: Kinase / Adaptive State

Message:

> PTM/kinase wiki를 열면서 phosphoproteome은 단순 marker가 아니라 adaptive signaling state를 읽는 readout이라는 질문으로 이동했다.

Capture:

- [PTM Correction and Kinase Signaling in Cancer Proteomics](../topics/ptm-correction-and-kinase-signaling-in-cancer-proteomics.md)

### Slide 8. Data Structure As Analysis Design

Message:

> 데이터 구조를 본 이유는 "데이터가 부족하다"가 아니라, 어떤 데이터에서 어떤 state 분석이 가능한지 구분하기 위해서였다.

Capture:

- [Cancer Multiomics Resistance Gap Decision Matrix](./cancer-multiomics-resistance-gap-decision-matrix.md)

### Slide 9. Resistance Definitions

Message:

> 내성을 primary, acquired, adaptive tolerance, refractory state로 나누면 같은 marker라도 어떤 state를 말하는지 달라진다.

Visual:

- resistance definitions table from this page.

### Slide 10. Functional State Map

Message:

> 위키 확장을 통해 immune-evasion, kinase/adaptive-signaling, DNA-repair/stress, stromal/access-limited, refractory mixed state라는 후보 state map이 생겼다.

Visual:

- table from this page or simple state map.

### Slide 11. Final Research Question

Message:

> 최종 질문: Cancer multiomics readout을 이용해 유전체 변이만으로 설명되지 않는 항암제 내성을 functional resistance state로 재분류할 수 있는가?

Visual:

- final question + arrows from layer to state.

### Slide 12. PoC / Next Step

Message:

> 다음 단계는 WGS-proteome-phosphoproteome 데이터에서 genomic alteration, protein abundance, phosphosite/kinase activity가 일치하거나 어긋나는 패턴을 보고 functional resistance state 후보를 정의하는 것이다.

Subquestions:

- 어떤 데이터 구조에서 baseline/acquired/refractory state를 구분할 수 있는가?
- protein abundance와 phosphosite/kinase activity는 어떤 state에서 더 informative한가?
- immune-evasion state와 kinase/adaptive-signaling state는 서로 배타적인가, 조합되는가?
- RNA-seq이 없어도 WGS-proteome-phosphoproteome concordance/discordance로 어떤 PoC를 할 수 있는가?

## What To Avoid

- Do not say the main gap is "data are insufficient."
- Do not say the goal is simply "integrating many omics layers."
- Do not present the cancer resistance review as if LLM-Wiki newly created it.
- Do not present `pre/post data` as the final question. It is a data-design sub-question.
- Do not use "claim audit" language.

## PPT-Ready Conclusion

> 처음에는 cancer multiomics를 통해 항암제 내성 marker를 더 잘 찾을 수 있을지 물었다. 하지만 LLM-Wiki로 논문과 개념 노드를 확장하면서, 중요한 것은 layer의 개수가 아니라 각 layer가 읽는 tumor state라는 점이 보였다. 그래서 최종적으로 저는 항암제 내성을 단일 marker가 아니라, proteome/phosphoproteome readout으로 구분되는 functional resistance states의 조합으로 볼 수 있는가라는 연구질문에 도달했다.

## Connections

- [Cancer Multiomics Presentation Storyline](./cancer-multiomics-presentation-storyline.md)
- [Cancer Multiomics Presentation Capture Board](./cancer-multiomics-presentation-capture-board.md)
- [Cancer Multiomics Resistance Biomarker Question Chain](./cancer-multiomics-resistance-biomarker-question-chain.md)
- [Cancer Multiomics Resistance Gap Decision Matrix](./cancer-multiomics-resistance-gap-decision-matrix.md)
- [My LLM-Wiki Use Rules](./my-llm-wiki-use-rules.md)
