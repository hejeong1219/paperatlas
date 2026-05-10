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

3. **Compose Slack messages** (formal Korean, ~합니다/~입니다 tone) using template:
   ```
   *<FirstAuthor> <Year>* — *<핵심 메서드/플랫폼/대상>*로 <무엇을 했는지 한 문장>. <구체 결과 1-2문장>. 한미암 프로젝트 관점에서, <활용 가능성, 본 과제의 어느 단계에 어떻게 들어갈지 1-2문장>. <https://doi.org/<DOI>|논문 사이트>
   ```

   Constraints:
   - Length: 3-5 문장 total per paper.
   - "활용 가능성" must reference a SPECIFIC phase (1차 내성 분석, 2차 내성 분석, 신생항원 파이프라인, AI 예측 모형, 데이터 전처리, ppQTL 분석 등).
   - DO NOT invent results. If `full_text` doesn't say it, don't claim it.
   - English author/journal/method names stay English.
   - Use `<URL|논문 사이트>` for the link (Slack mrkdwn link syntax).

4. **Post to Slack** via `slack` MCP tool. Channel: `C0B2RQ97Y3U`. Send each
   paper as a separate message (not threaded). Confirm each post returned `ok`.

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
