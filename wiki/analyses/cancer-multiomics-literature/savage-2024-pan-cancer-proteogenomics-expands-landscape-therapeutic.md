# Savage 2024 - Pan-cancer Proteogenomics Therapeutic Target Landscape (CPTAC)

## 논문 정보 (저자 / 저널 / DOI / Wiki 경로)

- 저자: Savage et al.
- 저널/연도: Cell, 2024
- DOI: 10.1016/j.cell.2024.05.039
- Wiki 경로: [Pan-cancer proteogenomics expands the landscape of therapeutic targets](../../sources/savage-2024-pan-cancer-proteogenomics-expands-landscape-therapeutic.md)

## 한 줄 요약

CPTAC pan-cancer(10 cancer types, 1,043 tumors) proteogenomics를 기반으로 “mRNA로는 잘 안 보이는” druggable dependency/synthetic lethality/항원(공유 neoantigen 포함) 후보를 **protein/phosphoprotein 상태**에서 체계적으로 우선순위화하는 타깃 탐색 프레임을 제공한다.

## 표준 메타데이터

- 치료 맥락: 치료반응 라벨링 임상시험이라기보다, treatment-naïve primary tumor 기반의 pan-cancer proteogenomics 리소스 분석(타깃/항원 후보 발굴 중심)
- 데이터 레이어: CPTAC harmonized multi-omics(유전체/전사체 + proteome + phosphoproteome) + 외부 public resources(유전 스크린/약물 반응 등) 통합
- 데이터 공개: CPTAC Data Portal/PDC, GDC, LinkedOmicsKB 및 targets portal(논문 Data and code availability 섹션 기준)

## 과제 관련성 (Cancer Multiomics)

- Cancer Multiomics 과제의 핵심 스토리(WGS 이벤트 → functional state(단백체/인산화단백체) → 표적/조합전략)를, **CPTAC pan-cancer 기반으로 “검증 가능한 분석 흐름”** 형태로 제시한다.
- “유전자 발현이 아니라 protein/phosphoprotein 상태로 표적 후보를 고르는 이유(mRNA–protein mismatch)”를 명시적으로 다루므로, WGS-only 기반 접근의 한계를 설득하는 근거로 쓰기 좋다.

## 주요 결과

- 10개 암종(BRCA, CCRCC, COAD, GBM, HNSCC, LUAD, LSCC, OV, PDAC, UCEC)에서 1,043 tumor를 통합해 druggable protein 세트를 tier로 정리하고, 단백질 abundance 범위와 mRNA–protein correlation 분포를 제시한다.
- tumor proteomics/phosphoproteomics 신호를 DepMap/약물 반응 데이터 등과 결합해 “overexpression/hyperactivation-driven dependency” 후보를 우선순위화한다.
- tumor suppressor gene loss 맥락에서 synthetic lethality 기반의 타깃 후보 탐색 프레임을 제시한다.
- MHC binding prediction 및 proteogenomic context를 이용해 mutant KRAS peptide 등 “공유(public) neoantigen”과 shared tumor-associated antigen 후보를 제시하고, 결과를 포털로 제공한다.

## Slack 메시지 초안

Savage et al. (Cell 2024)은 CPTAC pan-cancer(10 cancer types, 1,043 tumors) proteogenomics를 활용해 druggable dependency/synthetic lethality/항원 후보를 **protein/phosphoprotein 상태**에서 우선순위화하는 타깃 탐색 프레임을 제시합니다. Cancer Multiomics 과제에서도 “WGS 이벤트만으로는 설명되지 않는 치료 반응/내성 차이”를 phosphoproteome/kinase feature로 번역하고, 표적·조합 전략까지 연결하는 논리 구조를 설득하는 데 직접 참고할 수 있습니다.

