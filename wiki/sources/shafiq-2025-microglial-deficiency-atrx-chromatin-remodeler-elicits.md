---
title: "Microglial deficiency in the ATRX chromatin remodeler elicits a viral mimicry immune response that impacts neuronal function and behavior"
authors:
  - "Shafiq S"
  - "Ghahramani A"
  - "Mansour K"
  - "Pena-Ortiz M"
  - "Sunstrum JK"
  - "Pavlovic M"
  - "Jiang Y"
  - "Rowland ME"
  - "Inoue W"
  - "Bérubé NG"
year: 2025
journal: "PLoS Biology"
doi: "10.1371/journal.pbio.3002659"
pdf: "raw/inbox/papers/shafiq-2025-microglial-deficiency-atrx-chromatin-remodeler-elicits.pdf"
paper_kind: mechanistic
themes:
  - atrx
  - viral-mimicry
  - transposable-element
  - microglia
  - innate-immunity
  - interferon
  - retroelement-derepression
  - chromatin-accessibility
tags:
  - source
  - viral-mimicry
  - interferon
  - retrotransposon
  - atrx
  - neuroinflammation
pdf_status: full-text-read
---
# Microglial deficiency in the ATRX chromatin remodeler elicits a viral mimicry immune response that impacts neuronal function and behavior

_PLoS Biology, 2025._

## Summary

Targeted deletion of the Snf2-type chromatin remodeler **ATRX** in microglia of the mouse central nervous system (tamoxifen-inducible Cx3cr1ERT2; AtrxLoxP "ATRX miKO") de-condenses heterochromatin, de-represses endogenous retroelements, and triggers a **viral mimicry** innate-immune response. ATRX, together with its partner DAXX, normally deposits the histone variant H3.3 at repetitive genomic regions including telomeres, pericentric repeats, rDNA, and endogenous retroviral elements. Loss of ATRX in microglia produces globally increased chromatin accessibility (94% of 32,936 differentially accessible regions gained accessibility), aberrant transcription (6,168 DEGs), DNA damage, and proliferation. The de-repressed retroelements (LTR classes ERVK/ERVL, plus LINEs and SINEs) are bidirectionally transcribed, generating cytoplasmic double-stranded RNA (dsRNA) detectable with the J2 antibody. This cytosolic nucleic acid — together with DNA damage — engages the DNA/RNA-sensing pattern-recognition receptors **cGAS** and **RIG-1 (Dhx58)**, driving STAT1 phosphorylation, broad induction of **interferon-stimulated genes (ISGs)** (Mx1/2, Ifit1/3, Isg15/20, Oas family, Rsad2, Bst2), and cytokine/chemokine release (CCL2/5/12/17, CXCL9/10). The microglial immune activation has non-cell-autonomous consequences: hippocampal CA1 pyramidal neurons show altered dendritic morphology and electrophysiology, and the mice exhibit impaired long-term spatial memory and reduced anxiety. The work positions ATRX-maintained heterochromatin as a brake on retroelement-driven viral mimicry and links chromatin dysregulation in glia to neuronal dysfunction in ATR-X syndrome.

## Key Points

- **ATRX loss alters microglial morphology and disrupts homeostasis.** ATRX miKO microglia (>90% of Sun1GFP+ cells lack ATRX) develop elongated, rod-shaped somas and nuclei, are larger and hyper-ramified (Sholl: two-way ANOVA F(1,44)=8.857, p=0.0047; increased segment length F(1,36)=4.570, p=0.0394), and show a transient increase in lysosomal **CD68** foci (cortex 2 mo p=0.036, 3 mo p=0.005) that resolves by 6 months — a phenotype resembling Interferon-α–activated microglia.
- **Transcriptome shows proliferation, genome-integrity, and innate-immune activation.** RNA-seq of FANS-sorted microglia identified **6,168 DEGs** (3,265 up, 2,903 down; Adj p<0.05). Upregulated GSEA categories spanned cell cycle (Ccnb1, E2F2/3/7/8, Cdc25c, Mcm10), DNA repair/replication stability (Rad51, Fanca, Gen1, Blm, DNA2), and immune/inflammatory signaling (Cd69, Cd72, Axl, Mx1, Mx2, Tnf, Stat2, Cxcl10).
- **DNA damage and proliferation confirmed by imaging.** γ-H2AX foci (DNA double-strand-break marker) are increased in ATRX-null microglia (cortex p=0.003, hippocampus p=0.018) and Ki67+ proliferating microglia rise at 2 months (cortex p=0.020; hippocampus p=0.0005), largely resolving by 3 months. Deconvolution inferred increased "activated response" and "interferon response" microglial subclusters at the expense of homeostatic microglia.
- **Globally increased chromatin accessibility.** ATAC-seq identified **32,936 DARs** (Adj p<0.05), 94% with increased accessibility in ATRX-null microglia, concentrated at gene TSS; ~47% (2,945/6,182) of DEGs carried a DAR at their TSS, coupling chromatin opening to transcriptional activation.
- **Interferon TF motifs gain accessibility.** Of 30 TFs with increased differential binding scores (top 2%, TOBIAS), interferon-signaling TFs **IRF1, IRF7, IRF9, STAT1, STAT2, ELK1, MEF2C, ZNF384** had increased binding-site accessibility, confirming broad instigation of an interferon response.
- **Retroelement de-repression at chromatin and transcript level.** 11,155 DARs in repetitive sequences (>99% more accessible), enriched for LTR classes **ERVK and ERVL** plus non-LTR **LINEs and SINEs**; RNA-seq found **20,189 differentially expressed retroelements** with 71% de-repressed in ATRX-null microglia. RetroTector flagged a subset of upregulated ERVs as full-length (3%, n=99) with the majority solo LTRs (83%, n=2,641).
- **Cell-type specificity.** Deletion of ATRX in oligodendrocytes or astrocytes did **not** cause comparably extensive retroelement de-repression, indicating microglial retroelement suppression is particularly sensitive to ATRX loss.
- **Bidirectional TE transcription generates dsRNA.** 4,480 (forward) and 5,226 (reverse) differentially expressed TEs were detected, with 57 TEs significantly expressed from both strands — consistent with formation of immunogenic dsRNA. J2 immunostaining of primary cultures revealed cytoplasmic dsRNA accumulation in Ai14+ ATRX-null microglia.
- **TE-derived dsRNA reaches the cytoplasm.** J2 RNA-immunoprecipitation + RT-qPCR showed top-upregulated TEs **ERVB2_1-I MMdup5** and **MLT1C_LTR-ERVL** enriched in cytoplasmic fractions of ATRX miKO (not control) brain; ERVB2 is evolutionarily younger with higher viral-mimicry potential.
- **DNA/RNA-sensing pathway activation.** **cGAS** (dsDNA sensor → cGAMP → STING1) and **RIG-1/Dhx58** (dsRNA sensor → MAVS) are overexpressed; western blots confirm increased RIG-1 (p=0.002) and cGAS (p=0.047) protein, and increased total STAT1 (p=0.001) and phospho-STAT1 (p=0.042).
- **Broad ISG induction.** Downstream of STAT activation, ISGs are upregulated in ATRX-null microglia: **Bst2, Ch25h, Ifit1, Ifit3, Ifit3b, Ifitm3, Isg15, Isg20, Mx1, Mx2, Oas1a/1b/1g, Oas2, Oas3, Oasl1, Oasl2, Pml, Rsad2** (all p<0.05).
- **Cytokine/chemokine release.** A cytokine array of cortical extracts showed elevated **CCL2 (p=0.001), CCL5 (p=0.020), CCL12 (p=0.000), CCL17 (p=0.032), CXCL9 (p=0.000), CXCL10 (p=0.000)** in ATRX miKO mice (possibly amplified by secondary astrocytosis).
- **Non-cell-autonomous neuronal effects.** CA1 pyramidal neurons in ATRX miKO mice show increased dendritic branching, increased filopodia-spine density (p=0.0220), lower membrane (input) resistance (p=0.017) with unchanged capacitance, increased action-potential amplitude (p=0.009), and a leftward shift in sEPSC amplitude (Kolmogorov–Smirnov p<0.0001).
- **Behavioral deficits.** ATRX miKO mice show impaired long-term spatial memory (Morris water maze 12-day probe) and a 24-h novel-object recognition deficit (p=0.0013), plus reduced anxiety (light-dark box p=0.039; elevated plus maze p=0.032); locomotion, working memory, and contextual fear memory were intact.

## Methods

- **Microglia-specific Atrx deletion**: tamoxifen-inducible Cx3cr1ERT2-Cre × AtrxLoxP male mice ("ATRX miKO"), with Sun1GFP nuclear-membrane and Tomato-Ai14 cytoplasmic reporters to track Cre+ microglia; control comparisons to astrocyte (Glast-CreER) and OPC/oligodendrocyte (Sox10-iCreERT2) Atrx deletions.
- **Fluorescence-activated nuclei sorting (FANS)** of Sun1GFP+ microglia nuclei from cortex/hippocampus for **RNA-seq** (rRNA-depleted, strand-specific) and **ATAC-seq**; differential expression and DARs (MACS2-DESeq2 and csaw-EdgeR; Adj p<0.05).
- **Retroelement/TE analysis**: TE-aware RNA-seq quantification, subfamily analysis, RetroTector (full-length vs solo-LTR ERV classification), forward/reverse strand-specific TE expression for bidirectional transcription; ERV classification pipeline (GitHub/Zenodo archived).
- **TF footprinting**: TOBIAS differential binding-score scan across annotated TF motifs in ATAC-seq DARs.
- **dsRNA detection**: J2 anti-dsRNA antibody immunofluorescence on primary mixed glial cultures (7 DIV); J2-conjugated-bead RNA immunoprecipitation of cytoplasmic cerebellar fractions + RT-qPCR for ERVB2_1-I MMdup5 and MLT1C_LTR-ERVL.
- **Sensing-pathway readouts**: western blots for cGAS, RIG-1, STAT1, phospho-STAT1; ISG expression from RNA-seq (VST counts); cytokine/chemokine array of cortical protein extracts.
- **Validation imaging**: γ-H2AX (DSB marker), Ki67 (proliferation), CD68, IBA1 immunofluorescence; microglia morphology by Sholl analysis, convex-hull volume, branching order (Neurolucida).
- **Neuronal phenotyping**: Thy1GFP-M sparse labeling for CA1 dendrite Sholl/spine analysis; whole-cell current- and voltage-clamp electrophysiology (input resistance, capacitance, AP amplitude, sEPSC).
- **Behavior**: open field, light-dark box, elevated plus maze, Y-maze, novel object recognition, contextual fear conditioning, Morris water maze (≥15 mice/genotype, blinded/randomized, ARRIVE guidelines).

## Connections

- [P-Bodies and mRNA Regulation](../topics/p-bodies-and-mrna-regulation.md) — topic hub; this paper supplies the **immune-ISG / retrotransposon-defense** axis (viral mimicry from de-repressed transposable elements → cGAS/RIG-1 sensing → interferon), the downstream sensing layer that connects cytoplasmic RNA dysregulation to innate immunity.
- [Kodali 2024 — RNA sequestration in P-bodies sustains myeloid leukaemia](../sources/kodali-2024-rna-sequestration-pbodies-sustains-myeloid-leukaemia.md) — shared theme of chromatin-coupled RNA biology and a tumour-suppressor/immune axis; both link cytoplasmic RNA fate to chromatin state, here via retroelement de-repression rather than P-body sequestration.

## Open Questions

- **Which TE-derived nucleic-acid species is the dominant trigger?** The paper implicates both cytoplasmic dsRNA (RIG-1) and DNA-damage-derived cytosolic DNA (cGAS); the relative contribution of each sensing arm to the interferon response is not dissected.
- **Why are microglia uniquely sensitive to ATRX loss for retroelement suppression?** Astrocytes and oligodendrocytes do not de-repress retroelements as extensively; the authors hypothesize lower baseline DNA methylation at retroelements in microglia, but this is untested.
- **Which alteration drives the neuronal phenotype?** It remains unclear whether cytokines/chemokines, type-I interferon paracrine signaling, or altered microglia-neuron physical interaction is responsible for the CA1 morphological/electrophysiological changes and spatial-memory deficit.
- **How well does the murine viral-mimicry mechanism translate to human ATR-X syndrome?** Human ERVs are highly mutated and lack retrotranspositional capacity, potentially limiting their direct immunogenicity relative to the more active murine LTR elements.

## Sources

- Local PDF: `raw/inbox/papers/shafiq-2025-microglial-deficiency-atrx-chromatin-remodeler-elicits.pdf`
- DOI: [10.1371/journal.pbio.3002659](https://doi.org/10.1371/journal.pbio.3002659)
