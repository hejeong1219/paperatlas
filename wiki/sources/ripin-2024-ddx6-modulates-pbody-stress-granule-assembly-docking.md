---
title: "DDX6 modulates P-body and stress granule assembly, composition, and docking"
authors:
  - "Nina Ripin"
  - "Luisa Macedo de Vasconcelos"
  - "Daniella A. Ugay"
  - "Roy Parker"
year: 2024
journal: "Journal of Cell Biology"
doi: "10.1083/jcb.202306022"
pdf: "raw/inbox/papers/ripin-2024-ddx6-modulates-pbody-stress-granule-assembly-docking.pdf"
paper_kind: mechanistic
themes:
  - p-bodies
  - stress-granules
  - ddx6
  - rna-chaperone-network
tags:
  - source
  - p-body
  - stress-granule
  - ddx6
pdf_status: full-text-read
---
# DDX6 modulates P-body and stress granule assembly, composition, and docking

_Journal of Cell Biology, 2024._ (Vol. 223, No. 6, e202306022.)

## Summary

Stress granules (SGs) and P-bodies (PBs) are ribonucleoprotein (RNP) granules that condense from untranslating mRNPs during the stress response. SGs form in part through promiscuous intermolecular RNA–RNA interactions, which can be limited by an "RNA chaperone network" of proteins (e.g., the eIF4A helicase) that inhibits RNA-driven aggregation. Here Ripin et al. show that the DEAD-box helicase DDX6 — long known as a core PB component whose loss disassembles PBs — has an additional, PB-independent function: it limits the formation of stress granules. Using CRISPR knockouts, siRNA knockdowns, and a panel of structure-guided DDX6 point mutants in U-2 OS cells, they demonstrate that DDX6 limits the partitioning of RNAs, of itself, and of other RNPs (including G3BP1, TIA-1, eIF4A/E/G) into SGs in a manner requiring both RNA binding and ATPase activity. They also find that PB components reciprocally shape SG composition: when canonical PBs are reduced, PB proteins that normally co-localize with SGs accumulate more strongly in SGs, while PB-only proteins form smaller "PB-like assemblies" that dock to the SG surface. Loss of DDX6, 4E-T, or DCP1A increases this PB–SG docking, whereas CNOT1 and PAT1B are required to promote docking. The proposed model: DDX6 binds RNA and, via ATP hydrolysis, remodels RNPs to prevent their over-partitioning into SGs, acting as another RNA chaperone alongside eIF4A.

## Key Points

- **DDX6 is a P-body component (DEAD-box RNA helicase, RCK/p54) that also LIMITS stress granule formation, independently of P-body formation.** This is a new role distinct from its established function in promoting PB assembly (Ayache et al., 2015).
- **DDX6 limits SG formation in an ATPase- and RNA-binding–dependent manner**, limiting the partitioning of itself and other RNPs into SGs. The proposed mechanism: DDX6 binds RNAs accumulating in SGs and, via ATP hydrolysis, promotes protein/RNA release and RNP remodeling that reduces SG assembly — analogous to eIF4A in the RNA chaperone network that limits intermolecular RNA–RNA interactions.
- **DDX6 KO cells form ~2× as many SGs per cell** (multiple SG markers); individual SGs are smaller, but total SG area per cell is ~2× higher, ruling out a simple growth/fusion defect. SGs also form earlier and persist longer after recovery in DDX6 KO. Translation repression by arsenite is equivalent in WT and KO, so the effect is not via altered translation shutoff.
- **Loss of DDX6 partially restores SG-like foci in G3BP1/2 KO cells** (PABPC1- and eIF4A-positive, also containing YB1/UBAP2L), paralleling prior rescues by eIF4A inhibition or ADAR1 loss — additional evidence DDX6 normally limits SG assembly.
- **Loss of DDX6 increases mRNA partitioning into SGs**: by smFISH, higher fractions of GAPDH, DYNCH1, and NORAD RNAs enter SGs in DDX6 KO cells.
- **When P-bodies are limited, dual-residence proteins shift into SGs.** PB components that already localize to SGs in WT (LSM4, LSM14A, eIF4E, eIF4G, CNOT1) "mix" more diffusely into SGs upon DDX6 loss, because reduced canonical PBs lessen competition. PB-only proteins (EDC4, DCP1A, some 4E-T) instead form smaller distinct "PB-like assemblies."
- **PB-like assemblies dock to the SG surface, not seed SGs.** SoRa super-resolution 3D imaging shows EDC4/DCP1A puncta predominantly dock at the SG surface; time-course imaging shows SGs form first and then recruit EDC4 puncta — excluding a model where PB-like assemblies drive the increased SGs. Merged SG+PB area is still higher in DDX6 KO, so increased SGs are not just added PB material.
- **DDX6 limits SGs independently of PBs**, supported by: (i) DDX6 point mutants whose effects on PB formation and on SG limitation do not correlate; (ii) CNOT1 and LSM14A knockdowns that increase SGs without altering PBs; (iii) 4E-T/DCP1A knockdowns that increase SGs while PBs persist (altered).
- **Loss of DDX6, 4E-T, and DCP1A increases PB–SG docking.** DCP1A knockdown increases docking even though PBs are not reduced, so docking is not merely a consequence of smaller PBs. In DDX6 KO cells, 4E-T/DCP1A knockdowns add no further docking, indicating DDX6, DCP1A, and 4E-T act in a concerted mechanism.
- **PB–SG docking depends on CNOT1 and PAT1B.** Knockdown of either reduces docking in both WT and DDX6 KO cells; these are proposed to link PBs and SGs via PAT1B interactions with decapping factors (DCP2-DCP1A) and CNOT1. Notably, CNOT1 knockdown still increases SGs even though it reduces docking — so the SG effect is separable from the docking effect.
- **DDX6 mutant panel pins down requirements.** Mut1 (Q320A/H323A/T327A/R331A) and Mut2 (R443A/F444A/K447A/E450A/E451A) rescue PBs (with increased PB number and docking, resembling 4E-T knockdown) but do NOT fully rescue the SG phenotype — separating PB rescue from SG limitation. RNA-binding mutants (Mut3 S343D/Q345D/R346D; Mut4 R373A/T391A/R421A), the ATPase-dead E247A, and the CNOT1-binding/ATPase-stimulation mutant R386E all fail to make PBs and fail to limit SGs, showing both RNA binding and ATPase activity are required.
- **DDX6 partitioning into SGs tracks its catalytic cycle.** ATPase mutants (E247A, R386E) increase DDX6 enrichment in SGs; RNA-binding mutants (Mut3, Mut4) decrease it — consistent with RNA-dependent recruitment and ATP-hydrolysis–dependent release. Upon DDX6 loss, G3BP1, TIA-1, eIF4A, eIF4E, eIF4G1, LSM14A, and LSM4 show increased SG enrichment, while HuR, YB1, and UBAP2L are unaffected.
- **PB and SG kinetics during stress** (U-2 OS, arsenite): PBs increase first (1–2 PBs per unstressed cell), followed by SGs. Granule-marker definitions used throughout: SGs = PABPC1+/EDC4– puncta; PBs = EDC4+/PABPC1– puncta. DDX6 (and EDC4, DCP1A, 4E-T, EDC3) is predominantly in PBs in U-2 OS and generally not in SGs (cell-type difference vs. HeLa), confirmed with two antibodies.

## Methods

- **Cell system:** Human osteosarcoma U-2 OS cells. CRISPR-Cas9 was used to generate DDX6 KO in both WT and G3BP1/2 KO backgrounds (two DDX6-targeting gRNAs, px458, puromycin/clonal selection), yielding lines that make both PBs and SGs (WT), make PBs but not SGs (G3BP1/2 KO), make SGs but not PBs (DDX6 KO), or neither (G3BP1/2 + DDX6 triple KO). Western blots confirmed unchanged levels of G3BP1, PABP, DCP1A, EDC4.
- **Stress/drugs:** arsenite (500 µM, or 100 µM for recovery), sorbitol (0.5 M), hippuristanol (1 µM), 1 h at 37°C. Ribopuromycinylation (puromycin, 5 min) assayed translation repression.
- **Imaging/quantification:** immunofluorescence with PABPC1 (SG) and EDC4 (PB) primary markers; spinning-disk confocal and Nikon SoRa super-resolution (optical pixel reassignment) for 3D rendering. Fiji for processing; Imaris (spot/surface/cell functions) for SG/PB counts, areas, volumes, EDC4 spots, smFISH spots, and DDX6 partition coefficients (mean granule/cytoplasm intensity). Merged SG+PB surfaces (Imaris channel arithmetic) tested whether increased SG signal was just added PB material.
- **RNA localization:** single-molecule FISH (smFISH, Stellaris; Khong et al. probes) for NORAD, DYNCH1, GAPDH to quantify % mRNA in SGs.
- **Genetic perturbations:** siRNA SMARTpool knockdowns of DDX6, 4E-T, DCP1A, EDC3, LSM14A, PAT1B, CNOT1 (validated by Western, ~66–100% efficiency). DDX6 mutant rescue via lentiviral transduction of untagged or GFP-tagged DDX6 WT/mutants (Mut1–4, E247A, R386E) into DDX6 KO cells; mutants designed from prior DDX6/yeast DHH1 structural work.
- **Dynamics:** FRAP of GFP-G3BP1 (WT vs DDX6 KO) showed DDX6 KO does not alter G3BP1 exchange dynamics in SGs.
- **Statistics:** unpaired two-tailed t tests on per-cell data points across 2–3 biological replicates.

## Connections

- [P-Bodies and mRNA Regulation](../topics/p-bodies-and-mrna-regulation.md)
- [Ayache 2015 — P-body assembly requires DDX6 repression complexes](../sources/ayache-2015-pbody-assembly-requires-ddx6-repression-complexes.md)
- [Youn 2019 — Properties of stress granule and P-body proteomes](../sources/youn-2019-properties-stress-granule-pbody-proteomes.md)
- [Hubstenberger 2017 — P-body purification reveals condensation of repressed mRNA regulons](../sources/hubstenberger-2017-pbody-purification-condensation-repressed-mrna-regulons.md)

## Open Questions

- Does the ATPase-active vs -inactive state of DDX6 (tunable by expression level or activators like CNOT1) explain cell-type differences in DDX6 localization (PB vs SG) and in PB/SG regulation between U-2 OS and HeLa cells?
- Do DDX6's role in limiting SGs and its RNA-binding interface explain the pathogenicity of DDX6 missense mutations that cause intellectual disability (Balak et al., 2019) — i.e., do they act through aberrant SGs and not only through PB defects, paralleling DHX30, DDX3X, DDX59?
- What are the specific protein–protein, protein–RNA, and RNA–RNA interactions on PB and SG surfaces that CNOT1/PAT1B use to mediate docking, and can they reveal mechanisms of component exchange between granules?
- Does DDX6 limit PB–SG docking directly (ATPase breaking protein interactions / preventing inter-granule RNA–RNA contacts) or indirectly (concentrating proteins inside larger PBs reduces exposed docking sites)?
- How general is the principle that weakening intra-granule (homotypic) interactions yields smaller assemblies with higher surface-to-volume ratio that dock more — does it extend to SG assembly itself?

## Sources

- Local PDF: `raw/inbox/papers/ripin-2024-ddx6-modulates-pbody-stress-granule-assembly-docking.pdf`
- DOI: <https://doi.org/10.1083/jcb.202306022>
- J. Cell Biol. 2024, Vol. 223, No. 6, e202306022. Submitted 5 June 2023; accepted 4 March 2024.
