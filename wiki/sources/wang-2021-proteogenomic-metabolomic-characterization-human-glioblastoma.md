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
---
# Proteogenomic and metabolomic characterization of human glioblastoma

_Cancer Cell, 2021._

## Summary

Adult glioblastoma(GBM) 99예(치료 전)에서 WGS/WES·전사체·단백체·phosphoproteome·acetylome·lipidome·metabolome 및 snRNA-seq를 통합해, (1) RTK-altered tumor에서 PTPN11/PLCG1 phospho signaling hub, (2) bulk omics 기반 4개 immune subtype(후속 snRNA-seq로 확인), (3) EMT signature의 cell-type 특이성(종양세포 vs stroma 분리), (4) classical-like/immune-low에서 histone H2B acetylation 축(브로모도메인/CREBBP/EP300 연계)을 제시한다.

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
