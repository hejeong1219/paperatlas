---
title: "Transcriptomic landscape of transposable elements reveals LTR7-PLAAT4 as a potential oncogene and therapeutic target in pancreatic adenocarcinoma"
authors:
  - "Shi M"
  - "Teng C"
  - "Zhang S"
  - "He X"
  - "Xu L"
  - "Han F"
  - "Wen R"
  - "Yu G"
  - "Liu J"
  - "Feng Y"
  - "Wu Y"
  - "Ren Y"
  - "Jin G"
  - "Li J"
year: 2026
journal: "Genome Research"
doi: "10.1101/gr.280528.125"
pdf: "raw/inbox/papers/shi-2026-transcriptomic-landscape-transposable-elements-reveals-ltr.pdf"
paper_kind: mechanistic
modalities:
  - rna-seq
  - atac-seq
  - immunopeptidomics
  - organoid
cancer_types:
  - pancreatic-adenocarcinoma
themes:
  - transposable-element
  - ltr7
  - plaat4
  - oncogene
  - onco-exaptation
  - lipid-droplet
  - neoantigen
  - foxm1
tags:
  - source
  - transposable-element
  - pancreatic-cancer
  - oncogene
  - immunopeptidomics
pdf_status: full-text-read
---
# Transcriptomic landscape of transposable elements reveals LTR7-PLAAT4 as a potential oncogene and therapeutic target in pancreatic adenocarcinoma

_Genome Research, 2026._

## Summary

Using 71 patient-derived pancreatic adenocarcinoma (PAAD) organoids — which achieve nearly 100% tumor purity, circumventing the desmoplastic-stroma contamination that plagues bulk PAAD sequencing — the authors map the transcriptomic landscape of transposable elements (TEs) and their fusion with host genes (onco-exaptation). Differential analysis found **7,413 upregulated and 871 downregulated TE copies** in PAADs, associated with more accessible chromatin (ATAC-seq) and enriched near metabolic genes. TEprof2 analysis identified **469 PAAD-specific TE-chimeric transcripts** and **16 TE-driven fusion events involving 15 known oncogenes**. The lead candidate, **LTR7-PLAAT4**, is present in 29% of PAAD organoids, correlates with poor overall survival, and predicts prognosis/treatment response more accurately than driver mutations or CA19-9/CEA markers. LTR7 sits ~7 kb upstream of the PLAAT4 promoter and acts as an alternative promoter driving two novel PLAAT4 isoforms; its activity is transcriptionally driven by **FOXM1** binding to the LTR7 promoter (validated by ChIP-PCR and motif-mutagenesis luciferase assays). Functionally, **LTR7-PLAAT4 isoform 2** enhances migration/invasion and reprograms lipid metabolism — raising phospholipase activity, cholesteryl-ester (CE) accumulation, and CE-rich lipid droplet formation mediated through **BSCL2** (seipin) co-expression. LTR7-PLAAT4-positive tumors show broad multidrug resistance in organoid drug screens. On the immunogenic front, HLA-I immunopeptidomics of AsPC-1 cells (12,234 peptides) and DAC13 organoids (11,380 peptides) found mutation-derived neoantigens nearly absent (only one CAPN2 peptide) but recovered TE-chimeric-transcript–derived peptides; the TEprof2-predicted peptide **FLIQHLPLV** (detected in ~27% of organoids, binds HLA-A*02:01) showed robust immunogenicity by T2 binding, MS spectral matching, and ELISPOT IFNG response. The work positions TE activity as both an oncogenic driver and a source of tumor-specific neoantigens in PAAD.

## Key Points

- **TEs are broadly activated in PAAD with open chromatin.** Differential analysis of 66 PAAD vs 5 normal pancreatic ductal organoids found **7,413 upregulated and 871 downregulated DETE copies** (fold-change ≥4, FDR < 0.05); of the upregulated DETEs, **36.4% were LINE and 35.8% SINE**, and **0.18% of the 770,551 LTR genomic copies** were upregulated. Upregulated DETEs were associated with more accessible chromatin (ATAC-seq) and enriched near metabolic genes (purine nucleotide / hormone metabolic processes). No association with gene mutations or tumor markers was found.
- **469 PAAD-specific TE-chimeric transcripts; 16 oncogene fusions.** TEprof2 yielded 469 PAAD-specific TE-chimeric transcripts from 3,513 high-confidence TE transcripts after a three-step filter (tumor-enrichment scoring + FANTOM5 benign-promoter removal). Most originated from intronic (77%) or partially exonic (15%) regions; the L1PA2 subfamily was notably enriched. **16 TE-driven fusion events involving 15 known oncogenes** (ONGene database) were identified across all major TE classes.
- **LTR7-PLAAT4 is the lead TE-oncogene, present in 29% of tumors and prognostic.** LTR7-PLAAT4 was present in **29% of PAAD organoids**, correlated with poor overall survival (log-rank), and **predicted prognosis and treatment response more accurately than driver mutations or preoperative markers (CA19-9, CEA)**. The fusion was also detected in **24% of pancreatic, 37% of esophageal, and 35% of intestinal** GI cancer cell lines.
- **LTR7 acts as an alternative promoter ~7 kb upstream of PLAAT4.** LTR7 lies ~7 kb upstream of the PLAAT4 promoter and initiated **two transcript isoforms** in tumor organoids. LTR7-PLAAT4-positive organoids showed higher ATAC-seq accessibility at LTR7. Isoform 2 was validated by nested PCR + Sanger sequencing in Capan-1 and SNU-16 cells but absent in hTERT-HPNE normal cells.
- **MER21B has a positive cis-regulatory effect on LTR7.** Luciferase assays showed MER21B alone (a TE fragment adjacent to the 5′ end of LTR7) had minimal promoter activity, but **MER21B had a positive cis-regulatory effect on LTR7 transcription**.
- **FOXM1 transcriptionally drives LTR7 promoter activity.** Among four LTR7-specific TF motifs (FOXM1/HNF-3alpha, TFAP2A, MAZ, ETV4), **FOXM1 was exclusively highly expressed in LTR7-PLAAT4-positive samples**. FOXM1 binding to LTR7 was validated by ChIP-PCR (CUT&RUN); mutating the FOXM1 (HNF-3alpha) site significantly reduced luciferase expression in both 293T and AsPC-1.
- **Isoform-specific oncogenic phenotypes.** In PANC-1 and AsPC-1, overexpressed canonical PLAAT4 and isoform 1 promoted **cell viability**, whereas **isoform 2 notably enhanced migration** (wound-healing, transwell) and invasion. PLAAT4 was noted as having recently emerged as an oncogene in pancreatic cancer, contrasting prior tumor-suppressor roles elsewhere.
- **Isoform 2 has an alternative start codon and higher phospholipase activity.** A robust alternative start codon within the LTR7 sequence alters the N-terminus of isoform 2 (validated by mass spectrometry after overexpression). Isoform 2 showed a **significant increase in phospholipase activity** compared to canonical PLAAT4; the N-terminal modification did not affect membrane localization.
- **Isoform 2 drives cholesteryl-ester lipid-droplet remodeling.** Genes correlated with isoform 2 were enriched in **lipid droplet formation** (including PLA2G4C and BSCL2). Lipidomics showed cells overexpressing isoform 2 had the **highest cholesteryl-ester (CE) levels** among the three isoforms, with decreased triglyceride (TG) and a trend of decreased free fatty acids. CE-rich lipid droplet induction (methyl-β-cyclodextrin/cholesterol feeding + BODIPY) showed **significantly higher number and area of lipid droplets** in isoform 2-expressing cells.
- **BSCL2 (seipin) mediates isoform-2 lipid droplet formation.** Isoform 2 expression positively correlated with and significantly upregulated **BSCL2** (qPCR). Seipin (BSCL2 product) is central to the lipid-droplet assembly complex including CE droplets; lipid droplet formation alleviates lipid toxicity, mitigates ER stress, and supports tumor cell survival.
- **LTR7-PLAAT4-positive tumors are multidrug resistant.** A 64-compound organoid drug screen (14 chemotherapy, 23 targeted) showed **LTR7-PLAAT4-positive tumors predominantly enriched in the resistant subgroup** with broad drug resistance (χ² test); corroborated by GDSC data on LTR7-PLAAT4-positive CCLE lines.
- **TE-chimeric peptides serve as neoantigens; mutation-derived neoantigens are nearly absent.** HLA immunopeptidomics found **12,234 peptides in AsPC-1** (7,481 predicted binders) and **11,380 in DAC13** organoids. Only **one mutation-derived peptide (CAPN2)** was found in AsPC-1 and none in DAC13, underscoring PAAD's low mutational burden; instead **TEprof2-predicted (n=4) and locally translated TE ORFs (n=4)** contributed peptides.
- **FLIQHLPLV is a validated immunogenic TE neoantigen.** The TEprof2-derived peptide **FLIQHLPLV** (binds HLA-A*02:01) was detected in ~27% (3/11) of organoids, showed strong T2 binding and MS spectral matching, and **elicited a strong IFNG response** in ELISPOT with HLA-genotyped PBMCs. Two further TE-derived peptides (ETVTGVWSY, FLPDHWAVL) were validated in AsPC-1.

## Methods

- **Organoid discovery cohort + bulk validation cohort:** 71 patient-derived PAAD organoids (66 tumor, 5 paratumor) with RNA-seq on all 71, WGS on 29, and ATAC-seq on 67 (62 tumor, 5 normal); plus an independent bulk cohort (41 tumor / 39 paratumor), 41 CCLE/685 cancer cell lines, and hTERT-HPNE normal pancreatic epithelial lines.
- **TE quantification / DETEs:** featureCounts v2.0.6 and TElocal v1.1.1 with RepeatMasker annotations; DESeq2 v1.40.2 (fold-change ≥4, FDR < 0.05). Chromatin accessibility from ATAC-seq (BWA-MEM to GRCh38, MACS2 peak calling).
- **TE-chimeric transcripts:** TEprof2 (StringTie de novo assembly + quantification); filtered by TPM > 1, splice-junction support, ≥8-fold tumor-vs-normal enrichment, FANTOM5 CAGE-peak removal; annotated with ONGene oncogene database.
- **Functional validation:** lentiviral overexpression of canonical PLAAT4 / isoform 1 / isoform 2 / empty vector in PANC-1 and AsPC-1; CCK-8 proliferation, wound-healing/transwell migration, invasion assays; nested PCR + Sanger sequencing for isoform 2 (Capan-1, SNU-16, hTERT-HPNE); Western blot.
- **LTR7 promoter regulation:** luciferase reporter assays (LTR7, MER21B, motif mutants) in 293T and AsPC-1; PROMO TF-motif prediction; FOXM1 ChIP-PCR via CUT&RUN (Hyperactive pG-MNase kit).
- **Lipid biology:** mass-spectrometry lipidomics of PANC-1 isoform-overexpressing cells; PLA2 phospholipase activity assay (liposome/BODIPY substrate); CE-rich lipid-droplet induction (methyl-β-cyclodextrin/cholesterol, BODIPY staining, confocal); BSCL2 qPCR; correlation/GO analyses of isoform-correlated genes.
- **Drug screen:** organoid high-throughput screen of a bespoke 64-compound library (AUC/Z-score clustering); KRAS p.G12C organoid (DAC78) sensitivity to AMG510/MRTX849 as positive control; GDSC cross-validation.
- **Immunopeptidomics / neoantigens:** HLA-I immunopeptidomics (MS) of AsPC-1 and DAC13 organoids; NetMHCpan-4.1 binding prediction; ORF prediction by CPC2 and EMBOSS getorf; T2 binding assays, synthetic-peptide spectral matching, ELISPOT (IFNG) with HLA-genotyped PBMCs; WashU Epigenome Browser visualization of TE-chimeric transcript translation evidence.

## Connections

- [P-Bodies and mRNA Regulation](../topics/p-bodies-and-mrna-regulation.md) — topic hub; this paper extends the cancer-RNA-regulation theme to retroelement-derived oncogenic transcripts and TE-defense biology.
- [P-bodies in cancer and leukaemia](../concepts/p-bodies-in-cancer-and-leukaemia.md) — shares the framing of post-transcriptional / retroelement biology as a cancer dependency and therapeutic target; complements Kodali 2024's P-body tumour-suppressor sequestration with a TE-onco-exaptation mechanism.

## Open Questions

- **Isoform-specific loss-of-function is unproven.** The functional claims rest on overexpression in PLAAT4-null cells; isoform-specific knockdown is technically hard given repetitive sequences and shared promoters. Long-read isoform-specific RNA-seq, CRISPRa screening, or bespoke antibodies are needed.
- **No in vivo validation.** The oncogenic and lipid-remodeling phenotypes were established in cell lines/organoids; in vivo tumor models are absent.
- **Endogenous isoform-2 detection limited.** Low endogenous abundance and high sequence similarity to canonical PLAAT4 prevented confident detection of isoform-2-specific peptides under physiological conditions.
- **Neoantigen universality and TCR specificity untested.** Incomplete antigen universality due to MHC diversity and absence of TCR sequencing limit immunotherapeutic generalization; the RNA-seq approach also excluded non-polyadenylated TE transcripts.
- **Upstream epigenetic control of LTR7.** LTR7 may interact with m6A-modified HERV-H transcripts and TET1 (and HNF4A regulation) to evade silencing — the full upstream activation circuit in PAAD remains to be dissected.

## Sources

- Local PDF: `raw/inbox/papers/shi-2026-transcriptomic-landscape-transposable-elements-reveals-ltr.pdf`
- DOI: [10.1101/gr.280528.125](https://doi.org/10.1101/gr.280528.125)
