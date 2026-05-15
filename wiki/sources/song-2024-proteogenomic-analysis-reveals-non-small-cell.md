---
title: "Proteogenomic analysis reveals non-small cell lung cancer subtypes predicting chromosome instability, and tumor microenvironment"
authors:
  - Song
  - Choi
  - Kim
year: 2024
journal: "Nature Communications"
doi: "10.1038/s41467-024-54434-4"
pmid: "39580524"
pmcid: "PMC11585665"
paper_kind: proteogenomic-resource
cancer_types:
  - non-small-cell-lung-cancer
  - lung-adenocarcinoma
  - lung-squamous-cell-carcinoma
modalities:
  - WES
  - RNA-seq
  - TMT-proteomics
  - phosphoproteomics
  - acetylomics
  - neoantigen-analysis
  - histopathology
themes:
  - molecular-subtypes
  - adjuvant-therapy
  - tumor-microenvironment
  - chromosome-instability
  - whole-genome-doubling
  - kinase-signaling
  - immunogenicity
tags:
  - source
  - cancer-multiomics
  - non-small-cell-lung-cancer
  - proteogenomics
  - phosphoproteomics
  - acetylomics
  - drug-response
  - pmid-39580524
pdf: "raw/inbox/papers/song-2024-proteogenomic-analysis-reveals-non-small-cell.pdf"
batch_ingest_status: pdf-text-extracted
batch_ingested_on: 2026-05-13
ingest_status: full-text-read
ingested_on: 2026-05-13
---
# Proteogenomic Analysis Reveals Non-Small Cell Lung Cancer Subtypes Predicting Chromosome Instability, and Tumor Microenvironment

Song et al. define five proteogenomic NSCLC subtypes in a Korean surgical cohort and connect phosphoproteome-heavy subtype structure to whole-genome doubling, PI3K-Akt/hypoxia/metastatic biology, immune landscape, cryptic MAPs, and adjuvant therapy benefit.

## Full PDF Deep-Dive Status

- Status: `full-text-read` on 2026-05-13.
- Local PDF: `raw/inbox/papers/song-2024-proteogenomic-analysis-reveals-non-small-cell.pdf`.
- PDF identity checked against title, author, journal, DOI, and 25-page PDF metadata.
- Corpus role: major NSCLC proteogenomic subtype/resource paper with adjuvant therapy signal, not a prospective drug-response trial.

## Key Points

- Discovery cohort: **229 Korean NSCLC patients** from Asan Medical Center, Seoul, with surgery samples collected between 2010 and 2019. Histologies included 139 LUAD, 63 LSCC, and 27 other NSCLC tumors.
- Adjuvant therapy was given to **110/229 patients (48%)**: 59 chemotherapy, 16 radiation therapy, and 35 chemoradiation. Recurrence was observed in 54% of adjuvant-treated patients.
- Omics scale: WES for 228 matched tumor/NAT pairs plus one tumor-only case; bulk RNA-seq for 205 tumors and 85 matched NATs; TMT proteomics for 229 tumors and 26 NATs. Across >=30% of samples, the study quantified **10,788 proteins**, **40,738 phosphosites**, and **5,975 acetylation sites**.
- NMF on proteome, phosphoproteome, and acetylome identified five NSCLC subtypes: Subtype 1 metabolic, Subtype 2 alveolar-like, Subtype 3 proliferative, Subtype 4 hypoxic, and Subtype 5 immunogenic.
- Phosphoproteome was the most informative layer for subtype definition, contributing **80% (911/1,134)** of subtype features.
- Subtype 4 was a poor-prognosis, metastasis-rich subtype independent of histologic type. It was characterized by hypoxia, PI3K-Akt signaling, desmoplastic stromal components, and phospho-kinase features.
- Subtype 4-specific kinase analysis nominated **CSNK2A1** (FDR = 2.3e-7) and **GSK3B** (FDR = 1.9e-2). Poor-prognosis phosphosites included **SLK S347** and **LRRFIP1 S581**, both reproduced in combined CPTAC analyses.
- Subtype 3 was a highly proliferative, WGD-rich subtype: **75% (39/52)** of Subtype 3 patients had WGD. XPO1 was elevated, and patient-derived lung organoid experiments suggested higher selinexor sensitivity in WGD-positive LSCC organoids.
- Immune clustering defined hot-tumor-enriched (HTE), cold-tumor-enriched (CTE), and NAT-enriched immune states. HTE status was the most favorable immune factor for survival; CD8+ T cells, CD4+ T cells, B cells, and NK cells correlated with better prognosis, while epithelial-cell/neutrophil enrichment correlated negatively.
- Subtype 5 was immunogenic, with HTE status, active antigen processing/presentation, TNF-alpha/NF-kB activity, and high TILs, but also immunosuppressive Tregs/neutrophils and low cryptic MAP load.
- Adjuvant chemotherapy or chemoradiation substantially improved survival specifically in **Subtype 5**; other subtypes did not show substantial adjuvant therapy survival improvement.

## Detailed Evidence

### Cohort and Omics

- Tumors covered early to locally advanced disease: approximately 40% were stage IIIA/IIIB/IVA, and 51% had lymph node metastasis at surgical pathology.
- WES detected 33,301 somatic small mutations and 470,836 copy-number alterations; average TMB was 2.7.
- RNA-seq generated 60,688 transcripts, with 20,088 transcripts retained after low-count filtering.
- Proteome/PTM values were quantified as log2 ratios to common reference samples.

### Five Multiomics Subtypes

- Subtype 1 metabolic: mainly LUAD females, EGFR and TP53 mutations, frequent WGD, CDKN2A copy loss, oxidative phosphorylation, mitochondrial matrix, and cellular respiration.
- Subtype 2 alveolar-like: mainly LUAD with EGFR mutations but without WGD, low TP53 mutation frequency, low TMB, and relatively favorable histology.
- Subtype 3 proliferative: LSCC-enriched and WGD-rich, with cell-cycle and proliferative biology. XPO1 expression and selinexor sensitivity made it a therapy-hypothesis subtype.
- Subtype 4 hypoxic: distinct across histologies, phosphoproteome-heavy, metastatic/poor outcome, hypoxia/PI3K-Akt/HIF-1/VEGF/NF-kB-associated.
- Subtype 5 immunogenic: KRAS-enriched inflammatory subtype with immune and TNF-alpha/NF-kB activity and a clinical adjuvant therapy signal.

### Subtype 4 Kinase / Poor-Prognosis Axis

- Most Subtype 4 NMF features were phosphosites (178/186), indicating that phospho-kinase interactions are central to this subtype.
- CSNK2A1 and GSK3B were significantly upregulated by kinase activity inference from phosphoproteomic data.
- SLK S347 phosphorylation was higher in Subtype 4 and associated with poor survival in the Korean cohort and combined CPTAC dataset.
- LRRFIP1 S581 phosphorylation was also higher in Subtype 4 and associated with poor survival; the paper links LRRFIP1 to EMT and Wnt/beta-catenin signaling.
- Subtype 4 overall survival was worse than other Korean-cohort subtypes (log-rank P = 8.4e-3), and among non-metastatic patients remained worse (P = 2.6e-2), suggesting biology beyond stage distribution.

### WGD and Therapy Hypothesis

- Subtype 3 had WGD in 39/52 patients and represented a chromosomally unstable proliferative group.
- XPO1 was upregulated at protein and acetylated-protein levels in the proliferative/WGD subtype.
- Lung organoids from WGD-positive LUAD/LSCC and WGD-negative controls were tested with selinexor. WGD-positive LSCC organoids showed higher selinexor sensitivity, supporting a subtype-specific XPO1 inhibition hypothesis.
- Subtype 1 also had WGD in a subset, but XPO1 expression was not strongly increased and selinexor was less effective, cautioning against treating WGD as a single universal drug biomarker.

### Immune Landscape and Adjuvant Therapy

- The study used single-cell reference datasets, cell-type/pathway immune clustering, histology/TIL patterns, neoantigen candidates, cryptic MAPs, and antigen-processing/presentation machinery to characterize TIME.
- HTE tumors were enriched for CD8/CD4 T cells, Tregs, B cells, NK cells, neutrophils, DCs, monocytes, and macrophages relative to CTE tumors.
- High HTE status and cytotoxic/lymphoid immune cell enrichment were associated with favorable survival. Treg-enriched HTE tumors had worse survival than low-Treg HTE tumors.
- Subtype 5 combined HTE, active APM, TNF-alpha/NF-kB activity, low cryptic MAP load, and high TILs. Survival improved substantially with adjuvant chemotherapy or chemoradiation only in Subtype 5.

## Relevance to Drug-Response POC

- This paper is valuable for a POC where clinical drug response is incomplete or retrospective: it shows how to link multiomic subtype, immune state, and adjuvant treatment benefit.
- The strongest POC lesson is that phosphoproteome can dominate subtype discovery. If the user's phosphoproteome contributes most discriminative features, that should be shown explicitly rather than treated as a secondary annotation layer.
- Subtype 4 provides a kinase-signaling model: PI3K-Akt/hypoxia/CSNK2A1/GSK3B/SLK/LRRFIP1 phosphosites can explain poor outcome beyond histology and stage.
- Subtype 5 provides a therapy-benefit model: adjuvant chemotherapy benefit may be conditional on a hot immune/TIL/APM state rather than universal across NSCLC.
- The selinexor organoid result is a useful cautionary example: WGD alone was not enough; the WGD-positive LSCC/XPO1-high subtype showed more sensitivity than WGD-positive LUAD-like Subtype 1.
- For the user's global proteome + phosphoproteome + somatic SNV data, a useful analysis is to test whether response benefit is concentrated in immune-hot or phospho-defined subtypes, not only in mutation-defined groups.

## Limitations and Caveats

- WGD was inferred from exome sequencing, which is less accurate than WGS.
- Ethnic differences may affect subtype proportions, especially EGFR-positive female LUAD in Subtype 1.
- Adjuvant therapy analyses are retrospective and not randomized within subtype.
- Cryptic MAP confirmation was limited by normal sample availability.
- Selinexor sensitivity needs prospective and broader organoid/model validation.

## Data Availability

- Genomic and transcriptomic raw data: EGA `EGAS50000000592`, dataset `EGAD50000000844`, and KoNA `KAP210028`.
- Raw MS global proteome/phosphoproteome/acetylome: ProteomeXchange `PXD053969`, `PXD053921`, `PXD053903` via jPOST `JPST003210`, `JPST003211`, `JPST003212`.
- Processed proteomic data: K-BDS `KAP240387`, `KAP240391`, `KAP240392`.
- Code repository: `https://github.com/joonan-lab/PDIAMOND-NSCLC`.

## Connections

- [Drug Response Proof-of-Concept with Global Proteome, Phosphoproteome, and Somatic SNV](../analyses/drug-response-poc-global-phospho-somatic-snv.md)
- [Drug Response Phospho-Global Proteomics Corpus Queue](../analyses/drug-response-phospho-global-100-corpus-queue.md)
- [Drug Response Phospho-Global 100-PDF Bulk Ingest](../analyses/drug-response-phospho-global-100-bulk-ingest.md)
- [Cancer Multiomics Literature Monitor](../topics/cancer-multiomics-literature.md)
- [PTM Correction and Kinase Signaling in Cancer Proteomics](../topics/ptm-correction-and-kinase-signaling-in-cancer-proteomics.md)

## Open Questions

- Does the Subtype 5 adjuvant benefit persist after formal adjustment for stage, nodal status, histology, and treatment selection?
- Which phosphoproteome-derived kinase activities remain predictive of outcome in independent Korean or Asian NSCLC cohorts?
- Can the Subtype 4 SLK/LRRFIP1 phosphosite axis be experimentally perturbed in organoids or patient-derived models?
- Would immune checkpoint inhibitor benefit also concentrate in the Subtype 5 HTE/APM state?

## Sources

- Local PDF: `raw/inbox/papers/song-2024-proteogenomic-analysis-reveals-non-small-cell.pdf`
- DOI: <https://doi.org/10.1038/s41467-024-54434-4>
- PubMed: <https://pubmed.ncbi.nlm.nih.gov/39580524/>
- PMCID recorded in source metadata: `PMC11585665`
