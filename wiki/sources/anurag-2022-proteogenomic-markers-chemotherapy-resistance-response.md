---
title: "Proteogenomic Markers of Chemotherapy Resistance and Response in Triple-Negative Breast Cancer"
authors:
  - "Anurag"
year: 2022
journal: "Cancer Discovery"
doi: "10.1158/2159-8290.CD-22-0200"
paper_kind: proteogenomic
pdf: "raw/inbox/papers/anurag-2022-proteogenomic-markers-chemotherapy-resistance-response.pdf"
topic: "multiomics-proteomics-ptm-identification"
extra_topics:
  - "cancer-multiomics"
tags:
  - "multiomics-proteomics-ptm-identification"
  - "local-pdf-ingest"
  - "cancer-proteomics"
  - "phosphoproteomics"
  - "cancer-multiomics"
themes:
  - "multiomics-identification"
  - "ptm-methodology"
batch_ingest_status: pdf-text-extracted
batch_ingested_on: 2026-05-13
ingest_status: full-text-read
ingested_on: 2026-05-13
---
# Proteogenomic Markers of Chemotherapy Resistance and Response in Triple-Negative Breast Cancer

## Summary

Pretreatment TNBC biopsies from neoadjuvant carboplatin + docetaxel trials are profiled with WES, RNA-seq, and TMT-based proteomics/phosphoproteomics to identify multi-omic features associated with pathologic complete response (pCR) versus non-response. The study reports response-linked pathway programs (cell-cycle/DNA-repair/immune features) and highlights a resistance-associated 19q13.31–33 deletion (including LIG1/POLD1/XRCC1) connected to genomic instability and poorer outcomes.

## Full PDF Deep-Dive Status

- Status: `full-text-read` on 2026-05-13.
- Local PDF checked end-to-end: `raw/inbox/papers/anurag-2022-proteogenomic-markers-chemotherapy-resistance-response.pdf` (20 pages).
- Evidence scope: main text, figure legends, Methods, Data Availability, and model-system validation were re-read from the local PDF. Supplementary tables were not locally re-extracted in this pass.
- POC priority: high. This is a direct template for matched **somatic genomics + global proteome + phosphoproteome + clinical response** analysis.

## Batch PDF Ingest Status

- Status: `pdf-text-extracted` on 2026-05-13; superseded by `full-text-read` promotion above.
- Local PDF: `raw/inbox/papers/anurag-2022-proteogenomic-markers-chemotherapy-resistance-response.pdf`.
- Extracted text length: 35,731 characters.
- Scope note: automated local-PDF text ingest for the 100-paper drug-response/phospho-global batch, retained as provenance for the batch script.
- Evidence boundary: downstream scientific claims should now rely on the `Full PDF Deep-Dive Status`, `Key Points`, and `Detailed Evidence` sections rather than the automated snippets below.
- High-signal PDF snippets:
  - RESEARCH ARTICLE Proteogenomic Markers of Chemotherapy Resistance and Response in Triple-Negative Breast Cancer Downloaded from http://aacrjournals.org/cancerdiscovery/article-pdf/12/11/2586/3218265/2586.pdf by Korea University Medical Library user on 27 April 2026 Meenakshi Anurag1, Eric J.
  - Ellis1 ABSTRACT Microscaled proteogenomics was deployed to probe the molecular basis for dif- ferential response to neoadjuvant carboplatin and docetaxel combination chemo- therapy for triple-negative breast cancer (TNBC).
  - Proteomic analyses of pretreatment patient biopsies uniquely revealed metabolic pathways, including oxidative phosphorylation, adipogenesis, and fatty acid metabolism, that were associated with resistance.
  - Both proteomics and transcriptomics revealed that sensitivity was marked by elevation of DNA repair, E2F targets, G2–M checkpoint, interferon- gamma signaling, and immune-checkpoint components.
  - Proteogenomic analyses of somatic copy- number aberrations identified a resistance-associated 19q13.31–33 deletion where LIG1, POLD1, and XRCC1 are located.

## Key Points

- Cohort/setting: pretreatment TNBC biopsies from neoadjuvant carboplatin + docetaxel clinical trials, analyzed with pCR/RCB outcomes.
- Data layers: WES (~100x), RNA-seq, and quantitative TMT global proteomics + phosphoproteomics from the same biopsy material using BioTEXT/microscaled proteogenomics.
- Qualified baseline cohort: 59 patients after tumor-content filtering, with 22 pCR and 37 non-pCR cases; pCR and RCB were the primary response endpoints.
- Omics scale: the main PDF reports 11,063 proteins, 20,861 mRNAs, 25,242 SCNAs, and 26,919 phosphorylation sites on 5,041 phosphoproteins.
- Response-linked biology: pCR-associated tumors showed immune/IFN, E2F, G2-M checkpoint, and DNA-repair programs; non-pCR tumors showed proteome-level oxidative phosphorylation, fatty-acid metabolism, adipogenesis, and glycolysis signals.
- Phosphoproteome signal: PTM-SEA showed higher DNA damage / cell-cycle kinase target signatures in pCR tumors (including CDK1/2/7, CDC7, PRKDC/DNA-PK), while MARK2 targets were enriched in non-pCR tumors.
- Immune response nuance: PD-L1 RNA/protein/phosphoprotein levels and protein-based immune stimulatory scores were higher in pCR tumors, but nonsynonymous mutation load was not associated with pCR or immune scores.
- Genomic marker candidate: a resistance-associated 19q13.31-33 deletion lowered LIG1/POLD1/XRCC1-related DNA repair/replication proteins and was connected to carboplatin-selective resistance, higher CIN, lower HRD signature 3, and poorer outcomes in external/orthogonal contexts.
- Model-system validation: longitudinal PDXs from one patient showed progressive LIG1 loss from pretreatment primary to post-treatment/metastatic models; the LIG1-high model was carboplatin-sensitive, whereas LIG1-low models were carboplatin-insensitive.

## Multi-Omics Identification Extraction

- Cohort/scope: TNBC pretreatment biopsies from neoadjuvant carboplatin + docetaxel trials (clinical response-labeled cohort).
- Proteome count cue (PDF text): protein layer references ~11,063 proteins.
- Phosphoproteome count cue (PDF text): phosphoproteomic layer references ~27,000 phosphorylation sites across ~5,000 phosphoproteins.
- Acetylome count candidate: not confidently extracted from main PDF text.
- Method/instrument evidence from local PDF:
  - Genes Downloaded from http://aacrjournals.org/cancerdiscovery/article-pdf/12/11/2586/3218265/2586.pdf by Korea University Medical Library user on 27 April 2026 exome DNA sequencing (WES), RNA sequencing (RNA-seq), with lower correlations were enriched in pathways containing and tandem mass tag (TMT)–based proteomics and phos- large protein complexes servi...
  - (100×), RNA-seq, and quantitative, multiplexed (TMT) mass Expected associations for pCR with germline mutations in spectrometry (MS)–based proteomics and phosphoproteomics the homologous recombination genes BRCA1/2 and PALB2 (Fig.
  - TMT11 with high RCB (II or III; P = 0.03; Supplementary Fig.
  - (interferon alpha and gamma response) and cell cycle (G2–M 2588 | CANCER DISCOVERY NOVEMBER 2022 AACRJournals.org Proteogenomic Markers of Chemotherapy Resistance in TNBC RESEARCH ARTICLE A NCT02124902 (WashU) and B NCT02547987 (BCM) pCR (N = 22) Non-pCR (N = 37) Treatment = Docetaxel + Carboplatin RCB Patients enrolled in trial Race Mutation N = 87 patie...
  - Mutation and copy-number data were derived from WES and RNA from RNA-seq, and protein data were obtained from TMT proteomics generated by this current study.
- Count evidence snippets from local PDF:
  - Proteogenomic analyses of somatic copy- number aberrations identified a resistance-associated 19q13.31–33 deletion where LIG1, POLD1, and XRCC1 are located.
  - Sets of phosphosites induced by treatment chemotherapy (NCT02547987 and NCT02124902).
  - 1E; phosphoproteomic analysis quantified ∼27,000 phospho- Supplementary Table S6).
  - In contrast, immune signaling rylation sites in ∼5,000 distinct phosphoproteins (Fig.
  - baseline MYC TARGETS V1 MYC TARGETS V2 E2F TARGETS G2M CHECKPOINT 4 FATTY ACID METABOLISM C MITOTIC SPINDLE Signed −log10 (FDR) from 1,745 OXIDATIVE PHOSPHORYLATION MTORC1 SIGNALING 177 2 PI3K AKT MTOR SIGNALING UNFOLDED PROTEIN RESPONSE Protein (11,063) ADIPOGENESIS GLYCOLYSIS 6,091 0 APICAL JUNCTION Phosphoprotein NOTCH SIGNALING GSEA based on different...
- Interpretation note: preserve the reported unit; do not convert protein groups, phosphosites, phosphopeptides, acetylsites, and phosphoproteins into a false common metric.

## Analysis Pattern To Reuse

For the user's global proteome + phosphoproteome + somatic SNV drug-response proof of concept, this paper suggests a concrete, manuscript-ready ladder:

1. Freeze response labels first: pCR/non-pCR or ordered RCB class.
2. Keep genomics honest: if only somatic SNV is available, explicitly label the genomics block as SNV-only because this paper's strongest genomic predictor was SCNA, not point mutation.
3. Build feature blocks in this order: clinical/tumor-content/batch covariates; SNV/signature features; global proteome pathway scores; phosphosite/PTM-SEA or kinase activity scores.
4. Compare RNA/protein/phosphosite pathway signals side-by-side rather than assuming transcript abundance captures metabolic or kinase activity states.
5. Use pathway-level biology for the first figure, then nominate a compact resistance axis such as DNA repair, metabolism, immune signaling, or kinase activity.
6. Add case-level vignettes where genomics and proteomics disagree; Anurag 2022 is especially useful because mutation burden did not explain immune/pCR states, while protein/phosphoprotein layers did.

## Detailed Evidence

### Cohort and Processing

- Patients had clinical stage II/III ER-negative, HER2-negative TNBC and received six cycles of neoadjuvant docetaxel plus carboplatin.
- Baseline research biopsies were collected before chemotherapy; optional on-treatment biopsies were collected at cycle 1 day 3.
- OCT-embedded frozen core biopsies were cryosectioned into alternating analyte layers so WES, RNA-seq, TMT proteome, and TMT phosphoproteome came from adjacent tumor material.
- Samples with estimated tumor content below 45% were excluded from downstream bioinformatic analysis after poor RNA-protein correlation was observed.

### Response-Associated Omics

- PAM50 subtype, TNBC type, race, BRCA1/2/PALB2 pathogenic mutations, and HRD signature 3 were not associated with pCR in this cohort, likely partly due to sample size.
- COSMIC signature 6, reflecting mismatch repair defect, associated with higher residual cancer burden.
- Baseline non-pCR tumors were enriched for metabolic pathways at the protein level; several associations were not mirrored at RNA level, making global proteome a necessary layer rather than a proxy for RNA.
- pCR tumors had higher immune signaling, interferon alpha/gamma, E2F target, G2-M checkpoint, and DNA repair signatures across RNA/protein layers.
- Protein and phosphoprotein measurements of PD-L1 correlated with PD-L1 IHC, supporting targeted proteomic immune-marker measurement as a complement to IHC.

### LIG1 / 19q13.31-33 Resistance Axis

- Cytoband enrichment of differential mRNA/protein features nominated 19q13.31-33 loss in non-pCR tumors.
- LIG1, POLD1, XRCC1, and ERCC2 formed a DNA repair/replication set within this region, with LIG1 showing the strongest protein-level association with treatment response.
- LIG1 single-copy loss appeared in 8 of 31 non-pCR tumors and correlated with lower LIG1 mRNA/protein, higher CIN, lower HRD signature 3, and higher protein proliferation score.
- External chemotherapy datasets supported low LIG1/POLD1 or LIG1/XRCC1 expression as adverse response/prognosis signals, especially in carboplatin-containing settings.
- In PDX models, LIG1 loss aligned more strongly with carboplatin resistance than docetaxel resistance, suggesting drug selectivity rather than generic chemoresistance.

## Data Availability

- Genomics/transcriptomics: dbGAP `phs002505.v1`.
- Proteomics Data Commons: `PDC000408` for TNBC biopsy proteome raw files, `PDC000409` for TNBC biopsy phosphoproteome raw files, and `PDC000410` for TNBC PDX proteome raw files.
- MassIVE: `MSV000089758`.

## Cancer Multiomics Project Relevance

- Cancer Multiomics 과제에서 “치료 반응/내성 예측 모델”을 만들 때, **WES + proteome/phosphoproteome feature를 같은 환자 바이옵시에서 연결**하는 대표 사례로 참고할 수 있다.
- 특히 pCR vs non-pCR처럼 임상 라벨이 있는 데이터에서, 유전적 feature(예: 특정 SCNA)와 phosphoproteome-driven pathway/kinase feature를 동시에 보는 분석 흐름은 Cancer Multiomics 코호트의 분석 설계에 직접적인 힌트를 준다.
- 사용자의 데이터가 somatic SNV만 있고 CNA/SV가 없다면, 이 논문은 오히려 중요한 caveat가 된다. Anurag 2022의 핵심 resistance marker는 SNV가 아니라 19q13.31-33 copy-number loss였으므로, POC에서는 SNV-only model의 한계를 명시하고 global/phospho가 그 빈틈을 메우는지 테스트해야 한다.
- 첫 분석 후보 feature set: metabolism protein ssGSEA, immune stimulatory protein score, PD-L1 protein/phosphoprotein, PTM-SEA kinase targets, DNA repair/cell-cycle scores, mutation burden/signature proxies, and if available CNA/SCNA around 19q13.31-33.

## Connections

- [Multiomics Proteomics PTM Identification](../topics/multiomics-proteomics-ptm-identification.md)
- [Multiomics PTM Corpus Queue](../analyses/multiomics-ptm-corpus-queue.md)
- [Cancer Multiomics Literature Monitor](../topics/cancer-multiomics-literature.md)
- [Drug Response Proof-of-Concept with Global Proteome, Phosphoproteome, and Somatic SNV](../analyses/drug-response-poc-global-phospho-somatic-snv.md)
- [Drug Response Phospho-Global 100-PDF Bulk Ingest](../analyses/drug-response-phospho-global-100-bulk-ingest.md)

## Sources

- Local PDF: `raw/inbox/papers/anurag-2022-proteogenomic-markers-chemotherapy-resistance-response.pdf`
