---
title: "Pan-cancer proteogenomics characterization of tumor immunity"
authors:
  - "Petralia"
  - "Ma"
  - "Yaron"
year: 2024
journal: "Cell"
doi: "10.1016/j.cell.2024.01.027"
pmid: "38359819"
pmcid: "PMC10988632"
paper_kind: pan-cancer-proteogenomic-immunity
cancer_types:
  - pan-cancer
  - breast-cancer
  - clear-cell-renal-cell-carcinoma
  - colon-cancer
  - glioblastoma
  - head-and-neck-squamous-cell-carcinoma
  - lung-squamous-cell-carcinoma
  - lung-adenocarcinoma
  - ovarian-cancer
  - pancreatic-ductal-adenocarcinoma
  - uterine-cancer
modalities:
  - whole-genome-sequencing
  - rna-seq
  - dna-methylation
  - global-proteomics
  - phosphoproteomics
  - histopathology
  - deconvolution
themes:
  - tumor-immunity
  - immune-evasion
  - immune-subtypes
  - kinase-activity
  - immunotherapy-response
  - tumor-microenvironment
tags:
  - cancer-multiomics
  - drug-response
  - immune-evasion
  - proteogenomics
  - phosphoproteomics
  - kinase-signaling
corpus_role: immune-resistance-proteogenomic-context
ingest_status: full-text-read
ingested_on: 2026-05-13
pdf: "raw/inbox/papers/petralia-2024-pan-cancer-proteogenomics-characterization-tumor-immunity.pdf"
---
# Pan-Cancer Proteogenomics Characterization of Tumor Immunity

Petralia et al. use harmonized CPTAC pan-cancer proteogenomic data to define seven tumor-immune subtypes and connect them to DNA alteration, methylation, proteome, phosphoproteome, kinase activity, histopathology, and an external immunotherapy-response cohort. For the drug-response POC, this is best used as immune-resistance and tumor-microenvironment context rather than as a direct drug-response training cohort.

## Full-Text Read Status

- Status: `full-text-read` on 2026-05-13.
- Local PDF identity verified against title, Cell 2024 journal metadata, DOI `10.1016/j.cell.2024.01.027`, and 51-page local PDF.
- Evidence boundary: all scientific claims below come from the local PDF `raw/inbox/papers/petralia-2024-pan-cancer-proteogenomics-characterization-tumor-immunity.pdf`.

## Key Points

- The study analyzes 1,056 treatment-naive tumors from ten CPTAC cancer types: breast cancer, clear-cell renal cell carcinoma, colon cancer, glioblastoma, HNSCC, lung squamous cell carcinoma, lung adenocarcinoma, ovarian cancer, PDAC, and uterine cancer.
- Matched multi-omics layers include WGS, RNA-seq, DNA methylation, quantitative global proteomics, phosphoproteomics, and H&E histopathology. Proteomics and phosphoproteomics were harmonized with a University of Michigan pipeline using MSFragger, Philosopher, and TMT-Integrator, followed by reference-intensity centering, outlier TMT multiplex removal, selected ComBat correction, DreamAI imputation, and BCM phosphosite reannotation.
- BayesDeBulk integrates matched RNA and proteome data to estimate tumor, immune, stromal, and cell-type fractions. The paper uses 10,000 MCMC iterations with 1,000 burn-in iterations.
- Seven immune subtypes are reported: `CD8+/IFNG+`, `eosinophils/endothelial`, `fibroblast/TGF-beta`, `CCRCC/endothelial`, `brain/neuro`, `CD8-/IFNG+`, and `CD8-/IFNG-`.
- The `CD8+/IFNG+` subtype appears across all ten cancers, has T-cell/IFN/TCR signaling, and predicts better progression-free survival in the OAK atezolizumab arm, but not in the docetaxel chemotherapy arm.
- The `CD8-/IFNG+` subtype shows strong IFNG signaling despite low CD8 and B-cell infiltration, making it a useful immune-evasion example where pathway activity and cell infiltration disagree.
- Cold/proliferative subtypes show CDK1/CDK2 activation, while CD8+/IFNG+ tumors show MAPKAPK, IKK-beta, TBK1, PI3K-AKT-mTOR, LYN, HCK, and other Src-family kinase signals.
- DNA alteration associations include STK11 with `CD8-/IFNG+`, BAP1 and CASP8 with `CD8+/IFNG+`, AXIN1 with macrophage/fibroblast-TGF-beta phenotypes, and KEAP1/NFE2L2 with lower IFNG/endothelial/CD8 T-cell phenotypes and higher wound-healing features.
- Copy-number associations nominate chromosome 3p and 9p21 as immune-relevant loci. The paper highlights 9p21 loss involving CDKN2A/B and MTAP as linked to a wound-healing/proliferative immune-cold state.
- Cell-type-specific phosphosite deconvolution nominates FYN/LYN/LCK as lower in cold tumor cells versus hot tumor cells and immune/stromal cells across several cancers, while PTK2/FAK is higher in hot tumor cells and is discussed as a possible immunotherapy-combination target, especially in lung squamous cell carcinoma.

## Cohort and Data Design

- Sample count by tumor type: BC 113, CCRCC 103, CO 96, GBM 99, HNSCC 110, LSCC 108, LUAD 110, OV 82, PDAC 140, and UCEC 95.
- Proteomic data are drawn from CPTAC pan-cancer harmonized resources. The paper points to PDC for raw proteomics, GDC for raw genomics/transcriptomics, controlled-access processed genomics via CDS/dbGaP `phs001287.v16.p6`, and processed uncontrolled CPTAC pan-cancer data.
- The paper reports no single new protein or phosphosite count as a discovery experiment; it is a harmonized pan-cancer reanalysis. It should be represented as a compendium/context paper rather than a single acquisition row in identification-count plots.

## Immune Subtypes

- `CD8+/IFNG+`: high CD8 T cells, IFN signaling, TCR signaling, and broad pan-cancer representation. In OAK validation, this subtype aligns with atezolizumab benefit.
- `eosinophils/endothelial`: enriched in PDAC, LUAD, and LSCC, with eosinophilic and endothelial features.
- `fibroblast/TGF-beta`: enriched for fibroblasts, TGF-beta, EMT, focal adhesion, and proteomics-only hypoxia upregulation; enriched in smokers.
- `CCRCC/endothelial`: predominant in CCRCC, with mast/endothelial/focal-adhesion features and low T-cell signal; validated in an independent CCRCC cohort of 112.
- `brain/neuro`: glioblastoma/neuron-associated subtype with OXPHOS and pyruvate features.
- `CD8-/IFNG+`: IFNG-active but low CD8/B infiltration; enriched in East Asian versus European patients in this cohort.
- `CD8-/IFNG-`: lowest immune/stromal signal, enriched for cell cycle, DNA repair, MYC, and proteomics-only PPARA elevation.

## Immunotherapy Response Context

- The external OAK validation uses pretreatment tumor RNA-seq from the phase III NSCLC OAK trial.
- A model trained on CPTAC RNA classified 75 of 344 immunotherapy-arm patients as `CD8+/IFNG+`; those patients had significantly better PFS with atezolizumab.
- The same subtype association was not observed in the independent docetaxel chemotherapy arm of 355 patients.
- This supports using the `CD8+/IFNG+` state as an immunotherapy-specific context feature, not a generic chemotherapy-response marker.

## Genomic and Epigenomic Immune Associations

- Across 470 frequently mutated cancer genes, 102 genes associate with at least one immune phenotype.
- STK11 mutation associates with `CD8-/IFNG+`, with reduced STK11 RNA/protein in LUAD and reduced STK11 protein in the subtype.
- BAP1 and CASP8 mutations associate with `CD8+/IFNG+`; CASP8 RNA/protein are elevated in both IFNG-positive immune subtypes.
- KEAP1/NFE2L2 mutations are negatively associated with IFNG, endothelial, and CD8 T-cell phenotypes and positively associated with wound-healing features.
- MSI-high colon cancer associates with higher T-cell and myeloid infiltration, whereas the same signal is not observed in UCEC in this analysis.
- Smoking-related methylation mediation analysis across HNSCC, LSCC, and LUAD identifies 69 significant mediation effects among 160 DNAm genes, with PYCR1 highlighted as linked to smoking signature and immune subtype differences.

## Phosphoproteome and Kinase Findings

- The paper uses Kinase Library for serine/threonine kinase specificity and KEA3 for additional kinase inference, including tyrosine kinases.
- `CD8+/IFNG+` phosphosites are enriched for MAPKAPK, IKK-beta, and TBK1; KEA3 nominates LYN, HCK, and other Src-family kinases.
- `CD8-/IFNG-` and `CD8-/IFNG+` show CDK1/CDK2 activation; KEA3 also nominates CDK1-6 across multiple tumor types.
- Kinase-TF analysis links STAT1, STAT5A, and CEBPB activity positively with LYN/SYK and negatively with a MYO3B plus PDK1/3/4 module. L1000 CRISPR knockout signatures support the idea that PDK1/3/4 and MYO3B can suppress innate immune gene programs overlapping CEBPB targets.
- Cell-type-specific phosphosite deconvolution separates hot and cold tumor cells from immune/stromal compartments. Across at least eight tumor types, 33 kinases have consistent activation patterns.
- PTK2/FAK is higher in hot tumor cells, with LUAD and LSCC emphasized. In LSCC, the paper links PTK2/FAK activity to prior evidence for Treg recruitment and CD8 exhaustion, making it a hypothesis for immunotherapy combination rather than a proven clinical response marker in this dataset.

## Histopathology Findings

- CNN models trained on H&E slides distinguish hot and cold immune phenotypes. Pan-cancer models often outperform tissue-specific models.
- Multi-subtype model AUC values reported in the paper include 0.80 for `CD8+/IFNG+`, 0.72 for `eosinophils/endothelial`, 0.70 for `CD8-/IFNG-`, 0.66 for `fibroblast/TGF-beta`, and 0.62 for `CD8-/IFNG+`.
- Neoplastic cell area, axis length, diameter, and perimeter are inversely correlated with cytokine pathway activity and hot immune labels.

## Relevance to Drug-Response POC

- Use this paper for the immune-resistance branch of a global proteome/phosphoproteome/SNV POC: it shows how tumor immune state can be defined by cell composition, pathway activity, DNA alteration, protein abundance, and phosphoproteome-derived kinase activity.
- The OAK validation gives a clean treatment-specific contrast: `CD8+/IFNG+` predicts atezolizumab PFS benefit but not docetaxel benefit.
- The `CD8-/IFNG+` subtype is a strong example of why cell infiltration and pathway activation should not be collapsed into one immune score.
- The paper supports an analysis ladder where SNV features such as STK11/KEAP1/BAP1/CASP8/9p21 are compared against proteome/phosphoproteome immune-state features.
- For phosphoproteome interpretation, it suggests testing whether cold/proliferative CDK activity, hot-immune TBK1/IKK/MAPKAPK/Src-family activity, or PTK2/FAK tumor-cell activity adds signal beyond mutation status and global protein abundance.

## Limitations

- The CPTAC pan-cancer cohort lacks detailed treatment information, so survival associations are not equivalent to direct treatment-response modeling.
- Immune infiltration is a spectrum; seven discrete subtypes are useful but not exhaustive.
- Bulk phosphoproteomics mixes tumor, immune, and stromal signals. The paper uses deconvolution and scRNA-seq pseudo-bulk validation, but scRNA-seq validates transcript patterns rather than direct kinase activity.
- Kinase Library covers serine/threonine kinase specificity; KEA3 is used to broaden inference, but targeted phosphoproteomics would be needed for some low-abundance or ambiguous PTM signals.
- Antigen activity and immune subtype interactions are identified as a future direction rather than fully resolved in this paper.

## Connections

- [Drug Response Proof-of-Concept with Global Proteome, Phosphoproteome, and Somatic SNV](../analyses/drug-response-poc-global-phospho-somatic-snv.md)
- [Drug Response Phospho-Global 100-PDF Bulk Ingest](../analyses/drug-response-phospho-global-100-bulk-ingest.md)
- [Drug Response Phospho-Global Proteomics Corpus Queue](../analyses/drug-response-phospho-global-100-corpus-queue.md)
- [Cancer Multiomics Proteogenomic Atlas](../topics/cancer-multiomics-literature.md)
- [Immunotherapy Resistance and Immune Evasion](../topics/immunotherapy-resistance-and-immune-evasion.md)
- [PTM Correction and Kinase Signaling in Cancer Proteomics](../topics/ptm-correction-and-kinase-signaling-in-cancer-proteomics.md)
- Cancer Multiomics summary: [Petralia 2024 - Pan-Cancer Proteogenomics of Tumor Immunity](../analyses/cancer-multiomics-literature/petralia-2024-pan-cancer-tumor-immunity.md)

## Sources

- Local PDF: `raw/inbox/papers/petralia-2024-pan-cancer-proteogenomics-characterization-tumor-immunity.pdf`
