# Scheid 2025 - MHCquant2 (nf-core) Immunopeptidomics Pipeline for Tumor Antigen Discovery

## 논문 정보 (저자 / 저널 / DOI / Wiki 경로)

- 저자: Scheid et al.
- 저널/연도: Genome Biology, 2025
- DOI: 10.1186/s13059-025-03763-8
- Wiki 경로: [MHCquant2 refines immunopeptidomics tumor antigen discovery](../../sources/scheid-2025-mhcquant2-refines-immunopeptidomics-tumor-antigen.md)

## 한 줄 요약

MHCquant2는 nf-core/Nextflow 기반으로 immunopeptidomics를 **재현 가능하게 표준화**하고, DeepLC/MS2PIP 등 peptide-property 기반 rescoring로 동정률을 개선하며, benign reference 구축을 통해 “진짜 tumor-associated antigen” 정의를 더 보수적으로 만드는 방법 레퍼런스다.

## 표준 메타데이터

- 치료 맥락: 방법/소프트웨어 논문(대규모 immunopeptidomics 데이터 처리 및 항원 정의/필터링 프레임)
- 데이터 레이어: immunopeptidomics + pipeline/소프트웨어(Nextflow, OpenMS, rescoring) + benign reference 구축 및 re-analysis
- 데이터 공개: PRIDE PXD058436 및 코드(nf-core/GitHub/Zenodo; 논문 Data/Code availability 기준)

## 과제 관련성 (Cancer Multiomics)

- Cancer Multiomics 과제에서 neoantigen 후보를 immunopeptidomics로 확인할 경우, 분석 파이프라인의 표준화/재현성이 중요하며, **nf-core 기반 구현**은 내부 분석 인프라와의 접점이 크다.
- benign reference를 확장해 TAA를 필터링하는 논리는, 환자군/인종 맥락이 다른 public 데이터만으로 off-tumor 리스크를 과소평가하지 않도록 만드는 “보수적 정의” 프레임으로 활용 가능하다.

## 주요 결과

- nf-core/Nextflow DSL2로 immunopeptidomics identification/quantification을 모듈화하고, DeepLC/MS2PIP 등의 feature를 이용해 동정률을 “up to ~27%” 개선한다고 서술한다.
- benignMHCquant2(n=92) 신규 데이터와 기존 benign dataset 재분석을 결합해 대규모 benign reference(클래스 I/II)를 구축하고, 이를 이용해 tumor antigen discovery에서 TAA 정의를 정교화한다.
- 데이터는 PRIDE(PXD058436)에, 파이프라인은 nf-core/GitHub 및 Zenodo에 버전 관리 형태로 제공한다.

## Slack 메시지 초안

Scheid et al. (Genome Biology 2025)은 immunopeptidomics 처리를 nf-core/Nextflow로 표준화한 MHCquant2를 제시하고, DeepLC/MS2PIP 기반 rescoring로 동정률 향상 및 benign reference 구축을 통한 TAA 정의/필터링 프레임을 제공합니다. Cancer Multiomics 과제에서 immunopeptidomics 기반 neoantigen/항원 검증을 고려한다면, 파이프라인 표준화와 benign reference 활용 전략을 함께 가져갈 수 있는 레퍼런스입니다.

