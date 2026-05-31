---
title: "A proteogenomic portrait of lung squamous cell carcinoma"
authors:
  - "Satpathy"
  - "Krug"
  - "Jean"
year: 2021
journal: "Cell"
paper_kind: proteogenomic-atlas
cancer_types:
  - lung-squamous-cell-carcinoma
  - non-small-cell-lung-cancer
modalities:
  - whole-genome-sequencing
  - whole-exome-sequencing
  - copy-number
  - dna-methylation
  - rna-seq
  - mirna-seq
  - global-proteomics
  - phosphoproteomics
  - acetylomics
  - ubiquitylomics
  - immunohistochemistry
  - immune-deconvolution
themes:
  - cptac
  - kinase-signaling
  - rtk-signaling
  - cdk4-6-rb
  - nrf2
  - sox2-tp63
  - immune-landscape
  - ptm-crosstalk
  - therapeutic-vulnerability
tags:
  - ptmanchor
  - cancer-resistance
  - drug-response
  - proteomics
  - phosphoproteomics
  - ptm
  - cancer-proteomics
pmid: "34358469"
pmcid: "PMC8475722"
doi: "10.1016/j.cell.2021.07.016"
pdf: "raw/inbox/papers/satpathy-2021-proteogenomic-portrait-lung-squamous-cell.pdf"
corpus_role: core-proteogenomic-vulnerability
ingest_status: full-text-read
ingested_on: 2026-05-13
topic: cancer-multiomics
cm_axis: phospho
---
# A Proteogenomic Portrait of Lung Squamous Cell Carcinoma

Satpathy et al. provide a CPTAC lung squamous cell carcinoma (LSCC) atlas where WGS/WES, copy number, methylation, RNA, global proteome, phosphoproteome, acetylome, and a K-GG ubiquitylome subset are used to convert recurrent genomic lesions into functional pathway, PTM, immune, and therapeutic-vulnerability hypotheses.

## Full-Text Read Status

- Status: `full-text-read` on 2026-05-13.
- Local PDF: `raw/inbox/papers/satpathy-2021-proteogenomic-portrait-lung-squamous-cell.pdf`.
- PDF identity checked against title, journal, DOI, and full STAR Methods.
- Scope: this note is curated from the local PDF text, including main results, discussion, data availability, and mass-spectrometry methods.

## Key Points

- The cohort contains 108 treatment-naive primary LSCC tumors and 99 paired normal-adjacent tissues (NATs) after pathology exclusions from 113 collected participants.
- Proteome/phosphoproteome/acetylome were profiled across 22 TMT11 plexes with a common reference; K-GG ubiquitylome profiling was performed on a material-limited subset.
- Quantified scale: 11,575 global proteins for RNA-protein comparison, 68,674 VM-site-polished phosphosites, 15,186 acetylsites, and 25,489 ubiquitylsites.
- Multi-omic NMF across CNA, RNA, protein, phosphosite, and acetylsite layers produced five LSCC states: basal-inclusive, EMT-enriched, classical, inflamed-secretory, and proliferative-primitive.
- Several therapeutic lessons are functional rather than mutation-only: NSD3 is nominated over FGFR1 in the 8p11.23 amplicon; phospho-Rb refines CDK4/6 candidacy; EGFR ligand abundance may be more useful than EGFR amplification for EGFR activity; and TP63-low tumors nominate survivin/BIRC5 inhibition.
- Immune analysis separates Hot, Warm, Cold, and NAT-enriched states; Hot tumors show checkpoint/IDO1/FOXP3 expression and CSF1R-centered phosphoproteomic signals, while Warm/Cold retain canonical Wnt features.

## Cohort and Assay Design

- Human subjects: 113 participants, ages 40-88, from 13 tissue source sites in seven countries; 108 tumors and 99 paired NATs were used after excluding five samples.
- Samples were prospectively collected from newly diagnosed LSCC patients undergoing surgical resection with no prior chemotherapy or radiotherapy.
- LSCC diagnosis was confirmed by at least two expert pathologists; low-TP63 cases received additional pathology confirmation.
- Genomics/transcriptomics: WES, WGS, EPIC methylation array, total RNA-seq, and miRNA-seq.
- Proteomics: about 50 mg cryopulverized tissue was digested, TMT11-labeled, fractionated, and analyzed by LC-MS/MS.
- Mass-spec instrumentation: Q Exactive HF-X for proteome and acetylproteome; Orbitrap Fusion Lumos for phosphoproteome and ubiquitylproteome.
- Data filtering removed features missing in more than 70% of samples, with stricter 50% presence thresholds for selected marker and enrichment analyses.

## CNA, Methylation, and Driver Interpretation

- CNA cis analysis found 5,523 significant CNA-mRNA events, of which 2,154 were concordant at protein level, including 138 cancer-associated genes.
- The 8p11.23 amplicon contains FGFR1 and WHSC1L1/NSD3, but proteomic and functional triangulation nominate NSD3 as a more plausible driver than FGFR1, helping explain why FGFR1-directed LSCC trials have been disappointing.
- CNA trans-effect analysis combined protein-level trans signatures with Connectivity Map queries. IL18 and NR2F6 were highlighted because their copy-number states correlated with protein abundance and immune-score relationships.
- DNA methylation analysis identified genes whose methylation cascaded through mRNA, protein, and PTM layers; examples include FAM110A, PTGES3, PLAU, and SLC16A3.

## Multi-Omic Subtypes

- Basal-inclusive (B-I): basaloid histology; metabolic, immune, and estrogen receptor signaling; TACSTD2/TROP2 and PBX3 signals; neutrophil activation/degranulation.
- EMT-enriched (EMT-E): EMT, angiogenesis, myogenesis, myxoid histology, fibroblast infiltration, VCAN/FHL3, Wnt-related DVL3/FN1/FHL2, and LINCS reversal by TGF-beta inhibitors.
- Classical: KEAP1/CUL3/NFE2L2 alterations, SOX2/TP63 amplification, classical histology, CIMP-high methylation, OXPHOS/proliferation, and low immune signaling.
- Inflamed-secretory (I-S): overlaps the secretory RNA subtype and immune Hot state.
- Proliferative-primitive (P-P): proliferation up and immune signaling down.
- Tumors with low NMF membership scores were labeled "mixed" and had worse survival, with SOX2 amplification enriched in that group.

## RTK and EMT Phosphoproteome

- The authors derived a correlation-based phosphosite enrichment (CBPE) score for receptor tyrosine kinases using RTK protein abundance, cognate protein abundance, and optional purity adjustment.
- Nine RTKs passed the tumor CBPE threshold; seven were subtype-associated.
- PDGFRB and ROR2 CBPE scores were high in EMT-E tumors and correlated with extracellular matrix, cell migration, and epithelial-junction-loss programs.
- The ROR2/PDGFRB result nominates non-canonical Wnt/planar-cell-polarity and calcium-dependent branches as LSCC EMT vulnerabilities, but the paper frames this as hypothesis-generating.

## CDK4/6-Rb Axis

- CDKN2A/RB1 pathway interpretation is not resolved by mutation or copy number alone.
- RB1-mutated tumors upregulated cell-cycle proteins.
- CDKN2A alterations required isoform-level interpretation because p16 and p14 can move differently; homozygous deletion removes both isoforms, while some wild-type tumors suppress p16 through methylation or other mechanisms.
- Samples retaining high CDKN2A/p16 often had RB1 mutation/deletion or low Rb protein, consistent with mutual exclusivity in functional pathway loss.
- CCND1 amplification increased mean Rb protein and phospho-Rb, but distributions overlapped.
- Phospho-Rb abundance correlated with CDK4/6 inhibitor response in LSCC cell lines, arguing that trials should evaluate downstream Rb protein/phosphorylation state rather than excluding the class from genomic marker failures alone.

## NRF2 and Oxidative-Stress State

- The paper grouped alterations in NFE2L2/NRF2, CUL3, and KEAP1 as an NRF2-pathway mutated class.
- NRF2-pathway mutant tumors showed concordant mRNA, protein, and phosphoprotein changes; two-hit tumors showed a dosage effect for several markers including SQSTM1, NR0B1, AKR1B10, CARD11, and FFAR2.
- NRF2 activity scores were also high in some non-mutant tumors, especially in the classical subtype.
- NFE2L2 phosphorylation was elevated; CDK5 protein and PTM-SEA activity were higher in classical tumors, nominating a possible CDK5-mediated NRF2 activation route.
- Unlike LUAD, KEAP1 mutation in this LSCC cohort did not significantly reduce KEAP1 protein expression.

## Chromosome 3q, TP63, SOX2, and Survivin

- 3q amplification was a dominant LSCC feature; TP63 was among the most elevated tumor-associated proteins.
- DNp63alpha was the dominant TP63 isoform and tracked TP63 mRNA/protein. TP63 amplification was associated with better TCGA survival, but a small TP63-low LSCC subset existed despite histologic confirmation.
- TP63-low tumors overexpressed BIRC5/survivin, and TP63-low LSCC cell lines were more sensitive to YM-155 in supporting analyses.
- SOX2 amplification/overexpression connected to chromatin regulators and stem-like programs, including LSD1/KDM1A, KDM3A, EZH2, ALDH1A1, ALDH3A1, and WNT5A.
- SOX2 abundance was negatively associated with JAK1/IRF3/IFNGR1 and JAK-STAT signaling, supporting an immune-suppression hypothesis around SOX2-high disease.

## PTM Crosstalk and Metabolism

- Protein-corrected K-GG clustering identified two ubiquitylproteome clusters linked to geography/ethnicity and pathways including glycolysis, JAK-STAT, MAPK, and immune signaling.
- HERC5 had hundreds of positive K-GG correlations and tracked ISG15 and IFN-gamma, suggesting that many K-GG signals may represent ISGylation-like biology rather than degradation.
- Structural clustering of acetylation and ubiquitylation sites highlighted metabolic enzymes and redox regulation.
- Tumors showed decreased acetylation at inhibitory PGK1 and PKM sites, increased activating phosphorylation such as PFKFB3 S461 and PKM S37, and decreased TXN1 ubiquitylation with high TXN/TXNRD1 in classical/NRF2 tumors.
- RAN K127 acetylation was elevated in the P-P subtype, illustrating subtype-specific PTM crosstalk.

## Immune Landscape

- xCell-based immune/stromal clustering generated Hot, Warm, Cold, and NAT-enriched states.
- The I-S NMF subtype was strongly associated with immune Hot tumors.
- Hot tumors were enriched for macrophages, CD4/CD8 T cells, Tregs, dendritic cells, and immune pathways; CTLA4, PD-1/PDCD1, PD-L1/CD274, IDO1, and FOXP3 were elevated.
- Hot tumor acetylproteome was enriched for OXPHOS, mitochondrial, and TCA features. ARHGDIB/RhoGDIb K135 acetylation was a top signal and localized by IHC to infiltrating immune and mesenchymal cells.
- Warm tumors showed PD-1 signaling, IFN-gamma response, and allograft rejection features relative to Cold, but lacked the cell-cycle downregulation seen in Hot tumors.
- CSF1R had the strongest immune-associated RTK CBPE signal and correlated with CCL5, PIK3R1 Y580, WAS/WASF2 S103, and AKAP13, nominating macrophage/CSF1R biology and cytoskeletal phosphosignaling as immune-evasion axes.

## Cross-Cancer and Therapeutic Lessons

- LSCC had more frequent CNAs than LUAD or HNSCC, with immune-related deletions tied to immune-score variation.
- Squamous cancers shared 3q amplification, JAK2 deletion, and skin-development protein programs.
- LSCC-specific deletions included 4p14/5q regions containing Toll-like receptor and interleukin genes.
- Cross-cancer phosphoproteomics nominated activating sites on 27 kinases, including targetable MAPK14 and DCK/EGFR/SRC-related axes.
- EGFR protein abundance was higher in squamous cancers than LUAD, but EGFR amplification did not track PROGENy EGFR activity; EGFR ligand abundance correlated better with EGFR activity, a useful lesson for target-response feature design.

## Relevance to Drug-Response Global/Phospho/Somatic SNV POC

- This paper is a strong template for not stopping at somatic driver calls. CDKN2A, CCND1, RB1, KEAP1/CUL3/NFE2L2, TP63, SOX2, and FGFR1/NSD3 all need protein and PTM state to become treatment hypotheses.
- For CDK4/6 inhibitors, use a ladder of `CDKN2A/RB1/CCND1 alteration -> Rb protein -> phospho-Rb -> response`, because phospho-Rb may better reflect functional CDK4/6 dependency than upstream events.
- For EGFR/RTK therapy logic, test `target amplification/protein abundance -> ligand abundance -> RTK/CBPE or kinase activity -> response`, since amplification alone may fail.
- For immune resistance, include proteome/phosphoproteome immune-state features such as Hot/Warm/Cold, IFN-gamma, checkpoint abundance, CSF1R CBPE, Wnt signaling, antigen-presentation related deletions if CNA is available, and SOX2/JAK-STAT inverse relationships.
- For NRF2/oxidative-stress resistance, compare mutation-defined NRF2 pathway status with NRF2 activity and phosphosite-derived CDK5/NRF2 activation; non-mutant high-activity tumors are a key class for phosphoproteomic added value.
- For EMT/TME-driven resistance, PDGFRB/ROR2 CBPE, fibroblast/ECM proteins, and TGF-beta reversal signatures give a model for protein/phospho-defined bypass states.

## Limitations

- The study is primarily an atlas of treatment-naive primary tumors, so most therapeutic claims are hypotheses rather than direct clinical response validation.
- Bulk profiling limits cell-type assignment; the authors explicitly note tumor heterogeneity and point to microdissection, single-cell, mass spectrometry imaging, or mass cytometry as future directions.
- Ubiquitylproteome profiling used a smaller subset because of material requirements, so K-GG results should not be treated as full-cohort equivalent.
- Metastatic biology is not directly captured because paired metastatic lesions were not profiled.

## Data Availability

- LSCC proteomics data are listed at PDC identifiers `PDC000232`, `PDC000233`, `PDC000234`, and `PDC000237`.
- Genomic and transcriptomic files are at GDC/dbGaP accession `phs001287.v10.p5`.
- CPTAC data portal study: LSCC `S063`.
- Processed sample annotation and normalized data are in supplementary Tables S1-S3.

## Connections

- [Drug Response Proof-of-Concept with Global Proteome, Phosphoproteome, and Somatic SNV](../analyses/drug-response-poc-global-phospho-somatic-snv.md)
- [Drug Response Phospho/Global 100-Paper Bulk Ingest Tracker](../analyses/drug-response-phospho-global-100-bulk-ingest.md)
- [Ptmanchor Topic Hub](../topics/ptm-correction-and-kinase-signaling-in-cancer-proteomics.md)
- [Cancer Multiomics Proteogenomic Atlas](../topics/cancer-multiomics-literature.md)
- [Proteogenomic characterization reveals therapeutic vulnerabilities in lung adenocarcinoma](gillette-2020-proteogenomic-characterization-reveals-therapeutic-vulnerabilities.md)
- [Proteogenomics of Non-smoking Lung Cancer in East Asia](chen-2020-proteogenomics-non-smoking-lung-cancer-east.md)
- [Proteogenomic insights into the biology and treatment of HPV-negative head and neck squamous cell carcinoma](huang-2021-proteogenomic-insights-biology-treatment-hpv-negative.md)

## Sources

- Local PDF: `raw/inbox/papers/satpathy-2021-proteogenomic-portrait-lung-squamous-cell.pdf`
- DOI: `10.1016/j.cell.2021.07.016`
- PMID: `34358469`
- PMCID: `PMC8475722`

## 함께 인용된 논문

위키 분석·합성 페이지에서 이 논문과 함께 인용된 논문들 (co-citation).

- [[gillette-2020-proteogenomic-characterization-reveals-therapeutic-vulnerabilities|Gillette 2020]]
- [[huang-2021-proteogenomic-insights-biology-treatment-hpv-negative|Huang 2021]]
- [[cao-2021-proteogenomic-characterization-pancreatic-ductal-adenocarcinoma|Cao 2021]]
- [[zhang-2022-proteogenomic-characterization-2002-human-cancers|Zhang 2022]]
- [[chmielecki-2023-acquired-resistance-first-line-osimertinib|Chmielecki 2023]]
- [[dou-2020-proteogenomic-characterization-endometrial-carcinoma|Dou 2020]]
- [[holt-2025-proteogenomic-characterization-unveils-biomarkers-associated|Holt 2025]]
- [[jaehnig-2025-proteogenomic-analysis-calgb-40601-alliance|Jaehnig 2025]]
- [[lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc|Lee 2026]]
- [[li-2023-pan-cancer-proteogenomics-connects-oncogenic-drivers|Li 2023]]
