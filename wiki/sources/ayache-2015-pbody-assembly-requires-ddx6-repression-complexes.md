---
title: "P-body assembly requires DDX6 repression complexes rather than decay or Ataxin2/2L complexes"
authors:
  - "Ayache J"
  - "Bénard M"
  - "Ernoult-Lange M"
  - "Minshall N"
  - "Standart N"
  - "Kress M"
  - "Weil D"
year: 2015
journal: "Molecular Biology of the Cell"
doi: "10.1091/mbc.E15-03-0136"
pdf: "raw/inbox/papers/ayache-2015-pbody-assembly-requires-ddx6-repression-complexes.pdf"
paper_kind: mechanistic
themes:
  - p-bodies
  - ddx6
  - translational-repression
  - rnp-assembly
tags:
  - source
  - p-body
  - ddx6
  - rna-granule
pdf_status: full-text-read
---
# P-body assembly requires DDX6 repression complexes rather than decay or Ataxin2/2L complexes

_Molecular Biology of the Cell, 2015._

DOI: [10.1091/mbc.E15-03-0136](https://doi.org/10.1091/mbc.E15-03-0136)

## Summary

P-bodies are cytoplasmic ribonucleoprotein (RNP) granules involved in post-transcriptional regulation, and the DEAD-box RNA helicase DDX6 (RCK/p54; yeast Dhh1) is a key, non-redundant component of their assembly in human cells — uniquely, arsenite cannot re-induce P-bodies in DDX6-depleted cells. To learn which of DDX6's many complexes drives P-body assembly, the authors mapped the DDX6 interactome in HEK293 cells by tandem-affinity (FLAG/HA) purification coupled to mass spectrometry, with and without RNase treatment. Three complexes dominated the top partners: the decapping complex, a CPEB-like repression complex, and an Ataxin2/Ataxin2L (ATXN2/ATXN2L) complex; the exon junction complex (EJC) and nuclear cap/poly(A)-binding proteins were also recovered (suggesting DDX6 binds newly exported mRNAs), and some DDX6 co-sedimented with polysomes. Despite ~170-fold enrichment in P-bodies, most DDX6 (~94%) is localized outside them, so the interactome is largely cytosolic. Of the three main complexes, only the decapping and CPEB-like complexes were recruited into P-bodies; the ATXN2/ATXN2L complex was excluded. Systematic silencing across four P-body inducers (untreated, arsenite, vinblastine, mild 30°C cold shock) separated essential factors from conditional/dispensable ones, identifying three proteins required in all conditions — DDX6, 4E-T (EIF4ENIF1), and LSM14A — all components of the CPEB-like repression complex. The authors conclude that human P-body assembly is driven by mRNA repression complexes rather than decay or ATXN2/ATXN2L complexes.

## Key Points

- DDX6 is a non-redundant master factor for human P-body assembly: unlike GW182 or CPEB1, its depletion blocks even arsenite-induced re-formation of P-bodies.
- The DDX6 interactome was mapped by TAP-tag (FLAG-DDX6-HA in HEK293, dual FLAG→HA purification) plus LC-MS/MS, run with RNase inhibitor and with RNase A; ~367 (untreated) and ~323 (RNase) specific proteins were identified, overwhelmingly RNA-metabolism proteins by GO.
- Three prominent complexes emerged among the top 20 partners: the decapping complex (EDC4, EDC3, DCP1A, DCP1B; plus XRN1, DCP2, LSM1-7 lower down), a CPEB-like repression complex (4E-T, PAT1B, LSM14A, LSM14B; CPEB1 itself undetected due to low HEK293 abundance), and an ATXN2/ATXN2L complex (with PABPC1/4, LSM12, MOV10).
- EJC core proteins (eIF4A3, MLN51, MAGOH, Y14) plus nuclear cap-binding NCBP1/NCBP2 and PABPN1 were recovered — RNA-mediated interactions — suggesting DDX6 can bind mRNAs at nuclear exit, before the first round of translation.
- A substantial number of ribosomal proteins co-purified; sucrose-gradient analysis confirmed some DDX6 on polysomes, increasing after cycloheximide treatment (consistent with yeast Dhh1 reports).
- Despite ~170-fold enrichment in P-bodies, only ~6% of DDX6 resides in P-bodies; most DDX6 — and most of its complexes — is localized outside P-bodies (≈94% excluded in a 5-P-body cell).
- Only the decapping and CPEB-like complexes are recruited into P-bodies; ATXN2, ATXN2L, and PABPs do not localize to P-bodies, defining two classes of DDX6 complex distinguished by P-body targeting.
- Maintenance silencing (untreated HeLa): silencing DDX6, 4E-T, or LSM14A abolished P-bodies; PAT1B gave ~50% reduction, EDC4 ~24%; EDC3 and ATXN2 had no effect, and LSM14B silencing increased P-bodies (via LSM14A up-regulation; the paralogs cross-regulate).
- De novo assembly across arsenite, vinblastine, and 30°C cold shock: DDX6, 4E-T, and (to a lesser extent) LSM14A were required in all conditions, whereas EDC3 was dispensable, EDC4 only facilitated, and PAT1B's requirement was inducer-dependent.
- Three "master genes" — DDX6, 4E-T, LSM14A, all from the CPEB-like repression complex — are required for P-body assembly under every tested condition, and the DDX6 FDF-binding pocket (mutant Mut1) is partly needed, linking direct DDX6–LSM14A/PAT1B contacts to assembly.
- ATXN2L silencing prevented DDX6 recruitment to stress granules (without affecting P-bodies), confirming the DDX6–ATXN2L interaction in vivo and showing this complex routes DDX6 to stress granules, not P-bodies.
- Xenopus oocyte DDX6 immunoprecipitates showed cell-specific variation: CPEB1-complex proteins dominated, the canonical decapping enzymes were largely absent (instead Nudt16), and no ATXN2/2L or PABP complex was found — yet repression-type partners were conserved.
- Overall conclusion: P-body assembly reflects mRNA repression, not decay; in yeast the pathway differs (DDX6 dispensable, 4E-T absent), and DDX6/4E-T/LSM14A (self-oligomerizing / disordered-region-rich) are candidate assembly scaffolds.

## Methods

- Cell lines: HEK293 (TAP-tag, high transfection efficiency) and HeLa (P-body imaging, flatter cells); P-body induction by 0.5 mM arsenite (30 min), 10 µM vinblastine (1 h), or 30°C for 2 h.
- Tandem-affinity purification: transient FLAG-DDX6-HA, sequential anti-FLAG M2 then anti-HA agarose from cytoplasmic lysates of 2×10⁸ cells; parallel RNase A vs. RNase-inhibitor conditions; empty-vector control. Silver/Coomassie staining, then in-gel digestion and LC-MS/MS at the Cambridge Centre for Proteomics; Mascot search vs. UniProt human database.
- Validation in untransfected cells: anti-DDX6 co-immunoprecipitation Western blots (± RNase) for decapping, repression, ATXN2/2L, and EJC partners, quantified as % of DDX6 immunoprecipitated.
- Localization: immunofluorescence (EDC4/DDX6/LSM14A/XRN1 as P-body and TIA1 as stress-granule markers); immunoelectron microscopy of endogenous DDX6; P-body quantitation via Icy Spot Detector (size filters 250 nm all, 450 nm large).
- Functional silencing: siRNA knockdown of DDX6, 4E-T, LSM14A, LSM14B, PAT1B, EDC3, EDC4, ATXN2, ATXN2L; P-bodies counted in untreated and induced conditions; DDX6 FDF-pocket Mut1 complementation assay.
- Polysome profiling on 10–50% sucrose gradients (± cycloheximide); Xenopus stage VI oocyte FLAG-MS2-DDX6 RNA injection (± progesterone maturation) with anti-FLAG IP and LC-MS/MS vs. Xenopus databases.

## Connections

- [P-Bodies and mRNA Regulation](../topics/p-bodies-and-mrna-regulation.md)
- [Hubstenberger 2017 — P-body purification, condensation, and repressed mRNA regulons](../sources/hubstenberger-2017-pbody-purification-condensation-repressed-mrna-regulons.md) — purified P-bodies and the repressed-mRNA regulon view, complementing the DDX6-repression-complex assembly model here.
- [Ripin 2024 — DDX6 modulates P-body / stress-granule assembly and docking](../sources/ripin-2024-ddx6-modulates-pbody-stress-granule-assembly-docking.md) — later mechanistic dissection of DDX6 in granule assembly/docking.
- [Kodali 2024 — RNA sequestration in P-bodies sustains myeloid leukaemia](../sources/kodali-2024-rna-sequestration-pbodies-sustains-myeloid-leukaemia.md) — disease relevance of P-body mRNA sequestration.

## Open Questions

- How do mutually exclusive DDX6 contacts (e.g., LSM14A vs. EDC3, EDC3 vs. PAT1B) coexist on the same mRNAs — does DDX6 oligomerization or multiple DDX6 loading accommodate distinct complexes simultaneously?
- What is the biological role of the abundant DDX6–ATXN2/ATXN2L complex if it is excluded from P-bodies and dissociates before repressed mRNAs enter them?
- What does polysome-associated DDX6 do — cotranslational decapping, a sensor of suboptimal-codon/inefficient polysomes, or an ATXN2-linked function?
- Why does the EJC / nuclear cap- and poly(A)-binding association occur, and where are these nuclear-exit-bound mRNAs stored given the EJC is not found in P-bodies?
- How do DDX6, 4E-T, and LSM14A act mechanistically as scaffolds, and what distinguishes the multiple repression pathways underlying the conditional requirements of PAT1B and EDC4?
- What accounts for the cell-type-specific composition of DDX6 decapping and ATXN2/2L complexes (e.g., Nudt16 and absence of canonical decapping enzymes in oocytes)?

## Sources

- Local PDF: `raw/inbox/papers/ayache-2015-pbody-assembly-requires-ddx6-repression-complexes.pdf`
- DOI: <https://doi.org/10.1091/mbc.E15-03-0136>
