# Qu 2024 - Papillary Thyroid Cancer Recurrence Risk Multi-Omics (Proteome + Phospho + Metabolome)

## 논문 정보 (저자 / 저널 / DOI / Wiki 경로)

- 저자: Qu, Chen, Ma et al.
- 저널/연도: Nature Communications, 2024
- DOI: 10.1038/s41467-024-47581-1
- Wiki 경로: [Integrated proteogenomic and metabolomic characterization of papillary thyroid cancer with different recurrence risks](../../sources/qu-2024-integrated-proteogenomic-metabolomic-characterization-papillary.md)

## 한 줄 요약

중국 PTC 102명에서 WES+RNA-seq+proteome+phospho-proteome+metabolome을 통합해 재발 위험군을 분해하고, BRAF-like/대사형/면역형 등 4개 분자 subtype과 예후·타겟 후보 차이를 제시한다.

## 표준 메타데이터

- 치료 맥락: PTC 재발 위험(ATA risk stratification) 관점의 관찰/예후 분석; 특정 치료 반응 라벨은 중심이 아님(세부는 PDF 확인 필요).
- 데이터 레이어: WES(유전체), RNA-seq(전사체), proteome(3,147 proteins 보고), phospho-proteome(“652”로 요약되는 phospho layer; 정의는 PDF/Methods 확인 필요), metabolome(503 metabolites 보고).
- 데이터 공개: Data Availability 기반으로 raw/processed 및 repository 확인 필요.

## 과제 관련성 (Cancer Multiomics)

- “임상적 이질성(여기서는 재발 위험)”을 genomics만으로 두지 않고 **proteome/phospho/metabolome feature**로 분해하는 구성이라, Cancer Multiomics에서 치료반응/내성 라벨을 다룰 때 설계 레퍼런스로 활용 가능하다.
- 아시아(중국) 코호트 기반 multi-omics subtype 사례로, 한국 코호트에서도 유사한 통합 분석을 제안할 때 배경 근거로 쓸 수 있다.

## 주요 결과

- 102명 PTC를 재발 위험군(저/중/고)으로 나누고, multi-omics 통합으로 4개 분자 subtype(CS1–CS4)을 정의한다(저위험 BRAF-like, 고위험 대사형/면역형/ BRAF-like 등).
- 고위험군에서 TERT promoter mutation 및 RET fusion 등 특정 genomic event enrichment를 보고한다(정확한 수치/검정은 PDF 확인 필요).
- subtype별로 metabolism/immune pathway profile과 임상 변수(재발/예후) 차이를 연결해, 기능 상태 기반 환자 분류 프레임을 제공한다.

## Slack 메시지 초안

Qu et al. Nat Commun 2024는 PTC 102명에서 WES+RNA-seq+proteome+phospho-proteome+metabolome을 통합해 재발 위험을 4개 분자 subtype으로 재구성하고(대사형/면역형 고위험군 등), 예후 및 타겟 후보 차이를 제시합니다. Cancer Multiomics 과제에서 “WGS만으로 설명되지 않는 임상 이질성”을 proteome/phospho feature로 설명하는 분석 설계 레퍼런스로 참고할 수 있습니다.
