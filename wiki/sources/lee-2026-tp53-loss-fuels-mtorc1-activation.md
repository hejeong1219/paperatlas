---
title: "TP53 Loss Fuels mTORC1 Activation and Autophagy Suppression to Drive Immune-Cold Colorectal Cancer."
year: "2026"
journal: "World journal of oncology"
doi: "10.14740/wjon2695"
pmid: "41822325"
pmcid: "PMC12978393"
paper_kind: "tumor or pan-cancer study"
pdf: "raw/inbox/papers/lee-2026-tp53-loss-fuels-mtorc1-activation.pdf"
topic: "multiomics-proteomics-ptm-identification"
tags:
  - "multiomics-proteomics-ptm-identification"
  - "local-pdf-ingest"
  - "cancer-proteomics"
  - "phosphoproteomics"
themes:
  - "multiomics-identification"
  - "ptm-methodology"
cm_axis: phospho
---
# TP53 Loss Fuels mTORC1 Activation and Autophagy Suppression to Drive Immune-Cold Colorectal Cancer.

## Summary

Local-PDF ingest note for the cancer multiomics/PTM atlas. Lee et al. reanalyze public colorectal cancer datasets (GSE146009 paired tumor/normal, TCGA-COAD/READ, GSE108989 single-cell T cells, CPTAC proteome and phosphoproteome) to test whether p53 deficiency is associated with coordinated mTORC1 activation, autophagy attenuation, and immune-cold remodeling, with a stated focus on microsatellite-stable (MSS) disease. As TP53 dysfunction increases (wild type → missense → null), p53–mTORC1 pathway coupling weakens, FOXP3 rises, and the CD8A/FOXP3 ratio falls. p53-low tumors show higher phosphorylation of mTOR output sites (EIF4EBP2 S65, RPS6KB1 T421/S424) and lower phosphorylation of inhibitory RPTOR sites. The study is retrospective and correlational. The authors propose biomarker-guided TORC1/2 inhibition combined with PD-1/PD-L1 (± CTLA-4) blockade in TP53-deficient MSS CRC as a hypothesis for future trials.

## Key Points

- Atlas classification: tumor or pan-cancer study.
- Quantitative atlas row: candidate.
- Claims in this page were extracted from the local PDF text; web pages were not used as evidence.
- Cohorts (all public):
  - GSE146009: discovery; 24 paired tumor/adjacent normal, bulk RNA-seq.
  - TCGA-COAD/READ: validation; n = 647 (TP53 wild type 258, missense 287, null/loss-of-function 102).
  - GSE108989: 11,138 tumor-infiltrating T cells from 12 patients.
  - CPTAC–TCGA matched proteome PDC000111: n = 95.
  - CPTAC2 colon/rectal phosphoproteome PDC000116–000117: n = 234.
  - Pathway activity was scored by ssGSEA. CPTAC tumors were split by TP53 mutation status or by p53 protein abundance at the cohort median.
- Discovery cohort:
  - mTORC1 activity correlated with TNF-α/NF-κB (r = 0.35) and inversely with autophagy (r = −0.37).
  - mTORC1 activity also correlated with IL1B (r = 0.45, P = 0.027) and IL8 (r = 0.53, P = 0.007).
  - FOXP3, CTLA4, and CD274 were higher in tumors while CD8A was unchanged, so the CD8A/FOXP3 ratio was lower in tumor than in normal tissue (1.06 ± 0.12 vs 1.34 ± 0.17; P < 0.01).
- TCGA:
  - p53-pathway–mTORC1 coupling weakened from wild type (r = 0.50) to missense (r = 0.43) and was lost in null tumors (r = −0.05).
  - In null tumors, mTORC1 instead correlated with IFNG (r = 0.28, P = 0.0045).
  - FOXP3 rose stepwise across classes (Kruskal–Wallis P = 0.005) while CD8A stayed stable, and the CD8A/FOXP3 ratio declined (1.28 → 1.11 → 0.96; P = 4.7 × 10⁻⁵).
- Single cell: Tregs had the highest combined mTORC1, autophagy, and IFN-γ-response activity. CD8_exh cells had uniformly low pathway activity.
- Proteome/phosphoproteome:
  - TP53-mutant tumors had higher EIF4EBP2 (log2FC +5.98, FDR 0.07) and lower SQSTM1/p62 (−3.07, FDR 0.30). The authors note that not all proteome differences survived FDR correction and rely on consistent directionality.
  - p53-low tumors had higher EIF4EBP2 S65 (+1.12) and RPS6KB1 T421/S424 (+1.57) phosphorylation.
  - The same tumors had lower phosphorylation of the inhibitory RPTOR sites S705 (−0.60), T725 (−1.36), and S726 (−1.65).
  - Phosphosites were called on consistent directionality, effect size (log2FC > 0.5), and nominal significance.
- Limitations stated by the authors:
  - The study is retrospective and hypothesis-generating, and its associations do not establish causality.
  - Functional validation in experimental models is still needed.
  - Stromal, myeloid, and microbiome factors may also shape the immunometabolic state.
- Evidence scope (inferred from the listed data sources, not stated by the authors): no analyzed cohort carries immune-checkpoint-inhibitor treatment or response data.

## Multi-Omics Identification Extraction

- Cohort/scope: Colorectal cancer; classification `tumor or pan-cancer study`.
- Proteome count candidate: not confidently extracted from main PDF text.
- Phosphoproteome count candidate: not confidently extracted from main PDF text.
- Acetylome count candidate: not confidently extracted from main PDF text.
- Method/instrument evidence from local PDF:
  - Method/instrument phrases were not confidently exposed in the extractable main PDF text.
- Count evidence snippets from local PDF:
  - Pathway activities were quantified us- PD-1/PD-L1 blockade in MSS disease, underscoring the clini- ing single-sample gene set enrichment analysis (ssGSEA) im- cal relevance of this pathway in immune-refractory CRC.
  - Expression data were hypothesis that p53 deficiency is linked to persistent mTORC1 log-normalized and scaled; variable genes were identified with activation, relative autophagy suppression, and development of FindVariableFeatures().
  - Phosphosites-level differences cells isolated from 12 CRC patients.
  - Phosphosites were considered biologically relevant therefore exempt from institutional review board approval.
  - In contrast, TP53-null tumors demonstrated a positive Institutional Review Board (IRB) approval correlation between mTORC1 and IFNG expression (r = 0.28, P = 0.0045), accompanied by loss of autophagy-cytokine coupling This study analyzed de-identified, publicly accessible human (Fig.
- Interpretation note: preserve the reported unit; do not convert protein groups, phosphosites, phosphopeptides, acetylsites, and phosphoproteins into a false common metric.

## 한미암 활용 가능성

- TP53 기능 소실 정도(wild-type → missense → null)에 따라 CD8A/FOXP3 비가 단계적으로 낮아진다. p53 저발현 종양에서는 EIF4EBP2 S65·RPS6KB1 T421/S424 인산화가 높고 RPTOR 억제 site 인산화가 낮다. 이 두 관찰은 한미암 면역치료제 1차 내성 분석의 가설 축이 될 수 있다. 무반응군에서 WGS상 TP53 null 변이와 이들 mTORC1 출력 phosphosite 상승이 함께 나타나는지 반응군과 비교해보면, 저자들이 제안한 TORC1/2 억제제 + PD-1/PD-L1 차단 병용 가설을 위암 맥락에서 가늠해볼 수 있다.
- TP53을 변이 유무로만 나누지 않고 missense와 null로 구분하자 p53–mTORC1 coupling(r = 0.50 → 0.43 → −0.05)과 면역 지표가 단계적으로 달라졌다. 한미암 WGS 변이 annotation에서 TP53 변이를 기능 유형별로 나눠 phospho·면역 지표와 연결해볼 근거로 참고할 만하다.
- 근거 범위:
  - 공개 데이터(TCGA·CPTAC·GEO) 재분석에서 나온 상관 관찰이며, 인과는 확인되지 않았다(저자 명시).
  - proteome 차이 중 일부는 FDR 보정 후 유의하지 않다(EIF4EBP2 FDR 0.07). phosphosite는 방향 일관성·효과 크기·nominal 유의성을 기준으로 골랐다.
  - 분석 코호트에 면역관문억제제 치료·반응 데이터가 없다.
  - 저자들은 MSS 초점을 내세우지만, Methods에 MSI 상태로 코호트를 거른 절차는 기술되어 있지 않다.
  - 대장암 데이터이므로 위암으로의 연결은 가설이다.
- Slack 디지스트 게시: 2026-09-30.

## Connections

- [Multiomics Proteomics PTM Identification](../topics/multiomics-proteomics-ptm-identification.md)
- [Multiomics PTM Corpus Queue](../analyses/multiomics-ptm-corpus-queue.md)
- [Immunotherapy Resistance and Immune Evasion](../topics/immunotherapy-resistance-and-immune-evasion.md)

## Sources

- Local PDF: `raw/inbox/papers/lee-2026-tp53-loss-fuels-mtorc1-activation.pdf`
- PubMed: <https://pubmed.ncbi.nlm.nih.gov/41822325/>
- DOI: <https://doi.org/10.14740/wjon2695>
- PMC: <https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12978393/>
