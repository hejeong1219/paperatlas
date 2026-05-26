---
title: "Advances in mass spectrometry instrumentation and methodology for analysis of alternative protein isoforms"
authors:
  - "Micah D. Lehe"
  - "Raghad Almofeez"
  - "Erin D. Jeffery"
  - "Gloria M. Sheynkman"
year: 2026
journal: "Journal of Mass Spectrometry"
doi: "10.1002/jms.70024"
url: "https://analyticalsciencejournals.onlinelibrary.wiley.com/doi/full/10.1002/jms.70024"
pdf: "raw/inbox/papers/lehe-2026-mass-spectrometry-alternative-protein-isoforms-review.pdf"
paper_kind: review
cancer_types:
  - pan-cancer
modalities:
  - mass-spectrometry
  - long-read-rna-seq
  - ribosome-profiling
themes:
  - proteogenomics
  - alternative-splicing
  - isoform-resolution
  - proteoform-biology
  - dia-acquisition
  - dda-acquisition
  - targeted-proteomics
  - top-down-proteomics
  - sample-preparation
  - bioinformatics-tooling
topic: cancer-multiomics-literature
discovery_method: user-shared
tags:
  - source
  - cancer-multiomics
  - proteogenomics
  - alternative-splicing
  - review
  - mass-spectrometry
  - sheynkman-lab
  - jms-2026
---

# Advances in mass spectrometry instrumentation and methodology for analysis of alternative protein isoforms

_Journal of Mass Spectrometry, 2026 (Sheynkman lab — UVa)._ DOI: [10.1002/jms.70024](https://doi.org/10.1002/jms.70024) · OA via PMC: [PMC12912779](https://pmc.ncbi.nlm.nih.gov/articles/PMC12912779/) · PMID 41696826

## Summary

Lehe, Almofeez, Jeffery & Sheynkman (UVa) survey the modern MS toolkit for detecting and characterizing **splice-derived protein isoforms** — the "alternative proteome" that is essentially invisible to conventional bottom-up DDA workflows. The review argues that proteogenomic isoform analysis has reached an inflection point: long-read RNA-seq supplies sample-matched isoform databases, new mass analyzers (Astral, Orbitrap-based I²MS, TIMS-PASEF) and acquisition strategies (DIA, IS-PRM, PfRM, top-down PRM) substantially lift coverage of low-abundance/non-proteotypic peptides, and bioinformatics tooling for library-free DIA / de novo splice-peptide search / open-search PTM localization has matured. The authors structure the discussion as a **method-by-method matrix** (Table 1) with documented isoform-coverage benchmarks: standard DDA detects 0–10 AS peptides per study, deep DDA pushes to ~216, ultra-deep DDA with multi-protease + fractionation reaches 4,608 AS events (Sinitcyn 2023), SWATH-DIA reaches 2,964 isoform-specific peptides (Liu 2017), Astral DIA covers 935 AS events in one day (Guzman 2025), IS-PRM resolves 77 long-read-predicted isoform peptides (Korchak 2024), and top-down with FAIMS detects 267 AS proteoforms (Fulcher 2021). They argue for **bottom-up + top-down integration**: bottom-up localizes PTMs site-specifically while top-down resolves full-length isoform identity unambiguously. The closing position is that proteomic isoform analysis is now technically tractable, that the bottleneck has shifted from instrumentation to standardized workflow integration and clinical translation, and that the field should treat splice-driven proteoform diversity as on par with PTM diversity when defining the proteome.

## Key Points

- **The motivation problem**: ≥90% of protein-coding genes undergo AS, yet a transcribed RNA isoform does not guarantee a stable, localized, functional protein. Antibody methods can't scale; only MS can realistically interrogate the predicted ~300,000-proteoform human proteome. ~76% of 883 small-molecule cancer drugs miss a target isoform or co-target normal-tissue isoforms (Ji et al), framing isoform-MS as a translational, not academic, priority.
- **Transcriptomic prediction layer**: short-read RNA-seq + custom database boosts alternative isoform coverage ~28% over Swiss-Prot alone (Agosto 2019); Ribo-seq-derived predictions yielded 6,766 isoforms from public MS data (Wu et al); long-read RNA-seq is now the recommended upstream — the Sheynkman lab's own LRP pipeline matched ≥5,100 isoforms out of 45,068 long-read predictions in Jurkat, including 14 novel.
- **Standard DDA ceiling**: typical tryptic DDA covers ≤25% of full-proteome sequence; only ~20% of tryptic peptides map uniquely to one isoform. Result: 0–10 AS peptides detected in unfractionated DDA — a structural limit, not a tuning issue.
- **Deep DDA milestones**: Pandi 2024 (cardiac, deep DDA) → 216 stable AS isoforms incl. 29 tissue-specific upregulations; CPTAC breast (Mertins) → 672 splice-generated peptides with 422 novel from RNA-seq; CPTAC colon (Woo re-analysis) → 108 splice-junction peptides, 97 novel. **Sinitcyn 2023 ultra-deep** (six proteases × six cell lines, 2,491 runs) → 4,608 / 17,399 ENCODE splice events at protein level (~26%), the current depth ceiling for DDA.
- **DIA breakthrough**: Liu 2017 SWATH-DIA hit 2,964 isoform-specific peptides (~20% of detected gene-specific peptides) and reported global protein-level loss correlated with intron retention. Richards 2022 multi-protease DIA (trypsin + AspN + GluC) → +60% peptide detections vs trypsin alone. Fierro-Monti DIA distinguished 10 novel variant peptides across 104,296 total — single-amino-acid sensitivity.
- **DIA + new instruments**: Astral (Guzman 2025 preprint) detects 935 AS events in HEK293 in one day from >200,000 peptides — vs ~20,000-peptide ceiling in equivalent DDA. diaPASEF, Scanning SWATH, high-frequency analyzers, overlapping windows, RT-based window sizing all reduce co-isolation, improving spectral deconvolution for isoform peptides.
- **DIA tooling**: bypassing DDA-library limitation requires library-free / predicted-spectrum methods. Tools called out: MaxDIA, FragPipe / MSFragger-DIA, SeFilter-DIA, DIA-NN, DeepDIA, DIAVariant (Qiao 2025 preprint — 428 variant peptides validated, including peptides below DDA's MS1 LOD), CNovo/SpliceNovo for de novo splice-junction peptides.
- **PRM / IS-PRM**: PRM scales to ~few-dozen targets (Han 2021: 22 / 29 cardiac AS peptides). IS-PRM (Gallien 2015) with TMT-multiplexed synthetic triggers (Tomahto, GoDig) scales to several hundred. **Korchak 2024 (Sheynkman lab)** targeted 192 long-read-predicted isoform peptides in WTC11 iPSC → 77 hits with IS-PRM vs 21 with DDA, confirming 54 isoforms vs 16 — a clean apples-to-apples win for targeted over discovery for known-isoform validation. Synthetic-peptide-free PRM (Wichmann 2019, Remes 2024, Shuken & Gygi 2025, PRM Conductor on Stellar MS) is on the rise to remove the synthetic-peptide cost barrier.
- **Sample-prep auxiliaries** (Figure 2): multi-protease and middle-down digestion expand junction coverage; N- and C-terminomic enrichment (chemical labeling of termini before digestion) directly assigns alternative-terminus isoforms; NovelNSeq de novo N-terminal search identified 157 putative novel N-spliced isoforms; 2D gel + thermal protein profiling (TPP) infer isoform expression even without isoform-unique peptides (Donovan: BMP1 isoform upregulation in NSCLC serum; Kedan preprint via deep gel-MS — claims a majority of RNA isoforms produce detectable proteins).
- **Top-down (TDMS) — the only method that resolves full-length isoforms unambiguously**: still complexity-limited, so most successful applications add enrichment. **IP + TDMS**: Lin 2018 (troponin T, 7 isoforms + phospho-proteoforms), Xu 2025 (tau, 4 isoforms + PTMs). **Gel + TDMS**: GELFrEE (Tran 2011), Chen & Liu 2021 (DLD-1 CRC, 128 exon-skipping proteoforms). **PEPPI-MS** (passive elution from polyacrylamide) is the modern, MS-friendly replacement.
- **NCI RAS Initiative as cancer-relevant TDMS exemplar**: Adams et al characterized **39 proteoforms of KRAS4A + KRAS4B** across colorectal cell lines + primary tumors, including truncated/modified forms invisible to peptide-MS. Downstream: TDMS assays for KRAS4B–small molecule binding + isoform-selective inhibitors. Direct read for the project: TDMS is the validated route to isoform-resolved KRAS proteoform analysis.
- **Top-down instrumentation**: TIMS-PASEF gives ≥10× analytical peak capacity (Meier); FAIMS-enabled TDMS resolved 267 SwissProt splice variants vs 69 without (Fulcher 2021, tau); I²MS (individual-ion MS, Orbitrap) recovered four tau splice isoforms + proteolytic truncations (Xu 2025) — but I²MS is currently expert-only due to instrument tuning + deconvolution. PfRM (proteoform PRM) adapts PRM targeting to intact proteins (Huang 2024); Rusbjerg 2024 used PfRM-style top-down to resolve all 10 periostin isoforms at 64% sequence coverage.
- **Bottom-up + top-down integration**: TDMS confirms which full-length isoform exists; bottom-up confirms which residues carry which PTM. Open-search tools (ProsightPC, TopPIC, TopMG, MS-PathFinder, SPECTRUM, pTop) infer PTM-mass shifts from intact spectra without explicit PTM database, complementing site-specific bottom-up.
- **Computational tool atlas (Table 2)**: structured by analysis stage — genomic/proteomic integration (TopPG, LRP pipeline, MAJIQ), de novo splice junctions (CNovo/SpliceNovo), DIA deconvolution (DIA-Umpire, Ion-Decon, Group-DIA), library-free DIA (MaxDIA, FragPipe, DIA-NN, DeepDIA, DIAVariant), top-down deconvolution (FLASHDeconv, TopFD, MSDeconv, Xtract, Unidec, THRASH), open-search top-down (ProsightPC, TopPIC, TopMG, MS-PathFinder, SPECTRUM, pTop), spectral prediction (Prosit/Koina, MS²PIP), targeted (Tomahto, GoDig, MQL, PRM Conductor), retrospective re-mining (PepCentric, Yu 2025).
- **Authors' three-factor roadmap**: (1) iterative MS instrument/analysis improvement → higher throughput, (2) lower technical barrier-to-entry → wider community adoption of isoform-aware proteomics, (3) translation → biotech/pharma exploitation of isoform-specific biomarkers and drug targets, building on existing splice-targeting therapeutics.

## Methods (scope)

This is a methodology review, not a primary research paper. Scope:

- **Acquisition methods covered**: Standard DDA / Deep DDA (fractionation) / Ultra-deep DDA (multi-protease + fractionation); DIA (SWATH and modern derivatives — diaPASEF, Scanning SWATH, Astral); Targeted (SRM, PRM, IS-PRM with synthetic triggers, IS-PRM with multiplexed TMT triggers, synthetic-free real-time-RT-PRM); Top-down (DDA with complex mixture, IP-enriched, gel-isolated, PRM-targeted = PfRM).
- **Instrument capabilities**: TIMS-PASEF, FAIMS, Orbitrap I²MS (individual-ion charge-detection), Astral mass analyzer, Stellar MS with PRM Conductor.
- **Upstream sample prep**: multiple proteases (trypsin + AspN + GluC, six-protease deep), middle-down (chemical / non-tryptic digestion to 20–100 aa polypeptides), terminal enrichment (N- and C-terminomics with chemical labeling).
- **Inference methods**: peptide correlation profiling (Donovan 2019 for BMP1 in NSCLC), 2D gel electrophoresis (Kedan preprint), thermal protein profiling (TPP — TMPO isoforms).
- **Database & search**: long-read RNA-seq custom databases (LRP pipeline, Salz), Ribo-seq derived databases (Wu), de novo sequencing (NovelNSeq, CNovo/SpliceNovo), open search for top-down PTM mass shifts.
- **Integration**: bottom-up ↔ top-down PTM-localization handshake (multiple recent tools 149-153 references in paper).

## Cancer Multiomics Project Relevance

논문이 직접 다룬 cancer 관련 응용·인용만 정리. 본 위키의 한미암 프로젝트 적용 여부는 별도로 평가 필요.

- **논문이 인용한 cancer 사례 (Section 3.1, Deep DDA)**: CPTAC breast cancer (Mertins) deep coverage DDA로 672 splice-generated peptide + 422 novel RNA-seq 예측 peptide 검출. CPTAC colon cancer (Woo re-analysis, n=90) deep DDA로 108 splice junction peptide + 97 novel splice junction 검출.
- **논문이 인용한 cancer 사례 (Section 7, Inference)**: Donovan et al — non-small cell lung cancer (NSCLC) 환자 혈청에서 BMP1 alternative isoform upregulation을 peptide correlation profiling으로 추론 (isoform-specific peptide 직접 검출 없이).
- **논문이 인용한 cancer 사례 (Section 8.1, IP+TDMS)**: Chen & Liu 2021 — DLD-1 colorectal cancer cell line top-down MS + GELFrEE → 128 exon-skipping splice 유래 proteoform 검출. NCI RAS Initiative (2013–) — RAS-driven cancer 임상 미충족 수요 대응 목적의 KRAS isoform proteoform 분석 프로그램. Adams et al — colorectal-cancer cell line + primary tumor에서 KRAS4A + KRAS4B 39 proteoform 특성화 (truncation + modification 포함, peptide-centric workflow로는 검출 불가). 후속: KRAS4B–small molecule 상호작용 정량 TDMS assay (출처 127), KRAS4B 활성 억제 small molecule (출처 128).
- **논문이 인용한 cancer 사례 (Section 8.2, FAIMS-TDMS)**: Fulcher 2021 — tau splice isoform 검출 (cancer 아닌 neurodegeneration, 환자 brain tissue). Xu 2025 (tau, brain tissue, I²MS) — cancer 아님.
- **논문의 translational framing**: Section 1에서 인용한 Ji et al 통계 — "76 percent of 883 small molecule cancer drugs miss a target isoform or target different isoforms that are present in normal tissues". 논문은 이를 isoform-resolved proteomics가 cancer drug target 평가에 필요한 근거로 제시.
- **논문이 명시한 한계 (Section 5, 8.2, 9)**: IS-PRM은 synthetic heavy peptide 비용·추가 PTM/missed cleavage로 target miss 가능. I²MS는 instrument tuning + 전용 deconvolution 알고리즘 필요로 일반 TDMS 사용자에게는 적용 어려움. Splice + PTM 동시 분석은 top-down에서 modification site localization이 복잡 — bottom-up 보조 필요.

논문은 review/methodology paper로 새 실험 데이터를 제시하지 않으며, lung cancer–specific isoform proteomics 사례는 별도 cancer-section에서 직접 언급되지 않음 (NSCLC 인용은 Donovan BMP1 serum 사례에 한정).

## Connections

- [Awasthi 2026 – PEXMap proteogenomic exon/isoform mapping](./awasthi-2026-pexmap-proteogenomic-exon-isoform-mapping.md) — splice-isoform peptide mapping 도구; 본 리뷰의 splice-junction peptide 검출 workflow와 영역 중첩.
- [Jiang 2026 – 3DisoGalaxy isoform foldome](./jiang-2026-3disogalaxy-breast-cancer-isoform-foldome.md) — long-read RNA-seq + Ribo-seq 기반 isoform atlas (breast cancer); 본 리뷰가 권장하는 long-read DB build 방향과 영역 중첩.
- [Cancer Multiomics Proteogenomic Atlas](../topics/cancer-multiomics-literature.md) — topic hub (Section 1, Proteogenomics 통합 기반).

## Sources

- Raw PDF: `raw/inbox/papers/lehe-2026-mass-spectrometry-alternative-protein-isoforms-review.pdf` (1.1 MB, 30 pages; Europe PMC author-manuscript version, NIHMS-2134509)
- Publisher (paywalled): https://analyticalsciencejournals.onlinelibrary.wiley.com/doi/full/10.1002/jms.70024
- Open access via PMC: https://pmc.ncbi.nlm.nih.gov/articles/PMC12912779/
- Europe PMC render endpoint: https://europepmc.org/articles/PMC12912779?pdf=render
- PMID: 41696826
- Key sub-references (selected): Sheynkman lab LRP pipeline (Miller 2022), Korchak 2024 IS-PRM WTC11 (long-read-predicted isoforms), Guzman 2025 Astral DIA preprint, Sinitcyn 2023 ultra-deep DDA, Liu 2017 SWATH-DIA, Richards 2022 multi-protease DIA, Fulcher 2021 FAIMS-TDMS tau, NCI RAS Initiative Adams et al (KRAS proteoforms), Chen & Liu 2021 TopPG DLD-1 colorectal cancer, Pandi 2024 cardiac deep DDA, Mertins (CPTAC breast), Woo (CPTAC colon)
