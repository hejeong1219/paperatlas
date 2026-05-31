---
title: "Proteogenomic Characterization Reveals Metabolic Vulnerabilities and Aberrant Phosphorylation in Colorectal Metastasis to Liver"
authors:
  - "Wensi Zhao"
  - "Lei Zhao"
  - "Yannan Lian"
  - "Zhiwei Liu"
  - "Yaqi Li"
  - "Xuege Wang"
  - "Junjie Peng"
  - "Jun Qin"
  - "Minjia Tan"
year: 2026
journal: "Advanced Science"
doi: "10.1002/advs.202511744"
pmid: "41195591"
pmcid: "PMC12822478"
paper_kind: proteogenomic
local_source: "raw/inbox/papers/zhao-2026-proteogenomic-characterization-reveals-metabolic-vulnerabilities.html"
pdf_status: html-only
cancer_types:
  - "colorectal-cancer"
  - "colorectal-liver-metastasis"
modalities:
  - "wes"
  - "rna-seq"
  - "proteomics"
  - "phosphoproteomics"
topic: cancer-multiomics
tags:
  - "proteogenomics"
  - "colorectal-liver-metastasis"
  - "one-carbon-metabolism"
  - "shmt1"
  - "ndrg1"
  - "pim-kinase"
  - "patient-stratification"
  - "chinese-cohort"
  - "pmid-41195591"
themes:
  - "colorectal-liver-metastasis"
  - "one-carbon-metabolism"
  - "ndrg1-degradation"
  - "patient-stratification"
  - "subtype-biomarker"
  - "asian-cohort"
cm_axis: integration
---
# Proteogenomic Characterization Reveals Metabolic Vulnerabilities and Aberrant Phosphorylation in Colorectal Metastasis to Liver

_Advanced Science, 2026;13(4):e11744 (online 2025-11-06; collection 2026 Jan)._ PMID: [41195591](https://pubmed.ncbi.nlm.nih.gov/41195591/).

DOI: [10.1002/advs.202511744](https://doi.org/10.1002/advs.202511744)

## Summary

Zhao et al.는 treatment-naïve colorectal liver metastasis(CRLM) 34명에서 matched 원발 CRC(T) / 인접 정상(N) / 간 전이(LM) 102 sample을 수집해 WES + RNA-seq + TMT proteome(8,568 identified / 8,093 quantified) + Ti⁴⁺-IMAC phosphoproteome(25,775 identified / 19,803 quantified; class I 16,300)을 통합한 CRLM proteogenomic landscape를 구축했다. Fudan University Shanghai Cancer Center(FUSCC) 2012.07–2019.06 수집, IRB 050432-4-1805C + 050432-4-1911D. APC / TP53 / KRAS mutation frequency는 T와 LM 사이 유의 차이 없음 — genomic level alteration이 CRLM의 primary driver가 아니라는 선행 보고와 정합. SCNA cis-regulatory effect는 mRNA에서 가장 두드러졌고, CAG 551개가 cohort에서 식별되었다. 기능적으로 (1) 일탄소 대사 효소 SHMT1이 formate를 통해 AMPK를 억제해 CRC tumorigenesis와 간 전이를 촉진(KAP organoid in vitro + intrasplenic in vivo + 125 mM formate drinking water + AICAR 50 mg/kg i.p. rescue로 검증), (2) PIM kinase-의존 NDRG1 Ser330 phosphorylation이 ubiquitin-proteasome NDRG1 degradation을 유도해 간 전이를 가중(NDRG1 S330A KAP 세포 in vivo metastasis 감소 + WT vs S330A ubiquitination/CHX chase/MG132 + TP-3654 3 μM pan-PIM inhibitor로 검증). LM proteome unsupervised clustering으로 C1(metabolism, poor prognosis) / C2(RNA function, better prognosis) 2개 subtype을 확정(OS log-rank p<0.05; PCA clear separation). Subtype-specific biomarker FTCD / GPD1 / SOD2 / EIF4B Ser422 phosphorylation은 independent validation cohort n=87 IHC로 OS / PFS log-rank p<0.05로 재현.

## Key Points

### 코호트와 데이터 구성
- 34명 treatment-naïve CRLM 환자 = **102 samples**(matched T+N+LM 트리오; FUSCC Shanghai 2012.07–2019.06; IRB 050432-4-1805C + 050432-4-1911D). 추가 independent validation cohort n=87(IHC 검증용).
- WES: 19,493 nonsynonymous somatic mutation + 23,109 SCNA. CRC typical driver(APC, TP53, KRAS) mutation frequency T vs LM 유의 차이 없음(선행 보고와 정합).
- TMT proteome 8,568 identified / **8,093 quantified**. Ti⁴⁺-IMAC phosphoproteome 25,775 identified / **19,803 quantified**(class I 16,300 / class II 3,503; class I만 downstream 분석 사용).
- PCA: proteomics가 transcriptome / phosphoproteome 대비 N / T / LM 구분 power 최고.
- IRS(internal reference sample) 상관과 QC 모두 안정. mRNA-protein gene-wise 상관 globally positive(p<0.05, ρ>0.3); negative 조절은 소수.
- Mouse experimental model + KAP intestinal organoid + CRC cell line + independent IHC validation cohort(n=87)로 기능 검증.
- WES 추가: 공유 amplification 1q / 13q / 15q / 17q + deletion 1p / 10q / 12q / 17q(FDR<0.05). LM 고유 amp 8p + del 8p / 12q / 16p; T 고유 amp 17p / 20q + del 1q / 2p / 2q / 5q / 7q / 14q / 17p / 21q / 22q. PDS5B 등 551 CAG cis-regulatory; cis effect는 mRNA에서 가장 두드러짐.

### 일관된 LM 시그니처와 CRS 한계
- LM vs T proteome: complement / coagulation cascades + PPAR signaling + carbon / cholesterol / fructose-mannose / amino acid metabolism upregulation(FDR<0.05). T는 focal adhesion 우세.
- LM vs T phosphoproteome: actin filament organization, small GTPase signaling, regulation of cell morphogenesis, lamellipodium organization upregulation(FDR<0.05). T는 cell communication / cellular response to peptide / RNA splicing.
- 288,337 AS event 식별(A3SS 12,185 / A5SS 7,985 / MEX 51,671 / RI 5,537 / SE 210,959); LM vs T 유의 26 event(FDR<0.05, |IncLevelDiff|>0.1); **14/26 prognostic**. FN1 / KHK / SERPINA1 top gene(모두 OS 연관). 스플라이세오솜 DDX5+SF1 LM에서 down + prognostic.
- KSEA(LM vs T): LM에서 RAF1+PAK2+ROCK1 hyperactive(VIM phosphorylation + CFL1 Ser3 → EMT); T에서 CLK1+CDK7+PRKACB hyperactive.
- xCell: M2 macrophage가 LM에서 유의 ↑. Immunomodulatory antigen presentation 유전자 transcript/protein/phospho 수준 모두 down. **ARG1**(plasma protein/immune suppressor)는 protein-level only LM ↑ (mRNA 변화 없음); high ARG1 → poor prognosis(T + LM).
- **Clinical Risk Score(CRS) 한계**: high CRS(≥3) 환자는 ribosome + epigenetic regulation + histone modification + endothelial intestinal barrier 강조 vs low CRS는 cell adhesion + lysosome + steroid biosynthesis; **5-year OS log-rank p=0.23** — CRS는 본 코호트 prognosis 예측 불충분. Immune profile 유의 차이도 없음.

### LM-enriched protein set과 외부 재현
- 245개 LM-enriched protein set(주로 metabolism 관련) + 96개 T-enriched protein set. 추가 필터 후 200(LM, tissue-specific 제거 시 155) + 96(T).
- Li et al. 공개 mCRC proteomics dataset GSEA: LM-enriched protein set은 LM에서 NES=-3.50/FDR<0.001; T-enriched protein set은 T에서 NES=1.86/FDR<0.001. **Tissue-specific 유전자 제거 후에도 NES=-3.11 유지** — 조직 특이 발현 잔여 효과로 설명되지 않음.
- Li dataset T sample(n=146)에서 LM-enriched protein median expression high → **OS log-rank p=0.037**(외부 코호트 prognostic transferability 1차 증거).

### SHMT1–formate–AMPK 축
- LM vs T: one-carbon metabolism 효소 **SHMT1, MTHFD1, SHMT2 protein 모두 LM ↑**.
- SHMT1 high LM 환자: validation cohort n=87 IHC에서 **OS / PFS 모두 log-rank p<0.05로 poor**.
- KAP intestinal organoid(Villin^CreERT2; Kras^LSL-G12D; Apc^min/+; Trp53^flox/flox, 2 개월 TAM 처리): Shmt1 KD → pH3⁺ proliferation ↓ / CC3⁺ apoptosis ↑ / growth ↓; SHMT1 OE → 반대. 동일 isogenic luciferase-labeled organoid를 immunocompetent C57BL/6 WT에 **intrasplenic 주입** → BLI + 조직학적 평가로 **Shmt1 KD가 metastatic progression 약화** 확인. CPS1도 같은 접근으로 validated.
- 대사물 재공급 실험: **formate 단독으로만 Shmt1 KD organoid 성장 회복** — SHMT1-catalyzed formate가 down-stream effector를 조절한다는 가설 직접 지지. In vivo formate level: Shmt1 KD에서 ↓ / SHMT1 OE에서 ↑.
- Formate 보충 후 transcriptome: HIF-1 / **AMPK** / PPP 경로 inhibition + Wnt / Hippo upregulation(KEGG).
- Western: Shmt1 KD organoid → p-AMPK ↑; formate 첨가 → p-AMPK ↓; AICAR(AMPK agonist) → p-AMPK ↑↑.
- **In vivo rescue**: tumor-bearing mouse에 125 mM formate(drinking water) 또는 AICAR(50 mg/kg i.p.) → formate 보충은 liver tumor burden ↑, AICAR가 그 효과 mitigation. SHMT1-formate-AMPK 축이 in vivo에서 metastasis 조절 기능 확정.

### NDRG1 Ser330 phosphorylation-의존 degradation
- LM 유의 phosphosite 8개(functional score + prognostic log-rank p<0.05): 5 up + 3 down. SLC16A1 S498 / **NDRG1 S330** / PDLIM2 S129가 진화적으로 보존(human / mouse / 기타 종).
- NDRG1 S330p ↔ actin cytoskeleton reorganization Spearman **ρ=0.43, p=0.013**; actin filament-based movement ρ=0.34, p=0.053.
- NDRG1 S330A KAP cell → intrasplenic 주입 → liver metastasis burden 유의 감소. CRS high vs low에서는 NDRG1 S330p 유의 차이 없음.
- NDRG1 protein ↔ EMT pathway ρ=-0.2, p=0.098(tumor suppressor 역할과 정합). NDRG1 protein ↔ protein monoubiquitination ρ=0.52, p=0.002 / ↔ SCF-proteasome process ρ=0.39, p=0.024. BioGRID interaction partner GO BP enrichment도 protein proteolysis / stability / proteasomal catabolic process.
- WT vs S330A 비교 실험: **WT 세포 ubiquitination 수준 유의 ↑**(S330A 대비); cycloheximide chase에서 S330A 반감기 연장 → S330 phosphorylation이 degradation에 필수. MG132로 NDRG1 accumulation → ubiquitin-proteasome 경로 의존성 확정.
- Kinase predictor(Johnson 2023 Nat / publicly available substrate atlas)로 NDRG1 S330 phosphorylation 후보 1위 = **PIM family**(PIM1 / PIM2 / PIM3). Transcriptome에서 PIM1 LM ↑.
- **TP-3654 3 μM**(pan-PIM inhibitor): NDRG1 S330p ↓, migration / invasion ↓, p-AMPK ↑(PIM이 AMPK 활성을 음으로 조절한다는 선행 보고와 정합). PIM이 NDRG1을 통한 ubiquitin degradation과 AMPK 활성 모두를 조절하는 dual axis 시사.
- KSEA가 PIM→NDRG1 / PIM→AMPK 직접 detection 실패 → PIM은 AMPKα T172의 직접 substrate가 아니며, NDRG1 S330은 KSEA 기본 DB 부재. Sun et al. 알고리즘(PhosphoSitePlus v6.7.5 확장 DB)으로 재계산 시 **PIM1 activity LM에서 유의 ↑**(Wilcoxon p<0.001).

### LM 분자 아형 C1 vs C2
- LM proteome unsupervised clustering으로 **2 아형(C1, C2) 명확 분리** — phosphoproteome / transcriptome 기반 clustering보다 분리력 우수. PCA에서 C1 / C2 명확 분리.
- **OS log-rank p<0.05로 C1 poor prognosis vs C2 better prognosis**. Phosphoproteome / transcriptome 기반 subtype은 OS 유의 차이 없음 → 단백질 수준 stratification이 prognostic stratification에 가장 적합.
- 고빈도(>30%) mutated gene(APC / TP53 / KRAS 포함) C1 vs C2 유의 차이 없음; **17개 저빈도(≤15%) mutated gene**이 Fisher exact test p<0.05.
- KEGG: **C1 metabolism**(carbon / fatty acid / amino acid metabolism)에 enriched; **C2 RNA function**(RNA transport / splicing) enriched.
- 226,107 AS event in LM(A3SS 10,934 / A5SS 7,085 / MEX 37,125 / RI 5,393 / SE 165,570); 148 event C1 vs C2 차이(FDR<0.05, |IncLevelDiff|>0.1); **98/148 prognostic**. KHK / RPP21 / U2AF1L4 top gene.
- 17 splicing factor C2 protein ↑ vs 2 C1 ↑(FC>1.2, p<0.05). High DHX9 / DIS3 / HNRNPA0 / NCBP1 / PRPF8 / SNRPD1 → good prognosis(log-rank p<0.05); NCBP1 / PRPF8 / SNRPD1은 CRC + HCC dependency gene. 6 splicing factor ↔ 11 AS event 양/음 조절 네트워크(FDR<0.05); DIS3 / HNRNPA0 / PRPF8가 GRB7 AS event를 negative 조절.
- Phosphoproteome inference: C2가 cell junction organization / chromatin remodeling / actin filament-based movement / PTM 강화. KSEA C1 vs C2: **C1에서 RPS6KA1 + RPS6KB2 + PAK1 + PAK2 + PAK4 + CHEK1 + ROCK1 + MAPK1 hyperactive**; RPS6KA1 / RPS6KB2 / PAK2가 EIF4B S422 phosphorylation 후보 kinase.
- Immune / stromal score 유의 차이 없으나 ARG1은 C1에서 유의 ↑(prognosis와 정합).

### Subtype-specific biomarker
- C1 vs other(C2 LM + C1/C2 T + C1/C2 N) 비교: 90개 highly expressed protein(FC>1.2, p<0.05) → 42개 prognostic(log-rank p<0.05). One-carbon metabolic process top-enriched.
- **FTCD**(formimidoyltransferase-cyclodeaminase) + **GPD1**(glycerol-3-phosphate dehydrogenase 1): subcellular location / functional enzyme / 항체 가용성 기준으로 선정. Independent validation cohort n=87 IHC에서 OS / PFS 모두 log-rank p<0.05로 poor.
- **SOD2**(superoxide dismutase 2): DepMap CRC / HCC dependency gene 중 C1 LM 최상위 upregulation. **protein-level만** ↑ (mRNA 변화 없음); discovery cohort log-rank p=0.098(low power) but validation n=87 IHC log-rank p=0.0331로 재현.
- Phosphosite C1 vs C2: 108 up + 60 down(FC>1.5, p<0.05); functional score >0.5 + 25 prognostic. **EIF4B Ser422 + Thr420 C1 LM 특이 ↑**, mRNA / protein 수준에서는 차이 없음. **EIF4B S422 validation n=87: OS log-rank p=0.0265, PFS log-rank p=0.0099**.

### 한계(본문 명시)
- Discovery cohort n=34는 일부 핵심 분자 / 경로 식별의 통계 power 부족 — SOD2 log-rank p=0.098(discovery) → IHC validation cohort n=87에서 p=0.0331로 보완.
- Formate가 AMPK signaling을 어떤 정확한 mechanism(adenine nucleotide level → glycolysis → AMPK repression 후보)으로 억제하는지는 추가 정의 필요(본문 직접 인정).
- KSEA 기반 kinase 활성 추정은 알고리즘 한계로 PIM→NDRG1 S330 / PIM→AMPKα T172 indirect axis 직접 detection 불가; Sun et al. 알고리즘(PhosphoSitePlus 확장 DB)으로만 보완.
- Phosphorylation event의 functional role 다수는 후속 mechanistic 검증 필요(본문 명시).
- Single-cohort Chinese single-institution(FUSCC); validation cohort도 같은 기관 가능성 — 외부 ethnicity / institution 비교 부재.

## Methods

- **Cohort & Sample**: FUSCC 2012-07~2019-06 collected; treatment-naïve CRLM 34명; matched primary CRC + 인접 정상(>5 cm) + liver metastasis 102 samples. Independent IHC validation cohort n=87.
- **WES**: somatic SNV / indel / SCNA call. CAG cis-regulatory: SCNA-mRNA / SCNA-protein / SCNA-phospho 상관.
- **RNA-seq**: rMATS for AS event 분류(A3SS / A5SS / MEX / RI / SE).
- **TMT proteomics + Ti⁴⁺-IMAC phosphoproteomics**: high-resolution MS; class I phosphosite(localization score 기준) 우선 분석.
- **Clinical Risk Score**: Fong 1999 5-factor 정의(primary tumor size, CEA, regional lymph node 등)로 high(≥3) / low(<3) 분류.
- **Differential analysis**: FC>1.2(global protein, single-omic), FC>1.5(phosphosite), Wilcoxon rank-sum / signed-rank, p<0.05 + log-rank.
- **GSEA (external cross-reference)**: Li et al. 공개 mCRC proteomics dataset에 본 연구 LM / T-enriched protein set을 molecular signature로 적용 — NES + FDR 산출.
- **KSEA + Sun et al. 알고리즘**: 기본 KSEA는 PhosphoSitePlus 기본 DB; 보완 분석은 PhosphoSitePlus v6.7.5 확장 DB로 substrate coverage 확장(NDRG1 S330 포함).
- **xCell / ESTIMATE / immune database**: immune cell 분포 + stromal / immune score + immunomodulatory gene 평가.
- **Functional score**: Ochoa 2020 Nat Biotechnol(phosphosite functional score >0.5 임계 적용).
- **KAP organoid model**: Villin^CreERT2; Kras^LSL-G12D; Apc^min/+; Trp53^flox/flox 마우스에서 2 개월 tamoxifen 처리 후 intestinal organoid 분리. Shmt1 / SHMT1 / NDRG1 mutant variants(WT / S330A) lentivirus 도입 후 luciferase labeling.
- **In vivo intrasplenic injection**: C57BL/6 WT mouse 비장 주입 → 간 전이 모델; bioluminescence imaging + 조직학적 평가로 metastasis 정량.
- **Metabolite supplementation**: organoid에 individual one-carbon metabolite 재공급(formate 등); formate 단독으로 Shmt1 KD 효과 reverse.
- **In vivo rescue**: 125 mM formate drinking water 또는 AICAR(AMPK agonist) 50 mg/kg i.p.
- **NDRG1 cell-based experiments**: KAP cell에 NDRG1 WT / S330A mutant 도입; ubiquitination(IP-WB) / cycloheximide chase / MG132 proteasome inhibitor.
- **Kinase inhibitor**: TP-3654 3 μM(pan-PIM inhibitor) CRC organoid 처리 — NDRG1 S330p + migration / invasion + p-AMPK 측정.
- **Unsupervised clustering**: LM proteome 기반(phospho / transcriptome 모두 동일 적용), C1 / C2 2 cluster identification + PCA validation. OS / PFS는 log-rank.
- **Subtype-specific biomarker selection**: differential expression(FC>1.2, p<0.05) + missing value <10% + log-rank p<0.05; functional score >0.5(phosphosite); subcellular location + functional enzyme + IHC antibody availability 추가.
- **IHC validation cohort n=87**: same-institution(?) tissue microarray 추정; FTCD / GPD1 / SOD2 / EIF4B S422 / SHMT1 발현 정량 + OS / PFS 분석.
- **Statistics**: GraphPad Prism 8.0. mean ± SEM; *p<0.05, **p<0.01, ***p<0.001; ns 비유의.
- **Data IDs**: iProx Consortium **IPX0007391001**; GSA database **PRJCA020890**(https://ngdc.cncb.ac.cn/gsa/). Original code 없음.
- **Conflict of interest**: 없음(저자 본문 declaration).

## Cancer Multiomics Project Relevance

한미암 프로젝트가 한국인 CRC 코호트 또는 동아시아 비교 코호트에서 **liver metastasis-specific proteogenomic landscape**, **metabolic vulnerability**, 또는 **proteomic subtype-based stratification**을 검토할 때 직접 활용 가능한 reference. 적용 시 다음 5축으로 사용한다.

1. **Treatment-naïve CRLM proteogenomic baseline**: 34 patient × 102 sample(T+N+LM matched) + TMT proteome 8,093 quantified + Ti⁴⁺-IMAC phospho 19,803 quantified + 16,300 class I phosphosite의 데이터 스케일은 한국인 mCRC proteogenomic 코호트 설계의 1차 reference. 특히 **APC/TP53/KRAS frequency가 T와 LM에서 유의 차이 없음 + cis-regulatory effect가 mRNA에서 가장 강함**이라는 정량 관찰은 한미암 CRC 데이터 acquisition에서 WES-only 분석으로는 LM 분기를 식별할 수 없다는 결정의 근거.
2. **One-carbon metabolism druggability**: SHMT1 high → OS / PFS poor(n=87 IHC validation) + KAP intestinal organoid + intrasplenic 모델 + 125 mM formate / AICAR rescue로 **SHMT1-formate-AMPK 축 in vivo causal evidence** 완비. 한미암이 한국인 CRC LM 환자에서 SHMT1 / MTHFD1 / SHMT2 발현을 surrogate biomarker로 측정하고, SHMT1 inhibitor(SHIN1, SHIN2 후보) 혹은 AMPK agonist(metformin / AICAR analog)를 LM-specific subset에서 평가하는 임상-translational 경로의 reference. CPS1도 동일 접근으로 검증되었으므로 urea cycle / amino acid metabolism 후보 확장 reference.
3. **NDRG1 phospho-degradation axis + PIM inhibitor**: NDRG1 S330p / Ser330 phosphorylation-dependent ubiquitin degradation은 PIM kinase(특히 PIM1 mRNA LM ↑) 차단으로 mechanism 차단 가능 — **TP-3654 3 μM** in vitro 검증. 한미암 CRC LM 환자 stratification에서 NDRG1 S330p ↑ subset → PIM kinase inhibitor(TP-3654 같은 pan-PIM, 또는 SGI-1776) 임상 적용 후보군 추출 logic을 직접 차용. 또한 **PIM-AMPK indirect inhibition axis**(p-AMPK ↑ on TP-3654)는 SHMT1 축과 더불어 AMPK 회복을 공통 endpoint로 한 stratification 가설을 가능하게 함.
4. **C1(metabolism) vs C2(RNA function) proteomic subtype**: LM proteome 기반 unsupervised clustering이 phospho / transcriptome 기반보다 prognostic stratification에 우수(OS log-rank p<0.05) — 한국인 LM 코호트 분류 첫 layer로 protein-level clustering 채택 결정 근거. **FTCD / GPD1 / SOD2 / EIF4B S422 phospho 4-marker panel**은 n=87 IHC로 OS / PFS log-rank p<0.05로 외부 재현 — 한미암 LM patient stratification에 동일 항체 도입 후보. C1 RPS6KA1 / RPS6KB2 / PAK1/2/4 / CHEK1 / ROCK1 / MAPK1 hyperactive 시그니처는 한미암 kinase inhibitor library screening의 1차 target 후보(특히 MAPK / ROCK / PAK family).
5. **공개 데이터 cross-reference**: iProx **IPX0007391001** + GSA **PRJCA020890** raw data 접근 → 한국인 CRC LM 코호트 cross-reference / re-analysis 가능. Li et al. mCRC proteomics dataset(외부 GSEA 검증) + Tanaka 2024(CRC primary vs LM proteogenomics)와 함께 CRLM proteogenomic external reference triplet으로 사용. CPTAC PDAC / GBM / LUAD / CCRCC에서 SOD2 / GPD1 / EIF4B S422 prognostic 영향이 reproducible — pan-cancer metabolic / translational stratification 가설 추가 검증 자료.

한계 본문 명시 — discovery n=34 power 부족(SOD2 p=0.098 discovery → 0.0331 validation), formate-AMPK 정확 mechanism 미정의, KSEA가 PIM→NDRG1 / PIM→AMPK indirect axis detection 실패(Sun et al. 알고리즘으로만 보완), single-cohort Chinese single-institution. 한미암이 한국 환자 코호트에 적용할 때는 IRB 050432-4-1805C + 050432-4-1911D와 유사한 prospective treatment-naïve enrollment 설계, matched T+N+LM 트리오 sample, 그리고 independent IHC validation cohort를 동일 protocol로 확보하는 것이 외부 transferability 확인의 필수 조건.

## Connections

- [Cancer Multiomics Literature](../topics/cancer-multiomics-literature.md) — Section 1 (WGS/Proteogenomics 통합 기반)
- [Tanaka 2024 - CRC Primary vs Liver Metastasis Proteogenomics](../analyses/cancer-multiomics-literature/tanaka-2024-proteogenomic-characterization-primary-colorectal-cancer.md)
- [Xu 2026 - Chinese HER2-low BC Proteogenomics + Lactylome](./xu-2026-proteogenomic-characterization-reveals-subtype-specific-therapeutic.md)
- [Lee 2026 - Korean TNBC NAC Resistance Proteogenomics](./lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md)
- [Xiang 2025 - Non-Canonical TSA Proteogenomics in CRC + MC38](./xiang-2026-predominant-mutated-non-canonical-tumor-specific-antigens.md)
- [Zhao 2025 - Phosphoproteomic + Acetylomic Response to Kinase Inhibitors (CRC)](../analyses/cancer-multiomics-literature/zhao-2025-phosphoproteomic-acetylomic-characterization-colorectal-cancer.md)
- [Asuzu 2025 - Phosphoproteomic Dysregulation Drives Tumor Proliferation](../analyses/cancer-multiomics-literature/asuzu-2025-phosphoproteomic-dysregulation-drives-tumor-proliferation.md)
- [Anurag 2022 - Proteogenomic Markers of Chemotherapy Response (TNBC)](../analyses/cancer-multiomics-literature/anurag-2022-proteogenomic-markers-chemotherapy-resistance-response.md)
- [Yu 2024 - Proteogenomic Analysis of Cervical Cancer](../analyses/cancer-multiomics-literature/yu-2024-proteogenomic-analysis-cervical-cancer-reveals.md)
- [Müller-Dott 2025 - Phosphoproteomic Kinase Activity Inference (benchmarKIN)](../analyses/cancer-multiomics-literature/muller-dott-2025-phosphoproteomic-kinase-activity-inference.md)

## Sources

- Local HTML (PMC): `raw/inbox/papers/zhao-2026-proteogenomic-characterization-reveals-metabolic-vulnerabilities.html`
- PubMed: <https://pubmed.ncbi.nlm.nih.gov/41195591/>
- DOI: <https://doi.org/10.1002/advs.202511744>
- PMC: <https://pmc.ncbi.nlm.nih.gov/articles/PMC12822478/>
- Data — proteomics + phosphoproteomics: iProx [IPX0007391001](https://www.iprox.cn/page/project.html?id=IPX0007391001)
- Data — WES + RNA-seq: GSA [PRJCA020890](https://ngdc.cncb.ac.cn/gsa/browse/CRA020890)
- Citation: Zhao W., Zhao L., Lian Y., et al. *Adv. Sci.* 2026;13(4):e11744. doi:10.1002/advs.202511744
