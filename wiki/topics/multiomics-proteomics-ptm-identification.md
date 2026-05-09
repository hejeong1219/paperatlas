# Multiomics Proteomics PTM Identification

최근 10년간 MS 기반 멀티오믹스 연구에서 단백체, 인산화 단백체, 아세틸 단백체의 identification 규모와 방법론을 비교하기 위한 독립 주제 허브.

## Key Points

- 이 주제는 `ptmanchor`의 보조 자료가 아니라, 교수님 요청에 맞춘 별도 interactive atlas 주제다.
- 포함 기준은 MS 기반 proteome, phosphoproteome, acetylome 또는 acetyl-proteome 계층을 실제로 측정한 논문이다.
- 시각화에 들어가는 숫자는 웹 검색 결과가 아니라 로컬 PDF, 보충자료, 그리고 그 PDF에서 ingest된 source page만 근거로 삼는다.
- 단백질, protein group, gene-level protein abundance, phosphopeptide, phosphosite, acetylsite, acetylated peptide는 서로 다른 단위로 보존한다.
- patient cohort, pan-cancer compendium, workflow/method paper, cell-line perturbation study는 plot 안에서 분리해서 보여야 한다.

## Scope

- Time window: 2016-2026 범위의 최근 10년 논문을 우선한다.
- Core modalities: proteome, phosphoproteome, acetylome.
- Required extraction fields: cancer type or model, cohort/sample count, protein identification count, phosphosite/phosphopeptide count, acetylsite/acetylpeptide count, MS labeling/acquisition method, enrichment method, LC-MS/MS platform, instrument, software/search pipeline, count caveats.
- Output: Korean standalone interactive HTML under `interactives/multiomics-proteomics-ptm-identification/`.

## Corpus Workflow

1. 후보 논문을 [Multiomics PTM Corpus Queue](../analyses/multiomics-ptm-corpus-queue.md)에 먼저 등록한다.
2. PDF와 필요한 supplementary table을 `raw/` 아래에 확보한다.
3. 각 논문 source page에 `Multi-Omics Identification Extraction` 섹션을 만든다.
4. 추출 완료 논문만 `interactives/multiomics-proteomics-ptm-identification/data/studies.json`에 반영한다.
5. Korean interactive HTML을 갱신하고 GitHub Pages로 publish한다.

## Current Seed Sources

- [Proteogenomics connects somatic mutations to signalling in breast cancer](../sources/mertins-2016-proteogenomics-connects-somatic-mutations-signalling.md)
- [Proteogenomic Analysis of Human Colon Cancer Reveals New Therapeutic Opportunities](../sources/vasaikar-2019-proteogenomic-analysis-human-colon-cancer.md)
- [Integrated Proteogenomic Characterization of Clear Cell Renal Cell Carcinoma](../sources/clark-2020-integrated-proteogenomic-characterization-clear-cell.md)
- [Proteogenomic Characterization of Endometrial Carcinoma](../sources/dou-2020-proteogenomic-characterization-endometrial-carcinoma.md)
- [Proteogenomic Characterization Reveals Therapeutic Vulnerabilities in Lung Adenocarcinoma](../sources/gillette-2020-proteogenomic-characterization-reveals-therapeutic-vulnerabilities.md)
- [Proteogenomic and metabolomic characterization of human glioblastoma](../sources/wang-2021-proteogenomic-metabolomic-characterization-human-glioblastoma.md)
- [Proteogenomic insights into the biology and treatment of HPV-negative head and neck squamous cell carcinoma](../sources/huang-2021-proteogenomic-insights-biology-treatment-hpv-negative.md)
- [Proteogenomic characterization of pancreatic ductal adenocarcinoma](../sources/cao-2021-proteogenomic-characterization-pancreatic-ductal-adenocarcinoma.md)
- [A proteogenomic portrait of lung squamous cell carcinoma](../sources/satpathy-2021-proteogenomic-portrait-lung-squamous-cell.md)
- [Integrative proteogenomic characterization of hepatocellular carcinoma across etiologies and stages](../sources/ng-2022-integrative-proteogenomic-characterization-hepatocellular-carcinoma.md)
- [Proteogenomic characterization of 2002 human cancers reveals pan-cancer molecular subtypes and associated pathways](../sources/zhang-2022-proteogenomic-characterization-2002-human-cancers.md)
- [Pan-cancer proteogenomics connects oncogenic drivers to functional states](../sources/li-2023-pan-cancer-proteogenomics-connects-oncogenic-drivers.md)
- [Phosphoproteomic and Acetylomic Characterization of Colorectal Cancer Cells Treated with Kinase Inhibitors](../sources/zhao-2025-phosphoproteomic-acetylomic-characterization-colorectal-cancer.md)

## Open Questions

- 각 후보 논문의 supplementary table에서 main PDF보다 더 정확한 total identification count를 제공하는가?
- pan-cancer compendium row를 single-cohort row와 같은 scale에 놓을지, 별도 panel로 분리할지?
- acetylome이 없는 proteogenomic cohort를 핵심 비교군으로 둘지, 아니면 acetylome 포함 논문만 별도 강조할지?

## Connections

- [Multiomics PTM Corpus Queue](../analyses/multiomics-ptm-corpus-queue.md)
- [Multiomics Proteomics PTM Identification Atlas](../analyses/multiomics-proteomics-ptm-identification-atlas.md)
- Interactive project: `interactives/multiomics-proteomics-ptm-identification/`

## Sources

- Local PDFs under `raw/inbox/papers/`.
- Source pages listed above.
