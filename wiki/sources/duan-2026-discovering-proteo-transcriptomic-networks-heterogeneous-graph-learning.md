---
title: "Discovering Proteo-Transcriptomic Networks via Biologically Informed Heterogeneous Graph Learning"
authors: [Jingxian Duan, Yaou Liu, Dongling Pei, Zijian Zhou, Yuanshen Zhao, Jingran Deng, Haofei Ma, Hong Zhao, Zeyu Ma, Zilong Wang, Shifu Chen, Hairong Zheng, Dong Liang, Zhenyu Zhang, Zhi-Cheng Li]
year: 2026
journal: "Nucleic Acids Research"
doi: 10.1093/nar/gkag386
pmid: 42059203
pmcid: PMC13129546
license: CC BY-NC 4.0
paper_kind: method
modalities: [transcriptomics, proteomics, phosphoproteomics]
cancer_types: [colorectal-cancer, glioblastoma, pediatric-low-grade-glioma, pancreatic-ductal-adenocarcinoma]
themes:
  - multi-omic-graph-learning
  - heterogeneous-graph-neural-network
  - proteo-transcriptomic-network
  - biologically-informed-neural-network
  - kegg-string-prior
  - prognosis-prediction
  - mgsva
  - map4
  - pan-cancer-method
discovery_method: user-shared
pdf_status: html-only
topic: cancer-multiomics
cm_axis: integration
---

# Discovering Proteo-Transcriptomic Networks via Biologically Informed Heterogeneous Graph Learning

## Summary

Duan et al. (Nucleic Acids Res 2026;54(8):gkag386, OA CC BY-NC 4.0) propose **bioGraph**, a biologically informed heterogeneous graph neural network that jointly models mRNA / protein / phosphoprotein measurements as three distinct node types and five edge types (3 intra-omic + 2 inter-omic), trained with a Cox partial-likelihood loss for patient-specific survival risk prediction. Nodes are restricted to KEGG pathway genes; intra-omic edges follow KEGG pathway co-membership (RNA layer) and STRING-db PPI ≥700 (protein/phospho layers); inter-omic edges link the same gene across layers (RP = translation, PP = post-modification). The model is benchmarked on four CPTAC proteo-transcriptomic cohorts (COAD n=79, GBM n=74, pLGG n=73, PDAC n=92) and outperforms five multi-omic baselines (MOGONET / IGNN / MMGL / SALMON / MRGCN) on cross-validated C-index. From the trained graph, the authors extract three subgraph types (intra-omic, inter-omic, cross-omic) and introduce **MGSVA**, a KS-like running-sum statistic on edge weights that extends GSVA to multi-omic interaction activity. Inter-omic analysis identified five genes (MAP4 / SORBS1 / SPTAN1 / SRRM1 / TMPO) with consistent RP–PP edge-weight discordance across all four cancer types. **MAP4**, which is not flagged by conventional DEG analysis, was validated as a glioma tumor-promoting factor through an independent 119-patient FAHZZU glioma cohort (mRNA P<0.015, protein P<0.01) and T98G/U251 GBM cell-line shRNA experiments (↓migration/proliferation/colony formation, ↑apoptosis). Interactive platform: https://biograph.hapyun.com; code: codeocean.com/capsule/2357965.

## Key Points

### Method design — three-layer heterogeneous graph with KEGG/STRING priors

- Three node types: mRNA, protein, phosphoprotein; restricted to genes within KEGG pathway maps.
- Five edge types:
  - **Intra-omic transcriptome**: KEGG pathway co-membership (gene pairs within same pathway).
  - **Intra-omic proteome / phosphoproteome**: STRING-db v11.0b PPI with affinity score ≥700.
  - **Inter-omic RP (RNA–protein)**: same-gene cross-layer edge mimicking translation.
  - **Inter-omic PP (protein–phosphoprotein)**: each protein linked to its measured phosphosites mimicking post-modification.
- Inter-omic relations treated as **bidirectional during message passing** (paper explicitly notes bioGraph does not infer causal molecular flow from observational data); typed edges + relation-specific parameters preserve relation semantics.
- 2-layer HeteroRGCN via DGL with relation-specific edge-aware modulation (learned edge representations modulate messages; distinguished from GAT-style softmax attention). Cox partial-likelihood loss + L2 regularization; Adam optimizer; StepLR (step 20); gradient clip 1.0; early stopping on training-loss convergence (threshold 0.0001–0.002).

### Performance — outperforms 5 multi-omic baselines on 4 CPTAC cohorts

- Mean cross-validated C-index (5-fold for GBM/pLGG/PDAC; 3-fold for COAD due to repeated DFS values):
  - COAD: bioGraph **0.91±0.08**; transcriptome 0.89, proteome 0.89, phospho 0.49.
  - GBM: bioGraph **0.71±0.04**; transcriptome 0.56, proteome 0.66, phospho 0.69.
  - pLGG: bioGraph **0.73±0.03**; transcriptome 0.58, proteome 0.61, phospho 0.63.
  - PDAC: bioGraph **0.74±0.02**; transcriptome 0.59, proteome 0.59, phospho 0.53.
- Outperformed MOGONET / IGNN / MMGL / SALMON / MRGCN across all four datasets (Table 1 in paper). Kaplan–Meier high/low-risk separation log-rank P<0.05 in both training and validation cohorts.
- Ablations (Table 2 in paper): removing **biological priors** drops C-index across all 4 datasets (largest drop in PDAC 0.74→0.47); removing **edge-aware weighting** drops GBM 0.71→0.58 and pLGG 0.73→0.60. Two-layer variants (transcriptome–proteome; proteome–phospho) generally beat single-omic; phospho-only is the worst-performing single-omic in 2/4 datasets.
- bioGraph risk score correlated with tumor histology, BRAF status, and tumor necrosis (Supplementary Figs S1–S3).

### Intra-omic subgraph — interaction structure vs. DEG enrichment

- Subgraphs filtered by edge-weight top percentile (1% transcriptome / 5% proteome / 10% phospho) and intersected with high-risk vs. low-risk DEG-enriched pathways (edgeR P<0.05 in both training and validation).
- Top-ranked bioGraph nodes overlap with transcriptomic DEGs at 27% (COAD), 43% (GBM), 6% (pLGG), 21% (PDAC); overlap lower in protein/phospho layers (smaller DEG counts).
- Edge-weight reproducibility across 5 CV folds: Pearson P<0.05 in most pairwise comparisons; weakest for several edge categories in GBM (Supplementary Fig. S4).

### Inter-omic subgraph — pLGG has distinct cross-omic regulation

- RP vs. PP edge-weight comparison per gene across cohorts:
  - RP > PP in **91.49% / 93.37% / 94.77%** of genes in GBM / COAD / PDAC respectively.
  - pLGG: only **19.51%** RP > PP, **33.99%** PP > RP — distinct from adult tumors.
- Inter-omic-significant gene pathway enrichment (RP/PP weight Pearson with survival, P<0.05 in both training and validation): cell adhesion, oncogenic signaling, immune processes, metabolism, protein production.
- Cross-cohort intersection identifies a **5-gene core set**: MAP4, SORBS1, SPTAN1, SRRM1, TMPO — each has multiple measured phosphosites; bioGraph PP edge weights prioritize the most prognostic phospho-site per gene.

### MGSVA — edge-weight-based pathway activity score

- Extends GSVA: pathway membership defined on **edges connecting two pathway genes** (not on individual gene expression).
- Per relation type, edges ranked by decreasing weight; KS-like running-sum statistic with weighting exponent → 5 pathway scores per patient (one per edge type).
- Positive MGSVA = pathway-associated edges enriched at high-weight end; negative = depleted.
- Cross-cohort prognosis-correlated pathways (Pearson P<0.05 in both training and validation) cluster around metabolism and oncogenic signaling; same pathway can have different prognosis correlations for different edge types (transcriptome vs. proteome vs. phospho) — implying edge-type-specific therapeutic targeting.

### MAP4 validation — independent cohort + cell-line functional assays

- Discovery cohorts (CPTAC GBM/pLGG): higher MAP4 mRNA/protein associated with worse prognosis (Supplementary Fig. S10A).
- Independent FAHZZU glioma cohort (n=119; ClinicalTrials.gov NCT04216537, IRB 2019-KY-176): MAP4 **mRNA P<0.015**, **protein P<0.01** for shorter OS. Also significant: SPTAN1 mRNA P<0.001, TMPO protein P<0.05.
- T98G + U251 GBM cell lines with MAP4 shRNA (TRCN0000117163 / TRCN0000117166):
  - Wound healing / trans-well migration: significantly reduced.
  - CCK-8 + colony formation: significantly reduced proliferation/self-renewal.
  - Annexin V-FITC/PI FACS: increased apoptosis vs. sh-NC control.
- MAP4 was **not** flagged by conventional DEG analysis in any of the four discovery cohorts; identified through abnormal inter-omic edge weight pattern (RP/PP discordance).

### EMOGI cross-comparison — bioGraph also recovers cancer gene labels

- EMOGI = Schulte-Sasse 2021 GCN for cancer gene prediction across 5 PPI networks (CPDB / iRefIndex / Multinet / PCNet / STRING).
- bioGraph (using Youden's J binarization of continuous node features) achieved higher AUC than EMOGI in **one of the five PPI networks** for cancer gene identification.
- Reciprocally, EMOGI flagged MAP4 / SORBS1 / SPTAN1 as cancer-related in **3/4** discovery datasets; SRRM1 / TMPO in **2/4**.

### Limitations (stated in paper)

- **Retrospective design, limited cohort sizes** (COAD 79, GBM 74, pLGG 73, PDAC 92 — and FAHZZU validation n=119); cross-validation and multi-center sourcing only partly mitigate.
- **Clinical actionability unvalidated**: bioGraph identifies prognosis-associated cross-omic networks but does not show that these networks guide targeted therapy choices.
- **Requires matched complete omics**: extending bioGraph to partial / missing-modality inputs is flagged as future work.
- **Mechanistic roles of inter-omic edges await experimental validation**, particularly for the PP edges and the 5-gene core set beyond MAP4.

## Methods

- **Cohorts**: CPTAC via cBioPortal — COAD 79, GBM 74, pLGG (astrocytoma WHO grade I/II) 73, PDAC 92.
- **Endpoints**: DFS for COAD and pLGG (excluding samples without DFS or DFS > OS); OS for GBM and PDAC (excluding non-cancer-related deaths).
- **External validation cohort**: 119 primary curative-resection glioma tissues from First Affiliated Hospital of Zhengzhou University (FAHZZU) 2019–2021, no prior anti-tumor treatment; transcriptomic + proteomic sequencing per Duan 2023 protocol; ClinicalTrials.gov NCT04216537, IRB 2019-KY-176.
- **Preprocessing**: CPTAC data used as provided (no log transformation); features with >20% missing removed; remaining missing → NaN; z-score standardization per cohort and omic layer.
- **Graph construction**:
  - Nodes = KEGG pathway genes per layer.
  - Intra-omic edges = KEGG pathway co-membership (RNA) + STRING v11.0b PPI score ≥700 (protein/phospho).
  - Inter-omic edges = same-gene RP and PP links.
- **Training**: 2-layer HeteroRGCN via DGL with relation-specific learnable matrices for edge feature transform; LeakyReLU; mean aggregation within relation + mean fusion across relations. Cox partial-likelihood loss + L2; Adam (COAD/pLGG lr vs. GBM/PDAC lr per Supplementary Table S2); up to 200 epochs; StepLR step 20; gradient clip 1.0; deterministic seeding; PyTorch + DGL.
- **Cross-validation**: 5-fold (GBM/pLGG/PDAC); 3-fold (COAD due to repeated DFS values); risk-score-based KM stratification; edge-weight Pearson correlation across folds for stability assessment.
- **Benchmark baselines**: MOGONET, EMOGI, IGNN, MMGL, SALMON, MRGCN — all run on identical data splits.
- **Ablation conditions**: (i) fully connected baseline at matched parameter budget (removes priors); (ii) no edge-aware weighting; (iii) two-layer variants (transcriptome–proteome; proteome–phospho); (iv) single-omic graphs (including GraphSAGE and GAT on each single-omic graph).
- **Subgraph extraction**:
  - Intra-omic: edge weight top 10% for visualization (training/inference uses full graph); pathway-of-interest filtering via edgeR + clusterProfiler enrichment (P<0.05 in both training and validation); top 1% (RNA) / 5% (protein) / 10% (phospho) edges for Cytoscape visualization.
  - Inter-omic: per-gene RP/PP weight comparison (training + validation both P<0.05) → tree-like subgraphs.
  - Cross-omic: pathway-based extraction with top 50% edges in both training and validation.
- **MGSVA**: KS-like running-sum on edge weights ranked by magnitude per relation type; pathway-edge set = edges connecting two pathway genes; min-max normalization of Mann–Whitney U statistic across edge types for overall pathway score; pathways retained only if consistent in training and validation.
- **In vitro MAP4 validation**: T98G + U251 GBM cells (Cell Resource Center Shanghai) infected with pLKO.1 TRC lentivirus encoding sh-MAP4#1 (TRCN0000117163) or sh-MAP4#2 (TRCN0000117166); puromycin 1 μg/ml selection. Assays: wound healing 0/24/48 h; trans-well migration 24 h (5×10⁴ cells, 30% FBS gradient); CCK-8 proliferation (1×10³ cells/well, 4 days); colony formation (1×10⁴ cells/well, 2 weeks, crystal violet ≥50-cell colonies); Annexin V-FITC/PI apoptosis by flow cytometry (FlowJo 7.6.1). MAP4 detection: RT-qPCR (SYBR Green, GAPDH ref) + immunoblot (Cloud-clone PAB319Hu01 1:1000).
- **Statistics**: R 4.1.0 + Python 3.8. Normality test → Wilcoxon / Mann–Whitney / t-test depending on result. In vitro: t-test (two groups) or one-way ANOVA. Edge-weight statistics and node-embedding analyses **conducted within each cancer cohort**; no direct quantitative comparison of edge weights or embeddings across cohorts.
- **Data availability**: Input data from cBioPortal (https://www.cbioportal.org); preprocessed data on https://biograph.hapyun.com/analysis-workflow/; external validation RNA-seq in GSA HRA006184; external validation MS proteomics in iProX **PXD062023**; code at codeocean.com/capsule/2357965 and biograph.hapyun.com/analysis-workflow/Pipeline.
- **Conflict of interest**: Shifu Chen is employed by HaploX Biotechnology Co. Ltd. Other authors declare none.

## Cancer Multiomics Project Relevance

한미암 과제는 한국인 코호트의 **WGS/RNA-seq/global proteome/phosphoproteome 4-layer 데이터를 환자 단위로 결합해 임상 결과(OS / PFS / 치료 반응) 예측 및 분자 아형 stratification으로 이어주는 분석 파이프라인**을 운영해야 한다. Duan et al. 2026 bioGraph는 다음 5축에서 한 단계 더 구체적으로 한미암 파이프라인의 reference로 사용된다.

- **Cohort scale에 맞춰진 multi-omic graph learning method 후보**: bioGraph는 CPTAC 4-cohort(COAD 79 / GBM 74 / pLGG 73 / PDAC 92) — 한미암 단일 암종 코호트 규모(50–100명)와 동일 스케일 — 에서 5-fold CV C-index 0.71–0.91을 보고했고, MOGONET / IGNN / MMGL / SALMON / MRGCN(MOGONET COAD 0.66 / IGNN COAD 0.63) 대비 일관 우위. 한미암 TNBC chemo response 예측, CRLM C1/C2 subtype call, 가스트릭 cohort survival stratification 등 환자 수 100명 이하 시나리오에서 single-omic regression / multi-omic late-fusion 대비 graph 기반 prior-informed 방법론을 1차 비교 후보로 둘 근거.
- **KEGG + STRING-db priors로 학습 안정성 확보 - 한미암 비교 ablation 설계 reference**: 한미암 코호트에서 다층 graph learning 적용 시 prior 없이(fully-connected baseline) 학습하면 PDAC C-index 0.74→0.47(–0.27)까지 무너지는 것이 본문에 명시되어 있어, 한미암 graph 모델 ablation 설계에서 "biological prior 제거 vs. 유지" + "intra-omic edge-source(KEGG vs. STRING) 분해" + "edge-aware weighting 제거" 3축은 필수 비교 셀로 둘 수 있다. 동일 priors(KEGG + STRING v11.0b ≥700)로 한미암 cohort에 1차 재현 후 cohort-specific prior(예: KEGG cancer pathway 한정, COSMIC driver gene PPI 한정) 확장 비교 가능.
- **Inter-omic edge 기반 hidden marker identification logic - 한미암 protein-level/phospho-level prioritization 보완**: MAP4는 DEG 분석에서 prioritize되지 않았지만 RP/PP edge weight 비대칭으로 식별되었다. 한미암 코호트에서 expression-level fold-change가 작지만 RP/PP information flow가 비대칭인 protein/phosphosite를 식별하면 기존 DEG-based marker 후보군이 놓치는 inter-omic-regulated targets를 추출할 수 있다. 5-gene core set(MAP4 / SORBS1 / SPTAN1 / SRRM1 / TMPO)은 4 cancer 공통 RP-PP 비대칭 유전자로, 한미암 cohort에서도 같은 inter-omic discordance를 보이는지 우선 확인할 수 있는 후보 starting set.
- **pLGG-style inter-omic 비대칭 패턴이 한미암 소아·저등급 암종 분석 가설**: GBM/COAD/PDAC는 RP > PP 비율 91–95%인데 pLGG는 RP > PP가 19.5%로 정반대(post-translational regulation 우세). 한미암 코호트에 소아 암종 / 저등급 / 저분자 부담(TMB low) 환자군이 포함될 때 inter-omic 구조가 성인 진행성 암종과 다를 수 있다는 가설을 미리 확보; phospho-layer-heavy stratification 우선순위 조정의 근거.
- **MGSVA edge-weight pathway activity score - 한미암 pathway-level cohort visualization 도구**: MGSVA는 GSVA를 multi-omic 상호작용 수준으로 확장해 edge 단위 pathway activity 점수를 산출한다. 한미암 cohort에서 동일 pathway라도 transcriptome / proteome / phospho 별 prognosis 방향이 다른지 직접 비교할 수 있는 표준 visualization 도구로 사용 가능. 단, MGSVA는 edge weight가 학습된 후의 score이므로 bioGraph 또는 동등 heterogeneous GCN을 한미암 cohort에 한 번 학습한 뒤 적용 가능. 한미암 SHMT1/NDRG1(Zhao 2026) 등 metabolism + RNA function pathway 검토 시 동일 도구로 cross-omic activity 비교 가능.

다만 본문 명시 한계 — retrospective single-platform cohort, 환자별 모든 modality 측정 가정, 클리니컬 actionable 검증 부재, MAP4 외 4 gene mechanistic validation 미수행 — 는 한미암 활용 시에도 동일하게 적용된다. partial-omics 환자(예: WGS-only 또는 protein-only)는 현재 bioGraph 형식으로 학습 불가하며, bioGraph가 식별하는 hidden marker는 분리된 in vitro/in vivo 검증 단계 필요.

## Connections

- **Method baselines compared in paper**: MOGONET (Wang 2021 Nat Commun) / EMOGI (Schulte-Sasse 2021 Nat Mach Intell) / IGNN (Qiu 2022 Nat Commun) / MMGL (Zheng 2022 IEEE TMI) / SALMON (Huang 2019 Front Genet) / MRGCN (Yang 2023 Bioinformatics) — 한미암 graph learning 비교 후보 그룹.
- **Biologically informed NN family**: P-NET (Elmarakeby 2021 Nature, prostate cancer) / Cox-PASNet (Hao 2019 BMC Med Genomics) / GenNet (van Hilten 2024 npj Syst Biol Appl) — Duan et al. 본문 명시 BINN line, gene-level aggregation 한계 비교.
- **CPTAC input cohorts**: Vasaikar 2019 COAD / Wang 2021 GBM / Petralia 2020 pediatric brain / Cao 2021 PDAC — bioGraph가 직접 input으로 사용. 한미암 cohort에서 동등 데이터를 만들 때의 4-layer 측정 기준 reference (wiki에 Vasaikar 2019 sources/vasaikar-2019-proteogenomic-analysis-human-colon-cancer.md 존재).
- **Pan-cancer proteogenomics reference**: Li 2023 Cell driver-to-functional-state / Petralia 2024 Cell tumor immunity — bioGraph 본문에 Discussion에서 인용; 한미암 pan-cancer 비교 reference로도 사용 (wiki analyses에 brief 존재).
- **PTM atlas reference**: Geffen 2023 Cell pan-cancer PTM — bioGraph가 인용한 PTM cross-cohort 패턴 reference.
- **External resources**: KEGG (Kanehisa 2000) / STRING v11.0b (Szklarczyk 2019) / DGL (Wang 2019) / clusterProfiler (Yu 2012) / edgeR (Robinson 2010) / Cytoscape (Shannon 2003) / GSVA (Hanzelmann 2013).
- **Topic hub**: [Cancer Multiomics Literature - 6.1 AI / Foundation models / Deep learning](../topics/cancer-multiomics-literature.md#61-ai--foundation-models--deep-learning).
- **Corpus queue**: [Cancer Multiomics Corpus Queue (Target=100)](../analyses/cancer-multiomics-corpus-queue.md).

## Sources

- Duan J, Liu Y, Pei D, Zhou Z, Zhao Y, Deng J, Ma H, Zhao H, Ma Z, Wang Z, Chen S, Zheng H, Liang D, Zhang Z, Li Z-C. **Discovering proteo-transcriptomic networks via biologically informed heterogeneous graph learning.** Nucleic Acids Research. 2026 Apr 30;54(8):gkag386. doi: [10.1093/nar/gkag386](https://doi.org/10.1093/nar/gkag386). PMID: 42059203. PMCID: PMC13129546.
- Interactive platform: https://biograph.hapyun.com (per-patient subgraph viewer; KEGG-pathway-coded color).
- Code: https://codeocean.com/capsule/2357965/tree; pipeline: https://biograph.hapyun.com/analysis-workflow/Pipeline.
- Data: cBioPortal (https://www.cbioportal.org); external validation RNA-seq GSA **HRA006184**; external validation MS proteomics iProX **PXD062023**.
- License: CC BY-NC 4.0 (Oxford University Press).
- Local copy: `raw/inbox/papers/duan-2026-discovering-proteo-transcriptomic-networks-heterogeneous-graph-learning.html` (PMC HTML).
