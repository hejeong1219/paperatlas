---
title: "Deciphering the dark cancer phosphoproteome using machine-learned co-regulation of phosphosites."
authors:
  - "Jiang"
  - "Jaehnig"
  - "Liao"
  - "Shi"
  - "Yaron-Barir"
  - "Johnson"
  - "Cantley"
  - "Zhang"
year: "2025"
journal: "Nature Communications"
doi: "10.1038/s41467-025-57993-2"
pmid: "40113755"
pmcid: "PMC11926083"
paper_kind: proteogenomic
pdf: "raw/inbox/papers/jiang-2025-deciphering-dark-cancer-phosphoproteome-using.pdf"
topic: ptmanchor
tags:
  - "ptmanchor"
  - "phosphoproteomics"
  - "kinase-substrate-association"
  - "machine-learning"
  - "cancer-proteomics"
  - "cptac"
  - "pmid-40113755"
themes:
  - "ptm-correction"
  - "kinase-signaling"
  - "cancer-proteomics"
batch_ingest_status: pdf-text-extracted
batch_ingested_on: 2026-05-13
---
# Deciphering the dark cancer phosphoproteome using machine-learned co-regulation of phosphosites

_Nature Communications 16:2766, 2025._ PMID: [40113755](https://pubmed.ncbi.nlm.nih.gov/40113755/) · DOI: [10.1038/s41467-025-57993-2](https://doi.org/10.1038/s41467-025-57993-2) · PMC: [PMC11926083](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11926083/)

## Summary

Jiang et al. tackle the dark phosphoproteome — the >95% of detected phosphosites with no annotated upstream kinase or function — by mining co-regulation patterns in the CPTAC pan-cancer phosphoproteome (1,195 tumors across 11 cancer types). They first build CoPheeMap, an XGBoost-derived network of 26,280 phosphosites and 764,049 co-regulation edges that integrates sequence similarity, kinase-interaction-profile similarity, and PanCan Pearson correlations. They then plug CoPheeMap embeddings (via Node2Vec) plus a kinase-kinase network (KMap, 352 kinases / 3,238 edges built from STRING + cross-cohort co-expression) into a second XGBoost model, CoPheeKSA, which predicts 24,015 kinase–substrate associations (KSAs) between 9,399 phosphosites and 104 S/T kinases — a 5× expansion over their ground-truth KSA set. CoPheeKSA covers 26 understudied kinases, outperforms NetworKIN/LinkPhinder/PDT on Kinase-Library percentile validation, and is independently corroborated by STRING functional scores and IDPpub PubMed-mining (56 confirmed, 4 refuted). The team illustrates utility on three dark functional phosphosites (CD74-S8 → AKT3/SGK3, PRKCA-T497 → PDK1, HSP90AB1-S226 → CSNK2A1) and on differentially regulated tumor-vs-normal sites where most lacked any prior kinase annotation. The work positions CoPheeMap/CoPheeKSA as a pan-cancer prior for kinase-activity inference and as a hypothesis generator for under-explored kinases as therapeutic targets.

## Batch PDF Ingest Status

- Status: `pdf-text-extracted` on 2026-05-13.
- Local PDF: `raw/inbox/papers/jiang-2025-deciphering-dark-cancer-phosphoproteome-using.pdf`.
- Extracted text length: 71,835 characters.
- Scope note: automated local-PDF text ingest for the 100-paper drug-response/phospho-global batch; not yet a manual full-text deep-dive.
- Evidence boundary: downstream scientific claims should use this page only after source-specific Key Points are manually promoted or rechecked against the local PDF.
- High-signal PDF snippets:
  - Article https://doi.org/10.1038/s41467-025-57993-2 Deciphering the dark cancer phosphoproteome using machine-learned co-regulation of phosphosites Received: 7 July 2024 Wen Jiang1,2, Eric J.
  - Cantley 6,7 & Accepted: 10 March 2025 Bing Zhang 1,2 Published online: 20 March 2025 Check for updates Mass spectrometry-based phosphoproteomics offers a comprehensive view of 1234567890():,; 1234567890():,; protein phosphorylation, yet our limited knowledge about the regulation and function of most phosphosites hampers the e...
  - To address this challenge, we integrate machine learning with phosphoproteomic data from 1195 tumor specimens spanning 11 cancer types to construct CoPheeMap, a network that maps the co-regulation of 26,280 phosphosites.
  - By incorporating network features from CoPheeMap into a second machine learning model, namely CoPheeKSA, we achieve superior performance in predicting kinase-substrate associations.
  - CoPheeKSA uncovers 24,015 associations between 9399 phosphosites and 104 serine/ threonine kinases, shedding light on many unannotated phosphosites and understudied kinases.

## Key Points

- Pan-cancer phosphoproteome scope: 158,796 phosphosites total, 77,442 quantified in ≥20% of samples in at least one cohort across 11 CPTAC cancers (BRCA, CCRCC, COAD, GBM, HCC, HNSCC, LSCC, LUAD, OV, PDAC, UCEC) with paired global proteomics (14,103 proteins) and RNA-seq (21,592 genes); <5% of these sites carry an annotated upstream kinase.
- CoPheeMap construction: an XGBoost classifier trained on three feature types (15-mer sequence similarity, kinase-interaction-profile similarity, and phosphosite Pearson correlation across PanCan) — combining all three significantly beats any subset; thresholding at False Positive Rate = 0.2% yields 764,049 co-regulation edges connecting 26,280 phosphosites, far broader than the 4,873 ground-truth-KSA-covered sites.
- Network embeddings: Node2Vec produces 16-d phosphosite vectors (CoPheeMap) and 16-d kinase vectors (KMap, 352 kinases, 3,238 edges defined by STRING ≥400 OR per-cohort protein-protein correlation >0.5).
- CoPheeKSA features (55-d): 16 CoPheeMap site embedding + 16 KMap kinase embedding + 22 dynamic kinase-substrate correlations (protein × site, activity × site, requires ≥20 overlapping samples) + 1 static PSSM motif score; XGBoost (max_depth 2, eta 0.2, 300 rounds), threshold 0.76 (LLR 5.5 → 244× more likely positive than negative).
- Validation against the experimental Kinase Library (KL, Johnson et al. 2023): CoPheeKSA's positive predictions had significantly higher KL percentile scores than ground-truth positives for well-studied kinases (p ≤ 0.0001); for understudied kinases (CAMK2G, CDK7, DYRK1B, PAK4), CoPheeKSA predictions also outperformed even the ground-truth positives in KL alignment — i.e., it "rescues" KL signal that curated databases miss.
- Beats prior tools on the same PanCan sites: NetworKIN, LinkPhinder, and PDT all gave significantly lower KL percentile scores than CoPheeKSA; LinkPhinder/PDT predictions approached random-pair quality despite outputting more associations. CoPheeKSA also covered more understudied kinases than competing methods.
- Orthogonal STRING-functional-association validation: for 1,621 sites with disagreeing CoPheeKSA-top vs KL-top kinases, the CoPheeKSA top kinase had a higher STRING score (vs 577 for KL); cumulative STRING distributions strongly favor CoPheeKSA-supported KSAs (Kolmogorov-Smirnov p = 2.2e-16).
- PubMed text-mining (IDPpub) confirmed 56 CoPheeKSA-predicted KSAs that were absent from the ground-truth set (with only 4 refuted), including new substrates for understudied kinases AKT3 and MAP4K1/HPK1.
- Dark-functional-site case studies: CD74 Ser8 (cell-surface immune-stimulation receptor, recurrently overexpressed in tumors) → AKT3 + SGK3 predicted (both rank >99% KL percentile); PRKCA Thr497 → PDK1 (consistent with prior in-vitro evidence missing from the public database); HSP90AB1 Ser226 → CSNK2A1; for sites where CoPheeKSA had no confident KSA (e.g., VIM Ser25), CoPheeMap neighbors connected the site to substrates of PRKACA/PRKCA/PRKD1 — providing AGC-family kinase hypotheses through guilt-by-association.
- Tumor-vs-NAT differential phosphoproteomics across 8 cohorts: among the top 50 most-differential phosphosites, only 12 had annotated kinases, but CoPheeKSA+CoPheeMap provided regulatory hypotheses for all 50, illustrating how the network can be plugged into routine cohort analysis as a kinase-activity prior.
- Causality and coverage limits: the model is restricted to S/T kinases (Y-Y handled separately), depends on availability of dynamic features (so cohorts with smaller overlapping sample sizes get penalized), and only assesses "consistent direction" co-regulation — true regulatory direction (kinase A → site vs site → kinase A feedback) is not resolved.
- Code + data: model code at [github.com/bzhanglab/CoPheeMap](https://github.com/bzhanglab/CoPheeMap); harmonized PanCan proteomics/phospho/RNA matrices from the CPTAC PDC pan-cancer portal; HCC processed matrices archived at [Zenodo 14553766](https://zenodo.org/records/14553766).

## Methods

XGBoost-based machine-learning models built on the CPTAC pan-cancer harmonized v1 phosphoproteome (BRCA, CCRCC, COAD, GBM, HCC, HNSCC, LSCC, LUAD, OV, PDAC, UCEC) with paired global proteome and RNA-seq. Ground-truth KSAs are curated from a 14,679-KSA reference (362 kinases, 9,526 sites); kinases with ≥10 substrates are "well-studied," others "understudied." CoPheeMap features: 15-mer sequence similarity, kinase-interaction-profile similarity, and pan-cohort Pearson correlation; AUROC on held-out site-pair classification = 0.95 (median over 10 Monte Carlo iterations). KMap edges defined by STRING ≥400 OR ≥0.5 protein-protein correlation in ≥1 CPTAC cohort. Kinase-activity scores per sample = mean log-ratio of known substrates ground-truthed to that kinase (requires ≥3 quantified substrates; site itself excluded to prevent leakage); dynamic correlations computed between kinase protein abundance / activity scores and per-site phosphorylation, retaining only correlations where ≥20 samples have both measurements. KL percentile scores per Johnson et al. 2023 (303 S/T kinases scored against an a-priori curated phosphoproteome). External validation via STRING v12 functional association scores and IDPpub text-mining of PubMed abstracts. Differential tumor-vs-NAT analysis used meta-p-values (R metap sumz) across the 8 cohorts with paired normals.

## Cancer Multiomics Project Relevance

- CoPheeMap/CoPheeKSA는 한미암/Cancer Multiomics 과제의 인산화단백체 분석 단계에서 functional annotation이 없는 dark phosphosite의 기능 가설을 세우거나 understudied kinase의 활성을 추정할 때 외부 reference network으로 결합해볼 만한 자료다 — 특히 우리 코호트에서 풀리지 않는 "차이는 큰데 위키 정보가 없는" 사이트들을 CoPheeMap neighbor 기반 guilt-by-association으로 해석해볼 수 있다.
- 11개 암종 1195 종양 규모로 학습된 pan-cancer kinase-substrate prior는 우리 코호트에서 KSEA/CoPheeKSA 기반 kinase activity inference를 돌릴 때 "well-studied kinase에 치우치지 않는" 보강 reference로 검토 가치가 있고, 26개 understudied kinase(예: CDK12, SGK3, SMG1, NUAK1)에 대해서는 우리 데이터로도 활성 변화가 잡히는지 cross-cohort validation 대상이 된다.
- Cancer Multiomics에서 PTM-correction (ptmanchor) 후 kinase-substrate 신호가 어떻게 재편되는지를 본 연구의 KSA prior와 함께 분석하면, Q3 ("PTM 보정이 kinase activity inference에 미치는 영향")과 Q12 ("CoPheeKSA가 ptmanchor가 고치는 단백질-abundance 컨파운드에 얼마나 영향받는가")에 대한 직접적인 답변 데이터를 만들 수 있다.

## Connections

- [Ptmanchor Topic Hub](../topics/ptm-correction-and-kinase-signaling-in-cancer-proteomics.md)
- [Ptmanchor Manuscript Anchor](../analyses/ptmanchor-manuscript-anchor.md)
- [PTM Correction Confounding Foundations](../concepts/ptm-correction-confounding-foundations.md)
- [PTM Correction & Kinase Signaling Question Bank](../analyses/ptm-correction-kinase-signaling-question-bank.md)

## Sources

- Local PDF: `raw/inbox/papers/jiang-2025-deciphering-dark-cancer-phosphoproteome-using.pdf`
- PubMed: <https://pubmed.ncbi.nlm.nih.gov/40113755/>
- DOI: <https://doi.org/10.1038/s41467-025-57993-2>
- PMC: <https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11926083/>
- Code: <https://github.com/bzhanglab/CoPheeMap>
- HCC data: <https://zenodo.org/records/14553766>
- CPTAC pan-cancer data portal: <https://pdc.cancer.gov/pdc/cptac-pancancer>

## 함께 인용된 논문

위키 분석·합성 페이지에서 이 논문과 함께 인용된 논문들 (co-citation).

- [[jiang-2025-dark-cancer-phosphoproteome-coregulation|Jiang 2025]]
- [[mertins-2016-proteogenomics-somatic-mutations-signalling-breast-cancer|Mertins 2016]]
- [[muller-dott-2025-phosphoproteomic-kinase-activity-inference|Muller]]
- [[savage-2020-phosphoproteomics-bioinformatics-comprehensive-guide|Savage 2020]]
- [[wu-2011-correct-interpretation-comprehensive-phosphorylation-dynamics|Wu 2011]]
