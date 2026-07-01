---
title: "Identification of novel regulators of LINE-1 expression via CRISPR/Cas9 screening"
authors:
  - "Oksuz O"
  - "Chu C"
  - "Arisdakessian C"
  - "Diao L"
  - "Zaller D"
  - "Long KK"
  - "Keilhack H"
  - "Knutson S"
year: 2025
journal: "Mobile DNA"
doi: "10.1186/s13100-025-00386-5"
pdf: "raw/inbox/papers/oksuz-2025-identification-regulators-line-expression-crispr-cas.pdf"
paper_kind: mechanistic
modalities:
  - crispr-screen
  - functional-genomics
themes:
  - line-1
  - retrotransposon
  - gene-regulation
  - orf1p
  - orf2p
  - stress-granules
  - dna-repair
  - synthetic-lethality
tags:
  - source
  - line-1
  - retrotransposon
  - crispr-screen
pdf_status: full-text-read
---
# Identification of novel regulators of LINE-1 expression via CRISPR/Cas9 screening

_Mobile DNA, 2025._

## Summary

Oksuz et al. built a genome-wide loss-of-function CRISPR/Cas9 platform to find upstream regulators of the human LINE-1 (L1) retrotransposon, separating regulation of its two encoded proteins (ORF1p and ORF2p) at both the RNA and protein level. The core innovation is a **dual-reporter construct** based on the full-length native L1RP element: ORF1p is tagged with C-terminal GFP and ORF2p with C-terminal mCherry, with the native 5′/3′ UTRs preserved and a pGK-driven Hygromycin-BFP cassette as an internal normalization control. Two reporter versions were made — wild-type ORF2p and a catalytically inactive endonuclease/reverse-transcriptase (EN/RT) mutant — and integrated into HCT-116 colorectal cancer cells expressing Cas9 (chosen partly for its active p53 pathway). A genome-wide screen (~80,000 sgRNAs, ~20,000 genes, 4 sgRNAs/gene) sorted cells by ORF1p-GFP decreased, ORF1p-GFP increased, or ORF2p-mCherry increased, with hits then validated in a focused secondary screen (15,000 sgRNAs, 1,490 genes, 10 sgRNAs/gene). The screen recovered all four core HUSH-complex members (Periphilin/PPHLN1, MORC2, MPP8, TASOR) as ORF1p negative regulators, validating the system, and surfaced novel candidates enriched for stress-granule RNA-metabolism and DNA-repair factors among ORF1p negative regulators. A parallel **lethality screen** (WT vs EN/RT-mutant reporter, depleted guides at day 18) identified genes whose loss causes ORF2p-activity-dependent cell death. A striking result is that ORF1p and ORF2p are controlled by **non-overlapping** negative regulators, arguing for distinct translational/post-translational control that may explain the ~180-fold excess of ORF1p over ORF2p. The work is positioned as a resource (no individual hit functionally validated) for targeting LINE-1 in cancer, autoimmune, and neurodegenerative disease.

## Key Points

- **Dual-reporter design separates ORF1p and ORF2p readouts.** A full-length native L1RP element carries ORF1p–GFP and ORF2p–mCherry (WT or EN/RT-dead) with native 5′/3′ UTRs preserved and a pGK-Hygro-BFP internal control; the construct was integrated into HCT-116 Cas9 cells via piggyBac. ORF1p was confirmed by western blot, flow cytometry and RNA-seq, but **ORF2p-mCherry was never directly detectable**, consistent with known very low ORF2p abundance.
- **The reporter does not perturb the transcriptome.** Only a limited number of DEGs were seen (118 between no-reporter and L1 EN/RT MT; 60 between no-reporter and L1 WT; 28 between L1 EN/RT MT and L1 WT), and only four genes overlap between screen hits and DEGs, so screen results are not artifacts of the reporter.
- **Genome-wide screen scale and hit counts.** ~80,000 gRNAs / ~20,000 genes / 4 gRNAs per gene at ~500-fold coverage; using p < 0.05, gRNA count > 1, TPM < 2 filtering, the primary screen called **398 ORF1p positive regulators, 645 ORF1p negative regulators, and 93 ORF2p negative regulators**. No ORF2p-decreased populations existed because ORF2p-mCherry was undetectable at baseline.
- **Secondary screen validated a high-confidence set.** A 15,000-gRNA / 1,490-gene focused library (10 gRNAs/gene) validated **13 ORF1p positive regulators, 194 ORF1p negative regulators, and 14 ORF2p negative regulators**.
- **HUSH complex recovered as positive control.** All four core HUSH components — **Periphilin (PPHLN1), MORC2, MPP8, TASOR** — known to restrict LINE-1 transcription via heterochromatin, were identified as ORF1p negative regulators (p < 0.05), validating screen quality. (TASOR was supported by a single sgRNA and excluded from the strict primary table to limit false positives.)
- **ORF1p negative regulators are enriched for stress-granule and DNA-repair factors.** Pathway analysis of the 194 validated ORF1p negative regulators showed enrichment of RNA-metabolism proteins involved in stress-granule (SG) formation and of DNA-repair proteins, plus pathways previously linked to L1 — transcriptional regulation by TP53, epigenetic regulation, and viral infection — suggesting ORF1p is coupled to cellular stress-response pathways.
- **ORF1p positive and ORF2p negative regulators lacked clear pathway enrichment.** No significant pathway enrichment was found for ORF1p positive regulators or ORF2p negative regulators, attributed to the low hit numbers; ORF1p positive hits included RNA-binding, transcription, and signaling proteins, while ORF2p negative regulators included protein-degradation, translation, signaling, and transcription factors (suggesting ORF2p is controlled largely post-translationally).
- **Lethality screen finds ORF2p-activity-dependent vulnerabilities.** Reasoning that WT-ORF2p upregulation is toxic while EN/RT-mutant ORF2p is not, guides depleted in WT but not MT cells mark LINE-1-activity-dependent lethality. The primary lethality screen called **415 candidate genes, of which 57 were confirmed** in the secondary validation. Designation required FDR ≤ 0.05 (ORF2p-WT vs library) and FDR ≥ 0.3 (ORF2p-mutant vs library).
- **Lethality hits point to mitochondrial/metabolic and homeostatic processes.** No clean pathway enrichment emerged, but hit classes resembled ORF2p negative regulators (protein degradation, translation, transcription) and additionally included **mitochondrial electron-transport-chain (ETC)** proteins, suggesting a link between energy metabolism and ORF2p toxicity, with some hits connected to cancer biology.
- **ORF1p and ORF2p are controlled by non-overlapping regulators.** Overlap analysis of secondary-screen-confirmed negative-regulator hits for ORF1p vs ORF2p (lethality hits included) showed **no overlap**, with the sole exception of **UROD** — excluded because its knockout causes autofluorescence artifacts. This challenges the assumption that the two co-encoded proteins are co-regulated.
- **Distinct control may explain the ORF1p/ORF2p protein imbalance.** ORF1p is produced ~180-fold higher than ORF2p; the lack of shared regulators supports a model where cells limit ORF2p via translational/post-translational repression while allowing robust ORF1p, with ORF2p activity selectively inducible to drive retrotransposition.
- **Resource framing and limitations.** No individual regulator was functionally validated; ORF2p protein/activity could not be directly verified (~1,000-fold lower than ORF1p by targeted mass spec); cross-study hit overlap was limited; and fluorescence artifacts (e.g. UROD) are a known false-positive source. The L1RP reporter sequence is retrotransposition-competent per prior validation.

## Methods

- **Reporter system:** full-length native L1RP, ORF1p-GFP + ORF2p-mCherry (WT or EN/RT catalytically-inactive point mutants), native 5′/3′ UTRs, HSV-TK + synthetic polyA signals, endogenous ORF1p–ORF2p linker preserved; pGK-Hygro-BFP internal control. Integrated into HCT-116 Cas9 cells (Horizon HD Cas9-002) by piggyBac transposase; hygromycin-selected; validated by flow cytometry and western blot (anti-ORF1p Abcam ab245249).
- **Genome-wide CRISPR screen:** Cellecta KOHGW80 K library (~80,000 sgRNAs, ~20,000 genes, 4 sgRNAs/gene), lentiviral MOI ~0.3, ~500-fold coverage; puromycin 0.5 µg/mL from day 3–8; FACS sort at day 14 (Sony SH800) into ORF1p-GFP decreased/increased and ORF2p-mCherry increased, without altering Hygro-BFP; flash-freeze (ORF2p-mCherry low-yield populations briefly expanded two passages).
- **Lethality screen:** unsorted cells at 18 days post-infection; guides depleted in WT but not EN/RT-MT cells flagged as ORF2p-activity-dependent-lethality candidates.
- **Secondary screen:** custom 15,000-sgRNA library (1,490 genes, 10 sgRNAs/gene) in pRSGEP-U6-sg-EF1-Puro, including primary hits, known L1 regulators/interactors, essential-gene and negative controls; MOI ~0.3, ~1,000-fold coverage; same sort strategy.
- **NGS of gRNAs:** gDNA extraction, two sequential PCRs (Cellecta HTS6C), Illumina HiSeq/NovaSeq, ~500–1,000 reads/sgRNA; 580 negative + 40 positive control sgRNAs.
- **Analysis:** MAGeCK (count + test, total-count normalization, α-RRA), significance p ≤ 0.05 and ≥ 2 "good" sgRNAs for regulators; lethality FDR ≤ 0.05 (WT vs library) and ≥ 0.3 (MT vs library). RNA-seq via STAR/Salmon/DESeq2 (hg38; |log2FC| > 1, adj-p < 0.01). Pathway analysis with Enrichr (Hallmark, GO-BP, FDR < 0.1) and GSEA (fgsea).

## Connections

- [P-Bodies and mRNA Regulation](../topics/p-bodies-and-mrna-regulation.md) — topic hub; this paper links LINE-1 ORF1p control to RNA-metabolism / stress-granule and post-transcriptional regulators, relevant to the broader cytoplasmic mRNP-condensate axis.
- [Kodali 2024 — RNA sequestration in P-bodies sustains myeloid leukaemia](../sources/kodali-2024-rna-sequestration-pbodies-sustains-myeloid-leukaemia.md) — parallel use of comparative CRISPR/Cas9 screens (malignant vs normal here; ORF2p-WT vs EN/RT-mutant there) to find condensate/RNA-regulatory dependencies with a cancer therapeutic window.

## Open Questions

- **Which hits are real regulators vs indirect stress responses?** No individual regulator was functionally validated; the authors note ORF1p/ORF2p changes may be incidental consequences of broad stress responses rather than dedicated pathways.
- **How is ORF2p selectively kept low?** The non-overlapping regulator landscape implies a distinct translational/post-translational brake on ORF2p (~180-fold lower than ORF1p), but the molecular mechanism is unresolved, and ORF2p protein/activity could not be measured directly.
- **Why do stress-granule and DNA-repair factors restrain ORF1p?** The enrichment suggests SG sequestration and genome-maintenance pathways gate ORF1p, but causal mechanisms (e.g. whether ORF1p RNP is sequestered into SGs) are untested here.
- **What couples mitochondrial ETC to ORF2p toxicity?** ETC proteins appearing among lethality hits hint at an energy-metabolism link to LINE-1-activity-dependent death, but the connection is unexplored.
- **Will hits validate across cell types?** HCT-116-specific context (active p53) and limited cross-study overlap leave open whether the regulators generalize.

## Sources

- Local PDF: `raw/inbox/papers/oksuz-2025-identification-regulators-line-expression-crispr-cas.pdf`
- DOI: [10.1186/s13100-025-00386-5](https://doi.org/10.1186/s13100-025-00386-5)
