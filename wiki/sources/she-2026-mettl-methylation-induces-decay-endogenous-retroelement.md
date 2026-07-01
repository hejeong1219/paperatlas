---
title: "METTL3 Methylation Induces Decay of Endogenous Retroelement Transcripts to Promote Tumor Immune Evasion"
authors:
  - "She X"
  - "Lan J"
  - "Zhang H"
  - "Lu G"
  - "Xu J"
  - "Zhang J"
  - "Zhan W"
  - "Feng S"
  - "Rao Z"
  - "Yu C"
  - "Han B"
  - "Zhang R"
  - "Song D"
  - "Chen Y"
  - "Wang G"
  - "Hu J"
  - "Luo X"
  - "Li H"
year: 2026
journal: "Cancer Research"
doi: "10.1158/0008-5472.CAN-25-2893"
pdf: "raw/inbox/papers/she-2026-mettl-methylation-induces-decay-endogenous-retroelement.pdf"
paper_kind: mechanistic
cancer_types:
  - colorectal-cancer
modalities:
  - merip-seq
  - rna-seq
  - functional-genomics
  - in-vivo-syngeneic
themes:
  - m6a
  - endogenous-retroelement
  - viral-mimicry
  - innate-immunity
  - mrna-decay
  - type-i-interferon
  - immune-evasion
  - lysine-methylation
tags:
  - source
  - line-1
  - retrotransposon
  - m6a
  - immune-evasion
  - cancer
pdf_status: full-text-read
---
# METTL3 Methylation Induces Decay of Endogenous Retroelement Transcripts to Promote Tumor Immune Evasion

_Cancer Research, 2026._

## Summary

This study identifies dimethylation of METTL3 at lysine 513 (K513me2) as a recurrence-associated, non-histone lysine methylation that drives colorectal cancer immune evasion. Mass spectrometry of locally recurrent colorectal cancer tissues ranked METTL3 among the top pan-lysine-methylated proteins; K513me2 was elevated in recurrent vs primary tumors, in advanced (stage III/IV) vs early disease, and predicted shorter overall survival. The SETD1A methyltransferase complex (with ASH2L/RBBP5/WDR5) catalyzes K513 dimethylation. Mechanistically, K513 sits in the SAM-binding pocket of METTL3; dimethylation increases METTL3's binding affinity to S-adenosylmethionine (SAM) and augments global RNA m6A deposition. A substantial fraction of m6A peaks fall on endogenous retroelements (EREs — LTR/ERV, LINE, SINE), and K513me2-driven m6A destabilizes these retroelement transcripts via m6A-dependent RNA decay. Loss of the modification (METTL3 K513R) stabilizes ERE transcripts, raises cytoplasmic dsRNA, and activates type I IFN through the MDA5–MAVS (RNA-sensing) and cGAS–STING (DNA-sensing) pathways, inducing ISGs, MHC-I and antigen-presentation genes. In vivo, K513R CT26 tumors grow slower in immunocompetent (but not immunodeficient) mice, with more CD8+ T cells and NK cells and fewer M2 macrophages; the effect is type I IFN–dependent (anti-IFNAR1 abolishes it). 5-Fluorouracil induces an E2F4 → SETD1A → METTL3-K513me2 axis via E2F4 self-activation. Pharmacologic E2F4 inhibition (HLM006474) or genetic K513R, combined with anti–PD-1, synergistically suppresses tumors — a viral-mimicry strategy to sensitize colorectal cancer to immune checkpoint blockade.

## Key Points

- **METTL3 K513me2 marks recurrent, advanced colorectal cancer.** LC/MS-MS of three locally recurrent colorectal cancer tissues, enriched with a pan-lysine-methylation antibody, yielded 47 shared lysine-methylated proteins; the top five were EEF1A2, METTL3, GNL1, SUPT5H, CHERP. K513 dimethylation was detected in all three tumors and is evolutionarily conserved. IHC on nine paired tumors showed significantly higher K513me2 and m6A in recurrent vs primary tissue; in a 69-patient TMA, K513me2 was higher in tumor vs normal and in stage III/IV vs I/II, correlated with recurrence/distant metastasis, predicted shorter OS (K513me2 high n=35 vs low n=34), and was an independent prognostic factor (HR = 5.334, 2.666–10.67; log-rank P < 0.0001).
- **The SETD1A complex catalyzes METTL3 K513 dimethylation.** Screening SMYD1-5, SETD7/8, SETDB1, SETD1A/B in HEK293T showed only SETD1A overexpression increased K513me2. METTL3 and SETD1A co-IP (endogenous and exogenous) and colocalize by IF; the METTL3 C-terminal MT-A70 domain (containing K513) is required for binding. SETD1A knockdown lowered K513me2; the catalytically inactive SETD1A R1495A mutant (impaired ASH2L/RBBP5/WDR5 assembly) failed to methylate METTL3, and knockdown of WDR5/RBBP5/ASH2L reduced K513me2. An in vitro assay with recombinant SETD1A–SET complex + His-METTL3 + SAM directly methylated METTL3 at K513.
- **K513me2 increases METTL3 SAM binding and global m6A.** METTL3 K513R reduced RNA m6A (ELISA + dot blot); SETD1A knockdown or R1495A lowered m6A. K513 mutation did not change METTL3 protein level or nuclear/cytoplasmic distribution. K513 lies in the SAM-binding pocket; SPR showed the METTL3(WT)–METTL14 complex bound SAM (Kd = 23.9 μmol/L) whereas METTL3(K513R)–METTL14 showed no detectable SAM binding. Molecular dynamics on the 5TEY structure indicated K513me2 produces a more compact complex with more hydrogen bonds/salt bridges to SAM.
- **K513me2 is required for METTL3 phase separation.** In an optoDroplet (mCherry–Cry2) assay, METTL3 WT formed light-induced condensates while METTL3 K513R failed to form condensates, consistent with SAM binding being required for METTL3 LLPS.
- **A large fraction of m6A marks endogenous retroelements.** MeRIP-seq in WT vs K513R LoVo cells found the RRACH/GGACH motif; 24,743 m6A peaks in WT vs 15,574 in K513R, with 6,979 peaks significantly reduced in K513R. ~12% of total m6A peaks localized to retrotransposon regions; both LTR and non-LTR retroelements showed reduced m6A in K513R.
- **K513me2-driven m6A destabilizes ERE transcripts (m6A-dependent decay).** RNA-seq showed significant upregulation of retroelement expression in K513R cells (e.g. UP 2006 / Down 1084 retroelements). qRT-PCR validated derepression of HERV-E, HERV-F, HERV-K, HERV-H and LINE-1 in K513R LoVo cells, and MERVL, MMERVK10C, MMVL30, RLTR6, MLV2, LINE-1 in CT26. An actinomycin D decay assay showed HERV-E and LINE-1 transcripts were significantly more stable in K513R cells.
- **SETD1A acts through METTL3 K513 to silence EREs.** SETD1A knockdown raised ERE expression in METTL3(WT) cells but had no additive effect in METTL3(K513R) cells (which already had elevated basal EREs), establishing SETD1A regulates EREs in a K513-methylation-dependent manner.
- **Derepressed EREs raise dsRNA and activate type I IFN.** GSEA showed type I IFN pathways enriched in K513R cells. J2 antibody detected elevated cytoplasmic dsRNA. K513R activated RIG-I, MDA5, STING, p-TBK1, p-IRF3, p-STAT1, increased IFNβ and CXCL10 secretion, and upregulated a broad ISG panel (e.g. ISG15, MX1, MX2, OAS1/2/3, OASL, IFIT1/2/3, IFI6/16/27/44, RSAD2, IRF9, STAT1, RIGI, B2M, APOBEC3F) plus MHC-I and antigen-processing/presentation genes.
- **Both MDA5–MAVS (RNA) and cGAS–STING (DNA) sensing mediate the IFN response.** In K513R CT26, KO of Mda5 or Cgas partially attenuated ISG induction and partially restored tumor growth; dual Mda5/Cgas KO further suppressed ISGs and gave a stronger tumor-growth rescue — ERE dsRNA can also be reverse-transcribed to dsDNA to engage cGAS–STING.
- **Antitumor effect is immune- and IFN-dependent in vivo.** METTL3 K513R CT26 tumors grew slower in immunocompetent BALB/c mice with increased CD8+ T cells and NK cells and reduced M2 macrophages, but showed no growth difference in immunodeficient NOD/SCID/IL2Rγnull (NCG) mice. Anti-IFNAR1 antibody eliminated the K513R-induced tumor suppression and reduced immune infiltration, identifying type I IFN as the central mediator.
- **5-FU induces an E2F4 → SETD1A → METTL3-K513me2 axis.** TF screening (JASPAR/ENCODE/ChIP-Atlas/CHEA3/GTRD) identified E2F4 as a SETD1A regulator; E2F4 binds SETD1A promoter site 1 (luciferase + ChIP). E2F4 overexpression raised SETD1A and K513me2; the E2F4 inhibitor HLM006474 lowered SETD1A, K513me2 and m6A. 5-Fluorouracil progressively raised E2F4 then SETD1A mRNA/protein and K513me2, with E2F4 auto-binding its own promoter (self-activation).
- **Targeting the axis sensitizes to PD-1 blockade.** METTL3 K513R + anti–PD-1 reduced CT26 tumor growth more than either monotherapy and increased CD8+ T-cell infiltration. E2F4 inhibition (HLM006474) phenocopied K513R; HLM006474 + anti–PD-1 gave markedly greater tumor inhibition and CD8+ T-cell infiltration than monotherapy.

## Methods

- **Patient cohorts**: LC/MS-MS pan-lysine-methylation proteomics of three locally recurrent colorectal cancer tissues; IHC of nine paired primary/recurrent tumors and a 69-patient TMA (K513me2, SETD1A, E2F4 H-scores), with TNM staging, recurrence/metastasis and OS (KM, multivariate Cox).
- **Methyltransferase identification**: lysine-methyltransferase panel screen in HEK293T; co-IP (endogenous + exogenous) and IF colocalization of METTL3/SETD1A; METTL3 truncations for domain mapping; SETD1A R1495A complex-assembly mutant; WDR5/RBBP5/ASH2L knockdown; in vitro methylation with recombinant SETD1A–SET complex + His-METTL3 + SAM.
- **SAM-binding / biophysics**: m6A ELISA and dot blot; SPR (Biacore T200) of His-METTL3(354–580)–METTL14(107–395) WT vs K513R binding SAM (Kd); molecular dynamics simulations on PDB 5TEY (RMSD, Rg, SASA, RMSF, DCCM, FEL, pocket volume, MM/PBSA & MM/GBSA ΔGbind); optoDroplet (mCherry–Cry2) phase-separation assay.
- **m6A / ERE genomics**: MeRIP-seq and stranded RNA-seq in METTL3 WT vs K513R LoVo cells (STAR, exomePeak, RepeatMasker GRCh38/hg38 retrotransposon annotation ≥300 bp & ≥50 copies, featureCounts, edgeR; FC > 1.5, P < 0.05); qRT-PCR of HERV/LINE/MERV panels; actinomycin D (5 μg/mL) RNA decay assay.
- **Immune readouts**: J2 dsRNA IF; immunoblot of RIG-I/MDA5/STING/cGAS/TBK1/IRF3/STAT1 (total + phospho); IFNβ and CXCL10 ELISA; flow-cytometric surface MHC-I (H-2Kb/H-2Db); ISG/antigen-presentation qRT-PCR.
- **In vivo**: CT26 syngeneic subcutaneous tumors in BALB/c (METTL3 KO/WT/K513R; SETD1A knockdown; Mda5/Cgas single and dual KO) and in immunodeficient NCG mice; tumor-infiltrating lymphocyte flow cytometry (CD8+ T, CD49b+ NK, M1/M2 macrophages); anti-IFNAR1 and anti–PD-1 antibody treatments; E2F4 inhibitor HLM006474 (20 mg/kg).
- **E2F4 axis**: TF prediction (JASPAR/ENCODE/ChIP-Atlas/CHEA3/GTRD), dual-luciferase promoter reporters, E2F4 ChIP-qPCR on SETD1A and E2F4 promoters, 5-fluorouracil time-course.

## Connections

- [P-Bodies and mRNA Regulation](../topics/p-bodies-and-mrna-regulation.md) — topic hub; this paper extends the m6A → mRNA-decay axis to retroelement transcripts, linking 5'→3' decay machinery to innate-immune sensing.
- [P-bodies in cancer and leukaemia](../concepts/p-bodies-in-cancer-and-leukaemia.md) — concept page on RNA-decay/sequestration machinery as a cancer dependency; here m6A-driven decay of EREs is the tumor's immune-evasion lever, conceptually parallel to (but distinct from) P-body sequestration of tumor-suppressor mRNAs.
- [Kodali 2024 — RNA sequestration in P-bodies sustains myeloid leukaemia](../sources/kodali-2024-rna-sequestration-pbodies-sustains-myeloid-leukaemia.md) — another post-transcriptional control axis cancers hijack; Kodali uses P-body sequestration (translational silencing) of tumor-suppressor mRNAs, whereas She uses m6A-dependent decay of retroelement transcripts to evade immunity.

## Open Questions

- Which decay machinery executes m6A-dependent ERE turnover here (e.g. YTHDF2-directed CCR4–NOT/decapping vs RNase pathways), and do P-bodies physically house these decaying retroelement transcripts? The paper invokes m6A-dependent decay but does not map the reader/decay effectors.
- How are specific retroelement families selected for m6A? ~12% of m6A peaks are on retrotransposons, but the determinants of which LINE/LTR/SINE loci get marked (vs escape) are unresolved.
- Is the K513me2–SAM-binding relationship monotonic? Structural/MD data suggest K513me2 *reduces* SAM binding affinity (less favorable ΔGbind, weaker SPR for K513R), yet K513me2 *increases* global m6A — reconciling the simulation thermodynamics with the functional/optoDroplet phase-separation requirement is incompletely resolved.
- Does the E2F4/SETD1A/METTL3 axis generalize beyond colorectal cancer and beyond 5-FU? SETD1A/E2F4 correlate with poor outcome across several cancers, but causal viral-mimicry rescue was tested mainly in CT26.

## Sources

- Local PDF: `raw/inbox/papers/she-2026-mettl-methylation-induces-decay-endogenous-retroelement.pdf`
- DOI: [10.1158/0008-5472.CAN-25-2893](https://doi.org/10.1158/0008-5472.CAN-25-2893)
