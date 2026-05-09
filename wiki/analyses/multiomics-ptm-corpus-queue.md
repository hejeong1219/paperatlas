# Multiomics PTM Corpus Queue

This page is the acquisition and ingest queue for the Korean interactive atlas on recent multi-omics proteomics studies. It exists so the visualization is generated only after PDFs and, when needed, supplementary tables have been read locally.

## Key Points

- The interactive should not be treated as complete until each included row has a local PDF-backed source page and a filled `Multi-Omics Identification Extraction` section.
- Web search or general web pages may help locate candidate papers or downloadable files, but values used in the wiki and visualization must come from local PDFs, local supplements, or maintained source pages.
- Studies should be separated into patient-cohort MS studies, pan-cancer reanalysis/compendia, methods/workflow papers, and cell-line perturbation papers so the plot does not imply false comparability.

## Included / Extraction Started

| Source | Local PDF | Source page | Extraction status | Atlas status |
|---|---|---|---|---|
| Mertins 2016 breast cancer proteogenomics | yes | yes | protein/phospho extracted; acetyl not reported | included, needs instrument confirmation |
| Vasaikar 2019 colon cancer proteogenomics | yes | yes | protein/phospho extracted; acetyl not reported | candidate to add |
| Clark 2020 clear cell renal cell carcinoma | yes | yes | protein/phospho extracted; acetyl not reported | candidate to add |
| Dou 2020 endometrial carcinoma | yes | yes | protein/phospho/acetyl extracted | included |
| Gillette 2020 lung adenocarcinoma | yes | yes | protein/phospho/acetyl extracted | included |
| Wang 2021 glioblastoma | yes | yes | methods and measured-gene counts extracted; exact identification totals need supplements | hold until supplement check |
| Huang 2021 HPV-negative HNSCC | yes | yes | protein/phospho extracted; acetyl not reported | included |
| Cao 2021 pancreatic ductal adenocarcinoma | yes | yes | protein/phospho/glyco extracted; acetyl not reported | included with caveat |
| Satpathy 2021 lung squamous cell carcinoma | yes | yes | phospho/acetyl extracted; protein total needs confirmation | included, needs protein count confirmation |
| Ng 2022 hepatocellular carcinoma | yes | yes | protein/phospho extracted; acetyl not reported | candidate to add |
| Zhang 2022 pan-cancer proteogenomic compendium | yes | yes | aggregate protein/phospho extracted | included as compendium |
| Li 2023 pan-cancer CPTAC proteogenomics | yes | yes | aggregate protein/phospho extracted | included as compendium |
| Zhao 2025 HCT116 kinase inhibitor perturbation | yes | yes | protein/phospho/acetyl extracted | included as cell-line perturbation |

## Acquisition Snapshot

- Candidate corpus size: 60 papers from 2016-2026 PubMed metadata triage.
- Local PDFs available by resolver count: 56/60, but at least one local PDF is a title/DOI mismatch and is blocked from ingest until corrected.
- Status meaning: `downloaded` means a PDF exists locally; it does not yet mean numeric extraction is complete.

## Extraction Snapshot

- Current status: not fully ingested yet.
- Source pages with a `Multi-Omics Identification Extraction` section: 50.
- Placeholder extraction sections still awaiting PDF/supplement deep-read: 22.
- Blocked by verified local PDF mismatch or correction-only PDF: 2, Xu 2022 urothelial carcinoma and Dong 2024 high-risk prostate cancer.
- Newly deep-read in this pass: Abelin 2023 MONTE workflow, Shi 2022 medullary thyroid carcinoma, Deng 2023 cholangiocarcinoma, Li 2023 early duodenal cancer, and Zhao 2025 HCT116 kinase-inhibitor PTM perturbation metadata correction.
- Additional visualization-linked ingest batch: Ramberger 2024 multiple myeloma, Holt 2025 muscle-invasive bladder cancer, Park 2024 never-smoker lung adenocarcinoma, and Su 2025 LUAD subsolid nodules.
- Extra acquisition retry: selected 50 additional 2016-2026 candidates from the 336-paper discovery set; resolver plus KU/cookie retry recovered 32/50 PDFs.
- Extra visualization-linked ingest batch: Huang 2022 NPC SAHA perturbation, Zhao 2024 ESCC, and Oh 2020 IDH-wild-type glioblastoma.
- Visualization coverage update: `interactives/multiomics-proteomics-ptm-identification/data/studies.json` now includes 67 rows so the HTML reflects the 2016-2026 corpus breadth. Rows are status-coded as `extracted`, `pdf_pending_extraction`, `pdf_pending`, or `blocked_pdf`; quantitative bars should be interpreted only for rows with extracted values.

| Status | Year | Source | DOI |
|---|---:|---|---|
| downloaded | 2016 | [Proteogenomics connects somatic mutations to signalling in breast cancer.](../sources/mertins-2016-proteogenomics-connects-somatic-mutations-signalling.md) | 10.1038/nature18003 |
| downloaded | 2025 | [Integrative proteogenomic characterization of Wilms tumor.](../sources/cheng-2025-integrative-proteogenomic-characterization-wilms-tumor.md) | 10.1038/s41467-025-62234-7 |
| downloaded | 2025 | [Integrated proteogenomic characterization of localized prostate cancer identifies biological insights and subtype-specific therapeutic strategies.](../sources/ou-2025-integrated-proteogenomic-characterization-localized-prostate.md) | 10.1038/s41467-025-58569-w |
| downloaded | 2022 | [Integrative proteogenomic characterization of hepatocellular carcinoma across etiologies and stages.](../sources/ng-2022-integrative-proteogenomic-characterization-hepatocellular-carcinoma.md) | 10.1038/s41467-022-29960-8 |
| downloaded | 2020 | [Proteogenomic Characterization Reveals Therapeutic Vulnerabilities in Lung Adenocarcinoma.](../sources/gillette-2020-proteogenomic-characterization-reveals-therapeutic-vulnerabilities.md) | 10.1016/j.cell.2020.06.013 |
| downloaded | 2019 | [Proteogenomic Analysis of Human Colon Cancer Reveals New Therapeutic Opportunities.](../sources/vasaikar-2019-proteogenomic-analysis-human-colon-cancer.md) | 10.1016/j.cell.2019.03.030 |
| downloaded | 2025 | [Integrative proteogenomic characterization reveals therapeutic targets in poorly differentiated and anaplastic thyroid cancers.](../sources/pan-2025-integrative-proteogenomic-characterization-reveals-therapeutic.md) | 10.1038/s41467-025-58910-3 |
| downloaded | 2025 | [Proteogenomic characterization reveals that lipid droplet formation promotes esophageal squamous cell cancer progression.](../sources/qin-2025-proteogenomic-characterization-reveals-lipid-droplet.md) | 10.1126/scitranslmed.adt0214 |
| downloaded | 2024 | [Proteogenomic characterization of skull-base chordoma.](../sources/zhang-2024-proteogenomic-characterization-skull-base-chordoma.md) | 10.1038/s41467-024-52285-7 |
| downloaded | 2021 | [Proteogenomic characterization of pancreatic ductal adenocarcinoma.](../sources/cao-2021-proteogenomic-characterization-pancreatic-ductal-adenocarcinoma.md) | 10.1016/j.cell.2021.08.023 |
| downloaded | 2021 | [Proteogenomics of non-small cell lung cancer reveals molecular subtypes associated with specific therapeutic targets and immune evasion mechanisms.](../sources/lehti-2021-proteogenomics-non-small-cell-lung-cancer.md) | 10.1038/s43018-021-00259-9 |
| downloaded | 2019 | [Integrated Proteogenomic Characterization of Clear Cell Renal Cell Carcinoma.](../sources/clark-2019-integrated-proteogenomic-characterization-clear-cell.md) | 10.1016/j.cell.2019.10.007 |
| downloaded | 2022 | [Proteogenomic characterization of 2002 human cancers reveals pan-cancer molecular subtypes and associated pathways.](../sources/zhang-2022-proteogenomic-characterization-2002-human-cancers.md) | 10.1038/s41467-022-30342-3 |
| downloaded | 2023 | [Pharmaco-proteogenomic characterization of liver cancer organoids for precision oncology.](../sources/ji-2023-pharmaco-proteogenomic-characterization-liver-cancer-organoids.md) | 10.1126/scitranslmed.adg3358 |
| downloaded | 2016 | [Integrated Proteogenomic Characterization of Human High-Grade Serous Ovarian Cancer.](../sources/zhang-2016-integrated-proteogenomic-characterization-human-high-grade.md) | 10.1016/j.cell.2016.05.069 |
| downloaded | 2025 | [Integrated proteogenomic characterization of ampullary adenocarcinoma.](../sources/zhang-2025-integrated-proteogenomic-characterization-ampullary-adenocarcinoma.md) | 10.1038/s41421-024-00742-4 |
| downloaded | 2024 | [A proteogenomic analysis of cervical cancer reveals therapeutic and biological insights.](../sources/yu-2024-proteogenomic-analysis-cervical-cancer-reveals.md) | 10.1038/s41467-024-53830-0 |
| downloaded | 2020 | [Proteogenomic Characterization of Endometrial Carcinoma.](../sources/dou-2020-proteogenomic-characterization-endometrial-carcinoma.md) | 10.1016/j.cell.2020.01.026 |
| downloaded | 2020 | [Proteogenomic Landscape of Breast Cancer Tumorigenesis and Targeted Therapy.](../sources/krug-2020-proteogenomic-landscape-breast-cancer-tumorigenesis.md) | 10.1016/j.cell.2020.10.036 |
| downloaded | 2024 | [Pan-cancer proteogenomics characterization of tumor immunity.](../sources/petralia-2024-pan-cancer-proteogenomics-characterization-tumor-immunity.md) | 10.1016/j.cell.2024.01.027 |
| downloaded | 2023 | [Histopathologic and proteogenomic heterogeneity reveals features of clear cell renal cell carcinoma aggressiveness.](../sources/li-2023-histopathologic-proteogenomic-heterogeneity-reveals-features.md) | 10.1016/j.ccell.2022.12.001 |
| downloaded | 2023 | [Proteogenomics of clear cell renal cell carcinoma response to tyrosine kinase inhibitor.](../sources/zhang-2023-proteogenomics-clear-cell-renal-cell.md) | 10.1038/s41467-023-39981-6 |
| downloaded | 2022 | [Integrated proteogenomic characterization of medullary thyroid carcinoma.](../sources/shi-2022-integrated-proteogenomic-characterization-medullary-thyroid.md) | 10.1038/s41421-022-00479-y |
| downloaded | 2022 | [Proteogenomic analysis of lung adenocarcinoma reveals tumor heterogeneity, survival determinants, and therapeutically relevant pathways.](../sources/soltis-2022-proteogenomic-analysis-lung-adenocarcinoma-reveals.md) | 10.1016/j.xcrm.2022.100819 |
| downloaded | 2022 | [Proteogenomic characterization of MiT family translocation renal cell carcinoma.](../sources/qu-2022-proteogenomic-characterization-mit-family-translocation.md) | 10.1038/s41467-022-34460-w |
| downloaded | 2020 | [Proteogenomics of Non-smoking Lung Cancer in East Asia Delineates Molecular Signatures of Pathogenesis and Progression.](../sources/chen-2020-proteogenomics-non-smoking-lung-cancer-east.md) | 10.1016/j.cell.2020.06.012 |
| downloaded | 2020 | [Integrated Proteogenomic Characterization across Major Histological Types of Pediatric Brain Cancer.](../sources/petralia-2020-integrated-proteogenomic-characterization-across-major.md) | 10.1016/j.cell.2020.10.044 |
| downloaded | 2019 | [Proteogenomic Characterization of Human Early-Onset Gastric Cancer.](../sources/mun-2019-proteogenomic-characterization-human-early-onset-gastric.md) | 10.1016/j.ccell.2018.12.003 |
| pending | 2026 | [Proteogenomic Characterization Reveals Subtype-Specific Therapeutic Potential for HER2-Low Breast Cancer.](../sources/xu-2026-proteogenomic-characterization-reveals-subtype-specific-therapeutic.md) | 10.1002/advs.202513086 |
| pending | 2026 | [Proteogenomic Characterization Reveals Metabolic Vulnerabilities and Aberrant Phosphorylation in Colorectal Metastasis to Liver.](../sources/zhao-2026-proteogenomic-characterization-reveals-metabolic-vulnerabilities.md) | 10.1002/advs.202511744 |
| pending | 2025 | [Proteogenomic characterization of non-functional pancreatic neuroendocrine tumors unravels clinically relevant subgroups.](../sources/ji-2025-proteogenomic-characterization-non-functional-pancreatic-neuroendocrine.md) | 10.1016/j.ccell.2025.03.016 |
| downloaded | 2025 | [Proteogenomic characterization unveils biomarkers associated with chemoresistance in muscle-invasive bladder cancer.](../sources/holt-2025-proteogenomic-characterization-unveils-biomarkers-associated.md) | 10.1016/j.xcrm.2025.102255 |
| downloaded | 2025 | [Proteogenomic characterization reveals tumorigenesis and progression of lung cancer manifested as subsolid nodules.](../sources/su-2025-proteogenomic-characterization-reveals-tumorigenesis-progression.md) | 10.1038/s41467-025-57364-x |
| downloaded | 2025 | [Proteogenomic Analysis on RNA m6A Modification-Associated Genes Identifies a Distinct Subgroup with High IGF2BPs Expression Across Cancer Types.](../sources/ryu-2025-proteogenomic-analysis-rna-m6a-modification-associated.md) | 10.7150/ijms.115609 |
| pending | 2024 | [Integrated proteogenomic characterization of glioblastoma evolution.](../sources/kim-2024-integrated-proteogenomic-characterization-glioblastoma-evolution.md) | 10.1016/j.ccell.2023.12.015 |
| pending | 2024 | [Evolutionary proteogenomic landscape from pre-invasive to invasive lung adenocarcinoma.](../sources/zhang-2024-evolutionary-proteogenomic-landscape-pre-invasive-invasive.md) | 10.1016/j.xcrm.2023.101358 |
| downloaded | 2024 | [Proteogenomic Characterization Reveals Estrogen Signaling as a Target for Never-Smoker Lung Adenocarcinoma Patients without EGFR or ALK Alterations.](../sources/park-2024-proteogenomic-characterization-reveals-estrogen-signaling.md) | 10.1158/0008-5472.CAN-23-1551 |
| downloaded | 2024 | [Integrative proteogenomic profiling of high-risk prostate cancer samples from Chinese patients indicates metabolic vulnerabilities and diagnostic biomarkers.](../sources/dong-2024-integrative-proteogenomic-profiling-high-risk-prostate.md) | 10.1038/s43018-024-00820-2 |
| downloaded | 2024 | [Proteogenomic characterization of difficult-to-treat breast cancer with tumor cells enriched through laser microdissection.](../sources/rajkumar-2024-proteogenomic-characterization-difficult-to-treat-breast-cancer.md) | 10.1186/s13058-024-01835-4 |
| downloaded | 2024 | [Deciphering the ghost proteome in ovarian cancer cells by deep proteogenomic characterization.](../sources/garciadelrio-2024-deciphering-ghost-proteome-ovarian-cancer.md) | 10.1038/s41419-024-07046-1 |
| downloaded | 2024 | [Proteogenomic characterization of primary colorectal cancer and metastatic progression identifies proteome-based subtypes and signatures.](../sources/tanaka-2024-proteogenomic-characterization-primary-colorectal-cancer.md) | 10.1016/j.celrep.2024.113810 |
| downloaded | 2024 | [Integrated Proteogenomic Analysis Reveals Distinct Potentially Actionable Therapeutic Vulnerabilities in Triple-Negative Breast Cancer Subtypes.](../sources/kaur-2024-integrated-proteogenomic-analysis-reveals-distinct.md) | 10.3390/cancers16030516 |
| downloaded | 2023 | [Proteogenomic characterization of cholangiocarcinoma.](../sources/deng-2023-proteogenomic-characterization-cholangiocarcinoma.md) | 10.1002/hep.32624 |
| downloaded | 2022 | [Integrated proteogenomic characterization of urothelial carcinoma of the bladder.](../sources/xu-2022-integrated-proteogenomic-characterization-urothelial-carcinoma.md) | 10.1186/s13045-022-01291-7 |
| downloaded | 2022 | [Integrated proteogenomic characterization across major histological types of pituitary neuroendocrine tumors.](../sources/zhang-2022-integrated-proteogenomic-characterization-across-major.md) | 10.1038/s41422-022-00736-5 |
| downloaded | 2020 | [Proteogenomic Characterization of Ovarian HGSC Implicates Mitotic Kinases, Replication Stress in Observed Chromosomal Instability.](../sources/mcdermott-2020-proteogenomic-characterization-ovarian-hgsc-implicates.md) | 10.1016/j.xcrm.2020.100004 |
| downloaded | 2025 | [Deep proteogenomic characterization of pancreatic solid pseudopapillary neoplasm reveals unique features distinct from other pancreatic tumors.](../sources/tanaka-2025-deep-proteogenomic-characterization-pancreatic-solid.md) | 10.1186/s40364-025-00875-y |
| downloaded | 2024 | [Pan-cancer proteogenomics expands the landscape of therapeutic targets.](../sources/savage-2024-pan-cancer-proteogenomics-expands-landscape-therapeutic.md) | 10.1016/j.cell.2024.05.039 |
| downloaded | 2024 | [The proteogenomic landscape of multiple myeloma reveals insights into disease biology and therapeutic opportunities.](../sources/ramberger-2024-proteogenomic-landscape-multiple-myeloma-reveals.md) | 10.1038/s43018-024-00784-3 |
| downloaded | 2024 | [Proteogenomic characterization of highly enriched viable leukemic blasts in acute myeloid leukemia: A SWOG report.](../sources/naru-2024-proteogenomic-characterization-highly-enriched-viable.md) | 10.1002/jha2.1041 |
| downloaded | 2023 | [Comprehensive proteogenomic characterization of early duodenal cancer reveals the carcinogenesis tracks of different subtypes.](../sources/li-2023-comprehensive-proteogenomic-characterization-early-duodenal.md) | 10.1038/s41467-023-37221-5 |
| downloaded | 2023 | [Tissue Proteogenomic Landscape Reveals the Role of Uncharacterized SEL1L3 in Progression and Immunotherapy Response in Lung Adenocarcinoma.](../sources/shen-2023-tissue-proteogenomic-landscape-reveals-role.md) | 10.1021/acs.jproteome.2c00382 |
| downloaded | 2023 | [Proteogenomic characterization of ferroptosis regulators reveals therapeutic potential in glioblastoma.](../sources/wang-2023-proteogenomic-characterization-ferroptosis-regulators-reveals.md) | 10.1186/s12885-023-10894-3 |
| downloaded | 2018 | [Credentialing Individual Samples for Proteogenomic Analysis.](../sources/zhao-2018-credentialing-individual-samples-proteogenomic-analysis.md) | 10.1074/mcp.RA118.000645 |
| downloaded | 2017 | [Targeted proteomic assays for quantitation of proteins identified by proteogenomic analysis of ovarian cancer.](../sources/song-2017-targeted-proteomic-assays-quantitation-proteins.md) | 10.1038/sdata.2017.91 |
| downloaded | 2025 | [Proteogenomic analysis of the CALGB 40601 (Alliance) HER2+ breast cancer neoadjuvant trial reveals resistance biomarkers.](../sources/jaehnig-2025-proteogenomic-analysis-calgb-40601-alliance.md) | 10.1016/j.xcrm.2025.102154 |
| downloaded | 2025 | [Mapping the functional network of human cancer through machine learning and pan-cancer proteogenomics.](../sources/shi-2025-mapping-functional-network-human-cancer.md) | 10.1038/s43018-024-00869-z |
| downloaded | 2024 | [A proteogenomic analysis of the adiposity colorectal cancer relationship identifies GREM1 as a probable mediator.](../sources/lee-2024-proteogenomic-analysis-adiposity-colorectal-cancer.md) | 10.1093/ije/dyae175 |
| downloaded | 2024 | [The Proteogenomics of Prostate Cancer Radioresistance.](../sources/haas-2024-proteogenomics-prostate-cancer-radioresistance.md) | 10.1158/2767-9764.CRC-24-0292 |
| downloaded | 2024 | [Proteogenomic characterization identifies clinical subgroups in EGFR and ALK wild-type never-smoker lung adenocarcinoma.](../sources/kim-2024-proteogenomic-characterization-identifies-clinical-subgroups.md) | 10.1038/s12276-024-01320-0 |

## Candidate PDFs To Triage

| Source | Reason to triage | Current decision |
|---|---|---|
| Gillette 2019 breast cancer quantitative proteome landscape | breast CPTAC proteogenomics context | maybe; check whether phospho/acetyl counts are in scope |
| Li 2023 early esophageal squamous cell carcinoma | large proteome and phosphoproteome profiling | candidate; acetyl not apparent in PDF text |
| Hu 2024 early-onset endometrioid endometrial cancer | recent proteogenomic cohort | candidate; extract PDF before use |
| Jiang 2024 integrated multiomic breast cancer | large proteome/metabolome cohort | maybe; phospho/acetyl not apparent in extracted text |
| Zhang 2024 air-pollution-associated lung cancer proteogenomics | recent proteogenomic cohort | candidate; extract PDF before use |
| Yu 2024 cervical cancer proteogenomic analysis | recent cancer proteogenomics | candidate; extract PDF before use |
| Zhang 2025 ampullary adenocarcinoma proteogenomics | recent cancer proteogenomics | candidate; extract PDF before use |
| Pan 2025 integrative proteogenomic characterization | recent cancer proteogenomics | candidate; extract PDF before use |
| Ou 2025 localized prostate cancer proteogenomics | recent cancer proteogenomics | candidate; extract PDF before use |
| Qin 2025 lipid-droplet proteogenomic characterization | recent cancer proteogenomics | candidate; extract PDF before use |

## Exclusion Notes

- Spatial transcriptomics or single-cell multiomic papers without MS-based proteome/phosphoproteome/acetylome identification counts should be excluded from the quantitative atlas, even if they use the word multiomic.
- Methods-only, review, database, and visualization-tool papers should be cited in notes only if they explain methodology; they should not become study rows.
- Search result metadata is not evidence for counts, instruments, or methods.

## Next Actions

1. Download or locate supplementary tables for studies marked `needs_supplement`.
2. Deep-read candidate PDFs one by one and add the extraction section to each source page.
3. Rebuild `interactives/multiomics-proteomics-ptm-identification/data/studies.json` only from source pages with extraction status complete or clearly caveated.
4. Regenerate the Korean HTML interactive and publish after sync/build.

## Connections

- [Multiomics Proteomics PTM Identification](../topics/multiomics-proteomics-ptm-identification.md)
- [Multiomics Proteomics PTM Identification Atlas](./multiomics-proteomics-ptm-identification-atlas.md)
- [PTM Correction and Kinase Signaling in Cancer Proteomics](../topics/ptm-correction-and-kinase-signaling-in-cancer-proteomics.md)

## Sources

- Local PDFs under `raw/inbox/papers/`.
- Maintained source pages under `wiki/sources/`.
