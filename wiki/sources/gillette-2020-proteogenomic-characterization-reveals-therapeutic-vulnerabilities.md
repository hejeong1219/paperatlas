---
title: "Proteogenomic Characterization Reveals Therapeutic Vulnerabilities in Lung Adenocarcinoma"
authors:
  - "Gillette"
  - "Satpathy"
  - "Cao"
year: "2020"
journal: "Cell"
paper_kind: resource
cancer_types:
  - lung-adenocarcinoma
modalities:
  - proteogenomics
  - phosphoproteomics
  - acetylproteomics
pdf: "raw/inbox/papers/gillette-2020-proteogenomic-characterization-reveals-therapeutic-vulnerabilities.pdf"
topic: ptmanchor
tags:
  - "source"
  - "ptmanchor"
  - "proteomics"
  - "ptm"
  - "phosphoproteomics"
  - "cancer-proteomics"
themes:
  - "ptm-correction"
  - "kinase-signaling"
  - "cancer-proteomics"
pmid: "32649874"
doi: "10.1016/j.cell.2020.06.013"
pmcid: "PMC7373300"

---
# Proteogenomic Characterization Reveals Therapeutic Vulnerabilities in Lung Adenocarcinoma

_Cell, 2020._

## Summary

To explore the biology of lung adenocarcinoma (LUAD) and identify new therapeutic opportunities, we performed comprehensive proteogenomic characterization of 110 tumors and 101 matched normal adjacent tissues (NATs) incorporating genomics, epigenomics, deep-scale proteomics, phosphoproteomics, and acetylproteomics. Multi-omics clustering revealed four subgroups defined by key driver mutations, country, and gender. Proteomic and phosphoproteomic data illuminated biology downstream of copy number aberrations, somatic mutations, and fusions and identified therapeutic vulnerabilities associated with driver events involving KRAS, EGFR, and ALK. Immune subtyping revealed a complex landscape, reinforced the association of STK11 with immune-cold behavior, and underscored a potential immunosuppressive role of neutrophil degranulation. Smoking-associated LUADs showed correlation with other environmental exposure signatures and a field effect in NATs. Matched NATs allowed identification of differentially expressed proteins with potential diagnostic and therapeutic utility. This proteogenomics dataset represents a unique public resource for researchers and clinicians seeking to better understand and treat lung adenocarcinomas.

## Key Points

- CPTAC-style LUAD cohort (tumor + NAT)에서 **driver event(KRAS/EGFR/ALK, CNAs, fusions)**가 proteome/phosphoproteome 기능 상태로 어떻게 번역되는지 “측정 기반”으로 보여주는 대표 리소스.
- Multi-omics clustering으로 **4개 subgroup**을 제시하고, immune subtyping에서 **STK11과 immune-cold**의 연관을 재강조한다.
- NAT를 포함해 “field effect”와 진단/치료 타깃 후보 단백질을 같이 다룬다(종양만으로는 놓치기 쉬운 대비 구조).


## Multi-Omics Identification Extraction

This section was added for the interactive atlas on recent multi-omics proteomics/PTM identification scale. Values are taken from the local PDF and preserve the paper's own reporting unit.

- Cohort/scope: 110 tumors and 101 matched normal adjacent tissues.
- Proteome: 10,165 (filtered protein features used for tumor-NAT PCA).
- Phosphoproteome: 65,103 (VM-site polished phosphosites).
- Acetylome: 13,480 (VM-site polished acetylsites).
- MS method: TMT-10; global proteome, IMAC phosphoproteome, acetylproteome; Spectrum Mill processing.
- Instrument/platform: Q Exactive HF-X for proteome; Orbitrap Fusion Lumos for phosphoproteome and acetylproteome.
- Extraction evidence: STAR Methods: VM-site polishing yielded 65,103 phosphosites and 13,480 acetylsites; tumor-NAT PCA used 10,165 proteins, 40,845 phosphosites, and 6,984 acetylsites.
- Interpretation note: Protein count is the filtered analysis feature count visible in extracted text, not necessarily the total raw protein identification count.

## Cancer Multiomics Project Relevance

- Cancer Multiomics 과제의 “WGS만으로 설명되지 않는 반응/내성”을 설명할 때, LUAD에서 driver→protein/PTM 기능 상태로의 translation을 **phosphoproteome layer**까지 포함해 보여주는 reference 데이터셋이다.
- STK11 immune-cold, neutrophil degranulation 같은 immune axis를 proteogenomics로 관찰하는 구성이 **WGS-derived immune feature + phosphoproteome** 결합 분석 설계에 직접 도움이 된다.

## Connections

- [Multiomics Proteomics PTM Identification](../topics/multiomics-proteomics-ptm-identification.md)

- [Ptmanchor Topic Hub](../topics/ptm-correction-and-kinase-signaling-in-cancer-proteomics.md)
- [Ptmanchor Anchor](../analyses/ptmanchor-manuscript-anchor.md)
- [Cancer Multiomics Literature Monitor](../topics/cancer-multiomics-literature.md)
- [Gillette 2020 - LUAD CPTAC Proteogenomics (Tumor+NAT; Phospho+Acetyl)](../analyses/cancer-multiomics-literature/gillette-2020-proteogenomic-characterization-reveals-therapeutic-vulnerabilities.md)

## Sources

- Local PDF: `raw/inbox/papers/gillette-2020-proteogenomic-characterization-reveals-therapeutic-vulnerabilities.pdf`
