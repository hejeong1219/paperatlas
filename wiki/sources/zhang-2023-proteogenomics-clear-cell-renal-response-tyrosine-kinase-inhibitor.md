---
title: Proteogenomics of clear cell renal cell carcinoma response to tyrosine kinase inhibitor
authors:
  - "Zhang"
year: 2023
journal: "Nature Communications"
doi: "10.1038/s41467-023-39981-6"
url: "https://www.nature.com/articles/s41467-023-39981-6"
pdf: "raw/inbox/papers/zhang-2023-proteogenomics-clear-cell-renal-response-tyrosine-kinase-inhibitor.pdf"
paper_kind: translational
cancer_types:
  - renal-cell-carcinoma
modalities:
  - proteogenomics
  - phosphoproteomics
  - treatment-response
themes:
  - sunitinib-response
  - mtor-signaling
  - microenvironment
  - multi-omics-classifier
tags:
  - source
  - cancer-multiomics
  - renal-cell-carcinoma
  - proteogenomics
  - phosphoproteomics
  - treatment-response
batch_ingest_status: pdf-text-extracted
batch_ingested_on: 2026-05-13
ingest_status: full-text-read
ingested_on: 2026-05-13
---
# Proteogenomics of clear cell renal cell carcinoma response to tyrosine kinase inhibitor

Human ccRCC proteogenomics study linking protein and phosphoprotein features to differential response to sunitinib and building a response classifier from multi-omic tumor profiles.

## Full PDF Deep-Dive Status

- Status: `full-text-read` on 2026-05-13.
- Local PDF checked end-to-end: `raw/inbox/papers/zhang-2023-proteogenomics-clear-cell-renal-response-tyrosine-kinase-inhibitor.pdf` (21 pages).
- PDF identity verified: title, DOI `10.1038/s41467-023-39981-6`, Nature Communications metadata, and local `pdfinfo` match this source page.
- Evidence scope: main text, figure legends, Methods, Data Availability, classifier description, and experimental validation sections were re-read from the local PDF. Supplementary tables were not locally re-extracted in this pass.

## Batch PDF Ingest Status

- Status: `pdf-text-extracted` on 2026-05-13; superseded by the `full-text-read` promotion above.
- Local PDF: `raw/inbox/papers/zhang-2023-proteogenomics-clear-cell-renal-response-tyrosine-kinase-inhibitor.pdf`.
- Extracted text length: 79,206 characters.
- Scope note: automated local-PDF text ingest for the 100-paper drug-response/phospho-global batch, retained as provenance for the batch script.
- Evidence boundary: downstream scientific claims should now rely on the `Full PDF Deep-Dive Status`, `Key Points`, and `Detailed Evidence` sections rather than the automated snippets below.
- High-signal PDF snippets:
  - Article https://doi.org/10.1038/s41467-023-39981-6 Proteogenomics of clear cell renal cell carcinoma response to tyrosine kinase inhibitor Received: 19 August 2021 Hailiang Zhang 1,2,6, Lin Bai 1,6, Xin-Qiang Wu1,2,6, Xi Tian1,2,6, Jinwen Feng 1,6, Xiaohui Wu 1,6, Guo-Hai Shi1,2,6, Xiaoru Pei1,6, Jiacheng Lyu1,6, Guojian Yang...
  - Here, we undertake proteogenomic proﬁling of 115 tumors from patients with clear cell renal cell carcinoma (ccRCC) under- going Sunitinib treatment and reveal the molecular basis of differential clinical outcomes with TKI therapy.
  - We ﬁnd that chromosome 7q gain-induced mTOR signaling activation is associated with poor therapeutic outcomes with Suni- tinib treatment, whereas the aristolochic acid signature and VHL mutation synergistically caused enhanced glycolysis is correlated with better prognosis.
  - The proteomic and phosphoproteomic analysis further highlights the responsibility of mTOR signaling for non-response to Sunitinib.
  - Finally, we construct a multi-omics classiﬁer that can detect responder and non-responder patients (receiver operating characteristic–area under the curve, 0.98).

## Key Points

- Cohort: 115 Chinese ccRCC tumors from patients treated with sunitinib after surgery; 68 advanced and 47 recurrent tumors. Response was defined by RECIST as CR/PR responders (`n=27`) versus SD/PD non-responders (`n=88`).
- Data layers: WES (`n=113`), transcriptome (`n=94`), label-free global proteome (`n=115`), and phosphoproteome (`n=66`) from treatment-naive tumor/adjacent tissue collected at surgery before sunitinib exposure.
- Omics scale: 6487 somatic mutations; 12,276 expressed protein-coding genes; 12,310 identified proteins with 7451 proteins used for responder/non-responder analysis; 37,055 phosphosites across 7502 phosphoproteins, with 6749 phosphosites retained after the 25% coverage filter.
- Genomic response axis: VHL mutation occurred more often in responders and was associated with better survival; AA/SBS22 signature plus VHL/3p context aligned with enhanced glycolysis and better sunitinib outcomes.
- Resistance axis: chromosome 7q gain associated with poor survival and non-response. 7q-linked LAMTOR4, MDH2, and CALU showed cis effects and experimentally increased S6K phosphorylation, supporting 7q gain-induced mTORC1 activation as a resistance program.
- Phosphoproteome signal: sunitinib target RTK abundance/activity did not separate responders from non-responders, but KSEA/ssGSEA nominated MTOR and MAP2K1 activation in non-responders and CDK1/2 activity in responders.
- Immune/TME signal: proteome-inferred immune clusters separated T-cell infiltrated, cold, and progenitor-cell infiltrated tumors. The progenitor-cell infiltrated group had the lowest responder fraction, platelet/coagulation/complement features, higher PLT/thrombocytosis, and TGFB1-linked alternative angiogenesis.
- Classifier: a proteome-only random forest using 18 proteins reached AUC 0.85 on the test cohort; a multi-omics random forest using clinical, mutation, mutational signature, CNA, transcriptome, and proteome features reached test AUC 0.98, sensitivity 1.0, and specificity 0.86. The paper notes this is a single-center retrospective model needing prospective validation.

## Detailed Evidence

### Cohort and Response Definition

- Patients were treated at Fudan University Shanghai Cancer Center from January 2008 to December 2019.
- Sunitinib was given as 50 mg orally daily for 4 weeks followed by 2 weeks off treatment, until progression or unacceptable toxicity.
- Responders and non-responders had strongly different PFS and OS by Kaplan-Meier analysis, but many baseline clinical variables did not differ significantly between response groups.
- A separate untreated advanced ccRCC control cohort (`n=37`) was used to ask whether protein-survival associations were therapy-dependent; only 19 proteins overlapped between survival-associated markers in treated versus untreated cohorts.

### Genomics and Metabolism

- Frequently mutated genes included VHL (65%), PBRM1 (35%), BAP1 (16%), and SETD2 (14%).
- Patients carrying the AA/SBS22 mutational signature (`n=19`) had better PFS and smaller tumors. The authors observed attenuated pentose phosphate pathway proteins and enhanced glycolysis-related changes in AA-signature tumors.
- In vitro AA treatment of 786-O and ACHN cells enhanced the inhibitory effect of sunitinib on proliferation/invasiveness and reduced G6PD/PGD/TKT protein levels through SP1-related regulation.
- VHL loss-of-function was linked to HIF/glycolysis activation; VHL knockdown in ACHN cells increased lactate and made cells more vulnerable to sunitinib treatment.
- VHL/KMT2C co-mutation was associated with the highest responder proportion in the genotype stratification shown in the paper.

### 7q Gain and mTOR Resistance

- Common SCNAs included 3p deletion (75%), 14q deletion (45%), 9p deletion (44%), 9q deletion (44%), 5q gain (44%), 7q gain (32%), 7p gain (29%), and 20q gain (28%).
- Cox analysis linked 3q, 7p, 7q, and 8q gains with poor survival; after accounting for collinearity, 7p/7q gains remained dominant arm-level events.
- Gene-level CNA comparison showed genes more often amplified in non-responders were concentrated on 7q.
- 485 proteins correlated positively with 7q copy number and were enriched in lysosome, innate immune system, mTOR signaling, TCA cycle, OXPHOS, and fatty-acid biosynthesis pathways.
- LAMTOR4, MDH2, and CALU were cis-regulated 7q proteins. Their overexpression increased pS6K and reduced sunitinib effectiveness in renal cancer cell assays.
- pS6K IHC in additional responder/non-responder samples supported higher mTORC1 activity in non-responders.

### Proteome / Phosphoproteome Response Biology

- Sunitinib target RTK abundance and inferred global activity did not significantly differ between responders and non-responders.
- Proteome GSEA showed G2M checkpoint, antigen processing/presentation, Th17 differentiation, and NF-kappa B signaling enriched in responders.
- Non-responders were enriched for mTOR signaling, neutrophil degranulation, platelet activation, signaling, and aggregation.
- KSEA nominated MTOR and MAP2K1/MEK1 activity in non-responders and CDK1/2 activity in responders. MAP2K1 activity associated with poorer survival.
- The paper is therefore a useful warning for POC design: drug target abundance/activity alone may fail, while phosphoproteome-derived pathway/kinase context can expose resistance states.

### Immune/TME Stratification

- xCell was applied to proteomic profiles to infer 64 cell types; ESTIMATE-like immune/stromal scores were also applied at the proteome level.
- Three immune clusters were reported: T-cell infiltrated, cold, and progenitor-cell infiltrated.
- The T-cell infiltrated cluster had higher responder proportions; the progenitor-cell infiltrated cluster had lower responder proportions and worse PFS.
- The progenitor-cell infiltrated cluster showed platelet aggregation/coagulation/complement features, higher CD321, higher PLT, thrombocytosis concentrated in non-responders, and elevated TGFB1.
- TGFB1 intervention in 786-O and ACHN cell assays increased proliferation/invasiveness and weakened sunitinib inhibition, consistent with a TME-driven alternative angiogenesis resistance model.

### Classifier Design

- Proteome-only model: 18 selected protein features were used in an ensemble random forest; reported test ROC-AUC was 0.85, specificity 0.85, and sensitivity 0.75.
- Multi-omics model: included clinical features (LDH, tumor size, PLT), mutation features (VHL, KMT2C), AA signature, CNA features (7q, 3p), transcriptome features (MIR3939, ALDH1A3, LPAR1, FBLN5, C7), and the proteome feature set.
- Multi-omics model test performance: ROC-AUC 0.98, sensitivity 1.0, specificity 0.86; confusion matrix in the PDF shows 19 NR and 6 R correctly classified, with 3 NR predicted as R.
- Methods caveat: the study split data 70/30 into train/test and used fivefold cross-validation in training, but the cohort is retrospective and single-center.

## Relevance to Drug-Response POC

- This paper is a strong template for comparing `genomics-only` versus `global proteome` versus `phosphoproteome/kinase` models in a therapy-specific response setting.
- It supports including CNA/SV if available. If the user's current genomics layer is somatic SNV-only, then 7q gain and 3p/VHL context become an explicit limitation and a reason to frame the first genomics block as `SNV-only`.
- It argues against relying only on drug target abundance: sunitinib target RTK abundance/activity did not distinguish response groups, whereas mTOR/MAPK/CDK kinase context and proteome pathway states did.
- POC feature ideas: clinical LDH/PLT/tumor size; VHL/KMT2C mutation; AA-like mutational signature if relevant; 7q/3p CNA if available; mTOR/MAPK/CDK kinase scores; proteome GSEA for antigen presentation, mTOR, platelet/coagulation, neutrophil degranulation, and T-cell/TGFB1 features.

## Data Availability

- Proteome/phosphoproteome raw data: ProteomeXchange `PXD042844` via iProX project `IPX0002932000`.
- WES/RNA raw data: Genome Sequence Archive restricted accession `HRA003490`.
- Local scientific evidence used for this page: `raw/inbox/papers/zhang-2023-proteogenomics-clear-cell-renal-response-tyrosine-kinase-inhibitor.pdf`.

## Open Questions

- Supplementary tables are needed to recover the exact selected feature values, pathway score matrices, and per-sample classifier inputs.
- The multi-omics classifier should be treated as hypothesis-generating until externally or prospectively validated.
- The AA signature is population/environment-specific; it may not transfer to non-East-Asian cohorts or non-renal cancer settings.

## Cancer Multiomics Project Relevance

- Directly relevant to the ptmanchor manuscript because it shows how proteome and phosphoproteome layers can sharpen treatment-response interpretation beyond genomics alone.
- Useful as a disease-specific example where signaling-level interpretation has immediate translational value in a clinical therapy setting.
- Adds a therapy-response angle to the currently more pan-cancer-heavy PTM corpus.
- Cancer Multiomics 과제의 “WGS/WES만으로 설명되지 않는 반응성/내성 차이”를 **phosphoproteome(kinase/pathway)**로 설명하고, 나아가 multi-omics 분류기로 연결하는 구성이라 reference로 바로 재사용 가능하다.
- 사용자 POC에서는 Anurag 2022가 chemotherapy/pCR template라면, Zhang 2023은 targeted therapy/RECIST template이다. 둘을 나란히 두면 “drug target 자체보다 pathway/kinase state가 response를 더 잘 설명할 수 있다”는 논리 축이 선명해진다.

## Connections

- [ptmanchor Manuscript Anchor](../analyses/ptmanchor-manuscript-anchor.md)
- [PTM Correction and Kinase Signaling in Cancer Proteomics](../topics/ptm-correction-and-kinase-signaling-in-cancer-proteomics.md)
- [Cancer Multiomics Literature Monitor](../topics/cancer-multiomics-literature.md)
- [Drug Response Proof-of-Concept with Global Proteome, Phosphoproteome, and Somatic SNV](../analyses/drug-response-poc-global-phospho-somatic-snv.md)
- [Drug Response Phospho-Global 100-PDF Bulk Ingest](../analyses/drug-response-phospho-global-100-bulk-ingest.md)
- [Comprehensive evaluation of phosphoproteomic-based kinase activity inference](./muller-dott-2025-phosphoproteomic-kinase-activity-inference.md)
- [Proteogenomics connects somatic mutations to signalling in breast cancer](./mertins-2016-proteogenomics-somatic-mutations-signalling-breast-cancer.md)

## Sources

- PDF: [zhang-2023-proteogenomics-clear-cell-renal-response-tyrosine-kinase-inhibitor.pdf](../../raw/inbox/papers/zhang-2023-proteogenomics-clear-cell-renal-response-tyrosine-kinase-inhibitor.pdf)
