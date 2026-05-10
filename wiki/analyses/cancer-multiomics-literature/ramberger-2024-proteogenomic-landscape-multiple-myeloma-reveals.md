# Ramsberger 2024 - Multiple Myeloma Proteogenomics (Nanopore WGS + Phosphoproteome)

## 논문 정보 (저자 / 저널 / DOI / Wiki 경로)

- 저자: Ramsberger et al.
- 저널/연도: Nature Cancer, 2024
- DOI: 10.1038/s43018-024-00784-3
- Wiki 경로: [The proteogenomic landscape of multiple myeloma reveals insights into disease biology and therapeutic opportunities.](../../sources/ramberger-2024-proteogenomic-landscape-multiple-myeloma-reveals.md)

## 한 줄 요약

다양한 질병 단계의 plasma cell malignancy 138개 샘플에서 **nanopore whole-genome DNA sequencing 기반 CNV**와 **TMT proteome/phosphoproteome**, RNA-seq를 통합해 (phospho)proteome의 조절 축과 고위험군 시그니처를 제시하고, genetic lesion만으로는 포착되지 않는 기능 상태 기반의 치료 표적 후보를 정리한다.

## 표준 메타데이터

- 치료 맥락: 다발골수종/형질세포백혈병/전암단계(MGUS) 포함 코호트(치료반응 라벨보다는 baseline biology/예후·risk stratification 중심; 세부 포함 기준은 PDF 확인 필요).
- 데이터 레이어: nanopore WGS(CNV), RNA-seq, TMT 기반 proteome + phosphoproteome(대규모); 일부 follow-up로 기능유전학/단일세포 등 추가(세부는 PDF 확인 필요).
- 데이터 공개: Data availability 및 리소스/코드 공개 범위는 PDF 확인 필요.

## 과제 관련성 (Cancer Multiomics)

- Cancer Multiomics의 핵심 과제(“WGS 축 + 인산화단백체/kinase network 축 통합”)와 동일하게 **WGS(CNA)와 phosphoproteome을 함께 모델링**한 대표 reference라 feature 설계·QC·결측 처리 전략을 역추적하기 좋다.
- genetic lesion과 독립적으로 phosphoproteomic pathway 기반 고위험군을 분리한 사례는, Cancer Multiomics에서 “genome feature가 약한 환자”에서도 **기능 상태(kinase/경로 활성)로 반응/내성을 설명**할 수 있는지 검증하는 비교축이 된다.

## 주요 결과

- 138개 샘플(질병 단계 포함)에서 TMT 기반 글로벌 proteome/phosphoproteome, RNA-seq, nanopore WGS를 통합 분석한다.
- (phospho)proteome이 염색체 수준 변이(CNA 등)와 post-transcriptional regulation 모두의 영향을 받는다는 프레임을 제시한다.
- phosphoproteomics-derived pathway clustering으로 유전 변이와 독립적인 고위험군 아형을 분리하는 결과를 보고한다.
- 예후와 연관된 protein signature 및 잠재 치료 표적(면역치료 포함) 후보를 제시하고, 공개 리소스로 제공한다(정확한 제공 범위는 PDF 확인 필요).

## Slack 메시지 초안

Ramsberger et al. (Nature Cancer 2024)은 plasma cell malignancy 138개 샘플에서 **nanopore WGS(CNV) + TMT proteome/phosphoproteome + RNA-seq**를 통합해, genome 변화만으로 설명되지 않는 (phospho)proteome 기능 상태와 고위험군 시그니처를 제시합니다. Cancer Multiomics 과제의 “WGS–인산화단백체 통합 기반 반응/내성 해석”에서 CNV/SV/WGD feature를 kinase signaling과 연결하는 분석 설계의 좋은 reference입니다.

