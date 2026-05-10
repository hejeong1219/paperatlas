# Chen 2023 - SV Breakpoints → Protein Consequences (Pan-cancer WGS+Proteomics)

## 논문 정보 (저자 / 저널 / DOI / Wiki 경로)

- 저자: Chen, Zhang et al.
- 저널/연도: Nature Communications, 2023
- DOI: 10.1038/s41467-023-41374-8
- Wiki 경로: [Global impact of somatic structural variation on the cancer proteome](../../sources/chen-2023-global-impact-somatic-structural-variation-cancer-proteome.md)

## 한 줄 요약

pan-cancer 1307 tumors에서 WGS 기반 SV breakpoint 패턴과 proteomics를 결합해, 비암호화 SV(cis-regulation)가 mRNA뿐 아니라 단백질 수준에서도 얼마나 “실제로” 반영되는지(~25%)를 정량화하고, SV+protein evidence로 임상적으로 중요 pathway의 “altered 환자 수”가 늘어날 수 있음을 제시한다.

## 표준 메타데이터

- 치료 맥락: 단일 임상 코호트라기보다 공공 데이터 compendium(암종 혼합; 조직/치료 맥락은 데이터셋별로 상이).
- 데이터 레이어: WGS(SV) + mass-spec proteomics(+ mRNA, methylation 등 보조 레이어를 함께 사용).
- 데이터 공개: public-domain WGS/proteomics compendium 기반(구체 데이터셋/접근 경로는 PDF 확인 필요).

## 과제 관련성 (Cancer Multiomics)

- Cancer Multiomics에서 WGS SV/breakpoint feature를 “유전 이벤트”로만 두지 않고 **단백질 수준의 consequence**(expression/functional state)로 연결해야 한다는 근거를 제공한다.
- WGS로 잡히는 SV event가 RNA proxy와 항상 일치하지 않음을 전제로 하므로, Cancer Multiomics의 WGS-인산화단백체 통합 모델에서 “SV→protein/PTM evidence로 보정”하는 설계 원칙을 강화한다.

## 주요 결과

- 1307 tumors에서 SV breakpoint 패턴과 단백질 발현의 cis 연관을 대규모로 스캔한다.
- SV-associated cis-regulatory alteration이 mRNA에서 관찰되는 유전자들 중 일부만 단백질에서도 반영되며(~25%), enhancer hijacking/retrotransposon translocation/methylation/fusion event 등이 단백질 과발현과 연결될 수 있음을 기술한다.
- SV + 단백질 발현 변화 조합으로 pathway-level alteration 판별이 확장될 수 있다고 주장하며, 생존 연관 패턴과 세포주 dependency 연관을 카탈로그한다.

## Slack 메시지 초안

Chen et al. Nat Commun 2023은 pan-cancer 1307 tumors에서 WGS 기반 SV breakpoint와 proteomics를 결합해, 비암호화 SV(cis-regulation)가 mRNA뿐 아니라 단백질 수준에서도 얼마나 실제로 반영되는지(~25%)를 정량화하고, SV+protein evidence로 임상적으로 중요한 pathway의 “altered 환자 수”가 늘어날 수 있음을 제시합니다. Cancer Multiomics 과제에서 SV/WGS feature를 phosphoproteome/단백질 evidence로 보정해 반응·내성 모델에 넣는 설계 원칙을 뒷받침하는 시스템 reference입니다.
