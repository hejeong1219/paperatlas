# LLM Wiki

Personal knowledge base scaffold based on Andrej Karpathy's "LLM Wiki" idea.

This repository separates:

- `raw/`: immutable source material
- `wiki/`: LLM-maintained markdown knowledge base
- `wiki_html/`: Quartz-based publish layer for GitHub Pages
- `AGENTS.md`: operating schema for Codex and future agent sessions

## Directory layout

- `raw/inbox/`: drop new sources here before ingest
- `raw/inbox/papers/`: downloaded papers named with the shared PDF/MD basename convention
- `raw/processed/`: optional archive for sources that have been ingested
- `raw/assets/`: downloaded images and attachments referenced by sources
- `wiki/sources/`: one page per ingested source
- `wiki/entities/`: people, orgs, tools, places, papers, products
- `wiki/concepts/`: recurring ideas, themes, methods, frameworks
- `wiki/analyses/`: comparison pages, Q&A outputs, focused investigations
- `wiki/syntheses/`: higher-level overviews and evolving theses
- `wiki/_meta/`: navigation and maintenance files
- `wiki_html/`: static site generator config, build scripts, and generated HTML

## Start here

1. Put a source document into `raw/inbox/`.
2. Ask Codex to ingest it into the wiki.
3. Review the updated pages in `wiki/`.
4. Ask follow-up questions and file useful answers back into the wiki.

For papers, use:

- `firstauthor-year-five-key-words.pdf`
- matching `wiki/sources/firstauthor-year-five-key-words.md`

## Core files

- [`AGENTS.md`](./AGENTS.md): wiki maintenance rules and workflows
- [`wiki/_meta/index.md`](./wiki/_meta/index.md): catalog of wiki pages
- [`wiki/_meta/log.md`](./wiki/_meta/log.md): append-only activity log
- [`wiki/syntheses/overview.md`](./wiki/syntheses/overview.md): evolving overview of the entire knowledge base
- [`bin/qmd`](./bin/qmd): repo-local wrapper for QMD search and retrieval

## Search

Use QMD instead of plain recursive grep for wiki lookup:

- `./bin/qmd search "neoantigen pipeline" -c llm-wiki`
- `./bin/qmd vsearch "neoantigen pipeline B cell TLS" -c llm-wiki`
- `./bin/qmd query "Which papers connect neoantigen pipelines with B-cell and TLS biology?" -c llm-wiki`
- `./bin/qmd get qmd://llm-wiki/wiki/concepts/neoantigen-discovery-pipelines.md`
- `./bin/qmd status`

`./bin/qmd` keeps QMD's cache and config inside this repository so it works reliably in this workspace.

Notes:

- `search` is the default mode and should be your first choice.
- `vsearch` and `query` are optional and are much slower on CPU-only machines.
- The first `embed` and first `query` run download local model files into `.cache/qmd/models/`.

## Publishing

`wiki/` is the source of truth. `wiki_html/` is a Quartz publish layer that turns `wiki/` into a GitHub Pages site.

- Sync content: `./bin/sync-wiki-html`
- Preview locally: `cd wiki_html && npm run serve:wiki`
- Production build: `cd wiki_html && npm run build:wiki`

The sync step copies `wiki/` into `wiki_html/content/` and excludes internal `_meta/` files from the public site.

## Suggested workflow

Use Obsidian, any markdown editor, or git tooling on top of this repo. The raw sources stay untouched; the wiki layer accumulates summaries, links, contradictions, and synthesis over time.
