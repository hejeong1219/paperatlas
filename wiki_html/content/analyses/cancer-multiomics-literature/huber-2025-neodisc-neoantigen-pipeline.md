# Huber 2025 - NeoDisc Proteogenomic Neoantigen Pipeline

## 논문 정보 (저자 / 저널 / DOI / Wiki 경로)

- 저자: Huber et al.
- 저널/연도: Nature Biotechnology, 2025
- DOI: 10.1038/s41587-024-02420-y
- Wiki 경로: [A comprehensive proteogenomic pipeline for neoantigen discovery](../../sources/huber-2025-comprehensive-proteogenomic-pipeline-neoantigen-discovery.md)

## 한 줄 요약

NeoDisc는 genomics, transcriptomics, immunopeptidomics, prioritization logic을 결합해 임상형 personalized neoantigen discovery를 지원하는 end-to-end pipeline이다.

## 표준 메타데이터

- 치료 맥락: 임상형 neoantigen discovery pipeline; 적용 cohort/치료 맥락은 PDF 확인 필요
- 데이터 레이어: genomics + transcriptomics + immunopeptidomics + proteogenomics (세부 입력/출력은 PDF 확인 필요)
- 데이터 공개: code/data availability는 PDF 확인 필요

## 과제 관련성 (Cancer Multiomics)

- Cancer Multiomics 과제의 NeoFlow 기반 신생항원 pipeline을 최신 임상형 proteogenomic neoantigen pipeline과 비교할 수 있는 reference다.
- WGS-only candidate prediction을 넘어서 immunopeptidomics와 noncanonical antigen까지 확장하는 방향을 보여준다.
- 신생항원 후보를 단순 개수로 보고하는 것이 아니라, 임상 적용 가능한 ranking과 validation logic으로 정리해야 한다는 기준을 제공한다.
- Baylor/CPTAC 협력 기반의 neoantigen 분석 고도화와도 자연스럽게 연결된다.

## 주요 결과

- NeoDisc라는 end-to-end proteogenomic workflow를 제시했다.
- canonical mutation-derived neoantigen뿐 아니라 viral, tumor-specific, noncanonical antigen 후보까지 포함한다.
- rule-based와 machine-learning ranking strategy를 모두 활용해 personalized antigen discovery를 지원한다.
- immunopeptidomics evidence를 통합해 실제 제시 가능한 antigen 후보 선별력을 높이는 방향을 제시한다.

## Slack 메시지 초안

Huber et al. Nature Biotechnology 2025는 NeoDisc라는 임상형 proteogenomic neoantigen discovery pipeline을 제시한 논문입니다. Cancer Multiomics 과제에서 WGS/HLA 기반 neoantigen 후보를 만들고 면역치료 바이오마커로 연결하려면, 후보 생성뿐 아니라 immunopeptidomics evidence와 ranking logic이 중요하다는 점을 보여주는 최신 reference로 활용할 수 있습니다.
