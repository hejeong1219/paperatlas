---
title: My LLM-Wiki Use Rules
tags:
  - analysis
  - llm-wiki-rules
  - presentation
  - hypothesis-building
themes:
  - llm-use
  - question-chain
  - research-thinking
date: 2026-05-28
---

# My LLM-Wiki Use Rules

This page defines the user's own rules for using LLM-Wiki as a research-thinking tool. These are not biology-specific sorting categories. Cancer multiomics resistance is the example used to show how the rules worked in practice.

## Key Points

- The rule is not `resistance definition -> data time-axis -> drug context -> molecular readout -> validation strength`. That is the **topic-specific question path** produced after using the LLM-Wiki.
- The user's actual rule is about how to control the LLM: the user supplies the discomfort/question, the LLM expands it into nodes, the wiki stores the thought chain, and every answer must leave a next question.
- The goal is to show that LLM was not used as an answer generator, but as a structured thinking partner whose output was constrained by local sources and wiki links.
- For the presentation, this page should be captured as the user's "LLM 활용 규칙" slide.

## My Rules

### The Confusion -> Contrast -> Blank Rule

My LLM-Wiki rule is simple:

> 헷갈리는 말을 찾고, 그것을 대조쌍으로 나누고, 그 대조를 구분하려면 무엇이 비어 있는지 찾는다.

This is easier to explain than a long checklist. It is also different from simply asking the LLM to summarize papers.

### Step 1. Confusion: 헷갈리는 말을 그대로 넘기지 않는다

When a word feels obvious but keeps being used differently, I mark it as a confusion point.

In this project:

> "resistance biomarker" sounds like one idea, but the papers were not always talking about the same kind of resistance.

Presentation sentence:

> 저는 LLM에게 답을 묻기 전에, 먼저 제가 헷갈리는 단어가 무엇인지 찾게 했습니다.

### Step 2. Contrast: LLM에게 항상 "A와 B를 나눠보라"고 시킨다

I do not ask only "what is this?" I ask "what should this be compared against?"

In this project, LLM-Wiki helped turn one broad phrase into contrast pairs:

- primary resistance vs acquired resistance
- pre/post data vs resistant/non-resistant snapshot
- protein abundance vs phosphosite / kinase activity
- drug-specific resistance vs shared resistance axis
- biological question vs multiomics method

Presentation sentence:

> 제 규칙은 넓은 질문을 바로 답하지 않고, 항상 대조쌍으로 바꿔서 보게 하는 것입니다.

### Step 3. Blank: 대조쌍을 구분하려면 무엇이 비어 있는지 묻는다

After making a contrast pair, I ask what evidence would be needed to distinguish the two sides.

In this project:

Contrast:

> baseline primary resistance marker vs therapy-emergent acquired resistance marker

Blank:

> same-patient longitudinal patient proteome/phosphoproteome data are sparse.

Presentation sentence:

> 대조쌍을 만든 다음에는, 그 둘을 구분하려면 어떤 데이터가 빠져 있는지를 gap으로 남겼습니다.

### Step 4. Node: 혼동, 대조, 빈칸을 각각 위키 노드로 남긴다

Only the useful parts of the LLM conversation become wiki pages. A page is created when it helps preserve one of these:

- confusion: what word is unclear?
- contrast: what two things should not be mixed?
- blank: what comparison or data is missing?

In this project:

- confusion node: [Cancer Multiomics Resistance Biomarker Question Chain](./cancer-multiomics-resistance-biomarker-question-chain.md)
- contrast / blank node: [Cancer Multiomics Resistance Biomarker Evidence Boundary Map](./cancer-multiomics-resistance-biomarker-evidence-boundary-map.md)
- presentation node: [Cancer Multiomics Presentation Capture Board](./cancer-multiomics-presentation-capture-board.md)

Presentation sentence:

> 그래서 제 위키의 노드는 단순한 논문 요약이 아니라, 혼동을 대조쌍으로 바꾸고 빈칸을 찾은 흔적입니다.

### Step 5. Capture: 발표에서는 "질문 하나 -> 대조 하나 -> 빈칸 하나"만 보여준다

For each slide, I keep the capture unit small:

- one question
- one center node
- one contrast pair
- one missing piece
- one next question

Presentation sentence:

> 전체 위키 그래프를 보여주기보다, 질문 하나가 어떤 대조쌍과 빈칸으로 이어졌는지를 캡처합니다.

## Cancer Resistance Example

These LLM-use rules produced a topic-specific question path:

| Rule step | What happened in this project | Topic-specific result |
| --- | --- | --- |
| Confusion | "resistance biomarker"라는 말이 너무 넓었다 | 내성 정의 질문 |
| Contrast | LLM-Wiki가 대조쌍을 만들었다 | primary vs acquired, pre/post vs snapshot, abundance vs activity |
| Blank | 대조쌍을 구분할 때 빠진 데이터를 찾았다 | longitudinal acquired-resistance proteome/phosphoproteome gap |
| Node | 혼동과 대조를 wiki page로 고정했다 | question chain, evidence boundary map |
| Capture | 발표용으로 질문별 캡처 보드를 만들었다 | PPT-ready node sequence |

## Slide Version

One-slide version:

> 나의 LLM-Wiki 활용 규칙은 헷갈리는 단어를 찾고, 그 단어를 대조쌍으로 나눈 뒤, 그 대조를 구분하기 위해 비어 있는 데이터를 다음 질문으로 남기는 방식이다.

Very short version:

> Confusion -> Contrast -> Blank -> Node -> Capture

## How This Produced the Research Question

Starting discomfort:

> 항암제 내성 biomarker라고 할 때, 논문마다 내성의 의미와 데이터 구조가 섞여 있다.

LLM-Wiki expansion:

1. resistance라는 단어가 primary, acquired, adaptive, refractory를 섞는다는 것을 노드화했다.
2. pre/post, time-course, snapshot 데이터가 각각 말할 수 있는 범위를 나누었다.
3. protein abundance와 phosphosite/kinase activity를 같은 layer가 아니라 다른 functional readout으로 분리했다.
4. multiomics integration은 최종 질문이 아니라 method sub-question으로 내렸다.
5. longitudinal acquired-resistance patient proteome/phosphoproteome data gap을 다음 질문으로 남겼다.

Resulting research-question family:

> 항암제 내성 proteogenomics 연구에서 발견되는 protein/phosphosite marker를 baseline primary resistance, therapy-emergent acquired resistance, adaptive tolerance, refractory-state marker로 구분하려면 어떤 데이터 구조와 검증 기준이 필요한가?

## Connections

- [Cancer Multiomics Presentation Storyline](./cancer-multiomics-presentation-storyline.md)
- [Cancer Multiomics Presentation Capture Board](./cancer-multiomics-presentation-capture-board.md)
- [Cancer Multiomics Resistance Biomarker Question Chain](./cancer-multiomics-resistance-biomarker-question-chain.md)
- [Cancer Multiomics Resistance Biomarker Evidence Boundary Map](./cancer-multiomics-resistance-biomarker-evidence-boundary-map.md)
- [Primary and Acquired Resistance Proteogenomics Ingest Map](./primary-acquired-resistance-proteogenomics-ingest-map.md)

## Sources

- Local wiki pages linked above.
- `Advanced_Genetics_Zoom_Summary_2026-05-19.pdf` was used as a format reference for what "LLM-use rules" mean in this class: each presenter had personal constraints, routines, and node-building practices. The content and rules here are specific to this user's Cancer Multiomics project.
