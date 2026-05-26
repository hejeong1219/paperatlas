---
title: Cancer Multiomics Proteogenomic Atlas
tags:
  - cancer-multiomics
  - wgs
  - phosphoproteomics
  - proteogenomics
  - slack-digest
themes:
  - targeted-immunotherapy-resistance
  - ppqtl
  - neoantigen
  - kinase-signaling
  - response-prediction
---

# Cancer Multiomics Proteogenomic Atlas

Cancer Multiomics 과제의 중심 질문을 따라 인간암 proteogenomics, phosphoproteomics, spatial multiomics, neoantigen, 치료반응 예측 근거를 구조화한 프로젝트형 topic hub.

## Key Points

- 과제의 중심 질문은 전장유전체만으로 설명되지 않는 표적-면역치료제 반응성 및 내성 차이를 인산화단백체, kinase network, neoantigen, 면역 관련 feature와 통합해 설명할 수 있는지다.
- 논문 정리는 단순 요약이 아니라 과제의 4개 축에 직접 연결한다: 인산화단백체 분석 파이프라인, WGS-PTM 통합/ppQTL, 신생항원 및 면역회피, 치료반응 예측 모델.
- 각 논문은 하위 페이지로 정리하고, topic hub에는 분류별로 링크와 Slack 공유용 핵심 포인트만 남긴다.
- Slack 메시지는 교수진에게 바로 공유 가능한 짧은 형식으로 별도 섹션에 보존한다.
- 진행 현황/큐: [Cancer Multiomics Corpus Queue (Target=100)](../analyses/cancer-multiomics-corpus-queue.md)
- 항암제 반응성/내성 + global proteome/phosphoproteome 특화 큐: [Drug Response Phospho-Global Proteomics Corpus Queue (Target=100)](../analyses/drug-response-phospho-global-100-corpus-queue.md)

## Project Alignment

- **WGS 변이 해석**: SNV, indel, structural variant, copy-number signature, noncoding mutation, germline feature, HLA typing.
- **인산화단백체 분석**: TMT/DIA 기반 phosphoproteomics, 결측/배치 보정, phosphosite-level differential analysis, kinase activity inference.
- **WGS-단백체 통합**: pQTL, ppQTL, copy-number-to-protein effect, driver-to-functional-state mapping.
- **면역/신생항원**: WGS 기반 neoantigen candidate, HLA binding prediction, immunopeptidomics/proteogenomic validation, immune evasion.
- **치료반응 예측**: response/non-response classification, primary/acquired resistance, SHAP-style feature interpretation, basket-trial molecular grouping.
- **데이터 공유**: CPTAC/GDC/PDC/NCDC 기탁, 분석 재현성, cloud-scale WGS/proteomics integration.

## 하위 페이지 템플릿

각 논문 페이지는 최소한 아래 구조를 따른다.

```markdown
## 논문 정보 (저자 / 저널 / DOI / Wiki 경로)
## 한 줄 요약
## 과제 관련성 (Cancer Multiomics)
## 주요 결과
## Slack 메시지 초안
```

## 표준 메타데이터 체크리스트 (하위 페이지 공통)

하위 페이지에 아래 3개 bullet을 **고정 섹션**으로 넣는다(모르면 “PDF 확인 필요”로 표기).

- 치료 맥락: 암종 / 치료제 class / 라인 / 반응 라벨(Primary/Acquired 등) / 샘플 타이밍
- 데이터 레이어: WGS/WES, RNA-seq, proteome, phosphoproteome, acetylome, immunopeptidomics, spatial 등
- 데이터 공개: raw/processed/supplement/code(접근 경로는 PDF의 Data Availability 기준)

## Next Candidates

다음 배치에서 다룰 “PDF는 있으나 Cancer Multiomics 하위 페이지가 아직 없는” 후보는 큐에서 관리한다:

- [Cancer Multiomics Corpus Queue (Target=100)](../analyses/cancer-multiomics-corpus-queue.md)

## 1. WGS와 Proteogenomics 통합 기반

- [Chen 2020 - Non-Smoking Lung Cancer Proteogenomics](../analyses/cancer-multiomics-literature/chen-2020-non-smoking-lung-cancer-proteogenomics.md) - 동아시아 비흡연 폐암에서 WGS/단백체/인산화단백체를 통합해 EGFR-mutant 조기 폐암의 분자 이질성과 진행 축을 설명한다.
- [Huang 2021 - HPV-Negative HNSCC Proteogenomics](../analyses/cancer-multiomics-literature/huang-2021-hnscc-proteogenomics.md) - HNSCC에서 phosphoproteomics가 EGFR activation mode, immune-hot/cold state, 치료 취약성을 어떻게 분리하는지 보여준다.
- [Satpathy 2021 - LSCC Proteogenomic Portrait (WGS/WES + Multi-PTM + Immune)](../analyses/cancer-multiomics-literature/satpathy-2021-proteogenomic-portrait-lung-squamous-cell.md) - LSCC에서 WGS/WES+multi-PTM을 통합해 NSD3 driver, Rb phosphorylation 기반 CDK4/6 기능 biomarker 등 “유전→기능 상태” 연결을 제시한다.
- [Dou 2020 - Endometrial Carcinoma Proteogenomics (WES/WGS + Phospho + Acetyl + Immune)](../analyses/cancer-multiomics-literature/dou-2020-proteogenomic-characterization-endometrial-carcinoma.md) - CPTAC 자궁내막암에서 WES/WGS subtype을 proteome/phospho/acetyl 기능 상태로 재해석하고 MSI의 항원제시 결함 같은 면역 축까지 연결한다.
- [Clark 2019 - ccRCC CPTAC Proteogenomics (Tumor+NAT; immune subtypes)](../analyses/cancer-multiomics-literature/clark-2019-integrated-proteogenomic-characterization-clear-cell.md) - ccRCC에서 proteome/phosphoproteome + multi-omics를 통합해 genomic instability, 대사/번역/인산화 모듈 및 4개 immune subtype을 기능 상태로 제시한다.
- [Gillette 2020 - LUAD CPTAC Proteogenomics (Tumor+NAT; Phospho+Acetyl)](../analyses/cancer-multiomics-literature/gillette-2020-proteogenomic-characterization-reveals-therapeutic-vulnerabilities.md) - LUAD tumor+NAT에서 KRAS/EGFR/ALK driver 연관 기능 상태와 STK11-immune-cold 축을 proteome/phospho/acetyl 레이어로 해석한다.
- [Krug 2020 - Breast Cancer Proteogenomics (PTM-preserved; HER2/Rb/kinase)](../analyses/cancer-multiomics-literature/krug-2020-proteogenomic-landscape-breast-cancer-tumorigenesis.md) - PTM 보존 수집 코호트로 HER2(ERBB2), Rb, kinase signaling을 proteogenomics로 재정의하고 치료 취약성 후보를 논의한다.
- [Cao 2021 - PDAC CPTAC Proteogenomics (WGS/WES + Phospho + Glyco)](../analyses/cancer-multiomics-literature/cao-2021-proteogenomic-characterization-pancreatic-ductal-adenocarcinoma.md) - PDAC에서 WGS/WES·전사체·메틸화와 proteome/phosphoproteome/glycoproteome을 동일 샘플로 통합한 리소스.
- [Chen 2023 - SV Breakpoints → Protein Consequences (Pan-cancer WGS+Proteomics)](../analyses/cancer-multiomics-literature/chen-2023-global-impact-somatic-structural-variation-cancer-proteome.md) - WGS 기반 SV breakpoint 패턴이 단백질 발현으로 “실제 반영”되는 비율을 pan-cancer로 정량화해, SV-aware proteogenomics 필요성을 강조한다.
- [Chen 2026 - Germline SV → Cancer Proteome (Pan-cancer CPTAC + Ancestry + Methylation Mediation)](../sources/chen-2026-global-impact-germline-structural-variation-cancer-proteome.md) - Chen 2023 자매 논문, somatic이 아닌 **germline** structural variation의 cancer proteome cis-effect. CPTAC 11개 종양형 **1,637 환자** normal-WGS(Delly v3.1.1 ∩ SVABA v1.2.0, hg38, 200 bp slop) + RNA-seq + 정량 proteomics ± 450K methylation 통합. **704,263 distinct germline SV**(86% singleton; 84% DGV/gnomAD/TOPMed catalog 등재); 114,684 rare/singleton 중 **25,781 LoF SV**(SVAnnotate) → 12,442 paired proteomics에서 **1,847 low-protein outlier event(512 genes × 786 patients, FDR<10%)**. Hypergeometric: MHC class I antigen binding / antigen processing / exosome / mitochondrial matrix / Golgi enriched. **CSG enrichment**: 688 cancer susceptibility gene 중 **31개**(CDH13/CDKN2A/MSR1/SDHA/SMAD4/SMARCB1)에 LoF SV 보유자 단백 저발현, **101명(전체 6%)** 최소 1개 CSG LoF SV. **364 recurrent SV-altered gene 중 129개(17%) mRNA+protein concordant**(CA8/PTGR1 등 cis-locus); 33%는 protein-only direction(reverse) → MS-based proteomics가 mRNA-only로 못 잡는 cis-effect 포착. **CGI methylation 매개**: **1,237 CGI probe FDR<10%** SV-methylation cis; 233/2,686 positive-methylation → negative-mRNA 28개 protein concordant(CES1/GGACT/PTDSS2). **Enhancer methylation 매개**: 109 SV-enhancer-methylation pair 중 41개 CBTN pediatric brain tumour 재현(p<1E-22; ECHDC1/SH3GLB2/MAMDC2). **Tumour-type-specific**: 137 genes 단일 tissue에서만 concordant(pan-tissue 17개), 60 CGI probe tissue-specific(CDK2 GBM / RHOH LUAD / ARIH1 CCRCC). **Ancestry-enriched**: 69 concordant gene 중 **31(45%)** ancestry-specific — 10 African(FSCN1) / 8 Asian(TIGAR) / 13 European(CTSW); SIDT2는 ancestry alone explain → ancestry-aware analysis 필수. **DepMap + survival 교차**: **FABP5/NEDD1/TOP2A** 양쪽 통과; TOP2A common germline SV ~25–30% 환자. Data dbGaP phs001287.v21.p6 + phs003011.v1.p1 + phs000178.v11.p8 + PDC + GDC + CBTN/Cavatica + UALCAN + figshare. 한계: paired SV caller LoF 일부 잘림 + 단일 timepoint normal sample + Delly/SVABA short-read limitation(long-read WGS 미적용). Nat Commun 2026; DOI 10.1038/s41467-026-71967-y. User-shared via Springer 2026-05-12 PDF.
- [Li 2023 - Pan-Cancer Driver-to-Functional-State Proteogenomics](../analyses/cancer-multiomics-literature/li-2023-pan-cancer-driver-functional-states.md) - pan-cancer CPTAC 데이터로 driver event가 RNA, protein, phosphoprotein functional state로 어떻게 번역되는지 정리한다.
- [Savage 2024 - CPTAC Pan-Cancer Therapeutic Target Landscape](../analyses/cancer-multiomics-literature/savage-2024-pan-cancer-proteogenomics-expands-landscape-therapeutic.md) - pan-cancer proteogenomics를 기반으로 druggable dependency/synthetic lethality/항원 후보를 protein/phosphoprotein 상태에서 우선순위화한다.
- [Deng 2023 - Cholangiocarcinoma Proteogenomics (WES + Phosphoproteome)](../analyses/cancer-multiomics-literature/deng-2023-proteogenomic-characterization-cholangiocarcinoma.md) - 대규모 CCA 코호트에서 WES+phosphoproteome을 통합해 subtype과 kinase/면역 가설을 제시한다.
- [Cheng 2025 - Wilms Tumor Proteogenomics (WES + Phosphoproteome)](../analyses/cancer-multiomics-literature/cheng-2025-integrative-proteogenomic-characterization-wilms-tumor.md) - 소아 WT에서 tumor–NAT multi-omics로 아형을 정의하고 EHMT2 등 후보를 제시한다.
- [Song 2024 - NSCLC Multi-Omics Subtypes (WGD / PI3K–Akt / TME)](../analyses/cancer-multiomics-literature/song-2024-proteogenomic-analysis-reveals-non-small-cell.md) - 한국인 NSCLC 229명에서 WES+proteome/phosphoproteome(+acetylome)로 5개 subtype을 정의하고 WGD/면역 축과 예후·adjuvant therapy 신호를 연결한다.
- [Yu 2024 - Cervical Cancer Proteogenomics (Phospho + Acetyl + Radioresponse)](../analyses/cancer-multiomics-literature/yu-2024-proteogenomic-analysis-cervical-cancer-reveals.md) - 자궁경부암 139명에서 WES+phosphoproteome+acetylome을 통합해 3개 subgroup 및 radioresponse biomarker 후보(PRKCB)를 제시한다.
- [Qu 2024 - PTC Recurrence Risk Multi-Omics (Proteome + Phospho + Metabolome)](../analyses/cancer-multiomics-literature/qu-2024-integrated-proteogenomic-metabolomic-characterization-papillary.md) - PTC 102명에서 재발 위험을 multi-omics subtype으로 분해(대사형/면역형 등)하는 아시아 코호트 레퍼런스.
- [Tanaka 2024 - CRC Primary vs Liver Metastasis Proteogenomics](../analyses/cancer-multiomics-literature/tanaka-2024-proteogenomic-characterization-primary-colorectal-cancer.md) - 원발/간 전이 CRC 대규모 proteogenomics로 hypoxia/stemness/immune-cold(항원제시 억제) 진행 시그니처를 정리한다.
- [Ramsberger 2024 - Multiple Myeloma Proteogenomics (Nanopore WGS + Phosphoproteome)](../analyses/cancer-multiomics-literature/ramberger-2024-proteogenomic-landscape-multiple-myeloma-reveals.md) - nanopore WGS(CNV) + TMT phosphoproteomics로 CNA–기능 상태를 연결하고 phosphoproteomic risk stratification 사례를 제시한다(고형암 외이지만 설계 참고용).
- [Awasthi 2026 - PEXMap: k-mer 기반 Exon/Isoform-Resolved Peptide Mapper](../sources/awasthi-2026-pexmap-proteogenomic-exon-isoform-mapping.md) - MS/MS peptide를 8-mer 정확매칭으로 gene/transcript/exon/EXj 수준에 매핑하는 splice-isoform-aware proteogenomic 도구; PeptideAtlas 99.4% gene / 81.8% exon 정확도, EGFR 절단형·FLNA 엑손-30 skip 등 cancer isoform 사례를 EXj 증거로 제시. (tool · bioRxiv 2026)
- [Jiang 2026 - 3DisoGalaxy: 유방암 Translation-Supported Isoform Foldome Atlas](../sources/jiang-2026-3disogalaxy-breast-cancer-isoform-foldome.md) - PacBio Iso-Seq + Ribo-seq + AlphaFold2를 통합해 73,715 translation-supported ORF / 46,601 high-confidence 구조 + structural similarity network를 구축, KRAS4A C-말단 motif 손실과 ΔPH AKT1의 TNBC-biased 발현·RFS 연관(log-rank P=0.046)을 hypothesis-generating sci-grounded proteoform biology로 제시. (atlas · tool · bioRxiv 2026)
- [Lehe 2026 - Alternative Protein Isoform 분석을 위한 MS Instrumentation & Methodology 리뷰](../sources/lehe-2026-mass-spectrometry-alternative-protein-isoforms-review.md) - Sheynkman lab(UVa)의 splice-derived proteoform MS 방법론 리뷰. DDA(0–10→ultra-deep 4,608 AS event)부터 DIA(SWATH 2,964/Astral 935/일)·IS-PRM(WTC11 77 vs DDA 21)·top-down(FAIMS 267, NCI RAS 39 KRAS proteoform)까지 acquisition 매트릭스(Table 1) 및 long-read-DB·library-free DIA·de novo splice peptide·open-search 도구 stack(Table 2)을 cancer proteogenomic validation pipeline 관점에서 제시. (review · J. Mass Spectrom. 2026)
- [Sambath 2026 - Indian Cervical Cancer Chemoradiation Resistance Proteogenomics (WGS + Proteome + Phospho)](../sources/sambath-2026-integrated-genomic-proteomic-cervical-cancer-chemoradiation-resistance.md) - 인도 자궁경부암 36명(stage IIIB squamous HPV+) WGS 26(15 paired+10 unpaired)+WES 10 paired+TMT global proteome 10+동일 cohort phosphoproteome 통합. RECIST CCRT sens 19/res 17 binary classification. Resistant 코호트 고유 신호: 7p EGFR amp 6명, STK11 SV deletion 4명, chromothripsis 3/12, DNA repair + WNT/β-catenin pathway enrichment. Proteome top5 up: SERPINB7/STX3/LBP/EMILIN2/NQO2 — STX3는 IHC validation 32명에서 일관되게 elevated. CNA-protein trans hotspot 6q/9q/11p/22q. OncoKB Level 1 33%/2 11%/3A 25%/4 5%, EGFR amp는 Level 3(esophagogastric cetuximab 적응증). DNA repair pathway hyperactivation (ATM/ATR/BRCA2/RAD50 + CSNK2A1/SMC1A phospho)이 resistance 메커니즘. (research · Molecular Oncology 2026)
- [Lee 2026 - Korean TNBC NAC Resistance Proteogenomics (Severance n=50; AURKB·GRK2·ITGB8)](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md) - 한국인 stage II–III TNBC 50명 anthracycline+taxane neoadjuvant 코호트(IRB 4-2020-0473) baseline n=41 + paired post-treatment n=22로 WES + RNA-seq + TMT global proteome(10,457) + phosphoproteome(31,258 sites/5,373 proteins) 통합. NMF 5 subtype(immune/xenobiotic/EMT/MYC/mesenchymal+estrogen) pCR 55.6%/0%/0%/—/—; METABRIC n=258 외부 검증 197(76.3%). 5개 저항인자(estrogen GSVA + GRK2 PTM-SEA + ITGB8 7p21 no-loss + AKR1C2 + ABCA13) logistic regression non-pCR AUC **0.946** (Lehmann 0.781, +ESTIMATE 0.818). Druggable target 검증: barasertib(10 nM) + paclitaxel MDA-MB-468·HCC1937·organoid SBO-72 시너지; βARK1 + paclitaxel MDA-MB-231 Bliss synergy 8.08. ITGB8 CN status별 pCR 80%/41.7%/12.6%/0%(loss/loss/dip/gain, P=0.036), Cancer Surfaceome Atlas 교집합 ITGB8/THSD7A/TSPAN13 → ADC 후보. carboplatin 6/50(12%, AC→Pac 72%) — Anurag et al. 100% carboplatin과 명시적 대비. Data PRJNA1422845/1422844 + PDC000695/696. (translational · Genome Biology 2026)
- [Xu 2026 - Chinese HER2-low Breast Cancer Proteogenomics + Lactylome (PS1/PS2/PS3 stratification)](../sources/xu-2026-proteogenomic-characterization-reveals-subtype-specific-therapeutic.md) - 중국 Harbin Medical Univ Cancer Hospital prospective 115 tumor (HER2-low n=83 IHC 1+/2+ISH- + HER2-high n=32 IHC 3+) + 135 NAT + 14 RWD + 17 PDO. Treatment-naive Chinese, IRB KY2023-84. WES(115T 204.48×/86N 119.87×) + RNA-seq + global proteome **8,307 proteins** + phosphoproteome **43,963 sites / 7,808 proteins** + **lactylome 18,214 sites / 1,644 proteins** (timsTOF Pro + IMAC + PTM-1404 antibody). 3 proteomic subtype: PS1 n=21 estrogen response → tamoxifen/toremifen; PS2 n=35 angiogenesis → bevacizumab/apatinib; **PS3 n=27 (32.53%) proliferation + HER2-high-like → trastuzumab/T-DM1** (DESTINY-Breast04 T-DXd ORR ~40%와 양적 정합). SVM-RFE 10-feature train AUROC 0.97 / test 1.00; **IHC 10-단백질(COL16A1/SBSPON/VAV3/CREBBP/ELP1/RFC1/HEATR5B/XPO5/TFDP1/TOM1L2) AUROC 0.80 (n=76)** — 임상 사이트 deployable. RWD 14명 항혈관신생 치료: PS2 3/4 CR/PR vs PS1+PS3 1/10. 3 lactylomic subtype LS1/2/3 PFS log-rank **P=0.00172**. 핵심 Kla site: **PRKDC K2694/K2908 lactylation ↔ kinase activity ↑ + PFS ↓** (DNA-PK 의존 저항), STAT1 K193 lactylation + T727 phosphorylation ↔ STAT1 TF activity (VIPER+DoRothEA), AURKB lactylation-매개 조절. HER2-low 특이 SCNA: 7q gain (SSBP1/FIS1) 유일; **TP53 mut + 9p loss(MTAP cis) → HER2-low 한정 poor prognosis** (HER2-high에서는 비유의). CIN signature CX3 (NER 결함) + JNK 신호(MAPK11/12, MAP2K7) HER2-low 활성. Histone Kla H2B K5/H3 K27 등 50+ site는 HER2-high에서 더 높음. PDO subtype-specific drug response 검증 (PS1↑tamoxifen·toremifen / PS2↑bevacizumab·apatinib / PS3↑trastuzumab·T-DM1). CPTAC HER2-negative subset 외부 재현. 한계 본문 명시: HER2-negative 비교군 없음, 단일 인구(중국 Heilongjiang), PS-T-DXd 연결은 분자 정합 + 비율 일치 수준 — prospective 임상 입증 아님. PMC12948274. (proteogenomic · Advanced Science 2026)
- [Chang 2026 - Taiwanese Gastric Cancer Proteogenomics (n=154) + DBAC Carcinogen + SA Microbiome + 4-Anatomy + CDK4 Hub](../sources/chang-2026-integrative-proteogenomics-gastric-cancer-taiwan.md) - NTUH + KMUH + Academia Sinica IBC treatment-naïve East Asian Han Chinese 위암 154명 (2022-03~2024-12, median 67y, 62% male, 25% stage I, antral 우세) + 185명 KMUH endoscopy 외부 검증. WES 14,134 nonsyn / RNA-seq 19,504 transcripts / TMT proteome **>10,000 proteins** / phosphoproteome **30,000 sites** / microbial RNA(HRGMv2 MAPQ>10) + microbial protein(UniProt FDR<0.01, ≥5 unique protein/species) / IHC(MMR/HER2/CLDN18.2/PD-L1) / dual IgG ELISA+조직 pathology HP status (HP_E 69.5% / HP_N 30.5% / HP_A 22.7% culture+CagA PCR). **NMF 7 mutational signature(G1–G7) + 6 carcinogen cluster(C1–C6)**: G1 spontaneous deamination / G2 tumour MMR / G3 polymerase-η / G4 NAT MMR / G5 DSB repair / G6 nitrosamine / G7 irradiation + **DBAC PAH(dibenz[a,h]acridine) East-Asia 특이 high-risk signature**. **DBAC HR 2.36–3.16 multivariable Cox**(age/sex/stage 조정), diffuse subtype **5.9× EFS risk(p=0.013)**, Treg p=0.002 immunosuppressive cold TME. Cell-line 검증: **BaP MKN45 3.7× / MKN28 2.7× invasion(p<0.05)**; PAH-treated cells DBAC tissue signature pathway 일치(cell migration/matrix adhesion/neutrophil degranulation/p53). DBAC TCGA 부재, Taiwanese+Japanese cohort 존재(charcoal-grilling/pan-frying dietary BaP cooked 1.30 ng/g vs raw 0.12 ng/g). **Microbiome 4 RNA cluster + protein cross-validation 14 species**: Microvirga-dominant(DBAC link **p=9.3e-12**, M. pneumoniae co-occur, G2 peroxisome/CYP450) + HP-dominant(HP_E p=4.97e-8, IM1+PN3 inflammatory) + Streptococcus-dominant(C1+C3 nitrosamine **p=6.8e-10**, 젊은층 p=0.018, G1 cytoskeletal/hedgehog/DNA repair ↓) + Mixed(L. reuteri probiotic, immune-cold IM2/IM4). Bivariate φ: DBAC↔Microvirga **0.50** / Cardiobacterium **0.53** / F. nucleatum 0.20 / Desulfovibrio↔nitrosamine 0.31. **KMUH n=185 외부 검증 SA gastric juice prevalence**: no IM **47.3%** → IM **56.9%** → cancer **86.4%**. **3 NAT proteome cluster(PN1–PN3) Sankey 4 immune cluster(IM1–IM4)**: PN3 HP-driven intestinal IM1 (CagA virulence); PN1 female/diffuse mixed-HP partial-immune; PN2 non-HP F. nucleatum + N. aromaticivorans 이질자극 immune-silent antral (xenobiotic/estrogen activator). **Tumour 4 proteome cluster(PT1–PT4) + 5 immune cluster + PT1-IM1 vs PT1-IM3 bifurcation(p=0.025)**: PT1-IM3가 **stage IV 사망률 초과**. PT1↔Bormann type 3(p=0.002), PT2↔HP+(p=0.003), PT3↔diffuse(p=0.02), PT4↔intestinal(p=0.01). **HP-negative HP_N(n=47) 3 cluster T1–T3**: T2 SA-linked barrier loss (**CLDN18.2/OCLN/ZO-1 reduction** Wilcoxon adj. p<0.05, EMT/IL-17/NOD-like/NF-κB/PI3K-AKT, FN1/THBS1/PDGFRB ↑); T1 CLDN18.2-high epithelial-stable (innate immune ↓, **42% met 43-14A IHC criteria** for CLDN18.2-targeted therapy, late-stage Bormann type 4 diffuse 후기). **4 anatomy cluster(Loc 1–4) η²=0.257 vs binary η²=0.077, p=0.00386**: Loc 1 cardia TP53/MAPK; Loc 2 mid-body ABL1/SYK/ROCK; Loc 3 antrum BRAF/CDK4/ERBB2; Loc 4 antrum MET/PRKAA2/MYC. **Loc 4 antrum 5 prognostic biomarker** (SHROOM1, p-LYST S2627, XYLT1, CRIP1, SPATS2L) KM Plotter n=118–875 외부 검증. **CDK4 actionable hub**: IHC-positive + proteome-defined-positive(HER2/PD-L1/CLDN18.2 high) + IHC-negative(49.2%) 3 subgroup 공통 — palbociclib/ribociclib repurposing 후보. Decision tree EFS(stage+DBAC), OS(stage+C3+PT1+IM2/3). 한계: HP_A 22.7%, single-cohort Taiwanese, BaP cell-line 검증만 (DBAC 직접 검증 미수행), KEA3 location-specific kinase는 inference. Data dbGaP **phs004447.v1.p1** + PDC **PDC000645**(proteome) + **PDC000649**(phospho). User-shared via BMJ DOI 10.1136/gutjnl-2025-337247. (proteogenomic · Gut 2026;75:886–904)
- [Zhao 2026 - CRLM Proteogenomics + SHMT1·NDRG1 Mechanism + C1/C2 Subtype (FUSCC Chinese cohort)](../sources/zhao-2026-proteogenomic-characterization-reveals-metabolic-vulnerabilities.md) - Fudan University Shanghai Cancer Center treatment-naïve **34명 CRLM = 102 sample(matched T+N+LM 트리오)** + independent IHC validation cohort n=87 (IRB 050432-4-1805C + 050432-4-1911D, 2012-07~2019-06). WES 19,493 nonsyn mut + 23,109 SCNA (APC/TP53/KRAS T vs LM 무차이; cis-regulatory SCNA effect는 mRNA가 가장 강함) + TMT proteome **8,568 identified / 8,093 quantified** + Ti⁴⁺-IMAC phosphoproteome **25,775 identified / 19,803 quantified (class I 16,300)**. LM signature: proteome — complement/coagulation + PPAR + carbon/fructose-mannose/cholesterol/amino acid metabolism; phospho — actin filament organization + small GTPase + lamellipodium organization. LM KSEA RAF1+PAK2+ROCK1 (VIM phosphorylation + CFL1 Ser3 EMT). 288,337 AS event 14/26 prognostic (FN1/KHK/SERPINA1). ARG1 protein-only LM ↑ → poor OS T+LM. **Clinical Risk Score 한계 명시**: 5-yr OS log-rank p=0.23(예측 불충분). LM-enriched 245 protein set vs Li et al. mCRC dataset GSEA NES=-3.50/FDR<0.001 (tissue-corrected -3.11) + Li T(n=146) high LM-set → OS log-rank p=0.037 외부 transferability. **SHMT1-formate-AMPK 축**: SHMT1+MTHFD1+SHMT2 LM ↑; SHMT1 high → OS/PFS poor n=87 IHC. KAP organoid (Villin^CreERT2; Kras^LSL-G12D; Apc^min/+; Trp53^flox/flox; 2 mo TAM) Shmt1 KD ↓pH3+ ↑CC3+ ↓growth; SHMT1 OE 반대. Isogenic luciferase organoid intrasplenic C57BL/6 WT → ↓liver metastasis. **Only formate rescue** Shmt1 KD; in vivo formate level Shmt1 KD ↓/OE ↑. Formate transcriptome KEGG: HIF-1+AMPK+PPP inhibition + Wnt+Hippo activation. Western Shmt1 KD ↑p-AMPK, formate ↓, AICAR ↑↑. In vivo 125 mM formate drinking water ↑tumor burden, AICAR 50 mg/kg ip mitigation. CPS1 동일 검증. **NDRG1 S330p ubiquitin-degradation 축**: 보존된 5 up + 3 down phosphosite(functional score + log-rank p<0.05) — SLC16A1 S498 / **NDRG1 S330** / PDLIM2 S129; NDRG1 S330p ↔ actin cytoskeleton reorganization ρ=0.43 p=0.013; NDRG1 S330A KAP intrasplenic ↓liver metastasis burden. NDRG1 WT > S330A ubiquitination; cycloheximide chase S330A 반감기 ↑; MG132 accumulation → ubiquitin-proteasome 의존 확정. PIM family(PIM1/2/3) NDRG1 S330 phosphorylation 후보 1위(Johnson 2023); PIM1 mRNA LM ↑. **TP-3654 3 μM(pan-PIM)**: ↓NDRG1 S330p ↓migration/invasion ↑p-AMPK (PIM이 AMPK 음 조절 + NDRG1 degradation 동시 매개하는 dual axis). KSEA 기본 DB로는 detect 실패 → Sun et al. PhosphoSitePlus v6.7.5 확장 DB로 PIM1 LM activity ↑ Wilcoxon p<0.001. **C1 metabolism vs C2 RNA function 아형**: LM proteome unsupervised clustering이 phospho/transcriptome 기반보다 prognostic stratification 우수, **OS log-rank p<0.05 (C1 poor)**. 고빈도 mutated gene C1/C2 무차이; 17 저빈도 mutated gene Fisher p<0.05. 226,107 AS in LM; 148 C1/C2 차이 / 98 prognostic (KHK/RPP21/U2AF1L4 top). 17 splicing factor C2 ↑ (DHX9/DIS3/HNRNPA0/NCBP1/PRPF8/SNRPD1 good prognosis; NCBP1/PRPF8/SNRPD1 CRC+HCC dependency; DIS3/HNRNPA0/PRPF8 ↔ GRB7 AS negative). C1 KSEA hyperactive: RPS6KA1+RPS6KB2+PAK1/2/4+CHEK1+ROCK1+MAPK1 + EIF4B S422 substrate axis. **Subtype-specific biomarker validation n=87 IHC**: FTCD + GPD1 (C1 LM-specific, one-carbon metabolism) OS/PFS log-rank p<0.05; SOD2 (DepMap CRC/HCC dependency, protein-only) discovery p=0.098 → validation p=0.0331; **EIF4B Ser422 phospho** OS p=0.0265, PFS p=0.0099. CPTAC GBM/LUAD/CCRCC/PDAC 외부 SOD2/GPD1/EIF4B S422 reproducible. 한계 본문 명시: n=34 discovery power 제한, formate-AMPK 정확 mechanism 미정의, KSEA indirect axis detection 실패, single-cohort Chinese single-institution. Data iProx **IPX0007391001** + GSA **PRJCA020890**; original code 없음; competing interest 없음. PMC12822478. User-shared via Wiley DOI 10.1002/advs.202511744. (proteogenomic · Advanced Science 2026)

## 2. 인산화단백체와 Kinase Network

- [Jiang 2025 - Dark Cancer Phosphoproteome](../analyses/cancer-multiomics-literature/jiang-2025-dark-cancer-phosphoproteome.md) - annotation이 부족한 phosphosite를 co-regulation network로 해석해 kinase-substrate 후보 공간을 넓힌다.
- [Shi 2025 - Functional Network of Human Cancer](../analyses/cancer-multiomics-literature/shi-2025-functional-network-human-cancer.md) - protein-level network가 transcriptome보다 기능 관계 해석에 강한 축이 될 수 있음을 보여준다.
- [Muller-Dott 2025 - Benchmarking Kinase Activity Inference](../analyses/cancer-multiomics-literature/muller-dott-2025-phosphoproteomic-kinase-activity-inference.md) - kinase activity inference에서 알고리즘보다 substrate library 선택이 성능을 좌우할 수 있음을 보여주는 벤치마크.
- [Asuzu 2025 - Phosphoproteomic Dysregulation Drives Tumor Proliferation](../analyses/cancer-multiomics-literature/asuzu-2025-phosphoproteomic-dysregulation-drives-tumor-proliferation.md) - genomic driver가 약한 상황에서도 phosphatase 축(PP2A) 기반 인산화 dysregulation이 종양 phenotype을 구동할 수 있음을 multi-omics로 제시한다.
- [Zhao 2025 - Phosphoproteomic + Acetylomic Response to Kinase Inhibitors (CRC)](../analyses/cancer-multiomics-literature/zhao-2025-phosphoproteomic-acetylomic-characterization-colorectal-cancer.md) - inhibitor perturbation에서 off-target signaling과 PTM crosstalk까지 포함해 pathway/kinase 수준 요약 전략을 제공한다.
- [Khan 2026 - Public Phosphoproteomics Network Meta-analysis (CAMK2D–TPD52)](../analyses/cancer-multiomics-literature/khan-2026-integrative-phosphoproteomic-network-analysis-identifies.md) - 공개 phosphoproteomics를 통합해 phosphosite/network에서 upstream kinase 가설을 도출하는 예시(우선순위는 낮을 수 있음).

## 3. 면역회피와 Neoantigen

- [Petralia 2024 - Pan-Cancer Proteogenomics of Tumor Immunity](../analyses/cancer-multiomics-literature/petralia-2024-pan-cancer-tumor-immunity.md) - CPTAC pan-cancer proteogenomics로 immune subtype, pathway activity, kinase activity를 함께 해석한다.
- [Xiang 2025 - Non-Canonical Neoantigen Proteogenomics in CRC (Chinese cohort + MC38 in vivo)](../sources/xiang-2026-predominant-mutated-non-canonical-tumor-specific-antigens.md) - Chinese 10명 paired CRC tumor + 인접 정상에서 WGS + RNA-seq + MHC class I IP-MS 통합 + 6-frame translation(10 candidate start codon) + two-stage DB search(Comet/MSFragger/MaxQuant) + de novo(Casanovo/PepNet/pNovo3/SMSNet)로 **96 mutated MHC class I neo-epitope**(평균 9.6/환자, traditional ~1/환자) 식별, **80.21%가 non-coding origin**(intergenic 26 / intronic 28 / non-coding intronic 19; 비-coding ORF 평균 127 bp). DNA 78 / RNA 19 / Neo-074 양쪽. **TMB>25 hypermutation 그룹 87 epitope(86.2% non-canonical) vs TMB<25 9 epitope(22.2% non-canonical)**. Ribo-seq(smProt + nuORFdb) 35/77 non-canonical translation 지지. Cell-line 외부 검증 HCT116 79.61% recall+4.88× / HCC1143 96.44%+4.68×. MC38 mouse 20 neo-epitope(11 non-canonical) PRM 100% 검증; **ELISpot intronic 3/6 + intergenic 3/5 IFN-γ 양성; 7-peptide Vax 종양 성장 유의 억제, α-CD8β depletion으로 완전 abrogation(p<0.0001)**. scRNA-seq 67,471 cell에서 Vax 그룹 cytotoxic CD8⁺ TIL 0.40%(PBS 0.08%) + CD8/Treg ratio 3.93(PBS 2.39) + Treg %CD4⁺ 22.61%(PBS 36.14%). 한계 본문 명시: n=10 단일 기관 Chinese, 비-coding 80.21% 비율은 cancer/cohort 의존, Ribo-seq 지지 35/77만, PRM 92.59% empirical vs 이론 FDR 1% calibration 격차, BGI 저자 stock 이해관계. Data CNSA CNP0004656 + CNP0005402, GSA-Human HRA005229, Code Zenodo 10.5281/zenodo.17527817. (proteogenomic · Cell Genomics 2025)
- [Wen 2020 - NeoFlow Proteogenomic Neoantigen Prioritization](../analyses/cancer-multiomics-literature/wen-2020-neoflow-neoantigen-prioritization.md) - WGS/proteomics 기반 neoantigen 후보 우선순위화와 retention-time 기반 QC logic을 제공한다.
- [Huber 2025 - NeoDisc Proteogenomic Neoantigen Pipeline](../analyses/cancer-multiomics-literature/huber-2025-neodisc-neoantigen-pipeline.md) - immunopeptidomics와 multi-omics를 결합한 임상형 neoantigen discovery pipeline reference로 쓸 수 있다.
- [Shapiro 2025 - NeoDiscMS Real-time NGS-guided Immunopeptidomics](../analyses/cancer-multiomics-literature/shapiro-2025-sensitive-neoantigen-discovery-real-time-mutanome-guided.md) - inclusion list + real-time search로 표적 스캔을 트리거해 임상 TAT 제약에서 민감도를 높이는 acquisition 설계.
- [Scheid 2025 - MHCquant2 (nf-core) Immunopeptidomics Pipeline](../analyses/cancer-multiomics-literature/scheid-2025-mhcquant2-refines-immunopeptidomics-tumor-antigen.md) - immunopeptidomics 처리 표준화/재현성 및 benign reference 기반 antigen refinement 레퍼런스.
- [Saxena 2025 - Atezolizumab + Personalized Neoantigen Vaccination (Urothelial Cancer)](../analyses/cancer-multiomics-literature/atezolizumab-2025-personalized-neoantigen-vaccination-urothelial-cancer.md) - neoantigen vaccine(PGV001)+PD-L1 병용 1상에서 제조/기간/투여 feasibility와 면역반응 readout을 제시한다.
- [Braun 2025 - Peptide PCV in Resected ccRCC (± ipilimumab)](../analyses/cancer-multiomics-literature/braun-2025-neoantigen-vaccine-generates-antitumour-immunity.md) - low TMB ccRCC에서도 다중 epitope peptide 백신이 강한 면역반응(자가 종양 인지 7/9)을 보이고, 소규모지만 재발 없는 경과를 보고한 adjuvant 임상 근거.
- [Gainor 2024 - KEYNOTE-603 mRNA-4157(V940) Immunogenicity](../analyses/cancer-multiomics-literature/gainor-2024-t-cell-responses-individualized-neoantigen-therapy.md) - 개인맞춤 neoantigen mRNA가 예측 후보 중 어느 정도 실제 T cell 반응으로 이어지는지(ELISpot/ICS/TCR readout)를 보여주는 phase 1 중간기전 근거.
- [Weber 2024 - KEYNOTE-942 (V940 mRNA neoantigen + pembrolizumab; melanoma)](../analyses/cancer-multiomics-literature/weber-2024-individualised-neoantigen-therapy-mrna-4157-v940.md) - 개인맞춤 neoantigen mRNA 병용이 재발 위험을 낮추는 신호를 보여주는 임상 근거.
- [Keskin 2019 - Personalized Neoantigen Vaccine in Glioblastoma (Steroid Effect + TCR Tracking)](../analyses/cancer-multiomics-literature/keskin-2019-neoantigen-vaccine-generates-intratumoral-t.md) - GBM 개인맞춤 neoantigen 백신 1상에서 dexamethasone이 면역반응을 크게 억제하며, scTCR로 말초→종양 이동을 추적한다.
- [Abelin 2023 - MONTE Serial Multi-Omics (Immunopeptidome + PTM)](../analyses/cancer-multiomics-literature/abelin-2023-workflow-enabling-deepscale-immunopeptidome-proteome.md) - 제한된 샘플에서 immunopeptidome과 multi-PTM을 같은 샘플로 직렬 수집하는 실험 설계 레퍼런스.
- [Chong 2022 - Identification of Tumor Antigens with Immunopeptidomics](../analyses/cancer-multiomics-literature/chong-2022-identification-tumor-antigens-immunopeptidomics.md) - canonical/noncanonical 항원 발굴과 false positive 관리(FDR/검증)의 핵심 텐션을 정리한 리뷰.
- [Chen 2026 - Enrichment of Phosphorylated/Glycosylated MHC Peptides (Methods)](../analyses/cancer-multiomics-literature/chen-2026-enrichment-phosphorylated-glycosylated-mhc-peptides.md) - PTM-MHC peptide(phospho/glyco) 동정을 위한 순차 농축 워크플로(예측이 아닌 측정)의 방법 레퍼런스.

## 4. 치료반응 예측 모델과 데이터 인프라

- [Han 2024 - HLA-Based Neoantigen Presentation Score Predicts Pan-Cancer ICI Response](../analyses/cancer-multiomics-literature/han-2024-hla-based-neoantigen-presentation-pan-cancer-response.md) - neoantigen “개수”가 아니라 presentation-aware score로 ICI 반응/생존과의 연관을 제시한다.
- [Anurag 2022 - TNBC Neoadjuvant Chemo Response (WES + Phosphoproteome)](../analyses/cancer-multiomics-literature/anurag-2022-proteogenomic-markers-chemotherapy-resistance-response.md) - pCR/non-pCR 임상 라벨을 WES+TMT phosphoproteomics로 분해하고 19q13 결실 등 내성 신호를 제시한다.
- [Hsu 2025 - Osimertinib DTP Phosphoproteomics (DIA-MS + CDK1/YAP/mTOR)](../sources/hsu-2025-phosphoproteomics-osimertinib-tolerant-persister-cells-reveals.md) - EGFR-mutant NSCLC DTP/recovery 모델에서 global proteome+phosphoproteome time course를 이용해 CDK1-SAMHD1/PML, mTOR/YAP/BAD, PI3K/MAPK/PKA/PKC recovery signaling을 drug-tolerant persister 취약성으로 제시한다.
- [Haas 2024 - Prostate Cancer Radioresistance (WES + Proteome)](../analyses/cancer-multiomics-literature/haas-2024-proteogenomics-prostate-cancer-radioresistance.md) - 방사선 fractionation(CF/HF)에 따라 다른 내성 프로그램과 POLQ radiosensitizer 후보를 제시한다.
- [Zhang 2023 - ccRCC Sunitinib Response Proteogenomics (mTOR / 7q / Classifier)](../analyses/cancer-multiomics-literature/zhang-2023-proteogenomics-clear-cell-renal-response-tyrosine-kinase-inhibitor.md) - sunitinib responder/non-responder(RECIST) 라벨에서 mTOR/7q 등 proteome/phosphoproteome feature를 포함한 반응 예측 예시.
- 현재 seed 논문들은 주로 mechanistic feature와 data layer를 제공한다. 이후 Slack에서 들어오는 논문은 response model, SHAP/feature interpretation, basket trial, cloud-scale WGS/proteomics processing 축으로 추가한다.

## 5. 면역치료 내성 우회(조합 전략)

- [Skoulidis 2024 - CTLA4 blockade abrogates KEAP1/STK11-related resistance](../analyses/cancer-multiomics-literature/skoulidis-2024-ctla4-abrogates-keap1-stk11-resistance.md) - KEAP1/STK11 변이 NSCLC에서 dual ICB(CTLA-4 병용)가 내성 병목을 우회할 수 있다는 임상·기전 프레임을 제공.
- [Memon 2024 - Acquired Resistance to PD-(L)1 Blockade in NSCLC](../analyses/cancer-multiomics-literature/memon-2024-clinical-molecular-features-acquired-resistance.md) - NSCLC 획득내성(AR)에서 IFNγ signature 증가/지속과 항원제시 경로 이상(B2M 등)이 결합되는 “persistently inflamed but dysfunctional” 프레임을 cohort-scale로 제시.
- [Yaeger 2023 - Acquired Resistance to KRASG12C–EGFR Inhibition in CRC (ctDNA + ERK/mTOR Switch)](../analyses/cancer-multiomics-literature/yaeger-2023-molecular-characterization-acquired-resistance-krasg12c-egfr.md) - 표적치료 병용에서 ctDNA 시계열로 내성 변이를 추적하고, KRASG12C amplification·약물중단 후 senescence/mTOR 전환 같은 상태 전이를 내성 프레임으로 제시한다.

## 6. 2026-05 Expansion: AI/Spatial/ecDNA/CAR-T 보강 (45편)

Notion 'Cancer Multiomics' 페이지의 27개 시드 + OpenAlex 인용 그래프로 발굴한 score≥6 관련논문 18편을 통합 ingest. PDF 상태: 36편 다운로드 완료, 9편 manual_pending (Cell Press anti-bot, bioRxiv 2026 DOI 미등록 등). Discovery 메타데이터는 frontmatter `discovery_method`/`related_to_seeds`에 기록.

### 6.1 AI / Foundation models / Deep learning

- [TWAS signature-matching for drug prioritisation: a best-practice benchmark](../sources/chauquet-2026-twas-signature-matching-drug-prioritisation-benchmark.md) (Notion seed)
- [Towards a general-purpose foundation model for computational pathology](../sources/chen-2024-towards-general-purpose-foundation-model.md) (OpenAlex)
- [CenSegNet: a generalist high-throughput framework for centrosome phenotyping in heterogeneous cancer tissues](../sources/cheng-2025-censegnet-centrosome-phenotyping-cancer-tissues.md) (Notion seed)
- [Linking spatial biology and clinical histology via Haiku](../sources/cui-2026-haiku-tri-modal-spatial-biology-histology.md) (Notion seed)
- [Expanding the human proteome with peptideins from non-canonical ORFs](../sources/deutsch-2026-expanding-human-proteome-peptideins-noncanonical-orfs.md) (Notion seed)
- [Discovering proteo-transcriptomic networks via biologically informed heterogeneous graph learning (bioGraph)](../sources/duan-2026-discovering-proteo-transcriptomic-networks-heterogeneous-graph-learning.md) - SIAT CAS Shenzhen + Beijing Tiantan + FAHZZU Zhengzhou + Xiamen Univ의 3-layer heterogeneous GCN(mRNA/protein/phosphoprotein + KEGG intra-RNA + STRING≥700 intra-protein/phospho + 동일 유전자 RP/PP inter-omic). 2-layer HeteroRGCN(DGL) + Cox PL loss + edge-aware weighting. CPTAC 4 cohort(COAD 79/GBM 74/pLGG 73/PDAC 92) + 외부 FAHZZU glioma n=119(NCT04216537). Mean CV C-index COAD **0.91±0.08** / GBM 0.71±0.04 / pLGG 0.73±0.03 / PDAC 0.74±0.02; MOGONET/IGNN/MMGL/SALMON/MRGCN 전 cohort 우위. Ablation: prior 제거 PDAC 0.74→0.47, edge-aware 제거 GBM 0.71→0.58. **pLGG inter-omic 비대칭 정반대**: RP>PP 19.51%(GBM/COAD/PDAC 91-95%). 4-cancer 공통 RP-PP discordance core set **MAP4/SORBS1/SPTAN1/SRRM1/TMPO**. MGSVA = KS-like running-sum on edge weights(GSVA multi-omic 확장, pathway membership을 edge 단위로 정의). **MAP4 validation**: DEG 비표시 → discovery prognosis 비유의 → FAHZZU n=119 mRNA P<0.015 protein P<0.01; T98G/U251 sh-MAP4(TRCN0000117163/166) wound/transwell/CCK-8/colony ↓ + Annexin V apoptosis ↑. EMOGI 비교: bioGraph 1/5 PPI network cancer gene AUC 우위; EMOGI도 MAP4/SORBS1/SPTAN1 3/4 datasets cancer-related. Data cBioPortal input + GSA HRA006184(RNA-seq 외부) + iProX PXD062023(MS 외부); code codeocean.com/capsule/2357965 + biograph.hapyun.com. License CC BY-NC 4.0. PMC13129546.
- [Do larger models really win? A scaling benchmark in AI-driven drug discovery](../sources/guo-2026-larger-models-scaling-benchmark-drug-discovery.md) (Notion seed)
- [Simulating 500 million years of evolution with a language model (ESM3)](../sources/hayes-2025-simulating-500-million-years-evolution.md) (OpenAlex)
- [A deep-learning framework to predict cancer treatment response from histopathology images through imputed transcriptomics](../sources/hoang-2024-deep-learning-framework-predict-cancer.md) (OpenAlex)
- [Prediction of DNA methylation-based tumor types from histopathology in central nervous system tumors with deep learning](../sources/hoang-2024-prediction-dna-methylation-based-tumor.md) (OpenAlex)
- [DrugCLIP: contrastive protein-ligand model for genome-scale virtual screening (GenomeScreenDB)](../sources/jia-2026-drugclip-contrastive-protein-ligand-genome-scale.md) (Notion seed)
- [MolGene-E: inverse molecular design from single-cell transcriptomic reversal for anticancer perturbation](../sources/ohlan-2025-molgene-e-inverse-molecular-design-transcriptomic-reversal.md) (Notion seed)
- [Multimodal data fusion for cancer biomarker discovery with deep learning](../sources/steyaert-2023-multimodal-data-fusion-cancer-biomarker.md) (OpenAlex)
- [Reimagining human-centric drug development with new approach methodologies (NAMs)](../sources/wu-2026-reimagining-human-centric-drug-development-nams.md) (Notion seed)
- [Deep-learning-based de novo discovery and design of therapeutics that reverse disease-associated transcriptional phenotypes](../sources/xing-2026-deep-learning-de-novo-transcriptional-phenotype-reversal.md) 🟠 (Notion seed)
- [ProteinAligner: Tri-modal contrastive protein language model integrating sequence, structure, and text](../sources/zhang-2026-proteinaligner-tri-modal-contrastive-protein-language.md) 🟠 (Notion seed)
- [Systematically decoding pathological morphologies and molecular profiles with unified multimodal embedding](../sources/zhang-2026-systematically-decoding-pathological-morphologies-multimodal-embedding.md) (Notion seed)

### 6.2 Spatial multiomics

- [Resolving sensitivity, specificity and signal contamination in Xenium spatial transcriptomics](../sources/bilous-2026-xenium-sensitivity-specificity-signal-contamination.md) (Notion seed)
- [Molecular cartography uncovers evolutionary and microenvironmental dynamics in sporadic colorectal tumors](../sources/heiser-2023-molecular-cartography-uncovers-evolutionary-microenvironmental.md) 🟠 (OpenAlex)
- [High resolution mapping of the tumor microenvironment using integrated single-cell, spatial and in situ analysis](../sources/janesick-2023-high-resolution-mapping-tumor-microenvironment.md) (OpenAlex)
- [Spatially informed clustering, integration, and deconvolution of spatial transcriptomics with GraphST](../sources/long-2023-spatially-informed-clustering-integration-deconvolution.md) (OpenAlex)
- [Single-cell spatial multiomics identifies POSTN+ CAFs driving chemoradiotherapy resistance in rectal cancer](../sources/sakai-2026-postn-cafs-chemoradiotherapy-resistance-rectal-cancer.md) 🟠 (Notion seed)
- [Pan-cancer virtual spatial transcriptomics from routine histology with Phoenix](../sources/tran-2026-phoenix-pan-cancer-virtual-spatial-transcriptomics.md) (Notion seed)
- [Non-invasive profiling of the tumour microenvironment with spatial ecotypes](../sources/zhang-2026-non-invasive-tumour-microenvironment-spatial-ecotypes.md) (Notion seed)

### 6.3 ecDNA biology

- [Parallel sequencing of extrachromosomal circular DNAs and transcriptomes in single cancer cells](../sources/gonzalez-2023-parallel-sequencing-extrachromosomal-circular-dnas.md) (OpenAlex)
- [Coordinated inheritance of extrachromosomal DNAs in cancer cells](../sources/hung-2024-coordinated-inheritance-extrachromosomal-dnas-cancer.md) (OpenAlex)
- [Extrachromosomal DNA Amplification Contributes to Small Cell Lung Cancer Heterogeneity and Is Associated with Worse Outcomes](../sources/pongor-2023-extrachromosomal-dna-amplification-contributes-small.md) (OpenAlex)
- [Extrachromosomal DNA gives cancer a separate evolutionary pathway](../sources/wang-2025-extrachromosomal-dna-cancer-evolutionary-pathway.md) (Notion seed)

### 6.4 T-cell biology / CAR-T / TCR

- [Lymphoid chemokine signalling limits CD8+ T cell priming time to preserve effector function](../sources/altenburger-2026-lymphoid-chemokine-cd8-priming-effector.md) (Notion seed)
- [A generative reference grammar of healthy TCR repertoires for cancer immune remodeling analysis](../sources/balan-2026-generative-reference-grammar-tcr-repertoires-cancer.md) 🟠 (Notion seed)
- [T cell state transcription factor cooperation engineering: KLF2 x RUNX2 memory-like CAR-T design](../sources/savage-2026-klf2-runx2-memory-like-car-t.md) (Notion seed)

### 6.5 Single-cell methods / atlases

- [SCENIC+: single-cell multiomic inference of enhancers and gene regulatory networks](../sources/gonzalezblas-2023-scenic-single-cell-multiomic-inference.md) (OpenAlex)
- [Best practices for single-cell analysis across modalities](../sources/heumos-2023-best-practices-single-cell-analysis.md) (OpenAlex)
- [A transcription factor atlas of directed differentiation](../sources/joung-2023-transcription-factor-atlas-directed-differentiation.md) 🟠 (OpenAlex)
- [10x Genomics Gene Expression Flex enables single-cell transcriptomics on fixed and frozen xenograft samples](../sources/llora-batlle-2024-10x-flex-fixed-xenograft-single-cell.md) (Notion seed)
- [Applications of single-cell RNA sequencing in drug discovery and development](../sources/sande-2023-applications-single-cell-rna-sequencing.md) (OpenAlex)

### 6.6 Cancer biology / TME (PDAC, CRC, sarcoma)

- [Extra-lineage tissue programs define transcriptional states in human pancreatic cancer](../sources/ge-2026-extra-lineage-tissue-programs-pancreatic-cancer-transcriptional.md) 🟠 (Notion seed)
- [Sarcoma microenvironment cell states and ecosystems are associated with prognosis and predict response to immunotherapy](../sources/subramanian-2024-sarcoma-microenvironment-cell-states-ecosystems.md) (OpenAlex)
- [Schwann cells regulate tumor cells and cancer-associated fibroblasts in the pancreatic ductal adenocarcinoma microenvironment](../sources/xue-2023-schwann-cells-regulate-tumor-cells.md) (OpenAlex)

### 6.7 Drug discovery / Pathway / Resource

- [CADDIE: web-based network-medicine platform for cancer driver-based drug repurposing](../sources/hartung-2022-caddie-cancer-driver-drug-repurposing-platform.md) (Notion seed)
- [nf-core Nextflow disease module discovery and benchmarking pipeline for network medicine reproducibility](../sources/kersting-2025-nf-core-disease-module-network-medicine.md) (Notion seed)
- [Predicting bladder cancer molecular subtypes and BCG response from histology using deep learning](../sources/khoraminia-2026-predicting-bladder-molecular-subtypes-bcg-response.md) (Notion seed)
- [The Reactome Pathway Knowledgebase 2024](../sources/orlicmilacic-2023-reactome-pathway-knowledgebase-2024.md) (OpenAlex)
- [Multimodal deep learning on LINCS L1000 reveals brain-penetrant Class I HDAC inhibitors as pan-cancer candidates](../sources/tong-2026-multimodal-lincs-pan-cancer-hdac-inhibitor.md) (Notion seed)
- [Cross-assay RNA modeling reveals robust cancer biomarkers across heterogeneous platforms](../sources/townsend-2026-cross-assay-rna-modeling-cancer-biomarker-discovery.md) 🟠 (Notion seed)
- [Open Targets Gentropy: pleiotropy mapping across 100,526 GWAS for therapeutic target prioritisation](../sources/tsepilov-2026-open-targets-gentropy-pleiotropy-gwas-prioritisation.md) 🟠 (Notion seed)

**상태 표시**: 🟠 manual_pending (anti-bot/미공개 DOI), 표시 없음 = PDF 다운로드 완료.

## 7. Methodology / Resource Atlases (Deep Proteome References)

암종-비특이 deep-proteome / proteoform / variant detection reference 자료. 한미암 코호트 결과를 비교·해석할 때 baseline 수치 또는 도구 stack reference로 인용한다.

- [Sinitcyn 2023 - Deep Proteome Reference + SAP/AS Detection Framework (ENCODE 6세포주)](../sources/sinitcyn-2023-global-detection-human-variants-isoforms-deep-proteome.md) - ENCODE 6세포주(H1-hESC/HeLa S3/HepG2/GM12878/K562/HUVEC) × 6 protease(trypsin/LysC/LysN/AspN/GluC/chymotrypsin) × HCD/CAD/ETD 통합 reference. 2,491 raw files / ~164M MS/MS / 1% FDR에서 17,717 proteins / 1,119,510 unique peptides / 12,151,708 PSMs, median sequence coverage 79.2%(trypsin 단독 56.5%). SAP 검출 5,060개(transcriptome SNP 73% 단백 매핑), 미검출 SAP에서 SIFT/PolyPhen-2 deleterious 변이 enriched(P=2e-8, 1.1e-12)로 protein instability 가설. AS event 13,450개 중 34.3% / 양방향 6,145개 중 18.6% 단백 검출, frame-preserving 64%, XGBoost AUC 0.83(top features: transcript abundance, PSI, frame status; PSI ~33% 최적). De novo SOAPdenovo-Trans 35,480 scaffold 중 47%(16,496)가 9,695 protein group에 매칭. ProteomeXchange PXD024364 + deep-sequencing.app + github.com/coongroup/DeepProteomeSequencing-Software. (resource · Nature Biotechnology 2023)

### 8. 2026-05 Topic Sweep Additions

2026-05-25 자동 topic sweep으로 추가된 14편의 spatial / single-cell / multi-omics 관련 신규 페이지. 각 stub은 abstract + full_text 추출 기반 1차 요약과 한미암 연결 각도를 포함한다. 향후 manual deep-dive 우선순위는 (B) 인산화단백체/kinase, (C) WGS-단백체 통합, (D) 치료반응 예측 축에 직접 대응되는 항목부터 선정한다.

- [Wang 2026 – Spatial multi-omics in combined small-cell lung cancer](../sources/wang-2026-spatial-multi-omics-unveils-monoclonal-origin.md) — cSCLC 19명의 multi-region WES + ST + snRNA-seq로 monoclonal origin, COL11A1+ CAF 경계, NSCLC-to-SCLC transdifferentiation, 4-gene cSCLC Detector를 정의합니다.
- [Yang 2026 – IGHG1+ MEC-myCAF crosstalk drives NSCLC brain metastasis](../sources/yang-2026-ighg-malignant-epithelial-cell-mycaf-crosstalk.md) — NSCLC 53명 snRNA-seq + GeoMx + CosMx 통합으로 IGHG1+ MEC와 myCAF의 MIF-CD74 axis가 invasive front에서 뇌전이를 매개함을 보입니다 (HR=5.495, AUC=0.776).
- [Xu 2026 – UCASpatial: entropy-weighted ST deconvolution](../sources/xu-2026-ultra-precision-deconvolution-spatial-transcriptomics-decodes.md) — Shannon entropy weighting + WNNLS로 6개 기존 method 대비 RMSE 10~36% 개선, CRC chr20q-gain → HERV-H 감소 → T cell exclusion mechanism을 제시합니다.
- [Zhang 2026 – Cross-species CRC epithelial-macrophage atlas](../sources/zhang-2026-cross-species-single-cell-spatial-transcriptomic.md) — 인간 CRC와 Apc-min 생쥐 N-A-C 단계 scRNA + ST 통합으로 EFNA1-EPHA4 axis가 TAM immunosuppression과 종양 stemness를 매개함을 도출합니다.
- [Hallinan 2026 – Xenium off-target probe binding QC](../sources/hallinan-2026-evidence-off-target-probe-binding-affecting.md) — 10x Xenium human breast 313-gene panel 중 14개 이상이 off-target probe binding 영향을 받음을 OPT 도구로 식별해 spatial transcriptomics 해석 신뢰성 QC를 제공합니다.
- [Barone 2026 – AICL-KLRF1 axis in CD4-CD8 communication](../sources/barone-2026-aicl-klrf-axis-supports-cell-communication.md) — late-differentiated CD8+ T cell의 cytokine competence를 AICL+ CD4+ T cell이 KLRF1을 통해 강화함을 lung adenocarcinoma spatial proteomics + scRNA/ATAC로 입증합니다.
- [Agirre-Lizaso 2026 – MARCO drives cholangiocarcinoma immunosuppression](../sources/agirrelizaso-2026-marco-promotes-cholangiocarcinogenesis-inducing-immunosuppression-its.md) — iCCA에서 MARCO+ TAM이 TH2-skewed immune response·collagen deposition·worse survival과 연관되며 Marco-/- 및 anti-MARCO 항체가 종양 성장을 억제함을 보입니다.
- [Quail 2026 – Cancer ecosystems multi-scale framework (Cell review)](../sources/quail-2026-cancer-ecosystems-dynamic-interplay-across-scales.md) — TME를 분자·세포·조직·organismal·temporal scale의 cancer ecosystem으로 재정의하고 spatial multi-omics·AI pathology·immune-vascular normalization을 정밀종양학의 핵심 축으로 제시합니다.
- [Qi 2026 – PDAC single-cell + spatial review](../sources/qi-2026-unraveling-pancreatic-ductal-adenocarcinoma-single-cell.md) — PDAC scRNA-seq 연구를 cellular heterogeneity·tumorigenesis·immune remodeling·drug resistance·biomarker 다섯 축으로 정리하고 spatial multi-omics 통합 framework를 제안합니다.
- [Wu 2026 – iCLAP: integrable low-abundance protein high-plex imaging](../sources/wu-2026-iclap-innovative-method-integrable-detection-low.md) — TSA 기반 iterative amplification + fluorophore inactivation으로 FFPE에서 40개 이상 marker를 통합 검출해 IMC·CyCIF·CODEX와 결합 가능함을 췌장 senescence 사례로 시연합니다.
- [Yeo 2026 – EBV-driven cHL TME reorganization (spatial multi-omics)](../sources/yeo-2026-epstein-barr-virus-orchestrates-spatial-reorganization.md) — EBV+ cHL에서 HRS proximity·LMP1 발현 수준에 distance-dependent로 CD8 T cell terminal exhaustion이 강화됨을 spatial proteomics + transcriptomics로 정량합니다.
- [Zou 2026 – Spatial decoding of NSCLC ICI efficacy (JCI commentary)](../sources/zou-2026-understanding-immune-checkpoint-inhibitor-efficacy-through.md) — Isomoto 등의 103명 NSCLC multiplex IHC 연구에서 CD73 upregulation을 포함한 3-variable spatial composite가 PD-L1보다 ICI 효능을 substantial하게 더 잘 예측함을 정리합니다.
- [Sussman 2026 – Longitudinal pHGG multiomic atlas (snRNA/snATAC/WGS/CODEX)](../sources/sussman-2026-longitudinal-single-cell-spatial-multiomic-atlas.md) — pediatric HGG 16명의 1차-재발-autopsy longitudinal snRNA + snATAC + WGS + CODEX atlas로 post-therapy interferon/oligodendrocyte/myeloid shift와 in vitro target 검증을 결합합니다.
- [Wang 2026 – CD19/20 CAR-T outcomes + spatial profiles in R/R B-NHL](../sources/wang-2026-clinical-outcomes-spatial-transcriptomic-profiles-car.md) — bispecific CD19/20 CAR-T phase I/II 32명 (ORR 74%, CR 58%, mOS 22.1mo) + spatial single-cell으로 B-cell-dominant vs fibroblast/myeloid-enriched 두 architecture와 각각의 response 결정인자를 정의합니다.

## Open Questions

- 질문 확장 맵: [Four-Topic Question Expansion Map](../analyses/topic-question-expansion-map.md) (Topic 4)
- 표준 추출 체크리스트(초안): 치료 맥락(암종/치료제/라인/반응 라벨), 데이터 레이어(WGS/Proteome/Phospho/Neoantigen), 데이터 공개 수준(raw/processed/supplement/code), 핵심 방법(TMT/DIA/enrichment/instrument), 과제 연결(예측/내성/파이프라인) 1~2줄

- Cancer Multiomics 과제의 실제 환자군에서 치료제 class, primary/acquired resistance label, biopsy timing을 논문 요약 페이지의 표준 metadata로 넣을 것인가?
- neoantigen 논문은 WGS-only prediction 중심 논문과 immunopeptidomics/proteogenomics validation 중심 논문을 분리할 것인가?
- phosphoproteomics 논문은 identification scale보다 normalization, missingness, kinase inference, protein-abundance correction 여부를 우선 기록할 것인가?
- Slack 메시지는 짧은 공유용과 deep-dive용 두 버전으로 관리할 것인가?

## Connections

- [Multiomics Proteomics PTM Identification](./multiomics-proteomics-ptm-identification.md)
- [PTM Correction and Kinase Signaling in Cancer Proteomics](./ptm-correction-and-kinase-signaling-in-cancer-proteomics.md)
- [Immunotherapy Resistance and Immune Evasion](./immunotherapy-resistance-and-immune-evasion.md)
- [B-Cell Neoantigen Research Map](./b-cell-neoantigen-human-cancer.md)

## Sources

- User-provided Cancer Multiomics HWP research plan, read locally.
- Local extracted text: `/private/tmp/hwp_extract/cancer_multiomics_plan_extracted.txt`
- 하위 페이지에 연결된 local wiki source pages and PDFs.

## Linked Sources

- [10x Genomics Gene Expression Flex enables single-cell transcriptomics on fixed and frozen xenograft samples](../sources/llora-batlle-2024-10x-flex-fixed-xenograft-single-cell.md)
- [3DisoGalaxy: a structure-grounded breast cancer atlas of alternative-splicing-derived proteoforms](../sources/jiang-2026-3disogalaxy-breast-cancer-isoform-foldome.md)
- [A deep-learning framework to predict cancer treatment response from histopathology images through imputed transcriptomics](../sources/hoang-2024-deep-learning-framework-predict-cancer.md)
- [A generative reference grammar of healthy TCR repertoires for cancer immune remodeling analysis](../sources/balan-2026-generative-reference-grammar-tcr-repertoires-cancer.md)
- [A longitudinal single-cell and spatial multiomic atlas of pediatric high-grade glioma](../sources/sussman-2026-longitudinal-single-cell-spatial-multiomic-atlas.md)
- [A transcription factor atlas of directed differentiation](../sources/joung-2023-transcription-factor-atlas-directed-differentiation.md)
- [Advances in mass spectrometry instrumentation and methodology for analysis of alternative protein isoforms](../sources/lehe-2026-mass-spectrometry-alternative-protein-isoforms-review.md)
- [Applications of single-cell RNA sequencing in drug discovery and development](../sources/sande-2023-applications-single-cell-rna-sequencing.md)
- [Best practices for single-cell analysis across modalities](../sources/heumos-2023-best-practices-single-cell-analysis.md)
- [CADDIE: web-based network-medicine platform for cancer driver-based drug repurposing](../sources/hartung-2022-caddie-cancer-driver-drug-repurposing-platform.md)
- [Cancer ecosystems: A dynamic interplay across scales](../sources/quail-2026-cancer-ecosystems-dynamic-interplay-across-scales.md)
- [CenSegNet: a generalist high-throughput framework for centrosome phenotyping in heterogeneous cancer tissues](../sources/cheng-2025-censegnet-centrosome-phenotyping-cancer-tissues.md)
- [Clinical outcomes and spatial transcriptomic profiles of CD19/20 CAR-T therapy in relapsed or refractory B-cell non-Hodgkin's lymphoma](../sources/wang-2026-clinical-outcomes-spatial-transcriptomic-profiles-car.md)
- [Coordinated inheritance of extrachromosomal DNAs in cancer cells](../sources/hung-2024-coordinated-inheritance-extrachromosomal-dnas-cancer.md)
- [Cross-assay RNA modeling reveals robust cancer biomarkers across heterogeneous platforms](../sources/townsend-2026-cross-assay-rna-modeling-cancer-biomarker-discovery.md)
- [Cross-species single-cell and spatial transcriptomic mapping reveals EFNA1-EPHA4-mediated stem-like epithelial-macrophage crosstalk driving colorectal cancer progression](../sources/zhang-2026-cross-species-single-cell-spatial-transcriptomic.md)
- [Deep-learning-based de novo discovery and design of therapeutics that reverse disease-associated transcriptional phenotypes](../sources/xing-2026-deep-learning-de-novo-transcriptional-phenotype-reversal.md)
- [Do larger models really win? A scaling benchmark in AI-driven drug discovery](../sources/guo-2026-larger-models-scaling-benchmark-drug-discovery.md)
- [DrugCLIP: contrastive protein-ligand model for genome-scale virtual screening (GenomeScreenDB)](../sources/jia-2026-drugclip-contrastive-protein-ligand-genome-scale.md)
- [Epstein-Barr virus orchestrates spatial reorganization and immunomodulation in the classic Hodgkin lymphoma tumor microenvironment](../sources/yeo-2026-epstein-barr-virus-orchestrates-spatial-reorganization.md)
- [Evidence of off-target probe binding affecting 10x Genomics Xenium gene panels compromise accuracy of spatial transcriptomic profiling](../sources/hallinan-2026-evidence-off-target-probe-binding-affecting.md)
- [Expanding the human proteome with peptideins from non-canonical ORFs](../sources/deutsch-2026-expanding-human-proteome-peptideins-noncanonical-orfs.md)
- [Extra-lineage tissue programs define transcriptional states in human pancreatic cancer](../sources/ge-2026-extra-lineage-tissue-programs-pancreatic-cancer-transcriptional.md)
- [Extrachromosomal DNA Amplification Contributes to Small Cell Lung Cancer Heterogeneity and Is Associated with Worse Outcomes](../sources/pongor-2023-extrachromosomal-dna-amplification-contributes-small.md)
- [Extrachromosomal DNA gives cancer a separate evolutionary pathway](../sources/wang-2025-extrachromosomal-dna-cancer-evolutionary-pathway.md)
- [Global detection of human variants and isoforms by deep proteome sequencing](../sources/sinitcyn-2023-global-detection-human-variants-isoforms-deep-proteome.md)
- [High resolution mapping of the tumor microenvironment using integrated single-cell, spatial and in situ analysis](../sources/janesick-2023-high-resolution-mapping-tumor-microenvironment.md)
- [IGHG1+ malignant epithelial Cell-myCAF crosstalk via MIF-CD74/APP-CD74 drives early brain metastasis in NSCLC: Delineated via primary tumor-brain metastasis single-cell and spatial transcriptomics](../sources/yang-2026-ighg-malignant-epithelial-cell-mycaf-crosstalk.md)
- [Integrated genomic and proteomic profiling reveals insights into chemoradiation resistance in cervical cancer](../sources/sambath-2026-integrated-genomic-proteomic-cervical-cancer-chemoradiation-resistance.md)
- [Integrative analysis of lung adenocarcinoma across diverse ethnicities and exposures](../sources/satpathy-2025-integrative-analysis-lung-adenocarcinoma-across-diverse.md)
- [Linking spatial biology and clinical histology via Haiku](../sources/cui-2026-haiku-tri-modal-spatial-biology-histology.md)
- [Lymphoid chemokine signalling limits CD8+ T cell priming time to preserve effector function](../sources/altenburger-2026-lymphoid-chemokine-cd8-priming-effector.md)
- [MARCO promotes cholangiocarcinogenesis by inducing immunosuppression and its targeting reduces tumor growth](../sources/agirrelizaso-2026-marco-promotes-cholangiocarcinogenesis-inducing-immunosuppression-its.md)
- [MolGene-E: inverse molecular design from single-cell transcriptomic reversal for anticancer perturbation](../sources/ohlan-2025-molgene-e-inverse-molecular-design-transcriptomic-reversal.md)
- [Molecular cartography uncovers evolutionary and microenvironmental dynamics in sporadic colorectal tumors](../sources/heiser-2023-molecular-cartography-uncovers-evolutionary-microenvironmental.md)
- [Multimodal data fusion for cancer biomarker discovery with deep learning](../sources/steyaert-2023-multimodal-data-fusion-cancer-biomarker.md)
- [Multimodal deep learning on LINCS L1000 reveals brain-penetrant Class I HDAC inhibitors as pan-cancer candidates](../sources/tong-2026-multimodal-lincs-pan-cancer-hdac-inhibitor.md)
- [Non-invasive profiling of the tumour microenvironment with spatial ecotypes](../sources/zhang-2026-non-invasive-tumour-microenvironment-spatial-ecotypes.md)
- [Open Targets Gentropy: pleiotropy mapping across 100,526 GWAS for therapeutic target prioritisation](../sources/tsepilov-2026-open-targets-gentropy-pleiotropy-gwas-prioritisation.md)
- [PEXMap: A proteogenomic method for exon and isoform level mapping of mass spectrometry derived peptides](../sources/awasthi-2026-pexmap-proteogenomic-exon-isoform-mapping.md)
- [Pan-cancer virtual spatial transcriptomics from routine histology with Phoenix](../sources/tran-2026-phoenix-pan-cancer-virtual-spatial-transcriptomics.md)
- [Parallel sequencing of extrachromosomal circular DNAs and transcriptomes in single cancer cells](../sources/gonzalez-2023-parallel-sequencing-extrachromosomal-circular-dnas.md)
- [Predicting bladder cancer molecular subtypes and BCG response from histology using deep learning](../sources/khoraminia-2026-predicting-bladder-molecular-subtypes-bcg-response.md)
- [Prediction of DNA methylation-based tumor types from histopathology in central nervous system tumors with deep learning](../sources/hoang-2024-prediction-dna-methylation-based-tumor.md)
- [ProteinAligner: Tri-modal contrastive protein language model integrating sequence, structure, and text](../sources/zhang-2026-proteinaligner-tri-modal-contrastive-protein-language.md)
- [Proteogenomic Characterization Reveals Metabolic Vulnerabilities and Aberrant Phosphorylation in Colorectal Metastasis to Liver](../sources/zhao-2026-proteogenomic-characterization-reveals-metabolic-vulnerabilities.md)
- [Proteogenomic Characterization Reveals Subtype-Specific Therapeutic Potential for HER2-Low Breast Cancer](../sources/xu-2026-proteogenomic-characterization-reveals-subtype-specific-therapeutic.md)
- [Proteogenomic decoding of chemotherapy resistance in triple-negative breast cancer](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md)
- [Reimagining human-centric drug development with new approach methodologies (NAMs)](../sources/wu-2026-reimagining-human-centric-drug-development-nams.md)
- [Resolving sensitivity, specificity and signal contamination in Xenium spatial transcriptomics](../sources/bilous-2026-xenium-sensitivity-specificity-signal-contamination.md)
- [SCENIC+: single-cell multiomic inference of enhancers and gene regulatory networks](../sources/gonzalezblas-2023-scenic-single-cell-multiomic-inference.md)
- [Sarcoma microenvironment cell states and ecosystems are associated with prognosis and predict response to immunotherapy](../sources/subramanian-2024-sarcoma-microenvironment-cell-states-ecosystems.md)
- [Schwann cells regulate tumor cells and cancer-associated fibroblasts in the pancreatic ductal adenocarcinoma microenvironment](../sources/xue-2023-schwann-cells-regulate-tumor-cells.md)
- [Simulating 500 million years of evolution with a language model](../sources/hayes-2025-simulating-500-million-years-evolution.md)
- [Single-cell and spatial transcriptomics implicate a prognostic function of tertiary lymphoid structures in gastric cancer](../sources/wang-2025-single-cell-spatial-transcriptomics-implicate-prognostic.md)
- [Single-cell spatial multiomics identifies POSTN+ CAFs driving chemoradiotherapy resistance in rectal cancer](../sources/sakai-2026-postn-cafs-chemoradiotherapy-resistance-rectal-cancer.md)
- [Spatial multi-omics identifies aggressive prostate cancer signatures highlighting pro-inflammatory chemokine activity in the tumor microenvironment](../sources/krossa-2025-spatial-multi-omics-identifies-aggressive-prostate.md)
- [Spatial multi-omics unveils the monoclonal origin, neuroendocrine plasticity, and microenvironment niches in combined small-cell lung cancer](../sources/wang-2026-spatial-multi-omics-unveils-monoclonal-origin.md)
- [Spatially informed clustering, integration, and deconvolution of spatial transcriptomics with GraphST](../sources/long-2023-spatially-informed-clustering-integration-deconvolution.md)
- [Systematically decoding pathological morphologies and molecular profiles with unified multimodal embedding](../sources/zhang-2026-systematically-decoding-pathological-morphologies-multimodal-embedding.md)
- [T cell state transcription factor cooperation engineering: KLF2 x RUNX2 memory-like CAR-T design](../sources/savage-2026-klf2-runx2-memory-like-car-t.md)
- [TWAS signature-matching for drug prioritisation: a best-practice benchmark](../sources/chauquet-2026-twas-signature-matching-drug-prioritisation-benchmark.md)
- [The AICL-KLRF1 axis supports CD4-CD8 T cell communication and cytokine competence in pre-exhausted CD8+ T cells](../sources/barone-2026-aicl-klrf-axis-supports-cell-communication.md)
- [The Reactome Pathway Knowledgebase 2024](../sources/orlicmilacic-2023-reactome-pathway-knowledgebase-2024.md)
- [Towards a general-purpose foundation model for computational pathology](../sources/chen-2024-towards-general-purpose-foundation-model.md)
- [Ultra-precision deconvolution of spatial transcriptomics decodes immune heterogeneity and fate-defining programs in tissues](../sources/xu-2026-ultra-precision-deconvolution-spatial-transcriptomics-decodes.md)
- [Understanding immune checkpoint inhibitor efficacy through spatial decoding of the lung cancer tumor immune microenvironment](../sources/zou-2026-understanding-immune-checkpoint-inhibitor-efficacy-through.md)
- [Unraveling pancreatic ductal adenocarcinoma at single-cell resolution with spatial insights: From mechanisms to clinical translation](../sources/qi-2026-unraveling-pancreatic-ductal-adenocarcinoma-single-cell.md)
- [iCLAP: an innovative method for integrable co-detection of low-abundance antigens with high-plex immunostaining](../sources/wu-2026-iclap-innovative-method-integrable-detection-low.md)
- [nf-core Nextflow disease module discovery and benchmarking pipeline for network medicine reproducibility](../sources/kersting-2025-nf-core-disease-module-network-medicine.md)
