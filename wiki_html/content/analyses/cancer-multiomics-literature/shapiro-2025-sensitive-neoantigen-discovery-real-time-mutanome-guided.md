# Shapiro 2025 - NeoDiscMS (Real-time NGS-guided Immunopeptidomics) for Sensitive Neoantigen Discovery

## 논문 정보 (저자 / 저널 / DOI / Wiki 경로)

- 저자: Shapiro et al.
- 저널/연도: Nature Communications, 2025
- DOI: 10.1038/s41467-025-62647-4
- Wiki 경로: [Sensitive neoantigen discovery by real-time mutanome-guided immunopeptidomics](../../sources/shapiro-2025-sensitive-neoantigen-discovery-real-time-mutanome-guided.md)

## 한 줄 요약

NeoDiscMS는 WES/RNA-seq 기반 후보 리스트를 이용해 **real-time MS acquisition**에서 표적 스캔을 트리거함으로써, 글로벌 depth를 유지하면서도 임상 TAT 제약 하에서 neoantigen/항원 동정 민감도를 끌어올리는 immunopeptidomics 워크플로를 제시한다.

## 표준 메타데이터

- 치료 맥락: 방법/워크플로 논문(임상 적용을 염두에 둔 immunopeptidomics acquisition 설계; 예시로 uveal melanoma lesion 적용 포함)
- 데이터 레이어: WES + RNA-seq(후보 생성) + immunopeptidomics(real-time acquisition) + downstream search/validation
- 데이터 공개: PRIDE(PXD059824) 및 EGA(EGAD50000001422) 등(논문 Data availability 기준)

## 과제 관련성 (Cancer Multiomics)

- Cancer Multiomics 과제에서 WGS 기반 neoantigen 후보를 “실제로 제시되는 peptide”로 확인하려면, **샘플량·시간 제약**이 가장 큰 병목인데, NeoDiscMS는 이 병목을 직접 겨냥한 acquisition 설계(reference)다.
- WGS-only prediction vs immunopeptidomics validation을 병렬로 운영할 때, “sensitivity vs depth”를 어떻게 절충할지(표적 branch + discovery branch) 구체적인 구현 프레임을 제공한다.

## 주요 결과

- 3초 cycle에서 MS1 + targeted branch + discovery(DDA) branch를 분리하고, inclusion list 및 RT window로 scouting scan을 트리거한 뒤 real-time search 조건을 만족하면 high-sensitivity scan을 수행한다.
- discovery branch에서는 wider isolation window와 chimeric-spectrum deconvolution을 활용해 global coverage 손실을 줄인다.
- 논문 서술 기준으로 tumor-associated antigen 동정이 “up to ~20%” 개선되며, uveal melanoma case에서 lesion별로 ~12k–16k 수준의 unique peptide 동정을 보고한다.

## Slack 메시지 초안

Shapiro et al. (Nat Commun 2025)은 NeoDiscMS라는 **real-time NGS-guided immunopeptidomics** acquisition을 제시해, 임상 시간/샘플 제약 하에서도 후보 neoantigen/항원 동정 민감도를 높이는 방법을 보여줍니다(표적 branch + discovery branch 병행). Cancer Multiomics 과제에서 WGS 기반 neoantigen 후보를 immunopeptidomics로 확인하려 할 때 “sensitivity vs depth”를 어떻게 설계할지 구체적인 레퍼런스로 활용할 수 있습니다.

