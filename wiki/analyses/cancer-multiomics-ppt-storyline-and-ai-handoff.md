---
title: Cancer Multiomics PPT Storyline and AI Handoff
tags:
  - analysis
  - presentation
  - ai-handoff
  - cancer-multiomics
  - llm-wiki
  - research-question
themes:
  - layer-to-state
  - functional-resistance-state
  - question-centered-wiki
  - advanced-genetics-presentation
date: 2026-05-29
status: ppt-content-ready
---

# Cancer Multiomics PPT Storyline and AI Handoff

이 문서는 Advanced Genetics LLM-Wiki 발표를 만들기 위한 전체 handoff 파일이다. 다른 AI에게 이 파일만 줘도 사용자의 요청사항, 피해야 할 표현, LLM-Wiki 활용 규칙, 질문 확장 과정, 최종 연구질문, 슬라이드 구성을 이해할 수 있도록 정리한다.

## 1. 발표의 핵심 방향

발표의 중심은 다음 문장이 아니다.

> 유전체만으로 부족하니 단백체, 인산화단백체 evidence layer를 더 쌓아서 항암제 내성 marker를 찾자.

이 표현은 피해야 한다. 사용자가 원하는 발표는 “더 많은 데이터 layer를 모았다”가 아니라, LLM-Wiki를 쓰면서 질문의 단위가 바뀌는 과정을 보여주는 것이다.

최종 발표 흐름은 다음이다.

> Cancer multiomics 문헌을 위키로 확장하면서, 질문이 “어떤 omics layer가 내성 marker를 잘 찾는가?”에서 “각 omics layer는 어떤 functional resistance state를 읽고 있는가?”로 이동했다.

즉, 결론은 단순 marker 발굴이 아니라 functional resistance-state 가설 도출이다.

## 2. 반드시 반영할 사용자 요청사항

- “유전체만으로 부족하다”처럼 유전체를 디스하는 framing을 쓰지 않는다.
- “evidence layer를 쌓자”만으로 끝내지 않는다.
- “claim을 audit했다” 같은 표현을 쓰지 않는다. `claim`, `audit`이라는 단어는 발표용 문장에 넣지 않는 것이 좋다.
- 교수님 공지에 맞게 질문별 노드 캡처가 들어가야 한다.
- 발표자는 LLM-Wiki를 실제로 어떻게 사용했는지 보여줘야 한다.
- 단순 논문 요약이 아니라, 질문을 던지고 위키 노드를 확장하고, 그 결과 다음 질문이 생기는 흐름을 보여줘야 한다.
- 기존 cancer resistance review는 메인 주제가 아니라 cancer multiomics 연구질문을 도출하는 sub thought-chain으로 연결한다.
- 사용자가 원래 갖고 있던 생각을 “위키로 새로 발견한 척”하면 안 된다.
- 데이터 구조 질문은 중요하지만 최종 연구질문 자체가 되면 안 된다.
- 내성 정의, 데이터 시간축, 약물 맥락, molecular readout, 검증 강도는 biological sub-question으로 쓰되, “나만의 LLM 활용 규칙”으로 포장하지 않는다.
- LLM 활용 규칙은 다른 사람들도 참고할 수 있을 만큼 일반적이어야 한다.

## 3. 최종 LLM-Wiki 활용 규칙

발표용 규칙은 단순히 “질문 노드를 만든다”가 아니다. 그것은 위키의 기본 운영 방식에 가깝다. 이 발표에서 보여줄 사용자의 규칙은 같은 문헌 묶음을 고정해 놓고, 질문이 바뀔 때마다 분류축을 바꿔 다시 읽는 것이다.

> **같은 논문, 다른 좌표계**

말로 풀면 다음과 같다.

> 저는 LLM-Wiki를 논문을 계속 추가하는 도구가 아니라, 같은 논문 세트를 질문이 바뀔 때마다 다른 좌표계로 다시 배치해 보는 도구로 사용했습니다.

이 규칙은 biology-specific rule이 아니다. 다른 주제에도 적용 가능한 LLM-Wiki 활용 방식이다.

운영 방식:

1. 먼저 작은 문헌 묶음을 고정한다.
2. 바로 더 많은 논문을 추가하지 않는다.
3. LLM에게 같은 문헌을 다른 기준으로 다시 배열하게 한다.
4. 어떤 기준에서 문헌들이 가장 의미 있게 갈라지는지 본다.
5. 그 분류축이 다음 연구질문의 후보가 된다.

이 규칙을 cancer multiomics에 적용한 버전은 다음이다.

> **Layer로 모은 문헌을 State 좌표계로 다시 배치하기.**

말로 풀면:

> 처음에는 WGS, proteome, phosphoproteome처럼 layer 기준으로 문헌을 모았지만, 이후 같은 문헌을 내성 정의, 데이터 시간축, molecular readout, functional state 기준으로 다시 배열했습니다.

## 4. 이전 발표자와의 차이

첨부 PDF와 이전 발표자 사례는 “느낌”만 참고한다. 그대로 따라하면 안 된다.

이전 발표자들의 규칙은 대략 다음 결이었다.

| 발표자 | 규칙의 결 |
| --- | --- |
| 염경호 | source restriction, hallucination 방지, multi-collection 활용 |
| 여진 | 질문 / 키워드 / 가설 노드를 나누어 관리 |
| 현진 | 루틴 기반으로 논문 페이지와 개념 페이지를 함께 갱신하고, 강한 축과 불안정한 축을 구분 |

이번 발표는 이들과 똑같이 “완성/불완성 가설”이나 “질문/키워드/가설 노드”를 반복하지 않는다.

차별점은 다음이다.

> 나는 문헌을 계속 추가하기보다, 같은 문헌 묶음을 여러 좌표계로 다시 배치해 보았다. 그 과정에서 어떤 분류축이 실제 연구질문을 만들 수 있는지 확인했다.

## 5. 질문 도출의 전체 흐름

### Q0. 처음 질문

처음 질문은 넓었다.

> Cancer multiomics로 항암제 내성 marker를 더 잘 찾을 수 있을까?

이 질문의 문제:

- 너무 layer 중심이다.
- marker가 primary resistance인지, acquired resistance인지, refractory state인지 섞인다.
- protein abundance와 phosphosite/kinase activity가 같은 의미처럼 다뤄질 수 있다.
- “multiomics integration을 어떻게 할 것인가”라는 방법 질문으로 흐르기 쉽다.

다음 질문:

> 각 omics layer는 내성의 어떤 측면을 읽는가?

관련 노드:

- [Cancer Multiomics Proteogenomic Atlas](../topics/cancer-multiomics-literature.md)
- [Cancer Multiomics Resistance Biomarker Question Chain](./cancer-multiomics-resistance-biomarker-question-chain.md)

### Q1. 각 layer는 무엇을 읽는가?

질문:

> WGS, proteome, phosphoproteome은 같은 evidence layer인가, 아니면 서로 다른 state readout인가?

정리:

| Layer | 읽을 수 있는 것 |
| --- | --- |
| WGS | mutation, CNA, SV, genomic potential, antigenicity 가능성 |
| Proteome | 실제 protein abundance, pathway abundance, target abundance, immune/stromal context |
| Phosphoproteome | kinase activity, pathway rewiring, adaptive signaling |

생긴 변화:

> “어떤 layer가 더 좋은가?”가 아니라 “어떤 layer가 어떤 state를 읽는가?”로 질문이 바뀐다.

관련 노드:

- [PTM Correction and Kinase Signaling in Cancer Proteomics](../topics/ptm-correction-and-kinase-signaling-in-cancer-proteomics.md)
- [Drug Response Proof-of-Concept with Global Proteome, Phosphoproteome, and Somatic SNV](./drug-response-poc-global-phospho-somatic-snv.md)

### Q2. Cancer resistance review는 어떻게 연결되는가?

사용자는 이미 cancer resistance review에서 내성이 immune evasion으로 수렴한다는 생각을 정리한 적이 있다. 단, 이것은 위키가 새로 도출한 메인 결과처럼 말하면 안 된다.

발표에서의 역할:

> 기존 resistance thought-chain은 cancer multiomics에서 볼 수 있는 functional state 후보 중 하나를 제공했다.

즉, immune-evasion state는 최종 state map의 한 축이다.

관련 노드:

- [Cancer-Resistance Convergence Framework](../syntheses/resistance-convergence-framework.md)
- [Immunotherapy Resistance and Immune Evasion](../topics/immunotherapy-resistance-and-immune-evasion.md)

### Q3. Phosphoproteome / PTM anchor는 어떻게 연결되는가?

질문:

> Phosphoproteome은 단순히 marker 하나를 더 찾는 layer인가, 아니면 adaptive signaling state를 읽는 readout인가?

정리:

- Protein abundance는 “무엇이 많이 존재하는가”를 읽는다.
- Phosphosite와 kinase activity는 “그 pathway가 실제로 켜져 있는가”를 읽는다.
- 따라서 phosphoproteome은 adaptive tolerance, kinase rewiring, bypass signaling 같은 state를 해석하는 데 중요하다.

발표 메시지:

> PTM/kinase 쪽 위키 확장은 phosphoproteome을 단순 layer가 아니라 functional signaling-state readout으로 보게 만들었다.

관련 노드:

- [PTM Correction and Kinase Signaling in Cancer Proteomics](../topics/ptm-correction-and-kinase-signaling-in-cancer-proteomics.md)

### Q4. 내성 정의를 왜 먼저 나누는가?

질문:

> 논문들이 말하는 “resistance”는 같은 뜻인가?

정리:

| 내성 정의 | 의미 | 필요한 데이터 | 해석 가능한 것 |
| --- | --- | --- | --- |
| Primary resistance / baseline non-response | 치료 전부터 반응하지 않을 가능성이 높은 상태 | pre-treatment sample + response endpoint | baseline predictor, primary non-response state |
| Acquired resistance | 처음에는 반응했지만 치료 후 resistance/progression이 생긴 상태 | same-patient pre/post, progression biopsy, serial data | treatment-associated state transition |
| Adaptive tolerance | 치료 압력 아래 early/reversible하게 생기는 drug-tolerant state | on-treatment or model-system time course | early kinase rewiring, adaptive signaling |
| Refractory state | 이미 치료 실패 후 관찰되는 현재 상태 | refractory-only or treatment-failed cohort | resistant-state heterogeneity |
| Response-associated marker | 반응/비반응과 통계적으로 연결된 feature | response-labeled cohort | candidate marker, 추가 검증 필요 |

발표 문장:

> 내성 정의를 먼저 나눈 이유는 이 분류 자체가 결론이라서가 아니라, 같은 protein/phosphosite signal이라도 primary marker, acquired state, adaptive tolerance, refractory state 중 무엇을 말하는지 달라지기 때문입니다.

관련 노드:

- [Primary and Acquired Resistance Proteogenomics Ingest Map](./primary-acquired-resistance-proteogenomics-ingest-map.md)
- [Cancer Multiomics Resistance Biomarker Evidence Boundary Map](./cancer-multiomics-resistance-biomarker-evidence-boundary-map.md)

### Q5. 데이터 구조는 왜 보는가?

질문:

> pre/post 데이터가 있느냐, snapshot 데이터만 있느냐에 따라 어떤 분석이 가능한가?

중요한 점:

데이터 부족 자체를 메인 gap으로 말하면 안 된다. 사용자가 풀 수 없는 문제처럼 들릴 수 있다. 데이터 구조는 “어떤 state 해석이 가능한가”를 판단하기 위한 sub-question이다.

정리:

| 데이터 구조 | 가능한 해석 |
| --- | --- |
| Pre-treatment + response label | baseline primary resistance 또는 response-associated marker |
| Same-patient pre/post | treatment-associated state transition, acquired resistance |
| On-treatment time-course | adaptive tolerance, early signaling rewiring |
| Refractory-only cohort | 현재 refractory state의 heterogeneity |
| Resistant vs non-resistant snapshot | association은 가능하지만 timing 해석은 제한적 |

발표 메시지:

> 데이터 구조를 본 이유는 “데이터가 부족하다”가 아니라, 같은 marker라도 어떤 내성 상태로 해석할 수 있는지가 데이터 시간축에 따라 달라지기 때문입니다.

관련 노드:

- [Cancer Multiomics Resistance Gap Decision Matrix](./cancer-multiomics-resistance-gap-decision-matrix.md)

### Q6. 최종 연구질문

최종 연구질문:

> **Cancer multiomics readout을 이용해 유전체 변이만으로 설명되지 않는 항암제 내성을 functional resistance state로 재분류할 수 있는가?**

더 구체적인 버전:

> **Proteome/phosphoproteome readout은 항암제 내성 종양을 immune-evasion state, kinase/adaptive-signaling state, DNA-repair/stress state, stromal/access-limited state 같은 functional resistance states로 구분할 수 있는가?**

최종 가설:

> **항암제 내성은 단일 resistance marker가 아니라, cancer multiomics readout으로 구분되는 여러 functional resistance states의 조합으로 설명될 수 있다.**

운영 가능한 가설:

> Proteome은 pathway abundance, immune/stromal context, target abundance를 읽고, phosphoproteome은 kinase activity와 adaptive signaling을 읽는다. 따라서 WGS만으로 설명되지 않는 내성 종양을 proteome/phosphoproteome readout으로 functional state별로 재분류할 수 있다.

주의:

- 사용자의 데이터에는 RNA-seq이 없다고 가정한다.
- 따라서 `WGS/RNA`라고 쓰지 말고 `WGS, proteome, phosphoproteome` 중심으로 쓴다.

## 6. Functional Resistance-State Map

최종 발표에서 보여줄 state 후보는 다음과 같다.

| Functional state | Main readout | 왜 중요한가 |
| --- | --- | --- |
| Immune-evasion state | HLA/B2M/antigen presentation proteins, IFN/JAK-STAT proteins or phosphosites, immune context | 기존 cancer resistance review와 연결되는 state |
| Kinase/adaptive-signaling state | phosphosite modules, kinase activity, RTK/MAPK/PI3K/mTOR/CDK activity | phosphoproteome이 필요한 이유 |
| DNA-repair/stress-response state | DDR proteins/phosphosites, replication stress, DNA damage response | chemo/CCRT resistance와 연결 가능 |
| Stromal/access-limited state | ECM/CAF/TGF-beta/angiogenesis proteins, spatial exclusion if available | bulk proteomics에서 tumor-intrinsic/TME signal이 섞이는 문제 |
| Refractory mixed state | treatment-failed cohort clusters | acquired mechanism이 아니라 현재 resistant-state heterogeneity로 해석 |

## 7. PoC 데이터와 분석 설계

이 내용은 발표 끝부분에서 “이 질문을 실제로 풀려면 무엇을 해볼 수 있나?”로 짧게 넣는다. 메인 발표를 덮으면 안 된다.

### 필요한 데이터

- WGS 또는 WES: SNV/indel, CNA, SV, TMB, HLA/neoantigen 관련 feature 가능하면 포함
- Global proteome: protein abundance, pathway/module score, target abundance, immune/stromal proteins
- Phosphoproteome: phosphosite abundance, protein-corrected phosphosite signal, kinase/pathway activity inference
- Clinical label: response/non-response, refractory status, progression, treatment line
- 있으면 좋은 데이터: same-patient pre/post, on-treatment, progression sample

### 해볼 수 있는 분석

| Available data | Analysis | What it tests |
| --- | --- | --- |
| WGS + proteome | genomic alteration과 protein abundance concordance | genomic event가 protein-level functional state로 이어지는가 |
| Proteome + phosphoproteome | total protein abundance와 phosphosite/kinase activity 비교 | signaling activity가 abundance와 독립적인가 |
| WGS + phosphoproteome | genomic alteration과 kinase activity 비교 | genome-unexplained kinase/adaptive state가 있는가 |
| WGS + proteome immune features | predicted antigenicity와 antigen-presentation protein state 비교 | genomic visibility와 실제 presentation machinery가 맞는가 |
| Response label + proteome/phosphoproteome | non-response/refractory sample의 state enrichment | 어떤 functional state가 내성과 연결되는가 |
| Pre/post or serial sample | state transition analysis | 치료 압력 아래 어떤 state가 생기거나 사라지는가 |

핵심 PoC 질문:

> RNA-seq이 없어도 WGS, proteome, phosphoproteome만으로 genomic alteration, protein abundance, phosphosite/kinase activity가 서로 맞는지 어긋나는지를 보고 genome-unexplained resistance state를 찾을 수 있는가?

## 8. PPT 구성안

### Slide 1. Title

제목:

> **Cancer Multiomics LLM-Wiki: Layer에서 State로 이동한 질문**

핵심 메시지:

> 발표의 결론은 “더 많은 omics layer”가 아니라, “각 layer가 어떤 내성 상태를 읽는가”라는 질문으로 이동한 것이다.

시각화:

- 왼쪽: Cancer multiomics / resistance / PTM 세 개 노드
- 오른쪽: final question 한 문장

발표 멘트:

> 처음에는 cancer multiomics로 항암제 내성 marker를 더 잘 찾을 수 있을지 궁금했습니다. 그런데 위키를 확장하면서 marker를 찾기 전에, 그 marker가 어떤 내성 상태를 읽는지를 먼저 물어야 한다는 쪽으로 질문이 바뀌었습니다.

### Slide 2. Why LLM-Wiki

제목:

> **논문 요약보다 질문 변화가 중요했다**

핵심 메시지:

> 논문을 많이 모아도 연구질문이 생기지는 않았다. LLM-Wiki는 논문을 질문별로 다시 묶는 데 도움이 됐다.

시각화:

- “Paper list”에서 “Question-centered nodes”로 이동하는 그림
- 캡처: [Cancer Multiomics Proteogenomic Atlas](../topics/cancer-multiomics-literature.md)

발표 멘트:

> 제가 위키를 쓴 이유는 논문 요약을 저장하기 위해서라기보다, 같은 논문들을 다른 질문으로 다시 묶어 보기 위해서였습니다.

### Slide 3. My LLM-Wiki Rule

제목:

> **나의 규칙: 질문별로 다시 묶고, 다음 질문을 남긴다**

핵심 메시지:

> 답을 바로 결론으로 쓰지 않고, 답이 나온 지점에서 다음 질문을 위키 노드로 남겼다.

슬라이드 문구:

> 저는 LLM-Wiki를 논문 요약 저장소가 아니라, 같은 말로 묶여 있던 논문들을 질문별로 다시 나눠 보고, 답이 나온 자리에서 다음 질문을 남기는 도구로 사용했습니다.

시각화:

`Question -> Wiki node expansion -> What changed? -> Next question`

캡처:

- [Cancer Multiomics Presentation Capture Board](./cancer-multiomics-presentation-capture-board.md)

### Slide 4. Starting Question

제목:

> **처음 질문: multiomics로 내성 marker를 찾을 수 있을까?**

핵심 메시지:

> 이 질문은 출발점으로는 좋지만, 발표의 최종 질문으로는 너무 넓었다.

시각화:

- 가운데 큰 질문
- 주변에 문제점 4개:
  - resistance definition mixed
  - pre/post vs snapshot mixed
  - protein abundance vs kinase activity mixed
  - method question으로 흐름

캡처:

- [Cancer Multiomics Resistance Biomarker Question Chain](./cancer-multiomics-resistance-biomarker-question-chain.md)

### Slide 5. Reframing

제목:

> **Layer를 모으는 질문에서 State를 묻는 질문으로**

핵심 메시지:

> WGS, proteome, phosphoproteome은 같은 종류의 evidence layer가 아니라 서로 다른 state readout이다.

시각화:

| WGS | Proteome | Phosphoproteome |
| --- | --- | --- |
| alteration / genomic potential | abundance / pathway / context | kinase activity / adaptive signaling |

발표 멘트:

> 그래서 “세 layer를 어떻게 통합할까?”는 방법 질문이고, 그 전에 “각 layer가 어떤 내성 상태를 읽는가?”를 물어야 한다고 정리했습니다.

### Slide 6. Sub Thought-Chain 1: Immune-Evasion State

제목:

> **기존 cancer resistance 생각은 하나의 state 후보가 되었다**

핵심 메시지:

> 기존 review에서 정리한 immune-evasion 축은 최종 결론이 아니라, functional resistance-state map의 한 축으로 들어간다.

시각화:

`Visibility -> Access -> Effector dysfunction -> Immune-evasion state`

캡처:

- [Cancer-Resistance Convergence Framework](../syntheses/resistance-convergence-framework.md)

발표 멘트:

> 이 부분은 위키를 쓰면서 처음 만든 가설처럼 말하지 않습니다. 이전에 제가 갖고 있던 resistance 생각을 cancer multiomics 질문 안에서 하나의 state 후보로 재배치한 것입니다.

### Slide 7. Sub Thought-Chain 2: Kinase / Adaptive State

제목:

> **Phosphoproteome은 adaptive signaling state를 읽는다**

핵심 메시지:

> phosphoproteome은 marker를 하나 더 찾는 layer가 아니라, kinase rewiring과 adaptive tolerance를 읽는 기능적 readout이다.

시각화:

`Drug pressure -> kinase rewiring -> phosphosite modules -> adaptive-signaling state`

캡처:

- [PTM Correction and Kinase Signaling in Cancer Proteomics](../topics/ptm-correction-and-kinase-signaling-in-cancer-proteomics.md)

### Slide 8. Resistance Definition

제목:

> **같은 resistance marker라도 말하는 상태가 다르다**

핵심 메시지:

> primary, acquired, adaptive tolerance, refractory state를 구분해야 protein/phosphosite signal의 의미가 정해진다.

시각화:

- 내성 정의 표
- 색으로 primary/acquired/adaptive/refractory 구분

캡처:

- [Primary and Acquired Resistance Proteogenomics Ingest Map](./primary-acquired-resistance-proteogenomics-ingest-map.md)

### Slide 9. Data Structure As Analysis Design

제목:

> **데이터 구조는 결론이 아니라 해석 가능 범위를 정한다**

핵심 메시지:

> pre/post, time-course, snapshot 여부는 데이터 부족 이야기가 아니라 state 해석 범위를 정하는 기준이다.

시각화:

| Data structure | Can say | Cannot overstate |
| --- | --- | --- |
| baseline + response | primary non-response association | acquired mechanism |
| same-patient pre/post | state transition | population-only subtype |
| time-course | adaptive tolerance | durable clinical resistance |
| refractory snapshot | current resistant state | when it emerged |

캡처:

- [Cancer Multiomics Resistance Gap Decision Matrix](./cancer-multiomics-resistance-gap-decision-matrix.md)

### Slide 10. Functional State Map

제목:

> **위키 확장 결과: functional resistance-state 후보**

핵심 메시지:

> 위키 확장을 통해 내성 marker 후보를 state 후보로 다시 묶을 수 있었다.

시각화:

- 5개 state map:
  - immune-evasion
  - kinase/adaptive-signaling
  - DNA-repair/stress-response
  - stromal/access-limited
  - refractory mixed

발표 멘트:

> 이 지점이 발표의 핵심 결과입니다. 단순히 “어떤 marker가 있나”가 아니라, 내성 종양을 어떤 functional state로 다시 볼 수 있는지가 질문이 되었습니다.

### Slide 11. Final Research Question

제목:

> **최종 연구질문**

슬라이드 중앙 문장:

> Cancer multiomics readout을 이용해 유전체 변이만으로 설명되지 않는 항암제 내성을 functional resistance state로 재분류할 수 있는가?

아래 hypothesis:

> 항암제 내성은 단일 resistance marker가 아니라, WGS/proteome/phosphoproteome readout으로 구분되는 여러 functional resistance states의 조합으로 설명될 수 있다.

### Slide 12. PoC / Next Step

제목:

> **다음 단계: WGS–Proteome–Phosphoproteome으로 확인할 것**

핵심 메시지:

> RNA-seq이 없어도 WGS, proteome, phosphoproteome의 일치/불일치를 통해 genome-unexplained resistance state를 탐색할 수 있다.

시각화:

`WGS alteration -> protein abundance -> phosphosite/kinase activity -> functional state`

옆에 PoC 질문:

> 어떤 내성 샘플은 mutation으로 설명되지 않지만, protein abundance나 kinase activity 수준에서 특정 state로 묶이는가?

## 9. 교수님 공지 반영: 캡처 구성

발표에는 질문별로 HTML 또는 Obsidian 노드를 캡처해서 넣는다. 한 장에 거대한 전체 graph를 넣지 않는다.

실제 캡처 지시서는 별도 페이지로 고정했다.

- [Cancer Multiomics Question Node Capture Pack](./cancer-multiomics-question-node-capture-pack.md)

캡처 단위:

> 질문 하나 -> 중심 노드 하나 -> 같이 열린 노드 2-3개 -> 다음 질문 하나

추천 캡처 순서:

| Slide | Capture target | 보여줄 이유 |
| --- | --- | --- |
| 2 | [Cancer Multiomics Proteogenomic Atlas](../topics/cancer-multiomics-literature.md) | 처음 topic hub |
| 3 | [Cancer Multiomics Presentation Capture Board](./cancer-multiomics-presentation-capture-board.md) | 질문별 캡처 설계 |
| 4 | [Cancer Multiomics Resistance Biomarker Question Chain](./cancer-multiomics-resistance-biomarker-question-chain.md) | 첫 질문이 어떻게 쪼개졌는지 |
| 6 | [Cancer-Resistance Convergence Framework](../syntheses/resistance-convergence-framework.md) | 기존 review를 sub thought-chain으로 연결 |
| 7 | [PTM Correction and Kinase Signaling in Cancer Proteomics](../topics/ptm-correction-and-kinase-signaling-in-cancer-proteomics.md) | phosphoproteome/kinase state |
| 8 | [Primary and Acquired Resistance Proteogenomics Ingest Map](./primary-acquired-resistance-proteogenomics-ingest-map.md) | 내성 정의와 데이터 시간축 |
| 9 | [Cancer Multiomics Resistance Gap Decision Matrix](./cancer-multiomics-resistance-gap-decision-matrix.md) | 데이터 구조별 분석 가능 범위 |
| 11 | [Cancer Multiomics Final Presentation Brief](./cancer-multiomics-final-presentation-brief.md) | 최종 연구질문 |

## 10. 발표에서 피해야 할 표현

쓰지 말 것:

- “유전체만으로 부족해서”
- “evidence layer를 쌓아서 타겟 발굴”
- “claim을 audit했다”
- “데이터가 부족한 것이 main gap이다”
- “LLM이 최종 결론을 내려줬다”
- “기존 cancer resistance review를 위키로 도출했다”
- “multiomics integration이 최종 연구질문이다”

대신 쓸 표현:

- “질문의 단위가 layer에서 state로 이동했다”
- “같은 resistance marker라도 어떤 내성 상태를 읽는지 다르다”
- “데이터 구조는 state 해석 가능 범위를 정한다”
- “기존 resistance 생각은 final state map의 한 축으로 재배치했다”
- “답이 아니라 다음 질문을 위키 노드로 남겼다”

## 11. 한 장 요약

발표 전체를 한 문장으로 줄이면:

> 저는 LLM-Wiki를 이용해 cancer multiomics 문헌을 단순히 layer별로 모으는 대신, 각 layer가 어떤 항암제 내성 상태를 읽는지 질문별로 다시 묶었고, 그 과정에서 내성을 단일 marker가 아니라 WGS/proteome/phosphoproteome readout으로 구분되는 functional resistance states의 조합으로 보는 연구질문을 도출했습니다.

최종 결론:

> **Layer-centered biomarker discovery에서 state-centered resistance interpretation으로 이동했다.**

## Connections

- [Cancer Multiomics Final Presentation Brief](./cancer-multiomics-final-presentation-brief.md)
- [Cancer Multiomics Presentation Capture Board](./cancer-multiomics-presentation-capture-board.md)
- [Cancer Multiomics Resistance Biomarker Question Chain](./cancer-multiomics-resistance-biomarker-question-chain.md)
- [Cancer Multiomics Resistance Biomarker Evidence Boundary Map](./cancer-multiomics-resistance-biomarker-evidence-boundary-map.md)
- [Cancer Multiomics Resistance Gap Decision Matrix](./cancer-multiomics-resistance-gap-decision-matrix.md)
- [Primary and Acquired Resistance Proteogenomics Ingest Map](./primary-acquired-resistance-proteogenomics-ingest-map.md)
- [PTM Correction and Kinase Signaling in Cancer Proteomics](../topics/ptm-correction-and-kinase-signaling-in-cancer-proteomics.md)
- [Cancer-Resistance Convergence Framework](../syntheses/resistance-convergence-framework.md)

## Sources

- Local wiki pages linked above.
- User-provided class context and constraints from the Advanced Genetics LLM-Wiki presentation discussion.
