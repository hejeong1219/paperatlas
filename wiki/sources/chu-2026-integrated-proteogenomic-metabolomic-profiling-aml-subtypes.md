---
title: "Integrated proteogenomic and metabolomic profiling of acute myeloid leukemias to identify molecular subtypes and associated therapy targets"
authors:
  - "Chu"
  - "Hsiao"
  - "Wang"
  - "Nesvizhskii"
  - "Zhang"
  - "Liu"
  - "Cieslik"
year: 2026
journal: "Nature Cancer"
doi: "10.1038/s43018-026-01175-6"
paper_kind: proteogenomic
pdf: "raw/inbox/papers/chu-2026-integrated-proteogenomic-metabolomic-profiling-aml-subtypes.pdf"
topic: "cancer-multiomics-literature"
extra_topics:
  - "multiomics-proteomics-ptm-identification"
tags:
  - "cancer-multiomics"
  - "proteogenomics"
  - "acute-myeloid-leukemia"
  - "phosphoproteomics"
  - "acetylomics"
  - "metabolomics"
  - "lipidomics"
  - "cptac"
  - "local-pdf-ingest"
themes:
  - "multiomics-identification"
  - "molecular-subtyping"
  - "therapy-target-nomination"
  - "ptm-methodology"
ingest_status: full-text-read
ingested_on: 2026-07-06
cm_axis: multiomics
---
# Integrated proteogenomic and metabolomic profiling of acute myeloid leukemias to identify molecular subtypes and associated therapy targets

_Nature Cancer, Volume 7, June 2026, 993–1015._ Open Access (CC BY 4.0).

DOI: [10.1038/s43018-026-01175-6](https://doi.org/10.1038/s43018-026-01175-6)

Received 26 March 2025 · Accepted 21 April 2026 · Published online 12 June 2026. CPTAC resource paper (Univ. Michigan / Baylor College of Medicine / PNNL). Corresponding authors: Alexey I. Nesvizhskii, Bing Zhang, Tao Liu, Marcin P. Cieslik. First authors: Shih-Chun A. Chu, Yi Hsiao, Chenwei Wang, Jennifer E. Kyle (equal contribution).

## Summary

CPTAC가 치료 전(treatment-naive) 급성골수성백혈병(AML) 환자 **173명**을 **13개 오믹스 모달리티**로 프로파일링한 통합 proteogenomic·metabolomic 아틀라스다. DNA(WGS/WES/methylation), RNA(RNA-seq/miRNA-seq), 단백질(global/phospho/acetyl/glyco TMT), 대사체(metabolomics/lipidomics)를 통합해 총 **111,993개 분자 feature**를 정량했다. 핵심 발견은 (1) 세포 분화 위계(primitive↔committed↔GMP-like)를 따라 **MYC와 mTOR 활성이 상호 길항(antagonism)** 하며 광범위한 대사·지질 리프로그래밍을 유발한다는 것, (2) **CEBPA-변이 AML(C4)** 에서 acetyl-CoA 축적에 의한 **미토콘드리아 단백질의 비효소적 과아세틸화(nonenzymatic hyperacetylation)**, (3) 단백질 중심(protein-centric) SNF 서브타이핑으로 도출한 **AML-8(C1–C8)** 체계와, 그 안에서 FOXC1·HOXB8/9 outlier 발현으로 정의되는 **독특한 NPM1-변이 아형 C3**, (4) primitive AML의 범용 마커 **MAP1A**(베네토클락스 반응성과 연관), (5) 멀티오믹 머신러닝(FunMap 네트워크)으로 치료 표적을 지명하고 **MTA1을 파노비노스타트(panobinostat) 내성 매개인자로 검증**한 것이다. 유전형(WHO/ELN) 분류만으로는 놓치는 병태생리·치료 취약점을 오믹스 층위에서 통합적으로 드러낸다.

## Key Points

- **코호트 규모/구성**: 치료 전 AML 173명. 완전 somatic genomics는 전원, proteomics/PTM은 162명, metabolomics/lipidomics는 97명, matched normal DNA는 161명에서 확보. Tumor purity 평균 ~79%(IQR 73–92%). 넓은 연령 스펙트럼 + 주요 WHO 아형 포함(유럽계 다수, 정상 대조군 제한이 한계).
- **Feature counts(Fig. 1b)**: RNA 33,000 / Protein 10,957 / Phospho-site 49,999 / Acetyl-site 11,927 / Glyco-site 2,087 / Metabolite 2,655 / Lipid 1,365 → 총 111,993. TMT batch effect 최소, 재현성 양호. PTM 종류별로 서로 다른 세포소기관에 enrich(각 assay가 고유 생물학 조명).
- **MYC ↔ mTOR 길항(Fig. 1f,g)**: 공통 anabolism에도 불구하고 두 경로가 우리·여러 독립 AML 코호트에서 반대 방향으로 enrich(단백질·RNA 양쪽, R=−0.65). Monocytic AML=high mTOR/low MYC ↔ primitive AML=반대. Primitive=OXPHOS+PS(phosphatidylserine) 상향, committed=glycolytic+PC, GMP-like=이화(catabolic)·proteolysis↑·eIF4-의존 translation↓·HexCer 축적.
- **CEBPA-변이 C4 미토콘드리아 과아세틸화(Fig. 3–4)**: median-centering 없이 보면 C4에 강한 hyperacetylation(반대로 C8은 hypoacetylation). C4 아세틸화는 미토콘드리아에 거의 국한, **비효소적**(HAT 비의존)이며 acetyl-CoA 축적(pyruvate dehydrogenase + FA β-oxidation + amino acid degradation, SUCLG2 예외)에서 기인. TCA/OXPHOS 등 미토콘드리아 에너지 경로 다중 타격.
- **AML-8 protein-centric 서브타입(Fig. 2)**: RNA+global proteome를 SNF로 공동 클러스터링 → C1–C8. genetics(NPM1은 C1–C3, CEBPA는 C4, RUNX1–RUNX1T1은 C8, sAML aberration은 C5–C7)와 분화(C1/C6 monocytic, C8 GMP-like, C2/C7 HSC-like/multipotent) 축을 통합. ELN 예후와 정합(high-risk/MDS-related가 C5–C8에 집중).
- **NPM1-변이 3분할 + 신규 아형 C3(Fig. 2h,i)**: NPM1-mut은 C1(성숙 monocytic CD14⁺), C2(primitive triple-mut: NPM1+FLT3-ITD+DNMT3A, 기존 'C-mito' = 고미토콘드리아·베네토클락스 민감), **C3(HOXB8/9⁺·CD99⁺, FOXC1/POU2F1/SOX4 outlier, IDH1/2+GATA2 enrich, CIITA promoter hypermethylation으로 MHC-II 억제)** 로 나뉨. C3는 SCENIC에서 HOXB8/9·FOXC1·POU2F1(Oct1) TF 활성 outlier.
- **MAP1A = primitive AML 범용 마커(Fig. 2l 등)**: NPM1-mut(C1–C3) 한정으로 제안됐던 primitive/mature 축을 MDS-related까지 확장. MAP1A 단백 발현이 베네토클락스 약물반응(AUC)과 R=0.95로 강한 상관 → primitive·venetoclax-sensitive AML 진단 마커 + leukemic stem cell 구분 잠재력.
- **치료 취약점 지명 + MTA1 검증(Fig. 6–7)**: BeatAML-proteomics XGBoost 분류기로 서브타입 이식 → FDA 승인 약물(특히 kinase inhibitor) 차등반응. FunMap cofunction 네트워크 + ICE clique 알고리즘(274 clique)으로 primitive AML·생존과 연관된 clique 발굴. **MTA1**(NuRD scaffold, HDAC1/2와 복합체)이 파노비노스타트 민감도와 최강 음의 상관 → CRISPR KO로 파노비노스타트 민감 회복, MOLM-14 quizartinib-내성주에 MTA1 과발현 시 내성 부여 → **파노비노스타트 내성 매개인자로 검증**. 추가: **ATP1B3**(C1/C8 신규 표적, synthetic-lethal partner ATP1B1 저발현), **BCL2/베네토클락스**(primitive AML 의존성), **다사티닙+베네토클락스 시너지**(committed AML, FGR/Src↑).

## Detailed Evidence

### Cohort, design, and data scale
- 173 treatment-naive AML. 13 modalities: DNA sequence·DNA methylation; RNA-seq·miRNA-seq; global/phospho/acetyl/glyco TMT proteomics; metabolomics·lipidomics. Peripheral blood 및/또는 bone marrow + buccal swab(germline).
- Proteomics/PTM 162명, metabolomics/lipidomics 97명, matched normal DNA 161명. RBC 오염 보정(14-gene RBC score + limma remove-BatchEffect), tumor purity·source(BM/PB)를 covariate로 조정. Batch-corrected + uncorrected 데이터 모두 공개.
- WHO 2024 + ELN + FAB(형태학) 분류를 central histopathology review로 확정. Cellular deconvolution(BayesPrism, GSE235063 참조)으로 CD14⁺ monocytic / GMP-like / primitive(HSC) 분율 추정 → FAB와 정합.

### MYC/mTOR antagonism and metabolic-lipidomic reprogramming
- Differentiation score(LSC17, LinClass7, primitive/committed signature) vs proteome-wide pathway ssGSEA 비교 → MYC와 mTOR가 반대 극성. Fig. 1g: PI3K/AKT-mTOR vs MYC targets V2 hallmark, R=−0.65, P=1.79×10⁻²².
- Metabolomics(91명, ICA factorization S/A matrix; RP+HILIC LC-MS): C2(primitive) vs C1에서 ATP/sugar phosphate 등 차등. Primitive=dipeptide↑·amino acid↑(GMP-like는 semitryptic peptide↑ → proteolysis↑). GMP-like는 EIF4F complex regulation score 최저(translation 저하).
- Lipidomics(96명): FA-1 vs FA-2, primitive=unsaturated FA-2·22:6 상향, ferroptosis signature 및 peroxidizable PUFA↑(committed). GMP-like=HexCer/Cer salvage↑·SM↓. Caspase: primitive=CASP1/CASP4 pyroptosis↑, committed=proapoptotic.

### CEBPA (C4) mitochondrial hyperacetylation
- Non-median-centered acetylation → C4 hyperacetylation / C8 hypoacetylation(둘 다 분화 기반 설명 불가, succinylation과도 무관, CEBPA-mut 한정 재현). PTM-MOFA latent factor F1이 acetylation 주도·C4와 강연관.
- Acetyl-CoA 생성 경로(FA β-oxidation·lysine/amino-acid degradation) protein/RNA/acetyl 모두 C4 상향, pyruvate DH·TCA는 대체로 상향(SUCLG2 예외로 flux 역전 → acetyl-CoA↑). 미토콘드리아 아세틸화 = 비효소적(HAT 비의존).

### AML-8 clusters (protein-centric)
- **C1**: mature monocytic CD14⁺ AML(NPM1).
- **C2**: primitive, triple-mutant NPM1+FLT3-ITD+DNMT3A → 기존 'C-mito'(고미토콘드리아 단백·venetoclax 민감).
- **C3**: distinct NPM1-mut. HOXB8/9·CD99⁺, FOXC1/POU2F1/SOX4 outlier TF, IDH1/2+GATA2 enrich, CIITA hypermethylation→MHC-II↓. HOXB8/9·FOXC1·SOX4는 각각 myeloid 분화 억제/백혈병 촉진 보고.
- **C4**: CEBPA-mut, 미토콘드리아 과아세틸화(위 참조).
- **C5–C7**: MDS-related secondary AML(sAML). C6=monocytic MDS-related, C7=HSC-like/multipotent primitive MDS-related. NPM1 committed signature는 C1/C6, primitive는 C2/C7에 상향.
- **C8**: GMP-like, RUNX1–RUNX1T1(t(8;21)) enrich. 광범위 hypoacetylation + HDAC/HAT PTM 조절이상(EP300 K1794 deacetylation, EP300 K1180/CREBBP K1216 등).
- Severns/Jayavelu/Pino 분류와 비교 → AML-8은 Severns(transcriptomic)와 가장 근접하나, Jayavelu 대비 분화 축을 더 강하게 반영.

### Therapeutic vulnerabilities
- BeatAML-proteomics에서 500 gene RNA XGBoost로 서브타입 이식 후 drug response 매핑(BeatAML + DepMap). mTOR가 C1/C8의 top 표적(phosphoproteome·cell line dependency 지지, rapamycin ex vivo 검증). ATP1B3(막단백)도 C1/C8 표적.
- BCL2(venetoclax)=primitive AML 의존성(monocyte-like score와 venetoclax 내성 상관). FGR(Src family)=monocytic 분화와 최강 상관 → dasatinib+venetoclax가 committed AML에서 반응 개선, FGR가 반응 바이오마커.
- FunMap AML-specific network(13,729 gene / 134,100 edge, LLR≥3.912). ICE clique 274개 중 primitive·생존 연관 7개. C38 clique=HDAC1/HDAC2+NuRD/Sin3 등 11 단백. **MTA1**(NuRD scaffold)이 파노비노스타트 민감도와 최강 음상관·monocyte-like score와 최강 양상관. MTA1 KO(MOLM-14, MONO-MAC-6)→파노비노스타트 민감 회복·MTA1 survival dependency; quizartinib-내성 MOLM-14에 MTA1 과발현→내성 부여.

## Data & Code Availability
- **Genomic/clinical**: GDC, project CPTAC-3 (<https://portal.gdc.cancer.gov>).
- **Proteomic/PTM (Proteomic Data Commons)**: `PDC000554`–`PDC000562`.
- **Controlled-access germline/clinical (dbGaP)**: `phs001287.v22.p7`.
- **Imaging**: The Cancer Imaging Archive (TCIA) collection `cptac_aml`.
- **Code**: analysis scripts <https://github.com/Nesvilab/CPTAC_AML>; FunMap results <https://github.com/bzhanglab/funmap_aml>; interactive site <https://bzhanglab.github.io/funmap_aml/>.

## 한미암/Cancer Multiomics 과제 활용 가능성
- **13-모달 통합 설계의 레퍼런스**: WGS/WES/methylation + RNA/miRNA + global/phospho/acetyl/glyco proteome + metabolome/lipidome를 한 코호트에서 연결한 대표 사례. 각 층위 feature count·정규화(RBC/purity/source covariate 보정, batch-corrected+uncorrected 병행 공개) 방식이 코호트 설계·QC 템플릿으로 유용.
- **서브타이핑 방법론**: 단백질 중심 SNF(RNA+proteome 공동 클러스터링)로 유전형·분화 두 축을 통합한 AML-8은, 유전자 변이만으로 놓치는 아형(예: FOXC1/HOXB8-9 outlier C3)을 protein/PTM outlier로 규정하는 접근의 사례. 사용자의 다중오믹 코호트에서 "protein-centric subtype vs genotype 분류" 비교 프레임으로 참고 가능.
- **PTM·대사 층위가 유전형을 재해석**: CEBPA-mut의 비효소적 미토콘드리아 과아세틸화, GMP-like의 proteolysis↑/translation↓처럼, acetylome·metabolome이 mutation-only 해석을 뒤집는 사례 → PTM/metabolomics를 proxy가 아닌 필수 층위로 두는 근거.
- **치료 반응 예측 워크플로우**: BeatAML/DepMap로의 XGBoost 서브타입 이식 → drug response 매핑 → FunMap cofunction 네트워크 + clique로 표적 지명 → CRISPR/cell-line 검증(MTA1↔panobinostat)까지 이어지는 "멀티오믹 → 표적 → 검증" 파이프라인은 사용자 과제의 표적 발굴·내성 바이오마커 분석에 직접 이식 가능한 설계.
- **주의(한계 인용)**: 유럽계 다수·정상 대조군 제한으로 일반화 한계, MAP1A↔venetoclax 등 machine-learning 연관은 독립 코호트 mechanistic 검증 필요(저자 명시).

## Connections

- [Cancer Multiomics Proteogenomic Atlas](../topics/cancer-multiomics-literature.md)
- [Multiomics Proteomics PTM Identification](../topics/multiomics-proteomics-ptm-identification.md)
- [[wang-2021-proteogenomic-metabolomic-characterization-human-glioblastoma|Wang 2021 (CPTAC GBM proteome/phospho/acetyl + metabolome)]]
- [[clark-2020-integrated-proteogenomic-characterization-clear-cell|Clark 2020 (ccRCC proteogenomics)]]
- [[vasaikar-2019-proteogenomic-analysis-human-colon-cancer|Vasaikar 2019 (colon proteogenomics)]]
- [[anurag-2022-proteogenomic-markers-chemotherapy-resistance-response|Anurag 2022 (TNBC drug-response proteogenomics)]]

## Sources

- Local PDF: `raw/inbox/papers/chu-2026-integrated-proteogenomic-metabolomic-profiling-aml-subtypes.pdf`
- DOI: <https://doi.org/10.1038/s43018-026-01175-6>
