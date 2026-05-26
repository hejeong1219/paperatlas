# Krug 2020 - Breast Cancer Proteogenomics (PTM-preserved; HER2/Rb/kinase)

## 논문 정보 (저자 / 저널 / DOI / Wiki 경로)

- 저자: Krug, Jaehnig, Satpathy et al. (CPTAC)
- 저널/연도: Cell, 2020
- DOI: 10.1016/j.cell.2020.10.036
- Wiki 경로: [Proteogenomic Landscape of Breast Cancer Tumorigenesis and Targeted Therapy](../../sources/krug-2020-proteogenomic-landscape-breast-cancer-tumorigenesis.md)

## 한 줄 요약

치료 전(primary) 유방암을 PTM 보존 프로토콜로 수집해(122 fully analyzed) proteome/phosphoproteome/acetylome 기반 proteogenomics로 HER2(ERBB2)·Rb 상태·kinase signaling을 재해석하고, 표준 분류를 넘어서는 치료 취약성/면역 후보를 제시한다.

## 표준 메타데이터

- 치료 맥락: 새로 진단된 untreated 환자 중심(수술 또는 neoadjuvant 전 시점의 샘플 포함; 상세는 PDF 확인 필요).
- 데이터 레이어: WES + RNA-seq + miRNA-seq + proteome + phosphoproteome + acetylome(TMT 기반).
- 데이터 공개: CPTAC study S060, PDC(PDC000120), genomics는 GDC(dbGaP phs000892), processed matrix는 LinkedOmics 제공(세부는 PDF Data and Code Availability).

## 과제 관련성 (Cancer Multiomics)

- Cancer Multiomics에서 WGS 기반 변이/amplicon/TS loss 이벤트를 phosphoproteome 기능 상태로 연결할 때, **유전 이벤트→kinase signaling** 연결을 cohort-scale로 보여주는 reference다.
- HER2, CDK4/6 같은 임상적 의사결정 축을 proteogenomics로 “재정의/정교화”하는 흐름은, Cancer Multiomics에서도 genome-first 가설을 **protein/PTM evidence로 보정**하는 논리로 재사용 가능하다.

## 주요 결과

- 134 participants 중 122 tumors를 fully analyzed proteogenomics로 포함한다(PTM 보존 수집 프로토콜 기반).
- ERBB2 amplicon을 protein/phospho 수준으로 상세 해석하고, 표준 HER2 분류와의 불일치/재분류 가능성을 다룬다.
- Rb status를 proteomics로 더 정확히 평가해 CDK4/6 inhibitor 반응성 추정의 근거로 사용 가능하다고 주장한다.
- phosphoproteomics로 tumor suppressor loss와 targetable kinase 연관을 제시한다.

## Slack 메시지 초안

Krug et al. Cell 2020은 치료 전(primary) 유방암 122건을 PTM 보존 프로토콜로 수집해 proteome/phosphoproteome/acetylome 기반 proteogenomics로 HER2(ERBB2) 상태와 Rb 기능 상태를 재해석하고, tumor suppressor loss-연관 kinase signaling 취약성을 제시합니다. Cancer Multiomics 과제의 WGS-인산화단백체 통합 모델에서 “유전 이벤트→functional signaling state” feature 설계와 임상적 해석(예: targetable pathway 재분류)에 좋은 reference입니다.
