---
title: "Proteogenomic characterization of pancreatic ductal adenocarcinoma"
authors:
  - "Cao"
  - "Huang"
  - "Zhou"
year: 2021
journal: "Cell"
doi: "10.1016/j.cell.2021.08.023"
paper_kind: proteogenomic-atlas
cancer_types:
  - pancreatic-ductal-adenocarcinoma
modalities:
  - whole-genome-sequencing
  - whole-exome-sequencing
  - dna-methylation
  - rna-seq
  - mirna-seq
  - global-proteomics
  - phosphoproteomics
  - glycoproteomics
themes:
  - therapeutic-vulnerability
  - kras
  - kinase-signaling
  - glycoproteomics
  - immune-exclusion
  - tumor-microenvironment
  - proteogenomic-subtypes
tags:
  - cancer-multiomics
  - drug-response
  - ptmanchor
  - proteomics
  - phosphoproteomics
  - glycoproteomics
  - pdac
corpus_role: core-proteogenomic-vulnerability
ingest_status: full-text-read
ingested_on: 2026-05-13
pdf: "raw/inbox/papers/cao-2021-proteogenomic-characterization-pancreatic-ductal-adenocarcinoma.pdf"
---
# Proteogenomic Characterization of Pancreatic Ductal Adenocarcinoma

Cao et al. provide a CPTAC proteogenomic atlas of PDAC with matched genomic, transcriptomic, proteomic, phosphoproteomic, and glycoproteomic layers. For the drug-response POC, the paper is most useful for KRAS-downstream kinase targeting, immune-cold microenvironment logic, glycoprotein target nomination, and purity-aware multi-omics subtyping.

## Full-Text Read Status

- Status: `full-text-read` on 2026-05-13.
- Local PDF identity verified against title, Cell 2021 journal metadata, DOI `10.1016/j.cell.2021.08.023`, and 49-page local PDF.
- Evidence boundary: all scientific claims below come from the local PDF `raw/inbox/papers/cao-2021-proteogenomic-characterization-pancreatic-ductal-adenocarcinoma.pdf`.

## Key Points

- The study includes 140 treatment-naive pancreatic tumors, consisting of 135 PDACs and 5 pancreatic adenosquamous carcinomas, plus 67 paired NATs and 9 normal pancreatic duct tissues.
- Multi-omics layers include WES, WGS, DNA methylation, RNA-seq, miRNA-seq, TMT global proteomics, phosphoproteomics, and glycoproteomics.
- Proteomics, phosphoproteomics, and glycoproteomics identified and quantified 11,662 proteins, 51,469 phosphosites, and 34,024 glycopeptides.
- The paper treats tumor neoplastic cellularity as a central analysis requirement. It defines 105 tumors as sufficient purity using KRAS VAF, mutation burden, CNV, pathology, methylation deconvolution, and RNA-based deconvolution; 35 tumors are marked low purity.
- In 105 sufficient-cellularity tumors, KRAS, TP53, CDKN2A, and SMAD4 alterations occurred at 97%, 83%, 48%, and 29%, respectively.
- TP53 alterations had broad trans-effects at protein and phosphosite levels, including increased phosphorylation of DNA damage repair proteins and MKI67.
- Differential tumor/NAT analysis found 222 proteins increased more than 2-fold in tumors; after stromal/immune adjustment and ductal-normal comparison, 21 proteins remained strong early-detection/prognostic candidates.
- Phosphoproteomics nominates actionable kinase-substrate axes downstream of KRAS, including CDK7-MCM2, AKT1-FLNA, PAK1-BAD S134, PAK2-MAPK6 S189, and SRC-STAT3.
- Immune-cold PDACs are linked to endothelial-cell remodeling, VEGF/hypoxia pathway activation, increased glycolysis, and phosphorylation-specific cell-junction dysregulation.
- Purity-aware proteogenomic subtyping of 105 tumors identifies two main clusters, C1 and C2. C2 is basal-like/proliferative, has worse survival, and is enriched for activated proliferative and signaling pathways.

## Cohort and Data Design

- Tumors were treatment-naive and surgically resected, collected by 11 tissue source sites from 7 countries.
- The study controlled ischemia time for PTM quality and used cryopulverized tissue for parallel genomic, epigenomic, transcriptomic, and proteomic analyses.
- Low-purity samples were retained for selected microenvironment analyses but excluded from tumor-intrinsic subtyping and driver analyses where neoplastic signal would be too diluted.
- Normal pancreatic duct tissues were added to avoid treating acinar-rich NAT as a perfect ductal normal reference.

## Genomic Alterations and Functional Consequences

- KRAS is nearly universal, but KRAS itself remains difficult to target directly in PDAC because G12C is rare.
- TP53 mutations associate with phosphorylation of DNA damage repair proteins such as MSH6, TP53, and TP53BP1, and with MKI67 phosphorylation, suggesting a proliferation/DNA-damage state.
- TP53 missense tumors have higher TP53 protein and TP53 S315 phosphorylation than wild type, while truncating mutations do not show the same cis-protein pattern.
- SMAD4 mutation associates with lower SERPINE1 RNA/protein and upregulation of MAPK3 protein and downstream MAPK signaling.
- CDKN2A deletion is often focal copy-number loss rather than intragenic mutation, reinforcing the need for CNA/SV data when available.
- CNV-driven candidate genes include actin/cytoskeleton-related proteins, supporting a copy-number-to-protein vulnerability layer beyond SNV.

## Early Detection, Glycoproteomics, and Biomarker Candidates

- Tumor/NAT proteomics identified 2,218 proteins downregulated and 2,244 proteins upregulated in PDAC.
- Twenty-one tumor-associated proteins remained strongly upregulated relative to NAT, after epithelial-content adjustment, and relative to normal ducts; many were also upregulated in early-stage tumors.
- LOXL2 protein abundance associated with shorter overall survival.
- PTM-level prognosis sometimes differed from protein-level prognosis. An N-linked glycosylation site on APOD associated with better OS even when total APOD protein did not.
- Glycoproteomics identified 75 N-linked glycoproteins upregulated more than 2-fold at the protein level in tumors; 48 of those were validated by DIA.
- CEACAM5 and CEACAM6 were upregulated in tumors with KRAS G12D, G12V, and Q61H, but not G12R.
- Upregulated N-linked glycoproteins in PDAC were mainly modified by sialylated and/or fucosylated glycans, with tumor upregulation of enzymes including ST6GAL1, ST3GAL1, FUT3, FUT11, B4GALT1, B4GALT4, B3GALT5, and ST6GALNAC1.

## Kinase and KRAS-Downstream Targeting

- Kinase-substrate co-regulation across 41 tumor/NAT paired tissues nominates five phospho-substrates and associated kinases with available or investigational inhibitors: MCM2-CDK7, FLNA-AKT1, BAD-PAK1, MAPK6-PAK2, and STAT3-SRC.
- PAK1 showed higher expression in more than 70% of tumors and was supported by elevated phosphorylation of BAD S134.
- PAK2 was upregulated in almost 90% of tumors and linked to MAPK6 S189 phosphorylation, suggesting atypical MAPK signaling and motility biology.
- MET, KRAS, RAC1, PAK1, and PAK2 were concordantly upregulated at transcript and protein levels, supporting a MET/RAC1/PAK axis downstream of KRAS biology.
- KRAS hotspot-specific phosphosite analysis stratified 19 kinases, including seven FDA-approved drug targets, suggesting that specific KRAS alleles may need different downstream targeting hypotheses.

## Immune Exclusion and Microenvironment

- Transcriptomic deconvolution classified all 140 tumors into four composition clusters.
- A small immune-hot group had higher CD8+ T-cell infiltration, cytotoxic enzymes, immune checkpoint molecules, and prominent inflammatory infiltrates on histology.
- True immune-cold groups showed reduced endothelial adhesion proteins, elevated VEGF and hypoxia pathway activity, higher glycolysis, and phospho-specific cell-junction dysregulation.
- CD8+ T-cell infiltration was favorable prognostically, while elevated VEGF and hypoxia pathway signaling were associated with decreased survival.
- The paper proposes endothelial remodeling, hypoxia/VEGF, glycolysis, and cell-junction phosphorylation as linked mechanisms of immune exclusion in PDAC.

## Proteogenomic Subtypes

- RNA-based subtype labels and whole-cohort multi-omics subtypes were strongly confounded by tumor purity and cell composition.
- Restricting NMF subtyping to 105 sufficient-purity tumors yielded two clusters: C1, overlapping Moffitt classical, and C2, overlapping Moffitt basal-like.
- C2 had elevated proliferative signaling and worse survival.
- Proteogenomic subtyping split some Moffitt-classified tumors differently and showed stronger survival separation than Moffitt RNA subtype alone.
- Drug-signature enrichment suggested chemotherapy-associated signatures for C1 and kinase-inhibitor signatures for C2, including PP-242, CP466722, and sunitinib, supported by elevated target expression.

## Relevance to Drug-Response POC

- This paper is a strong template for purity-aware multi-omics modeling: before comparing SNV/proteome/phosphoproteome blocks, neoplastic cellularity and stromal/immune dilution must be estimated and sensitivity-tested.
- For KRAS-driven tumors, the most useful POC ladder is `KRAS allele/CNA/TP53/SMAD4 -> protein pathway state -> kinase-substrate phosphosite axis -> druggable downstream target`.
- PAK1/PAK2, AKT1, CDK7, SRC, MET/RAC1, and mTOR/AKT/ERK pathways provide candidate feature families for phosphoproteome-driven response hypotheses.
- For immunotherapy or immune-evasion endpoints, the paper supports testing `VEGF/hypoxia + glycolysis + endothelial adhesion + junction phosphosite state` as a cold-tumor module beyond mutation status.
- Glycoproteomics is not part of the user's stated dataset, but CEACAM5/6 and sialylation/fucosylation enzymes are useful target/context pages if the manuscript later adds surface targets or serum biomarkers.

## Limitations

- The cohort is treatment-naive and surgically resected, limiting direct inference to metastatic systemic-therapy response.
- Therapy predictions are hypotheses based on molecular state, drug signatures, and known targets; causal effects require validation in cell lines, PDX models, or clinical trials.
- Bulk tumor and NAT profiling cannot fully resolve cellular heterogeneity, despite the study's careful purity/deconvolution strategy.
- Laser capture microdissection or single-cell analyses would further refine tumor-intrinsic versus microenvironmental signals.

## Data Availability

- Raw proteomics: Proteomic Data Commons.
- Genomic, epigenomic, and transcriptomic data: Genomic Data Commons.
- Processed data tables: PDC publications and LinkedOmics CPTAC-PDAC.
- Multi-omics clustering workflow: PANOPLY module with Docker containers reported in the paper.

## Connections

- [Drug Response Proof-of-Concept with Global Proteome, Phosphoproteome, and Somatic SNV](../analyses/drug-response-poc-global-phospho-somatic-snv.md)
- [Drug Response Phospho-Global 100-PDF Bulk Ingest](../analyses/drug-response-phospho-global-100-bulk-ingest.md)
- [Drug Response Phospho-Global Proteomics Corpus Queue](../analyses/drug-response-phospho-global-100-corpus-queue.md)
- [Cancer Multiomics Literature Monitor](../topics/cancer-multiomics-literature.md)
- [PTM Correction and Kinase Signaling in Cancer Proteomics](../topics/ptm-correction-and-kinase-signaling-in-cancer-proteomics.md)
- [Multiomics Proteomics PTM Identification](../topics/multiomics-proteomics-ptm-identification.md)
- Cancer Multiomics summary: [Cao 2021 - PDAC CPTAC Proteogenomics](../analyses/cancer-multiomics-literature/cao-2021-proteogenomic-characterization-pancreatic-ductal-adenocarcinoma.md)

## Sources

- Local PDF: `raw/inbox/papers/cao-2021-proteogenomic-characterization-pancreatic-ductal-adenocarcinoma.pdf`
