---
title: "Proteogenomics of Non-smoking Lung Cancer in East Asia Delineates Molecular Signatures of Pathogenesis and Progression"
authors:
  - "Chen"
  - "Roumeliotis"
  - "Chang"
year: 2020
journal: "Cell"
doi: "10.1016/j.cell.2020.06.012"
pmid: "32649875"
paper_kind: proteogenomic-atlas
cancer_types:
  - lung-adenocarcinoma
  - non-small-cell-lung-cancer
modalities:
  - whole-exome-sequencing
  - rna-seq
  - global-proteomics
  - phosphoproteomics
  - immune-deconvolution
  - immunohistochemistry
themes:
  - egfr
  - mapk-signaling
  - proteomic-subtypes
  - phosphoproteomics
  - tumor-progression
  - immune-evasion
  - apobec
  - druggable-targets
tags:
  - cancer-multiomics
  - drug-response
  - ptmanchor
  - proteomics
  - phosphoproteomics
  - lung-cancer
corpus_role: core-proteogenomic-vulnerability
ingest_status: full-text-read
ingested_on: 2026-05-13
pdf: "raw/inbox/papers/chen-2020-proteogenomics-non-smoking-lung-cancer-east.pdf"
---
# Proteogenomics of Non-Smoking Lung Cancer in East Asia

Chen et al. build a deep proteogenomic map of treatment-naive, predominantly early-stage, non-smoking lung adenocarcinoma from Taiwan. For the drug-response POC, the strongest reusable ideas are EGFR/KRAS/TP53 mutation-to-phosphosite interpretation, proteome-based staging beyond clinical stage, and APOBEC/immune-context stratification.

## Full-Text Read Status

- Status: `full-text-read` on 2026-05-13.
- Local PDF identity verified against title, Cell 2020 journal metadata, DOI `10.1016/j.cell.2020.06.012`, and 37-page local PDF.
- Evidence boundary: all scientific claims below come from the local PDF `raw/inbox/papers/chen-2020-proteogenomics-non-smoking-lung-cancer-east.pdf`.

## Key Points

- The proteogenomics cohort includes patient-matched tumor and NAT from 103 treatment-naive Taiwanese patients; 83% were non-smokers, 58% female, median age was 63 years, and 80% were stage IA/IB.
- In the adenocarcinoma group (n=91), WES identified 23,145 nonsynonymous somatic SNVs. RNA-seq quantified 30,155 RNAs. Isobaric labeling quantified more than 10,000 proteins and more than 20,000 phosphosites.
- EGFR mutations occurred in 85% of patients, followed by TP53 in 33% and RBM10 in 20%. RBM10 and EGFR-L858R were frequent in females, whereas KRAS and APC were more frequent in males; KRAS and ATM were prominent among patients with smoking history.
- RNA-to-protein correspondence was modest: median sample-wise Spearman correlation was 0.31, median gene-wise correlation was 0.14, and only 22% of proteins had significant positive correlation with cognate RNA.
- EGFR activating mutations correlated with increased EGFR S1064 and Y1197 phosphorylation. EGFR pY1197 correlated with MAP2K2 pT394 and MAPK3 pT198/T202, supporting a phosphosite-defined EGFR-MEK-ERK activity chain.
- MAPK activity varied across both EGFR-mutant and EGFR-WT tumors. KRAS-mutant EGFR-WT cases were often high-MAPK, while TP53 mutation and later stage coincided with lower MAPK activity.
- TP53 mutation was an eQTL/pQTL hotspot and associated with cell-cycle proteins, TOP2A, MCM complex proteins, lower KIT abundance, and higher phosphorylation of DNA condensation/recombination/damage-response proteins including ABRAXAS1 S406 and UIMC1 S101.
- Mutational signature analysis identified five profiles including APOBEC, deamination of 5-methylcytosine, tobacco-like, dibenz[a,j]acridine-like, and other environmental-agent-like signals. APOBEC-high status was enriched in females and younger patients.
- Proteomic subtyping identified early-stage tumors with late-stage-like proteomic features. Stage IB EGFR-L858R tumors were enriched in the late-like proteomic class, and an independent retrospective cohort showed inferior OS for stage IB EGFR-L858R versus EGFR-Del19.
- Protein network analysis nominated progression-associated matrix metalloproteinases, especially MMP11 and MMP7, whose strong IHC expression associated with poorer OS in an independent early-stage cohort.

## Cohort and Methods

- The proteogenomics cohort was prospectively collected at National Taiwan University Hospital between July 2016 and July 2018.
- Inclusion required newly diagnosed, treatment-naive patients undergoing primary surgery for lung adenocarcinoma. Patients with neoadjuvant chemotherapy or molecular targeted therapy were excluded.
- Qualified tissue required at least 60% tumor-cell nuclei and less than 20% necrosis.
- Validation cohorts included 134 FFPE specimens for MMP IHC validation and 208 completely resected stage IA/IB LUAD patients for EGFR-subtype survival analysis.
- Proteome analysis used TMT 10-plex labeling, high-pH RPLC, and UltiMate 3000 RSLCnano coupled to a Q Exactive HF.
- Phosphoproteome analysis used home-made IMAC StageTip enrichment and UltiMate 3000 RSLCnano coupled to an Orbitrap Fusion Lumos.
- Phosphosite analysis used ptmRS localization; phosphosite probability above 0.75 was treated as confident. Protein-corrected net phosphorylation was computed by regressing phosphosite log2T/N values against matched protein log2T/N values.

## Mutation-to-Protein and Phosphosite Interpretation

- Customized patient-specific mutation databases identified 337 mutated peptides corresponding to 319 proteins, including variant isoforms in 15 cancer driver genes.
- RBM10 truncating mutations had a systematic negative effect on RNA and protein levels.
- KRAS, LAMB1, and PIK3CA missense mutations associated with increased protein expression without the same RNA pattern, consistent with possible protein stability effects.
- EGFR activating mutations did not produce a simple total-protein abundance conclusion, but they did associate with EGFR phosphorylation at S1064 and Y1197.
- The EGFR-MEK-ERK phosphosite chain gives a strong POC template: mutation status should be followed by phosphosite-level pathway activity, not just receptor abundance.
- TP53 mutation-associated TOP2A and DNA damage phosphorylation suggest possible sensitivity hypotheses for topoisomerase or DNA-damage-targeted therapy, but this study uses public cell-line drug-response support rather than prospective patient treatment response.

## APOBEC, Environmental Signatures, and Immune Context

- APOBEC-high signature was present in 44% of patients, with higher prevalence in females than males.
- Younger females with EGFR-WT tumors were especially enriched for APOBEC-high signature.
- APOBEC3 family proteins were frequently upregulated in tumors, with APOBEC3F and APOBEC3G showing gender-specific protein differences not recapitulated at RNA level.
- Female APOBEC-high tumors showed higher DNA repair and replication protein abundance; phosphosite analysis nominated ATR T1989 and UIMC1 S101 among DNA damage/repair-related sites.
- Kinase enrichment in APOBEC-high females nominated Aurora B, CK2, CDK1, and CDK2 as activated kinase candidates.
- The paper also reports environmental-agent-like mutational signatures, including PAH/nitro-PAH/nitrosamine-like categories, with pathway enrichment in detoxification, ERBB/MAPK, DNA repair, and immune signaling processes.
- The paper links APOBEC-high status to external immunotherapy context: in an advanced NSCLC combination immunotherapy cohort, APOBEC-high status had marginally prolonged PFS. This is supportive context, not a direct treatment-response result from the Taiwanese cohort.

## Proteomic Subtypes and Progression

- Consensus clustering identified three proteomic subtypes, three RNA subtypes, and four phosphoproteomic subtypes after excluding small or unstable clusters.
- Proteomic subtype 1 was enriched for later stage tumors, visceral pleural invasion, TP53 mutations, and higher mutational burden.
- Proteomic subtype 2 consisted mainly of early-stage tumors without EGFR-L858R.
- Proteomic subtype 3 was enriched for stage IA and lacked TP53 mutations; it also showed higher phosphorylation in cancer, PI3K-AKT, and cell-cycle pathways, suggesting early activated signaling.
- Proteomics reclassified some stage IA/IB tumors into late-like classes. At stage IB, EGFR-L858R tumors were enriched in the late-like class, and all stage IB EGFR-L858R/TP53 double-mutant tumors were late-like.
- In an independent retrospective cohort, stage IB EGFR-L858R patients had significantly inferior overall survival compared with EGFR-Del19 patients, whereas stage IA did not show this difference.

## Protein Networks, Immune Features, and Druggable Targets

- WGCNA on 9,072 proteins quantified in at least 80% of adenocarcinoma patients produced 279 modules; 195 modules had significant annotation enrichment.
- A trimmed network contained 3,014 nodes and 44,665 edges, with a mean Pearson correlation of 0.63 and 28% of edges matching STRING interactions above score 0.4.
- Immune-related protein modules included IKZF1, IKZF3, NFATC1, and NFATC2 and were higher in subtype 3. These modules correlated with CIBERSORT RNA-based immune profiles.
- Antigen processing and presentation, especially MHC class II, was higher in subtype 3.
- A 65-protein upregulated druggable subnetwork included MMP2, MMP11, MMP12, and MMP14.
- MMP7, MMP11, and MMP12 were most upregulated in late and late-like classes; independent IHC validation linked strong MMP11 and MMP7 expression to poorer overall survival.

## Relevance to Drug-Response POC

- This paper supports a lung cancer POC ladder where `EGFR/KRAS/TP53 mutation -> target/bypass phosphosite activity -> proteomic subtype/progression state -> therapy hypothesis`.
- For EGFR-mutant lung cancer, use phosphosite-level EGFR-MEK-ERK activity rather than EGFR mutation status or EGFR protein abundance alone.
- EGFR-L858R versus Del19 should be treated as biologically distinct in early-stage LUAD. The proteomic late-like class suggests that the same clinical stage and same broad oncogene can still have different proteomic risk states.
- TP53 mutation can be modeled as a functional state rather than a binary covariate: link TP53 to cell-cycle protein abundance, TOP2A, DNA damage phosphosites, and possible etoposide/topoisomerase sensitivity hypotheses.
- APOBEC-high and immune/proteomic features provide a possible immunotherapy-sensitivity branch, but the evidence here is external and indirect.

## Limitations

- The main proteogenomics cohort is treatment-naive and surgical; most therapy conclusions are stratification or vulnerability hypotheses rather than direct drug-response findings.
- The cohort is geographically and demographically specific: Taiwanese, predominantly early-stage, non-smoking LUAD.
- Proteomic subtype-to-outcome inference is supported by independent retrospective cohorts, but not by randomized treatment assignment.
- APOBEC/immunotherapy association is drawn from external advanced NSCLC immunotherapy data and is reported as marginally significant.
- Tumor heterogeneity and variable tumor cellularity may influence subtype and pathway analyses.

## Data Availability

- Genomics and proteomics data: dbGaP `phs001954.v1.p1`.
- Proteomics/phosphoproteomics: NCI Proteomics Data Commons `PDC000219` and `PDC000220`.

## Connections

- [Drug Response Proof-of-Concept with Global Proteome, Phosphoproteome, and Somatic SNV](../analyses/drug-response-poc-global-phospho-somatic-snv.md)
- [Drug Response Phospho-Global 100-PDF Bulk Ingest](../analyses/drug-response-phospho-global-100-bulk-ingest.md)
- [Drug Response Phospho-Global Proteomics Corpus Queue](../analyses/drug-response-phospho-global-100-corpus-queue.md)
- [Cancer Multiomics Literature Monitor](../topics/cancer-multiomics-literature.md)
- [PTM Correction and Kinase Signaling in Cancer Proteomics](../topics/ptm-correction-and-kinase-signaling-in-cancer-proteomics.md)
- Cancer Multiomics summary: [Chen 2020 - Non-Smoking Lung Cancer Proteogenomics](../analyses/cancer-multiomics-literature/chen-2020-non-smoking-lung-cancer-proteogenomics.md)

## Sources

- Local PDF: `raw/inbox/papers/chen-2020-proteogenomics-non-smoking-lung-cancer-east.pdf`
