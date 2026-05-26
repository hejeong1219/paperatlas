# Keskin 2019 - Personalized Neoantigen Vaccine in Glioblastoma (Steroid Effect + TCR Tracking)

## 논문 정보 (저자 / 저널 / DOI / Wiki 경로)

- 저자: Keskin, Anandappa, Sun et al.
- 저널/연도: Nature, 2019
- DOI: 10.1038/s41586-018-0792-9
- Wiki 경로: [Neoantigen vaccine generates intratumoral T cell responses in phase Ib glioblastoma trial.](../../sources/keskin-2019-neoantigen-vaccine-generates-intratumoral-t.md)

## 한 줄 요약

수술 및 표준 방사선치료 후 신규 GBM 환자에서 개인맞춤 neoantigen 장펩타이드 백신(phase I/Ib)이 가능함을 보이며, **dexamethasone 사용 여부가 백신 유도 T 세포 반응을 강하게 좌우**하고, scTCR 분석으로 말초 혈액의 neoantigen-반응 T 세포가 종양 내로 이동할 수 있음을 제시한다.

## 표준 메타데이터

- 치료 맥락: 신규 진단 glioblastoma에서 수술 절제 + 표준 방사선치료 후 personalized neoantigen vaccine(phase I/Ib); dexamethasone 동반 여부가 핵심 교란 요인.
- 데이터 레이어: 종양/정상 샘플에서 변이 기반 neoantigen 후보 선정(WES/RNA 기반), 면역 모니터링(ELISPOT/ICS), 종양 면역침윤 정량, scTCR/레퍼토리 트래킹.
- 데이터 공개: 공개 저장소(dbGaP 등) 및 raw/processed 접근 경로는 PDF 확인 필요.

## 과제 관련성 (Cancer Multiomics)

- Cancer Multiomics에서 WGS 기반 neoantigen 후보를 다룰 때, “예측된 후보”를 **면역 반응(혈액/종양 내 T 세포)으로 연결**하는 임상형 레퍼런스다.
- 동반약물(dexamethasone) 같은 임상 변수에 의해 면역 readout이 크게 교란될 수 있어, Cancer Multiomics cohort에서도 **약물/시점 메타데이터를 표준화해서 기록**해야 함을 보여준다.
- (확장) 향후 immunopeptidomics/neoantigen validation을 붙일 때, “neoantigen 후보 선정→면역 반응 측정→클론 트래킹”의 end-to-end 스토리라인을 제공한다.

## 주요 결과

- personalized neoantigen long-peptide 백신을 수술-방사선치료 회복 기간에 제조하고 prime–boost 스케줄로 투여하는 임상 운영 가능성을 보고한다.
- dexamethasone을 vaccine priming 기간에 사용하지 않은 환자에서 neoantigen-specific CD4+/CD8+ 반응(ELISPOT/ICS)이 관찰되고, polyfunctional/memory-like 특징이 기술된다.
- 재수술/재발 시점의 종양에서, 비-dexamethasone 환자에서 CD8+/CD4+ 침윤 증가가 관찰되며, scTCR 기반으로 말초 혈액에서 확인된 클론이 종양에서도 추적될 수 있음을 제시한다.

## Slack 메시지 초안

Keskin et al. (Nature 2019)은 신규 GBM 환자에서 개인맞춤 neoantigen 장펩타이드 백신(phase I/Ib)의 가능성을 보여주며, **dexamethasone 사용 여부가 백신 유도 T 세포 반응을 크게 좌우**함을 명확히 제시합니다. 또한 scTCR 분석으로 말초의 neoantigen-반응 T 세포가 종양 내로 이동할 수 있음을 보여 “변이 기반 neoantigen 후보→면역 반응→클론 트래킹” 연결의 좋은 reference입니다.

