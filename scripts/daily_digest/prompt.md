You are running the daily 한미암 paper digest task. Today's job is to post 2 paper summaries to Slack channel `C0B2RQ97Y3U` (#한미암_관련논문).

## Inputs you can read

1. `/tmp/digest_today.json` — output of `select_papers.py`, contains 2 selected backlog papers with metadata and source path.
2. The wiki source markdown files at the paths inside that JSON (under `wiki/sources/`). Each contains the user's hand-written `## Summary` and `## Key Points` sections — these are based on full PDF reading, so you can trust them as primary content.
3. `wiki/_meta/han-mi-am-project-context.md` — the project context describing what 한미암 project is about and how to write the "활용 가능성" section. This is also appended as your system prompt — use it.

## Task

For each of the 2 selected papers:

1. Read the wiki source file (path is in `selected[i].path` — relative to repo root).
2. Extract: first author last name, year, journal, DOI, title, Summary, Key Points.
3. Compose a Slack message in **Korean, formal reporting tone** (격식 있는 보고체, ~합니다/~입니다), addressing professors who do not code. Follow this template **exactly**:

```
*<FirstAuthor> <Year>* — *<핵심 메서드/플랫폼/대상>*로 <무엇을 했는지 한 문장>. <구체 결과 1-2문장>. 한미암 프로젝트 관점에서, <활용 가능성 1-2문장>. <https://doi.org/<DOI>|논문 사이트>
```

Length: 3-5 sentences total. The "활용 가능성" must reference a *specific* phase of the 한미암 project (1차/2차 내성 분석, 신생항원 파이프라인, AI 예측 모형, 데이터 전처리, ppQTL 분석 등) — don't write generic platitudes.

4. Post each message to Slack using the `slack` MCP server. Use the tool to send to channel `C0B2RQ97Y3U`. Send the two messages as separate posts (not threaded).

5. After both posts succeed, update `wiki/_meta/slack-posted.json`:
   - Append both slugs to the `slugs` array.
   - Append a new entry to `history`: `{"date": "<YYYY-MM-DD>", "slugs": ["<slug1>", "<slug2>"]}`.
   - Preserve existing entries; do NOT overwrite the file from scratch.

## Failure handling

- If a Slack post fails (MCP error), do NOT update `slack-posted.json` for that paper. Print the error to stderr.
- If a wiki source file is missing or malformed, skip it and continue with the other.
- If both fail, exit with non-zero status.

## Important constraints

- Do NOT invent results. If the wiki source's Summary/Key Points don't say something, don't claim it.
- Do NOT use English-only summaries. Korean is required.
- Do NOT post abstract-level fluff. The "활용 가능성" must be concrete.
- The DOI in the link must come from the source's frontmatter `doi:` field. If missing, link to the PMID instead: `https://pubmed.ncbi.nlm.nih.gov/<PMID>/`.
- The `*...*` markdown produces bold in Slack. Keep them literal in the post.
