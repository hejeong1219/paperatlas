---
title: "Proteogenomic and metabolomic characterization of human glioblastoma"
authors:
  - "Wang"
  - "Karpova"
  - "Gritsenko"
year: 2021
journal: "Cancer Cell"
doi: "10.1016/j.ccell.2021.01.006"
paper_kind: proteogenomic
pdf: "raw/inbox/papers/wang-2021-proteogenomic-metabolomic-characterization-human-glioblastoma.pdf"
topic: multiomics-proteomics-ptm-identification
tags:
  - "multiomics-proteomics-ptm-identification"
  - "ptmanchor"
  - "proteomics"
  - "ptm"
  - "phosphoproteomics"
  - "acetylomics"
  - "cancer-proteomics"
themes:
  - "ptm-correction"
  - "kinase-signaling"
  - "cancer-proteomics"
batch_ingest_status: pdf-text-extracted
batch_ingested_on: 2026-05-13
cm_axis: phospho
---
# Proteogenomic and metabolomic characterization of human glioblastoma

_Cancer Cell, 2021._

## Summary

Adult glioblastoma(GBM) 99예(치료 전)에서 WGS/WES·전사체·단백체·phosphoproteome·acetylome·lipidome·metabolome 및 snRNA-seq를 통합해, (1) RTK-altered tumor에서 PTPN11/PLCG1 phospho signaling hub, (2) bulk omics 기반 4개 immune subtype(후속 snRNA-seq로 확인), (3) EMT signature의 cell-type 특이성(종양세포 vs stroma 분리), (4) classical-like/immune-low에서 histone H2B acetylation 축(브로모도메인/CREBBP/EP300 연계)을 제시한다.

## Batch PDF Ingest Status

- Status: `pdf-text-extracted` on 2026-05-13.
- Local PDF: `raw/inbox/papers/wang-2021-proteogenomic-metabolomic-characterization-human-glioblastoma.pdf`.
- Extracted text length: 52,286 characters.
- Scope note: automated local-PDF text ingest for the 100-paper drug-response/phospho-global batch; not yet a manual full-text deep-dive.
- Evidence boundary: downstream scientific claims should use this page only after source-specific Key Points are manually promoted or rechecked against the local PDF.
- High-signal PDF snippets:
  - Article Proteogenomic and metabolomic characterization of human glioblastoma Graphical Abstract Authors Liang-Bo Wang, Alla Karpova, Marina A.
  - Gritsenko, ..., Tao Liu, Li Ding, Clinical Proteomic Tumor Analysis Consortium Correspondence karin.rodland@pnnl.gov (K.D.R.), tao.liu@pnnl.gov (T.L.), lding@wustl.edu (L.D.) In Brief Wang et al.
  - perform integrated proteogenomic analysis of adult glioblastoma (GBM), including metabolomics, lipidomics, and single nuclei RNA-Seq, revealing insights into the immune landscape of GBM, cell- specific nature of EMT signatures, histone acetylation in classical GBM, and the existence of signaling hubs which could provide thera...
  - https://doi.org/10.1016/j.ccell.2021.01.006 ll ll OPEN ACCESS Article Proteogenomic and metabolomic characterization of human glioblastoma Liang-Bo Wang,1,2,48 Alla Karpova,1,2,48 Marina A.
  - Integrated analysis of genomic, proteomic, post-trans- lational modification and metabolomic data on 99 treatment-naive GBMs provides insights to GBM biology.

## Key Points

- Cohort/레이어: 치료 전 GBM 99예에서 proteome/phosphoproteome/acetylome 및 lipid/metabolome까지 포함하는 multi-omics를 수집하고, 일부 샘플은 snRNA-seq로 bulk 기반 immune subtype을 검증한다.
- Signaling hub: RTK alteration과 연동되는 PTPN11(Shp2)·PLCG1의 특정 phosphosite가 기능적 전환점(candidate switch)으로 제시된다.
- Immune subtyping: bulk omics 기반으로 서로 다른 면역세포 조성/경로를 갖는 4개 immune subtype을 제시하고, 단일핵 RNA-seq로 세포 조성 차이를 확인한다.
- Acetylome 메시지: histone H2B acetylation이 classical-like + macrophage-low 상태를 특징짓는 축으로 제시되며, BRD/CREBBP/EP300과의 연결을 강조한다.
- Atlas 관점 caveat: 논문 본문/STAR Methods에는 iProFun에 사용된 “measured gene” 수가 나오지만, proteome/phosphoproteome/acetylome의 전체 identification 총량(단백/사이트/펩타이드 단위)은 main PDF만으로는 한 줄로 확정하기 어렵다(보충자료/테이블 확인 필요).

## Multi-Omics Identification Extraction

- Cohort / scope: glioblastoma proteogenomic and metabolomic cohort with MS-based proteome, phosphoproteome, acetylome, lipidome, and metabolome layers.
- Proteome: global proteome was measured by TMT-11 LC-MS/MS. The extracted main PDF text exposes 7,464 genes with measured RNA/protein for iProFun, but a clean total identified protein count was not visible in the main text extraction. The STAR Methods phrase “hg38; 41,734 proteins” refers to the RefSeq search database size used for MS-GF+, not proteins identified in the cohort.
- Phosphoproteome: extracted PDF text reports 4,433 genes with measured RNA/protein/phospho for iProFun; exact total identified phosphosites should be confirmed from supplementary tables before atlas use.
- Acetylome: extracted PDF text reports 1,315 genes with measured RNA/protein/acetyl for iProFun and describes acetylated peptide quantification; exact total acetylsite or acetylpeptide identification count should be confirmed from supplementary tables before atlas use.
- MS method: TMT-11 labeling, phosphopeptide enrichment, PTMScan acetyl-lysine immunoaffinity purification, and LC-MS/MS.
- Instrument / platform: nanoACQUITY LC separations; Orbitrap Fusion Lumos mass spectrometer for global proteome/phosphoproteome/acetylome LC-MS/MS.
- Extraction evidence: local PDF STAR Methods include “LC-MS/MS analysis of the TMT11-labeled…” and explicitly state Orbitrap Fusion Lumos for MS analysis; STAR Methods also report the iProFun measured-gene counts (RNA/protein=7,464; RNA/protein/phospho=4,433; RNA/protein/acetyl=1,315).
- Interpretation note: mark this source as `needs_supplement` for exact identification counts before it becomes a quantitative bar in the interactive.

## Open Questions

- Proteome/phosphoproteome/acetylome의 “총 identification” (protein vs protein group vs peptide vs site)의 대표 숫자는 어느 Supplementary Table에 존재하는가?
- CPTAC 데이터 포털/공개 테이블에서 atlas가 참조해야 할 “단위별 총량”은 어떤 레벨(IDs vs quantified features)로 제공되는가?

## Connections

- [Ptmanchor Topic Hub](../topics/ptm-correction-and-kinase-signaling-in-cancer-proteomics.md)
- [Ptmanchor Anchor](../analyses/ptmanchor-manuscript-anchor.md)
- [Multiomics Proteomics PTM Identification](../topics/multiomics-proteomics-ptm-identification.md)

## Sources

- Local PDF: `raw/inbox/papers/wang-2021-proteogenomic-metabolomic-characterization-human-glioblastoma.pdf`

## 함께 인용된 논문

위키 분석·합성 페이지에서 이 논문과 함께 인용된 논문들 (co-citation).

- [[clark-2020-integrated-proteogenomic-characterization-clear-cell|Clark 2020]]
- [[vasaikar-2019-proteogenomic-analysis-human-colon-cancer|Vasaikar 2019]]
- [[cao-2021-proteogenomic-characterization-pancreatic-ductal-adenocarcinoma|Cao 2021]]
- [[dou-2020-proteogenomic-characterization-endometrial-carcinoma|Dou 2020]]
- [[gillette-2020-proteogenomic-characterization-reveals-therapeutic-vulnerabilities|Gillette 2020]]
- [[huang-2021-proteogenomic-insights-biology-treatment-hpv-negative|Huang 2021]]
- [[li-2023-pan-cancer-proteogenomics-connects-oncogenic-drivers|Li 2023]]
- [[mertins-2016-proteogenomics-connects-somatic-mutations-signalling|Mertins 2016]]
- [[ng-2022-integrative-proteogenomic-characterization-hepatocellular-carcinoma|Ng 2022]]
- [[satpathy-2021-proteogenomic-portrait-lung-squamous-cell|Satpathy 2021]]
