---
title: "Properties of Stress Granule and P-Body Proteomes"
authors:
  - "Youn J-Y"
  - "Dyakov BJA"
  - "Zhang J"
  - "Knight JDR"
  - "Vernon RM"
  - "Forman-Kay JD"
  - "Gingras A-C"
year: 2019
journal: "Molecular Cell"
doi: "10.1016/j.molcel.2019.09.014"
pdf: "raw/inbox/papers/youn-2019-properties-stress-granule-pbody-proteomes.pdf"
paper_kind: review
themes:
  - p-bodies
  - stress-granules
  - proteomics
  - biomolecular-condensates
  - intrinsically-disordered-regions
tags:
  - source
  - p-body
  - stress-granule
  - rna-granule
pdf_status: full-text-read
---
# Properties of Stress Granule and P-Body Proteomes

_Molecular Cell, 2019._

## Summary

This review synthesizes the cumulative progress in defining the protein components of mammalian stress granules (SGs) and P-bodies (PBs), two cytosolic biomolecular condensates that form by phase separation of RNAs and proteins and participate in translational control. SGs sequester mRNAs bound to the translation-initiation machinery upon stress (becoming microscopically detectable only under stress), while PBs (constitutively visible) hold translationally stalled mRNAs associated with the mRNA-degradation machinery. The authors describe the experimental approaches used to map SG/PB proteomes — candidate-based microscopy/co-IP/genetics versus discovery-based core/particle purification (SG cores via G3BP1-GFP; PBs via LSM14A-GFP FAPS) and proximity-dependent biotinylation (BioID, APEX) — and introduce a new literature-curated RNA granule database (RNAgranuleDB) that scores and tiers proteins by their evidence for SG/PB residence. Analysis of the resulting "gold-standard" SG-PB proteome shows a strong bias toward intrinsically disordered regions (IDRs) and sequence features that favor phase separation. The review closes with a proposed multi-level/hierarchical assembly model in which pre-existing proximal protein interactions in stress-free conditions act as "seed interactions" poised to nucleate microscopically visible condensates upon stress.

## Key Points

- **RNAgranuleDB**: a new user-friendly, manually curated online database of literature evidence for genes/proteins associated with SGs or PBs, available at <http://rnagranuledb.lunenfeld.ca/>. It holds entries for 4,385 mammalian proteins (human, mouse, rat) and was built by text-mining ~1,900 articles (to Feb 2019) and manually curating 122 peer-reviewed publications.
- **Tiered confidence scoring**: each protein gets an "SG-PB curation score" (range 0.1 to 39) by summing weighted evidence (co-localization weighted above genetic evidence; indirect RBP annotation lowest). Arbitrary cutoffs assign 368 proteins to tier 1, 475 to tier 2, 428 to tier 3, and 3,114 to tier 4. **Tier 1 (368 proteins) is the gold-standard "SG-PB proteome."** Co-localization/proteomics curation provided SG/PB evidence for ~800 proteins.
- **Discovery-based core/particle purification counts**: Jain et al. (2016) purified G3BP1-GFP SG cores and identified **317 SG proteins**; Hubstenberger et al. (2017) used FAPS of LSM14A-GFP+ particles to reveal **125 PB proteins**. **28 of the 125 PB proteins** overlapped the SG core proteome — including LSM14A itself, which localizes to both PBs and SGs under stress.
- **Proximity-labeling (this review synthesizes BioID/APEX data)**: Markmiller et al. (2018) used APEX on G3BP1, finding ~120 proximal interactors in HEK293T (half present without stress) plus cell-type-specific interactors in NPCs, together annotating ~150 novel SG components. The authors' own BioID survey (Youn et al., 2018) profiled **90 SG/PB baits** (+30 mRNA-life-cycle proteins) and computationally predicted **106 SG proteins and 38 PB proteins, with 16 overlapping both**; microscopy validated 44/51 candidates (~90% validation rate).
- **IDR bias**: relative to the whole proteome or all curated tiers, the SG-PB proteome (tier 1) has IDRs making up a higher fraction of total sequence and contains longer IDRs, indicating an inherent bias toward IDR-mediated interactions (all pairwise tier comparisons p < 0.002).
- **Domain/motif enrichment**: 63 domains and RGG/RG motifs were enriched in the SG-PB proteome versus the whole human proteome; 15 of 63 remained enriched relative to the full curated list. Enriched features include RNA-binding domains (KH, RRM, DSRM), zinc fingers (zf-CCCH, zf-CCHC), DEAD-box helicase, PARP catalytic, and LSM domains.
- **Phase-separation propensity**: using six sequence-feature predictors (PLAAC, LARKS, R+Y, DDX4-like, CatGRANULE, PScore), higher tiers contain a larger fraction of proteins matching phase-separation features, with tier 1 highest — a **3.5- to 7.5-fold enrichment** over expectation. SG-PB proteins predicted to phase separate are also more likely to localize to nuclear condensates (29% vs 13%; chi-square p = 0.0003).
- **SG/PB "docking" concept**: although SGs and PBs are distinct organelles, a fraction become "docked" against one another upon SG induction, attributed to shared RBPs and mRNAs shuttling between the two, suggesting the organelles are functionally linked.
- **Named core PB proteins / machinery**: PB purification used the LSM14A marker; the PB cluster prominently features the CCR4-NOT deadenylase complex (highest internal correlation), connecting to eIF4E2-GIGYF2 and the miRNA silencing machinery (RISC). In vitro PB-like condensates form from purified S. pombe Dcp2, Dcp1, Edc3, and Pdc1 with RNA. (Decapping/PB hub proteins DDX6, DCP1A, EDC4, 4E-T are central PB markers in this literature.)
- **How SG and PB proteomes differ**: SGs assemble around translation-initiation components and the G3BP1 nucleator and are stress-induced; PBs are constitutive and built around the mRNA-degradation/decapping and deadenylation machinery (CCR4-NOT, decapping enzymes). The two proteomes overlap only modestly (e.g., 28/125 PB proteins shared; 16 overlap in the BioID predictions), with the overlap including dual-residence proteins like LSM14A.
- **Submicroscopic SG pools**: both proximity-labeling studies found SG-component proximal interactions are largely constitutive in unstressed cells and only moderately stress-modulated, implying SGs may exist as stable sub-microscopic condensates poised for rapid assembly.
- **Hierarchical/multi-level assembly model**: correlated BioID prey-labeling patterns (119 baits) reveal subclusters reflecting protein complexes that nest into larger SG/PB clusters; the authors propose pre-existing "seed interactions" facilitate stepwise, RNA-coupled assembly into visible condensates (SG cores first, then core+shell).

## Scope

Covers: the proteomic landscape of mammalian SGs and PBs; experimental methods for component identification (candidate-based microscopy/co-IP/genetics vs discovery-based purification and proximity-dependent biotinylation); construction, scoring, and tiering of the RNAgranuleDB; sequence-level properties (IDRs, domains/motifs, phase-separation predictors) of the gold-standard SG-PB proteome; and a model for hierarchical structural organization and assembly. Does not cover (or only briefly notes): detailed mechanisms of individual post-translational modifications in SG/PB regulation (acknowledged as important but not discussed in depth); RNA/transcriptome composition in depth (mentions ~1,800 mRNAs in SGs and ~6,000 in PBs); nuclear membraneless organelles beyond comparison; and direct disease mechanism studies (SG links to ALS/FTD, viral defense, and cancer chemoresistance/metastasis are noted as context).

## Connections

- [P-Bodies and mRNA Regulation](../topics/p-bodies-and-mrna-regulation.md)
- [Hubstenberger 2017 — P-body purification reveals condensation of repressed mRNA regulons](../sources/hubstenberger-2017-pbody-purification-condensation-repressed-mrna-regulons.md)
- [Ripin 2024 — DDX6 modulates P-body and stress granule assembly/docking](../sources/ripin-2024-ddx6-modulates-pbody-stress-granule-assembly-docking.md)
- [Luo 2018 — P-bodies: composition, properties, and functions](../sources/luo-2018-pbodies-composition-properties-functions.md)

## Open Questions

- How do nanoscopic/biochemical properties of individual molecules relate to the mesoscopic properties of SGs or PBs as a whole? In-vitro single-molecule phase behavior cannot be directly extrapolated to the whole organelle.
- How are >100 proteins and thousands of mRNAs (~1,800 in SGs, ~6,000 in PBs) spatially organized within SGs and PBs, given that individual phase-separation behavior changes with the context of co-phase-separating partners?
- Do all SG components show the biphasic (immobile core + labile shell) distribution seen for G3BP1/IMP1, and do PBs contain more than a single condensed phase?
- What are the relative stoichiometries of condensate components, and which act as scaffolds versus clients — likely groups of redundant paralogs rather than single proteins?
- How do post-translational modifications (and RNA modifications) quantitatively control SG/PB formation, dynamics, and function?
- Are the hierarchical proximity relations observed in the predominantly pre-assembled state actually responsible for spatial organization, or do RNAs and energy-driven machinery (helicases, chaperones, PTM enzymes) remodel them during assembly?

## Sources

- Local PDF: `raw/inbox/papers/youn-2019-properties-stress-granule-pbody-proteomes.pdf`
- DOI: <https://doi.org/10.1016/j.molcel.2019.09.014>
- RNAgranuleDB: <http://rnagranuledb.lunenfeld.ca/>
