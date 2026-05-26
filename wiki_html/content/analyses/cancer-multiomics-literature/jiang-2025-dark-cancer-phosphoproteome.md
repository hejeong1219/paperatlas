# Jiang 2025 - Dark Cancer Phosphoproteome

## 논문 정보 (저자 / 저널 / DOI / Wiki 경로)

- 저자: Jiang et al.
- 저널/연도: Nature Communications, 2025
- DOI: 10.1038/s41467-025-57993-2
- Wiki 경로: [Deciphering the dark cancer phosphoproteome](../../sources/jiang-2025-dark-cancer-phosphoproteome-coregulation.md)

## 한 줄 요약

pan-cancer phosphoproteomics에서 annotation이 부족한 phosphosite들을 co-regulation network로 묶어 kinase-substrate association 후보를 확장한 machine-learning 연구.

## 표준 메타데이터

- 치료 맥락: pan-cancer phosphoproteomics 기반 방법론/해석 연구; 치료/반응 라벨은 PDF 확인 필요
- 데이터 레이어: phosphoproteomics + network/ML inference (원 데이터의 genomics/proteome 포함 여부는 PDF 확인 필요)
- 데이터 공개: Data Availability 기반으로 PDF 확인 필요

## 과제 관련성 (Cancer Multiomics)

- Cancer Multiomics 과제의 인산화단백체 분석은 phosphosite를 많이 찾는 것에서 끝나지 않고 kinase network와 치료 타깃으로 번역해야 하므로, dark phosphoproteome 해석이 중요하다.
- 기존 database에 없는 phosphosite가 많은 clinical cohort에서 co-regulation 기반 inference를 적용할 수 있는 방향을 제시한다.
- ppQTL 또는 differential phosphorylation 결과를 downstream kinase-substrate hypothesis로 확장하는 데 참고할 수 있다.
- 치료반응 예측 모델에서 phosphosite feature를 pathway/network feature로 요약하는 전략의 후보가 된다.

## 주요 결과

- 1,195 tumor specimen, 11개 cancer type의 phosphoproteomics data로 CoPheeMap phosphosite co-regulation network를 구축했다.
- CoPheeKSA를 통해 conventional motif/database-limited 접근보다 넓은 kinase-substrate association 후보를 예측했다.
- annotation이 부족한 phosphosite와 kinase를 해석 가능한 signaling network로 끌어올리는 framework를 제시했다.
- dark phosphoproteome을 motif matching이 아니라 network learning 문제로 다뤘다.

## Slack 메시지 초안

Jiang et al. Nature Communications 2025는 암 phosphoproteome에서 annotation이 없는 phosphosite들을 co-regulation network로 해석해 kinase-substrate 후보를 넓힌 논문입니다. Cancer Multiomics 과제에서 인산화단백체 데이터를 kinase network와 치료 타깃으로 연결하려면, known substrate database에만 의존하지 않는 이런 dark phosphoproteome 해석 전략이 중요할 수 있습니다.
