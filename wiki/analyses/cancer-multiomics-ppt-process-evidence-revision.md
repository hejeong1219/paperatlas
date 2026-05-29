---
title: Cancer Multiomics PPT Process Evidence Revision
tags:
  - analysis
  - presentation
  - revision
  - llm-wiki
  - cancer-multiomics
themes:
  - process-evidence
  - node-growth
  - question-chain
  - layer-to-state
date: 2026-05-29
status: revision-ready
---

# Cancer Multiomics PPT Process Evidence Revision

이 문서는 `cancer-multiomics-llm-wiki-presentation.pptx`를 LLM-Wiki 활용 발표답게 고치기 위한 수정 지시서다. 현재 PPT는 biological storyline은 좋지만, LLM-Wiki를 실제로 어떻게 굴렸는지의 흔적이 약하다. 따라서 앞부분에 `질문 -> 같은 문헌의 재분류 -> 노드 생성 -> 다음 질문`의 작업 과정을 더 명확히 넣는다.

## Diagnosis

현재 PPT의 장점:

- `layer-centered marker discovery -> state-centered resistance interpretation` 흐름이 선명하다.
- 최종 연구질문과 가설이 비교적 잘 들어가 있다.
- 질문별 캡처 placeholder가 있다.

현재 PPT의 약점:

- 캡처 자리가 많지만 실제로 어떤 노드가 어떻게 자랐는지의 작업 증거가 아직 약하다.
- 앞부분이 “LLM-Wiki 활용 과정”보다 “잘 정리된 cancer multiomics 발표”처럼 보일 수 있다.
- 여진 발표자료의 강점이었던 “토론이 노드가 되고, 노드가 연결되고, 가설이 자란 흔적”이 덜 보인다.

## Revision Principle

PPT의 핵심 메시지를 다음처럼 조정한다.

> 저는 LLM-Wiki를 답을 얻는 도구로 쓰기보다, 같은 논문을 질문이 바뀔 때마다 다시 묶어 보면서 연구질문을 키우는 도구로 사용했습니다.

Cancer multiomics에 적용한 버전:

> 같은 논문들을 layer별로만 모으지 않고, 질문이 바뀔 때마다 resistance definition, timing, readout, state 후보로 다시 묶었다.

One-line rule:

> **같은 논문, 다른 좌표계.**

Cancer multiomics version:

> **Layer로 모은 문헌을 State 좌표계로 다시 배치하기.**

## Slide-Level Revision

### Slide 1. Keep

현재 title slide는 유지한다.

Optional small subtitle:

> LLM-Wiki를 통해 paper list가 question chain으로 바뀐 과정

### Slide 2. Replace With Process Framing

Current:

> 논문 요약보다 질문 변화가 중요했다.

Revise to:

> **같은 논문, 다른 좌표계**

Message:

> 같은 cancer multiomics 문헌을 처음에는 layer별로 모았지만, 질문이 바뀌면서 resistance definition, timing, readout, state 후보라는 다른 좌표계로 다시 배치했다.

Visual:

```text
Same paper set
    -> Layer question
    -> Resistance-definition coordinate
    -> Timing/data-structure coordinate
    -> Readout coordinate
    -> Functional-state coordinate
```

Use actual node names:

```text
Cancer Multiomics Proteogenomic Atlas
    -> Resistance Biomarker Question Chain
    -> Evidence Boundary Map
    -> Gap Decision Matrix
    -> Final Presentation Brief
    -> Question Node Capture Pack
```

Speaker line:

> 저는 논문을 저장하기 위해서만 위키를 쓴 것이 아니라, 같은 문헌이 질문에 따라 어떻게 다르게 묶이는지를 보기 위해 썼습니다.

### Slide 3. Make The Rule Operational

Current:

> 질문별로 다시 묶고, 다음 질문을 남긴다.

Keep the rule, but add concrete operating rules:

1. 문헌을 계속 추가하기 전에, 먼저 같은 문헌 묶음을 고정한다.
2. LLM에게 같은 문헌을 서로 다른 좌표계로 다시 배열하게 한다.
3. 각 좌표계가 문헌을 어떻게 다르게 나누는지 비교한다.
4. 가장 의미 있게 문헌을 갈라놓는 좌표계를 연구질문 후보로 올린다.
5. topic hub에는 최종 답보다 좌표계가 바뀐 경로를 남긴다.

Add one line to avoid sounding generic:

> 노드 종류를 많이 늘리기보다, 같은 문헌 묶음이 어떤 좌표계에서 가장 잘 갈라지는지를 보았다.

### New Slide 4. Show Actual Node Growth

Insert or replace current Slide 4 with a process-evidence slide.

Title:

> **질문이 노드로 자란 실제 경로**

Visual:

```text
Q0. 내성 marker를 찾을 수 있을까?
  -> cancer-multiomics-resistance-biomarker-question-chain.md

Q1. 이 marker는 어떤 resistance를 말하나?
  -> cancer-multiomics-resistance-biomarker-evidence-boundary-map.md

Q2. 어떤 gap을 발표 중심으로 삼을까?
  -> cancer-multiomics-resistance-gap-decision-matrix.md

Q3. 최종 질문은 layer인가 state인가?
  -> cancer-multiomics-final-presentation-brief.md

Q4. 발표에서 어떤 노드를 캡처할까?
  -> cancer-multiomics-question-node-capture-pack.md
```

Key message:

> 이 발표의 결과는 논문 요약 목록이 아니라, 같은 문헌 묶음을 다른 좌표계로 재배치하면서 생긴 wiki node들의 체인이다.

This slide is essential. It is the closest equivalent to Yeojin's “question page / hypothesis page / cross-link” evidence.

### Slide 5. Move Current Starting Question Here

Current Slide 4 content can become Slide 5:

> 처음 질문: multiomics로 내성 marker를 찾을 수 있을까?

Add process note:

> 이 질문은 `Question Chain` 노드로 고정했고, 이후 follow-up에서 내성 정의 / 데이터 시간축 / readout 질문으로 쪼개졌다.

### Slide 6. Layer To State

Keep current layer-to-state slide.

Small wording change:

- Replace `evidence layer` with `정보 단위` or `readout`.

Recommended sentence:

> WGS, proteome, phosphoproteome은 같은 정보 단위가 아니라 서로 다른 state readout이다.

### Slide 7-10. Keep Biological State Story

Keep:

- Immune-evasion state
- Kinase/adaptive-signaling state
- Resistance definitions
- Data structure as interpretation boundary
- Functional state map

But each slide should contain one small process tag:

```text
Wiki action: reopened [node name] -> added this as a state/readout question
```

Example for immune-evasion slide:

> Wiki action: reopened `Cancer-Resistance Convergence Framework` -> moved immune-evasion from previous review into the state map.

Example for kinase slide:

> Wiki action: reopened `PTM Correction and Kinase Signaling` -> reframed phosphoproteome as adaptive-signaling readout.

### Slide 11. Final Research Question

Keep, but replace:

> 유전체 변이만으로 설명되지 않는

with:

> WGS 변이와 단순 대응되지 않는

Reason:

- Avoids sounding like “genomics is insufficient.”
- Keeps the focus on readout/state mismatch.

Recommended final question:

> Cancer multiomics readout을 이용해 WGS 변이와 단순 대응되지 않는 항암제 내성을 functional resistance state로 재분류할 수 있는가?

### Slide 12. Next Step

Keep PoC slide.

Add:

> 이 PoC는 위키의 마지막 답이 아니라 다음 질문이다.

This links the ending back to the LLM-Wiki rule.

## Capture Replacement Priority

Do not try to replace every placeholder at once. Replace these first:

1. Slide 2 or 3: actual capture of `Cancer Multiomics Proteogenomic Atlas` Question Runs section.
2. New process slide: actual capture or screenshot strip showing the five generated nodes.
3. Layer-to-state slide: capture of `Cancer Multiomics Final Presentation Brief` Question-Derivation Chain.
4. Functional state map slide: capture of `Functional State Map` section.
5. Final question slide: capture of `Q6. 최종 연구질문` in the handoff page.

Minimum acceptable version:

- 3 real captures + remaining placeholders.

Stronger version:

- 5 real captures + placeholders only for optional supporting slides.

## Comparison To Yeojin Reference

Do not copy Yeojin's exact terms or framing. Only use the reference to remember that the presentation must show actual LLM-Wiki work, not only the final biology story.

| Yeojin reference | This presentation should show |
| --- | --- |
| discussion becomes wiki memory | 같은 문헌 묶음을 질문이 바뀔 때마다 다시 분류 |
| question/hypothesis pages link to papers | question chain nodes link topic hub, source pages, gap map, final brief |
| 60 papers become 7-axis landscape | cancer multiomics papers become functional resistance-state map |
| hypothesis grows through follow-up | marker question grows into layer-to-state research question |

One-sentence parallel:

> 여진 발표가 autism 논문들을 하나의 landscape로 보이게 했다면, 이 발표는 cancer multiomics 문헌을 질문이 바뀔 때마다 다시 묶어 functional resistance-state map으로 옮겨간 과정이다.

## New 12-Slide Spine

Recommended revised order:

1. Title: Layer에서 State로 이동한 질문
2. 나의 규칙: 같은 논문, 다른 좌표계
3. My rule: 같은 문헌 묶음을 여러 분류축으로 다시 배열한다
4. 실제 노드 성장 경로: question-chain -> boundary-map -> gap-matrix -> final-brief -> capture-pack
5. Starting question: multiomics로 내성 marker를 찾을 수 있을까?
6. Reframing: WGS/proteome/phosphoproteome은 서로 다른 state readout
7. Sub thought-chain: immune-evasion state
8. Sub thought-chain: kinase/adaptive-signaling state
9. Resistance definitions: primary/acquired/adaptive/refractory
10. Data structure: interpretation boundary
11. Functional resistance-state map + final research question
12. PoC / next question

If slide count must stay 12, combine the current Slide 10 state map and current Slide 11 final question into one slide.

## Exact Prompt For PPT-Editing AI

```text
현재 PPT는 biological storyline은 좋지만, LLM-Wiki를 실제로 어떻게 굴렸는지의 process evidence가 약합니다.

첨부한 cancer-multiomics-ppt-process-evidence-revision.md를 따라 PPT를 수정해주세요.

핵심 수정:
1. 앞부분 2-4장을 LLM-Wiki process 중심으로 바꿔주세요.
   단, "외재화" 같은 여진 발표의 표현은 사용하지 말고,
   "같은 논문, 다른 좌표계"를 이 발표의 고유 규칙으로 써주세요.
2. 질문이 실제 wiki node로 자란 경로를 한 장으로 보여주세요:
   Question Chain -> Evidence Boundary Map -> Gap Decision Matrix -> Final Presentation Brief -> Question Node Capture Pack
3. biological story는 유지하되, 각 슬라이드에 "Wiki action: reopened node -> what changed"를 작게 넣어주세요.
4. "evidence layer" 표현은 "readout" 또는 "정보 단위"로 바꿔주세요.
5. "유전체 변이만으로 설명되지 않는"은 "WGS 변이와 단순 대응되지 않는"으로 부드럽게 바꿔주세요.
6. 최소 3개 캡처 자리는 실제 캡처로 교체할 수 있게 크게 남기고, 어떤 노드를 캡처할지 명확히 표시해주세요.

목표는 cancer multiomics 정리 발표가 아니라, LLM-Wiki로 질문이 어떻게 자랐는지 보여주는 발표입니다.
```

## Connections

- [Cancer Multiomics PPT Storyline and AI Handoff](./cancer-multiomics-ppt-storyline-and-ai-handoff.md)
- [Cancer Multiomics Question Node Capture Pack](./cancer-multiomics-question-node-capture-pack.md)
- [Cancer Multiomics Presentation Capture Board](./cancer-multiomics-presentation-capture-board.md)
- [Cancer Multiomics Final Presentation Brief](./cancer-multiomics-final-presentation-brief.md)

## Sources

- Local PPT under `wiki/analyses/cancer-multiomics-llm-wiki-presentation.pptx`.
- Yeojin reference deck downloaded from the user-provided Dropbox link for presentation-logic comparison.
- Local handoff and capture-pack pages linked above.
