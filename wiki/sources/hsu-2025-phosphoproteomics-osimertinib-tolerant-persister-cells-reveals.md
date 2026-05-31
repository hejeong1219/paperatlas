---
title: "Phosphoproteomics of osimertinib-tolerant persister cells reveals targetable kinase-substrate signatures"
authors:
  - Hsu
  - Martin
  - Weng
  - Kitata
  - Nagelli
  - Chang
  - Hess
  - Chen
year: 2025
journal: "Molecular Systems Biology"
doi: "10.1038/s44320-025-00141-1"
pmid: "41023502"
paper_kind: mechanistic-phosphoproteomics
cancer_types:
  - nsclc
  - egfr-mutant-lung-cancer
modalities:
  - cell-line-model
  - global-proteomics
  - phosphoproteomics
  - dia-ms
  - kinase-substrate-enrichment
  - western-blot-validation
themes:
  - drug-tolerant-persisters
  - osimertinib-resistance
  - kinase-signaling
  - cdk1-samhd1-axis
  - yap1-mtor-bad-survival
tags:
  - ptmanchor
  - cancer-multiomics
  - phosphoproteomics
  - drug-response
  - resistance
  - egfr-tki
  - pmid-41023502
pdf: "raw/inbox/papers/hsu-2025-phosphoproteomics-osimertinib-tolerant-persister-cells-reveals.pdf"
ingest_status: full-text-read
ingested_on: 2026-05-13
batch_ingest_status: pdf-text-extracted
batch_ingested_on: 2026-05-13
topic: cancer-multiomics
cm_axis: phospho
---

# Phosphoproteomics of osimertinib-Tolerant Persister Cells Reveals Targetable Kinase-Substrate Signatures

Hsu et al. use DIA-MS global proteomics and phosphoproteomics in EGFR-mutant NSCLC drug-tolerant persister (DTP) models to map the transition from acute osimertinib response to persister survival and recovery, nominating CDK1 substrate signaling, YAP1, mTOR, and BAD phosphorylation as actionable resistance-state features.

## Batch PDF Ingest Status

- Status: `pdf-text-extracted` on 2026-05-13.
- Local PDF: `raw/inbox/papers/hsu-2025-phosphoproteomics-osimertinib-tolerant-persister-cells-reveals.pdf`.
- Extracted text length: 47,142 characters.
- Scope note: automated local-PDF text ingest for the 100-paper drug-response/phospho-global batch; not yet a manual full-text deep-dive.
- Evidence boundary: downstream scientific claims should use this page only after source-specific Key Points are manually promoted or rechecked against the local PDF.
- High-signal PDF snippets:
  - Article Phosphoproteomics of osimertinib-tolerant persister cells reveals targetable kinase-substrate signatures Hsiang-En Hsu1,5, Matthew J Martin2,5, Shao-Hsing Weng 1, Reta Birhanu Kitata 1 , Srikar Nagelli 2 , Chiung-Yun Chang3, Sonja Hess 3 ✉ & Yu-Ju Chen 1,4 ✉ Abstract without the T790M gatekeeper mutation (Cross et al,...
  - Despite its proven clinical beneﬁt in the metastatic setting, nearly Osimertinib is the ﬁrst-line therapy for EGFR-mutated non-small all patients eventually relapse during drug treatment.
  - Recent work cell lung cancer, but acquired resistance emerges in most patients has shown that a very heterogeneous set of genetic and non-genetic and remains a major barrier for complete cure.
  - This phenomenon is events can drive this clinical resistance (Leonetti et al, 2019), most likely associated with the drug-tolerant persister (DTP) cell making the development of broadly applicable treatment strategies 1234567890();,: phenotype, a reversible state that enables survival under treatment for resistant patients hi...
  - This has led to an and leads to irreversible drug resistance.

## Key Points

- **Model and treatment design:** PC9 EGFR exon 19 deletion NSCLC cells were treated with osimertinib 160 nM acutely (5 min, 10 min, 6 h; the text also frames 24 h as initial response) or for 21 days to create DTP cells, then washed out for 24 h or 7 days to examine recovery. Validation experiments also used H1975, HCC4006, and HCC827 cells.
- **DIA-MS resource depth:** The authors built custom lung-cancer proteome and phosphoproteome spectral libraries from NSCLC cell lines/tissues plus 36 project DIA datasets. The proteome library covered 12,360 protein groups and 256,941 peptide sequences; the phosphoproteome library covered 221,618 phosphopeptides, 53,182 phosphosites, and 10,326 protein groups.
- **Quantified omics scale:** Across time points they identified an average of about 5,200 proteins and 21,500 phosphopeptides per condition. The phosphoproteome included 10,742 unique phosphosites from 38,957 phosphopeptides and 3,625 proteins. ANOVA FDR < 0.05 found 2,953 differentially expressed proteins and 3,711 differentially expressed phosphopeptides across DMSO, acute, and DTP states.
- **State separation:** PCA separated DMSO, acute osimertinib, and DTP/recovery states. PC1 captured 52.3% of variance and was driven by DTP samples; PC2 captured 13.4% and was driven by acute treatment.
- **DTP programs:** DTP cells upregulated actin cytoskeleton, cell adhesion, tight junction, endocytosis, metabolic, ribosome biogenesis, cytoskeleton, and translation-related programs. Long washout/recovery clusters also pointed to DNA repair, RNA splicing, and drug metabolism.
- **Resistance-state signaling:** Acute osimertinib suppressed EGFR and downstream phosphosignaling, but DTP/recovery cells showed reactivation or remodeling of PI3K/AKT, MAPK, PKA, and PKC signaling. Recovered phosphorylation included GAB1, mTOR, PRKACA, PRKC family sites, ARAF/BRAF/RPS6KA3, and BAD S99/S118.
- **Anti-apoptotic hypothesis:** BAD S99/S118 hyperphosphorylation in DTP/recovery is interpreted as a survival/anti-apoptotic mechanism, alongside mTOR pathway activity and YAP1 regulation.
- **CDK1 substrate axis:** KSEA found enrichment of CDK1-related substrate phosphorylation in DTP states, including PML S518 and SAMHD1 T592. Western blot validation confirmed dynamic pCDK1 Y15 behavior and increased phosphorylation of SAMHD1/PML in DTPs across multiple EGFR-mutant lung cancer lines.
- **Functional targeting:** CDC25 inhibition with NSC-663428, used to indirectly inhibit CDK1 activation, reduced DTP growth/regrowth under several dosing schedules. CRISPR/Cas9 CDK1 and CDK2 knockout pools reduced DTP confluency compared with osimertinib-treated controls, with CDK1 emphasized as a DTP vulnerability.
- **mTOR/YAP validation:** The mTOR inhibitor vistusertib reduced DTP growth in PC9, H1975, and HCC827 dosing-schedule assays and decreased pS6 in western blot validation. YAP1 phosphorylation and CYR61 expression were linked to active YAP-state regulation in DTPs.
- **Data availability:** MS proteomics data are deposited in ProteomeXchange/PRIDE as `PXD058009`; source data are in BioStudies record `S-SCDT-10_1038-S44320-025-00141-1`.

## Experimental Design

The paper is a mechanistic perturbation study rather than a patient cohort. Its value for the Cancer Multiomics / drug-response project is that it shows a concrete workflow for using time-resolved global proteome plus phosphoproteome data to distinguish:

- acute drug effect,
- persister-cell adaptive survival,
- recovery after drug withdrawal,
- kinase-substrate signatures that may be targetable before stable genetic resistance dominates.

The authors used Fe-IMAC phosphopeptide enrichment, Orbitrap Fusion Lumos DIA acquisition, Spectronaut library-based processing, phosphosite localization probability >= 0.75 for class 1 sites, Perseus statistics, KEGG/ShinyGO enrichment, PhosphoSitePlus kinase-substrate relationships, KSEA, and CausalPath network analysis.

## Relevance to Drug-Response POC

- **Directly useful for global/phospho feature engineering:** The acute/DMSO, DTP/acute, and recovery/acute contrasts are a good template for building response-state features in our own global and phospho data.
- **Kinase activity over single phosphosite calls:** The paper supports using substrate-set enrichment and causal network inference rather than interpreting one phosphosite at a time.
- **Resistance as reversible cell state:** DTPs are modeled as a reversible persister state, so this paper is more relevant to minimal residual disease and early adaptive resistance than to late clonal resistance.
- **Candidate feature families:** CDK1 substrates, mTOR/S6, YAP1/CYR61, BAD S99/S118, MAPK rebound, and cytoskeleton/adhesion/endocytosis programs are candidate features to check in anticancer-drug response data.
- **Complement to somatic SNV:** The study's main signal is not a new SNV driver; it illustrates how phosphoproteome state can explain drug tolerance beyond genotype.

## Connections

- [Drug Response Proof-of-Concept with Global Proteome, Phosphoproteome, and Somatic SNV](../analyses/drug-response-poc-global-phospho-somatic-snv.md)
- [Drug Response Phospho-Global Proteomics Corpus Queue](../analyses/drug-response-phospho-global-100-corpus-queue.md)
- [Cancer Multiomics Proteogenomic Atlas](../topics/cancer-multiomics-literature.md)
- [PTM Correction and Kinase Signaling in Cancer Proteomics](../topics/ptm-correction-and-kinase-signaling-in-cancer-proteomics.md)
- [Osimertinib Resistance and Immune Remodeling](../concepts/osimertinib-resistance-and-immune-remodeling.md)
- [EGFR-Mutant NSCLC and Immunotherapy Mismatch](../concepts/egfr-mutant-nsclc-and-immunotherapy-mismatch.md)

## Open Questions

- The main model is cell-line based, so the CDK1/SAMHD1/PML and mTOR/YAP/BAD axes should be checked against patient tumors or patient-derived models before being treated as clinical biomarkers.
- SAMHD1 knockdown alone did not reduce DTP growth in the authors' discussion, suggesting that the CDK1 signal may depend on coordinated substrate programs rather than a single substrate.
- The source page should be revisited if supplementary tables are ingested, because the exact phosphosite matrices and substrate lists would be useful for building a reusable feature dictionary.

## Sources

- Local PDF: `raw/inbox/papers/hsu-2025-phosphoproteomics-osimertinib-tolerant-persister-cells-reveals.pdf`
- DOI in PDF: `10.1038/s44320-025-00141-1`
- ProteomeXchange/PRIDE: `PXD058009`
- BioStudies source data: `S-SCDT-10_1038-S44320-025-00141-1`

## 함께 인용된 논문

위키 분석·합성 페이지에서 이 논문과 함께 인용된 논문들 (co-citation).

- [[anurag-2022-proteogenomic-markers-chemotherapy-resistance-response|Anurag 2022]]
- [[lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc|Lee 2026]]
- [[chmielecki-2023-acquired-resistance-first-line-osimertinib|Chmielecki 2023]]
- [[holt-2025-proteogenomic-characterization-unveils-biomarkers-associated|Holt 2025]]
- [[jaehnig-2025-proteogenomic-analysis-calgb-40601-alliance|Jaehnig 2025]]
- [[yaeger-2023-molecular-characterization-acquired-resistance-krasg12c-egfr|Yaeger 2023]]
- [[sambath-2026-integrated-genomic-proteomic-cervical-cancer-chemoradiation-resistance|Sambath 2026]]
- [[gillette-2020-proteogenomic-characterization-reveals-therapeutic-vulnerabilities|Gillette 2020]]
- [[huang-2021-proteogenomic-insights-biology-treatment-hpv-negative|Huang 2021]]
- [[jin-2026-deciphering-mediated-phosphorylated-alterations-cancer-related|Jin 2026]]
