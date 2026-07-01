---
title: "Retrotransposon LINE-1 bodies in the cytoplasm of piRNA-deficient mouse spermatocytes: Ribonucleoproteins overcoming the integrated stress response"
authors:
  - "De Luca C"
  - "Gupta A"
  - "Bortvin A"
year: 2023
journal: "PLoS Genetics"
doi: "10.1371/journal.pgen.1010797"
pdf: "raw/inbox/papers/deluca-2023-retrotransposon-line-bodies-cytoplasm-pirna-deficient.pdf"
paper_kind: mechanistic
themes:
  - line-1
  - rnp-granule
  - pirna
  - stress-granule
  - integrated-stress-response
  - orf1p
  - retrotransposon-defense
  - condensate-biophysics
tags:
  - source
  - p-body
  - line-1
  - stress-granule
  - rnp-granule
pdf_status: full-text-read
---
# Retrotransposon LINE-1 bodies in the cytoplasm of piRNA-deficient mouse spermatocytes: Ribonucleoproteins overcoming the integrated stress response

_PLoS Genetics, 2023._

## Summary

To understand how retrotransposon LINE-1 (L1) endures despite host defenses, the authors characterized **LINE-1 Bodies (LBs)** — large cytoplasmic ORF1p condensates that form in meiotic male germ cells (spermatocytes) of piRNA-deficient *Maelstrom* (Mael)-null mice, which overexpress L1. LBs are hybrid RNP granules: they concentrate L1 ORF1p, L1 RNA, and ribosomes, and reach up to 3 μm — larger than stress granules (SGs, ≤2 μm) or P-bodies (PBs, ≤0.5 μm) — while uniquely containing both 40S and 60S ribosomal subunits, which canonical SGs and PBs lack. By anti-ORF1p RNA-seq from EDTA-resistant RNP fractions and AP-MS, ORF1p is shown to bind young L1 (L1MdA/L1MdT) and MMERVK10C-int RNAs plus ~2081 genic mRNAs (driven by transcript abundance, not length), and to interact with **stress-granule proteins** (G3BP2, CAPRIN1, FMR1, FXR1, FXR2, ELAVL1, PABPC1, LARP1, MOV10, YBX1, DDX6), the **CCR4-NOT deadenylation complex** (catalytic CNOT6L/CNOT7, plus CNOT1 in LBs by IF), and ribosomal proteins (RNase-resistant, biased toward the 60S subunit). Paradoxically, despite this repressive cargo, LB-localized mRNAs show **no 5'/3' degradation, no increased deadenylation (poly(A) of Sycp1/Setx unchanged), and no loss of translation efficiency** (ribosome profiling), and bulk phospho-eIF2α is unchanged in Mael-/- testes. The key mechanism: ORF1p binds **PRKRA (RAX/PACT)**, an RNA-independent interactor and Protein Kinase R (PKR) factor, in LBs. In cultured cells, PRKRA co-expression elevates ORF1p levels and **stimulates L1 retrotransposition**, with a moderate reduction of eIF2α phosphorylation — suggesting L1 co-opts PRKRA to evade the integrated stress response (ISR) translational shut-off and promote its own propagation without compromising host RNA metabolism.

## Key Points

- **LBs are large ORF1p/L1-RNA/ribosome condensates distinct from SGs and PBs.** In Mael-/- spermatocytes, smaller LBs fuse into large bodies reaching **3 μm**, "exceeding the maximum sizes reported for Stress Granules (SGs, 2 μm) and Processing Bodies (p-bodies or PBs, 0.5 μm)." LBs are packed with ~25 nm electron-dense particles and sometimes associate with bilayer membranes; HCR RNA-FISH shows L1 RNA colocalizing with ORF1p, and IF shows ribosomal proteins RPS6 and RPL28 throughout LBs.
- **ORF1p exists in both ribosome-independent RNPs and translating polysomes.** Sucrose-gradient fractionation of Mael-/- testes shows ORF1p across all fractions but enriched in polysomes; EDTA (ribosome dissociation) leaves ORF1p and L1 RNA co-sedimenting in fractions 5–8, and RNase digestion disrupts these complexes — indicating EDTA-resistant L1 RNPs distinct from L1 polysomes.
- **ORF1p binds young L1 and an ERV, but not SINEs.** Anti-ORF1p RNA-seq shows strong enrichment of evolutionarily young **L1MdA and L1MdT** RNAs and **MMERVK10C-int** ERV RNA, with a strong cis-preference for coding L1 RNA; unexpectedly, abundant **SINE B1/B2** and IAP RNAs are *not* enriched.
- **ORF1p amasses ~2081 genic mRNAs by abundance, not length.** 2081 transcripts associate with ORF1p (1347 enriched over TOTAL); enrichment correlates strongly with expression level (R² = 0.844) but **not** with transcript length (R² flat) — unlike SG/PB cargo, which is typically longer. Setx and MMERVK10c-int mRNAs colocalize with L1 RNA in LBs by HCR RNA-FISH.
- **ORF1p interacts with stress-granule proteins.** AP-MS of 80 high-confidence interactors places ORF1p in an "RNA granules" STRING network including **LARP1, G3BP2, MOV10, DDX6, FMR1, YBX1, ELAVL1 (ELAV1), PABPC1**, plus newly found **CAPRIN1, FXR1, FXR2** — "many of these proteins are exclusive for SGs, known to harbor ORF1p upon L1 overexpression in cultured cells."
- **ORF1p associates with the CCR4-NOT deadenylation complex.** Newly identified interactors include catalytic **CNOT6L and CNOT7** (but not scaffold CNOT1 or CNOT4 in MS). IF confirms **CNOT7** and (despite absence from MS) **CNOT1** redistribute into LBs with ORF1p; CCR4-NOT is "a global regulator of mRNA metabolism frequently recruited to PBs."
- **DDX6 redistributes from PB-like foci into LBs.** RNA helicase DDX6 (enriched in both PBs and SGs) forms cytoplasmic foci in control/ORF1p-negative cells but "clearly redistributed to LBs whenever present" in Mael-/- spermatocytes.
- **LBs coincide with disappearance of canonical P-bodies.** The PB decapping factor **DCP1A** is abundant in PBs of control samples but in Mael-/- is "mostly confined to prominent granules... at the periphery" with only weak diffuse signal in LBs, suggesting "L1 overexpression and LBs formation coincided with the disappearance of PBs."
- **LBs uniquely contain large (60S) ribosomal subunits.** Of ORF1p-associated ribosomal proteins, "six of eleven... and six newly discovered" are 60S components — "LBs are distinct from SGs, which contain the small (40S) but not large (60S) ribosomal subunits, and PBs, devoid of ribosomes altogether." ORF1p–ribosomal-protein interactions are RNase-resistant.
- **LB cargo is NOT degraded or deadenylated.** RNA-seq read coverage of ORF1p-bound (IP) mRNAs shows no 5'/3'-end reduction vs TOTAL; poly(A) tail lengths of **Sycp1 and Setx** are unchanged between Mael-/- and control P16 testes — so the resident CCR4-NOT does not deadenylate LB mRNAs.
- **LB cargo translation is unaffected; ISR not engaged.** Ribosome profiling of P16 testes shows no significant disruption of translation efficiency, including for the 1313 ORF1p-bound mRNAs (ΔTE n.s.); and **phospho-eIF2α is unchanged** between Mael-/- and Mael+/- testes — consistent with unperturbed translation.
- **ORF1p binds PRKRA (RAX/PACT), an RNA-independent PKR factor, in LBs.** PRKRA is detected in ORF1p IPs from both untreated and RNase-treated lysates (RNase-resistant) and colocalizes with ORF1p in LBs. PKR normally phosphorylates eIF2α to trigger ISR translational inhibition; the authors propose ORF1p sequesters/redirects PRKRA (possibly substituting for TARBP2) to preclude PKR activation.
- **PRKRA stimulates L1 retrotransposition and raises ORF1p.** In HeLa cells, ectopic mouse PRKRA co-expressed with L1spa (pTN201) **enhances retrotransposition** (5 replicates); L1spa RNA falls ~25% yet **ORF1p protein rises**, and eIF2α phosphorylation is moderately reduced — implicating PRKRA-mediated relief of translational inhibition.
- **Model — L1 acts virus-like to overcome translational shut-off.** Like viruses, L1 "encodes an active mechanism that counteracts cellular defenses"; by co-opting PRKRA/PKR rather than globally inhibiting cap-dependent translation, L1 boosts its own ORF1p/mobilization without compromising host RNA metabolism — a strategy the authors speculate is relevant to L1 in aging and disease in somatic cells that naturally lack piRNAs.

## Methods

- **In vivo model**: C57BL/6 *Maelstrom* (Mael) mutant mice; Mael-/- spermatocytes overexpress L1 and form ORF1p+ LBs. Testes from WT, Mael+/- and Mael-/- (~3 months) used for EM, IF, RNA-FISH and biochemistry.
- **Imaging**: electron microscopy of LBs; immunofluorescence for ORF1p, RPS6, RPL28, DDX6, CNOT7, CNOT1, DCP1A, PRKRA (with same-species double-labeling via Zenon / Mix-n-Stain direct conjugation); 3D confocal reconstruction; HCR RNA-FISH (v3.0) for L1 RNA (L1spa probes), MMERVK10c-int, Setx, U6 snRNA control.
- **Fractionation**: 10–50% linear sucrose-gradient ultracentrifugation of testicular extracts with cycloheximide (polysome preservation) or EDTA (ribosome dissociation) ± RNase A/T1; Western blot (ORF1p, RPS6) and qRT-PCR (L1 ORF1 amplicon, Actb) per fraction.
- **RNP RNA content**: anti-ORF1p immunoprecipitation from pooled EDTA-resistant fractions 5–8 + RNA-seq, compared to TOTAL, INPUT and beads-only (BO); analysis of genomic repeat RNAs and genic mRNAs (log2FC > 1, padj < 0.05).
- **Interactome**: anti-ORF1p co-IP + mass spectrometry from total Mael-/- testis extracts (two replicates; 80 high-confidence interactors), with/without RNase pretreatment to score RNA-dependency; STRING network analysis.
- **Translation/decay readouts**: RNA-seq 5'/3' coverage binning (10 bins) for degradation; PCR-based poly(A) tail-length assay (Sycp1, Setx, P16 testes); ribosome profiling (Ribo-seq) of P16 testes for translation efficiency; Western blot of phospho-eIF2α (Ser51) vs pan-eIF2α.
- **PRKRA / L1 functional assays**: 3XFLAG-PRKRA expression plasmid (pPRKRA, P2A-EGFP); transfection in mouse F9 cells (endogenous L1) and HeLa cells; ORF1p–PRKRA co-IP and colocalization; L1 retrotransposition assay (mouse L1spa pTN201 + synthetic pCEPsmL1 / catalytically inactive mutant) ± pPRKRA, with neo-resistant colony counts corrected by a pPAGFP control; qRT-PCR of L1 RNA, Western blot of ORF1p and phospho-eIF2α in HeLa.

## Connections

- [P-Bodies and mRNA Regulation](../topics/p-bodies-and-mrna-regulation.md) — topic hub; LBs are a third cytoplasmic RNP granule that shares CCR4-NOT, DDX6 and DCP1A with P-bodies yet behaves oppositely (no decay/repression of cargo).
- [Kodali 2024 — RNA sequestration in P-bodies sustains myeloid leukaemia](../sources/kodali-2024-rna-sequestration-pbodies-sustains-myeloid-leukaemia.md) — contrast: in AML, P-body sequestration *represses* translation of cargo (tumour suppressors); in LBs, ORF1p amasses mRNAs and CCR4-NOT/DDX6 *without* repressing them.

## Open Questions

- **Why is CCR4-NOT catalytically silent in LBs?** The deadenylase subunits (CNOT6L/CNOT7) are present yet poly(A) tails are unchanged. The authors speculate inactivation (e.g. by RNF219-like factors) or a non-canonical role such as facilitating co-translational ORF1p trimer assembly.
- **Are LBs sites of active translation rather than storage/decay?** Ribosome content and unchanged TE of cargo (e.g. Setx) hint LBs may host translation, unlike SGs/PBs — but this is not directly demonstrated.
- **What is the precise ORF1p–PRKRA–PKR mechanism?** Does ORF1p sequester PRKRA away from PKR, or actively induce PRKRA to inhibit PKR (TARBP2-like heterodimer substitution)? And is ORF1p augmentation translational or post-translational (protein stabilization)?
- **How relevant is the LB/PRKRA mechanism to somatic L1 in aging and disease?** Somatic cells naturally lack piRNAs; whether this ISR-evasion strategy operates there is speculative.

## Sources

- Local PDF: `raw/inbox/papers/deluca-2023-retrotransposon-line-bodies-cytoplasm-pirna-deficient.pdf`
- DOI: [10.1371/journal.pgen.1010797](https://doi.org/10.1371/journal.pgen.1010797)
