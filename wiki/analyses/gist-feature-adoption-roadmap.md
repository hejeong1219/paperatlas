---
title: Gist Feature Adoption Roadmap
tags:
  - analysis
  - workflow
  - atlas
themes:
  - knowledge-system
  - ingest-pipeline
  - publishing
---

# Gist Feature Adoption Roadmap

Working roadmap for adapting the collaborator-guide gist workflow into this repository's wiki, ingest, and publish stack.

## Key Points

- The reference gist describes a three-tier knowledge workflow: immutable PDFs, structured source summaries, and higher-order wiki synthesis pages. This repository already follows that logic in `raw/`, `wiki/sources/`, and topic or concept or analysis pages, so the next step is to tighten consistency rather than rebuild from zero.
- The most important adoption target is not a single script but a mode of growth: each new paper should reinforce a topic tree, expand a concept network, and connect back to active manuscript or proposal anchors when relevant.
- The Quartz site should increasingly expose topics as first-class atlas objects, closer to a paper-atlas experience than a flat note dump.

## What Is Already In Place

- Immutable local paper storage under `raw/inbox/papers/` with matched source-page basenames.
- Deep `wiki/sources/` ingest tied into topic and concept pages.
- Curated topic hubs such as [B-Cell Neoantigen Research Map](../topics/b-cell-neoantigen-human-cancer.md) and [Immunotherapy Resistance and Immune Evasion](../topics/immunotherapy-resistance-and-immune-evasion.md).
- Manuscript and proposal anchors that allow paper-to-project relevance mapping:
  - [B-Cell Neoantigen Proposal Anchor](./b-cell-neoantigen-proposal-anchor.md)
  - [Cancer Resistance Manuscript Anchor](./cancer-resistance-manuscript-anchor.md)
  - [ptmanchor Manuscript Anchor](./ptmanchor-manuscript-anchor.md)
- Quartz publish layer with sync and GitHub Pages workflow.
- QMD-first search rules embedded in repository operations.

## What Should Be Built Next

- Topic-first connectivity pages so each major subject has its own visible paper and concept map rather than relying mainly on the homepage graph.
- Stronger per-paper relevance signals to active manuscripts and proposals.
- More standardized source-page sections when batch-ingesting large corpora.
- Better overnight automation reporting so each run leaves a compact build trail in the log and trackers.
- Public HTML navigation that makes the difference between papers, concepts, analyses, and live project anchors obvious to outside viewers.

## Connections

- [LLM Wiki](../concepts/llm-wiki.md)
- [B-Cell Neoantigen Research Map](../topics/b-cell-neoantigen-human-cancer.md)
- [Immunotherapy Resistance and Immune Evasion](../topics/immunotherapy-resistance-and-immune-evasion.md)
- [PTM Correction and Kinase Signaling in Cancer Proteomics](../topics/ptm-correction-and-kinase-signaling-in-cancer-proteomics.md)

## Sources

- Reference workflow gist: [LLM Wiki: AI for Biology -- Collaborator Guide](https://gist.github.com/joonan30/cbce305684d079dbe9a3fbaefe4e3959)
