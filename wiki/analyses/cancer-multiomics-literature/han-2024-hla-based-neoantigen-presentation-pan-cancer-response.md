# Han 2024 - HLA-Based Neoantigen Presentation Score Predicts Pan-Cancer ICI Response

## 논문 정보 (저자 / 저널 / DOI / Wiki 경로)

- 저자: Han et al.
- 저널/연도: Nature Communications, 2024
- DOI: 10.1038/s41467-024-45361-5
- Wiki 경로: [Assessment of human leukocyte antigen-based neoantigen presentation to determine pan-cancer response to immunotherapy](../../sources/han-2024-hla-based-neoantigen-presentation-pan-cancer-response.md)

## 한 줄 요약

neoantigen “개수(TMB)”보다 한 단계 더 나아가 **HLA 매개 제시(presentation) 능력**을 정량화한 점수(HAPS)가 pan-cancer 면역항암제 반응/생존과 연관됨을 보여준다.

## 과제 관련성 (Cancer Multiomics)

- Cancer Multiomics 과제에서 WGS 기반 neoantigen 후보를 반응 예측 feature로 쓰려면, 단순 후보 수가 아니라 **제시 가능성(allele, binding, presentation context)**을 반영하는 지표가 필요하다.
- 인산화단백체/kinase signaling feature와 neoantigen feature를 함께 모델링할 때, neoantigen 쪽 feature를 “presentation-aware”하게 요약하는 방향을 제공한다.
- basket-trial/precision oncology 맥락에서 pan-cancer 공통 biomarker를 설계할 때, HLA 기반 presentation score는 cohort 차이를 넘어 비교 가능한 축이 될 수 있다.

## 주요 결과

- neoantigen–HLA binding과 HLA class I allele divergence를 결합해 HLA tumor-Antigen Presentation Score(HAPS)를 제시한다.
- ICI 치료 pan-cancer 코호트에서 presentation capacity가 높을수록 임상적 benefit(생존/반응)에 유리하다는 연관성을 보고한다.
- presentation capacity가 높은 군에서 항원제시 관련 pathway enrichment 등 면역 미세환경 차이를 함께 해석한다.

## Slack 메시지 초안

Han et al. Nat Commun 2024는 neoantigen “개수(TMB)”가 아니라 HLA 기반 ‘제시(presentation) 능력’을 정량화한 HAPS 점수가 pan-cancer 면역항암제 반응/생존과 연결될 수 있음을 보여줍니다. Cancer Multiomics 과제에서 WGS 기반 neoantigen 후보를 반응 예측 모델에 넣을 때도, 단순 후보 수 대신 presentation-aware feature로 요약하는 방향을 참고할 수 있습니다.

