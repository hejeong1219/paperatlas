---
title: "Dual function of DOT1L suppresses tumor cell-intrinsic immunogenicity in hepatocellular carcinoma"
authors:
  - "Xu S"
  - "Gong R"
  - "Liu S"
  - "Wang J"
  - "Shen Y"
  - "Peng C"
  - "Feng Q"
  - "Luo M"
  - "Lan F"
  - "Fan J"
  - "Cai J"
  - "Lan X"
year: 2026
journal: "Oncogene"
doi: "10.1038/s41388-026-03744-6"
pdf: "raw/inbox/papers/xu-2026-dual-function-dot-suppresses-tumor-cell.pdf"
paper_kind: mechanistic
cancer_types:
  - hepatocellular-carcinoma
modalities:
  - crispr-screen
  - functional-genomics
  - chip-seq
  - atac-seq
themes:
  - dot1l
  - viral-mimicry
  - transposable-element
  - immunogenicity
  - innate-immunity
  - type-i-interferon
  - immune-checkpoint
  - epigenetic-therapy
tags:
  - source
  - line1
  - retrotransposon
  - hcc
  - cancer
  - immunotherapy
pdf_status: full-text-read
---
# Dual function of DOT1L suppresses tumor cell-intrinsic immunogenicity in hepatocellular carcinoma

_Oncogene, 2026._

## Summary

A FACS-based CRISPR/Cas9 screen using the immune-checkpoint molecules CD47 and PD-L1 as reporters in hepatocellular carcinoma (HCC) cells identified **DOT1L** — the sole histone H3K79 methyltransferase — as a repressor of tumor cell-intrinsic immunity. DOT1L suppresses antitumor immunity through a **dual mechanism**: (1) it restrains the expression of transposable elements (TEs, predominantly LINEs and LTRs), preventing accumulation of immunogenic double-stranded RNA (dsRNA) that would otherwise trigger an **MDA5/RIG-I → type I interferon (IFN)** response; and (2) it activates **ZEB1**, a negative regulator that further represses immune-related genes (PD-L1, JAK2, STAT1, IRF1, IFIH1). Both arms require DOT1L's catalytic activity: the clinical-stage inhibitor **EPZ-5676** phenocopies genetic depletion, elevating CD47/PD-L1, ISGs, MHC I, and dsRNA, while a catalytically inactive DOT1L mutant fails to rescue. Mechanistically, DOT1L directly binds a fraction of LINEs/LTRs (12.3%) in cooperation with **NPM1** to repress them, and indirectly represses the remainder by sustaining MEN1 chromatin binding that limits H3K4me3 redistribution; the TE-repressive arm is conserved between human and mouse, but the DOT1L–ZEB1 axis is human-specific. In vivo, Dot1l loss or EPZ-5676 alone barely affected tumor growth but **sensitized murine HCC tumors to anti-PD-L1 ICB**, increasing CD4+/CD8+ T-cell infiltration; in humanized mice and patient-derived organoids, **EPZ-5676 alone** enhanced antitumor immunity. Across TCGA cancers, DOT1L expression inversely correlates with IFN signatures and high DOT1L predicts worse survival, nominating DOT1L inhibition as a strategy to overcome immunotherapy resistance.

## Key Points

- **CRISPR screen of ~219 epigenetic factors identified DOT1L as a CD47/PD-L1 repressor.** A sgRNA library (~6 sgRNAs per chromatin-regulatory domain) was screened in HuH-7-Cas9 HCC cells sorting CD47/PD-L1-high vs -low populations; **all twelve DOT1L sgRNAs were significantly enriched** in CD47- and PD-L1-high cells with or without IFNγ, alongside positive controls KDM1A and EZH2.
- **DOT1L depletion induces a type I IFN / ISG program.** RNA-seq of DOT1L-depleted HuH-7 cells showed far more up- than down-regulated genes (DOT1L acts as a transcriptional repressor); GO/GSEA top hits were IFN and antiviral response. Validated ISGs included antiviral **OAS1/OAS3**, pro-inflammatory **CXCL10/CXCL11**, and antigen-presentation **HLA-A/B/C**; MHC I surface expression rose at baseline and hyper-induced with IFNγ.
- **DOT1L derepresses transposable elements, mostly LINEs and LTRs.** Total RNA-seq found **440 TEs up-regulated and only 6 down-regulated** upon DOT1L KO, mainly LINEs, LTR, SINEs, and DNA transposons; ATAC-seq showed increased chromatin accessibility on TEs (with gained H3K4me3/H3K27ac) while global accessibility was minimally affected (~38% of TEs in more-accessible vs ~22% in less-accessible sites).
- **Derepressed TEs generate dsRNA sensed by MDA5/RIG-I.** DOT1L depletion caused dsRNA accumulation (J2 antibody flow cytometry); abrogating dsRNA sensors **MDA5 or RIG-I significantly diminished ISG induction**, and knockdown of type I IFN receptor **IFNAR1 (but not IFNGR1)** restored ISG repression — establishing a dsRNA–type I IFN axis.
- **DOT1L cooperates with NPM1 to directly repress a subset of LINEs/LTRs.** fanChIP found 15,015 high-confidence DOT1L peaks (~40% at gene promoters, 12% at TEs); **12.3% of the up-regulated LINEs/LTRs were directly DOT1L-bound**. IP-MS identified and validated DOT1L–NPM1 interaction; ~66% of DOT1L peaks overlapped NPM1, and **~42.5% of DOT1L-bound/-inhibited LINEs and LTRs were also occupied by NPM1**.
- **TE repression is independent of local H3K79me2.** DOT1L-bound TE regions carried only background, DOT1L-insensitive H3K79me2 signals, arguing DOT1L represses these LINEs/LTRs not through local H3K79me2 deposition.
- **Indirect TE repression runs through MEN1 and H3K4me3 redistribution.** DOT1L loss reduced H3K79me2 and weakened MEN1 chromatin binding genome-wide; the ~88% of accessible LINEs/LTRs lacking DOT1L binding gained H3K4me3 upon DOT1L loss (re-distribution), while global H3K4me3 occupancy was minimally changed.
- **DOT1L's second arm: it directly activates ZEB1.** DOT1L fanChIP occupied the **ZEB1 promoter**; DOT1L KO reduced ZEB1 gene-body H3K79me2, promoter H3K4me3/H3K27ac, and accessibility, lowering ZEB1 mRNA/protein. WT (not catalytically inactive) DOT1L rescued ZEB1; DOT1L positively correlates with ZEB1 in liver (GTEx).
- **ZEB1 represses immune-related genes; high ZEB1 predicts worse HCC survival.** DOT1L loss weakened ZEB1 binding at **PD-L1, JAK2, STAT1, IRF1, and IFIH1**; ZEB1 depletion induced immune genes, and forced ZEB1 re-expression in DOT1L-deficient cells partially restored repression. ZEB1 did **not** affect CD47 or TE expression. LIHC patients with high tumor ZEB1 showed significantly reduced overall survival.
- **Both arms require DOT1L catalytic activity (EPZ-5676 phenocopy).** EPZ-5676 dose-dependently lowered global H3K79me2 without changing DOT1L protein, and elevated CD47/PD-L1 mRNA and surface protein, ISGs, MHC I, TE expression, and dsRNA; **366 genes were commonly up-regulated** in DOT1L-depleted and EPZ-5676-treated cells and were IFN-associated. WT-DOT1L (not catalytically inactive) rescued immune-gene repression.
- **DOT1L loss sensitizes murine HCC to anti-PD-L1 ICB.** In Hepa1-6 and Hep53.4 syngeneic C57BL/6 models, Dot1l KO or EPZ-5676 alone barely affected tumor growth, but **Dot1l loss markedly sensitized tumors to anti-PD-L1**, reducing tumor size and improving survival; combination EPZ-5676 + anti-PD-L1 increased intratumoral CD4+ and CD8+ T cells (Tregs, NK1.1, macrophages unchanged). Murine cells showed the TE/dsRNA arm but **not** the Dot1l–Zeb1 axis (species-specific).
- **EPZ-5676 alone enhances antitumor immunity in humanized models.** In HuH-7 CDX humanized (huHSC-NCG) mice, EPZ-5676 alone reduced tumor volume, prolonged survival, and increased intratumoral cytotoxic CD8+ T cells; effect was absent in immunodeficient NSG mice. T-cell cytotoxicity against patient-derived organoids (PDO) was stronger when PDOs were co-cultured with EPZ-5676 (LDH assay).
- **DOT1L inversely correlates with IFN signatures pan-cancer.** EPZ-5676/SGC0946 datasets in IGROV, MDA-MB-468, MCF7, and K562 cells showed IFN up-regulation; across TCGA, DOT1L is overexpressed in tumors, high DOT1L predicts shorter overall/disease-free survival, and DOT1L expression negatively correlates with IFN signatures pan-cancer. IHC on HCC TMAs showed DOT1L inversely correlated with PD-L1 and CD8; anti-PD-1 responders expressed lower DOT1L than non-responders.
- **Synergy with EZH2/KDM1A loss.** Co-depletion of DOT1L with EZH2 or KDM1A produced a stronger ISG (incl. CD47, PD-L1) induction than single KO, indicating DOT1L acts independently of EZH2/KDM1A, likely by targeting different TE families.

## Methods

- **FACS-based CRISPR/Cas9 screen** in HuH-7-Cas9 HCC cells with a domain-focused sgRNA library (~219 epigenetic factors, ~6 sgRNAs/domain) at MOI ~0.3, sorting top/bottom 15% CD47- and PD-L1-expressing cells ± IFNγ; MAGeCK analysis.
- **Genetic perturbation**: six independent DOT1L sgRNAs + non-targeting control in HuH-7 and HepG2; murine Dot1l KO in Hepa1-6, Hep53.4, and LLC cells; shRNA knockdown of MDA5, RIG-I, IFNAR1, IFNGR1, ZEB1.
- **DOT1L inhibitor** EPZ-5676 (7-day treatment in vitro; 20 mg/kg twice weekly in vivo); rescue with WT vs catalytically inactive (CI) HA-DOT1L.
- **Transcriptomics**: RNA-seq and total RNA-seq (rRNA-depleted) with TEtranscripts/Homer for repeat-element quantification; GO/KEGG/GSEA.
- **Epigenomics**: H3K4me3, H3K27ac, H3K79me2 ChIP-seq; DOT1L **fanChIP** (fractionation-assisted native ChIP); NPM1, MEN1, ZEB1 ChIP-seq; ATAC-seq; Cistrome-GO/Cistrome toolkit and HOMER motif analysis.
- **Protein interaction**: FLAG IP-MS (Nano-HPLC-MS/MS) and endogenous DOT1L IP-WB to identify/validate NPM1.
- **Functional/immune readouts**: dsRNA flow cytometry (J2 antibody), MHC I / CD47 / PD-L1 / HLA-A,B,C flow cytometry, RT-qPCR.
- **In vivo**: syngeneic C57BL/6 (Hepa1-6, Hep53.4) ± anti-PD-L1; HuH-7 CDX in humanized huHSC-NCG and immunodeficient NSG mice; tumor-infiltrating lymphocyte profiling; HCC patient-derived organoids + T-cell co-culture (LDH cytotoxicity); HCC tissue-microarray IHC (DOT1L, PD-L1, CD8).
- **Patient data**: TCGA expression/survival, cBioPortal mutation, GTEx, and two pre-anti-PD-1 RNA-seq responder/non-responder datasets.

## Connections

- [P-Bodies and mRNA Regulation](../topics/p-bodies-and-mrna-regulation.md) — topic hub; this paper extends the transposable-element/viral-mimicry and immune-ISG axes that intersect P-body biology.
- [P-bodies in cancer and leukaemia](../concepts/p-bodies-in-cancer-and-leukaemia.md) — DOT1L is itself a P-body-dissolution agent (the DOT1L inhibitor EPZ-5676 dissolves P-bodies in Kodali 2024); here DOT1L's chromatin function silences retroelements to suppress tumor immunogenicity, a complementary cancer-dependency / immune-evasion axis.
- [Kodali 2024 — RNA sequestration in P-bodies sustains myeloid leukaemia](../sources/kodali-2024-rna-sequestration-pbodies-sustains-myeloid-leukaemia.md) — independently reports that the DOT1L inhibitor EPZ-5676 dissolves AML P-bodies; this paper details DOT1L's transcriptional/epigenetic program over transposable elements and the type I IFN response.

## Open Questions

- **What other factors mediate DOT1L-inhibited TEs?** Only ~12.3% of derepressed LINEs/LTRs are directly DOT1L/NPM1-bound; the indirect MEN1–H3K4me3 redistribution and possible non-histone DOT1L substrates remain incompletely defined.
- **Is repression truly H3K79me2-independent at TEs?** TE regions carry only inert background H3K79me2, yet catalytic activity is required; whether non-histone methylation (e.g., as reported for androgen receptor, RAP80) underlies TE repression is untested here.
- **How translatable is the human-specific DOT1L–ZEB1 axis?** Mice lack Dot1l–Zeb1 regulation, so murine models may underestimate single-agent EPZ-5676 efficacy; humanized-mouse/PDO data are encouraging but limited.
- **Which TE families drive the IFN response, and do they overlap with EZH2/KDM1A targets?** The synergy with EZH2/KDM1A loss implies distinct TE subsets, but the precise immunogenic-TE catalog is unresolved.

## Sources

- Local PDF: `raw/inbox/papers/xu-2026-dual-function-dot-suppresses-tumor-cell.pdf`
- DOI: [10.1038/s41388-026-03744-6](https://doi.org/10.1038/s41388-026-03744-6)
