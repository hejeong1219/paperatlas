---
title: "Pharmaco-proteogenomic characterization of liver cancer organoids for precision oncology"
authors:
  - Ji
  - Feng
  - Fu
year: 2023
journal: "Science Translational Medicine"
doi: "10.1126/scitranslmed.adg3358"
pmid: "37494474"
pmcid: "PMC10949980"
paper_kind: pharmaco-proteogenomic
cancer_types:
  - hepatocellular-carcinoma
  - intrahepatic-cholangiocarcinoma
  - combined-hepatocellular-cholangiocarcinoma
  - liver-cancer
modalities:
  - patient-derived-organoid
  - drug-screen
  - WES
  - CNV
  - RRBS
  - RNA-seq
  - DIA-proteomics
  - phosphoproteomics
themes:
  - drug-response
  - functional-precision-oncology
  - pharmaco-proteogenomics
  - kinase-signaling
  - drug-combination
  - mTOR-lenvatinib
tags:
  - drug-response
  - proteomics
  - phosphoproteomics
  - cancer-proteomics
  - organoids
  - pmid-37494474
pdf: "raw/inbox/papers/ji-2023-pharmaco-proteogenomic-characterization-liver-cancer-organoids.pdf"
topic: cancer-multiomics-drug-response
batch_ingest_status: pdf-text-extracted
batch_ingested_on: 2026-05-13
ingest_status: full-text-read
ingested_on: 2026-05-13
---
# Pharmaco-proteogenomic Characterization of Liver Cancer Organoids for Precision Oncology

Ji et al. built a patient-derived liver cancer organoid biobank and used matched genomics, methylation, transcriptomics, DIA proteomics, drug screening, and follow-up phosphoproteomics to connect molecular state to drug response and combination therapy.

## Full PDF Deep-Dive Status

- Status: `full-text-read` on 2026-05-13.
- Local PDF: `raw/inbox/papers/ji-2023-pharmaco-proteogenomic-characterization-liver-cancer-organoids.pdf`.
- PDF identity checked against title, journal, DOI, PMID, and page count.
- Earlier `pdf-text-extracted` batch snippets are superseded by this curated source page.

## Key Points

- The LICOB cohort contains **65 patient-derived liver cancer organoids from 57 patients**: 44 HCC organoids, 12 ICC organoids, 4 combined HCC-CCA organoids, and 5 hepatic-biliary organoids. Forty of 65 organoids were HBV positive, and 13 of 65 came from multi-region sampling of the same patients.
- Organoids preserved major parental-tumor molecular features across mutation, CNV, methylation, RNA, and protein layers. Paired organoid-tissue correlations were higher than unpaired correlations for CNV, DNA methylation, mRNA, and protein profiles.
- Consensus clustering across five omics datasets defined four LICOB subtypes: L-ICC, L-PL proliferative, L-LM lipid-metabolism, and L-DM drug-metabolism. Projecting organoid features into CPTAC HCC linked L-PL to the worst survival and L-LM to the best survival, while L-DM had intermediate survival inferior to L-LM.
- L-DM organoids showed a G6PD / pentose-phosphate / glutathione program. G6PD was higher in L-DM, high G6PD associated with worse survival in CPTAC and TCGA HCC, G6PD knockdown reduced L-DM organoid growth, and L-DM organoids were more sensitive to G6PDi-1 than L-LM organoids.
- The paper screened **76 drugs or compounds** in LICOB and derived AUC, IC50, and Emax after serial-dose treatment in 384-well organoid assays.
- Drug response was subtype-associated: L-PL was sensitive to PI3K-AKT-mTOR inhibitors BEZ235 and temsirolimus and to chemotherapy drugs; L-LM and L-DM were generally more sensitive to multi-kinase inhibitors, with L-LM more sensitive to regorafenib and L-DM more sensitive to lenvatinib.
- Elastic-net models using multiomics predicted drug response for each of the 76 drugs. For approved liver cancer TKIs, prediction correlations between predicted and measured AUC were reported as regorafenib R = 0.85, lenvatinib R = 0.75, and sorafenib R = 0.70 in the testing set.
- Lenvatinib resistance was linked to EGFR-TKI-resistance features and, in the predictive model, to higher KRT19 and NDN mRNA plus thromboxane pathway enrichment; it negatively correlated with higher ADH1C, CES1, and VEGF-pathway-related protein abundance.
- A network-based combination algorithm predicted lenvatinib plus temsirolimus. Six-hour perturbation phosphoproteomics quantified **23,754 phosphosites**, showing broader suppression of drug-targeted pathways with the combination than with either single agent.
- Combination validation showed strong in vitro synergy in ICCO10, ICCO2, HCCO3, and HCCO31 organoids. In vivo, lenvatinib plus temsirolimus inhibited HCCO31 xenograft growth more than either drug alone and reduced tumor size in lenvatinib-resistant HCC PDX models.

## Detailed Evidence

### Biobank and Molecular Fidelity

- The study objective was to establish liver cancer organoids and generate pharmaco-proteogenomic information for predictive biomarkers and therapeutic options.
- Multiomics included mutation, CNV, DNA methylation, transcriptomics, and proteomics. The main profiling stack was WES, RRBS, RNA-seq, and label-free DIA proteomics; phosphoproteomic MS data were also generated for the combination experiment.
- Tumor purity estimated from WES approached 100% in organoids and was higher than in corresponding tissues.
- Organoids retained common liver-cancer driver alterations including TP53, KMT2C, RB1, PBRM1, HCC-specific CTNNB1, and ICC-specific KRAS and BAP1 patterns.
- Organoid profiles clustered with TCGA, CPTAC, and paired tissues, whereas liver cancer cell lines were less representative. Metabolic pathways were preserved, while immune/inflammatory signals were reduced, consistent with the absence of tumor microenvironment cells in organoid cultures.

### Multiomic Subtypes

- L-ICC was defined by ICC dominance, RAS signaling, and cell-junction features.
- L-PL was enriched for cell-cycle and MAPK pathways, lower methylation of pluripotency-related genes, higher CD44, and shorter doubling time than other subtypes.
- L-LM carried lipid-metabolism features, including APOB mutations and higher CPS1 / PLA2G2A mRNA.
- L-DM carried drug/xenobiotic and pentose-phosphate metabolism features, including ALB and PLEC mutations and higher UGT1A1 and ALDH1A1 protein abundance.
- L-DM had enhanced NADPH/GSH biology and PPP enzymes PGD, TKT, and TALDO1. The authors proposed a MYC-NRF2-G6PD axis that shifts metabolic flux toward redox defense and nucleotide synthesis.

### Drug Response and Prediction

- The 76-drug screen used 384-well organoid plating, 72-hour recovery, serial drug dilution, another 72-hour treatment, CellTiter-Glo 3D readout, and GRmetrics fitting for AUC, IC50, and Emax.
- Organoids from the same patient had more similar drug responses than organoids from different patients, even though some intrapatient heterogeneity remained.
- HBV-positive organoids were generally more chemotherapy-resistant than HBV-negative organoids.
- Same-target drugs could behave concordantly or discordantly. TOP2 inhibitors doxorubicin and epirubicin were highly concordant, while PARP inhibitors olaparib and talazoparib were only weakly concordant, showing that target-class labels alone were not sufficient.
- Tivantinib sensitivity in L-LM/L-DM was not explained by MET mutation, amplification, or expression. Instead, response was linked to multiomic activation of MET-related function, including HGF, HPN, USP8, DOCK7, and CRKL features.
- Elastic-net regression used 1000 bootstraps and an 8:2 split, with 51 training organoids and 13 testing organoids. Performance was assessed with Pearson or Spearman correlation, cosine similarity, and MSE between predicted and measured AUC.
- Sorafenib sensitivity features included MYEOV hypermethylation, higher EFNA2/TINAG/UPK3A mRNA, and lower IGF1R protein abundance. Sorafenib resistance features were enriched in IGF1/IGF1R, EGFR, FGF11, RAS, ERK, HDAC, and endocytosis pathways.

### Combination Validation

- The combination algorithm connected drugs through pathways where one drug's AUC correlated positively and the other's AUC correlated negatively with pathway activity.
- Temsirolimus ranked as a strong complementary partner for lenvatinib and also for tivantinib.
- The lenvatinib-temsirolimus connection involved EGFR-inhibitor-resistance and TGF-beta signaling pathways, with opposite relationships to lenvatinib and temsirolimus sensitivity.
- After six hours of treatment, phosphoproteomics showed that lenvatinib and temsirolimus each downregulated phosphosites in their targeted pathways, including mTOR, VEGF, and PDGF-related pathways; the combination downregulated nearly all of these phosphosites compared with DMSO.
- Mechanistically, lenvatinib alone slightly reduced MEK/ERK activation but increased AKT phosphorylation. Adding temsirolimus enhanced MEK/ERK inhibition and reversed AKT activation.
- The HCCO31 xenograft combination result was significant versus single agents by two-way ANOVA, P = 1.2e-6. In lenvatinib-resistant HCC PDX models, lenvatinib plus temsirolimus reduced tumor size, P = 2.1e-6.

## Relevance to Drug-Response POC

- This is a strong template for a **functional precision oncology** version of the user's POC: baseline multiomics can nominate response features, but drug-screen or perturbation readouts can validate whether the inferred state is pharmacologically meaningful.
- It supports a model ladder where SNV/CNV, methylation/RNA, global proteome, and phosphoproteome are evaluated as distinct explanatory layers rather than collapsed into one feature set.
- The most useful lesson for a global proteome + phosphoproteome + somatic SNV project is that drug target abundance alone may be insufficient. Pathway-context features, protein-level state, methylation/RNA features, and perturbation phosphosites can explain resistance more directly.
- The combination experiment is especially relevant: phosphoproteomics was used after drug perturbation to show whether the predicted combination actually suppresses bypass signaling. For the user's POC, a small perturbation validation panel could make a response model much more persuasive than prediction metrics alone.
- Caveat for SNV-only datasets: LICOB relies on CNV, methylation, RNA, proteome, and phosphoproteome as well as drug-screen phenotypes. If the user's genomics layer is somatic SNV only, missing CNA/SV/methylation drivers should be labeled explicitly.

## Limitations and Caveats

- Sample size was limited by low liver cancer organoid establishment success.
- Organoids lack the native tumor microenvironment; immune and inflammatory states were reduced relative to tissues.
- Multi-region organoids from the same patient were generally similar but still showed some molecular and drug-response heterogeneity.
- Cell-cycle-targeting drug effects may be underestimated in slow-growing organoids because treatment duration was limited.
- Multiomics response features and proposed combinations need clinical validation before being treated as patient-selection biomarkers.

## Data Availability

- The PDF states that all data are in the paper or Supplementary Materials, with supplemental tables in data file S1 and figure raw data in data file S2.
- WES, RNA-seq, RRBS, proteomics, and phosphoproteomics data are reported as available from the biosino NODE project `OEP003191`.
- Organoids can be requested from the Liver Cancer Institute, Zhongshan Hospital under material-transfer and ethics approval terms.

## Connections

- [Drug Response Proof-of-Concept with Global Proteome, Phosphoproteome, and Somatic SNV](../analyses/drug-response-poc-global-phospho-somatic-snv.md)
- [Drug Response Phospho-Global Proteomics Corpus Queue](../analyses/drug-response-phospho-global-100-corpus-queue.md)
- [Drug Response Phospho-Global 100-PDF Bulk Ingest](../analyses/drug-response-phospho-global-100-bulk-ingest.md)
- [Cancer Multiomics Literature Monitor](../topics/cancer-multiomics-literature.md)
- [PTM Correction and Kinase Signaling in Cancer Proteomics](../topics/ptm-correction-and-kinase-signaling-in-cancer-proteomics.md)

## Open Questions

- Which LICOB data matrices are sufficient for external reanalysis without requesting organoid materials?
- How much of the elastic-net performance comes from proteome/phosphoproteome features versus RNA/methylation/genomics for each individual drug?
- Would temsirolimus-lenvatinib synergy remain robust in immune-competent or microenvironment-preserving models?
- For SNV-only user datasets, what orthogonal assay can best substitute for the missing CNA/methylation layers used by LICOB?

## Sources

- Local PDF: `raw/inbox/papers/ji-2023-pharmaco-proteogenomic-characterization-liver-cancer-organoids.pdf`
- DOI: <https://doi.org/10.1126/scitranslmed.adg3358>
- PubMed: <https://pubmed.ncbi.nlm.nih.gov/37494474/>
- PMCID recorded in source metadata: `PMC10949980`
