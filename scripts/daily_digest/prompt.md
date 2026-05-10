You are running the daily 한미암 paper digest task.

## Inputs

1. `/tmp/digest_today.json` — JSON with this schema:
   ```
   {
     "mode": "phase_b" | "phase_a_fallback",
     "date": "YYYY-MM-DD",
     "candidates": [...],   // from fetch_new_papers.py (when mode=phase_b)
     "selected":   [...]    // from select_papers.py (when mode=phase_a_fallback)
   }
   ```

2. `wiki/_meta/han-mi-am-project-context.md` — also appended to your system
   prompt. Use it to write the "활용 가능성" sections.

3. `wiki/_meta/slack-posted.json` — current state (slugs + pmids + history).

## Mode A: phase_b — new papers from PubMed

Each `candidates[i]` has: `pmid`, `slug`, `title`, `authors`, `year`, `journal`,
`doi`, `pmcid`, `pdf_path`, `full_text` (~30K chars).

For each candidate, judge against the 한미암 tier rubric in the system prompt.

1. **Relevance assessment** (DO NOT skip this step). Read `full_text` and decide tier:
   - **Tier 1**: phosphoproteome × drug response/resistance × cancer (직접 핵심)
   - **Tier 2**: pQTL/proteogenomics+WGS, neoantigen+WGS, CPTAC cohort,
                 targeted therapy resistance mechanism, immunotherapy resistance
   - **Tier 3**: WGS SV in cancer, noncoding driver, tumor heterogeneity,
                 PTM crosstalk, AI drug response prediction
   - **Tier 0 (skip)**: animal/cell-line only (no human clinical data),
                        non-cancer disease, weak relevance

2. **Pick top 1-2** with Tier ≥ 2. Prefer Tier 1 over Tier 2 over Tier 3.
   - If 0 candidates reach Tier 2: fall back to phase_a backlog (run
     `python3 scripts/daily_digest/select_papers.py` and use its top 2).
   - If exactly 1 reaches Tier 2: post that 1 + 1 backlog from select_papers.py.
   - If 2+ reach Tier 2: post the top 2.

3. **Compose ONE single Slack message** containing both papers. The full
   message must follow this structure exactly (use literal newlines):

   ```
   *:books: 오늘의 참고 논문 (<YYYY-MM-DD>)*

   한미암 프로젝트 관련 proteogenomics × 항암제 반응성 논문 <N>편을 공유드립니다.

   *<https://doi.org/<DOI1>|<FirstAuthor1> <Year1>, <Journal1>>*
   <3-4문장 본문, formal Korean (~합니다/~입니다)>. 한미암 프로젝트 관점에서, <활용 가능성 1-2문장: 본 과제의 어느 단계에 어떻게 들어갈지>.

   *<https://doi.org/<DOI2>|<FirstAuthor2> <Year2>, <Journal2>>*
   <같은 형식의 본문 + 활용 가능성>.
   ```

   Formatting rules:
   - **The bold-with-link line is the citation header**, e.g. `*<https://doi.org/10.1016/j.xcrm.2025.102255|Holt 2025, Cell Reports Medicine>*`. The full hyperlink anchor text is `Author Year, Journal`. **Do NOT** add a separate "논문 사이트" link at the end.
   - **Journal name**: use the frontmatter `journal:` value but strip parenthetical location info (e.g., `Advanced science (Weinheim, Baden-Wurttemberg, Germany)` → `Advanced Science`). For long names, common short forms are OK: `Cell reports. Medicine` → `Cell Rep Med`, `Nature communications` → `Nat Commun`, `Cancer Discovery` → `Cancer Discovery`.
   - **Body length**: 3-4 sentences (2-3 for what/results, 1-2 for 한미암 활용 가능성). Keep readable; avoid stuffing every detail.
   - **Activation phrase for relevance**: start the relevance sentence with `한미암 프로젝트 관점에서,` or `한미암 과제의 ___단계에서,` so it's visually distinguishable.
   - **Mid-sentence emphasis**: bold key methods/findings with `*...*` sparingly (1-2 per paper) for scannability — e.g. *phosphoproteome 통합 분석*, *GSK3B-S9 인산화*.
   - **Tone**: formal but readable; ~합니다 / ~입니다. Avoid translating English technical terms unnecessarily (proteogenomics, phosphoproteome, neoantigen 등은 그대로).
   - **Do NOT invent results**. If `full_text` (Phase B) or wiki Summary/Key Points (Phase A) doesn't say it, don't claim it.

4. **Post to Slack** via `slack` MCP tool — single `chat_postMessage` call to
   channel `C0B2RQ97Y3U` with the entire composed text in `text` field.
   Confirm the response has `ok: true`. If failure, retry once.

5. **Add to wiki/sources** for each posted NEW paper:
   - Read the existing wiki source page if it exists at `wiki/sources/<slug>.md`,
     otherwise create one with this template:
     ```
     ---
     title: "<title>"
     authors:
       - "<first author last name>"
     year: <year>
     journal: "<journal>"
     doi: "<doi>"
     pmid: "<pmid>"
     pmcid: "<pmcid or empty>"
     paper_kind: research
     pdf: "<pdf_path>"
     topic: cancer-multiomics
     tags:
       - "cancer-multiomics"
       - "phosphoproteomics"  # adjust based on content
     themes:
       - "<theme>"
     ---
     # <title>

     _<journal>, <year>._ PMID: [<pmid>](https://pubmed.ncbi.nlm.nih.gov/<pmid>/).

     DOI: [<doi>](https://doi.org/<doi>)

     ## Summary
     <2-4 sentence Korean summary of what was done and found, based on full_text>

     ## Key Points
     - <bullet 1>
     - <bullet 2>
     - <bullet 3>

     ## 한미암 활용 가능성
     <2-3 sentences: which phase of the project this connects to>

     ## Sources
     - Local PDF: `<pdf_path>`
     - PubMed: <https://pubmed.ncbi.nlm.nih.gov/<pmid>/>
     - DOI: <https://doi.org/<doi>>
     ```

6. **Update slack-posted.json**: append posted PMIDs to `pmids[]`, slugs to
   `slugs[]`, and add a history entry. Preserve existing entries.

## Mode B: phase_a_fallback — backlog only

If mode is `phase_a_fallback` (PubMed yielded 0 valid new papers OR all skipped):
- Use `selected` array directly (already 2 papers from select_papers.py).
- Read each wiki source path, format Slack post per template (skip Tier
  judgment — already curated by user).
- Post to Slack, update slack-posted.json.

## Failure handling

- If a Slack post fails (MCP error), do NOT add that paper to slack-posted.json.
  Print error to stderr and continue with the other.
- If wiki source ingestion fails for a posted paper, that's OK — log and
  continue. Posting succeeded, that's what matters.
- If both papers fail, exit with non-zero status.

## Output

When done, print a one-line summary to stdout:
```
DONE: posted N papers (pmids: ...). Updated slack-posted.json.
```
