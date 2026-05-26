---
title: "Proteogenomic Characterization Reveals Therapeutic Vulnerabilities in Lung Adenocarcinoma"
authors:
  - "Gillette"
  - "Satpathy"
  - "Cao"
year: 2020
journal: "Cell"
paper_kind: proteogenomic-atlas
cancer_types:
  - lung-adenocarcinoma
modalities:
  - WES
  - WGS
  - RNA-seq
  - miRNA-seq
  - DNA-methylation
  - global-proteomics
  - phosphoproteomics
  - acetylproteomics
themes:
  - therapeutic-vulnerability
  - driver-to-signaling
  - kinase-signaling
  - immune-cold
  - tumor-normal-comparison
tags:
  - source
  - ptmanchor
  - proteomics
  - ptm
  - phosphoproteomics
  - cancer-proteomics
pmid: "32649874"
doi: "10.1016/j.cell.2020.06.013"
pmcid: "PMC7373300"
pdf: "raw/inbox/papers/gillette-2020-proteogenomic-characterization-reveals-therapeutic-vulnerabilities.pdf"
topic: ptmanchor
corpus_role: core-proteogenomic-vulnerability
ingest_status: full-text-read
ingested_on: 2026-05-13
---
# Proteogenomic Characterization Reveals Therapeutic Vulnerabilities in Lung Adenocarcinoma

This CPTAC LUAD resource uses matched genomics, transcriptomics, deep global proteomics, phosphoproteomics, acetylproteomics, and paired normal adjacent tissues to show that driver mutations and fusions often become interpretable therapeutic vulnerabilities only after protein and PTM layers are measured.

## Full-Text Read Status

- Status: `full-text-read` on 2026-05-13.
- Local PDF: `raw/inbox/papers/gillette-2020-proteogenomic-characterization-reveals-therapeutic-vulnerabilities.pdf`.
- PDF identity verified from the local PDF metadata and title page: Cell 2020, DOI `10.1016/j.cell.2020.06.013`, 62 pages.
- Corpus role: `core-proteogenomic-vulnerability`. This is not a response-labeled treatment cohort, but it is a core global proteome/phosphoproteome reference for driver-to-signaling translation and therapeutic vulnerability nomination.

## Key Points

- Cohort: 110 treatment-naive LUAD tumors and 101 matched normal adjacent tissues, with complete data for 101 tumors and 96 NATs.
- Assays: WES, WGS, RNA-seq, miRNA-seq, DNA methylation, TMT global proteomics, phosphoproteomics, and acetylproteomics.
- Multi-omics NMF clustering produced four LUAD clusters aligned with immune, proximal-proliferative, STK11-mutant, EGFR/ALK-enriched, and terminal respiratory unit-like biology.
- Phosphoproteomics made several driver events more actionable than RNA/protein alone, including ALK Y1507 in ALK fusions, PTPN11/Shp2 Y62 in EGFR-mutant tumors, and SOS1 S1161 in KRAS-mutant tumors.
- STK11-mutant LUAD showed immune-cold behavior and a proteome-only neutrophil degranulation program, suggesting a non-cell-count immunosuppressive mechanism.
- Tumor-normal PTM analysis identified site-level changes larger than protein abundance changes, supporting the need for protein-aware phosphosite interpretation rather than raw phosphosite abundance alone.
- Data are public through CPTAC/GDC/dbGaP and include processed tables and an interactive CPTAC LUAD viewer.

## Cohort and Methods

- Patient material: newly diagnosed LUAD surgical resections, treatment-naive before collection, with paired NAT and whole blood when available.
- Tissue handling: prospective CPTAC collection with cold ischemia <40 minutes; mean ischemic time was 13 minutes.
- Minimum tumor quality: average 50% tumor cell nuclei and <20% necrosis in reviewed top/bottom histologic sections.
- Sequencing: WES nominal 150x, WGS nominal 15x, RNA-seq, miRNA-seq, and EPIC methylation array.
- Proteomics: cryopulverized tissue, urea lysis, LysC/trypsin digestion, TMT-10 labeling, common reference sample, basic reverse-phase fractionation, IMAC phosphopeptide enrichment, acetyl-lysine enrichment, and LC-MS/MS.
- MS platforms: Q Exactive HF-X for whole proteome; Orbitrap Fusion Lumos for phosphoproteome and acetylproteome.
- Analysis scale after filtering included RNA 18,099 genes, protein 10,165 features, 40,845 phosphosites, and 6,984 acetylsites for tumor-NAT PCA; VM-site polishing reported 65,103 phosphosites and 13,480 acetylsites.
- PTM quality: aggregate phosphosite FDR 0.74%, 71% fully localized; aggregate acetylsite FDR 0.89%, 99% fully localized.

## Major Findings

### Multi-Omics LUAD Taxonomy

- C1 aligned with proximal-inflammatory LUAD, enriched for TP53 mutation, STK11 wild type, CIMP-high status, and immune signaling.
- C2 was a proximal-proliferative subcluster enriched for Western/US patients, TP53 and EGFR wild type status, and hemostasis/platelet activation signatures.
- C3 was the dominant proximal-proliferative cluster, enriched for Vietnamese patients and STK11 mutation, with histone deacetylase and cell-cycle programs.
- C4 aligned with terminal respiratory unit biology, enriched for EGFR mutations, female sex, Chinese nationality, EML4-ALK fusions, and absence of KRAS/STK11 mutations.

### Driver Events Become More Informative in PTM Space

- ALK fusion cases had outlier ALK mRNA and, when detected, ALK protein, but ALK Y1507 phosphorylation was the most dramatic fusion-associated signal.
- ALK and phospho-ALK Y1507 IHC were tumor-specific in available ALK fusion-positive cases and not detected in ROS1/RET fusions or paired NATs.
- KRAS-mutant tumors showed SOS1 S1161 phosphorylation, nominating SOS1/KRAS activation biology and SOS1 inhibition as a therapeutic strategy.
- EGFR-mutant tumors showed highly consistent PTPN11/Shp2 Y62 phosphorylation with no corresponding RNA or protein effect, nominating SHP2 inhibition as a phosphoproteome-specific vulnerability.
- ALK fusion-driven tumors also showed PTPN11/Shp2 phosphorylation at Y546/Y584, extending the SHP2 logic beyond EGFR mutation.
- A systematic kinase outlier analysis found hyperphosphorylated kinases in EGFR-, KRAS-, TP53-, STK11-, KEAP1-, and EML4-ALK-altered samples, many without corresponding CNA, RNA, or protein outliers.

### Copy Number, Methylation, and Protein Consequences

- CNA cis effects were dampened from RNA to protein and PTM: significant positive cis correlations numbered 6,043 for RNA, 2,354 for proteins, and 244 for phosphoproteins, with 156 overlapping across all three.
- Cancer-associated genes with overlapping cis regulation included EGFR, AKT2, YES1, CREBBP, KMT2B, NFKB2, and others.
- Protein-level trans effects were compared with Connectivity Map perturbation profiles to nominate functionally important genes within CNA regions.
- DNA methylation showed cascading effects on RNA, protein, and phosphoprotein for genes including CLDN18, ANK1, and PTPRCAP.

### Immune Landscape and STK11

- xCell-based immune clustering identified hot tumor-enriched, cold tumor-enriched, and NAT-enriched immune clusters.
- Hot tumors showed stronger B-cell, CD4/CD8 T-cell, dendritic-cell, and macrophage signatures, with PD1 RNA and PD-L1 RNA/protein upregulated.
- Cold tumor-enriched tumors showed proteome-level glycolysis, peroxisome, PPAR signaling, and epithelial barrier features.
- STK11-mutant tumors showed the strongest immune downregulation, including lower dendritic-cell, natural-killer T-cell, and macrophage signatures.
- This immune-cold state was not simply low mutational burden: the STK11-enriched C3 multi-omics cluster had high somatic mutation burden.
- Independent component analysis found a stable STK11-associated proteomic signature whose top pathway was neutrophil degranulation; all 16 measured neutrophil-degranulation proteins were coherently overexpressed in STK11-mutant tumors, but the signal was not detectable at RNA level.

### Tumor-NAT PTM and Biomarker Findings

- Tumor and NAT proteomes separated clearly by PCA.
- Tumor-NAT comparison identified 70 phosphosites and 11 acetylsites whose tumor changes were markedly different from associated protein changes, implying site stoichiometry changes.
- NPM1 T199 and MKI67 phosphorylation were strongly upregulated in tumors relative to protein abundance, consistent with DNA damage/cell-cycle biology.
- Stringent tumor-NAT protein biomarker analysis identified 289 proteins upregulated at the protein level; 60 were also differential at RNA level.
- Protein biomarker candidates included metabolic/stress/EMT-associated proteins such as GFPT1, BZW2, PDIA4, P4HB, PMM2, GREM1, OCIAD2, DHFR, HYOU1, LDHA, and CBX8.
- Tumor antigen analysis identified 44 recurrently overexpressed cancer-testis antigens, 9 present in at least 10% of samples, plus 2,481 mRNA-validated and 49 peptide-validated somatic mutations.

## Relevance to Drug-Response POC

- This is a template for the user's model ladder because it explicitly asks whether driver mutation status is functionally translated into RNA, protein, phosphosite, and acetylsite states.
- The PTPN11 Y62 example is ideal for a manuscript figure: EGFR-mutant tumors had a therapeutically relevant phosphosite signal with no RNA/protein abundance effect, exactly the kind of independent phospho layer that an SNV/proteome/phosphoproteome POC should test.
- The SOS1 S1161 and ALK Y1507 examples show how phosphoproteomics can nominate druggable pathway nodes or diagnostic markers downstream of genomic drivers.
- The STK11 immune-cold/neutrophil-degranulation result is a strong caution that response biology may appear at the protein layer even when RNA or mutation features are insufficient.
- For POC analysis, this paper supports comparing `mutation status -> protein abundance -> phosphosite/kinase outlier` for EGFR/KRAS/STK11/KEAP1/TP53-like driver blocks and reporting whether the phospho signal remains after protein correction.

## Limitations and Caveats

- The cohort is treatment-naive and not response-labeled, so therapeutic vulnerabilities are hypothesis-generating rather than clinical drug-response predictors.
- Bulk tumor profiling lacks spatial and single-cell resolution; tumor epithelium versus microenvironment contributions can remain ambiguous.
- Associations are confounded by country, sex, smoking status, mutation status, and histology; the authors warn that linear adjustment may not fully resolve these issues in a cohort of this size.
- The outlier and vulnerability calls should be interpreted as prioritization hypotheses requiring functional or clinical validation.

## Data Availability

- Proteomics raw datasets are publicly available through the CPTAC data portal: `https://cptac-data-portal.georgetown.edu/cptac/s/S056`.
- Genomic and transcriptomic files are available through GDC/dbGaP accession `phs001287.v5.p4`.
- Sample annotation and processed/normalized data are provided in Tables S1-S3.
- Interactive CPTAC LUAD data viewer: `http://prot-shiny-vm.broadinstitute.org:3838/CPTAC-LUAD2020/`.

## Connections

- [Drug Response Proof-of-Concept with Global Proteome, Phosphoproteome, and Somatic SNV](../analyses/drug-response-poc-global-phospho-somatic-snv.md)
- [Cancer Multiomics Proteogenomic Atlas](../topics/cancer-multiomics-literature.md)
- [PTM Correction and Kinase Signaling in Cancer Proteomics](../topics/ptm-correction-and-kinase-signaling-in-cancer-proteomics.md)
- [Multiomics Proteomics PTM Identification](../topics/multiomics-proteomics-ptm-identification.md)
- [Gillette 2020 - LUAD CPTAC Proteogenomics (Tumor+NAT; Phospho+Acetyl)](../analyses/cancer-multiomics-literature/gillette-2020-proteogenomic-characterization-reveals-therapeutic-vulnerabilities.md)
- [Proteogenomic analysis reveals non-small cell lung cancer subtypes predicting chromosome instability, and tumor microenvironment](./song-2024-proteogenomic-analysis-reveals-non-small-cell.md)
- [Candidate mechanisms of acquired resistance to first-line osimertinib in EGFR-mutated advanced non-small cell lung cancer](./chmielecki-2023-acquired-resistance-first-line-osimertinib.md)

## Sources

- Local PDF: `raw/inbox/papers/gillette-2020-proteogenomic-characterization-reveals-therapeutic-vulnerabilities.pdf`
