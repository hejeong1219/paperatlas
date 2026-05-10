# Muller-Dott 2025 - Benchmarking Kinase Activity Inference from Phosphoproteomics

## 논문 정보 (저자 / 저널 / DOI / Wiki 경로)

- 저자: Muller-Dott et al.
- 저널/연도: Nature Communications, 2025
- DOI: 10.1038/s41467-025-59779-y
- Wiki 경로: [Comprehensive evaluation of phosphoproteomic-based kinase activity inference](../../sources/muller-dott-2025-phosphoproteomic-kinase-activity-inference.md)

## 한 줄 요약

phosphoproteomics에서 kinase activity를 추정하는 방법들을 비교·평가하고, **알고리즘보다 substrate library 선택이 성능을 더 좌우**할 수 있음을 보여주는 벤치마크.

## 과제 관련성 (Cancer Multiomics)

- Cancer Multiomics 과제의 핵심 산출물 중 하나는 phosphosite 변화에서 “해석 가능한 kinase network”로 번역하는 것이므로, kinase activity inference의 신뢰도를 외부 벤치마크로 점검할 근거가 된다.
- cohort 분석에서 coverage가 부족할 때 predicted target(예: NetworKIN) 추가가 도움이 될 수 있다는 관찰은, 임상 코호트의 sparse phosphosite 문제를 다루는 전략 후보가 된다.
- Cancer Multiomics response-prediction 모델에 kinase activity feature를 넣을 때, 어떤 라이브러리/방법 조합을 쓰는 것이 합리적인지 의사결정 프레임을 제공한다.

## 주요 결과

- benchmarKIN(R) 프레임워크로 kinase activity inference 방법 및 substrate library를 비교한다.
- perturbation 데이터와 CPTAC 등 tumor multi-omics 기반 평가를 함께 사용해, 실제 종양 맥락에서의 성능/일관성을 점검한다.
- inference algorithm 자체보다 substrate library의 선택(큐레이션된 자원 vs 확장된 예측 자원)이 결과에 큰 영향을 줄 수 있음을 보고한다.

## Slack 메시지 초안

Muller-Dott et al. Nat Commun 2025는 phosphoproteomics 기반 kinase activity inference 방법/라이브러리를 비교하는 벤치마크 논문입니다. Cancer Multiomics 과제에서 phosphosite 변화를 kinase network/활성도로 번역해 반응 예측에 쓰려면, 알고리즘 선택뿐 아니라 어떤 kinase–substrate 라이브러리를 쓰는지가 결과를 크게 좌우할 수 있다는 점을 확인해주는 좋은 외부 기준입니다.

