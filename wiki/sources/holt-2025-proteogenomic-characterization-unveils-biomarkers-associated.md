---
title: "Proteogenomic characterization unveils biomarkers associated with chemoresistance in muscle-invasive bladder cancer"
authors:
  - Holt
  - Dou
  - Young
year: 2025
journal: "Cell Reports Medicine"
doi: "10.1016/j.xcrm.2025.102255"
pmid: "40749681"
pmcid: "PMC12432383"
paper_kind: proteogenomic
cancer_types:
  - muscle-invasive-bladder-cancer
  - urothelial-carcinoma
modalities:
  - WES
  - CNV
  - RNA-seq
  - TMT-proteomics
  - TMT-phosphoproteomics
  - SEPepQuant
  - PRM
themes:
  - chemoresistance
  - neoadjuvant-chemotherapy
  - cisplatin-response
  - proteogenomics
  - phosphoproteomics
  - antibody-drug-conjugate-targets
  - isoform-proteomics
tags:
  - drug-response
  - bladder-cancer
  - proteomics
  - phosphoproteomics
  - chemoresistance
  - pmid-40749681
pdf: "raw/inbox/papers/holt-2025-proteogenomic-characterization-unveils-biomarkers-associated.pdf"
topic: cancer-multiomics-drug-response
batch_ingest_status: pdf-text-extracted
batch_ingested_on: 2026-05-13
ingest_status: full-text-read
ingested_on: 2026-05-13
---
# Proteogenomic Characterization Unveils Biomarkers Associated with Chemoresistance in Muscle-Invasive Bladder Cancer

Holt et al. profile chemotherapy-sensitive and -resistant muscle-invasive bladder cancer with genomics, RNA-seq, TMT proteomics, phosphoproteomics, protein-isoform analysis, and matched pre/post-treatment comparisons, showing that several resistance and sensitivity signals are visible mainly at protein or PTM level.

## Full PDF Deep-Dive Status

- Status: `full-text-read` on 2026-05-13.
- Local PDF: `raw/inbox/papers/holt-2025-proteogenomic-characterization-unveils-biomarkers-associated.pdf`.
- PDF identity checked against title, author, journal, DOI, and 26-page PDF metadata.
- Earlier `pdf-text-extracted` batch snippets are superseded by this curated source page.

## Key Points

- The study started from 143 MIBC tissues and selected a proteogenomic cohort after tumor purity, clinical-history, pathologic-response, and proteomics QC. The final analysis included 57 tissues from 45 patients with proteogenomic data, plus 8 patients with genomic data only. The article summary describes 46 pre- and 14 post-treatment tumors, while the Results section describes 45 pre-chemotherapy and 12 post-chemotherapy tissues after final filtering.
- Chemotherapy sensitivity was defined as pathologic downstaging to pT1N0 or less; resistance was residual pT2-4N0 disease, any node-positive residual disease, or metastatic progression. Among 57 proteogenomic tissues, 22 were sensitive and 35 resistant.
- Omics scale: **11,596 gene products** from 206,856 peptides, **27,090 transcripts**, and **11,799 quantified phosphosites** (9,143 serine, 2,266 threonine, 390 tyrosine). Detected proteins included 425 kinases, 316 DNA-binding transcription factors, and 6 ADC targets.
- Chemoresistance was significantly associated with overall survival. The cohort had bladder-cancer-like mutation and CNV patterns, but somatic DDR genes and germline mutations were not significantly associated with chemoresistance.
- APOBEC-related SBS2 was enriched in chemotherapy-sensitive tumors (p = 9.70e-3), SBS13 trended similarly, while SBS5 was enriched in resistant tumors (p = 6.63e-3).
- Proteome/phosphoproteome NMF of 42 pretreatment samples generated four clusters. Clusters 1 and 2 were enriched for chemotherapy-sensitive patients, while clusters 3 and 4 were enriched for resistant patients.
- Sensitive tumors showed protein-level G2M checkpoint and DNA-repair hallmarks without a matching enrichment of DNA-repair gene mutations, reinforcing that mutation-only response markers miss functional repair-state signals.
- Resistant tumors showed EMT, myogenesis, angiogenesis, KRAS signaling, WNT/beta-catenin, hypoxia, and apoptosis programs. Several resistance-associated genes were protein-only or stronger at protein level than RNA level.
- GSK3B-S9 phosphorylation was significantly higher in chemotherapy-sensitive tumors while total GSK3B protein was not significantly changed. Since S9 is inhibitory, the paper interprets this as lower GSK3B activity in sensitive tumors and nominates GSK3B activity as a resistance mechanism.
- SEPepQuant protein-isoform analysis found partially discriminative BRD2, RHOT2, and ATAD1 peptide groups elevated in sensitive tumors; ATAD1 isoform-level signal was not visible at gene level. A RAF-family shared peptide group was also elevated in sensitive tumors and validated with targeted SIL-PRM.
- ADC target analysis found TROP-2 and NECTIN-4 positively correlated, PD-L1 weakly negatively correlated with TROP-2 and NECTIN-4, and F3 correlated with PD-L1. EGFR showed a bimodal distribution with high EGFR enriched in resistant basal-squamous tumors.
- Matched pre/post-treatment tumors mostly remained similar but showed some subtype switching. Post-treatment samples upregulated lysosomal trafficking / ATPase genes, interferon signaling, and MYC targets; RAF1-S641 and GSK3B-S9 phosphorylation were significantly decreased after treatment.
- The authors propose subtype-aware therapeutic hypotheses: pan-resistance GSK3B/EMT targeting with elraglusib or NP137; luminal papillary TROP-2/NECTIN-4 ADC strategies; luminal infiltrated EMT/ILK targeting; basal-squamous STAT3 and F3/PD-L1 strategies.

## Detailed Evidence

### Cohort and Response Definition

- Patients had muscle-invasive urothelial bladder cancer undergoing cisplatin-based neoadjuvant chemotherapy with M-VAC or gemcitabine/cisplatin and radical cystectomy or radiation therapy.
- Sensitivity was pathologic downstaging to <=T1N0. Resistance was residual muscle-invasive disease, any node-positive residual disease, or metastatic progression.
- Pre-treatment sample analyses often use 42 samples after additional filtering, especially in the NMF clustering and ADC-target correlation figures.
- Overall survival was significantly associated with chemoresistance.

### Genomics and Proteogenomic Context

- Top mutated genes included TP53, KDM6A, ERBB2, and CSMD3 with frequencies similar to prior cohorts.
- CNV focal alterations such as 1q21.3, 6p22.3, 8q22.3 amplification, and 9p21.3 deletion matched known bladder cancer patterns. Candidate CNV drivers were enriched in PI3K/AKT, MYC, E2F, and protein-secretion/proliferative pathways.
- The median gene-wise Spearman RNA-protein correlation was 0.485. Protein data outperformed RNA data for coexpression-based gene-function prediction.

### Chemoresistance Programs

- NMF clusters from proteome/phosphoproteome recapitulated luminal/basal RNA-based subtype biology, but subtypes did not fully explain response because sensitive and resistant cases existed within subtypes.
- Protein and RNA comparisons showed both concordant and discordant response-associated genes. Protein-only signals included EPHA7, LANCL3, SFRP1, and several DNA-damage-repair-related genes.
- Resistant tumors had stronger EMT/myogenesis and microenvironment-associated signals; active mast cell fraction was higher in resistant samples.
- Sensitive tumors had G2M and DNA-repair hallmarks at protein level. This is important because DDR mutations themselves were not significantly enriched in response.
- WNT signaling and KRAS signaling were associated with resistance only at proteomics level.

### Phosphoproteomics and Isoform-Level Features

- GSK3B-S9 phosphorylation was higher in sensitive tumors with no significant change in total GSK3B. The authors propose that active GSK3B contributes to resistance, making GSK3B inhibition a candidate strategy.
- SEPepQuant identified ATAD1_SEPEP.3_PD, BRD2, and RHOT2 peptide groups elevated in sensitive tumors without gene-level elevation.
- The ATAD1 peptide group lacks mitochondrial localization and transmembrane features in the inferred isoform, suggesting proteolytic or isoform-level regulation not captured by mRNA alone.
- RAF-family shared peptides, especially SEPEP 3148_MG across ARAF/BRAF/RAF1, were elevated in sensitive tumors and were more significant than individual RAF proteins. Targeted SIL-PRM of RAF1 and BRAF supported co-expression and elevation in sensitive samples.
- Post-treatment samples showed decreased inhibitory RAF1-S641 and GSK3B-S9 phosphorylation, and increased ILK-S232 phosphorylation.

### Therapeutic Targets and ADC Context

- FDA-approved ADC targets had heterogeneous relationships: TROP-2 and NECTIN-4 were positively correlated; PD-L1 was weakly negatively correlated with TROP-2 and NECTIN-4; F3 correlated with PD-L1 and was inversely related to ERBB2.
- NECTIN-4 was relatively stable pre/post-treatment, while TROP-2 changed unpredictably across individual patients.
- Neuronal subtype tumors lacked high expression of ADC targets, while basal-squamous tumors had elevated PD-L1, EGFR, and F3.
- DepMap-guided prioritization nominated actionable resistant-associated targets, including COL1A1, PRKCA, PDGFRB, and ILK depending on subtype comparison and dependency context.

## Relevance to Drug-Response POC

- This paper is a useful template when the user's genomics layer is somatic SNV only: DDR mutations did not explain chemoresistance, but DNA-repair and G2M response state appeared at protein level.
- The POC should therefore separate `mutation in pathway` from `pathway activity at protein/phospho level`. Holt 2025 shows these can disagree in a clinically meaningful way.
- Protein-level WNT/KRAS/hypoxia/apoptosis and phospho-level GSK3B-S9 are good examples of signals that would be missed or diluted by RNA/SNV-only analysis.
- For a manuscript figure, Holt suggests a strong comparison: DDR mutation status vs DNA-repair protein-pathway score vs GSK3B phosphosite/activity vs response label.
- SEPepQuant/RAF and ATAD1 are a reminder that global proteome can be informative below the gene level. If the user's pipeline can preserve peptide/protein-group information, isoform/domain-level response markers may be worth an exploratory supplement.
- The ADC-target section is useful for a translational add-on: response and resistance states can be orthogonal to target expression, so combination therapy hypotheses should consider both response biology and target abundance.

## Limitations and Caveats

- The main pretreatment statistical analyses are small (often 42 samples), limiting rare subtype detection and validation power.
- Bulk tumors have stromal and muscle contamination risk, especially for MIBC myogenesis signatures, although the study selected high-tumor-content samples and repeated some checks in high-purity subsets.
- Several proposed targets and combinations are hypotheses rather than direct functional validations in this paper.
- RAF domain quantification was validated by targeted MS on the same peptides; it is orthogonal technically but not fully independent biologically.
- The authors are developing PDX/organoid validation and an expanded cohort, but those results are not included here.

## Data Availability

- Proteomics data: PRIDE `PXD060290`.
- RNA-seq and WES data: dbGaP `phs004049.v1.p1`.
- Somatic mutations: Data S1.
- The paper does not report original code.

## Connections

- [Drug Response Proof-of-Concept with Global Proteome, Phosphoproteome, and Somatic SNV](../analyses/drug-response-poc-global-phospho-somatic-snv.md)
- [Drug Response Phospho-Global Proteomics Corpus Queue](../analyses/drug-response-phospho-global-100-corpus-queue.md)
- [Drug Response Phospho-Global 100-PDF Bulk Ingest](../analyses/drug-response-phospho-global-100-bulk-ingest.md)
- [Cancer Multiomics Literature Monitor](../topics/cancer-multiomics-literature.md)
- [Multiomics Proteomics PTM Identification](../topics/multiomics-proteomics-ptm-identification.md)

## Open Questions

- Which response-associated protein-only signals remain significant after explicit adjustment for tumor purity, muscle content, and subtype?
- Can GSK3B-S9 / RAF-family peptide response signals be validated in independent MIBC proteomic cohorts or patient-derived models?
- Are ADC target protein abundances predictive of actual ADC response in preclinical MIBC models, or only of target availability?
- Should future POC modeling include peptide-domain features or keep them as hypothesis-generating supplements?

## Sources

- Local PDF: `raw/inbox/papers/holt-2025-proteogenomic-characterization-unveils-biomarkers-associated.pdf`
- DOI: <https://doi.org/10.1016/j.xcrm.2025.102255>
- PubMed: <https://pubmed.ncbi.nlm.nih.gov/40749681/>
- PMCID recorded in source metadata: `PMC12432383`
