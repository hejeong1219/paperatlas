---
title: "Gastric cancer genomics study using reference human pangenomes"
authors:
  - "Jiao"
  - "Dong"
  - "Fan"
  - "Liu"
  - "Yu"
  - "Wei"
year: 2025
journal: "Life Science Alliance"
doi: "10.26508/lsa.202402977"
paper_kind: resource
pdf: "raw/inbox/papers/jiao-2025-gastric-cancer-reference-human-pangenomes.pdf"
modalities:
  - wgs
  - pangenome
themes:
  - structural-variants
  - reference-bias
cancer_types:
  - gastric-cancer
tags:
  - source
  - wgs
  - pangenome
  - gastric-cancer
  - structural-variants
---
# Gastric cancer genomics study using reference human pangenomes

_Life Science Alliance, published online 2025-01-27._  
DOI: [10.26508/lsa.202402977](https://doi.org/10.26508/lsa.202402977)

## Summary

Graph-based pangenome reference construction for gastric cancer WGS: the authors build a gastric-cancer graph pangenome (GGCPan) from 185 cases by embedding sample-derived structural variants (SVs) into GRCh38 and compare analysis outcomes across GRCh38, a linear pangenome (GCPan), and the graph pangenome (GGCPan). They report little difference for small variants/MSI, but a measurable advantage for SV identification when using the graph pangenome reference.

## Key Points

- Constructed a gastric-cancer graph pangenome (GGCPan) from 185 WGS cases by embedding SVs (>50 bp) into GRCh38 (merged set reported as 39,605 SVs across the cohort).
- Reported mapping-rate improvements vs GRCh38 when using pangenome references; graph anchoring is argued to reduce soft-clips/gaps compared with a linear pangenome with unanchored non-reference sequences.
- In a 5-sample SV simulation benchmark, SV-calling precision was similar across references, while recall improved with GGCPan (reported recall: GRCh38 71.28%, GCPan 61.02%, GGCPan 82.70%).
- Downstream driver discovery: 24 candidate gastric-cancer driver genes were detected across the three references (8 common; 5 detected only with pangenome-based analysis).

## Cancer Multiomics Project Relevance

- WGS 파이프라인에서 SV 신호가 중요한 경우(예: SV-derived neoantigen, gene fusion/amplicon 구조 해석), **reference bias / mapping ambiguity**를 줄이는 접근으로 pangenome 기반 reference가 어떤 이득을 주는지(특히 recall) 점검하는 레퍼런스로 활용 가능.
- 단, 본 과제의 핵심 축(인산화단백체/kinase network/치료반응 예측)과는 직접 연결성이 약하므로 Cancer Multiomics 100-paper 코퍼스의 “핵심”보다는 **WGS SV 보강** 관점의 주변 레퍼런스에 가깝다.


## Connections

- [Cancer Multiomics Literature Monitor](../topics/cancer-multiomics-literature.md)

## Sources

- Local PDF: `raw/inbox/papers/jiao-2025-gastric-cancer-reference-human-pangenomes.pdf`
- DOI: <https://doi.org/10.26508/lsa.202402977>
