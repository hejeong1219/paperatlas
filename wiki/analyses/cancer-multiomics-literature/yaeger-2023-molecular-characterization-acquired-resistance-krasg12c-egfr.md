# Yaeger 2023 - Acquired Resistance to KRASG12C–EGFR Inhibition in CRC (ctDNA + ERK/mTOR Switch)

## 논문 정보 (저자 / 저널 / DOI / Wiki 경로)

- 저자: Yaeger, Mezzadra, Sinopoli et al.
- 저널/연도: Cancer Discovery, 2023
- DOI: 10.1158/2159-8290.CD-22-0405
- Wiki 경로: [Molecular Characterization of Acquired Resistance to KRASG12C-EGFR Inhibition in Colorectal Cancer.](../../sources/yaeger-2023-molecular-characterization-acquired-resistance-krasg12c-egfr.md)

## 한 줄 요약

KRASG12C inhibitor + EGFR inhibitor 병용에서 획득내성은 주로 **ERK signaling 억제 실패**로 수렴하며, ctDNA 시계열에서 다수 내성 변이는 저빈도(subclonal)인 반면 **KRASG12C amplification**은 임상 진행과 함께 증가하는 반복 메커니즘으로 보고되고, 치료 중단 후 senescence 및 mTOR 활성화라는 “상태 전환” 취약성이 제안된다.

## 표준 메타데이터

- 치료 맥락: 전이성 대장암에서 KRASG12C–EGFR 병용 치료 후 획득내성(세부 약제/라인/대상 환자 수는 PDF 확인 필요).
- 데이터 레이어: 세포주/PDX + 환자 샘플, ctDNA(연속 혈액 샘플) 기반 변이 추적, 경로 활성(ERK/mTOR) 관련 기능 실험 포함(세부는 PDF 확인 필요).
- 데이터 공개: raw/processed 및 코드 공개 범위는 PDF 확인 필요.

## 과제 관련성 (Cancer Multiomics)

- Cancer Multiomics에서 “획득내성”을 모델링할 때, **정적 snapshot이 아니라 시간축(치료 중·중단·재투여)에서 분자 상태가 전환**됨을 명시적으로 feature화해야 함을 보여준다.
- WGS에서 얻는 변이(CNA/증폭 포함)를 ctDNA로 추적해 내성 메커니즘을 분해하는 접근은, Cancer Multiomics에서 **WGS feature ↔ 치료 반응/내성의 시계열 연결**을 설계하는 reference가 된다.
- phosphoproteomics/kinase signaling 관점에서는, “ERK suppression 회피”와 “mTOR 상승” 같은 **경로 전환 시나리오**를 phospho feature로 어떻게 포착할지(예: ERK target site vs mTOR axis) 질문을 만든다.

## 주요 결과

- 획득내성에서 다양한 putative resistance alteration이 관찰되며, 전반적으로 ERK pathway 억제 실패로 수렴하는 내성 프레임을 제시한다.
- 치료 중 ctDNA 시계열에서 다수 alteration은 저빈도인 반면, KRASG12C amplification이 진행과 함께 증가하는 반복 메커니즘으로 기술된다.
- 약제 중단 후 KRASG12C amplification 관련 내성 세포에서 oncogene-induced senescence가 나타나고, circulating DNA에서 해당 alteration이 빠르게 감소할 수 있음을 보고한다.
- 이 상태에서 약제 재투여는 비효율적이며 mTOR signaling 상승이 동반된다는 관찰을 바탕으로, senescence response를 표적하는 조합 전략 가능성을 제안한다.

## Slack 메시지 초안

Yaeger et al. (Cancer Discovery 2023)은 KRASG12C inhibitor + EGFR inhibitor 병용의 획득내성을 **ctDNA 시계열**과 기능 실험으로 분해한 연구입니다. 내성은 ERK 억제 실패로 수렴하고, KRASG12C 증폭이 진행과 함께 증가하는 반복 메커니즘으로 제시되며, 치료 중단 후 senescence 및 mTOR 상승이라는 “상태 전환” 취약성이 논의됩니다. Cancer Multiomics 과제에서 WGS feature(CNA/증폭 포함)와 phospho/kinase signaling을 시간축 반응/내성과 연결하는 분석 설계에 참고가 됩니다.

