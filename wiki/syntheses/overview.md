---
title: Overview
tags:
  - overview
  - synthesis
  - atlas
---

# Overview

This wiki is a persistent knowledge base intended to accumulate structured understanding over time rather than re-derive it from raw documents on every query.

## Current Scope

- Repository scaffold is in place.
- The initial neoantigen and B-cell/TLS corpus has been ingested.
- A second corpus focused on immunotherapy resistance and immune evasion has been added, spanning framework reviews, CAR-T escape, and bispecific antibody trials.
- The initial schema favors source summaries, entity pages, concept pages, analyses, and higher-level syntheses.

## Operating Model

- Raw documents live in `raw/` and remain immutable.
- The wiki in `wiki/` is maintained by the LLM agent.
- Navigation and change history live in `wiki/_meta/index.md` and `wiki/_meta/log.md`.

## Next Steps

- Add a first source to `raw/inbox/`.
- Ingest it into `wiki/sources/`.
- Update entity and concept pages as recurring topics emerge.
- Periodically lint for missing links, duplication, and stale claims.

## Connections

- [LLM Wiki](../concepts/llm-wiki.md)
- [B-Cell Neoantigen Pipeline in Human Cancer](../analyses/b-cell-neoantigen-pipeline-human-cancer-corpus.md)
- [Neoantigen Discovery Pipelines](../concepts/neoantigen-discovery-pipelines.md)
- [B Cells and Tertiary Lymphoid Structures](../concepts/b-cells-and-tertiary-lymphoid-structures.md)

## Sources

- Internal repository framing and ingested paper corpus.
