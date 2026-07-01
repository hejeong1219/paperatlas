---
title: "P-Body Purification Reveals the Condensation of Repressed mRNA Regulons"
authors:
  - "Hubstenberger A"
  - "Courel M"
  - "Bénard M"
  - "Souquere S"
  - "Ernoult-Lange M"
  - "Chouaib R"
  - "Yi Z"
  - "Morlot J-B"
  - "Munier A"
  - "Fradet M"
  - "Daunesse M"
  - "Bertrand E"
  - "Pierron G"
  - "Mozziconacci J"
  - "Kress M"
  - "Weil D"
year: 2017
journal: "Molecular Cell"
doi: "10.1016/j.molcel.2017.09.003"
pdf: "raw/inbox/papers/hubstenberger-2017-pbody-purification-condensation-repressed-mrna-regulons.pdf"
paper_kind: mechanistic
themes:
  - p-bodies
  - mrna-decay-and-storage
  - biomolecular-condensates
  - translational-repression
tags:
  - source
  - p-body
  - rna-granule
pdf_status: full-text-read
---
# P-Body Purification Reveals the Condensation of Repressed mRNA Regulons

_Molecular Cell, 2017._

## Summary

The authors developed a fluorescence-activated particle sorting (FAPS) method to purify intact cytosolic P-bodies from human HEK293 cells (labeled with GFP-LSM14A), then characterized them by LC-MS/MS proteomics and RNA-seq. P-bodies were found to concentrate hundreds of proteins and thousands of mRNAs that form a dense, specific interaction network distinct from stress granules. The mRNAs accumulating in P-bodies are translationally repressed (low protein yield, low ribosome density) but are not degraded there; rather they constitute a storable reservoir. Strikingly, P-body mRNAs preferentially encode regulatory functions and co-segregating subunits of protein complexes, leading the authors to propose that P-bodies condense repressed mRNA regulons as a substrate for coordinated post-transcriptional regulation.

## Key Points

- **Method (FAPS):** Intact ~500 nm P-bodies (only 4–7 per cell) were purified by flow-sorting GFP-LSM14A-labeled granules; a non-localizing truncated GFP-LSM14A-Δ served as the negative control. Sorted granules retained size/morphology and accumulated canonical markers (DDX6, 4E-T, DCP1, EDC3) but not the SG marker TIA1.
- **Proteome:** LC-MS/MS (sorted vs. pre-sorted) identified **125 proteins significantly enriched** in P-bodies (Fisher exact test, p < 0.025), of which 15 were known P-body components. **DDX6 binding partners accounted for 62/125 (~half)** of P-body proteins; DDX6 is a central network node interacting with half of P-body proteins.
- **Enriched machineries:** translation repression / decay factors (4E-T, LSM14A, LSM14B, IGF2BP2), miRNA pathway (AGO1, AGO2, MOV10, ZCCHC3), decapping (DCP1A, DCP1B, DCP2, EDC4), and NMD factors (UPF1, SMG7). Eight new components were validated by immunostaining (e.g., TUT4 uridyltransferase, IGF2BP1/IGF2BP3, PUM1, ZC3H7B, and several myosins MYO1C/1D/6/MYH10).
- **Depleted (observed exclusion):** mitochondrial proteins, stress-granule proteins (TIA-1, G3BP1/2, eIF3), and all translation initiation factors **except eIF4E** (which co-enriched with its repressor 4E-T). Only 5 of 78 detected ribosomal proteins were enriched.
- **No ribosomes/rRNA:** ISH-electron microscopy showed robust depletion of 18S and 28S rRNA from P-body cores and periphery, whereas 18S was enriched in arsenite-induced SGs — supporting that P-body mRNAs are repressed *upstream* of translation initiation.
- **Distinct from SGs (interpretation):** Only ~25% of P-body proteins overlapped a published SG proteome; the P-body interaction network is **~3× denser** than the SG network, **2× more enriched** in RNA-binding proteins (up to ~70% by domain homology), and helicases are 12× / 4× overrepresented vs. total / SG proteins.
- **Transcriptome:** Of 28,320 RNAs detected, **6,168 transcripts were significantly enriched** and **7,588 significantly depleted** (p < 0.05) — i.e. **>1/5 of cytoplasmic transcripts selectively accumulate in P-bodies**. Enriched RNAs were more protein-coding (89% vs. 67%); ncRNAs (sno/sn/scaRNA, lincRNA, antisense) were depleted. smiFISH validated 5/6 enriched and 2/2 depleted mRNAs; ~15% of cellular SPEN mRNA was in P-bodies on average (>30% in 12% of cells).
- **RNA-protein targeting:** Using CLIP data for 53 RBPs, 43 had targets enriched or depleted; **14 of 15** detected P-body proteins bound mRNAs that were themselves P-body-enriched. Binding context mattered — many targets enriched only when bound in the **3′UTR** (e.g. PUM2, AGO1/3, HNRNPM/U, MOV10), while some (EIF4A3, NOP58) only when bound in CDS. PCA on the RNA-protein matrix separated P-body from non-P-body mRNAs.
- **Translational repression (observed):** P-body-enriched mRNAs had ~20× lower protein yield (protein/mRNA) at the 95th vs. 5th percentile, ~2× lower ribosome density, and contributed to the genome-wide RNA–protein decoupling (RNA–protein correlation r = 0.49 for P-body mRNAs vs. 0.63 for depleted). Poly(A) tails were not shorter but more *heterogeneous* (r = 0.42 with enrichment).
- **Not decayed — reversible storage (central conclusion):** Four lines of evidence argue mRNAs are stored, not degraded: (1) P-body mRNAs were not less abundant; (2) half-life correlated only weakly (r = 0.22, ~2× shorter at most); (3) no 5′-truncated degradation intermediates accumulated (read coverage suggested 5′-end protection); (4) DDX6 knockdown dissolved P-bodies and **derepressed translation for ~75% of P-body mRNAs** (r = 0.36) **without** increasing their levels — only normally-depleted mRNAs accumulated.
- **mRNA regulons:** P-body-enriched mRNAs encode regulatory switches (chromatin remodeling, Pol II transcription control, RNA processing, cell division, differentiation, development), whereas depleted mRNAs encode housekeeping/constitutive functions (ribosomes, mitochondria, ER, metabolism). mRNAs encoding subunits of a given protein complex (e.g. cohesin, PIK3) tend to be co-enriched or co-depleted; mRNAs encoding P-body proteins are themselves enriched, implying a possible negative-feedback loop.

## Methods

- FAPS purification of GFP-LSM14A-labeled P-bodies from a stable HEK293 line; differential centrifugation to a pre-sorted (10,000 g pellet) fraction, then fluorescence-activated particle sorting; GFP-LSM14A-Δ truncation as non-localizing control.
- LC-MS/MS proteomics comparing sorted vs. pre-sorted fractions (normalized total spectra; Fisher exact test).
- RNA-seq of sorted P-bodies vs. pre-sorted fraction (edgeR differential enrichment, FDR < 0.05).
- Immunofluorescence/confocal and ISH coupled to immuno-electron microscopy (18S/28S rRNA, DDX6) for validation.
- smiFISH single-molecule imaging to quantify mRNA fraction in P-bodies.
- Integration with public datasets: SG proteome (Jain 2016), human interactomes (Hein 2015; Huttlin 2015 / BioPlex), CLIP targets for 53 RBPs (CLIPdb), HEK293 proteome (Geiger 2012), ribosome profiling and poly(A) profiling (Subtelny 2014), half-lives (Schueler 2014).
- DDX6 siRNA knockdown to dissolve P-bodies; polysomal/total RNA-seq ratio as a translation-rate proxy.
- Network analysis: Louvain community detection on the interactome to define protein complexes; GO-term enrichment.

## Connections

- [P-Bodies and mRNA Regulation](../topics/p-bodies-and-mrna-regulation.md)
- [Ayache 2015 — P-body assembly requires DDX6 repression complexes](../sources/ayache-2015-pbody-assembly-requires-ddx6-repression-complexes.md) — DDX6 centrality and assembly logic invoked throughout this paper.
- [Youn 2019 — properties of stress granule and P-body proteomes](../sources/youn-2019-properties-stress-granule-pbody-proteomes.md) — proteomic comparison of the two granules.
- [Franks 2008 — control of mRNA decapping and P-body formation](../sources/franks-2008-control-mrna-decapping-pbody-formation.md) — decapping vs. P-body relationship discussed here.
- [Vindry 2017 — dual RNA processing roles of PAT1B/LSM complexes](../sources/vindry-2017-dual-rna-processing-pat1b-lsm-complexes.md) — PAT1B/LSM repression machinery enriched in P-bodies.
- [Safieddine 2024 — cell-cycle-dependent mRNA localization to P-bodies](../sources/safieddine-2024-cell-cycle-dependent-mrna-localization-pbodies.md) — downstream work on regulated P-body mRNA targeting.

## Open Questions

- What exactly are the mRNA "ZIP codes" (sequence/structure elements, mostly in 3′UTRs) and the combinatorial RBP logic that address specific transcripts to P-bodies?
- Mechanistically, does condensation strengthen repression stoichiometrically (sequestering mRNA from initiation factors) or enzymatically (concentrating DDX6/TUT4 activity) — and to what degree each?
- Is the observed translation derepression upon DDX6 knockdown a cause or a consequence of P-body dissolution?
- How general is the "repressed mRNA regulon" model across cell types and conditions, and what physiological cues trigger coordinated release/translation of P-body mRNAs?

## Sources

- Local PDF: `raw/inbox/papers/hubstenberger-2017-pbody-purification-condensation-repressed-mrna-regulons.pdf`
- DOI: <https://doi.org/10.1016/j.molcel.2017.09.003>
