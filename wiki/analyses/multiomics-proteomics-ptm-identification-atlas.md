# Multiomics Proteomics PTM Identification Atlas

This analysis supports the Korean interactive atlas comparing recent multi-omics proteomics studies by protein, phosphorylation, acetylation, MS method, and instrument. It is based only on maintained wiki pages and local source PDFs.

## Key Points

- This atlas is currently a draft seeded from locally available PDFs. It should be expanded only through the corpus queue and per-paper ingest workflow in [Multiomics PTM Corpus Queue](./multiomics-ptm-corpus-queue.md).
- The strongest directly comparable patient-cohort studies are CPTAC-style tumor proteogenomics papers with TMT/iTRAQ labeling, LC-MS/MS, and phosphopeptide enrichment.
- Acetylome coverage is uneven: endometrial carcinoma, LUAD, LSCC, GBM-like source text, and Zhao 2025 report acetylation layers, while several otherwise relevant proteogenomic studies report only proteome/phosphoproteome or substitute another PTM layer such as glycoproteomics.
- Count units differ by paper. The atlas preserves reported units instead of converting phosphopeptides, phosphosites, phosphoproteins, acetylsites, and protein groups into a false common metric.
- Pan-cancer compendia are useful for scale but are not single acquisition experiments; their bars should be interpreted as aggregate processed-feature counts.

## Extraction Table

| Study | Scope | Proteome | Phospho | Acetyl | Instrument/platform |
|---|---:|---:|---:|---:|---|
| Mertins et al. 2016 | Breast cancer | 15369 | 62679 | NR | not explicit in extracted main PDF text |
| Dou et al. 2020 | Endometrial carcinoma | 12153 | 73212 | 10862 | nanoACQUITY UPLC coupled to Orbitrap Fusion Lumos |
| Gillette et al. 2020 | Lung adenocarcinoma | 10165 | 65103 | 13480 | Q Exactive HF-X for proteome; Orbitrap Fusion Lumos for phosphoproteome and acetylproteome |
| Huang et al. 2021 | HPV-negative HNSCC | 11744 | 56959 | NR | Easy nLC 1200 UHPLC coupled to Thermo Fusion Lumos |
| Cao et al. 2021 | Pancreatic ductal adenocarcinoma | 11662 | 51469 | NR | Easy nLC 1200 UHPLC coupled to Orbitrap Fusion Lumos |
| Satpathy et al. 2021 | Lung squamous cell carcinoma | NR | 68674 | 15186 | Q Exactive HF-X for proteome/acetylproteome; Orbitrap Fusion Lumos for phosphoproteome/ubiquitylproteome |
| Zhang et al. 2022 | Pan-cancer | 15439 | 199284 | NR | varied by contributing source study |
| Li et al. 2023 | Pan-cancer CPTAC | 15699 | 110274 | NR | varied by contributing CPTAC source study |
| Zhao et al. 2025 | HCT116 colorectal cancer cell line | 6147 | 6213 | 185 | Orbitrap Fusion |

## Connections

- [Multiomics Proteomics PTM Identification](../topics/multiomics-proteomics-ptm-identification.md)
- [Multiomics PTM Corpus Queue](./multiomics-ptm-corpus-queue.md)
- [PTM Correction and Kinase Signaling in Cancer Proteomics](../topics/ptm-correction-and-kinase-signaling-in-cancer-proteomics.md)
- [ptmanchor Manuscript Anchor](./ptmanchor-manuscript-anchor.md)
- Interactive HTML: `interactives/multiomics-proteomics-ptm-identification/index.html`

## Sources

- [Proteogenomics connects somatic mutations to signalling in breast cancer](../sources/mertins-2016-proteogenomics-connects-somatic-mutations-signalling.md) - Breast cancer; proteome 15369, phospho 62679, acetyl not reported.
- [Proteogenomic Characterization of Endometrial Carcinoma](../sources/dou-2020-proteogenomic-characterization-endometrial-carcinoma.md) - Endometrial carcinoma; proteome 12153, phospho 73212, acetyl 10862.
- [Proteogenomic Characterization Reveals Therapeutic Vulnerabilities in Lung Adenocarcinoma](../sources/gillette-2020-proteogenomic-characterization-reveals-therapeutic-vulnerabilities.md) - Lung adenocarcinoma; proteome 10165, phospho 65103, acetyl 13480.
- [Proteogenomic insights into HPV-negative head and neck squamous cell carcinoma](../sources/huang-2021-proteogenomic-insights-biology-treatment-hpv-negative.md) - HPV-negative HNSCC; proteome 11744, phospho 56959, acetyl not reported.
- [Proteogenomic characterization of pancreatic ductal adenocarcinoma](../sources/cao-2021-proteogenomic-characterization-pancreatic-ductal-adenocarcinoma.md) - Pancreatic ductal adenocarcinoma; proteome 11662, phospho 51469, acetyl not reported.
- [A proteogenomic portrait of lung squamous cell carcinoma](../sources/satpathy-2021-proteogenomic-portrait-lung-squamous-cell.md) - Lung squamous cell carcinoma; proteome not reported, phospho 68674, acetyl 15186.
- [Proteogenomic characterization of 2002 human cancers reveals pan-cancer molecular subtypes and associated pathways](../sources/zhang-2022-proteogenomic-characterization-2002-human-cancers.md) - Pan-cancer; proteome 15439, phospho 199284, acetyl not reported.
- [Pan-cancer proteogenomics connects oncogenic drivers to functional states](../sources/li-2023-pan-cancer-proteogenomics-connects-oncogenic-drivers.md) - Pan-cancer CPTAC; proteome 15699, phospho 110274, acetyl not reported.
- [Phosphoproteomic and Acetylomic Characterization of Colorectal Cancer Cells Treated with Kinase Inhibitors](../sources/zhao-2025-phosphoproteomic-acetylomic-characterization-colorectal-cancer.md) - HCT116 colorectal cancer cell line; proteome 6147, phospho 6213, acetyl 185.

## Open Questions

- Several studies likely have more precise total protein counts or per-plex counts in supplementary tables that are not currently stored locally. Those values should be added only after the supplements are downloaded into `raw/` and re-read.
- A stricter version of the atlas should separate total identified, filtered quantified, and analysis-feature counts into separate views.
