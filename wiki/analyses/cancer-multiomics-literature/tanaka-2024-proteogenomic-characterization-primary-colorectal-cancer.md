# Tanaka 2024 - CRC Primary vs Liver Metastasis Proteogenomics (Hypoxia / Stemness / Immune-cold)

## 논문 정보 (저자 / 저널 / DOI / Wiki 경로)

- 저자: Tanaka, Ogawa, Zhou et al.
- 저널/연도: Cell Reports, 2024
- DOI: 10.1016/j.celrep.2024.113810
- Wiki 경로: [Proteogenomic characterization of primary colorectal cancer and metastatic progression identifies proteome-based subtypes and signatures](../../sources/tanaka-2024-proteogenomic-characterization-primary-colorectal-cancer.md)

## 한 줄 요약

원발 대장암(154)과 간 전이암(142)을 대규모 proteogenomics로 비교해, 전이 진행에서 hypoxia/대사 재배선, stemness(ALT 포함), immune-cold(항원제시 억제) 시그니처가 강화되는 subtype 축을 제시한다.

## 표준 메타데이터

- 치료 맥락: 원발 vs 전이 진행(progression) 자체를 주요 축으로 두는 비교 연구(치료 반응 라벨 중심은 아님).
- 데이터 레이어: 일부 환자(16 triplets)에서 whole genomes + transcriptomes + proteomes; 전체 코호트에서는 deep proteome 중심 + 많은 샘플에서 MSK-IMPACT(타깃 패널) 기반 genomics annotation.
- 데이터 공개: Data Availability 기반으로 raw/processed 공개 여부 확인 필요.

## 과제 관련성 (Cancer Multiomics)

- Cancer Multiomics 과제에서 “WGS feature(예: SV/CNA/WGD 등) + proteome/PTM feature + 면역 feature”로 반응성/내성을 설명하려면, 진행/전이에서 **항원제시 억제(immune evasion)** 같은 면역 축을 결과 변수/설명 변수로 포함시키는 설계가 중요해진다. 본 논문이 그 축을 명확히 보여준다.
- 전이 진행에서 hypoxia/stemness/immune-cold 시그니처가 함께 움직이는 프레임은, phosphoproteome 기반 signaling 해석과 결합해 “전이-내성 program”을 정의할 때 참고할 수 있다.

## 주요 결과

- pCRC 154, 간 mCRC 142, 정상 colon 78, 정상 liver 14를 통합 multi-omics로 분석한다.
- proteome 기반으로 primary/metastasis 각각 3개 subtype(총 6개)을 정의하고, hypoxia/stemness/immune 시그니처가 이를 설명하는 축으로 제시된다.
- metastasis에서 hypoxia 시그니처(대사 재편)와 stemness 시그니처(ALT feature)가 강화된다고 기술한다.
- immune-cold subtype에서 MHC I/II 및 antigen processing 경로 억제가 두드러지며, 특히 metastasis에서 더 강하다고 보고한다.

## Slack 메시지 초안

Tanaka et al. Cell Reports 2024는 원발 CRC(154)와 간 전이암(142)을 proteogenomics로 비교해, 전이 진행에서 hypoxia/대사 재배선, stemness(ALT 포함), immune-cold(항원제시 억제) 시그니처가 강화되는 subtype 축을 제시합니다. Cancer Multiomics 과제에서 전이·내성 프로그램을 정의할 때, WGS/SV/CNA feature와 proteome(및 가능하면 phosphoproteome) feature를 함께 두고 “항원제시 억제” 같은 면역회피 축을 모델 변수로 포함시키는 근거 레퍼런스로 활용 가능합니다.
