---
title: "Maximal inhibitory effect of MOV10 on LINE-1 retrotransposition requires both the MOV10/LINE-1 association and granule formation"
authors:
  - "Liu Q"
  - "Liu Y"
  - "Mao Y"
  - "Yi D"
  - "Li Q"
  - "Ding J"
  - "Guo S"
  - "Zhang Y"
  - "Wang J"
  - "Zhao J"
  - "Ma L"
  - "Peng X"
  - "Cen S"
  - "Li X"
year: 2025
journal: "PLoS Genetics"
doi: "10.1371/journal.pgen.1011709"
pdf: "raw/inbox/papers/liu-2025-maximal-inhibitory-effect-mov-line-retrotransposition.pdf"
paper_kind: mechanistic
modalities:
  - mutagenesis
  - co-immunoprecipitation
  - immunofluorescence
themes:
  - mov10
  - line-1
  - retrotransposon
  - rna-helicase
  - p-body
  - stress-granule
  - phase-separation
  - decapping
tags:
  - source
  - p-body
  - retrotransposon
  - rna-granule
pdf_status: full-text-read
---
# Maximal inhibitory effect of MOV10 on LINE-1 retrotransposition requires both the MOV10/LINE-1 association and granule formation

_PLoS Genetics, 2025._

## Summary

LINE-1 is the only autonomously active mobile element in the human genome, and the host restricts its retrotransposition through many factors, including the SF-1 RNA helicase **MOV10**. The authors' prior work (Liu 2023, EMBO Rep) showed MOV10 recruits the decapping enzyme **DCP2** to form a DCP2/MOV10/LINE-1 RNP complex ("DMLC") by liquid-liquid phase separation (LLPS), decapping and degrading LINE-1 RNA, with stress-granule scaffolds **G3BP1** and **TIA1** assisting condensate formation. Here, using a panel of MOV10 N- and C-terminal truncations and internal deletions in a CMV-L1-neoRT retrotransposition reporter (HeLa / HEK293T), they dissect *which* MOV10 domains drive maximal inhibition. Two regions cooperate: the **extended motif II (aa 563-675)**, which mediates the interaction between MOV10 and the LINE-1 RNP (ORF1p), and the **C-terminal domain (aa 907-1003)**, which is required for MOV10's association with **G3BP1** and thereby formation of large cytoplasmic granules. Loss of motif II abolishes anti-LINE-1 activity entirely (it is "dominantly attributed" to inhibition), while loss of the C-terminal domain leaves only partial activity. G3BP1 binding alone is insufficient: a chimera replacing MOV10's C-terminus with Caprin-1's G3BP1-interacting motif (GIM) restores G3BP1 binding but fails to form granules or restore inhibition, showing granule assembly — not mere G3BP1 contact — is the functional requirement. The MOV10-active mutants reduce LINE-1 RNA levels via cap removal (m7G-cap RIP), tying domain function back to the decapping/decay mechanism. The model: motif II tethers MOV10 to LINE-1 RNP and the C-terminal domain promotes LLPS granule formation, and both are needed for maximal restriction.

## Key Points

- **Two MOV10 regions cooperate for maximal anti-LINE-1 activity: extended motif II (aa 563-675) and the C-terminal domain (aa 907-1003).** Wild-type MOV10 gave a ~90% reduction in G418-resistant colonies vs empty vector; C-terminal truncations 1-906/1-863/1-727/1-675 retained only ~40-50% inhibition and 1-644 ~70%, while 1-547, 1-523 and 1-92 had no significant effect.
- **Motif II is dominant for inhibition.** Among N-terminal truncations only 532-1003 and 563-1003 retained near-full activity; deleting through motif II (e.g. 649-1003) caused complete loss of anti-LINE-1 function, whereas removing the N-terminus up to aa 532 was largely dispensable.
- **Internal-deletion mutants confirm the domain logic.** Δ563-675 and the double mutant Δ563-675/Δ907-1003 lost anti-LINE-1 activity, while Δ907-1003 (1-906) retained partial inhibitory activity — consistent with the truncation series.
- **Active mutants reduce LINE-1 RNA via decapping.** WT MOV10 reduced LINE-1 RNA ~80%; active mutants reduced it to ~35-65% of control, correlating with retrotransposition inhibition. m7G-cap RIP (with XRN1 knocked down to preserve decapped RNA) showed WT and active mutants (1-906, 563-1003) halved capped LINE-1 RNA, while inactive mutants (1-547, 649-1003) did not — linking activity to **DCP2-mediated decapping**.
- **The C-terminal domain (aa 907-1003) is required for cytoplasmic granule formation.** WT MOV10 formed large foci co-localizing with LINE-1 **ORF1p**; removing aa 907-1003 made MOV10-containing granules "almost disappear," giving diffuse cytoplasmic MOV10.
- **The C-terminal domain mediates MOV10/G3BP1 association.** Co-IP showed C-terminal truncations (1-906, 1-863) had markedly reduced G3BP1 binding, whereas N-terminal truncations bound G3BP1 like WT. **G3BP1** is described as the molecular switch triggering RNA-dependent LLPS.
- **G3BP1 binding alone is insufficient for granules or inhibition.** N-terminal truncation 684-1003 recruited G3BP1 but had no anti-LINE-1 activity; expressing 684-1003 to compete for G3BP1 reduced WT MOV10's activity (a dominant-negative effect), confirming G3BP1 recruitment matters but is not sufficient on its own.
- **A Caprin-1 GIM chimera dissociates G3BP1 binding from granule formation.** MOV10-delC-GIM (C-terminus replaced by Caprin-1's GIM, residues 369-378) restored G3BP1 binding by Co-IP but failed to form granules or improve anti-LINE-1 activity, showing the C-terminal domain has additional granule-promoting functions beyond G3BP1 contact.
- **An intrinsically disordered region alone is not sufficient.** Replacing the MOV10 C-terminus with Caprin-1's disordered CTD (MOV10-delC-CTD) failed to bind G3BP1, form granules, or enhance inhibition.
- **The predicted disordered aa 966-1003 is dispensable; aa 906-966 matters.** MOV10 Δ966-1003 still co-localized with ORF1p, formed large granules and retained full anti-LINE-1 activity, implicating the aa 906-966 region in puncta formation.
- **Extended motif II mediates the MOV10/LINE-1 RNP (ORF1p) interaction.** By Co-IP, C-terminal truncations down to 1-644 and N-terminal 532-1003/563-1003 bound ORF1p, while 1-547, 1-523 and 649-1003 did not; deleting motif II abolished co-localization with ORF1p and gave smaller granules. The prior MOV10EQ (E647Q in motif II) mutant likewise lost ORF1p association.
- **Granule size tracks co-localization.** Mutants lacking motif II formed substantially smaller cytoplasmic granules unable to co-localize with ORF1p; the double mutant Δ563-675/Δ907-1003 showed complete loss of granule formation (diffuse distribution).
- **Model.** MOV10 helicase motif II associates with LINE-1 RNP and motif VI (C-terminal domain) associates with G3BP1 to drive LLPS simultaneously; the platform may concurrently recruit other LINE-1 restriction factors (DCP2, TUT4/7, RNASEH2) to enclose and degrade LINE-1 RNA.

## Methods

- **LINE-1 retrotransposition reporter**: CMV-L1-neoRT (full human LINE-1 with an intron-disrupted neomycin-resistance cassette before the 3'UTR in antisense), scored as G418-resistant colony formation in HeLa cells after co-transfection with Flag-MOV10 WT or mutants.
- **MOV10 mutant panel**: pcDNA4.0 N-terminal Flag-tagged human MOV10; C-terminal truncations (1-906, 1-863, 1-727, 1-675, 1-644, 1-547, 1-523, 1-92), N-terminal truncations (532-1003, 563-1003, 649-1003, 684-1003, 734-1003), internal deletions (Δ563-675, Δ907-1003, Δ563-675/Δ907-1003, Δ966-1003), and MOV10/Caprin-1 chimeras (MOV10-delC-GIM, MOV10-delC-CTD).
- **LINE-1 RNA quantification**: RT-qPCR normalized to GAPDH; primers span the neo-cassette intron so only spliced (reverse-transcribed) LINE-1 cDNA is amplified.
- **Decapping readout**: m7G-cap RNA immunoprecipitation (RIP) with anti-m7G-cap antibody and qPCR for capped LINE-1 RNA, with endogenous **XRN1** knocked down by siRNA to prevent degradation of decapped RNA.
- **Interaction assays**: co-immunoprecipitation (anti-ORF1p IP for MOV10/LINE-1 RNP; anti-Flag IP for endogenous G3BP1) in HEK293T.
- **Imaging**: immunofluorescence confocal microscopy (Olympus IX81) for MOV10 (Flag), ORF1p and DAPI; granule-size quantification (ImageJ). Transfection efficiency (GFP co-transfection) and cytotoxicity (CCK-8) controls.

## Connections

- [P-Bodies and mRNA Regulation](../topics/p-bodies-and-mrna-regulation.md) — topic hub; MOV10 is a P-body/granule-associated RNA helicase that recruits the **DCP2** decapping enzyme, directly linking retrotransposon defense to P-body decapping/decay machinery and **DDX6**-style condensate biology.
- [Kodali 2024 — RNA sequestration in P-bodies sustains myeloid leukaemia](../sources/kodali-2024-rna-sequestration-pbodies-sustains-myeloid-leukaemia.md) — both papers center on RNP condensates that sequester/regulate specific RNAs; MOV10/DCP2 granules use decapping-decay where AML P-bodies use storage/repression. LINE-1 is also elevated in tumor cells.
- MOV10 has long been annotated as a P-body component (historical references to "P-body component Mov10" in HIV/HCV restriction), reinforcing the granule/P-body crosstalk theme; G3BP1/TIA1 here are stress-granule scaffolds, placing this work at the P-body ↔ stress-granule interface.

## Open Questions

- **How exactly does the C-terminal domain drive LLPS beyond G3BP1 binding?** Neither the Caprin-1 GIM nor a generic disordered CTD reconstitutes granule formation; the granule-promoting function of aa 906-966 (possibly RNA binding) is undefined.
- **What is the full set of factors enclosed in MOV10-driven granules?** The authors hypothesize concurrent recruitment of DCP2, TUT4/7 and RNASEH2, but the composition and stoichiometry of the DMLC condensate in cells is not directly resolved here.
- **Does motif II contribute to anti-LINE-1 activity beyond ORF1p binding?** The prior MOV10KR (K530R) mutant binds ORF1p but not DCP2 and is inactive, suggesting motif II may also aid DCP2 recruitment.
- **How general is the granule-formation requirement across MOV10's other antiviral/retroelement targets** (HIV, HCV, endogenous retroelements)?

## Sources

- Local PDF: `raw/inbox/papers/liu-2025-maximal-inhibitory-effect-mov-line-retrotransposition.pdf`
- DOI: [10.1371/journal.pgen.1011709](https://doi.org/10.1371/journal.pgen.1011709)
