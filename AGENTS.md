# LLM Wiki Operating Schema

This repository is a persistent markdown wiki maintained primarily by an LLM agent. The goal is not simple retrieval from raw documents, but cumulative knowledge compilation into a structured, interlinked wiki.

## Mission

Maintain a high-signal, low-duplication markdown wiki that sits between the user and raw source material.

The agent should:

- read raw sources
- extract key claims, entities, concepts, timelines, and tensions
- update existing wiki pages instead of creating redundant ones
- preserve uncertainty and disagreement explicitly
- maintain cross-links between related pages
- keep navigation files current
- treat the raw layer as immutable

## Repository contract

There are three layers:

1. `raw/`: source of truth, never edited by the agent except for optional file moves from `raw/inbox/` to `raw/processed/` when the user wants archival organization.
2. `wiki/`: LLM-authored markdown pages that summarize, synthesize, compare, and connect information.
3. `wiki_html/`: Quartz-based publish layer that renders `wiki/` into static HTML for GitHub Pages.
4. `AGENTS.md`: this operating schema, which governs structure and workflow.

## Directory conventions

- `wiki/sources/`: source summaries, one page per ingested source
- `wiki/entities/`: people, organizations, projects, tools, products, places, named systems
- `wiki/topics/`: curated topic hubs that group papers, concepts, analyses, and syntheses around a reusable research subject
- `wiki/concepts/`: recurring ideas, methods, themes, arguments, frameworks
- `wiki/analyses/`: user-driven analyses, comparisons, Q&A outputs worth preserving
- `wiki/syntheses/`: top-level overviews, theses, and long-running summaries
- `wiki/_meta/index.md`: authoritative page catalog
- `wiki/_meta/log.md`: append-only operational log
- `wiki_html/content/`: synchronized copy of `wiki/` used for public publishing
- `wiki_html/public/`: generated static site output, never edited by hand

Create new top-level categories only when the current structure becomes insufficient.

## Naming

- Prefer lowercase kebab-case filenames.
- Use descriptive, stable names.
- For papers, use the same basename for the raw PDF and the wiki source page.
- Default paper basename format: `firstauthor-year-five-key-words`.
- Example: `huber-2025-comprehensive-proteogenomic-pipeline-neoantigen-discovery.pdf` and `huber-2025-comprehensive-proteogenomic-pipeline-neoantigen-discovery.md`.
- Match page titles to their subject in readable title case.

## Markdown conventions

Each wiki page should usually contain:

1. A level-1 title.
2. A short summary sentence or paragraph near the top.
3. A `## Key Points` section for distilled facts and claims.
4. A `## Connections` section linking related wiki pages.
5. A `## Sources` section listing supporting raw sources or source pages.

Optional sections:

- `## Open Questions`
- `## Timeline`
- `## Contradictions / Tensions`
- `## Quotes`
- `## Notes`

Keep pages concise, but not skeletal. Prefer updating an existing page over creating a near-duplicate.

## Source page frontmatter

For pages in `wiki/sources/`, prefer adding structured frontmatter whenever the information is available.

Minimum preferred fields:

- `title`
- `year`
- `journal`
- `paper_kind`
- `cancer_types`
- `modalities`
- `themes`
- `tags`

Use the conventions in `wiki/_meta/paper-frontmatter-schema.md` and favor stable, reusable controlled values over ad hoc labels.

## Citation conventions

- Link first to the relevant `wiki/sources/` page.
- When useful, also mention the raw file path in backticks.
- Distinguish observed facts from inferred synthesis.
- If sources disagree, keep both views and label the conflict.

## Ingest workflow

When the user asks to ingest a source:

1. Read the new source from `raw/inbox/` or another specified path.
2. Identify major entities, concepts, claims, timelines, and evidence.
3. Create or update a page in `wiki/sources/` for that source.
4. Add or refine structured frontmatter for source pages whenever the information is available.
5. Update related topic, entity, concept, analysis, and synthesis pages.
6. Update `wiki/_meta/index.md`.
7. Append an entry to `wiki/_meta/log.md`.
8. Preserve uncertainty, ambiguity, and contradictions explicitly.

Do not silently overwrite stronger existing synthesis with weaker new evidence.

## Query workflow

When the user asks a question:

1. Read `wiki/_meta/index.md` first.
2. Open the most relevant wiki pages.
3. Synthesize an answer from the existing wiki.
4. If the answer creates durable value, offer to save it as a new or updated page in `wiki/analyses/` or `wiki/syntheses/`.
5. Log substantial filed outputs in `wiki/_meta/log.md`.

## Lint workflow

When asked to lint or health-check the wiki:

- find orphan pages
- detect stale claims
- identify missing links
- surface duplicate pages
- note unresolved contradictions
- suggest promising new source gaps

Record meaningful maintenance passes in the log.

## Editing rules

- Never modify raw source contents unless the user explicitly asks.
- Avoid duplicating the same claim across many pages if one canonical page can hold it.
- Keep cross-links dense enough for navigation, but not noisy.
- Prefer incremental edits to full rewrites.
- Preserve useful existing structure unless there is a clear improvement.
- Treat `wiki/` as the only source of truth for public content.
- Do not manually edit `wiki_html/content/` unless the change is part of the sync or publishing pipeline itself.
- Do not manually edit `wiki_html/public/`; rebuild it from Quartz instead.

## Publishing workflow

When the user asks to publish or update the site:

1. Update or create content in `wiki/`.
2. Run `./bin/sync-wiki-html` to copy public markdown into `wiki_html/content/`.
3. Build or serve Quartz from `wiki_html/`.
4. Keep `wiki/_meta/` and `raw/` out of the public site unless explicitly requested.
5. Record meaningful publishing setup changes in `wiki/_meta/log.md`.

## Index format

`wiki/_meta/index.md` is the navigation spine for the repo. Keep entries grouped by category. Each entry should include:

- page link
- one-line summary
- optional source count or status note

## Log format

Append entries to `wiki/_meta/log.md` using:

`## [YYYY-MM-DD] operation | title`

Then include short bullets describing what changed.

## Default assumptions

- This repo is optimized for markdown-first local workflows.
- Obsidian compatibility is desirable but not required.
- Search begins with the index file, then uses `./bin/qmd` for repo-wide retrieval.

## Search rules

- Do not default to `grep`, `find`, or raw recursive scans for wiki content lookup when `qmd` can answer the question.
- For wiki search in this repository, default to `./bin/qmd search "<terms>"` for fast lexical retrieval.
- Use `./bin/qmd query "<question>"` only when lexical search is insufficient or the user explicitly wants deeper semantic retrieval.
- Use `./bin/qmd vsearch "<terms>"` only when semantic similarity is specifically helpful and the extra latency is acceptable.
- Use `./bin/qmd get <path-or-docid>` to open the matched document after search.
- Fall back to `rg` only for non-markdown codebase tasks, tool debugging, or when `qmd` is unavailable.
- If the user says "search" or asks a wiki question, interpret that as "run `qmd search` first."

## First-run priority

If the repo is mostly empty, establish the base structure, seed the meta files, and create an initial overview page before ingesting any sources.
