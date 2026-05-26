---
title: "Proteogenomic insights into the biology and treatment of HPV-negative head and neck squamous cell carcinoma"
authors:
  - "Huang"
  - "Chen"
  - "Savage"
year: 2021
journal: "Cancer Cell"
paper_kind: proteogenomic-atlas-treatment-hypothesis
pdf: "raw/inbox/papers/huang-2021-proteogenomic-insights-biology-treatment-hpv-negative.pdf"
cancer_types:
  - HPV-negative-head-and-neck-squamous-cell-carcinoma
modalities:
  - WES
  - WGS
  - RNA-seq
  - miRNA-seq
  - DNA-methylation
  - global-proteomics
  - phosphoproteomics
themes:
  - EGFR
  - CDK4-CDK6-Rb
  - immunotherapy
  - kinase-signaling
  - therapeutic-stratification
tags:
  - source
  - ptmanchor
  - proteomics
  - phosphoproteomics
  - cancer-proteomics
pmid: "33417831"
doi: "10.1016/j.ccell.2020.12.007"
pmcid: "PMC7946781"
topic: ptmanchor
corpus_role: core-proteogenomic-treatment-hypothesis
ingest_status: full-text-read
ingested_on: 2026-05-13
---
# Proteogenomic insights into the biology and treatment of HPV-negative head and neck squamous cell carcinoma

This CPTAC Cancer Cell study profiles 108 HPV-negative HNSCC tumors and shows how global proteome/phosphoproteome layers can refine treatment hypotheses for CDK4/6 inhibition, anti-EGFR antibody therapy, and immunotherapy beyond genomics or RNA alone.

## Full-Text Read Status

- Status: `full-text-read` on 2026-05-13.
- Local PDF: `raw/inbox/papers/huang-2021-proteogenomic-insights-biology-treatment-hpv-negative.pdf`.
- PDF identity verified from the local PDF title page and metadata: Cancer Cell 2021, DOI `10.1016/j.ccell.2020.12.007`, 36 pages.
- Corpus role: `core-proteogenomic-treatment-hypothesis`. This is a treatment-stratification atlas rather than a prospective response cohort, but it contains external PDX/clinical-trial support for EGFR ligand and phospho-Rb biomarkers.

## Key Points

- Cohort: 110 treatment-naive primary HNSCC tumors were collected; one HPV-positive sample was removed, leaving 108 HPV-negative HNSCC tumors for main analysis. Sixty-six tumors had matched NATs.
- Assays: WES, WGS, methylation array, RNA-seq, miRNA-seq, TMT global proteomics, and TMT phosphoproteomics.
- Proteomics identified 11,744 proteins; phosphoproteomics identified 97,210 phosphopeptides covering 56,959 confidently localized phosphosites from 8,133 genes.
- Tumor/NAT analysis found 3,355 increased and 3,163 decreased proteins, plus 7,265 increased and 6,320 decreased phosphosites in tumors.
- CDKN2A/CCND1 genomic aberrations did not always imply high CDK4/6-Rb activity; Rb phosphorylation better represented CDK4/6-dependent cell-cycle activity.
- EGFR ligand abundance, not EGFR receptor abundance, aligned with EGFR pathway activity and anti-EGFR monoclonal antibody response signals.
- Immune-cold tumors showed reduced antigen-presentation machinery linked to copy-number deletions of immune regulators such as IFNGR2, JAK2, and IRF1; immune-hot tumors co-upregulated multiple checkpoint/suppressor proteins.
- Integrated multi-omics defined CIN, Basal, and Immune subtypes linked to CDK inhibitors, EGFR mAb therapy, and immunotherapy hypotheses, respectively.

## Cohort and Methods

- Sample source: CPTAC-3, six tissue source sites, seven countries, treatment-naive primary squamous cell carcinomas.
- Demographics: 87% male; oral cavity and larynx were the dominant sites.
- Smoking: genomics-based smoking inference associated 70% of patients with strong smoking evidence.
- Tissue handling: snap-frozen within 30-minute cold ischemic time; average cold ischemia 13 minutes.
- Pathology requirements: viable tumor nuclei >80%, total cellularity >50%, necrosis <20%.
- WES: HiSeq 4000, paired 76-cycle reads, minimum 150x on-target coverage.
- WGS: PCR-free, HiSeq X, minimum 15x coverage.
- Proteomics: 11-plex TMT, 19 TMT sets, pooled reference channel, bRPLC fractionation, Fe-IMAC phosphopeptide enrichment, Easy nLC 1200 UHPLC coupled to Thermo Fusion Lumos.
- Search/quantification: MSFragger, Philosopher, PTMProphet, and TMT-Integrator; PSMs required TMT label and quality filters.

## Major Findings

### Proteomic and Phosphoproteomic Tumor Biology

- Protein-RNA median gene-wise correlation was 0.52 and median sample-wise correlation was 0.43.
- Protein data outperformed RNA data for co-expression-based gene function prediction, supporting the value of the protein layer.
- SCNA integration prioritized 202 putative focal-amplification drivers from 759 quantifiable genes, including PIK3CA, EGFR, CCND1, CTTN, and RNA-processing genes.
- Protein data supported tumor suppressor roles for truncating KMT2D and AJUBA mutations when mRNA abundance did not show the effect.
- Tumor-associated phosphosites were enriched in DNA replication, cell-cycle checkpoint, and actin/cytoskeleton biology.

### FAT1 and 11q13.3 Converge on Actin Dynamics

- FAT1 truncating mutations and 11q13.3 amplification were mutually exclusive in the CPTAC cohort and TCGA HPV-negative HNSCCs.
- Both alteration classes converged on downregulated actin-dynamics proteins, especially beta-actin/ACTB at the protein level despite mRNA changes.
- 11q13.3-amplified tumors showed elevated CTTN phosphosites, with CTTN S418 as the most elevated site; this phosphosite has reported roles in motility and cytoskeletal rearrangement.

### CDK4/6-Rb Treatment Logic

- CDKN2A alterations were widespread: homozygous deletion, promoter hypermethylation, and p16-disrupting truncation/LOH were all considered.
- The authors grouped tumors into pathway-WT, p16 aberration without CCND1 amplification, and p16 aberration plus CCND1 amplification groups.
- Mean Rb CDK4/6 target-site phosphorylation was higher in the altered groups, but many altered tumors still had Rb phosphosite scores within the WT range.
- Rb phosphosite score correlated with E2F activity and multi-gene proliferation score, but some tumors showed high proliferation with low Rb phosphorylation, including RB1-mutant cases.
- In HPV-negative HNSCC PDX models treated with abemaciclib, CCND1/CDKN2A status did not separate response, whereas responsive PDXs had elevated phospho-Rb S807/811.
- HNSCC cell lines with higher Rb protein, strongly correlated with Rb phosphosite score in the CPTAC cohort, were more sensitive to CDK6 genetic depletion.

## EGFR and Immune Treatment Stratification

### Two Modes of EGFR Activation

- EGFR mutations were rare: three tumors, none hotspot; no EGFRvIII fusion was detected.
- EGFR amplification was common: 49 samples had EGFR amplification by CN log2 ratio >0.1, and six had high amplification by CN log2 ratio >1.
- EGFR copy number associated with EGFR mRNA, protein, overall phosphorylation, and activation-site phosphorylation at Y1110, Y1172, and Y1197.
- PROGENy EGFR pathway activity showed no or weak correlation with EGFR alterations, but strong correlation with EGFR ligands AREG, TGFA, EREG, EPGN, and HBEGF.
- Phosphosites in downstream PI3K/Akt/mTOR and RAF/MEK/ERK pathways correlated with EGFR ligands independently of host RNA/protein expression; none significantly correlated with EGFR protein abundance.
- In external HNSCC PDX cetuximab data, EGFR ligands, not receptor abundance, were higher in responders.
- In a panitumumab clinical-trial dataset, EGFR ligand abundance, not receptor abundance, correlated with PFS.
- Interpretation: EGFR ligand abundance may stratify anti-EGFR mAb benefit, whereas high EGFR-amplified tumors with ligand-independent phosphorylation may require EGFR TKIs rather than mAbs.

### Immuno-Proteogenomics

- Immune infiltration varied broadly and was measured by ESTIMATE immune score, CD3 IHC, and CD3 proteomic data.
- Higher immune infiltration associated with lower clinical stage, less smoking, and better prognosis.
- Immune-hot tumors co-enriched cytotoxic immune cells and immunosuppressive cells and showed concordant upregulation of multiple immune checkpoints/suppressors, supporting combination-checkpoint logic rather than PD-1 monotherapy alone.
- Immune-cold tumors did not lack antigen sources: tumor mutational burden, cancer/testis antigen abundance, and proteomics-supported neoantigens did not explain low infiltration.
- Instead, immune-cold tumors had reduced antigen-presentation machinery at mRNA/protein levels and frequent CN deletions of regulators IFNGR2, JAK2, and IRF1.
- Genome-wide analysis identified 294 putative immunosuppressive SCNA drivers enriched in cytokine/chemokine receptor, JAK-STAT, and TLR pathways.

### Integrated Subtypes

- Multi-omics NMF clustering using CN, RNA, miRNA, protein, and phosphopeptide data identified three subtypes: CIN, Basal, and Immune.
- CIN subtype: larynx/strong-smoking/high chromosome instability, frequent CCND1/CDKN2A aberration, high CDK4/6 activity by Rb hyperphosphorylation, and potential CDK inhibitor sensitivity.
- Basal subtype: high EGFR ligand expression and EGFR pathway activity, suggesting potential anti-EGFR mAb sensitivity.
- Immune subtype: high immune and checkpoint/suppressor protein expression, suggesting immunotherapy or combination-checkpoint potential.
- High-potential candidate proportions reported by subtype were 32% of CIN tumors for CDK inhibitors, 62% of Basal tumors for EGFR mAb, and 83% of Immune tumors for immunotherapy.

## Relevance to Drug-Response POC

- This paper is a direct analysis-flow template for the user's POC because it repeatedly tests whether genomic features are sufficient or whether proteome/phosphoproteome signals better represent targetable activity.
- CDK4/6 example: do not stop at `CDKN2A/CCND1 altered`; add Rb protein/phospho-Rb and cell-cycle activity to identify likely CDK4/6 dependence.
- EGFR example: do not stop at `EGFR amplified` or EGFR protein abundance; compare ligand expression, receptor phosphorylation, downstream pathway phosphosites, and external response data.
- Immunotherapy example: low immune infiltration may reflect CN deletion of immune regulators and APM failure, while immune-hot states may require multi-checkpoint profiling rather than a single PD-L1 marker.
- Practical POC figure: `genomic alteration -> target protein abundance -> phosphosite/pathway activity -> external or internal response phenotype` with discordant cases highlighted.

## Limitations and Caveats

- The main CPTAC cohort is treatment-naive and treatment hypotheses are inferred, with external PDX/trial datasets used for partial support.
- Bulk profiling cannot fully resolve tumor-cell versus microenvironmental origins of immune and stromal features.
- HNSCC site, smoking, sex, geography, and tumor composition are confounders that should be considered when transferring signatures.
- Some treatment candidacy rules are proposed biomarker logic, not prospective clinical validation.

## Data Availability

- Raw proteomics data: CPTAC Data Portal and Proteomic Data Commons.
- Genomic/transcriptomic data: Genomic Data Commons.
- Processed data: LinkedOmics, CPTAC-HNSCC.
- Software/code: CNVEX, Philosopher, TMT-Integrator, NeoFlow, PepQuery, and other tools listed in STAR Methods.

## Connections

- [Drug Response Proof-of-Concept with Global Proteome, Phosphoproteome, and Somatic SNV](../analyses/drug-response-poc-global-phospho-somatic-snv.md)
- [Cancer Multiomics Literature Monitor](../topics/cancer-multiomics-literature.md)
- [PTM Correction and Kinase Signaling in Cancer Proteomics](../topics/ptm-correction-and-kinase-signaling-in-cancer-proteomics.md)
- [Immunotherapy Resistance and Immune Evasion](../topics/immunotherapy-resistance-and-immune-evasion.md)
- [Huang 2021 - HPV-Negative HNSCC Proteogenomics](../analyses/cancer-multiomics-literature/huang-2021-hnscc-proteogenomics.md)
- [Proteogenomic characterization reveals therapeutic vulnerabilities in lung adenocarcinoma](./gillette-2020-proteogenomic-characterization-reveals-therapeutic-vulnerabilities.md)

## Sources

- Local PDF: `raw/inbox/papers/huang-2021-proteogenomic-insights-biology-treatment-hpv-negative.pdf`
