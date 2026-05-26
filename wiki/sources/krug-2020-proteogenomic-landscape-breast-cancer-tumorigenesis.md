---
title: "Proteogenomic Landscape of Breast Cancer Tumorigenesis and Targeted Therapy"
authors:
  - "Krug"
  - "Jaehnig"
  - "Satpathy"
year: 2020
journal: "Cell"
doi: "10.1016/j.cell.2020.10.036"
pmid: "33212010"
pmcid: "PMC8077737"
paper_kind: proteogenomic-atlas
cancer_types:
  - breast-cancer
  - triple-negative-breast-cancer
modalities:
  - whole-exome-sequencing
  - copy-number
  - rna-seq
  - global-proteomics
  - phosphoproteomics
  - acetylomics
  - immunohistochemistry
themes:
  - cptac
  - breast-cancer-subtypes
  - erbb2-her2
  - cdk4-6-rb
  - immune-microenvironment
  - kinase-signaling
  - acetyl-metabolism
  - therapeutic-vulnerability
tags:
  - cancer-resistance
  - drug-response
  - ptmanchor
  - proteomics
  - phosphoproteomics
  - acetylomics
  - breast-cancer
pdf: "raw/inbox/papers/krug-2020-proteogenomic-landscape-breast-cancer-tumorigenesis.pdf"
corpus_role: core-proteogenomic-vulnerability
ingest_status: full-text-read
ingested_on: 2026-05-13
---
# Proteogenomic Landscape of Breast Cancer Tumorigenesis and Targeted Therapy

Krug et al. profile prospectively collected, treatment-naive breast tumors under PTM-preserving CPTAC protocols and show how proteome, phosphoproteome, and acetylome layers refine HER2 status, immune-therapy candidacy, Rb/CDK4/6 vulnerability, mutation-to-kinase hypotheses, and subtype-specific metabolism.

## Full-Text Read Status

- Status: `full-text-read` on 2026-05-13.
- Local PDF: `raw/inbox/papers/krug-2020-proteogenomic-landscape-breast-cancer-tumorigenesis.pdf`.
- PDF identity checked against title, author, Cell citation, DOI, and STAR Methods.
- Scope: curated from the local full PDF, including main results, discussion, data availability, and mass-spectrometry methods.

## Key Points

- Cohort: 134 prospectively collected tumors; 125 underwent proteomics; 122 tumors were fully analyzed after RNA-seq exclusions.
- The cohort covers all major PAM50 groups: HER2-enriched 11.5%, basal-like 23.8%, LumA 46.7%, LumB 13.9%, normal-like 4.1%.
- Filtered analysis dataset: 29,647 somatic mutations, 23,692 gene-level copy-number events, 23,121 transcripts, 10,107 proteins, 38,968 phosphorylation sites, and 9,869 acetylation sites.
- STAR Methods report VM-site polishing totals of 63,416 phosphosites and 18,392 acetylsites; 70% of phosphosites and 99% of acetylsites were fully localized.
- Multi-omic NMF across SCNA, mRNA, protein, phosphosite, and acetylsite layers found four clusters: LumA-inclusive, LumB-inclusive, Basal-inclusive, and HER2-inclusive.
- Proteogenomic HER2 status exposed pseudo-ERBB2-positive tumors where ERBB2 was amplified but ERBB2 protein stayed in the non-amplified range, a direct example of why target DNA status must be checked at protein/phosphoprotein level.
- Rb protein/phosphoprotein state improved CDK4/6 inhibitor response interpretation, especially for TNBC, where RB1 wild-type tumors can still lose Rb protein and become less palbociclib-sensitive.
- Immune profiling nominated subsets of luminal tumors with APOBEC/SSBR-defect/immune-checkpoint features for immunotherapy consideration.

## Cohort and Assay Design

- Specimens came from newly diagnosed, untreated breast cancer patients with stage IIA-IIIC disease or core needle biopsy before neoadjuvant therapy.
- Tissue collection prioritized PTM preservation: less than 30 minutes total ischemic time, OCT embedding, central molecular/pathology qualification, and cryopulverization.
- DNA, RNA, and protein were extracted from a single homogenized tumor segment, reducing cross-fragment discordance relative to earlier residual TCGA proteogenomics.
- WES was generated with Nextera Rapid Capture Exome libraries and HiSeq4000 sequencing; RNA-seq used TruSeq stranded libraries.
- Proteomics used TMT10 plexes with nine samples plus a common tumor reference per plex. The common reference was composed from 40 tumors: 9 triple negative, 12 HER2 positive, and 19 estrogen receptor positive specimens.
- Proteome/phosphoproteome/acetylome experiments were organized as 15 tumor TMT10 plexes plus two NAT plexes. The NAT plexes failed quality standards for downstream quantitative analyses.

## Omics Scale and Processing

- The filtered analysis dataset included 10,107 proteins, 38,968 phosphorylation sites, and 9,869 acetylation sites.
- Protein-level FDR after polishing across TMT plexes was reported as less than 0.01% at the protein-group level.
- VM-site polishing yielded 63,416 phosphosites with 0.44% aggregate phosphosite-level FDR and 18,392 acetylsites with 0.57% aggregate acetylsite-level FDR.
- TMT reporter ratios were two-component normalized to center an inferred unregulated component for each sample.
- Acetylsite analysis used protein-abundance residualization for selected metabolism analyses, separating acetylation change from total protein change.
- PTM-SEA used 29,406 fully localized phosphosites after resolving multiply phosphorylated peptides.

## Multi-Omic Subtypes

- NMF LumA-I largely corresponded to PAM50 LumA, hormone receptor positivity, wild-type TP53, and high stromal infiltration.
- NMF Basal-I included nearly all PAM50 basal tumors and was enriched for TP53 mutation, hormone receptor negativity, immune/stemness/CIN scores, E2F, and G2/M.
- NMF LumB-I contained all but one PAM50 LumB tumor plus a subset of PAM50 LumA samples; METABRIC projection showed those LumA samples had intermediate outcomes between remaining LumA and LumB.
- NMF HER2-I was heterogeneous and included tumors from all PAM50 subtypes. HER2-I-defining features included ER/sterol/cholesterol biology and immune features, not only the ERBB2 amplicon.

## Mutation-to-Kinase Phosphoproteomics

- Phosphorylated kinase outliers were identified with BlackSheep and used as kinase activation surrogates.
- Previously seen subtype-enriched kinases were reproduced: PRKDC, MAP4K4, and SPEG in Basal-I; ERBB2 and CDK12 in HER2-I; DCLK1 in LumA-I.
- Mutation-associated phosphokinase outliers included TNIK in ARID1A-mutant tumors, RIPK3 in MAP3K1-mutant tumors, MAST4/DCLK1 in GATA3-mutant tumors, and SLK/LATS1 in AKT-mutant tumors.
- These are hypothesis-generating kinase vulnerabilities, not direct response markers, but they are useful examples for a somatic-SNV-to-phospho-signaling POC.

## ERBB2/HER2 Proteogenomic Status

- The paper explicitly follows up earlier neoadjuvant anti-ERBB2 biopsy work where two treatment-resistant ERBB2-amplified cases had pseudo-ERBB2-positive status: low ERBB2 protein despite ERBB2 amplification.
- In the current prospective cohort, 15 tumors were classified as ERBB2 proteogenomically positive (PG+).
- Pseudo-ERBB2 positivity appeared in two of 17 ERBB2-amplified cases in this cohort and one of 16 in the retrospective cohort.
- Some pseudo-ERBB2-positive cases showed TOP2A amplification and protein overexpression without ERBB2 protein overexpression, suggesting an alternative chromosome 17 amplicon driver.
- PAM50 HER2E and ERBB2 PG+ did not perfectly align: only seven of 15 ERBB2 PG+ samples were HER2E, and seven HER2E samples were not ERBB2 PG+.
- HER2E/ERBB2 PG- samples showed lower ERBB2 phosphopeptides but elevated phosphorylation of other ERBB family and MAPK signaling proteins, nominating alternative ERBB/MAPK drivers.

## Immune Microenvironment

- RNA deconvolution and protein-level immune modulator signatures revealed immune heterogeneity across all PAM50 subtypes.
- PD1, PD-L1, and CTLA4 were profiled at RNA/protein/phosphoprotein levels where available; CD3 IHC validated active immune microenvironment estimates.
- LumA tumors with high CIBERSORT immune scores had stromal/fibroblast/mast/endothelial/neutrophil features but lower acquired immune response hallmarks than other subtypes.
- LumB, basal, and some HER2E/luminal tumors showed features consistent with acquired immunity, supporting the idea that immunotherapy should not be restricted to TNBC alone.
- APOBEC3G protein correlated with PD-L1 and CIBERSORT immune score; six tumors were APOBEC-enriched, including luminal cases.
- In luminal tumors, lower nucleotide-excision repair and broader single-strand-break repair protein scores correlated with immune features and PD-L1, suggesting a link between DNA repair loss, endocrine resistance biology, and immune-checkpoint candidacy.

## Rb and CDK4/6 Inhibitor Logic

- The paper compares HR+/ERBB2- and TNBC tumors using proliferation score, Cyclin/CDK features, Rb RNA/protein/phosphoprotein, PTM-SEA kinase activity, and palbociclib sensitivity in external breast cancer cell lines.
- In HR+/ERBB2- tumors, CDK4/6 activity correlated with proliferation; phospho-Rb correlated more strongly with proliferation than total Rb protein.
- In TNBC, Rb protein and phospho-Rb were negatively correlated with proliferation; many high-proliferation tumors were Rb-low.
- TNBC cases separated into phospho-Rb-low and phospho-Rb-high groups. CDK4 and CDK6 activity were higher in phospho-Rb-high TNBC.
- In GDSC cell lines, TNBC lines with RB1 mutation/deletion were refractory to palbociclib, but some RB1-wild-type TNBC lines were sensitive.
- Rb protein abundance correlated with palbociclib response across HER2-negative breast cancer cell lines regardless of RB1 genotype (Spearman rho = -0.61, p = 0.022; high AUC means low sensitivity).
- POC lesson: RB1 mutation status is necessary but insufficient; Rb protein and phospho-Rb should be modeled as functional biomarkers.

## Acetylome and Metabolic Vulnerability

- Metabolic protein clustering mostly recapitulated the four NMF clusters.
- Basal-I tumors upregulated carbohydrate metabolism, DNA elongation, translation, glycolysis, and serine synthesis proteins while downregulating cholesterol, amino-acid, vitamin, and cofactor metabolism.
- HER2-I tumors upregulated cholesterol biosynthesis and lipid metabolism independent of ERBB2 amplification.
- Protein-normalized acetylome analysis showed Basal-I-specific mitochondrial hyperacetylation and cytoplasmic/glycolytic hypoacetylation.
- Glycolysis proteins such as HK3, PFKP, GAPDH, ENO1, and LDHB were up, while several glycolytic enzymes were hypoacetylated, suggesting combined abundance and PTM regulation.
- SIRT3 protein was negatively associated with mitochondrial metabolic protein acetylation, nominating SIRT3-related control of mitochondrial acetylation.
- Nuclear acetylation split Basal-I tumors into subgroups with differences in DNA-repair pathway protein abundance and HAT-associated acetylation signals.

## Relevance to Drug-Response Global/Phospho/Somatic SNV POC

- This is a direct blueprint for a model ladder in which clinical receptor/genomic status is checked against target protein and phosphosite activity before being treated as a response feature.
- For HER2/ERBB2 therapy, use `ERBB2 amplification/IHC -> ERBB2 protein -> ERBB2 phosphopeptide -> alternative ERBB/MAPK/TOP2A features -> response`.
- For CDK4/6 inhibitor hypotheses, use `RB1 mutation/CNA -> Rb protein -> phospho-Rb -> CDK4/6 PTM-SEA -> palbociclib or clinical response`.
- For immunotherapy/immune evasion, include APOBEC, mutation burden, SSBR/NER protein scores, PD-L1/PD1/CTLA4, CIBERSORT or protein immune-modulator scores, and subtype-specific interpretation.
- For phospho-SNV links, mutation-associated kinase outliers provide a compact figure template: mutation group, kinase phosphorylation outlier, pathway, candidate drug or vulnerability.
- For PTM correction, the acetylome analysis is a useful parallel to phosphoproteomics: compare raw PTM with protein-corrected/residual PTM, especially for metabolism.

## Limitations

- This is mainly a treatment-naive primary tumor atlas; most therapeutic claims are mechanistic hypotheses, not direct clinical response validation.
- Bulk cryopulverized tumor improves molecular depth and layer concordance but loses spatial and cell-type resolution.
- Prospective collection improves quality but may limit subgroup and demographic representation.
- NAT proteomic plexes failed downstream quantitative quality control and should not be treated as a tumor/NAT matched analysis layer.
- The authors state that PG findings should be integrated into therapeutic trials and microscaled biopsy workflows before clinical deployment.

## Data Availability

- CPTAC data portal study: `S060`.
- Proteomic Data Commons: `PDC000120`.
- Genomics/transcriptomics: dbGaP `phs000892`.
- Processed sample annotation and normalized data are provided in Tables S1 and S2 and were deposited in LinkedOmics.
- Interactive multi-omics viewer was listed in the PDF for CPTAC-BRCA2020.

## Connections

- [Drug Response Proof-of-Concept with Global Proteome, Phosphoproteome, and Somatic SNV](../analyses/drug-response-poc-global-phospho-somatic-snv.md)
- [Drug Response Phospho/Global 100-Paper Bulk Ingest Tracker](../analyses/drug-response-phospho-global-100-bulk-ingest.md)
- [Ptmanchor Topic Hub](../topics/ptm-correction-and-kinase-signaling-in-cancer-proteomics.md)
- [Cancer Multiomics Proteogenomic Atlas](../topics/cancer-multiomics-literature.md)
- [Proteogenomics connects somatic mutations to signalling in breast cancer](mertins-2016-proteogenomics-somatic-mutations-signalling-breast-cancer.md)
- [Proteogenomic markers of chemotherapy resistance and response in TNBC](anurag-2022-proteogenomic-markers-chemotherapy-resistance-response.md)
- [Proteogenomic analysis of the CALGB 40601 HER2+ breast cancer neoadjuvant trial reveals resistance biomarkers](jaehnig-2025-proteogenomic-analysis-calgb-40601-alliance.md)

## Sources

- Local PDF: `raw/inbox/papers/krug-2020-proteogenomic-landscape-breast-cancer-tumorigenesis.pdf`
- DOI: `10.1016/j.cell.2020.10.036`
- PMID: `33212010`
- PMCID: `PMC8077737`
