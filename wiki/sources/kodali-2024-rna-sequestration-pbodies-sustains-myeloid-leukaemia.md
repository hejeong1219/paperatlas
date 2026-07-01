---
title: "RNA sequestration in P-bodies sustains myeloid leukaemia"
authors:
  - "Kodali S"
  - "Proietti L"
  - "Valcarcel G"
  - "López-Rubio AV"
  - "Pessina P"
  - "Eder T"
  - "Sardina JL"
  - "Grebien F"
  - "Di Stefano B"
year: 2024
journal: "Nature Cell Biology"
doi: "10.1038/s41556-024-01489-6"
pdf: "raw/inbox/papers/kodali-2024-rna-sequestration-pbodies-sustains-myeloid-leukaemia.pdf"
paper_kind: mechanistic
cancer_types:
  - acute-myeloid-leukemia
modalities:
  - crispr-screen
  - functional-genomics
themes:
  - p-bodies
  - mrna-storage
  - tumor-suppressor-sequestration
  - leukemia
tags:
  - source
  - p-body
  - aml
  - cancer
pdf_status: full-text-read
---
# RNA sequestration in P-bodies sustains myeloid leukaemia

_Nature Cell Biology, 2024._

## Summary

Genome-wide CRISPR/Cas9 dropout screens run in parallel in malignant (CebpaN-mut/C-mut "CNC") versus normal (HPC7) mouse haematopoietic progenitors identified post-transcriptional regulators of translational repression and P-body assembly as **selective vulnerabilities of acute myeloid leukaemia (AML)**. AML cells harbour aberrantly elevated numbers of P-bodies, overexpress P-body genes (notably **DDX6** and **EIF4ENIF1/4E-T**, both linked to worse patient survival), and depend on P-body assembly for leukaemia initiation and maintenance driven by distinct oncogenes (biallelic CEBPA mutation, MLL-AF9, AML1-ETO9a). Strikingly, loss of the P-body machinery had little effect on steady-state homoeostatic haematopoiesis but severely impaired **regenerative/emergency** haematopoiesis (HSC self-renewal under stress and serial competitive transplantation). Mechanistically, FACS-based purification of intact P-bodies from human AML cells (GFP-LSM14A particle sorting + RNA-seq) revealed that P-bodies **sequester translationally repressed mRNAs encoding potent tumour suppressors** (e.g. KDM5B, TRAF6, IDH1, BACH1, ZNF131, FBXO30) away from ribosomes. P-body dissolution (via DDX6, LSM14A or EIF4ENIF1 loss, or NBDY microprotein) de-represses translation of these tumour-suppressor mRNAs, raising their protein levels and rewiring the AML transcriptional and chromatin landscape. The work establishes RNA sequestration in P-bodies as a molecular node coupling cytoplasmic translation control to nuclear chromatin architecture in leukaemia, with a therapeutic window distinct from normal haematopoiesis.

## Key Points

- **Parallel CRISPR screens defined P-body genes as AML-specific dependencies.** Genome-wide dropout screens in mouse CNC leukaemia cells vs normal HPC7 progenitors found **308 genes selectively required by CNC cells** (log2FC < −0.5); GO analysis enriched for translational repression and P-bodies (GO:0000932), RISC complex, and miRNA-mediated translation inhibition. Top hits (DDX6, EIF4ENIF1, LSM14A, DCP1A, EDC4, XRN1, AGO2, TNRC6B, ZFP36L1, NUFIP2, etc.) validated as AML-selective in competitive growth assays.
- **AML cells have aberrantly elevated P-body numbers.** Immunocytochemistry for DDX6+/EDC4+ punctae showed AML patient cells (n = 4) carry significantly more P-bodies than normal CD34+ HSPCs (n = 2). DDX6 overexpression alone was sufficient to increase P-body numbers in progenitors. P-body genes are upregulated in AML (TCGA) with increased H3K27ac at their enhancers/promoters; DDX6 and EIF4ENIF1 elevation correlated with worse AML survival.
- **DDX6 is required for AML survival and identity across subtypes.** shRNA, CRISPR KO and CRISPRi silencing of DDX6 in MOLM-13, HEL, SKM-1, THP-1, MV411 and HL-60 triggered P-body dissolution and impaired proliferation; induced myeloid (MOLM-13) or megakaryocytic (HEL) differentiation and apoptosis. RNA-seq after DDX6 KD downregulated chromatin/cell-cycle genes (CHAF1B, UHRF1, MKI67, AURKB) and upregulated myeloid-differentiation and tumour-suppressor genes (CD40, CD14, IRF8, **CDKN1A**, **ID2**).
- **Other P-body assembly factors phenocopy DDX6.** Knockdown of **EIF4ENIF1 (4E-T)** and **LSM14A** caused P-body loss and growth arrest in MOLM-13 comparable to DDX6 loss, confirming the dependency is on P-body assembly per se.
- **Reversible degron model shows a time/dose window.** A homozygous DDX6-FKBP12^F36V-HA-P2A-mCherry knock-in enabled dTAG-13–induced degradation within 6 h; even 62.5 nM attenuated proliferation, and 6 days of continuous degradation **irreversibly** suppressed AML growth (DDX6 re-expression failed to rescue), suggesting therapeutic time/dose windows.
- **DDX6 is essential for AML progression in vivo.** Doxycycline-inducible CRISPRi DDX6 silencing prolonged survival of NSG mice bearing HEL or MOLM-13 xenografts; DDX6 KD primary patient AML cells were severely depleted from spleen, bone marrow, blood and liver at 60 d. In *Ddx6*-conditional mice, deletion ablated MLL-AF9– and AML1-ETO9a–driven leukaemia, showing requirement across driver oncogenes.
- **Minimal impact on homoeostatic haematopoiesis vs strong impact on regenerative haematopoiesis.** *Ddx6* deletion (Mx1-Cre or Rosa26-Cre) over 4 months left spleen/marrow cellularity, overall LSK frequency and mature lineage output largely intact, but caused ~3-fold HSC (LSK CD150+CD48−) expansion, increased HSC cycling (Ki-67) and mitochondrial activity. Under stress, *Ddx6*KO cells failed to engraft in serial competitive transplantation (homing-independent), marking DDX6 as essential for emergency/regenerative HSC function but dispensable at steady state. DDX6/LSM14A/EIF4ENIF1 KD did not impair primary human CD34+ HSPCs.
- **P-body assembly capacity, not just protein presence, is required.** A helicase-dead DDX6 (E247Q) and P-body–assembly-defective LSM14A mutants (ΔTFG, ΔFFD) failed to restore P-bodies or rescue proliferation in KD AML cells. Overexpressing the human microprotein **NBDY** (destabilizes P-bodies via EDC4) reduced P-bodies ~2-fold with a proportional drop in cell number. Differentiation agents PMA and the DOT1L inhibitor EPZ-5676 also dissolved P-bodies.
- **Purified AML P-bodies sequester tumour-suppressor mRNAs.** FACS-based isolation of GFP-LSM14A+ P-bodies + RNA-seq detected ~12,000 transcripts; **3,390 mRNAs enriched in MOLM-13 P-bodies and 2,972 in HEL P-bodies** (FC > 1.5, P < 0.05), independent of expression level. GSEA showed enrichment of a **tumour-suppressor gene signature** (NES = 1.26, P = 0.0038). P-body–enriched mRNAs include **KDM5B, TRAF6, ZNF131, IDH1, BACH1, FBXO30, NPM1, ZEB1, ID2, TLE4, MXI1, PHF6, KMT2C, KDM7A, NFKB1**; pro-leukaemic transcripts (PRTN3, ELANE, YBX1) stayed cytoplasmic. smFISH confirmed ~50–70% of KDM5B/POLK/RSRC2 mRNA colocalizing with P-bodies (KDM5B mean 48.98%).
- **Sequestered mRNAs are translationally repressed, not degraded.** Loss of sequestration did not change P-body mRNA levels. Polysome profiling showed P-body enrichment correlated with **reduced ribosome association** (R = −0.458), and P-body mRNAs were longer and more AU-rich (features of inefficient translation). eCLIP-seq mapped DDX6 binding (exon-preferring), overlapping **54%** of P-body-targeted mRNAs (enriched for transcription, chromatin, cell cycle, cell death).
- **P-body dissolution de-represses tumour-suppressor translation and protein.** After DDX6 KD, translation rate of P-body-associated mRNAs rose significantly (P ≈ 2.2 × 10⁻¹⁶); de-repressed mRNAs were enriched for binding sites of miRNAs that became downregulated upon DDX6 loss (added selectivity layer). Proteomics confirmed increased protein of P-body tumour suppressors (KDM5B, TRAF6, BACH1, IDH1, FBXO30, ZNF131). Forced expression of IDH1, FBXO30, BACH1, ZNF131, TRAF6 or KDM5B each impaired MOLM-13 proliferation.
- **RNA sequestration maintains leukaemic chromatin architecture.** DDX6 KD increased global chromatin accessibility (ATAC-seq: 2,345 gained vs 1,222 lost regions in MOLM-13), opening tumour-suppressor loci (PCDH8, TUSC3, GATA2, PRDM11, ARID1B) and tumour-suppressive TF motifs (SPIB, PU.1, AP-1, BACH1, IRF8), while pro-leukaemic loci (BCL2, SIRT7, MEIS2, BRD4, IKZF2) lost accessibility. CUT&RUN/CUT&Tag showed coordinated H3K27ac/H3K4me3 (positively correlated) and H3K27me3 (negatively correlated) changes; liCHi-C showed reduced promoter looping at downregulated loci (e.g. ZNF785).
- **KDM5B is a direct effector linking P-body loss to chromatin remodelling.** The de-repressed H3K4 demethylase **KDM5B** is enriched at regions that lose accessibility after DDX6 KD. **DDX6/KDM5B double knockout abrogated the effect of P-body dissolution and restored proliferation** to near-WT, placing KDM5B downstream of P-body dissolution. KDM5B KO alone did not affect growth.
- **Therapeutic implication.** AML cells hijack P-bodies to keep tumour-suppressor mRNAs translationally silent; pharmacologically dissolving P-bodies (e.g. targeting DDX6) could reactivate these tumour suppressors and dismantle leukaemic chromatin, with a therapeutic window that spares steady-state haematopoiesis (5-year AML survival remains ~30%, underscoring the need).

## Methods

- **Genome-wide CRISPR/Cas9 dropout screens** in mouse CNC (CEBPA biallelic-mutant AML model) and normal HPC7 progenitor lines; comparative log2FC enrichment/depletion analysis with GO biological-process and cellular-component enrichment (two-tailed Fisher's exact test).
- **Human AML cell lines** (MOLM-13, HEL, SKM-1, THP-1, MV411, HL-60) with shRNA knockdown, CRISPR/Cas9 knockout, and dox-inducible CRISPRi silencing; competitive growth, proliferation, apoptosis and flow-cytometric differentiation assays.
- **DDX6 degron**: homozygous CRISPR knock-in of FKBP12^F36V-HA-P2A-mCherry into the DDX6 locus; dTAG-13–induced reversible degradation with washout time-course.
- **In vivo**: NSG xenografts of cell lines and primary patient AML; conditional *Ddx6*fl/fl mice (exon 3 floxed) crossed to Mx1-Cre (poly(I:C)) and Rosa26-ERT2-Cre (tamoxifen); MLL-AF9 and AML1-ETO9a transplantation leukaemia models; colony-forming assays; serial competitive transplantation into CD45.1 recipients.
- **P-body purification**: GFP-LSM14A fluorescent labelling + fluorescence-activated particle sorting of intact P-bodies, with RNA-seq vs total cytoplasmic fractions (FC > 1.5, P < 0.05, Wald test + BH correction).
- **Mechanistic readouts**: smFISH (KDM5B, POLK, RSRC2), polysome profiling / translation-efficiency analysis, eCLIP-seq (DDX6 targets), small RNA-seq (miRNA, tsRNA, rsRNA) + TargetScan, quantitative proteomics.
- **Chromatin/epigenome**: ATAC-seq, H3K27ac/H3K4me1 CUT&RUN, H3K4me3/H3K27ac/H3K27me3/H3K9me3 CUT&Tag, low-input promoter capture Hi-C (liCHi-C), KDM5B ChIP-seq (GSM1003586); DDX6/KDM5B double-knockout competition assays.
- Rescue experiments with WT vs assembly-defective mutants (DDX6 E247Q; LSM14A ΔTFG/ΔFFD) and NBDY microprotein overexpression; differentiation agents PMA and DOT1L inhibitor EPZ-5676.

## Connections

- [P-Bodies and mRNA Regulation](../topics/p-bodies-and-mrna-regulation.md) — topic hub for P-body biology and post-transcriptional control.
- [Hubstenberger 2017 — P-body purification reveals condensation of repressed mRNA regulons](../sources/hubstenberger-2017-pbody-purification-condensation-repressed-mrna-regulons.md) — the P-body isolation method (GFP-LSM14A particle sorting) adapted here for AML cells.
- [Ayache 2015 — P-body assembly requires DDX6 repression complexes](../sources/ayache-2015-pbody-assembly-requires-ddx6-repression-complexes.md) — establishes DDX6/LSM14A/4E-T requirement for P-body assembly that this paper exploits as an AML dependency.

## Open Questions

- **How do AML cells select which transcripts to sequester?** Authors implicate mRNA length and AU-richness (inefficient translation) plus differential miRNA expression, but the precise targeting code remains unresolved; do oncogenic mRNAs preferentially escape sequestration?
- **Is the AML-vs-normal therapeutic window druggable pharmacologically?** DDX6 has no direct inhibitor; whether the 6-day "irreversible" window seen with the degron translates to a tractable drug that spares steady-state but not regenerative haematopoiesis is open.
- **How general is the P-body–tumour-suppressor axis beyond myeloid leukaemia?** P-body genes are dysregulated across cancers; whether the same sequestration-of-tumour-suppressors mechanism operates in other tissues is untested here.
- **What is the full chain from cytoplasmic de-repression to nuclear chromatin rewiring?** KDM5B is one validated node downstream of P-body dissolution; the contribution of other de-repressed chromatin/TF regulators (IDH1, TRAF6, BACH1, KMT2C, KDM7A) to the epigenetic switch remains to be dissected.

## Sources

- Local PDF: `raw/inbox/papers/kodali-2024-rna-sequestration-pbodies-sustains-myeloid-leukaemia.pdf`
- DOI: [10.1038/s41556-024-01489-6](https://doi.org/10.1038/s41556-024-01489-6)
