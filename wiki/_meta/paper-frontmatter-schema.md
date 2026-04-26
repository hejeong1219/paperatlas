# Paper Frontmatter Schema

Structured frontmatter is the foundation for making the public site feel more like an app than a plain markdown garden.

## Goal

Every paper page in `wiki/sources/` should gradually converge on a common schema so the publish layer can support:

- paper cards
- faceted filtering
- cancer-type landing pages
- journal landing pages
- modality-specific pages
- richer graph and related-paper suggestions

## Minimum Schema

Use this frontmatter for source pages whenever the information is available:

```yaml
---
title: "Paper title"
authors:
  - "First Author"
  - "Second Author"
year: 2025
journal: "Nature Medicine"
doi: "10.1038/..."
url: "https://..."
pdf: "raw/inbox/papers/file.pdf"
paper_kind: trial
cancer_types:
  - hepatocellular-carcinoma
modalities:
  - neoantigen-vaccine
  - checkpoint-blockade
themes:
  - neoantigen
  - clinical-trial
  - personalized-therapy
tags:
  - source
  - neoantigen
  - vaccine
---
```

## Recommended Controlled Fields

### `paper_kind`

Use one of:

- `trial`
- `translational`
- `mechanistic`
- `computational`
- `review`
- `resource`

### `cancer_types`

Prefer stable kebab-case values:

- `melanoma`
- `hepatocellular-carcinoma`
- `ovarian-cancer`
- `head-and-neck-cancer`
- `nasopharyngeal-carcinoma`
- `pan-cancer`
- `solid-tumors`

### `modalities`

Examples:

- `neoantigen-vaccine`
- `shared-neoantigen-vaccine`
- `adoptive-cell-therapy`
- `immunopeptidomics`
- `proteogenomics`
- `single-cell`
- `spatial-transcriptomics`
- `tls-biology`

### `themes`

Examples:

- `neoantigen`
- `b-cells`
- `tls`
- `pipeline`
- `tumor-microenvironment`
- `clinical-trial`
- `immunotherapy`

## Why Both `themes` and `tags`

- `themes` should be more semantically stable and power future filters.
- `tags` can remain broader and Quartz-friendly for lightweight browsing.

## App-Layer Implications

Once enough papers use this schema, the publish layer can generate:

- a paper card grid with author, year, journal, and topic chips
- filter bars for cancer type, journal, modality, and paper kind
- `/cancers/<slug>` pages
- `/journals/<slug>` pages
- `/modalities/<slug>` pages
- richer "related papers" panels based on overlapping metadata

## Migration Strategy

Do not block ingest on perfect metadata. Start with:

1. `title`
2. `year`
3. `journal`
4. `paper_kind`
5. at least one `cancer_types` value or `pan-cancer`
6. at least one `modalities` value

Then enrich older pages incrementally.
