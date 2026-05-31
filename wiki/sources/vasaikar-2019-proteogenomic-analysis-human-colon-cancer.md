---
title: "Proteogenomic Analysis of Human Colon Cancer Reveals New Therapeutic Opportunities"
authors:
  - "Vasaikar"
  - "Huang"
  - "Wang"
year: 2019
journal: "Cell"
doi: "10.1016/j.cell.2019.03.030"
pmid: "31031003"
pmcid: "PMC6768830"
paper_kind: proteogenomic-atlas
cancer_types:
  - colon-cancer
modalities:
  - whole-exome-sequencing
  - copy-number
  - rna-seq
  - mirna-seq
  - label-free-proteomics
  - tmt-global-proteomics
  - tmt-phosphoproteomics
  - targeted-proteomics
themes:
  - therapeutic-vulnerability
  - kinase-signaling
  - immune-evasion
  - tumor-antigen
  - msi
  - glycolysis
  - rb-phosphorylation
tags:
  - cancer-multiomics
  - drug-response
  - ptmanchor
  - proteomics
  - phosphoproteomics
  - immune-evasion
  - colon-cancer
corpus_role: core-proteogenomic-vulnerability
ingest_status: full-text-read
ingested_on: 2026-05-13
pdf: "raw/inbox/papers/vasaikar-2019-proteogenomic-analysis-human-colon-cancer.pdf"
topic: cancer-multiomics
cm_axis: wgs
---
# Proteogenomic Analysis of Human Colon Cancer Reveals New Therapeutic Opportunities

Vasaikar et al. profile a prospective colon cancer cohort with WXS, copy-number, RNA, miRNA, label-free proteomics, TMT global proteomics, and TMT phosphoproteomics. The paper is especially useful for the drug-response POC because it shows multiple cases where mutation/CNA-level interpretation is revised or sharpened by protein abundance and phosphosite activity.

## Full-Text Read Status

- Status: `full-text-read` on 2026-05-13.
- Local PDF identity verified against title, Cell 2019 journal metadata, DOI `10.1016/j.cell.2019.03.030`, and 35-page local PDF.
- Evidence boundary: all scientific claims below come from the local PDF `raw/inbox/papers/vasaikar-2019-proteogenomic-analysis-human-colon-cancer.pdf`.

## Key Points

- The cohort contains 110 prospectively collected colon cancer patients with tumor, matched normal adjacent tissue (NAT), and blood. Inclusion required newly diagnosed, untreated colon adenocarcinoma undergoing primary surgery; rectal tumors were excluded.
- WXS analysis of 106 tumor/blood pairs identified 64,010 somatic SNVs, 7,691 somatic indels, 6,186 somatic microsatellite indels, and 56,592 unique protein-altering events.
- Microsatellite analysis separated 24 MSI-H tumors and 82 MSS tumors. WXS-based MSI assignment completely matched PCR-based MSI results for the 85 cases with PCR testing.
- TMT global proteomics of 96 tumor/NAT pairs identified 8,067 proteins; 6,422 were quantified in at least 50% of samples. Of those, 2,217 were significantly increased and 2,527 significantly decreased in tumor versus NAT.
- TMT phosphoproteomics quantified 7,295 phosphosites in at least 50% of matched samples. Of those, 2,119 were significantly increased and 3,053 significantly decreased in tumor versus NAT.
- Proteomics changed the interpretation of SOX9: despite truncating mutations that would suggest tumor-suppressor logic under a mutation-only rule, SOX9 protein was overexpressed in tumors, including tumors with truncating mutations, supporting an oncogenic interpretation.
- Phosphoproteomics nominates Rb phosphorylation as an oncogenic driver-like state in colon cancer. RB1 copy number and total Rb are elevated, but tumor/NAT phospho-Rb fold change is higher than total Rb fold change, and phospho-Rb links to E2F1 activity, CDK2 activity, H3.1 phosphorylation, and lower apoptosis hallmark signal.
- Tumor-antigen analysis finds 88 putative proteomics-supported neoantigens in 38% of tumors and proteomics-supported neoantigens or cancer/testis antigens in 78% of tumors.
- MSI tumors show broad protein-level glycolysis elevation and TCA-cycle decrease. Within MSI tumors, glycolytic activity negatively correlates with activated CD8 T-cell infiltration, nominating glycolysis inhibition as a possible way to improve checkpoint blockade response in resistant MSI tumors.

## Cohort and Assay Design

- Clinical procurement required tumor and NAT collection within less than 30 minutes total ischemic time and OCT embedding to preserve phosphoprotein suitability.
- Tumor specimens were required to be greater than 300 mg, at least 60% tumor-cell nuclei, and less than 20% necrosis.
- Assay layers include WXS, copy-number profiling, RNA-seq, miRNA-seq, label-free shotgun proteomics on tumors, and TMT 10-plex global and phosphoproteomics on tumors plus NATs.
- Global TMT proteome LC-MS/MS used a Q Exactive Plus instrument. TMT phosphoproteomics used Fe3+-NTA IMAC enrichment and an Orbitrap Fusion Lumos.
- TMT global proteomics generated 264 data files; TMT phosphoproteomics generated 132 data files.
- Channel 131 was used as an internal reference sample pooled from all tumor and normal samples, enabling comparison across TMT 10-plexes.

## Mutation and Copy-Number Interpretation

- Non-hypermutated tumors had eight significantly mutated genes, all previously reported in TCGA. Hypermutated tumors had nine significantly mutated genes, including six not reported in TCGA; CASP5, RNF43, LTN1, and BMPR2 were mutated in more than 50% of hypermutated samples.
- Protein/phosphosite readouts confirmed predictable truncation effects such as reduced APC T2451 and TGFBR2 S553 abundance downstream of mutations.
- TP53 R273 mutations showed high TP53 S315 phosphorylation; the authors cross-checked CPTAC breast and ovarian studies and found R273-mutant tumors had TP53 S315 phosphorylation above cohort medians.
- SCNA analysis found arm-level patterns similar to TCGA, including 1q, 7p/q, 8p/q, 13q, and 20p/q amplifications plus 1p, 14q, 15q, 17p/q, 18p/q, and 22q deletions.
- SCNA cis-effects on protein abundance were stronger than in an earlier label-free analysis, and tumor/NAT protein comparison refined focal SCNA driver candidates. Only 59% of correlated amplification/deletion candidates showed the expected tumor-versus-NAT protein-level effect.

## Rb Phosphorylation and Kinase Vulnerability

- RB1 is recurrently amplified in this colon cancer cohort and Rb protein is overexpressed in tumors compared with NATs.
- Six Rb phosphorylation sites were quantified in at least 50% of samples; four sites, T373, S807, S811, and T826, regulate E2F binding.
- The average abundance of those four Rb phosphosites was higher in tumors than NATs, and phospho-Rb tumor/NAT change exceeded total Rb change.
- Phospho-Rb change correlated with E2F1 activity, CDK2 activity, H3.1 phosphorylation, and inversely with apoptosis hallmark protein signal.
- The paper proposes CDK2 inhibition as a way to target Rb phosphorylation in colon cancer, especially because this context differs from cancers where RB1 is deleted or mutated.
- More broadly, kinase activity prediction identified CDK7 by both activating-site and substrate-enrichment approaches. The nominated kinase set includes CDK4, CDK1, CDK2, CDK7, MELK, PFKFB3, and PI4KB; CDK4 already had FDA-approved inhibitors and the other CDKs/MELK/PFKFB3 had clinical-trial drugs at the time of the paper.

## Tumor Antigen Findings

- Customized proteomics databases incorporating WXS and RNA-seq variants were used to search label-free proteomics, TMT global proteomics, and TMT phosphoproteomics data.
- The study detected 173 proteomics-supported somatic mutations and then evaluated 8-11 amino acid mutant peptides for HLA-I binding.
- Eighty-eight mutant peptides with predicted HLA binding affinity below 150 nM were considered putative neoantigens; at least one was found in 38% of tumors.
- TMT global proteomics identified 16 cancer/testis antigens. IGF2BP3, SPAG1, and ATAD2 were increased at least 2-fold in tumors versus NATs in more than 5% of pairs; IGF2BP3 was increased in 51%.
- Unlike patient-specific neoantigens enriched in MSI-H tumors, cancer/testis antigens were independent of MSI status and shared across patients, making them relevant for MSS tumors with lower neoantigen load.

## Unified Molecular Subtypes and Immune Metabolism

- The study integrated MSI status, RNA CMS subtypes, and proteomic ProS subtypes into three unified multi-omics subtypes: `MSI`, `CIN`, and `Mesenchymal`.
- The UMS classification assigned 87 of 110 tumors. It removed a discrete CMS3 group by distributing CMS3-like tumors across other UMS subtypes.
- CIN tumors had higher chromosome instability and higher RB1 copy-number gain than other subtypes. Rb S811 and S807 phosphosites were more elevated than total Rb in CIN, supporting a CIN-specific CDK2/Rb hypothesis.
- Mesenchymal tumors had higher stromal infiltration and suppressive immune-cell features including MDSCs, macrophages, and Tregs.
- MSI tumors had cytotoxic immune-cell enrichment, including NK cells and activated CD8 T cells, but also elevated glycolytic enzymes at the protein level.
- In MSI tumors, glycolytic activity negatively correlated with activated CD8 T-cell infiltration (Spearman r = -0.61, p = 0.02). This correlation was not observed when all colon tumors were pooled or in other subtypes.
- SRM/PRISM-SRM targeted validation supported the TMT measurements for CD8A, SLC2A3, and PKM2 and showed higher SLC2A3 and PKM2 in MSI tumors versus CIN/Mesenchymal tumors.

## Relevance to Drug-Response POC

- This paper is a strong POC template for showing why SNV-only precision oncology is incomplete: SOX9 mutation interpretation, RB1 amplification, and MSI immune behavior all require protein or phosphoprotein context.
- For a global proteome/phosphoproteome/somatic SNV drug-response manuscript, the Rb example gives a clean ladder: `RB1 CNA/protein abundance -> phospho-Rb S807/S811/T373/T826 -> E2F/CDK2/proliferation/apoptosis state -> CDK2 inhibitor hypothesis`.
- For immune-evasion or immunotherapy-response analyses, the MSI example gives another ladder: `MSI/TMB-like genomic state -> protein glycolysis/PKM2/SLC2A3 -> CD8 infiltration suppression -> checkpoint resistance hypothesis`.
- The paper also supports separating tumor antigen evidence into mutation-derived neoantigens and shared cancer/testis antigens, which matters if the broader wiki keeps B-cell neoantigen and immune-evasion tracks connected.
- In the user's POC, Vasaikar 2019 should be used as a foundational colon cancer atlas and mechanistic hypothesis template, not as a direct treated-response training cohort.

## Limitations

- The cohort is treatment-naive and surgical; the therapeutic conclusions are hypotheses rather than direct drug-response validation.
- Rectal tumors were excluded, so findings should not be generalized to all CRC without care.
- The glycolysis/checkpoint-resistance idea is inferred from proteomics and immune deconvolution plus targeted-proteomics support; it is not directly tested with checkpoint inhibitor response in this cohort.
- The neoantigen analysis uses proteomics-supported variants and HLA binding prediction, but the paper does not demonstrate immunogenicity for the predicted neoantigens in this cohort.
- Some kinase nominations depend on known activating-site or substrate-set coverage; low substrate coverage can miss relevant kinases.

## Data Availability

- Raw genomics data: SRA BioProject `PRJNA514017`.
- Raw and low-level processed proteomics data: CPTAC Data Portal study `S045`.
- Final data matrices: LinkedOmics CPTAC colon portal.

## Connections

- [Drug Response Proof-of-Concept with Global Proteome, Phosphoproteome, and Somatic SNV](../analyses/drug-response-poc-global-phospho-somatic-snv.md)
- [Drug Response Phospho-Global 100-PDF Bulk Ingest](../analyses/drug-response-phospho-global-100-bulk-ingest.md)
- [Drug Response Phospho-Global Proteomics Corpus Queue](../analyses/drug-response-phospho-global-100-corpus-queue.md)
- [Cancer Multiomics Proteogenomic Atlas](../topics/cancer-multiomics-literature.md)
- [Immunotherapy Resistance and Immune Evasion](../topics/immunotherapy-resistance-and-immune-evasion.md)
- [PTM Correction and Kinase Signaling in Cancer Proteomics](../topics/ptm-correction-and-kinase-signaling-in-cancer-proteomics.md)
- [Multiomics Proteomics PTM Identification](../topics/multiomics-proteomics-ptm-identification.md)

## Sources

- Local PDF: `raw/inbox/papers/vasaikar-2019-proteogenomic-analysis-human-colon-cancer.pdf`

## 함께 인용된 논문

위키 분석·합성 페이지에서 이 논문과 함께 인용된 논문들 (co-citation).

- [[cao-2021-proteogenomic-characterization-pancreatic-ductal-adenocarcinoma|Cao 2021]]
- [[clark-2020-integrated-proteogenomic-characterization-clear-cell|Clark 2020]]
- [[gillette-2020-proteogenomic-characterization-reveals-therapeutic-vulnerabilities|Gillette 2020]]
- [[huang-2021-proteogenomic-insights-biology-treatment-hpv-negative|Huang 2021]]
- [[wang-2021-proteogenomic-metabolomic-characterization-human-glioblastoma|Wang 2021]]
- [[zhao-2025-phosphoproteomic-acetylomic-characterization-colorectal-cancer|Zhao 2025]]
- [[anurag-2022-proteogenomic-markers-chemotherapy-resistance-response|Anurag 2022]]
- [[chen-2020-proteogenomics-non-smoking-lung-cancer-east|Chen 2020]]
- [[chmielecki-2023-acquired-resistance-first-line-osimertinib|Chmielecki 2023]]
- [[dou-2020-proteogenomic-characterization-endometrial-carcinoma|Dou 2020]]
