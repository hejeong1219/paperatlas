---
title: PTM Correction and Kinase Signaling Question Bank
tags:
  - question-bank
  - ptm-correction
  - phosphoproteomics
  - kinase-signaling
---

# PTM Correction and Kinase Signaling Question Bank

PTM(protein post-translational modification) 보정(특히 protein abundance correction)과 kinase signaling 해석을 더 깊게 읽기 위한 질문 은행.  
기존에는 “Four-Topic Question Expansion Map”의 Topic 4로 운영했으나, 2026-05-10부터는 Cancer Multiomics 문헌 모니터링이 Topic 4로 승격되면서 이 페이지로 분리했다.

## Key Points

- 이 질문들은 “PTM identification count” 자체가 아니라 **해석층(보정/추론/검증)**을 강화하기 위한 큐다.
- 논문마다 correction 여부/방법/입력 단위가 달라, 단위와 가정의 차이를 드러내는 질문을 우선한다.

## Questions (100)

1. PTM abundance 변화와 total protein abundance 변화는 어떤 상황에서 분리해서 해석해야 하는가?
2. protein abundance correction을 하지 않은 phosphosite 변화는 어떤 false interpretation을 만들 수 있는가?
3. site-level correction과 protein-level correction은 어떤 statistical assumption이 다른가?
4. PTM correction에서 shared peptide, isoform ambiguity, protein group 문제는 어떻게 다뤄야 하는가?
5. phosphosite 변화가 kinase activity를 의미하려면 어떤 추가 근거가 필요한가?
6. acetylsite 변화가 acetyltransferase/deacetylase activity를 의미하려면 어떤 조건이 필요한가?
7. PTM stoichiometry와 relative abundance는 biological interpretation이 어떻게 다른가?
8. absolute site occupancy를 측정하지 못할 때 어떤 caveat를 달아야 하는가?
9. protein abundance correction이 biological signal을 과도하게 제거하는 경우는 언제인가?
10. correction 전후 결과를 함께 보여주는 visualization은 어떤 해석을 가능하게 하는가?
11. MSstatsPTM 같은 model은 PTM-specific regulation과 global protein regulation을 어떻게 분리하는가?
12. linear model, empirical Bayes, mixed model은 PTM data에서 어떤 차이를 만든다?
13. missing value가 많은 phosphoproteome에서 correction model은 어떤 bias를 갖는가?
14. replicate structure가 약한 clinical cohort에서 PTM correction 신뢰도를 어떻게 판단할 것인가?
15. batch effect와 protein abundance correction 효과를 어떻게 구분할 수 있는가?
16. tumor purity correction과 protein abundance correction은 서로 다른 confounder를 다루는가?
17. PTM site가 여러 protein isoform에 매핑될 때 correction denominator를 어떻게 고를 것인가?
18. peptide-level quantification에서 protein-level correction을 적용하면 어떤 정보가 손실되는가?
19. global scaling normalization과 site-specific correction은 어떤 단계에서 충돌할 수 있는가?
20. correction model 결과를 source page에 기록할 때 필요한 최소 metadata는 무엇인가?
21. kinase activity inference는 substrate phosphorylation의 단순 평균인가, network-based score인가?
22. KSEA, PTM-SEA, VIPER-like, network-based methods는 어떤 입력과 assumption이 다른가?
23. kinase-substrate database coverage가 낮은 kinase는 inference에서 어떻게 불리해지는가?
24. dark phosphoproteome은 known kinase-substrate map 밖의 signaling을 어떻게 드러내는가?
25. co-regulation 기반 phosphosite module은 kinase annotation 없는 site를 어떻게 해석하게 해주는가?
26. kinase activity inference benchmark는 ground truth를 어떻게 정의하는가?
27. inhibitor perturbation dataset은 kinase inference method 평가에 어떤 장점과 한계를 갖는가?
28. pan-cancer cohort에서 inferred kinase activity와 actual kinase expression은 얼마나 다를 수 있는가?
29. upstream kinase prediction과 downstream pathway activity inference는 어떻게 구분해야 하는가?
30. kinase activity score가 drug sensitivity를 예측하는 사례는 어떤 evidence가 필요한가?
31. PI3K/AKT/mTOR pathway proteogenomic atlas는 genomic alteration과 phosphoproteome을 어떻게 연결했는가?
32. MAPK pathway activation은 phosphosite data에서 어떤 canonical marker로 확인되는가?
33. receptor tyrosine kinase activation은 ligand, mutation, copy number, phosphorylation 중 어떤 근거를 결합해야 하는가?
34. WEE1, CDK, ATM/ATR, DNA damage kinase 축은 cancer therapy resistance와 어떻게 연결되는가?
35. AMPK, mTOR, metabolic kinase signaling은 proteogenomic subtype과 어떻게 연결되는가?
36. immune checkpoint pathway의 PTM regulation은 tumor immunity와 kinase signaling을 어떻게 만나는가?
37. kinase fusion 또는 structural variation은 proteome/phosphoproteome에서 어떤 downstream signature를 만든다?
38. somatic structural variation의 proteome effect와 phosphoproteome effect는 어떻게 다르게 나타나는가?
39. copy number-driven protein abundance change를 correction하면 어떤 pathway signal이 남는가?
40. driver mutation이 protein abundance change 없이 phosphosite만 바꾸는 사례는 무엇인가?
41. pan-cancer proteogenomic studies는 tissue-specific signaling과 shared cancer signaling을 어떻게 구분하는가?
42. cancer type별 phosphosite baseline 차이는 cross-cancer inference에서 어떤 batch-like artifact를 만들 수 있는가?
43. phosphosite module이 tissue-specific program을 반영하는지, tumor-specific program을 반영하는지 어떻게 구분할 것인가?
44. sample processing(ischemia time, lysis buffer, inhibitor cocktail)은 phosphosite stability를 얼마나 좌우하는가?
45. phosphatase inhibitor 사용 여부가 site count와 effect size에 어떤 영향을 주는가?
46. enrichment(예: IMAC) 조건이 motif bias를 만들 때 kinase inference는 어떻게 왜곡되는가?
47. fractionation 전략이 kinase inference의 coverage(특정 pathway) 편향을 만들 수 있는가?
48. DIA vs DDA는 PTM correction과 kinase inference 신뢰도에서 어떤 차이를 만들 수 있는가?
49. single-shot phosphoproteomics는 network inference에 필요한 depth를 제공하는가?
50. PTM correction이 가능한 최소 replicate 구조(기술/생물학)는 무엇인가?
51. clinical cohort에서 covariate(성별, stage, treatment line)를 넣은 correction/inference 모델은 어떤 형태가 적절한가?
52. subgroup 비교에서 “subgroup-specific protein abundance difference”가 PTM 차이를 가리는 상황은 무엇인가?
53. phosphosite significance threshold가 kinase activity score 결과를 얼마나 민감하게 바꾸는가?
54. kinase activity score는 site count가 많은 kinase에 유리한가? 불리한가?
55. substrate set overlap가 높은 kinase family에서 cross-talk 오해를 어떻게 줄일 것인가?
56. upstream phosphatase activity 변화는 kinase inference에서 어떻게 오인될 수 있는가?
57. phosphoproteome에서 cell cycle confounding을 어떻게 분리할 것인가?
58. proliferation signature가 kinase activity처럼 보이는 상황을 어떻게 진단할 것인가?
59. tumor purity가 낮은 sample에서 stromal kinase activity가 tumor-intrinsic activity로 오인되는 사례는 무엇인가?
60. immune infiltration이 높은 sample에서 immune-cell kinase activity(예: LCK)가 tumor signaling처럼 보이는 문제를 어떻게 다룰 것인가?
61. phosphosite module을 pathway로 이름 붙일 때 “주요 marker site”는 무엇을 근거로 선택할 것인가?
62. unknown phosphosite를 기능적으로 prioritization하려면 conservation, motif, co-regulation, drug response 중 무엇을 볼까?
63. phosphosite localization ambiguity를 network inference에 넣으면 어떤 오류가 생길 수 있는가?
64. kinase motif similarity 때문에 wrong kinase assignment가 생기는 사례를 어떻게 표시할 것인가?
65. pan-cancer kinase signaling synthesis에서 canonical pathway별로 묶을지, method별로 묶을지 어떤 구조가 나은가?
66. perturbed vs observational dataset에서 kinase inference 해석 층을 다르게 기록할 필요가 있는가?
67. “kinase activity↑” claim을 논문에서 확인할 때 반드시 체크해야 하는 figure/표는 무엇인가?
68. inhibition/activation의 directionality를 motif or site-level로 확인하는 방법은 무엇인가?
69. kinase activity inference가 drug response prediction model에서 transcriptome보다 유리한 조건은 무엇인가?
70. kinase inference가 실제로 actionable하게 이어진 임상/전임상 사례는 무엇인가?
71. corrected PTM effect size와 uncorrected effect size를 동시에 보여주는 interactive plot은 어떤 insight를 줄까?
72. correction이 signal을 제거하는지 artifact를 제거하는지 판단하려면 어떤 negative/positive control이 필요한가?
73. PTM correction을 모르는 독자가 먼저 읽어야 할 concept page(또는 최소 프라이머)는 무엇이어야 하는가?
74. source page에서 PTM correction 여부를 표시하는 표준 field를 만들 필요가 있는가?
75. 각 논문의 phosphosite count, correction method, kinase inference method를 한 table에 모으면 어떤 gap이 보일까?
76. correction method가 명시되지 않은 논문은 kinase inference 결과를 얼마나 신뢰할 수 있는가?
77. review paper가 correction importance를 강조하지만 primary paper가 적용하지 않는 경우를 어떻게 기록할 것인가?
78. “phosphorylation increased”라는 문장이 protein abundance 증가만 반영할 가능성을 어떻게 점검할 것인가?
79. kinase activity figure를 읽을 때 substrate list, directionality, significance threshold를 어떻게 확인해야 하는가?
80. volcano plot, heatmap, network diagram은 각각 PTM signaling 해석에서 어떤 장단점이 있는가?
81. tissue-level atlas에서 phosphosite module을 pathway로 이름 붙이는 기준은 무엇인가?
82. machine-learned phosphosite module은 biological naming을 어떻게 부여받는가?
83. functional network에서 hub kinase 또는 hub phosphosite를 therapeutic target으로 주장하려면 어떤 validation이 필요한가?
84. perturbation proteomics는 causal signaling을 보여주는 데 cohort atlas보다 어떤 장점이 있는가?
85. CRISPR, inhibitor, time-course phosphoproteomics는 각각 어떤 signaling question에 적합한가?
86. time-resolved phosphoproteomics는 steady-state cohort data가 놓치는 무엇을 보여주는가?
87. acute kinase inhibitor response와 chronic resistance state는 phosphoproteome에서 어떻게 다르게 보이는가?
88. personalized phosphoproteomics는 individual patient therapy selection에 실제로 얼마나 가까워졌는가?
89. clinical phosphoproteomics를 routine precision oncology로 쓰기 어려운 병목은 무엇인가?
90. sample amount, turnaround time, enrichment reproducibility는 clinical translation을 어떻게 제한하는가?
91. phosphoproteome-guided therapy recommendation은 어떤 prospective validation이 필요한가?
92. patient-derived organoid phosphoproteomics는 drug response를 예측하는 bridge가 될 수 있는가?
93. kinase signaling atlas와 resistance topic을 연결하면 어떤 treatment failure mechanism을 더 잘 설명할 수 있는가?
94. neoantigen/TLS topic과 PTM signaling topic은 immune checkpoint PTM regulation에서 만날 수 있는가?
95. PTM correction topic과 multiomics identification topic은 count extraction 이후 어떤 synthesis로 이어져야 하는가?
96. ptm manuscript anchor와 이 질문 은행 사이에서 중복되는 claim을 어떻게 줄일 것인가?
97. 현재 topic의 representative papers가 method, cohort, review, computational paper를 균형 있게 포함하는가?
98. 다음 ingest에서는 kinase inference benchmark와 clinical proteogenomic cohort 중 무엇을 우선해야 하는가?
99. 이 질문 은행을 교수님께 공유할 때 가장 먼저 보여줘야 하는 plot과 가장 먼저 읽혀야 하는 explanation은 무엇인가?
100. 이 topic을 공부한 사람이 마지막에 설명해야 하는 핵심 원칙은 무엇인가?

## Connections

- [Multiomics Proteomics PTM Identification](../topics/multiomics-proteomics-ptm-identification.md)
- [PTM Correction and Kinase Signaling in Cancer Proteomics](../topics/ptm-correction-and-kinase-signaling-in-cancer-proteomics.md)

## Sources

- Local PDFs linked from the PTM topic hubs and their `wiki/sources/*` pages.
