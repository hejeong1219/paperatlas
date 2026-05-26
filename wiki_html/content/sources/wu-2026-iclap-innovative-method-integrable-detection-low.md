---
title: "iCLAP: an innovative method for integrable co-detection of low-abundance antigens with high-plex immunostaining"
authors:
  - "Wu"
  - "Zheng"
  - "Chen"
  - "Ye"
  - "Kim"
year: 2026
journal: "Nature communications"
doi: "10.1038/s41551-017-0093"
pmid: "41735278"
pmcid: "PMC6675017"
pdf: "raw/inbox/papers/wu-2026-iclap-innovative-method-integrable-detection-low.pdf"
paper_kind: computational
cancer_types:
  - "pancreatic-cancer"
themes:
  - "spatial-omics"
topic: cancer-multiomics-literature
discovery_method: topic-sweep-2026-05-25
tags:
  - "cancer-multiomics-literature"
  - "nat-commun-2026"
  - "spatial-omics"
  - "topic-sweep"
batch_ingest_status: topic-sweep-stub
batch_ingested_on: 2026-05-25
---

# iCLAP: an innovative method for integrable co-detection of low-abundance antigens with high-plex immunostaining

_Nat Commun, 2026._ [10.1038/s41551-017-0093](https://doi.org/10.1038/s41551-017-0093) · [PubMed 41735278](https://pubmed.ncbi.nlm.nih.gov/41735278/) · [PMC PMC6675017](https://pmc.ncbi.nlm.nih.gov/articles/PMC6675017/)

## Summary

FFPE 조직에서 low-abundance protein (예: senescence marker, transcription factor, secreted protein)을 high-plex spatial proteomics에 통합 검출할 수 있는 신규 방법 iCLAP (integrable Co-detection of Low-Abundant Proteins)을 제안한 방법론 논문입니다. iCLAP은 iterative signal amplification (TSA 기반)과 효율적 fluorophore inactivation을 결합해 동일 조직 절편을 반복 staining할 수 있고, IMC·CyCIF·CODEX 등 기존 multiplex imaging 플랫폼과 seamless하게 통합되어 40개 이상 marker 프로파일링을 달성합니다. 인간 췌장 조직에 적용해 tissue compartment별로 공간적으로 구분되는 senescence-associated protein 패턴을 발견했습니다.

## Key Points

- iCLAP은 tyramide signal amplification (TSA) 기반 enzymatic deposition으로 형광 신호를 증폭하고 fluorophore inactivation 단계를 결합해, FFPE 절편을 반복 staining함으로써 40개 이상 marker 통합 검출이 가능합니다.
- 기존 high-plex method (CODEX, CyCIF, IMC, 4i)는 detection limit으로 인해 highly expressed protein 위주로 제한되었고, 기존 TSA-based approach는 절편당 8개 marker 이하라는 한계가 있었음을 정리합니다.
- iCLAP는 IMC, CyCIF, CODEX 등 기존 플랫폼에 plug-in 가능한 modular 설계로, 기존 워크플로 자산을 유지하며 low-abundance protein 검출 capability를 확장합니다.
- 인간 췌장 FFPE 시료 적용을 통해 tissue compartment별 공간적으로 구분되는 senescence-associated protein 패턴을 시연했습니다.
- 결과적으로 iCLAP는 transcription factor·secreted factor·senescence marker 같은 기존에는 in situ로 검출하기 어려웠던 단백질을 spatial proteomics에 통합해 분석할 수 있는 새로운 자원을 제공합니다.

## 한미암 활용 가능성

WGS-단백체 통합 및 인산화단백체/kinase 측면에서, iCLAP의 low-abundance protein high-plex 검출 capability는 위암 FFPE 조직에서 kinase·transcription factor·secreted ligand 등 mass spec에서도 정량이 까다로운 단백질을 spatial context와 함께 검출하는 데 검토해 볼 만합니다. 또한 senescence marker 패턴 시연은 위암 chemotherapy 후 therapy-induced senescence (TIS) niche를 spatial proteomics로 매핑하는 데 참고할 수 있겠습니다.

## Topic Sweep Ingest Status

- Status: `topic-sweep-stub` (2026-05-25)
- Topic: `cancer-multiomics-literature`
- Local PDF: `raw/inbox/papers/wu-2026-iclap-innovative-method-integrable-detection-low.pdf`
- Download path: `europepmc-xml: https://europepmc.org/articles/PMC13039418?pdf=render`
- Extracted text length: 30013 characters
- Scope note: automated topic-sweep batch ingest; not yet a manual full-text deep-dive.

## Abstract (PubMed)

Multiplexed protein imaging enables spatial analysis of complex tissues, but detecting proteins expressed at low levels remains challenging, particularly in widely available formalin-fixed, paraffin-embedded (FFPE) specimens. Many biologically important regulators-including senescence markers, transcription factors, and secreted proteins-are therefore difficult to study in situ using existing high-plex methods. Here we show that integrable Co-detection of Low-Abundant Proteins (iCLAP) enables sensitive and highly multiplexed protein detection within the same FFPE tissue section. iCLAP combines iterative signal amplification with efficient fluorophore inactivation, enabling repeated staining of the same tissue section and seamless integration with established multiplex imaging platforms to achieve profiling of more than 40 markers. Application of iCLAP to human pancreatic tissues revealed spatially distinct senescence-associated protein patterns across tissue compartments. Together, iCLAP expands the analytical capabilities of FFPE tissues, enabling high-sensitivity, high-dimensional spatial proteomic studies of complex biological processes.

## High-signal PDF head

```
Article                                                                                                   https://doi.org/10.1038/s41467-026-69752-y


                                    iCLAP: an innovative method for integrable
                                    co-detection of low-abundance antigens with
                                    high-plex immunostaining
                                    Received: 26 April 2025                             Fan Wu 1,2, Shuyuan Zheng1, Yani Chen1, Peijia Ye3, Moo Joong Kim1, Seojin Lee1,
                                                                                        Geroge Kuo4, Shriya Pillan1, Ruihan Yuan 3, Kyu Sang Han1, Bofei Yu3,
                                    Accepted: 9 February 2026
                                                                                        Qingfeng Zhu 5,6, Sarah M. Shin 5, Courtney D. Cannon5, Gabriele Pierre1,
                                                                                        Kanako Iwasaki 7, Cristina Aguayo-Mazzucato 7, Nicolas Musi8,
                                                                                        George A. Kuchel 9, Birgit Schilling 10, Laura D. Wood11, Won Jin Ho 5,
                                        Check for updates                               Robert A. Anders5,6, Denis Wirtz 1,2,3,5,11,12 & Pei-Hsun Wu 1,2

1234567890():,;   1234567890():,;

                                                                               
```

## Sources

- Local PDF: `raw/inbox/papers/wu-2026-iclap-innovative-method-integrable-detection-low.pdf`
- DOI: <https://doi.org/10.1038/s41551-017-0093>
- PubMed: <https://pubmed.ncbi.nlm.nih.gov/41735278/>
- PMC: <https://pmc.ncbi.nlm.nih.gov/articles/PMC6675017/>
