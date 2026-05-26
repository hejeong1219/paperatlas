---
title: "Multimodal fusion of radio-pathology and proteogenomics identify integrated glioma subtypes with prognostic and therapeutic opportunities."
authors:
  - "Liu"
  - "Wu"
  - "Xu"
year: "2025"
journal: "Nature Communications"
doi: "10.1038/s41467-025-58675-9"
pmid: "40222975"
pmcid: "PMC11994800"
paper_kind: proteogenomic
pdf: "raw/inbox/papers/liu-2025-multimodal-fusion-radio-pathology-proteogenomics-identify.pdf"
topic: ptmanchor
extra_topics:
  - "resistance"
tags:
  - "multimodal-fusion"
  - "glioma"
  - "idh-wildtype"
  - "radiomics"
  - "pathomics"
  - "proteogenomic"
  - "anti-pd-1"
  - "tumor-microenvironment"
  - "cancer-proteomics"
  - "pmid-40222975"
themes:
  - "multimodal-fusion"
  - "cancer-proteomics"
  - "immunotherapy-response"
---
# Multimodal fusion of radio-pathology and proteogenomics identify integrated glioma subtypes with prognostic and therapeutic opportunities

_Nature Communications 16:3510, 2025._ PMID: [40222975](https://pubmed.ncbi.nlm.nih.gov/40222975/) · DOI: [10.1038/s41467-025-58675-9](https://doi.org/10.1038/s41467-025-58675-9) · PMC: [PMC11994800](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11994800/)

## Summary

Liu et al. introduce MOFS (multimodal fusion subtyping), a 5-layer intermediate-fusion clustering framework that takes radiomics (5,929 MRI features from T1WI/CE-T1WI/T2WI/FLAIR/ADC), pathomics (CellProfiler features from WSIs), WES, RNA-seq, and DIA mass-spec proteomics from the same 122 IDH-wildtype adult glioma patients (FAHZZU1 cohort) and combines 11 fusion algorithms (CIMLR, iClusterBayes, IntNMF, LRAcluster, MCIA, NEMO, PINSPlus, RGCCA, SGCCA, SNF, CPCA) via late-fusion COCA to define three robust subtypes: **MOFS1 (proneural)** with neurodevelopmental enrichment, neuron/astrocyte/oligodendrocyte infiltration, and the best prognosis; **MOFS2 (proliferative)** with cell-cycle/E2F enrichment, RTK-RAS+TP53 pathway hits, heavy CNV burden, STRAP amplification, TMZ resistance, and the worst prognosis; and **MOFS3 (TME-rich)** with abundant immune+stromal infiltration, immunogram-elevated cancer-immunity-cycle activity, and an anti-PD-1 response signal validated in an external GBM ICB cohort (Zhao et al., PRJNA482620). They show single-modality clustering fails to recover prognostic separation, validate the subtypes in 7 external transcriptomic cohorts using an ensemble 17-algorithm classifier (FAHZZU2/CGGA/GEO), and translate the taxonomy to the clinic with a 22-feature DNN classifier (resilient backpropagation) on MRI alone — predicting MOFS subtypes in 992 imaging-only FAHZZU3 cases with significant prognostic discrimination (P = 0.00025). STRAP emerges as a MOFS2-specific prognostic biomarker / therapeutic candidate; stromal abundance (S100A4) sub-stratifies MOFS3 into a low-stroma "MOFS1-like" and high-stroma "MOFS2-like" survival bracket. The work argues intermediate multimodal fusion materially outperforms single-omics taxonomy for IDH-wildtype GBM management.

## Key Points

- Cohorts: 1,194 IDH-wildtype glioma patients from FAHZZU split into FAHZZU1 (122 patients with all five modalities — radio/patho/WES/RNA/proteomics), FAHZZU2 (80 patients with transcriptomic + partial proteomics), and FAHZZU3 (992 patients with MRI only). Inclusion: age ≥18, primary glioma, IDH-wt by 2021 WHO classification, no prior radiation/chemo. Median WES coverage 112× tumor / 128× normal; DIA-MS on Orbitrap Exploris 480.
- MOFS framework: intermediate fusion of 11 algorithms (CIMLR, CPCA, iClusterBayes, IntNMF, LRAcluster, MCIA, NEMO, PINSPlus, RGCCA, SGCCA, SNF) → Jaccard-distance late fusion via 10,000-iteration COCA consensus clustering → silhouette filter (≥0.4) yields a 116-patient core; optimal K=3 by CPI + GAP + PAC + CHI; PCA shows clean separation.
- MOFS1 (proneural, n = 34, mostly histo-GBM with limited CE-T1WI enhancement): enriched in distal axon, GABA receptor binding, long-term synaptic depression, neuron-to-neuron synapse; high infiltration of neurons, astrocytes, oligodendrocytes (P < 0.0001); higher DNAH3 mutation frequency; the most favorable survival in both FAHZZU1 and 7 external cohorts.
- MOFS2 (proliferative, n = 33, mass-like CE-T1WI enhancement, heterogeneous H&E architecture with pronounced atypia): enriched in G1/S transcription, G2/M checkpoint, E2F targets, cell cycle; RTK-RAS and TP53 pathway mutation enrichment; SCN5/USH2A/PLEC mutations; heavy broad+focal CNV burden (chromosomal instability phenotype); the worst prognosis; no overall-survival benefit from TMZ (P = 0.179) suggesting chemo-resistance.
- MOFS3 (TME-rich, n = 49, all histo-GBM with ring-like enhancement + central necrosis): enriched in cell-extracellular matrix interaction, TNF-α via NF-κB, immune cell activation, IFN-γ response; lowest tumor purity, highest immune+stromal scores; predicted highest immunogram (cancer-immunity cycle) activation; in the external anti-PD-1 ICB cohort (Zhao et al.), MOFS3 patients enriched the responder group.
- STRAP as a MOFS2-specific biomarker: among 1,023 subtype-specific functional CNV genes, STRAP amplification was MOFS2-exclusive (P < 0.0001), with significantly higher mRNA + protein (IHC + TMA) expression; STRAP discriminates MOFS2 by ROC AUC 0.802; high STRAP CNV or expression independently predicts poor OS (IHC P = 0.00015); top 500 STRAP-correlated genes enriched in proliferation pathways — pointing to STRAP as a candidate druggable node for proliferative IDH-wt GBM.
- MOFS3 stromal heterogeneity: stromal abundance (ssGSEA score) was a prognostic axis within MOFS3 — low-stroma MOFS3 had survival comparable to MOFS1, high-stroma had survival comparable to MOFS2; S100A4 served as a translatable single-marker proxy for stroma level.
- Modality contribution analysis: dropping any single modality from the fusion preserved most prognostic separation, but single-modality clustering on its own failed to recover MOFS-equivalent survival groups — full multimodal Kaplan-Meier outperformed every single-omics or partial-multi-omics alternative.
- DNN radiomics classifier: 22 logistic-regression-selected MRI features fed into a resilient-backpropagation neural network; trained on FAHZZU1 with 60:40 internal split, validated on FAHZZU2, then applied to FAHZZU3 (992 imaging-only patients) — Kaplan-Meier across DNN-predicted MOFS subtypes in FAHZZU3 reached log-rank P = 0.00025; a web tool is provided for clinical use.
- Cross-cohort validation: a 17-algorithm ensemble transcriptomic classifier (selected from {GST, AdaBoost, DT, Enet, GBDT, KNN, Lasso, LDA, NBayes, NNet, PCA, RF, ridge, StepLR, SVD, SVM, XGBoost}) recapitulated MOFS survival differences in 8 external cohorts (FAHZZU2, CGGA-array, CGGA-RNAseq, and 6 GEO compilations); multivariate Cox confirmed prognostic value remained after adjusting for age, sex, MGMT status, and treatment.
- Limitations: classifier development relied on transcriptomic data alone for external cohorts (public datasets lack matched proteomics + pathomics + radiomics); single-tumor-class assignment ignores intratumoral spatial heterogeneity (each patient gets one MOFS label even though MRI features vary across regions); external validation of the DNN classifier on truly independent multi-center MRI cohorts is still pending.
- Code + data: MOFSR R package and pipeline at [github.com/Zaoqu-Liu/MOFS](https://github.com/Zaoqu-Liu/MOFS); ICB validation cohort = SRA PRJNA482620 (Zhao et al. 2019 anti-PD-1 GBM); ethics approval FAHZZU 2019-KY-176 / 2023-KY-1028.

## Methods

Five-modality intermediate fusion on a single-center 122-patient discovery cohort (FAHZZU1). MRI preprocessing: N4ITK bias correction, isotropic 1×1×1 mm³ resampling, mutual-information rigid registration to CE-T1WI, histogram matching for gray-level normalization, manual VOI delineation by a neuroradiologist (10+ yr experience), 5,929 PyRadiomics features extracted from rT1WI/rCE-T1WI/rT2WI/rFLAIR/rADC (first-order + shape + GLCM/GLRLM/GLSZM/GLDM/NGTDM textures on original + wavelet + LoG images), retained 4,271 with ICC ≥0.75. Pathomics: 20× WSI scanning (KF-PRO-120-HI), Otsu tissue segmentation in Lab space, Yottixel patch selection, CellProfiler v4.2.5 feature extraction. WES: SureSelect V6 capture, Novaseq 6000, BWA-mem hg38 alignment, GATK v4.2 + MuTect2 calling with paired normal, stringent VAF/MAF/COSMIC filters; CNVkit v0.9.9 + GISTIC2.0 for CNV calling. RNA-seq: HiSeq X Ten 150 bp PE, Trimmomatic → STAR v2.7.6a → RSEM v1.3.3 (GENCODE v35) → FPKM/TPM. Proteomics: Triton X-100 lysis, trypsin digestion, high-pH HPLC fractionation (12 fractions), EASY-nLC 1200 + Orbitrap Exploris 480 DIA-MS with FAIMS (-40/-55/-70 V), 350-1350 m/z primary at 120K resolution, 30K secondary. Fusion pipeline: 11 algorithms × 2,640 variable combinations selected by CPI+GAP, COCA consensus over 10,000 iterations on Jaccard distance, silhouette filter ≥0.4 for core sample identification. Validation: TMA IHC for STRAP / S100A4 (Proteintech antibodies), ssGSEA immune/stromal scores from prior GBM scRNA-seq markers, Immunogram via 8 cancer-immunity-cycle axes (per Karasaki et al.), MSigDB ssGST/ORA/GSEA enrichment.

## Cancer Multiomics Project Relevance

- 한미암/Cancer Multiomics 과제의 면역치료제 반응성 분석에서, anti-PD-1 반응이 단일 omics layer가 아니라 **radiomics + pathomics + 다중오믹스의 결합으로 정의된 TME-rich MOFS3**에 집중된 결과는 환자 층화 marker를 구성할 때 영상·병리 layer까지 포함시킨 통합 모델을 검토해볼 만한 강력한 사례다.
- MOFS2의 prognostic biomarker로 도출된 STRAP는 한미암 표적치료제 분석에서 IDH-wt GBM이 아니더라도 proliferative phenotype 환자군(예: cell-cycle high 코호트)에서 잠재 표적/예후 지표 후보로 cross-check해볼 가치가 있다. 같은 맥락에서 MOFS3 내 stromal abundance를 S100A4 단일 marker로 sub-stratify한 접근은 우리 코호트의 TME-rich 환자군에서 single-IHC-based stratification을 설계할 때 참고 모델이 된다.
- DNN radiomics classifier(22 MRI feature → MOFS subtype)는 multi-omics taxonomy를 **비침습적 영상 단독으로 clinical 적용 가능한 surrogate**로 바꾸는 전략의 좋은 reference — 한미암 코호트에서 multi-omics 기반 stratification을 정한 뒤 routine 임상 변수(MRI/CT, H&E patho)만으로 같은 group을 재현할 수 있는지 검증할 때 동일한 ensemble + DNN downstream을 차용 가능하다.

## Connections

- [Ptmanchor Topic Hub](../topics/ptm-correction-and-kinase-signaling-in-cancer-proteomics.md)
- [Cancer Multiomics Literature Hub](../topics/cancer-multiomics-literature.md)
- [Biomarkers and Response Models](../concepts/biomarkers-and-response-models.md)
- [Cancer Immunity Cycle and Set Point](../concepts/cancer-immunity-cycle-and-set-point.md)
- [Stromal and Myeloid Barriers to Immunotherapy](../concepts/stromal-and-myeloid-barriers-to-immunotherapy.md)

## Sources

- Local PDF: `raw/inbox/papers/liu-2025-multimodal-fusion-radio-pathology-proteogenomics-identify.pdf`
- PubMed: <https://pubmed.ncbi.nlm.nih.gov/40222975/>
- DOI: <https://doi.org/10.1038/s41467-025-58675-9>
- PMC: <https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11994800/>
- Code/pipeline: <https://github.com/Zaoqu-Liu/MOFS>
- ICB validation dataset: SRA <https://www.ncbi.nlm.nih.gov/sra/?term=PRJNA482620>
