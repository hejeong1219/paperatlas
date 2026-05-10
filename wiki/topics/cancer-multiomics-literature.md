---
title: Cancer Multiomics Literature Monitor
tags:
  - cancer-multiomics
  - wgs
  - phosphoproteomics
  - proteogenomics
  - slack-digest
themes:
  - targeted-immunotherapy-resistance
  - ppqtl
  - neoantigen
  - kinase-signaling
  - response-prediction
---

# Cancer Multiomics Literature Monitor

Cancer Multiomics 과제와 연결되는 최신 high-impact 암 단백유전체 논문을 읽고, 전장유전체·인산화단백체·신생항원·면역회피·치료반응 예측 모델 관점에서 교수진에게 공유할 수 있는 형태로 정리하는 topic hub.

## Key Points

- 과제의 중심 질문은 전장유전체만으로 설명되지 않는 표적-면역치료제 반응성 및 내성 차이를 인산화단백체, kinase network, neoantigen, 면역 관련 feature와 통합해 설명할 수 있는지다.
- 논문 정리는 단순 요약이 아니라 과제의 4개 축에 직접 연결한다: 인산화단백체 분석 파이프라인, WGS-PTM 통합/ppQTL, 신생항원 및 면역회피, 치료반응 예측 모델.
- 각 논문은 하위 페이지로 정리하고, topic hub에는 분류별로 링크와 Slack 공유용 핵심 포인트만 남긴다.
- Slack 메시지는 교수진에게 바로 공유 가능한 짧은 형식으로 별도 섹션에 보존한다.
- 진행 현황/큐: [Cancer Multiomics Corpus Queue (Target=100)](../analyses/cancer-multiomics-corpus-queue.md)

## Project Alignment

- **WGS 변이 해석**: SNV, indel, structural variant, copy-number signature, noncoding mutation, germline feature, HLA typing.
- **인산화단백체 분석**: TMT/DIA 기반 phosphoproteomics, 결측/배치 보정, phosphosite-level differential analysis, kinase activity inference.
- **WGS-단백체 통합**: pQTL, ppQTL, copy-number-to-protein effect, driver-to-functional-state mapping.
- **면역/신생항원**: WGS 기반 neoantigen candidate, HLA binding prediction, immunopeptidomics/proteogenomic validation, immune evasion.
- **치료반응 예측**: response/non-response classification, primary/acquired resistance, SHAP-style feature interpretation, basket-trial molecular grouping.
- **데이터 공유**: CPTAC/GDC/PDC/NCDC 기탁, 분석 재현성, cloud-scale WGS/proteomics integration.

## 하위 페이지 템플릿

각 논문 페이지는 최소한 아래 구조를 따른다.

```markdown
## 논문 정보 (저자 / 저널 / DOI / Wiki 경로)
## 한 줄 요약
## 과제 관련성 (Cancer Multiomics)
## 주요 결과
## Slack 메시지 초안
```

## 표준 메타데이터 체크리스트 (하위 페이지 공통)

하위 페이지에 아래 3개 bullet을 **고정 섹션**으로 넣는다(모르면 “PDF 확인 필요”로 표기).

- 치료 맥락: 암종 / 치료제 class / 라인 / 반응 라벨(Primary/Acquired 등) / 샘플 타이밍
- 데이터 레이어: WGS/WES, RNA-seq, proteome, phosphoproteome, acetylome, immunopeptidomics, spatial 등
- 데이터 공개: raw/processed/supplement/code(접근 경로는 PDF의 Data Availability 기준)

## Next Candidates

다음 배치에서 다룰 “PDF는 있으나 Cancer Multiomics 하위 페이지가 아직 없는” 후보는 큐에서 관리한다:

- [Cancer Multiomics Corpus Queue (Target=100)](../analyses/cancer-multiomics-corpus-queue.md)

## 1. WGS와 Proteogenomics 통합 기반

- [Chen 2020 - Non-Smoking Lung Cancer Proteogenomics](../analyses/cancer-multiomics-literature/chen-2020-non-smoking-lung-cancer-proteogenomics.md) - 동아시아 비흡연 폐암에서 WGS/단백체/인산화단백체를 통합해 EGFR-mutant 조기 폐암의 분자 이질성과 진행 축을 설명한다.
- [Huang 2021 - HPV-Negative HNSCC Proteogenomics](../analyses/cancer-multiomics-literature/huang-2021-hnscc-proteogenomics.md) - HNSCC에서 phosphoproteomics가 EGFR activation mode, immune-hot/cold state, 치료 취약성을 어떻게 분리하는지 보여준다.
- [Satpathy 2021 - LSCC Proteogenomic Portrait (WGS/WES + Multi-PTM + Immune)](../analyses/cancer-multiomics-literature/satpathy-2021-proteogenomic-portrait-lung-squamous-cell.md) - LSCC에서 WGS/WES+multi-PTM을 통합해 NSD3 driver, Rb phosphorylation 기반 CDK4/6 기능 biomarker 등 “유전→기능 상태” 연결을 제시한다.
- [Dou 2020 - Endometrial Carcinoma Proteogenomics (WES/WGS + Phospho + Acetyl + Immune)](../analyses/cancer-multiomics-literature/dou-2020-proteogenomic-characterization-endometrial-carcinoma.md) - CPTAC 자궁내막암에서 WES/WGS subtype을 proteome/phospho/acetyl 기능 상태로 재해석하고 MSI의 항원제시 결함 같은 면역 축까지 연결한다.
- [Clark 2019 - ccRCC CPTAC Proteogenomics (Tumor+NAT; immune subtypes)](../analyses/cancer-multiomics-literature/clark-2019-integrated-proteogenomic-characterization-clear-cell.md) - ccRCC에서 proteome/phosphoproteome + multi-omics를 통합해 genomic instability, 대사/번역/인산화 모듈 및 4개 immune subtype을 기능 상태로 제시한다.
- [Gillette 2020 - LUAD CPTAC Proteogenomics (Tumor+NAT; Phospho+Acetyl)](../analyses/cancer-multiomics-literature/gillette-2020-proteogenomic-characterization-reveals-therapeutic-vulnerabilities.md) - LUAD tumor+NAT에서 KRAS/EGFR/ALK driver 연관 기능 상태와 STK11-immune-cold 축을 proteome/phospho/acetyl 레이어로 해석한다.
- [Krug 2020 - Breast Cancer Proteogenomics (PTM-preserved; HER2/Rb/kinase)](../analyses/cancer-multiomics-literature/krug-2020-proteogenomic-landscape-breast-cancer-tumorigenesis.md) - PTM 보존 수집 코호트로 HER2(ERBB2), Rb, kinase signaling을 proteogenomics로 재정의하고 치료 취약성 후보를 논의한다.
- [Cao 2021 - PDAC CPTAC Proteogenomics (WGS/WES + Phospho + Glyco)](../analyses/cancer-multiomics-literature/cao-2021-proteogenomic-characterization-pancreatic-ductal-adenocarcinoma.md) - PDAC에서 WGS/WES·전사체·메틸화와 proteome/phosphoproteome/glycoproteome을 동일 샘플로 통합한 리소스.
- [Chen 2023 - SV Breakpoints → Protein Consequences (Pan-cancer WGS+Proteomics)](../analyses/cancer-multiomics-literature/chen-2023-global-impact-somatic-structural-variation-cancer-proteome.md) - WGS 기반 SV breakpoint 패턴이 단백질 발현으로 “실제 반영”되는 비율을 pan-cancer로 정량화해, SV-aware proteogenomics 필요성을 강조한다.
- [Li 2023 - Pan-Cancer Driver-to-Functional-State Proteogenomics](../analyses/cancer-multiomics-literature/li-2023-pan-cancer-driver-functional-states.md) - pan-cancer CPTAC 데이터로 driver event가 RNA, protein, phosphoprotein functional state로 어떻게 번역되는지 정리한다.
- [Savage 2024 - CPTAC Pan-Cancer Therapeutic Target Landscape](../analyses/cancer-multiomics-literature/savage-2024-pan-cancer-proteogenomics-expands-landscape-therapeutic.md) - pan-cancer proteogenomics를 기반으로 druggable dependency/synthetic lethality/항원 후보를 protein/phosphoprotein 상태에서 우선순위화한다.
- [Deng 2023 - Cholangiocarcinoma Proteogenomics (WES + Phosphoproteome)](../analyses/cancer-multiomics-literature/deng-2023-proteogenomic-characterization-cholangiocarcinoma.md) - 대규모 CCA 코호트에서 WES+phosphoproteome을 통합해 subtype과 kinase/면역 가설을 제시한다.
- [Cheng 2025 - Wilms Tumor Proteogenomics (WES + Phosphoproteome)](../analyses/cancer-multiomics-literature/cheng-2025-integrative-proteogenomic-characterization-wilms-tumor.md) - 소아 WT에서 tumor–NAT multi-omics로 아형을 정의하고 EHMT2 등 후보를 제시한다.
- [Song 2024 - NSCLC Multi-Omics Subtypes (WGD / PI3K–Akt / TME)](../analyses/cancer-multiomics-literature/song-2024-proteogenomic-analysis-reveals-non-small-cell.md) - 한국인 NSCLC 229명에서 WES+proteome/phosphoproteome(+acetylome)로 5개 subtype을 정의하고 WGD/면역 축과 예후·adjuvant therapy 신호를 연결한다.
- [Yu 2024 - Cervical Cancer Proteogenomics (Phospho + Acetyl + Radioresponse)](../analyses/cancer-multiomics-literature/yu-2024-proteogenomic-analysis-cervical-cancer-reveals.md) - 자궁경부암 139명에서 WES+phosphoproteome+acetylome을 통합해 3개 subgroup 및 radioresponse biomarker 후보(PRKCB)를 제시한다.
- [Qu 2024 - PTC Recurrence Risk Multi-Omics (Proteome + Phospho + Metabolome)](../analyses/cancer-multiomics-literature/qu-2024-integrated-proteogenomic-metabolomic-characterization-papillary.md) - PTC 102명에서 재발 위험을 multi-omics subtype으로 분해(대사형/면역형 등)하는 아시아 코호트 레퍼런스.
- [Tanaka 2024 - CRC Primary vs Liver Metastasis Proteogenomics](../analyses/cancer-multiomics-literature/tanaka-2024-proteogenomic-characterization-primary-colorectal-cancer.md) - 원발/간 전이 CRC 대규모 proteogenomics로 hypoxia/stemness/immune-cold(항원제시 억제) 진행 시그니처를 정리한다.
- [Ramsberger 2024 - Multiple Myeloma Proteogenomics (Nanopore WGS + Phosphoproteome)](../analyses/cancer-multiomics-literature/ramberger-2024-proteogenomic-landscape-multiple-myeloma-reveals.md) - nanopore WGS(CNV) + TMT phosphoproteomics로 CNA–기능 상태를 연결하고 phosphoproteomic risk stratification 사례를 제시한다(고형암 외이지만 설계 참고용).

## 2. 인산화단백체와 Kinase Network

- [Jiang 2025 - Dark Cancer Phosphoproteome](../analyses/cancer-multiomics-literature/jiang-2025-dark-cancer-phosphoproteome.md) - annotation이 부족한 phosphosite를 co-regulation network로 해석해 kinase-substrate 후보 공간을 넓힌다.
- [Shi 2025 - Functional Network of Human Cancer](../analyses/cancer-multiomics-literature/shi-2025-functional-network-human-cancer.md) - protein-level network가 transcriptome보다 기능 관계 해석에 강한 축이 될 수 있음을 보여준다.
- [Muller-Dott 2025 - Benchmarking Kinase Activity Inference](../analyses/cancer-multiomics-literature/muller-dott-2025-phosphoproteomic-kinase-activity-inference.md) - kinase activity inference에서 알고리즘보다 substrate library 선택이 성능을 좌우할 수 있음을 보여주는 벤치마크.
- [Asuzu 2025 - Phosphoproteomic Dysregulation Drives Tumor Proliferation](../analyses/cancer-multiomics-literature/asuzu-2025-phosphoproteomic-dysregulation-drives-tumor-proliferation.md) - genomic driver가 약한 상황에서도 phosphatase 축(PP2A) 기반 인산화 dysregulation이 종양 phenotype을 구동할 수 있음을 multi-omics로 제시한다.
- [Zhao 2025 - Phosphoproteomic + Acetylomic Response to Kinase Inhibitors (CRC)](../analyses/cancer-multiomics-literature/zhao-2025-phosphoproteomic-acetylomic-characterization-colorectal-cancer.md) - inhibitor perturbation에서 off-target signaling과 PTM crosstalk까지 포함해 pathway/kinase 수준 요약 전략을 제공한다.
- [Khan 2026 - Public Phosphoproteomics Network Meta-analysis (CAMK2D–TPD52)](../analyses/cancer-multiomics-literature/khan-2026-integrative-phosphoproteomic-network-analysis-identifies.md) - 공개 phosphoproteomics를 통합해 phosphosite/network에서 upstream kinase 가설을 도출하는 예시(우선순위는 낮을 수 있음).

## 3. 면역회피와 Neoantigen

- [Petralia 2024 - Pan-Cancer Proteogenomics of Tumor Immunity](../analyses/cancer-multiomics-literature/petralia-2024-pan-cancer-tumor-immunity.md) - CPTAC pan-cancer proteogenomics로 immune subtype, pathway activity, kinase activity를 함께 해석한다.
- [Wen 2020 - NeoFlow Proteogenomic Neoantigen Prioritization](../analyses/cancer-multiomics-literature/wen-2020-neoflow-neoantigen-prioritization.md) - WGS/proteomics 기반 neoantigen 후보 우선순위화와 retention-time 기반 QC logic을 제공한다.
- [Huber 2025 - NeoDisc Proteogenomic Neoantigen Pipeline](../analyses/cancer-multiomics-literature/huber-2025-neodisc-neoantigen-pipeline.md) - immunopeptidomics와 multi-omics를 결합한 임상형 neoantigen discovery pipeline reference로 쓸 수 있다.
- [Shapiro 2025 - NeoDiscMS Real-time NGS-guided Immunopeptidomics](../analyses/cancer-multiomics-literature/shapiro-2025-sensitive-neoantigen-discovery-real-time-mutanome-guided.md) - inclusion list + real-time search로 표적 스캔을 트리거해 임상 TAT 제약에서 민감도를 높이는 acquisition 설계.
- [Scheid 2025 - MHCquant2 (nf-core) Immunopeptidomics Pipeline](../analyses/cancer-multiomics-literature/scheid-2025-mhcquant2-refines-immunopeptidomics-tumor-antigen.md) - immunopeptidomics 처리 표준화/재현성 및 benign reference 기반 antigen refinement 레퍼런스.
- [Saxena 2025 - Atezolizumab + Personalized Neoantigen Vaccination (Urothelial Cancer)](../analyses/cancer-multiomics-literature/atezolizumab-2025-personalized-neoantigen-vaccination-urothelial-cancer.md) - neoantigen vaccine(PGV001)+PD-L1 병용 1상에서 제조/기간/투여 feasibility와 면역반응 readout을 제시한다.
- [Braun 2025 - Peptide PCV in Resected ccRCC (± ipilimumab)](../analyses/cancer-multiomics-literature/braun-2025-neoantigen-vaccine-generates-antitumour-immunity.md) - low TMB ccRCC에서도 다중 epitope peptide 백신이 강한 면역반응(자가 종양 인지 7/9)을 보이고, 소규모지만 재발 없는 경과를 보고한 adjuvant 임상 근거.
- [Gainor 2024 - KEYNOTE-603 mRNA-4157(V940) Immunogenicity](../analyses/cancer-multiomics-literature/gainor-2024-t-cell-responses-individualized-neoantigen-therapy.md) - 개인맞춤 neoantigen mRNA가 예측 후보 중 어느 정도 실제 T cell 반응으로 이어지는지(ELISpot/ICS/TCR readout)를 보여주는 phase 1 중간기전 근거.
- [Weber 2024 - KEYNOTE-942 (V940 mRNA neoantigen + pembrolizumab; melanoma)](../analyses/cancer-multiomics-literature/weber-2024-individualised-neoantigen-therapy-mrna-4157-v940.md) - 개인맞춤 neoantigen mRNA 병용이 재발 위험을 낮추는 신호를 보여주는 임상 근거.
- [Keskin 2019 - Personalized Neoantigen Vaccine in Glioblastoma (Steroid Effect + TCR Tracking)](../analyses/cancer-multiomics-literature/keskin-2019-neoantigen-vaccine-generates-intratumoral-t.md) - GBM 개인맞춤 neoantigen 백신 1상에서 dexamethasone이 면역반응을 크게 억제하며, scTCR로 말초→종양 이동을 추적한다.
- [Abelin 2023 - MONTE Serial Multi-Omics (Immunopeptidome + PTM)](../analyses/cancer-multiomics-literature/abelin-2023-workflow-enabling-deepscale-immunopeptidome-proteome.md) - 제한된 샘플에서 immunopeptidome과 multi-PTM을 같은 샘플로 직렬 수집하는 실험 설계 레퍼런스.
- [Chong 2022 - Identification of Tumor Antigens with Immunopeptidomics](../analyses/cancer-multiomics-literature/chong-2022-identification-tumor-antigens-immunopeptidomics.md) - canonical/noncanonical 항원 발굴과 false positive 관리(FDR/검증)의 핵심 텐션을 정리한 리뷰.
- [Chen 2026 - Enrichment of Phosphorylated/Glycosylated MHC Peptides (Methods)](../analyses/cancer-multiomics-literature/chen-2026-enrichment-phosphorylated-glycosylated-mhc-peptides.md) - PTM-MHC peptide(phospho/glyco) 동정을 위한 순차 농축 워크플로(예측이 아닌 측정)의 방법 레퍼런스.

## 4. 치료반응 예측 모델과 데이터 인프라

- [Han 2024 - HLA-Based Neoantigen Presentation Score Predicts Pan-Cancer ICI Response](../analyses/cancer-multiomics-literature/han-2024-hla-based-neoantigen-presentation-pan-cancer-response.md) - neoantigen “개수”가 아니라 presentation-aware score로 ICI 반응/생존과의 연관을 제시한다.
- [Anurag 2022 - TNBC Neoadjuvant Chemo Response (WES + Phosphoproteome)](../analyses/cancer-multiomics-literature/anurag-2022-proteogenomic-markers-chemotherapy-resistance-response.md) - pCR/non-pCR 임상 라벨을 WES+TMT phosphoproteomics로 분해하고 19q13 결실 등 내성 신호를 제시한다.
- [Haas 2024 - Prostate Cancer Radioresistance (WES + Proteome)](../analyses/cancer-multiomics-literature/haas-2024-proteogenomics-prostate-cancer-radioresistance.md) - 방사선 fractionation(CF/HF)에 따라 다른 내성 프로그램과 POLQ radiosensitizer 후보를 제시한다.
- [Zhang 2023 - ccRCC Sunitinib Response Proteogenomics (mTOR / 7q / Classifier)](../analyses/cancer-multiomics-literature/zhang-2023-proteogenomics-clear-cell-renal-response-tyrosine-kinase-inhibitor.md) - sunitinib responder/non-responder(RECIST) 라벨에서 mTOR/7q 등 proteome/phosphoproteome feature를 포함한 반응 예측 예시.
- 현재 seed 논문들은 주로 mechanistic feature와 data layer를 제공한다. 이후 Slack에서 들어오는 논문은 response model, SHAP/feature interpretation, basket trial, cloud-scale WGS/proteomics processing 축으로 추가한다.

## 5. 면역치료 내성 우회(조합 전략)

- [Skoulidis 2024 - CTLA4 blockade abrogates KEAP1/STK11-related resistance](../analyses/cancer-multiomics-literature/skoulidis-2024-ctla4-abrogates-keap1-stk11-resistance.md) - KEAP1/STK11 변이 NSCLC에서 dual ICB(CTLA-4 병용)가 내성 병목을 우회할 수 있다는 임상·기전 프레임을 제공.
- [Memon 2024 - Acquired Resistance to PD-(L)1 Blockade in NSCLC](../analyses/cancer-multiomics-literature/memon-2024-clinical-molecular-features-acquired-resistance.md) - NSCLC 획득내성(AR)에서 IFNγ signature 증가/지속과 항원제시 경로 이상(B2M 등)이 결합되는 “persistently inflamed but dysfunctional” 프레임을 cohort-scale로 제시.
- [Yaeger 2023 - Acquired Resistance to KRASG12C–EGFR Inhibition in CRC (ctDNA + ERK/mTOR Switch)](../analyses/cancer-multiomics-literature/yaeger-2023-molecular-characterization-acquired-resistance-krasg12c-egfr.md) - 표적치료 병용에서 ctDNA 시계열로 내성 변이를 추적하고, KRASG12C amplification·약물중단 후 senescence/mTOR 전환 같은 상태 전이를 내성 프레임으로 제시한다.

## 6. 2026-05 Expansion: AI/Spatial/ecDNA/CAR-T 보강 (45편)

Notion 'Cancer Multiomics' 페이지의 27개 시드 + OpenAlex 인용 그래프로 발굴한 score≥6 관련논문 18편을 통합 ingest. PDF 상태: 36편 다운로드 완료, 9편 manual_pending (Cell Press anti-bot, bioRxiv 2026 DOI 미등록 등). Discovery 메타데이터는 frontmatter `discovery_method`/`related_to_seeds`에 기록.

### 6.1 AI / Foundation models / Deep learning

- [TWAS signature-matching for drug prioritisation: a best-practice benchmark](../sources/chauquet-2026-twas-signature-matching-drug-prioritisation-benchmark.md) (Notion seed)
- [Towards a general-purpose foundation model for computational pathology](../sources/chen-2024-towards-general-purpose-foundation-model.md) (OpenAlex)
- [CenSegNet: a generalist high-throughput framework for centrosome phenotyping in heterogeneous cancer tissues](../sources/cheng-2025-censegnet-centrosome-phenotyping-cancer-tissues.md) (Notion seed)
- [Linking spatial biology and clinical histology via Haiku](../sources/cui-2026-haiku-tri-modal-spatial-biology-histology.md) (Notion seed)
- [Expanding the human proteome with peptideins from non-canonical ORFs](../sources/deutsch-2026-expanding-human-proteome-peptideins-noncanonical-orfs.md) (Notion seed)
- [Do larger models really win? A scaling benchmark in AI-driven drug discovery](../sources/guo-2026-larger-models-scaling-benchmark-drug-discovery.md) (Notion seed)
- [Simulating 500 million years of evolution with a language model (ESM3)](../sources/hayes-2025-simulating-500-million-years-evolution.md) (OpenAlex)
- [A deep-learning framework to predict cancer treatment response from histopathology images through imputed transcriptomics](../sources/hoang-2024-deep-learning-framework-predict-cancer.md) (OpenAlex)
- [Prediction of DNA methylation-based tumor types from histopathology in central nervous system tumors with deep learning](../sources/hoang-2024-prediction-dna-methylation-based-tumor.md) (OpenAlex)
- [DrugCLIP: contrastive protein-ligand model for genome-scale virtual screening (GenomeScreenDB)](../sources/jia-2026-drugclip-contrastive-protein-ligand-genome-scale.md) (Notion seed)
- [MolGene-E: inverse molecular design from single-cell transcriptomic reversal for anticancer perturbation](../sources/ohlan-2025-molgene-e-inverse-molecular-design-transcriptomic-reversal.md) (Notion seed)
- [Multimodal data fusion for cancer biomarker discovery with deep learning](../sources/steyaert-2023-multimodal-data-fusion-cancer-biomarker.md) (OpenAlex)
- [Reimagining human-centric drug development with new approach methodologies (NAMs)](../sources/wu-2026-reimagining-human-centric-drug-development-nams.md) (Notion seed)
- [Deep-learning-based de novo discovery and design of therapeutics that reverse disease-associated transcriptional phenotypes](../sources/xing-2026-deep-learning-de-novo-transcriptional-phenotype-reversal.md) 🟠 (Notion seed)
- [ProteinAligner: Tri-modal contrastive protein language model integrating sequence, structure, and text](../sources/zhang-2026-proteinaligner-tri-modal-contrastive-protein-language.md) 🟠 (Notion seed)
- [Systematically decoding pathological morphologies and molecular profiles with unified multimodal embedding](../sources/zhang-2026-systematically-decoding-pathological-morphologies-multimodal-embedding.md) (Notion seed)

### 6.2 Spatial multiomics

- [Resolving sensitivity, specificity and signal contamination in Xenium spatial transcriptomics](../sources/bilous-2026-xenium-sensitivity-specificity-signal-contamination.md) (Notion seed)
- [Molecular cartography uncovers evolutionary and microenvironmental dynamics in sporadic colorectal tumors](../sources/heiser-2023-molecular-cartography-uncovers-evolutionary-microenvironmental.md) 🟠 (OpenAlex)
- [High resolution mapping of the tumor microenvironment using integrated single-cell, spatial and in situ analysis](../sources/janesick-2023-high-resolution-mapping-tumor-microenvironment.md) (OpenAlex)
- [Spatially informed clustering, integration, and deconvolution of spatial transcriptomics with GraphST](../sources/long-2023-spatially-informed-clustering-integration-deconvolution.md) (OpenAlex)
- [Single-cell spatial multiomics identifies POSTN+ CAFs driving chemoradiotherapy resistance in rectal cancer](../sources/sakai-2026-postn-cafs-chemoradiotherapy-resistance-rectal-cancer.md) 🟠 (Notion seed)
- [Pan-cancer virtual spatial transcriptomics from routine histology with Phoenix](../sources/tran-2026-phoenix-pan-cancer-virtual-spatial-transcriptomics.md) (Notion seed)
- [Non-invasive profiling of the tumour microenvironment with spatial ecotypes](../sources/zhang-2026-non-invasive-tumour-microenvironment-spatial-ecotypes.md) (Notion seed)

### 6.3 ecDNA biology

- [Parallel sequencing of extrachromosomal circular DNAs and transcriptomes in single cancer cells](../sources/gonzalez-2023-parallel-sequencing-extrachromosomal-circular-dnas.md) (OpenAlex)
- [Coordinated inheritance of extrachromosomal DNAs in cancer cells](../sources/hung-2024-coordinated-inheritance-extrachromosomal-dnas-cancer.md) (OpenAlex)
- [Extrachromosomal DNA Amplification Contributes to Small Cell Lung Cancer Heterogeneity and Is Associated with Worse Outcomes](../sources/pongor-2023-extrachromosomal-dna-amplification-contributes-small.md) (OpenAlex)
- [Extrachromosomal DNA gives cancer a separate evolutionary pathway](../sources/wang-2025-extrachromosomal-dna-cancer-evolutionary-pathway.md) (Notion seed)

### 6.4 T-cell biology / CAR-T / TCR

- [Lymphoid chemokine signalling limits CD8+ T cell priming time to preserve effector function](../sources/altenburger-2026-lymphoid-chemokine-cd8-priming-effector.md) (Notion seed)
- [A generative reference grammar of healthy TCR repertoires for cancer immune remodeling analysis](../sources/balan-2026-generative-reference-grammar-tcr-repertoires-cancer.md) 🟠 (Notion seed)
- [T cell state transcription factor cooperation engineering: KLF2 x RUNX2 memory-like CAR-T design](../sources/savage-2026-klf2-runx2-memory-like-car-t.md) (Notion seed)

### 6.5 Single-cell methods / atlases

- [SCENIC+: single-cell multiomic inference of enhancers and gene regulatory networks](../sources/gonzalezblas-2023-scenic-single-cell-multiomic-inference.md) (OpenAlex)
- [Best practices for single-cell analysis across modalities](../sources/heumos-2023-best-practices-single-cell-analysis.md) (OpenAlex)
- [A transcription factor atlas of directed differentiation](../sources/joung-2023-transcription-factor-atlas-directed-differentiation.md) 🟠 (OpenAlex)
- [10x Genomics Gene Expression Flex enables single-cell transcriptomics on fixed and frozen xenograft samples](../sources/llora-batlle-2024-10x-flex-fixed-xenograft-single-cell.md) (Notion seed)
- [Applications of single-cell RNA sequencing in drug discovery and development](../sources/sande-2023-applications-single-cell-rna-sequencing.md) (OpenAlex)

### 6.6 Cancer biology / TME (PDAC, CRC, sarcoma)

- [Extra-lineage tissue programs define transcriptional states in human pancreatic cancer](../sources/ge-2026-extra-lineage-tissue-programs-pancreatic-cancer-transcriptional.md) 🟠 (Notion seed)
- [Sarcoma microenvironment cell states and ecosystems are associated with prognosis and predict response to immunotherapy](../sources/subramanian-2024-sarcoma-microenvironment-cell-states-ecosystems.md) (OpenAlex)
- [Schwann cells regulate tumor cells and cancer-associated fibroblasts in the pancreatic ductal adenocarcinoma microenvironment](../sources/xue-2023-schwann-cells-regulate-tumor-cells.md) (OpenAlex)

### 6.7 Drug discovery / Pathway / Resource

- [CADDIE: web-based network-medicine platform for cancer driver-based drug repurposing](../sources/hartung-2022-caddie-cancer-driver-drug-repurposing-platform.md) (Notion seed)
- [nf-core Nextflow disease module discovery and benchmarking pipeline for network medicine reproducibility](../sources/kersting-2025-nf-core-disease-module-network-medicine.md) (Notion seed)
- [Predicting bladder cancer molecular subtypes and BCG response from histology using deep learning](../sources/khoraminia-2026-predicting-bladder-molecular-subtypes-bcg-response.md) (Notion seed)
- [The Reactome Pathway Knowledgebase 2024](../sources/orlicmilacic-2023-reactome-pathway-knowledgebase-2024.md) (OpenAlex)
- [Multimodal deep learning on LINCS L1000 reveals brain-penetrant Class I HDAC inhibitors as pan-cancer candidates](../sources/tong-2026-multimodal-lincs-pan-cancer-hdac-inhibitor.md) (Notion seed)
- [Cross-assay RNA modeling reveals robust cancer biomarkers across heterogeneous platforms](../sources/townsend-2026-cross-assay-rna-modeling-cancer-biomarker-discovery.md) 🟠 (Notion seed)
- [Open Targets Gentropy: pleiotropy mapping across 100,526 GWAS for therapeutic target prioritisation](../sources/tsepilov-2026-open-targets-gentropy-pleiotropy-gwas-prioritisation.md) 🟠 (Notion seed)

**상태 표시**: 🟠 manual_pending (anti-bot/미공개 DOI), 표시 없음 = PDF 다운로드 완료.

## Open Questions

- 질문 확장 맵: [Four-Topic Question Expansion Map](../analyses/topic-question-expansion-map.md) (Topic 4)
- 표준 추출 체크리스트(초안): 치료 맥락(암종/치료제/라인/반응 라벨), 데이터 레이어(WGS/Proteome/Phospho/Neoantigen), 데이터 공개 수준(raw/processed/supplement/code), 핵심 방법(TMT/DIA/enrichment/instrument), 과제 연결(예측/내성/파이프라인) 1~2줄

- Cancer Multiomics 과제의 실제 환자군에서 치료제 class, primary/acquired resistance label, biopsy timing을 논문 요약 페이지의 표준 metadata로 넣을 것인가?
- neoantigen 논문은 WGS-only prediction 중심 논문과 immunopeptidomics/proteogenomics validation 중심 논문을 분리할 것인가?
- phosphoproteomics 논문은 identification scale보다 normalization, missingness, kinase inference, protein-abundance correction 여부를 우선 기록할 것인가?
- Slack 메시지는 짧은 공유용과 deep-dive용 두 버전으로 관리할 것인가?

## Connections

- [Multiomics Proteomics PTM Identification](./multiomics-proteomics-ptm-identification.md)
- [PTM Correction and Kinase Signaling in Cancer Proteomics](./ptm-correction-and-kinase-signaling-in-cancer-proteomics.md)
- [Immunotherapy Resistance and Immune Evasion](./immunotherapy-resistance-and-immune-evasion.md)
- [B-Cell Neoantigen Research Map](./b-cell-neoantigen-human-cancer.md)

## Sources

- User-provided Cancer Multiomics HWP research plan, read locally.
- Local extracted text: `/private/tmp/hwp_extract/cancer_multiomics_plan_extracted.txt`
- 하위 페이지에 연결된 local wiki source pages and PDFs.
