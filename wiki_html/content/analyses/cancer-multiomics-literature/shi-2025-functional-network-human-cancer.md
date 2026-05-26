# Shi 2025 - Functional Network of Human Cancer

## 논문 정보 (저자 / 저널 / DOI / Wiki 경로)

- 저자: Shi et al.
- 저널/연도: Nature Cancer, 2025
- DOI: 10.1038/s43018-024-00869-z
- Wiki 경로: [Mapping the functional network of human cancer](../../sources/shi-2025-functional-network-human-cancer-proteogenomics.md)

## 한 줄 요약

CPTAC pan-cancer proteomics와 machine learning으로 human cancer functional network를 구축해 protein-level coexpression이 기능 해석에 강력한 정보를 준다는 것을 보인 연구.

## 표준 메타데이터

- 치료 맥락: pan-cancer compendium 기반 network inference; 치료/반응 라벨은 PDF 확인 필요
- 데이터 레이어: proteomics + (RNA-seq 등) + ML/network analysis (세부 레이어는 PDF 확인 필요)
- 데이터 공개: CPTAC 기반(공개 경로는 PDF 확인 필요)

## 과제 관련성 (Cancer Multiomics)

- WGS 변이를 단백체/인산화단백체 feature로 번역한 뒤, 이를 network-level functional interpretation으로 확장하는 데 참고할 수 있다.
- RNA 중심 해석보다 protein-level network가 functional association을 더 잘 설명할 수 있다는 점은 과제의 단백유전체 필요성을 뒷받침한다.
- 치료반응 예측 모델에서 개별 feature보다 network/module-level feature를 구성하는 근거가 된다.
- understudied protein 또는 low-frequency driver를 functional context 안에서 해석하는 방식은 basket-trial molecular grouping과 연결된다.

## 주요 결과

- 1,194명, 11개 cancer type의 CPTAC-era tumor data로 FunMap functional network를 구축했다.
- protein coexpression이 RNA coexpression보다 functional relationship recovery에 더 강한 정보를 제공했다.
- cancer hallmark와 clinical phenotype에 연결되는 functional module을 제시했다.
- low-frequency driver와 understudied cancer-associated protein의 기능 해석을 확장했다.

## Slack 메시지 초안

Shi et al. Nature Cancer 2025는 CPTAC pan-cancer proteomics로 FunMap이라는 cancer functional network를 만든 논문입니다. Cancer Multiomics 과제에서 WGS/인산화단백체 feature를 치료반응 예측 모델에 넣을 때, 단일 gene이나 phosphosite만 보는 것보다 protein network/module feature로 요약하는 전략을 생각해볼 수 있게 해주는 reference입니다.
