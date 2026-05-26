# Satpathy 2021 - LSCC Proteogenomic Portrait (WGS/WES + Multi-PTM + Immune)

## 논문 정보 (저자 / 저널 / DOI / Wiki 경로)

- 저자: Satpathy, Krug, Jean Beltran et al.
- 저널/연도: Cell, 2021
- DOI: 10.1016/j.cell.2021.07.016
- Wiki 경로: [A proteogenomic portrait of lung squamous cell carcinoma](../../sources/satpathy-2021-proteogenomic-portrait-lung-squamous-cell.md)

## 한 줄 요약

LSCC 종양 108개(및 NAT 99개)에서 **WGS/WES + multi-PTM(proteome/phospho/acetyl/ubiquityl)**을 통합해 분자 아형과 면역 조절 축을 정리하고, FGFR1 amplicon의 driver 후보(NSD3), CDK4/6 inhibitor 반응을 설명할 기능적 biomarker로서의 Rb phosphorylation 등 “유전-기능 상태” 연결 지점을 제시한다.

## 표준 메타데이터

- 치료 맥락: 수술 기반 LSCC 코호트(치료 반응 라벨보다는 분자 아형/취약성 탐색 중심; 세부 포함 기준은 PDF 확인 필요).
- 데이터 레이어: WGS/WES, RNA-seq, DNA methylation, proteome, phosphoproteome, acetylome, (subset) ubiquitylome 등 multi-omic/PTM.
- 데이터 공개: CPTAC/관련 레포지토리 공개 범위 및 raw/processed 접근 경로는 PDF 확인 필요.

## 과제 관련성 (Cancer Multiomics)

- Cancer Multiomics의 목표(“WGS만으로 설명되지 않는 치료 반응성/내성 차이”를 phosphoproteome/kinase network로 설명)와 유사하게, **유전 변이→protein/PTM 기능 상태**로 번역하는 구체적 분석 예시를 제공한다.
- CDKN2A/RB1 축을 “변이 유무”가 아니라 **Rb protein 및 phosphorylation 상태**로 재평가하는 논리는, Cancer Multiomics에서 표적치료/면역치료 반응 feature를 설계할 때 바로 재사용 가능하다.
- multi-PTM(특히 phospho/acetyl/ubiquityl) crosstalk와 면역 조절 관찰을 포함해, “genome + PTM + immune” 통합 서사의 reference로 적합하다.

## 주요 결과

- WGS/WES 및 multi-PTM을 포함한 LSCC 대규모 코호트에서 multi-omic clustering을 통해 subtype을 정의하고, EMT 및 phosphoprotein signature 기반 축을 보고한다.
- FGFR1 amplicon(8p11.23) 내에서 FGFR1보다 NSD3(WHSC1L1)가 driver일 수 있다는 proteomics 기반 근거를 제시한다.
- CDK4/6 경로에서는 CDKN2A 변이/메틸화/발현 저하와 RB1 상태를 함께 보며, **phospho-Rb가 CDK4/6 inhibitor 반응성 예측**에 도움이 될 수 있음을 제시한다.
- 면역 관련 proteogenomic 관찰(면역 조절 지점/immune score 연계 등)과 PTM crosstalk(ubiquitylation 포함)을 함께 정리한다.

## Slack 메시지 초안

Satpathy et al. (Cell 2021)은 LSCC 코호트에서 **WGS/WES + proteome/phosphoproteome/acetylome(+ubiquitylome)**을 통합해 분자 아형과 면역 조절 축을 정리한 대표 CPTAC proteogenomics 논문입니다. FGFR1 amplicon의 driver로 NSD3를 제안하고, CDK4/6 경로에서는 “변이 유무”보다 **Rb phosphorylation 같은 기능 상태 biomarker**가 반응성 예측에 중요할 수 있음을 보여줘 Cancer Multiomics의 WGS–인산화단백체 통합 feature 설계에 직접 도움이 됩니다.

