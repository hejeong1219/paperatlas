# PTM Correction and Kinase Signaling — Question Expansion Map

`ptmanchor`(PTM correction & kinase signaling) 트랙을 확장하기 위한 질문 은행. 각 질문은 로컬 PDF와 source page를 더 깊게 읽고, concept/analysis/synthesis 페이지를 추가·보강하기 위한 “읽기 프롬프트”로 사용한다.

## Key Points

- 이 문서는 웹 검색용이 아니라, **이미 로컬에 있는 PDF/보충자료를 더 깊게 읽기 위한 큐**다.
- 숫자/주장/결론은 질문에 답하기 전까지 확정하지 않는다(필요 시 “미확인/보충자료 필요”로 표시).
- “교정(correction)으로 신호가 사라지는가 vs artifact가 사라지는가”라는 긴장을 지속적으로 기록한다.
- 질문은 (1) 교정의 정의/가정, (2) 결측·배치·표준화, (3) kinase inference, (4) 임상 번역·내성과의 연결, (5) 위키 구조화로 묶는다.

## Question Bank (100)

1. “protein abundance confounding”을 논문마다 어떤 용어(예: normalization, adjustment, correction)로 부르는가?
2. phosphosite 변화가 protein 변화만 반영하는 “가짜 상승/하락”의 가장 흔한 패턴은 무엇인가?
3. total protein이 측정되지 않은 phosphoproteome-only 연구에서 confounding을 어떻게 추정/완화하는가?
4. peptide→protein summarization 방식(razor/unique, protein group)이 correction에 어떤 구조적 오류를 만들 수 있는가?
5. isoform ambiguity가 site-level 해석을 망치는 대표 사례는 무엇인가?
6. shared peptide 비율이 높은 단백질에서 site-level coupling 모델은 어떻게 실패하는가?
7. correction을 “phosphosite ~ protein” 회귀로 정의할 때 잔차(residual)의 의미는 무엇인가?
8. cohort 간에 coupling slope가 다른 경우(암종/샘플준비/기기), 단일 correction 모델은 왜 위험한가?
9. tumor purity가 protein과 phospho에 동시에 영향을 줄 때 correction은 무엇을 제거하고 무엇을 남기는가?
10. stromal content가 kinase activity score를 왜곡하는 대표 시나리오는 무엇인가?
11. MSstatsPTM, limma 기반 접근, mixed model 접근은 각각 어떤 가정 차이가 있는가?
12. empirical Bayes shrinkage가 small-n clinical cohort에서 어떤 이득/위험을 갖는가?
13. technical replicate가 없는 cohort에서 correction 신뢰도는 무엇으로 판단해야 하는가?
14. batch effect와 protein confounding을 동시에 다룰 때 권장되는 모델 구조는 무엇인가?
15. “global scaling normalization” 이후 correction을 하면 과교정이 생길 수 있는가?
16. missing value가 많은 PTM 데이터에서 MAR/MNAR 가정이 결과에 미치는 영향은 무엇인가?
17. left-censoring imputation은 phosphosite vs protein coupling을 어떻게 왜곡할 수 있는가?
18. site-level localization probability threshold는 correction 이전/이후 해석에 어떻게 반영해야 하는가?
19. phosphopeptide 수준(펩타이드)과 phosphosite 수준(자리) 중 어떤 수준에서 correction을 적용하는 게 더 일관적인가?
20. multi-phosphorylated peptide가 많은 단백질에서 site disentangling은 가능한가?
21. “occupancy(절대 점유율)”가 없을 때 relative phospho 변화의 흔한 오해는 무엇인가?
22. occupancy가 측정된 논문에서는 correction 필요성이 줄어드는가, 혹은 더 명확해지는가?
23. PTM-specific regulation의 gold standard evidence는 무엇인가(perturbation, mutagenesis, kinase assay)?
24. kinase inhibition 실험에서 phosphosite가 내려가도 protein이 함께 내려가는 경우 어떻게 해석해야 하는가?
25. time-course phosphoproteomics에서 early vs late timepoint는 correction 관점에서 어떤 차이가 있는가?
26. acute drug response와 chronic resistance state의 phospho/protein coupling이 달라지는가?
27. KSEA는 “substrate set 평균”이라는 단순성 때문에 어떤 상황에서 취약한가?
28. PTM-SEA(또는 pathway set enrichment)는 kinase inference를 대체할 수 있는가?
29. network-based kinase inference는 어떤 입력(서열 motif, PPI, co-regulation)을 추가하고 어떤 편향을 만든다?
30. kinase-substrate database coverage가 낮은 kinase는 어떻게 “항상 안 보이는” 상태가 되는가?
31. dark phosphosite(미주석) 비율이 높은 논문에서 inference는 어떻게 정직하게 보고해야 하는가?
32. co-regulation module은 “가짜 상관”을 어떤 조건에서 크게 만들 수 있는가?
33. pan-cancer 통합에서 batch/암종 confounding이 kinase module을 가짜로 만들 수 있는가?
34. cross-cancer에서 baseline phosphorylation 차이를 보정하지 않으면 어떤 오류가 생기는가?
35. driver mutation이 protein abundance 변화 없이 phospho만 바꾸는 대표 예시는 무엇인가?
36. copy number-driven protein 변화가 큰 암종에서는 correction 후 어떤 pathway가 “사라져야 정상”인가?
37. correction 후에도 남는 phospho 변화는 어떤 종류의 biology를 시사하는가?
38. correction이 과하게 적용돼 진짜 signaling을 제거하는 사례를 어떻게 탐지할 수 있는가?
39. correction 전후 결과를 동시에 보여주는 표준 visualization(예: paired volcano, slope-residual plot)은 무엇인가?
40. per-site coupling slope/SE를 interactive로 보여주면 어떤 해석이 쉬워지는가?
41. protein abundance correction을 적용한 논문과 적용하지 않은 논문을 같은 synthesis에 넣을 때 최소 caveat는 무엇인가?
42. “protein-corrected phospho”를 선언하는 논문에서 실제 계산이 무엇인지(모델/식)를 어떻게 확인할 것인가?
43. PTM correction을 source page frontmatter 수준으로 표준화해야 하는가(예: ptm_correction: none|global|site_model)?
44. kinase inference method도 frontmatter로 표준화해야 하는가(예: ksea|ptmsea|network|unknown)?
45. 논문이 correction을 하지 않았지만 downstream에서 kinase score를 해석하는 경우, 위키에서 어떤 경고를 붙일 것인가?
46. immunotherapy resistance 논문에서 phosphoproteome이 사용될 때 가장 흔한 용도는 무엇인가(immune state, signaling vulnerability)?
47. EGFR/MAPK/PI3K 축에서 phospho marker는 어떤 기준으로 “canonical”로 취급되는가?
48. DNA damage response kinase(ATM/ATR, CHK1/2, WEE1, CDK) 신호는 어떤 데이터로 안정적으로 읽을 수 있는가?
49. EMT/lineage plasticity는 phosphoproteome에서 어떤 모듈로 나타나는가?
50. antigen presentation 관련 신호(예: IFN pathway)는 phosphoproteome에서 어떤 방식으로 잡히는가?
51. immune checkpoint 단백질 자체의 PTM(예: PD-L1 glycosylation 등)은 이 트랙에서 어디까지 다룰 것인가?
52. tumor intrinsic signaling과 immune cell signaling을 bulk phosphoproteome에서 어떻게 분리할 것인가?
53. deconvolution(immune/stromal) 방법을 쓰는 논문은 phospho 해석에서 어떤 장점을 주장하는가?
54. single-cell/spatial proteomics의 등장으로 correction 문제는 줄어드는가, 더 어려워지는가?
55. label-free/DIA 기반 phosphoproteome은 TMT 대비 coupling 추정이 더 쉬운가?
56. missingness가 낮은 데이터가 항상 coupling 추정에 유리한가(선택 편향 가능성 포함)?
57. enrichment(IMAC/TiO2/Fe-NTA) 선택이 phospho/protein coupling 해석에 어떤 영향을 줄 수 있는가?
58. gradient length/fractionation 깊이가 coupling slope 분포를 바꾸는가?
59. phosphosite localization ambiguity가 kinase inference에 주는 대표 오류는 무엇인가?
60. motif-based kinase assignment가 잘못되는 대표 사례(kinase family motif similarity)는 무엇인가?
61. kinase score가 높지만 kinase 단백질 양이 낮은 경우(또는 반대) 무엇을 우선 해석해야 하는가?
62. kinase activity와 drug sensitivity를 연결할 때 필요한 최소 실험/임상 근거는 무엇인가?
63. cohort atlas에서 “kinase vulnerability”를 주장하려면 어떤 외부 검증(세포주/오가노이드/PDX)이 필요할까?
64. functional network(단백질 co-variation)과 kinase inference(PTM) 결과가 충돌할 때 무엇을 기록해야 하는가?
65. WGS→protein→phospho로의 causal chain을 논문은 어떻게 주장하고 있는가?
66. ppQTL(또는 pQTL)이 보고되는 논문에서 correction은 ppQTL 검출력에 어떤 영향을 주는가?
67. ppQTL이 protein-driven인지 PTM-specific인지 구분하는 방법은 무엇인가?
68. cis vs trans QTL 신호를 phospho에서 해석할 때 흔한 오해는 무엇인가?
69. copy-number-to-protein 전달이 강한 암종에서 phospho QTL의 해석은 어떻게 달라지는가?
70. multi-omics integration 모델(MOFA, iCluster 등)이 correction된 phospho를 입력으로 요구하는가?
71. clinical endpoint(생존/반응/재발) 모델에서 corrected phospho feature가 성능을 올린 사례가 있는가?
72. 성능이 올랐다면 “해석 가능성”은 좋아졌는가 나빠졌는가?
73. “signature” 중심 분석과 “mechanism” 중심 분석은 correction 요구 수준이 다른가?
74. 논문 간에 kinase activity 결과가 다를 때 disagreement를 위키에서 어떤 형식으로 보존할 것인가?
75. 동일 cohort를 다른 팀이 재분석했을 때 correction 효과가 재현되는가?
76. 공개 데이터(CPTAC 등)의 processing pipeline 차이가 correction 결론을 바꿀 수 있는가?
77. raw data 접근 없이 PDF만으로 correction 여부를 판별하기 어려운 경우 어떤 메타데이터를 추가로 찾아야 하는가?
78. 보충자료/Methods에만 correction 설명이 있을 때 위키에 어떻게 기록할 것인가?
79. “protein correction”이라는 표현이 사실상 “median normalization”인 경우를 어떻게 구별할 것인가?
80. PTM correction을 소개하는 최소한의 onboarding concept page는 어떤 구조가 좋을까?
81. correction을 반대/회의적으로 보는 논문/리뷰가 있다면 어떤 논점을 제시하는가?
82. correction 지지 논문은 어떤 실증(예: spike-in, perturbation)으로 정당화하는가?
83. correction을 적용하지 않고도 안전한 해석을 하는 규칙(guardrail)은 무엇인가?
84. “단백질이 안 변했는데 phospho만 변했다”는 결과는 어떤 추가 확인(coverage, missingness)을 요구하는가?
85. “phospho만 변했다”를 주장할 때 protein quantification 한계(LOD/coverage) 문제는 어떻게 다룰까?
86. phosphoproteome에서 outlier sample이 coupling 모델을 망치는 상황을 어떻게 감지할까?
87. robust regression(또는 winsorization)이 왜 필요할 수 있는가?
88. correction 모델 선택을 자동화할 때 어떤 진단 플롯이 필수인가?
89. 위키의 source page에 “교정 전/후 대표 figure”를 기록하는 표준 섹션이 필요한가?
90. interactive atlas(예: multiomics PTM identification)와 달리, 이 트랙의 interactive는 무엇을 보여줘야 하는가?
91. phospho/protein coupling 분포를 암종별로 비교하면 어떤 새로운 질문이 생길까?
92. 특정 pathway(PI3K/MAPK)에서 coupling이 다르게 보이는가?
93. 항암제 class(표적치료/면역치료/화학치료)에 따라 coupling 해석이 달라지는가?
94. CAR-T/BsAb 같은 면역세포 치료의 resistance를 phosphoproteome으로 읽을 수 있는 scope는 어디까지인가?
95. 항원 소실/가공 결함과 kinase signaling은 어떤 교차점에서 연결되는가?
96. interferon pathway defect가 kinase module로 나타나는가, 아니면 transcriptome에만 남는가?
97. “교정이 artifact를 제거한다”는 주장과 “교정이 진짜 신호를 제거한다”는 주장 사이의 핵심 실험은 무엇인가?
98. 결국 이 트랙에서 독자가 설명해야 하는 핵심 원칙 3가지는 무엇인가?
99. 다음 ingest에서 cohort proteogenomics와 perturbation phosphoproteomics 중 무엇을 우선해야 하는가?
100. 이 질문 은행을 통해 만들어야 할 다음 durable 산출물(개념/분석/시각화)은 무엇인가?

## Connections

- [PTM Correction and Kinase Signaling in Cancer Proteomics](../topics/ptm-correction-and-kinase-signaling-in-cancer-proteomics.md)
- [ptmanchor Manuscript Anchor](./ptmanchor-manuscript-anchor.md)
- [Research Questions Queue](../_meta/research-questions-queue.md)

## Sources

- Local PDFs linked from the topic hub and the ptmanchor anchor.
