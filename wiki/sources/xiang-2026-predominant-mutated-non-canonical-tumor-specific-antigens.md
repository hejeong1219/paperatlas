---
title: "Predominant mutated non-canonical tumor-specific antigens identified by proteogenomics demonstrate immunogenicity and tumor suppression in CRC"
authors:
  - "Haitao Xiang"
  - "Xiangyu Guan"
  - "Yaohua Wei"
  - "Shuzhen Luo"
  - "Haibo Zhang"
  - "Fanyu Bu"
  - "Feng Gao"
  - "Xuan Dong"
year: 2025
journal: "Cell Genomics"
doi: "10.1016/j.xgen.2025.101062"
pmid: "41237784"
pmcid: "PMC12926194"
paper_kind: proteogenomic
pdf: "raw/inbox/papers/xiang-2026-predominant-mutated-non-canonical-tumor-specific-antigens.pdf"
local_source: "raw/inbox/papers/xiang-2026-predominant-mutated-non-canonical-tumor-specific-antigens.html"
pdf_status: complete
cancer_types:
  - "colorectal-cancer"
modalities:
  - "wgs"
  - "rna-seq"
  - "ip-ms-immunopeptidomics"
  - "ribo-seq"
  - "scrna-seq"
topic: bcell-neoantigen
tags:
  - "neoantigen"
  - "non-canonical-tsa"
  - "immunopeptidomics"
  - "hypermutated-crc"
  - "vaccine"
  - "chinese-cohort"
  - "pmid-41237784"
themes:
  - "neoantigen-discovery"
  - "non-canonical-orf"
  - "immunopeptidomics"
  - "hypermutated-msi-h"
  - "personalized-vaccine"
  - "asian-cohort"
---
# Predominant mutated non-canonical tumor-specific antigens identified by proteogenomics demonstrate immunogenicity and tumor suppression in CRC

_Cell Genomics, 2025;6(1):101062 (published 2025-11-13; corrected 2026-01-22;6(2):101163)._ PMID: [41237784](https://pubmed.ncbi.nlm.nih.gov/41237784/).

DOI: [10.1016/j.xgen.2025.101062](https://doi.org/10.1016/j.xgen.2025.101062)

## Summary

Xiang et al.는 결직장암(CRC)에서 traditional exome-기반 neoantigen 발굴이 놓치는 non-canonical TSA(intergenic / intronic / 비-coding intronic 등 non-coding origin)를 정량화하기 위해 WGS + RNA-seq + MHC class I IP-MS를 통합한 proteogenomic 파이프라인을 적용했다. Sixth Affiliated Hospital of Sun Yat-sen University의 10 쌍 CRC tumor + 인접 정상 조직에서 환자별 mutant protein DB(6-frame translation, 10개 start codon 후보)와 two-stage DB search(Comet / MSFragger / MaxQuant) + de novo(Casanovo / PepNet / pNovo3 / SMSNet)를 결합해 96개 고유 mutated MHC class I neo-epitope(평균 9.6/환자, 전통 ~1/환자 대비)를 식별했다. 그 중 80.21%(77/96)가 non-coding region에서 유래했고, 86.2%가 hypermutated(TMB>25) CRC에 집중되며 intergenic + intronic 영역이 dominant했다. MC38 mouse 모델에서 11개 non-canonical 후보 중 6개(intronic 3/6, intergenic 3/5)가 IFN-γ ELISpot 양성이었고, 이 6개 + 1개 추가로 구성한 7-peptide pool 백신은 PBS / CtrlVax 대비 종양 성장을 유의하게 억제했으며 α-CD8β depletion으로 효과가 사라졌다. scRNA-seq(67,471 cell)에서 Vax 그룹의 cytotoxic CD8⁺ T cell 비율 0.40%(PBS 0.08%) 및 CD8/Treg ratio 3.93(PBS 2.39)으로 TME activation을 확인했다.

## Key Points

### 코호트와 데이터 구성
- 10명 paired CRC tumor + 인접 정상 (Sixth Affiliated Hospital of Sun Yat-sen University, Guangzhou; Chinese cohort). 추가로 cell line 외부 벤치마크 2개(HCT116 CRC, HCC1143 BC). MC38 mouse syngeneic CRC 모델 in vivo validation.
- 각 환자에 대해 WGS(somatic SNV/indel/AS/fusion) + RNA-seq + MHC class I IP-MS를 모두 측정. 환자별 mutant protein DB는 mutation site 주변 6-frame translation(24–45 bp window)으로 구성하고 ATG + 9개 single-nt substitution(총 10개) 후보 start codon으로 ORF 예측.
- 1% FDR + ΔRT<300s + SSS>0.4 필터링 후 10 CRC tumor에서 총 **26,666 epitope** 식별. Two-stage DB search로 DB 크기 76.55% 축소 + 1% FDR 유지하며 **59,442 peptides**(총 peptide 2.21× / novel peptide 1.33× 증가). 3 search engine 교차 검증 분포: 29.19%(7,783) 3-engine 합의, 37.03%(9,872) 1-engine 단독.

### Two-stage DB search 벤치마크
- HCT116 외부 데이터셋 적용 시 기존 epitope의 **79.61% 회수 + 총 epitope 4.88배 증가**; HCC1143은 **96.44% 회수 + 4.68배 증가**. 두 cell line 모두 기존 결과 대부분 보존하면서 식별 폭 확장.
- 무작위 선택 27 peptide PRM 검증: 25/27(92.59%) MS/MS 신호 확인.
- NetMHCPan 4.1 기반 80% 이상 epitope이 적어도 한 MHC class I allele에 rank<2% affinity 보유.

### Mutated neo-epitope 96개의 origin 분해
- DNA-level mutation 78개 / RNA-level mutation 19개; Neo-074 단일 peptide만 양쪽에서 검출. 전체 96개 중 SNV 64.58%(62), deletion 14.58%(14), insertion 3.12%(3), 나머지(주로 RNA-level)는 AS(14/19; SE 우세) 및 기타.
- **77/96(80.21%)이 non-coding origin**. DNA-level non-coding 분포: intergenic 26 + intronic 28 + non-coding intronic 19. RNA-level은 18/19이 exonic. 전체 exonic in-frame 16.
- 비-coding 유래 96개 모두 예측 ORF 안에 위치. 비-coding ORF 평균 길이 **127 bp(~42 aa)** — 보고된 nuORF MHC class I 기여 길이대와 일치. 반면 annotated exonic ORF 평균 **2,128 bp**. Intergenic neo-epitope 변이 위치는 인근 유전자에서 평균 >10 kb 떨어진 곳에 위치, 인근 유전자는 lncRNA / protein-coding / processed pseudogene 순.
- Start codon 분포: 비-coding ORF에서 AAG 19.48% 우세, ATG는 annotated ORF에서만; CTG는 5.21%(5/96)로 적음.
- 30.21%가 NetMHCPan rank top 2%; 모든 후보가 wild-type 대비 유의하게 높은 affinity.
- Chinese CRC 인구 mutation frequency 0.1–2.4%(intra-patient), 96 neo-epitope 중 10명 모두 공유되는 peptide 0개 — inter-patient variability 극단.

### Hypermutation vs non-hypermutation 비교(TMB cutoff 25)
- Hypermutation 그룹: 87 neo-epitope(평균 14.5/환자), **86.2% non-canonical**(전체 non-canonical의 97.4%, 평균 12.5/환자). Intergenic + intronic 빈도가 non-hypermutation 대비 ~25배 / ~46배. Non-coding intronic neo-epitope는 hypermutation 그룹에서 21.84%, non-hypermutation 그룹에서 0%.
- Non-hypermutation 그룹: 9 neo-epitope(평균 2.2/환자), **22.2% non-canonical**(평균 0.5/환자). Coding variation + AS가 우세.

### Ribo-seq 교차 검증
- smProt + nuORFdb 두 데이터베이스로 mutation 좌표 cross-mapping. **77 non-canonical neo-epitope 중 35개가 Ribo-seq 지지** — active translation 증거. 다수가 intronic. Start codon 분포: ATA, ATC, ATG 각각 14.29%.

### MC38 in vivo validation
- MC38 종양 WGS+RNA-seq: genomic/transcriptomic mutation overlap 0.7%, 대부분 non-coding. 환자 코호트와 정합.
- Proteogenomic pipeline으로 MC38에서 5,646개 전체 epitope + **20 neo-epitope** 식별(11 non-canonical: intergenic 5 / intronic 4 / non-coding RNA intronic 2). PRM 20/20(100%) 검증.
- 11 non-canonical(intronic 6 + intergenic 5) repeat peptide challenge + ELISpot: **intronic 3/6(50%) + intergenic 3/5(60%)** IFN-γ 양성.
- 7-peptide Vax(immunogenic 비-coding 후보 풀) vs PBS vs CtrlVax(non-immunogenic 비-coding 7-peptide pool): MC38 inoculation 후 day 3/5/7 3회 투여. **Vax 그룹 종양 성장 유의 억제**(PBS/CtrlVax 대비).
- Antibody-mediated depletion: α-CD8β로 Vax 효과 완전 abrogation(p<0.0001 vs Vax). α-CD4 / α-NK / α-macrophage는 효과 미손상 → MHC class I-restricted CD8⁺ T cell이 primary mechanism.
- IF: Vax 종양에서 CD8⁺ infiltration ↑, CD4⁺Foxp3⁺ Treg 빈도 ↓.

### scRNA-seq TME(67,471 cells)
- UMAP 4 major compartment: malignant / fibroblast / TIL / TIM. TIL 8 subpopulation: cytotoxic CD8⁺(Ccl5/Gzmk), exhausted CD8⁺(Pdcd1/Lag3/Havcr2), naive CD4⁺(Tcf7/Lef1), exhausted CD4⁺(Tnfsf8/Pdcd1), proliferating CD4⁺(Mki67), Treg(Foxp3/Il2ra), NK(Gzma/Xcl1/Klra7/Sell), B cell(Cd79a).
- Vax 그룹 전체 CD8⁺ T cell 비율 controls 대비 >2배. Cytotoxic CD8⁺ TIL 비율 0.08%(PBS) / 0.15%(CtrlVax) / **0.40%(Vax)**. Exhausted CD8⁺ TIL 0.12% / 0.34% / **0.84%**.
- Cytotoxic CD8⁺ DEG: TNF-α via NF-κB + IFN-γ response 경로 upregulation(Socs3, Cdkn1a, Ccl5). Exhausted CD8⁺: p53 경로(Cyfip2, Mapkapk3, Mxd1).
- Treg as proportion of CD4⁺: 36.14%(PBS) / 35.74%(CtrlVax) / **22.61%(Vax)**. **CD8⁺/Treg ratio 2.39(PBS) / 2.07(CtrlVax) / 3.93(Vax)**.

### 한계(본문 명시)
- 6-frame translation으로 ORF redundancy 증가 → 중복 ORF source 비-coding peptide는 식별 제외 (잠재적으로 일부 후보 누락).
- 비-coding TSA 메커니즘(intronic / intergenic) 추가 in vivo 검증 필요.
- PRM 92.59%로 stringent FDR 1%(target-decoy)보다 empirical 정확도가 높음 → FDR calibration 체계적 편향 가능성 본문 인정.
- 패널 환자 코호트 n=10, 단일 기관, 단일 인구(Chinese), 단일 cancer type. 따라서 80.21% non-coding 비율의 일반화는 추가 코호트 필요.
- 35/77 non-canonical만 Ribo-seq 지지 — 나머지 42개는 translation 증거 부재(짧은 ORF의 빠른 post-transcriptional degradation 가설).
- Long-read transcriptome / RNC-seq / 비-poly(A) 40% transcript 포함은 향후 과제로 명시.

## Methods

- **Sample acquisition**: 10명 CRC 환자 paired tumor + 인접 정상; Sun Yat-sen Sixth Affiliated Hospital. Sample preparation per supplementary protocol.
- **WGS somatic mutation calling**: 6-caller consensus(다중 caller 합의)로 SNV / indel 호출. TMB는 10⁶ nt당 mutation 빈도로 계산; cutoff 25 기준 hypermutation 그룹 분리.
- **RNA-seq**: STAR alignment + STAR-Fusion(gene fusion) + rMATs(alternative splicing, SE/A3SS/A5SS/RI/MXE 5 type). 추가로 Trinity de novo transcriptome assembly로 reference 외 transcript 포함.
- **환자별 mutant protein DB**: mutation site 주변 24–45 bp window의 6-frame translation. 10 후보 start codon(ATG + 9 single-nt substitution)으로 ORF 예측.
- **IP-MS immunopeptidome**: MHC class I 면역침강 + LC-MS/MS. 환자별 mutant DB와 reference proteome 결합.
- **Two-stage DB search**: 1차 unfiltered PSM 기반 protein extraction → DB 76.55% 축소 → 2차 1% FDR strict search. 다중 검색 엔진(Comet + MSFragger + MaxQuant) + de novo(Casanovo, PepNet, pNovo3, SMSNet) 결과 통합.
- **추가 필터링**: ΔRT(retention time difference) <300 s + SSS(spectral similarity score) >0.4 + 1% FDR.
- **NetMHCPan 4.1**: peptide-HLA affinity 예측. Rank <2%를 보통 binder cutoff로 사용.
- **PRM**: 무작위 27 peptide 합성 + parallel reaction monitoring으로 MS/MS 신호 검증.
- **Neo-epitope backtracking**: 비-coding origin 확정을 위해 mutated genomic coordinate를 smProt + nuORFdb Ribo-seq translation atlas와 cross-mapping.
- **In vivo MC38**: C57BL/6 mouse syngeneic xenograft. ELISpot for IFN-γ (peptide challenge 후). 7-peptide Vax 그룹(immunogenic 비-coding 풀) / CtrlVax(non-immunogenic 비-coding 풀) / PBS. Day 3 / 5 / 7 vaccination. Antibody-mediated depletion: α-CD8β / α-CD4 / α-NK / α-macrophage.
- **scRNA-seq**: 10x Genomics platform 추정(본문 명시는 67,471 quality-filtered cells, UMAP, 4 compartment + 8 TIL subpopulation). DEG marker 기반 cluster annotation.
- **CD8 T cell generation**: dendritic cell(DC) priming 후 peptide-pulsed CD8 T cell 자극 → ELISpot readout.
- **Data IDs**: WGS+RNA-seq CNSA CNP0004656 + GSA-Human HRA005229; IP-MS CNSA CNP0005402.
- **Code**: github.com/Leo-Guan-git/Codes-for-scirpts-of-CRC_WGS + Zenodo 10.5281/zenodo.17527817.

## Cancer Multiomics Project Relevance

한미암 프로젝트가 한국인 CRC 코호트 또는 동아시아 비교 코호트에서 non-canonical neoantigen 발굴을 검토할 때 직접 활용 가능한 reference. 적용 시 다음 5축으로 사용한다.

1. **Non-canonical TSA discovery pipeline 자체**: WGS + RNA-seq + IP-MS 통합 + 6-frame translation + 10 후보 start codon + two-stage DB search + 다중 search engine + de novo + Ribo-seq cross-mapping의 stack을 한미암 in-house pipeline 설계 / calibration의 1차 reference로 사용. 특히 HCT116 / HCC1143 cell-line 외부 검증 결과(79.61% / 96.44% recall + 4.88× / 4.68× 식별 확장)는 자체 pipeline 벤치마크 시 비교 baseline.
2. **Hypermutated CRC subset 특화 가설**: 한국인 dMMR/MSI-H CRC 환자(전체 CRC의 ~5%)에서 비-coding intergenic + intronic neo-epitope이 dominant할 가능성을 가설로 잡고 — 한미암 personalized vaccine 후보 풀을 exome 한정에서 WGS 기반으로 확장하는 결정의 근거. 정량 비교: hypermutated 14.5/환자 vs non-hypermutated 2.2/환자.
3. **MC38 in vivo validation 설계 reference**: 비-coding TSA의 immunogenicity(IFN-γ ELISpot ~55% 양성) + 7-peptide pool Vax + α-CD8β depletion으로 mechanism 확정 + scRNA-seq로 TME readout(CD8/Treg ratio) — 한미암 mouse PoC 단계의 실험 설계 템플릿.
4. **Public data cross-reference**: CNSA CNP0004656(WGS+RNA-seq) + CNP0005402(MS)로 Chinese 10명 raw data 접근 가능 → 한국 환자 cohort의 cross-reference / re-analysis 가능. BGI Research / HIM-BGI Omics Center 데이터로 동아시아 baseline 확장.
5. **방법론적 위험 분리**: PRM 92.59% empirical 정확도 vs 이론 FDR 1% — DB 확장에 따른 FDR calibration 이슈가 본문 인정. 한미암 자체 pipeline 도입 시 random sampling + PRM 재검증을 SOP에 포함하는 결정의 근거.

한계 본문 명시 — n=10, Chinese 단일 인구, 단일 기관, BGI Group 저자 stock(competing interest), Ribo-seq 지지 ORF 35/77만 (나머지 42개는 translation 증거 부재). 일반화에는 추가 코호트 + long-read transcriptome / RNC-seq / 비-poly(A) transcript 포함이 필요. PS-T-DXd 연결처럼 mechanistic alignment이지 prospective 임상 outcome은 아님.

## Connections

- [B-Cell Neoantigen Topic Hub](../topics/b-cell-neoantigen-human-cancer.md)
- [B-Cell Neoantigen Proposal Anchor](../analyses/b-cell-neoantigen-proposal-anchor.md)
- [Cancer Multiomics Literature](../topics/cancer-multiomics-literature.md) — 면역회피와 Neoantigen 섹션
- [Wen 2020 - NeoFlow Proteogenomic Neoantigen Prioritization](../analyses/cancer-multiomics-literature/wen-2020-neoflow-neoantigen-prioritization.md)
- [Huber 2025 - NeoDisc Proteogenomic Neoantigen Pipeline](../analyses/cancer-multiomics-literature/huber-2025-neodisc-neoantigen-pipeline.md)
- [Shapiro 2025 - NeoDiscMS Real-time NGS-guided Immunopeptidomics](../analyses/cancer-multiomics-literature/shapiro-2025-sensitive-neoantigen-discovery-real-time-mutanome-guided.md)
- [Scheid 2025 - MHCquant2 (nf-core) Immunopeptidomics Pipeline](../analyses/cancer-multiomics-literature/scheid-2025-mhcquant2-refines-immunopeptidomics-tumor-antigen.md)
- [Chong 2022 - Identification of Tumor Antigens with Immunopeptidomics](../analyses/cancer-multiomics-literature/chong-2022-identification-tumor-antigens-immunopeptidomics.md)
- [Abelin 2023 - MONTE Serial Multi-Omics (Immunopeptidome + PTM)](../analyses/cancer-multiomics-literature/abelin-2023-workflow-enabling-deepscale-immunopeptidome-proteome.md)
- [Tanaka 2024 - CRC Primary vs Liver Metastasis Proteogenomics](../analyses/cancer-multiomics-literature/tanaka-2024-proteogenomic-characterization-primary-colorectal-cancer.md)

## Sources

- Local PDF: `raw/inbox/papers/xiang-2026-predominant-mutated-non-canonical-tumor-specific-antigens.pdf`
- Local HTML (PMC): `raw/inbox/papers/xiang-2026-predominant-mutated-non-canonical-tumor-specific-antigens.html`
- PubMed: <https://pubmed.ncbi.nlm.nih.gov/41237784/>
- DOI: <https://doi.org/10.1016/j.xgen.2025.101062>
- PMC: <https://pmc.ncbi.nlm.nih.gov/articles/PMC12926194/>
- Correction: Cell Genom. 2026 Jan 22;6(2):101163
- Data — WGS/RNA-seq: CNSA [CNP0004656](https://db.cngb.org/data_resources/project/CNP0004656/) + GSA-Human HRA005229
- Data — IP-MS: CNSA [CNP0005402](https://db.cngb.org/data_resources/project/CNP0005402/)
- Code: <https://github.com/Leo-Guan-git/Codes-for-scirpts-of-CRC_WGS> + Zenodo [10.5281/zenodo.17527817](https://doi.org/10.5281/zenodo.17527817)
