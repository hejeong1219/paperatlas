---
title: "Phosphoproteomic and Acetylomic Characterization of Colorectal Cancer Cells Treated with Kinase Inhibitors"
authors:
  - Zhao
  - Zhang
  - Zhou
year: 2025
journal: "ACS Pharmacology & Translational Science"
doi: "10.1021/acsptsci.5c00398"
pmid: "40969873"
pmcid: "PMC12441852"
paper_kind: perturbation-proteomics
cancer_types:
  - colorectal-cancer
modalities:
  - cell-line
  - kinase-inhibitor-perturbation
  - TMTpro-proteomics
  - phosphoproteomics
  - acetylomics
themes:
  - kinase-signaling
  - drug-perturbation
  - PTM-crosstalk
  - drug-combination
  - phosphoproteomics
tags:
  - ptmanchor
  - drug-response
  - proteomics
  - phosphoproteomics
  - acetylomics
  - kinase-inhibitors
  - pmid-40969873
pdf: "raw/inbox/papers/zhao-2025-phosphoproteomic-acetylomic-characterization-colorectal-cancer.pdf"
topic: cancer-multiomics-drug-response
batch_ingest_status: pdf-text-extracted
batch_ingested_on: 2026-05-13
ingest_status: full-text-read
ingested_on: 2026-05-13
corpus_role: perturbation-context
---
# Phosphoproteomic and Acetylomic Characterization of Colorectal Cancer Cells Treated with Kinase Inhibitors

Zhao et al. perturb HCT116 colorectal cancer cells with seven kinase inhibitors and profile proteome, phosphoproteome, and acetylome changes, providing a compact perturbation reference for kinase activity, off-target signaling, PTM crosstalk, and phosphoproteomics-guided drug-combination hypotheses.

## Full PDF Deep-Dive Status

- Status: `full-text-read` on 2026-05-13.
- Local PDF: `raw/inbox/papers/zhao-2025-phosphoproteomic-acetylomic-characterization-colorectal-cancer.pdf`.
- PDF identity checked against title, author list, journal, DOI, and 12-page PDF metadata.
- Corpus role: perturbation/context paper, not a patient-response cohort.

## Key Points

- The experiment treated **HCT116 colorectal cancer cells** with seven kinase inhibitors or DMSO for **12 hours** at **1 uM**, with two replicates per inhibitor.
- Inhibitors covered EGFR/ERBB2 signaling, ERK/MAPK signaling, PI3K/mTOR signaling, and cell-cycle kinases: lapatinib, refametinib, PIK-93, Ro-3306, AT7519, ZSTK474, and AS-605240.
- TMTpro quantified **6,147 proteins**. Lapatinib had the broadest proteome effect with 444 upregulated and 289 downregulated proteins; AT7519 followed with 292 upregulated and 416 downregulated proteins.
- Proteome GSEA separated AT7519 from the other inhibitors: AT7519 activated protein secretion, oxidative phosphorylation, and fatty-acid metabolism, while most other inhibitors activated MYC targets, E2F targets, and G2M checkpoint.
- Same-pathway inhibitors had distinct proteome effects. AT7519 and Ro-3306 both target cell-cycle kinases but differed in fatty-acid metabolism and mitochondrial effects; ZSTK474 and AS-605240 both target PI3K signaling but had different pathway perturbations.
- Lapatinib downregulated 89 mitochondrial proteins and upregulated 9 mitochondrial proteins, especially affecting mitochondrial matrix and inner membrane proteins, suggesting mitochondrial dysfunction.
- Phosphoproteomics quantified **6,213 phosphorylation sites**, including **5,048 class I sites**, on **2,552 proteins**. PTM-SEA and KSEA recovered expected target effects: lapatinib inhibited ERBB2 activity; AT7519 inhibited CDK1, CDK2, and CDK6.
- Phosphoproteomics also nominated potential off-target or indirect effects: lapatinib activated CDK4; PIK-93 activated CDK1/CDK4; refametinib inhibited CDK1/CDK2/CDK4/CDK6; AS-605240 inhibited AKT1/AKT2 and MAPK12/MAPK13.
- Acetylomics quantified **185 acetylated sites** on **135 proteins**. Lapatinib and AT7519 had the largest acetylome effects, showing that kinase inhibitors can alter lysine acetylation as well as phosphorylation.
- PTM crosstalk analysis corrected phosphosite and acetylsite changes for protein abundance and found 22 same-protein acetylation/phosphorylation pairs with significant correlation. Examples include HNRNPA1 K350 with HNRNPA1 S337/S199 and HSPD1 K72 with HSPD1 S70.
- Phosphoproteomics-guided drug-combination analysis found 33 reverse-correlated drug pairs as possible synergistic combinations and 17 concordant pairs as possible antagonistic combinations. Lapatinib and AT7519 showed negative correlation across public perturbation contexts; afatinib and refametinib showed positive correlation.

## Methods / Design Notes

- Cells: HCT116 in DMEM with 10% FBS and penicillin/streptomycin.
- Treatment: 12-hour kinase inhibitor perturbation at 1 uM or DMSO control.
- TMT channels: DMSO, lapatinib, AT7519, PIK-93, AS-605240, Ro-3306, refametinib, and ZSTK474 with two channels per condition.
- Phosphopeptide enrichment: TiO2 enrichment, followed by fractionation.
- Acetylated peptide enrichment: acetyl-lysine antibody enrichment from the phosphopeptide-enrichment flowthrough.
- Proteome MS: Orbitrap Fusion, DDA, 90-minute gradient.
- Phosphoproteome/acetylome MS: Q Exactive HF-X, DDA, 110-minute gradient.
- Search: MaxQuant v2.4.3.0 with UniProt isoform database, 1% FDR for proteins, peptides, and sites. Phosphosites with localization score >0.75 were retained.
- Analysis: two-tailed Student's t test; fold-change cutoff 1.2 or 1/1.2 with p < 0.05; GSEA, PTM-SEA, KSEAapp, WebGestaltR; PTM crosstalk used linear-regression residual correction for protein abundance.

## Relevance to Drug-Response POC

- This paper is best used as a **perturbation interpretation template**, not as evidence for patient response biomarkers.
- It shows how to test whether a candidate kinase signature from patient phosphoproteomics is druggable or compensatory: perturb with a relevant inhibitor, then look for expected target suppression plus off-target or bypass activation.
- The lapatinib -> CDK4 activation example is useful for resistance logic: even when an inhibitor suppresses its intended kinase, phosphoproteomics can reveal compensatory pathways that motivate combination therapy.
- For a user's global proteome + phosphoproteome + somatic SNV POC, the direct lesson is to separate:
  - target engagement,
  - off-target kinase reprogramming,
  - mitochondrial/metabolic proteome effects,
  - PTM crosstalk,
  - and combination-pair hypotheses.
- If patient data nominates an EGFR/ERBB2, CDK, PI3K, MAPK, or mitochondrial resistance axis, a small HCT116-like perturbation design could validate directionality before making strong therapeutic claims.

## Limitations and Caveats

- Single cell line and one time point; no patient cohort or clinical response endpoint.
- Single inhibitor concentration at 1 uM; dose-response and time-course dynamics are not captured.
- Acetylome coverage is small relative to proteome and phosphoproteome.
- Drug-combination predictions are correlation-based and require experimental synergy validation.
- Some effects may reflect HCT116-specific biology rather than general colorectal cancer or pan-cancer signaling.

## Data Availability

- Raw MS data and raw MaxQuant results are deposited in iProX: `IPX0007733000`.
- Supporting information includes proteomic, phosphoproteomic, acetylomic, quality-control, and PTM-correlation analyses.

## Connections

- [Drug Response Proof-of-Concept with Global Proteome, Phosphoproteome, and Somatic SNV](../analyses/drug-response-poc-global-phospho-somatic-snv.md)
- [Drug Response Phospho-Global Proteomics Corpus Queue](../analyses/drug-response-phospho-global-100-corpus-queue.md)
- [Drug Response Phospho-Global 100-PDF Bulk Ingest](../analyses/drug-response-phospho-global-100-bulk-ingest.md)
- [PTM Correction and Kinase Signaling in Cancer Proteomics](../topics/ptm-correction-and-kinase-signaling-in-cancer-proteomics.md)
- [Multiomics Proteomics PTM Identification](../topics/multiomics-proteomics-ptm-identification.md)

## Open Questions

- Which predicted drug pairs are experimentally synergistic in HCT116 or other CRC models?
- How stable are the off-target kinase effects across dose and time?
- Would protein-abundance-corrected phosphosite and acetylsite residuals improve PTM crosstalk discovery compared with raw PTM signals?
- Which findings replicate in patient-derived organoids or clinical tumor perturbation models?

## Sources

- Local PDF: `raw/inbox/papers/zhao-2025-phosphoproteomic-acetylomic-characterization-colorectal-cancer.pdf`
- DOI: <https://doi.org/10.1021/acsptsci.5c00398>
- PubMed: <https://pubmed.ncbi.nlm.nih.gov/40969873/>
- PMCID recorded in source metadata: `PMC12441852`
