---
title: Cancer Multiomics Corpus Queue (Target=100)
tags:
  - cancer-multiomics
  - corpus-queue
  - wgs
  - phosphoproteomics
  - proteogenomics
---

# Cancer Multiomics Corpus Queue (Target=100)

Cancer Multiomics 과제에 직접 연결되는 “100편 high-impact 코퍼스”를 운영하기 위한 큐/진행 현황 페이지.

## Key Points

- 이 페이지는 **선정(Selection)** → **PDF 확보(Acquired)** → **소스 페이지(ingested `wiki/sources/`)** → **Cancer Multiomics 하위 페이지(brief: `wiki/analyses/cancer-multiomics-literature/`)**의 4단계를 구분해 추적한다.
- 웹은 “논문 발견/메타데이터/다운로드”에만 사용하고, 과학적 요약/Slack 메시지는 로컬 PDF 또는 로컬 소스 페이지 기반으로만 작성한다.
- 배치 단위로 진행한다(후보 추가 → PDF 확보 → 소스 deep-dive → Cancer Multiomics 하위 페이지/토픽 허브 반영).

## Status (rolling)

- Target: **100**
- Selected (in-scope, rolling): **91** (briefed=44 + 2026-05 expansion stubs=45 + blocked=2)
- Acquired PDFs (`raw/inbox/papers/`): **80** (44 prior + 36 new from 2026-05 expansion; excludes 1 invalid-HTML and 1 correction-only)
- Ingested source pages (`wiki/sources/` updated beyond placeholder): **90** (45 prior + 45 new stubs from 2026-05 expansion)
- Cancer Multiomics subpages (`wiki/analyses/cancer-multiomics-literature/`): **44** (expansion batch awaits deep-dive)
- Blocked (PDF missing / paywall / metadata unresolved): **11** (2 prior + 9 new manual_pending in 2026-05 expansion: Cell Press anti-bot, bioRxiv 2026 미등록 DOI 등)

## Seed Set (already in Cancer Multiomics topic hub)

- [Chen 2020 - Non-Smoking Lung Cancer Proteogenomics](./cancer-multiomics-literature/chen-2020-non-smoking-lung-cancer-proteogenomics.md)
- [Huang 2021 - HPV-Negative HNSCC Proteogenomics](./cancer-multiomics-literature/huang-2021-hnscc-proteogenomics.md)
- [Li 2023 - Pan-Cancer Driver-to-Functional-State Proteogenomics](./cancer-multiomics-literature/li-2023-pan-cancer-driver-functional-states.md)
- [Petralia 2024 - Pan-Cancer Proteogenomics of Tumor Immunity](./cancer-multiomics-literature/petralia-2024-pan-cancer-tumor-immunity.md)
- [Huber 2025 - NeoDisc Proteogenomic Neoantigen Pipeline](./cancer-multiomics-literature/huber-2025-neodisc-neoantigen-pipeline.md)
- [Jiang 2025 - Dark Cancer Phosphoproteome](./cancer-multiomics-literature/jiang-2025-dark-cancer-phosphoproteome.md)
- [Shi 2025 - Functional Network of Human Cancer](./cancer-multiomics-literature/shi-2025-functional-network-human-cancer.md)
- [Wen 2020 - NeoFlow Proteogenomic Neoantigen Prioritization](./cancer-multiomics-literature/wen-2020-neoflow-neoantigen-prioritization.md)

## Selected set (beyond seed set)

Status legend:
- `selected` = in-scope for 100-paper set
- `needs-deep-dive` = source page is placeholder; update from PDF before Cancer Multiomics brief
- `needs-brief` = ready for Cancer Multiomics subpage
- `briefed` = Cancer Multiomics subpage created + topic hub linked
- `blocked` = PDF/metadata not yet resolved

| Basename | Area | Status | Notes |
| --- | --- | --- | --- |
| `abelin-2023-workflow-enabling-deepscale-immunopeptidome-proteome` | immunopeptidomics + multi-PTM workflow | `briefed` | MONTE workflow (HLA peptidome + phospho/acetyl/ubiquitylome). |
| `atezolizumab-2025-personalized-neoantigen-vaccination-urothelial-cancer` | personalized neoantigen vaccine + ICI (clinical) | `briefed` | PGV001 + atezolizumab phase 1 feasibility/safety and immune readouts. |
| `braun-2025-neoantigen-vaccine-generates-antitumour-immunity` | personalized neoantigen vaccine (clinical; adjuvant RCC) | `briefed` | Peptide-based PCV(± ipilimumab) in resected high-risk ccRCC; autologous tumour reactivity in 7/9; small-n. |
| `gainor-2024-t-cell-responses-individualized-neoantigen-therapy` | neoantigen mRNA immunogenicity (phase 1) | `briefed` | KEYNOTE-603: predicted neoantigen 238개 중 29.8% immunogenic; immunogenic 반응 중 84.5% de novo(ELISpot 기반). |
| `anurag-2022-proteogenomic-markers-chemotherapy-resistance-response` | chemo response (TNBC) + phosphoproteomics | `briefed` | pCR/non-pCR을 WES+TMT proteome/phosphoproteome으로 분해; 19q13 결실 신호. |
| `asuzu-2025-phosphoproteomic-dysregulation-drives-tumor-proliferation` | phosphoproteomics + signaling | `briefed` | PPP1R17–PP2A 축으로 phosphoproteome dysregulation의 druggability를 제시. |
| `cheng-2025-integrative-proteogenomic-characterization-wilms-tumor` | proteogenomics cohort (pediatric) | `briefed` | WT tumor–NAT multi-omics(WES+phosphoproteome)로 아형 및 EHMT2 후보 제시. |
| `zhao-2025-phosphoproteomic-acetylomic-characterization-colorectal-cancer` | phospho+acetyl multi-PTM | `briefed` | CRC inhibitor perturbation: off-target + PTM crosstalk. |
| `chong-2022-identification-tumor-antigens-immunopeptidomics` | immunopeptidomics (canonical/noncanonical) | `briefed` | Review: noncanonical 후보 확장 vs false positive 텐션 정리. |
| `chen-2026-enrichment-phosphorylated-glycosylated-mhc-peptides` | PTM-MHC peptides (phospho/glyco) | `briefed` | PTM-MHC peptide enrichment workflow. |
| `deng-2023-proteogenomic-characterization-cholangiocarcinoma` | proteogenomics cohort (CCA) | `briefed` | 대규모 CCA 코호트에서 WES+phosphoproteome 기반 subtype/kinase/면역 가설. |
| `haas-2024-proteogenomics-prostate-cancer-radioresistance` | proteogenomics + resistance | `briefed` | CF/HF fractionation-specific radioresistance + POLQ radiosensitizer 후보. |
| `han-2024-hla-based-neoantigen-presentation-pan-cancer-response` | HLA/presentation + ICI response | `briefed` | Presentation-aware score(HAPS)로 pan-cancer 반응 예측. |
| `muller-dott-2025-phosphoproteomic-kinase-activity-inference` | kinase activity inference (phosphoproteomics) | `briefed` | benchmarKIN 기반 벤치마크. |
| `memon-2024-clinical-molecular-features-acquired-resistance` | acquired resistance (NSCLC; PD-(L)1) | `briefed` | 획득내성 코호트에서 IFNγ signature 분기(stable vs increase)와 항원제시 경로 이상(B2M 등) 프레임을 제시. |
| `skoulidis-2024-ctla4-abrogates-keap1-stk11-resistance` | immunotherapy resistance (NSCLC; dual ICB) | `briefed` | KEAP1/STK11 변이 아형에서 CTLA-4 병용(dual ICB)로 내성 병목을 우회할 수 있다는 임상·기전 프레임. |
| `savage-2024-pan-cancer-proteogenomics-expands-landscape-therapeutic` | pan-cancer proteogenomics target landscape | `briefed` | CPTAC pan-cancer 기반 druggable dependency/synthetic lethality/항원 후보 우선순위화. |
| `shapiro-2025-sensitive-neoantigen-discovery-real-time-mutanome-guided` | neoantigen discovery + immunopeptidomics | `briefed` | NeoDiscMS: real-time NGS-guided immunopeptidomics acquisition. |
| `scheid-2025-mhcquant2-refines-immunopeptidomics-tumor-antigen` | immunopeptidomics pipeline | `briefed` | nf-core MHCquant2: 표준화 + benign reference 기반 antigen refinement. |
| `weber-2024-individualised-neoantigen-therapy-mrna-4157-v940` | personalized neoantigen therapy (clinical) | `briefed` | KEYNOTE-942 (phase 2b) adjuvant melanoma. |
| `khan-2026-integrative-phosphoproteomic-network-analysis-identifies` | phosphoproteomic network meta-analysis | `briefed` | 공개 phosphoproteomics 통합으로 kinase/network 가설 생성 예시. |
| `song-2024-proteogenomic-analysis-reveals-non-small-cell` | proteogenomics cohort (NSCLC; Korea) | `briefed` | 229명 multi-omics subtype + WGD/PI3K–Akt/TME/neoantigen 축. |
| `yu-2024-proteogenomic-analysis-cervical-cancer-reveals` | proteogenomics cohort (cervical; phospho+acetyl) | `briefed` | 139명; 3 subgroup + EP300–FOSL2 acetylation; PRKCB radioresponse 후보. |
| `qu-2024-integrated-proteogenomic-metabolomic-characterization-papillary` | proteogenomics + metabolomics (PTC recurrence) | `briefed` | 102명; recurrence risk subtype(대사형/면역형 등) 제시. |
| `tanaka-2024-proteogenomic-characterization-primary-colorectal-cancer` | proteogenomics cohort (CRC metastasis) | `briefed` | pCRC 154 vs 간 mCRC 142; hypoxia/stemness/immune-cold(항원제시 억제). |
| `zhang-2023-proteogenomics-clear-cell-renal-response-tyrosine-kinase-inhibitor` | treatment response (ccRCC; sunitinib) | `briefed` | responder/non-responder 라벨에서 mTOR/7q + phosphoproteome 기반 예측/해석. |
| `satpathy-2021-proteogenomic-portrait-lung-squamous-cell` | proteogenomics cohort (LSCC; multi-PTM + immune) | `briefed` | CPTAC LSCC; NSD3 driver 후보 및 phospho-Rb 기능 biomarker 프레임. |
| `dou-2020-proteogenomic-characterization-endometrial-carcinoma` | proteogenomics cohort (endometrial; phospho+acetyl + immune) | `briefed` | CPTAC EC; WES/WGS + PTM + MSI antigen presentation 텐션. |
| `ramberger-2024-proteogenomic-landscape-multiple-myeloma-reveals` | proteogenomics cohort (MM; nanopore WGS + phospho) | `briefed` | nanopore CNV + TMT phosphoproteome 통합; phospho 기반 risk stratification. |
| `keskin-2019-neoantigen-vaccine-generates-intratumoral-t` | neoantigen vaccine (clinical; GBM) | `briefed` | dexamethasone 교란 + scTCR 기반 blood→tumor 트래킹. |
| `yaeger-2023-molecular-characterization-acquired-resistance-krasg12c-egfr` | acquired resistance (CRC; KRASG12C+EGFR) | `briefed` | ctDNA 시계열; KRASG12C amplification; withdrawal 후 senescence/mTOR 전환. |
| `cao-2021-proteogenomic-characterization-pancreatic-ductal-adenocarcinoma` | proteogenomics cohort (PDAC; WGS/WES + phospho + glyco) | `briefed` | CPTAC PDAC 통합 리소스(140 cases + NAT + normal duct); purity/QC + multi-omics clustering 프레임. |
| `gillette-2020-proteogenomic-characterization-reveals-therapeutic-vulnerabilities` | proteogenomics cohort (LUAD; tumor+NAT; phospho+acetyl) | `briefed` | CPTAC LUAD(110 tumor + 101 NAT); 4-subgroup + STK11 immune-cold 축. |
| `krug-2020-proteogenomic-landscape-breast-cancer-tumorigenesis` | proteogenomics cohort (breast; phospho+acetyl) | `briefed` | PTM 보존 수집 코호트(122 fully analyzed)로 HER2/Rb/kinase 기능 상태를 proteogenomics로 재해석. |
| `clark-2019-integrated-proteogenomic-characterization-clear-cell` | proteogenomics cohort (ccRCC; phosphoproteome + immune subtypes) | `briefed` | CPTAC ccRCC(110 tumors + 84 NAT; 103 ccRCC 중심)에서 4개 immune subtype + phospho 모듈. |
| `chen-2023-global-impact-somatic-structural-variation-cancer-proteome` | SV (pan-cancer WGS) → protein consequence | `briefed` | WGS SV breakpoint가 단백질 발현 변화로 이어지는 비율(~25%)을 정량화; non-coding SV 해석 근거. |
| `chen-2026-global-impact-germline-structural-variation-cancer-proteome` | germline SV (pan-cancer) → protein consequence | `blocked` | 로컬 “PDF” 파일이 HTML로 확인되어 scientific ingest 불가(올바른 PDF 재확보 필요). |
| `dong-2024-integrative-proteogenomic-profiling-high-risk-prostate` | proteogenomics cohort (prostate) | `blocked` | 현재 로컬 PDF가 본문이 아닌 publisher correction이라 full article PDF가 필요. |

## Next up (PDF acquired; needs Cancer Multiomics brief)

2026-05 expansion batch 36편이 PDF만 확보된 상태로 deep-dive를 기다린다 — 토픽 허브의 [§6 2026-05 Expansion](../topics/cancer-multiomics-literature.md#6-2026-05-expansion-aispatialecdnacar-t-보강-45편) 참조.

## 2026-05-10 Expansion batch (Notion seeds + OpenAlex relateds, 45편)

Notion 'Cancer Multiomics > 참고 논문 및 아이디어' 27편 + OpenAlex citation graph로 발굴한 score≥6 관련논문 18편을 한 번에 ingest. 모든 stub은 `topic: cancer-multiomics-literature`, `discovery_method` (manual-notion or openalex-citation-graph), 그리고 (related인 경우) `related_to_seeds` frontmatter를 갖는다. 자동 다운로드 36편 / manual_pending 9편.

**Discovery 메커니즘**: `scripts/ingest/find_related_via_openalex.py` — DOI seed 27편 → OpenAlex Work fetch (20 resolved, 7 미등록 DOI) → referenced_works + related_works 합집합 852개 → cancer/multiomics 키워드 필터 444개 → 2023+ 최근논문 score≥3 shortlist 50개 → 사용자 승인 후 Top-18 (score≥6) ingest.

| Basename | Source | Status | Notes |
| --- | --- | --- | --- |
| `altenburger-2026-lymphoid-chemokine-cd8-priming-effector` | notion | `needs-deep-dive` | Lymphoid chemokine signalling on CD8+ T-cell priming time. |
| `balan-2026-generative-reference-grammar-tcr-repertoires-cancer` | notion | `blocked` | bioRxiv 2026 DOI 미등록 (manual_pending). TCR generative reference grammar. |
| `bilous-2026-xenium-sensitivity-specificity-signal-contamination` | notion | `needs-deep-dive` | Xenium platform benchmarking. |
| `chauquet-2026-twas-signature-matching-drug-prioritisation-benchmark` | notion | `needs-deep-dive` | TWAS-based drug prioritisation benchmark. |
| `cheng-2025-censegnet-centrosome-phenotyping-cancer-tissues` | notion | `needs-deep-dive` | CenSegNet centrosome phenotyping framework. |
| `cui-2026-haiku-tri-modal-spatial-biology-histology` | notion | `needs-deep-dive` | Haiku tri-modal spatial+histology bridge. |
| `deutsch-2026-expanding-human-proteome-peptideins-noncanonical-orfs` | notion | `needs-deep-dive` | Non-canonical ORF peptideins. |
| `ge-2026-extra-lineage-tissue-programs-pancreatic-cancer-transcriptional` | notion | `blocked` | bioRxiv 2026 DOI 미등록 (manual_pending). Extra-lineage PDAC programs. |
| `guo-2026-larger-models-scaling-benchmark-drug-discovery` | notion | `needs-deep-dive` | Drug discovery scaling benchmark. |
| `hartung-2022-caddie-cancer-driver-drug-repurposing-platform` | notion | `needs-deep-dive` | CADDIE network-medicine platform. |
| `jia-2026-drugclip-contrastive-protein-ligand-genome-scale` | notion | `needs-deep-dive` | DrugCLIP contrastive virtual screening. |
| `kersting-2025-nf-core-disease-module-network-medicine` | notion | `needs-deep-dive` | nf-core network-medicine pipeline. |
| `khoraminia-2026-predicting-bladder-molecular-subtypes-bcg-response` | notion | `needs-deep-dive` | Histology→bladder cancer subtype + BCG response. |
| `llora-batlle-2024-10x-flex-fixed-xenograft-single-cell` | notion | `needs-deep-dive` | 10x Flex on FFPE xenografts. |
| `ohlan-2025-molgene-e-inverse-molecular-design-transcriptomic-reversal` | notion | `needs-deep-dive` | MolGene-E inverse molecular design. |
| `sakai-2026-postn-cafs-chemoradiotherapy-resistance-rectal-cancer` | notion | `blocked` | bioRxiv 2026 DOI 미등록 (manual_pending). POSTN+ CAFs in rectal cancer. |
| `savage-2026-klf2-runx2-memory-like-car-t` | notion | `needs-deep-dive` | KLF2/RUNX2 memory-like CAR-T design. |
| `tong-2026-multimodal-lincs-pan-cancer-hdac-inhibitor` | notion | `needs-deep-dive` | LINCS L1000 multimodal HDAC repositioning. |
| `townsend-2026-cross-assay-rna-modeling-cancer-biomarker-discovery` | notion | `blocked` | bioRxiv 2026 DOI 미등록 (manual_pending). Cross-assay RNA biomarker modeling. |
| `tran-2026-phoenix-pan-cancer-virtual-spatial-transcriptomics` | notion | `needs-deep-dive` | Phoenix virtual spatial transcriptomics. |
| `tsepilov-2026-open-targets-gentropy-pleiotropy-gwas-prioritisation` | notion | `blocked` | bioRxiv 2026 DOI 미등록 (manual_pending). Gentropy GWAS pleiotropy. |
| `wang-2025-extrachromosomal-dna-cancer-evolutionary-pathway` | notion | `needs-deep-dive` | ecDNA evolutionary pathway perspective. |
| `wu-2026-reimagining-human-centric-drug-development-nams` | notion | `needs-deep-dive` | NAMs reimagining drug development. |
| `xing-2026-deep-learning-de-novo-transcriptional-phenotype-reversal` | notion | `blocked` | Cell Press anti-bot (manual_pending). DL de novo phenotype reversal. |
| `zhang-2026-non-invasive-tumour-microenvironment-spatial-ecotypes` | notion | `needs-deep-dive` | Non-invasive TME spatial ecotypes. |
| `zhang-2026-proteinaligner-tri-modal-contrastive-protein-language` | notion | `blocked` | Cell Press anti-bot (manual_pending). ProteinAligner tri-modal PLM. |
| `zhang-2026-systematically-decoding-pathological-morphologies-multimodal-embedding` | notion | `needs-deep-dive` | Multimodal embedding for pathology decoding. |
| `chen-2024-towards-general-purpose-foundation-model` | openalex | `needs-deep-dive` | Nat Med pathology foundation model (cited 1019). |
| `gonzalez-2023-parallel-sequencing-extrachromosomal-circular-dnas` | openalex | `needs-deep-dive` | Single-cell ecDNA + transcriptome parallel sequencing. |
| `gonzalezblas-2023-scenic-single-cell-multiomic-inference` | openalex | `needs-deep-dive` | SCENIC+ single-cell multiomic GRN inference. |
| `hayes-2025-simulating-500-million-years-evolution` | openalex | `needs-deep-dive` | ESM3 protein language model. |
| `heiser-2023-molecular-cartography-uncovers-evolutionary-microenvironmental` | openalex | `blocked` | Cell 2023 (Cell Press anti-bot, manual_pending; PMC OA available). CRC molecular cartography. |
| `heumos-2023-best-practices-single-cell-analysis` | openalex | `needs-deep-dive` | Single-cell best practices review. |
| `hoang-2024-deep-learning-framework-predict-cancer` | openalex | `needs-deep-dive` | DL cancer treatment response from H&E. |
| `hoang-2024-prediction-dna-methylation-based-tumor` | openalex | `needs-deep-dive` | DL methylation tumor type from histology (CNS). |
| `hung-2024-coordinated-inheritance-extrachromosomal-dnas-cancer` | openalex | `needs-deep-dive` | ecDNA coordinated inheritance. |
| `janesick-2023-high-resolution-mapping-tumor-microenvironment` | openalex | `needs-deep-dive` | Xenium TME high-resolution mapping. |
| `joung-2023-transcription-factor-atlas-directed-differentiation` | openalex | `blocked` | Cell 2023 (Cell Press anti-bot, manual_pending; PMC OA available). TF atlas (3500 isoforms). |
| `long-2023-spatially-informed-clustering-integration-deconvolution` | openalex | `needs-deep-dive` | GraphST spatial transcriptomics tool. |
| `orlicmilacic-2023-reactome-pathway-knowledgebase-2024` | openalex | `needs-deep-dive` | Reactome 2024 update. |
| `pongor-2023-extrachromosomal-dna-amplification-contributes-small` | openalex | `needs-deep-dive` | ecDNA SCLC heterogeneity. |
| `sande-2023-applications-single-cell-rna-sequencing` | openalex | `needs-deep-dive` | scRNA-seq drug discovery applications. |
| `steyaert-2023-multimodal-data-fusion-cancer-biomarker` | openalex | `needs-deep-dive` | Multimodal fusion review for cancer biomarkers. |
| `subramanian-2024-sarcoma-microenvironment-cell-states-ecosystems` | openalex | `needs-deep-dive` | Sarcoma microenvironment ecosystems + IO response. |
| `xue-2023-schwann-cells-regulate-tumor-cells` | openalex | `needs-deep-dive` | Schwann cells in PDAC microenvironment. |

## Discovery candidates (PDF pending; download requires network-enabled resolver run)

- `klomp-2024-erk-regulated-phosphoproteome-kras-cancer` - Science 2024 (ERK-regulated phosphoproteome; KRAS-mutant). 현재 PMC 접근이 자동화 환경에서 차단되어 PDF 확보가 막힘(대안 경로 필요).
- `suhre-2024-nanoparticle-enrichment-proteomics-pqtl-mapping` - Nat Commun 2024 pQTL mapping (MS-based; Proteograph workflow) 후보.
- `wang-2024-fine-mapped-blood-eqtls-pqtls-1405-humans` - Nat Genet 2024 blood eQTL/pQTL fine-mapping (method/architecture 참고용; 암 특이 코호트는 아님).
- `van-bentum-2025-spike-in-phosphoproteomics-mek-inhibition` - Nat Commun 2025 spike-in phosphoproteomics + MEK inhibition 후보.
- (제외/중복) `mullerdott-2025-comprehensive-evaluation-phosphoproteomic-based-kinase-activity`는 본문이 아니라 publisher correction PDF로 확인되어, Cancer Multiomics 코퍼스 카운트에는 포함하지 않고 원문은 `muller-dott-2025-phosphoproteomic-kinase-activity-inference`로 관리한다.

## Connections

- [Cancer Multiomics Literature Monitor](../topics/cancer-multiomics-literature.md)

## Sources

- The linked `wiki/sources/*` pages and their local PDFs under `raw/inbox/papers/`.
