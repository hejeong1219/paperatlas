# Multiomics Proteomics PTM Identification

Korean interactive visualization project for recent-10-year multi-omics studies comparing identification counts and mass-spectrometry methods.

Canonical wiki topic: `wiki/topics/multiomics-proteomics-ptm-identification.md`.

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

- `data/studies.json` currently contains 67 rows spanning the 2016-2026 corpus and extra downloaded candidates.
- Rows have `extraction_status` values: `extracted`, `pdf_pending_extraction`, `pdf_pending`, or `blocked_pdf`.
- Quantitative bars are meaningful only where count fields were extracted from verified local PDFs/source pages; pending rows are shown for coverage and triage visibility.

## Extraction Notes

- Values are taken from local wiki source pages and re-read local PDFs only.
- Counts preserve the paper's reported unit: proteins, protein groups, genes, phosphosites, phosphopeptides, phospho-protein features, acetylsites, or acetylated proteins are not forced into one artificial unit.
- Some papers report total identified counts, while others expose filtered analysis-feature counts in the PDF text. The visualization labels these differences with `*_count_type`.
- If a single global value was not visible in extracted PDF text, the field remains empty instead of being filled from the web.
- Pan-cancer compendia are marked separately from single-cohort MS experiments because their counts aggregate processed data across multiple contributing studies.

## Standard Keys (unit-preserving)

To prevent accidental “unit conversion,” `data/studies.json` should keep both value and unit/type fields for each omics layer.

- `proteome_count_value` + `proteome_count_unit` + `proteome_count_type`
- `phospho_count_value` + `phospho_count_unit` + `phospho_count_type`
- `acetyl_count_value` + `acetyl_count_unit` + `acetyl_count_type`

Recommended controlled values:

- `*_count_unit`: `protein`, `protein_group`, `gene`, `phosphosite`, `localized_phosphosite`, `phosphopeptide`, `acetylsite`, `localized_acetylsite`, `acetylpeptide`, `ubiquitylsite`, `not_reported`, `unknown`
- `*_count_type`: `identified_total`, `quantified_filtered`, `site_polished`, `analysis_feature_set`, `aggregate_compendium`, `not_reported`, `unknown`

## Corpus-First Status

The current HTML has moved from a small seed dataset to a corpus-coverage atlas. The intended production workflow is:

1. Curate the paper corpus in `wiki/analyses/multiomics-ptm-corpus-queue.md`.
2. Download or locate every needed PDF and supplement in `raw/`.
3. Ingest each source page with a `Multi-Omics Identification Extraction` section.
4. Rebuild `data/studies.json` from those source pages, preserving status fields when extraction is incomplete.
5. Rebuild and publish the interactive site.

Further refinement should add supplementary-table-derived values where local supplements become available.
