---
title: "Proteogenomic analysis of the CALGB 40601 (Alliance) HER2+ breast cancer neoadjuvant trial reveals resistance biomarkers"
authors:
  - Jaehnig
  - Fernandez-Martinez
  - Vashist
year: 2025
journal: "Cell Reports Medicine"
doi: "10.1016/j.xcrm.2025.102154"
pmid: "40480221"
pmcid: "PMC12208316"
paper_kind: clinical-trial-proteogenomic
cancer_types:
  - HER2-positive-breast-cancer
  - breast-cancer
modalities:
  - WES
  - RNA-seq
  - TMT-proteomics
  - TMT-phosphoproteomics
  - IHC
themes:
  - neoadjuvant-therapy
  - anti-HER2-response
  - pCR
  - resistance-biomarkers
  - proteogenomics
  - phosphoproteomics
  - tumor-microenvironment
tags:
  - drug-response
  - HER2-positive-breast-cancer
  - proteomics
  - phosphoproteomics
  - neoadjuvant
  - pmid-40480221
pdf: "raw/inbox/papers/jaehnig-2025-proteogenomic-analysis-calgb-40601-alliance.pdf"
topic: cancer-multiomics-drug-response
batch_ingest_status: pdf-text-extracted
batch_ingested_on: 2026-05-13
ingest_status: full-text-read
ingested_on: 2026-05-13
cm_axis: phospho
---
# Proteogenomic Analysis of the CALGB 40601 (Alliance) HER2+ Breast Cancer Neoadjuvant Trial Reveals Resistance Biomarkers

Jaehnig et al. reanalyze pretreatment biopsies from the CALGB 40601 randomized neoadjuvant anti-HER2 trial with DNA, RNA, proteome, and phosphoproteome layers, identifying false HER2-positive cases, protein-level resistance pathways, immune/cell-cycle response signals, and reproducible non-pCR markers GPRC5A and TPBG.

## Full PDF Deep-Dive Status

- Status: `full-text-read` on 2026-05-13.
- Local PDF: `raw/inbox/papers/jaehnig-2025-proteogenomic-analysis-calgb-40601-alliance.pdf`.
- PDF identity checked against title, author, journal, DOI, and 22-page PDF metadata.
- Correct DOI: `10.1016/j.xcrm.2025.102154`. Earlier placeholder DOI/PMC links on this page were wrong and are superseded.

## Key Points

- CALGB 40601 randomized stage II/III HER2+ breast cancer patients to paclitaxel plus trastuzumab (TH), lapatinib (TL), or trastuzumab plus lapatinib (THL). The full trial accrued 305 patients; pCR rates were 57% for THL, 45% for TH, and 30% for TL, with TL closed early for lower efficacy.
- This proteogenomic substudy received 218 OCT-embedded core needle biopsies from 117 patients, but only 80 biopsies from 54 patients passed QC for proteogenomic analysis. The high failure rate mainly reflected low tumor content or inadequate material.
- Of the 80 QC-passed biopsies, 75 yielded TMT proteome/phosphoproteome, 67 yielded WES, and 52 yielded QC-passed RNA-seq. RNA covered about 21,500 genes; proteomics identified peptides from about 11,000 genes; phosphopeptides covered about 5,000 genes.
- Six samples from four patients lacked ERBB2 amplification by WES and had low HER2 RNA, protein, or phosphorylation. These were associated with absence of pCR, suggesting false-positive clinical HER2 assignment or clinically relevant heterogeneity.
- Combining CALGB 40601 with the DP1 HER2+ proteogenomics dataset, 5 of 68 cases were potential false HER2 positives, all without pCR, with Fisher exact p = 0.04. Central HER2 IHC supported low HER2 in these cases.
- After excluding cases without proteogenomic evidence of ERBB2 amplification, protein-level pathway analysis in the THL arm showed ECM-receptor interaction, extracellular-structure organization, connective tissue development, collagen processes, and TGFB2 higher in non-pCR cases.
- In trastuzumab-containing arms, EMT, angiogenesis, myogenesis, apical junction, and WNT-beta-catenin were higher in non-pCR mainly at protein level. Cell-cycle and immune pathways were higher in pCR tumors.
- PTM-SEA nominated pCR-associated cell-cycle phosphosite signatures including nocodazole-perturbed sites and AURKB, CDK2, and DYRK2 targets. Non-pCR-associated phosphosite sets included GSK3A/B, PKACA, PKCE, PRKD, JNK1, AMPKA1, and CDK5 targets.
- Immune profiling showed the RNA-level IgG signature was reproduced at RNA and protein levels. BayesDeBulk found a protein-based CD8 T-cell signature significantly lower in non-pCR than pCR.
- Cross-proteomic validation using DP1 and Debets HER2+ neoadjuvant datasets nominated 24 reproducible proteins; four remained significant in all three proteomic datasets: **GPRC5A**, **TPBG/5T4**, **NEU1**, and **SP140L**.
- TPBG protein by MS was independently supported by IHC: tumors with IHC score 2/3 had higher MS TPBG than tumors scored 0/1.
- RNA meta-analysis across four clinical-trial datasets and ten anti-HER2 neoadjuvant regimens confirmed higher non-pCR expression for GPRC5A (p = 0.00016) and TPBG (p = 0.000081), while HER2 expression was lower in non-pCR (p = 0.0072).
- Combined GPRC5A + TPBG - ERBB2 RNA signatures reached AUROC 0.741 in CHER-LOB trastuzumab arms, 0.776 in I-SPY2 trastuzumab-treated samples, and 0.79 in I-SPY2 neratinib-treated HER2+ samples.

## Detailed Evidence

### Trial and Omics Design

- CALGB 40601 tested 16 weeks of weekly paclitaxel plus trastuzumab, lapatinib, or both. The trial is registered as NCT00770809.
- Pretreatment research biopsies were available from the clinical trial, and this study used microscaled proteogenomic methods for OCT frozen core biopsies.
- Protein/phosphosite expression was reported as TMT intensity ratios to a common reference. Samples were analyzed in TMT16 plexes, with 15 biopsy channels plus a common reference channel.
- Proteomics used nLC-1200 coupled to Thermo Lumos instrumentation. Phosphopeptides were enriched using Fe(III)-NTA cartridges.
- Phosphosite single-sample activity used ssGSEA2.0/PTM-SEA with PTMSigDB; pathway enrichment used WebGestalt/GSEA on signed p values from limma models.

### HER2 Proteogenomic QC

- All patients entered the trial as clinically HER2+, but WES/proteome/phosphoproteome found a subset without ERBB2 amplification and without HER2 overexpression.
- ERBB2 copy-number ratios correlated with HER2 protein levels (Spearman rho = 0.57, p = 1.3e-6).
- Samples without ERBB2 amplification had low HER2 RNA, protein, and/or phosphorylation and were non-pCR.
- The authors caution that intratumoral heterogeneity may explain some discordance because proteogenomics and diagnostic IHC used different biopsies, but central IHC also supported lack of HER2 in several cases.
- For biomarker discovery in confirmed HER2+ tumors, four CALGB 40601 cases lacking proteogenomic ERBB2 amplification evidence were excluded.

### Resistance and Response Pathways

- In THL samples, protein-level non-pCR pathways included ECM-receptor interaction, extracellular-structure organization, connective tissue development, collagen metabolic process, and TGFB2.
- Immune-related pathways were lower in non-pCR at both RNA and protein levels, consistent with prior CALGB 40601 RNA analyses.
- PTM-SEA in the THL arm showed CDK4 target and nocodazole-related phosphosite signatures higher in pCR, and PAK1 targets enriched in non-pCR.
- In combined trastuzumab-containing arms, EMT/WNT/angiogenesis/myogenesis/apical-junction pathways were higher in non-pCR mostly at protein level, while cell-cycle and immune pathways were higher in pCR.
- pCR phosphosite signatures included AURKB, CDK2, and DYRK2 targets; non-pCR phosphosite signatures included GSK3A/B, PKACA, PKCE, PRKD, JNK1, AMPKA1, and CDK5 targets.

### Immune Microenvironment

- Protein immune modulator scores, ESTIMATE, CIBERSORT, xCell, IgG signature, ICI target RNA/protein/phosphoprotein, BayesDeBulk, and CD3 IHC were compared.
- The IgG signature previously reported at RNA level was significant at both RNA and protein levels in this smaller proteogenomic subset.
- BayesDeBulk CD8 T-cell protein signature was significantly lower in non-pCR than pCR.
- The BDB CD8 signature positively correlated with interferon/allograft protein scores and with HIPK2 and paclitaxel-perturbed phosphosite signatures. It anti-correlated with TGF-beta/Hedgehog protein scores and PRKD1/PRKCE phosphosite activity.
- CD3 IHC correlated with immune-modulator protein scores but did not significantly separate pCR and non-pCR, likely because both groups were heterogeneous and sample size was limited.

### Biomarker Validation

- CALGB 40601 and DP1 protein data were compared using differential analysis accounting for clinical covariates where available. Candidate proteins also remained significant after tumor purity adjustment.
- Four proteins were significant in CALGB 40601, DP1, and Debets et al.: GPRC5A, TPBG, NEU1, and SP140L. GPRC5A, TPBG, and NEU1 were higher in non-pCR; SP140L was lower in non-pCR.
- GPRC5A and TPBG were the most robust in larger RNA validation: both were higher in non-pCR and associated with worse OS in the highest-expression quartile in the full CALGB 40601 RNA data.
- GPRC5A and TPBG protein levels correlated with PRKD1/PRKCE activity and were negatively associated with the BDB T-cell signature, suggesting resistance biology beyond simple HER2 or ESR1 abundance.

## Relevance to Drug-Response POC

- This is a strong template for **target-abundance and diagnostic-QC figures**. The paper shows that nominal clinical HER2 positivity can be biologically weak when ERBB2 CNA, HER2 RNA/protein, and HER2 phosphorylation disagree, and those cases fail to achieve pCR.
- For the user's dataset, a useful first figure would compare clinical target status or SNV label with actual drug target protein abundance and phospho-activation status.
- The paper supports a `response biology is not only target expression` message: confirmed HER2+ non-pCR tumors showed EMT/ECM/WNT/TGF-beta/PRKD/GSK3-type resistance states, while pCR tumors showed immune and cell-cycle phosphosite activity.
- GPRC5A and TPBG are examples of reproducible resistance biomarkers that are membrane-associated and translationally targetable; they illustrate how proteomics can nominate alternative targets after standard therapy fails.
- For phosphoproteome modeling, Jaehnig 2025 provides candidate kinase-feature classes to test: pCR-associated AURKB/CDK2/DYRK2 activity versus non-pCR-associated GSK3/PKC/PRKD/JNK/AMPK/CDK5 signatures.

## Limitations and Caveats

- The sample size per treatment arm is limited, creating type II error risk and making cross-cohort validation essential.
- Many biopsies failed QC, showing that small clinical core-biopsy proteogenomics needs strict sample handling and tumor-content thresholds.
- TPBG and GPRC5A are reproducible association markers, but their mechanistic role in anti-HER2 resistance requires model-system validation.
- Protein MS translation to clinical deployment remains technically specialized.

## Data Availability

- Genomics and transcriptomics: dbGaP `phs003576.v1.p1`.
- Proteomics: NCI PDC `PDC000582`.
- Phosphoproteomics: NCI PDC `PDC000583`.
- Processed data: Table S2A-E for CNA, mutation, RNA, global proteome, and phosphosite abundance.
- Code for systems biology analysis is available on request.

## Connections

- [Drug Response Proof-of-Concept with Global Proteome, Phosphoproteome, and Somatic SNV](../analyses/drug-response-poc-global-phospho-somatic-snv.md)
- [Drug Response Phospho-Global Proteomics Corpus Queue](../analyses/drug-response-phospho-global-100-corpus-queue.md)
- [Drug Response Phospho-Global 100-PDF Bulk Ingest](../analyses/drug-response-phospho-global-100-bulk-ingest.md)
- [Cancer Multiomics Proteogenomic Atlas](../topics/cancer-multiomics-literature.md)
- [PTM Correction and Kinase Signaling in Cancer Proteomics](../topics/ptm-correction-and-kinase-signaling-in-cancer-proteomics.md)

## Open Questions

- Can GPRC5A and TPBG protein assays be converted into practical IHC or targeted-MS biomarkers for anti-HER2 escalation?
- Does the GPRC5A/TPBG/PRKD/T-cell axis causally mediate resistance or mark a broader resistant tumor state?
- In a somatic SNV + global proteome + phosphoproteome POC, how often do target protein/phosphosite measurements contradict the clinical or genomic treatment label?
- Would confirmed HER2-amplified, HER2-protein-high tumors with high TPBG/GPRC5A preferentially benefit from ADC or immune-combination escalation?

## Sources

- Local PDF: `raw/inbox/papers/jaehnig-2025-proteogenomic-analysis-calgb-40601-alliance.pdf`
- DOI: <https://doi.org/10.1016/j.xcrm.2025.102154>
- PubMed: <https://pubmed.ncbi.nlm.nih.gov/40480221/>
- PMCID recorded in source metadata: `PMC12208316`

## 함께 인용된 논문

위키 분석·합성 페이지에서 이 논문과 함께 인용된 논문들 (co-citation).

- [[holt-2025-proteogenomic-characterization-unveils-biomarkers-associated|Holt 2025]]
- [[lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc|Lee 2026]]
- [[anurag-2022-proteogenomic-markers-chemotherapy-resistance-response|Anurag 2022]]
- [[chmielecki-2023-acquired-resistance-first-line-osimertinib|Chmielecki 2023]]
- [[sambath-2026-integrated-genomic-proteomic-cervical-cancer-chemoradiation-resistance|Sambath 2026]]
- [[gillette-2020-proteogenomic-characterization-reveals-therapeutic-vulnerabilities|Gillette 2020]]
- [[hsu-2025-phosphoproteomics-osimertinib-tolerant-persister-cells-reveals|Hsu 2025]]
- [[huang-2021-proteogenomic-insights-biology-treatment-hpv-negative|Huang 2021]]
- [[petralia-2024-pan-cancer-proteogenomics-characterization-tumor-immunity|Petralia 2024]]
- [[song-2024-proteogenomic-analysis-reveals-non-small-cell|Song 2024]]
