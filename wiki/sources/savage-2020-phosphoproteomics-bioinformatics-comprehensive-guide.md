---
title: "Using phosphoproteomics data to understand cellular signaling: a comprehensive guide to bioinformatics resources"
authors:
  - "Savage"
  - "Zhang"
year: 2020
journal: "Clinical Proteomics"
doi: "10.1186/s12014-020-09290-x"
pmid: "32636719"
pmcid: "PMC7333321"
paper_kind: review
pdf: "raw/inbox/papers/savage-2020-phosphoproteomics-bioinformatics-comprehensive-guide.pdf"
topic: ptmanchor
tags:
  - "ptmanchor"
  - "phosphoproteomics"
  - "kinase-activity-inference"
  - "bioinformatics-review"
  - "kinase-substrate-association"
  - "review"
themes:
  - "ptm-correction"
  - "kinase-signaling"
  - "cancer-proteomics"
related_papers:
  - "jiang-2025-dark-cancer-phosphoproteome-coregulation"
  - "muller-dott-2025-phosphoproteomic-kinase-activity-inference"
discovery_method: openalex-related-q3
batch_ingest_status: pdf-text-extracted
batch_ingested_on: 2026-05-13
---
# Using phosphoproteomics data to understand cellular signaling: a comprehensive guide to bioinformatics resources

_Clinical Proteomics 17:27, 2020 (corrected publication 2024)._ PMID: [32636719](https://pubmed.ncbi.nlm.nih.gov/32636719/) · DOI: [10.1186/s12014-020-09290-x](https://doi.org/10.1186/s12014-020-09290-x) · PMC: [PMC7333321](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7333321/)

## Summary

Savage & Zhang (Bing Zhang's lab — the same group that later released CoPheeMap/CoPheeKSA in Jiang 2025) catalog **16 kinase/phosphatase knowledge bases and 27 phosphorylation-site databases**, and benchmark **4 kinase activity inference tools (KEA2, KSEA App, PHOXTRACK, IKAP)** on a 20-kinase-inhibitor cell-line dataset. They recommend PhosphoSitePlus as the preferred experimentally-curated site resource and KinBase as the primary kinase reference (538 human protein kinases), but flag **systematic ID-mapping errors** (PEG/MELK confusion, PDPK1/PDK1 ambiguity, PTPN11 incorrectly classified as kinase) that propagate from upstream databases into downstream tools. On the activity-inference side: **KSEA App made the most true-positive kinase predictions, PHOXTRACK made the fewest false positives, and IKAP underperformed across the board**. The review's standing observation that **over half of kinase substrate sets contain fewer than 10 substrates** is the empirical basis for the "understudied kinase" threshold later used in Jiang 2025 (CoPheeKSA covers 26 such kinases). The paper is positioned as a practitioner's guide for biologists/clinicians who are not professional bioinformaticians, with explicit usability scoring for each tool.

## Batch PDF Ingest Status

- Status: `pdf-text-extracted` on 2026-05-13.
- Local PDF: `raw/inbox/papers/savage-2020-phosphoproteomics-bioinformatics-comprehensive-guide.pdf`.
- Extracted text length: 29,941 characters.
- Scope note: automated local-PDF text ingest for the 100-paper drug-response/phospho-global batch; not yet a manual full-text deep-dive.
- Evidence boundary: downstream scientific claims should use this page only after source-specific Key Points are manually promoted or rechecked against the local PDF.
- High-signal PDF snippets:
  - Savage and Zhang ﻿Clinical Proteomics (2020) 17:27 Clinical Proteomics https://doi.org/10.1186/s12014-020-09290-x REVIEW Open Access Using phosphoproteomics data to understand cellular signaling: a comprehensive guide to bioinformatics resources Sara R.
  - Savage1,2 and Bing Zhang2,3* Abstract Mass spectrometry-based phosphoproteomics is becoming an essential methodology for the study of global cellular signaling.
  - Numerous bioinformatics resources are available to facilitate the translation of phosphopeptide identifica- tion and quantification results into novel biological and clinical insights, a critical step in phosphoproteomics data analysis.
  - These resources include knowledge bases of kinases and phosphatases, phosphorylation sites, kinase inhibi- tors, and sequence variants affecting kinase function, and bioinformatics tools that can predict phosphorylation sites in addition to the kinase that phosphorylates them, infer kinase activity, and predict the effect of ...
  - Therefore, we put together a comprehensive collection of resources related to phosphoproteomics data interpretation, compared the use of tools with similar functions, and assessed the usability from the standpoint of typical biologists or clinicians.

## Key Points

- **Kinase/phosphatase knowledge base inventory (16 resources)**: KinBase (538 kinases, Manning's primary classification), Kinomer, MOKCa, KIDFamMap, EKPD, KinaseNET, Kin-Driver, KLIFS, KinG, ProKinO, iEKPD (most comprehensive but only online), KinWeb (outdated since 2005), KinMutBase (outdated, 31 kinases only), Phosphatome.Net, HuPho, DEPOD. Only EKPD/iEKPD cover both kinases and phosphatases.
- **Phosphorylation-site database inventory (27 resources)**: 4 main literature-curated databases — HPRD (last update 2010, 78,005 sites), Swiss-Prot (Jun-19, 40,135 sites), Phospho.ELM (2010, 26,651 sites), and **PhosphoSitePlus (Aug-19, 239,664 sites, 372 kinases — preferred resource)**. Among the 27, PhosphoSitePlus is the most-frequently-updated, distinguishes high-throughput vs low-throughput sites, and is well-curated.
- **"Understudied kinase" empirical threshold**: among the 485 substrate sets aggregated from the 4 main databases, **CSNK2A1 has the most substrates (596) while >50% of kinase substrate sets contain fewer than 10 substrates** — directly motivates Jiang 2025's <10-substrate "understudied kinase" definition.
- **ID-mapping errors flagged**: (a) PEG (paternally expressed gene 3) erroneously entered as a kinase phosphorylating CDC25B when the true kinase is pEg3/MELK; (b) PDPK1 (3-phosphoinositide-dependent protein kinase 1 = "PDK1" in biology) systematically confused with pyruvate dehydrogenase kinase PDK1; (c) PTPN11 — a known phosphatase — entered in HPRD as kinase of PTK2B and propagated downstream into RegPhos and PhosphoAtlas. These errors propagate into every integrative database and every kinase activity inference tool.
- **Phosphosite kinase prediction tool benchmark (8 tools)**: NetPhorest, NetworKIN, iGPS, GPS, GPS5.0, PhosScan, musite, MusiteDeep, DeepPhos, phos_pred, pkaPS. ROC-AUC tested on CDK1, CK2, MAPK1, PKA. **MusiteDeep + GPS had highest AUC across all 4 kinases**; PKA-specific tool pkaPS also performed well; performance was strongly kinase-dependent for the other tools.
- **Kinase activity inference tool benchmark (4 tested)**: KEA2 (Fisher's exact test, 250 kinase sets), KSEA App (Z score, accepts PhosphoSitePlus + NetworKIN substrates), PHOXTRACK (GSEA on 13-mer peptides, 1000 permutations), IKAP (MATLAB-based cost function). Benchmark dataset = 20-kinase-inhibitor cell-line phosphoproteomes; positive set = annotated drug targets, negative = all other significant calls. **KSEA App made the most true-positive predictions across 20 inhibitors; PHOXTRACK had the fewest false positives; IKAP made the fewest TP** (and required hard-coded MATLAB edits).
- **Tool excluded from benchmark**: PHOSIDA Motif Finder (online-only, no downloadable results); INKA (requires MaxQuant search files only).
- **Kinase activity input format friction**: KEA2 takes `HGNC_symbol_position`; KSEA App takes a strict CSV with HGNC + position + non-log-transformed fold change; PHOXTRACK takes a 13-mer + log-FC two-column file; IKAP takes MATLAB tabular data. The lack of a common format prevents head-to-head pipeline comparison without custom adapters.
- **Pathway-level / downstream tools listed**: PTMsigDB (limited PTM-aware pathway sets), String, RegPhos2, WikiPathways, GSEA. Explicit acknowledgment that gene-level pathway tools lose information when applied to PTM data because individual phosphosites' functional contributions are not annotated.
- **Time-course + clustering tools**: CellNOpt (logic formalisms), Sorad (ODEs), DynaPho (activity modules), CLUE (k-means clustering on time courses), KinasePA (perturbation testing), SELPHI (multi-function exploratory analysis).
- **Usability scoring criteria**: free availability, current accessibility, OS support (Linux vs Windows vs Mac), documentation quality, input/output format flexibility, last update year. Many "available" tools were eliminated as obsolete, broken, or platform-restricted (e.g., PhoScan = Linux only, KinMutBase = broken links).
- **Authorship note**: Sara R. Savage + Bing Zhang at Baylor. This is the *prequel* paper to Jiang 2025 (CoPheeMap/CoPheeKSA) — Savage 2020 catalogs the field's tools and identifies their gaps (especially the kinase activity inference benchmark limitation), and Jiang 2025 then builds CoPheeKSA explicitly to address those gaps using pan-cancer co-regulation as the new feature layer.

## Methods

Literature + OMICtools search (July 2019, kinase/phosphorylation/phosphatase keywords) → curate ≥1-update-since-2015, freely available, human-relevant, non-obsolete tools only. Phosphosite kinase predictor benchmark: 1,000 positive sites + 5,000 random protein sequences submitted to each tool; ROC/AUROC via R ROCR. Kinase activity inference benchmark: 20-kinase-inhibitor phosphoproteomic dataset (cell-line study); each tool's significantly-downregulated kinases (FDR < 0.05, ≥3 substrates) compared against the drug's annotated targets (positive set) vs all other predictions (negative set). True positive = predicted ∩ annotated drug target; false positive = predicted ∩ not in annotated set.

## Cancer Multiomics Project Relevance

- 한미암 / Cancer Multiomics 과제 phosphoproteomics 분석 파이프라인에서 Savage 2020은 "어떤 kinase activity inference 도구를 쓸 것인가"의 1차 의사결정 매트릭스다 — 특히 KSEA App + PHOXTRACK 조합이 (KSEA의 TP rate × PHOXTRACK의 낮은 FP rate) 보완적이라는 결론은 우리 5-cohort 분석 SOP에 직접 적용 가능하다.
- 16개 kinase 지식베이스와 27개 phospho-site DB 비교는 우리 위키의 ptmanchor 매뉴스크립트가 어떤 외부 DB를 ground truth로 채택해야 하는지에 직접 답한다 — PhosphoSitePlus (실험), NetworKIN (예측), CoPheeKSA (Jiang 2025의 새 prediction layer) 의 3-tier 구조로 정리.
- "understudied kinase" 정의 (<10 substrate sets) 의 empirical 근거가 Savage 2020 절반-이상-소수-기질 통계로부터 나왔다는 점은 Jiang 2025와의 직접적 연결점이며, ptmanchor 매뉴스크립트가 같은 정의를 채택했을 때 26개 (Jiang의 26 understudied kinase) 가 우리 코호트에서도 활성 변화로 잡히는지 cross-validation 대상이 된다.
- PEG/MELK, PDPK1/PDK1, PTPN11 등 ID-mapping 오류는 우리 ptmanchor pipeline에서 KSA prior를 가져올 때 반드시 sanity-check해야 할 사례 리스트로, Q12 ("CoPheeKSA가 ptmanchor가 고치는 confound에 영향받는가") 분석 단계에서 직접 활용된다.

## Connections

- [Synthesis: Kinase Activity Inference Under PTM Correction (Q3)](../syntheses/kinase-activity-inference-under-ptm-correction.md)
- [PTM Correction Confounding Foundations](../concepts/ptm-correction-confounding-foundations.md)
- [ptmanchor Manuscript Anchor](../analyses/ptmanchor-manuscript-anchor.md)
- [PTM Correction Topic Hub](../topics/ptm-correction-and-kinase-signaling-in-cancer-proteomics.md)
- [Source: Jiang 2025 — CoPheeMap / CoPheeKSA](../sources/jiang-2025-dark-cancer-phosphoproteome-coregulation.md)
- [Source: Müller-Dott 2025 — Phosphoproteomic Kinase Activity Inference Benchmark](../sources/muller-dott-2025-phosphoproteomic-kinase-activity-inference.md)
- [Source: Wu 2011 — Correct Interpretation of Phosphorylation Dynamics](../sources/wu-2011-correct-interpretation-comprehensive-phosphorylation-dynamics.md)

## Sources

- Local PDF: `raw/inbox/papers/savage-2020-phosphoproteomics-bioinformatics-comprehensive-guide.pdf`
- PubMed: <https://pubmed.ncbi.nlm.nih.gov/32636719/>
- DOI: <https://doi.org/10.1186/s12014-020-09290-x>
- PMC: <https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7333321/>
- Companion paper (same group): Jiang W et al., *Nat Commun* (2025) — CoPheeMap/CoPheeKSA expands kinase activity inference to dark phosphoproteome.

## 함께 인용된 논문

위키 분석·합성 페이지에서 이 논문과 함께 인용된 논문들 (co-citation).

- [[jiang-2025-dark-cancer-phosphoproteome-coregulation|Jiang 2025]]
- [[mertins-2016-proteogenomics-somatic-mutations-signalling-breast-cancer|Mertins 2016]]
- [[muller-dott-2025-phosphoproteomic-kinase-activity-inference|Muller]]
- [[wu-2011-correct-interpretation-comprehensive-phosphorylation-dynamics|Wu 2011]]
- [[jiang-2025-deciphering-dark-cancer-phosphoproteome-using|Jiang 2025]]
