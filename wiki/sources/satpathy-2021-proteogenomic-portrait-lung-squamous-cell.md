---
title: "A proteogenomic portrait of lung squamous cell carcinoma"
authors:
  - "Satpathy"
  - "Krug"
  - "Jean"
year: "2021"
journal: "Cell"
paper_kind: proteogenomic
pdf: "raw/inbox/papers/satpathy-2021-proteogenomic-portrait-lung-squamous-cell.pdf"
topic: ptmanchor
tags:
  - "ptmanchor"
  - "proteomics"
  - "ptm"
  - "phosphoproteomics"
  - "cancer-proteomics"
themes:
  - "ptm-correction"
  - "kinase-signaling"
  - "cancer-proteomics"
pmid: "34358469"
doi: "10.1016/j.cell.2021.07.016"
pmcid: "PMC8475722"

---
# A proteogenomic portrait of lung squamous cell carcinoma

_Cell, 2021._

## Summary

Lung squamous cell carcinoma (LSCC) remains a leading cause of cancer death with few therapeutic options. We characterized the proteogenomic landscape of LSCC, providing a deeper exposition of LSCC biology with potential therapeutic implications. We identify NSD3 as an alternative driver in FGFR1-amplified tumors and low-p63 tumors overexpressing the therapeutic target survivin. SOX2 is considered undruggable, but our analyses provide rationale for exploring chromatin modifiers such as LSD1 and EZH2 to target SOX2-overexpressing tumors. Our data support complex regulation of metabolic pathways by crosstalk between post-translational modifications including ubiquitylation. Numerous immune-related proteogenomic observations suggest directions for further investigation. Proteogenomic dissection of CDKN2A mutations argue for more nuanced assessment of RB1 protein expression and phosphorylation before declaring CDK4/6 inhibition unsuccessful. Finally, triangulation between LSCC, LUAD, and HNSCC identified both unique and common therapeutic vulnerabilities. These observations and proteogenomics data resources may guide research into the biology and treatment of LSCC.

## Key Points

- This paper contributes to the multi-omics/PTM atlas as a tumor/normal cohort.
- The extracted visualization fields are protein-scale, phosphorylation-scale, acetylation-scale, MS method, and instrument/platform.
- Count units are not harmonized when the paper reports different entities such as proteins, protein groups, phosphosites, phosphopeptides, acetylsites, or phospho-protein features.


## Multi-Omics Identification Extraction

This section was added for the interactive atlas on recent multi-omics proteomics/PTM identification scale. Values are taken from the local PDF and preserve the paper's own reporting unit.

- Cohort/scope: 108 tumors and 99 paired NATs.
- Proteome: 11,575 (quantified proteins; used for RNA–protein correlation across samples in Methods).
- Phosphoproteome: 68,674 (VM-site polished phosphosites).
- Acetylome: 15,186 (VM-site polished acetylsites).
- MS method: TMT-11; serial proteome/phosphoproteome/acetylproteome workflow; K-GG ubiquitylproteome subset.
- Instrument/platform: Q Exactive HF-X for proteome/acetylproteome; Orbitrap Fusion Lumos for phosphoproteome/ubiquitylproteome.
- Extraction evidence: STAR Methods: VM-site polishing yielded 68,674 phosphosites, 15,186 acetylsites, and 25,489 ubiquitylsites; Methods: RNA–protein correlation section names “global proteome with 11,575 quantified proteins”.
- Interpretation note: Figure S1B contains per-plex quantified protein bars, but the extracted PDF text did not expose a single global protein count.
- Follow-up needed: confirm whether the paper also reports a broader “identified proteins/protein groups” total distinct from the 11,575 quantified proteins.

## Cancer Multiomics Project Relevance

- Cancer Multiomics 과제의 “WGS–(phospho/acetyl/ubiquityl)proteome 통합” 축에서, **WGS/WES + multi-PTM + 면역 조절**을 한 코호트에서 동시에 다룬 대표적인 reference다.
- CDKN2A/RB1 축을 “유전 변이”만으로 단정하지 않고 **protein 및 phosphorylation 상태로 기능적으로 재평가**하는 논리는, Cancer Multiomics에서 반응/내성 feature를 설계할 때 직접 적용 가능하다.

## Connections

- [Ptmanchor Topic Hub](../topics/ptm-correction-and-kinase-signaling-in-cancer-proteomics.md)
- [Ptmanchor Anchor](../analyses/ptmanchor-manuscript-anchor.md)
- [Cancer Multiomics Literature Monitor](../topics/cancer-multiomics-literature.md)
- [Cancer Multiomics brief: Satpathy 2021](../analyses/cancer-multiomics-literature/satpathy-2021-proteogenomic-portrait-lung-squamous-cell.md)

## Sources

- Local PDF: `raw/inbox/papers/satpathy-2021-proteogenomic-portrait-lung-squamous-cell.pdf`
- PubMed: <https://pubmed.ncbi.nlm.nih.gov/34358469/>
- DOI: <https://doi.org/10.1016/j.cell.2021.07.016>
- PMC: <https://pmc.ncbi.nlm.nih.gov/articles/PMC8475722/>
