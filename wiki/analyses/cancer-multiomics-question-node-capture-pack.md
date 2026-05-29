---
title: Cancer Multiomics Question Node Capture Pack
tags:
  - analysis
  - presentation
  - capture-pack
  - cancer-multiomics
  - llm-wiki
themes:
  - question-node-capture
  - layer-to-state
  - functional-resistance-state
date: 2026-05-29
status: capture-ready
---

# Cancer Multiomics Question Node Capture Pack

이 페이지는 Advanced Genetics LLM-Wiki 발표에서 교수님 공지사항인 “질문별 위키 노드 캡처”를 처리하기 위한 캡처 지시서다. 전체 HTML graph를 그대로 쓰지 말고, 아래처럼 질문별 중심 노드와 주변 노드만 보이게 캡처한다.

## Key Points

- 발표용 PPT에는 **빈 캡처 자리 + 캡션**을 먼저 넣는 것이 가장 안전하다.
- 실제 캡처는 이 페이지의 `Capture Target`을 따라 HTML 또는 Obsidian local graph에서 찍는다.
- 전체 wiki graph는 쓰지 않는다. B-cell neoantigen, PTM atlas, unrelated source pages가 섞이면 질문 체인이 흐려진다.
- 한 슬라이드에 하나의 질문만 보여준다.
- 캡처 옆 캡션은 항상 `Question -> nodes reopened -> what changed -> next question` 형식으로 둔다.

## Capture Rule For PPT Builder

PPT 제작 AI에게는 다음 옵션을 선택하라고 말한다.

> **1. 빈 캡처 자리 + 캡션**으로 먼저 만들고, 아래 Capture Pack의 캡처 대상 이름을 각 자리 안에 적어둔다. 발표자가 나중에 실제 Obsidian/HTML 스크린샷을 교체한다.

이유:

- 지금 실제 캡처 이미지는 아직 없다.
- HTML 전체 graph는 다른 주제까지 섞여서 발표 의도와 다르다.
- 그래도 각 슬라이드에 어떤 캡처가 들어갈지는 아래처럼 고정할 수 있다.

## What To Capture

### Capture 1. Topic Hub As Starting Point

PPT slide:

- Slide 2. Why LLM-Wiki

Question:

> Cancer multiomics 논문을 단순히 모으면 연구질문이 생기는가?

Capture Target:

- [Cancer Multiomics Proteogenomic Atlas](../topics/cancer-multiomics-literature.md)

Crop:

- Page title
- `Question Runs` section
- Links to question-chain / evidence-boundary / final brief pages

Caption:

> Question -> Cancer multiomics topic hub를 열었다 -> paper list만으로는 연구질문이 되지 않았다 -> 질문별 노드가 필요해졌다.

Avoid:

- 전체 graph 캡처
- unrelated B-cell neoantigen topic nodes

### Capture 2. My LLM-Wiki Rule

PPT slide:

- Slide 3. My LLM-Wiki Rule

Question:

> 나는 LLM-Wiki를 어떤 규칙으로 사용했는가?

Capture Target:

- [Cancer Multiomics PPT Storyline and AI Handoff](./cancer-multiomics-ppt-storyline-and-ai-handoff.md)

Crop:

- `## 3. 최종 LLM-Wiki 활용 규칙`
- Rule sentence: `질문별로 문헌을 다시 묶고, 답변보다 다음 질문을 남긴다.`

Caption:

> Question -> 문헌을 질문별로 다시 묶었다 -> 답을 결론으로 고정하지 않았다 -> 다음 질문을 위키 노드로 남겼다.

### Capture 3. First Broad Question

PPT slide:

- Slide 4. Starting Question

Question:

> Cancer multiomics로 항암제 내성 marker를 찾을 수 있을까?

Capture Target:

- [Cancer Multiomics Resistance Biomarker Question Chain](./cancer-multiomics-resistance-biomarker-question-chain.md)

Crop:

- Page title
- First question / question chain section
- Any table showing broad question -> sub-questions

Caption:

> Question -> resistance biomarker question chain을 만들었다 -> marker라는 말이 너무 넓었다 -> 내성 정의와 readout을 나눠야 했다.

### Capture 4. Layer To State Reframing

PPT slide:

- Slide 5. Reframing

Question:

> WGS, proteome, phosphoproteome은 같은 evidence layer인가, 서로 다른 state readout인가?

Capture Target:

- [Cancer Multiomics Final Presentation Brief](./cancer-multiomics-final-presentation-brief.md)

Crop:

- `## Final Direction`
- `## Question-Derivation Chain`
- Especially Q0-Q3 rows if visible

Caption:

> Question -> final brief에서 질문 변화를 정리했다 -> layer 중심 질문이 흐릿했다 -> 각 layer가 읽는 state를 묻는 질문으로 이동했다.

### Capture 5. Immune-Evasion Sub Thought-Chain

PPT slide:

- Slide 6. Sub Thought-Chain 1

Question:

> 기존 cancer resistance review는 새 질문에 어떻게 연결되는가?

Capture Target:

- [Cancer-Resistance Convergence Framework](../syntheses/resistance-convergence-framework.md)

Crop:

- Page title
- visibility / access / effector dysfunction 관련 부분
- 가능하면 immune-evasion 축이 보이는 section

Caption:

> Question -> 기존 resistance framework를 다시 열었다 -> review 자체를 새로 도출한 척하지 않았다 -> immune-evasion을 functional state 후보로 재배치했다.

### Capture 6. Kinase / Adaptive Signaling Sub Thought-Chain

PPT slide:

- Slide 7. Sub Thought-Chain 2

Question:

> Phosphoproteome은 어떤 내성 상태를 읽는가?

Capture Target:

- [PTM Correction and Kinase Signaling in Cancer Proteomics](../topics/ptm-correction-and-kinase-signaling-in-cancer-proteomics.md)

Crop:

- Page title
- kinase activity / phosphoproteome readout 관련 section
- connections to drug-response or PTM correction nodes if visible

Caption:

> Question -> PTM/kinase 노드를 열었다 -> phosphoproteome은 단순 marker layer가 아니었다 -> adaptive signaling state를 읽는 readout으로 보게 되었다.

### Capture 7. Resistance Definition

PPT slide:

- Slide 8. Resistance Definition

Question:

> 논문들이 말하는 resistance는 같은 뜻인가?

Capture Target:

- [Primary and Acquired Resistance Proteogenomics Ingest Map](./primary-acquired-resistance-proteogenomics-ingest-map.md)

Crop:

- primary / acquired / refractory / adaptive 분류가 보이는 부분
- sampling design table if present

Caption:

> Question -> resistance timing 노드를 열었다 -> 같은 marker라도 primary/acquired/adaptive/refractory 의미가 달랐다 -> 데이터 시간축을 봐야 했다.

### Capture 8. Data Structure As Interpretation Boundary

PPT slide:

- Slide 9. Data Structure As Analysis Design

Question:

> Pre/post, time-course, snapshot 데이터는 각각 무엇을 말할 수 있는가?

Capture Target:

- [Cancer Multiomics Resistance Gap Decision Matrix](./cancer-multiomics-resistance-gap-decision-matrix.md)

Crop:

- decision matrix table
- section explaining why data structure is a sub-question

Caption:

> Question -> gap decision matrix를 만들었다 -> 데이터 부족이 결론이 아니라 해석 가능 범위를 정했다 -> state 질문으로 돌아갔다.

### Capture 9. Functional State Map

PPT slide:

- Slide 10. Functional State Map

Question:

> 위키 확장을 통해 어떤 functional resistance-state 후보가 생겼는가?

Capture Target:

- [Cancer Multiomics Final Presentation Brief](./cancer-multiomics-final-presentation-brief.md)

Crop:

- `## Functional State Map`
- state table

Caption:

> Question -> 기능 상태 후보를 다시 묶었다 -> immune-evasion, kinase/adaptive, DNA-repair/stress, stromal/access-limited state가 생겼다 -> 최종 연구질문을 만들 수 있었다.

### Capture 10. Final Research Question

PPT slide:

- Slide 11. Final Research Question

Question:

> 최종 연구질문은 무엇인가?

Capture Target:

- [Cancer Multiomics PPT Storyline and AI Handoff](./cancer-multiomics-ppt-storyline-and-ai-handoff.md)

Crop:

- `### Q6. 최종 연구질문`
- final research question and hypothesis

Caption:

> Question -> 최종 handoff에서 질문을 고정했다 -> marker discovery가 아니라 functional resistance-state reclassification이 되었다 -> PoC 설계로 이어졌다.

### Capture 11. PoC / Next Step

PPT slide:

- Slide 12. PoC / Next Step

Question:

> WGS, proteome, phosphoproteome만으로 무엇을 확인할 수 있는가?

Capture Target:

- [Cancer Multiomics PPT Storyline and AI Handoff](./cancer-multiomics-ppt-storyline-and-ai-handoff.md)

Crop:

- `## 7. PoC 데이터와 분석 설계`
- analysis table

Caption:

> Question -> 실제 데이터 제약으로 돌아왔다 -> RNA-seq 없이도 WGS/proteome/phosphoproteome의 일치와 어긋남을 볼 수 있다 -> genome-unexplained resistance state를 탐색한다.

## Obsidian Capture Settings

If using Obsidian local graph instead of HTML page screenshot:

- Center node: use the `Capture Target` page.
- Graph depth: 1.
- Filter search terms:
  - `cancer-multiomics`
  - `resistance`
  - `proteogenomics`
  - `phosphoproteomics`
  - `ptm`
- Hide or avoid:
  - `b-cell`
  - `neoantigen` unless the slide is specifically about immune-evasion context.
  - unrelated source pages that clutter the graph.

Recommended crop:

- Capture only the center node and 3-5 nearest related nodes.
- Put the slide question above the screenshot.
- Put the `Question -> nodes -> changed -> next question` caption below the screenshot.

## PPT Placeholder Text

If the PPT is made before screenshots are ready, put this inside each placeholder:

```text
[CAPTURE: <center node title>]
Question:
<one-line question>
Caption:
Question -> nodes reopened -> what changed -> next question
```

## Connections

- [Cancer Multiomics PPT Storyline and AI Handoff](./cancer-multiomics-ppt-storyline-and-ai-handoff.md)
- [Cancer Multiomics Presentation Capture Board](./cancer-multiomics-presentation-capture-board.md)
- [Cancer Multiomics Final Presentation Brief](./cancer-multiomics-final-presentation-brief.md)
- [Cancer Multiomics Resistance Biomarker Question Chain](./cancer-multiomics-resistance-biomarker-question-chain.md)
- [Cancer Multiomics Resistance Gap Decision Matrix](./cancer-multiomics-resistance-gap-decision-matrix.md)

## Sources

- Local wiki pages linked above.
- User instruction that the Advanced Genetics presentation should include question-specific node captures.
