---
title: "In vivo CRISPR screens identify CBX4 as an epigenetic regulator for cancer immunotherapy"
authors:
  - "Ma Z"
  - "Jia W"
  - "Zhou X"
  - "Liu J"
  - "Li Q"
  - "Chang R"
  - "Shiqi G"
  - "Yuan N"
  - "Chen Z"
  - "Lan P"
year: 2026
journal: "Journal of Clinical Investigation"
doi: "10.1172/JCI200564"
pdf: "raw/inbox/papers/ma-2026-vivo-crispr-screens-identify-cbx-epigenetic.pdf"
paper_kind: mechanistic
cancer_types:
  - hepatocellular-carcinoma
  - colon-cancer
  - melanoma
modalities:
  - crispr-screen
  - functional-genomics
themes:
  - cbx4
  - viral-mimicry
  - transposable-element
  - immunotherapy
  - innate-immunity
  - endogenous-retrovirus
  - epigenetic-silencing
tags:
  - source
  - retrotransposon
  - viral-mimicry
  - immunotherapy
  - cancer
pdf_status: full-text-read
---
# In vivo CRISPR screens identify CBX4 as an epigenetic regulator for cancer immunotherapy

_Journal of Clinical Investigation, 2026._

## Summary

In vivo CRISPR/Cas9 screens targeting epigenetic factors in immune-checkpoint-blockade (ICB)-treated mouse tumour models identified **chromobox 4 (CBX4)** — a SUMO E3 ligase and component of the canonical polycomb-repressive complex 1 (PRC1) — as a key negative regulator of the immune tumour microenvironment (TME). A focused lentiviral library (10 sgRNAs each for 998 epigenetics-related genes) was transduced into Hepa1-6 (HCC) and MC38 (colon) cells and transplanted into immunocompetent WT mice, ICB-treated WT mice, and immunodeficient NSG controls; sgRNAs targeting the polycomb-repressive complex pathway, with **Cbx4 among the most depleted**, were lost selectively under immune pressure. CBX4 is overexpressed in HCC, accumulates in nonresponders to anti-PD-1 therapy in both tumour cells and immunosuppressive tumour-associated macrophages (TAMs), and predicts poor outcome. Deletion of Cbx4 in tumour cells (sgCbx4) or myeloid cells (LysMCre Cbx4fl/fl) inhibited tumour growth in a CD8+ T cell- and NK cell-dependent manner, shifted macrophages toward M1-like states, and increased MHC-I. Mechanistically, CBX4 silences **H3K9me3- and H3K27me3-marked endogenous retroelements (ERVs), notably RLTR4-Mm-int**. Loss of CBX4 lowered the repressive marks at the RLTR4-Mm-int locus, derepressed retrotransposons, and produced cytosolic dsRNA that activated the **RIG-I cytosolic RNA-sensing pathway and a type I IFN response** (RIG-I, not cGAS, was the essential sensor). CBX4 interacts with EZH2 (H3K27me3) and SETDB1 (H3K9me3) by IP-MS. The CBX4 inhibitor UNC3866 phenocopied genetic loss and synergized with anti-PD-1 in syngeneic models and humanized-mouse PDX. The work establishes CBX4 as an "epigenetic immune checkpoint" that enforces retrotransposon silencing, and ERV: RLTR4_Mm_int / CBX4 inhibition as immunotherapy-sensitizing strategies.

## Key Points

- **Focused in vivo CRISPR screen pinpointed CBX4 as an immune-evasion target.** A library of **10 sgRNAs for each of 998 epigenetics-related genes** was screened in Hepa1-6 (HCC) and MC38 (colon) tumours across NSG, WT, and ICB-treated WT mice; sgRNAs targeting the polycomb-repressive complex pathway were "predominantly depleted in tumor cells under immune pressure," with **Cbx4 ranking among the most depleted** hits. Known hits Ezh2, Setdb1, Ep300, Mettl14 were also recovered.
- **Validation: KO of Cbx4, Kdm8, Ezh2, or Kdm2a sensitized tumours to anti-PD-1** in Hepa1-6 tumour-bearing mice.
- **CBX4 is overexpressed in HCC and marks aggressive, ICB-resistant disease.** Across 92 paired HCC/normal samples (Tongji cohort 2) plus TCGA/CPTAC, CBX4 was significantly higher in tumour than normal tissue, higher in advanced stage, an independent risk factor by Cox regression, and "high CBX4 expression was associated with resistance to immunotherapy across multiple cancer types" (HCC, colorectal, melanoma, urothelial).
- **CBX4 accumulates in nonresponders in both tumour cells and immunosuppressive TAMs.** scRNA-seq and spatial transcriptomics of neoadjuvant anti-PD-1 patients showed CBX4 "highly expressed in tumor cells and subpopulations of immunosuppressive tumor-associated macrophages" and "significantly enriched in the tumor tissues of nonresponders compared with responders." MAZ was identified as a transcription factor driving Cbx4 (Maz binds the Cbx4 promoter P1/P2 sites; MAZ/CBX4 positively correlated; both elevated in nonresponders).
- **Loss of CBX4 in tumour cells induces CD8+ T cell- and NK cell-dependent antitumor immunity.** sgCbx4 Hepa1-6 tumours showed increased T cells, NK cells, DCs and decreased Spp1+ macrophages; rises in cytotoxic Tef (IFN-γ+TNF-α+, perforin+granzyme B+), Tpex (PD-1+TIM3−TOX+TCF1+), and cyto-NK cells, with fewer Tregs and Tex cells. Effect was immune-dependent: targeting Cbx4 "only slightly inhibited tumor growth in NSG mice," and depletion of CD8+ T and NK cells "abolished the effect of Cbx4 ablation on tumor progression." sgCbx4 tumour cells upregulated antigen-presentation genes B2m, H2-D1 and the chemokine Cxcl10.
- **CBX4 deletion in macrophages (LysMCre Cbx4fl/fl) reprograms TAMs toward an immunostimulatory M1-like state.** scRNA-seq showed increased M1-like C1qc+ and Ccr2+ macrophages and decreased immunosuppressive Spp1+/Arg1+ macrophages; flow cytometry showed more CD86+ and fewer CD206+ TAMs, increased MHC-I (H2-Db) and PD-L1, and enhanced antigen presentation to OT-I CD8+ T cells. This also acted in a CD8+ T cell- and NK cell-dependent manner.
- **CBX4 loss activates type I IFN via cytosolic RNA sensing.** KEGG/GSEA of Cbx4-deficient tumour cells and TAMs showed upregulated type I IFN, RIG-I-like receptor signaling, cytosolic DNA-sensing, and antigen-presentation pathways; increased mRNA/protein of RIG-I, MAVS, cGAS and phospho-IRF3/IRF7/STAT1/NF-κB.
- **RIG-I, not cGAS, is the essential sensor.** "loss of RIG-I completely reversed Cbx4 ablation-induced interferon-stimulated gene (ISG) and inflammatory gene expression," whereas cGAS loss "only modestly declined" the signal. Cbx4/RIG-I double ablation attenuated the tumour-suppressive and immune effects of Cbx4 loss; Cbx4/cGAS, Cbx4/Mavs, Cbx4/Sting1 did not.
- **CBX4 represses H3K9me3- and H3K27me3-marked ERVs, especially RLTR4-Mm-int.** Targeting Cbx4 induced cytosolic/tumour dsRNA (J2 antibody) and bidirectional transcription of LTR-containing ERVs and non-LTR elements, with **RLTR4-Mm-int a top Cbx4-ablation-induced ERV in TAMs**. Global DNA methylation (5-mC) was unchanged, implicating histone modification. Cbx4 deficiency decreased H3K9me3 and H3K27me3 levels and "decreased binding of the H3K9me3 and H3K27me3 repressive marks at the RLTR4-Mm-int loci."
- **RLTR4-Mm-int is a functional effector.** Its knockdown "decreased type I IFN responses without affecting the expression of other ERVs"; Cbx4/RLTR4-Mm-int double knockdown "restored the tumor-suppressive and immune-modulatory effects associated with Cbx4 deficiency" (i.e., reversed Cbx4-loss benefit), placing the ERV downstream.
- **ERV: RLTR4_Mm_int is therapeutic.** Intratumoral injection of an ERV: RLTR4_Mm_int dsRNA construct inhibited Hepa1-6 and MC38 growth, boosted cytotoxic CD8+ T and NK cells, and synergized with anti-PD-1 for "robust and durable antitumor responses."
- **CBX4 partners with EZH2 and SETDB1.** Anti-CBX4 IP-MS showed CBX4 "specifically interacted with the epigenetic regulators EZH2 (primarily targets H3K27me3) and SETDB1 (primarily targets H3K9me3)," but not EP300 or KDM5B. EZH2 inhibitor GSK126 and SETDB1 inhibitor SETDB1-TTD-IN-1 reversed CBX4-overexpression-induced immunosuppression.
- **Pharmacological CBX4 inhibition (UNC3866) sensitizes tumours to anti-PD-1.** UNC3866 phenocopied genetic loss (M1 TAM shift, increased MHC-I, more CD8+ T/NK cells), was immune-dependent (mild effect in Rag−/−γc−/−), and combined with ICB for durable responses in syngeneic Hepa1-6/B16 models and humanized-mouse HCC PDX.
- **Clinical anti-correlation.** CBX4 expression negatively correlated with antigen-presentation/innate-immunity/T-cell-activation genes and with ERVs (ERVmap_2550, ERVmap_2192, ERVmap_705), which were higher in anti-PD-1 complete responders; dsRNA (J2) was higher in low-CBX4 responders than high-CBX4 nonresponders.

## Methods

- **In vivo CRISPR/Cas9 screen**: lentiviral focused library (10 sgRNAs × 998 epigenetics genes) in Hepa1-6 and MC38 cells, transplanted into NSG (control), WT, and ICB-treated WT C57BL/6J mice; depletion/enrichment of sgRNAs under immune pressure with core-pathway enrichment analysis.
- **Genetic models**: tumour-cell sgCbx4 KO and Cbx4 shRNA knockdown; myeloid-conditional LysMCre Cbx4fl/fl (cKO) mice; stable Cbx4/RIG-I, Cbx4/cGAS, Cbx4/Mavs, Cbx4/Sting1 double-ablation and Cbx4/RLTR4-Mm-int double-knockdown Hepa1-6/MC38 lines; Cbx4-overexpressing lines.
- **Immune profiling**: scRNA-seq and spatial transcriptomics of tumours and of neoadjuvant anti-PD-1 patient cohorts; flow cytometry of T-cell/NK/macrophage subsets; multiplex IHC (Tongji cohorts); CellPhoneDB cell-cell interaction inference; OVA/OT-I coculture and adoptive transfer into Rag−/−γc−/− mice; CD8/NK depleting-antibody experiments.
- **Mechanism**: KEGG/GSEA on RNA-seq; Western blot and qPCR for RIG-I/MAVS/cGAS/p-IRF3/IRF7/STAT1/NF-κB; siRNA knockdown of dsDNA/dsRNA sensors; J2 dsRNA staining; retroelement RNA-seq (LTR/non-LTR ERV quantification); MethylFlash 5-mC ELISA; CUT&Tag for Cbx4/H3K9me3/H3K27me3 (IGV at RLTR4-Mm-int locus); anti-CBX4 IP-MS; rescue with EZH2 inhibitor GSK126 and SETDB1 inhibitor SETDB1-TTD-IN-1.
- **Clinical/therapeutic**: Tongji HCC cohorts (IHC, Cox regression, multiplex IHC), TCGA/CPTAC, melanoma anti-PD-1 RNA-seq (ref. 49), RCC scRNA-seq (ref. 26); CBX4 inhibitor UNC3866 mono and anti-PD-1 combination in syngeneic Hepa1-6/B16 and humanized-NSG HCC PDX; intratumoral ERV: RLTR4_Mm_int dsRNA therapy ± anti-PD-1.

## Connections

- [P-Bodies and mRNA Regulation](../topics/p-bodies-and-mrna-regulation.md) — topic hub; CBX4-driven retrotransposon silencing feeds the viral-mimicry / cytosolic-RNA-sensing axis adjacent to P-body post-transcriptional control.
- [P-bodies in cancer and leukaemia](../concepts/p-bodies-in-cancer-and-leukaemia.md) — like P-body sequestration of tumour-suppressor mRNAs, CBX4 epigenetic silencing is a tumour-intrinsic dependency that, when relieved, switches on antitumor programs; both are CRISPR-screen-identified cancer vulnerabilities.

## Open Questions

- **Do CBX4-derepressed ERVs contribute neoantigens?** Authors note ERV-encoded peptides can be MHC-I-presented and suggest "future studies should be warranted to explore whether the induced ERVs contribute to the gross antigen pools of CBX4-deficient tumor to induce antigen-specific T cell responses."
- **How does CBX4 select retroelement targets?** CBX4 lacks intrinsic methyltransferase activity; whether it directs EZH2/SETDB1 to specific ERVs (e.g., RLTR4-Mm-int) versus reading pre-existing marks is not fully resolved.
- **How general is the RLTR4-Mm-int axis in humans?** RLTR4-Mm-int is a murine element; the human ERV equivalents (ERVmap loci shown only by correlation) that mediate CBX4-dependent ICB response remain to be functionally validated.
- **What is CBX4's SUMO E3-ligase contribution here?** The paper invokes CBX4's chromodomain/PRC1 reader function but does not dissect whether its SUMO ligase activity contributes to retrotransposon silencing or TME remodeling.

## Sources

- Local PDF: `raw/inbox/papers/ma-2026-vivo-crispr-screens-identify-cbx-epigenetic.pdf`
- DOI: [10.1172/JCI200564](https://doi.org/10.1172/JCI200564)
