---
title: "SFPQ directs histone H3.3 deposition to R-loops in DNA repeats to protect genome stability"
authors:
  - "Ferrando A"
  - "Giaquinto M"
  - "Napolitano LMR"
  - "Canarutto G"
  - "Framarini A"
  - "Gambelli A"
  - "Veneziano Broccia P"
  - "Zappone A"
  - "Petti E"
  - "Boncristiani C"
  - "Parlante A"
  - "Onesti S"
  - "Piazza S"
  - "Benetti R"
  - "Schoeftner S"
year: 2026
journal: "Nature Communications"
doi: "10.1038/s41467-026-69479-w"
pdf: "raw/inbox/papers/ferrando-2026-sfpq-directs-histone-deposition-loops-dna.pdf"
paper_kind: mechanistic
cancer_types:
  - sarcoma
  - osteosarcoma
modalities:
  - chip-seq
  - drip-pcr
  - emsa
  - immunoprecipitation
themes:
  - sfpq
  - r-loops
  - genome-stability
  - dna-repeats
  - histone
  - retrotransposon
  - daxx-atrx
  - cgas-sting
  - innate-immunity
tags:
  - source
  - line-1
  - retrotransposon
  - r-loops
  - genome-stability
  - rna-binding-protein
pdf_status: full-text-read
---
# SFPQ directs histone H3.3 deposition to R-loops in DNA repeats to protect genome stability

_Nature Communications, 2026._

## Summary

R-loops — three-stranded RNA:DNA hybrid plus displaced single-stranded DNA structures — accumulate preferentially at the repetitive DNA elements that make up ~75% of the human genome, where unscheduled R-loops drive transcription–replication conflicts and genome instability. This paper shows that the multifunctional RNA-binding protein **SFPQ** (a DBHS-family paraspeckle protein, partner of NONO/PSPC1) is a surveillance factor that suppresses R-loop-mediated replication stress and DNA damage at telomeres, (peri)centromeric satellites, and the **LINE-1 and SINE/Alu retroelements**. SFPQ binds three-stranded R-loop structures directly in vitro (preferring R-loops with protruding single-stranded RNA tails, and repeat RNAs such as TERRA [UUAGGG] and SatIII [GGAAU]), is recruited to chromosomal R-loops via its **RRM1/RRM2 motifs**, and uses its intrinsically disordered **proline-rich P-domain** to recruit the histone H3.3-specific chaperone **DAXX** (a new SFPQ interactor identified by IP-MS). The SFPQ→DAXX axis deposits histone variant H3.3 at repeat elements to preserve a correct nucleosome template that counteracts R-loop accumulation. SFPQ loss displaces DAXX from repeats (and destabilizes ATRX protein), reduces H3.3 incorporation, and produces replication stress (p-ATR, p-RPA32, γH2AX, FANCD2/RAD51), chromosome breaks, sister-chromatid exchanges, mitotic defects, micronuclei, and cytoplasmic DNA. Cytoplasmic DNA activates innate immune signaling through the **cGAS–STING/IRF3/NF-κB** axis, inducing a 29-gene interferon-stimulated/innate-immunity signature. Clinically, in TCGA sarcoma high SFPQ expression correlates with poor survival and low innate-immunity signature, whereas the innate-immunity signature (and low SFPQ) correlates with improved survival; an osteosarcoma patient-derived P-domain mutation (T150delinsKP / "nFS") acts as a dominant-negative that breaks DAXX recruitment.

## Key Points

- **SFPQ suppresses R-loops genome-wide at repeats, including LINE-1.** siRNA depletion of SFPQ (or RNaseH1) in U-2 OS, H1299, MCF-7 and MCF-10A cells raised steady-state DNA:RNA hybrid levels and increased C0t-1 RNA-FISH repeat foci. DRIP-PCR after SFPQ knockdown showed increased R-loop abundance at telomeres, Chr16p subtelomeres, Sat III, Sat II, centromeric α-satellite, AluS, AluY and **LINE** elements, plus the PD3A promoter; WRNIP and SSH control promoters showed none.
- **Elevated R-loops recruit SFPQ to repeats.** Experimentally raising R-loops by transient RNaseH1 depletion or hydroxyurea drove SFPQ accumulation at centromeres (CREST) and telomeres (TRF2); anti-SFPQ ChIP-qPCR in RNaseH1-depleted cells confirmed SFPQ recruitment to telomeres, subtelomeres, Sat III, Sat II, α-satellite, AluS, AluY and **LINE** elements. C0t-1 RNA-FISH foci co-localized with replication-stress markers p-ATR(Thr1989) and FANCD2; SFPQ loss elevated p-Chk1 and p-RPA32.
- **SFPQ binds three-stranded R-loop structures in vitro.** Recombinant His6-myc-SFPQ in EMSA did not bind dsDNA, dsRNA, or a fully paired DNA:RNA hybrid duplex, but bound ssDNA and (more strongly) ssRNA, a DNA bubble, and synthetic R-loops. Binding was most efficient for R-loops with protruding 5′/3′ single-stranded RNA tails; ten-fold molar excess ssRNA was required to compete it off. Affinity was markedly higher for repeat ssRNAs [UUAGGG]₄ (TERRA), [GGAAU]₄ (SatIII) and [GAAA]₅.
- **DAXX is a new SFPQ interactor.** Anti-myc IP of myc-SFPQ in H1299 followed by MALDI-TOF MS identified DAXX (and validated NONO) as SFPQ-interacting; reciprocal co-IP of myc-SFPQ/HA-DAXX, endogenous co-IP in U-2 OS, and recombinant His6-myc-SFPQ + GST-DAXX-HA pull-down confirmed a direct interaction. DAXX was detected in reverse-crosslinked anti-SFPQ ChIP chromatin.
- **SFPQ directs DAXX localization and H3.3 deposition at repeats.** ChIP-seq in control U-2 OS found 6,375 SFPQ peaks and 6,643 DAXX peaks; SFPQ knockdown collapsed DAXX to 2,816 peaks and redistributed remaining DAXX toward promoter-TSS (9.54%→21.12%) and CpG (1.99%→5.34%), away from introns, LINE, SINE and intergenic regions. SFPQ–DAXX co-bound peaks were depleted at promoters/TSS (0.39%) and enriched at intergenic, intronic and repetitive elements (LINEs 21.75%, satellites 12.36%, SINE 5.83%, simple repeats 6.28%). H3.3 peaks rose 29,869→55,388 but with reduced peak height (global AUC drop), i.e., H3.3 redistributed from focal high-occupancy repeats to diffuse low-occupancy. ChIP-PCR confirmed reduced DAXX and H3.3 (not canonical H3) at α-satellite, SatII, SatIII, (sub)telomeres, **LINE1**, AluY, AluS after SFPQ loss; total H3.3 protein was unchanged.
- **The P-domain recruits DAXX; RRM1+2 load SFPQ onto R-loops.** Deletion of the intrinsically disordered proline-rich P-domain (residues 105–204) abolished SFPQ–DAXX binding; the isolated P-domain (GFP-NLS fusion) sufficed to bind DAXX. By contrast, anti-myc ChIP showed a ΔRRM1+2 mutant failed to load onto telomeres, α-satellite, SatIII, SatII and AluS, whereas ΔP retained chromatin loading. RRM1/RRM2 are required for R-loop chromatin binding; the P-domain is specifically required for DAXX recruitment.
- **SFPQ sustains ATRX protein.** DAXX partners ATRX (silenced in U-2 OS, expressed in H1299). SFPQ depletion in H1299 reduced ATRX protein (not mRNA); MG132 restored it, indicating ATRX is proteasomally degraded without SFPQ. SFPQ loss also raised DAXX protein/mRNA by ~20%.
- **A patient P-domain mutation is dominant-negative.** Whole-exome sequencing of an osteosarcoma cohort (31 patients; two disabling SFPQ mutations) identified a non-frameshift Tyr150→Lys-Pro substitution (T150delinsKP, "SFPQ nFS") in the P-domain. SFPQ nFS showed impaired HA-DAXX binding and, when expressed, drove DAXX delocalization, replication stress and micronuclei dominant-negatively, worsened by depletion of endogenous SFPQ.
- **SFPQ loss causes replication stress, DNA damage and mitotic chaos.** ChIP showed increased ATR, RPA32 and γH2AX at telomeres, subtelomeres, α-satellite, SatII, SatIII and SINE/LINE repeats, with FANCD2/RAD51 recruitment. Native metaphase spreads showed centromeric p-ATR(Thr1989), p-RPA32(Ser33) and pericentric SatIID transcript accumulation; time-lapse of GFP-H2B cells showed increased chromatin bridges, multilobular cells and micronuclei; Giemsa/SCE assays showed increased chromatid breaks and sister-chromatid exchanges in U-2 OS and MCF-10A.
- **Genome instability activates cGAS–STING innate immunity.** RNA-seq of SFPQ-depleted U-2 OS found 1,268 up / 1,163 down genes, with GO enrichment for cytokine production, antiviral defense and innate immunity, and a 29-gene innate-immunity/ISG signature (IFIT1/2/3, STING1, OASL, MX2, OAS2, DDX60, CCL5, CXCL10, AIM2, ZBP1, RSAD2, IL1A, APOBEC3H, HERC5 etc.). SFPQ or DAXX loss increased cGAS-positive micronuclei and cytoplasmic dsDNA, induced p-IRF3, p-STING, and NF-κB/IRF3 target genes (qPCR + WB).
- **R-loops are the upstream cause.** Inducible mCherry-RNaseH1 expression suppressed micronuclei in SFPQ- or DAXX-depleted cells and blocked 10/11 pro-inflammatory genes; the STING antagonist H151 suppressed IFIT1, IFNB1, CXCL10, IL1A, IRF2, IL12 without changing CGAS/STING/IL8. IL8 induction was RNaseH1-independent (SFPQ is a known IL8 transcriptional repressor).
- **Clinical correlation in sarcoma.** In TCGA pan-cancer, SFPQ was not prognostic overall, but in sarcoma high SFPQ correlated with reduced survival, while the 29-gene innate-immunity signature correlated with improved survival; SFPQ expression inversely correlated with the signature. Patients with low SFPQ + high signature had markedly better overall survival. Authors frame SFPQ–DAXX disruption as a way to stimulate antitumor immunity / boost STING-agonist efficacy in sarcoma.

## Methods

- **Cells:** U-2 OS (osteosarcoma), H1299 (NSCLC), MCF-7, MCF-10A, MCF-7, HEK293; U-2 OS TetON-mCherry-RNaseH1 (dox-inducible); stable U-2 OS lines expressing myc-tagged SFPQ deletion mutants (selected for analysis of truncated variants by 5′UTR-specific siRNA depletion of endogenous SFPQ).
- **R-loop / repeat assays:** immuno-dot blot (S9.6) of DNA:RNA hybrids; C0t-1 RNA-FISH (non-denaturing); DRIP-PCR across repeat classes; anti-SFPQ and anti-myc ChIP-qPCR; ChIP for ATR/RPA32/γH2AX/FANCD2/RAD51; S9.6 specificity validated with RNaseT1/T3/H1.
- **In vitro binding:** EMSA with 5′-[6-FAM] ssDNA, ssRNA, dsDNA, dsRNA, DNA:RNA duplex, DNA bubble, D-loops and R-loops (with/without ssRNA tails; repeat-RNA tails), plus competition assays; recombinant His6-myc-SFPQ from E. coli.
- **Interaction mapping:** anti-myc IP-MS (MALDI-TOF, ProteinPilot/Paragon); reciprocal co-IP (myc-SFPQ / HA-DAXX); endogenous co-IP; recombinant GST-DAXX-HA + His6-myc-SFPQ FL/ΔP pull-down; SFPQ deletion panel (ΔN, ΔP, ΔRGG, ΔRRM1, ΔRRM2, ΔRRM1+2, nFS).
- **Chromatin/epigenome:** ChIP-seq for SFPQ, DAXX, H3.3 in control vs SFPQ-knockdown U-2 OS; ChIP-PCR validation; genomic-region annotation and H3.3 log2FC AUC analysis (Wilcox, FDR-adjusted).
- **Genome stability:** native metaphase chromosome spreads + immuno-RNA-FISH (SatIID, telomere, CREST); GFP-H2B time-lapse microscopy; UV/Giemsa SCE and chromosome-break scoring (BrdU two-round labeling); cGAS / dsDNA / micronuclei immunofluorescence; super-resolution SIM (ZEISS ELYRA 7).
- **Immune/clinical readouts:** RNA-seq + GO/network analysis; qRT-PCR and WB for cGAS-STING/IFN/NF-κB targets; STING antagonist H151; inducible RNaseH1 rescue; TCGA pan-cancer and sarcoma survival/correlation (Kaplan-Meier, log-rank); osteosarcoma WES cohort (SFPQ mutations).

## Connections

- [P-Bodies and mRNA Regulation](../topics/p-bodies-and-mrna-regulation.md) — topic hub. SFPQ is an RNA-binding protein of the DBHS/paraspeckle family relevant to nuclear RNP granules and RNA-repeat metabolism; this paper extends the wiki's repeat-element / retrotransposon-defense axis from cytoplasmic P-bodies into nuclear R-loop surveillance at LINE-1, SINE and satellite repeats.
- [Kodali 2024 — RNA sequestration in P-bodies sustains myeloid leukaemia](../sources/kodali-2024-rna-sequestration-pbodies-sustains-myeloid-leukaemia.md) — both link RNA-binding-protein condensate/granule biology to cancer chromatin state; here the coupling runs through R-loop suppression and H3.3 deposition rather than cytoplasmic translational sequestration.

## Open Questions

- **How is SFPQ-directed H3.3 deposition partitioned between ATRX-dependent and ATRX-independent DAXX functions?** Authors note DAXX also acts via a SETDB1–KAP1–HDAC1 complex (with SMARCAD1) at ERVs; the role of R-loops/SFPQ in coordinating these routes is unresolved.
- **Does SFPQ act on LINE-1 retrotransposition itself, or only on R-loop/chromatin stability at LINE-1 loci?** The paper measures R-loops, H3.3 and damage at LINE elements but not retroelement mobilization.
- **What is the contribution of repeat RNAs escaping R-loops vs cytoplasmic R-loops vs promoter chromatin changes to the interferon response?** Authors explicitly cannot exclude these alternative cytoplasmic-DNA / ISG sources.
- **Is the SFPQ–DAXX axis a tractable immunotherapy target in sarcoma?** Whether pharmacologic disruption (to raise cGAS-STING activity and boost STING agonists / checkpoint therapy) is achievable and selective remains untested.

## Sources

- Local PDF: `raw/inbox/papers/ferrando-2026-sfpq-directs-histone-deposition-loops-dna.pdf`
- DOI: [10.1038/s41467-026-69479-w](https://doi.org/10.1038/s41467-026-69479-w)
