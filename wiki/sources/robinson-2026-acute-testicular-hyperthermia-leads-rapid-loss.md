---
title: "Acute testicular hyperthermia leads to rapid loss of global piRNA and a concurrent increase in LINE1 activity within heat sensitive male germ cells"
authors:
  - "Robinson BR"
  - "Netherton JK"
  - "Ogle RA"
  - "Burnard SM"
  - "Williams GE"
  - "Tennant GM"
  - "Hussein M"
  - "Lee HJ"
  - "Velkov T"
  - "Baker MA"
year: 2026
journal: "Mobile DNA"
doi: "10.1186/s13100-025-00390-9"
pdf: "raw/inbox/papers/robinson-2026-acute-testicular-hyperthermia-leads-rapid-loss.pdf"
paper_kind: mechanistic
themes:
  - line-1
  - pirna
  - germ-cell
  - retrotransposon
  - chromatoid-body
  - phase-separation
  - dna-damage
  - testicular-hyperthermia
tags:
  - source
  - line-1
  - pirna
  - retrotransposon
  - germ-cell
  - condensate
pdf_status: full-text-read
---
# Acute testicular hyperthermia leads to rapid loss of global piRNA and a concurrent increase in LINE1 activity within heat sensitive male germ cells

_Mobile DNA, 2026._

## Summary

Spermatogenesis occurs 2–6 °C below core body temperature, and acute testicular hyperthermia preferentially damages the most heat-sensitive germ cells (spermatocytes, then round spermatids), producing fewer, poorer-quality sperm with elevated DNA damage. To capture the *immediate* molecular response, the authors submerged mouse testes in a 42 °C water bath for 30 min (vs 33 °C anaesthetic controls) and performed whole-transcriptome RNA-seq on FACS-/STA-PUT–isolated round spermatids ~6 h later, comparing responses with enriched pachytene spermatocytes. RNA-seq (DESeq2, FDR < 0.05, |FC| > 1.5) found a striking, atypical bias toward upregulation: **124 transcripts up vs 10 down (93% upregulated)**. Re-analysis with TEtranscripts showed transposable elements (class I retrotransposons — LINEs, SINEs, LTRs — and class II DNA transposons) trending up. The authors validated **LINE1**: RT-qPCR (3′UTR/ORF1/ORF2 primers) detected an average **3.3-fold LINE1 increase in spermatocytes** (and an upward, non-significant trend in round spermatids), and immunoblotting showed a significant rise in **ORF1p** protein. Because piRNAs normally silence TEs, they quantified mature piRNA by denaturing Urea-PAGE and found a **>50% global piRNA reduction**, significant in spermatocytes (trend in round spermatids). PIWIL1 protein abundance/localisation was unchanged at 3 h, ruling out simple mature-piRNA degradation; instead, the precursor **pre-piR1 accumulated** in heat-stressed spermatocytes (pre-piR2/pre-piR3 unchanged), pointing to a block in pre-piRNA *processing*. BLAT of the piR1-derived mature piRNA against mm39 matched an annotated **LINE1 (L1M2 subfamily)** element, giving a direct piRNA→LINE1 targeting link. Electron microscopy showed the **chromatoid body (CB)** — an LLPS ribonucleoprotein granule that is an epicentre of piRNA biogenesis — became dispersed by 3 h post-heat, *before* piRNA loss and LINE1 upregulation. The proposed model: heat dissolves LLPS biocondensates (CB/IMC) rich in temperature-sensitive IDR proteins → defective piRNA biogenesis → global piRNA loss → TE/LINE1 de-repression → DNA damage and impaired spermatogenesis. Effects were transient (piRNA and LINE1 normalised by 24 h). The work frames condensate destabilisation as the upstream trigger coupling germ-cell heat sensitivity to retrotransposon activation.

## Key Points

- **An atypical upregulation bias dominates the acute heat response.** RNA-seq of isolated heat-stressed round spermatids found **124 transcripts upregulated vs 10 downregulated**, i.e. **93% of differentially expressed transcripts upregulated** (DESeq2, FDR < 0.05, |FC| > 1.5, N = 5) — unusual for omics data, hinting at a loss of a global repressor.
- **RT-qPCR validated the signature across two heat-sensitive cell types.** *LncRNA4930555K19Rik* and the heat-shock gene *Hspa1a* rose while *Stat2* fell in both round spermatids and spermatocytes; *Hspa1a* showed ~3 (log2)-fold increase in isolated round spermatids vs 8.5 (log2)-fold in a comparable whole-testis dataset, and was the only gene shared between the two datasets at 6 h, underscoring that whole-testis RNA masks germ-cell–specific changes.
- **Transposable elements of all classes trend upward after heat.** TEtranscripts re-analysis showed both class I retrotransposons (LINEs, SINEs, LTRs) and class II DNA transposons increasing; only one TE passed Benjamini–Hochberg significance in round spermatids, but the directional trend was clear.
- **LINE1 transcript abundance rises, strongest in spermatocytes.** Using three primer sets (3′UTR, ORF1, ORF2), RT-qPCR detected an **average 3.3-fold LINE1 increase in spermatocytes** and an upward but non-significant trend in round spermatids — consistent with spermatocytes being the more heat-sensitive cell type.
- **LINE1 protein output increases (ORF1p).** Immunoblotting showed a clear, significant rise in **ORF1p** abundance in heat-stressed round spermatids (similar trend in spermatocytes), indicating not just transcription but active LINE1 protein production. ORF1p and ORF2p are the LINE1-encoded proteins required for template RNA binding and retrotransposition respectively.
- **Global piRNA levels drop >50%.** Denaturing 15% Urea-PAGE quantification of the mature piRNA band (normalised to total RNA) showed a **significant reduction in spermatocytes** and a downward trend in round spermatids — a >50% global piRNA loss that the authors argue explains the broad TE de-repression.
- **The loss is not due to PIWIL1 destabilisation.** Immunohistochemistry showed **PIWIL1 abundance and localisation remained stable at 3 h** post-heat versus stage-matched controls; TDRD6 was likewise stable (data not shown). So mature-piRNA degradation via loss of PIWI is unlikely; the defect is upstream in biogenesis.
- **pre-piR1 accumulates — a processing block, not just degradation.** Of three precursors quantified, **pre-piR1 significantly accumulated** in heat-stressed spermatocytes while pre-piR2 and pre-piR3 were unchanged, indicating a failure to process pre-piR1 into mature piRNA.
- **piR1 directly targets a LINE1 (L1M2) element.** BLAT alignment of the mature piR1 complement against mm39 returned two high-confidence matches, one overlapping an annotated **LINE1 of the L1M2 subfamily** — a direct mechanistic link explaining why LINE1 specifically is de-repressed when pre-piR1 processing fails.
- **The chromatoid body is structurally disrupted by 3 h.** Scanning EM of stage 7–8 round spermatids showed the CB, normally a compact electron-dense perinuclear granule, became **dispersed with electron-dense material spread through the cytoplasm** 3 h after 42 °C heat. This disorganisation **precedes both piRNA loss and LINE1 upregulation**, placing CB destabilisation upstream.
- **Condensate dissolution, not component degradation, is the proposed cause.** The CB/IMC are LLPS granules enriched in temperature-sensitive intrinsically disordered region (IDR) proteins; lower temperatures favour condensate formation while higher temperatures drive dissolution. Stable PIWIL1/TDRD6 levels argue the granule disperses by temperature-dependent dissolution rather than its proteins being degraded.
- **Effects are transient.** By **24 h post-heat, piRNA levels and LINE1 transcript abundance were no longer significantly different from controls** in either spermatocytes or round spermatids, marking these as an acute early response.
- **Splicing/polyadenylation changes are secondary.** 395 local splice-variation events (e.g. *Fads2* intron retention, validated) and differential APA (20 proximal, 41 distal sites) occurred but were variable/low-magnitude and showed no GO pathway enrichment; the authors conclude LSV and APA are secondary consequences, not primary drivers.
- **Downstream consequence and epigenetic reach.** The model ties global piRNA loss → TE/LINE1 activation → DNA damage and impaired spermatogenesis (apoptosis, abnormal manchette/acrosome formation). piRNAs also guide DNMT3C-mediated TE-promoter methylation via MILI-piRNA complexes, so heat-induced piRNA loss may have lasting epigenetic and embryo-loss consequences.

## Methods

- **Testicular heat-stress model:** anaesthetised Swiss (CD1) mice with scrotum submerged in a thermally controlled water bath at **42 °C (heat) or 33 °C (control) for 30 min**; sacrificed at indicated times. Note: heating + cell isolation took ~6 h, so the "immediate" RNA-seq timepoint is ~6 h.
- **Germ-cell purification:** seminiferous tubules enzymatically dissociated (collagenase/DNase then trypsin/DNase); round spermatids isolated by **FACS** (~90% purity) for NGS and by **STA-PUT velocity sedimentation** (spermatocytes ~80% purity) for all other assays.
- **Whole-transcriptome RNA-seq:** Illumina NovaSeq 150 bp PE (N = 5; 56–148 M reads/sample); STAR alignment to GRCm38; **TEtranscripts** for gene+TE counts; **DESeq2** (base-mean > 10, FDR < 0.05, |FC| > 1.5); GO via clusterProfiler.
- **Splicing/APA:** **MAJIQ/VOILA** for local splice variations (Δψ > 0.1, CI > 0.9), Sashimi plots via IGV; **QAPA** for alternative polyadenylation.
- **RT-qPCR:** RNeasy + TURBO DNase; QuantiTect RT; PowerUp SYBR Green; *actb* reference; LINE1 primers (3′UTR/ORF1/ORF2) and pre-piRNA primers from published sources.
- **piRNA quantification:** TRIzol RNA + **15% denaturing Urea-PAGE**, GelRed stain, piRNA band normalised to 6 control RNA bands (FIJI).
- **Protein:** immunoblot for **ORF1p** (ab216324) normalised to α-tubulin; **immunohistochemistry** for **PIWIL1** (ab12337) on testis sections, stage-matched.
- **piRNA target prediction:** **BLAT** of piR1 complement vs mm39 (UCSC), inspected against RepeatMasker TE annotations.
- **DNA damage:** Click-iT Plus **TUNEL** assay.
- **Ultrastructure:** **Scanning Electron Microscopy** of the chromatoid body in stage 7–8 round spermatids, 3 h post-heat.

## Connections

- [P-Bodies and mRNA Regulation](../topics/p-bodies-and-mrna-regulation.md) — topic hub; this paper extends the condensate/RNP-granule theme from cytoplasmic P-bodies to the germ-cell chromatoid body and intermitochondrial cement, where LLPS dissolution (rather than P-body assembly) drives small-RNA loss and retrotransposon de-repression.
- The retrotransposon-defense axis here (piRNA loss → LINE1/ORF1p activation → DNA damage) parallels the LINE-1/retroelement-control thread running through the broader LINE-1 source set, but via a phase-separation–dependent biogenesis failure rather than a protein-level perturbation.

## Open Questions

- **Is LINE1 retrotransposition (new insertions), not just transcription/ORF1p, actually increased?** The authors validate transcript and protein but call for future work to "definitively investigate the role of LINE1" as a driver of heat-induced DNA damage.
- **What is the causal chain from CB dissolution to a specific pre-piR1 processing block?** CB disruption precedes piRNA loss, but which biogenesis enzymes/steps fail (and why pre-piR1 specifically, not pre-piR2/3) is unresolved.
- **Do the persistent epigenetic consequences (DNMT3C/MILI-piRNA-mediated TE-promoter methylation) explain heat-associated embryo loss?** Raised as a hypothesis, untested here.
- **How much do somatic cells (Sertoli, Leydig) and the dissociation procedure itself contribute?** The germ-cell-autonomous model does not preclude their involvement.

## Sources

- Local PDF: `raw/inbox/papers/robinson-2026-acute-testicular-hyperthermia-leads-rapid-loss.pdf`
- DOI: [10.1186/s13100-025-00390-9](https://doi.org/10.1186/s13100-025-00390-9)
- Data: GEO accession GSE290301
