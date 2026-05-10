# Four-Topic Question Expansion Map

현재 위키의 네 개 사용자-facing topic track을 확장하기 위한 질문 은행. 각 질문은 **로컬 PDF / 보충자료 / 기존 wiki source page**를 더 깊게 읽기 위한 “읽기 프롬프트”로 사용한다.

## Key Points

- 질문은 웹 검색용이 아니라, 로컬 증거(PDF/보충자료)를 더 깊게 읽기 위한 확장 큐다.
- 각 질문은 하나 이상의 source page, concept/analysis/synthesis 페이지 보강으로 이어져야 한다.
- 논문 간 기준/정의/방법 차이를 드러내는 질문을 우선한다(“동일 용어, 다른 의미”를 특히 표기).
- Cancer Multiomics topic은 교수진 공유를 위해 Slack-ready 형태의 출력까지 연결한다.

## Concrete Growth Targets (by topic)

각 토픽은 “질문 → (source page deep-dive) → (concept/topic 연결) → (durable artifact)”로 이어지도록 다음 작업을 우선한다.

### Topic 1 (B-Cell Neoantigen)

- (DONE 2026-05-10) `wiki/concepts/b-cell-and-tls-context-for-neoantigen-research.md`에 “B cell/TLS가 neoantigen efficacy를 바꾸는 경로(항원제시, Tfh, DC 교차, 항체/immune complex)” + 읽기 체크리스트 보강
- (DONE 2026-05-10) `wiki/concepts/neoantigen-discovery-and-prioritization.md`에 class I/II, noncanonical, evidence tier(예측 vs MS 관측 vs 면역원성) 표준 정의 추가
- (DONE 2026-05-10) `wiki/analyses/b-cell-neoantigen-pipeline-human-cancer-corpus.md`에 “neoantigen→면역구조(B/TLS)→임상반응” 5편 우선 읽기 큐 추가
- (NEXT) Topic 1에서 우선 deep-dive할 source page 1편을 지정하고, 해당 PDF에서 “HLA-II/비정형 ORF/검증 정의”를 source page에 표준 섹션으로 채움(예: `huber-2025-comprehensive-proteogenomic-pipeline-neoantigen-discovery`)

### Topic 2 (Immunotherapy Resistance / Immune Evasion)

- (DONE 2026-05-10) `wiki/concepts/mhc-i-loss-and-interferon-pathway-defects-in-checkpoint-resistance.md`에 “유전적 결함 vs 적응적 downregulation” 체크리스트/표 추가
- (DONE 2026-05-10) `wiki/concepts/antigen-loss-lineage-switch-and-target-escape.md`에 therapy 유형별 “관측 단위(유전체/전사/단백/표면/라인리지)” 표준 추가
- (DONE 2026-05-10) `wiki/analyses/cancer-resistance-manuscript-anchor.md`에 “Primary/Adaptive/Acquired × evidence tier” 매트릭스 초안 추가
- (NEXT) Topic 2에서 “내성 우회(조합 전략)” paper 1편을 source page + Cancer Multiomics brief로 동시 deep-dive(예: `skoulidis-2024-ctla4-abrogates-keap1-stk11-resistance`)

### Topic 3 (Multiomics Proteomics PTM Identification)

- (DONE 2026-05-10) `wiki/analyses/multiomics-ptm-corpus-queue.md`에 “추출 우선순위 규칙(PTM breadth, cohort signal, method novelty, supplement, unit integrity)” 추가
- (DONE 2026-05-10) `interactives/multiomics-proteomics-ptm-identification/README.md`에 unit-preserving 표준 key 정의 고정
- (DONE 2026-05-10) `satpathy-2021-proteogenomic-portrait-lung-squamous-cell`의 proteome count(11,575 quantified proteins)를 local PDF Methods 기반으로 보강
- (DONE 2026-05-10) multi-omics/atlas 핵심 cohort 논문 3편을 “요약/Key Points + atlas caveat”까지 최소 업그레이드:
  - `wiki/sources/vasaikar-2019-proteogenomic-analysis-human-colon-cancer.md` (neoantigen/CT antigen + glycolysis↔CD8 MSI 프레임)
  - `wiki/sources/clark-2020-integrated-proteogenomic-characterization-clear-cell.md` (ccRCC immune subtype + phosphopeptide quantified count 보강)
  - `wiki/sources/wang-2021-proteogenomic-metabolomic-characterization-human-glioblastoma.md` (GBM multi-omics; instrument 근거 명시, 총량은 supplement 필요로 고정)
- (NEXT) atlas row로 쓰이는 논문 중 `## Multi-Omics Identification Extraction`이 “instrument/model 미기재” 또는 “count unit 불명확” 상태인 항목 3편을 골라, **local PDF 근거 문장**과 **supplement 위치(있다면 Table S#)**까지 명시해 `extracted`로 승격
  - 후보 1: `mertins-2016-proteogenomics-connects-somatic-mutations-signalling` (instrument/platform 근거 문장 확보 필요)
  - 후보 2: `shi-2022-integrated-proteogenomic-characterization-medullary-thyroid` (instrument model은 main PDF 미기재 → supplement 확보 필요)
  - 후보 3: `wang-2021-proteogenomic-metabolomic-characterization-human-glioblastoma` (proteome/phospho/acetyl 총량 count는 supplement 확인 필요)

### Topic 4 (Cancer Multiomics Monitor)

- `wiki/topics/cancer-multiomics-literature.md`의 표준 체크리스트를 “치료 맥락 / 데이터 레이어 / 데이터 공개” 3줄로 고정하고, 하위 페이지에서 동일한 bullet을 유지
- `wiki/analyses/cancer-multiomics-literature/*` seed 요약에 위 3개 bullet을 우선 보강(미확인 값은 “PDF 확인 필요”로 표기)
- `wiki/analyses/cancer-multiomics-corpus-queue.md`에 “raw/inbox/papers에 이미 있는 후보”를 3–5편만 우선 등록하고, 각 항목에 Cancer Multiomics relevance 1줄과 확인 필요한 supplement/데이터 항목을 함께 기록
- (DONE 2026-05-10) `skoulidis-2024-ctla4-abrogates-keap1-stk11-resistance` brief + hub/queue 갱신
- (DONE 2026-05-10) `memon-2024-clinical-molecular-features-acquired-resistance` brief + hub/queue 갱신
- (DONE 2026-05-10) `braun-2025-neoantigen-vaccine-generates-antitumour-immunity` brief + hub/queue 갱신
- (DONE 2026-05-10) `gainor-2024-t-cell-responses-individualized-neoantigen-therapy` brief + source-page deep-dive(면역원성 수치) 반영

## Topic 1: B-Cell Neoantigen Research Map (100)

1. 인간 암에서 neoantigen 후보를 정의할 때 mutation-derived peptide와 noncanonical peptide를 어떻게 구분하는가?
2. 각 논문은 DNA variant, RNA expression, proteomics, immunopeptidomics 중 어떤 근거를 neoantigen 우선순위에 사용했는가?
3. HLA class I 기반 neoantigen과 HLA class II 기반 neoantigen은 discovery 단계에서 어떤 다른 필터를 요구하는가?
4. tumor-specific mutation이 실제 MHC presentation으로 이어지지 않는 가장 흔한 병목은 무엇인가?
5. RNA 발현량은 neoantigen 후보의 신뢰도를 어느 정도까지 보강하는가?
6. immunopeptidomics로 직접 검출된 peptide와 prediction-only 후보는 임상 번역에서 어떻게 다른 무게를 갖는가?
7. frameshift, splice junction, fusion, circRNA, retroelement peptide는 canonical SNV neoantigen과 어떤 면에서 다르게 평가되는가?
8. clonal neoantigen과 subclonal neoantigen은 vaccine 또는 TCR therapy 설계에서 어떻게 다르게 쓰이는가?
9. neoantigen quality를 평가하는 논문들은 binding affinity 외에 어떤 feature를 강조하는가?
10. proximal variant 또는 peptide context가 neoepitope prediction을 어떻게 바꾸는가?
11. HLA typing 불확실성은 neoantigen ranking에 어떤 오류를 만들 수 있는가?
12. HLA loss 또는 allele-specific HLA loss가 neoantigen therapy의 실패와 어떻게 연결되는가?
13. HLA micropolymorphism은 peptide conformation과 TCR selectivity를 어떻게 바꾸는가?
14. MHC-I peptide와 MHC-II peptide의 antigen processing 경로 차이는 후보 검증 실험 설계를 어떻게 바꾸는가?
15. immunopeptidomics 논문들은 peptide-spectrum match의 false discovery를 어떻게 통제하는가?
16. tumor mutanome-guided immunopeptidomics는 일반 immunopeptidomics보다 어떤 민감도를 얻는가?
17. noncanonical ORF 기반 antigen discovery에서 번역 증거는 어떤 수준까지 필요하다고 보는가?
18. BamQuery, iPepGen, moPepGen 같은 pipeline은 서로 어떤 단계에서 차별화되는가?
19. neoantigen prediction algorithm 비교 논문에서 가장 자주 실패하는 조건은 무엇인가?
20. AI 기반 neoantigen predictor는 어떤 입력 feature를 추가하면서 기존 binding model을 넘어서는가?
21. neoantigen-specific T cell response를 확인하는 functional assay는 어떤 종류가 있는가?
22. fresh tumor TIL에서 neoantigen-reactive T cell을 찾는 phenotypic signature는 얼마나 재현되는가?
23. tetramer, ELISpot, activation-induced marker, TCR sequencing은 각각 어떤 검증 질문에 적합한가?
24. CD8 T cell neoantigen response와 CD4 T cell neoantigen response는 임상적 의미가 어떻게 다른가?
25. cytotoxic CD4 T cell이 보고된 암종에서는 MHC-II antigen presentation을 어떻게 해석해야 하는가?
26. neoantigen-specific TCR의 affinity 향상은 efficacy와 off-target risk 사이에서 어떤 trade-off를 만든다?
27. public neoantigen과 private neoantigen은 치료 개발 경로가 어떻게 달라지는가?
28. KRAS, TP53, PIK3CA 같은 recurrent mutation neoantigen은 어떤 HLA 제한 조건 때문에 확장성이 제한되는가?
29. shared neoantigen vaccine은 personalized vaccine보다 어떤 임상 운영 장점과 생물학적 한계를 갖는가?
30. neoantigen vaccine에서 adjuvant 선택은 T cell quality를 어떻게 바꾸는가?
31. mRNA-LNP, peptide, viral vector, nanoparticle vaccine platform은 antigen delivery와 면역 지속성에서 어떻게 다른가?
32. personalized vaccine trial들은 후보 선정부터 투여까지의 turnaround time을 어떻게 줄였는가?
33. checkpoint blockade와 neoantigen vaccine 병용은 priming, expansion, exhaustion 중 어느 단계를 주로 보완하는가?
34. pembrolizumab, atezolizumab 등 ICI 병용 trial에서 response와 neoantigen-specific immunity는 얼마나 직접 연결되는가?
35. neoadjuvant와 adjuvant setting에서 neoantigen vaccine의 목표 endpoint는 어떻게 다른가?
36. low-TMB 암종에서 neoantigen vaccine은 어떤 방식으로 “antigen scarcity”를 우회하는가?
37. “neoantigen load”와 “neoantigen quality”는 TLS/B-cell biology와 어떤 경로로 연결될 수 있는가?
38. B cell이 neoantigen을 인지한다는 증거는 항체(serology) 기반인가, BCR 기반인가, 기능 기반인가?
39. tumor-reactive antibody가 실제 tumor control에 기여하는가, 바이오마커인가?
40. intratumoral B cell의 항원 특이성은 tumor antigen, 바이러스 항원, 자가항원 중 어디에 더 치우치는가?
41. TLS 안에서 germinal center 반응은 neoantigen-driven selection을 의미하는가?
42. antigen-specific B cell을 찾기 위한 실험(antigen bait, single-cell BCR)에서 가장 큰 기술 병목은 무엇인가?
43. TLS maturity(예: GC marker)와 ICI response의 관계는 암종마다 일관적인가?
44. TLS density와 TLS function(활성/비활성)을 구분하는 가장 좋은 proxy는 무엇인가?
45. CXCL13 axis는 TLS 유도에서 충분조건인가 필요조건인가?
46. TLS 유도 전략(방사선, STING agonist, cytokine engineering)은 어떤 부작용/역효과를 갖는가?
47. TLS가 오히려 면역억제 niche가 되는 사례(Breg, IgA) 는 어떻게 구분하는가?
48. Breg의 표지자/정의는 논문마다 어떻게 달라져 비교를 어렵게 만드는가?
49. plasma cell vs memory B cell 역할을 구분하는 기능적 근거는 무엇인가?
50. class-switch(예: IgG/IgA) 패턴이 “항암 면역”인지 “면역억제”인지 어떻게 해석되는가?
51. 공간적으로 TLS가 종양 내부/경계/주변에 위치할 때 기능이 달라지는가?
52. spatial transcriptomics는 TLS 기능을 어떤 관점에서 정량화할 수 있는가?
53. neoantigen vaccine trial에서 B cell/TLS 관련 readout이 포함된 사례는 무엇인가?
54. humoral response를 측정했지만 효능과 연결되지 않은 사례는 무엇인가?
55. 항원 제시(APC)로서의 B cell 역할은 종양 환경에서 어느 정도 입증되었는가?
56. MHC-II 발현(종양/면역세포)의 손실은 B cell 도움과 어떻게 연결되는가?
57. antigen presentation defect(B2M/HLA)와 TLS/B cell signature가 공존하는 상황은 가능한가?
58. tumor antigen이 사라지는 경우(antigen loss)와 TLS가 유지되는 경우를 어떻게 설명할 수 있는가?
59. “공유 neoantigen”이 B cell/TLS 반응을 더 잘 유도할 수 있다는 근거가 있는가?
60. shared neoantigen이 오히려 central tolerance/자가반응 위험을 키우는가?
61. cryptic peptide(TE-derived, lncRNA, intronic) 는 B cell이 표적하기 더 쉬운가 어려운가?
62. noncanonical peptide는 T cell과 B cell 사이에서 어떤 “검증 격차”가 더 큰가?
63. immunopeptidomics로 확인된 antigen과 serology로 확인된 antigen이 일치하지 않는 경우는 얼마나 흔한가?
64. 항체 epitope(구조 epitope)와 MHC epitope(선형 peptide)는 같은 항원을 공유해도 다른 면역 경로를 만들 수 있는가?
65. neoantigen-specific T cell이 존재해도 종양이 제거되지 않는 경우, TLS/B cell은 어떤 역할을 할 수 있는가?
66. epitope spreading은 TLS 존재와 어떤 관계가 있는가?
67. vaccine로 유도된 면역이 tumor microenvironment로 침투하지 못하는 병목은 무엇인가?
68. TLS는 T cell priming의 대체 경로인가, 증폭 경로인가?
69. ICI가 TLS를 “활성화”하는가, TLS가 ICI에 “반응할 준비”를 만드는가?
70. 항암 치료(화학/표적/방사선)가 TLS를 파괴하는 사례는 어떤 조건에서 나타나는가?
71. anti-CD20이 ICI benefit을 줄이는지에 대한 근거는 일관적인가?
72. B cell depletion이 도움이 되는(면역억제 B cell dominant) 종양 환경은 존재하는가?
73. TLS/B cell biomarker는 pan-cancer로 쓸 수 있는가, 암종별로 재학습이 필요한가?
74. TLS signature가 치료 반응 예측에서 기존 biomarker(TMB/PD-L1)보다 독립적인가?
75. multi-omics(단백질/인산화) 레이어가 TLS 기능을 더 잘 구분할 수 있는가?
76. cytokine network(IL-21, IL-4 등) 변화는 TLS maturation과 어떤 관계가 있는가?
77. follicular helper T cell(Tfh) signature는 TLS 기능의 더 직접적인 proxy인가?
78. tumor mutational process(APOBEC 등)가 neoantigen quality와 TLS 형성 둘 다에 영향을 줄 수 있는가?
79. 바이러스 관련 암에서 TLS/neoantigen 논리는 어떻게 달라지는가?
80. HERV/retroelement antigen은 TLS/B cell 반응과 연결될 수 있는가?
81. B cell이 인지하는 항원이 “neoantigen”이 아닐 때도 TLS가 항암 예후를 개선할 수 있는가?
82. TLS는 단순히 immune infiltration의 proxy인가, 독립적인 기능 단위인가?
83. “mature TLS”의 최소 기준은 무엇이며 논문마다 어떻게 다르게 정의되는가?
84. TLS를 유도하는 intervention의 성공/실패를 판단하는 최소 readout은 무엇인가?
85. TLS 유도와 neoantigen vaccine을 병용할 때 가장 큰 위험(면역관련 부작용)은 무엇인가?
86. personalized neoantigen vaccine에서 후보 수를 늘리는 전략은 TLS/B cell 반응에 어떤 영향을 줄까?
87. 후보 수를 늘리면 면역 분산(immune dilution)이 생기는가?
88. vaccine platform이 B cell 반응(항체/GC) 유도에 미치는 차이는 무엇인가?
89. adjuvant가 humoral arm을 과도하게 자극할 때 생길 수 있는 부정적 결과는 무엇인가?
90. neoantigen-specific antibody가 치료에 직접 쓰이려면(단클론 항체) 어떤 조건이 필요한가?
91. B cell/TLS 논문에서 “항원 특이성”을 뒷받침하는 가장 강한 증거는 무엇인가?
92. 현재 위키에서 neoantigen discovery와 TLS biology 사이의 가장 약한 연결고리는 무엇인가?
93. 다음 ingest batch에서 B cell/TLS와 neoantigen specificity를 동시에 다루는 논문을 어떻게 우선순위화할 것인가?
94. 이 주제를 한 장짜리 그림으로 그릴 때 discovery→context→translation 흐름을 어떻게 배치할 것인가?
95. 이 토픽에서 반드시 만들어야 할 표준 비교표(논문별)를 어떤 컬럼으로 구성할 것인가?
96. 이 토픽의 “핵심 긴장(tension)” 3가지는 무엇인가?
97. neoantigen quality vs quantity 중 어느 쪽이 TLS와 더 강하게 연결될까?
98. TLS가 강하지만 ICI에 실패하는 경우의 대표 메커니즘 family 5개는 무엇인가?
99. 이 토픽의 최종 synthesis는 discovery, context, translation 중 어느 축을 중심 narrative로 삼을 것인가?
100. 이 topic을 처음 읽는 사람이 마지막에 설명할 수 있어야 하는 핵심 모델은 무엇인가?

## Topic 2: Immunotherapy Resistance and Immune Evasion (100)

1. primary resistance와 acquired resistance는 각 논문에서 어떤 기준으로 구분되는가?
2. response, stable disease, hyperprogression, relapse를 다루는 endpoint 정의는 논문마다 어떻게 다른가?
3. tumor-intrinsic resistance와 microenvironment-mediated resistance를 가르는 근거는 무엇인가?
4. immunotherapy resistance를 checkpoint blockade, CAR-T, bispecific, ADC, targeted therapy 이후 immune remodeling으로 나누면 어떤 지도가 생기는가?
5. cancer-immunity cycle의 어느 단계가 각 resistance mechanism에서 막히는가?
6. immune set point 개념은 single biomarker보다 어떤 설명력을 주는가?
7. TMB, PD-L1, MSI-H, dMMR, IFN signature 중 어떤 biomarker가 어떤 상황에서 실패하는가?
8. pan-tumor biomarker와 cancer-specific biomarker는 어떤 조건에서 충돌하는가?
9. 같은 biomarker-positive tumor 안에서 response heterogeneity가 생기는 이유는 무엇인가?
10. resistance 논문에서 pre-treatment sample과 on-treatment sample의 해석 차이는 무엇인가?
11. B2M loss, HLA loss, antigen processing defect는 ICI resistance에서 어떻게 구분되는가?
12. allele-specific HLA loss는 neoantigen burden이 높은 tumor에서 어떤 immune escape 경로를 만든다?
13. JAK1/2 mutation과 IFN pathway defect는 tumor killing과 antigen presentation을 각각 어떻게 방해하는가?
14. MHC-I downregulation이 genetic loss인지 reversible suppression인지 구분하려면 어떤 evidence가 필요한가?
15. autophagy-mediated MHC-I degradation은 classical antigen presentation defect와 어떻게 다르게 해석되는가?
16. epigenetic silencing of MHC-I 또는 retroelement suppression은 어떤 치료 조합으로 되돌릴 수 있는가?
17. 9p21 alteration, STING suppression은 immune-cold tumor와 어떻게 연결되는가?
18. tumor antigen loss와 antigen presentation loss는 치료 선택에서 어떻게 다른 문제인가?
19. antigen escape 이후 CD8 T cell response가 유지되는지 붕괴되는지 어떻게 확인하는가?
20. acquired ICI resistance에서 neoantigen loss와 immune exhaustion 중 무엇이 더 직접적인 driver인가?
21. CD19 CAR-T resistance에서 antigen mutation, alternative splicing, lineage switch는 어떻게 다르게 발생하는가?
22. lineage switch는 selection된 pre-existing clone인가, therapy-induced plasticity인가?
23. CAR-T exhaustion, trafficking failure, persistence failure는 어떤 assay로 구분되는가?
24. solid tumor CAR-T에서 physical barrier와 antigen heterogeneity 중 어느 쪽이 더 큰 병목인가?
25. armored CAR(IL-12/IL-18 등)는 어떤 resistance layer를 해결하려는가?
26. BCMA-targeted therapy에서 antigen density와 soluble antigen은 efficacy를 어떻게 바꾸는가?
27. bispecific antibody는 CAR-T와 비교해 target loss에 더 강한가 약한가?
28. BsAb에서 T cell fitness, exhaustion, cytokine toxicity는 어떻게 trade-off를 만든다?
29. hematologic malignancy와 solid tumor에서 T-cell redirection resistance는 어떤 구조적 차이를 보이는가?
30. ADC는 target expression의 “binary 기준”을 어떻게 무너뜨렸는가?
31. ADC resistance에서 target loss와 payload resistance는 어떻게 구분되는가?
32. ADC bystander effect는 heterogeneity 문제를 얼마나 보완하는가?
33. ADC 치료가 antigen release/IFN signaling을 통해 ICI와 연결될 수 있는가?
34. EGFR-mutant NSCLC에서 ICI benefit이 낮은 이유는 어디에 더 가까운가(TMB, TME, oncogene signaling)?
35. EGFR TKI failure 이후 tumor microenvironment는 어떤 방향으로 재편되는가?
36. KRAS G12C inhibitor resistance는 tumor-intrinsic adaptation과 immune ecosystem change를 어떻게 동시에 만든다?
37. STK11/LKB1 mutation은 PD-1 resistance를 어떤 immune axis로 설명하는가?
38. KEAP1/NFE2L2 축은 면역억제/대사 재편과 어떻게 연결되는가?
39. TGF-β driven immune exclusion은 어떤 tumor class에서 가장 반복적으로 관찰되는가?
40. CAF/myeloid barrier는 원인인가 결과인가(인과 방향을 어떻게 판단할 것인가)?
41. gut microbiota와 ICI response는 재현성이 얼마나 강하며 어떤 메커니즘이 가장 견고한가?
42. hyperprogression은 독립적 생물학인가, 측정/선택 편향인가?
43. immunotherapy 후 “immune editing”은 어떤 수준(클론/항원/세포상태)에서 관찰되는가?
44. tumor mutational process(APOBEC 등)가 resistance와 연결되는 경로는 무엇인가?
45. epigenetic therapy가 immune visibility를 회복한다는 주장은 어떤 조건에서 성립하는가?
46. antigen presentation 회복을 목표로 하는 치료 조합은 어떤 것들이 있는가?
47. interferon pathway를 강화하는 전략은 종양 성장도 함께 촉진할 수 있는가?
48. myeloid targeting(CSF1R 등)은 왜 임상에서 자주 실패하는가?
49. TGF-β blockade가 임상에서 실패한 사례에서 핵심 실패 원인은 무엇인가?
50. immune checkpoint가 아닌 metabolic checkpoint(adenosine, tryptophan 등)는 resistance에서 어떤 비중을 갖는가?
51. hypoxia는 immune exclusion과 어떤 방식으로 연결되는가?
52. vascular normalization(anti-angiogenic)과 ICI 병용은 어떤 조건에서 효과적인가?
53. antigen density를 올리는 전략(표적 증가)은 실제로 가능한가?
54. bispecific/ADC에서 target heterogeneity는 어떤 threshold에서 치명적인가?
55. CAR-T에서 persistence를 늘리면 toxicity와 어떤 trade-off가 생기는가?
56. CAR-T/BsAb의 공통 실패 축(antigen/effector/traffic)은 무엇인가?
57. “effector dysfunction”을 T cell intrinsic과 extrinsic으로 나누면 어떤 분류가 되는가?
58. PD-1/CTLA4 외 checkpoint axis(LAG3, TIGIT 등)는 resistance를 어떻게 설명하는가?
59. co-inhibitory receptors는 원인인가, 이미 실패한 면역의 결과 표지자인가?
60. “immune cold”가 단일 상태가 아니라면 가장 실용적인 세부 분류는 무엇인가?
61. 병용요법이 실패한 경우, 실패의 원인을 어떤 축(visibility/access/effector)로 기록할 것인가?
62. “visibility”를 올리는 조합(방사선/바이러스 등)은 어떤 부작용을 유발하는가?
63. “access”를 올리는 조합(ECM/혈관)은 어떤 바이오마커로 선택해야 하는가?
64. “effector”를 올리는 조합(IL-2/IL-15 등)은 어떤 안전성 문제가 있는가?
65. acquired resistance에서 종양이 택하는 가장 흔한 “cost-effective” 전략은 무엇인가?
66. primary resistance에서 종양이 이미 갖고 있는 “baseline immune escape”의 대표 패턴은 무엇인가?
67. single-cell/spatial이 resistance 해석을 실제로 바꿔놓은 대표 사례는 무엇인가?
68. bulk 기반 signature는 어떤 조건에서 충분하고, 어떤 조건에서 반드시 single-cell/spatial이 필요한가?
69. 같은 암종에서도 치료 라인/이전 치료가 면역 상태를 얼마나 바꾸는가?
70. steroids/antibiotics 같은 동반 약물이 ICI 결과에 미치는 영향은 어느 정도까지 조정되었는가?
71. tumor mutational burden가 높지만 ICI에 실패하는 대표 설명은 무엇인가?
72. PD-L1이 높지만 실패하는 대표 설명은 무엇인가?
73. MSI-H인데 실패하는 경우의 대표 메커니즘은 무엇인가?
74. organ-specific immune context(간/뇌 등)가 resistance를 결정하는 사례는 무엇인가?
75. metastasis site별로 immune escape가 다르다는 근거는 얼마나 강한가?
76. circulating biomarkers(ctDNA, proteomics)은 resistance 조기 탐지에 쓸 수 있는가?
77. neoantigen 변화 추적을 resistance monitoring에 쓰려면 무엇이 필요할까?
78. antigen presentation loss를 치료 중 모니터링할 수 있는 방법은 무엇인가?
79. immune-related adverse event(irAE)와 efficacy는 항상 같이 가는가?
80. toxicity를 줄이면서 efficacy를 유지하는 공학적/임상적 전략은 무엇인가?
81. resistance를 줄이기 위해 치료 순서를 바꾸는 전략(priming→ICI)은 어떤 근거가 있는가?
82. “priming failure” vs “exhaustion”을 구분하는 최소 지표는 무엇인가?
83. tumor antigenicity를 높이는 전략(예: epigenetic reactivation)은 언제 도움이 되는가?
84. STING agonist는 왜 사람에서 어려운가(전달/독성/효과)?
85. oncolytic virus는 어떤 조건에서 작동하고 왜 자주 실패하는가?
86. IL-12 같은 강한 cytokine 전략이 다시 부상하려면 무엇이 필요할까?
87. tumor-intrinsic oncogenic signaling이 면역회피를 구동하는 대표 축은 무엇인가(WNT, MAPK 등)?
88. EMT/plasticity는 면역회피의 원인인가 결과인가?
89. lineage plasticity는 면역세포 치료(CAR-T/BsAb)에서 왜 치명적인가?
90. antigen loss가 reversible adaptation일 수 있는 조건은 무엇인가?
91. antigen loss가 clonal selection일 수 있는 조건은 무엇인가?
92. 치료 전부터 존재하는 minor clone이 치료 후 지배하는 시나리오는 어떤 데이터로 확인되는가?
93. resistance 논문을 위키로 정리할 때 최소 메타데이터(치료제/암종/endpoint/시점)는 무엇인가?
94. resistance를 한 장짜리 그림으로 그릴 때 visibility/access/effector는 어떻게 배치하는가?
95. 이 토픽에서 만들어야 할 “표준 메커니즘 taxonomy”는 어떤 구조가 좋은가?
96. 위키에서 가장 먼저 확장해야 할 concept page 5개는 무엇인가?
97. 현재 위키에서 가장 약한 연결(빈 링크)은 어떤 메커니즘 축에 있는가?
98. 다음 ingest batch에서 clinical trial, mechanism paper, review paper의 비율을 어떻게 잡을 것인가?
99. 이 주제를 교수진/공동연구자에게 공유할 때 어떤 3문장 구조가 가장 효과적인가?
100. 이 topic을 읽은 사람이 최종적으로 설명해야 하는 resistance logic은 무엇인가?

## Topic 3: Multiomics Proteomics PTM Identification (100)

1. proteome identification count는 protein, protein group, gene product 중 어떤 단위로 보고되었는가?
2. phosphoproteome identification count는 phosphosite, localized site, phosphopeptide, phosphospectrum 중 무엇을 의미하는가?
3. acetylome identification count는 acetylsite, acetylated peptide, lysine acetylation event 중 어떤 단위를 쓰는가?
4. 단백체, 인산화체, 아세틸체 count를 한 그래프에 놓을 때 어떤 단위 변환을 하면 안 되는가?
5. main text와 supplementary table의 identification count가 다를 때 어떤 값을 우선해야 하는가?
6. localized site probability threshold는 phosphosite count를 얼마나 바꿀 수 있는가?
7. peptide-level FDR과 protein-level FDR은 reported count 해석에 어떤 차이를 만든다?
8. missing value 처리와 quantifiable feature 기준은 identification count와 어떻게 다르다?
9. cohort-level total identification과 per-sample median identification은 어떤 질문에 각각 적합한가?
10. pan-cancer compendium의 pooled count는 single cancer cohort count와 직접 비교 가능한가?
11. 2016-2026 인간 암 proteogenomic 연구에서 가장 반복적으로 등장하는 cancer type은 무엇인가?
12. CPTAC-style cohort와 single-institution cohort는 sample processing과 count scale에서 어떻게 다른가?
13. FFPE, fresh frozen, cell line, organoid, PDX sample은 MS depth에 어떤 영향을 준다?
14. tumor purity와 stromal content는 proteome identification과 quantification 해석을 어떻게 바꾼다?
15. paired normal tissue가 있는 연구와 tumor-only 연구는 baseline 해석이 어떻게 다른가?
16. sample amount가 적은 연구는 어떤 enrichment 또는 fractionation trade-off를 선택하는가?
17. clinical cohort size와 MS depth 사이에는 어떤 실험 설계 trade-off가 보이는가?
18. longitudinal 또는 treatment-response cohort는 baseline atlas cohort와 count reporting 방식이 다른가?
19. tumor subtype discovery 논문과 therapeutic vulnerability 논문은 어떤 omics layer를 더 강조하는가?
20. multi-region sampling 연구는 identification count보다 heterogeneity map을 더 중요하게 다루는가?
21. TMT, iTRAQ, label-free, DIA는 multiplexing, missingness, quantification accuracy에서 어떻게 다른가?
22. TMT 10/11/16/18-plex 발전은 cohort proteomics throughput을 어떻게 바꾸었는가?
23. ratio compression 문제는 TMT 기반 cancer proteomics의 biological interpretation에 어떤 영향을 준다?
24. carrier/reference channel design은 cross-batch 비교를 어떻게 가능하게 하는가?
25. iTRAQ 기반 초기 연구와 TMT 기반 후속 연구는 depth와 reproducibility에서 어떻게 달라졌는가?
26. DIA는 DDA 대비 identification과 quantification completeness에서 어떤 장점을 갖는가?
27. library-based DIA와 library-free DIA는 cancer cohort 분석에서 어떤 trade-off가 있는가?
28. BoxCar, gas-phase fractionation, high-pH fractionation 같은 전략은 depth를 어떻게 올리는가?
29. fractionation 수가 증가하면 identification count와 clinical scalability는 어떻게 교환되는가?
30. phosphoproteome과 acetylome을 동시에 측정할 때 sample split은 어떤 bias를 만들 수 있는가?
31. phosphopeptide enrichment에는 IMAC, TiO2, Fe-NTA, PolyMAC 등이 어떻게 쓰이는가?
32. mono-phosphopeptide와 multi-phosphopeptide 분리는 signaling 해석에 어떤 의미가 있는가?
33. acetyl-peptide enrichment는 anti-acetyl-lysine antibody 의존성 때문에 어떤 bias를 갖는가?
34. PTM enrichment 효율은 reported site count와 biological absence를 구분하기 어렵게 만드는가?
35. enrichment 후 LC-MS/MS instrument time은 phosphosite depth를 얼마나 좌우하는가?
36. global proteome과 PTM layer를 같은 sample에서 측정하지 않았을 때 correction 해석에 어떤 문제가 생기는가?
37. acetylome이 phosphoproteome보다 적게 보고되는 이유는 biology 때문인가, method burden 때문인가?
38. ubiquitinomics, glycoproteomics 등 다른 PTM layer가 포함된 논문은 이 topic에서 어떻게 분류해야 하는가?
39. PTM count가 높아도 site localization이 낮으면 어떤 caveat를 달아야 하는가?
40. PTM identification과 PTM quantification의 차이를 페이지에서 어떻게 시각적으로 구분할 것인가?
41. Orbitrap Fusion, Fusion Lumos, Q Exactive, Exploris, Eclipse, Astral은 어떤 시기와 연구 유형에서 등장하는가?
42. instrument generation 변화는 count 증가와 얼마나 직접적으로 연결되는가?
43. high-field Orbitrap과 ion mobility, FAIMS, Astral-like speed improvement는 PTM depth에 어떤 의미가 있는가?
44. instrument name이 main text에 없고 methods supplement에만 있는 경우 extraction을 어떻게 표준화할 것인가?
45. LC gradient length와 column setup은 identification depth를 어떻게 바꾼다?
46. FAIMS 또는 ion mobility를 쓴 연구는 peptide coverage와 missingness에서 어떤 이득을 보고하는가?
47. DDA의 stochastic sampling은 cohort-wide missingness를 어떻게 만드는가?
48. DIA는 phosphoproteome에서도 동일하게 유리한가?
49. single-shot proteomics와 deep fractionated proteomics는 atlas 구축 목적이 어떻게 다른가?
50. limited sample workflow는 deep atlas workflow와 어떤 다른 질문에 최적화되는가?
51. database search engine 선택은 identification count에 얼마나 영향을 준다?
52. MaxQuant, Proteome Discoverer, MSFragger, SpectroMine, DIA-NN, FragPipe는 어떤 데이터 유형에 자주 쓰이는가?
53. search space에 variant peptide, fusion peptide, noncanonical ORF가 포함되면 FDR control은 어떻게 어려워지는가?
54. open search 또는 spectral library search는 PTM discovery에 어떤 기회를 준다?
55. phosphosite annotation은 UniProt, PhosphoSitePlus, kinase-substrate DB와 어떻게 연결되는가?
56. acetylsite annotation은 histone vs non-histone을 어떻게 나눠야 하는가?
57. batch correction과 normalization은 count보다 biological clustering에 더 큰 영향을 주는가?
58. bridge/reference pool이 없는 연구는 cross-cohort 비교에서 어떤 한계를 갖는가?
59. multi-omics integration 전에 layer별 missingness/depth 차이를 어떻게 표시해야 하는가?
60. supplement table extraction을 자동화할 때 units, sheet names, abbreviations를 어떻게 기록해야 하는가?
61. genome, transcriptome, proteome, phosphoproteome, acetylome이 함께 있을 때 가능한 질문은 무엇인가?
62. copy number alteration이 protein abundance로 전달되는 정도는 cancer type마다 어떻게 다른가?
63. RNA-protein discordance는 proteogenomic study에서 어떤 insight로 해석되는가?
64. driver mutation이 phosphoproteome 또는 kinase activity로 이어지는 사례는 무엇인가?
65. acetylome은 chromatin/metabolism/mitochondria 중 어떤 축을 더 잘 보여주는가?
66. proteome-only subtype과 phosphoproteome-informed subtype은 환자 분류를 어떻게 다르게 만든다?
67. phosphoproteome은 druggable kinase pathway를 어떻게 드러내는가?
68. acetylome은 epigenetic regulator와 metabolic enzyme을 어떻게 연결하는가?
69. supervised clinical outcome model과 unsupervised subtype model은 목적이 어떻게 다른가?
70. pan-cancer clustering에서 tissue of origin과 molecular state를 어떻게 분리할 수 있는가?
71. identification count가 높은 논문이 반드시 더 좋은 biological insight를 주는가?
72. count가 낮지만 perturbation design인 논문은 어떤 가치가 있는가?
73. cohort atlas 논문과 cell-line perturbation 논문은 같은 visualization에 넣을 때 어떻게 구분해야 하는가?
74. sample 수와 feature 수를 동시에 보여주는 plot은 어떤 해석을 가능하게 하는가?
75. method/instrument/enrichment/count를 함께 보여줄 때 가장 이해하기 쉬운 시각화 구조는 무엇인가?
76. 연도별 기술 발전을 보여주는 plot은 count 증가와 method adoption을 어떻게 분리해야 하는가?
77. cancer type별 proteome/phospho/acetyl coverage gap은 어떤 ingest 우선순위를 만든다?
78. acetylome 포함 연구가 적다면 methods-level explanation을 별도 section으로 써야 하는가?
79. 2024-2026 흐름(DIA, Astral, single-cell/spatial)은 어떻게 등장하는가?
80. foundation model/ML integration은 atlas에서 어떤 downstream task에 쓰이는가?
81. human cancer 대상이 아닌 method paper는 support source로 남길 것인가 제외할 것인가?
82. review 논문은 count source가 아니라 method context로만 써야 하는가?
83. raw PDF만 있고 source page가 약한 논문은 어떤 extraction checklist로 보강해야 하는가?
84. supplement(Excel/PRIDE)가 필요한 논문은 ingest status를 어떻게 표시해야 하는가?
85. inaccessible supplement는 visualization에서 어떤 caveat로 처리해야 하는가?
86. 같은 논문 내에서 proteome vs phospho vs acetyl count의 정의가 뒤섞일 때 어떻게 정리할까?
87. “quantified”와 “identified”를 혼용하는 논문은 어떻게 구분해 기록할까?
88. protein group vs gene-level abundance를 동일 축에 놓을 수 있는가?
89. phosphosite count가 “localized”인지 여부를 어떻게 표준화할까?
90. LC/MS 기기 업그레이드가 sample 처리량과 어떻게 연결되는가?
91. “많이 식별했다”보다 중요한 method quality indicator는 무엇인가?
92. reproducibility, missingness, batch correction, clinical scalability를 한 페이지에 어떻게 같이 설명할 것인가?
93. 현재 위키에서 identification count와 biological interpretation 사이의 연결이 약한 지점은 어디인가?
94. 각 source page의 `Multi-Omics Identification Extraction` 섹션을 표준화하려면 어떤 fields가 필수인가?
95. `interactives/.../data/studies.json`과 source page 사이 provenance를 어떻게 검증할 것인가?
96. 같은 논문의 duplicate source page가 있을 때 어떤 canonical page를 유지할 것인가?
97. 다음 ingest batch는 cancer cohort diversity와 method diversity 중 무엇을 우선해야 하는가?
98. 최종 synthesis는 기술 발전사, cancer biology map, visualization atlas 중 무엇을 중심으로 구성해야 하는가?
99. 교수님께 공유할 때 가장 먼저 보여줘야 하는 plot과 가장 먼저 읽혀야 하는 explanation은 무엇인가?
100. 독자가 methods를 읽고 스스로 count/method caveat를 판단하려면 무엇을 알아야 하는가?

## Topic 4: Cancer Multiomics Literature Monitor (100)

1. 이 논문이 다루는 임상 맥락은 무엇인가(암종, 치료제 class, 라인, 반응 라벨)?
2. primary resistance와 acquired resistance를 논문은 어떤 기준으로 구분하는가(시간/시점/정의)?
3. 샘플링 시점(pre/on/post)과 바이옵시 위치/방법이 결과 해석에 어떤 제약을 만드는가?
4. WGS/WES에서 변이 범위를 어디까지 포함하는가(SNV/indel/CNV/SV/noncoding/germline)?
5. HLA typing은 어떤 입력과 도구로 수행했는가(정확도/불확실성 근거 포함)?
6. neoantigen을 다루는가? 다룬다면 prediction-only인가, immunopeptidomics/proteogenomics 검증이 있는가?
7. neoantigen 후보 필터는 무엇인가(binding, expression, clonality, processing, stability, RT prediction)?
8. MHC-I와 MHC-II를 분리해 분석하는가? 분리하지 않으면 어떤 위험이 생기는가?
9. immune evasion feature를 어떤 층에서 측정/추정하는가(HLA LOH, B2M, JAK/IFN, antigen processing 등)?
10. proteogenomics/phosphoproteomics 레이어가 있으면 측정 깊이(단백질/사이트 수)는 어떻게 보고되는가?
11. kinase activity inference를 수행하는가? 방법(KSEA/PTM-SEA/network)과 근거는 무엇인가?
12. protein abundance confounding(PTM correction)을 명시적으로 다루는가? 안 다루면 어떤 caveat를 남길 것인가?
13. multi-omics integration은 어떤 목표로 수행했는가(subtype, driver→state, prediction model)?
14. prediction model이 있으면 학습/검증 설계는 무엇인가(외부 검증, CV, prospective)?
15. feature importance/해석(SHAP 등)을 제공하는가? 제공한다면 어떤 레이어가 상위에 오는가?
16. 데이터 레이어의 공개 수준은 무엇인가(raw/processed/supplement/portal/code)?
17. 재현을 위해 꼭 필요한 파일/파라미터가 공개되었는가?
18. cohort 규모와 MS depth 사이의 trade-off를 논문은 어떻게 설계했는가?
19. 샘플 준비(FFPE/frozen), 라벨링(TMT/DIA), enrichment(IMAC 등), 기기(instrument)는 무엇인가?
20. tumor purity/immune infiltration 조정은 어떤 방식으로 했는가(병리/추정/모델)?
21. immune-hot/cold 정의는 무엇인가(GEP/CD8/IFN/TIL/단백질 면역마커)?
22. proteomics가 transcriptome 대비 제공하는 추가 설명력은 무엇이라고 주장하는가?
23. phosphoproteome이 면역 상태와 연결된다고 주장하면 어떤 경로/모듈을 제시하는가?
24. 표적치료 맥락에서 kinase activation mode를 어떻게 구분하는가(리간드, mutation, phosphorylation)?
25. 치료 전 상태(baseline) vs 치료 후 상태(on-treatment)에서 어떤 레이어가 가장 크게 변하는가?
26. longitudinal 샘플이 있으면 내성을 어떤 레이어 변화로 설명하는가(유전 선택, signaling rewiring, immune remodeling)?
27. neoantigen burden/quality 변화가 내성과 연결된다고 주장하는가? 근거는 무엇인가?
28. immunopeptidomics가 있으면 peptide 검출 FDR/검증을 어떻게 통제하는가?
29. variant peptide(proteogenomics) 탐지가 있으면 search space/FDR 문제를 어떻게 다루는가?
30. 공유 neoantigen(shared)을 주장하면 HLA 제한 조건과 확장성 제약은 무엇인가?
31. WGS 기반 neoantigen prediction이 임상 표적이 되려면 어떤 추가 실험이 필요하다고 말하는가?
32. 환자 분류(subtype)에서 유전체 기반 vs 단백질/인산화 기반 subtype은 어떤 차이를 보이는가?
33. driver가 같아도 단백질/인산화 상태가 달라지는 사례를 논문은 보여주는가?
34. ppQTL/pQTL을 보고하는가? 있다면 cis/trans와 해석은 무엇인가?
35. ppQTL이 면역 phenotype 또는 치료 반응과 연결되는가?
36. 데이터가 공용 코호트(CPTAC 등)인가, 기관 코호트인가, 임상시험 코호트인가?
37. 임상시험 코호트라면 arm/병용/라인 구성과 라벨 정의는 무엇인가?
38. MSI-H/dMMR 같은 특수 집단은 별도로 다루는가(heterogeneity 관점 포함)?
39. HLA LOH/antigen presentation loss를 WGS만으로 추정하는가, 단백질/표현형 근거가 있는가?
40. immune exclusion(TGF-β/ECM/CAF) 신호를 어떤 레이어로 측정하는가?
41. myeloid suppression(MDSC/TAM) 관련 신호는 어떤 근거로 제시되는가?
42. T cell exhaustion signature는 어떤 층에서 측정되는가(전사체/단백질/기능)?
43. B cell/TLS 시그니처가 feature로 등장하는가? 등장한다면 어떤 근거가 가장 강한가?
44. 논문이 TLS/neoantigen을 직접 다루지 않으면, 위키에서 어떤 연결은 “추론”으로만 남겨야 하는가?
45. signaling 결과가 타깃 제안으로 이어질 때 약물 가능성/임상 근거를 무엇으로 판단할 것인가?
46. 내성 기전 주장에 대해 “관찰 기반”과 “인과 기반(perturbation)”을 어떻게 분리해 기록할 것인가?
47. 한 논문에서 endpoint(생존/반응/재발)가 여러 개인 경우, Cancer Multiomics 요약은 무엇을 우선할까?
48. Cancer Multiomics 과제 deliverable(예측모델/바이오마커/통합 파이프라인) 중 어디에 직접 연결되는가?
49. Slack 공유용 “한 줄 요약”에 꼭 포함해야 하는 요소는 무엇인가(암종/레이어/핵심 주장)?
50. Slack 메시지는 어떤 구조(문제→핵심 결과→과제 연결)가 가장 전달력이 좋은가?
51. “당장 적용 가능한 아이디어” 1개를 뽑는 기준은 무엇인가?
52. “조심해야 할 caveat” 1개를 뽑는 기준은 무엇인가?
53. 수치(단백질 수/사이트 수/샘플 수)가 main vs supplement에서 다르면 어떤 값을 택할 것인가?
54. Cancer Multiomics 표준 추출 체크리스트에 포함해야 할 최소 필드는 무엇인가(치료/레이어/공개/방법)?
55. 논문을 읽고 반드시 업데이트해야 하는 페이지는 무엇인가(토픽 허브, 소스 페이지, 컨셉 페이지)?
56. Cancer Multiomics 하위 페이지와 source page 사이의 역할 분리를 어떻게 유지할 것인가?
57. source page에 “Cancer Multiomics relevance”를 추가할지, 하위 페이지만 유지할지 어떤 기준으로 결정할까?
58. “high-impact” 기준을 Cancer Multiomics 모니터링에서 어떻게 operationalize 할까(저널/데이터/임상 연결)?
59. WGS-only 논문과 proteogenomics/phosphoproteomics 논문을 같은 큐에서 어떻게 우선순위화할까?
60. 파이프라인/방법론 논문(neoantigen pipeline 등)은 어떤 추가 메타를 템플릿에 넣어야 할까?
61. WGS feature와 proteomics feature 통합에서 leakage/overfitting 위험을 어떻게 점검할까?
62. 모델이 batch를 학습하는 위험을 논문은 어떻게 회피했는가(또는 회피하지 못했는가)?
63. response prediction에서 “설명가능성”을 주장할 때 어떤 검증이 있어야 하는가?
64. kinase activity feature는 protein confounding 통제를 어떻게 요구하는가?
65. neoantigen feature는 어떤 ground truth 문제를 갖는가(검증 부재, 정의 불일치)?
66. immune composition feature는 원자료(IHC/flow)와의 일치 여부를 확인했는가?
67. small-n/high-p 문제에서 논문은 어떤 차원축소/정규화 전략을 쓰는가?
68. multi-omics layer 간 missingness가 다를 때 통합 모델은 어떻게 구성하는가?
69. sample type(FFPE)과 turnaround time은 임상 적용에 어떤 제약을 만드는가?
70. clinical phosphoproteomics를 routine으로 쓰기 위한 핵심 병목은 무엇인가(sample amount, enrichment reproducibility 등)?
71. Cancer Multiomics 과제에서 추가로 확보해야 할 데이터 레이어는 무엇인가(immunopeptidomics/spatial 등)?
72. WGS만으로 약한 질문을 phosphoproteome이 어떻게 보완할 수 있는가?
73. phosphoproteome만으로 약한 질문을 WGS가 어떻게 보완할 수 있는가?
74. 논문 subtype이 실제 치료 선택으로 이어지려면 어떤 단계가 필요한가?
75. 논문 표적/바이오마커가 과제에서 재현 가능한지 판단하는 기준은 무엇인가?
76. 공개 데이터로 “Cancer Multiomics 파일럿 재분석”이 가능한가? 무엇이 부족한가?
77. 재분석을 한다면 가장 먼저 재현해야 할 figure/table은 무엇인가?
78. 재분석을 위해 우선 확인해야 할 supplement/데이터 가용성 단서는 무엇인가?
79. 같은 결론을 유전체와 단백질/인산화로 각각 주장할 때, 어느 쪽 근거가 더 강한가?
80. 용어(immune-hot, subtype 등)가 논문마다 다른 정의로 쓰일 때 위키는 어떻게 표준화할까?
81. 토픽 허브에서 논문을 어떤 카테고리로 분류하는 것이 좋은가(통합/kinase/neoantigen/모델)?
82. 새로운 논문이 들어오면 기존 seed 중 어떤 것과 먼저 연결할지(“근연” 규칙)는 무엇인가?
83. Cancer Multiomics 하위 페이지 “주요 결과”는 몇 개 bullet이 적정한가?
84. “주요 결과” bullet의 권장 순서는 무엇인가(데이터→핵심 발견→과제 연결→한계)?
85. 교수진 공유에서 디테일 vs 단순화의 균형을 어떻게 잡을까?
86. Slack 메시지에서 피해야 할 표현(과장, 확정 인과)은 무엇인가?
87. 관찰 기반 결과를 전달할 때 “관찰” caveat를 짧게 넣는 문장 패턴은 무엇인가?
88. seed 논문들을 기반으로 Cancer Multiomics 과제 통합 스토리라인 1장을 만들면 어떤 구조가 되는가?
89. 스토리라인에서 WGS, phosphoproteome, neoantigen, immune evasion, prediction은 어떤 순서가 좋은가?
90. 현재 seed 세트에서 가장 비어 있는 축은 무엇인가(임상 반응예측, immunopeptidomics 등)?
91. 다음 ingest는 어떤 축을 먼저 채워야 하는가(예측모델 vs 면역회피 유전기전 vs phosphosignaling)?
92. Cancer Multiomics 토픽이 “읽은 논문 리스트”로만 남지 않게 하려면 어떤 표준 산출물이 필요할까?
93. 한 논문당 표준적으로 남겨야 하는 “Cancer Multiomics relevance” 3줄은 무엇인가?
94. 한 논문당 표준적으로 남겨야 하는 “Methods for reuse” 3줄은 무엇인가?
95. 한 논문당 표준적으로 남겨야 하는 “Data availability” 2줄은 무엇인가?
96. seed 8편 중에서 현재 위키에서 “source page deep-dive가 필요한” 논문은 무엇인가?
97. seed 8편 중에서 현재 위키에서 “Cancer Multiomics 요약 보강이 필요한” 논문은 무엇인가?
98. Cancer Multiomics 토픽 허브에 “표준 체크리스트”를 넣으면 어떤 field가 가장 먼저 도움이 될까?
99. 교수진 Slack 공유용 “주간 digest”를 만들면 어떤 4개 섹션이 좋을까?
100. 이 토픽을 통해 다음으로 만들어야 할 durable 산출물은 무엇인가(체크리스트/메타테이블/재분석 노트)?

### Concrete Growth Targets (Next)

- `wiki/topics/cancer-multiomics-literature.md`에 질문 맵 링크와 표준 추출 체크리스트 추가
- Cancer Multiomics seed 8편의 `wiki/sources/*` Connections에 Cancer Multiomics topic hub 교차 링크 추가
- `wiki/analyses/cancer-multiomics-literature/*`에 “치료 맥락/데이터 레이어/데이터 공개” 표준 bullet 보강
- (분리됨) PTM 보정/kinase 해석 질문 은행: `wiki/analyses/ptm-correction-kinase-signaling-question-bank.md`

## Connections

- [B-Cell Neoantigen Research Map](../topics/b-cell-neoantigen-human-cancer.md)
- [Immunotherapy Resistance and Immune Evasion](../topics/immunotherapy-resistance-and-immune-evasion.md)
- [Multiomics Proteomics PTM Identification](../topics/multiomics-proteomics-ptm-identification.md)
- [Cancer Multiomics Literature Monitor](../topics/cancer-multiomics-literature.md)

## Sources

- Existing topic hubs and their linked local source pages.
- Local PDF/source-note workflow in this repository.
