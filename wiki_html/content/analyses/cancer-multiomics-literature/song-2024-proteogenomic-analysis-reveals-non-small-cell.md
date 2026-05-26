# Song 2024 - NSCLC Multi-Omics Subtypes (WGD / PI3K–Akt / TME)

## 논문 정보 (저자 / 저널 / DOI / Wiki 경로)

- 저자: Song, Choi, Kim et al.
- 저널/연도: Nature Communications, 2024
- DOI: 10.1038/s41467-024-54434-4
- Wiki 경로: [Proteogenomic analysis reveals non-small cell lung cancer subtypes predicting chromosome instability, and tumor microenvironment](../../sources/song-2024-proteogenomic-analysis-reveals-non-small-cell.md)

## 한 줄 요약

한국인 NSCLC 229명 코호트에서 WES+RNA-seq+proteome+phosphoproteome+acetylome을 통합해 5개 분자 subtype을 정의하고, WGD(염색체 불안정성), PI3K–Akt signaling, TME/neoantigen load 차이가 예후·adjuvant therapy 효능 신호와 연결됨을 보여준다.

## 표준 메타데이터

- 치료 맥락: 수술 기반 NSCLC 코호트(2010–2019); 일부는 수술 후 adjuvant 치료(화학요법/방사선 등) 시행. 반응 라벨은 “responder/non-responder”가 아니라 예후·치료 효능 신호 중심(세부는 PDF 확인 필요).
- 데이터 레이어: WES(228), bulk RNA-seq(205 tumor + 85 NAT), proteome(229), phosphoproteome, acetylome(TMT 기반); 면역 미세환경 + neoantigen load 비교 포함.
- 데이터 공개: Data Availability 기반으로 raw/processed 및 repository(예: PRIDE, EGA 등) 확인 필요.

## 과제 관련성 (Cancer Multiomics)

- 한국인 코호트에서 **WES + (phospho/acetyl)proteome** 통합으로 “histology보다 기능적 subtype”을 정의한 예시라, Cancer Multiomics의 **WGS-인산화단백체 통합 기반 반응성/내성 해석** 논리를 보강한다.
- WGD/염색체 불안정성과 proteome/PTM 상태를 같이 두는 구성은, Cancer Multiomics에서 **SV/CNA/WGD와 kinase signaling**을 연결하는 feature 설계에 직접 참고 가능하다.
- subtype별 TME/neoantigen load 차이를 같이 보여줘서 “genome-derived immune feature + phosphoproteome” 결합 프레임을 제공한다.

## 주요 결과

- 229명(한국) discovery + 462명 replication multi-omics 데이터를 통합해 5개 분자 subtype을 정의한다.
- PI3K–Akt pathway upregulation subtype은 특정 LUAD/LSCC histology에 국한되지 않으면서 전이 비율과 불량 예후와 연결되는 것으로 기술된다.
- proliferative subtype은 WGD 사건과 강하게 연관된 축으로 제시된다.
- immune microenvironment 조성(침윤)과 neoantigen load가 subtype별로 다르고, immune-hot subtype에서 adjuvant therapy 효능 신호가 더 크다고 서술한다(정량 정의/모형은 PDF 확인 필요).
- cohort-scale phosphoproteome/acetylome(TMT)까지 포함해 kinase/pathway 해석을 RNA만으로 대체하기 어려운 사례로 제시한다.

## Slack 메시지 초안

Song et al. Nat Commun 2024는 한국인 NSCLC 229명 코호트에서 WES+RNA-seq+proteome+phosphoproteome+acetylome을 통합해 5개 분자 subtype을 정의하고, WGD(염색체 불안정성), PI3K–Akt signaling, TME/neoantigen load 차이가 예후 및 adjuvant therapy 효능 신호와 연결됨을 보여줍니다. Cancer Multiomics 과제의 “WGS만으로 설명되지 않는 반응성/내성 차이”를 phosphoproteome/kinase network와 면역 feature로 보완하는 분석 설계의 좋은 reference입니다.
