---
title: Cancer Multiomics Presentation Storyline
tags:
  - analysis
  - presentation
  - cancer-multiomics
  - llm-wiki
themes:
  - knowledge-chain
  - research-question-development
  - proteogenomics
  - therapy-response
---

# Cancer Multiomics Presentation Storyline

고급유전학 후반기 발표를 위해, Cancer Multiomics LLM-Wiki가 어떻게 항암제 내성 바이오마커 발굴의 연구 gap을 찾고, 질문-위키확장을 반복하면서 더 구체적인 연구질문으로 수렴했는지 설명하는 15분 발표 설계안.

## Key Points

- 발표의 핵심은 "많이 읽었다"가 아니라, **어떤 규칙으로 위키를 운영했고 그 규칙이 어떤 질문을 낳았는가**이다.
- Cancer Multiomics 위키의 중심은 하나의 질문이 아니라, **항암제 내성 바이오마커 발굴이라는 큰 문제를 여러 개의 작은 질문으로 쪼개며 연구 gap을 좁혀간 과정**이다.
- `pre/post 단백체·인산화단백체 데이터 구조가 필요한가?`는 최종 질문이 아니라, 메인 연구질문으로 가기 위한 중간 방법론 질문이다.
- 질문 체인의 첫 단계는 "단백체가 유용한가?"가 아니라 **내성을 어떻게 정의할 것인가**이다. 그 다음에 pre/post 데이터인지, resistant vs non-resistant 스냅샷인지, 어떤 omics와 분석 방법이 필요한지로 내려간다.
- multiomics 데이터를 어떻게 통합했는지는 메인 질문이 아니라, 내 연구 질문을 구체화하기 위해 거쳐야 하는 **방법적 sub-question**이다.
- 스토리의 결론 연구질문은 아직 단일 문장으로 고정하지 않고, `내성의 timing`, `내성 state의 기능적 readout`, `바이오마커로 어디까지 말할 수 있는지`, `검증 가능한 후보 축`을 거쳐 점진적으로 좁힌다.
- 발표에서는 Obsidian graph를 "전체 위키 자랑"이 아니라 질문별 subgraph로 보여주는 것이 좋다.

## 발표 제목 후보

**질문이 질문을 낳는 방식: Cancer Multiomics 위키로 항암제 내성 바이오마커 gap을 좁혀간 과정**

대안:

- **Resistant sample 하나로 충분한가: pre/post 단백체·인산화단백체 데이터가 필요한 이유**
- **논문 요약을 넘어 근거 범위 정리로: 항암제 내성 연구 gap을 찾는 LLM-Wiki 활용기**
- **항암제 내성 바이오마커는 타이밍의 문제다: primary vs acquired resistance 질문 체인**

## 참고 발표에서 얻은 형식적 힌트

이전 발표 자료와 2026-05-19 수업 요약은 내용이 아니라 발표 형식의 참고로만 사용한다. 따라 할 점은 특정 주제나 슬라이드 문구가 아니라, **LLM-Wiki 활용 과정을 하나의 사고 흐름으로 보여주는 방식**이다.

참고할 수 있는 형식:

- 먼저 왜 위키가 필요했는지 말한다: 논문 요약 저장소가 아니라 작업 기억의 외재화.
- 다음으로 본인만의 운영 규칙을 제시한다: 자유도 제한, raw PDF boundary, 질문별 노드화.
- 그 다음 주제별 질문을 보여준다: 질문 하나마다 관련 노드/그래프 캡처를 붙인다.
- 마지막에 결과물을 말한다: 단순 정리가 아니라 가설 또는 연구질문이 어떻게 자랐는지.

사용자님 발표에 맞게 바꾸는 점:

- `autism landscape`나 `idiosyncrasy framework` 같은 전 발표자의 프레임은 쓰지 않는다.
- 내 프레임은 **항암제 내성 바이오마커를 말하기 전에 내성을 어떻게 정의하고, 어떤 데이터 구조가 그 정의를 뒷받침하는지 확인하는 것**이다.
- LLM-Wiki의 역할은 답을 주는 것이 아니라, 내가 던진 질문을 `정의 질문`, `데이터 질문`, `측정 질문`, `방법 질문`으로 쪼개고 다음 질문을 남기는 것이다.

## 1문장 Thesis

Cancer Multiomics LLM-Wiki를 운영하면서 처음에는 항암제 반응/내성 proteogenomics 논문을 모았지만, 위키로 질문을 반복해보니 "내성 바이오마커"라는 말 안에 여러 문제가 섞여 있었다. 어떤 신호는 치료 전부터 존재하는 primary resistance marker일 수 있고, 어떤 신호는 치료 후 새로 생기는 acquired resistance marker일 수 있으며, 어떤 신호는 단지 refractory tumor의 현재 상태일 수 있다. 그래서 발표의 핵심은 하나의 완성된 답이 아니라, **질문-위키확장을 반복하면서 내성 바이오마커 연구에서 어떤 gap들이 차례로 드러났고, 그 gap들이 어떻게 더 날카로운 연구질문 후보로 이어졌는가**를 보여주는 것이다.

## 기존 Cancer Resistance 리뷰와의 연결

기존에 작성한 cancer resistance review는 이번 발표에서 별개의 리뷰 논문 자랑이 아니라, **LLM-Wiki가 이미 한 번 연구질문을 고도화한 사례**로 연결할 수 있다.

이전 생각 체인:

> 여러 항암제 내성 문헌을 읽다 보니, 내성은 약제별로 따로 설명되는 것 같지만 많은 경우 `visibility`, `access`, `effector dysfunction`이라는 면역회피 축으로 수렴한다.

위키에서 만들어진 노드:

- [Cancer Resistance Manuscript Anchor](./cancer-resistance-manuscript-anchor.md)
- [Cancer-Resistance Convergence Framework](../syntheses/resistance-convergence-framework.md)
- [Immunotherapy Resistance and Immune Evasion](../topics/immunotherapy-resistance-and-immune-evasion.md)

이전 체인이 이번 질문으로 이어지는 방식:

1. 먼저 cancer resistance review에서는 **내성 상태를 면역회피의 큰 축으로 정리**했다.
2. 그런데 그 과정에서 "내성"이라는 단어가 primary, adaptive, acquired, refractory를 섞는다는 문제가 보였다.
3. 그래서 이번 Cancer Multiomics 질문은 더 구체적으로 내려간다: **단백체/인산화단백체 biomarker가 어떤 내성 상태를 반영하는지 구분할 수 있는가?**
4. 즉 이전 리뷰가 "내성은 어떤 방향으로 수렴하는가"를 물었다면, 이번 발표의 질문은 "그 내성 상태를 어떤 데이터 구조와 functional readout으로 구분할 수 있는가"를 묻는다.

발표에서의 위치:

- 슬라이드 초반에 1장만 사용한다.
- 제목은 "이전 생각 체인: 내성은 면역회피 축으로 수렴한다" 정도가 좋다.
- 너무 자세히 설명하지 않고, 이번 질문의 출발점으로만 사용한다.
- 핵심 메시지는 "이미 한 번 LLM-Wiki로 큰 프레임을 만들었고, 이번에는 그 프레임 안에서 데이터 구조와 단백체/인산화단백체 readout을 더 구체적으로 묻는다"이다.

## 나의 LLM-Wiki 운영 규칙

나만의 규칙을 별도 노드로 정리했다:

- [My LLM-Wiki Use Rules](./my-llm-wiki-use-rules.md)

핵심은 특정 생물학적 분류표가 아니라, **LLM을 어떤 자유도와 루틴으로 활용했는지에 대한 나의 사용 원칙**이다.

1. **질문의 출발점은 내가 정한다**: LLM에게 주제를 맡기지 않고, 내가 느낀 불편한 지점에서 시작한다.
2. **LLM은 답을 확정하지 않고 질문을 쪼갠다**: broad question을 여러 sub-question과 node 후보로 확장하게 한다.
3. **답변은 chat에 두지 않고 wiki node로 고정한다**: 다시 열고, 수정하고, 캡처할 수 있게 만든다.
4. **LLM이 만든 연결은 local source/wiki node로만 살린다**: 그럴듯하지만 근거가 없는 연결은 발표 체인에서 제외한다.
5. **방법은 질문 아래에 둔다**: multiomics integration 같은 방법론이 이야기를 지배하지 않게 한다.
6. **답보다 다음 질문을 남긴다**: answer가 생기면 그 answer가 만든 next question을 기록한다.
7. **질문별 graph capture를 만든다**: 전체 graph가 아니라 질문 하나당 중심 노드와 주변 노드를 보여준다.

이 규칙을 cancer resistance에 적용했더니, topic-specific한 질문 축이 생겼다:

> 내성 정의 -> 데이터 시간축 -> 약물 맥락 -> molecular readout -> 검증 강도

즉 이것은 LLM 활용 규칙 자체가 아니라, **그 규칙을 항암제 내성 biomarker 주제에 적용해서 나온 질문 분해 결과**이다.

## 발표용 노드 캡처 계획

교수님 공지의 핵심은 질문별로 노드를 캡처해 시각적으로 보여주는 것이다. 그래서 발표에서는 전체 graph가 아니라 아래 subgraph를 순서대로 보여준다.

캡처 준비용 전용 페이지:

- [Cancer Multiomics Presentation Capture Board](./cancer-multiomics-presentation-capture-board.md)
- [Cancer Multiomics Resistance Gap Decision Matrix](./cancer-multiomics-resistance-gap-decision-matrix.md)

| 발표 질문 | 캡처할 중심 노드 | 같이 보이면 좋은 연결 노드 | 보여줄 메시지 |
| --- | --- | --- | --- |
| LLM-Wiki를 그냥 논문 저장소가 아니라 어떻게 썼나? | `Cancer Multiomics Proteogenomic Atlas` | corpus queue, source pages, question-chain pages | source -> topic -> analysis -> question으로 지식이 올라간다 |
| 나만의 규칙은 무엇인가? | `My LLM-Wiki Use Rules` | presentation storyline, capture board, question chain | 내가 질문한다 -> LLM이 쪼갠다 -> 위키 노드로 고정한다 -> local source로 제한한다 -> 다음 질문을 남긴다 |
| 이전에 만든 큰 프레임은 무엇이었나? | `Cancer-Resistance Convergence Framework` | Cancer Resistance Manuscript Anchor, Immunotherapy Resistance and Immune Evasion | 내성은 여러 치료제에서 visibility/access/effector dysfunction 축으로 수렴할 수 있다 |
| 논문에서 말하는 내성은 무엇인가? | `Primary and Acquired Resistance Proteogenomics Ingest Map` | primary/acquired/refractory/atlas bucket에 해당하는 paper nodes | 내성 정의를 먼저 나눴다 |
| pre/post 데이터인가, resistant vs non-resistant 스냅샷인가? | `Primary and Acquired Resistance Proteogenomics Ingest Map` | Lee 2026, Anurag 2022, Chmielecki 2023, Yaeger 2023, Hsu 2025 | 데이터 구조가 해석 범위를 정한다 |
| protein/phosphosite marker는 어디까지 말할 수 있나? | `Cancer Multiomics Resistance Biomarker Evidence Boundary Map` | Lee 2026, Anurag 2022, Holt 2025, Jaehnig 2025, Hsu 2025, Yaeger 2023 | baseline marker와 therapy-emergent marker를 구분했다 |
| 여러 gap 후보 중 무엇을 메인으로 삼을까? | `Cancer Multiomics Resistance Gap Decision Matrix` | evidence boundary map, question chain, ingest map | resistance-associated marker가 어떤 내성 상태를 뜻하는지 구분하는 해석 gap을 중심으로 잡는다 |
| multiomics 통합 분석은 무엇을 답하기 위한 도구인가? | `Drug Response Proof-of-Concept with Global Proteome, Phosphoproteome, and Somatic SNV` | source pages, PTM/kinase topic | 방법 질문은 최종 질문이 아니라 해석을 돕는 sub-question이다 |
| phosphoproteome은 왜 별도 질문이 필요한가? | `PTM Correction and Kinase Signaling in Cancer Proteomics` | kinase inference, PTM correction, Hsu 2025, Holt 2025 | phosphosite는 raw site인지 protein-corrected site인지 구분해야 한다 |
| 이 과정이 어떤 연구질문으로 고도화됐나? | `Cancer Multiomics Presentation Storyline` | question chain, evidence boundary map, ingest map | 하나의 답이 아니라 질문이 다음 질문을 낳은 과정을 보여준다 |

캡처 원칙:

- 한 슬라이드에 하나의 질문만 둔다.
- 노드가 너무 많으면 paper cluster를 줄이고, 질문 노드와 4-6개 핵심 paper node만 보이게 한다.
- graph 캡처 옆에는 긴 설명 대신 `질문 -> 다시 연 노드 -> 발견한 gap -> 다음 질문` 네 칸만 둔다.
- 날짜형 파일명이나 chat transcript 느낌의 노드는 보여주지 않는다. durable한 질문/개념 slug만 보여준다.

## 질문 설계 원칙

이번 발표의 질문 체인은 큰 질문 하나를 바로 답하는 방식이 아니라, 아래 네 층의 sub-question을 차례로 통과하면서 연구 질문을 좁히는 방식이다.

| 질문 층 | 내가 물어본 것 | 왜 필요한가 | 발표에서의 역할 |
| --- | --- | --- | --- |
| 이전 큰 프레임 | cancer resistance는 어떤 공통 축으로 수렴하는가? | 면역회피 축이라는 큰 해석 틀을 이미 만든 경험이 있다 | 배경 생각 체인 |
| 정의 질문 | 논문에서 말하는 `resistance`는 primary non-response인가, acquired resistance인가, refractory state인가? | 내성 정의가 섞이면 같은 biomarker라도 해석이 달라진다 | 출발점 |
| 데이터 질문 | pre/post 또는 time-course 데이터인가, 아니면 resistant vs non-resistant 스냅샷인가? | 데이터 구조가 말할 수 있는 범위를 결정한다 | 핵심 gap 발견 |
| 측정 질문 | protein abundance, phosphosite, kinase activity 중 무엇을 보고 있는가? | 단백체와 인산화단백체는 같은 정보를 주지 않는다 | 기능 상태 해석 |
| 방법 질문 | 여러 multiomics layer를 어떻게 통합했고, 어떤 검증이 붙었는가? | 분석 방법과 검증 강도를 알아야 후보 biomarker의 신뢰도를 판단할 수 있다 | 보조 질문 |

따라서 `여러 멀티오믹스 데이터를 어떻게 통합했는가?`는 중요하지만 최종 질문은 아니다. 이 질문은 논문을 읽고 정리하기 위한 방법적 sub-question이고, 최종적으로는 **내성 정의와 데이터 구조가 protein/phosphosite biomarker 해석을 어떻게 제한하는가**로 올라간다.

## 질문-위키확장 체인

| 단계 | 내가 던진 질문 | 위키에서 확장한 노드 | 발견한 gap | 다음 질문 |
| --- | --- | --- | --- | --- |
| 0 | 항암제 내성은 약제별로 흩어져 있는가, 아니면 공통 축으로 수렴하는가? | Cancer resistance manuscript anchor, convergence framework | visibility/access/effector dysfunction이라는 면역회피 축으로 수렴하는 큰 프레임을 만들 수 있었다 | 이 큰 프레임 안에서 내성 biomarker를 더 구체적으로 어떻게 정의할까? |
| 1 | 항암제 내성은 논문마다 어떻게 정의되고 있나? | Primary/acquired resistance ingest map, resistance-state subtyping page | resistance가 baseline non-response, acquired resistance, refractory state, adaptive tolerance를 섞고 있었다 | 내가 말하려는 내성은 어떤 종류인가? |
| 2 | resistant sample 하나로 acquired resistance를 말할 수 있을까? | Primary/acquired resistance ingest map | post-treatment 또는 refractory sample만으로는 emergence를 증명할 수 없다 | 어떤 sampling design이 primary와 acquired를 구분하게 해줄까? |
| 3 | pre/post 또는 time-course 데이터인가, 아니면 resistant vs non-resistant 스냅샷인가? | Lee 2026, Anurag 2022, Holt 2025, Jaehnig 2025, Chmielecki 2023, Yaeger 2023, Hsu 2025 | 스냅샷 response-labeled 데이터는 baseline marker에는 강하지만 therapy-emergent marker에는 제한이 있다 | pre-treatment, post-treatment, progression, model time-course를 어떻게 구분할까? |
| 4 | pre-treatment response-labeled 논문들은 무엇을 잘 말해주나? | Lee 2026, Anurag 2022, Holt 2025, Jaehnig 2025, Zhang 2023, Sambath 2026 | baseline non-response marker에는 강하지만 치료 후 새로 생긴 resistance marker와는 다르다 | acquired resistance에는 어떤 pre/post 또는 time-course data가 필요한가? |
| 5 | acquired resistance 논문들은 무엇이 부족한가? | Chmielecki 2023, Yaeger 2023, Memon 2024, Hsu 2025, Wei 2026 | serial/longitudinal evidence는 있지만 patient proteome/phosphoproteome이 함께 있는 경우가 드물다 | protein/phosphosite state가 치료 후 새로 생겼는지 어떻게 검증할까? |
| 6 | 단백체와 인산화단백체는 서로 다른 내성 정보를 주는가? | PTM/kinase topic, drug-response POC page | protein abundance marker와 kinase/phosphosite state marker가 같은 의미를 갖지는 않는다 | 어떤 내성은 protein abundance로, 어떤 내성은 phosphosite/kinase state로 더 잘 보일까? |
| 7 | phosphosite 변화는 진짜 signaling인가, protein abundance 변화의 반영인가? | PTM correction and kinase signaling topic | phosphoproteome biomarker로 해석하려면 correction/normalization 기준이 필요하다 | 내성 biomarker 후보를 raw site, protein-corrected site, kinase activity 중 무엇으로 정의할까? |
| 8 | 여러 multiomics 데이터는 어떻게 통합했나? | Drug response POC page, source pages, topic hub | 통합 방법은 중요하지만, 내성 정의와 sampling design을 먼저 고정하지 않으면 해석이 흐려진다 | 통합 분석은 어떤 질문을 답하기 위한 도구인가? |
| 9 | 내성 state가 종양세포 intrinsic인지 TME/immune state인지 어떻게 나눌까? | resistance framework, Cancer Multiomics immune/neoantigen pages | bulk proteomics에서는 tumor-intrinsic kinase와 immune/stromal signal이 섞일 수 있다 | 단백체/인산화단백체 marker를 tumor-intrinsic, immune-access, effector-dysfunction 축으로 나눌 수 있을까? |
| 10 | response-labeled 논문의 protein/phosphosite marker는 어디까지 말할 수 있나? | Resistance biomarker evidence boundary map | baseline marker, therapy-emergent marker, adaptive tolerance marker, refractory-state marker가 섞이면 review 질문이 흐려진다 | marker별 검증 강도를 어떻게 나눌까? |
| 11 | 최종적으로 내가 파야 할 질문 후보는 무엇인가? | presentation storyline, ingest map, PTM/kinase topic, evidence boundary map 연결 | 아직 하나의 정답보다, 후보 질문군을 ranking해야 한다 | 어떤 질문이 내 리뷰 논문과 실제 분석으로 가장 이어지기 쉬울까? |

## 고도화된 연구질문 후보군

이 발표에서는 최종 연구질문을 하나로 너무 빨리 고정하지 않는다. 대신 위키를 통해 아래 후보군으로 좁혀졌다고 보여준다.

### 후보 1. Timing 중심 질문

> 항암제 내성 단백체/인산화단백체 바이오마커는 치료 전부터 존재하는 primary resistance marker와 치료 후 emergence되는 acquired resistance marker로 어떻게 구분될 수 있는가?

이 질문은 `pre/post 데이터 구조가 필요한가?`라는 방법론 질문을 포함하지만, 그 자체가 메인 질문은 아니다.

### 후보 2. Functional State 중심 질문

> 항암제 내성에서 단백질 발현 변화와 phosphosite/kinase activity 변화는 각각 어떤 종류의 resistance state를 더 잘 포착하는가?

이 질문은 proteome과 phosphoproteome을 단순히 "레이어"로 쌓는 것이 아니라, 서로 다른 정보를 주는 readout으로 분리한다.

### 후보 3. 바이오마커 근거 기준 질문

> Cancer proteogenomics 논문에서 어떤 조건을 만족해야 protein/phosphosite signal을 resistance biomarker라고 조심스럽게 말할 수 있는가?

이 질문은 review 논문에 잘 맞는다. 논문들을 primary/acquired/refractory/atlas blueprint로 재분류하고 근거 기준표를 만들 수 있다.

### 후보 4. Drug-Class Specific 질문

> chemotherapy, TKI, anti-HER2 therapy, immunotherapy에서 반복적으로 등장하는 protein/phosphosite resistance axis는 서로 같은가, drug-class specific한가?

이 질문은 너무 크기 때문에 발표에서는 "다음 단계"로 두는 편이 좋다.

### 후보 5. 방법론/통합분석 질문

> 내성 바이오마커를 해석하기 위해 WES/WGS, RNA-seq, proteome, phosphoproteome, kinase activity를 어떤 순서와 기준으로 통합해야 하는가?

이 질문은 내가 논문을 읽고 내 데이터를 설계하기 위해 필요한 sub-question이다. 하지만 발표의 최종 질문으로 세우면 "멀티오믹스 통합 방법 소개"처럼 보일 수 있으므로, 내성 정의와 데이터 구조를 정한 뒤에 나오는 방법론 질문으로 둔다.

### 현재 가장 좋은 발표용 메인 질문

> **항암제 내성 바이오마커를 단백체·인산화단백체로 찾으려면, 먼저 그 신호가 언제 생긴 내성인지와 어떤 기능 상태를 반영하는지를 어떻게 구분해야 하는가?**

이 문장이 발표용으로 가장 균형이 좋다. `내성 정의`, `pre/post 데이터 필요성`, `primary/acquired 구분`, `protein vs phosphosite readout`, `multiomics 통합 방법`, `바이오마커 근거 기준`을 모두 하위 질문으로 품을 수 있다.

### 더 날카로운 리뷰 논문용 질문

> **Proteogenomic studies of anticancer resistance often identify protein or phosphosite markers in response-labeled or refractory tumors, but how can these markers be classified into baseline resistance, therapy-emergent resistance, and functional resistance-state biomarkers?**

한국어:

> **항암제 내성 proteogenomics 연구에서 발견되는 protein/phosphosite marker를 baseline resistance, therapy-emergent resistance, functional resistance-state biomarker로 구분하기 위한 기준은 무엇인가?**

## Slide Plan (15분)

### 1. 문제 제기: 대학원 연구는 지식 체인을 직접 만드는 과정이다

말할 내용:

- 처음에는 논문을 많이 읽으면 연구질문이 생길 거라고 생각했다.
- 하지만 Cancer Multiomics를 읽을수록 논문 수보다 중요한 것은 **논문 사이의 연결 규칙**이었다.
- 그래서 LLM-Wiki를 단순 요약 저장소가 아니라 "질문이 남는 구조"로 운영했다.

시각 자료:

- `wiki/_meta/index.md` 전체 구조 스크린샷
- 아주 단순한 흐름도: raw PDF -> source note -> topic hub -> question -> synthesis

### 2. 나의 코퍼스: Cancer Multiomics 100편 큐에서 시작했지만, 곧바로 막힌 지점

말할 내용:

- Cancer Multiomics 코퍼스는 target 100편으로 운영했고, selected/acquired/ingested/briefed를 분리해 추적했다.
- 현재 큐는 WGS+proteogenomics, phosphoproteomics, neoantigen/immunopeptidomics, treatment response model, AI/spatial/ecDNA 확장으로 나뉜다.
- 그런데 "항암제 내성 바이오마커"라는 말이 너무 넓어서, 논문을 많이 모아도 연구질문이 바로 선명해지지는 않았다.
- 그래서 위키의 역할이 바뀌었다. 논문을 모으는 도구가 아니라, **각 논문이 어떤 내성에 대해 어디까지 말할 수 있는지 정리하는 도구**가 되었다.

시각 자료:

- [Cancer Multiomics Corpus Queue](./cancer-multiomics-corpus-queue.md)의 Status 캡처
- Obsidian graph 1: `Cancer Multiomics Literature Monitor` 중심 전체 graph

### 3. 이전 생각 체인: 내성은 면역회피 축으로 수렴하는가?

출발 질문:

> 여러 항암제 내성 논문은 약제별로 흩어진 이야기인가, 아니면 공통적인 immune-evasion failure mode로 정리할 수 있는가?

위키로 만든 결과:

- [Cancer Resistance Manuscript Anchor](./cancer-resistance-manuscript-anchor.md)
- [Cancer-Resistance Convergence Framework](../syntheses/resistance-convergence-framework.md)
- [Immunotherapy Resistance and Immune Evasion](../topics/immunotherapy-resistance-and-immune-evasion.md)

중간 결론:

> 다양한 치료제 내성은 visibility, access, effector dysfunction이라는 면역회피 축으로 수렴할 수 있지만, 각 치료제 class마다 축의 비중은 다르다.

이번 발표로 이어지는 질문:

> 그렇다면 단백체·인산화단백체 데이터로 관찰되는 내성 biomarker는 이 큰 면역회피 프레임 안에서 어떤 상태를 반영하는가?

시각 자료:

- Obsidian graph: `Cancer-Resistance Convergence Framework` 중심 subgraph
- visibility / access / effector dysfunction 세 축과 연결된 concept nodes

### 4. 첫 질문: 논문에서 말하는 내성은 무엇인가?

출발 질문:

> 내가 읽는 논문에서 말하는 resistance는 치료 전부터 반응이 없던 상태인가, 치료 후 새로 생긴 상태인가, 아니면 치료 실패 후 남은 refractory state인가?

위키로 확인한 점:

- 같은 "내성"이라도 primary non-response, acquired resistance, adaptive tolerance, refractory state가 서로 다르다.
- response-labeled baseline 논문은 baseline marker를 말하기 좋지만, 치료 후 새로 생긴 내성을 말하려면 시간축이 필요하다.
- refractory sample은 현재 resistant state를 보여줄 수 있지만, 그 상태가 언제 생겼는지는 별도 근거가 필요하다.

중간 결론:

> 내성 바이오마커 질문은 "어떤 omics를 쓸 것인가"보다 먼저 "내성을 무엇으로 정의할 것인가"에서 시작해야 한다.

시각 자료:

- Obsidian graph 2: `Primary and Acquired Resistance Proteogenomics Ingest Map`
- 네 bucket: primary resistance / acquired resistance / adaptive tolerance / refractory state

### 5. 두 번째 질문: resistant sample 하나로 acquired resistance를 말할 수 있을까?

출발 질문:

> 항암제 내성 환자 샘플에서 단백체/인산화단백체 바이오마커를 찾으면, 그것을 곧바로 acquired resistance biomarker라고 부를 수 있을까?

위키로 확인한 점:

- Resistant sample만 있으면 현재 상태는 설명할 수 있지만, 그 상태가 치료 전부터 있었는지 치료 압력으로 생겼는지는 알 수 없다.
- Pre-treatment sample + response label이 있으면 primary resistance marker를 말할 수 있다.
- Same-patient pre/post 또는 serial progression data가 있으면 acquired resistance에 가깝게 말할 수 있다.
- Post-treatment/refractory sample만 있으면 acquired mechanism이 아니라 refractory resistance-state marker라고 더 조심스럽게 말해야 한다.

중간 결론:

> 내성 바이오마커 발굴에서 첫 번째 gap은 omics layer의 문제가 아니라 **sampling time과 해석 범위의 불일치**였다.

시각 자료:

- Obsidian graph 3: `primary/acquired resistance proteogenomics ingest map`
- 네 bucket: primary resistance / acquired resistance / static refractory state / baseline atlas blueprint

### 6. 세 번째 질문: primary resistance와 acquired resistance는 데이터 구조가 어떻게 달라야 하나?

발전 질문:

> 내가 찾고 싶은 단백체·인산화단백체 기반 내성 바이오마커는 baseline non-response marker인가, 치료 후 emergence marker인가?

위키에서 정리된 data requirement:

1. **Primary resistance**: pre-treatment biopsy + fixed response label(pCR/non-pCR, RECIST, RCB 등)
2. **Acquired resistance**: same-patient pre-treatment + post-progression sample, 가능하면 on-treatment/serial ctDNA 포함
3. **Adaptive tolerance**: early on-treatment 또는 model-system time course
4. **Static refractory state**: treatment-failed sample; 현재 resistance state 묘사는 가능하지만 emergence 해석은 제한
5. **Feature-design atlas**: treatment-naive atlas; target/protein/phosphosite readout 설계에는 유용하지만 직접 내성 근거로 쓰기에는 제한

예시:

- Lee 2026 TNBC, Anurag 2022 TNBC, Holt 2025 MIBC, Jaehnig 2025 HER2+ breast: pre-treatment + response label이 있어 primary resistance biomarker 질문에 강하다.
- Chmielecki 2023, Yaeger 2023, Memon 2024, Wei 2026: acquired resistance의 time-axis를 묻는 데 중요하지만, proteome/phosphoproteome까지 갖춘 논문은 더 드물다.
- Hsu 2025 osimertinib DTP: patient cohort는 아니지만 on-treatment/adaptive phosphoproteome time course가 왜 필요한지 보여준다.

시각 자료:

- `Primary and Acquired Resistance Proteogenomics Ingest Map`의 classification table
- Obsidian graph 4: `pre/post`, `snapshot`, `longitudinal`, `drug-tolerant persister`, `phosphoproteomics` 주변 노드

### 7. 네 번째 질문: 그렇다면 protein/phosphoproteome marker는 어떤 내성 상태를 뜻하나?

고도화 질문:

> acquired resistance에서 DNA alteration이 명확하지 않거나, baseline feature와 post-treatment state가 섞여 보일 때, 단백체·인산화단백체는 어떤 종류의 바이오마커를 줄 수 있을까?

왜 이 질문이 생겼나:

- Response-labeled proteogenomics 논문들은 protein abundance, pathway protein score, phosphosite/kinase activity가 non-response phenotype과 연결될 수 있음을 보여준다.
- Longitudinal acquired-resistance 논문들은 치료 후 새로 생긴 clone/state를 잡으려면 pre/post가 필요하다는 점을 보여준다.
- 그런데 같은 `resistance-associated marker`라도 baseline non-response marker인지, therapy-emergent marker인지, refractory-state feature인지 해석이 섞일 수 있다. 즉 핵심 gap은 단순한 데이터 부족이 아니라, **protein/phosphosite marker가 어떤 내성 상태를 의미하는지 구분하는 기준이 부족하다**는 점이다.
- Longitudinal pre/post 데이터 부족은 이 해석 gap을 만든 중요한 이유 중 하나다.
- 그래서 질문은 "단백체로 타겟을 찾자"가 아니라, **protein/phosphosite marker를 어떤 내성 상태와 근거 수준으로 분류할 것인가**로 좁혀진다.

시각 자료:

- Obsidian graph 5: `Lee/Anurag/Holt/Jaehnig` primary-response cluster vs `Chmielecki/Yaeger/Memon/Hsu/Wei` acquired/time-course cluster
- 두 cluster 사이에 비어 있는 edge: `same-patient pre/post + proteome/phosphoproteome`
- 이 빈 edge의 의미: 데이터가 없다는 말에서 끝나는 것이 아니라, therapy-emergent marker와 baseline marker를 구분하는 해석 기준이 아직 약하다는 점

### 7-1. 실제 두 번째 위키 확장: marker 근거 범위 정리

추가 질문:

> response-labeled proteogenomics 논문에서 나온 protein/phosphosite marker는 baseline non-response marker인가, therapy-emergent marker인가, adaptive tolerance marker인가, refractory-state marker인가?

위키에서 새로 만든 노드:

- [Cancer Multiomics Resistance Biomarker Evidence Boundary Map](./cancer-multiomics-resistance-biomarker-evidence-boundary-map.md)

중간 결론:

- Lee 2026, Anurag 2022, Holt 2025, Jaehnig 2025, Zhang 2023, Sambath 2026은 주로 baseline primary resistance 또는 response-labeled marker 근거에 강하다.
- Hsu 2025는 patient cohort는 아니지만 adaptive tolerance phosphoproteome time-course의 필요성을 보여준다.
- Chmielecki 2023, Yaeger 2023, Memon 2024는 acquired-resistance timing을 보여주지만, patient-level proteome/phosphoproteome layer가 부족하거나 별도 검증이 필요하다.

따라서 다음 질문은 `pre/post가 필요한가?`가 아니라:

> 어떤 marker가 같은 cohort association을 넘어 independent cohort, perturbation, organoid/PDX, IHC/PRM, patient-longitudinal validation까지 올라갈 수 있는가?

### 8. 방법론 sub-question: multiomics는 어떻게 통합해야 하나?

위치:

> 이 질문은 내가 논문과 데이터를 이해하기 위해 꼭 필요하지만, 발표의 메인 질문은 아니다.

물어볼 것:

- WES/WGS alteration, RNA, protein abundance, phosphosite, kinase activity 중 무엇을 먼저 기준으로 삼았나?
- response label 또는 resistance definition이 먼저 고정되어 있었나?
- omics layer를 단순히 많이 넣었나, 아니면 각 layer가 서로 다른 생물학적 상태를 설명하도록 설계했나?
- validation은 same cohort association인지, independent cohort인지, perturbation/organoid/PDX/IHC/PRM인지?

중간 결론:

> multiomics integration은 "증거 레이어를 많이 쌓자"가 아니라, 정의한 내성 상태를 설명하기 위해 어떤 측정값이 필요한지 묻는 방법론 질문이다.

### 9. 현재 도달한 메인 질문 후보

발표용 메인 질문:

> **항암제 내성 바이오마커를 단백체·인산화단백체로 찾으려면, 먼저 그 신호가 언제 생긴 내성인지와 어떤 기능 상태를 반영하는지를 어떻게 구분해야 하는가?**

이 질문을 이루는 하위 질문:

- 이 신호는 치료 전부터 있던 baseline non-response marker인가?
- 치료 후 새로 생긴 therapy-emergent marker인가?
- post-treatment refractory tumor의 현재 상태 marker인가?
- protein abundance 변화인가, phosphosite/kinase activity 변화인가?
- tumor-intrinsic state인가, immune/stromal context인가?
- 같은 약제 class에서 반복되는가, 암종/약제 특이적인가?

리뷰 논문용 확장 질문:

> **항암제 내성 proteogenomics 연구에서 발견되는 protein/phosphosite marker를 baseline resistance, therapy-emergent resistance, functional resistance-state biomarker로 구분하기 위한 기준은 무엇인가?**

### 10. 내가 앞으로 쓸 리뷰 논문의 구조로 연결

리뷰 논문 구조 후보:

1. 항암제 내성 바이오마커 연구에서 "resistance"라는 단어가 섞는 서로 다른 의미들
2. Primary resistance: pre-treatment response-labeled proteogenomics가 가능한 질문
3. Acquired resistance: pre/post 또는 serial sampling이 필요한 이유
4. Functional resistance state: protein abundance와 phosphosite/kinase activity가 포착하는 것
5. 현재 문헌 gap: longitudinal patient proteomics/phosphoproteomics 부족
6. 제안: pre/post protein/phosphosite 기반 내성 바이오마커 근거 기준

### 11. 결론: LLM-Wiki가 한 일

말할 내용:

- LLM-Wiki가 대신 연구질문을 "생성"한 것이 아니라, 내가 broad한 질문을 던질 때마다 그 질문에 필요한 근거가 무엇인지 되묻게 만들었다.
- source page는 사실을 안정화했고, ingest map은 논문별 근거로 말할 수 있는 범위를 분리했고, question chain은 연구 gap을 드러냈다.
- 그래서 이번 발표의 핵심은 "내가 어떤 주제를 골랐다"가 아니라, **내 지식 체인이 어떻게 연구질문이 되었는가**이다.

마지막 문장:

> Cancer Multiomics 위키를 만들면서 제가 얻은 가장 큰 결론은, 항암제 내성 바이오마커를 찾기 전에 먼저 "이 신호가 치료 전부터 있던 primary resistance인지, 치료 후 생긴 acquired resistance인지, 아니면 refractory state의 단면인지"를 구분해야 한다는 것이었습니다.

## Q&A 대비 질문

- primary resistance와 acquired resistance를 왜 먼저 구분해야 하나?
- pre/post sample이 없으면 무엇을 말할 수 없게 되나?
- phosphoproteomics는 내성 바이오마커 발굴에서 어떤 정보를 추가하나?
- LLM이 만든 요약의 오류는 어떻게 막았나?
- 코퍼스가 너무 넓어지는 것을 어떻게 통제했나?
- 최종 리뷰 논문에서는 암종별로 쓸 것인가, 내성 timing별로 쓸 것인가?
- 실제 분석으로 이어진다면 어떤 pre/post comparison을 먼저 설계할 것인가?

## LLM 활용규칙 Q&A 대비

### Q. LLM이 그냥 그럴듯한 말을 만든 것과 어떻게 구분했나?

답변:

> 저는 LLM 답변을 바로 결론으로 쓰지 않고, 반드시 로컬 PDF나 이미 작성한 source page로 돌아가게 했습니다. 특히 과학적 수치나 바이오마커 해석은 웹 검색으로 채우지 않고, raw PDF/source page에 있는 경우만 위키에 남겼습니다. LLM은 답을 생성하는 도구라기보다, 기존 노드를 다시 열고 말이 너무 앞서가는지 점검하는 도구로 썼습니다.

### Q. 본인만의 LLM-Wiki 규칙은 무엇이었나?

답변:

> 제 규칙은 세 가지였습니다. 첫째, source page는 사실을 안정화하는 층으로 두고 raw PDF 경계를 넘지 않았습니다. 둘째, topic hub에는 논문을 쌓기만 하지 않고 질문별로 다시 연결했습니다. 셋째, 결론을 쓰기 전에 각 논문이 어디까지 말할 수 있는지 먼저 확인했습니다. 예를 들어 "내성 biomarker"라고 쓰기 전에 baseline non-response인지, acquired resistance인지, refractory-state인지 먼저 분류했습니다.

### Q. 왜 질문별 노드 캡처가 중요한가?

답변:

> 전체 graph만 보여주면 위키가 커졌다는 사실만 보이고, 제가 어떤 사고 과정을 거쳤는지는 잘 안 보입니다. 그래서 질문별로 관련 노드만 캡처했습니다. 예를 들어 acquired resistance 질문에서는 primary/acquired ingest map과 serial resistance papers만 보여주고, marker 해석 질문에서는 evidence boundary page와 response-labeled proteogenomics papers만 보여주는 식입니다.

### Q. LLM이 연구질문을 대신 만들어준 것 아닌가?

답변:

> 저는 LLM에게 "연구질문 하나 만들어줘"라고 맡긴 것이 아니라, 제가 던진 broad한 질문을 위키 규칙으로 계속 쪼갰습니다. LLM은 각 질문이 요구하는 evidence structure를 되묻게 했고, 그 결과 pre/post 데이터 구조, protein vs phosphosite readout, validation tier 같은 하위 질문이 생겼습니다. 최종 연구질문은 그 질문 체인의 결과입니다.

### Q. 위키가 커지면 산만해지지 않았나?

답변:

> 그래서 날짜별 기록이나 chat transcript를 남기지 않고, durable한 질문 노드로 쪼갰습니다. `question chain`, `evidence boundary map`, `ingest map`처럼 다시 열었을 때 바로 다음 질문으로 이어지는 페이지명과 구조를 썼습니다. 새 페이지를 만들 때도 기존 topic hub와 index에 연결해서 고립된 요약이 되지 않게 했습니다.

## 추천 Obsidian Graph 구성

1. **Whole Wiki Graph**: 전체 구조를 5초만 보여주고 바로 넘어간다.
2. **Cancer Multiomics Hub Graph**: topic hub 중심으로 source/analysis가 붙는 구조.
3. **Resistance Timing Graph**: primary / acquired / refractory / atlas blueprint bucket.
4. **Primary Response Graph**: Lee 2026, Anurag 2022, Holt 2025, Jaehnig 2025, Zhang 2023, Sambath 2026.
5. **Acquired-Time-Course Gap Graph**: Chmielecki 2023, Yaeger 2023, Memon 2024, Hsu 2025, Wei 2026, plus missing edge to patient pre/post phosphoproteomics.
6. **Evidence Boundary Graph**: `Cancer Multiomics Resistance Biomarker Evidence Boundary Map` 중심으로 baseline marker papers와 acquired timing papers가 갈라지는 구조.

## Connections

- [Cancer Multiomics Literature Monitor](../topics/cancer-multiomics-literature.md)
- [Cancer Multiomics Corpus Queue](./cancer-multiomics-corpus-queue.md)
- [Cancer Multiomics Presentation Capture Board](./cancer-multiomics-presentation-capture-board.md)
- [Cancer Resistance Manuscript Anchor](./cancer-resistance-manuscript-anchor.md)
- [Cancer-Resistance Convergence Framework](../syntheses/resistance-convergence-framework.md)
- [Immunotherapy Resistance and Immune Evasion](../topics/immunotherapy-resistance-and-immune-evasion.md)
- [Primary and Acquired Resistance Proteogenomics Ingest Map](./primary-acquired-resistance-proteogenomics-ingest-map.md)
- [Cancer Multiomics Resistance Biomarker Evidence Boundary Map](./cancer-multiomics-resistance-biomarker-evidence-boundary-map.md)
- [Drug Response Proof-of-Concept with Global Proteome, Phosphoproteome, and Somatic SNV](./drug-response-poc-global-phospho-somatic-snv.md)
- [PTM Correction and Kinase Signaling in Cancer Proteomics](../topics/ptm-correction-and-kinase-signaling-in-cancer-proteomics.md)
- [Kinase Activity Inference Under PTM Correction](../syntheses/kinase-activity-inference-under-ptm-correction.md)
- [Four-Topic Question Expansion Map](./topic-question-expansion-map.md)

## Sources

- [Cancer Multiomics Resistance Biomarker Question Chain](./cancer-multiomics-resistance-biomarker-question-chain.md)
- [Cancer Multiomics Resistance Biomarker Evidence Boundary Map](./cancer-multiomics-resistance-biomarker-evidence-boundary-map.md)
- [Cancer Multiomics Presentation Capture Board](./cancer-multiomics-presentation-capture-board.md)
- [Cancer Resistance Manuscript Anchor](./cancer-resistance-manuscript-anchor.md)
- [Cancer-Resistance Convergence Framework](../syntheses/resistance-convergence-framework.md)
- [Cancer Multiomics Literature Monitor](../topics/cancer-multiomics-literature.md)
- [Cancer Multiomics Corpus Queue](./cancer-multiomics-corpus-queue.md)
- [Primary and Acquired Resistance Proteogenomics Ingest Map](./primary-acquired-resistance-proteogenomics-ingest-map.md)
- [Drug Response Proof-of-Concept with Global Proteome, Phosphoproteome, and Somatic SNV](./drug-response-poc-global-phospho-somatic-snv.md)
- Advanced Genetics Zoom Summary 2026-05-19: `/Users/zzeongvely/Desktop/Advanced_Genetics_Zoom_Summary_2026-05-19.pdf`

## PPT 압축안

실제 PPT는 10-12장 정도로 압축한다. 각 슬라이드는 한 문장 메시지와 하나의 캡처/도식만 갖는 것이 좋다.

| Slide | 제목 | 핵심 메시지 | 시각 자료 |
| --- | --- | --- | --- |
| 1 | 질문이 질문을 낳는 방식 | Cancer Multiomics 위키를 항암제 내성 바이오마커 연구질문을 좁히는 도구로 사용했다 | 제목 + 작은 wiki graph |
| 2 | 왜 위키가 필요했나 | 논문을 많이 읽는 것만으로는 내성 정의, 데이터 구조, 분석 방법이 분리되지 않았다 | raw PDF -> source page -> topic hub -> question node 도식 |
| 3 | 나만의 LLM-Wiki 규칙 | 내가 질문을 던지고, LLM은 질문을 쪼개며, 답은 위키 노드로 고정하고, local source로 제한하고, 다음 질문을 남기는 방식으로 사용했다 | `My LLM-Wiki Use Rules` |
| 4 | 이전 생각 체인: 내성은 어디로 수렴하나 | 기존 cancer resistance review에서 내성을 visibility/access/effector dysfunction 축으로 정리했다 | Cancer-Resistance Convergence Framework graph |
| 5 | 이번 질문의 출발점: 내성이란 무엇인가 | resistance는 primary non-response, acquired resistance, adaptive tolerance, refractory state를 섞고 있었다 | `Primary and Acquired Resistance Proteogenomics Ingest Map` 캡처 |
| 6 | 데이터는 시간축을 갖는가 | pre/post 또는 time-course 데이터와 resistant vs non-resistant 스냅샷은 말할 수 있는 범위가 다르다 | baseline cluster vs acquired/time-course cluster |
| 7 | baseline marker와 therapy-emergent marker는 다른가 | response-labeled baseline 논문은 primary resistance에 강하지만 acquired emergence에는 제한이 있다 | Lee/Anurag/Holt/Jaehnig vs Chmielecki/Yaeger/Hsu |
| 8 | 단백체와 인산화단백체는 무엇을 다르게 보나 | protein abundance와 phosphosite/kinase activity는 서로 다른 기능 상태를 보여준다 | PTM/kinase topic subgraph |
| 9 | multiomics 통합은 무엇을 위한 방법인가 | 여러 layer를 쌓는 것이 아니라, 정의한 내성 상태를 설명하기 위해 통합한다 | Drug Response POC ladder |
| 10 | 위키 확장 결과 | 질문 체인이 `Evidence Boundary Map`으로 확장되어 marker 해석 범위를 정리했다 | Evidence Boundary Map graph |
| 11 | 발견한 연구 gap | resistance-associated protein/phosphosite marker가 어떤 내성 상태를 뜻하는지 구분하는 기준이 부족하다 | Gap Decision Matrix |
| 12 | 도출된 연구질문 | protein/phosphosite marker를 baseline, therapy-emergent, functional resistance-state biomarker로 어떻게 구분할 것인가 | 최종 질문 + 하위 질문 4개 |
| 13 | 결론 | LLM은 답을 준 것이 아니라 질문을 외재화하고, 다음 질문으로 연결하게 했다 | 질문 체인 요약 |

피해야 할 것:

- "유전체만으로 부족하다"를 발표의 출발점으로 삼지 않는다.
- "evidence layer를 쌓자"를 결론으로 삼지 않는다.
- multiomics integration 방법 자체를 메인 질문으로 삼지 않는다.
- 이전 발표자의 용어와 구성을 그대로 가져오지 않는다.

발표의 중심 문장:

> 항암제 내성 바이오마커를 단백체·인산화단백체로 찾으려면, 먼저 그 신호가 어떤 종류의 내성을 반영하는지, 그리고 그 해석을 뒷받침할 데이터 구조가 있는지를 구분해야 한다.
