# Abelin 2023 - MONTE Serial Multi-Omics (Immunopeptidome + PTM)

## 논문 정보 (저자 / 저널 / DOI / Wiki 경로)

- 저자: Abelin et al.
- 저널/연도: Nature Communications, 2023
- DOI: 10.1038/s41467-023-37547-0
- Wiki 경로: [Workflow enabling deepscale immunopeptidome, proteome, ubiquitylome, phosphoproteome, and acetylome analyses of sample-limited tissues](../../sources/abelin-2023-workflow-enabling-deepscale-immunopeptidome-proteome.md)

## 한 줄 요약

하나의 제한된 조직 샘플에서 HLA immunopeptidome과 ubiquitome/proteome/phosphoproteome/acetylome을 **직렬(serial)로 깊게 측정**하는 MONTE 워크플로를 제시한다.

## 과제 관련성 (Cancer Multiomics)

- Cancer Multiomics 코호트에서 **샘플이 제한된 상황에서** WGS·인산화단백체·면역항원(neoantigen)까지 같은 샘플로 최대한 연결하려면, MONTE 같은 serial multi-omics 설계가 직접적인 레퍼런스가 된다.
- “WGS 후보 생성 → 실제 제시되는 항원(면역펩티돔) evidence → kinase signaling(인산화단백체)”를 한 흐름으로 묶는 실험 설계 방향성을 제공한다.
- 향후 **CPTAC/Baylor 협업** 등에서 immunopeptidomics를 포함한 종합 측정이 가능할 때, 파이프라인/실험 단계 설계 체크리스트로 활용 가능하다.

## 주요 결과

- HLA-I/HLA-II immunopeptidome capture를 먼저 수행한 뒤, 동일 샘플에서 UbiFast → proteome → phosphoproteome(IMAC) → acetylome(PTMScan)로 이어지는 serial workflow를 제시한다.
- 직렬화(serialization)가 PTM readout의 depth/정밀도를 크게 희생하지 않는다는 실험적 근거를 제시한다.
- workflow 검증(폐선암 조직/PDX)에서 immunopeptidomics를 포함한 multi-PTM 동시 수집이 가능함을 보여준다.

## Slack 메시지 초안

Abelin et al. Nat Commun 2023는 제한된 조직 샘플에서 HLA immunopeptidome과 ubiquitome/proteome/phosphoproteome/acetylome을 같은 샘플로 직렬 측정하는 MONTE 워크플로를 제시합니다. Cancer Multiomics 과제에서 WGS 기반 후보(neoantigen)와 실제 제시되는 항원 evidence, 그리고 kinase signaling(인산화단백체)을 한 흐름으로 연결하려면 이런 serial multi-omics 설계가 중요한 레퍼런스가 될 수 있습니다.

