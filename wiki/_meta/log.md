# Log

Append-only operational history for this wiki.

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
