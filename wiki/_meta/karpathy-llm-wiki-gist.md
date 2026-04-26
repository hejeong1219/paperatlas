---
title: Andrej Karpathy - LLM Wiki Gist
authors:
  - "Andrej Karpathy"
year: 2026
journal: "GitHub Gist"
url: "https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f"
paper_kind: resource
cancer_types:
  - pan-cancer
modalities:
  - knowledge-base
themes:
  - llm-wiki
  - workflow
tags:
  - meta
  - llm-wiki
  - workflow
---

# Andrej Karpathy - LLM Wiki Gist

High-level proposal for maintaining a personal or team knowledge base as a persistent markdown wiki curated by an LLM rather than a retrieval-only document system.

## Key Points

- The core artifact is a maintained wiki, not a one-shot answer over retrieved chunks.
- New sources should be integrated into existing pages and syntheses, not merely indexed.
- The system is organized around three layers: raw sources, wiki pages, and an agent schema file.
- Two navigation files are central: a content-oriented index and a chronological log.
- Query outputs can themselves become durable wiki pages.
- Periodic linting helps surface contradictions, orphan pages, stale claims, and missing concepts.

## Notes

- This source is intentionally abstract and implementation-agnostic.
- It recommends starting simple with markdown files and optional local tooling later.
- Obsidian is suggested as a practical interface for browsing the wiki.

## Connections

- [LLM Wiki](../concepts/llm-wiki.md)
- [Overview](../syntheses/overview.md)

## Sources

- Original gist: [llm-wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
