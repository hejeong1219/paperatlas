---
title: "Proteogenomic Characterization Reveals Subtype-Specific Therapeutic Potential for HER2-Low Breast Cancer"
authors:
  - "Xu S"
  - "Yang K"
  - "Liu L"
  - "Wang Q"
  - "Wang X"
  - "Cheng Z"
  - "Cui X"
  - "Wu H"
  - "Pang D"
year: 2026
journal: "Advanced Science"
doi: "10.1002/advs.202513086"
pmid: "41454718"
pmcid: "PMC12948274"
url: "https://advanced.onlinelibrary.wiley.com/doi/full/10.1002/advs.202513086"
pdf: "raw/inbox/papers/xu-2026-proteogenomic-her2-low-breast-cancer-subtypes.html"
pdf_status: html-only
paper_kind: proteogenomic
cancer_types:
  - her2-low-breast-cancer
  - her2-high-breast-cancer
modalities:
  - wes
  - rna-seq
  - proteomics
  - phosphoproteomics
  - lactylomics
themes:
  - her2-low
  - lactylation-ptm
  - patient-stratification
  - patient-derived-organoid
  - asian-cohort
  - druggable-target
discovery_method: user-shared
topic: cancer-multiomics-literature
tags:
  - source
  - her2-low-breast-cancer
  - proteogenomics
  - lactylomics
  - phosphoproteomics
  - chinese-cohort
  - pdo
  - aurkb
  - prkdc
  - stat1
  - jnk
  - itgb8
  - svm-classifier
---

# Proteogenomic Characterization Reveals Subtype-Specific Therapeutic Potential for HER2-Low Breast Cancer

_Advanced Science (2026)._ PMID: [41454718](https://pubmed.ncbi.nlm.nih.gov/41454718/). PMC: [PMC12948274](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12948274/).
· DOI: [10.1002/advs.202513086](https://doi.org/10.1002/advs.202513086)
· Harbin Medical University Cancer Hospital(Heilongjiang, 중국) + PTM Biolab(Hangzhou) + Cedars-Sinai 협력. Co-first authors: S.X., K.Y., L.L., Q.W., X.W.

## Summary

Xu et al.은 HER2-low breast cancer의 분자적 이질성을 분리해 임상적으로 다른 표적치료 선택지를 제시할 수 있는지를 묻기 위해, 중국 단일 기관(Harbin Medical University Cancer Hospital)에서 prospective로 수집한 **115개 종양 + 135개 인접정상조직(NAT)** 코호트에 WES(115T/86N) + RNA-seq + global proteome + phosphoproteome + **lactylome**(4-layer multiomics + PTM 2-layer)을 적용했다. HER2 분류는 2023 ASCO/CAP 가이드라인 기반으로 **HER2-low n=83(IHC 1+ 또는 IHC 2+/ISH-)** 과 **HER2-high n=32(IHC 3+)** 로 구성된다. 데이터 규모는 8,307 proteins / 43,963 phosphosites(7,808 phosphoproteins) / **18,214 lactylation sites on 1,644 proteins**이며, MaxQuant + timsTOF Pro 기반 1% FDR로 식별했다. 종양 단백체 unsupervised consensus clustering으로 세 개의 HER2-low 단백체 subtype(**PS1 n=21 — estrogen response / PS2 n=35 — angiogenesis / PS3 n=27 — proliferation + HER2-high-like**)을 정의하고, 각 subtype에 대응하는 치료 가설을 **endocrine therapy / anti-angiogenic therapy / anti-HER2 therapy**로 묶었다. PS subtype 분류는 (i) CPTAC HER2-negative cohort에서 외부 재현, (ii) SVM-RFE 10-feature classifier에서 train AUROC 0.97 / test 1.00, (iii) IHC 10-단백질 보조 모델에서 AUROC **0.80**(n=76)로 검증되고, **17개 환자 유래 organoid(PDO)** 약물민감도 실험으로 PS1↑(tamoxifen/toremifen) · PS2↑(bevacizumab/apatinib) · PS3↑(trastuzumab/T-DM1)을 in vitro에서 확인했다. 별도 14명의 real-world data(RWD) — 항혈관신생제 치료 — 에서 PS2 환자 4명 중 3명(CR/PR) vs PS1+PS3 10명 중 1명만 반응(P value는 본문 결과 그림에서 제시). 또한 **PS3 비율이 전체 HER2-low의 32.53%**로, DESTINY-Breast04에서 T-DXd가 보인 ~40% ORR 환자군과 양적으로 비교 가능한 sub-population이 분자 단위로 정의된다. Lactylome 측면에서는 **3개 lactylomic subtype(LS1/2/3)**으로 PFS 차이(log-rank P=0.00172)가 분리되고, PS2-LS3 교집합은 PS2 내부에서 생존이 더 좋은 sub-cluster를 추가로 분리한다. 핵심 site-level 발견은 **(i) PRKDC K2694/K2908 lactylation이 kinase activity와 양의 상관**(DNA-PK 의존 손상복구 → 치료 저항), (ii) **STAT1 K193 lactylation + T727 phosphorylation**이 STAT1 TF activity와 강한 상관, (iii) **AURKB가 lactylation-매개 조절 대상**, (iv) histone Kla(H2B K5, H3 K27 등 50+ site)는 **HER2-high에서 전반적으로 더 높음**(Wilcoxon)이다. HER2-low-특이 genomic feature는 (i) **TP53 mutation이 HER2-low에서만 poor prognosis 신호**(HER2-high에서는 비유의), (ii) **9p loss(MTAP cis-effect)가 HER2-low에서만 worse prognosis**, (iii) **7q arm-level gain(SSBP1, FIS1)이 유일한 HER2-low 우세 SCNA**, (iv) **CX3 CIN signature(NER 결함)와 JNK 신호(MAPK11/12, MAP2K7)가 HER2-low에서 활성화**되어 있다는 점. 본 연구는 동아시아 HER2-low BC의 multi-omic landscape를 제시하고 lactylome을 환자 stratification 차원에서 처음 통합한 데이터로, T-DXd / HER2-low ADC 시대에 환자 분류 기반 결정의 분자 근거를 마련한다.

## Key Points

### 코호트 / 임상 디자인

- **환자 코호트**: Harbin Medical University Cancer Hospital(Heilongjiang, 중국) prospective. IRB Protocol **KY2023-84**, written informed consent. Treatment-naive(수술 전 항암치료 없음) Chinese 환자.
- 본 분석에 포함된 시료: **115 tumor + 135 NAT (multiomics)**, **14 patient RWD(항혈관신생 치료군)**, **17 추가 환자 fresh tumor (PDO 제작용)**.
- HER2 분류 기준: 2023 ASCO/CAP — **HER2-low = IHC 1+ 또는 IHC 2+ / ISH-**, **HER2-high = IHC 3+**. HER2-negative(IHC 0)는 본 코호트에 미포함(**저자가 명시한 한계**).
- HER2-low 83명 / HER2-high 32명 구성. 임상병리적 변수: 연령·종양 크기·조직학적 grade·림프절·ER/PR/HER2/Ki67 status(Table S1).
- OS는 수술 시점 ~ 사망까지로 정의. PFS는 lactylomic subtype 비교(log-rank P=0.00172)에 사용.

### 데이터 레이어 / QC 수치

- **WES**: SureSelect Human All Exon v6(Agilent) + DNB-seq(BGI). 평균 coverage **204.48× tumor / 119.87× normal**(115T / 86N). hg38 + BWA-MEM, MuTect2 + Funcotator.
- **RNA-seq**: DNB-seq, 150bp PE. 평균 genome mapping **97.94%**, gene region mapping **75.04%**. Bowtie2(2.3.4.3) + RSEM(1.3.1), FPKM.
- **Global proteome (timsTOF Pro, Bruker)**: **8,307 proteins** identified (MaxQuant 1.6.15.0, Swiss-Prot 20,389 entries 2023.01.03, 1% peptide+protein FDR, iBAQ quantification).
- **Phosphoproteome (IMAC enrichment + timsTOF Pro)**: **43,963 phosphosites on 7,808 phosphoproteins**.
- **Lactylome (PTM-1404 antibody, PTM Bio)**: **18,214 lactylation sites on 1,644 lactylated proteins**.
- 결측 처리: tumor / NAT 양쪽에서 50% 이상 missing은 제외, DreamAI KNN imputation. 정규화는 sample median centering → log2 변환.
- **QC**: HeLa tryptic digest를 매 1–2일마다 reference QC로 측정 + Pearson 상관 표시(Fig S1C).

### 유전체 / mutation landscape

- 가장 빈번한 somatic mutation: **TP53 31%**, **PIK3CA 29%**.
- **HER2-low 특이적 유의 SCNA**: arm-level 차원에서 **7q gain**이 유일하게 HER2-low > HER2-high (SSBP1, FIS1 포함).
- **9p loss (MTAP cis-deletion 포함)**: HER2-low에서만 poor prognosis와 결합. HER2-high에서는 prognosis 신호 없음.
- **CIN signature CX3 (NER impairment)**: HER2-low에서 활성. (Sigminer + CINSignatureQuantification — Ruben et al. ref 30).
- TP53 mutation × HER2 status interaction: HER2-low subset에서만 enhanced proliferation + altered immune response. HER2-high에서는 비유의(저자 본문 — 추정 원인: HER2-high의 기저 proliferation/immune signal이 이미 강해 TP53 효과 가려짐).

### 인산화 / kinase activity

- HER2-low의 **JNK signaling cascade(MAPK11, MAPK12, MAP2K7)**이 인산화 단계에서 활성화.
- Phosphosite-level kinase activity는 PhosphoSitePlus + NetworKIN(score>5) → KSEA 앱(FDR<0.05) + ssGSEA로 도출.

### 단백체 unsupervised subtype (PS1/PS2/PS3)

- **CancerSubtypes R(v1.22.1)** consensus hierarchical clustering, Spearman 거리, 1000 bootstrap, 0.8 item subsampling. Top 50% MAD 단백질 사용. k=2~6 비교 후 **k=3 최적**(consensus matrix + CDF + delta-AUC + silhouette, Fig S5A–C).
- **PS1 (n=21) — Estrogen response signaling enriched** → 임상 가설: **endocrine therapy (tamoxifen / toremifen)**. PDO에서 PS1 organoid가 tamoxifen/toremifen에 우선 반응.
- **PS2 (n=35) — Angiogenesis enriched** → 임상 가설: **anti-angiogenic therapy (bevacizumab, apatinib)**. PDO에서 PS2 organoid가 bevacizumab/apatinib에 우선 반응.
- **PS3 (n=27) — Proliferation enriched + HER2-high-like proteomic signature** → 임상 가설: **anti-HER2 therapy (trastuzumab, T-DM1)**. PDO에서 PS3 organoid가 trastuzumab/T-DM1에 우선 반응.
- **PS3 비율 32.53%** — HER2-low BC 중 약 1/3이 HER2-high-like proteomic profile을 보유. 이는 DESTINY-Breast04(T-DXd)에서 보고된 ORR ~40%와 양적으로 정합(저자 본문 강조).

### Subtype classifier 검증

- **SVM-RFE classifier**: 70% train / 30% test, 5-fold CV, 각 PS의 GSEA signature top/bottom 20 단백질 후보 → **10-feature 모델**, train AUROC **0.97**, test AUROC **1.00**.
- **CPTAC HER2-negative cohort 외부 재현**: LinkedOmics에서 CPTAC-BRCA proteome 다운로드 후 median centering + KNN + scale normalize, HER2-negative subset만 PS classifier 적용 → 동일 PS1/PS2/PS3 패턴 재현(Fig 4/5의 외부 validation panel).
- **IHC-based deployable classifier**: 10개 단백질(**COL16A1, SBSPON, VAV3, CREBBP, ELP1, RFC1, HEATR5B, XPO5, TFDP1, TOM1L2**) IHC 점수로 학습 → **AUROC 0.80 (n=76)**. 두 명의 인증 유방암 병리과 전문의 blind 검수, 불일치 <5%는 3rd 시니어 병리과와 multi-head 현미경 합의(2023 ASCO/CAP).
- **Tamoxifen response 예측 모델**: Marchi et al. ref 41 데이터 활용 — 80%/20% split, 상위 100개 DEP → RF-RFE 특성 선택 + 5-fold CV.

### PDO 약물 검증

- **17개 PDO 생성**: Hanks BSS + collagenase type II(Gibco) 효소소화 → Matrigel + OrganoPro medium(K2 ONCOLOGY).
- 단일세포 dissociation → 2,000 cells/well 저접착 96-well + Matrigel 코팅, 48h 약물 처치, Enhanced CCK-8(BL1055C) 480-well 광흡광도.
- 결과 — PS1 PDO: tamoxifen/toremifen 우선 반응; PS2 PDO: bevacizumab/apatinib 우선 반응; PS3 PDO: trastuzumab/T-DM1 우선 반응.

### Real-World data (n=14)

- 14명의 **항혈관신생제 임상 사용 환자**의 사후(retrospective) 분석 — 본 PS subtyping을 적용한 결과 **PS2 4명 중 3명이 CR 또는 PR**, vs **PS1+PS3 10명 중 1명만 PR**(저자 본문 강조; subgroup p값은 본 PMC 텍스트에서 미명시 — 본문 Fig 5G 인근 참조).

### Lactylome 발견 (논문의 가장 신규한 axis)

- 총 **18,214 lactylation sites on 1,644 proteins** — 유방암 분야에서 첫 대규모 lactylomic reference.
- **Histone Kla 50+ sites**: H2B K5, H3 K27 등이 HER2-high에서 평균적으로 더 높음(Wilcoxon).
- **Histone Kla 조절** — Lasso regression(80%/20% split, 300 bootstrap): acyltransferase/deacylase + histone 단백질 발현 → histone lactylation site 예측. 평균 계수 |β|<0.1은 제외.
- **Lactylomic subtypes (LS1/2/3)**: k-means(Euclidean) + 상위 50% MAD lactylation site → 3 stable cluster, PFS log-rank **P=0.00172**.
- **PS2 ∩ LS3** 교집합이 PS2 내부에서 추가로 더 좋은 생존군을 분리(저자 강조).
- **AURKB는 lactylation에 의해 조절** — 본문 강조 신규 mechanism.
- **STAT1 K193 lactylation + STAT1 T727 phosphorylation**이 STAT1 TF activity(VIPER + DoRothEA)와 강한 양의 상관.
- **PRKDC (DNA-PK catalytic subunit) K2694/K2908 lactylation**: kinase activity와 양의 상관 + 짧은 PFS와 연관. 저자는 DNA 손상복구 의존 치료 저항의 분자 메커니즘으로 해석.
- **Treatment resistance 관련 다른 Kla 단백질** (본문 인용): NBS1, MRE11, XRCC1, XLF — 모두 DNA damage response.
- 단백체-PTM 비교: **MPR(Modification:Protein Ratio)** — High-MPR: MPR > median + SD; Low-MPR: MPR < median - SD. (PTR 계산법 — Mertins 2016; ref 32, 33 기반).

### Discussion 핵심 (본문)

- TP53 mut → HER2-low 특이적 proliferation + immune 변화. HER2-high는 기저 proliferation/immune 신호가 이미 강해 TP53 효과를 가린다는 해석.
- Zijian et al.(ref 37)의 hepatocellular carcinoma lactylome 보고 이후 본 연구가 **유방암 첫 대규모 histone + non-histone lactylome**.
- Lactylation은 metabolic regulation뿐 아니라 DNA repair (ref 69), transcriptional regulation (ref 70) 등 nonmetabolic 기능 확장.
- 향후 PRKDC 직접 표적 또는 lactylation 자체 억제가 치료 저항 극복 전략 후보.

### 한계 (저자 본문)

- **HER2-negative 비교군 없음** — HER2-low vs HER2-negative 구분 feature는 본 연구에서 직접 정의 불가. 저자는 향후 HER2-negative/low/high 모두 포함한 연속 spectrum 분석이 다음 단계라고 명시.
- **단일 인구집단(중국)** — Heilongjiang 중심 prospective. 다른 ancestry / 환경에서의 generalizability는 제한.
- 단일 기관 prospective(n=115 tumor) — multi-center 외부 검증은 CPTAC HER2-negative subset이 유일.
- PDO/PS3 subtype에서 trastuzumab/T-DM1 효과 검증은 in vitro 단계.

## Methods

- **WES 파이프라인**: SureSelect Human All Exon v6 + DNB-seq → SOAPnuke 2.2.1 → BWA-MEM 0.7.17 + SAMtools 1.3.1 + Picard/GATK MarkDuplicates 4.4.0 → MuTect2 4.4.0 + Funcotator 4.4.0.
- **RNA-seq 파이프라인**: SOAPnuke → Bowtie2 2.3.4.3 → RSEM 1.3.1 (FPKM).
- **SCNA**: CNVkit + GISTIC2.0 (q<0.05). 파라미터: amp/del threshold 0.1, cap 1.5, broad length cutoff 0.50, confidence 0.99, join segment 4, max segments 4000.
- **Mutational signature**: Sigminer NMF → COSMIC cosine similarity. **CIN signature**: CINSignatureQuantification(Ruben et al. ref 30 — markowetzlab).
- **Protein extraction**: TCA/acetone precipitation + lysis buffer(1% SDS, 1% protease inhibitor, 1% phosphatase inhibitor, 3 μM TSA, 50 mM NAM — NAM은 deacylase 차단). 4°C, sonication × 3, 12,000 g 10 min. BCA 정량.
- **Trypsin digestion**: 1:50 trypsin:protein, 37°C overnight, DTT 5 mM 30 min 56°C + IAM 11 mM 15 min RT dark, C18 SPE desalt.
- **Phosphopeptide enrichment**: IMAC microspheres(50% ACN / 0.5% AcOH), 10% NH4OH elution.
- **Lactylation enrichment**: PTM-1404 antibody beads(PTM Bio Hangzhou), 100 mM NaCl + 1 mM EDTA + 50 mM Tris-HCl + 0.5% NP-40 pH 8.0 overnight 4°C, 0.1% TFA elution × 3, C18 Zip Tip desalt.
- **LC-MS/MS (3 layers 모두)**: NanoElute UHPLC + timsTOF Pro(Bruker Daltonics), 25 cm × 100 μm i.d. self-packed reverse-phase, 100–1700 m/z. Global proteome: 70+14+3+3 min gradient; phospho: 76+6+4+4 min; lactylome: 40+12+4+4 min. Dynamic exclusion 24–30 s. Electrospray 1.60–1.75 kV. PASEF mode, 10 PASEF-MS/MS scans/cycle.
- **데이터베이스 검색**: MaxQuant 1.6.15.0 + Swiss-Prot 20,389 entries(2023.01.03) + reverse decoy. Trypsin/P 최대 missed cleavage 2 (phospho/proteome), 4 (lactylome). MS1 tol 20 ppm, MS2 tol 20 ppm. Fixed: Carbamidomethyl(C); Variable: protein N-term acetylation, Met oxidation, +phospho(S/T/Y), +Kla(K). 1% FDR peptide + protein.
- **단백체 정량**: iBAQ. Phospho/Kla는 site level.
- **GSEA / GSVA / KSEA / Kinase activity**: GSEA v4.3.2 + KEGG + WikiPathways + HALLMARK (MSigDB v7.1). ssGSEA via GSVA. KSEA app(casecpb.shinyapps.io/ksea) + PhosphoSitePlus + NetworKIN (score>5), FDR<0.05.
- **TF activity**: DoRothEA(A,B,C confidence) → VIPER. TP53 target도 DoRothEA.
- **Proteomic subtyping**: CancerSubtypes R v1.22.1, Spearman, 1000 bootstrap, item 0.8 / feature 1.0, top 50% MAD HER2-low samples.
- **Lactylomic subtyping**: k-means Euclidean, top 50% MAD lactylation site, 동일 1000 bootstrap.
- **SVM-RFE classifier**: 70/30 split, 5-fold CV, GSEA top/bottom 20 단백질/PS subtype → 최종 10 feature.
- **IHC**: 60°C 20 min deparaffinize → xylene → alcohol gradient → 95–100°C citrate buffer 항원회수 → blocking(2% goat serum + 2% BSA + 0.05% Tween) 2h RT → primary antibody overnight 4°C → 0.3% H2O2 + HRP 2nd Ab(Abbkine A21020/A21030) + DAB(ZSGB-BIO ZLI-9018) + hematoxylin. 10× 시야(≈2 mm²)에서 양성세포 카운트. 2명의 board-certified 유방암 병리과 blind → 5% 이내 불일치는 3rd 시니어와 합의.
- **IHC 항체**: COL16A1 ab231044, SBSPON HPA029595, VAV3 NB300-817, CREBBP HPA055861, ELP1 HPA050686, RFC1 ab180613, HEATR5B HPA042025, XPO5 HPA023959, TFDP1 ab186831, TOM1L2 HPA022541.
- **PDO 모델**: Hanks BSS + 항생제 + collagenase II(Gibco 17101015, 2 mg/mL) 37°C 1h → 100 μm cell strainer → 1640 medium(Gibco 11875093) + Matrigel(Corning 356231) → 24-well plate → OrganoPro medium(K2 ONCOLOGY K2O-M-BR). 약물처치: 2,000 cells/well, 저접착 96-well + Matrigel 코팅, 48h, Enhanced CCK-8(BL1055C 1:10) 1h RT, Enspire 2300 microplate reader.
- **TME**: ESTIMATE R v1.0.11(immune score, stromal score, tumor purity) + xCell(64 cell type → tumor에 없는 hepatocyte/neuron/astrocyte 제외).
- **Histone Kla 조절 모델**: Lasso regression, acyltransferase/deacylase + histone 단백질 → histone lactylation site dependent, 80%/20% × 300 bootstrap, 평균 계수 |β|<0.1 제외. Spearman: histone Kla site ↔ Hallmark GSVA.

## Cancer Multiomics Project Relevance

본 논문은 한미약품-Yonsei 한미암 표적항암치료제 멀티오믹스 프로젝트와 **(a) 동아시아 HER2-low BC 참조 데이터, (b) 환자 stratification 전개도, (c) lactylome 신규 modality 도입 평가, (d) ADC/T-DXd 전략 결정 보조 마커**의 네 차원에서 사용 가능하다. 모두 본 논문 본문 결과 기반의 적용 후보이며 한미암 자체 데이터로 재현 검증이 전제된다.

- **동아시아 HER2-low BC 참조 코호트(중국 n=83) — 한국인 한미암 코호트의 비교 baseline**: 본 논문은 IHC 0(HER2-negative)을 제외했지만, HER2-low(IHC 1+ / IHC 2+ ISH-) 정의는 2023 ASCO/CAP 기준으로 한국 임상에서도 호환된다. 한미암 한국인 HER2-low 환자 baseline biopsy를 본 데이터셋과 동일 4-layer 스택(WES + RNA-seq + global proteome + phosphoproteome)으로 비교 → PS1/PS2/PS3 분포(21/35/27)가 한국인에서 재현되는지가 1차 검증 포인트.
- **PS subtype 기반 환자 stratification 가이드**:
  - PS1(n=21, estrogen response high) — HER2-low subset 중 일부에서 ER/PR IHC 음성/약양성에도 단백체 estrogen 신호가 있다면, 한미암 SERD/endocrine 후보 환자 선정에 사용 가능. (Lee 2026 TNBC 논문에서 ER/PR 음성에서도 estrogen 단백 시그니처 관찰과 일관된 신호 — 두 한국·중국 코호트 모두 IHC 음성 ≠ 호르몬 신호 부재라는 결론으로 수렴 가능성.)
  - PS2(n=35, angiogenesis high) — 14명 RWD에서 PS2 3/4 CR/PR vs PS1+PS3 1/10 → 항혈관신생제(bevacizumab, apatinib) 우선 환자군. 한미암이 anti-angiogenic 후보 또는 anti-VEGF ADC 후보를 보유 중일 때, baseline proteome으로 사전 환자 선별을 시도할 수 있는 분자 근거.
  - PS3(n=27, 32.53%, proliferation + HER2-high-like) — DESTINY-Breast04에서 T-DXd ORR ~40%와 양적으로 일치하는 sub-population. **한미암이 T-DXd 후보 또는 HER2 ADC 후보를 한국인 HER2-low에 적용할 경우, PS3 stratification이 직접 적용 가능한 환자 선택 마커.** 단, 본 논문 검증은 PDO + 외부 CPTAC HER2-negative subset 수준이며 prospective 임상 검증은 아님.
- **IHC 10-단백질 보조 classifier(AUROC 0.80, n=76)는 한미암에서 즉시 도입 가능한 deployable workflow**: COL16A1, SBSPON, VAV3, CREBBP, ELP1, RFC1, HEATR5B, XPO5, TFDP1, TOM1L2 — 모두 상용 항체(Abcam, Atlas Antibodies, Novus) 보유. proteome 전체 없이도 임상병리 IHC 패널로 PS subtype 분류 가능 → 한미암 임상 사이트에서 환자 등록 단계 빠른 stratification 시도 가능. (다만 AUROC 0.80은 같은 코호트 76명 내부 — 한국인 코호트 외부 검증 별도 필요.)
- **Lactylome — 한미암 플랫폼에 아직 없는 신규 modality 평가용 reference**: 본 논문 18,214 Kla site / 1,644 단백질은 유방암 첫 대규모 lactylomic baseline. **PRKDC K2694/K2908 + STAT1 K193 + AURKB**는 한미암 자체 lactylomic 데이터 생성이 어려울 경우에도 phospho 및 protein abundance 데이터로 일부 간접 추적 가능한 site. 한미암이 lactylome enrichment(PTM-1404 antibody) workflow를 도입할 가치가 있는지의 cost-benefit 평가 시 본 reference가 첫 참고점.
- **PRKDC lactylation → DNA-PK 의존 치료저항** 가설: 한미암이 anthracycline/방사선 치료 또는 DNA damage 유도 약물 파이프라인을 보유 중이라면, PRKDC 자체 / lactylation 일반 억제(예: HDAC inhibitor 등 본문에서 추론) 병용 가설을 lactylome reference로 grounding 가능. 본 논문 자체에서 약리적 검증은 없음 — 가설 단계로 한정.
- **JNK 신호(MAPK11/12, MAP2K7) HER2-low 활성**: 한미암 phosphoproteome / 인산화 단계 데이터에서 동일 axis가 잡힌다면, JNK 표적 또는 stress kinase 억제 후보 평가의 분자 근거. 본 논문은 신호 활성을 phosphoproteome으로 식별한 단계까지(약리 검증 없음).
- **7q gain(SSBP1, FIS1) — HER2-low 유일한 enriched arm-level SCNA**: copy number 차원의 단일 marker로 HER2-low 식별에 보조 (그러나 본 논문은 patient stratification까지 진행하지 않음).
- **9p loss + MTAP cis-deletion → HER2-low 특이 poor prognosis**: MTAP-loss 종양에 대한 합성치사(MAT2A / PRMT5 inhibitor) 전략은 다른 암종에서 보고 — 한미암이 MAT2A/PRMT5 후보를 보유 중이라면 HER2-low 9p loss subset이 후보 환자군. 본 논문 자체에서 합성치사 약리 검증은 없음.

**한계 / 사용 시 주의 (본 논문 본문 명시)**: (i) HER2-negative (IHC 0) cohort 없음 → HER2-low vs HER2-negative 분류 신뢰성은 본 데이터로 직접 평가 불가, (ii) 단일 인구집단(중국 Heilongjiang) → 한국인 코호트에서 PS 분포 재현은 한미암이 직접 검증해야 함, (iii) PS3 → T-DXd ORR 연결은 분자적 정합 + 비율 일치 수준 — prospective 임상 데이터로 입증된 단계 아님, (iv) PDO 실험 n=17 — drug response 검증의 효과 크기는 본 PMC 텍스트에서 정량적 P값 미명시(Fig 5/Fig 6 참조), (v) IHC SVM AUROC 0.80은 same-cohort 76명 내부.

## Connections

- [Cancer Multiomics Literature Topic Hub](../topics/cancer-multiomics-literature.md) — Section 1 WGS/Proteogenomics 통합 기반.
- [Lee 2026 — Proteogenomic Decoding of Chemotherapy Resistance in TNBC](lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md) — 한국인 TNBC(Severance n=50) 결과와 동아시아 BC stratification 관점에서 직접 비교. 두 코호트 모두 ER/PR 음성에서도 estrogen 단백체 신호 보고 → IHC 음성과 단백체 신호의 불일치라는 공통 주제.
- [Krug 2020 — Proteogenomic landscape of breast cancer tumorigenesis (PTM-preserved)](../analyses/cancer-multiomics-literature/krug-2020-proteogenomic-landscape-breast-cancer-tumorigenesis.md) — CPTAC-BRCA reference, 본 논문에서 외부 validation cohort로 사용(LinkedOmics).
- [Jiang 2024 — Integrated Multi-omic Profiling of Breast Cancer](jiang-2024-integrated-multiomic-profiling-breast-cancer.md) — Chinese BC proteogenomic cohort, 동아시아 BC stratification 비교.
- [Cancer Multiomics Corpus Queue](../analyses/cancer-multiomics-corpus-queue.md)

## Sources

- Local HTML (PMC OA): `raw/inbox/papers/xu-2026-proteogenomic-her2-low-breast-cancer-subtypes.html` (313 KB, PMC HTML; PDF route blocked by anti-bot — extracted via pandoc → plain text 1,957 lines for analysis).
- Wiley OA: <https://advanced.onlinelibrary.wiley.com/doi/full/10.1002/advs.202513086>
- PMC: <https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12948274/>
- PubMed: <https://pubmed.ncbi.nlm.nih.gov/41454718/>
- DOI: <https://doi.org/10.1002/advs.202513086>
- Data Availability: 저자 본문 — "available from the corresponding author upon reasonable request" (공개 repository 식별자는 본 PMC 텍스트에서 미명시).
