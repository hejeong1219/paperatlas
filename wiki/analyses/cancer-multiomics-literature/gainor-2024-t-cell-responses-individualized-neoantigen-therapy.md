# Gainor 2024 - KEYNOTE-603: mRNA-4157(V940) 면역원성(Phase 1) + Pembrolizumab 병용

## 논문 정보 (저자 / 저널 / DOI / Wiki 경로)

- 저자: Gainor et al.
- 저널/연도: Cancer Discovery, 2024
- DOI: 10.1158/2159-8290.CD-24-0158
- Wiki 경로: [T-cell Responses to Individualized Neoantigen Therapy mRNA-4157 (V940) Alone or in Combination with Pembrolizumab in the Phase 1 KEYNOTE-603 Study](../../sources/gainor-2024-t-cell-responses-individualized-neoantigen-therapy.md)

## 한 줄 요약

개인맞춤 neoantigen mRNA-4157(V940)은 **예측된 neoantigen 중 약 30%에서 면역반응(ELISpot)을 유도**했고(Part D 기준 29.8%), 그 반응의 대부분이 **de novo(84.5%)**로 보고되어, “WGS/설계 → 실제 T cell 반응”의 중간 다리를 제공한다.

## 표준 메타데이터

- 치료 맥락: 절제 후(resected) setting; Part A(NSCLC)에서 mRNA-4157 1 mg 단독(n=4), Part D(흑색종)에서 mRNA-4157 1 mg + pembrolizumab 200 mg 병용(n=12); trial `NCT03313778`
- 데이터 레이어: tumor sequencing 기반 개인맞춤 neoantigen 설계 + PBMC 기반 면역원성(ELISpot/ICS) + TCR repertoire 분석(요약 수준) + 안전성(AE)
- 데이터 공개: PDF는 AACR 저널 본문(PDF)로 확인되며, 세부 데이터/코드 공개 범위는 Data Availability 섹션 추가 확인 필요

## 과제 관련성 (Cancer Multiomics)

- Cancer Multiomics 과제에서 “WGS 기반 neoantigen 후보를 만들었을 때, 그중 실제로 면역반응을 유도하는 비율/특성은?”을 논의할 때 **정량적 근거(29.8% immunogenic, 84.5% de novo)**를 제공한다.
- KEYNOTE-942(Weber 2024)처럼 임상 endpoint(RFS)까지 간 이야기와 연결할 때, 이 논문은 **면역학적 proof-of-concept(중간기전 근거)**를 보강한다.
- phosphoproteome/kinase feature로 반응 예측을 하더라도, 최종적으로 “neoantigen therapy + ICI”가 목표 전략일 때 어떤 **면역 readout을 표준화**해야 하는지(ELISpot/ICS/TCR repertoire) 실무 기준을 제공한다.

## 주요 결과

- Safety: DLT 없음; grade 4/5 AE 없음. mRNA 관련 TEAE는 주로 grade 1–2로 보고되며, 가장 흔한 TEAE는 fatigue(66.7%), pyrexia(60.0%), injection-site pain(40.0%)로 기술된다(PDF 본문).
- Immunogenicity (Part A): longitudinal PBMC에서 ELISpot으로 평가 가능한 3/3 환자에서 mRNA-4157 이후 neoantigen 반응이 관찰된다(PDF 본문 Fig. 구간).
- Immunogenicity (Part D): 평가 가능한 7/7 환자에서 neoantigen 반응이 관찰되며, pembrolizumab run-in 전후에는 대부분 preexisting 반응이 낮거나 관찰되지 않는다고 기술된다.
- Breadth: (Parts A+D) 10명에서 개인별 neoantigen 반응 개수 중앙값 4개(범위 1–20); 5명에서 ≥5개 neoantigen에 대한 반응이 관찰된다(PDF 본문).
- Prediction→response: Part D에서 실험 평가한 in silico 예측 neoantigen 238개 중 29.8%가 immunogenic으로 분류되며, immunogenic 반응 중 84.5%가 de novo, 15.5%가 preexisting 반응으로 보고된다(ELISpot 기반).

## Slack 메시지 초안

Gainor et al. (Cancer Discov 2024, KEYNOTE-603)는 개인맞춤 neoantigen mRNA-4157(V940)의 면역원성 기전 근거를 phase 1에서 정리했습니다(NCT03313778). 절제 후 setting에서 PBMC ELISpot/ICS 기반으로 neoantigen 반응을 추적했으며, Part D(흑색종 병용 파트)에서 in silico 예측 neoantigen 238개 중 29.8%가 immunogenic으로 분류되고, 그중 84.5%가 de novo 반응으로 보고됩니다. Safety 측면에서는 DLT 및 grade 4/5 AE가 없고, 주로 grade 1–2 TEAE(피로/발열/주사부위 통증)가 관찰됩니다. Cancer Multiomics 과제에서 WGS 기반 neoantigen 후보가 실제 면역반응으로 이어지는 비율/표준 readout(ELISpot/ICS/TCR repertoire)을 논의할 때 중간기전 근거로 참고할 수 있습니다.

