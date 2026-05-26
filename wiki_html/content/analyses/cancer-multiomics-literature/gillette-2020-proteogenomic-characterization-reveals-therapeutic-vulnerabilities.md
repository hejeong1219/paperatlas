# Gillette 2020 - LUAD CPTAC Proteogenomics (Tumor+NAT; Phospho+Acetyl)

## 논문 정보 (저자 / 저널 / DOI / Wiki 경로)

- 저자: Gillette, Satpathy, Cao et al. (CPTAC)
- 저널/연도: Cell, 2020
- DOI: 10.1016/j.cell.2020.06.013
- Wiki 경로: [Proteogenomic Characterization Reveals Therapeutic Vulnerabilities in Lung Adenocarcinoma](../../sources/gillette-2020-proteogenomic-characterization-reveals-therapeutic-vulnerabilities.md)

## 한 줄 요약

LUAD 110 tumor + 101 NAT에서 genomics/epigenomics와 deep proteome·phosphoproteome·acetylproteome을 통합해 4개 multi-omics subgroup과 driver(KRAS/EGFR/ALK)-연관 취약성, STK11-immune-cold 축을 “측정 기반”으로 정리한 대표 CPTAC 리소스다.

## 표준 메타데이터

- 치료 맥락: 수술 절제 기반 LUAD 코호트(치료 전; chemotherapy/radiotherapy prior 없음).
- 데이터 레이어: genomics + epigenomics + proteome + phosphoproteome + acetylproteome(+ NAT 포함).
- 데이터 공개: CPTAC data portal(S056)에 proteomics raw, genomics/transcriptomics는 GDC(dbGaP phs001287.v5.p4)로 접근(세부는 PDF Data and Code Availability).

## 과제 관련성 (Cancer Multiomics)

- Cancer Multiomics의 핵심 질문(“WGS만으로 설명되지 않는 반응/내성 차이”)에 대해, LUAD에서 driver event가 proteome/phosphoproteome 기능 상태로 번역되는 양상을 cohort-scale로 제공해 **feature 설계의 기준점**이 된다.
- STK11-immune-cold, neutrophil degranulation 등 **면역 축을 proteogenomics로 관찰**한 구성이, WGS-derived immune feature + phosphoproteome 결합 모델을 설계할 때 직접적인 참고가 된다.

## 주요 결과

- 110 tumor + 101 NAT를 포함한 multi-omics proteogenomics로 4개 subgroup을 제시한다.
- KRAS/EGFR/ALK 등 driver 연관 단백질/인산화 신호에서 치료 취약성 후보를 논의한다(정량 기준/검정은 PDF 확인 필요).
- immune subtyping에서 STK11과 immune-cold 연관을 재확인하고, neutrophil degranulation의 면역억제 가능성을 언급한다.
- NAT를 포함해 흡연 관련 signature 및 “field effect”를 다룬다.

## Slack 메시지 초안

Gillette et al. Cell 2020은 LUAD 110 tumor + 101 NAT에서 deep proteome/phosphoproteome/acetylproteome과 genomics/epigenomics를 통합해 4개 multi-omics subgroup과 KRAS/EGFR/ALK driver-연관 취약성, STK11-immune-cold 축을 “측정 기반”으로 제시한 CPTAC 대표 리소스입니다. Cancer Multiomics 과제의 WGS-인산화단백체 통합 분석에서 driver→functional-state(kinase/immune) feature 설계의 기준 데이터로 활용 가치가 큽니다.
