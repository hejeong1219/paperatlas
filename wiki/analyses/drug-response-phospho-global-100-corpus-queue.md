---
title: Drug Response Phospho-Global Proteomics Corpus Queue (Target=100)
tags:
  - corpus-queue
  - drug-response
  - phosphoproteomics
  - global-proteomics
  - cancer-multiomics
---

# Drug Response Phospho-Global Proteomics Corpus Queue (Target=100)

최근 10년(2016–2026) high-impact 중심으로, human cancer에서 global proteome / phosphoproteome / proteogenomics를 이용해 항암제 반응성, 내성, 치료 취약성, kinase signaling, 또는 정밀의학 stratification을 분석한 논문 100편을 모으기 위한 큐.

## Key Points

- 이 큐는 기존 세 주제(B-cell neoantigen, cancer resistance / immune evasion, ptmanchor)를 대체하지 않는다.
- 역할은 **Cancer Multiomics / drug-response literature monitor**이다: 세 주제에 논문을 공급하고, 특히 global proteome + phospho + somatic SNV 기반 항암제 반응성 POC의 근거 코퍼스를 만든다.
- 웹/PubMed는 후보 발견과 PDF 확보에만 사용한다. 과학적 claim은 PDF/source page deep-dive 이후에만 확정한다.
- Quantitative corpus row에는 human cancer + local PDF/source-note 근거가 있는 primary paper를 우선한다. Review, methods, database, non-human cancer, generic signaling paper는 context로 분리한다.

## Status

- Target: **100**
- Existing high-confidence local papers already usable: **31** (brief/source pages already present; many already PDF-backed)
- New PubMed/PDF resolver batch on 2026-05-13: **40 PDFs downloaded + 40 source stubs generated**
- Provisional pool before triage: **71**
- Full-text deep-dive from the 2026-05-13 batch: **18 completed** (`hsu-2025-phosphoproteomics-osimertinib-tolerant-persister-cells-reveals`, `lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc`, `anurag-2022-proteogenomic-markers-chemotherapy-resistance-response`, `zhang-2023-proteogenomics-clear-cell-renal-response-tyrosine-kinase-inhibitor`, `ji-2023-pharmaco-proteogenomic-characterization-liver-cancer-organoids`, `holt-2025-proteogenomic-characterization-unveils-biomarkers-associated`, `jaehnig-2025-proteogenomic-analysis-calgb-40601-alliance`, `zhao-2025-phosphoproteomic-acetylomic-characterization-colorectal-cancer`, `song-2024-proteogenomic-analysis-reveals-non-small-cell`, `chmielecki-2023-acquired-resistance-first-line-osimertinib`, `gillette-2020-proteogenomic-characterization-reveals-therapeutic-vulnerabilities`, `huang-2021-proteogenomic-insights-biology-treatment-hpv-negative`, `petralia-2024-pan-cancer-proteogenomics-characterization-tumor-immunity`, `vasaikar-2019-proteogenomic-analysis-human-colon-cancer`, `chen-2020-proteogenomics-non-smoking-lung-cancer-east`, `cao-2021-proteogenomic-characterization-pancreatic-ductal-adenocarcinoma`, `satpathy-2021-proteogenomic-portrait-lung-squamous-cell`, `krug-2020-proteogenomic-landscape-breast-cancer-tumorigenesis`); **1 blocked as wrong PDF** (`jeong-2025-proteogenomic-profiling-predicts-outcomes-adjuvant-chemotherapy`).
- Remaining to target after strict triage: **at least 29**, likely more if reviews/non-human/context papers are excluded.
- First discovery window: PubMed E-utilities, last 3650 days, query = proteogenomic/phosphoproteomic/pQTL × drug response/resistance/precision oncology × cancer/humans, retmax 250. Result: 250 PMIDs, 209 fresh by PMID filter, 40 PDFs obtained.

## Topic Architecture

The durable public tracks are:

1. **B-cell Neoantigen** — neoantigen discovery, B/TLS biology, immunopeptidomics, antigen specificity.
2. **Cancer Resistance / Immune Evasion** — immune visibility, access, effector dysfunction, antigen loss, lineage switch, checkpoint/CAR/BsAb resistance.
3. **ptmanchor** — PTM correction, phosphosite interpretation, kinase activity inference.
4. **Cancer Multiomics / Drug-response Monitor** — cross-cutting acquisition layer for WGS/SNV/CNA + global proteome + phosphoproteome + drug response papers. This feeds the other three rather than competing with them.

## Inclusion Rules

Core inclusion:

- human cancer or patient-derived model strongly tied to human cancer
- global proteome and/or phosphoproteome, ideally both
- explicit treatment response, drug resistance, therapy vulnerability, subtype-to-therapy, or targetable signaling question
- recent 10 years preferred
- high-impact/high-signal journals preferred: Nature, Science, Cell family, Cancer Cell, Cancer Discovery, Nature Medicine, Nature Cancer, Nature Communications, JCI, JCO, Annals of Oncology, Journal of Hepatology, Cancer Research, Molecular & Cellular Proteomics, Genome Biology, Science Translational Medicine, Cell Reports Medicine, etc.

Context inclusion:

- review / methods / database / algorithm papers
- non-patient perturbation studies
- broad cancer biology papers without direct matched global/phospho response data
- lower-impact but directly useful phospho drug-response papers

Exclude or low priority:

- non-human cancer only unless used as a method/perturbation reference
- generic signaling reviews without cancer proteomics data
- papers without local PDF or sufficient source text after resolver attempts

## Existing Core Local Papers

| Basename | Status | Why it matters |
| --- | --- | --- |
| `vasaikar-2019-proteogenomic-analysis-human-colon-cancer` | `core-ingested` | Full PDF deep-dive complete. Prospective colon cancer tumor/NAT proteogenomics with WXS/CNA/RNA/miRNA/label-free proteome/TMT proteome/phosphoproteome; SOX9 mutation interpretation revised by protein abundance, RB1/Rb phosphorylation-CDK2 axis, 88 proteomics-supported putative neoantigens, shared CT antigens, and MSI glycolysis-CD8 immune-evasion hypothesis. |
| `chen-2020-proteogenomics-non-smoking-lung-cancer-east` | `core-ingested` | Full PDF deep-dive complete. Taiwanese early-stage never-smoker LUAD proteogenomics with WES/RNA/TMT proteome/phosphoproteome; EGFR/KRAS/TP53 mutation-to-phosphosite MAPK interpretation, TP53 DNA-damage phosphorylation state, APOBEC-high female subgroup with CDK/AurB/CK2 signals, proteomic late-like staging, EGFR-L858R vs Del19 outcome split, and MMP biomarker/druggable-target network. |
| `lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc` | `core-ingested` | Full PDF deep-dive complete. Korean TNBC, WES/RNA/global proteome/phosphoproteome, pCR/non-pCR, AUC 0.946 resistance-factor model, GRK2/AURKB/ITGB8 axes. |
| `anurag-2022-proteogenomic-markers-chemotherapy-resistance-response` | `core-ingested` | Full PDF deep-dive complete. TNBC neoadjuvant chemo response, WES/RNA/TMT proteome/phosphoproteome, pCR/RCB, proteome-level metabolic resistance programs, PTM-SEA kinase signals, and 19q13.31-33 LIG1/POLD1/XRCC1 resistance axis. |
| `zhang-2023-proteogenomics-clear-cell-renal-response-tyrosine-kinase-inhibitor` | `core-ingested` | Full PDF deep-dive complete. Chinese ccRCC sunitinib response cohort with WES/RNA/global proteome/phosphoproteome; 7q gain-LAMTOR4/MDH2/CALU-mTOR resistance, VHL/AA/glycolysis sensitivity, KSEA MTOR/MAP2K1/CDK response split, immune/TGFB1/platelet resistance, and multi-omics RF classifier. |
| `ji-2023-pharmaco-proteogenomic-characterization-liver-cancer-organoids` | `core-ingested` | Full PDF deep-dive complete. LICOB patient-derived liver cancer organoids with WES/CNV/RRBS/RNA/DIA proteome, 76-drug screen, elastic-net AUC prediction, subtype-linked TKI/chemotherapy response, and lenvatinib-temsirolimus combination validation with 23,754-site perturbation phosphoproteomics. |
| `sambath-2026-integrated-genomic-proteomic-cervical-cancer-chemoradiation-resistance` | `core-ingested` | Cervical CCRT response, WGS/WES/global proteome/phosphoproteome, DNA repair hyperactivation, STX3 validation. |
| `xu-2026-proteogenomic-characterization-reveals-subtype-specific-therapeutic` | `core-ingested` | HER2-low breast cancer, WES/RNA/global proteome/phosphoproteome/lactylome, PS1/PS2/PS3 drug-response stratification. |
| `jeong-2025-proteogenomic-profiling-predicts-outcomes-adjuvant-chemotherapy` | `blocked-wrong-pdf` | Journal of Hepatology target, but attempted full ingest found local PDF mismatch: downloaded file is Annals of Transplantation DOI `10.12659/AOT.951088`, not DOI `10.1016/j.jhep.2025.07.031`. |
| `tian-2026-proteogenomic-characterization-cervical-cancer-identifies-molecular` | `new-stub` | JCI; cervical cancer proteogenomic subtype and clinical outcome/subtype-linked therapy candidate. |
| `yang-2026-proteogenomic-atlas-brain-metastases-identifies-molecular` | `new-stub` | Nature Communications; large brain metastasis proteogenomic atlas with therapeutic vulnerabilities. |
| `wu-2025-large-scale-drug-sensitivity-gene-dependency` | `new-stub` | Nature Communications; drug sensitivity, gene dependency, proteogenomics in cancer cell lines. |
| `hsu-2025-phosphoproteomics-osimertinib-tolerant-persister-cells-reveals` | `core-ingested` | Molecular Systems Biology; full PDF deep-dive complete. DIA-MS global/phosphoproteomics of EGFR-mutant NSCLC osimertinib DTPs; CDK1-SAMHD1/PML, mTOR/YAP/BAD, and recovery-state kinase signatures. |
| `holt-2025-proteogenomic-characterization-unveils-biomarkers-associated` | `core-ingested` | Full PDF deep-dive complete. MIBC cisplatin-based chemotherapy response cohort with WES/RNA/TMT proteome/phosphoproteome; mutation-only DDR markers fail, while protein DNA-repair/G2M, GSK3B-S9, RAF-domain SEPEPs, EMT/WNT/KRAS resistance, and ADC-target abundance nominate response and combination strategies. |
| `mcandrews-2025-allele-agnostic-mutant-kras-inhibitor-suppresses` | `new-stub` | Science Translational Medicine; KRAS inhibitor response and tumor immunity/reprogramming. |
| `zheng-2025-depleted-breast-cancers-differentially-sensitive-cdk` | `new-stub` | Science Translational Medicine; NF1-depleted ER+ breast cancer differential CDK4/6 sensitivity. |
| `stupichev-2025-driven-multimodal-algorithm-predicts-immunotherapy-targeted` | `new-stub` | Cell Reports Medicine; multimodal algorithm for immunotherapy/targeted therapy outcomes in ccRCC. |
| `renner-2026-multi-layered-molecular-profiling-informs-diagnosis` | `new-stub` | Nature Communications; multi-layer profiling tied to diagnosis and targeted therapy in DSRCT. |
| `solanki-2026-ras-gtp-inhibition-overcomes-acquired-resistance` | `new-stub` | Cancer Research; acquired KRASG12C inhibitor resistance overcome by RAS-GTP inhibition. |
| `zhao-2025-phosphoproteomic-acetylomic-characterization-colorectal-cancer` | `context-ingested` | Full PDF deep-dive complete. HCT116 kinase-inhibitor perturbation, TMTpro proteome/phosphoproteome/acetylome, target engagement plus off-target kinase reprogramming, mitochondrial effects, PTM crosstalk, and phosphoproteomics-guided drug-pair hypotheses; context reference, not patient-response cohort. |
| `chmielecki-2023-acquired-resistance-first-line-osimertinib` | `context-ingested` | Full PDF deep-dive complete. FLAURA first-line osimertinib plasma ctDNA resistance analysis; 65% of osimertinib-arm acquired-resistance subset had no detectable plasma genomic mechanism, motivating proteome/phosphoproteome/non-genetic resistance layers for the POC. |
| `jaehnig-2025-proteogenomic-analysis-calgb-40601-alliance` | `core-ingested` | Full PDF deep-dive complete. CALGB 40601 HER2+ neoadjuvant trial proteogenomics; ERBB2/HER2 proteogenomic false-positive QC, EMT/ECM/WNT non-pCR programs, immune/cell-cycle pCR programs, PTM-SEA kinase signatures, and validated GPRC5A/TPBG non-pCR biomarkers. |
| `song-2024-proteogenomic-analysis-reveals-non-small-cell` | `core-ingested` | Full PDF deep-dive complete. Korean NSCLC WES/RNA/TMT proteome/phosphoproteome/acetylome cohort; phosphoproteome-heavy five-subtype map, Subtype 4 PI3K-Akt/hypoxia/SLK/LRRFIP1 poor prognosis, Subtype 3 WGD/XPO1-selinexor organoid sensitivity, and Subtype 5 immune-hot adjuvant therapy benefit signal. |
| `satpathy-2021-proteogenomic-portrait-lung-squamous-cell` | `core-ingested` | Full PDF deep-dive complete. CPTAC LSCC atlas with WGS/WES/CNA/methylation/RNA/TMT proteome/phosphoproteome/acetylome and K-GG subset; NSD3-vs-FGFR1 driver logic, phospho-Rb/CDK4/6 response logic, EGFR ligand-vs-amplification lesson, PDGFRB/ROR2 EMT CBPE, TP63-low survivin vulnerability, NRF2 activity, PTM crosstalk, and immune Hot/Warm/Cold states. |
| `yu-2024-proteogenomic-analysis-cervical-cancer-reveals` | `core-briefed` | Cervical cancer WES/phospho/acetyl, subgrouping and radioresponse biomarker nomination. |
| `huang-2021-proteogenomic-insights-biology-treatment-hpv-negative` | `core-ingested` | Full PDF deep-dive complete. HPV-negative HNSCC CPTAC atlas with 108 tumors, 11,744 proteins, 56,959 localized phosphosites, CDK4/6-Rb phosphosite biomarker logic, EGFR ligand-dependent anti-EGFR mAb stratification, EGFR-amplification phosphosignaling, and immune-hot/cold immunotherapy logic. |
| `gillette-2020-proteogenomic-characterization-reveals-therapeutic-vulnerabilities` | `core-ingested` | Full PDF deep-dive complete. CPTAC LUAD with WES/WGS/RNA/methylation/TMT proteome/phosphoproteome/acetylome; ALK Y1507, EGFR-PTPN11 Y62, KRAS-SOS1 S1161, STK11 immune-cold/neutrophil-degranulation proteome signal, and tumor-NAT PTM stoichiometry nominate therapeutic vulnerabilities. |
| `krug-2020-proteogenomic-landscape-breast-cancer-tumorigenesis` | `core-ingested` | Full PDF deep-dive complete. CPTAC breast cancer atlas with 122 tumors, WES/RNA/TMT proteome/phosphoproteome/acetylome, HER2 pseudo-positive protein discordance, ERBB2/MAPK phosphosite logic, immune-active luminal subsets, APOBEC/SSBR-immune links, Rb/phospho-Rb CDK4/6 response logic, mutation-associated kinase outliers, and acetyl-metabolism crosstalk. |
| `cao-2021-proteogenomic-characterization-pancreatic-ductal-adenocarcinoma` | `core-ingested` | Full PDF deep-dive complete. CPTAC PDAC atlas with 140 pancreatic tumors, 67 NATs, 9 normal ducts, WGS/WES/methylation/RNA/miRNA/TMT proteome/phosphoproteome/glycoproteome; purity-aware analysis, KRAS/TP53/CDKN2A/SMAD4 functional effects, PAK1/PAK2/CDK7/AKT1/SRC kinase-substrate axes, immune-cold VEGF/hypoxia/glycolysis/junction-phosphosite mechanism, and C1/C2 proteogenomic subtypes. |
| `deng-2023-proteogenomic-characterization-cholangiocarcinoma` | `core-briefed` | CCA WES + phosphoproteome subtype/kinase hypotheses. |
| `cheng-2025-integrative-proteogenomic-characterization-wilms-tumor` | `core-briefed` | Pediatric WT WES + phosphoproteome, subtype and EHMT2 target emphasis. |
| `ramberger-2024-proteogenomic-landscape-multiple-myeloma-reveals` | `core-briefed` | MM nanopore WGS + phosphoproteomics, risk stratification design reference. |
| `petralia-2024-pan-cancer-proteogenomics-characterization-tumor-immunity` | `context-ingested` | Full PDF deep-dive complete. CPTAC pan-cancer tumor immunity proteogenomics with 1,056 treatment-naive tumors, seven immune subtypes, OAK atezolizumab validation for CD8+/IFNG+ state, mutation/CNV/methylation immune associations, and phosphoproteome-derived kinase hypotheses including CDK, TBK1/IKK/MAPKAPK/Src-family, and PTK2/FAK axes. |
| `li-2023-pan-cancer-driver-functional-states` | `core-briefed` | Pan-cancer driver-to-functional-state proteogenomics. |
| `savage-2024-pan-cancer-proteogenomics-expands-landscape-therapeutic` | `core-briefed` | Pan-cancer therapeutic target landscape from proteogenomics. |
| `jiang-2025-dark-cancer-phosphoproteome-coregulation` | `core-ingested` | Dark phosphoproteome / CoPheeMap / CoPheeKSA, kinase-substrate inference expansion. |
| `muller-dott-2025-phosphoproteomic-kinase-activity-inference` | `core-briefed` | Kinase activity inference benchmark. |
| `chen-2023-global-impact-somatic-structural-variation-cancer-proteome` | `context-briefed` | Somatic SV → protein consequence; useful when response signal is not SNV-only. |

## 2026-05-13 PubMed/PDF Resolver Batch

Status legend:

- `new-stub` = PDF downloaded and `wiki/sources/*` placeholder created; needs full local-PDF deep-dive.
- `duplicate-existing` = already represented by a stronger existing source page; do not count twice.
- `context` = potentially useful but not a core 100-row primary response/proteogenomics paper.
- `exclude-low-priority` = outside strict human cancer global/phospho response scope.

| Basename | Journal | Status | Triage note |
| --- | --- | --- | --- |
| `renner-2026-multi-layered-molecular-profiling-informs-diagnosis` | Nature Communications | `new-stub` | Multi-layer diagnosis/targeted therapy; inspect for proteome/phospho layers. |
| `jin-2026-deciphering-mediated-phosphorylated-alterations-cancer-related` | Int J Biol Macromol | `new-stub` | Cisplatin resistance + phosphorylated proteome; likely mechanistic but journal lower priority. |
| `lombardi-2026-dual-inhibition-mtor-hsp-enhances-cisplatin` | Cell Death & Disease | `new-stub` | Cisplatin resistance, mTOR/HSP90; inspect whether phospho/global proteome data are central. |
| `chesney-2026-longitudinal-detection-tumor-specific-peptides-cerebrospinal` | Cells | `context` | Tumor-specific peptide surveillance; more neoantigen/immunopeptidomics than response-phospho. |
| `chen-2026-timescale-dependent-phosphoproteomic-remodeling-motility-associated` | Cancer Genomics & Proteomics | `new-stub` | Chronic cabozantinib exposure, phosphoproteomic remodeling; likely useful perturbation reference. |
| `dunphy-2026-phosphoproteomic-profiling-multiple-myeloma-vivo-drug` | Biomolecules | `new-stub` | Ex vivo drug sensitivity/resistance testing + phosphoproteomics; direct scope but journal lower priority. |
| `tian-2026-proteogenomic-characterization-cervical-cancer-identifies-molecular` | JCI | `new-stub` | High-priority human proteogenomic subtype/outcome paper. |
| `yang-2026-proteogenomic-atlas-brain-metastases-identifies-molecular` | Nature Communications | `new-stub` | High-priority large human proteogenomic atlas. |
| `sambath-2026-integrated-genomic-proteomic-profiling-reveals-insights` | Molecular Oncology | `duplicate-existing` | Same paper as existing Sambath 2026 source; keep existing canonical page. |
| `wen-2026-lncrna-encoded-micropeptides-emerging-regulators-cancer` | Current Opinion in Cell Biology | `context` | Review; not a core primary response/proteomics row. |
| `shoji-2026-clinical-applications-phosphoproteomics-illuminating-cancer-signaling` | Cancer Science | `context` | Review/clinical applications; useful framing, not core quantitative row. |
| `sitthirak-2026-integrative-sequencing-proteogenomic-approaches-intratumoral-heterogeneity` | Medical Sciences | `context` | Review-like CCA heterogeneity; lower priority. |
| `park-2026-panorama-database-oncogenic-evaluation-somatic-mutations` | Database | `context` | Database for somatic mutation evaluation; supports SNV block, not phospho/global response row. |
| `lin-2026-cabozantinib-induces-nlrp-casp-gsdmd-dependent` | Life Sciences | `context` | Cabozantinib mechanism; inspect if omics depth is sufficient. |
| `hu-2025-mitochondrial-derived-microproteins-cancer-neurodegeneration-era` | Pathology Research and Practice | `context` | Review/context. |
| `wu-2025-large-scale-drug-sensitivity-gene-dependency` | Nature Communications | `new-stub` | High-priority large-scale drug sensitivity + proteogenomics. |
| `chambwe-2025-cellular-heterogeneity-therapeutic-response-profiling-idh` | Scientific Reports | `context` | Therapeutic response profiling; lower-impact but may be model reference. |
| `lefeivre-2026-reduced-prc-function-causes-asparaginase-resistance` | Blood Advances | `new-stub` | Drug resistance in T-ALL; inspect omics/proteome depth. |
| `swift-2026-integration-short-long-read-rna-sequencing` | Cancer Research | `context` | RNA/circRNA discovery; likely not global/phospho response. |
| `hsu-2025-driven-multi-omics-integration-precision-oncology` | Clinical and Experimental Medicine | `context` | AI multi-omics review. |
| `hu-2025-identification-validation-plasma-protein-biomarkers-therapeutic` | Frontiers in Immunology | `context` | Plasma biomarkers; probably not tumor global/phospho response. |
| `son-2025-dual-targeting-ret-src-synergizes-ret` | Molecular Oncology | `new-stub` | RET/SRC co-targeting; inspect proteomic/phospho support. |
| `solanki-2026-ras-gtp-inhibition-overcomes-acquired-resistance` | Cancer Research | `new-stub` | Acquired KRASG12C resistance; high relevance to resistance. |
| `wang-2025-proteomic-analysis-pten-deficient-cells-reveals` | MCP | `new-stub` | Proteomic analysis of PTEN-deficient cells and Src/EphA2 therapeutic potential. |
| `mizuno-2025-focal-adhesion-kinase-dependent-reprogramming-ifn` | J Invest Dermatol | `new-stub` | FAK/PYK2 + IFN signaling sensitization; inspect response/proteomics depth. |
| `serafino-2025-mechanical-cues-regulate-cargo-sorting-export` | Advanced Science | `context` | Broad cell biology; likely outside strict cancer response scope. |
| `liang-2025-promising-immunotherapeutic-target-enhancing-efficacy-third` | Cancer Communications | `new-stub` | CD24 + EGFR-TKI efficacy in EGFR-mutant lung cancer; inspect omics layers. |
| `xiao-2025-identification-bpa-genetically-informed-drug-target` | Human Genomics | `context` | Genetically informed NSCLC target; not necessarily proteome/phospho. |
| `ali-2026-ybx-ybx-targets-potentiate-immune-checkpoint` | Neuro-Oncology | `new-stub` | ICB potentiation target in gliomas; inspect proteomics/phospho evidence. |
| `hsu-2025-phosphoproteomics-osimertinib-tolerant-persister-cells-reveals` | Molecular Systems Biology | `core-ingested` | Full PDF deep-dive complete: EGFR-mutant NSCLC osimertinib DTP phosphoproteomics; CDK1-SAMHD1/PML, mTOR/YAP/BAD, PI3K/MAPK/PKA/PKC recovery signatures; PRIDE `PXD058009`. |
| `peng-2025-targeting-cell-cycle-machinery-cancer-therapy` | Trends in Cell Biology | `context` | Review. |
| `woodard-2025-structural-machine-learning-approach-rapid-prediction` | Cell Reports Methods | `context` | Phosphorylation ML methods; supports prediction, not response cohort. |
| `mcandrews-2025-allele-agnostic-mutant-kras-inhibitor-suppresses` | Science Translational Medicine | `new-stub` | High-priority KRAS inhibitor/translational response paper. |
| `geng-2025-open-pediatric-cancer-project` | GigaScience | `context` | Data infrastructure. |
| `zheng-2025-depleted-breast-cancers-differentially-sensitive-cdk` | Science Translational Medicine | `new-stub` | High-priority ER+ breast CDK4/6 sensitivity paper. |
| `rocca-2025-refining-treatment-strategies-non-small-cell` | British Journal of Cancer | `context` | Multi-omics NSCLC strategy; inspect for proteome/phospho. |
| `aruvornlop-2025-phosphoproteomic-profiling-feline-mammary-carcinoma-insights` | PLOS One | `exclude-low-priority` | Non-human feline cancer; not counted in human cancer core. |
| `stupichev-2025-driven-multimodal-algorithm-predicts-immunotherapy-targeted` | Cell Reports Medicine | `new-stub` | High-priority outcome prediction in ccRCC. |
| `jeong-2025-proteogenomic-profiling-predicts-outcomes-adjuvant-chemotherapy` | Journal of Hepatology | `blocked-wrong-pdf` | High-priority target, but local PDF is wrong article; reacquire before ingest. |
| `burchfield-2025-insulin-signalling-network` | Nature Metabolism | `context` | Signaling reference, likely outside human cancer response corpus. |

## Next Batch Strategy

- Run a narrower PubMed/OpenAlex query for **2016–2026 + journal filter + title/abstract terms**:
  - phosphoproteomics / proteogenomics / global proteome
  - drug response / resistance / chemotherapy / targeted therapy / immunotherapy
  - patient / cohort / organoid / PDX / cell-line perturbation
- Prefer missing high-impact response-labeled papers over generic reviews.
- De-duplicate by DOI/title before generating source pages; the first batch revealed PMID gaps can create duplicate slugs for already ingested papers.
- After each download batch, promote only core rows into the count; context rows remain useful but do not inflate the target.

## Connections

- [Drug Response Proof-of-Concept with Global Proteome, Phosphoproteome, and Somatic SNV](drug-response-poc-global-phospho-somatic-snv.md)
- [Cancer Multiomics Literature Monitor](../topics/cancer-multiomics-literature.md)
- [Cancer Multiomics Corpus Queue (Target=100)](cancer-multiomics-corpus-queue.md)
- [PTM Correction and Kinase Signaling in Cancer Proteomics](../topics/ptm-correction-and-kinase-signaling-in-cancer-proteomics.md)
- [Immunotherapy Resistance and Immune Evasion](../topics/immunotherapy-resistance-and-immune-evasion.md)

## Sources

- Local source pages and PDFs listed above.
- 2026-05-13 PubMed/PDF resolver output: `/tmp/drug_response_phospho_recent_candidates.json` (operational metadata only; not a scientific evidence source).
