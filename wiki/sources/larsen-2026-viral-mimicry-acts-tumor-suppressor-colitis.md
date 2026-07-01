---
title: "Viral mimicry acts as a tumor suppressor in colitis"
authors:
  - "Larsen F"
  - "Jeong W"
  - "Schep D"
  - "Good HJ"
  - "Shin AE"
  - "Zhang L"
  - "Derouet MF"
  - "Wang TC"
  - "Castellani CA"
  - "Shooshtari P"
  - "Asfaha S"
year: 2026
journal: "Nature Communications"
doi: "10.1038/s41467-026-68850-1"
pdf: "raw/inbox/papers/larsen-2026-viral-mimicry-acts-tumor-suppressor-colitis.pdf"
paper_kind: mechanistic
cancer_types:
  - colorectal-cancer
modalities:
  - mouse-genetics
  - organoid
  - rna-seq
  - dna-methylation-array
themes:
  - viral-mimicry
  - endogenous-retroelement
  - transposable-elements
  - innate-immunity
  - interferon
  - dsRNA
  - tumor-suppression
  - colitis-associated-cancer
  - stemness
tags:
  - source
  - viral-mimicry
  - line1
  - retrotransposon
  - colorectal-cancer
  - innate-immunity
pdf_status: full-text-read
---
# Viral mimicry acts as a tumor suppressor in colitis

_Nature Communications, 2026._

## Summary

Transposable elements (TEs) — LINEs, SINEs, and ERVs that make up nearly 50% of the genome — are normally epigenetically silenced, but become re-expressed during inflammatory injury of the colon in both mice and humans. Larsen et al. show that this re-expression triggers a "viral mimicry" response: TE-derived double-stranded RNAs activate innate immune sensors (MDA5/RIG-I → MAVS) and induce a type I/III interferon program, and that this response acts as a **tumor suppressor during colitis-associated cancer initiation**. Active IBD patient tissue upregulates TEs (notably Alu/SINEs) and interferon-response genes, but progression to IBD-associated dysplasia is accompanied by **downregulation** of both TEs and interferon genes — implying that escaping viral mimicry is permissive for tumor formation. Further activating the response by DNA hypomethylation (the demethylating drug 5-AZA-2′-deoxycytidine or conditional *Dnmt1* knockout) raised TE and interferon expression and significantly reduced colonic tumor number and size in AOM/DSS and Dclk1^CreERT2^;Apc^f/f^ models. Crucially, genetic knockout of the antiviral adaptor **MAVS** promoted tumorigenesis and reversed the anti-tumor effect of DNA hypomethylation, restoring tumor incidence to 100%. Organoid lineage-tracing showed the effect is **cell-autonomous and independent of an adaptive immune response**: viral mimicry suppresses the stemness of APC-mutant DCLK1+ cancer-initiating cells, while MAVS loss restores their organoid-forming/lineage-tracing capacity and organoid size. The work positions endogenous retroelement expression and innate dsRNA sensing as a natural tumor-suppressive barrier in inflammation-driven colorectal cancer.

## Key Points

- **TEs and interferon genes are co-upregulated in active IBD.** In GSE83687 (61 non-IBD controls vs 77 active-IBD inflamed tissues), TEs of multiple subclasses including Alu/SINEs (known to engage MDA5) and interferon-response genes (IFNAR1/2, IRFs, ISG15, MX1) were significantly upregulated in active IBD. The majority of TEs were upregulated with inflammation (p = 3.21 × 10⁻²¹; 174 elements up vs 36 down by binomial test), with a positive correlation between IFN and TE expression.
- **Viral mimicry is downregulated in IBD-associated dysplasia.** In GSE230524 (41 controls, 22 IBD without dysplasia, 7 IBD-associated dysplasia), interferon genes (ISG15, STAT1) were up in IBD vs control but **down** in dysplasia vs non-dysplastic IBD; the top 10 GO pathways enriched in non-dysplastic IBD were interferon/response-to-virus terms. TE expression was likewise downregulated in dysplasia, and sporadic CRC (n = 8) also had decreased TE expression vs controls — consistent with TE/IFN loss accompanying tumorigenesis.
- **Colitis induces TEs and interferon in mice.** Colonic epithelial cells from DSS-treated mice had significantly increased LINE1, SINE, and Mu-LV expression and elevated Ifnα, Ifnβ, Isg15; the magnitude scaled with DSS dose/colitis severity (2.5% DSS gave the highest TE and IFN expression).
- **TE overexpression is sufficient to drive interferon.** Transfecting HCT116 and HT29 colorectal cancer cell lines with LINE1 or SINE B2 overexpression plasmids induced interferons and interferon-response genes in both lines, confirming TEs directly trigger interferon signaling.
- **5-AZA reduces colitis-associated tumors.** In the AOM (10 mg/kg) + 2.5% DSS model, 5-AZA (5 mg/kg weekly × 6) significantly reduced tumor number vs vehicle (no size change), and reduced global 5-mC. In the Dclk1^CreERT2^;Rosa26^mTmG^;Apc^f/f^ model, 5-AZA reduced both tumor number and size, with fewer mice bearing tumors, alongside increased LINE/SINE/ERV and IFN/JAK-STAT expression.
- **5-AZA hypomethylates TEs specifically.** Infinium Mouse Methylation array (>285,000 CpGs) showed 5-AZA hypomethylated 154,488 CpGs (only 1 hypermethylated) vs control, and all TE classes (SINEs, LINEs, satellites, ERVs) were hypomethylated. CpGs in CpG islands/shelves/shores of interferon genes including *Mavs* were **not** differentially methylated, indicating IFN activation is a consequence of TE upregulation rather than direct promoter demethylation.
- **DNMT1 knockout in cancer-initiating cells phenocopies 5-AZA.** Dclk1^CreERT2^;Apc^f/f^;Rosa26^TdTomato^;Dnmt1^f/f^ mice developed significantly fewer and smaller tumors than Dnmt1^+/+^/^+/f^ controls, with reduced global 5-mC and induced TE/interferon expression. DNMT1 loss did not change DCLK1+ cell number, so the effect is on stemness, not cell survival. Unlike 5-AZA, DNMT1 KO did not cause γH2AX DNA damage, dissociating the anti-tumor effect from DNA damage.
- **DNA hypomethylation reduces DCLK1+ stemness.** Dnmt1^f/f^ mice had significantly fewer TdTomato+ lineage-traced crypts than Dnmt1^+/+^; in organoids, DNMT1 loss reduced the percentage of DCLK1+ cells forming lineage-traced organoids. 5-AZA similarly reduced GFP+ lineage-traced crypts, with rare 5-AZA-treated DCLK1+ cells remaining quiescent rather than tracing crypts/tumors.
- **MAVS knockout promotes tumorigenesis and reverses hypomethylation's effect.** In AOM/1.5% DSS, Mavs-tm1Zjc (MAVS-KO) mice had more tumors and higher tumor incidence than WT regardless of 5-AZA, and reduced survival. In the Dclk1;Apc^f/f^;Dnmt1^f/f^ model, crossing to MAVS-KO restored tumor incidence to 100% and reverted tumor number to control levels, while 5-AZA-induced interferon induction was lost in MAVS-KO mice — establishing MAVS-dependent viral mimicry as essential to the anti-tumor effect.
- **Viral mimicry suppresses stemness cell-autonomously.** In epithelial-only organoid cultures, APC-WT DCLK1+ cells formed no organoids whereas 5–10% of Apc^f/f^ DCLK1+ cells did. DNMT1 loss reduced organoid-forming/lineage-tracing capacity; MAVS KO promoted stemness (increased tracing and organoid size) even in the DNMT1-KO background, and reversed the 5-AZA effect — demonstrating the response acts within epithelial cells, independent of immune cells.
- **Element-specificity and clinical context.** SINE B2 and LINE1 are more likely to induce viral mimicry than other elements (e.g., LTRs that drive antigen presentation/T-cell killing); the authors detected broad SINE/LINE/LTR upregulation. They note that high ERV and interferon-gene expression is associated with improved cancer survival, and acknowledge contrary evidence that some TEs (e.g., HERV-H, LINE1 retrotransposition into APC) can be tumor-promoting — implying disease- and element-specific roles.
- **Model.** A two-hit model (mutation + inflammatory injury) drives a normal cell toward a cancer-initiating stem state; an intact viral mimicry response (TE re-expression → dsRNA → MAVS → IFN) suppresses stemness and tumor formation, whereas loss of the response (MAVS-KO) enhances stemness and tumors. DNA hypomethylation further activates viral mimicry and inhibits tumors.

## Methods

- **Human RNA-seq reanalysis** of two public datasets: GSE83687 (Peters et al.; 61 control resections, 77 active-IBD inflamed) and GSE230524 (Shaw et al.; 41 controls, 22 IBD, 7 IBD-associated dysplasia, 8 sporadic CRC); HISAT2 alignment to hg38 with a custom GTF merging GENCODE transcripts and RepeatMasker repeat loci, htseq-count quantification, DESeq2 differential expression, GO enrichment (clusterProfiler), repeat-element volcano plots.
- **Mouse models of colitis-associated cancer**: AOM (10 mg/kg i.p.) + 0.5–2.5% DSS in C57BL/6J; Dclk1^CreERT2^;Apc^f/f^;Rosa26^mTmG/TdTomato^ tamoxifen-inducible models; conditional Dnmt1^f/f^ and Mavs-tm1Zjc (MAVS-KO) crosses; 5-AZA-2′-deoxycytidine (5 mg/kg i.p.).
- **DNA methylation**: Infinium Mouse Methylation BeadChip Array (>285,000 CpGs, GSE283386), SeSaMe preprocessing, DML differential-methylation modeling (FDR < 0.01, effect size > 0.1); global 5-mC ELISA.
- **Epithelial organoids** from colon (Apc^f/f^ ± Dnmt1^f/f^ ± Mavs-tm1Zjc); 4-hydroxytamoxifen recombination, single-cell dissociation, TdTomato+ lineage-traced organoid counting at day 7, organoid size by ImageJ; in-vitro 5-AZA (1 µM).
- **Readouts**: RT-qPCR for TEs and interferon/JAK-STAT genes (normalized to GAPDH), in-vivo lineage tracing (TdTomato+/GFP+ crypts), γH2AX staining, MPO activity, p-STAT1/STAT1 western blot, H&E histology; LINE1 (pBS-L1PA1-CH-mneo) and SINE B2 (pB2-neo-TET) overexpression in HCT116/HT29.

## Connections

- [P-Bodies and mRNA Regulation](../topics/p-bodies-and-mrna-regulation.md) — topic hub; viral-mimicry dsRNA sensing and ISG/interferon signaling intersect P-body/cytoplasmic RNA-regulation biology.
- [P-bodies in cancer and leukaemia](../concepts/p-bodies-in-cancer-and-leukaemia.md) — both works frame post-transcriptional/RNA-driven control as a tumor-suppressive or tumor-dependency axis; here endogenous retroelement RNAs act as a tumor suppressor, mirror image of P-body sequestration of tumor-suppressor mRNAs in AML.

## Open Questions

- **Which specific TEs drive the tumor-suppressive viral mimicry?** Broad SINE/LINE/LTR upregulation was seen, but the element classes (and individual loci) responsible for the anti-stemness effect in colitis remain unresolved; the authors note Alu evolutionary age did not stratify expression.
- **How does dysplasia silence viral mimicry?** TEs and interferon genes are downregulated in IBD-associated dysplasia — the epigenetic or post-transcriptional mechanism that re-silences them during progression is not defined.
- **Mechanism linking dsRNA/MAVS sensing to loss of stemness.** The downstream effectors by which interferon signaling suppresses DCLK1+ cell stemness cell-autonomously are not dissected.
- **Therapeutic translation.** Whether targeting TEs directly, or combining 5-AZA with ADAR1/DHX9 inhibitors (negative regulators of viral mimicry), can suppress cancer initiation/prevention in high-risk patients is untested.
- **Tumor-suppressive vs tumor-promoting TE roles.** The authors acknowledge HERV-H and LINE1 retrotransposition into APC can be pro-tumorigenic; reconciling disease- and element-specific outcomes is open.

## Sources

- Local PDF: `raw/inbox/papers/larsen-2026-viral-mimicry-acts-tumor-suppressor-colitis.pdf`
- DOI: [10.1038/s41467-026-68850-1](https://doi.org/10.1038/s41467-026-68850-1)
