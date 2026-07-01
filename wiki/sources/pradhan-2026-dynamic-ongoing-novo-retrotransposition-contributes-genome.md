---
title: "Dynamic and Ongoing De Novo L1 Retrotransposition Contributes to Genome Plasticity and Intrapatient Heterogeneity in Ovarian Cancer"
authors:
  - "Pradhan B"
  - "Oikkonen J"
  - "Zhang K"
  - "Botto JM"
  - "Eriksson MR"
  - "Sundaresan S"
  - "Genç F"
  - "Pisanic TR 2nd"
  - "Marín Falco M"
  - "Li Y"
  - "Pikkusaari S"
  - "Lavikka K"
  - "Micoli G"
  - "Marchi G"
  - "Muranen TA"
  - "Huhtinen K"
  - "Vähärautio A"
  - "Badge R"
  - "Burns KH"
  - "Hietanen S"
  - "Hynninen J"
  - "Faulkner GJ"
  - "Hautaniemi S"
  - "Kauppi L"
year: 2026
journal: "Cancer Research"
doi: "10.1158/0008-5472.CAN-24-4419"
pdf: "raw/inbox/papers/pradhan-2026-dynamic-ongoing-novo-retrotransposition-contributes-genome.pdf"
paper_kind: mechanistic
cancer_types:
  - ovarian-cancer
themes:
  - line-1
  - retrotransposition
  - genome-plasticity
  - tumor-heterogeneity
  - replication-stress
  - lin28-let7
tags:
  - source
  - line-1
  - retrotransposon
  - ovarian-cancer
  - cancer
pdf_status: full-text-read
---
# Dynamic and Ongoing De Novo L1 Retrotransposition Contributes to Genome Plasticity and Intrapatient Heterogeneity in Ovarian Cancer

_Cancer Research, 2026._

## Summary

Long INterspersed Element-1 (L1/LINE-1) retrotransposons are the only active, protein-coding transposable elements in the human genome; although silenced in normal adult cells, they are highly expressed in epithelial cancers including high-grade serous ovarian cancer (HGSC). This study quantifies and maps de novo somatic L1 insertions in real-world clinical HGSC specimens from the prospective DECIDER trial, combining genome-wide detection (xTea on WGS) with a highly sensitive, locus-specific assay (LDI-PCR/Nanopore-seq) targeting two known "hot" source elements, **RC-L1_22q12.1** and **RC-L1_Xp22.2**. Across 50 tumors from 28 patients (cohort 1; corroborated in 57 tumors from 38 patients in cohort 2), the authors identified **938 de novo somatic insertions** and found enormous between-patient heterogeneity in total L1 burden (0–228 per tumor; median 8). L1 burden was a **patient-specific** rather than tumor-specific trait — concordant across anatomic sites within a patient — yet the **specific** L1 insertion profiles diverged sharply between tumor sites (82% of LDI-PCR/Nanopore-seq insertions were private to one site), and far more than SNV profiles, identifying L1 retrotransposition as a recent and ongoing mutational process that drives intrapatient genome plasticity at late stages. L1 insertion burden is shaped by genomic (whether a functional RC-L1 is present), transcriptional (whether it is expressed), and posttranscriptional regulation. A central posttranscriptional axis is **LIN28B → let-7 → L1-ORF2p**: L1-high tumors overexpress LIN28B and have low let-7, L1-low tumors have high let-7, and pharmacologic LIN28 inhibition (C1632) raised let-7 and cut L1 retrotransposition ~30% in PA-1 cells. L1-high tumors were highly proliferative (Ki67-high, SBS1 clock signature) and enriched for DNA-replication/repair and ATR-replication-stress pathways, whereas L1-low tumors were enriched for immune-response and cell-death pathways. The authors propose retrotransposition-associated DNA damage / replication stress (e.g. ATR dependence) as a candidate precision-medicine vulnerability.

## Key Points

- **Two complementary detection methods, minimal overlap.** Genome-wide xTea (WGS) and locus-specific LDI-PCR/Nanopore-seq (targeting RC-L1_22q12.1 and RC-L1_Xp22.2, detecting only 3′-transduction events) showed little overlap; together they identified **938 de novo somatic insertions (712 by xTea, 226 by LDI-PCR/Nanopore-seq)** across 50 HGSC tumors from 28 patients, underscoring that relying on one method misses bona fide insertions.
- **L1 burden is highly heterogeneous between patients.** Burden ranged **0–228 insertions per tumor (median 8, mean 19)**; all tumors except two contained ≥1 insertion (both L1-null samples were from one patient, EOC891). Two tumors of a single patient (EOC839) accounted for **>40% (408/938)** of all insertions.
- **Orphan transductions are surprisingly common.** Insertions containing no L1 sequence at all (orphan 3′ transductions) made up **59% and 84%** of total events from RC-L1_22q12.1 and RC-L1_Xp22.2, respectively — these would be missed by methods relying on internal L1 sequence. None of the somatic L1 copies were full-length (average insertion length 807 bp), so they cannot support further retrotransposition.
- **L1 burden is a patient-specific, not tumor-specific, trait.** Within-patient tumors from different anatomic sites (typically ovary/adnexus vs omentum) were largely concordant in both L1 burden and L1 status (low/intermediate/high), corroborated in cohort 2.
- **Insertion profiles diverge within a patient (intrapatient heterogeneity).** Despite concordant burden, the **specific** insertion sites differed: **55%/72% of xTea insertions were shared (cohorts 1/2), but 82% of LDI-PCR/Nanopore-seq insertions were private** to one tumor site; in four patients there were no shared insertions at all. Most shared insertions had the highest normalized read count (dominant subclone).
- **L1 profiles diverge more than SNVs — ongoing, late mutational process.** In 14 L1-high patients, intertumor SNV similarity was significantly higher than L1 insertion similarity (Jaccard Index; Wilcoxon signed-rank P = 0.0354), indicating SNVs are largely early/clonal whereas L1 insertions reflect recent, ongoing retrotransposition during cancer spread.
- **Genomic and transcriptional gating of L1 activity.** RC-L1_Xp22.2 was absent from the genome in five tumors (no insertions possible). RC-L1_22q12.1 was expressed in ~98% of tumors but produced insertions in only 58% (29/50), showing **RC-L1 mRNA expression is not sufficient** to drive insertions.
- **A coding-region SNP inactivates a source L1.** An ORF2p missense variant **rs201455670** (present in patient EOC737 with no RC-L1_22q12.1 insertions, and in cell lines KURAMOCHI and OVSAHO) abolished retrotransposition when engineered into an LRE3 reporter in PA-1 cells; KURAMOCHI/OVSAHO showed no RC-L1_22q12.1 insertions whereas four WT-allele HGSC lines had ≥9 insertions each.
- **LIN28B–let-7–ORF2p is a posttranscriptional regulator of L1.** L1-high tumors overexpressed **LIN28A and LIN28B** (LIN28B more robustly: expressed in all five L1-high but zero L1-low scRNA-seq tumors, in 0.1–40.9% of cancer cells); let-7 miRNAs were high in L1-low and low in L1-high tumors. LIN28 inhibits let-7 maturation, and let-7 represses L1 by inhibiting **L1-ORF2p** translation.
- **Functional validation of LIN28 → L1.** Treating PA-1 cells with the LIN28 inhibitor **C1632 (2.5 μmol/L)** upregulated let-7 family members and reduced L1 retrotransposition by **~30%** in an EGFP reporter assay (two-tailed t test), indicating LIN28 promotes L1 activity via let-7 suppression.
- **L1-high tumors are proliferative.** L1-high tumors were enriched for DNA-replication/cell-cycle pathways, the mitotic clock signature **SBS1**, SBS40, and higher tumor mutation burden. Ki67 immunofluorescence in 40 tumors showed L1-high tumors were predominantly Ki67-high (median Ki67 = 32%; two-tailed Fisher exact P = 0.0152), consistent with L1 insertion's dependence on S-phase DNA replication.
- **Replication stress / DNA-repair vs immune-cell-death dichotomy.** L1-high tumors were enriched for "Activation of ATR in Response to Replication Stress," HRR, and viral-ribonucleoprotein nuclear trafficking pathways; L1-low tumors were enriched for **immune response and cell death (apoptotic and necrotic) pathways**. Notably, genomic HRD metrics (SBS3, ID6, ovaHRDscar) and biallelic BRCA1/BRCA2/RAD51C loss showed **no** association with L1 burden.
- **MAGE/GAGE/PAGE up in L1-high; SERPIN up in L1-low.** Differential expression (L1-high n=30 vs L1-low n=29) found cancer-testis antigen families (MAGE, GAGE, PAGE) upregulated in L1-high and SERPIN family upregulated in L1-low tumors (fold change >2, FDR <0.05).
- **Therapeutic implication.** Retrotransposition-associated DNA damage and/or replication stress is proposed as a candidate molecular vulnerability; L1-high tumors may be sensitive to **ATR inhibitors**, and LIN28 inhibition is raised as a way to attenuate L1 mobilization.

## Methods

- **Clinical specimens**: 50 HGSC tumor samples from 28 patients (cohort 1, FIGO stage III+) and 57 samples from 38 patients (cohort 2), from the prospective observational DECIDER trial (NCT04846933); tumors sampled mainly from tubo-ovarian (ovary/adnexus) and omentum sites, with matched blood DNA.
- **L1 insertion detection**: genome-wide WGS + **xTea** v0.1 (≥20% tumor purity required); **LDI-PCR/Nanopore-seq** (restriction digest, self-ligation, long-distance inverse PCR with inverse primers in the 3′ flanking region, Oxford Nanopore MinION sequencing) targeting RC-L1_22q12.1 and RC-L1_Xp22.2; SV calling via minimap2 + Sniffles with manual IGV curation; normalized read count (NRC) for clonality; joint-calling (JC) for shared/private analysis; Jaccard Index for intertumor similarity.
- **Source-L1 characterization**: genotyping PCR (presence/absence of source RC-L1), RT-PCR/qRT-PCR for locus-specific RC-L1 transcription, ORF1p IHC (anti-L1-ORF1p MABC1152), LONGSHOT SNV detection in RC-L1_22q12.1 to find inactivating variants.
- **Functional retrotransposition assays**: EGFP-based L1 reporter (99gfpLRE3 / 99CBhgfpLRE3 modified, with mCherry-2A-puromycin) in **PA-1** teratocarcinoma cells; engineered ORF2p variant rs201455670 into LRE3; RT-deficient (D702A) negative control; LIN28 inhibitor C1632 (2.5 μmol/L) treatment with let-7 readout by miRCURY LNA qRT-PCR.
- **Multiomics**: cancer-cell-specific RNA-seq deconvolution (PRISM), DESeq2 differential expression, fgsea GSEA (Hallmark/KEGG/PID/REACTOME); scRNA-seq (GEO GSE266577) for LIN28A/LIN28B cell-fraction; let-7 qRT-PCR panel in 14 tumors; SBS mutational signatures (COSMIC v3.2), ovaHRDscar; Ki67 + pan-cytokeratin immunofluorescence quantified in QuPath/StarDist across 40 tumors.
- **HGSC cell lines**: OAW28, COV318, OVCAR5, COV362, KURAMOCHI, OVSAHO, and teratocarcinoma PA-1.

## Connections

- [P-Bodies and mRNA Regulation](../topics/p-bodies-and-mrna-regulation.md) — topic hub; L1-ORF1p/ORF2p RNPs and L1 mRNA are post-transcriptionally regulated cytoplasmic mRNP particles, intersecting P-body/granule biology and let-7-mediated translational repression.
- [P-bodies in cancer and leukaemia](../concepts/p-bodies-in-cancer-and-leukaemia.md) — both works frame post-transcriptional/RNA-level control as a cancer dependency; here let-7 repression of L1-ORF2p translation and LIN28B over-expression gate a cancer-promoting process (genome instability) rather than tumour-suppressor sequestration.
- [Kodali 2024 — RNA sequestration in P-bodies sustains myeloid leukaemia](../sources/kodali-2024-rna-sequestration-pbodies-sustains-myeloid-leukaemia.md) — companion "post-transcriptional control as cancer axis" paper; Kodali shows sequestration silences tumour suppressors, whereas Pradhan shows translational control (let-7/LIN28) of a mutagenic retroelement.

## Open Questions

- **What drives the patient-specific propensity for L1 insertion?** Burden is concordant within a patient but varies widely between patients; the authors implicate molecular properties of the progenitor tumor, but the determining factor(s) beyond LIN28B/let-7 and replication capacity remain unresolved.
- **Do L1-low tumors harbor "idle" L1 cDNA that drives immune activation?** L1-low tumors are enriched for immune and cell-death pathways, but whether this links to innate-immune sensing of L1 cDNA (and whether such cDNA exists in low-insertion tumors) is untested.
- **Is the LIN28B–let-7–ORF2p axis causal in vivo and druggable?** C1632 reduced L1 activity ~30% in vitro; whether LIN28 inhibition meaningfully limits retrotransposition-driven genome plasticity in patients is open.
- **Can replication-stress dependence be exploited therapeutically?** L1-high tumors are proliferative and ATR-replication-stress-enriched; whether ATR inhibitors selectively target L1-high HGSC requires functional testing.
- **Are the L1-high/L1-low DEGs causal or bystanders?** MAGE/GAGE/PAGE and SERPIN signatures, and other pathways, may report upstream/downstream processes independent of L1 insertional activity, possibly mediated by let-7.

## Sources

- Local PDF: `raw/inbox/papers/pradhan-2026-dynamic-ongoing-novo-retrotransposition-contributes-genome.pdf`
- DOI: [10.1158/0008-5472.CAN-24-4419](https://doi.org/10.1158/0008-5472.CAN-24-4419)
