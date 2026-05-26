# Zhang 2023 - ccRCC Sunitinib Response Proteogenomics (mTOR / 7q / Classifier)

## 논문 정보 (저자 / 저널 / DOI / Wiki 경로)

- 저자: Zhang et al.
- 저널/연도: Nature Communications, 2023
- DOI: 10.1038/s41467-023-39981-6
- Wiki 경로: [Proteogenomics of clear cell renal cell carcinoma response to tyrosine kinase inhibitor](../../sources/zhang-2023-proteogenomics-clear-cell-renal-response-tyrosine-kinase-inhibitor.md)

## 한 줄 요약

ccRCC 115명에서 sunitinib 반응(RECIST)을 responder/non-responder로 라벨링하고, WES+proteome+phosphoproteome 기반으로 mTOR/7q 축 등 비유전적 기능 상태를 포함해 반응 예측 분류기를 구축한 치료반응 proteogenomics 레퍼런스다.

## 표준 메타데이터

- 치료 맥락: sunitinib TKI 치료; RECIST 기준 responder(CR/PR) vs non-responder(SD/PD)로 구분(27 vs 88).
- 데이터 레이어: WES(n=113), RNA-seq(n=94), proteome(n=115), phosphoproteome(n=66) (모두 main PDF text에 기술).
- 데이터 공개: Data Availability 기반으로 sequencing/proteomics repository(PRIDE/EGA 등) 확인 필요.

## 과제 관련성 (Cancer Multiomics)

- Cancer Multiomics 과제의 목표인 “**WGS/WES로 완전히 설명되지 않는 치료반응 차이**”를 phosphoproteome 기반 signaling(mTOR 등)으로 해석하고, 이를 예측 모델(분류기)로 연결하는 end-to-end 사례다.
- cohort 내 responder/non-responder 라벨이 명확해, 향후 Cancer Multiomics 코호트에서 response prediction model(특히 feature 해석/SHAP 등)을 설계할 때 구조를 그대로 참고할 수 있다.

## 주요 결과

- sunitinib 치료를 받은 ccRCC 115명에서 responder(27)와 non-responder(88)를 비교한다.
- 7q gain 및 mTOR signaling activation이 불량 반응과 연관되는 축으로 기술되고, proteome/phosphoproteome에서 mTOR 관련 신호가 비반응 프로그램으로 강조된다.
- 면역 미세환경 차이를 함께 기술하며, multi-omics 기반 responder/non-responder 분류기를 구축한다(세부 모델/검증은 PDF 확인 필요).

## Slack 메시지 초안

Zhang et al. Nat Commun 2023는 ccRCC 115명에서 sunitinib 반응을 RECIST로 responder/non-responder(27/88)로 라벨링하고, WES+proteome+phosphoproteome을 통합해 mTOR/7q 축 등 기능 상태를 포함한 반응 예측 모델을 제시합니다. Cancer Multiomics 과제에서 WGS(또는 WES)만으로 설명되지 않는 반응성/내성 차이를 phosphoproteome(kinase/pathway) feature로 보완하고, 이를 예측 모델로 연결하는 대표적인 레퍼런스입니다.
