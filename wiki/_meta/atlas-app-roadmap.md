# Atlas App Roadmap

This document defines how the current Quartz-based public wiki can evolve toward a more app-like paper atlas similar in feel to `paperatlas`.

## Target Experience

The public site should feel less like a file browser and more like a navigable research atlas:

- paper cards instead of only text lists
- filter-first exploration
- landing pages by cancer type
- landing pages by journal
- stronger related-paper discovery
- visible topic clusters and network structure

## Phase 1: Structured Metadata

Goal: normalize source pages so the site can reason about papers as records.

Required work:

- add consistent paper frontmatter
- normalize journals
- normalize cancer types
- normalize modality labels
- normalize paper kinds

Outcome:

- enough structure to build cards and filters without brittle regex parsing

## Phase 2: Atlas Navigation Layer

Goal: create atlas entry points that feel curated instead of filesystem-driven.

Pages to add:

- `/papers` or `/sources` card overview
- `/cancers`
- `/journals`
- `/modalities`
- `/themes`

Each landing page should include:

- short intro
- card grid or grouped list
- counts
- links to related collections

## Phase 3: Paper Cards

Goal: replace plain file listings with compact paper summaries.

Card fields:

- title
- year
- journal
- first author or author string
- cancer type chips
- modality chips
- paper kind badge
- one-line summary

Implementation options:

- Quartz custom component that reads frontmatter
- generated markdown index pages if we want a lower-complexity path first

Recommended path:

- start with generated markdown index pages
- move to a custom Quartz component after metadata stabilizes

## Phase 4: Filtering

Goal: make the site feel app-like.

Desired filters:

- cancer type
- journal
- year
- modality
- paper kind
- theme

Implementation options:

- Quartz tags only: fastest, but limited and noisy
- generated filtered pages: simple and static
- client-side filter UI backed by `contentIndex.json`: most app-like

Recommended path:

1. generated filtered pages first
2. client-side filter UI second

## Phase 5: Connectivity

Goal: make related papers discoverable beyond direct markdown links.

Relationship types:

- shared cancer type
- shared modality
- shared journal
- same paper kind
- shared concept page links
- shared analysis membership

Display surfaces:

- graph view
- related papers side panel
- "you may also want" card strip on paper pages

## Phase 6: Journal and Cancer Pages

Goal: introduce domain-relevant navigation rather than generic folders.

Examples:

- `/cancers/melanoma`
- `/cancers/hepatocellular-carcinoma`
- `/journals/nature-medicine`
- `/journals/nature-biotechnology`

Each page should include:

- short description
- included papers
- adjacent concepts
- adjacent analyses

## Phase 7: Optional App Enhancements

Possible later additions:

- client-side sorting by year or journal
- saved URL-based filters
- citation export links
- DOI and PubMed links in card views
- mini stats widgets
- timeline views

## Design Constraints

- `wiki/` remains the source of truth
- `wiki_html/` remains the publish layer
- raw PDFs stay out of the public site unless intentionally linked
- prefer static generation first, richer client-side behavior second

## Recommended Next Implementation Steps

1. backfill frontmatter for the current 10-paper corpus
2. create generated `cancers/` and `journals/` landing pages
3. add a paper-card listing page for all source papers
4. add a lightweight client-side filter bar after the metadata is stable
