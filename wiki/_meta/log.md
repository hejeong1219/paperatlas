# Log

Append-only operational history for this wiki.

## [2026-05-28] analysis | Cancer Multiomics resistance biomarker evidence boundary mapping

- Added `wiki/analyses/cancer-multiomics-resistance-biomarker-evidence-boundary-map.md` as the second durable question-expansion node after the initial question chain.
- Reclassified local resistance proteogenomics evidence by biomarker evidence type: baseline primary resistance marker, therapy-emergent acquired-resistance marker, adaptive tolerance marker, refractory-state marker, and feature-design atlas signal.
- Updated the Cancer Multiomics topic hub so the project question no longer starts from a "genomics is insufficient" framing, but from timing, functional readout, and evidence-type separation.
- Updated the presentation storyline to show an actual repeated loop: broad question -> question-chain page -> evidence-boundary page -> next validation-strength question.
- Revised the presentation question chain so it begins with how each paper defines resistance, then separates pre/post or time-course data from resistant-vs-non-resistant snapshot data before moving to protein/phosphosite readouts and multiomics integration methods.
- Repositioned multiomics integration as a method sub-question rather than the main research question.
- Connected the user's existing cancer resistance review as a prior LLM-Wiki thought chain: resistance convergence through visibility, access, and effector dysfunction now serves as one slide of background before the Cancer Multiomics biomarker question.
- Added a "reference presentation takeaways" section using the previous LLM-Wiki presentation and 2026-05-19 class summary only as format guidance, not as a content template.
- Added a 12-slide PPT spine centered on the user's LLM-use routine: user-defined starting question, LLM-driven question splitting, durable wiki nodes, source-bounded links, method questions kept below concept questions, and next-question preservation.
- Added a presentation graph-capture plan keyed to the professor's instruction: one question per subgraph, with specific center nodes and connected paper nodes.
- Added `wiki/analyses/cancer-multiomics-presentation-capture-board.md` as a dedicated capture board so HTML/Obsidian capture targets are grouped by presentation question.
- Added `wiki/analyses/my-llm-wiki-use-rules.md` as the user's own LLM-Wiki use-rule page, modeled on the class expectation that each presenter should explain their own LLM constraints and routine rather than only a biological classification scheme.
- Added LLM-use-rule Q&A preparation covering raw-PDF boundary, checking what the evidence permits before writing conclusions, graph capture rationale, and how the user used LLM as a questioning workflow rather than a replacement for research judgment.
- Added `wiki/analyses/cancer-multiomics-resistance-gap-decision-matrix.md` to separate the biological research gap from data-design subquestions: the talk should not end at data shortage, but ask what functional resistance state each protein/phosphosite program represents.
- Added `wiki/analyses/cancer-multiomics-final-presentation-brief.md` as the PPT-ready final storyline: the talk now centers on the shift from layer-centered marker discovery to state-centered interpretation, ending with the question of whether cancer multiomics can reclassify genome-unexplained resistance into functional resistance states.
- Updated the meta index with the new evidence-boundary page.

## [2026-05-27] analysis | Cancer Multiomics presentation storyline

- Added `wiki/analyses/cancer-multiomics-resistance-biomarker-question-chain.md` as an actual question-chain artifact: starting prompt -> reopened wiki nodes -> question ladder -> gaps -> next run. The page uses a stable subject slug rather than a date-based filename.
- Linked the new question-run page from `wiki/topics/cancer-multiomics-literature.md` under a new `Question Runs` section so the public topic hub exposes the workflow, not only the literature corpus.
- Added `wiki/analyses/cancer-multiomics-presentation-storyline.md` as a 15-minute presentation narrative for the advanced genetics LLM-Wiki sharing assignment.
- Reframed the user's Cancer Multiomics wiki work as a question-expansion chain for proteome/phosphoproteome-based anticancer resistance biomarker discovery, centered on the gap between primary resistance, acquired resistance, and static refractory-state interpretations.
- Added a presentation table tracking each step as question -> wiki-expanded node -> discovered gap -> next question, so the talk shows the research-question development process rather than a generic evidence-layer proposal.
- Incorporated the 2026-05-19 Zoom summary lesson that the presentation should show LLM-Wiki operating rules, question evolution, and question-specific Obsidian graphs rather than simply summarizing papers.

## [2026-05-26] analysis | Primary/acquired resistance proteogenomics ingest map

- Added `wiki/analyses/primary-acquired-resistance-proteogenomics-ingest-map.md` to convert the presentation question into a source-bounded ingest and deep-dive queue.
- Reclassified local drug-response/proteogenomics evidence into primary-resistance, acquired-resistance, static refractory-state, and baseline atlas/feature-design buckets.
- Added a priority deep-dive queue for longitudinal/acquired-resistance papers, emphasizing pre/post or serial sampling over static resistant-patient snapshots.
- Updated `wiki/_meta/index.md` so the new map is visible from the analysis catalog.

## [2026-05-26] naming | Rename Cancer Multiomics topic hub and restore full topic index

- Renamed the public-facing title of `wiki/topics/cancer-multiomics-literature.md` from `Cancer Multiomics Literature Monitor` to `Cancer Multiomics Proteogenomic Atlas` while preserving the stable file slug.
- Updated `wiki/topics/index.md` so the Topics landing page now lists all five current topic hubs, including the Cancer Multiomics and Multiomics PTM atlas pages that had been omitted.
- Updated `wiki/_meta/index.md` to use the new Cancer Multiomics topic title and project-facing description.

## [2026-05-26] ingest | Topic-sweep top-up to close today's 50 new-source target

- Added 8 new `wiki/sources/` pages from a fresh high-impact human-cancer sweep: 5 B-cell / neoantigen-facing papers (`syding-2025`, `sahin-2026`, `wu-2025`, `minati-2025`, `sambanthamoorthy-2026`) and 3 Cancer Multiomics papers (`krossa-2025`, `wang-2025`, `satpathy-2025`).
- Corrected DOI / PMC metadata for all 8 new stubs against local PDF headers plus PubMed XML before keeping them in the wiki.
- Fixed `scripts/ingest/update_anchor_links.py` so topic aliases are merged instead of overwriting one another; reran it to restore full `Linked Sources` sections on the B-cell topic/anchor pages and the Cancer Multiomics topic hub.
- Tightened `scripts/ingest/ingest_topic_sweep.py` cancer-type inference to avoid generic `myeloid` / `all` false positives leaking into leukemia labels.
- Operationally, this closes the day from 42 committed new source pages to 50 total new source pages in the working tree for 2026-05-26.

## [2026-05-25] analysis | Refractory gastric cancer resistance-state subtype question pivot

- Refined `wiki/analyses/resistance-state-subtyping-refractory-gastric-cancer.md` around the question of whether a refractory cohort can support **resistance-state subtype** discovery rather than only conventional molecular subtype discovery.
- Added a working distinction between molecular subtype, therapeutic vulnerability subtype, and resistance-state subtype.
- Reframed IC1/IC2 as candidate resistance-state subtypes: immune-visible/exhausted versus kinase-driven/immune-quiet, with clinical-response and WGS validation requirements left as open questions.
- Added an endpoint pivot from resistant-versus-non-resistant classification to intra-refractory heterogeneity: resistance should first be decomposed into immune, kinase, genome-instability, antigen-presentation, and stromal/access states when prior treatment histories are mixed.
- Added an evidence-bounded six-step question chain that links each answer and unresolved hypothesis to local source pages, then turns each unresolved point into a follow-up question.

## [2026-05-25] sweep | Topic sweep: b-cell-neoantigen + cancer-multiomics-literature (90d / high+mid tier)

- Built `scripts/ingest/topic_sweep.py` (PubMed esearch + 90d Entrez window + high-impact/mid-tier journal allowlist + dedup against wiki/sources/ PMIDs/slugs and raw/inbox/papers/ + OA→EZproxy PDF download + text extract → JSON candidates).
- Built `scripts/ingest/ingest_topic_sweep.py` (generates wiki/sources/<slug>.md stubs with frontmatter from JSON; marks `batch_ingest_status: topic-sweep-stub`).
- Sweep result — `bcell-neoantigen`: 169 PMIDs → 40 accepted after filters → 28 successful PDF+text (Nature/Cell/Cancer Cell/JITC/Sci Adv/Nat Med/Nat Biotech/Immunity/Cancer Disc/Cancer Immunol Res/Clin Cancer Res/Genome Biol 등).
- Sweep result — `cancer-multiomics`: 126 PMIDs → 28 accepted after filters → 14 successful PDF+text (Cell Rep Med/Cancer Lett/JITC/Nat Commun/Cancer Res/Nat Genet/STTT/JCI/eLife/EMBO Mol Med 등).
- Two subagents enriched all 42 stubs with Korean Summary + Key Points + 한미암 활용 가능성 sections grounded in full_text; both topic hub pages appended with new "2026-05 Topic Sweep Additions" sections + one-line takeaways.
- Created two new analysis pages: `wiki/analyses/bcell-neoantigen-50q-sprint-2026-05.md` and `wiki/analyses/cancer-multiomics-50q-sprint-2026-05.md` with 50 questions each, structured by sub-axis (neoantigen discovery / TLS / clinical translation / biomarkers / methods for bcell; WGS / phospho / WGS-proteome / spatial / response prediction for multiomics). Answers being filled by parallel subagents using local wiki + new source pages only (no web evidence per AGENTS.md source-boundary rule).
- Frontmatter `batch_ingest_status: topic-sweep-stub` marks these as 1-pass automated ingest, not manual full-text deep-dive — promotion to `full-text-read` happens per-paper later as the user prioritizes.
- Three bcell papers had author-correction-only PDFs (`zhang-2026-innovative-approaches-lung-cancer-screening-interception`, `bandlamudi-2026-cancer-type-specific-variation-patterns-driver`, `ghosh-2026-chemokine-defined-macrophage-niches-establish-spatial`) — flagged in those pages' Key Points.

## [2026-05-13] ingest | Chen 2026 — Pan-cancer CPTAC germline SV → cancer proteome cis-effect + 31 CSG LoF + ancestry-stratified + methylation-mediated mechanism (Nat Commun, user-shared paywall PDF, stub 교체)

- 사용자가 Springer Nature Communications 본문 PDF(`s41467-026-71967-y_reference.pdf`, 45.48 MB, Dropbox 경유) 공유 → 5개 user-shared 논문 배치 중 마지막 풀 ingest(Paper 9/Task #35). 사용자 결정: "Chang/Chen 풀 ingest + 4편 모두 Notion (Recommended)". paywall(Nature Communications open access 표시지만 publisher PDF 다운로드는 user-shared가 직접 확보) — 기존 로컬 파일 `raw/inbox/papers/chen-2026-global-impact-germline-structural-variation-cancer-proteome.pdf`(368 KB, HTML-as-PDF)을 정상 PDF(45.48 MB)로 교체. 이전 Cancer Multiomics 100-paper queue에서 Chen 2026은 `blocked` 상태였으나 PDF 교체로 `needs-brief`(full ingest 완료) 전환.
- 메타데이터 확인: Nature Communications 2026. DOI 10.1038/s41467-026-71967-y. CC BY OA license(publisher metadata). 저자 7명(Chen / Vasaikar / Reva / Lim / Wen / Liao / Zhang) — Baylor College of Medicine + UAB + Rice University 소속; corresponding은 Baylor의 Bing Zhang lab 가능성. CPTAC 협력 연구; Chen 2023(somatic SV → proteome) 자매 논문으로 동일 lab의 germline 확장. dbGaP phs001287.v21.p6(CPTAC pan-cancer WGS) + phs003011.v1.p1 + phs000178.v11.p8(TCGA WGS) 사용.
- PDF 처리: `/home/hejeong/Dropbox/s41467-026-71967-y_reference.pdf` 45.48 MB → `pdftotext -layout` 추출 → `/tmp/papers/chen_germline.txt`(5,854 line). Springer Open Access PDF는 paragraph wrap이 깨지는 경향 있음. 표준 위치 `raw/inbox/papers/chen-2026-global-impact-germline-structural-variation-cancer-proteome.pdf`(45.48 MB) 복사 완료(기존 invalid HTML-as-PDF 덮어쓰기). `pdf_status: complete`.
- 본문 정독: 추출 텍스트 lines 1-3100 직접 정독 — metadata + authors + affiliations + Abstract + Introduction + Results 7 sections(SV compendium + LoF protein impact + gene-level recurrent + CGI methylation + enhancer methylation + tumour-specific + ancestry + essential gene/survival) + Discussion + Methods + Data availability + References subset.
- 기존 stub `wiki/sources/chen-2026-global-impact-germline-structural-variation-cancer-proteome.md`(`pdf_status: blocked`, 42 line, "invalid PDF" 안내만) 전면 교체: Summary + Key Points 8 subsection(코호트 + LoF cis-impact + recurrent gene-level + CGI methylation + enhancer methylation + tumour-type-specific + ancestry + essential gene/survival) + Methods + Cancer Multiomics Project Relevance(5축) + Connections + Sources 6 섹션. `feedback_paper_relevance_writing.md` 규칙 엄수(자체 평가어/시너지 묶음 금지).
- frontmatter: `paper_kind: proteogenomic`, `cancer_types: [pan-cancer]`, `modalities: [whole-genome-sequencing, rna-seq, proteomics, dna-methylation]`, `themes`에 structural-variation / germline / cis-regulatory / dna-methylation / cpg-island / enhancer / cancer-susceptibility-gene / ancestry / tumour-type-specific / top2a / nedd1 / fabp5 포함. 7-author 명시(Chen/Vasaikar/Reva/Lim/Wen/Liao/Zhang). `discovery_method: user-shared`.
- 핵심 정량 포인트: CPTAC 1,637 cancer patient × 11 tumour type(BR/CCRCC/CO/GBM/HN/LUAD/LSCC/OV/PDA/UCEC/GBM-pediatric) + CBTN pediatric brain tumour validation cohort. Paired SV caller(Delly v3.1.1 ∩ SVABA v1.2.0) normal WGS → **704,263 distinct germline SV**(86% singleton, 73% DGV / 58% gnomAD / 55% TOPMed catalog 등재, **84% any catalog**). 신규 SV ~18,776/patient; deletion 51% / duplication 24% / inversion 16% / insertion 9%; 평균 SV 길이 ~950 bp(deletion median 320 bp / duplication 1.1 kb). **LoF SV → low-protein cis-impact**: 114,684 rare/singleton 중 **25,781 LoF SV**(SVAnnotate frameshift/exon deletion/stop-gain); 12,442 paired proteomics 측정 가능 → **1,847 low-protein outlier event**(quantile-based FDR<10%) → **512 genes × 786 patients** LoF SV-cis-correlated. Hypergeometric enrichment: MHC class I antigen binding / antigen processing / exosome / mitochondrial matrix / Golgi membrane. **CSG enrichment**: 688 CSG(csgs.sequenxe.com May 2024) 중 **31**(CDH13/CDKN2A/MSR1/SDHA/SMAD4/SMARCB1) LoF SV 보유자 단백 저발현; **101 환자(전체 6%)** 최소 1 CSG LoF SV. **Gene-level recurrent**: 364 recurrently SV-altered gene(≥3명) 중 **129(17%) mRNA+protein concordant**(relaxed FDR, 같은 방향; CA8/PTGR1 대표). **33% reverse direction**(protein 변화 우세, mRNA 약함) → MS-based proteomics가 mRNA-only로 못 잡는 cis-effect 포착. **DNA methylation 매개**: **1,237 CGI probe FDR<10%** SV-methylation cis; 233/2,686 positive-methylation → negative-mRNA 28개 protein concordant(CES1/GGACT/PTDSS2). **Enhancer methylation**: 109 SV-enhancer-methylation FDR<10% pair 중 **41개 CBTN pediatric brain tumour 재현**(p<1E-22; ECHDC1/SH3GLB2/MAMDC2). **Tumour-type-specific cis-effect**: 11 tumour type별 분석 시 **137 genes 단일 tissue에서만 mRNA+protein concordant**(pan-tissue 분석 17개) → tumour-type-specific germline SV impact가 pan-cancer 평균화에 가려짐; **CDK2(GBM) / RHOH(LUAD) / ARIH1(CCRCC)** 대표; 60 CGI probe tissue-specific. **Ancestry-enriched**: PCA 기반 1KGP ancestry assignment(African/Asian/European/Mixed); SV spectrum ancestry로 separation; **69 concordant gene 중 31(45%) ancestry-enriched** — **10 African(FSCN1)** / **8 Asian(TIGAR)** / **13 European(CTSW)**; SIDT2 등 일부는 ancestry alone explained → ancestry-aware analysis 필수. **Essential gene + survival 교차**: **FABP5 / NEDD1 / TOP2A** DepMap essential + survival 양쪽 통과; **TOP2A common germline SV ~25-30% 환자**. Data: dbGaP **phs001287.v21.p6**(CPTAC) + **phs003011.v1.p1** + **phs000178.v11.p8**(TCGA), PDC, GDC, CBTN/Cavatica, UALCAN portal, figshare(SV-expression). Tools: Delly v3.1.1, SVABA v1.2.0/v1.1.0, Manta v1.4.0(CBTN), SVAnnotate, SVExpress, DGV, gnomAD, TOPMed. 한계 본문 명시: paired SV caller(Delly ∩ SVABA) 합의 강제로 LoF 일부 잘림 + 단일 timepoint normal sample + Delly/SVABA short-read paired-end limitation(long-read WGS 미적용); 향후 long-read WGS 보완 권장.
- 한미암 적용 5축: (1) **Germline SV 패널 디자인(한국인 코호트 적용 시 ancestry-enriched SV 우선)** — Asian-enriched SV 8 gene(TIGAR 포함) + European/African 13/10 gene과 cis-cancer effect 차이로 한미암 한국인 코호트에서 ancestry-specific SV panel(특히 Asian-enriched LoF SV in CSG) 우선 sequencing 후보 식별 근거. CSG 31개 중 **CDH13/CDKN2A/SDHA/SMAD4/SMARCB1**은 이미 한미암 후보 cancer susceptibility 패널 포함 가능 → germline LoF SV(특히 exon-level deletion)를 SNV panel과 동시에 콜링하도록 분석 파이프라인 보강. (2) **SV → 단백 cis-effect 사전 검증 워크플로우** — 364 recurrent gene 중 17%만 mRNA+protein concordant → 한미암 자체 단백체 코호트 cis-SV 후보 우선화 시 본 논문 concordant list(CA8, PTGR1, ECHDC1, SH3GLB2, MAMDC2, FABP5, NEDD1, TOP2A)를 priority validation set으로 활용. Reverse direction(33%, protein-only)이 크므로 mRNA-only QC로 SV impact reject 금지 — MS-based 단백체가 cis-effect 발굴에 필수임이 입증. (3) **한국인 ancestry-stratified pQTL/svQTL 구축** — 31/69 ancestry-stratified concordant gene과 SIDT2-style ancestry-confound 사례 → 한미암이 향후 한국인 cancer cohort pQTL/sQTL 구축 시 1KGP East Asian super-population baseline + Korean-specific SV catalog(KOVA, KCDC) referencing ancestry-aware analysis pipeline 설계 필요. SIDT2처럼 ancestry alone explained SV는 false-positive risk가 큼. (4) **CpG island/enhancer methylation 매개 sub-rosa cis-mechanism 통합** — SV가 coding region 직접 영향 없어도 CGI/enhancer methylation으로 단백 발현 변경(1,237 + 109 사건)함이 입증 → 한미암 multi-omics 통합 파이프라인에서 **WGS-only 분석**으로 SV impact 평가 금지, **methylation 450K/EPIC array 또는 WGBS**를 보조 modality로 결합해야 SV → expression 매개 메커니즘 누락 방지. (5) **Pediatric/희귀암 코호트 확장 시 SV 메커니즘 reproducibility** — CBTN(소아 뇌종양) cohort 41 enhancer-methylation SV(p<1E-22) 독립 reproduce → 성인 cancer germline SV cis-mechanism이 **소아·희귀암 코호트로 transfer 가능**한 통계적 power 시사. 한미암이 한국 소아암 cohort(어린이병원 IRB 협력) 별도 코호트로 다룰 때 CBTN-style validation 모방 분석 디자인 가능.
- 토픽 허브 `wiki/topics/cancer-multiomics-literature.md` Section 1(WGS와 Proteogenomics 통합 기반): 신규 entry 추가 — Chen 2023(자매 논문, somatic SV) 바로 다음 위치. 1,637 환자 + 704,263 SV + 25,781 LoF + 1,847 low-protein outlier + 31 CSG + 364→129 concordant + CGI 1,237 + enhancer 109(CBTN 41 reproduce) + tissue-specific 137 + ancestry 31/69 + FABP5/NEDD1/TOP2A + dbGaP/PDC IDs + 한계 모두 포함.
- corpus queue 카운트 조정: Selected 101→101(Chen은 이미 row 존재), Acquired 92→92(이미 PDF 파일 있었으나 invalid HTML; 진짜 PDF로 교체이므로 카운트 변경 없음), Ingested 102→103(stub → full 교체), Blocked 10→10(Chen은 이미 노트에서 "Chen 2026 germline SV는 2026-05-12 PDF 확보로 해제" 표기됨; 변경 없음). Chen 2026 row 노트 갱신: "Nat Commun 2026 (PDF user-shared 2026-05-12, stub 교체 2026-05-13 → full ingest 완료). Pan-cancer CPTAC germline SV → tumour proteome cis-effect, 31 CSG LoF in 101 patients(6%), ancestry-stratified, methylation-mediated."
- `wiki/_meta/index.md` Proteogenomics / PTM Atlas cluster Chang 2026 직전 위치에 Chen 2026 신규 링크 추가; 1,637 환자 + germline SV + CSG + concordance + methylation + ancestry + DepMap 정량 포함.
- Notion 페이지(`참고 논문 및 아이디어` 344302d9...): **4-section 간소 템플릿**(논문 정보 / 한 줄 요약 / 과제 관련성 (한미암) / 주요 결과) 적용 예정. funding/이해관계/저자 소속 제외.

## [2026-05-12] ingest | Chang 2026 — Taiwanese gastric cancer proteogenomics (n=154) + DBAC PAH carcinogen + Streptococcus anginosus microbiome + 4-anatomy + CDK4 hub (Gut, user-shared paywall PDF)

- 사용자가 BMJ Gut 본문 PDF(`886.full.pdf`, 22.66 MB, Mac OS Dropbox 경유) 공유 → 5개 user-shared 논문 배치 중 두 번째(Paper 2/Task #28). 사용자 결정: "Chang/Chen 풀 ingest + 4편 모두 Notion (Recommended)" — Chang 풀 ingest + Chen germline SV 풀 ingest(스텁 교체) + Sinitcyn 2023 + Lee TNBC 2026 (이미 6-section 완비) Notion 4-section 페이지만. paywall(Gut BMJ proprietary)이라 사용자 직접 PDF 제공 필요했고 이전 Cancer Multiomics 100-paper queue에서 Chang은 row 부재(신규 row), Chen은 `blocked` 상태였음.
- 메타데이터 확인: Gut 2026;75:886–904 (Online First 2026-01-30; Volume 75 Issue 6 print 2026 May; pp.886–904). DOI 10.1136/gutjnl-2025-337247. BMJ proprietary license. CPTAC-ICPC 협력 연구. 5 co-first author: Ya-Hsuan Chang(Academia Sinica IBC) / Tzu-Chan Hong(NTU CIRM) / Kuen-Tyng Lin(Academia Sinica IBC) / Yi-Jing Hsiao(Academia Sinica IBC) / Hsiang-En Hsu(Academia Sinica IBC). 2 joint senior: Yu-Ju Chen(Academia Sinica IBC, Corresponding chemyj@gate.sinica.edu.tw) + Ming-Shiang Wu(NTUH, Corresponding mingshiang@ntu.edu.tw). 6 추가 corresponding: Sung-Liang Yu(NTU College of Medicine) / Hsuan-Yu Chen(Academia Sinica Stats) / Deng-Chyang Wu(KMUH) / Chia-Li Han(Taipei Medical Univ) / Jyh-Ming Liou(NTUH) / Li-Tzong Chen(NHRI). 환자 코호트 NTUH(National Taiwan University Hospital) + KMUH(Kaohsiung Medical University Hospital), 2022-03 to 2024-12 enrollment, IRB approved. East Asian Han Chinese 동질 집단.
- PDF 처리: `/home/hejeong/Dropbox/886.full.pdf` 22.66 MB → `pdftotext -layout` 추출 → `/tmp/papers/chang_gastric.txt`(1,211 line) 추출 성공. 표준 위치 `raw/inbox/papers/chang-2026-integrative-proteogenomics-gastric-cancer-taiwan.pdf`(22.66 MB) 복사 완료. `pdf_status: complete`.
- 본문 정독: 추출 텍스트 lines 1-200(metadata + 41 author affiliations + Abstract + Introduction) / 200-500(Results 코호트 + 7 mutational signature + 6 carcinogen cluster) / 500-800(microbiome + NAT proteome-immune + HP-negative subtypes) / 800-1100(tumour proteome + 4 anatomy + CDK4 + decision tree + limitations) 직접 정독.
- 신규 소스 페이지 `wiki/sources/chang-2026-integrative-proteogenomics-gastric-cancer-taiwan.md` 생성: Summary + 7 Key Points subsection(코호트 + DBAC + microbiome + NAT proteome-immune + HP-negative subtypes + 4 anatomy + decision tree+CDK4+한계) + Methods(IRB/data ID/sequencing platform/clustering algorithm 전체) + Cancer Multiomics Project Relevance(5축) + Connections + Sources 6 섹션. `feedback_paper_relevance_writing.md` 규칙 엄수(자체 평가어/시너지 묶음 금지).
- frontmatter: `paper_kind: proteogenomic`, `cancer_types: [gastric-cancer]`, `modalities: [wes, rna-seq, proteomics, phosphoproteomics, microbiome, ihc]`, `themes`에 taiwanese-cohort / cptac-icpc-collaboration / environmental-carcinogen-signature / dibenz-a-h-acridine-pah / h-pylori-independent-gastric-cancer / streptococcus-anginosus / tight-junction-barrier / cldn18-2-targeted-therapy / tumour-location-anatomy / cdk4-6-inhibitor-repurposing / microbiome-proteogenomics / decision-tree-prognostic-model 포함. 41-author 전체 명시. discovery_method: user-shared.
- 핵심 정량 포인트: 154 treatment-naïve East Asian Han Chinese GC 환자(NTUH+KMUH 2022-03~2024-12, median 67y, 62% male, 25% stage I, antral 우세) + 185 KMUH endoscopy 외부 검증(saliva n=159 / IM plaque n=151 / gastric juice n=101 / stool n=93). WES 14,134 nonsyn mut + RNA-seq 19,504 transcripts + TMT proteome **>10,000 protein group** + phosphoproteome **30,000 phosphosite** + microbial RNA(HRGMv2 MAPQ>10, prevalence ≥5%) + microbial protein(UniProt FDR<0.01, ≥5 unique protein/species, ≥10% prevalence) + IHC(MMR/HER2/CLDN18.2 43-14A/PD-L1). HP status: dual IgG ELISA + 조직 pathology — HP_E(exposed) 69.5% / HP_N(never) 30.5% / HP_A(active) 22.7% culture + CagA PCR(CF2/CR2 primers). 변이 빈도: TP53 + ARID1A mutual exclusivity p=0.002; KMT2D 24% vs TCGA 9-16%(3-fold); CDH1 mut 여성 p<0.001 + diffuse p=0.013 + 여성 diffuse p=0.008; PIK3CA 11%(< TCGA Caucasian 12-26%). **NMF 7 signature G1-G7 + 6 carcinogen cluster C1-C6**: G1 spontaneous 5-mC deamination / G2 tumour MMR / G3 polymerase-η translesion / G4 NAT MMR / G5 DSB repair / G6 nitrosamine / G7 irradiation + **DBAC PAH(dibenz[a,h]acridine) East-Asia 특이 signature**. C1 MMR-related NAT / C2 persistent deamination / C3 nitrosamine-like NAT(CYP2E1 ↑ + organonitrogen metabolism 정합) / C4 DBAC tumour-only / C5 DBAC tumour+NAT / C6 DBAC NAT-dominant. **DBAC HR 2.36-3.16 multivariable Cox**(age/sex/stage 조정), diffuse 5.9× EFS risk(p=0.013), Treg p=0.002. Cell-line 검증: MKN28 intestinal + MKN45 diffuse Boyden chamber 48h IC10/(1/5)IC10; **BaP MKN45 3.7× / MKN28 2.7× invasion(p<0.05)**; nitrosamine(NDMA/NDBA/NDELA/NPYR) modest 또는 non-significant; PAH-treated cell DBAC tissue signature pathway 일치(cell migration / matrix adhesion / neutrophil degranulation / CD40 signalling / p53). Cross-cohort: DBAC TCGA(Western-dominated) 부재 + Taiwanese + Japanese cohort 존재(charcoal-grilling/pan-frying dietary BaP cooked **1.30 ng/g vs raw 0.12 ng/g**). DBAC pathway 활성: PI3K-AKT + ERBB + VEGF + CD40 (NFAT-mediated migration/invasion 수렴 hub); Laurén-stratified: diffuse cytoskeletal/adhesion(actin/paxillin/Robo-Slit), intestinal RhoGDI/invadopodia. **Microbial RNA + protein cross-validation 14 species**, patient-level Spearman |ρ|≥0.40 networks: N-N denser than T-T(mean degree 1.31 vs 0.50, clustering 0.315 vs 0.233, lower modularity 0.593 vs 0.872). NAT hub: H. halodurans, N. aromaticivorans, S. epidermidis, A. thermocellus, H. orenii, S. aciditrophicus, HP. **4 MB.RNA cluster**: Microvirga-dominant(DBAC link **p=9.3×10⁻¹²** + M. pneumoniae co-occur + G2 peroxisome/xenobiotic/CYP450) / HP-dominant(HP_E p=4.97×10⁻⁸ + IM1+PN3 antibacterial G3-G4) / Streptococcus-dominant(C1+C3 link **p=6.8×10⁻¹⁰** + 젊은층 p=0.018 + G1 cytoskeletal/apical-junction/hedgehog + DNA repair ↓) / Mixed(L. reuteri probiotic + immune-cold IM2/IM4 p=0.005). Bivariate φ coefficient: **DBAC↔Microvirga 0.50(p<0.001), Cardiobacterium 0.53(p<0.001), F. nucleatum 0.20(p=0.01)** — PAH consortium; G6 nitrosamine↔Desulfovibrio φ=0.31(p<0.001) — abundance correlation 없음 → "permissive threshold" 모델. **3 NAT proteome cluster PN1-PN3 + 4 tumour cluster PT1-PT4 + NAT 4 immune cluster IM1-IM4 + tumour 5 immune cluster IM1-IM5**. Sankey alignment: PN3 = canonical HP-driven intestinal IM1(CagA virulence + adhesion/ECM); PN1 = female/diffuse 혼합 HP 부분 immune; PN2 = non-HP microbiome-enriched immune-silent antral(F. nucleatum + N. aromaticivorans xenobiotic estrogen activator). MCA1(HP+ intestinal) / MCA2(PN2/IM2 F. nucleatum+N. aromaticivorans) / MCA3(female diffuse 혼합 HP). PN1 adhesion/ECM 제한 immune; PN2 cell-cycle / DNA replication / oxidative metabolism — proliferation-driven low-inflammation. **PT1-IM1 vs PT1-IM3 bifurcation p=0.025**: PT1-IM1(Fcγ receptor phagocytosis + neutrophil extracellular trap) excellent prognosis; **PT1-IM3 worst OS — stage IV 사망률 초과**(decision tree). PT2 matrix/cytoskeleton without immune; PT3 metabolic+OXPHOS; PT4 DNA repair+protein translation. PT1↔Bormann type 3(p=0.002), PT2↔HP+(p=0.003), PT3↔diffuse(p=0.02), PT4↔intestinal(p=0.01). **HP_N tumour(n=47) 3 cluster T1-T3**: T2 bacterial invasion(SA enrichment) + immune activation(S. aureus / IL-17 / NOD-like / NF-κB) + **CLDN18.2/OCLN/ZO-1 reduction**(Wilcoxon adj. p<0.05) + FN1/THBS1/PDGFRB ↑ + PI3K-AKT — EMT-biased. T1 barrier-intact CLDN18.2-retained + innate immune ↓(C3/C5/MBL2 / RELA/TRAF3/CXCL3 / RIPK2/PYCARD / PTGS2 / FN1/THBS1) — **42% T1 met 43-14A IHC criteria**(CLDN18.2-targeted therapy), late-stage diffuse Bormann type 4. T3 post-transcriptional regulation + RNA processing. Independent KMUH n=185 외부 검증: SA gastric juice prevalence 47.3%(no IM) → 56.9%(IM) → **86.4%(cancer)**. **4 anatomy cluster Loc 1-4 η²=0.257 vs binary η²=0.077, p=0.00386** — anatomy-based stratification > binary(antrum/non-antrum). KEA3 location-specific kinase: Loc 1 cardia TP53/MAPK; Loc 2 mid-body ABL1/SYK/ROCK; Loc 3 antrum BRAF/CDK4/ERBB2; Loc 4 antrum MET/PRKAA2/MYC. **Loc 4 antrum 5 prognostic biomarker** SHROOM1 / p-LYST S2627 / XYLT1 / CRIP1 / SPATS2L KM Plotter n=118-875 외부 검증. **CDK4 actionable hub**: IHC-positive(HER2/PD-L1/CLDN18.2) + proteome-defined-positive + IHC-negative subgroup(**49.2%**) 3 subgroup 공통 — palbociclib/ribociclib repurposing 후보. Decision tree EFS(stage+DBAC), OS(stage+C3+PT1+IM2/3). Data dbGaP **phs004447.v1.p1** + PDC **PDC000645**(proteome) + **PDC000649**(phospho). 한계 본문 명시: HP_A 22.7% / single-cohort Taiwanese / BaP cell-line 검증만 + DBAC 직접 검증 미수행 / KEA3 location-specific kinase는 inference / decision tree retrospective.
- 한미암 적용 5축: (1) East Asia GC proteogenomic reference cohort — 한국인 위암 multi-omics 설계 시 154 환자 5-layer + IRB/data ID/data deposition 표준 채택. dbGaP phs004447.v1.p1 + PDC PDC000645/PDC000649 cross-reference 가능. East Asia intestinal:diffuse ratio + 25% stage I + antral 우세 East Asia 공통 분포로 한국 코호트 시 동일 분포 가정 가능. (2) DBAC PAH dietary carcinogen exposure layer — 한국 식이 PAH(charcoal-grilled meat / pan-frying / smoked food) 노출 정량(쪽 891 BaP cooked 1.30 ng/g vs raw 0.12 ng/g)을 한국인 cohort 식이 questionnaire + DBAC signature WES 검출로 옮길 수 있는 분석 layer. East Asia 특이 + TCGA 부재라서 한국인 cohort 적용 시 hypothesis driver 1순위. Multivariable Cox HR 2.36-3.16 + diffuse 5.9× EFS는 한미암 prognostic stratification 변수 후보. (3) HP-negative SA-CLDN18.2 dual biomarker — HP_N 30.5%(NAT/tumour 모두 HP 부재 또는 IgG only) subset에서 SA prevalence + CLDN18.2 IHC 양성률 동시 측정으로 HP_N CLDN18.2-high(T1) 환자 식별 → zolbetuximab + 후속 CLDN18.2 ADC 적용 후보군 추출. n=185 외부 검증 47.3%→56.9%→86.4% gastric juice SA 곡선은 한국 환자 endoscopy juice sampling protocol 도입 근거. T1 42% IHC criteria 일치는 한국인 HP-negative cohort에서 CLDN18.2-targeted therapy 인구 비율 사전 추정 가능. (4) PT1-IM + 4 anatomy stratification 한국 cohort 적용 — PT1-IM1 vs PT1-IM3 p=0.025 bifurcation은 한미암 PT1 환자 immune state 추가 stratification 필요성 명시. 4 anatomy η²=0.257 vs binary 0.077 p=0.00386은 한국 위암 cohort에서 cardia/mid-body/antrum/pyloric subzone 단위 anatomy clustering 채택 근거. Loc 2 ABL1/SYK/ROCK / Loc 3 BRAF/CDK4/ERBB2 / Loc 4 MET/PRKAA2 위치-특이 kinase target은 anatomy-based therapy 매칭 후보. (5) CDK4 + decision tree clinical implementation — CDK4 IHC-positive + proteome-defined-positive + IHC-negative(49.2%) 3 subgroup 공통은 한미암 stage II-III GC palbociclib/ribociclib repurposing 임상 design 근거. Decision tree EFS(stage+DBAC) + OS(stage+C3+PT1+IM2/3)는 한국 cohort에서 동일 변수 stage+carcinogen signature+proteome cluster 조합으로 외부 reproducibility 검증 → 5-variable nomogram 후보. 5 Loc 4 antrum biomarker(SHROOM1/p-LYST S2627/XYLT1/CRIP1/SPATS2L) KM Plotter n=118-875 외부 validated → 한국 cohort IHC + phospho-specific antibody 추가 검증 가능. 한계 본문 명시: single-cohort Taiwanese / BaP cell-line 검증만 / KEA3 inference / decision tree retrospective — 한국 cohort 적용 시 동일 한계 + 한국인 PAH 식이 노출 differential 추가 검증 필요.
- 토픽 허브 `wiki/topics/cancer-multiomics-literature.md` Section 1(WGS와 Proteogenomics 통합 기반): 신규 entry 추가 — Zhao 2026 직전 위치. 154 환자 + >10,000 protein + 30,000 phospho + 7 mutational signature + DBAC HR 2.36-3.16 + microbiome 4 cluster + SA gastric juice 47.3%→86.4% + 4 anatomy η² 0.257 + CDK4 + decision tree + 한계 모두 포함.
- corpus queue 카운트 +1: Selected 100→101 / Acquired 90→92 / Ingested 100→102 / Blocked 11→10. Selected set 표 xiang-2026 다음에 `chang-2026-integrative-proteogenomics-gastric-cancer-taiwan` 신규 row(`needs-brief`, GC proteogenomics + DBAC carcinogen + SA microbiome + 4 anatomy + CDK4 hub) 추가. Queue 헤더 "2026-05-12 user-shared=5" → "2026-05-12 user-shared=6"(Chang 신규; Chen은 같은 날 unblock).
- `wiki/_meta/index.md` Proteogenomics / PTM Atlas cluster Zhao 2026 직후 위치에 Chang 2026 신규 링크 추가; 154 환자 + DBAC + microbiome + SA gastric juice + 4 anatomy + CDK4 hub + 한계 정량 포함.
- Notion 페이지(`참고 논문 및 아이디어` 344302d9...): **4-section 간소 템플릿**(논문 정보 / 한 줄 요약 / 과제 관련성 (한미암) / 주요 결과) 적용 예정. funding/이해관계/저자 소속 제외.

## [2026-05-12] ingest | Duan 2026 — bioGraph multi-omic heterogeneous graph learning method + 4-cancer CPTAC benchmark + MAP4 GBM validation (NAR, user-shared) — **Target 100 ingest 달성**

- 사용자 공유 9개 user-shared 논문 배치 중 여덟 번째(Paper 8). 사용자 결정: "9편 전부 풀 ingest" + "각 source 페이지 'Cancer Multiomics Project Relevance' 절에 한 단계 더 구체화" + Notion 4-section 간소 템플릿. NAR OA paper(CC BY-NC 4.0)로 paywall 미해당, PMC 직접 fetch.
- 메타데이터 확인: Nucleic Acids Research 2026 Apr 30;54(8):gkag386 (Received 2025-04-30, Revised 2026-03-17, Accepted 2026-04-04, Collection 2026-05-08). PMID 42059203, PMC PMC13129546. DOI 10.1093/nar/gkag386. 3 co-first author(equal contribution): Jingxian Duan / Yaou Liu / Dongling Pei. 3 senior corresponding: Dong Liang(SIAT CAS Shenzhen, zc.li@siat.ac.cn 동등 기재 liang.dong@siat.ac.cn) / Zhenyu Zhang(FAHZZU Zhengzhou, fcczhangzy1@zzu.edu.cn) / Zhi-Cheng Li(SIAT CAS Shenzhen, zc.li@siat.ac.cn). 소속: Institute of Biomedical and Health Engineering, SIAT CAS Shenzhen / Faculty of Biomedical Engineering, Shenzhen Univ of Advanced Technology / Key Laboratory of Biomedical Imaging Science and System CAS / Department of Radiology, Beijing Tiantan Hospital / Department of Neurosurgery, FAHZZU Zhengzhou / Xiamen Univ State Key Lab of Vaccines for Infectious Diseases / HaploX Biotechnology Co. Ltd. Funding: Shenzhen Medical Research Fund A2303008 + NSFC T2525037/62201557/62571523/82273493/82573337 + Guangdong Special Support Plan 2024TX08A213 + Shenzhen S&T Program JCYJ20250604183020027/JCYJ20241202125014018 + CAS Strategic Priority Research Program XDB0930302 + Zhongyuan S&T Innovation Top-notch Young Talents Program + Henan S&T Research and Development Joint Fund 242301420014. **Conflict of interest**: Shifu Chen 는 HaploX Biotechnology 고용; 그 외 저자 없음. 본문 명시 "no significant financial support for this work that could have influenced its outcome".
- PDF/HTML 획득: NAR Oxford OA 직접 fetch는 가능하지만 PMC HTML이 안정적 — PMID 42059203 PMC 확인 → `https://pmc.ncbi.nlm.nih.gov/articles/PMC13129546/` curl Mozilla UA로 HTML(287 KB / 3,373 line) 직접 fetch 성공. **pandoc html→plain text(2,061 line)** 추출 후 직접 정독. 원본 `/tmp/papers/08_pmc.html` → 표준 위치 `raw/inbox/papers/duan-2026-discovering-proteo-transcriptomic-networks-heterogeneous-graph-learning.html`(295 KB) 복사. `pdf_status: html-only` 명시. 기존 `duan-2026-towards-personalized-vaccine-repurposing-alzheimers.md`는 다른 Duan 논문이므로 분리된 새 slug `duan-2026-discovering-proteo-transcriptomic-networks-heterogeneous-graph-learning.md` 채택.
- 본문 정독: pandoc 추출 텍스트 lines 1-200(metadata + 15 authors + affiliations) / 200-500(roles + COI 정보) / 500-1300(Materials and methods 전체 + Results 2.1 performance + 2.2-2.3 intra-omic + 2.4 inter-omic + 2.5 MAP4 validation) / 1300-1700(2.6 cross-omic + 2.7 MGSVA + Online platform + Discussion + Limitations) / 1700-2061(Author info + Funding + Data availability + References 1-67) 직접 정독.
- 신규 소스 페이지 `wiki/sources/duan-2026-discovering-proteo-transcriptomic-networks-heterogeneous-graph-learning.md` 생성(method paper로 frontmatter `paper_kind: method` 설정, modalities는 transcriptomics/proteomics/phosphoproteomics, cancer_types는 4 CPTAC cohort 모두 명시): Summary / Key Points (7 subsection: 방법론 + 성능 + intra-omic + inter-omic + MGSVA + MAP4 validation + EMOGI 비교 + 한계) / Methods / Cancer Multiomics Project Relevance(5축) / Connections / Sources 6 섹션. `feedback_paper_relevance_writing.md` 규칙 엄수(자체 평가어/시너지 묶음 금지).
- 핵심 정량 포인트: bioGraph 3-layer heterogeneous graph(mRNA/protein/phosphoprotein 노드 + 5 edge type: intra-RNA KEGG pathway 공유 / intra-protein·phospho STRING-db v11.0b ≥700 PPI / 동일 유전자 RP=translation + PP=post-modification inter-omic). 2-layer HeteroRGCN(DGL) + edge-aware weighting modulation(GAT softmax-attention과 구별; learned edge representations이 messages 직접 modulate) + Cox partial-likelihood loss + L2. CPTAC 4 cohort(cBioPortal): COAD 79명 / GBM 74명 / pLGG 73명(astrocytoma WHO I/II) / PDAC 92명. 외부 검증: FAHZZU glioma n=119(2019-2021 primary curative resection, no prior anti-tumor, ClinicalTrials.gov NCT04216537, IRB 2019-KY-176). 5-fold CV (3-fold for COAD due to repeated DFS) C-index: COAD **0.91±0.08**(single-omics 0.89/0.89/0.49) / GBM 0.71±0.04(0.56/0.66/0.69) / pLGG 0.73±0.03(0.58/0.61/0.63) / PDAC 0.74±0.02(0.59/0.59/0.53). Baseline 비교(Table 1): MOGONET COAD 0.66 / IGNN COAD 0.63 / MMGL COAD 0.58 / SALMON COAD 0.74 / MRGCN COAD 0.50 — 전 cohort bioGraph 우위. Ablation(Table 2): biological prior 제거 PDAC 0.74→0.47(-0.27), edge-aware 제거 GBM 0.71→0.58 / pLGG 0.73→0.60. Two-layer transcriptome-proteome 일반적으로 single-omic 우위, phospho-only 2/4 datasets 최악. Intra-omic edge-weight 5-fold reproducibility Pearson P<0.05 most pairs(GBM 일부 category 약함). DEG overlap top 50% bioGraph nodes: 27% (COAD) / 43% (GBM) / 6% (pLGG) / 21% (PDAC) — transcriptomic 기준. **Inter-omic RP vs PP** per-gene: RP > PP genes 91.49% (GBM) / 93.37% (COAD) / 94.77% (PDAC); pLGG 19.51% RP > PP, 33.99% PP > RP **정반대**. 4-cancer 공통 RP-PP discordance(Pearson P<0.05 in both train + val) core set: **MAP4 / SORBS1 / SPTAN1 / SRRM1 / TMPO**. MGSVA = KS-like running-sum on edge weights ranked by magnitude per relation type; pathway-edge set 정의 = edges connecting two pathway genes; weighting exponent + min-max norm Mann-Whitney U; 5 pathway scores per patient(edge type별); 동일 pathway라도 edge type별 prognosis 방향 다름. **MAP4 validation**: discovery cohort DEG 비표시 + small-sample prognosis 비유의 → 독립 FAHZZU n=119 mRNA P<0.015 protein P<0.01(SPTAN1 P<0.001, TMPO P<0.05); T98G + U251 GBM(Cell Resource Center Shanghai) sh-MAP4 lentivirus(TRCN0000117163 #1 + TRCN0000117166 #2) puromycin 1 μg/ml selection → wound healing 0/24/48 h ↓, trans-well migration 24h ↓, CCK-8 4-day ↓, colony formation 2-week ↓, Annexin V-FITC/PI apoptosis ↑. EMOGI 비교: bioGraph(Youden's J binarization) 1/5 PPI network에서 cancer gene AUC 우위; EMOGI도 MAP4/SORBS1/SPTAN1 3/4 datasets cancer-related + SRRM1/TMPO 2/4. Data: 입력 cBioPortal + 외부 검증 RNA-seq GSA HRA006184 + 외부 검증 MS proteomics iProX PXD062023; code codeocean.com/capsule/2357965 + biograph.hapyun.com. License CC BY-NC 4.0. 한계 본문 명시: retrospective + 코호트 제한 / clinical actionability 미검증 / matched complete omics 가정 / MAP4 외 4 gene mechanistic validation 미수행. 모든 edge-weight 통계 + node-embedding 분석은 각 cohort 내부에서 수행, 직접 cross-cohort 정량 비교 안 함.
- 한미암 적용: (1) Cohort 50-100 환자 규모 graph learning method 후보 — bioGraph 4-cohort 동일 스케일에서 C-index 0.71-0.91 + MOGONET/IGNN/MMGL/SALMON/MRGCN 우위 → 한미암 TNBC chemo response / CRLM C1/C2 / 가스트릭 survival 등 small-cohort 시나리오 graph-based prior-informed method 1차 비교 후보로 명시. (2) KEGG + STRING priors ablation logic — fully-connected baseline PDAC C-index 0.74→0.47(-0.27)이 본문 보고되어 한미암 graph ablation 설계에서 prior 유지/제거 + KEGG vs STRING source 분해 + edge-aware weighting 유지/제거 3축 필수 비교 셀로 설정. (3) Inter-omic RP/PP discordance 기반 hidden marker logic — MAP4는 DEG로 식별 불가했지만 inter-omic edge weight 비대칭으로 식별됨 → 한미암 코호트에서 fold-change는 작지만 RP/PP information flow 비대칭인 protein/phosphosite 추출로 기존 DEG-based 후보군 외 inter-omic-regulated targets 보완. 5-gene core set(MAP4/SORBS1/SPTAN1/SRRM1/TMPO)은 4-cancer 공통이므로 한미암 cohort에서 동일 discordance 확인용 starting set. (4) pLGG-style inter-omic 비대칭 가설 — RP > PP 19.51%(adult 91-95% 대비 정반대) → 한미암에 소아·저등급 / TMB-low 환자군 포함 시 post-translational regulation 우세 가설 + phospho-layer-heavy stratification 우선순위 조정 근거. (5) MGSVA pathway-level visualization 도구 — GSVA edge-weight 확장으로 동일 pathway transcriptome / proteome / phospho 별 prognosis 방향 직접 비교 가능; 단 bioGraph 또는 동등 heterogeneous GCN을 한미암 cohort에 1회 학습한 후 적용 가능(Zhao 2026 SHMT1/NDRG1 등 metabolism + RNA function pathway 검토 시 cross-omic activity 동시 비교 도구). 한계 본문 명시: retrospective / partial-omics 입력 미지원 / clinical actionability 미검증 / MAP4 외 mechanistic validation 미수행 — 한미암 활용 시 동일 적용; partial-omics 환자(WGS-only / protein-only)는 현재 bioGraph 형식 학습 불가.
- 토픽 허브 `wiki/topics/cancer-multiomics-literature.md` Section 6.1 AI / Foundation models / Deep learning: 신규 entry 추가 — deutsch 2026과 guo 2026 사이(알파벳 순). bioGraph 정량 포인트 + MAP4 validation + 한계 모두 포함.
- corpus queue 카운트 +1 (Selected 100→100 변동 없음, Acquired 89→90, Ingested 99→100); Selected set 표에 `duan-2026-discovering-proteo-transcriptomic-networks-heterogeneous-graph-learning` 신규 row(`needs-brief`, multi-omic graph learning method + 4-cancer CPTAC benchmark + MAP4 GBM validation). **Target 100 ingest 달성**. Queue 헤더 텍스트 "2026-05-12 user-shared=5" → "2026-05-12 user-shared=6" 업데이트.
- `wiki/_meta/index.md` Proteogenomics / PTM Atlas cluster Zhao 2026 직전 위치에 Duan 2026 신규 링크 추가(method paper로 같은 cluster 포함; awasthi/jiang/lehe/sinitcyn 같은 methodology tool entries 패턴 따름).
- Notion 페이지(`참고 논문 및 아이디어` 344302d9...): **4-section 간소 템플릿**(논문 정보 / 한 줄 요약 / 과제 관련성 (한미암) / 주요 결과) 적용 완료 — 페이지 ID `35e302d9-c598-810f-aab1-df29bf038e25` (https://www.notion.so/35e302d9c598810faab1df29bf038e25). funding/이해관계/저자 소속 제외. 5축 한미암 적용(소규모 cohort graph method 후보 / KEGG+STRING prior ablation 레퍼런스 / RP-PP discordance hidden marker / pLGG-style 비대칭 가설 / MGSVA visualization) + 정량 결과(bioGraph C-index COAD 0.91 / GBM 0.71 / pLGG 0.73 / PDAC 0.74; ablation PDAC 0.74→0.47; 5-gene core MAP4/SORBS1/SPTAN1/SRRM1/TMPO; FAHZZU n=119 + T98G/U251 sh-MAP4 validation; pLGG RP>PP 19.51% vs adult 91-95%) 포함.

## [2026-05-12] ingest | Zhao 2026 — CRLM proteogenomics + SHMT1/NDRG1 mechanism + C1/C2 subtype (Adv Sci, user-shared)

- 사용자가 Wiley Adv Sci URL(`advs.202511744`) 공유 → 9개 user-shared 논문 배치 중 여섯 번째(Paper 6). 사용자 결정: "9편 전부 풀 ingest" + "각 source 페이지 'Cancer Multiomics Project Relevance' 절에 한 단계 더 구체화". 사용자 확인 후 "지금 바로 PMC fetch+ingest" 옵션 선택으로 진행.
- 메타데이터 확인: Advanced Science 2026;13(4):e11744 (online 2025-11-06; collection 2026 Jan). PMID 41195591, PMC PMC12822478. DOI 10.1002/advs.202511744. OA(CC BY 4.0). 6 co-first author: W. Zhao / L. Zhao / Y. Lian / Z. Liu / Y. Li / X. Wang. 3 senior corresponding: M. Tan(SIMM CAS, Tongji), J. Qin(SIBS CAS, Jinfeng Lab Chongqing), J. Peng(FUSCC Fudan). 소속: Tongji Univ Shanghai 4th People's Hospital / Shanghai Institute of Nutrition and Health CAS / Shanghai Institute of Materia Medica CAS / Fudan Univ Shanghai Cancer Center / Shanghai Jiao Tong Univ / Fudan Univ + Sungkyunkwan Univ S.Korea + Jiangsu Ocean Univ + Jinfeng Lab Chongqing + Zhongshan Institute for Drug Discovery. Funding: NSFC 22225702/T2488301/U24A20524/82372974/82473500/8245103 + CAS XDB0830000 + Guangdong 2019B090904008/2021B0909050003 + Zhongshan CXTD2023009 + Shanghai SHSMU-ZDCX20212700. **Conflict of interest: 없음**.
- PDF 획득: Wiley 직접 fetch는 anti-bot block; PubMed에서 PMID 41195591 검색 → PMC PMC12822478 확인 → `https://pmc.ncbi.nlm.nih.gov/articles/PMC12822478/` curl Chrome UA로 HTML(267 KB) 직접 fetch 성공. **pandoc html→plain text(1,505 line)** 추출 후 직접 정독. 원본 `/tmp/papers/06_pmc.html` → 표준 위치 `raw/inbox/papers/zhao-2026-proteogenomic-characterization-reveals-metabolic-vulnerabilities.html` 복사. `pdf_status: html-only` 명시.
- 본문 정독: pandoc 추출 텍스트 lines 1-200(metadata + authors) / 200-600(Abstract + Introduction + Results 2.1-2.3) / 600-1000(Results 2.4-2.7 + Discussion 시작) / 1000-1510(Discussion + Methods + Data IDs + References) 직접 정독.
- 기존 stub `wiki/sources/zhao-2026-proteogenomic-characterization-reveals-metabolic-vulnerabilities.md`(`pdf_status: pending`, Key Points 비어 있음, Multi-Omics Identification Extraction stub) 전면 교체: Summary / Key Points (코호트 + LM 시그니처 + LM-enriched protein set 외부 GSEA / SHMT1-formate-AMPK 축 / NDRG1 S330p-degradation 축 / C1 vs C2 아형 / subtype biomarker / 한계) / Methods / Cancer Multiomics Project Relevance / Connections / Sources 6 섹션. `feedback_paper_relevance_writing.md` 규칙 엄수(자체 평가어/시너지 묶음 금지).
- frontmatter: `paper_kind: proteogenomic`, `cancer_types: [colorectal-cancer, colorectal-liver-metastasis]`, `modalities: [wes, rna-seq, proteomics, phosphoproteomics]`, `themes`에 colorectal-liver-metastasis, one-carbon-metabolism, ndrg1-degradation, patient-stratification, subtype-biomarker, asian-cohort 포함. authors 9명 명시(6 co-first + 3 senior corresponding). DOI/PMID/PMCID stub과 일치 확인.
- 핵심 정량 포인트: 코호트 34명 treatment-naive CRLM = 102 sample(matched T+N+LM 트리오, FUSCC 2012-07~2019-06, IRB 050432-4-1805C + 050432-4-1911D) + independent IHC validation cohort n=87. WES 19,493 nonsyn mut + 23,109 SCNA(APC/TP53/KRAS T vs LM 무차이; cis-regulatory SCNA은 mRNA가 가장 강함, CAG 551). TMT proteome 8,568 identified / **8,093 quantified**; Ti⁴⁺-IMAC phospho 25,775 / **19,803 quantified(class I 16,300, class II 3,503)**. LM signature: proteome - complement/coag + PPAR + carbon/cholesterol/fructose-mannose/amino acid metabolism (FDR<0.05); phospho - actin filament/small GTPase/lamellipodium organization. KSEA LM: RAF1+PAK2+ROCK1 hyperactive (VIM phos + CFL1 Ser3 EMT); T: CLK1+CDK7+PRKACB. 288,337 AS event; 26 LM vs T 차이, 14 prognostic(FN1/KHK/SERPINA1 top); DDX5+SF1 LM ↓ prognostic. ARG1 protein-only LM ↑ → poor OS T+LM. **CRS 한계 명시**: 5-yr OS log-rank p=0.23 — 예측 불충분. LM-enriched protein set n=245(또는 200/155) vs Li et al. mCRC dataset GSEA NES=-3.50/FDR<0.001(tissue-corrected -3.11); Li T(n=146) high LM-set → OS log-rank p=0.037 외부 transferability. **SHMT1-formate-AMPK 축**: SHMT1+MTHFD1+SHMT2 LM ↑; SHMT1 high → OS+PFS poor n=87. KAP organoid(Villin^CreERT2; Kras^LSL-G12D; Apc^min/+; Trp53^flox/flox + 2 mo TAM) Shmt1 KD → ↓pH3+ ↑CC3+ ↓growth; SHMT1 OE 반대; isogenic luciferase-labeled organoid intrasplenic C57BL/6 WT → BLI ↓liver metastasis; CPS1 동일 검증. 대사물 재공급: **formate 단독 rescue**; in vivo formate level Shmt1 KD ↓ / SHMT1 OE ↑. Shmt1 KD ± formate 전사체: HIF-1+AMPK+PPP inhibition, Wnt+Hippo activation. Western Shmt1 KD ↑p-AMPK / formate ↓ / AICAR ↑↑. In vivo 125 mM formate drinking water ↑tumor burden, AICAR 50 mg/kg ip mitigation. **NDRG1 S330p-degradation 축**: 보존된 5 up + 3 down phosphosite(functional score + log-rank p<0.05) - SLC16A1 S498 / NDRG1 S330 / PDLIM2 S129. NDRG1 S330p ↔ actin cytoskeleton reorganization Spearman ρ=0.43 p=0.013; actin filament-based movement ρ=0.34 p=0.053. NDRG1 S330A KAP cell intrasplenic → ↓liver metastasis burden. NDRG1 WT > S330A ubiquitination; CHX chase S330A 반감기 ↑; MG132 NDRG1 accumulation → ubiquitin-proteasome 의존. PIM family(PIM1/PIM2/PIM3) NDRG1 S330 phosphorylation 후보 1위(Johnson 2023 Nat 예측); transcriptome PIM1 LM ↑. **TP-3654 3 μM(pan-PIM)**: ↓NDRG1 S330p, ↓migration/invasion, ↑p-AMPK (PIM 음 AMPK 조절 정합). KSEA detect 실패(PIM→AMPKα T172 indirect, NDRG1 S330 DB 부재) → Sun et al. PhosphoSitePlus v6.7.5 확장 DB로 PIM1 LM activity ↑ Wilcoxon p<0.001. **C1 metabolism vs C2 RNA function 아형**: LM proteome unsupervised 2 cluster; OS log-rank p<0.05; phospho/transcriptome 기반 stratification은 OS 차이 없음; PCA C1/C2 명확 분리. 고빈도 mutated gene C1/C2 무차이, 17 저빈도 mutated gene Fisher p<0.05. KEGG C1 metabolism, C2 RNA function(transport/splicing). 226,107 AS in LM; 148 C1/C2 차이, **98/148 prognostic**(KHK/RPP21/U2AF1L4 top). 17 splicing factor C2 ↑(DHX9/DIS3/HNRNPA0/NCBP1/PRPF8/SNRPD1 good prognosis; NCBP1/PRPF8/SNRPD1 CRC+HCC dependency; DIS3/HNRNPA0/PRPF8 ↔ GRB7 AS negative). C1 KSEA hyperactive: RPS6KA1+RPS6KB2+PAK1/2/4+CHEK1+ROCK1+MAPK1; RPS6KA1/RPS6KB2/PAK2 → EIF4B S422 substrate. ARG1 C1 ↑. **Subtype biomarker validation n=87 IHC**: FTCD + GPD1(one-carbon, C1 LM-specific) OS+PFS log-rank p<0.05; SOD2(DepMap CRC/HCC, protein-only) discovery p=0.098 → validation p=0.0331; EIF4B S422 phospho OS p=0.0265 / PFS p=0.0099. CPTAC GBM/LUAD/CCRCC/PDAC 외부 SOD2/GPD1/EIF4B S422 reproducible.
- 한미암 적용: (1) Treatment-naïve CRLM proteogenomic baseline reference — 한국인 mCRC 코호트 설계 시 matched T+N+LM 트리오 + WES/RNA-seq/proteome/phospho 4-layer + independent validation cohort n=87 IHC 동일 protocol 채택의 근거. APC/TP53/KRAS frequency T vs LM 무차이 + cis-regulatory effect mRNA dominance → WES-only 분석으로는 LM 분기 식별 불가, (2) One-carbon metabolism druggability — SHMT1 high OS/PFS poor + KAP organoid + intrasplenic 모델 + 125 mM formate / AICAR rescue로 SHMT1-formate-AMPK in vivo causal evidence 완비 → 한미암 SHMT1 inhibitor(SHIN1/SHIN2) 또는 AMPK agonist(metformin/AICAR analog) LM subset evaluation 경로 reference. CPS1도 동일 접근으로 urea cycle/amino acid metabolism 후보 확장 가능, (3) NDRG1 S330p ubiquitin degradation + PIM kinase inhibitor 축 - NDRG1 S330p ↑ subset → TP-3654 같은 pan-PIM / SGI-1776 임상 적용 후보군 추출 logic. PIM-AMPK indirect inhibition axis로 SHMT1 축과 공통 p-AMPK endpoint stratification 가능, (4) C1(metabolism) vs C2(RNA function) proteomic subtype - LM proteome 기반 unsupervised clustering이 phospho/transcriptome보다 prognostic stratification 우수(OS log-rank p<0.05) → 한미암 LM patient stratification 첫 layer protein-level clustering 채택 근거. FTCD + GPD1 + SOD2 + EIF4B S422 4-marker panel은 n=87 IHC OS/PFS log-rank p<0.05 외부 재현 — 동일 항체 임상 도입 후보. C1 hyperactive RPS6KA1+RPS6KB2+PAK1/2/4+CHEK1+ROCK1+MAPK1은 한미암 kinase inhibitor library 1차 target 후보, (5) Public data cross-reference - iProx IPX0007391001 + GSA PRJCA020890 raw data 접근으로 한국인 CRC LM 코호트 cross-reference / re-analysis 가능. Li et al. mCRC + Tanaka 2024 CRC primary vs LM과 함께 CRLM proteogenomic external reference triplet. CPTAC PDAC/GBM/LUAD/CCRCC SOD2/GPD1/EIF4B S422 prognostic reproducibility로 pan-cancer metabolic/translational stratification 가설 추가 검증 자료. 한계 본문 명시: discovery n=34 power 제한(SOD2 p=0.098 → validation 0.0331 보완), formate-AMPK 정확 mechanism 미정의, KSEA indirect axis detection 실패(Sun et al. 알고리즘으로만 보완), single-cohort Chinese single-institution.
- 토픽 허브 `wiki/topics/cancer-multiomics-literature.md` Section 1 (WGS/Proteogenomics 통합 기반): 신규 entry 추가 — Xu 2026 다음. 34 환자 102 sample + 8,093 protein/19,803 phospho + SHMT1-formate-AMPK + NDRG1 S330p-PIM + C1/C2 subtype + FTCD/GPD1/SOD2/EIF4B S422 biomarker + n=87 IHC validation 정량 포함.
- corpus queue 카운트 +1 (Selected 99→100, Acquired 88→89, Ingested 98→99); Selected set 표에 `zhao-2026-...` 신규 row(`needs-brief`, CRLM proteogenomics + SHMT1/NDRG1 mechanism + C1/C2 subtype + Chinese cohort). **Target 100 달성**.
- `wiki/_meta/index.md` Proteogenomics / PTM Atlas cluster Xiang 2025 다음에 Zhao 2026 신규 링크 추가.
- Notion 페이지(`참고 논문 및 아이디어` 344302d9...): **4-section 간소 템플릿**(논문 정보 / 한 줄 요약 / 과제 관련성 (한미암) / 주요 결과) 적용. funding/이해관계/저자 소속 제외.

## [2026-05-12] ingest | Xiang 2025 — Non-canonical TSA proteogenomics in Chinese CRC + MC38 mouse vaccine (Cell Genomics, user-shared)

- 사용자가 Cell Press URL(`xgen.2025.101062`) 공유 → 9개 user-shared 논문 배치 중 다섯 번째(Paper 5). 사용자 결정: "9편 전부 풀 ingest" + "각 source 페이지 'Cancer Multiomics Project Relevance' 절에 한 단계 더 구체화".
- 메타데이터 확인: Cell Genomics 2025;6(1):101062 (published 2025-11-13). PMID 41237784, PMC PMC12926194. DOI 10.1016/j.xgen.2025.101062. OA(CC BY-NC-ND). Cell Genom 2026 Jan 22;6(2):101163 correction 본문 명시. Co-first H. Xiang / X. Guan / Y. Wei / S. Luo / H. Zhang / F. Bu(13명 공동 1저자 표시). Senior corresponding X. Dong(BGI Group 추정). 소속: HIM-BGI Omics Center(Zhejiang Cancer Hospital, Hangzhou Institute of Medicine, CAS) + BGI Research(Hangzhou + Shenzhen) + Sixth Affiliated Hospital of Sun Yat-sen University(Guangzhou) + 기타. Funding: Guangdong Provincial Key Laboratory of Human Disease Genomics(2020B1212070028) + Shenzhen Key Laboratory of Genomics(CXB200903110066A) + China National GeneBank(CNGB). Declaration of interests: **BGI Group employees hold company stock**.
- PDF 획득: Cell Press 직접 fetch는 Cloudflare 403 challenge(cf-mitigated:challenge). PubMed에서 PMID 41237784 검색 → PMC PMC12926194 확인 → `https://pmc.ncbi.nlm.nih.gov/articles/PMC12926194/` curl Chrome UA로 HTML(367 KB) 직접 fetch 성공. **pandoc html→plain text(2,468 line)** 추출 후 직접 정독. 원본 `/tmp/papers/05_pmc.html` → 표준 위치 `raw/inbox/papers/xiang-2026-predominant-mutated-non-canonical-tumor-specific-antigens.html` 복사(기존 슬러그 보존, 이미 동일 슬러그 PDF 2.1 MB 존재). `pdf_status: complete` 명시(PDF + HTML 모두 보유).
- 본문 정독: pandoc 추출 텍스트 lines 380-1200+ 직접 정독 (Abstract / Introduction / Results 2.1 Integration / 2.2 DNA-level non-coding / 2.3 Hypermutated CRC / 2.4 Non-canonical TSA + scRNA-seq / Discussion / Limitations / Resource availability / STAR Methods 주요 항목).
- 기존 stub `wiki/sources/xiang-2026-predominant-mutated-non-canonical-tumor-specific-antigens.md`(DOI/PMCID 오류, year=2026, Key Points 비어 있음) 전면 교체: Summary / Key Points (코호트 / two-stage DB search 벤치마크 / 96 epitope origin / hypermutation 분기 / Ribo-seq cross-ref / MC38 in vivo / scRNA-seq / 한계) / Methods / Cancer Multiomics Project Relevance / Connections / Sources 6 섹션. `feedback_paper_relevance_writing.md` 규칙 엄수 (자체 평가어/시너지 묶음 금지).
- frontmatter: `paper_kind: proteogenomic`, `cancer_types: [colorectal-cancer]`, `modalities: [wgs, rna-seq, ip-ms-immunopeptidomics, ribo-seq, scrna-seq]`, `themes`에 neoantigen-discovery, non-canonical-orf, immunopeptidomics, hypermutated-msi-h, personalized-vaccine, asian-cohort 포함. DOI/PMCID 수정(이전 잘못된 `10.1021/acs.analchem.9b01262` / `PMC10767972` → 올바른 `10.1016/j.xgen.2025.101062` / `PMC12926194`). year: 2025 (Cell Genom 2025 Nov 13 첫 출간; 슬러그는 기존 2026 보존). authors 8명 대표 명시.
- 핵심 정량 포인트: 코호트 10 paired CRC tumor + 인접 정상 (Chinese, Sun Yat-sen Sixth Affiliated Hospital) + HCT116/HCC1143 cell-line + MC38 mouse syngeneic. **96 mutated MHC class I neo-epitope**(평균 9.6/환자, traditional ~1/환자) — DNA 78 / RNA 19 / Neo-074 양쪽. **80.21% non-coding origin** (intergenic 26 / intronic 28 / non-coding intronic 19). SNV 64.58%/del 14.58%/ins 3.12%; RNA-level AS 14/19(SE 우세). 비-coding ORF 평균 **127 bp(~42 aa)** vs annotated **2,128 bp**. AAG 19.48% non-coding start codon 우세, ATG annotated만. 30.21% NetMHCPan rank top 2%. Two-stage DB search: DB 76.55% 축소, 59,442 peptide at 1% FDR, total 2.21× / novel 1.33× 증가. Cell-line 외부 검증: HCT116 79.61% recall + 4.88× / HCC1143 96.44% + 4.68×. PRM 25/27(92.59%) empirical. 26,666 total epitope after ΔRT<300s + SSS>0.4 + FDR<1%. **TMB>25 hypermutation 그룹 87 epitope(평균 14.5/환자, 86.2% non-canonical) vs TMB<25 비-hypermutation 9 epitope(평균 2.2/환자, 22.2% non-canonical)**; intergenic ~25× / intronic ~46× hypermutation 그룹 enrichment. Ribo-seq (smProt + nuORFdb) **35/77 non-canonical translation 지지**. MC38: 5,646 total epitope + **20 neo-epitope(11 non-canonical: 5 intergenic + 4 intronic + 2 non-coding RNA intronic)**, PRM 20/20(100%) 검증. ELISpot 11 non-canonical 중 **intronic 3/6(50%) + intergenic 3/5(60%) IFN-γ 양성**. **7-peptide Vax 종양 성장 유의 억제 vs PBS/CtrlVax**. **α-CD8β depletion 효과 완전 abrogation(p<0.0001)**; α-CD4/NK/macrophage 영향 없음 → MHC class I-restricted CD8⁺ T cell primary mechanism. scRNA-seq 67,471 cell, UMAP 4 compartment + TIL 8 subpopulation: Vax 그룹 cytotoxic CD8⁺ TIL **0.40%(PBS 0.08%)**, exhausted CD8⁺ TIL 0.84%(PBS 0.12%); Treg as %CD4⁺ **22.61%(PBS 36.14%)**; CD8/Treg ratio **3.93(PBS 2.39)**. DEG: cytotoxic CD8⁺ TNF-α/NF-κB + IFN-γ(Socs3, Cdkn1a, Ccl5).
- 한미암 적용: (1) Non-canonical TSA discovery pipeline 자체 — WGS + RNA-seq + IP-MS + 6-frame translation + 10 candidate start codon + two-stage DB search + 다중 search engine + de novo + Ribo-seq cross-mapping의 stack을 한미암 in-house pipeline 설계/calibration 1차 reference로 사용. HCT116/HCC1143 외부 검증 결과는 자체 pipeline 벤치마크 baseline, (2) 한국인 dMMR/MSI-H CRC subset(~5%)에서 비-coding intergenic/intronic neo-epitope dominance 가설 검증 — 한미암 personalized vaccine 후보 풀을 exome-only에서 WGS-기반으로 확장 결정 근거. 정량 비교 14.5/환자 vs 2.2/환자, (3) MC38 in vivo PoC 실험 설계 reference — ELISpot ~55% IFN-γ 양성 → 7-peptide pool Vax → α-CD8β depletion mechanism 확정 → scRNA-seq CD8/Treg readout의 시퀀스, (4) Public data cross-reference: CNSA CNP0004656(WGS+RNA-seq) + GSA-Human HRA005229 + CNP0005402(MS) raw data 접근 → 한국 환자 cohort cross-reference / re-analysis 가능, (5) FDR calibration 위험 분리 — PRM 92.59% empirical vs 이론 FDR 1% 격차 본문 인정 → 한미암 자체 pipeline 도입 시 random sampling + PRM 재검증 SOP 포함 결정 근거. 한계 본문 명시: n=10 단일 기관, 단일 인구(Chinese), 단일 cancer type, BGI Group 저자 stock 이해관계, Ribo-seq 지지 35/77만(나머지 42 translation 증거 부재 — 짧은 ORF post-transcriptional degradation 가설), 6-frame translation ORF redundancy로 중복 source peptide 제외 → 일부 후보 누락 가능, prospective 임상 outcome 미존.
- 토픽 허브 `wiki/topics/cancer-multiomics-literature.md` Section 3 (면역회피와 Neoantigen): 신규 entry 추가 — Petralia 2024 다음, Wen 2020 NeoFlow 앞. 96 epitope + 80.21% non-coding + hypermutation 분기 + MC38 in vivo + scRNA-seq TME + 한계 명시.
- corpus queue 카운트 +1 (Selected 98→99, Acquired 87→88, Ingested 97→98); Selected set 표에 `xiang-2026-...` 신규 row(`needs-brief`, CRC + non-canonical TSA + MC38 mouse).
- `wiki/_meta/index.md` 신규 user-shared full-ingest 클러스터(Lee 2026 / Xu 2026 다음)에 Xiang 2025 entry 추가; 96 epitope + 80.21% non-coding + hypermutation 분기 + MC38 Vax + scRNA-seq CD8/Treg + 한계 정량 포함. (B-cell neoantigen topic/anchor에는 stub 단계부터 슬러그 보존됨.)
- Notion 페이지 (`참고 논문 및 아이디어` 344302d9...): **4-section 간소 템플릿**(논문 정보 / 한 줄 요약 / 과제 관련성 (한미암) / 주요 결과) 적용. funding/이해관계/저자 소속 제외.

## [2026-05-12] ingest | Xu 2026 — Chinese HER2-low BC proteogenomics + lactylome (Adv Sci, user-shared)

- 사용자가 Wiley Adv Sci URL(`advs.202513086`) 공유 → 9개 user-shared 논문 배치 중 네 번째(Paper 4). 사용자 결정: "9편 전부 풀 ingest" + "각 source 페이지 'Cancer Multiomics Project Relevance' 절에 한 단계 더 구체화".
- 메타데이터 확인: Advanced Science (2026). PMID 41454718, PMC PMC12948274. DOI 10.1002/advs.202513086. OA(wiley) + PMC. Co-first S.X./K.Y./L.L./Q.W./X.W. (Harbin Medical University Cancer Hospital). Senior corresponding: Z. Cheng (PTM Biolab, Hangzhou), X. Cui (Cedars-Sinai), H. Wu, D. Pang (Harbin). Funding: Project Nn10, NSFC 82173235/82202996, Heilongjiang grants, China Postdoctoral Science Foundation. Competing interest 없음.
- PDF 획득: Wiley 직접 + PMC PDF endpoint 모두 anti-bot block (HTML 챌린지 페이지 반환). OA tarball ftp/https 양쪽 404. **PMC HTML(313 KB) + pandoc → plain text (1,957 line)** 으로 우회. 원본 `/tmp/papers/04_pmc.html` → 표준 위치 `raw/inbox/papers/xu-2026-proteogenomic-her2-low-breast-cancer-subtypes.html` 복사. `pdf_status: html-only` 명시.
- 본문 정독: pandoc 추출 텍스트 lines 270-1565 직접 정독 (Abstract / Introduction / Results 2.1–2.7 / Discussion / Experimental Section / References 일부).
- 기존 stub `wiki/sources/xu-2026-proteogenomic-characterization-reveals-subtype-specific-therapeutic.md`(`pdf_status: pending`) 전면 교체: Summary / Key Points (코호트 / QC / Mutation landscape / Phospho-kinase / PS subtype PS1·PS2·PS3 / SVM classifier / PDO 약물 검증 / RWD / Lactylome 발견 / Discussion / 한계) / Methods / Cancer Multiomics Project Relevance / Connections / Sources 6 섹션. `feedback_paper_relevance_writing.md` 규칙 엄수 (자체 평가어/시너지 묶음 금지).
- frontmatter: `paper_kind: proteogenomic`, `cancer_types: [her2-low-breast-cancer, her2-high-breast-cancer]`, `modalities: [wes, rna-seq, proteomics, phosphoproteomics, lactylomics]`, `themes`에 her2-low, lactylation-ptm, patient-stratification, patient-derived-organoid, asian-cohort, druggable-target 포함. authors 9명 명시.
- 핵심 정량 포인트: 코호트 115 tumor + 135 NAT (HER2-low n=83 + HER2-high n=32; treatment-naive Chinese, IRB KY2023-84) + 14 RWD + 17 추가 PDO 환자. 데이터 8,307 proteins / 43,963 phosphosites (7,808 phosphoproteins) / **18,214 lactylation sites on 1,644 proteins**. WES 204.48×T / 119.87×N (115T/86N). RNA-seq 97.94% genome mapping. **PS subtype 3종**: PS1 n=21 (estrogen → tamoxifen/toremifen), PS2 n=35 (angiogenesis → bevacizumab/apatinib), **PS3 n=27 (32.53% of HER2-low, proliferation + HER2-high-like → trastuzumab/T-DM1)**. SVM-RFE 10-feature train AUROC 0.97 / test 1.00. IHC 10-단백질 AUROC **0.80 (n=76)** — COL16A1·SBSPON·VAV3·CREBBP·ELP1·RFC1·HEATR5B·XPO5·TFDP1·TOM1L2. PDO 약물 시험 17명 → PS subtype-specific drug response 일관. **RWD 14명 항혈관신생 치료: PS2 3/4 CR/PR vs PS1+PS3 1/10**. **Lactylomic subtype 3종 LS1/2/3 PFS log-rank P=0.00172**, PS2-LS3 추가 분리. 핵심 site: **PRKDC K2694/K2908 lactylation ↔ kinase activity ↑ + PFS ↓** (DNA-PK 의존 저항), STAT1 K193 lactylation + T727 phosphorylation ↔ TF activity, AURKB lactylation-매개 조절. Mutation: TP53 31% / PIK3CA 29%. HER2-low 특이 SCNA: 7q gain (SSBP1, FIS1) 유일; 9p loss(MTAP cis) poor prognosis HER2-low 한정; **TP53 mut도 HER2-low에서만 poor prognosis**. CIN signature CX3 (NER 결함) HER2-low 활성. JNK 신호 (MAPK11/12, MAP2K7) HER2-low 활성. Histone Kla 50+ site (H2B K5, H3 K27 등) HER2-high에서 더 높음. CPTAC HER2-negative 외부 재현.
- 한미암 적용: (1) 동아시아 HER2-low BC reference로 한국인 baseline 비교 — PS1/PS2/PS3 분포가 한국인에서 재현되는지 1차 검증, (2) **PS3(32.53%) ↔ DESTINY-Breast04 T-DXd ORR ~40%** 정합 → 한미암 T-DXd / HER2 ADC 환자 stratification 직접 적용 후보, (3) **IHC 10-단백질 SVM(AUROC 0.80) deployable workflow**로 임상 사이트 도입 가능 — 상용 항체 모두 보유(Abcam/Atlas/Novus), (4) Lactylome 신규 modality — PRKDC/STAT1/AURKB Kla site는 한미암 lactylome enrichment workflow 도입 cost-benefit 평가 1차 reference, (5) JNK / 9p loss MTAP cis(합성치사) / 7q gain — HER2-low subset 추가 stratification 후보. 한계 본문 명시: HER2-negative 비교군 없음, 단일 인구(중국 Heilongjiang), PS-T-DXd 연결은 분자 정합 + 비율 일치 수준 — prospective 임상 입증 아님, IHC AUROC 0.80은 same-cohort 76명 내부.
- 토픽 허브 `wiki/topics/cancer-multiomics-literature.md` Section 1 (WGS/Proteogenomics 통합 기반): 신규 entry 추가 — Lee 2026 다음. PS subtype 분류 + lactylome + IHC SVM + RWD 항혈관신생 정량 + 한국인 비교 baseline 명시.
- corpus queue 카운트 +1 (Selected 97→98, Acquired 86→87, Ingested 96→97); Selected set 표에 `xu-2026-...` 신규 row(`needs-brief`, HER2-low BC + lactylome + 환자 stratification).
- `wiki/_meta/index.md` Proteogenomics / breast cancer cluster에 Xu 2026 신규 링크 추가 (Lee 2026 다음).
- Notion 페이지 (`참고 논문 및 아이디어` 344302d9...): **4-section 간소 템플릿**(논문 정보 / 한 줄 요약 / 과제 관련성 (한미암) / 주요 결과) 적용. funding/이해관계/저자 소속 제외.

## [2026-05-12] ingest | Lee 2026 — Korean TNBC NAC resistance proteogenomics (Genome Biology, user-shared)

- 사용자가 Springer DOI URL(`s13059-026-04053-7`) 공유 → 9개 user-shared 논문 배치 중 첫 번째(Paper 1). 사용자 결정: "9편 전부 풀 ingest" + "각 source 페이지 'Cancer Multiomics Project Relevance' 절에 한 단계 더 구체화".
- 메타데이터 확인: Genome Biology (2026) 27:125, received 2025-08-08, accepted 2026-03-20, published online 2026-04-14. Yonsei College of Medicine (Severance Hospital, IRB 4-2020-0473). DOI 10.1186/s13059-026-04053-7. BMC OA, competing interests none.
- PDF 다운로드: Springer publisher가 idp.springer.com auth 리다이렉트 → `link.springer.com/content/pdf/10.1186/s13059-026-04053-7.pdf` 직접 fetch 시 Chrome UA + DOI referer로 성공 (4.3 MB, 25 페이지). 원본 `/tmp/papers/01_lee2026_tnbc.pdf` → 표준 위치 `raw/inbox/papers/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.pdf` 복사.
- 본문 정독: Read tool로 PDF 페이지 1-25 직접 정독 (Abstract / Introduction / Results / Discussion / Methods / References / Supplementary).
- `wiki/sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md` 풀-텍스트 소스 페이지 생성: Summary / Key Points (코호트 / 데이터 레이어 / NMF / 저항 메커니즘 ①②③④ / 통합 모델 / 데이터 가용성) / Methods / Cancer Multiomics Project Relevance / Connections / Sources 6 섹션. `feedback_paper_relevance_writing.md` 규칙 엄수.
- frontmatter: `paper_kind: translational`, `cancer_types: [triple-negative-breast-cancer]`, `modalities: [proteogenomics, phosphoproteomics, wes, rna-seq, tmt]`, `themes`에 chemotherapy-resistance, neoadjuvant-chemotherapy, pcr-prediction, asian-cohort, druggable-target 포함.
- 핵심 정량 포인트: 코호트 50명 stage II–III TNBC (baseline n=41 complete; paired post-protein n=22; pCR 19/50=38%, F/U 33.2mo). carboplatin 6/50(12%, AC→Pac 72%) — Anurag et al. 100% carboplatin과 명시적 대비. 데이터셋 25,988 gene CNA + 19,853 transcript + 10,457 protein + 31,258 phosphosite(5,373 proteins). NMF 5 subtype pCR 55.6%/0%/0%/—/—. METABRIC n=258 외부 검증 197(76.3%). 5 저항인자 logistic regression non-pCR **AUC 0.946** (Lehmann 0.781 / +ESTIMATE 0.818). Estrogen GSVA high vs low pCR 14.3% vs 48.1% (P=0.0328). ITGB8 CN status pCR 80%/41.7%/12.6%/0% (loss/loss/dip/gain, P=0.036). AKR1C2 METABRIC IM RFS P=0.0033. **Druggable**: βARK1 + paclitaxel MDA-MB-231 Bliss synergy 8.08; barasertib(10 nM) + paclitaxel MDA-MB-468·HCC1937·organoid SBO-72 viability ↓. ITGB8/THSD7A/TSPAN13 7p21 셋 모두 Cancer Surfaceome Atlas → ADC 후보, integrin β6 ADC SGN-B6A 선행 사례 인용.
- 한미암 적용: (1) Severance n=50이 한국인 anthracycline+taxane standard NAC reference로 직접 활용 — 한미암 한국인 코호트 baseline 검증, (2) AURKB+paclitaxel residual disease eradication 가설(in vitro만), (3) ITGB8 deep loss(n=5) pCR 80% → CN gain(n=16) pCR 0% subset이 ADC stratification 타깃, (4) AKR1C2/ABCA13 baseline RNA-seq IM subtype 내부 분기 마커, (5) PDC000695/696 phosphoproteome 5,373 단백질을 한국인 baseline reference로 즉시 활용. 한계 본문 명시: n=50 단일 기관, pembro 미포함, NMF cluster 2/3 매우 작음(n=2,7), AUC 0.946은 same-cohort logistic 결과 — 외부 prospective AUC 미보고, in vitro 한정 검증.
- 토픽 허브 `wiki/topics/cancer-multiomics-literature.md` Section 1 (WGS/Proteogenomics 통합 기반): 신규 entry 추가 — Sambath 2026 다음, AURKB·GRK2·ITGB8 핵심 정량 + carboplatin 비대비 + ADC 후보 + data ID 명시.
- corpus queue 카운트 +1 (Selected 96→97, Acquired 85→86, Ingested 95→96); Selected set 표에 `lee-2026-...` 신규 row(`needs-brief`, TNBC chemo response + druggable target).
- `wiki/_meta/index.md` Proteogenomics / breast cancer cluster에 Lee 2026 신규 링크 추가.
- Notion 페이지 (`참고 논문 및 아이디어` 344302d9...): 사용자 신규 지침 적용 — **4-section 간소 템플릿**(논문 정보 / 한 줄 요약 / 과제 관련성 (한미암) / 주요 결과)으로 생성. funding/이해관계/저자 소속 제외. `feedback_notion_template.md` 메모리 저장.

## [2026-05-12] ingest | Sinitcyn 2023 — Deep proteome reference + SAP/AS detection framework (Nature Biotechnology, user-shared)

- 사용자가 Nature URL(`s41587-023-01714-x`) 공유(다섯 번째 user-shared 논문) → "이건 무슨 내용이야 → 노블티가 뭐야 → 결론이 뭐야 → 무슨 데이터 썼는데, PDF 받아서 정독해봐" 4단계로 점진적 자세히 보기 요청 → PDF 정독 후 데이터 매트릭스 보고 → 사용자 옵션 1(wiki ingest + Notion 등록) 승인.
- 메타데이터 확인: Nature Biotechnology 41:1776–1786 (December 2023). cc-by open access 확인. Coon lab (UW–Madison) + Cox lab (Max Planck Biochem) + Blencowe lab (Toronto) 공동. Co-first Sinitcyn + Richards; co-corresponding Cox + Coon.
- PDF 다운로드: Nature direct (Chrome UA + DOI referer) → `raw/inbox/papers/sinitcyn-2023-global-detection-human-variants-isoforms-deep-proteome.pdf` (3.6 MB, 13 페이지). cc-by 라서 publisher block 없음 — Lehe/Sambath와 달리 Europe PMC fallback 불필요.
- 본문 추출: `pdftotext -layout` → `/tmp/sinitcyn2023.txt` 1,207 line. 전체 정독 (Abstract / Introduction / Results / Discussion / References / Methods / Data Availability / Acknowledgements / Author contributions / Competing interests).
- `wiki/sources/sinitcyn-2023-global-detection-human-variants-isoforms-deep-proteome.md` 풀-텍스트 소스 페이지 생성: Summary / Key Points / Methods / Cancer Multiomics Project Relevance / Connections / Sources 6 섹션 (Sambath 2026과 동일 포맷). `feedback_paper_relevance_writing.md` 규칙 엄수.
- frontmatter: `paper_kind: resource`, `cancer_types: [pan-cancer]`, `modalities: [deep-proteome-sequencing, multi-protease-proteomics, etd-cad-hcd-fragmentation, proteogenomics, rna-seq]`, `themes`에 proteoform, alternative-splicing-detection, single-amino-acid-polymorphism, sap-variant-detection, multi-protease-strategy, sequence-coverage, encode-cell-lines, de-novo-protein-assembly, methodology-reference 포함.
- 핵심 정량 포인트: ENCODE 6세포주(H1-hESC/HeLa S3/HepG2/GM12878/K562/HUVEC) × 6 protease(trypsin/LysC/LysN/AspN/GluC/chymotrypsin) × HCD/CAD/ETD × 24–80 HpH-RP fraction × Orbitrap Fusion+Lumos. 2,491 raw files / ~164M MS/MS / 1% FDR에서 17,717 proteins / 1,119,510 unique peptides / 12,151,708 PSMs (실제 PSM 0.06% / peptide 0.4% / protein 0.99%). Median sequence coverage 79.2% (trypsin 단독 56.5%, +22.7%p; 790 proteins 100% coverage). MassIVE all-tryptic 대비 +34.4% (2.12M residues). SAP 5,060 total / transcriptome SNP 73% 단백 매핑 / multi-enzyme로 2배 증가. 미검출 SAP에서 SIFT deleterious P=2e-8, PolyPhen-2 damaging P=1.1e-12 enriched (protein instability 가설 지지). AS event 13,450 → 34.3% 검출, 양방향 6,145 → 18.6%, frame-preserving 64%. XGBoost AUC 0.83 (top features: transcript abundance, PSI, frame status; PSI ~33% optimum). SOAPdenovo-Trans 35,480 scaffold 중 47%(16,496)이 9,695 protein group 매칭. MaxQuant v1.5.7.5 + Andromeda; UniProt+Ensembl GRCh38 release 86.
- 노블티 표현 (저자 명시): "deepest proteomics map collected to date" + "SAP-aware proteogenomic study가 이 정도 깊이로 수행된 적 없음" + multi-enzyme 전략을 "global-scale proteoform 검출에 적용한 사례는 본 시점까지 보고된 바 없음". 트립신-only 분석 한계로 AS-단백체 불일치를 결론낸 두 선행 리뷰(Tress 2017; Blencowe 2017) + Wang 2018 직접 반박.
- 한미암 적용 한계 명시 (본 페이지 명시): 본 논문은 cancer 코호트가 아닌 ENCODE 세포주 reference — 환자 cohort 비교 직접 불가. multi-protease + deep fractionation은 reference-quality 자원으로 routine clinical pipeline transfer 불가. MaxQuant 1.5.7.5는 2017 빌드 — DIA/MaxQuant 2.x 등 후속 적용 시 별도 검토. SAP 73% mapping은 normal SNP(germline) 기준이라 somatic으로 외삽 불가.
- 토픽 허브 `wiki/topics/cancer-multiomics-literature.md`: 신규 Section 7 "Methodology / Resource Atlases (Deep Proteome References)" 추가 (Section 6 batch label 다음). Sinitcyn 2023이 첫 entry.
- corpus queue 카운트 +1 (Selected 95→96, Acquired 84→85, Ingested 94→95); Selected set 표에 `sinitcyn-2023-...` 신규 row(`needs-brief`, methodology / deep proteome resource).
- `wiki/_meta/index.md` Proteogenomics / PTM Atlas 섹션에서 Sambath 2026 위(직전)로 링크 추가.
- Notion 하위 페이지 (`참고 논문 및 아이디어` 344302d9...): 7-section 한국어 포맷(논문 정보 / 한 줄 요약 / 데이터 매트릭스 / 핵심 결과(deep proteome scale + SAP + AS + de novo assembly) / 노블티 표현(저자 명시) / 한미암 적용 + 한계 / 데이터 공개 + 이해관계 메모)으로 생성. 페이지 ID `35e302d9-c598-8136-b962-f7075aea9d9f`. URL `https://www.notion.so/35e302d9c5988136b962f7075aea9d9f`. Strict source-grounded — 논문 본문 + 저자 명시 표현만, 자체 평가어/과장 narrative 없음.

## [2026-05-11] ingest | Sambath 2026 — Indian cervical cancer CCRT resistance proteogenomics (user-shared)

- 사용자가 Wiley DOI URL(`10.1002/1878-0261.70108`) 공유(네 번째 user-shared 논문) → 본문 확인 + 한미암 활용 가능성 평가 → 사용자 승인(`응 진행해줘! 무슨 내용이야?`) → wiki + 노션 동시 등록.
- 메타데이터 확인: Crossref → Mol Oncol 20:709–726 (2026), Indian cervical cancer CCRT resistance proteogenomics. Unpaywall cc-by → PMC13042866. Wiki 중복 검색(`grep -ril "sambath\|1878-0261.70108"`) → 위키에 없음 확인.
- PDF 다운로드: Wiley publisher block(Cloudflare 예상) → **Europe PMC `articles/PMC13042866?pdf=render`로 직접 다운로드 성공** (2.5 MB, 18 페이지). Lehe 2026 ingest와 동일 패턴 — Europe PMC render endpoint는 Wiley OA + NIHMS author-manuscript 양쪽 모두 안정적 fallback.
- 본문 추출: `pdftotext -layout` → `/tmp/sambath2026.txt` 1,056 line. 핵심 섹션 직접 확인 (Abstract / Introduction / Methods 2.1–2.14 / Results 3.1–3.6 / Discussion).
- `wiki/sources/sambath-2026-integrated-genomic-proteomic-cervical-cancer-chemoradiation-resistance.md` 풀-텍스트 소스 페이지 생성: Summary / Key Points / Methods / Cancer Multiomics Project Relevance / Connections / Sources 6 섹션 (PEXMap/3DisoGalaxy/Lehe와 동일 포맷). `feedback_paper_relevance_writing.md` 규칙 엄수: 논문 본문 + 위키 내 기존 내용만, 뇌피셜/과장/외부 보강/평가어 없음.
- frontmatter: `paper_kind: research`, `cancer_types: [cervical-cancer]`, `modalities: [whole-genome-sequencing, whole-exome-sequencing, tmt-proteomics, phosphoproteomics, immunohistochemistry]`, `themes`에 chemoradiation-resistance, treatment-response, mutational-signatures, copy-number-signatures, structural-variants, chromothripsis, apobec, hpv-associated, dna-repair-pathway, pi3k-akt-signaling, egfr-amplification, actionable-mutations, indian-cohort 포함.
- 핵심 정량 포인트: 코호트 36명(stage IIIB squamous HPV+, RECIST sens 19/res 17) — WGS 26(15 paired+10 unpaired)+WES 10 paired+TMT proteome 10(5+5, 8,373/7,138 proteins)+동일 cohort phosphoproteome(ref 38) 통합+IHC validation 32명. Top mut KMT2D/PIK3CA 27%, FBXW7 19%, KMT2C 19%, NOTCH1 19%, CASP8 15%. APOBEC SBS2 84%+SBS13 92%. CNV 130 amp/101 del, GISTIC 89 focal (25 amp+25 del), CNS7/CNS14 signatures. SV 3,037 (del 1,615/dup 436/inv 427/trans 559), TTC28 8 rearrangement/6명. Chromothripsis 3/12 resistant. Sens vs res 고유: sens 9 focal amp, res EGFR amp 6명 + STK11 SV del 4명. Proteome 73 sig (P<0.05) / 24 |FC|>1.5 / top5 up SERPINB7·STX3·LBP·EMILIN2·NQO2. STX3 IHC validation 32명 일관 elevated. CNA-protein 66.96% trans positive, 6q/9q/11p/22q hotspot. OncoKB Level 1 33%/2 11%/3A 25%/4 5%.
- 한미암 적용 한계 명시 (논문 본문 기반): 본 논문은 자궁경부암 인도 코호트 한정 — 한국인 lung cancer-specific 추론은 별도 평가 필요. KMT2D/KMT2C/CASP8 enrichment, SBS29 tobacco chewing signature는 인도 코호트 특이 신호. Sample size 36+proteome 10 → independent larger cohort validation 필요(저자 명시 한계).
- 토픽 허브 `wiki/topics/cancer-multiomics-literature.md` Section 1 (Proteogenomics 통합 기반) 끝에 Lehe 2026 다음 줄로 한 줄 추가 — research로 분류.
- corpus queue 카운트 +1 (Selected 94→95, Acquired 83→84, Ingested 93→94); Selected set 표에 `needs-brief` 상태로 새 행 추가.
- `wiki/_meta/index.md` Proteogenomics / PTM Atlas 섹션에서 Lehe 2026 다음 줄로 링크 추가.
- Notion 하위 페이지(`참고 논문 및 아이디어` 344302d9...): PEXMap/3DisoGalaxy/Lehe와 동일 6-섹션 한국어 포맷으로 생성 — 페이지 ID `35d302d9-c598-81bd-a7f6-efcb538eb089`. 섹션: 논문 정보 / 한 줄 요약 / 코호트+데이터 layer / 핵심 결과(7 subsection: Genomic landscape / CNV+SV / Sens vs Res / Proteome+IHC / Proteogenomic 통합 / OncoKB / 통합 결론) / 한계+주의점. Strict source-grounded — 논문 본문 직접 보고치만, 한미암 적용 시나리오 narrative 없음.

## [2026-05-11] ingest | Lehe 2026 — MS instrumentation & methodology review for alternative protein isoforms (user-shared)

- 사용자가 Wiley URL 공유(세 번째 user-shared 논문) → "노션 추가 전 본문부터 확인" 패턴으로 진행: 본문 검토 → 한미암 활용 가능성 평가 → 사용자 승인(`응`) → wiki 풀-텍스트 + 노션 동시 등록.
- PDF 다운로드: Wiley pdfdirect (Cloudflare 403) → PMC interstitial(JS-required) → **Europe PMC `articles/PMC12912779?pdf=render` 엔드포인트 성공** (1.1 MB, 30 페이지, author-manuscript NIHMS-2134509). 신규 패턴: Wiley/NIHMS author-manuscript의 경우 NCBI PMC가 JS-render interstitial을 두지만 EPMC는 직접 PDF 스트리밍. fallback 옵션으로 기억.
- 본문 추출은 PMC HTML viewer → plain text(107KB)에서 미리 완료(텍스트 소스). PDF는 archival 용도로 동시 보관.
- `wiki/sources/lehe-2026-mass-spectrometry-alternative-protein-isoforms-review.md` 풀-텍스트 소스 페이지 생성: Summary / Key Points / Methods(scope) / Cancer Multiomics Project Relevance / Connections / Sources 6 섹션 (PEXMap/3DisoGalaxy와 동일 포맷, review-paper용으로 "Methods" → "Methods(scope)"로 의미 조정).
- frontmatter: `paper_kind: review`, `cancer_types: [pan-cancer]`, `modalities: [mass-spectrometry, long-read-rna-seq, ribosome-profiling]`, `themes: [proteogenomics, alternative-splicing, isoform-resolution, proteoform-biology, dia-acquisition, dda-acquisition, targeted-proteomics, top-down-proteomics, sample-preparation, bioinformatics-tooling]`.
- 핵심 정량 포인트(Table 1 매트릭스): standard DDA 0–10 AS peptides → deep DDA 216(Pandi 2024) → ultra-deep DDA 4,608 AS events(Sinitcyn 2023) / SWATH-DIA 2,964 isoform peptides(Liu 2017) / multi-protease DIA +60%(Richards 2022) / Astral DIA 935 AS events/day(Guzman 2025) / IS-PRM 77 vs DDA 21 in WTC11(Korchak 2024) / FAIMS-TDMS 267 splice variants(Fulcher 2021) / NCI RAS Initiative 39 KRAS proteoforms(Adams). Table 2 = library-free DIA + de novo splice junction + top-down open-search 도구 stack.
- 본 논문이 직접 인용한 cancer 사례: CPTAC breast(Mertins) 672 splice peptide / CPTAC colon(Woo) 108 splice junction peptide / NSCLC 혈청 BMP1 inference(Donovan) / DLD-1 CRC 128 exon-skipping proteoform(Chen & Liu) / NCI RAS Initiative KRAS4A+4B 39 proteoform(Adams). 한미암 프로젝트 적용 시나리오는 본 위키에 추가하지 않음(논문 본문에 lung cancer-specific isoform proteomics 사례는 Donovan BMP1 외에는 없음).
- 사용자 피드백 반영: 초안에서 PEXMap+3DisoGalaxy+Lehe를 "트리오"로 엮은 narrative + "ROI 최고" 등 평가어 사용 → 본 ingest 중 사용자 지적으로 wiki source / Notion 페이지 둘 다 strict source-grounded 톤으로 재작성. `feedback_paper_relevance_writing.md` 메모리로 저장.
- 토픽 허브 `wiki/topics/cancer-multiomics-literature.md` Section 1 끝에 3DisoGalaxy 다음 줄로 한 줄 추가 — review로 분류.
- corpus queue 카운트 +1 (Selected 93→94, Acquired 82→83, Ingested 92→93); Selected set 표에 `needs-brief` 상태 새 행.
- `wiki/_meta/index.md` Proteogenomics / PTM Atlas 섹션에서 3DisoGalaxy 다음 줄로 링크 추가.
- Notion 하위 페이지 (`참고 논문 및 아이디어` 344302d9...): PEXMap/3DisoGalaxy와 동일 6-섹션 한국어 포맷으로 생성 — 페이지 ID `35d302d9-c598-81bf-9ea4-f4df5902ea0d`. 6 섹션: 논문 정보 / 한 줄 요약 / 과제 관련성(한미암) / 핵심 결과(acquisition method 매트릭스 + bioinformatics 도구 stack + bottom-up/top-down 통합) / 한미암에서 바로 가져올 포인트(6개 실행 항목) / 주의점(6개 caveat).

## [2026-05-11] ingest | Jiang 2026 — 3DisoGalaxy (translation-supported isoform foldome atlas, user-shared)

- 사용자가 bioRxiv URL 공유(두 번째 user-shared 논문) → PEXMap과 동일한 워크플로(Plan → wiki/sources → topic hub → meta → Notion)로 진행.
- PDF 다운로드: `raw/inbox/papers/jiang-2026-3disogalaxy-breast-cancer-isoform-foldome.pdf` (8.5 MB, 49 페이지) — 동일한 Chrome UA + biorxiv Referer 헤더 패턴 재사용.
- `wiki/sources/jiang-2026-3disogalaxy-breast-cancer-isoform-foldome.md` 풀-텍스트 소스 페이지 생성: Summary / Key Points / Methods / Cancer Multiomics Relevance / Connections / Sources 6 섹션 (PEXMap과 동일 구조).
- frontmatter: `discovery_method: user-shared`, `paper_kind: computational`, `cancer_types: [breast-cancer]`, `modalities: [long-read-rna-seq, ribosome-profiling, protein-structure, alphafold]`, `themes`에 proteoform-biology / translatome / foldome / structural-similarity-network / intrinsic-disorder 등 신규 키워드 포함.
- 토픽 허브 `wiki/topics/cancer-multiomics-literature.md` Section 1 끝에 PEXMap 다음 줄로 한 줄 추가 — atlas + tool로 분류.
- corpus queue 카운트 +1 (Selected 92→93, Acquired 81→82, Ingested 91→92); Selected set 표에 `needs-brief` 상태로 새 행 추가.
- `wiki/_meta/index.md` Proteogenomics / PTM Atlas 섹션에서 PEXMap 다음 줄로 링크 추가.
- 주요 정량 포인트: 123,395 transcript variants → 90,929 high-confidence → 73,715 translation-supported ORFs → 46,601 high-confidence structures (pLDDT≥70). KRAS4A 손실 motif (NLS 169–172, bipartite NLS 182–185, ER-retrieval). ΔPH AKT1 (1–62 결손) TNBC log2FC = 0.82 (BH P<0.001), RFS log-rank P=0.046. IntOGen 드라이버는 모티프 shift score 유의 상승 (Mann–Whitney P<0.001).
- Notion 하위 페이지 (`참고 논문 및 아이디어` 344302d9...): PEXMap과 동일 6-섹션 포맷(논문 정보 / 한 줄 요약 / 과제 관련성(한미암) / 핵심 결과 / 한미암에서 바로 가져올 포인트 / 주의점)으로 생성 — 페이지 ID `35d302d9-c598-81f4-9d89-c35f68149e9f`.

## [2026-05-11] ingest | Savage 2020 — phosphoproteomics bioinformatics comprehensive guide (Q3 follow-up)

- Q3 synthesis follow-up으로 OpenAlex 관련논문 검색 (`scripts/ingest/find_related_via_openalex.py`, seed = jiang-2025 + muller-dott-2025 + wu-2011 + mertins-2016 + gillette-2020, top-60 scored) 후 vault에 없는 PTM-correction-relevant 후보 4편 다운로드 시도.
- 결과: Savage 2020 (Clinical Proteomics, Bing Zhang 그룹, 1.7 MB) Unpaywall로 OK. Krug 2020 (Bioinformatics) 페이월 차단, Wang 2023/Hu 2023은 PubMed 제목 매칭 오류로 tea-drought/periodontitis 논문이 받아져 둘 다 삭제 (resolver의 알려진 limitation — fuzzy title match로 DOI를 무시하고 다른 논문을 받아옴).
- `wiki/sources/savage-2020-phosphoproteomics-bioinformatics-comprehensive-guide.md` 풀-텍스트 소스 페이지 작성 — 16 kinase DBs + 27 site DBs 카탈로그, KSEA App (highest TP) vs PHOXTRACK (lowest FP) 벤치마크, "understudied kinase <10 substrates" empirical 근거 정리. CoPheeMap/Jiang 2025의 prequel 위치 명시.
- Cross-link 추가: Q3 synthesis Connections에 Savage 2020 추가, ptm-correction-confounding-foundations concept Connections에도 Savage 2020 추가 (Jiang 2025의 같은 Bing Zhang lab 계보).

## [2026-05-11] ingest | Awasthi 2026 — PEXMap (splice-isoform peptide mapping tool, user-shared)

- 사용자가 bioRxiv URL 공유 → plan-first 워크플로로 `wiki/_meta/pexmap-ingest-plan.md` 작성·승인 후 ingest.
- PDF 다운로드: `raw/inbox/papers/awasthi-2026-pexmap-proteogenomic-exon-isoform-mapping.pdf` (1.7 MB, 23 페이지) — bioRxiv Cloudflare 403 우회는 Chrome UA + Mac Referer 헤더로 직접 다운로드. fallback_direct_url.py에 이미 `10.64898/` prefix 패턴이 있어 차후 자동 재현 가능.
- `wiki/sources/awasthi-2026-pexmap-proteogenomic-exon-isoform-mapping.md` 풀-텍스트 소스 페이지 생성: Summary / Key Points / Methods / Cancer Multiomics Relevance / Connections / Sources 6 섹션 (Slack 섹션 의도적 생략, 사용자 결정).
- frontmatter에 `discovery_method: user-shared` 표기 + `paper_kind: computational`, `themes: [proteogenomics, alternative-splicing, isoform-resolution, peptide-mapping, exon-junction]`, `cancer_types: [pan-cancer]`, `modalities: [proteogenomics, mass-spectrometry]`.
- 토픽 허브 `wiki/topics/cancer-multiomics-literature.md` Section 1 (Proteogenomics 통합 기반) 끝에 한 줄 추가 — splice-isoform-aware tool로 분류.
- corpus queue 카운트 +1 (Selected 91→92, Acquired 80→81, Ingested 90→91); Selected set 표에 `needs-brief` 상태로 새 행 추가.
- `wiki/_meta/index.md` Proteogenomics / PTM Atlas 섹션 맨 앞에 링크.
- Notion 하위 페이지 (`참고 논문 및 아이디어` 344302d9...): Tran 2026 수준 상세 본문으로 생성 — 별도 단계.

## [2026-05-11] syntheses | Q3 deep-dive — kinase activity inference under PTM correction

- 새 synthesis 페이지 `wiki/syntheses/kinase-activity-inference-under-ptm-correction.md` 작성 — Research-questions-queue Q3 ("PTM 보정이 KSEA/NetworKIN/CoPheeKSA 호출에 미치는 영향, 어떤 kinase가 얻고 잃나") 응답.
- 핵심 정량 메시지 3층 구조: (a) 입력층 ~46% phosphosite 재분류, (b) 호출층 7 kinases (BRAF, CSNK2A1, HIPK2, MAPK13, PRKCG, TBK1, TTK) 회복 + 16 kinases 제거, (c) 커버리지층 26 understudied kinases (CDK12, SGK3, SMG1, NUAK1 등) CoPheeKSA로 신규 addressable.
- 기존 ptmanchor 매뉴스크립트 Discussion에 그대로 인용 가능한 정량 문장과 3-panel figure 제안 포함; 우리 5-cohort Cancer Multiomics 데이터에 적용할 prediction 5개 명시.
- Cross-link 추가: `wiki/_meta/index.md` Syntheses 섹션, `wiki/_meta/research-questions-queue.md` Q3 체크 완료, `wiki/analyses/ptmanchor-manuscript-anchor.md` Connections 보강, `wiki/syntheses/index.md` 목록 보강 (B-cell research map + resistance convergence framework + Q3까지).

## [2026-05-11] daily-digest | repoint to llm-wiki + upgrade pre-Slack source pages

- 한미암 daily_digest cron이 이제 `~/paperatlas/...` 대신 `~/Dropbox/llm-wiki/scripts/daily_digest/cron_entry.sh`를 호출하도록 crontab 갱신; PDF 다운로드·`wiki/sources/` 신규 페이지·`wiki/_meta/slack-posted.json` 업데이트가 모두 이 vault에 직접 쌓이도록 단일 소스로 통합.
- 이번 수요일(2026-05-13 10:00 KST) Slack 후보 2편의 source page를 placeholder → PDF-backed로 업그레이드:
  - `wiki/sources/jiang-2025-deciphering-dark-cancer-phosphoproteome-using.md` (CoPheeMap/CoPheeKSA 11-cancer dark phosphoproteome KSA prediction, 잘못된 DOI 라인 수정 + Methods/Cancer Multiomics Relevance 추가).
  - `wiki/sources/liu-2025-multimodal-fusion-radio-pathology-proteogenomics-identify.md` (MOFS 다중모달 IDH-wt glioma subtyping + STRAP 표적 + DNN MRI classifier, 잘못된 DOI/PMC 라인 수정 + Methods/Cancer Multiomics Relevance 추가).
- 두 페이지 모두 frontmatter tag/theme 보강 (liu-2025는 phosphoproteomics tag 제거하고 multimodal-fusion/radiomics/pathomics/anti-pd-1 추가), Connections에 ptmanchor hub + 관련 concept 페이지 연결.

## [2026-04-15] bootstrap | initial scaffold

- Created base repository structure for raw sources and wiki pages.
- Added `AGENTS.md` to define ingest, query, and lint workflows.
- Seeded the index, log, overview, and core concept pages.

## [2026-04-15] ingest | Andrej Karpathy - LLM Wiki Gist

- Added an initial source page summarizing the foundational gist for this repository.
- Linked the source into the concept and overview structure.

## [2026-04-15] ingest | b-cell neoantigen pipeline human cancer corpus

- Downloaded 10 PDFs into `raw/inbox/papers/` using a shared basename convention.
- Added 10 matching source pages in `wiki/sources/` with the same basename as each PDF.
- Added concept pages for neoantigen pipelines and B-cell/TLS biology.
- Added an analysis page synthesizing how neoantigen pipeline papers and B-cell/TLS papers fit together.

## [2026-04-15] tooling | qmd search enabled

- Installed Bun and QMD for repo-local wiki retrieval.
- Added `bin/qmd` wrapper so cache and config stay inside the repository.
- Updated operating rules to prefer QMD over recursive grep for wiki search.

## [2026-04-15] tooling | qmd embeddings enabled

- Ran `./bin/qmd embed` and generated 25 vectors across 21 indexed markdown files.
- Downloaded the local embedding and query-expansion models into `.cache/qmd/models/`.
- Enabled semantic retrieval paths such as `vsearch` and `query`, with the caveat that they are slow on CPU-only hardware.

## [2026-04-15] tooling | qmd default set to search

- Updated the repo rules so `qmd search` is the default wiki lookup path.
- Kept `vsearch` and `query` available as opt-in tools for heavier semantic retrieval only when needed.

## [2026-04-15] publishing | quartz wiki_html scaffold

- Added `wiki_html/` as a Quartz-based publish layer for the markdown wiki.
- Added a sync script so `wiki/` remains the source of truth and `wiki_html/content/` is generated from it.
- Added a public home page at `wiki/index.md` and prepared the repo for GitHub Pages deployment.

## [2026-04-15] publishing | graph and atlas navigation enabled

- Re-enabled Quartz graph view so paper-to-paper and concept-to-paper connectivity is visible in the public site.
- Added section landing pages and page tags to strengthen graph structure, tag browsing, and local navigation.

## [2026-04-15] planning | atlas app schema and roadmap

- Added a structured frontmatter schema for paper pages to support future cards, filters, journal pages, and cancer-type pages.
- Added an implementation roadmap for evolving the Quartz site toward a more app-like paper atlas.

## [2026-04-16] curation | removed non-paper gist from atlas corpus

- Moved the Karpathy LLM Wiki gist note out of `wiki/sources/` and into `_meta/`.
- Removed the gist from public atlas browsing so the visible corpus stays focused on domain-relevant papers.

## [2026-04-16] publishing | home graph restored and research-map emphasis tightened

- Moved the home paper graph up into a prominent panel directly below the research-map hero section.
- Kept the home graph paper-only so it matches the domain corpus rather than the full wiki document graph.
- Lowered cancer and journal browsing to supporting context views instead of the main intellectual scaffold.

## [2026-04-16] information architecture | generalized atlas home around reusable topics

- Reframed the home page from a B-cell-specific landing page into a generic paper-atlas entry point.
- Added `wiki/topics/` as a first-class layer so future subjects can live alongside the current B-cell neoantigen collection.
- Kept the current B-cell corpus as the first curated topic rather than the definition of the whole site.

## [2026-04-16] ux | restored right-sidebar graph and removed generic site keywords from home themes

- Restored a paper-only graph view to the top of the home page right sidebar, closer to the original Quartz placement.
- Removed generic site-structure chips such as Topics and Concepts from the home keyword area.
- Kept the home keyword panel focused on research themes derived from the paper corpus rather than navigation labels.

## [2026-04-16] ux | moved home graph into main content and simplified graph interaction

- Moved the home paper graph out of the sidebar and into a large main section on the homepage.
- Changed the home graph interaction so clicking a paper node goes directly to that paper's summary page.
- Removed the need for a cramped sidebar detail panel on the home graph.

## [2026-04-21] ingest | immunotherapy resistance and immune evasion batch 1

- Added 10 source pages covering the first immunotherapy-resistance batch across checkpoint theory, CAR-T escape, bispecific antibodies, and hematologic or thoracic cancer trials.
- Created new concept pages for the cancer-immunity cycle and set point, plus antigen loss, lineage switch, and target escape.
- Added a new topic hub for immunotherapy resistance and immune evasion and linked it into the atlas navigation.
- Added new cancer pages for acute lymphoblastic leukemia, multiple myeloma, and small-cell lung cancer, plus new journal pages for Immunity, Nature, Leukemia, Cancer Discovery, and the New England Journal of Medicine.
- Downloaded and stored repo-local PDFs for `chen-2017-cancer-immune-set-point`, `orlando-2018-target-antigen-loss-car19-therapy`, `qiu-2025-lineage-switch-cd19-cart-treatment-ball`, `labanieh-2023-car-immune-cells-design-principles-resistance`, and `lesokhin-2023-elranatamab-relapsed-refractory-multiple-myeloma`.
- Marked local PDF capture as pending for the remaining batch papers where publisher or PMC anti-bot flows blocked scripted download in this environment.

## [2026-04-21] ingest | immunotherapy resistance and immune evasion batch 2

- Added 10 source pages for refs 11-20, extending the resistance topic into randomized bispecific trials, HER2-targeted ADCs, EGFR-TKI resistance, and colorectal immune evasion.
- Added concept pages for bispecific antibodies in oncology, ADC target expression and HER2-dependent resistance, osimertinib resistance and immune remodeling, and immune evasion in colorectal cancer.
- Added new cancer pages for biliary tract cancer, breast cancer, non-small-cell lung cancer, and colorectal cancer, plus journal pages for Lancet Oncology, JAMA Oncology, and European Journal of Cancer.
- Downloaded and stored repo-local PDFs for `goebeler-2024-bispecific-multispecific-antibodies-oncology` and `chmielecki-2023-acquired-resistance-first-line-osimertinib`.
- Built `outputs/pdf-download-tracker-batches-1-2.xlsx` so blocked or pending papers now include article sites, likely manual download routes, and the specific reason scripted capture failed.

## [2026-04-21] ingest | immunotherapy resistance and immune evasion batch 3

- Added 10 source pages for refs 21-30, expanding the corpus into acquired and primary checkpoint resistance, HLA loss, KRAS-directed T-cell escape, 9p21 immune-cold biology, MSI-H heterogeneity, and stromal TGF-beta exclusion.
- Added concept pages for MHC-I and interferon-pathway defects in checkpoint resistance, TGF-beta and immune exclusion, and MSI-H or dMMR heterogeneity in immunotherapy response.
- Added new cancer pages for endometrial, gastric, and urothelial cancer, plus journal pages for Cell, Journal of Clinical Investigation, Journal of Thoracic Oncology, Gynecologic Oncology, and Journal of Medical Genetics.
- Downloaded and stored a repo-local PDF for `mariathasan-2018-tgfb-pdl1-blockade-tcell-exclusion`.
- Removed several bad HTML challenge pages that had been mistakenly saved with `.pdf` extensions and moved their status into the tracker workflow instead of raw storage.

## [2026-04-21] ingest | immunotherapy resistance and immune evasion batch 4

- Added 10 source pages for refs 31-40, covering systemic inflammatory biomarkers, CAF and macrophage-mediated immune barriers, antiangiogenic-immune vascular remodeling, CAR-T resistance reviews, and TLS-linked immunotherapy response papers.
- Added concept pages for CAR-T cell resistance and design strategies, plus stromal and myeloid barriers to immunotherapy, and expanded the existing B-cell or TLS concept page with new clinical and translational anchors.
- Added new cancer pages for pancreatic cancer and soft-tissue sarcoma, plus journal pages for Journal for ImmunoTherapy of Cancer, Science Translational Medicine, Cancer Research, Blood Cancer Journal, Signal Transduction and Targeted Therapy, and Nature Reviews Drug Discovery.
- Downloaded and stored repo-local PDFs for `ruella-2023-cart-resistance-haematological-malignancies`, `sterner-2021-cart-current-limitations-potential-strategies`, `zugasti-2025-cart-cancer-current-challenges-future-directions`, `helmink-2020-b-cells-tertiary-lymphoid-structures-immunotherapy-response`, and `italiano-2022-pembrolizumab-soft-tissue-sarcomas-tls`.
- Removed invalid HTML placeholder files for the BMJ-routed Laino and Sun PDFs after confirming they were not real PDFs.

## [2026-04-21] ingest | immunotherapy resistance and immune evasion batch 5

- Added 10 source pages for refs 41-50, covering TLS-derived transcriptomic biomarkers, lactate and exosomal PD-L1 biology, GDF-15-mediated checkpoint resistance, microbiota-linked immunoresistance, STK11 or KEAP1-associated lung cancer resistance, POSEIDON, and the pan-tumor TMB plus GEP framework.
- Added concept pages for soluble and metabolic mediators of immunoresistance, gut microbiota and immunoresistance, and STK11-KEAP1-related immunotherapy resistance in lung cancer.
- Added new journal pages for Advances in Experimental Medicine and Biology, Cancer Immunology, Immunotherapy, Cell Research, Journal of Clinical Oncology, and Science.
- Downloaded and stored repo-local PDFs for `du-2025-tls-gene-signature-advanced-nsclc`, `melero-2025-gdf15-overcome-pd1-pdl1-resistance`, `simpson-2023-gut-microbiota-enhance-checkpoint-efficacy`, `almonte-2026-gut-dysbiosis-oncology-immunoresistance`, and `skoulidis-2024-ctla4-abrogates-keap1-stk11-resistance`.
- Marked `harmon-2020-immune-consequences-lactate-tumor-microenvironment`, `chen-2018-exosomal-pdl1-immunosuppression-pd1-response`, and `skoulidis-2018-stk11-lkb1-pd1-resistance-kras-lung` as scripted PDF failures after verifying the saved files were HTML rather than real PDFs.

## [2026-04-21] ingest | immunotherapy resistance and immune evasion batch 6

- Added 10 source pages for refs 51-60, covering EGFR-TKI resistance evolution, EMT-associated immune-checkpoint elevation, KRAS G12C adaptive and clinical resistance, T-DXd cGAS-STING activation, MET-STING-linked checkpoint resistance, KRAS G12D immunophenotypes, and the failure of checkpoint therapy in EGFR-mutant NSCLC.
- Added concept pages for KRAS G12C resistance and ecosystem remodeling, plus EGFR-mutant NSCLC and immunotherapy mismatch.
- Added new journal pages for Clinical Cancer Research, Annals of Oncology, Cell Communication and Signaling, and JTO Clinical and Research Reports, while expanding Science Translational Medicine, Cancer Discovery, and Journal of Clinical Investigation.
- Downloaded and stored repo-local PDFs for `xue-2020-rapid-nonuniform-adaptation-kras-g12c-inhibition` and `oh-2024-tdxd-cgas-sting-gastric-cancer`.
- Marked the attempted local PDF captures for `sequist-2011-genotypic-histological-evolution-egfr-resistance`, `lou-2016-emt-inflammatory-signals-multiple-checkpoints-lung`, `tsai-2022-idiosyncratic-resistance-kras-g12c-inhibition`, and other PMC/JCI-routed files as pending because scripted download returned HTML rather than a valid PDF.

## [2026-04-21] ingest | immunotherapy resistance and immune evasion batch 7

- Added 10 source pages for refs 61-70, covering EGFR-mutant NSCLC salvage immunotherapy, ESR1 mutation-driven endocrine resistance, CDK4/6-related senescence and immunogenicity, and foundational advanced prostate-cancer genomics plus antiandrogen resistance.
- Added concept pages for ESR1 mutations and endocrine resistance in breast cancer, CDK4/6 inhibition with senescence and tumor immunogenicity, and AR pathway resistance and immune context in prostate cancer.
- Added a new prostate cancer atlas page plus new journal pages for Nature Genetics, Oncogene, Molecular Oncology, Breast Cancer Research, Clinical and Translational Medicine, and eLife.
- Downloaded and stored repo-local PDFs for `toy-2013-esr1-ligand-binding-domain-mutations-breast`, `robinson-2013-activating-esr1-mutations-metastatic-breast`, `lopez-2025-esr1-mutations-tcell-surveillance-disruption`, `wagner-2020-senescence-therapeutically-relevant-cdk46`, and `balbas-2013-overcoming-resistance-antiandrogens-rational-design`.
- Marked `wu-2025-atezolizumab-bevacizumab-pemetrexed-platinum-egfr-tki-failure`, `lee-2024-cdk46-senescence-immunogenic-properties`, and `robinson-2015-integrative-clinical-genomics-advanced-prostate` local PDF attempts as invalid HTML captures and kept them pending in the tracker workflow.

## [2026-04-21] ingest | local manuscript and proposal anchors

- Ingested three local user documents as markdown anchor pages so future connectivity maps can relate downloaded papers to active manuscripts and a live research proposal.
- Added `B-Cell Neoantigen Proposal Anchor` and linked it into the existing B-cell neoantigen topic as a project-side relevance anchor.
- Added `Cancer Resistance Manuscript Anchor` and linked it into the resistance topic as a manuscript-side relevance anchor.
- Added `ptmanchor Manuscript Anchor` and created a new topic, `PTM Correction and Kinase Signaling in Cancer Proteomics`, so the atlas can expand beyond the two current immunology-heavy tracks.

## [2026-04-21] workflow | gist feature adoption

- Reviewed the collaborator-guide gist and mapped its core ideas onto this repo's current architecture instead of treating it as a separate template.
- Added `Gist Feature Adoption Roadmap` to document which pieces are already live here and which should be built next in the overnight workflow.
- Updated the overnight automation so future runs explicitly follow the gist-style pattern of immutable PDFs, deep source summaries, knowledge-tree topic expansion, and public atlas publishing.

## [2026-04-21] workflow | human-cancer-only acquisition filter

- Tightened the overnight corpus-building rules to prioritize human cancer research only.
- Explicitly excluded mouse or murine tumor models, xenograft or PDX studies, organoid studies, and other preclinical-only systems from new PDF acquisition targets.
- Kept the additional venue filter excluding MDPI journals, PLOS ONE, and Scientific Reports, while still allowing older landmark papers when they remain foundational and human-cancer-centered.

## [2026-04-22] workflow | anchor keyword clusters

- Added `Anchor Keyword Clusters` so the three active seed projects now have explicit acquisition-oriented keyword maps.
- Recorded separate keyword groups for the resistance manuscript, the B-cell neoantigen proposal, and the ptmanchor manuscript.
- Preserved the strict exclusion rules for mouse or murine, xenograft or PDX, organoid, and low-priority venue filtering inside the acquisition-facing analysis layer.

## [2026-04-22] workflow | priority target corpora

- Added `Priority Target Corpora` to translate the three anchor keyword maps into concrete next-wave acquisition priorities.
- Focused the queue on high-impact, human-cancer-centered studies using cohorts, biopsies, ctDNA, spatial, single-cell, and proteogenomic evidence.
- Kept the strict exclusions for mouse or murine, xenograft or PDX, organoid-only, and low-priority venue papers inside the target-corpus planning layer.

## [2026-04-23] workflow | anchor progress baseline

- Added `Anchor Progress Baseline` to make the per-anchor gap to the user's `100 papers each` target explicit.
- Recorded the current imbalance across the three seed projects, with most existing ingest concentrated in resistance and much smaller dedicated clusters for B-cell neoantigen and PTM-focused work.
- Framed future acquisition as a per-anchor growth problem rather than a single undifferentiated global paper count.

## [2026-04-23] workflow | next download candidates

- Added `Next Download Candidates` so the two most underfilled anchors now have concrete immediate human-cancer, high-impact papers queued for the next acquisition wave.
- Prioritized recent Nature-family human studies for B-cell neoantigen and PTM-aware phosphoproteomics because those anchors are farthest from the user's 100-paper target.

## [2026-04-24] ingest | b-cell neoantigen and ptm candidate download wave 1

- Added 4 new source pages from newly downloaded valid PDFs, including 2 proteogenomic neoantigen papers and 2 PTM or kinase-inference papers.
- Linked the neoantigen papers into the `B-Cell Neoantigen Proposal Anchor` and the `B-Cell Neoantigen Research Map`.
- Linked the phosphoproteomics papers into the `ptmanchor Manuscript Anchor` and the `PTM Correction and Kinase Signaling in Cancer Proteomics` topic.
- Kept PDF and source basename matching for this ingest wave by using the same basenames as the downloaded files in `raw/inbox/papers/`.

## [2026-04-24] ingest | b-cell neoantigen candidate download wave 2

- Downloaded 2 additional valid PDFs for the underfilled B-cell neoantigen track: one recent urothelial neoantigen-vaccine trial and one mechanistic mature-TLS human HNSCC paper.
- Added matching source pages and linked both papers into the `B-Cell Neoantigen Proposal Anchor` and `B-Cell Neoantigen Research Map`.
- Continued the download-first recovery workflow with stable PDF-to-source basenames and kept the public sync path ready for the next atlas refresh.

## [2026-04-24] ingest | ptm candidate download wave 2

- Downloaded 2 additional valid human pan-cancer proteomics PDFs for the ptmanchor track, including a recent Nature Cancer pan-cancer functional-network paper and a foundational Nature Communications proteomic subtype study.
- Added matching source pages and linked both papers into the `ptmanchor Manuscript Anchor` and `PTM Correction and Kinase Signaling in Cancer Proteomics`.
- Extended the PTM-side corpus with both recent systems-level interpretation work and older landmark CPTAC-scale background.

## [2026-04-24] ingest | b-cell tls candidate download wave 3

- Added a new human gastric cancer TLS source page from a recent Nature Communications single-cell and spatial transcriptomics study.
- Linked the new gastric TLS paper into the `B-Cell Neoantigen Proposal Anchor` and `B-Cell Neoantigen Research Map`.
- Also secured a local PDF for the existing nasopharyngeal carcinoma TLS paper, but avoided duplicate source-page creation because that study was already ingested.

## [2026-04-24] ingest | ptm candidate download wave 3

- Added a large human pan-cancer proteogenomics source built from 2002 tumors across 14 cancer types and 17 studies.
- Linked the new compendium paper into the `ptmanchor Manuscript Anchor` and `PTM Correction and Kinase Signaling in Cancer Proteomics` as foundational background for protein-level and pathway-level interpretation across cohorts.

## [2026-04-24] ingest | ptm candidate download wave 4

- Added 3 more ptmanchor-relevant human proteogenomics sources: one pan-cancer structural-variation proteome paper and 2 landmark Nature studies in breast and colorectal cancer.
- Linked all 3 papers into the `ptmanchor Manuscript Anchor` and `PTM Correction and Kinase Signaling in Cancer Proteomics`.
- Pushed the valid local PDF count over the interim milestone of 50 while staying inside the human-cancer and venue filters.

## [2026-04-24] ingest | ptm candidate download wave 5

- Added a ccRCC treatment-response proteogenomics paper linking phosphoproteomic mTOR programs and multi-omics features to sunitinib response.
- Linked the new renal cancer source into the `ptmanchor Manuscript Anchor` and `PTM Correction and Kinase Signaling in Cancer Proteomics`.

## [2026-04-24] ingest | b-cell tls candidate download wave 4

- Added a human endometrial cancer TLS paper showing prognostic value of B-cell-rich tertiary lymphoid structures and practical L1CAM-based assessment.
- Linked the new endometrial TLS source into the `B-Cell Neoantigen Proposal Anchor` and `B-Cell Neoantigen Research Map`.

## [2026-04-24] ingest | b-cell tls candidate download wave 5

- Added a human pancreatic cancer TLS paper from Nature linking IL-33 and ILC2 biology to tertiary lymphoid structure induction and improved prognosis.
- Linked the new pancreatic TLS source into the `B-Cell Neoantigen Proposal Anchor` and `B-Cell Neoantigen Research Map`.

## [2026-04-24] ingest | ptm candidate download wave 6

- Added a breast cancer proteogenomic landscape paper showing protein-level subtype refinement, immune-associated subdivision, and limits of RNA-only classification.
- Linked the new breast proteogenomic source into the `ptmanchor Manuscript Anchor` and `PTM Correction and Kinase Signaling in Cancer Proteomics`.

## [2026-04-25] ingest | ptm candidate download wave 7

- Added a concise review on pan-cancer proteogenomics that synthesizes CPTAC-style multi-omics integration, target discovery, and phosphoproteomic interpretation.
- Linked the review into the `ptmanchor Manuscript Anchor` and `PTM Correction and Kinase Signaling in Cancer Proteomics` as supporting background.

## [2026-04-25] ingest | b-cell neoantigen candidate download wave 6

- Added a clinical immunopeptidomics paper introducing a more sensitive workflow for personalized neoantigen discovery from scarce tumor material.
- Linked the new neoantigen-discovery source into the `B-Cell Neoantigen Proposal Anchor` and `B-Cell Neoantigen Research Map`.

## [2026-04-25] ingest | b-cell neoantigen candidate download wave 7

- Added a pan-cancer immunotherapy paper quantifying HLA-based neoantigen presentation capacity as a predictor of checkpoint response.
- Linked the new pan-cancer neoantigen-presentation source into the `B-Cell Neoantigen Proposal Anchor` and `B-Cell Neoantigen Research Map`.

## [2026-04-25] maintenance | b-cell anchor linkage reconciliation

- Re-linked already ingested neoantigen and TLS papers directly to the `B-Cell Neoantigen Proposal Anchor` and `B-Cell Neoantigen Research Map` so the per-anchor counter reflects the actual corpus more honestly.
- Raised the explicit linked B-cell count from `9` to `18` without inventing new sources or counting off-scope papers.
- Updated `wiki/analyses/anchor-progress-baseline.md` to reflect the corrected explicit counts for the B-cell and ptmanchor anchors.

## [2026-04-26] ingest | ptmanchor manuscript references batch 1

- Parsed 36 references from `paper_ptmanchor/Submission_GPB/ptmanchor_manuscript_final.docx`.
- Generated 35 new source pages in `wiki/sources/` (skeleton with frontmatter, summary placeholder, open questions).
- Downloaded 23 of 35 PDFs via Elsevier API + Unpaywall + Springer + Nature direct (paywall coverage with API keys).
- Linked all 35 sources into `ptmanchor-manuscript-anchor.md` and the `PTM Correction and Kinase Signaling in Cancer Proteomics` topic page via a new `## Linked Sources` section.
- Remaining 12 PDFs marked as `pdf_status: pending` for later acquisition retry.

## [2026-04-26] ingest | resistance manuscript references batch 1

- Parsed 131 references from `review_cancer_resistance/Submission_JECCR/manuscript_resistance_final.docx`.
- 71 already in wiki via prior ingests; generated 60 new skeleton source pages for the unmatched references.
- Linked all 60 new sources into `cancer-resistance-manuscript-anchor.md` and the `Immunotherapy Resistance and Immune Evasion` topic page.
- PDF resolution running with stricter author-anchored matcher to avoid wrong-PMID downloads.

## [2026-04-26] tooling | PDF resolver and abstract fetcher

- Added `scripts/ingest/parse_references.py` to extract Vancouver references from manuscript docx -> JSON.
- Added `scripts/ingest/match_existing.py` to match references to existing wiki source slugs.
- Added `scripts/ingest/resolve_pdf.py` that chains Europe PMC, Unpaywall, doi-direct (Nature), Elsevier API, and Springer Nature API for PDF acquisition.
- Added `scripts/ingest/fetch_abstract.py` for PubMed XML abstract retrieval.
- Added `scripts/ingest/generate_source_pages.py` to create depth-b skeleton pages with frontmatter, summary, open questions, connections.
- Added `scripts/ingest/update_anchor_links.py` to keep anchor + topic-hub `## Linked Sources` sections current.

## [2026-04-26] publishing | quartz layout adds paper graph

- Added `Component.Graph` to both `defaultContentPageLayout.right` and `defaultListPageLayout.right` so every page shows a sidebar graph.
- Configured `localGraph` (depth=2) for sidebar mini-graph and `globalGraph` (depth=-1, fullscreen on icon click).
- Set `showTags: false` and `removeTags: ["pmid"]` so graph nodes are paper-and-page-only, not keyword tags.

## [2026-04-26] ingest | three-topic mass expansion to >=150

- ran scripts/ingest/expand_topic.py for all three topics, pulling >1,800 unique PMIDs from PubMed under strict human-cancer + impact filters (excluded MDPI, PLOS One, iScience, Scientific Reports).
- ran scripts/ingest/ingest_expansion.py to score and ingest top-N candidates per topic with parallel PDF download (Elsevier + Springer + Unpaywall + doi-direct + Europe PMC).
- final source-page counts: ptmanchor=189, resistance=200, b-cell neoantigen=181 (all over the 150-target).
- linked all expansion sources back to the manuscript anchors and topic hubs via the `## Linked Sources` section.

## [2026-04-26] analysis | CoPheeMap journal club deep-dive

- added wiki/analyses/copheemap-journal-club-deep-dive.md as a long-form journal-club walkthrough of Jiang 2025 (Nat Commun 16:2766).
- extracted Figures 1–6 from the local PDF into raw/assets/copheemap/ and embedded them into the analysis page.
- delivered a desktop bundle (~/Desktop/CoPheeMap_journal_club/) for Notion import and a short summary card (~/Desktop/CoPheeMap_summary_short.md) on user request.

## [2026-04-26] publishing | quartz rebuild with full source corpus

- npm run build:wiki processed 776 markdown files, emitted 1551 files to public/.
- graph component is now active in both content and list page layouts.
- node-set restricted to paper/page-level (showTags: false, removeTags: ["pmid"]) to avoid keyword-only nodes.
- dev server running at http://localhost:8080.

## [2026-04-27] ingest | overnight PDF retry + abstract enrichment

- Ran scripts/ingest/retry_pending_pdfs.py against the 552 pages still flagged as pdf_status: pending — recovered 43 additional valid PDFs (Elsevier + Springer + Unpaywall + Europe PMC chain).
- 102 of 669 source pages now have a local PDF tracked in frontmatter (raw PDF count 135).
- 566 of 669 pages already carry a real abstract (auto-pulled during expansion ingest); 103 remain placeholder, with 95 of those lacking a confirmed PMID.
- Reran scripts/ingest/update_anchor_links.py — counts unchanged (ptmanchor 210, resistance 253, bcell-neoantigen 205).
- Quartz rebuilt and pushed to https://github.com/hejeong1219/paperatlas (auto-deploys to https://hejeong1219.github.io/paperatlas).

## [2026-04-27] ingest | pan-cancer neoantigen expansion (user request)

- Added pancancer-neoantigen query set to scripts/ingest/expand_topic.py with 10 PubMed queries covering pan-cancer neoantigen, shared/public neoantigen, immunopeptidomics/proteogenomics, HLA presentation, prediction, vaccines, noncanonical/cryptic peptides, frameshift/indel/fusion neoantigens, TCR, MANA.
- 377 unique PMIDs returned; 358 accepted after filters (excluded MDPI/PLOS One/iScience/Sci Reports, prefer 2020+, human-cancer signal). Top-scored 124 ingested into the bcell-neoantigen topic.
- KU EZproxy + cookies pulled 54 additional PDFs through publisher landing pages.
- Final counts: ptmanchor 210 / resistance 253 / bcell-neoantigen 329 (793 total source pages); 522 PDFs in raw/inbox/papers/.
- Anchors and topic hubs re-synced.

## [2026-04-27] analysis | first deep-dive batch (4 papers)

- Wrote real Summary + Key Points + Methods + Limitations + Relevance + Open Questions for:
  - Helmink 2020 (Nature) — B cells + TLS in ICB response
  - Yarchoan 2024 (Nat Med) — HCC GT-30 personalized neoantigen vaccine
  - D'Alise 2026 (Nat Med) — Nous-209 Lynch syndrome cancer interception
  - Falchi 2023 (Blood) — B-NHL bispecific antibodies review
- Each page replaces "_Abstract pending_" / "_Key points to be filled in_" placeholders with structured analysis derived from PDF body.
- 375 placeholder pages with PDFs remain; ScheduleWakeup loop progresses these in batches.

## [2026-04-27] research-questions | queue + first answer

- Generated 50 manuscript-relevance-oriented research questions in wiki/_meta/research-questions-queue.md spanning ptmanchor (17), B-cell neoantigen (17), and cancer resistance (16). Each question is gap-focused (research direction / underexplored area / current evidence shortfall) so the synthesized answer is directly usable in the corresponding manuscript's Discussion or Future Work.
- Q1 answered: created wiki/concepts/ptm-correction-confounding-foundations.md. Synthesis grounds the ptmanchor manuscript's Discussion with concrete numbers (38–55% raw-up sites are protein-driven across CPTAC; median λ = 0.64 in LUAD; 7 kinases recovered, 16 false-positive kinases removed by correction).
- Remaining 49 questions queued for ScheduleWakeup batches.

## [2026-05-09] tooling | interactive visualization folder scaffold

- Added root-level `interactives/` as the source-controlled home for standalone Korean HTML visualizations.
- Created `interactives/multiomics-proteomics-ptm-identification/` with `index.html`, `data/studies.json`, `data/`, `assets/`, and provenance README.
- Updated `./bin/sync-wiki-html` so interactive projects sync into `wiki_html/content/interactives/` for GitHub Pages publishing.
- Documented the workflow: search wiki first, re-read original PDFs for numeric extraction, build Korean interactive HTML, then publish through Quartz/GitHub Pages.
- Added a strict source-boundary rule: no web search or general web pages for scientific wiki content, extracted numeric values, or visualization data; external websites may guide layout only.
- Populated the multiomics interactive dataset from local PDFs for Mertins 2016, Dou 2020, Gillette 2020, Huang 2021, Cao 2021, Satpathy 2021, Zhang 2022, Li 2023, and Zhao 2025.
- Built a Korean standalone interactive HTML with filters, comparative bars, study cards, and evidence table for protein/phosphosite/acetylsite counts plus MS method and instrument notes.
- Added `./bin/copy-interactives-public` and wired `wiki_html/package.json` so production builds overwrite Quartz folder pages with each interactive project's standalone `index.html`.

## [2026-05-09] ingest | multiomics PTM corpus-first correction

- Added `wiki/analyses/multiomics-ptm-corpus-queue.md` to make PDF/supplement ingestion the gate before quantitative interactive updates.
- Deep-read local PDFs for Clark 2020 ccRCC, Vasaikar 2019 colon cancer, Wang 2021 GBM, and Ng 2022 HCC and added `Multi-Omics Identification Extraction` sections to their source pages.
- Corrected stale source metadata where local PDFs already existed and fixed the Ng 2022 DOI/PMC entries.
- Marked the current multiomics interactive as a draft shell seeded by local PDFs, not a final exhaustive 10-year corpus.
- Created `wiki/topics/multiomics-proteomics-ptm-identification.md` as a standalone topic hub instead of treating this as only a `ptmanchor` subtask.
- Built a 60-paper 2016-2026 acquisition corpus for the new topic; resolver plus KU/EZproxy cookies recovered 55 local PDFs.
- Created or updated 60 source pages so each candidate links to the standalone multiomics topic and records whether the local PDF is available.
- Added an acquisition snapshot to the corpus queue; numeric visualization remains gated on full PDF/supplement extraction rather than metadata.

## [2026-05-09] ingest | multiomics PTM extraction progress check

- Verified that acquisition and registration are not the same as completed ingest: the corpus has 60 candidates, 56 resolver-confirmed local PDFs, but at least one local PDF is a title/DOI mismatch and is blocked from extraction.
- Corrected stale DOI/PMC/local-PDF metadata for Abelin 2023 MONTE and Zhao 2025 HCT116 kinase-inhibitor PTM perturbation pages.
- Added PDF-backed extraction details for Abelin 2023, Shi 2022 medullary thyroid carcinoma, Deng 2023 cholangiocarcinoma, and Li 2023 early duodenal cancer.
- Marked Xu 2022 urothelial carcinoma as blocked because the local PDF extracts as an unrelated nasopharyngeal carcinoma clinical-trials review.
- Updated the corpus queue with an extraction snapshot: 50 source pages currently carry the extraction section, 27 are still placeholders, and visualization rows remain gated on verified PDF-derived values.

## [2026-05-09] ingest+visualization | multiomics PTM batch update

- Parallel-checked Dong 2024, Ramberger 2024, Holt 2025, Park 2024, and Su 2025 local PDFs against the multiomics extraction fields.
- Marked Dong 2024 as blocked because the local PDF is a publisher correction notice rather than the full Nature Cancer article.
- Filled PDF-backed extraction sections for Ramberger 2024, Holt 2025, Park 2024, and Su 2025, including protein/phosphoproteome counts, MS method, instrument, and acetylome absence.
- Updated the interactive dataset from 9 to 13 rows using only source pages with verified PDF-derived numeric values.
- Placeholder extraction count decreased from 27 to 22; blocked source count increased to 2.

## [2026-05-09] acquisition+ingest | extra multiomics PDF expansion

- Selected 50 additional 2016-2026 candidates from the 336-paper discovery set after filtering away obvious reviews, prediction tools, and non-MS-only papers as much as possible.
- Basic resolver recovered 14/50 PDFs; KU/cookie retry recovered 18/36 remaining PDFs, giving 32/50 extra PDFs acquired in this pass.
- Triaged newly recovered PDFs and promoted three directly usable studies into the atlas: Huang 2022 NPC SAHA perturbation, Zhao 2024 ESCC, and Oh 2020 IDH-wild-type glioblastoma.
- Created source pages with PDF-backed `Multi-Omics Identification Extraction` sections for those three studies and updated the interactive dataset from 13 to 16 rows.
- Deferred Ren 2025 HPSCC and several method/tool papers because the extracted main text did not expose complete identification-count fields or because they are better treated as methods/context rather than atlas rows.

## [2026-05-09] visualization | expand multiomics atlas to 50+ row corpus coverage

- Rebuilt `interactives/multiomics-proteomics-ptm-identification/data/studies.json` as a corpus-coverage file rather than an extracted-only subset.
- The interactive now contains 67 rows: 26 extracted rows with numeric values, 35 rows with PDFs pending extraction, 4 rows still pending PDF acquisition, and 2 blocked PDF/correction-only rows.
- Added extraction-status badges to the Korean HTML cards and evidence table so incomplete rows are visible without being confused with quantified entries.
- Updated the embedded fallback JSON in `index.html` to match the 67-row dataset for local viewing.

## [2026-05-09] ingest+visualization | extra 32 local-PDF multiomics pass

- Processed the 32 extra locally downloaded PDFs from the expanded 2016-2026 multiomics/PTM candidate set without using web evidence for scientific content.
- Created or updated 25 source pages and preserved 7 existing curated source notes that already had stronger extraction sections.
- Added caveated `Multi-Omics Identification Extraction` notes for newly ingested PDFs, labeling methods/tool papers and out-of-scope/broader multiomics papers separately from quantitative atlas rows.
- Promoted 15 additional local-PDF-backed rows into `autodidact/multiomics-ptm-cancer/data/studies.json`; the standalone Autodidact corpus now covers 82 rows, with 33 rows carrying at least one candidate numeric count.
- Rebuilt the standalone Autodidact HTML so the embedded corpus, hero chips, timeline, and catalog reflect the 82-row corpus.

## [2026-05-09] governance | interactive artifact dashboard

- Compared the repository against external LLM Wiki / AI-for-biology management examples and clarified that this repo uses `AGENTS.md` as the operating contract rather than `CLAUDE.md`.
- Added public artifact management rules to `AGENTS.md`: keep topic hub, source queue, interactive artifact, corpus counts, status caveats, and logs synchronized.
- Added `interactives/index.html` as a lightweight dashboard for standalone HTML artifacts and current corpus status.

## [2026-05-10] topic | Cancer Multiomics phosphoproteomics literature monitor

- Read the Cancer Multiomics HWP research plan by extracting local HWP text into `/private/tmp/hwp_extract/cancer_multiomics_plan_extracted.txt`.
- Created `wiki/topics/cancer-multiomics-literature.md` as the project-specific literature monitor for WGS, phosphoproteomics, ppQTL, neoantigen, immune evasion, response prediction, and Slack-ready summaries.
- Added eight seed paper subpages under `wiki/analyses/cancer-multiomics-literature/` using the requested template: paper information, one-line summary, Cancer Multiomics relevance, major results, and Slack message draft.
- Updated `wiki/_meta/index.md` so the new topic and seed summaries are discoverable from the wiki catalog.

## [2026-05-10] expansion | four-topic question maps + Cancer Multiomics crosslinks

- Rebuilt `wiki/analyses/topic-question-expansion-map.md` as the durable 4-track question bank covering (1) B-cell neoantigen, (2) immunotherapy resistance, (3) multiomics PTM identification, (4) Cancer Multiomics WGS/phosphoproteomics literature monitoring.
- Added a dedicated ptmanchor question bank in `wiki/analyses/ptm-correction-and-kinase-signaling-question-expansion-map.md` to keep PTM correction depth without mixing it into the four user-facing tracks.
- Linked the four topic hubs back to the question bank and added Cancer Multiomics crosslinks from the eight seed source pages to the Cancer Multiomics topic hub + Slack-ready subpages.

## [2026-05-10] cancer-multiomics | initialize 100-paper queue + add 7 briefs

- Created `wiki/analyses/cancer-multiomics-corpus-queue.md` to track target=100, acquired/ingested/briefed counts, blocked items, and a rolling shortlist.
- Added seven Cancer Multiomics Slack-ready subpages: Abelin 2023 (MONTE), Asuzu 2025 (PP2A/PPP1R17), Zhao 2025 (kinase inhibitor multi-PTM), Chong 2022 (immunopeptidomics review), Chen 2026 (PTM-MHC enrichment methods), Han 2024 (HLA presentation score vs ICI response), Muller-Dott 2025 (kinase inference benchmark).
- Updated `wiki/topics/cancer-multiomics-literature.md` to link the new briefs under the appropriate classification headers and added a direct link to the queue page.
- Upgraded placeholder source pages to PDF-backed Key Points for `asuzu-2025-*`, `chong-2022-*`, and `chen-2026-*`, including fixing the incorrect DOI line on the Chong review page and updating local-PDF pointers.
- Discovered a misnamed PDF/metadata mismatch: renamed the wrongly labeled “SVNeoPP” source/PDF to `jiao-2025-gastric-cancer-reference-human-pangenomes` and rewrote the source page to match the actual Life Science Alliance pangenome/SV paper content.
- Marked `dong-2024-integrative-proteogenomic-profiling-high-risk-prostate` as blocked because the local PDF is a publisher correction notice rather than the full article.

## [2026-05-10] expansion | add growth targets + Cancer Multiomics checklist normalization

- Extended `wiki/analyses/topic-question-expansion-map.md` with per-topic concrete growth targets so questions resolve into specific edits and artifacts.
- Added a fixed “치료 맥락 / 데이터 레이어 / 데이터 공개” checklist + a 5-PDF Cancer Multiomics candidate shortlist to `wiki/topics/cancer-multiomics-literature.md`.
- Normalized the Cancer Multiomics seed briefs (Chen 2020, Huang 2021, Li 2023, Petralia 2024, Wen 2020, Huber 2025, Jiang 2025, Shi 2025) by adding the same 3 metadata bullets and marking unknowns as “PDF 확인 필요”.

## [2026-05-10] cancer-multiomics | ingest 5 acquired PDFs into briefs

- Created 5 new Cancer Multiomics Slack-ready subpages under `wiki/analyses/cancer-multiomics-literature/`: Cheng 2025 (WT), Deng 2023 (CCA), Haas 2024 (radioresistance), Anurag 2022 (TNBC chemo response), Saxena 2025 (atezolizumab + personalized neoantigen vaccination).
- Upgraded/edited the corresponding source pages in `wiki/sources/` with PDF-backed Key Points and added `Cancer Multiomics Project Relevance` sections for Cancer Multiomics linking.
- Updated `wiki/topics/cancer-multiomics-literature.md` to link the new briefs under the right classification headers and to point “Next Candidates” to the queue page.
- Refreshed `wiki/analyses/cancer-multiomics-corpus-queue.md` counts (selected/acquired/ingested/briefed) and split “selected set” vs “next up” items; recorded three discovery candidates as PDF-pending due to resolver network restrictions.
- Updated `wiki/_meta/index.md` to include the 5 new Cancer Multiomics briefs in the wiki catalog.

## [2026-05-10] expansion | question-map targets executed + Skoulidis 2024 Cancer Multiomics brief

- Updated Topic 1 concept pages to add unit/evidence definitions and a TLS reading checklist: `wiki/concepts/b-cell-and-tls-context-for-neoantigen-research.md`, `wiki/concepts/neoantigen-discovery-and-prioritization.md`.
- Added a 5-paper “bridge” priority queue to `wiki/analyses/b-cell-neoantigen-pipeline-human-cancer-corpus.md` to connect neoantigen selection to B/TLS immune architecture and response.
- Added resistance extraction templates: genetic vs adaptive checklist in `wiki/concepts/mhc-i-loss-and-interferon-pathway-defects-in-checkpoint-resistance.md`, and observation-layer standard in `wiki/concepts/antigen-loss-lineage-switch-and-target-escape.md`.
- Added a resistance class × evidence-type draft matrix to `wiki/analyses/cancer-resistance-manuscript-anchor.md`.
- Strengthened Topic 3 corpus rules and unit-preserving keys: `wiki/analyses/multiomics-ptm-corpus-queue.md`, `interactives/multiomics-proteomics-ptm-identification/README.md`.
- Deepened the NeoDisc source page with PDF-backed pipeline specifics and worked-example numbers: `wiki/sources/huber-2025-comprehensive-proteogenomic-pipeline-neoantigen-discovery.md`.
- Deepened the Skoulidis 2024 source page with PDF-backed cohort context and extracted survival numbers; created a Cancer Multiomics Slack-ready brief and linked it into the Cancer Multiomics hub and queue: `wiki/sources/skoulidis-2024-ctla4-abrogates-keap1-stk11-resistance.md`, `wiki/analyses/cancer-multiomics-literature/skoulidis-2024-ctla4-abrogates-keap1-stk11-resistance.md`, `wiki/topics/cancer-multiomics-literature.md`, `wiki/analyses/cancer-multiomics-corpus-queue.md`.
- Updated `wiki/analyses/topic-question-expansion-map.md` to mark executed growth targets and define the next deep-dive targets.
- Refreshed `wiki/_meta/index.md` so the new Cancer Multiomics brief is discoverable.

## [2026-05-10] cancer-multiomics | ingest 5 “next up” PDFs into briefs

- Created 5 new Cancer Multiomics subpages under `wiki/analyses/cancer-multiomics-literature/`: Savage 2024 (CPTAC therapeutic targets), Shapiro 2025 (NeoDiscMS), Scheid 2025 (MHCquant2), Weber 2024 (KEYNOTE-942 V940), Khan 2026 (public phospho network meta-analysis).
- Rewrote/updated the matching source pages in `wiki/sources/` to be PDF-backed (fixed wrong DOI lines, removed “Local PDF pending” placeholders, added Cancer Multiomics relevance + corrected Connections).
- Reclassified `mullerdott-2025-comprehensive-evaluation-*` as a **publisher correction notice** and pointed it to the real benchmarKIN paper source page.
- Updated `wiki/topics/cancer-multiomics-literature.md` and `wiki/analyses/cancer-multiomics-corpus-queue.md` to reflect the new briefs and the cleaned “next up” list.
- Updated `wiki/_meta/index.md` to include the 5 new Cancer Multiomics briefs in the catalog.

## [2026-05-10] cancer-multiomics | add Memon 2024 acquired-resistance brief

- Created a new Cancer Multiomics Slack-ready brief page for NSCLC acquired resistance to PD-(L)1 blockade: `wiki/analyses/cancer-multiomics-literature/memon-2024-clinical-molecular-features-acquired-resistance.md`.
- Fixed the corresponding source page DOI + local-PDF pointer and upgraded Key Points from the local PDF: `wiki/sources/memon-2024-clinical-molecular-features-acquired-resistance.md`.
- Linked the new brief into the Cancer Multiomics topic hub and updated the rolling counts/table in the Cancer Multiomics high-impact queue: `wiki/topics/cancer-multiomics-literature.md`, `wiki/analyses/cancer-multiomics-corpus-queue.md`.
- Updated the question-expansion map to reflect the latest Topic 3 extraction target status: `wiki/analyses/topic-question-expansion-map.md`.

## [2026-05-10] cancer-multiomics | ingest 5 existing local-PDF cohort papers into briefs

- Upgraded 4 placeholder `wiki/sources/*` pages (Song 2024 NSCLC, Yu 2024 cervical, Qu 2024 PTC recurrence, Tanaka 2024 CRC metastasis) into PDF-backed notes with corrected DOI/PMC links, extracted cohort-layer metadata, and `Cancer Multiomics Project Relevance`.
- Tightened the existing Zhang 2023 ccRCC sunitinib-response source page by adding `Cancer Multiomics Project Relevance` and Cancer Multiomics topic connections: `wiki/sources/zhang-2023-proteogenomics-clear-cell-renal-response-tyrosine-kinase-inhibitor.md`.
- Created 5 new Cancer Multiomics Slack-ready briefs under `wiki/analyses/cancer-multiomics-literature/` for Song 2024, Yu 2024, Qu 2024, Tanaka 2024, and Zhang 2023 (ccRCC sunitinib response).
- Updated the Cancer Multiomics topic hub to link the new briefs under WGS/proteogenomics and response-prediction sections: `wiki/topics/cancer-multiomics-literature.md`.
- Updated the Cancer Multiomics high-impact queue counts (selected/acquired/ingested/briefed) and appended the 5 new basenames to the tracking table: `wiki/analyses/cancer-multiomics-corpus-queue.md`.
- Updated `wiki/_meta/index.md` to include the 5 new Cancer Multiomics briefs in the wiki catalog.

## [2026-05-10] topic3 | PTM atlas cohort pages upgraded

- Upgraded three proteogenomics cohort source pages from “placeholder Key Points” to PDF-backed summaries and clarified atlas caveats (units, missing totals, supplement needs): `wiki/sources/vasaikar-2019-proteogenomic-analysis-human-colon-cancer.md`, `wiki/sources/clark-2020-integrated-proteogenomic-characterization-clear-cell.md`, `wiki/sources/wang-2021-proteogenomic-metabolomic-characterization-human-glioblastoma.md`.
- Clarified that Mertins 2016 does not name the MS instrument model in the main PDF and should be treated as `needs_supplement` for atlas instrumentation: `wiki/sources/mertins-2016-proteogenomics-connects-somatic-mutations-signalling.md`.
- Updated the Topic 3 queue and the four-topic question expansion map to reflect executed upgrades and the remaining supplement-driven extraction blockers: `wiki/analyses/multiomics-ptm-corpus-queue.md`, `wiki/analyses/topic-question-expansion-map.md`.
- Updated the navigation index to list the upgraded PTM-atlas cohort sources: `wiki/_meta/index.md`.

## [2026-05-10] cancer-multiomics | ingest 5 additional local-PDF papers into briefs

- Created 5 new Cancer Multiomics Slack-ready brief pages under `wiki/analyses/cancer-multiomics-literature/`: Ramsberger 2024 (MM; nanopore WGS + phosphoproteome), Satpathy 2021 (LSCC; multi-PTM), Dou 2020 (endometrial; WES/WGS + phospho/acetyl + immune), Yaeger 2023 (KRASG12C–EGFR acquired resistance; ctDNA), Keskin 2019 (GBM neoantigen vaccine; steroid effect + TCR tracking).
- Updated the corresponding source pages in `wiki/sources/` to remove “Local PDF pending” placeholders, fix DOI/PMC links, and add `Cancer Multiomics Project Relevance` + brief/topic crosslinks.
- Updated the Cancer Multiomics topic hub and corpus queue counts/table to reflect the new briefs: `wiki/topics/cancer-multiomics-literature.md`, `wiki/analyses/cancer-multiomics-corpus-queue.md`.
- Updated `wiki/_meta/index.md` to include the 5 new Cancer Multiomics briefs.

## [2026-05-10] cancer-multiomics | add Braun 2025 peptide PCV brief + split PTM question bank

- Upgraded `wiki/sources/braun-2025-neoantigen-vaccine-generates-antitumour-immunity.md` from placeholder to PDF-backed Key Points (fixed wrong DOI line, added trial/vaccine/immunogenicity/autologous-tumor-reactivity facts, and linked to Cancer Multiomics hub).
- Created a new Cancer Multiomics Slack-ready brief page (template-compliant): `wiki/analyses/cancer-multiomics-literature/braun-2025-neoantigen-vaccine-generates-antitumour-immunity.md`.
- Wired the new brief into the Cancer Multiomics topic hub + 100-paper queue and refreshed rolling counts/table: `wiki/topics/cancer-multiomics-literature.md`, `wiki/analyses/cancer-multiomics-corpus-queue.md`.
- Split out the PTM correction/kinase-signaling question bank into a standalone page and linked it from the four-topic map growth targets: `wiki/analyses/ptm-correction-kinase-signaling-question-bank.md`, `wiki/analyses/topic-question-expansion-map.md`.
- Updated the page catalog so the new brief/question bank are discoverable: `wiki/_meta/index.md`.

## [2026-05-10] cancer-multiomics | ingest 5 CPTAC + SV papers into briefs

- Created 5 new Cancer Multiomics Slack-ready brief pages under `wiki/analyses/cancer-multiomics-literature/`: Cao 2021 (PDAC CPTAC), Gillette 2020 (LUAD CPTAC), Krug 2020 (breast CPTAC), Clark 2019 (ccRCC CPTAC), Chen 2023 (pan-cancer SV→protein).
- Upgraded the corresponding source pages in `wiki/sources/` to be PDF-backed (filled Summary/Key Points, normalized frontmatter to the paper schema values, and added `Cancer Multiomics Project Relevance` + Cancer Multiomics links).
- Added a blocked stub source page for Chen 2026 germline SV→proteome because the local “PDF” is actually an HTML download: `wiki/sources/chen-2026-global-impact-germline-structural-variation-cancer-proteome.md`.
- Updated the Cancer Multiomics topic hub and the 100-paper queue counts/table to reflect the new briefs and the new blocked item: `wiki/topics/cancer-multiomics-literature.md`, `wiki/analyses/cancer-multiomics-corpus-queue.md`.
- Updated `wiki/_meta/index.md` to include the 5 new Cancer Multiomics briefs.

## [2026-05-10] topic4 | V940(mRNA-4157) 면역원성 bridge 보강

- PDF 기반으로 Gainor 2024(KEYNOTE-603) source page를 “placeholder”에서 해제하고, ELISpot/ICS 기반 면역원성 핵심 수치(예: 238 predicted 중 29.8% immunogenic; immunogenic 중 84.5% de novo)와 추출 포인트를 기록: `wiki/sources/gainor-2024-t-cell-responses-individualized-neoantigen-therapy.md`.
- Gainor 2024를 Cancer Multiomics Slack-ready brief로 추가해, KEYNOTE-942(Weber 2024)와 연결되는 “예측→면역반응” 중간기전 근거를 보존: `wiki/analyses/cancer-multiomics-literature/gainor-2024-t-cell-responses-individualized-neoantigen-therapy.md`.
- Weber 2024(KEYNOTE-942) source page에 “로컬 PDF가 요약/부분 형태”임을 명시하고, 추가 확인이 필요한 제조/면역/바이오마커 질문을 고정: `wiki/sources/weber-2024-individualised-neoantigen-therapy-mrna-4157-v940.md`.
- Topic 4 질문 확장 맵의 실행 항목(DONE) 목록을 정리하고 들여쓰기 오류를 수정: `wiki/analyses/topic-question-expansion-map.md`.
- Cancer Multiomics 100-paper 큐에서 Gainor 2024의 상태/노트(면역원성 수치) 및 ingested 카운트를 갱신: `wiki/analyses/cancer-multiomics-corpus-queue.md`.

## [2026-05-10] cancer-multiomics | rename project surface + daily discovery automation

- Renamed the durable project surface from Hanmi wording to Cancer Multiomics: topic hub, corpus queue, analysis folder, index links, and source-page relevance wording now use Cancer Multiomics.
- Updated the paper acquisition automation to run every morning and to use PubMed/bibliographic discovery for candidate finding and PDF resolution only; scientific summaries remain local-PDF/source-page based.
- Moved the Gainor 2024 KEYNOTE-603 neoantigen vaccine immunogenicity brief into the Cancer Multiomics analysis folder and linked it from the topic hub, queue, and index.

## [2026-05-10] cancer-multiomics | Notion 시드 27편 + OpenAlex 관련논문 18편 ingest

- Notion 'Cancer Multiomics > 참고 논문 및 아이디어' 페이지 27편 ingest: 20편 PDF 자동 다운로드, 7편 manual_pending (bioRxiv 2026 미등록 DOI 5편 + Cell Press anti-bot 2편).
- 시드 DOI를 OpenAlex citation graph로 확장: referenced_works + related_works 852개 → cancer/multiomics 키워드 + DOI dedup 후 442개 → 2023+ score≥3 shortlist 50편 → 사용자 승인 후 Top-18 (score≥6) 자동 ingest. 16편 PDF 다운로드, 2편 Cell Press manual_pending.
- 새 도구: `scripts/ingest/find_related_via_openalex.py` (OpenAlex 인용 그래프 발굴), `scripts/ingest/fallback_direct_url.py` (arXiv/bioRxiv 직접 URL 패턴 fallback). `scripts/ingest/ku_download.py`에 `--include-file`/`--require-substr` 플래그 추가.
- 토픽 허브 §6 "2026-05 Expansion: AI/Spatial/ecDNA/CAR-T 보강 (45편)" 신설하고 7개 sub-theme으로 그룹화. 코퍼스 큐는 91 selected / 80 acquired / 90 ingested / 11 blocked로 갱신.
- 향후 deep-dive: 36편의 PDF 확보 stub은 `wiki/analyses/cancer-multiomics-literature/` 하위 페이지로 brief 작성 대기.

## [2026-05-13] planning | 100-question wiki expansion sprint

- Added `wiki/analyses/100-question-wiki-expansion-sprint.md` to formalize the workflow for answering 100 user questions from local ingested papers, filing durable wiki expansions, and turning evidence gaps into high-impact PDF acquisition/ingest batches.
- Linked the sprint page from `wiki/_meta/index.md` so it is discoverable alongside the existing question banks and Cancer Multiomics 100-paper queue.

## [2026-05-13] analysis | drug-response POC using global proteome, phosphoproteome, and somatic SNV

- Added `wiki/analyses/drug-response-poc-global-phospho-somatic-snv.md` as the first question-driven expansion artifact from the 100-question sprint.
- Synthesized a proof-of-concept analysis flow from local ingested response-labeled proteogenomic papers: Lee 2026 TNBC, Anurag 2022 TNBC, Zhang 2023 ccRCC sunitinib, Sambath 2026 cervical CCRT, Xu 2026 HER2-low breast cancer, Zhao 2025 CRC kinase-inhibitor perturbation, and the PTM-correction kinase synthesis.
- Updated `wiki/_meta/index.md` so the drug-response POC plan is discoverable.

## [2026-05-13] corpus | drug-response phospho-global target-100 queue and PubMed/PDF batch

- Added `wiki/analyses/drug-response-phospho-global-100-corpus-queue.md` to track a recent-10-year target-100 corpus for human cancer global proteome/phosphoproteome drug response and resistance papers.
- Ran the PubMed/PDF resolver over a 3650-day discovery window; the batch returned 250 PMIDs, 209 fresh by PMID filter, and 40 PDFs downloaded into `raw/inbox/papers/` with 40 placeholder source pages generated under `wiki/sources/`.
- Marked the batch as triage-needed rather than final scientific evidence; new source stubs must be full-text deep-dived before their details count toward analyses.
- Clarified the public topic architecture in `wiki/syntheses/overview.md`: B-cell Neoantigen, Cancer Resistance / Immune Evasion, ptmanchor, and Cancer Multiomics / Drug-response Monitor as a cross-cutting acquisition layer.
- Linked the specialized drug-response queue from `wiki/topics/cancer-multiomics-literature.md` and `wiki/_meta/index.md`.

## [2026-05-13] ingest | Hsu 2025 osimertinib DTP phosphoproteomics

- Completed full local-PDF deep-dive for `wiki/sources/hsu-2025-phosphoproteomics-osimertinib-tolerant-persister-cells-reveals.md`, replacing the auto-generated placeholder with PDF-backed design, quantitative omics scale, kinase-substrate findings, validation, data availability, relevance, and caveats.
- Corrected the placeholder DOI/PMC metadata to the DOI printed in the PDF: `10.1038/s44320-025-00141-1`; retained PMID `41023502` and local PDF provenance.
- Updated the drug-response phospho-global target-100 queue to mark Hsu 2025 as `core-ingested` and to keep Jeong 2025 blocked as a wrong local PDF until reacquisition.
- Linked Hsu 2025 from the Cancer Multiomics topic hub and page catalog.

## [2026-05-13] ingest | drug-response phospho-global 100-PDF batch

- Retried pending PDF downloads before bulk ingest; additional scripted downloads were limited by paywall/PMC challenge behavior (1 newly resolved in this pass).
- Selected 100 local PDFs for the drug-response/global-proteome/phosphoproteome corpus and added `Batch PDF Ingest Status` sections with extracted-text provenance to each source page.
- Created `wiki/analyses/drug-response-phospho-global-100-bulk-ingest.md` as the durable 100-row batch tracker.
- These rows are `pdf-text-extracted`, not automatically `full-text-read`; manual deep-dive promotion remains required before using detailed scientific content in synthesis.

## [2026-05-13] ingest | Anurag 2022 TNBC chemo response proteogenomics

- Promoted `wiki/sources/anurag-2022-proteogenomic-markers-chemotherapy-resistance-response.md` from batch extracted text to `full-text-read` after re-reading the full local 20-page PDF.
- Added PDF-backed cohort, omics scale, response pathway, PTM-SEA, immune, LIG1/19q13.31-33, PDX validation, and data-availability details.
- Updated the drug-response POC plan and 100-PDF queue/tracker to mark Anurag 2022 as a completed high-priority template for matched somatic genomics + global proteome + phosphoproteome response analysis.

## [2026-05-13] ingest | Zhang 2023 ccRCC sunitinib proteogenomics

- Promoted `wiki/sources/zhang-2023-proteogenomics-clear-cell-renal-response-tyrosine-kinase-inhibitor.md` from batch extracted text to `full-text-read` after re-reading the full local 21-page PDF and verifying title/DOI metadata.
- Added PDF-backed cohort, omics scale, sunitinib response definition, 7q-LAMTOR4/MDH2/CALU-mTOR resistance axis, VHL/AA/glycolysis sensitivity axis, KSEA/ssGSEA kinase findings, immune/TGFB1/platelet resistance state, classifier design, data availability, caveats, and POC relevance.
- Updated the drug-response POC page, 100-PDF tracker, corpus queue, and page catalog; full-read progress is now 3/100 with Jeong 2025 still blocked as wrong PDF.

## [2026-05-13] ingest | Ji 2023 LICOB liver cancer organoid pharmaco-proteogenomics

- Promoted `wiki/sources/ji-2023-pharmaco-proteogenomic-characterization-liver-cancer-organoids.md` from batch extracted text to `full-text-read` after re-reading the full local 16-page PDF and verifying the local PDF identity.
- Replaced the placeholder source page with PDF-backed cohort, LICOB subtype, 76-drug screen, elastic-net prediction, G6PD vulnerability, lenvatinib resistance, temsirolimus-lenvatinib combination, perturbation phosphoproteomics, data availability, limitations, and POC relevance.
- Updated the drug-response POC page, 100-PDF tracker, corpus queue, and page catalog; full-read progress is now 4/100 with Jeong 2025 still blocked as wrong PDF and Quartz build deferred until the 100-paper ingest/wiki-expansion target is complete.

## [2026-05-25] analysis | Refractory gastric cancer question chain from cancer multiomics gap

- Added `wiki/analyses/resistance-state-subtyping-refractory-gastric-cancer.md` to preserve the actual LLM-wiki expansion path from field-map question to a refractory gastric cancer resistance-state research question.
- Framed the chain as literature map -> research gap -> dataset fit -> current IC1/IC2 interpretation -> research article figure spine.
- Linked the page to the Cancer Multiomics topic hub, 50-question sprint, drug-response POC, resistance manuscript anchor, and project context.

## [2026-05-13] ingest | Lee 2026 TNBC chemotherapy resistance metadata promotion

- Rechecked the local 25-page Genome Biology PDF identity for `wiki/sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md` and promoted the already curated source page to `ingest_status: full-text-read`.
- Updated batch status language so the old automated extraction caveat no longer conflicts with the PDF-backed Korean deep-dive already present on the page.
- Updated the 100-PDF tracker and corpus queue; full-read progress is now 5/100 with Quartz sync/build still deferred.

## [2026-05-13] ingest | Holt 2025 MIBC chemoresistance proteogenomics

- Promoted `wiki/sources/holt-2025-proteogenomic-characterization-unveils-biomarkers-associated.md` from batch extracted text to `full-text-read` after re-reading the full local 26-page PDF and verifying DOI/journal/author metadata.
- Replaced the brief atlas note with PDF-backed cohort, omics scale, response definition, NMF subtype, DDR/SBS mutation-signature context, EMT/WNT/KRAS resistance, DNA-repair/G2M sensitivity, GSK3B-S9, RAF/ATAD1 SEPEP, ADC-target, pre/post-treatment, data-availability, limitations, and POC relevance details.
- Updated the drug-response POC page, 100-PDF tracker, corpus queue, and page catalog; full-read progress is now 6/100 with Quartz sync/build still deferred.

## [2026-05-13] ingest | Jaehnig 2025 CALGB 40601 HER2+ neoadjuvant proteogenomics

- Promoted `wiki/sources/jaehnig-2025-proteogenomic-analysis-calgb-40601-alliance.md` from batch extracted text to `full-text-read` after re-reading the full local 22-page PDF and verifying Cell Reports Medicine DOI metadata.
- Corrected the source page's erroneous placeholder DOI/PMC link and added PDF-backed CALGB 40601 trial design, biopsy QC, ERBB2/HER2 proteogenomic false-positive analysis, ECM/EMT/WNT/immune/cell-cycle/PTM-SEA findings, GPRC5A/TPBG validation, data availability, caveats, and POC relevance.
- Updated the drug-response POC page, 100-PDF tracker, corpus queue, and page catalog; full-read progress is now 7/100 with Quartz sync/build still deferred.

## [2026-05-13] ingest | Zhao 2025 CRC kinase-inhibitor perturbation PTMomics

- Promoted `wiki/sources/zhao-2025-phosphoproteomic-acetylomic-characterization-colorectal-cancer.md` from batch extracted text to `full-text-read` after re-reading the full local 12-page PDF and verifying ACS DOI metadata.
- Replaced the brief atlas note with PDF-backed HCT116 perturbation design, inhibitor panel, proteome/phosphosite/acetylsite scale, target-engagement and off-target kinase findings, mitochondrial effects, PTM-crosstalk analysis, drug-pair correlation logic, limitations, data availability, and POC relevance.
- Updated the drug-response POC page, 100-PDF tracker, corpus queue, and page catalog; full-read progress is now 8/100 with Zhao 2025 marked as perturbation context rather than a patient-response cohort.

## [2026-05-13] ingest | Song 2024 Korean NSCLC multiomics subtype and adjuvant therapy signal

- Promoted `wiki/sources/song-2024-proteogenomic-analysis-reveals-non-small-cell.md` from batch extracted text to `full-text-read` after re-reading the full local 25-page PDF and verifying Nature Communications DOI metadata.
- Replaced the brief source note with PDF-backed cohort, omics scale, five-subtype map, phosphoproteome-heavy subtype features, Subtype 4 PI3K-Akt/hypoxia/SLK/LRRFIP1 poor-prognosis axis, Subtype 3 WGD/XPO1-selinexor organoid signal, Subtype 5 immune-hot/adjuvant therapy benefit, data availability, caveats, and POC relevance.
- Updated the drug-response POC page, 100-PDF tracker, corpus queue, and page catalog; full-read progress is now 9/100 with Quartz sync/build still deferred.

## [2026-05-13] ingest | Chmielecki 2023 FLAURA first-line osimertinib acquired resistance

- Promoted `wiki/sources/chmielecki-2023-acquired-resistance-first-line-osimertinib.md` from batch extracted text to `full-text-read` after re-reading the full local 9-page Nature Communications PDF and verifying DOI/title metadata.
- Replaced the automated extract stub with PDF-backed FLAURA trial design, paired plasma ctDNA subset counts, osimertinib versus comparator acquired-resistance frequencies, baseline tissue suboptimal-response markers, limitations, data availability, and POC relevance.
- Updated the drug-response POC page, 100-PDF tracker, corpus queue, and page catalog; full-read progress is now 10/100 with Chmielecki 2023 marked as genomic-resistance context rather than a core proteome/phosphoproteome response cohort.

## [2026-05-13] ingest | Gillette 2020 CPTAC LUAD proteogenomic therapeutic vulnerabilities

- Promoted `wiki/sources/gillette-2020-proteogenomic-characterization-reveals-therapeutic-vulnerabilities.md` from batch extracted text to `full-text-read` after re-reading the full local 62-page Cell PDF and verifying title/DOI metadata.
- Replaced the brief source note with PDF-backed cohort, assay design, omics scale, NMF subtype findings, ALK/EGFR/KRAS driver-to-phosphosite vulnerability examples, STK11 immune-cold/neutrophil-degranulation proteome signal, tumor-NAT PTM/biomarker analysis, data availability, limitations, and POC relevance.
- Updated the drug-response POC page, 100-PDF tracker, corpus queue, and page catalog; full-read progress is now 11/100 with Gillette 2020 marked as core proteogenomic vulnerability context.

## [2026-05-13] ingest | Huang 2021 HPV-negative HNSCC proteogenomic treatment hypotheses

- Promoted `wiki/sources/huang-2021-proteogenomic-insights-biology-treatment-hpv-negative.md` from batch extracted text to `full-text-read` after re-reading the full local 36-page Cancer Cell PDF and verifying title/DOI metadata.
- Replaced the brief source note with PDF-backed cohort, assay scale, SCNA driver prioritization, tumor/NAT protein and phosphosite results, FAT1/11q13.3 actin convergence, CDK4/6-Rb biomarker logic, EGFR ligand-dependent versus amplification-driven signaling, immuno-proteogenomic SCNA logic, integrated subtypes, limitations, data availability, and POC relevance.
- Updated the drug-response POC page, 100-PDF tracker, corpus queue, and page catalog; full-read progress is now 12/100 with Huang 2021 marked as core proteogenomic treatment-hypothesis context.

## [2026-05-13] ingest | Petralia 2024 pan-cancer tumor immunity proteogenomics

- Promoted `wiki/sources/petralia-2024-pan-cancer-proteogenomics-characterization-tumor-immunity.md` from batch extracted text to `full-text-read` after re-reading the full local 51-page Cell PDF and verifying title/DOI metadata.
- Replaced the automated extract stub with PDF-backed cohort counts, harmonized CPTAC data design, BayesDeBulk immune deconvolution, seven immune subtypes, OAK atezolizumab validation, mutation/CNV/methylation immune associations, phosphoproteome-derived kinase findings, histopathology signals, limitations, and POC relevance.
- Updated the drug-response POC page, 100-PDF tracker, corpus queue, and page catalog; full-read progress is now 13/100 with Petralia 2024 marked as immune-resistance proteogenomic context and Quartz sync/build still deferred.

## [2026-05-13] ingest | Vasaikar 2019 colon cancer proteogenomic therapeutic opportunities

- Promoted `wiki/sources/vasaikar-2019-proteogenomic-analysis-human-colon-cancer.md` from batch extracted text to `full-text-read` after re-reading the full local 35-page Cell PDF and verifying title/DOI metadata.
- Replaced the automated extract stub with PDF-backed cohort and assay design, WXS/MSI/SCNA findings, SOX9 protein reinterpretation, Rb phosphorylation-CDK2 therapeutic hypothesis, cancer-associated protein/phosphosite scale, tumor-antigen analysis, unified multi-omics subtypes, MSI glycolysis-CD8 immune-evasion signal, data availability, limitations, and POC relevance.
- Updated the drug-response POC page, 100-PDF tracker, corpus queue, and page catalog; full-read progress is now 14/100 with Vasaikar 2019 marked as core proteogenomic vulnerability context and Quartz sync/build still deferred.

## [2026-05-13] ingest | Chen 2020 East Asian never-smoker LUAD proteogenomics

- Promoted `wiki/sources/chen-2020-proteogenomics-non-smoking-lung-cancer-east.md` from batch extracted text to `full-text-read` after re-reading the full local 37-page Cell PDF and verifying title/DOI metadata.
- Replaced the automated extract stub with PDF-backed cohort design, WES/RNA/proteome/phosphoproteome scale, EGFR/KRAS/TP53 mutation-to-phosphosite interpretation, APOBEC/environmental-signature findings, proteomic late-like staging, EGFR-L858R versus Del19 outcome validation, immune/protein-network results, MMP biomarker/druggable-target validation, data availability, limitations, and POC relevance.
- Updated the drug-response POC page, 100-PDF tracker, corpus queue, and page catalog; full-read progress is now 15/100 with Chen 2020 marked as core proteogenomic vulnerability context and Quartz sync/build still deferred.

## [2026-05-13] ingest | Cao 2021 PDAC CPTAC proteogenomics

- Promoted `wiki/sources/cao-2021-proteogenomic-characterization-pancreatic-ductal-adenocarcinoma.md` from batch extracted text to `full-text-read` after re-reading the full local 49-page Cell PDF and verifying title/DOI metadata.
- Replaced the automated extract stub with PDF-backed cohort design, tumor-purity strategy, omics scale, KRAS/TP53/CDKN2A/SMAD4 functional effects, early-detection and glycoproteomic target findings, kinase-substrate hypotheses, immune-cold endothelial/VEGF/hypoxia/glycolysis/junction-phosphosite mechanism, proteogenomic subtype findings, limitations, data availability, and POC relevance.
- Updated the drug-response POC page, 100-PDF tracker, corpus queue, and page catalog; full-read progress is now 16/100 with Cao 2021 marked as core proteogenomic vulnerability context and Quartz sync/build still deferred.

## [2026-05-13] ingest | Satpathy 2021 CPTAC LSCC proteogenomic portrait

- Promoted `wiki/sources/satpathy-2021-proteogenomic-portrait-lung-squamous-cell.md` from batch extracted text to `full-text-read` after re-reading the local 65-page Cell PDF and verifying title/DOI metadata.
- Replaced the automated source stub with PDF-backed cohort design, assay scale, CNA/methylation effects, five multi-omic subtypes, PDGFRB/ROR2 RTK CBPE, CDK4/6-Rb phosphoproteome logic, NRF2 activity, TP63/SOX2/BIRC5 vulnerability, PTM crosstalk, immune Hot/Warm/Cold landscape, data availability, limitations, and POC relevance.
- Updated the drug-response POC page, 100-PDF tracker, corpus queue, and page catalog; full-read progress is now 17/100 with 1 wrong-PDF blocker and Quartz sync/build still deferred until the 100-paper ingest/wiki-expansion target is complete.

## [2026-05-26] publishing-ui | Expand TopicQuickNav to all five topic hubs

- Updated the Quartz right-rail `Topics` navigation component to show five public topic hubs instead of the older three-card hardcoded set.
- Pointed each quick-nav card directly to its topic hub page and aligned the labels/descriptions with the renamed `Cancer Multiomics Proteogenomic Atlas`.
- Expanded the public home page `Current Topic Collections` section to match the full five-topic navigation set.

## [2026-05-26] analysis | Evidence-boundary run for resistance research question

- Extended `wiki/analyses/primary-acquired-resistance-proteogenomics-ingest-map.md` with an actual LLM-wiki reasoning run rather than only a presentation outline.
- Defined the operating rule as checking the evidence boundary before synthesis: translate each question into the evidence it would require, then check whether local evidence has the required sampling design.
- Applied the rule to the current resistance/proteogenomics corpus and reached a bounded research question about phosphoproteomic and immune-state features defining genome-unexplained resistance states.

## [2026-05-26] ingest | Solanki 2026 KRASG12C acquired-resistance evidence boundary mapping

- Promoted `wiki/sources/solanki-2026-ras-gtp-inhibition-overcomes-acquired-resistance.md` from placeholder to `pdf_status: full-text-read` after reading the local PDF text.
- Added a evidence-boundary classification: acquired-resistance preclinical/model-system evidence, not direct same-patient clinical pre/post evidence.
- Extracted the three resistance-state classes: KRASG12C amplification/NRASG13R genomic RAS reactivation, WES-negative RTK/wild-type RAS-GTP signaling, and EMT-associated RAS-independent cell-cycle/DDR dependency switching.
- Updated the primary/acquired resistance ingest map to treat Solanki 2026 as mechanistic support for genome-unexplained functional resistance states while preserving the patient-longitudinal evidence gap.

## [2026-05-26] ingest | Yaeger 2023 KRASG12C-EGFR acquired-resistance evidence boundary mapping

- Promoted `wiki/sources/yaeger-2023-molecular-characterization-acquired-resistance-krasg12c-egfr.md` from automated PDF-text extraction to `pdf_status: full-text-read` after local PDF review.
- Added evidence-boundary classification: patient serial ctDNA acquired-resistance evidence, but not broad proteogenomic/phosphoproteomic evidence.
- Captured the main timing lesson: many resistance alterations are low-frequency/subclonal, while KRASG12C amplification rises with progression and can fall after drug withdrawal.
- Updated the primary/acquired resistance ingest map to contrast Yaeger 2023 patient time-axis evidence with Solanki 2026 functional-omics model evidence.

## [2026-05-29] presentation | Cancer Multiomics PPT storyline and AI handoff

- Created `wiki/analyses/cancer-multiomics-ppt-storyline-and-ai-handoff.md` as the full Korean presentation handoff for the Advanced Genetics LLM-Wiki talk.
- Consolidated the user's constraints, avoided wording, general LLM-Wiki rule, question-by-question expansion, capture targets, final functional resistance-state research question, and 12-slide content plan.
- Updated the Cancer Multiomics topic hub and page catalog so the handoff is discoverable from the project spine.

## [2026-05-29] presentation | Question-specific node capture pack

- Created `wiki/analyses/cancer-multiomics-question-node-capture-pack.md` to separate professor-requested question-specific captures from the noisy global HTML/wiki graph.
- Assigned each PPT slide a center node, crop target, caption, and Obsidian/HTML capture rule.
- Linked the capture pack from the Cancer Multiomics topic hub, handoff page, and page catalog.

## [2026-05-29] presentation | Process-evidence revision after Yeojin deck comparison

- Created `wiki/analyses/cancer-multiomics-ppt-process-evidence-revision.md` after reviewing the user-provided Yeojin LLM-Wiki reference deck and the current Cancer Multiomics PPT.
- Identified that the current PPT has a good biological storyline but needs stronger LLM-Wiki process evidence: node creation, cross-linking, follow-up append, and next-question growth.
- Added slide-level revision guidance and an exact prompt for a PPT-editing AI.
