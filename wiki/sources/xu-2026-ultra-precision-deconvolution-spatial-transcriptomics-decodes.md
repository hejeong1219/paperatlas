---
title: "Ultra-precision deconvolution of spatial transcriptomics decodes immune heterogeneity and fate-defining programs in tissues"
authors:
  - "Xu"
  - "Huang"
  - "Zhang"
  - "Gong"
  - "Wang"
year: 2026
journal: "Nature communications"
doi: "10.1038/s41596-020-0292-x"
pmid: "41862467"
pmcid: "PMC13168514"
pdf: "raw/inbox/papers/xu-2026-ultra-precision-deconvolution-spatial-transcriptomics-decodes.pdf"
paper_kind: research
cancer_types:
  - "colorectal-cancer"
themes:
  - "spatial-omics"
  - "treatment-response"
topic: cancer-multiomics-literature
discovery_method: topic-sweep-2026-05-25
tags:
  - "cancer-multiomics-literature"
  - "nat-commun-2026"
  - "spatial-omics"
  - "topic-sweep"
  - "treatment-response"
batch_ingest_status: topic-sweep-stub
batch_ingested_on: 2026-05-25
---

# Ultra-precision deconvolution of spatial transcriptomics decodes immune heterogeneity and fate-defining programs in tissues

_Nat Commun, 2026._ [10.1038/s41596-020-0292-x](https://doi.org/10.1038/s41596-020-0292-x) · [PubMed 41862467](https://pubmed.ncbi.nlm.nih.gov/41862467/) · [PMC PMC13168514](https://pmc.ncbi.nlm.nih.gov/articles/PMC13168514/)

## Summary

Shannon entropy 기반 가중치를 사용하는 spatial transcriptomics deconvolution 알고리즘 UCASpatial을 제안하고, 인간 colorectal cancer (CRC)·생쥐 ear wound healing 모델에 적용한 방법론 논문입니다. Reference scRNA-seq에서 meta-purity로 cell identity-specific gene expression profile (cGEP)을 추출한 뒤 entropy weight로 식별력 높은 유전자를 강조하고 weighted NNLS로 spot 단위 cell composition을 추정해, SPOTlight·RCTD·cell2location·CARD·stereoscope·Spotiphy 등 6개 기존 method 대비 median RMSE 0.051(10~36% 개선) 성능을 보였습니다. CRC에서는 chr20q gain이 종양 내 HERV-H 발현 감소와 type I interferon response 손상을 매개해 T cell-excluded TIME과 연결됨을 도출했고, 생쥐 wound model에서는 IL11-IL11RA axis 차단이 pro-fibrotic community 형성을 줄이고 재생능을 개선함을 확인했습니다.

## Key Points

- UCASpatial은 cGEP 추출(meta-purity threshold + NMF) → Shannon entropy 기반 gene weighting → WNNLS deconvolution 3단계로 구성되며, Seurat framework에 통합되어 사용 가능합니다.
- Simulated ST 750 spot 벤치마크에서 median RMSE 0.051로 RCTD(0.058) 10%, SPOTlight(0.066) 21%, CARD/Spotiphy(0.075) 31%, cell2location(0.081) 36%, stereoscope(0.080) 35% 개선; F1 score는 모든 복잡도 구간에서 6~25% 우위였습니다.
- 20개 cell subpopulation reference 조건에서 fine-grained landscape 해독 우수성이 두드러졌으며, 5~20 cells per spot 범위에서 cell2location·stereoscope가 성능 저하를 보인 반면 UCASpatial은 robust했습니다.
- 인간 CRC 적용에서 spatial CNV inference와 결합해 T cell-rich vs T cell-excluded TIME 두 functional community를 정의했고, 종양세포 chr20q gain → HERV-H 발현 감소 → type I IFN response 손상 → T cell exclusion이라는 mechanism을 제시했습니다.
- 생쥐 MRL/B6 ear wound healing 모델에서 Igfbp5+ chondrocyte·Cd36+Gpnmb+Il1b- macrophage·Fmod+ fibroblast의 3-cell pro-fibrotic community를 발견하고, PPARγ agonist rosiglitazone 혹은 IL11-IL11RA 차단으로 fibrotic community 감소 및 재생능 개선을 검증했습니다.

## 한미암 활용 가능성

WGS-단백체 통합 측면에서, UCASpatial의 spatial deconvolution + spatial CNV (chr20q-gain → HERV-H → IFN response) 통합 워크플로는 위암 spatial transcriptomics 데이터에 적용해 driver CNV/structural variant가 TIME 표현형으로 이어지는 functional state를 mapping하는 데 참고할 수 있겠습니다. 또한 entropy-weighted gene 선택이 low-abundance immune subset에 강하다는 점은, 위암 spatial proteomics와 결합해 sparse한 TLS·TIL niche 정량화 시 검토해 볼 만합니다.

## Topic Sweep Ingest Status

- Status: `topic-sweep-stub` (2026-05-25)
- Topic: `cancer-multiomics-literature`
- Local PDF: `raw/inbox/papers/xu-2026-ultra-precision-deconvolution-spatial-transcriptomics-decodes.pdf`
- Download path: `europepmc-xml: https://europepmc.org/articles/PMC13168514?pdf=render`
- Extracted text length: 30013 characters
- Scope note: automated topic-sweep batch ingest; not yet a manual full-text deep-dive.

## Abstract (PubMed)

Elucidating the spatial organization and functional specialization of immune cells within complex tissues remains challenging. We present UCASpatial, an ultra-precision spatial transcriptomics deconvolution algorithm utilizing entropy-based weighting to accurately map cell subpopulations. Benchmarking confirms its superiority in identifying low-abundant cell subpopulations and distinguishing transcriptionally heterogeneous cell subpopulations. Applying UCASpatial to human colorectal cancer, we reveal that chromosome 20q gain in individual cancer clones orchestrates a T cell-excluded microenvironment, associated with HERV-H silencing and impaired type I interferon responses. In murine wound healing models, we reveal spatiotemporal dynamics distinguishing scarring from regenerative phenotypes. Specifically, we identify a pro-fibrotic community comprising Igfbp5+ chondrocytes, Cd36+ Gpnmb+ Il1b- macrophages, and Fmod+ fibroblasts in scarring-healing mice (C57BL/6). We further demonstrate that IL11-IL11RA signaling within this triad drives the pro-fibrotic community formation and limits regeneration. Together, UCASpatial serves as a versatile tool for deciphering fine-grained cellular landscapes and exploring intercellular mechanisms in complex and dynamic microenvironments.

## High-signal PDF head

```
Article                                                                                                   https://doi.org/10.1038/s41467-026-70645-3


                                    Ultra-precision deconvolution of spatial
                                    transcriptomics decodes immune
                                    heterogeneity and fate-deﬁning programs in
                                    tissues

                                    Received: 25 September 2025                             Yin Xu 1,2,3,7, Zurui Huang 1,2,3,7, Yawei Zhang1,2,3,7, Minghui Gong1,2,3,7,
                                                                                            Zhenghang Wang4,5,7, Peijin Guo6, Feifan Zhang1,2,3, Jing Yang 1,2,3,
                                    Accepted: 27 February 2026
                                                                                            Guanghao Liang1,2,3, Lihui Dong1,2,3, Renbao Chang1,2,3, Yu Xia6, Haochen Ni1,2,3,


1234567890():,;   1234567890():,;
                                                                                            Wenxuan Gong1,2,3, Boyuan Mei6, Yuan Gao1,3, Zhaoqi Liu 1,3, Lin Shen 4,
                                                                                            Jian Li 4, Meng Michelle Xu 6 & Dali Han 1,2,3
                                       Check for updates


                                                                                            Elucidating the spat
```

## Sources

- Local PDF: `raw/inbox/papers/xu-2026-ultra-precision-deconvolution-spatial-transcriptomics-decodes.pdf`
- DOI: <https://doi.org/10.1038/s41596-020-0292-x>
- PubMed: <https://pubmed.ncbi.nlm.nih.gov/41862467/>
- PMC: <https://pmc.ncbi.nlm.nih.gov/articles/PMC13168514/>
