---
title: "Expression of endogenous retroviral elements is associated with extracellular matrix remodeling in prostate cancer"
authors:
  - "Williams EC"
  - "Mayarata DR"
  - "Horvath A"
  - "Chiappinelli KB"
  - "Shibata M"
year: 2026
journal: "Mobile DNA"
doi: "10.1186/s13100-025-00382-9"
pdf: "raw/inbox/papers/williams-2026-expression-endogenous-retroviral-elements-associated-extracellular.pdf"
paper_kind: mechanistic
cancer_types:
  - prostate-cancer
modalities:
  - mouse-model
  - bulk-rna-seq
  - te-transcript-quantification
themes:
  - endogenous-retrovirus
  - transposable-element
  - extracellular-matrix
  - trim28-silencing
  - viral-mimicry
  - tumor-microenvironment
tags:
  - source
  - retrotransposon
  - erv
  - prostate-cancer
  - cancer
pdf_status: full-text-read
---
# Expression of endogenous retroviral elements is associated with extracellular matrix remodeling in prostate cancer

_Mobile DNA, 2026._

## Summary

This study uses an immune-competent genetically engineered mouse model (GEMM) of prostate cancer to ask how the transcriptional co-repressor **TRIM28 (TIF1β/KAP1)** controls endogenous retroviral element (ERV) expression and what the downstream consequences of ERV derepression are in a tumor context. Building on the NPp53 model (Nkx3.1-CreERT2; Pten f/f; p53 f/f, modeling castration-resistant prostate cancer), the authors conditionally delete *Trim28* in prostate epithelium (NPp53T) and profile transposable element (TE) and gene expression by bulk RNA-seq with TE-aware quantification (TEtranscripts, TElocal, SQuIRE). *Trim28* deletion specifically derepressed long terminal repeat (LTR) ERV subfamilies of the **ERVK and ERV1** families — 14 subfamilies in hormonally intact tumors and 22 in castrated tumors — without affecting LINE, SINE, or DNA TE classes. ERV derepression was **androgen-independent** (occurring in both intact and castrated mice, with 13 subfamilies shared) and persisted to 3 months. Derepressed ERVs were associated with increased **dsRNA formation** (J2 antibody staining/dot blot) and, in some cases, acted as alternative promoters driving expression of neighboring protein-coding genes (*Bglap3* via RLTR10D::IAP-d-int; *Ptpn22* alongside ERVs and *Bcl2l15*; plus *Nyx*, *Fbxw19*, *Mdb1*; a predicted LTRIS_Mus–*Naalad2* chimeric transcript). Despite dsRNA and an innate-immune GSEA signature (allograft rejection, IL2-STAT5, complement), the authors did **not** detect a classical viral-mimicry response (no induction of dsRNA sensors or downstream ISGs), and CD3+ T-cell / CD206+ macrophage infiltration was unchanged at 1 month. The most striking downstream phenotype was **excessive extracellular matrix (ECM) deposition**: GSEA highlighted collagen formation and ECM organization Reactome pathways, and Picrosirius Red staining confirmed increased interstitial collagen in *Trim28*-deleted tumors. The authors propose that ERV derepression promotes tumor progression by remodeling the ECM (fibrosis), which may impede immune cell infiltration and foster an immunosuppressive microenvironment.

## Key Points

- **TRIM28 represses ERVs in prostate tumors; deletion derepresses LTR ERVs only.** In hormonally intact NPp53T (Trim28-deleted) vs NPp53 prostates (n = 5/genotype), **14 TE subfamilies were significantly increased** (log2 fold change ≥ 1.5, p < 0.01), and "All 14 of these transposable element subfamilies were long terminal repeat (LTR) elements, belonging to the ERVK and ERV1 families." Other TE classes (LINE, SINE, DNA) were unaffected; no LTR subfamilies were significantly decreased.
- **Some subfamilies are strongly overexpressed.** MER52-int reached a "log2 fold change over 6" in Trim28-deleted NPp53T prostates, though many other derepressed subfamilies showed lower-level overexpression.
- **Derepression spans many genomic loci.** Locus-level analysis (TElocal, SQuIRE) showed ERVB5_1-I_MM and RLTR45-int increased from distinct loci across several chromosomes, whereas MER52-int, RLTR44D, and MURVY-int each increased from only a single locus.
- **ERV repression by TRIM28 is androgen-independent.** In castrated NPp53T vs NPp53 prostates, **22 TE subfamilies were increased**, again all LTR ERVK/ERV1. **13 subfamilies overlapped** between intact and castrated tumors (log2FC ≥ 1.5, p < 0.01), with 7 more at a relaxed threshold (log2FC ≥ 0.9, p < 0.05).
- **Conserved repression mechanism.** Of the 22 ERV subfamilies up in castrated NPp53T, **12 were also derepressed** after Trim28 deletion in embryonic stem cells or neural progenitor cells (log2FC > 1.0, p < 0.05), supporting a conserved TRIM28 repression mechanism.
- **Castration shortens survival.** Castrated NPp53T mice had a median survival of **134 days** after tumor induction, significantly shorter than castrated NPp53 mice (log-rank test), and similar to the previously reported 122 days for intact NPp53T tumors.
- **ERV derepression correlates with dsRNA formation.** J2-antibody immunohistochemistry showed high dsRNA staining (> 50% of epithelial cells) in all Trim28-deleted NPp53T tumors at 1 month; staining was high/intermediate in NPp53 and absent (< 1%) in wild-type C57BL/6 prostate. dsRNA persisted at 3 months. Both **p53 deletion and Trim28 deletion** independently promoted dsRNA formation (NP vs NPT comparison).
- **ERVs act as promoters for neighboring genes.** The 3'LTR of **RLTR10D::IAP-d-int** drove expression of a short *Bglap3* isoform; ERVs upstream of *Ptpn22* coincided with *Ptpn22* and *Bcl2l15* upregulation. Increased PTPN22 protein was confirmed by immunostaining. Additional ERV-adjacent overexpressed genes: *Nyx*, *Fbxw19*, *Mdb1*.
- **Predicted TE–gene chimeric transcript.** TEProf2 predicted splicing of **LTRIS_Mus to exon 7 of *Naalad2***, generating a transcript predicted to encode a truncated protein in NPp53T tumors.
- **Differential gene expression.** Comparing intact NPp53T vs NPp53: **375 genes upregulated, 252 downregulated** (log2FC ≥ 1.5, p < 0.01). Upregulated genes included *Bglap3*, *Ptpn22*, and granzyme E (*Gzme*, a cytotoxic-T-cell gene).
- **Innate-immune signature without classical viral mimicry.** GSEA showed positive enrichment for Hallmark allograft rejection, IL2-STAT5 signaling, and complement gene sets in NPp53T tumors. However, the authors "did not detect increased expression of dsRNA sensors or downstream interferon-stimulated genes in NPp53T prostates," i.e., no full viral-mimicry response.
- **No increase in T-cell or macrophage infiltration at 1 month.** CD3+ T-cell density in YFP+ tumor regions and the microenvironment did not differ between NPp53T and NPp53; most CD206+ macrophages localized outside YFP+ ducts. ERV expression alone was insufficient to increase early CD3+ T-cell infiltration.
- **ERV derepression is associated with ECM remodeling / fibrosis.** GSEA against 1309 Reactome pathways identified collagen formation and ECM organization pathways with high NES in NPp53T tumors. Picrosirius Red staining confirmed increased interstitial collagen fibers at 1 month (n = 4/genotype), more pronounced at 3 months.
- **Proposed model.** ECM remodeling precedes the previously reported increase in CD206+ M2-like macrophages (at 3 months, not 1 month). Higher collagen density may suppress T-cell migration and promote immunosuppressive macrophage activity, linking ERV derepression → fibrosis → immune evasion → tumor progression.

## Methods

- **Mouse models:** NPp53 (Nkx3.1-CreERT2/+; Pten f/f; p53 f/f; R26r-YFP), NPp53T (adds Trim28 f/f), NP (Nkx3.1-CreERT2/+; Pten f/f), NPT (adds Trim28 f/f), and wild-type C57BL/6. Tamoxifen (200 mg/kg, 4 days) induced CreERT2 recombination at 2 months of age; surgical castration 1 month post-tamoxifen for survival/androgen-deprivation analysis.
- **RNA-seq with TE quantification:** Bulk RNA-seq (Illumina Stranded Total RNA, Ribo-Zero Plus); STAR alignment to mouse GENCODE GRCm39; TE subfamily counts via **TEtranscripts**, locus-level counts via **TElocal** and **SQuIRE** (RepeatMasker-derived GTFs). DESeq2 differential expression (NPp53 reference; intact and castrated batches analyzed separately). PCA, GSEA (Hallmark + 1309 Reactome gene sets, MSigDB). Public ESC, NPC, and adult liver datasets reanalyzed for comparison.
- **TE–gene chimera prediction:** TEProf2 with Kozak/CPC2 filtering (transcripts in ≥ 3/5 NPp53T samples, enrichment > 1 vs NPp53). Co-regulated ERVs identified within 200 kb of the top 20 derepressed genes using UCSC/WashU RepeatMasker annotations.
- **RT-qPCR:** Locus-specific ERV validation (ΔΔCT, Gapdh reference) confirming persistent expression to 3 months.
- **dsRNA detection:** J2 monoclonal antibody immunohistochemistry (low/intermediate/high scoring) and dsRNA dot blot (5 and 1 µg RNA, chemiluminescence, methylene-blue loading control).
- **Immunostaining:** IHC/IF for PTPN22, CD3 (T cells), CD206 (M2-like macrophages), YFP lineage label; Picrosirius Red for collagen fibers. Confocal (Zeiss LSM 980), ImageJ Fiji quantification.

## Connections

- [P-Bodies and mRNA Regulation](../topics/p-bodies-and-mrna-regulation.md) — topic hub; this paper sits on the retrotransposon-defense / viral-mimicry axis relevant to RNA-level control of repetitive elements (ERVs here vs LINE-1 elsewhere in the corpus).
- TRIM28/KRAB-ZFP heterochromatin silencing (H3K9me3 via SETDB1) is the genomic-defense counterpart to cytoplasmic RNA sequestration mechanisms discussed in the P-body literature; both restrain retroelement-derived RNA and its immune/oncogenic consequences.

## Open Questions

- **Are ERV proteins translated?** The study "did not examine whether ERV proteins are synthesized from these ERV transcripts" — only RNA-level derepression and dsRNA were measured.
- **Why no full viral-mimicry response?** Despite dsRNA and an innate-immune GSEA signature, dsRNA sensors and ISGs were not induced. Authors attribute this to early (1-month) timing or to the NPp53 baseline (p53 loss itself promotes dsRNA), leaving the dsRNA-sensing block unresolved.
- **Is ECM remodeling caused by ERVs specifically?** The authors note "genes other than ERVs affected by Trim28 deletion could affect extracellular matrix remodeling" — the causal link from ERV derepression to fibrosis is associative, not proven.
- **Do ERV-derived chimeric/truncated proteins (e.g., LTRIS_Mus–Naalad2) have functional consequences?** Predicted but not validated.
- **Were histone marks near ERV loci examined?** No — the study "did not examine histone marks near ERV loci," so it cannot fully distinguish direct ERV derepression from co-upregulation with neighboring genes.

## Sources

- Local PDF: `raw/inbox/papers/williams-2026-expression-endogenous-retroviral-elements-associated-extracellular.pdf`
- DOI: [10.1186/s13100-025-00382-9](https://doi.org/10.1186/s13100-025-00382-9)
- GEO: GSE298402 (RNA-seq generated in this study)
