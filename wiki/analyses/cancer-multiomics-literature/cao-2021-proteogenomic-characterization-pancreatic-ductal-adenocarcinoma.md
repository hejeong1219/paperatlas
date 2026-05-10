# Cao 2021 - PDAC CPTAC Proteogenomics (WGS/WES + Phospho + Glyco)

## 논문 정보 (저자 / 저널 / DOI / Wiki 경로)

- 저자: Cao, Li, Zhang et al. (CPTAC)
- 저널/연도: Cell, 2021
- DOI: 10.1016/j.cell.2021.08.023
- Wiki 경로: [Proteogenomic characterization of pancreatic ductal adenocarcinoma](../../sources/cao-2021-proteogenomic-characterization-pancreatic-ductal-adenocarcinoma.md)

## 한 줄 요약

PDAC 140건(67 NAT + 9 정상 duct)에서 proteome/phosphoproteome/glycoproteome과 WGS/WES·methylation·RNA/miRNA를 같은 샘플에서 통합해, 유전 이벤트가 단백질·PTM 신호 및 signaling 경로로 번역되는 양상을 리소스 형태로 제시한다.

## 표준 메타데이터

- 치료 맥락: 수술 기반 PDAC 코호트(치료 전; treatment-naive) 중심.
- 데이터 레이어: WGS + WES + methylation + RNA-seq + miRNA-seq + proteome + phosphoproteome + glycoproteome.
- 데이터 공개: proteomics raw/processed는 PDC, genomics/epigenomics/transcriptomics는 GDC, processed table은 PDC/LinkedOmics(CPTAC-PDAC)로 제공(상세 accession은 PDF Data and code availability 참조).

## 과제 관련성 (Cancer Multiomics)

- Cancer Multiomics의 핵심인 **WGS–인산화단백체 통합**을 “동일 샘플에서의 측정 기반”으로 수행한 CPTAC 리소스라, 변이/복제수/메틸화/전사체로 설명되지 않는 기능 상태를 phosphoproteome으로 보완하는 분석 프레임을 제공한다.
- **tumor purity/세포성 평가를 다중 전략으로 수행**한 점은, WGS feature와 phosphoproteome feature를 결합할 때 전처리·QC 체크리스트(표본 필터링/보정)를 설계하는 데 직접 참고 가능하다.

## 주요 결과

- 140 pancreatic cancers(주로 PDAC) + 67 NAT + 9 정상 ductal tissue에서 multi-omics를 통합해 proteogenomic resource를 구축한다.
- proteome/phosphoproteome/glycoproteome과 WGS/WES, methylation, RNA/miRNA를 같은 조직에서 측정해, genomic alteration의 단백질/신호전달/PTM 영향 평가를 목표로 한다.
- STAR Methods에 kinase/substrate co-regulation, multi-omics clustering, epithelial content adjustment, TME inference 등이 포함되어(정량/모형은 PDF 확인 필요) Cancer Multiomics 파이프라인 설계에 재사용 가능하다.

## Slack 메시지 초안

Cao et al. Cell 2021은 PDAC 140건(67 NAT + 9 정상 duct)에서 WGS/WES·methylation·RNA/miRNA와 proteome/phosphoproteome/glycoproteome을 동일 샘플에서 통합해 “유전 이벤트→단백질/인산화 기능 상태” 번역을 해석할 수 있는 CPTAC 리소스를 제공합니다. Cancer Multiomics 과제의 WGS-인산화단백체 통합 모델(반응/내성 feature 설계)에서 purity/QC와 multi-omics clustering 프레임을 그대로 참고할 수 있는 핵심 reference입니다.
