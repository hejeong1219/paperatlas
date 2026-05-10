# Dou 2020 - Endometrial Carcinoma Proteogenomics (WES/WGS + Phospho + Acetyl + Immune)

## 논문 정보 (저자 / 저널 / DOI / Wiki 경로)

- 저자: Dou, Kawaler, Cui et al. (CPTAC)
- 저널/연도: Cell, 2020
- DOI: 10.1016/j.cell.2020.01.026
- Wiki 경로: [Proteogenomic Characterization of Endometrial Carcinoma](../../sources/dou-2020-proteogenomic-characterization-endometrial-carcinoma.md)

## 한 줄 요약

전향적 자궁내막암 95예(및 정상 49예)에서 **WES/WGS + (mi)RNA + DNA methylation + TMT proteome/phosphoproteome/acetylome**을 통합해 POLE/MSI/CNV subtype의 기능 상태를 protein/PTM 수준에서 재정의하고, p53/Wnt 축 및 **MSI에서의 항원제시 결함** 등 면역·치료 타깃 관점의 연결점을 제시한다.

## 표준 메타데이터

- 치료 맥락: 수술/진단 기반 EC 코호트(예후·분자 subtype 및 치료 표적 탐색 중심; ICI 반응 라벨링 연구는 아님).
- 데이터 레이어: WES/WGS, total RNA-seq 및 miRNA-seq, DNA methylation, TMT 기반 proteome + phosphoproteome + acetylome.
- 데이터 공개: CPTAC/관련 레포지토리 공개 범위 및 raw/processed 접근 경로는 PDF 확인 필요.

## 과제 관련성 (Cancer Multiomics)

- Cancer Multiomics에서 “WGS 기반 subtype/driver”를 **protein/phospho/acetyl 기능 상태로 번역**해 반응성·내성을 해석하는 데, 대표적인 multi-omics 설계와 분석 흐름을 제공한다.
- MSI/POLE 같은 고변이 subtype에서도 **항원제시(antigen presentation) 결함**이 병존할 수 있다는 관찰은, Cancer Multiomics에서 “neoantigen 개수”만으로 반응성을 단정하지 않고 HLA/presentation 기능(및 PTM 레이어)까지 포함해야 함을 뒷받침한다.

## 주요 결과

- 95개 종양(83 endometrioid, 12 serous)과 49개 정상 샘플을 대상으로 DNA/RNA/단백체/PTM을 통합해 TCGA 유사 subtype(POLE, MSI, CNV-low, CNV-high)을 기능적으로 비교한다.
- proteome/phosphoproteome 수준에서 somatic driver의 cis/trans 효과를 분석해, 변이 효과가 RNA를 넘어 protein/PTM에서 어떻게 나타나는지 정리한다.
- 광범위한 acetylome 분석을 포함해, Wnt/β-catenin 및 histone acetylation 연결 등 PTM 기반 조절 메커니즘을 제시한다.
- 면역 landscape(neoantigen 관련 특징 포함)와 함께, **MSI에서 항원 처리/제시 결함이 checkpoint blockade 반응을 제한**할 수 있음을 논의한다.

## Slack 메시지 초안

Dou et al. (Cell 2020, CPTAC)은 전향적 자궁내막암 95예에서 **WES/WGS + (mi)RNA + DNAme + TMT proteome/phosphoproteome/acetylome**을 통합해 POLE/MSI/CNV subtype의 기능 상태를 protein/PTM 수준에서 해석한 대표 proteogenomics 논문입니다. 특히 MSI에서도 항원제시 결함이 동반될 수 있다는 관찰은 Cancer Multiomics에서 neoantigen “개수”뿐 아니라 HLA/presentation 기능과 phosphoproteome 신호를 같이 봐야 함을 뒷받침합니다.

