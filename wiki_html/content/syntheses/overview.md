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

- Repository scaffold is in place and now supports four public research tracks.
- **B-cell Neoantigen** covers neoantigen discovery, immunopeptidomics, B-cell/TLS biology, and antigen-specific immune context.
- **Cancer Resistance / Immune Evasion** covers immune visibility, access, effector dysfunction, antigen loss, lineage switch, checkpoint/CAR/BsAb resistance, and therapy escape frameworks.
- **ptmanchor** covers PTM correction, phosphosite interpretation, protein-abundance confounding, and kinase activity inference.
- **Cancer Multiomics / Drug-response Monitor** is the cross-cutting acquisition layer for WGS/SNV/CNA + global proteome + phosphoproteome + drug-response papers. It feeds the three main research tracks rather than replacing them.
- The schema favors source summaries, entity pages, concept pages, analyses, and higher-level syntheses.

## Operating Model

- Raw documents live in `raw/` and remain immutable.
- The wiki in `wiki/` is maintained by the LLM agent.
- Navigation and change history live in `wiki/_meta/index.md` and `wiki/_meta/log.md`.

## Next Steps

- Continue question-driven wiki expansion through the 100-question sprint.
- Promote newly downloaded drug-response phosphoproteomics papers from source stubs to full PDF-backed notes.
- De-duplicate newly acquired papers against existing canonical source pages before counting them toward target corpora.
- Keep public pages updated through the Quartz sync/publish workflow.

## Connections

- [LLM Wiki](../concepts/llm-wiki.md)
- [B-Cell Neoantigen Pipeline in Human Cancer](../analyses/b-cell-neoantigen-pipeline-human-cancer-corpus.md)
- [Neoantigen Discovery Pipelines](../concepts/neoantigen-discovery-pipelines.md)
- [B Cells and Tertiary Lymphoid Structures](../concepts/b-cells-and-tertiary-lymphoid-structures.md)
- [Cancer Multiomics Literature Monitor](../topics/cancer-multiomics-literature.md)
- [Drug Response Proof-of-Concept with Global Proteome, Phosphoproteome, and Somatic SNV](../analyses/drug-response-poc-global-phospho-somatic-snv.md)
- [Drug Response Phospho-Global Proteomics Corpus Queue](../analyses/drug-response-phospho-global-100-corpus-queue.md)

## Sources

- Internal repository framing and ingested paper corpus.
