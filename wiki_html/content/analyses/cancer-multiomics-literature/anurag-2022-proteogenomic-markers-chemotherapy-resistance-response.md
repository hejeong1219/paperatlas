# Anurag 2022 - TNBC Neoadjuvant Chemo Response (WES + Phosphoproteome)

## 논문 정보 (저자 / 저널 / DOI / Wiki 경로)

- 저자: Anurag et al.
- 저널/연도: Cancer Discovery, 2022
- DOI: 10.1158/2159-8290.CD-22-0200
- Wiki 경로: [Proteogenomic Markers of Chemotherapy Resistance and Response in Triple-Negative Breast Cancer](../../sources/anurag-2022-proteogenomic-markers-chemotherapy-resistance-response.md)

## 한 줄 요약

TNBC neoadjuvant carboplatin+docetaxel에서 pCR vs non-pCR을 WES·RNA-seq·TMT proteome/phosphoproteome으로 분해하고, 19q13 결실(LIG1/POLD1/XRCC1) 등 내성 연관 신호를 제시한다.

## 표준 메타데이터

- 치료 맥락: TNBC neoadjuvant carboplatin+docetaxel; endpoint는 pCR 및 RCB
- 데이터 레이어: WES(~100×) + RNA-seq + TMT proteomics + phosphoproteomics (동일 biopsy 기반)
- 데이터 공개: Data Availability 기반으로 PDF 확인 필요

## 과제 관련성 (Cancer Multiomics)

- Cancer Multiomics 과제에서 가장 바로 쓰일 수 있는 형태의 레퍼런스: **임상 반응 라벨(pCR/non-pCR)**이 있고, 동일 바이옵시에서 WES+phosphoproteome feature를 동시에 다룬다.
- “WGS/WES 변이/SCNA + phosphoproteome-driven pathway/kinase feature”를 결합해 반응 예측/내성 해석을 설계할 때, feature 정의와 보고 방식(예: PTM-SEA 같은 요약) 측면에서 직접적인 힌트를 준다.

## 주요 결과

- pCR과 연관된 생물학적 프로그램으로 DNA repair, E2F, G2–M checkpoint, IFN-γ/immune-checkpoint 관련 신호를 언급한다.
- 내성과 연관된 유전체 신호로 19q13.31–33 결실(LIG1/POLD1/XRCC1)을 강조하고, chromosomal instability 및 carboplatin-selective resistance와의 연결을 논의한다.
- 측정 스케일(논문 본문 수치): proteome은 ~11,063 proteins, phosphoproteome은 ~27,000 phosphorylation sites(~5,000 phosphoproteins)를 언급한다.

## Slack 메시지 초안

Anurag et al. Cancer Discovery 2022는 TNBC neoadjuvant carboplatin+docetaxel에서 pCR vs non-pCR을 WES·RNA-seq·TMT proteome/phosphoproteome으로 통합 분석한 논문입니다. Cancer Multiomics 과제에서도 임상 반응 라벨과 WGS(WES) 이벤트를 인산화단백체 기반 pathway/kinase feature로 번역해 예측/내성 모델을 설계할 때 직접적인 레퍼런스로 활용할 수 있습니다(예: 19q13 결실 신호, PTM-SEA 기반 요약).

