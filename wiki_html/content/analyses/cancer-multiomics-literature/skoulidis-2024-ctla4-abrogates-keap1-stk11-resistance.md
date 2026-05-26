---
title: "Skoulidis 2024 - CTLA4 blockade abrogates KEAP1/STK11-related resistance to PD-(L)1 inhibitors"
tags:
  - cancer-multiomics
  - wgs
  - immunotherapy-resistance
  - checkpoint
  - nsclc
  - stk11
  - keap1
---

# Skoulidis 2024 - CTLA4 blockade abrogates KEAP1/STK11-related resistance to PD-(L)1 inhibitors

## 논문 정보 (저자 / 저널 / DOI / Wiki 경로)

- 저자: Skoulidis et al.
- 저널: Nature (2024)
- DOI: 10.1038/s41586-024-07943-7
- Wiki 경로: `wiki/analyses/cancer-multiomics-literature/skoulidis-2024-ctla4-abrogates-keap1-stk11-resistance.md`
- Source page: [CTLA4 blockade abrogates KEAP1/STK11-related resistance to PD-(L)1 inhibitors](../../sources/skoulidis-2024-ctla4-abrogates-keap1-stk11-resistance.md)
- Local PDF: `raw/inbox/papers/skoulidis-2024-ctla4-abrogates-keap1-stk11-resistance.pdf`

## 한 줄 요약

`KEAP1/STK11` 변이로 대표되는 “PD-(L)1 저반응” NSCLC 아형에서, `CTLA-4` 병용(dual ICB)이 면역 병목을 바꿔 임상적 효능을 부분적으로 회복할 수 있음을 임상·전임상·기전 분석으로 제시한다.

## 과제 관련성 (Cancer Multiomics)

- 치료 맥락: advanced nsNSCLC에서 PD-(L)1 기반 chemo-ICI(및 dual ICB) 레짐 맥락의 **유전체 기반 내성 바이오마커 → 조합 전략** 논리 제공.
- 데이터 레이어: 임상(outcome) + 종양 유전체(KEAP1/STK11) + TME 면역세포 조성(특히 myeloid/CD4/CD8) + 유전 스크린/마우스 모델을 함께 사용(“내성 설명”과 “내성 우회”를 같은 프레임에 배치).
- 데이터 공개: PDF 확인 필요 (accession/리포지토리/재현 가능한 분석 산출물 유무를 별도 체크해야 함).

Cancer Multiomics 관점에서의 직접 연결 포인트:

- WGS에서 `STK11/KEAP1` 변이/LOH/공동변이(`KRAS` 동반 등)를 식별한 뒤, **“단독 PD-(L)1 회피”가 아니라 “dual ICB 후보”**로 환자군을 분기할 수 있는지(가설)로 연결 가능.
- 인산화단백체/kinase network와 직접 연결하려면, 이 논문이 제시하는 myeloid reprogramming(iNOS 등) 축이 Cancer Multiomics 데이터에서 **phospho 기반 immune-state feature**로 잡히는지 확인하는 후속 질문으로 확장 가능.

## 주요 결과

- (임상 관찰) KEAP1 변이는 pembrolizumab+chemo(PCP) 맥락에서 불량 예후와 강하게 연관:
  - KEAP1 mutant vs WT: median PFS 2.7 vs 5.7 months, median OS 7.6 vs 16.6 months (figure text 기준).
  - multivariable HR도 PFS/OS 모두 유의하게 악화되는 방향으로 제시됨(figure text 기준; 상세는 source page에 기록).
- (주요 메시지) POSEIDON trial 맥락에서 `durvalumab + tremelimumab`(dual ICB) + chemo가 `STK11`/`KEAP1` 변이 환자군에서 **durvalumab 단독 + chemo 대비 임상적 benefit**을 보였다는 프레이밍을 제시.
- (기전) KEAP1/STK11 변이는 suppressive myeloid predominance + CD8 depletion으로 특징지어지는 불리한 TME와 연결되며, dual ICB는 CD4 effector engagement 및 myeloid compartment의 tumoricidal(iNOS+) 방향 reprogramming을 통해 효능을 만든다고 주장.

## Slack 메시지 초안

KEAP1/STK11 변이 NSCLC에서 PD-(L)1 단독이 약한 이유를 “myeloid 우세 + CD8 감소(상대적으로 CD4 effector는 남아 있음)”로 설명하고, CTLA-4 병용(dual ICB)이 그 병목을 바꿔 효능을 회복할 수 있다는 Nature 2024 논문입니다.

- POSEIDON(trial) 맥락: `durvalumab + tremelimumab` + chemo가 `STK11/KEAP1` 변이군에서 durvalumab 단독 + chemo 대비 benefit 프레이밍
- PCP(펨브롤리주맙+chemo) 관찰: KEAP1 mutant의 PFS/OS가 WT 대비 크게 불량(figure text: PFS 2.7 vs 5.7m, OS 7.6 vs 16.6m)
- Cancer Multiomics 연결: WGS로 STK11/KEAP1 변이군을 잡아 “면역치료 포기”가 아니라 “dual ICB 후보”로 분기하는 전략 가설로 연결 가능

