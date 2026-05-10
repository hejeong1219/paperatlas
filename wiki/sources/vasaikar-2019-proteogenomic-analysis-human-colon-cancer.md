---
title: "Proteogenomic Analysis of Human Colon Cancer Reveals New Therapeutic Opportunities"
authors:
  - "Vasaikar"
  - "Huang"
  - "Wang"
year: "2019"
journal: "Cell"
paper_kind: proteogenomic
pdf: "raw/inbox/papers/vasaikar-2019-proteogenomic-analysis-human-colon-cancer.pdf"
topic: ptmanchor
tags:
  - "ptmanchor"
  - "multiomics-proteomics-ptm-identification"
  - "proteomics"
  - "ptm"
  - "phosphoproteomics"
  - "cancer-proteomics"
themes:
  - "ptm-correction"
  - "kinase-signaling"
  - "cancer-proteomics"
pmid: "31031003"
doi: "10.1016/j.cell.2019.03.030"
pmcid: "PMC6768830"

---
# Proteogenomic Analysis of Human Colon Cancer Reveals New Therapeutic Opportunities

_Cell, 2019._

## Summary

We performed the first proteogenomic study on a prospectively collected colon cancer cohort. Comparative proteomic and phosphoproteomic analysis of paired tumor and normal adjacent tissues produced a catalog of colon cancer-associated proteins and phosphosites, including known and putative new biomarkers, drug targets, and cancer/testis antigens. Proteogenomic integration not only prioritized genomically inferred targets, such as copy-number drivers and mutation-derived neoantigens, but also yielded novel findings. Phosphoproteomics data associated Rb phosphorylation with increased proliferation and decreased apoptosis in colon cancer, which explains why this classical tumor suppressor is amplified in colon tumors and suggests a rationale for targeting Rb phosphorylation in colon cancer. Proteomics identified an association between decreased CD8 T cell infiltration and increased glycolysis in microsatellite instability-high (MSI-H) tumors, suggesting glycolysis as a potential target to overcome the resistance of MSI-H tumors to immune checkpoint blockade. Proteogenomics presents new avenues for biological discoveries and therapeutic development.

## Key Points

- Cohort: 110명의 colon cancer에서 tumor, matched NAT, blood를 전향적으로 수집하고, tumor는 WXS/CNV/RNA-seq/miRNA-seq 및 label-free proteomics를 수행했으며, tumor+NAT에 대해 TMT 기반 global proteome + phosphoproteome을 추가로 측정했다.
- Neoantigen/항원 후보: WXS/RNA 기반 HLA typing(OptiType)과 HLA binding 예측(netMHCpan)을 결합해 변이 펩타이드 후보를 생성하고, proteomics에서 관측된 변이 펩타이드 중 고결합(예: IC50 < 150 nM) 88개를 putative neoantigen으로 정리했으며, 환자의 38%에서 ≥1개 후보가 관측되었다(Table S6).
- “MSS에서 공공 항원 후보” 축: MSI-H 중심의 patient-specific neoantigen과 별개로, CT antigen(비변이) 과발현 후보를 제시해 MSS에서 checkpoint/neoantigen 전략의 빈틈을 메우는 항원 후보 프레임을 제공한다.
- Phospho-driven therapeutic hypothesis: phosphoproteomics가 Rb phosphorylation 증가를 proliferation↑/apoptosis↓와 연결하며, CDK2–Rb 축을 “표적 가능”한 oncogenic driver로 제안한다.
- MSI-H 면역 회피의 대안적 레버: MSI subtype에서 glycolysis↑가 CD8 infiltration/activation과 역상관되는 패턴을 제시하며, glycolysis inhibition이 MSI-H ICI 내성 우회 전략 후보가 될 수 있음을 논의한다.

## Multi-Omics Identification Extraction

- Cohort / scope: prospective colon cancer cohort with matched tumor and normal adjacent tissues.
- Proteome: TMT global proteomic analysis identified 8,067 proteins; 6,422 proteins were quantified in at least 50% of samples.
- Phosphoproteome: 7,295 phosphorylation sites were quantified in at least 50% of samples. The PDF text also reports 63 cancer-associated phosphosites mapping to 50 proteins after differential filtering.
- Acetylome: not reported as a separate acetylome layer in the extracted PDF text.
- MS method: TMT 10-plex global proteome and phosphoproteome profiling; phosphoproteome analyzed at phosphopeptide/site level after enrichment.
- Instrument / platform: Q Exactive Plus for TMT global proteome; Orbitrap Fusion Lumos for TMT phosphoproteome; nanoACQUITY UPLC for phosphoproteome separations.
- Extraction evidence: local PDF Results and STAR Methods sections report the 8,067 protein groups, 6,422 quantifiable proteins, 7,295 phosphorylation sites, TMT 10 labeling, Q Exactive Plus, and Orbitrap Fusion Lumos details.
- Interpretation note: this is proteome/phosphoproteome only for the requested atlas; acetylome should remain blank rather than inferred from N-terminal acetylation search settings.

## Open Questions

- Proteomics-supported neoantigen(변이 펩타이드 관측) 정의는 “MS에서 변이 펩타이드 동정”인지 “변이 유래 protein evidence”까지 포함하는지, 그리고 해당 FDR/필터는 무엇인가?
- CT antigen 후보는 tumor–NAT fold-change 외에 정상 조직 발현(잠재 독성) 또는 면역원성 근거가 있는가?

## Connections

- [Multiomics Proteomics PTM Identification](../topics/multiomics-proteomics-ptm-identification.md)

- [Ptmanchor Topic Hub](../topics/ptm-correction-and-kinase-signaling-in-cancer-proteomics.md)
- [Ptmanchor Anchor](../analyses/ptmanchor-manuscript-anchor.md)

## Sources

- Local PDF: `raw/inbox/papers/vasaikar-2019-proteogenomic-analysis-human-colon-cancer.pdf`
