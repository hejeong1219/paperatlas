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
   message must follow this 3-line-per-paper structure exactly (literal newlines):

   ```
   *:books: 오늘의 참고 논문 (<YYYY-MM-DD>)*

   <인트로 1문장 — 아래 풀에서 하나 골라 사용; 매일 동일하지 않게 적당히 다양화>

   *<https://doi.org/<DOI1>|<FirstAuthor1> <Year1>, <Journal1>>*
   <Line 1: 무엇을 했는지 + 핵심 결과 1-2문장 (compact, formal Korean ~합니다/~입니다)>
   <Line 2: 한미암 활용 1문장 — 시사·참고 톤 종결>

   *<https://doi.org/<DOI2>|<FirstAuthor2> <Year2>, <Journal2>>*
   <같은 3줄 구조>
   ```

   ### 톤 가이드 — 매우 중요

   청중은 한미암 과제의 **임상·기초 교수진**. 이 디지스트는 "이걸 보고 당장 적용하세요"가 아니라
   **"이런 각도/사례도 있더라"고 연구자 시야를 넓혀드리는 큐레이션**의 성격. 따라서:

   - **명령·지시 어조 금지**: "활용 가능합니다", "사용해야 합니다", "적용해야 합니다", "적용 가능합니다" → 부담스러움
   - **가능성·시사·참고 어조 권장**: "~참고해볼 수 있겠습니다", "~사료됩니다", "~시사합니다", "~보입니다"
   - **정중하고 상냥하게** ~합니다 / ~입니다 / ~보입니다 / ~사료됩니다. 너무 딱딱하지 않게.
   - 영어 기술 용어는 그대로 (proteogenomics, phosphoproteome, neoantigen, ppQTL 등 번역 X)

   ### 인트로 라인 풀 (매일 하나 선택, 적당히 변주)

   ⚠️ **봇이 자동 큐레이션해서 전달하는 디지스트**입니다. **"살펴보았습니다", "정리해보았습니다",
   "추려보았습니다", "모아보았습니다", "읽어보았습니다"** 같이 *사람이 직접 검토했다는 인상을
   주는 동사는 절대 사용 금지*. 봇이 자동으로 가져왔다는 톤을 유지하세요.

   - `단백유전체 및 항암제 반응성 분야의 최근 논문 N편입니다.`
   - `다음은 proteogenomics × 항암제 반응성 주제의 최근 논문 N편입니다.`
   - `오늘의 디지스트 — 단백유전체·항암제 반응성 분야 N편을 공유드립니다.`
   - `proteogenomics × 항암제 반응성 영역에서 큐레이션된 N편의 논문입니다.`
   - `오늘의 참고 논문 — 단백유전체 및 항암제 반응성 주제 N편입니다.`
   - `PubMed 최신 proteogenomics·phosphoproteome 논문 N편을 안내드립니다.`
   - `단백유전체·항암제 반응성 분야 큐레이션 N편입니다.`
   - `오늘의 큐레이션: proteogenomics × 항암제 반응성 분야 N편을 공유드립니다.`

   해당 날짜의 논문 주제(예: 신생항원 위주, ppQTL 위주, 임상 trial 위주)에 맞게 단어 살짝 조정해도 됨.
   단, 위의 사람-주체 동사는 절대 X.

   Formatting rules:

   - **3 lines per paper, separated by single newline**. Empty line BETWEEN papers (between paper 1's 활용 line and paper 2's citation header).
   - **Citation header is the hyperlink anchor**: `*<URL|Author Year, Journal>*`. Bold works here because line-start is a word boundary in Slack mrkdwn. Do NOT add separate "논문 사이트" link at end.
   - **NO mid-sentence bold (`*...*`) in Korean text**. Slack mrkdwn does NOT recognize `*` as bold when adjacent to Korean characters (e.g. `이러한 *PCSK9 표적 제거*는` shows literal asterisks). Bold ONLY in citation header. For emphasis on English technical terms, leave them plain or in backticks `PCSK9`.
   - **Journal name**: strip parenthetical location (`Advanced science (Weinheim,...)` → `Advanced Science`). Use common abbreviations for long names: `Cell reports. Medicine` → `Cell Rep Med`, `Nature communications` → `Nat Commun`, `Journal of Clinical Oncology` → `J Clin Oncol`.
   - **Total body length per paper**: 2-3 sentences max across the two body lines combined. Keep COMPACT. The example below is the target verbosity:

     ```
     *<.../102255|Holt 2025, Cell Rep Med>*
     근육침윤성 방광암 환자 종양 60건의 proteogenomics-phosphoproteomics 통합 분석으로, ATAD1 isoform과 GSK3B-S9 인산화 매개 Wnt/JAK-STAT 경로가 화학요법 내성 극복의 잠재 표적으로 제시됩니다.
     한미암 과제의 1차 내성 인산화단백체–WGS 통합 분석 단계에서, 환자 층화·표적 도출 파이프라인 설계 시 참고해볼 수 있는 레퍼런스로 보입니다.
     ```

   - **활용 line**: 항상 `한미암 과제의 ___단계에서,` 또는 `한미암 프로젝트 관점에서,` 로 시작. 본 과제 SPECIFIC 단계 (1차 내성 분석, 2차 획득 내성 분석, 신생항원 파이프라인, AI 예측 모형, 데이터 전처리, ppQTL 분석, 인산화단백체 파이프라인 구축 중 하나)에 매핑.

   - **활용 line의 종결어 — 톤 매우 중요**. "활용 가능합니다", "사용해야 합니다", "적용해야 합니다" 등 **단정·지시형 종결 절대 금지**. 청중이 임상·기초 교수님이라 "당장 해봐"로 읽힐 수 있음. **가능성·시사·참고 톤**으로 마무리하세요. 권장 종결 패턴:
     * `~참고해볼 수 있는 레퍼런스로 보입니다.`
     * `~검토해볼 만한 자료로 사료됩니다.`
     * `~시사점을 줄 수 있을 것으로 보입니다.`
     * `~고민해볼 가치가 있어 보입니다.`
     * `~생각해볼 만한 분석 축이 될 수 있겠습니다.`
     * `~참고할 만한 사례로 보입니다.`
     * `~방향성을 시사합니다.`
     같은 표현을 매일 반복하지 말고 적절히 다양화.
   - **Tone**: formal but readable; ~합니다 / ~입니다. Avoid translating English technical terms (proteogenomics, phosphoproteome, neoantigen 그대로).
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
