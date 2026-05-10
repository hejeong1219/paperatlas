You are running the daily 한미암 paper digest task.

## Inputs

1. `/tmp/digest_today.json` — JSON with this schema:
   ```
   {
     "mode": "phase_b",
     "date": "YYYY-MM-DD",
     "candidates": [...]   // from fetch_new_papers.py — full PDF text included
   }
   ```
   (Phase A backlog mode disabled per user policy: no posting on days with 0 fresh PubMed candidates.)

2. `wiki/_meta/han-mi-am-project-context.md` — also appended to your system
   prompt. Use it to write the "활용 가능성" sections.

3. `wiki/_meta/slack-posted.json` — current state (slugs + pmids + history).

## Phase B — new papers from PubMed (the only mode)

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
   message must follow this structure exactly (literal newlines):

   ```
   *:books: 오늘의 참고 논문 (<YYYY-MM-DD>)*

   *<https://doi.org/<DOI1>|<FirstAuthor1> <Year1>, <Journal1>>*
   <Line 1: 무엇을 했는지 + 핵심 결과 1-2문장 (compact, formal Korean ~합니다/~입니다)>
   <Line 2: 한미암 활용 1문장 — 시사·참고 톤 종결>

   *<https://doi.org/<DOI2>|<FirstAuthor2> <Year2>, <Journal2>>*
   <같은 3줄 구조>
   ```

   **인트로 멘트(부제) 절대 추가 X**. 헤더 다음 빈 줄, 바로 첫 논문 citation.

   ### 톤 가이드 — 매우 중요

   청중은 한미암 과제의 **임상·기초 교수진**. 이 디지스트는 "이걸 보고 당장 적용하세요"가 아니라
   **"이런 각도/사례도 있더라"고 연구자 시야를 넓혀드리는 큐레이션**의 성격. 따라서:

   - **명령·지시 어조 금지**: "활용 가능합니다", "사용해야 합니다", "적용해야 합니다", "적용 가능합니다" → 부담스러움
   - **가능성·시사·참고 어조 권장**: "~참고해볼 수 있겠습니다", "~사료됩니다", "~시사합니다", "~보입니다"
   - **정중하고 상냥하게** ~합니다 / ~입니다 / ~보입니다 / ~사료됩니다. 너무 딱딱하지 않게.
   - 영어 기술 용어는 그대로 (proteogenomics, phosphoproteome, neoantigen, ppQTL 등 번역 X)

   ### 인트로 멘트 — 추가하지 마세요

   "오늘의 참고 논문 (날짜)" 헤더 외에 **인트로/부제/소개 문장 절대 추가하지 않습니다**.
   헤더 → 빈 줄 → 첫 논문 citation 으로 바로 들어가세요.

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

   - **활용 line**: 한미암 과제와의 연결 1문장. **앵글은 매일 다양화** — 모든 논문을 "파이프라인 참고"로만 매핑하지 마세요. 다음 5가지 앵글 중 *논문 내용에 가장 자연스러운 것* 선택:

     * **(A) 생물학적 발견 앵글**: 논문이 보고한 특정 *단백질·유전자·기전*을 한미암 데이터에서 검토할 후보로 제시
       예: "본 연구가 chemoresistance 극복 표적으로 보고한 GSK3B-S9 인산화 매개 Wnt/JAK-STAT 축은, 한미암 인산화단백체 데이터에서도 우선 살펴볼 만한 신호 경로로 사료됩니다."

     * **(B) 바이오마커·환자 층화 앵글**: 논문이 동정한 마커를 한미암 코호트 환자 층화에 후보로 고려
       예: "ATAD1 short isoform이 chemosensitivity 마커 후보로 동정된 점은, 한미암 코호트 환자 층화 시 함께 고려해볼 만한 변수로 보입니다."

     * **(C) 표적·치료 경로 앵글**: 논문이 새롭게 제시한 표적·치료 전략의 한미암 연관성
       예: "PD-L1과 TROP-2/NECTIN-4 상관성에서 도출된 병용요법 가설은, 한미암 과제의 면역치료제 반응성 분석에서도 검토 가치가 있어 보입니다."

     * **(D) 코호트·디자인 앵글**: 논문의 종단·비교 디자인이 한미암 1차/2차 내성 비교에 주는 시사점
       예: "치료 전·후 60건 종양의 phosphoproteome 비교 디자인은, 한미암 과제의 1차/2차 내성 분석 설계에 시사점을 줄 수 있을 것으로 보입니다."

     * **(E) 메서드·파이프라인 앵글**: 분석 워크플로·방법론 자체가 한미암 파이프라인 구축에 참고
       예: "TMT11 + Fe-NTA IMAC + Orbitrap Lumos + Philosopher 워크플로는 한미암 인산화단백체 파이프라인 구축 시 참고할 만한 구성으로 사료됩니다."

   - 매일 같은 앵글(특히 E 메서드)로만 가지 말 것. 가능하면 (A)/(B)/(C) 중 하나를 우선 선택. 논문이 발견 위주면 (A)/(B), 임상·치료 전략 위주면 (C), 종단 디자인 비교면 (D), 순수 메서드 논문이면 (E).
   - 시작은 자연스럽게: `한미암 과제 관점에서, ...`, `한미암 코호트의 ___ 관점에서, ...`, `본 논문이 보고한 ___은, 한미암 ...`, `본 연구의 ___ 디자인은, 한미암 ...` 등 다양한 도입.

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
   - **Do NOT invent results**. If `full_text` doesn't say it, don't claim it.

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
