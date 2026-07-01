---
title: "Dual RNA Processing Roles of Pat1b via Cytoplasmic Lsm1-7 and Nuclear Lsm2-8 Complexes"
authors:
  - "Vindry C"
  - "Marnef A"
  - "Broomhead H"
  - "Twyffels L"
  - "Ozgur S"
  - "Stoecklin G"
  - "Llorian M"
  - "Smith CW"
  - "Mata J"
  - "Weil D"
  - "Standart N"
year: 2017
journal: "Cell Reports"
doi: "10.1016/j.celrep.2017.06.091"
pdf: "raw/inbox/papers/vindry-2017-dual-rna-processing-pat1b-lsm-complexes.pdf"
paper_kind: mechanistic
themes:
  - p-bodies
  - mrna-decay
  - alternative-splicing
  - lsm-complexes
tags:
  - source
  - p-body
  - pat1b
  - rna-granule
pdf_status: full-text-read
---
# Dual RNA Processing Roles of Pat1b via Cytoplasmic Lsm1-7 and Nuclear Lsm2-8 Complexes

_Cell Reports, 2017._

## Summary

Pat1 RNA-binding proteins (human paralogs Pat1a/PATL2 in oocytes and Pat1b/PATL1 in soma) are enriched in cytoplasmic processing bodies (P bodies) and act as conserved enhancers of 5'-to-3' mRNA decay, activating decapping in complex with the cytoplasmic Lsm1-7 heptamer. This study shows that human Pat1b additionally forms a distinct **nuclear** complex with the Lsm2-8 heptamer. Through co-immunoprecipitation, immunofluorescence, mass spectrometry, and RNAi, the authors establish a chain of interactions linking Pat1b/Lsm2-8/U6 snRNA/SART3 together with U4/U6.U5 tri-snRNP components, localized to Cajal bodies (the site of snRNP biogenesis). RNA-seq after Pat1b depletion reveals two separable functions on distinct gene sets: stabilization of mRNAs normally stored in P bodies and enriched in 3' UTR AU-rich elements (mRNA decay role), and altered alternative splicing characterized by skipping of cassette exons with weak donor sites (pre-mRNA processing role). Thus Pat1b is a decapping enhancer with a dual role in both pre-mRNA splicing and mRNA decay, operating via compartment-specific Lsm complexes.

## Key Points

- Pat1b (PATL1) is enriched in P bodies and is a key player in cytoplasmic 5'-to-3' mRNA decay, activating decapping in complex with the cytoplasmic **Lsm1-7** heptamer.
- New central finding: Pat1b also forms a **nuclear** complex with the **Lsm2-8** heptamer (the spliceosome-specific ring containing Lsm8 instead of Lsm1).
- Two independent affinity purifications (FLAG-Pat1b and YFP-Pat1b in HEK293) recovered 166 specific Pat1b interactors; GO terms were dominated by RNA processing/splicing. Alongside known partners (DDX6, Lsm proteins, CNOT1, Xrn1, Dcp1a/Dcp2, Edc3, Edc4), the immunoprecipitate unexpectedly contained almost the entire **tri-snRNP** (SART3, Prp31, snRNP200/Brr2, Prp4, Prp3, Prp8, NHP2L1).
- Pat1b/Lsm2-8 binds spliceosomal **U6 and U4 snRNA (but not U1)** and connects to **SART3** (Prp24 ortholog); these interactions map to the **C-terminal** (Mid + PatC) region of Pat1b.
- The chain Pat1b → Lsm2-8 → U6 snRNA → SART3 is mediated by Lsm2/8: depleting Lsm2 or Lsm8 abolishes Pat1b binding to SART3 and U6 snRNA, whereas Lsm1 depletion does not. A phosphomimetic **T522E** mutation (PKA-site-like, near the Lsm2/3 interface) specifically disrupts Lsm8/SART3/U6 binding while leaving Lsm1 binding intact.
- Pat1b co-localizes with **coilin and SART3 in Cajal bodies**; the T522E mutation reduces co-localization with coilin (71% → 12%) and SART3 (82% → 29%) and is dominant-negative for endogenous P bodies. ~20% of endogenous Pat1b is nuclear at steady state and runs at lower mobility, suggesting a modified (possibly phosphorylated) nuclear form.
- Pat1b stabilizes SART3–Lsm2/8 interactions: depleting Pat1b reduces Lsm2/Lsm8 binding to SART3 (but SART3–U6 binding persists).
- **mRNA decay role:** RNA-seq found high-confidence changes in 3,703 transcripts, ~60% upregulated after Pat1b knockdown. Stabilized RNAs correlate positively with P-body enrichment (coefficient 0.39); 80% of significantly stabilized RNAs were also significantly P-body-enriched (vs 17% of downregulated). Upregulated mRNAs were enriched for 3' UTR AREs (up to 29%), TTP targets (up to 31%), and HuR targets (up to 53%); downregulated mRNAs were enriched for SMN-bound transcripts.
- **Splicing role:** rMATS identified **189 alternative splicing events**, >80% involving cassette-exon inclusion/skipping; 85% of regulated cassette exons showed **decreased inclusion** upon Pat1b depletion, i.e. Pat1b normally **promotes cassette-exon inclusion**. SART3, Lsm2, and Lsm8 (but not Lsm1) knockdowns reproduced the splicing effect, with Lsm2/8 strongest.
- Pat1b-activated cassette exons (vs 16,228 control exons) have weaker donor and acceptor splice sites, are modestly shorter, and are flanked by markedly **shorter introns** (median 1,030 nt vs 2,337 nt) with higher GC content (~46% vs 41% upstream). Model: Pat1b stabilizes SART3/Lsm2-8 to support tri-snRNP recycling, favoring inclusion of weak exons.
- The splicing and decay target gene sets are **distinct**, demonstrating two separable RNA-processing roles via compartmentally distinct Lsm complexes. Intron retention was rare, so global splicing efficiency is unaffected.

## Methods

- FLAG-Pat1b / FLAG-GFP (and YFP-Pat1b via GFP-Trap) expressed in HEK293; M2-Sepharose affinity purification, FLAG-peptide elution, GELC-MS/MS (Cambridge Centre for Proteomics, SwissProt search). Pat1b N-terminal, C-terminal, and T522E/T522A constructs used for domain mapping.
- Co-immunoprecipitation validated by western blot, northern blot, and qRT-PCR for protein (DDX6, Lsm1/2/8, SART3, Prp31) and snRNA (U1, U4, U6) partners; RNase A treatment to test RNA dependence; reciprocal FLAG-SART3 pulldowns.
- siRNA knockdown of Pat1b, SART3, Lsm1, Lsm2, Lsm8 (control b-globin) in HEK293/HeLa; biochemical nuclear/cytoplasmic fractionation (S6, lamin A/C markers).
- Immunofluorescence in HeLa using GFP-Pat1b / GFP-Pat1bNES with coilin and SART3 (Cajal-body markers) and DDX6 (P-body marker); foci quantitated in ImageJ (50 cells, 3-4 experiments), two-tailed t test.
- RNA-seq: two biological replicates of b-globin vs Pat1b siRNA HEK293, Ribo-Zero TruSeq stranded libraries, Illumina NextSeq 500 (~100M 75-bp paired-end reads/sample). DESeq2 for differential expression; rMATS for alternative splicing; MaxEnt splice-site scoring; Mann-Whitney tests. Data: ArrayExpress E-MTAB-5577.

## Connections

- [P-Bodies and mRNA Regulation](../topics/p-bodies-and-mrna-regulation.md)
- [Franks 2008 — Control of mRNA Decapping and P-Body Formation](../sources/franks-2008-control-mrna-decapping-pbody-formation.md)
- [Safieddine 2024 — Cell-Cycle-Dependent mRNA Localization in P-Bodies](../sources/safieddine-2024-cell-cycle-dependent-mrna-localization-pbodies.md)

## Open Questions

- Does Pat1b bind U6 snRNA directly, or only through Lsm2-8? Recombinant Pat1b C-terminus did not bind U4/U6 snRNA in vitro, leaving the contribution of any direct contact unresolved.
- What is the molecular basis of the differential nuclear vs cytoplasmic Pat1b form — is differential phosphorylation (e.g., the T522/PKA-like site) the switch between Lsm1-7 and Lsm2-8 complex partner choice?
- Mechanistically, at which step of tri-snRNP biogenesis/recycling does Pat1b act, and how does stabilizing SART3/Lsm2-8 translate into the observed bias toward weak, short-intron-flanked cassette exons?
- The number of alternative splicing changes was modest (189 events) in proliferating HEK293, possibly reflecting low nuclear Pat1b; how much larger is Pat1b's splicing role in cell types with a higher nuclear pool?
- Is the nuclear Pat1/Lsm2-8 complex conserved across species (hints from Drosophila HPat nuclear accumulation and fungal Pat1 shuttling), and does it regulate splicing there too?

## Sources

- Local PDF: `raw/inbox/papers/vindry-2017-dual-rna-processing-pat1b-lsm-complexes.pdf`
- DOI: <https://doi.org/10.1016/j.celrep.2017.06.091>
- Cell Reports 20, 1187-1200, August 1, 2017. Data: ArrayExpress E-MTAB-5577.
