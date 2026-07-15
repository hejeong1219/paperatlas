---
title: "Proteogenomic profiling predicts outcomes of adjuvant chemotherapy in extrahepatic cholangiocarcinoma."
authors:
  - "Jeong"
  - "Oh"
  - "Ahn"
year: 2025
journal: "Journal of hepatology"
doi: "10.1016/j.jhep.2025.07.031"
pmid: "40803577"
paper_kind: proteogenomic
pdf: "raw/inbox/papers/jeong-2025-proteogenomic-profiling-predicts-outcomes-adjuvant-chemotherapy.pdf"
pdf_status: wrong-pdf
topic: ptmanchor
tags:
  - "ptmanchor"
  - "proteomics"
  - "ptm"
  - "phosphoproteomics"
  - "cancer-proteomics"
  - "pmid-40803577"
themes:
  - "ptm-correction"
  - "kinase-signaling"
  - "cancer-proteomics"
---
# Proteogenomic profiling predicts outcomes of adjuvant chemotherapy in extrahepatic cholangiocarcinoma.

_Journal of hepatology, 2025._ PMID: [40803577](https://pubmed.ncbi.nlm.nih.gov/40803577/).

DOI: [10.1016/j.jhep.2025.07.031](https://doi.org/10.1016/j.jhep.2025.07.031)

> **본문 출처 주의:** 아래 Summary/Key Points는 2026-07-15 Slack digest 게시를 위해 공식 PubMed/MEDLINE 초록(PMID 40803577)에서 확보한 내용입니다. 로컬 PDF(`raw/inbox/papers/jeong-2025-...pdf`)는 여전히 **다른 논문**(Annals of Transplantation 2025, DOI `10.12659/AOT.951088`)이므로 `pdf_status: wrong-pdf`를 유지하며, 전문(full-text) 수준 주장·인용 시에는 올바른 Journal of Hepatology PDF를 재확보한 뒤 재검증이 필요합니다.

## Summary

Extrahepatic cholangiocarcinoma(간외 담관암, EH-CCA)의 분자 지형과 보조요법 바이오마커를 규명하기 위해, 절제 후 capecitabine 또는 gemcitabine+cisplatin(GemCis) 보조요법을 비교한 무작위 2상 STAMP 시험 내에서 사전 지정된 탐색적 분석을 수행한 연구입니다. ITT 101명 중 89명(GemCis 45명, capecitabine 44명)의 수술 검체를 whole-exome sequencing과 proteomics로 분석하고 무병생존(DFS)에 대한 예후·예측 바이오마커를 상관 분석했습니다. TP53(63%)·SMAD4(20%)·KRAS(18%) 변이가 흔했고, PIK3CA·FBXW7 변이는 불량한 DFS, 11q13.3 amplification은 양호한 DFS와 연관되었으며, 8q24.21·3q26.1·4p16.3 amplification·8p23.1 deletion·homologous recombination deficiency(HRD) 등은 보조요법 regimen과 유의한 상호작용을 보여 GemCis에 유리했습니다. 이들 예측 바이오마커를 통합해 conditional average treatment effect(CATE)를 산출하는 machine-learning 예측 모형을 구축, 환자를 GemCis 유리·차이 없음·capecitabine 유리의 3군으로 층화했고 이 모형은 DFS와 유의하게 연관되었습니다.

## Key Points

- STAMP 무작위 2상 시험(절제된 EH-CCA, GemCis vs capecitabine 보조요법) 내 사전 지정 탐색 분석; 89명 검체를 whole-exome sequencing + proteomics로 통합 분석.
- 예후 바이오마커: PIK3CA·FBXW7 변이 → 불량 DFS; 11q13.3 amplification → 양호 DFS. 빈발 변이는 TP53(63%)·SMAD4(20%)·KRAS(18%).
- 예측(치료-상호작용) 바이오마커: 8q24.21·3q26.1·4p16.3 amplification, 8p23.1 deletion, HRD가 regimen과 유의한 상호작용 → GemCis에 유리.
- Machine-learning 모형으로 conditional average treatment effect(CATE) 산출 → 환자를 3군(GemCis 유리 / 차이 없음 / capecitabine 유리)으로 층화, DFS와 유의 연관.
- ESCAT 기준 actionable alteration 15%, HRD 11%, MSI 1%. 저자들은 추가 검증이 필요함을 명시.

## 한미암 활용 가능성

한미암 과제의 AI 치료반응성 예측 모형(목표 4) 및 항암제 반응성 프로파일링(목표 2) 관점에서, 예후 바이오마커와 치료-상호작용(predictive) 바이오마커를 분리해 conditional average treatment effect로 regimen별 이득군을 나누고 무작위 시험 내에서 DFS로 검증한 설계는, "반응/무반응" 이분 예측을 넘어 "어느 치료가 더 이득인지"를 출력하는 모형 구조와 그 검증 틀을 설계할 때 참고할 만한 사례입니다. WGS(본 논문에서는 WES)+proteomics 통합에서 도출한 CNV·HRD·변이 신호를 치료-상호작용 축으로 다루는 방식은, 한미암 코호트의 1차/2차 내성 층화 변수 후보를 고민하는 데에도 시사점을 줄 수 있습니다.

## Open Questions

- 올바른 Journal of Hepatology 전문 PDF를 재확보하고, 제목/DOI가 frontmatter와 일치하는지 확인한 뒤 full-text 재수집.
- CATE 기반 예측 모형의 외부 코호트 일반화 가능성 및 위암 등 다른 GI 암종으로의 전이 가능성 검토.

## Connections

- [Ptmanchor Topic Hub](../topics/ptm-correction-and-kinase-signaling-in-cancer-proteomics.md)
- [Ptmanchor Anchor](../analyses/ptmanchor-manuscript-anchor.md)

## Sources

- Local PDF: `raw/inbox/papers/jeong-2025-proteogenomic-profiling-predicts-outcomes-adjuvant-chemotherapy.pdf`
- PubMed: <https://pubmed.ncbi.nlm.nih.gov/40803577/>
- DOI: <https://doi.org/10.1016/j.jhep.2025.07.031>
