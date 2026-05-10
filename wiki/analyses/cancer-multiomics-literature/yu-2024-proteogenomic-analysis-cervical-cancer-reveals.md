# Yu 2024 - Cervical Cancer Proteogenomics (Phospho + Acetyl + Radioresponse)

## 논문 정보 (저자 / 저널 / DOI / Wiki 경로)

- 저자: Yu, Gui, Zou et al.
- 저널/연도: Nature Communications, 2024
- DOI: 10.1038/s41467-024-53830-0
- Wiki 경로: [A proteogenomic analysis of cervical cancer reveals therapeutic and biological insights](../../sources/yu-2024-proteogenomic-analysis-cervical-cancer-reveals.md)

## 한 줄 요약

자궁경부암 139명(중국) 환자에서 WES+RNA-seq+proteome+phosphoproteome+acetylome을 통합해 HPV 관련 변이를 기능적 경로/PTM 상태로 연결하고, 예후·면역·PTM 조절이 다른 proteomic subgroup과 방사선 반응성(radioresponse) 바이오마커 후보를 제시한다.

## 표준 메타데이터

- 치료 맥락: 자궁경부암 표준치료(수술/동시항암방사선치료 등) 맥락에서 radio-resistance/반응성 이질성을 문제로 둔다(세부 치료 라인/반응 라벨은 PDF 확인 필요).
- 데이터 레이어: WES, RNA-seq, proteome(TMT + DIA), phosphoproteome(41,448 phosphosites; 7,721 phosphoproteins), acetylome(5,749 acetylsites; 2,456 acetylproteins) 보고.
- 데이터 공개: Data Availability 기반으로 PRIDE/EGA 등 raw/processed 공개 경로 확인 필요.

## 과제 관련성 (Cancer Multiomics)

- Cancer Multiomics 과제의 “WGS/WES → 단백체/인산화단백체 기능 상태(kinase/pathway) → 예후/치료반응 설명” 흐름을 **acetylome까지 포함해** 확장한 레퍼런스다.
- phosphoproteome/acetylome을 포함한 subgrouping은, Cancer Multiomics에서 “유전변이 동일 군 내 반응성 차이”를 PTM 상태로 설명하는 서사를 강화한다.
- radioresponse biomarker 후보(PRKCB) 제시는, Cancer Multiomics에서 방사선/표적치료 등 치료 class별 반응 feature를 정의할 때 참고할 수 있다.

## 주요 결과

- 139명 자궁경부암 종양(NAT 포함)에서 WES/RNA/proteome/phosphoproteome/acetylome을 통합해 HPV 연관 변화의 multi-omics landscape를 제시한다.
- EP300이 FOSL2-K222 acetylation을 증가시켜 종양 증식에 기여한다는 기전적 축을 제시한다(구체 실험 근거는 PDF의 해당 figure/assay 확인 필요).
- proteomic stratification으로 3개 subgroup을 정의하고, 각 subgroup의 예후/유전변이/면역침윤/PTM 조절 차이를 기술한다.
- PRKCB를 radioresponse 관련 바이오마커 후보로 제시한다(정량 성능/검증 코호트 구성은 PDF 확인 필요).

## Slack 메시지 초안

Yu et al. Nat Commun 2024는 자궁경부암 139명에서 WES+RNA-seq+proteome+phosphoproteome+acetylome을 통합해 HPV 관련 변이를 기능적 경로/PTM 상태로 연결하고, proteomic subgroup(예후/면역/PTM 조절 차이)과 radioresponse 바이오마커 후보(PRKCB)를 제시합니다. Cancer Multiomics 과제의 “WGS만으로 설명되지 않는 반응성 차이”를 phosphoproteome/acetylome feature로 보완하는 분석 설계 레퍼런스로 활용 가능합니다.
