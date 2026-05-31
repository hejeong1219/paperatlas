---
title: "3DisoGalaxy: a structure-grounded breast cancer atlas of alternative-splicing-derived proteoforms"
authors:
  - "Felicia T. Jiang"
  - "Yujie Sun"
  - "Tianqi Lan"
  - "Yiyuan Zhang"
  - "Mengyao Li"
  - "Hongjun Chen"
  - "Hao Yuan"
  - "Jun Tan"
  - "Xin Wang"
year: 2026
journal: "bioRxiv"
doi: "10.64898/2026.04.30.722115"
url: "https://www.biorxiv.org/content/10.64898/2026.04.30.722115v1"
pdf: "raw/inbox/papers/jiang-2026-3disogalaxy-breast-cancer-isoform-foldome.pdf"
paper_kind: computational
cancer_types:
  - breast-cancer
modalities:
  - long-read-rna-seq
  - ribosome-profiling
  - protein-structure
  - alphafold
themes:
  - proteogenomics
  - alternative-splicing
  - isoform-resolution
  - proteoform-biology
  - translatome
  - foldome
  - structural-similarity-network
  - intrinsic-disorder
  - subtype-association
topic: cancer-multiomics-literature
discovery_method: user-shared
tags:
  - source
  - cancer-multiomics
  - proteogenomics
  - alternative-splicing
  - breast-cancer
  - tool
  - atlas
  - bioRxiv-2026
cm_axis: integration
---

# 3DisoGalaxy: a structure-grounded breast cancer atlas of alternative-splicing-derived proteoforms

_bioRxiv preprint, posted 2026-04-30._ DOI: [10.64898/2026.04.30.722115](https://doi.org/10.64898/2026.04.30.722115) · Corresponding: Jun Tan (Zunyi Medical), Xin Wang (CUHK) · Portal: [3disogalaxy.com](http://3disogalaxy.com/) · Code: [github.com/FeliciaTJiang/3DisoGalaxy](https://github.com/FeliciaTJiang/3DisoGalaxy) · Data: Zenodo [10.5281/zenodo.14865747](https://doi.org/10.5281/zenodo.14865747) · License: CC BY 4.0

## Summary

Jiang et al (CUHK + Tencent AI Lab + Peking U + Zunyi Medical) introduce **3DisoGalaxy**, an isoform-resolved breast cancer atlas that fuses three orthogonal layers into a single structure-organized resource: a long-read transcriptome (PacBio Iso-Seq, n=35 tumor+NAT), an isoform-level translatome (Ribo-seq, n=42 across Normal/ER+/TNBC), and an AlphaFold2-derived foldome (53,066 predicted structures; 46,601 pLDDT≥70 high-confidence subset). After hybrid transcriptomic assembly with multi-cohort short-read validation, the team curates **123,395 transcript variants → 90,929 high-confidence variants → 73,715 translation-supported ORFs**. They organize the 46,601-structure subset into a TM-score≥0.9 structural similarity network, annotate domain architecture (Pfam-A 35.0 via HMMER), intrinsic disorder (IUPred3), subcellular localization (DeepLoc 2.0), and short linear motifs (FoldDisco structure-based search). Two mechanistic vignettes illustrate the platform: **KRAS4A** (non-canonical, exon-4A) shows selective depletion of C-terminal NLS / bipartite-NLS / ER-retrieval motif instances relative to canonical KRAS4B while preserving the Ras effector core (residues 32–40); **ΔPH AKT1** (PH-domain-deleted, kinase + hydrophobic motif preserved) shows the largest TNBC vs non-TNBC log2FC in the AKT1 family (0.82, BH-adjusted P<0.001) and stratifies relapse-free survival in the Fudan cohort (log-rank P=0.046). The interactive portal at 3disogalaxy.com exposes the structural similarity network (Cosmograph v1.3) with linked Mol* 3D viewers (v3.35) for gene-centric and global-discovery workflows. The authors frame the platform as a hypothesis-generating scaffold for "computational proteoform biology" rather than as functional validation.

## Key Points

- **Three-layer integration**: PacBio Iso-Seq (n=35, 24 tumor + 11 NAT, spanning Basal/HER2/LumA/LumB/Normal-like) + 4 cohorts of short-read RNA-seq (n=339 incl. Fudan TNBC PRJNA486023, Fusion, Her2, Circadian PRJNA975550, Microbial PRJNA839244) + 2 Ribo-seq cohorts (PRJNA898352 n=24 incl. Normal/ER+/TNBC matched-mRNA; PRJNA523167 n=18). Reference: GENCODE v41 + UniProtKB/Swiss-Prot (52,582 entries, 2025-08-08).
- **Transcript landscape**: SQANTI3 classifies 90,929 high-confidence variants into FSM (~26.6%, canonical), ISM (~10.5%), NIC (~29.4%), NNC (~33.5%); non-canonical (NNC+NIC) dominate at ~63%. Splice-event quantification via SUPPA2 across SE/MX/A5SS/A3SS/RI/AF/AL classes. Top isoform-rich genes accumulate >100 variants per gene with strong non-canonical bias. Pathway enrichments primarily driven by RI and SE events including tumor-immunity-related programs.
- **Translatome**: RiboCode (v1.2.13) calls ORFs at transcript-level; 58,292 / 90,929 transcripts (64%) have Ribo-seq translation evidence, of which 71.9% are non-canonical (NNC/NIC/ISM). One representative ORF per translated transcript becomes the standardized protein input for foldome construction. TNBC samples sit in the upper RPF-distribution tail for annotated, 3′ dORF, and 5′ uORF classes (Kruskal–Wallis P<2.2×10⁻¹⁶ for each).
- **Foldome QC**: AlphaFold2 predictions → 53,066 structures → 46,601 high-confidence subset (pLDDT≥70). Length-stratified disorder–pLDDT coupling recapitulates canonical extracellular (long, ~1,500aa disorder peak), nuclear (<500aa peak), and mitochondrial (short N-terminal targeting) patterns. NLS↔NES correlation r=0.40 (regulated nucleo-cytoplasmic trafficking); SP↔TMD r=0.64 (secretory targeting + membrane topogenesis).
- **Domain remodeling at isoform level**: 38,903 / 46,411 isoforms (83.8%) from multi-isoform genes. Pfam ΔN distribution centers at zero but >60% of isoforms show non-zero Pfam shift; remodeling is **biased toward loss** rather than gain — consistent with splicing being unlikely to wholesale rewrite folded cores. In top-15 isoform-rich membrane-protein families, ~15% of ERBB2 isoforms show altered Pfam but 37.3% (19/51) show altered predicted localization; PLXNB2 reaches ~70% altered localization.
- **Motif remodeling**: FoldDisco structure-based motif search (RMSD ≤1.5Å, coverage ≥0.80, idf ≥0.40 for Tier A; IDR ≥50% disorder filter; AUPR 0.903 stable across IDR thresholds). 6,774 genes assessed: **58.9% gain-dominant, 15.4% loss-dominant, 25.8% balanced** (Wilcoxon signed-rank P<0.001). Median Jaccard distance between reference and non-reference motif sets = 0.50. **IntOGen cancer drivers show significantly higher motif shift scores** than non-drivers (Mann–Whitney U, P<0.001), linking isoform-level motif remodeling to cancer driver status.
- **KRAS4A vs KRAS4B vignette**: KRAS4B (canonical) has preserved C-terminal NLS (residues 167–170), bipartite NLS (182–185), ER-retrieval motif (169–172). KRAS4A loses these matches but retains the Ras effector core (32–40) and SUMO (7–9), TXY (2–4) motifs. Structural alignment shows KRAS4B-specific motif clusters along the C-terminal regulatory region absent in KRAS4A — providing a structure-resolved hypothesis for the known KRAS4A/4B subcellular localization divergence (Zhang 2018; Whitley 2024; Rossi 2025 — BIRC6 as KRAS4A-specific ubiquitin ligase).
- **ΔPH AKT1 vignette**: Non-canonical AKT1 isoform missing N-terminal residues 1–62 (PH domain) while retaining kinase + hydrophobic motif. Family-leading TNBC log2FC = 0.82 (BH P<0.001; canonical AKT1 log2FC = 0.19, BH P=0.97). Elevated Ribo-seq mean ORF RPF RPKM in TNBC vs non-TNBC. RFS in Fudan cohort: log-rank P=0.046 (median-split dichotomization). GO-BP shifts toward growth/microenvironment programs and away from differentiation (GO:0030154), consistent with PH-loss disrupting PIP3-dependent membrane recruitment.
- **Structural similarity network**: 46,601 nodes; Foldseek easy-search (TM-align type-1; --tmalign-fast 1) all-versus-all; edges at TM-score ≥0.9. Pfam-set Jaccard similarity remains high across neighborhood sizes, validating structure-defined clusters as domain-coherent. Largest Pfam families: PF13853 olfactory receptor (1.84%), PF07686 Ig V-set (1.39%), PF00001 rhodopsin 7TM (1.31%), PF00069 protein kinase (1.11%), PF00071 Ras (1.00%), PF00400 WD repeat (0.69%). Non-canonical isoforms (19,957) form the largest node category, with annotated anchors broadly embedded across all cluster sizes for annotation propagation.
- **Computational stack**: SQANTI3, TALON v5.0, minimap2, IsoSeq v3, RiboCode v1.2.13, RSEM, limma-voom (Ritchie 2015), TransDecoder v5.7.1, AlphaFold2, HMMER v3.4 + Pfam-A v35.0, IUPred3, DeepLoc 2.0, FoldDisco (Kim 2025), Foldseek, Gephi v0.10.1 (ForceAtlas2), PyMOL v3.1.6, Cosmograph v1.3, Mol* v3.35.
- **Authors' framing & caveats**: Translation evidence ≠ stable protein abundance; AlphaFold predictions weak for disordered / context-dependent / membrane-assembly states; motif calls are consensus-matching predictions, not validated regulatory sites; survival association presented as exploratory. Platform is explicitly positioned as hypothesis-generating, not validation.

## Methods

- **Hybrid transcriptomics**: PacBio Iso-Seq (Sequel IIe, SMRT Link v11; FLNC reads, QV≥20, ≥2 sub-reads at ≥99% accuracy; pbmm2 vs hg38; IsoSeq v3 collapse) merged with ONT long-reads (TranscriptClean-corrected). TALON v5.0 cross-sample integration with coverage/identity ≥0.95 and presence in ≥2 samples. SQANTI3 with GENCODE v41 + CAGE peaks + polyA motif lists for FSM/ISM/NIC/NNC classification and rule-based filtering (filtering.json from Brain Iso-Seq pipeline). Final 90,928 high-confidence isoforms after indel-correction, ≥3 Iso-Seq sample support, novel-junction STAR support ≥5, and 3′-end / polyA filtering.
- **AS event quantification**: SUPPA2 over SE/MX/A5SS/A3SS/RI/AF/AL classes for global and Basal-specific subset analyses with pathway enrichment.
- **Ribosome profiling & ORF calling**: Standard RNase I → ribosome footprint isolation; metagene QC for 3-nt periodicity and 29–30nt RPF length distribution; RiboCode v1.2.13 with frame periodicity + P-site enrichment; one representative ORF per transcript (longest support-weighted). Annotated/uORF/dORF/overlap/not-annotated ORF type labels follow RiboCode classification.
- **Foldome construction**: TransDecoder v5.7.1 → AlphaFold2 → pLDDT ≥70 filter; AFDB human proteome reference (UP000005640 v4, 23,391 structures, 4,877 MB); long-protein sliding window (1,400 aa fragments, 200 aa step) for fragment-coordinate remapping.
- **Annotation layers**: HMMER (hmmscan v3.4) + Pfam-A v35.0 trusted cutoffs; DeepLoc 2.0 for subcellular localization; IUPred3 for IDR length/fraction.
- **Motif benchmarking**: FoldDisco (Kim 2025) batched on SLURM (112-way parallel); RMSD≤3.0Å search; Tier A (RMSD≤1.5Å, coverage≥0.80, gap≤0.05, idf≥0.40), Tier B supportive. Gold standard from UniProtKB FT/CC fields restricted to 3DisoGalaxy graph nodes; ±2aa site-match tolerance; Precision–Recall AUPR with bootstrap (200×, 70% target subsampling); decoy-based FDR with rule-of-three upper bound. Operating point: Tier A + IDR≥50% for general motifs; Tier A no IDR filter for ZnF.
- **Motif shift score**: gain + loss + λ × (1 − Jaccard); λ=1.0. IntOGen-driver vs non-driver comparison by two-sided Mann–Whitney U.
- **Structural similarity network**: Foldseek easy-search with TM-align type-1 (--tmalign-fast 1); all-vs-all; edge cutoff TM-score ≥0.9; Gephi ForceAtlas2 layout (32 threads, gravity=0.1, scaling=10.0, dissuade-hubs, prevent-overlap).
- **AKT1 multi-omics validation**: Isoform-level RSEM quantification on Fudan TNBC cohort (PRJNA486023, n=90); STAR alignment; limma-voom differential expression; Kaplan–Meier RFS with two-sided log-rank, median-split dichotomization of ΔPH AKT1 signal; GO-BP predictions from 3DisoDeepPF (Jiang et al, 2026, companion model).
- **Portal stack**: Cosmograph v1.3 (network visualization); Mol* v3.35 (3D viewer); Foldseek for structure-based queries from user uploads; node color = subtype/tissue context, size = log2FC magnitude.

## Cancer Multiomics Project Relevance

- **Direct isoform-level proteoform layer for proteogenomic workflow**: 3DisoGalaxy converts long-read RNA + Ribo-seq into a translation-supported, structure-resolved protein database that can serve as a **drop-in reference for cancer proteogenomic database searches**. For the project's CPTAC-style lung-cancer proteogenomics, building an analogous lung-specific 3DisoGalaxy (Iso-Seq + Ribo-seq + AlphaFold2) would yield isoform-resolved MS/MS peptide assignments at the level of translation-supported ORFs rather than UniProt canonical entries. Pairs naturally with [PEXMap](./awasthi-2026-pexmap-proteogenomic-exon-isoform-mapping.md) as the peptide → exon/EXj annotation engine.
- **AKT1 / KRAS isoform analyses transfer directly to lung cancer**: KRAS4A vs KRAS4B is a top-tier finding for lung adenocarcinoma where KRAS-G12C / G12V drive a major subset; isoform-specific motif loss (NLS / ER-retrieval) provides a structural-mechanism hypothesis layer beyond mutation status. AKT1 alternative-PH isoforms are similarly relevant for AKT1-amplified or AKT1-E17K lung adenocarcinoma cases. Both vignettes show how a structure-grounded atlas can nominate proteoforms that classical mutation-centric driver analysis misses.
- **Subtype-association methodology is reusable for LUAD/LUSC**: The "structural neighborhood → subtype-biased log2FC + RFS stratification → exploratory hypothesis" workflow (ΔPH AKT1 in TNBC) is a template for nominating LUAD-biased proteoforms from any future lung-cancer 3DisoGalaxy build. Methodology section explicitly lays out the structure-similarity-network → motif/Pfam/IDR remodeling → subtype-coordinated signal → outcome-association pipeline.
- **Computational proteoform biology framework**: The "represent, organize, hypothesize" framing (Discussion §1–2) is a clean abstraction for the project — define ORFs, build foldome, organize into structural similarity network, annotate with multi-layer features, prioritize via subtype + outcome signals. Translatable to other cancers and not breast-cancer-specific.
- **Connects to companion 3DisoDeepPF model**: GO-BP predictions in Fig. 6G are from Jiang 2026 _3DisoDeepPF_, an isoform-aware function predictor cited as an in-prep companion. Worth tracking for a follow-up paper that could provide isoform-level GO predictions reusable across other cancer projects.
- **Caveats specific to project re-use**: (a) Iso-Seq + Ribo-seq matched samples are required — typical CPTAC cohorts lack Ribo-seq, so this is a future-data-collection guidance rather than a current-data-reanalysis play. (b) AlphaFold2 isoform structures don't resolve context-dependent conformations or large complexes — KRAS / AKT1 vignettes work because both are single-domain folds with localized regulatory regions. (c) Motif calls are SLiM consensus predictions, not experimental binding sites — the "lost NLS in KRAS4A" claim is hypothesis-strength, matching CPTAC-style "altered PTM site" hypothesis-strength. (d) RFS log-rank P=0.046 is exploratory; for biomarker use, project needs replication in larger independent cohorts with covariate adjustment.

## Connections

- [Awasthi 2026 – PEXMap proteogenomic exon/isoform mapping](./awasthi-2026-pexmap-proteogenomic-exon-isoform-mapping.md) — complementary tool: PEXMap maps MS/MS peptides to exon/EXj on annotated isoforms; 3DisoGalaxy supplies the translation-supported isoform reference + structural context to interpret which mappings matter.
- [Jiang 2025 – Dark Cancer Phosphoproteome](./jiang-2025-deciphering-dark-cancer-phosphoproteome-using.md) — both papers (different Jiang) build hypothesis-generating annotation layers on top of cancer proteomics, with explicit framing of evidence constraints.
- [Cancer Multiomics Proteogenomic Atlas](../topics/cancer-multiomics-literature.md) — topic hub (Section 1, Proteogenomics 통합 기반).

## Sources

- Raw PDF: `raw/inbox/papers/jiang-2026-3disogalaxy-breast-cancer-isoform-foldome.pdf` (8.5 MB, 49 pages)
- Code: https://github.com/FeliciaTJiang/3DisoGalaxy
- Portal: http://3disogalaxy.com/
- Curated data: https://doi.org/10.5281/zenodo.14865747
- Major datasets: PacBio Iso-Seq (in-house n=35), PRJNA975550 (Circadian RNA-seq), PRJNA839244 (Microbial RNA-seq), PRJNA486023 (Fudan TNBC), PRJNA898352 (Ribo-seq A132), PRJNA523167 (Ribo-seq A133), UniProtKB/Swiss-Prot (2025-08-08 snapshot), AFDB UP000005640 v4
- Companion: 3DisoDeepPF (Jiang et al, 2026; isoform-resolved GO-BP prediction)
