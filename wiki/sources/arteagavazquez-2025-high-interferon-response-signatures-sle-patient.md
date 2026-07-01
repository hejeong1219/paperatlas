---
title: "High interferon response signatures in SLE patient leukocytes are associated with increased transposable element expression in gene introns and intergenic regions"
authors:
  - "Arteaga-Vazquez LJ"
  - "Sepulveda H"
  - "Villalobos Reveles B"
  - "Suzuki K"
  - "Kalunian KC"
  - "Ay F"
  - "Boothby MR"
  - "Rao A"
year: 2025
journal: "Mobile DNA"
doi: "10.1186/s13100-025-00377-6"
pdf: "raw/inbox/papers/arteagavazquez-2025-high-interferon-response-signatures-sle-patient.pdf"
paper_kind: computational
themes:
  - transposable-element
  - interferon
  - sle
  - autoimmunity
  - innate-immunity
  - retrotransposon
  - heterochromatin
tags:
  - source
  - transposable-element
  - interferon
  - sle
  - autoimmunity
pdf_status: full-text-read
---
# High interferon response signatures in SLE patient leukocytes are associated with increased transposable element expression in gene introns and intergenic regions

_Mobile DNA, 2025._

## Summary

This is a computational re-analysis of previously published bulk RNA-seq from purified leukocytes of systemic lupus erythematosus (SLE) patients (Panwar et al. 2021, GEO GSE149050) asking whether transposable element (TE) expression tracks with the type I interferon (IFN) signature that defines a major SLE patient subset. Patients had been pre-stratified by a gene-network analysis into ISG-high ("IFNpos", n = 12) and ISG-low ("IFNneg", n = 11) groups and compared to 10 healthy controls (HC) across six cell types — B and T lymphocytes, conventional and plasmacytoid dendritic cells, conventional monocytes, and neutrophils (PMN). Using the TEtranscripts (subfamily-level) and Telescope (locus-level) pipelines on T2T-CHM13v2.0 alignments, the authors find that **increased TE-derived RNA in SLE leukocytes is essentially confined to the IFNpos subset**: IFNneg patients show no significant TE upregulation versus HC, whereas IFNpos patients upregulate many TE families (dominated by LTR/ERV elements, but spanning LINE, SINE, satellite and DNA transposons). PMN had the highest number of differentially expressed TEs and ISGs. Expression of several specific TE subfamilies correlated strongly and positively with the ISG GSVA score and with clinical disease activity (SLEDAI) and severity — in some cases as well as or better than ISG expression itself. Mapping uniquely-assignable upregulated TEs showed ~80% lie in introns (or 3'UTRs) of co-upregulated genes (~67% of which are ISGs), but a substantial ~20% map to genes that are *not* differentially expressed or to intergenic regions distant from any annotated gene, arguing for a component of TE de-repression that is regulated autonomously from neighbouring genes (consistent with heterochromatin weakening). Intronic TE expression correlated with read-through transcription and with splicing alterations in flanking exons of ISGs (e.g. IFI44L/IFI44). The authors are explicit that the data are **correlative, not causal**: they cannot say whether TE expression drives the IFN response or vice versa, and they call for long-read sequencing to resolve mechanism. This paper is included in the P-body corpus as background on the immune-ISG / retrotransposon-defense axes (LINE-1, ERV de-repression, dsRNA sensing, innate immunity) rather than as direct P-body evidence — it contains no P-body experiment.

## Key Points

- **Re-analysis design.** Publicly available bulk RNA-seq from Panwar et al. (288 samples, 91 subjects: 65 SLE + 26 HC; six leukocyte types), restricted here to first-visit samples; SLE split into IFNpos (n = 12) and IFNneg (n = 11) vs HC (n = 10). Reads were mapped to the T2T-CHM13v2.0 reference with STAR; TEs quantified by TEtranscripts v2.2.1 (subfamily) and Telescope v1.0.3 (locus).
- **TE upregulation is IFNpos-specific.** "No TEs were differentially expressed when comparing patient samples stratified as IFNneg to those of healthy controls"; in sharp contrast, multiple TE families/subfamilies were strongly increased in IFNpos SLE vs HC or vs IFNneg.
- **Stratification boosts sensitivity ~5-fold.** Stratifying to IFNpos increased detection of upregulated TEs five-fold versus pooling all SLE (55 TEs upregulated in IFNpos-vs-HC versus 11 in total-SLE-vs-HC).
- **PMN (neutrophils) are the most affected cell type.** Among the six leukocyte types, PMN had the highest number of differentially expressed TEs and ISGs in IFNpos SLE versus HC, motivating the PMN-centric focus.
- **LTR/ERV elements dominate but all classes detected.** Differentially expressed TEs were dominated by LTR (endogenous retrovirus, ERV) sequences, with LINE, SINE, satellite and DNA transposons also detected; SINEs were a larger fraction of upregulated TEs in B cells.
- **TE expression correlates with disease activity and severity.** Normalized counts of differentially expressed TE subfamilies (e.g. LTR80A:ERVL, MLT1A:ERVL-MaLR, LTR103_Mam:ERV1, MLT1-int:ERVL-MaLR) correlated positively and significantly with the ISG GSVA score and with SLEDAI and disease severity; for certain subfamilies the TE–severity correlation was even stronger than the ISG–severity correlation.
- **Only a small fraction of any TE family is upregulated.** Overall TE-encoded RNA load changed only modestly across groups, implying that only a small subset of TEs in a given family/subfamily are de-repressed — "suggesting a stochastic process rather than a broad upregulation affecting all members of a TE family or subfamily."
- **Intronic TE expression is not simply explained by host-gene expression.** For 64% of ISGs (433/672), expression of intronic TEs correlated with the ISG across cell types only weakly (>0 and ≤25%); only 3.13% (21/672) had half-or-more of their TEs correlated, indicating intronic-TE increases are not just a readout of ISG transcription.
- **~80% of upregulated TEs sit in introns/3'UTRs of co-upregulated genes; ~67% of those genes are ISGs.** Expression of genes linked to upregulated TEs was increased (~80%) or unchanged (~20%) but never decreased; no instance had opposite-direction change for a TE and its linked gene.
- **A ~20% autonomous fraction.** In over 200 instances an intronic TE was upregulated while its host gene was unchanged ("TE UP, GENE NO"; only ~28% of those genes were ISGs), and several hundred uniquely-mapped intergenic TEs (nearly 20% of all TE reads) were activated far from any annotated gene — arguing against intron retention/batch effects as the sole mechanism.
- **Intron retention and batch effects largely excluded.** IRFinder analysis showed very few instances with substantial likelihood of intron retention, and typically only a portion of the TE-containing intron was transcribed, arguing against canonical intron retention or contaminating unspliced nuclear RNA as global explanations.
- **Intronic TEs correlate with splicing alterations in flanking ISG exons.** At loci such as IFI44L/IFI44 (and IFIH1/MDA5, IFI6), high intronic TE expression (e.g. HAL1B, L1MC5, LTR80A elements) tracked with increased ISG expression and with splicing variations in adjacent annotated exons, recalling TE "exonisation."
- **Honest causality caveat.** "Our data do not offer mechanistic insights into how TE expression might be linked to SLE pathogenesis or ISG expression"; whether TE expression is a root cause or an effect of heightened ISG expression "remains unclear," and "direct experimental evidence supporting causality is absent."
- **Proposed innate-sensing bridge (background, not tested here).** The authors frame TE-derived dsRNA (e.g. inverted Alu repeats) as a potential activator of the dsRNA sensor MDA5 (IFIH1) — especially with compromised ADAR1 editing or gain-of-function MDA5 — and note that anti-ERV-K102 immune complexes and L1 ORF1p/ORF2p expression in SLE PMN could feed NETosis and IFN-I production; none of these mechanisms is experimentally tested in this paper.

## Methods

- **Dataset:** publicly available bulk RNA-seq from Panwar et al. (GEO GSE149050); 288 samples / 91 subjects (65 SLE, 26 HC); six leukocyte types (cMo, cDC, pDC, T, B, PMN); first-visit samples used; SLE pre-stratified into IFNpos / IFNneg by the original gene-network analysis. No new data, materials or wet-lab experiments generated.
- **Alignment / quantification:** TrimGalore v0.6.7; STAR v2.7.10a to T2T-CHM13v2.0 (unique mapping for genes; multimapper mode for TEs); HTSeq v2.0.4 for gene counts; **TEtranscripts v2.2.1** (--mode multi) for TE subfamily quantification; **Telescope v1.0.3** for locus-specific TE quantification.
- **Differential expression:** DESeq2 v1.38.3; genes at |log2FC| ≥ 1 and adjusted p ≤ 0.05; TEs at |log2FC| ≥ 0.5 and adjusted p ≤ 0.05. Four comparisons: all-SLE-vs-HC, IFNpos-vs-HC, IFNneg-vs-HC, IFNpos-vs-IFNneg.
- **Genomic-location classification:** BEDtools + R to assign DE TEs to (a) ≤2 kb upstream, (b) exon, (c) intron, (d) 3'-UTR, (e) 5'-UTR, (f) intergenic relative to nearby genes; correlation of DE TEs with DE genes.
- **Intron retention:** IRFinder v1.3.1 on T2T-CHM13v2.0 to test whether intronic TE signal reflects intron retention / batch effects.
- **Pathway / signature scoring:** GSEA (clusterProfiler v4.6.2, MSigDB hallmark sets) and GSVA v1.52.3 with curated ISG / IFN-alpha / IFN-gamma gene lists.
- **Clinical correlation:** Pearson correlation and linear regression (R stats) of normalized TE counts against SLEDAI score, disease severity, and ISG GSVA score.
- **Tracks / visualization:** deepTools v3.5.4, Wiggletools v1.2.11, bedGraphToBigWig; UCSC genome browser (2025) for locus-level inspection of individual TE units (TE/noise ≥ 2-fold metric).

## Connections

- [P-Bodies and mRNA Regulation](../topics/p-bodies-and-mrna-regulation.md) — topic hub; this paper supplies immune-ISG / retrotransposon-defense context (LINE-1, ERV de-repression, dsRNA sensing) for the P-body corpus rather than direct P-body evidence.
- [Kodali 2024 — RNA sequestration in P-bodies sustains myeloid leukaemia](../sources/kodali-2024-rna-sequestration-pbodies-sustains-myeloid-leukaemia.md) — links retroelement/RNA control to disease; complementary view of cytoplasmic RNA regulation feeding into cell state.
- [Chamma 2025 — methyl-CpG-binding protein inhibits cGAS](../sources/chamma-2025-methyl-cpg-binding-protein-inhibits-cgas.md) — shares the innate-immune nucleic-acid-sensing / viral-mimicry theme (cGAS/STING, dsRNA/dsDNA sensing) invoked here as the route from TE de-repression to IFN-I.

## Open Questions

- **Cause or effect?** Whether TE de-repression drives the type I IFN response in SLE or is a downstream consequence of heightened ISG expression (or both) is left unresolved; only correlation is shown.
- **Independent regulation vs exonisation/intron retention.** Is intronic TE expression in ISGs independently regulated, or does it reflect partial intron retention / TE exonisation? Long-read sequencing is needed to distinguish.
- **Which TEs and structures trigger sensing?** The threshold TE-RNA load, the specific dsRNA structures, and the particular innate sensors (MDA5/IFIH1, TLR7, cGAS/STING) engaged in patients with different genetic backgrounds are unknown.
- **Functional dsRNA load vs total load.** Total TE-RNA changes are modest; whether specific immunostimulatory dsRNA species (e.g. inverted Alu duplexes) increase far more than bulk TE RNA remains to be measured.
- **Generality across autoimmune disease.** Whether IFNpos-restricted TE de-repression generalizes to rheumatoid arthritis, dermatomyositis, type 1 diabetes and other IFN-high conditions is raised but not addressed here.

## Sources

- Local PDF: `raw/inbox/papers/arteagavazquez-2025-high-interferon-response-signatures-sle-patient.pdf`
- DOI: [10.1186/s13100-025-00377-6](https://doi.org/10.1186/s13100-025-00377-6)
- Data: GEO accession GSE149050 (Panwar et al. 2021 RNA-seq, re-analysed)
