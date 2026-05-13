---
title: "Proteogenomic decoding of chemotherapy resistance in triple-negative breast cancer"
authors:
  - "Lee DK"
  - "Hwang Y"
  - "Ryu W-J"
  - "Kim G-U"
  - "Yun HM"
  - "Park SY"
  - "Lee JD"
  - "Han HJ"
  - "Kim GM"
  - "Kim K-H"
  - "Park JB"
  - "Kim MJ"
  - "Koo JS"
  - "Kim JY"
  - "Park HS"
  - "Kim SI"
  - "Gee HY"
  - "Park S"
  - "Sohn J"
year: 2026
journal: "Genome Biology"
doi: "10.1186/s13059-026-04053-7"
url: "https://link.springer.com/article/10.1186/s13059-026-04053-7"
pdf: "raw/inbox/papers/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.pdf"
paper_kind: translational
cancer_types:
  - triple-negative-breast-cancer
modalities:
  - proteogenomics
  - phosphoproteomics
  - wes
  - rna-seq
  - tmt
themes:
  - chemotherapy-resistance
  - neoadjuvant-chemotherapy
  - pcr-prediction
  - asian-cohort
  - druggable-target
discovery_method: user-shared
topic: cancer-multiomics-literature
tags:
  - source
  - tnbc
  - proteogenomics
  - phosphoproteomics
  - neoadjuvant
  - korean-cohort
  - aurkb
  - itgb8
  - grk2
  - akr1c2
  - abca13
---

# Proteogenomic decoding of chemotherapy resistance in triple-negative breast cancer

_Genome Biology (2026) 27:125. Received 2025-08-08, Accepted 2026-03-20, Published online 2026-04-14._
· DOI: [10.1186/s13059-026-04053-7](https://doi.org/10.1186/s13059-026-04053-7)
· Yonsei University College of Medicine (Severance Hospital, Seoul) + 협력기관 다수.

## Summary

Lee et al.은 anthracycline + taxane 기반 neoadjuvant chemotherapy(NAC)를 받은 stage II–III TNBC 환자 50명의 한국인 코호트를 대상으로 baseline(n=41) 및 post-treatment residual tumor(n=22 paired protein, 31 collected) 샘플에서 WES + RNA-seq + TMT global proteome + phosphoproteome을 통합한 prospective 다중오믹스 분석을 수행했다. NMF 통합 클러스터링으로 5개 subtype(immune-enriched, xenobiotic metabolism, EMT, MYC-dependent, mesenchymal+estrogen)을 정의했고, 이는 Lehmann 분류와 부분적으로만 일치했다(pCR 55.6%/0%/0%/—/— 분포). 비반응(non-pCR) 메커니즘으로 (1) **estrogen response 단백질 시그니처 + GRK2 PTM-SEA 활성**(GSVA high vs low pCR 14.3% vs 48.1%, P=0.0328), (2) **ITGB8를 포함한 7p21 cytoband copy gain**(pCR 0%/12.6%/41.7%/80% by gain/diploid/shallow loss/deep loss, P=0.036), (3) **doxorubicin 대사 AKR1C2 + 약물 efflux ABCA13 상향**(Lehmann IM subtype 내부 36.8% non-pCR 설명)이라는 세 축을 도출했다. paired pre/post 분석에서는 residual tumor에 EMT/myogenesis 시그니처와 **AURKB phosphoproteome 신호**가 일관되게 enriched되었고, 저자들은 (i) GRK2 inhibitor(βARK1 inhibitor) + paclitaxel은 MDA-MB-231에서 SynergyFinder 3.0 Bliss 8.08의 시너지, (ii) Aurora B inhibitor barasertib (10 nM) + paclitaxel은 MDA-MB-468·HCC1937·환자 유래 organoid SBO-72에서 cell viability 감소를 in vitro로 검증했다. 다섯 가지 저항인자(estrogen high / GRK2 high / no ITGB8 loss / AKR1C2 high / ABCA13 high)를 통합한 로지스틱 회귀모델은 non-pCR 예측에서 AUC **0.946**으로 Lehmann 분류(AUC 0.781) 및 Lehmann+ESTIMATE immune score(AUC 0.818)를 능가했다. 본 연구는 한국인 TNBC 코호트라는 인종 특수성과 anthracycline-taxane 중심 regimen이라는 임상 맥락에서 proteogenomic NAC response biomarker + druggable target(AURKB·GRK2·ITGB8 ADC)을 모두 제시한 첫 보고이다.

## Key Points

### 코호트 / 임상 디자인

- **환자 50명, stage II–III TNBC**(ER-/PR-/HER2-IHC 0–1 or 2+ with negative ISH; Severance Hospital), Sept 2020 – July 2021 prospective enrollment, IRB 4-2020-0473.
- Median age 48 (range 26–69), clinical T2 92%, N0 58% (Table S1; PDF p.5).
- **NAC regimen 분포**: AC→weekly paclitaxel n=36 (72%), AC→docetaxel n=6, weekly paclitaxel+carboplatin (AUC 5)→AC n=6, FEC-docetaxel n=2 — 즉 **carboplatin 사용은 6/50 (12%)에 불과**(저자 본문 인용 — Anurag et al. 코호트의 100% carboplatin과 명시적 대비).
- 44명이 chemo schedule 완주, 6명은 disease progression으로 중단. pCR(ypT0 ypN0) **19명(38%)**, progression 6명(12%), recurrence 7명(14%), median follow-up 33.2 months.
- Baseline biopsy 50개 중 **41개(82%)에서 WES + RNA-seq + TMT proteome 모두 사용 가능**; non-pCR 환자에서 surgical residual tumor 31개 채집, 이 중 protein-paired 분석은 n=22.
- Cell line/organoid 실험은 별도 IRB 4-2023-0098(SBO-72 organoid 환자 유래) 승인.

### 데이터 레이어 / QC 수치

- **데이터셋 규모**: 25,988개 gene CNA, 19,853개 gene transcript, 10,457개 protein, 31,258개 phosphosite (5,373 proteins). TMT 11-plex.
- Tumor purity는 RNA 추정치와 proteomic 추정치가 매우 높은 상관(본문 PDF p.6 — exact r 미명시; supplementary Fig S2).
- **mRNA-protein correlation**: 93.8%가 양의 상관, 그 중 62.0%가 P<0.01 유의 (본문).
- Lehmann subtype assignment: 41 baseline에 대해 TNBCtype tool 적용 (BL1/BL2/IM/M/MSL/LAR/UNS 7-class).

### NMF 통합 클러스터링 (5 subtype)

- **Optimal k=5**, brunet method, 50 iterations (NMF R v0.28). CNA(GISTIC2 absolute) + RNA + protein + phosphoprotein 4 modality concatenated.
- Cluster 1 — **immune-enriched** (n=9): pCR 55.6% (5/9). HALLMARK immune/IFN signature 강함.
- Cluster 2 — **xenobiotic metabolism** (n=2): pCR 0% (0/2). AKR1C2 RNA 가장 높음.
- Cluster 3 — **EMT** (n=7): pCR 0% (0/7).
- Cluster 4 — **MYC-dependent** (n=12): MYC targets V1/V2 + mTORC1 + E2F targets enrich.
- Cluster 5 — **mesenchymal + estrogen** (n=11): estrogen response + EMT mix.
- 5개 cluster 합 41 ✓.
- **METABRIC 외부 validation**: 258개 TNBC 중 197(76.3%) NMF cluster assignable (k-NN 기반 mapping); 동일 immune/EMT/estrogen prognostic pattern 재현.

### 저항 메커니즘 ① — Estrogen response + GRK2

- ER/PR IHC 모두 음성이지만 **GSEA Hallmark "Estrogen response early/late" 단백질 시그니처는 non-pCR에서 유의 enrich**.
- Estrogen response GSVA high vs low: pCR 14.3% vs 48.1%, P=0.0328 (Anurag et al. 외부 cohort + Gong & Jiang TNBC cohort에서도 일관 — supplementary Fig S7).
- **PTM-SEA**(phosphosite-level): non-pCR에서 GRK2 + GRK5 + RAPAMYCIN + CDK2 cluster enriched; pCR에서 GSK3β + IL2 + CCR7 + SYK + YES1 enriched.
- **GRK2 기능 검증**: estradiol 처리 MDA-MB-468에서 GRK2 단백질 증가; βARK1 inhibitor (Sigma 24269-96-3) + paclitaxel concentration gradient 72h MTT assay → MDA-MB-231에서 SynergyFinder 3.0 **Bliss synergy score 8.08**.

### 저항 메커니즘 ② — ITGB8 / 7p21 cytoband CNA

- Cytoband enrichment: transcriptomics + proteomics 양쪽에서 **7p21이 non-pCR로 가장 강하게 enriched**.
- 7p21 core enrichment gene + Cancer Surfaceome Atlas 교집합 3개: **ITGB8, THSD7A, TSPAN13** (ITGB8: cell-surface protein score 15.5, Δlog2 CN 4.794).
- **ITGB8 CN status별 pCR rate**: deep loss (n=5) **80%**, shallow loss (n=12) **41.7%**, diploid (n=8) **12.6%**, shallow gain (n=16) **0%**, P=0.036.
- ITGB8 GFP overexpression in MDA-MB-468 (Addgene #205093, Lipofectamine LTX) → GSEA Hallmark NES: IFN-α response -1.73 (FDR=0.005), IFN-γ response -2.31, inflammatory response -2.52, TNF-α NF-κB -3.06; **즉 ITGB8 발현은 종양세포의 면역 시그니처를 직접 억압**.
- **TCGA TNBC validation** (n=154): ITGB8 CN deletion (n=39) vs no deletion (n=115) OS Kaplan-Meier P=0.0516 — deletion이 생존 우위.

### 저항 메커니즘 ③ — Doxorubicin metabolism + drug efflux (IM subtype)

- Lehmann IM subtype 중 36.8%는 pCR 미달 — 같은 IM 안에서도 내성 분기.
- **AKR1C2** (aldo-keto reductase family, doxorubicin metabolism) RNA non-pCR up; cluster 2(xenobiotic)에서 가장 높음.
- **ABCA13** (ATP-binding cassette efflux transporter) RNA non-pCR up; cluster 4/5에서 enriched.
- METABRIC IM subtype 외부 검증: AKR1C2 high → relapse-free survival 악화 P=0.0033; ABCA13는 worse survival trend (P=0.2225, NS).

### 저항 메커니즘 ④ — Post-treatment AURKB phosphoproteome (paired pre/post n=22)

- Residual tumor에서 GSEA Hallmark EMT + myogenesis + xenobiotic metabolism + coagulation + complement + epithelial-mesenchymal transition 상향; baseline에서는 mTORC1, MYC targets V1/V2, E2F targets, G2M checkpoint 상향.
- PTM-SEA post-treatment enriched: **CGK2 (CKII?) + Aurora kinase B (AURKB) + MAP3K3 + MAPKAPK3 + BAFILOMYCIN A1 + LENALIDOMIDE signature**; pre-treatment enriched: PD-0332991 (palbociclib), REGORAFENIB, MAPK7/ERK5, HIPK1/HIPK3.
- **AURKB 기능 검증**: barasertib (Aurora B inhibitor, Selleckchem S1147, 10 nM) + paclitaxel 농도구배 72h MTT → MDA-MB-468 viability 명확한 시너지(Fig 5G). MDA-MB-231 + HCC1937에서도 doxorubicin 환경에서 barasertib 단독으로 viability 감소 (Fig S13A,B). TNBC organoid SBO-72에서도 barasertib+paclitaxel viability 감소 (CellTiter-Glo 3D, Fig S13C).

### 통합 예측 모델

- 5개 저항인자 logistic regression 모델 — AUC **0.946** (Lehmann 0.781 / Lehmann + ESTIMATE immune score 0.818 대비 우월).
- Stromal proportion / ESTIMATE stromal score는 5개 인자 분포에 영향 없음 (Fig S14).
- non-pCR 80.7% (21/26)가 ≥1 저항인자 보유, 그중 10/21이 ≥2 보유; pCR 환자는 26.7%만 1개 인자 보유.
- 대표 사례: T39 (51세, 3 risk factors: high estrogen GSVA + high GRK2 PTM-SEA + no ITGB8 loss) — pac+carbo로 progression → AC+RT + nab-pac+atezolizumab으로 2022-01 lung metastasis 처리; T47 (45세, 1 risk factor) — AC→docetaxel → non-pCR → adjuvant capecitabine → 2022-12 lung metastasis.

### 데이터 가용성

- WES PRJNA1422845, RNA-seq PRJNA1422844 (NCBI Bioproject).
- Proteome PDC000695, phosphoproteome PDC000696 (CPTAC PDC).
- Author 명시 — competing interest 없음.

## Methods

- **WES**: MagNA Pure 24 (Roche) extraction → Illumina sequencing, GISTIC2 absolute CN → NMF input.
- **RNA-seq**: RNeasy Mini Kit + QIAcube (Qiagen); TNBCtype tool ([https://www.vumc.org/pietenpol-lab/tools](https://www.vumc.org/pietenpol-lab/tools)) for Lehmann subtype; PAM50 model for intrinsic subtype.
- **TMT proteome / phosphoproteome**: TMT 11-plex labeling; 10,457 proteins, 31,258 phosphosites identified. MaxQuant standard workflow (참조: 본문 ref [62] 동일 방법).
- **GSEA / GSVA / PTM-SEA**: MSigDB Hallmark + C6 oncogenic (proteome); ssGSEA R package for GSVA per-sample; PTM-SEA (Krug Mol Cell Proteomics 2019, ref [64]) for phosphoprotein 차원.
- **NMF clustering**: NMF R v0.28, brunet method, 50 nrun, rank=2:8; cophenetic/dispersion/consensus stability metric 기반 k=5 선정. 4 modality concat normalize 후 non-neg shift.
- **iKiP/Kinase-Library mapping은 본 논문에서 사용하지 않음** — PTM-SEA만 사용.
- **In vitro 검증 세포주**: MDA-MB-231 (HTB-26), MDA-MB-468 (HTB-132), HCC1937 (CRL-2336) — 모두 ATCC, RPMI-1640 + 10% FBS + 1% P/S, STR profiling으로 인증.
- **약물**: Doxorubicin (Sigma D1515, water), carboplatin (Selleckchem S1215, water), Barasertib (Selleckchem S1147, DMSO), β-estradiol (Sigma E2257, 100% ethanol + advanced DMEM/F-12), βARK1 inhibitor (Sigma 24269-96-3, GRK2 inhibitor).
- **Cell viability assay**: 6×10^3 cells/well 96-well, 72h treat, MTT 570 nm absorbance, Bliss synergy via SynergyFinder 3.0.
- **ITGB8 overexpression**: pEGFP-C2-entry plasmid + GFP-tagged human integrin β8 plasmid (Addgene #205093), Lipofectamine LTX, G418 (0.4–1 mg/mL) selection → stable clones.
- **Organoid**: SBO-72 환자 유래 organoid (Yonsei Cancer Center; IRB 4-2023-0098), TrypLE Express dissociation, AdDF+++ medium + 1.5×10^4 cells in 20 μL BME dome, 48-well, 72h barasertib+doxorubicin/carboplatin treatment, CellTiter-Glo 3D ATP assay.
- **Survival analysis**: Kaplan-Meier + log-rank (TCGA TNBC n=154, METABRIC IM subtype n=58); 통계는 모두 R 4.3.1 + GraphPad Prism + SPSS + GENE-E, two-sided P<0.05.

## Cancer Multiomics Project Relevance

본 논문은 한미약품-Yonsei 한미암 표적항암치료제 멀티오믹스 프로젝트와 **(a) 코호트 인종 매칭, (b) 임상 시나리오 직결성, (c) druggable target 동반 검증, (d) biomarker 패널 prototype**의 네 차원에서 직접 활용 여지가 있다. 아래는 모두 본문 결과 기반의 적용 후보이며, 단순화 / 자동 일반화는 피한다.

- **한국인 TNBC 코호트(Severance n=50, IRB 4-2020-0473)의 proteogenomic 레퍼런스 데이터**: 한미암 한국인 환자 baseline NAC pre-treatment biopsy를 본 데이터셋(PRJNA1422845/1422844, PDC000695/696)과 동일 modality 스택(WES+RNA-seq+TMT 단백체+인산화단백체)으로 비교 가능. NMF 5-subtype 할당이 한미암 코호트에서 재현되는지 + pCR 분포가 유사한지 검증할 수 있는 첫 한국인 reference.
- **anthracycline+taxane regimen 데이터 보유** — 본 코호트에서 AC→weekly paclitaxel이 72% (n=36), 즉 carboplatin 비포함 표준 NAC가 압도적인 한국인 임상 현실을 그대로 반영. 한미암 코호트가 동일 regimen 환자를 받는다면 본 5-resistance factor 모델(AUC 0.946)을 즉시 외부 검증 후보로 쓸 수 있다(반대로 carboplatin 포함 환자는 Anurag et al. 데이터로 비교).
- **AURKB + paclitaxel 병용을 druggable resistance target으로 제안**: post-treatment residual tumor에서 AURKB phosphoproteome 신호가 일관되게 enriched이고, MDA-MB-468·HCC1937·organoid SBO-72에서 barasertib(10 nM) + paclitaxel 시너지가 검증됨. 한미암에서 진행 중인 표적항암제 파이프라인 중 Aurora kinase 계열(또는 mitotic spindle 표적) 후보가 있다면, "residual disease eradication" 적응증 가설을 본 데이터로 grounding 가능. 단, 본 논문의 시너지는 **세포주/organoid 수준이며 임상 데이터는 아님** — 한미암이 후속 trial을 디자인할 경우 anthracycline 미반응 잔존 종양 subset이 일차 표적이 된다.
- **GRK2(βARK) inhibitor + paclitaxel — Bliss 8.08 시너지 (MDA-MB-231)**: estrogen response 단백질 시그니처가 ER/PR IHC 음성에서도 유의하므로 IHC 음성 = 호르몬 신호 부재 가정은 단백체 레벨에서는 깨진다. estrogen→GRK2 축이 한미암 코호트에서도 단백체로 잡힌다면 GRK2를 표적하는 후보 또는 estrogen 단백 시그니처 high subset에 selective ER degrader (SERD) 재해석을 시도해볼 수 있다 — 이는 가설이며 임상 검증 미진행.
- **ITGB8 / 7p21 CN deep loss → pCR 80%의 정량적 biomarker**: Cancer Surfaceome Atlas 교차 후 ITGB8/THSD7A/TSPAN13 셋 모두 cell-surface 노출 → **ADC 표적**으로의 평가가 가능하다. 본문은 integrin β-targeting ADC(SGN-B6A, ref [50])가 이미 개발 중임을 명시. 한미암에서 ITGB8 또는 7p21 cluster를 표적하는 ADC 후보를 보유 중이라면, 한국인 TNBC에서 CN deep loss 환자(약 10%, 본 코호트 n=5)는 **NAC 단독으로도 pCR 80%** — 즉 ADC 추가가 정당화되는 환자는 CN gain (n=16, pCR 0%) 또는 diploid (n=8, pCR 12.6%) subset이며, "환자 stratification" 입력값이 분명히 정해진다.
- **AKR1C2 + ABCA13 — Lehmann IM subtype 내부 36.8% non-pCR을 설명하는 분자 마커**: 한미암 환자의 baseline RNA-seq에서 AKR1C2 / ABCA13 발현 측정만으로 doxorubicin metabolism / efflux 메커니즘 기반 위험군을 분별할 수 있다. METABRIC IM 외부 검증(P=0.0033)이 RFS까지 연결되므로 BSA / 용량 조정·약물 교체 의사결정을 보조하는 baseline 마커 패널의 후보가 된다.
- **공개 데이터 재활용**: PDC000695/696 는 phosphoproteome 5,373 단백질 31,258 sites — 한미암 자체 데이터 생성 전 in silico kinase activity inference / PTM-SEA / iKiP 매핑 실험을 위한 동아시아 baseline으로 즉시 활용 가능.

**한계 (본문 명시)**: (i) n=50 단일 기관 prospective, (ii) pembrolizumab 추가 regimen 미포함(한국 승인 timeline 사유), (iii) NMF cluster 2/3 sample size 매우 작음 (n=2, 7), (iv) AUC 0.946은 same-cohort logistic regression 결과 — 외부 cohort에서의 prospective AUC는 미보고, (v) AURKB / GRK2 / ITGB8 함수 검증은 모두 cell line + organoid in vitro 수준.

## Connections

- [Cancer Multiomics Literature Topic Hub](../topics/cancer-multiomics-literature.md) — Section 1 WGS/Proteogenomics 통합 기반.
- [Anurag 2022 - TNBC Neoadjuvant Chemo Response (WES + Phosphoproteome)](../analyses/cancer-multiomics-literature/anurag-2022-proteogenomic-markers-chemotherapy-resistance-response.md) — 본 논문이 carboplatin 100% 사용을 명시적으로 비교 대상으로 언급한 선행 코호트.
- [Krug 2020 - Breast Cancer Proteogenomics (PTM-preserved; HER2/Rb/kinase)](../analyses/cancer-multiomics-literature/krug-2020-proteogenomic-landscape-breast-cancer-tumorigenesis.md) — 본 논문 ref [43]; PTM 보존 proteogenomic baseline.
- [Song 2024 - NSCLC Multi-Omics Subtypes (한국인 코호트)](../analyses/cancer-multiomics-literature/song-2024-proteogenomic-analysis-reveals-non-small-cell.md) — 동일 Yonsei 그룹의 한국인 NSCLC proteogenomic 코호트(229명).
- [Cancer Multiomics Corpus Queue](../analyses/cancer-multiomics-corpus-queue.md)

## Sources

- Local PDF: `raw/inbox/papers/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.pdf` (4.3 MB, 25 pages).
- Springer/BMC OA: <https://link.springer.com/article/10.1186/s13059-026-04053-7>
- WES: NCBI Bioproject [PRJNA1422845](https://www.ncbi.nlm.nih.gov/bioproject/?term=PRJNA1422845)
- RNA-seq: NCBI Bioproject [PRJNA1422844](https://www.ncbi.nlm.nih.gov/bioproject/?term=PRJNA1422844)
- Proteome: CPTAC PDC [PDC000695](https://pdc.cancer.gov/pdc/study/PDC000695)
- Phosphoproteome: CPTAC PDC [PDC000696](https://pdc.cancer.gov/pdc/study/PDC000696)
