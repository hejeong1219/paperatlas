# Interactives

Standalone interactive HTML visualizations live here. Each project should be self-contained enough to publish through the Quartz/GitHub Pages pipeline.

## Folder Pattern

- `index.html`: Korean interactive visualization entry point.
- `data/`: curated CSV or JSON extracted from wiki pages and re-read PDFs.
- `assets/`: local images, styles, or other static files.
- `README.md`: provenance, source list, extraction notes, missing values, and update status.

## Workflow

1. Search the wiki first with `./bin/qmd search`.
2. Open the relevant source pages and original PDFs in `raw/`.
3. Extract the numeric fields into `data/` with explicit definitions.
4. Build the interactive Korean HTML in `index.html`.
5. Run `./bin/sync-wiki-html`.
6. Build or publish the Quartz site so the page is hosted at `/interactives/<slug>/`.

## Evidence Rule

- Do not use web search or general web pages for scientific content.
- Use only local raw papers, local supplementary files, and maintained wiki pages that cite those files.
- External websites may be inspected only for visual/layout inspiration or publishing mechanics.
- If a value is missing from the available papers, keep it missing and document the gap.

## Active Projects

- `multiomics-proteomics-ptm-identification/`: recent-10-year multi-omics studies comparing protein, phosphoprotein, and acetylprotein identification counts, MS methods, and instruments.
