---
title: "PEXMap: A proteogenomic method for exon and isoform level mapping of mass spectrometry derived peptides"
authors:
  - "Deepanshi Awasthi"
  - "Paras Verma"
  - "Shashi Bhushan Pandit"
year: 2026
journal: "bioRxiv"
doi: "10.64898/2026.04.29.721330"
url: "https://www.biorxiv.org/content/10.64898/2026.04.29.721330v1"
pdf: "raw/inbox/papers/awasthi-2026-pexmap-proteogenomic-exon-isoform-mapping.pdf"
paper_kind: computational
cancer_types:
  - pan-cancer
modalities:
  - proteogenomics
  - mass-spectrometry
themes:
  - proteogenomics
  - alternative-splicing
  - isoform-resolution
  - peptide-mapping
  - exon-junction
topic: cancer-multiomics-literature
discovery_method: user-shared
tags:
  - source
  - cancer-multiomics
  - proteogenomics
  - alternative-splicing
  - tool
  - bioRxiv-2026
cm_axis: integration
---

# PEXMap: A proteogenomic method for exon and isoform level mapping of mass spectrometry derived peptides

_bioRxiv preprint, posted 2026-05-04._ DOI: [10.64898/2026.04.29.721330](https://doi.org/10.64898/2026.04.29.721330) · Group: Systems Biology · Code: [github.com/deepanshicbg/PEXMap](https://github.com/deepanshicbg/PEXMap) · License: CC BY-NC-ND 4.0

## Summary

Awasthi, Verma & Pandit (IISER Mohali) introduce **PEXMap** (PeptideEXonMapper), a k-mer based proteogenomic framework that maps MS/MS peptides to genes, transcripts, exons, or exon–exon junctions (EXj) by exact 8-mer lookups against an exon-resolved isoform database (ENACTdb). They build two hash-indexed reference DBs — **octamerDB** (overlapping 8-mers across 114,541 human isoforms / 19,730 protein-coding genes) and **exonjunctionDB** (1,363,811 EXj-specific 8-mers, 53,827 multi-gene). On PeptideAtlas Full Build 2022-01 (1,739,961 filtered peptides), PEXMap achieves 99.4% gene-level concordance, ~93% transcript-level accuracy for 1-to-1 peptide–isoform pairs, and assigns 81.8% of peptides to a single exon — a level of resolution not currently available in public proteomic repositories. Applied to liver/pancreas proteomes, it identified 1,076 genes with differential transcript usage (273 unique-isoform genes in liver, 58 in pancreas), with EXj-supported cases like MYL6 (exon-6 inclusion in liver, skipped in pancreas), SEPTIN9, TOR1B, and STK39. On a 1.15M-peptide pooled cancer proteome, PEXMap recovered 14,296 genes (97%) and 7,489 transcripts (89%); EXj evidence supported known cancer isoforms — EGFR truncated NP_958441.1 (peptides only up to EXj 17–19, no downstream kinase domain) and FLNA exon-30 skipped NP_001447.2 (EXj 29–31 present, exon-30 absent). The tool runs in ~4 min (DB build) + ~2 min (search of ~10⁷ 8-mers) on Linux.

## Key Points

- **Method**: pure exact-match k-mer (k=8) lookup in a precomputed hash table; no probabilistic scoring. Each isoform is fragmented into overlapping 8-mers; each 8-mer is linked to gene → transcript → exon (via EUID) → optional EXj. MS/MS peptides ≥8 aa with non-zero Shannon entropy and a single gene assignment are queried.
- **Reference database scale**: ENACTdb v0.5 → 19,730 genes / 114,541 transcripts / 1,363,811 unique EXj 8-mers. Multi-level annotation by **maximum-matched 8-mer** criterion; multi-mapping resolved by reporting all tied entities.
- **Benchmark vs PeptideAtlas** (1,739,961 input peptides, octamerDB):
  - Gene level: 99.4% accurate.
  - Transcript level (all peptides): 84.1%; restricted to 572,037 peptide-to-isoform 1-to-1 mappings → ~93%.
  - Exon level: 81.8% peptides assigned to a single exon — capability absent from PeptideAtlas itself.
  - exonjunctionDB recovered 95% gene concordance over ~78% of genes; 79% of mapped EXj peptides matched PeptideAtlas transcripts.
- **Tissue specificity (liver vs pancreas)**: 5,774 shared-expressed genes → 1,076 with differential transcript usage. Liver: 273 genes / 1,129 unique isoforms / 1,175 peptides; pancreas: 58 genes / 181 isoforms / 80 peptides. EXj-anchored examples: MYL6 (NP_066299.2 liver / NP_524147.2 pancreas), SEPTIN9 (NP_001106963.1 / NP_001106965.1), TOR1B alt-5′ splice site, STK39 exon-16 skipping pattern.
- **Cancer proteome (1,152,437 pooled peptides → 14,549 genes / 8,417 transcripts)**: 97% gene concordance, 89% transcript concordance, 81% exon-linked. Case studies: **EGFR** truncated isoform NP_958441.1 supported by EXj 17–19 with no downstream peptides — consistent with kinase-domain-altering exon-19 events (Lynch 2004, Paez 2004); **FLNA** exon-30 skipping isoform NP_001447.2 supported by EXj 29–31 with no exon-30 peptides.
- **Compute footprint**: ~4 min to build the 8-mer DBs (one-off per genome), ~2 min to search ~10⁷ MS/MS-derived 8-mers. Python dictionary-based; Linux only.
- **Limitations called out by authors**:
  - Exact 8-mer match — no mismatch tolerance, so peptides bearing PTMs or sequencing/identification ambiguities can drop out.
  - Constitutive-exon sequences yield identical 8-mers across isoforms → unresolved multi-mapping for many isoform calls; only EXj peptides give clean discrimination, and those are scarce (~27% of transcript-level mappings).
  - Performance depends on the completeness of the reference isoform annotation (ENACTdb) and the depth of MS/MS sampling.
  - True splice-junction novelty (non-annotated EXj, e.g., neojunctions) is **not** discovered — PEXMap only validates annotated isoforms with peptide evidence.
- **Data & code**: source at [github.com/deepanshicbg/PEXMap](https://github.com/deepanshicbg/PEXMap). PeptideAtlas Full Build 2022-01 + tissue and cancer pooled builds. ENACTdb at iscbglab.in/enactdb. No new proteomic data generated.

## Methods

- **References**: ENACTdb v0.5 (NCBI RefSeq GRCh38) provides exon-resolved isoforms; each exon carries a unique EUID (ordinal position, occurrence, coding status, splice-variant features). Two hash-indexed 8-mer DBs are built: octamerDB (all overlapping 8-mers per isoform; multi-mapped where shared) and exonjunctionDB (8-mers that strictly span two adjacent exons in an isoform).
- **Peptide preprocessing**: drop identical sequences, length <8, homopolymer (Shannon entropy = 0), and peptides annotated to multiple genes. Human proteome reduced 2,883,406 → 1,739,961; liver 184,342; pancreas 75,517; cancer pool 1,152,437.
- **Annotation**: exact-match lookup of MS/MS-derived 8-mers in octamerDB and exonjunctionDB. Two-stage: gene assignment first (max-matched 8-mer), then transcript / exon / EXj assignment within the gene. Ties produce explicit multi-mappings.
- **Benchmarking**: PeptideAtlas gene/transcript identifiers cross-referenced to RefSeq (15,771 / 15,855 genes; 97,443 / 112,312 transcripts mapped). Concordance defined as identical entity assignment for uniquely mapped reference peptides. Exon-level performance evaluated indirectly via peptides unambiguously assigned to a single exon after gene-level concordance.
- **Cancer application**: peptides from cancer tissue/cell-line builds in PeptideAtlas, filtered the same way. Functional examples (EGFR, FLNA, CASP2 in supplementary) chosen for prior literature links between AS and oncogenic function.

## Cancer Multiomics Project Relevance

- **Splice-aware peptide annotation as a post-processing module**: the project's proteogenomic workflow currently maps MS/MS peptides to genes/proteins via UniProt/Ensembl, which collapses isoform structure. PEXMap is a drop-in module to re-annotate the same peptide-spectrum matches at exon/EXj resolution — a near-zero-marginal-cost addition (~6 min one-off) that preserves PSM-level evidence and can be applied retrospectively to existing CPTAC/MS pipelines.
- **Splice-junction neoantigen hypothesis space**: EXj peptides directly evidence specific splice variants. Combining PEXMap EXj-resolved isoform calls with the project's [neoantigen pipeline](./wen-2020-neoflow-neoantigen-prioritization.md) and [NeoDisc proteogenomic flow](./huber-2025-neodisc-neoantigen-pipeline.md) opens splice-junction neoantigen candidates that gene-level proteomics misses. The trade-off is low EXj peptide yield (~27%), so this only works as a hypothesis-generation layer, not a primary screen.
- **Driver-isoform-level functional state**: the EGFR truncated-isoform example (NP_958441.1 with no peptides past EXj 17–19) is exactly the kind of "protein-level confirmation of WGS-implicated driver event" the project chases. Adding PEXMap on top of CPTAC pan-cancer phosphoproteomes (cf. [Li 2023](../analyses/cancer-multiomics-literature/li-2023-pan-cancer-driver-functional-states.md), [Petralia 2024](../analyses/cancer-multiomics-literature/petralia-2024-pan-cancer-tumor-immunity.md)) could reveal where driver mutations match splice-level proteome states and where they diverge.
- **Tissue / cell-state reference**: liver/pancreas tissue-specific isoform calls (e.g., MYL6 exon-6, SEPTIN9) provide a non-cancer baseline that the project's lung-cancer cohort can be benchmarked against — useful when separating "tumor-acquired isoform shift" from "normal tissue isoform program."
- **What it does NOT solve**: novel splice junctions (e.g., tumor-specific neojunctions from intron retention) are out of scope, because PEXMap only validates annotated isoforms. For neojunction-derived neoantigens, the project still needs a transcript-assembly step (e.g., StringTie + custom DB) upstream of PEXMap.

## Connections

- [Jiang 2025 – Dark Cancer Phosphoproteome](./jiang-2025-deciphering-dark-cancer-phosphoproteome-using.md) — both papers attack annotation gaps in proteogenomics (phosphosite → kinase vs peptide → isoform).
- [Wen 2020 – NeoFlow Proteogenomic Neoantigen Prioritization](../analyses/cancer-multiomics-literature/wen-2020-neoflow-neoantigen-prioritization.md) — natural upstream pipeline; PEXMap adds isoform-resolution post-annotation.
- [Huber 2025 – NeoDisc Proteogenomic Neoantigen Pipeline](../analyses/cancer-multiomics-literature/huber-2025-neodisc-neoantigen-pipeline.md) — clinical-grade neoantigen pipeline that could ingest PEXMap EXj evidence for splice-junction antigen hypotheses.
- [Chong 2022 – Identification of Tumor Antigens with Immunopeptidomics](../analyses/cancer-multiomics-literature/chong-2022-identification-tumor-antigens-immunopeptidomics.md) — review on noncanonical antigen FDR control; relevant for any splice-junction antigen pipeline that would use PEXMap.
- [Cancer Multiomics Proteogenomic Atlas](../topics/cancer-multiomics-literature.md) — topic hub (Section 1, Proteogenomics 통합 기반).

## Sources

- Raw PDF: `raw/inbox/papers/awasthi-2026-pexmap-proteogenomic-exon-isoform-mapping.pdf` (1.7 MB, 23 pages)
- Code: https://github.com/deepanshicbg/PEXMap
- Reference DB: ENACTdb v0.5 (https://www.iscbglab.in/enactdb)
- Test data: PeptideAtlas Full Build 2022-01 (https://peptideatlas.org/builds/human/)
- Funding: Department of Biotechnology, Govt. of India (BT/PR40419/BTIS/137/36/2022, BT/PR40198/BTIS/137/56/2023); PMRF for D. Awasthi.
