# Wen 2020 - NeoFlow Proteogenomic Neoantigen Prioritization

## 논문 정보 (저자 / 저널 / DOI / Wiki 경로)

- 저자: Wen, Li, Zhang et al.
- 저널/연도: Nature Communications, 2020
- DOI: 10.1038/s41467-020-15456-w
- Wiki 경로: [Cancer neoantigen prioritization through sensitive and reliable proteogenomics analysis](../../sources/wen-2020-cancer-neoantigen-prioritization-through-sensitive.md)

## 한 줄 요약

proteogenomics 기반 variant peptide QC와 retention-time prediction을 이용해 neoantigen 후보를 더 신뢰도 있게 우선순위화하는 NeoFlow workflow 논문.

## 표준 메타데이터

- 치료 맥락: workflow/method 중심; 적용된 cohort/임상 맥락은 PDF 확인 필요
- 데이터 레이어: (genomic variant) + proteomics/proteogenomics 기반 variant peptide QC; immunopeptidomics 포함 여부는 PDF 확인 필요
- 데이터 공개: Data Availability 기반으로 PDF 확인 필요

## 과제 관련성 (Cancer Multiomics)

- 과제 문서에서 직접 언급되는 NeoFlow의 기반 논문으로, WGS 기반 neoantigen 후보를 단백체 evidence와 QC로 좁히는 논리의 출발점이다.
- RNA 데이터가 제한적이거나 WGS/HLA 중심으로 후보를 만들 때, peptide detectability와 false-positive control을 어떻게 보완할지 참고할 수 있다.
- NetMHCpan, PepQuery, immunopeptidome database와 연결되는 후보 검증 전략을 설계하는 데 필요하다.
- 신생항원 후보를 면역항암제 타깃/biomarker 후보로 제시하기 전에 proteogenomic reliability를 확보해야 한다는 메시지를 준다.

## 주요 결과

- AutoRT retention-time prediction을 활용해 variant peptide identification의 QC 기준을 평가했다.
- 287 tumor sample, 3개 cancer dataset을 통해 QC 전략에 따라 identified variant peptide와 putative neoantigen 수가 크게 달라질 수 있음을 보였다.
- NeoFlow workflow를 통해 proteogenomics 기반 neoantigen prioritization을 표준화하려 했다.
- prediction-only neoantigen list보다 proteomic evidence를 통합한 후보 우선순위가 더 신뢰도 높다는 framework를 제시한다.

## Slack 메시지 초안

Wen et al. Nature Communications 2020은 NeoFlow의 기반 논문으로, WGS에서 나온 변이 peptide 후보를 proteogenomics evidence와 retention-time QC로 검증해 neoantigen 우선순위를 정하는 방법을 제시합니다. Cancer Multiomics 과제의 WGS 기반 신생항원 파이프라인에서 false-positive 후보를 줄이고, 면역치료 타깃으로 연결 가능한 후보를 선별하는 기준점으로 쓸 수 있습니다.
