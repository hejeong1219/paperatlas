---
title: "Cell-cycle-dependent mRNA localization in P-bodies"
authors:
  - "Safieddine A"
  - "Benassy M-N"
  - "Bonte T"
  - "Slimani F"
  - "Pourcelot O"
  - "Kress M"
  - "Bertrand E"
  - "Bénard M"
  - "Weil D"
year: 2024
journal: "Molecular Cell"
doi: "10.1016/j.molcel.2024.09.011"
pdf: "raw/inbox/papers/safieddine-2024-cell-cycle-dependent-mrna-localization-pbodies.pdf"
paper_kind: mechanistic
themes:
  - p-bodies
  - cell-cycle
  - mrna-localization
  - biomolecular-condensates
tags:
  - source
  - p-body
  - cell-cycle
  - rna-granule
pdf_status: full-text-read
---
# Cell-cycle-dependent mRNA localization in P-bodies

_Molecular Cell, 2024._

## Summary

Safieddine et al. ask whether P-bodies (PBs) — constitutive cytoplasmic RNP condensates of translational repressors and decay factors — change their RNA content over an unstressed cell cycle, and if so, whether those changes simply mirror cytoplasmic mRNA abundance. Working in HEK293 cells, they purify PBs at four cell-cycle stages (mid-G1, G1S transition, mid-S, G2M transition) by fluorescence-activated particle sorting (FAPS), then profile the PB and pre-sorting (cytoplasmic) transcriptomes by RNA-seq. PB RNA content turns out to be highly dynamic and **partly uncoupled** from cytoplasmic expression: thousands of mRNAs gain or lose PB localization across phases, and a subset changes in PBs without a matching cytoplasmic change (or vice versa), especially in the second half of the cycle. Single-molecule FISH (smFISH) and high-throughput smFISH confirm diverse cyclic localization patterns peaking in G1, S, or G2, including a striking case where G2-induced mRNAs (TOP2A, BUB1B, CENPF) are captured in PBs only after mitotic exit in early G1, when their protein is no longer needed. The cyclic pattern is **not** a passive reflection of untranslated mRNA pools (puromycin does not force premature recruitment); instead it is shaped by extrinsic and intrinsic factors — HuR/ELAVL1 binding prevents PB localization in G2, while AU-rich composition (at all phases) and long mRNA length (specifically in G1) favor PB accumulation. The work argues PBs are more than a default dump for excess untranslated mRNA: they are a regulated, cell-cycle-resolved RNA compartment.

## Key Points

- **PB morphology across the cycle:** After dissolving at mitosis, PBs reform in G1 and progressively enlarge through interphase, peaking in size (and DDX6 intensity) in G2, while PB number per cell increases only modestly. None of the tested PB proteins (DDX6, LSM14A, 4E-T, PAT1B) is transcriptionally induced across the cycle.
- **PB proteome is stable:** FAPS purification (>140 h sorting; 40× 15-cm plates per phase) followed by LC-MS/MS recovered the major known PB proteins (28–43 detected per phase: DDX6, LSM14A, LSM14B, 4E-T, EDC4, DCP1A), enriched over pre-sorting fractions in all phases; pairwise comparison showed no drastic changes in well-detected PB proteins between successive stages. FXR1/FXR2 were confirmed in a crown-like localization around PBs.
- **PB RNA content is highly dynamic:** Between 3,838 and 5,106 mRNAs were enriched in PBs depending on phase; 2,043 were enriched in only a subset or single phase. Phase-to-phase comparisons showed widespread shifts — e.g., from mid-G1 to G1S, 2,943 mRNAs increased and 2,599 decreased in PBs.
- **Functional GO shifts:** mRNAs accumulating in PBs from mid-G1 to mid-S were enriched (181/1,889) for proteins in mitotic cell-cycle phase transition, chromosome condensation, and cytokinesis; those decreasing were enriched (154/1,813) for transcription, transcriptional regulation, and RNA binding.
- **Partial uncoupling from cytoplasm:** PB changes broadly track cytoplasmic changes (distribution along the diagonal) from mid-G1 through mid-S, but mRNAs decreasing in PBs decreased about twice less in the cytoplasm, and from mid-S to G2M to the next G1 the PB content was only weakly coupled to large cytoplasmic up/downregulation (e.g., the cytoplasmic surge of TOP2A, BUB1B, CENPF was not mirrored in PBs).
- **Cyclic localization can peak at any phase (smFISH):** CCNE2 peaks in PBs at G1S, FBXO5 at mid-S, and CLK1 at G2M — single-molecule evidence that differential PB localization is not restricted to one stage and does not simply follow whole-PB growth.
- **PBs capture G2 mRNAs after mitotic exit:** TOP2A, BUB1B, and CENPF mRNAs are highly expressed yet weakly PB-localized in S/G2, then strongly concentrate in PBs in early G1 (when the protein is no longer needed); PUM2 mRNA served as a stable-localization benchmark.
- **M-G1 decay mRNAs accumulate in PBs in G1:** In a 94-mRNA HT-smFISH screen, a subgroup showed higher PB fraction in G1 than G2 (often >50% of molecules in G1). Of 161 reported M-G1-transition decay mRNAs well detected by FAPS, 62% were enriched in G1 PBs vs ~44% expected by chance (e.g., ECT2, TTK, DLGAP5).
- **Not a buffer / not just untranslated mRNA:** Even within a phase, PB fraction correlated weakly or not at all with cytoplasmic expression, arguing against a buffering role. Puromycin (which disrupts polysomes within minutes) did not drive TOP2A/BUB1B/CENPF mRNAs prematurely into PBs in G2 — disrupting translation is not sufficient for PB recruitment.
- **HuR/ELAVL1 gates G2 localization:** HuR and 4E-T targets were less PB-enriched in G2 than other phases (an ARE-specific effect). The HuR-ARE inhibitor CMLD-2 (24 h) sharply increased PB localization of HuR-target G2 mRNAs in G2, abolishing (CENPE, CENPF) or reducing (TOP2A) the G2-to-G1 differential; non-HuR-target or non-cyclic controls were unaffected. HuR thus prevents mRNA recruitment to PBs in G2.
- **Intrinsic features — AU-richness and length:** PB-enriched mRNAs were AU rich at all phases (GC content of CDS/3′UTR is the best predictor, rs up to 0.79), with little phase-to-phase compositional change. mRNA **length** was specifically biased toward longer transcripts in G1; for the top 500 AU-rich mRNAs, PB enrichment correlated with length in G1 (rs = 0.55) but not G2 (rs = 0.12).
- **Length is causal (reporters):** Lengthening Renilla luciferase reporters (all ~36–37% GC) from 0.9 kb to 1.7–1.8 kb increased their PB accumulation in early G1 but not S/G2; total mRNA length rather than CDS length per se was the determinant, possibly linked to post-mitotic PB reassembly (long RNAs proposed to seed/stabilize nascent PBs).

## Methods

- **Cell-cycle staging:** PIP-FUCCI and Cdt1-mVenus / mCherry-Geminin FUCCI reporters; DAPI-based G1/G2 classification for HT-smFISH.
- **Synchronization:** Double thymidine block and the selective CDK1 inhibitor RO-3306 to enrich mid-G1, G1S transition, mid-S, and G2M transition; FACS of HEK293-FUCCI cells into G1/S/G2M.
- **PB purification:** Fluorescence-activated particle sorting (FAPS) from HEK293-GFP-LSM14A cells (GFP-LSM14A expressed near-endogenous, co-localizes with DDX6 but not the stress-granule marker TIA1); cytoplasmic lysate split into a pre-sorting fraction (PSF, cytoplasm proxy) and sorted PBs.
- **Proteomics:** LC-MS/MS on purified PBs vs PSF per phase (qualitative — material too limited for quantitative replicates).
- **Transcriptomics:** RNA-seq of PBs and PSFs; differential enrichment by DESeq2 (p-adj < 0.05); GO analyses; comparisons across phases.
- **Imaging:** smFISH / smiFISH and high-throughput smFISH (HT-smFISH, 94 mRNAs), single-molecule counting in cytoplasm vs PBs; two-color smFISH using TOP2A as an early-G1 marker; Halo-/GFP-LSM14A PB labeling.
- **Perturbations:** Puromycin (polysome disruption) and CMLD-2 (HuR-ARE interaction inhibitor, 24 h); Renilla luciferase length-series reporters.
- **Data:** RNA-seq at ArrayExpress E-MTAB-12923; images/blots on Mendeley Data; analysis code on Zenodo.

## Connections

- [P-Bodies and mRNA Regulation](../topics/p-bodies-and-mrna-regulation.md) — topic hub for PB composition, condensate biology, and mRNA fate.
- [hubstenberger-2017-pbody-purification-condensation-repressed-mrna-regulons](../sources/hubstenberger-2017-pbody-purification-condensation-repressed-mrna-regulons.md) — same Weil-lab FAPS purification lineage; established that PBs hold ~one-third of the coding transcriptome and concentrate AU-rich, regulatory mRNAs (the asynchronous-cell baseline this paper resolves across the cycle).
- [vindry-2017-dual-rna-processing-pat1b-lsm-complexes](../sources/vindry-2017-dual-rna-processing-pat1b-lsm-complexes.md) — PAT1B/LSM-complex RNA processing, complementary to the PB protein/RNA repression machinery profiled here.

## Open Questions

- Which RBPs beyond HuR (and which combinations) set phase-specific PB localization, given that PB proteome MS could not be made quantitative and RBP-content changes are inferred rather than measured?
- Where and how do M-G1 decay mRNAs that transit PBs actually get degraded — is PB localization causal for their silencing/decay, or coincident?
- Does PB localization functionally silence residual G1 transcripts (e.g., TOP2A), and does removing PBs change cell-cycle gene expression or progression?
- Why does total mRNA length (not CDS length) drive early-G1 PB recruitment, and is the "long RNA seeds nascent PBs" condensate model correct mechanistically?
- How much of the dynamics seen after synchronization reflects synchronization artifacts vs native biology, and how do these patterns extend beyond HEK293 to other cell types, development, and differentiation?

## Sources

- Local PDF: `raw/inbox/papers/safieddine-2024-cell-cycle-dependent-mrna-localization-pbodies.pdf`
- DOI: [10.1016/j.molcel.2024.09.011](https://doi.org/10.1016/j.molcel.2024.09.011) — Molecular Cell 84, 4191–4208, November 7, 2024.
