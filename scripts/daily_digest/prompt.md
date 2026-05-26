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
   - **Tier 0 (skip)**:
     * animal/cell-line only (no human clinical data),
     * non-cancer disease, weak relevance,
     * **method/tool/model/pipeline/software paper without clinical or
       translational findings in cancer patients.** 청중이 임상·기초 교수진이라
       "새로운 분석 툴/모델/워크플로우 자체"가 본문 contribution인 논문은
       의사·실험 랩 입장에서 실용성이 낮음. 단, 새로운 메서드를 실제 환자
       코호트에 적용해 임상·생물학적 발견을 내놓은 논문(예: CPTAC, proteogenomic
       characterization)은 Tier 0이 아님 — 발견이 main contribution이면 통과.
     * benchmark/comparison/validation-only studies of existing tools.

2. **Pick top 1-2** with Tier ≥ 2. Prefer Tier 1 over Tier 2 over Tier 3.

   **위암 우선순위 가산** — 후보들이 같은 tier에 있을 때 또는 tier가 비슷할 때,
   **위암(gastric cancer / stomach cancer / gastric adenocarcinoma / GC) 관련 논문을
   먼저 선택**. 한미암 과제의 핵심 암종이 위암이므로, 비위암(범암종 pan-cancer
   포함) 후보보다 위암 특이 코호트·기전·치료 연구를 우선. 단 명백히 더 높은
   tier의 비위암 논문이 있으면 그쪽 우선 (Tier 1 비위암 > Tier 2 위암).
   위암 논문이 없으면 평소대로 진행.
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
   - **Total body length per paper**: 2-3 sentences across body + 활용 line (활용 line 자체는 1-2 sentences 가능). 청중이 짧은 글에서 actionable한 그림이 보이게 하는 게 우선.

   ### 활용 line의 깊이 — 절대로 얕게 쓰지 말 것

   ❌ **얕은 활용 line (피해야 할 패턴)** — "어쩌라고" 느낌:
   - "한미암 과제 관점에서, 단백체 기반 환자 분류·바이오마커 검증 프레임워크는 AI 치료반응성 예측 모형 설계 시 참고해볼 수 있는 사례로 사료됩니다."
   - "본 연구가 보고한 FOXA1 Ser331 인산화 매개 cistrome 조절 기전은, 한미암 과제의 인산화단백체-WGS 통합 분석에서 검토해볼 만한 신호 축으로 보입니다."

   문제점:
   - "참고해볼 수 있는 사례", "검토해볼 만한 신호 축" 같은 *추상 명사구*만 있음
   - 한미암의 *구체적 어떤 작업*을 할 때, *논문의 어떤 측면*을, *어떻게* 쓸지가 안 보임

   ✅ **깊은 활용 line (목표 패턴)** — 시야를 실제로 넓혀줌:

   사용자가 제시한 reference 예시 톤:
   - "한미암 후향적 병리/멀티오믹스 분석에서 **TME를 공간적 ecosystem state로 요약**하는 레퍼런스로 활용할 수 있겠습니다."
   - "한미암의 병리 이미지·임상정보·다중오믹스 데이터를 연결하는 분석 축과 직접적으로 맞닿으며, 특히 **실측 spatial transcriptomics가 없는 샘플을** 공간 분자 가설로 **확장하는 전략**을 보여줍니다."
   - "한미암에서 Xenium·CosMx 등 데이터를 치료반응 biomarker로 쓸 때, **cell-cell proximity signal이 artifact인지 실제 biology인지 구분**하는 데 중요한 참고 자료가 될 것으로 보입니다."

   특징:
   - **구체 작업·시나리오 명시**: "TF activity inference 시", "외부 코호트 검증 시", "subtype 층화 시", "transcript spillover 의심 시" 등
   - **논문의 specific 측면 적시**: 단백질 이름·기전·디자인 등 결과에서 직접 인용
   - **어떻게**가 보임: "...로 요약하는", "...로 확장하는", "...를 구분하는", "...의 hypothesis prior로"

   ### 깊은 활용 line 작성 체크리스트 (3개 다 충족해야 함)

   1. **What** — 본문의 *구체적 발견/디자인/메서드*가 무엇인지 인용 (숫자·단백질명·메서드명·디자인 특징 등)
   2. **Where** — 한미암의 *어떤 작업/분석/단계*에 연결되는지 (TF activity inference, subtype 층화, AI 모형 외부 검증, 1차/2차 내성 비교, 신생항원 우선순위 등 구체 작업명)
   3. **How** — 그 발견을 *어떻게* 적용/참고할지 (가설 prior, 검증 프레임워크 구성, hypothesis 확장 전략, artifact 판별 기준 등)

   체크리스트 통과 못 하면 다시 작성. "참고해볼 수 있는 사례로 보입니다" 같은 추상 명사구로 끝내지 말고 *구체 작업 + 구체 사용 방식*까지 적시.

   ### 깊이 강화 예시 (Holt 2025)

   - 얕은 (피하기): "한미암 과제의 1차 내성 인산화단백체–WGS 통합 분석 단계에서, 환자 층화·표적 도출 파이프라인 설계 시 참고해볼 수 있는 레퍼런스로 보입니다."

   - 깊은 (목표): "ATAD1 short isoform과 GSK3B-S9 인산화 매개 Wnt/JAK-STAT 축이 화학내성 극복 표적으로 제시된 점은, 한미암 코호트의 인산화단백체 데이터에서 화학요법 반응성 환자군을 층화할 때 *isoform-level peptide quantification*과 *Wnt-axis phospho-signature*를 우선 후보 변수로 고려해볼 수 있는 단서를 제공합니다. 또한 치료 전 46건 + 치료 후 14건의 종단 디자인은 한미암 과제의 1차 vs 2차 내성 phospho-network 변화 비교 시 참고할 만한 코호트 규모와 비교 구조의 사례로 보입니다."

   - **활용 line**: 한미암 과제와의 연결 1문장. **앵글은 매일 다양화** — 모든 논문을 "파이프라인 참고"로만 매핑하지 마세요. 다음 5가지 앵글 중 *논문 내용에 가장 자연스러운 것* 선택:

     * **(A) 생물학적 발견 앵글**: 논문이 보고한 특정 *단백질·유전자·기전*을 한미암 데이터에서 검토할 후보로 제시
       예: "본 연구가 chemoresistance 극복 표적으로 보고한 GSK3B-S9 인산화 매개 Wnt/JAK-STAT 축은, 한미암 인산화단백체 데이터에서도 우선 살펴볼 만한 신호 경로로 사료됩니다."

     * **(B) 바이오마커·환자 층화 앵글**: 논문이 동정한 마커를 한미암 코호트 환자 층화에 후보로 고려
       예: "ATAD1 short isoform이 chemosensitivity 마커 후보로 동정된 점은, 한미암 코호트 환자 층화 시 함께 고려해볼 만한 변수로 보입니다."

     * **(C) 표적·치료 경로 앵글**: 논문이 새롭게 제시한 표적·치료 전략의 한미암 연관성
       예: "PD-L1과 TROP-2/NECTIN-4 상관성에서 도출된 병용요법 가설은, 한미암 과제의 면역치료제 반응성 분석에서도 검토 가치가 있어 보입니다."

     * **(D) 코호트·디자인 앵글**: 논문의 종단·비교 디자인이 한미암 1차/2차 내성 비교에 주는 시사점
       예: "치료 전·후 60건 종양의 phosphoproteome 비교 디자인은, 한미암 과제의 1차/2차 내성 분석 설계에 시사점을 줄 수 있을 것으로 보입니다."

   - **메서드·파이프라인·툴·모델 자체에 대한 활용 앵글은 사용하지 마세요.** 청중이
     임상·기초 교수진이라 "TMT11+IMAC 워크플로 참고", "이 AI 모델 구조 참고",
     "이 deconvolution 툴 적용" 같은 분석 워크플로/방법론/소프트웨어 자체의 채택
     앵글은 의미가 없습니다. 같은 논문이라도 *발견·표적·바이오마커·디자인* 앵글로
     돌려서 작성하세요. (메서드 contribution이 주인 논문은 애초에 Tier 0로
     빠져야 하지만, 임상 발견 있는 논문이라도 활용 line은 발견 쪽으로 잡을 것.)
   - 가능하면 (A)/(B)/(C) 중 하나를 우선 선택. 논문이 발견 위주면 (A)/(B),
     임상·치료 전략 위주면 (C), 종단 디자인 비교면 (D).
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
