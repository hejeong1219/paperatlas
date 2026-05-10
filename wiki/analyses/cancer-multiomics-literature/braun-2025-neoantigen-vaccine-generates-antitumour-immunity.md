# Braun 2025 - Peptide-based Personalized Neoantigen Vaccine in Resected ccRCC (± Ipilimumab)

## 논문 정보 (저자 / 저널 / DOI / Wiki 경로)

- 저자: Braun et al.
- 저널/연도: Nature, 2025
- DOI: 10.1038/s41586-024-08507-5
- Wiki 경로:
  - Source page: [A neoantigen vaccine generates antitumour immunity in renal cell carcinoma.](../../sources/braun-2025-neoantigen-vaccine-generates-antitumour-immunity.md)
  - Local PDF: `raw/inbox/papers/braun-2025-neoantigen-vaccine-generates-antitumour-immunity.pdf`

## 한 줄 요약

수술 후 고위험 clear cell RCC(총 9명)에서 **peptide 기반 개인맞춤 neoantigen 백신(± ipilimumab)**이 강한 면역원성(다중 epitope 반응, 장기 TCR 확장)과 자가 종양 인지(7/9)를 보였고, median 40.2개월 추적에서 재발이 없었다는 **hypothesis-generating 임상·면역 근거**를 제시한다.

## 표준 메타데이터

- 치료 맥락: 절제 후(adjuvant) 고위험 clear cell RCC(stage III/IV); peptide-based personalized neoantigen vaccine(PCV) ± ipilimumab; trial `NCT02950766`
- 데이터 레이어: 종양 코딩 변이 기반 neoantigen 설계 + 면역반응(ELISpot, scRNA/TCR-seq 등) + 임상 경과(재발/DFS) + 안전성(AE)
- 데이터 공개: Open access Nature 논문(PDF); 상세 데이터/코드 공개 수준은 PDF Data Availability 추가 확인 필요

## 과제 관련성 (Cancer Multiomics)

- Cancer Multiomics의 “WGS 기반 neoantigen 후보가 실제로 면역반응(특히 driver mutation 포함)과 자가 종양 인지로 이어질 수 있는가?” 질문에 직접 연결되는 임상 근거다.
- low TMB 암종에서도 환자별 다중 epitope 백신을 제조/투여하고 면역반응을 확인한 예로, Cancer Multiomics에서 neoantigen 파이프라인을 ‘예측’에서 ‘검증 가능한 치료 축’으로 확장할 때 참고할 수 있다.
- phosphoproteomics/kinase 신호를 직접 다루는 논문은 아니지만, “최종적으로 어떤 임상 설정(adjuvant, recurrence)”에서 무엇을 목표로 삼는지(재발 억제, 면역반응 지속성) 기준점을 제공한다.

## 주요 결과

- 대상/설계: high-risk, fully resected ccRCC 환자 9명에서 PCV를 제조·투여(일부는 접종 부위 인접 ipilimumab 병용).
- 백신 구성: 환자당 합성 neoantigen peptide 중앙값 15개(범위 8–19), 최대 4개 peptide pool로 투여; 모든 환자에서 frameshift indel 유래 peptide ≥1 포함, 7/9에서 RCC driver(VHL/PBRM1/BAP1/KDM5C/PIK3CA 등) 유래 peptide 포함.
- 안전성: 주사부위 반응(100%), 일시적 독감 유사 증상(8/9) 중심; grade ≥3 DLT 보고 없음.
- 임상 경과: 수술 기준 median follow-up 40.2개월에서 9명 모두 재발 없음(대조군 부재·소규모 한계는 명시적으로 고려 필요).
- 면역반응: 9/9에서 백신 특이 T cell 반응 관찰; in vitro deconvolution 후 환자당 면역반응 peptide 중앙값 7개(범위 1–14).
- clonotype/자가종양 인지: 백신 유도 TCR clonotype의 빠르고 큰 확장(평균 166배)과 장기 지속(최대 수 년) 패턴을 보고하며, 자가 종양 인지를 7/9(77.8%)에서 관찰.

## Slack 메시지 초안

Braun et al. (Nature 2025)은 수술 후 고위험 clear cell RCC에서 peptide 기반 개인맞춤 neoantigen 백신(± ipilimumab)을 적용한 phase I 연구(NCT02950766)를 보고했습니다. 총 9명에서 백신 특이 T 세포 반응이 모두 관찰되었고(환자당 반응 neoantigen peptide 중앙값 7개), driver mutation(VHL/PBRM1/BAP1 등) 유래 항원에 대한 반응과 자가 종양 인지(7/9)도 확인했습니다. median 40.2개월 추적에서 재발이 없었다는 점은 표본이 작고 대조군이 없어 hypothesis-generating 근거이지만, Cancer Multiomics 과제의 WGS 기반 neoantigen 후보가 실제 면역반응/종양 인지로 이어질 수 있는지 평가하는 축에 직접 참고할 수 있습니다.

