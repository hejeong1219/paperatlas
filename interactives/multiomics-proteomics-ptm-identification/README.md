# Multiomics Proteomics PTM Identification

Korean interactive visualization project for recent-10-year multi-omics studies comparing identification counts and mass-spectrometry methods.

## Intended Scope

- Time window: recent 10 years from the request date unless the user specifies exact dates.
- Modalities: proteome, phosphoproteome, acetylome or acetyl-proteome where reported.
- Fields: study, year, cohort or cancer type, sample count, protein identification count, phosphoprotein/phosphosite count, acetylprotein/acetylsite count, MS acquisition method, LC-MS/MS platform, instrument, software/database notes, and uncertainty notes.

## Source Protocol

1. Search the wiki for multi-omics, proteomics, phosphoproteomics, acetylomics, CPTAC, and cancer proteogenomics.
2. Open relevant `wiki/sources/` pages.
3. Re-read the original PDFs in `raw/`, including Methods, supplemental methods, figure legends, and supplementary tables.
4. Record values exactly as defined by the paper. Do not silently convert phosphosites into phosphoproteins or quantified proteins into identified proteins.
5. Mark missing or incomparable values as `not_reported` or with a short note.

Do not use web search or general web pages to fill study values. The `audodidactic`-style reference can guide layout, navigation density, and interaction patterns only.

## Files

- `index.html`: final Korean interactive plot.
- `data/studies.json`: curated source dataset for the visualization.
- `assets/`: optional local static assets.

## Included Sources

- Mertins 2016 breast cancer proteogenomics.
- Dou 2020 endometrial carcinoma proteogenomics.
- Gillette 2020 lung adenocarcinoma proteogenomics.
- Huang 2021 HPV-negative HNSCC proteogenomics.
- Cao 2021 pancreatic ductal adenocarcinoma proteogenomics.
- Satpathy 2021 lung squamous cell carcinoma proteogenomics.
- Zhang 2022 pan-cancer proteogenomic compendium.
- Li 2023 pan-cancer CPTAC proteogenomics.
- Zhao 2025 colorectal cancer cell-line kinase-inhibitor proteome/phosphoproteome/acetylome perturbation.

## Extraction Notes

- Values are taken from local wiki source pages and re-read local PDFs only.
- Counts preserve the paper's reported unit: proteins, protein groups, genes, phosphosites, phosphopeptides, phospho-protein features, acetylsites, or acetylated proteins are not forced into one artificial unit.
- Some papers report total identified counts, while others expose filtered analysis-feature counts in the PDF text. The visualization labels these differences with `*_count_type`.
- If a single global value was not visible in extracted PDF text, the field remains empty instead of being filled from the web.
- Pan-cancer compendia are marked separately from single-cohort MS experiments because their counts aggregate processed data across multiple contributing studies.

## Status

Initial interactive visualization created from local PDFs. Further refinement should add supplementary-table-derived values where local supplements become available.
