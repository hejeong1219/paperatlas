# Clark 2019 - ccRCC CPTAC Proteogenomics (Tumor+NAT; immune subtypes)

## 논문 정보 (저자 / 저널 / DOI / Wiki 경로)

- 저자: Clark, Dhanasekaran, Petralia et al. (CPTAC)
- 저널/연도: Cell, 2019
- DOI: 10.1016/j.cell.2019.10.007
- Wiki 경로: [Integrated Proteogenomic Characterization of Clear Cell Renal Cell Carcinoma](../../sources/clark-2019-integrated-proteogenomic-characterization-clear-cell.md)

## 한 줄 요약

ccRCC에서 genomics/epigenomics/transcriptomics와 proteome/phosphoproteome을 통합해(110 RCC tumors + 84 NAT; 본문 해석은 103 ccRCC 중심) genomic instability, 대사/번역/인산화 signaling 모듈, 그리고 4개 immune-based subtype을 기능 상태 관점에서 정리한 CPTAC 리소스다.

## 표준 메타데이터

- 치료 맥락: treatment-naive(치료 전) RCC/ccRCC 코호트 + paired NAT.
- 데이터 레이어: multi-omics + proteome + phosphoproteome(PTM).
- 데이터 공개: CPTAC data portal(S044, S050)에 proteomics raw/processed, genomics/transcriptomics는 GDC로 접근(세부는 PDF Data and Code Availability).

## 과제 관련성 (Cancer Multiomics)

- WGS/SV/CNA 같은 유전 이벤트가 실제로는 **단백질·인산화 기능 모듈(대사/번역/kinase signaling)**로 번역되어 나타난다는 관점을 cohort-scale로 제공해, Cancer Multiomics의 “유전→기능 상태” feature 설계에 바로 연결된다.
- immune infiltration을 signature 기반으로 subtype화하고 pathway와 연결하는 구성은, 표적치료/면역치료 반응·내성 모델에서 **WGS-derived immune feature + phosphoproteome** 결합 프레임의 참고점이 된다.

## 주요 결과

- multi-omics 통합으로 genomic instability 관련 subgroup을 포함한 기능 모듈 해석을 제시한다.
- proteogenomic 통합으로 oxidative phosphorylation, translation, phospho-signaling 등 “유전 이벤트로 인해 영향을 받는” 단백질 레벨 변화 축을 강조한다.
- microenvironment cell signature로 4개 immune-based ccRCC subtype을 정의하고 subtype별 pathway 차이를 보고한다.

## Slack 메시지 초안

Clark et al. Cell 2019는 ccRCC에서 genomics/epigenomics/transcriptomics와 proteome/phosphoproteome을 통합해(110 tumors + 84 NAT; 103 ccRCC 중심) genomic instability, 대사/번역/인산화 signaling 모듈, 그리고 4개 immune-based subtype을 기능 상태 관점에서 정리한 CPTAC 대표 리소스입니다. Cancer Multiomics 과제의 WGS-인산화단백체 통합 모델에서 “유전 이벤트→functional module”과 immune axis를 함께 feature로 설계하는 데 좋은 reference입니다.
