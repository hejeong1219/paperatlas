---
title: Cancer Multiomics Literature 50-Question Sprint (2026-05-25)
tags:
  - question-bank
  - wiki-expansion
  - cancer-multiomics
  - proteogenomics
  - phosphoproteomics
  - spatial-omics
themes:
  - proteogenomics
  - phosphoproteomics
  - wgs
  - kinase-signaling
  - response-prediction
  - spatial-omics
date: 2026-05-25
status: completed-2026-05-25
---

# Cancer Multiomics Literature 50-Question Sprint (2026-05-25)

`cancer-multiomics-literature` topic hub의 신착 14편(`topic-sweep-2026-05-25`) + 기존 80+ 시드 + 한미암 4축(WGS 변이 / 인산화단백체 / WGS-단백체 통합 / 신항원-면역 / 치료반응 예측)에 맞춰 50개 질문 → 답변 → wiki 확장.

## 답변 정책

- 답변은 로컬 `wiki/sources/`, `wiki/concepts/`, `wiki/syntheses/` pages만 근거
- 답이 durable value면 concept/synthesis 페이지로 승격
- evidence gap이면 `cancer-multiomics-corpus-queue.md` 또는 `next-download-candidates.md`에 후보 등록
- 한미암 4축 중 어떤 축에 해당하는지 답변마다 명시

## Section A — WGS variant interpretation (Q1-10)

### Q1. SV breakpoint pattern (translocation, tandem dup, inversion)이 cancer proteome에 실제로 반영되는 비율은 pan-cancer scale에서 어떻게 정량되는가?

**A.** Chen 2023 pan-cancer 1,307 tumor 코호트의 SV–proteomics 통합 분석은 SV-associated cis-regulatory alteration이 mRNA에서 관찰되는 유전자 중 **약 25%만 단백질 수준에서도 일관되게 반영**됨을 정량적으로 보고합니다 ([Chen 2023](../sources/chen-2023-global-impact-somatic-structural-variation-cancer-proteome.md)). 자매 연구인 Chen 2026 germline SV 분석은 paired SV caller(Delly ∩ SVABA)로 식별된 364개 recurrent SV-altered gene 중 **17%(129/364)** 만이 mRNA·protein concordant cis-regulation을 보였고, 동일 set의 **33%는 protein-only direction**(mRNA로는 약한 변화만 잡힘)이라는 비대칭을 명시합니다 ([Chen 2026](../sources/chen-2026-global-impact-germline-structural-variation-cancer-proteome.md)). 즉 enhancer hijacking·retrotransposon translocation·CGI methylation 매개 SV는 mRNA layer만으로는 ~3분의 1을 놓칠 수 있어, SV-aware proteogenomics가 필수적으로 시사됩니다. 한미암 위암 코호트에서도 SV-only / RNA-only / protein-only / triple-concordant 4분면으로 cis-effect를 layer해 단백체 evidence 기반 SV consequence를 평가할 수 있겠습니다.

**한미암 4축**: (C) WGS-단백체 통합

**Cited**: [Chen 2023](../sources/chen-2023-global-impact-somatic-structural-variation-cancer-proteome.md), [Chen 2026](../sources/chen-2026-global-impact-germline-structural-variation-cancer-proteome.md)

**Filed**: `existing`.

### Q2. Germline structural variation (Chen 2026)이 cancer proteome cis-effect를 통해 단백 저발현/이상발현을 어떻게 일으키는가?

**A.** Chen 2026은 CPTAC 11개 종양형 1,637명의 normal WGS에서 paired SV caller로 704,263개 distinct germline SV를 식별하고, 그 중 25,781개 LoF SV(SVAnnotate frameshift/exon-deletion/stop-gain)가 paired proteomics에서 **1,847개 low-protein outlier event (FDR<10%, 512 genes × 786 patients)** 를 야기함을 보고합니다 ([Chen 2026](../sources/chen-2026-global-impact-germline-structural-variation-cancer-proteome.md)). 기능적 enrichment는 **MHC class I antigen binding / antigen processing / exosome / mitochondrial matrix / Golgi** 카테고리에 집중되어 germline SV가 면역회피와도 연결될 수 있음을 시사합니다. 단백 저발현 메커니즘은 (i) coding exon deletion → frameshift LoF, (ii) **CGI methylation 매개**(1,237 CGI probe FDR<10%), (iii) **enhancer methylation 매개**(109 SV-enhancer pair, 41개는 CBTN 소아 뇌종양 코호트에서 p<1E-22로 reproduce) 세 축으로 분해됩니다. 한미암 한국인 위암 코호트에서도 germline SV → CGI/enhancer methylation → 단백 저발현 cascade를 평가하는 분석 파이프라인 설계에 참고할 수 있겠습니다.

**한미암 4축**: (C) WGS-단백체 통합 + (D) 신항원-면역(MHC class I enrichment)

**Cited**: [Chen 2026](../sources/chen-2026-global-impact-germline-structural-variation-cancer-proteome.md)

**Filed**: `existing`.

### Q3. Chromothripsis / focal amplification (EGFR 7p, MYC, ERBB2 17q)이 phosphoproteome state에 미치는 effect의 양적 측정?

**A.** Sambath 2026 인도 자궁경부암(stage IIIB squamous HPV+, n=36) 화학방사선 저항 코호트에서 **7p EGFR amplification이 저항군 환자 6명**에서만 관찰되었고, 동일 코호트에서 **chromothripsis가 12명 중 3명(25%)** 으로 나타나 ATM/ATR/BRCA2/RAD50 DNA repair pathway 및 CSNK2A1/SMC1A phosphorylation 활성과 연결됨을 보고합니다 ([Sambath 2026](../sources/sambath-2026-integrated-genomic-proteomic-cervical-cancer-chemoradiation-resistance.md)). Xu 2026 중국 HER2-low breast 코호트에서는 **7q gain (SSBP1/FIS1)** 이 HER2-low 특이 SCNA로 식별되었고 PS3 proliferation subtype에서 trastuzumab/T-DM1 반응 가설로 연결됩니다 ([Xu 2026](../sources/xu-2026-proteogenomic-characterization-reveals-subtype-specific-therapeutic.md)). Chen 2023의 SV breakpoint–단백체 매핑에서도 focal amplification은 cis 단백 과발현으로 ~25% 반영되어 phosphoproteome state(특히 EGFR/ERBB2 downstream MAPK/PI3K cascade)에 직접 영향을 미칠 가능성이 시사됩니다 ([Chen 2023](../sources/chen-2023-global-impact-somatic-structural-variation-cancer-proteome.md)). 한미암 위암 코호트에서 ERBB2 17q amplification 환자의 HER2 phospho-substrate 활성을 정량화하면 표적 적합성 평가에 직접 활용될 수 있겠습니다.

**한미암 4축**: (A) WGS 변이 + (B) 인산화단백체

**Cited**: [Sambath 2026](../sources/sambath-2026-integrated-genomic-proteomic-cervical-cancer-chemoradiation-resistance.md), [Xu 2026](../sources/xu-2026-proteogenomic-characterization-reveals-subtype-specific-therapeutic.md), [Chen 2023](../sources/chen-2023-global-impact-somatic-structural-variation-cancer-proteome.md)

**Filed**: `existing`.

### Q4. ecDNA (extrachromosomal DNA) 의 inheritance pattern과 cancer phenotype heterogeneity 기여도?

**A.** Hung 2024 Nature 연구는 같은 종양세포 내 cooperative한 다중 ecDNA species가 random하게 분리되지 않고 **mitotic co-segregation을 통해 coordinated하게 유전**됨을 single-cell 이미징과 sequencing으로 보였고, daughter cell에서 동시에 oncogene copy number가 유지되는 패턴을 입증했습니다 ([Hung 2024](../sources/hung-2024-coordinated-inheritance-extrachromosomal-dnas-cancer.md)). Pongor 2023은 small-cell lung cancer에서 ecDNA가 oncogenic **MYC amplification의 주요 origin**이며 neuroendocrine ↔ non-neuroendocrine cell state 가소성 및 worse outcome과 연관됨을 WGS + optical mapping + single-cell DNA-seq + FISH 통합 분석으로 정량합니다 ([Pongor 2023](../sources/pongor-2023-extrachromosomal-dna-amplification-contributes-small.md)). Wang 2025 bioRxiv는 ecDNA가 cancer 진화와 치료저항성에 **별도의 evolutionary pathway**를 제공한다는 framework를 제시합니다 ([Wang 2025](../sources/wang-2025-extrachromosomal-dna-cancer-evolutionary-pathway.md)). 한미암 위암 코호트에서 EGFR/MYC/ERBB2 high-copy amplification 환자의 ecDNA 가능성을 long-read WGS 또는 AmpliconArchitect로 평가하면 acquired resistance 기전 해석에 추가 차원을 제공할 수 있겠습니다.

**한미암 4축**: (A) WGS 변이 + (E) 치료반응 예측(plasticity 기반 resistance)

**Cited**: [Hung 2024](../sources/hung-2024-coordinated-inheritance-extrachromosomal-dnas-cancer.md), [Pongor 2023](../sources/pongor-2023-extrachromosomal-dna-amplification-contributes-small.md), [Wang 2025](../sources/wang-2025-extrachromosomal-dna-cancer-evolutionary-pathway.md)

**Filed**: `existing`.

### Q5. APOBEC (SBS2/SBS13), MMR deficiency (G2/G4), NAT-MMR, polymerase-η, DSB repair, nitrosamine, DBAC PAH 등 mutational signature가 cancer type/지역별로 어떻게 differential하게 나타나는가?

**A.** Chang 2026 Taiwanese gastric cancer 코호트(NTUH/KMUH n=154 + 외부검증 n=185)는 NMF로 **7개 mutational signature(G1 spontaneous deamination / G2 tumour MMR / G3 polymerase-η / G4 NAT MMR / G5 DSB repair / G6 nitrosamine / G7 irradiation)** 와 **6개 carcinogen cluster(C1–C6)** 를 정의하고, 특히 **dibenz[a,h]acridine (DBAC PAH)** 이 East Asia 특이 high-risk signature이며 multivariable Cox HR 2.36–3.16, diffuse subtype 5.9× EFS risk(p=0.013)임을 입증합니다 ([Chang 2026](../sources/chang-2026-integrative-proteogenomics-gastric-cancer-taiwan.md)). DBAC는 charcoal-grilling/pan-frying dietary BaP(cooked 1.30 ng/g vs raw 0.12 ng/g) 환경 노출과 연계되며 TCGA에는 부재하나 Taiwanese·Japanese 코호트에서 재현됩니다. Lee 2026 Korean TNBC 코호트는 NMF 5 subtype 중 xenobiotic metabolism subtype에서 AKR1C2 RNA 가장 높음을 보고합니다 ([Lee 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md)). 한미암 한국 위암 코호트에 SigProfilerExtractor·deconstructSigs로 SBS·DBS·ID signature를 추출 후 Taiwanese G1–G7 / C1–C6 framework와 비교하면 식이성 PAH 노출과 한국인 위암 driver pattern 매핑을 검토해 볼 만합니다.

**한미암 4축**: (A) WGS 변이

**Cited**: [Chang 2026](../sources/chang-2026-integrative-proteogenomics-gastric-cancer-taiwan.md), [Lee 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md)

**Filed**: `existing`.

### Q6. HLA typing (class I/II)의 WGS-based call 정확도와 immunopeptidomics validation gap?

**A.** Han 2024는 HLA class I allele divergence와 neoantigen–HLA binding을 결합한 **HLA tumor-Antigen Presentation Score (HAPS)** 가 단순 neoantigen 개수보다 pan-cancer ICI 반응을 더 잘 예측함을 보여, WGS-based HLA call이 quantitative presentation capacity로 변환되어야 임상 신호가 살아남는다는 점을 시사합니다 ([Han 2024](../sources/han-2024-hla-based-neoantigen-presentation-pan-cancer-response.md)). Chen 2026은 LoF germline SV의 functional enrichment에서 **MHC class I antigen binding/antigen processing** 카테고리가 유의함을 보여, WGS-based HLA-presentation pathway 평가가 단순 4-digit allele call을 넘어 antigen processing 전체 cascade로 확장되어야 함을 제시합니다 ([Chen 2026](../sources/chen-2026-global-impact-germline-structural-variation-cancer-proteome.md)). Xiang 2025 Chinese CRC 코호트의 MHC class I IP-MS + 6-frame translation은 **80.21%가 non-coding origin neoantigen**을 입증해, WGS-only prediction과 immunopeptidomics 측정 사이에 큰 갭이 존재함을 명시합니다 ([Xiang 2025](../sources/xiang-2026-predominant-mutated-non-canonical-tumor-specific-antigens.md)). 한미암 위암 코호트에서 OptiType/HLA-LA/HLA*PRG 등으로 4-digit HLA call 후 NeoFlow/NeoDisc + immunopeptidomics validation을 dual-track으로 운영하면 validation gap을 정량화할 수 있겠습니다.

**한미암 4축**: (A) WGS 변이 + (D) 신항원-면역

**Cited**: [Han 2024](../sources/han-2024-hla-based-neoantigen-presentation-pan-cancer-response.md), [Chen 2026](../sources/chen-2026-global-impact-germline-structural-variation-cancer-proteome.md), [Xiang 2025](../sources/xiang-2026-predominant-mutated-non-canonical-tumor-specific-antigens.md)

**Filed**: `existing`.

### Q7. Noncoding driver mutation (TERT promoter, enhancer hijacking)이 expression/protein readout으로 detect되는 사례?

**A.** Chen 2023 pan-cancer 1,307 tumor 분석은 SV 기반 **enhancer hijacking·retrotransposon translocation·CGI methylation 매개 cis-regulation**이 단백질 과발현으로 직접 연결되는 사례를 다수 카탈로그하며, 비암호화 SV의 protein consequence가 mRNA만 보면 놓치는 영역임을 강조합니다 ([Chen 2023](../sources/chen-2023-global-impact-somatic-structural-variation-cancer-proteome.md)). Chen 2026 germline SV 자매연구는 **109개 SV-enhancer methylation pair** 중 41개가 CBTN pediatric brain tumour 코호트에서 p<1E-22로 재현되고, **ECHDC1 / SH3GLB2 / MAMDC2**가 enhancer methylation 매개 cis-target임을 명시합니다 ([Chen 2026](../sources/chen-2026-global-impact-germline-structural-variation-cancer-proteome.md)). Attig 2019의 LTR retroelement expansion 분석도 noncoding regulatory element가 cancer expression program으로 어떻게 활성화되는지의 reference로 활용될 수 있습니다 ([Attig 2019](../sources/attig-2019-ltr-retroelement-expansion-human-cancer.md)). 한미암 위암 WGS에서 TERT promoter mutation·enhancer hijacking을 SV+methylation 매개 cis-regulation framework로 평가하면 protein evidence 기반 driver call에 활용될 수 있겠습니다.

**한미암 4축**: (A) WGS 변이 + (C) WGS-단백체 통합

**Cited**: [Chen 2023](../sources/chen-2023-global-impact-somatic-structural-variation-cancer-proteome.md), [Chen 2026](../sources/chen-2026-global-impact-germline-structural-variation-cancer-proteome.md), [Attig 2019](../sources/attig-2019-ltr-retroelement-expansion-human-cancer.md)

**Filed**: `existing`.

### Q8. Tumor heterogeneity (clonal vs subclonal SV/SNV)가 single-cell WGS + spatial multi-omics로 어떻게 layer되는가?

**A.** Wang 2026 combined small-cell lung cancer 19명 코호트는 **multi-region WES (95개 region/16명) + spatial transcriptomics (6명) + snRNA-seq (12명)** 통합으로 TP53는 모든 region에서 clonal, RB1은 6명 clonal·2명 subclonal로 정량해 monoclonal origin을 입증하고, COL11A1+ CAF S3-like fibroblast가 종양 도메인 경계를 형성해 immune exclusion에 공간적으로 기여함을 보입니다 ([Wang 2026](../sources/wang-2026-spatial-multi-omics-unveils-monoclonal-origin.md)). Pongor 2023 SCLC ecDNA 연구는 single-cell DNA sequencing + FISH로 cell-to-cell MYC copy number heterogeneity를 정량합니다 ([Pongor 2023](../sources/pongor-2023-extrachromosomal-dna-amplification-contributes-small.md)). Sussman 2026 pediatric high-grade glioma 16명 longitudinal multiomic atlas는 snRNA + snATAC + WGS + CODEX spatial proteomics를 1차 절제–재발–autopsy 시점에 결합해 clonal evolution과 spatial niche를 동시에 layer합니다 ([Sussman 2026](../sources/sussman-2026-longitudinal-single-cell-spatial-multiomic-atlas.md)). 한미암 위암 코호트에서 다구역 WGS + spatial transcriptomics + 단백체를 결합해 clonal driver와 spatial niche를 dual-layer로 분석하면 1차 vs 2차 내성 진화 분석에 직접 참고할 수 있겠습니다.

**한미암 4축**: (A) WGS 변이 + (D) 신항원-면역(공간 layer)

**Cited**: [Wang 2026](../sources/wang-2026-spatial-multi-omics-unveils-monoclonal-origin.md), [Pongor 2023](../sources/pongor-2023-extrachromosomal-dna-amplification-contributes-small.md), [Sussman 2026](../sources/sussman-2026-longitudinal-single-cell-spatial-multiomic-atlas.md)

**Filed**: `existing`.

### Q9. WGS-based copy number signature vs proteome-derived functional state — 어느 layer가 prognosis와 더 강하게 연관되는가?

**A.** Zhao 2026 CRLM proteogenomics는 LM proteome unsupervised clustering이 phospho·transcriptome 기반 클러스터링보다 prognostic stratification에서 우월하며(C1 vs C2 OS log-rank p<0.05; C1 poor), CRS 임상 위험 점수는 5-yr OS log-rank p=0.23으로 예측력이 충분하지 않음을 명시합니다 ([Zhao 2026](../sources/zhao-2026-proteogenomic-characterization-reveals-metabolic-vulnerabilities.md)). Lee 2026 Korean TNBC는 5개 저항인자(estrogen GSVA + GRK2 PTM-SEA + ITGB8 7p21 + AKR1C2 + ABCA13) 통합 로지스틱 회귀가 non-pCR AUC **0.946**으로 Lehmann 분류(AUC 0.781)나 Lehmann+ESTIMATE(AUC 0.818)를 능가함을 보여, **protein/phospho functional state가 단순 CNA·transcriptome 기반 분류보다 임상 endpoint와 더 강하게 연관**됨을 입증합니다 ([Lee 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md)). Song 2024 Korean NSCLC 5 subtype에서도 phosphoproteome이 80%(911/1,134) subtype feature를 제공하며 Subtype 4(hypoxic, CSNK2A1/GSK3B 활성)가 stage 보정 후에도 worse survival을 보입니다 ([Song 2024](../sources/song-2024-proteogenomic-analysis-reveals-non-small-cell.md)). 한미암 위암 코호트도 CNA·signature layer와 proteome/phospho layer를 prognostic model에 분리 입력해 두 축의 상대 기여도를 정량할 수 있겠습니다.

**한미암 4축**: (C) WGS-단백체 통합 + (E) 치료반응 예측

**Cited**: [Zhao 2026](../sources/zhao-2026-proteogenomic-characterization-reveals-metabolic-vulnerabilities.md), [Lee 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md), [Song 2024](../sources/song-2024-proteogenomic-analysis-reveals-non-small-cell.md)

**Filed**: `existing`.

### Q10. East Asian / Chinese / Korean / Indian 코호트 specific mutational signature (DBAC, charcoal-grilling, HBV-driven HCC)와 한국 위암 코호트 매핑?

**A.** Chang 2026 Taiwanese gastric cancer 154명 코호트가 핵심 reference로, DBAC PAH signature가 East Asian charcoal-grilling/pan-frying 식이 노출과 연계되며 다변량 Cox HR 2.36–3.16, diffuse subtype 5.9× EFS risk, BaP MKN45/MKN28 invasion 3.7×/2.7× cell-line 검증까지 제시합니다 ([Chang 2026](../sources/chang-2026-integrative-proteogenomics-gastric-cancer-taiwan.md)). Sambath 2026 인도 자궁경부암 코호트는 EGFR 7p amp + STK11 SV deletion + chromothripsis + DNA repair/WNT-β-catenin pathway enrichment를 저항 코호트 특이 신호로 보고합니다 ([Sambath 2026](../sources/sambath-2026-integrated-genomic-proteomic-cervical-cancer-chemoradiation-resistance.md)). Xu 2026 중국 HER2-low breast 코호트는 TP53 mut + 9p loss(MTAP cis)가 HER2-low 한정 poor prognosis임을 보여 ancestry-specific co-occurrence를 제시합니다 ([Xu 2026](../sources/xu-2026-proteogenomic-characterization-reveals-subtype-specific-therapeutic.md)). Chen 2026 germline SV 연구도 ancestry-enriched SV(Asian 8개 — TIGAR 포함; African 10개; European 13개)가 cis-cancer effect의 45%를 별도로 설명한다고 보고합니다 ([Chen 2026](../sources/chen-2026-global-impact-germline-structural-variation-cancer-proteome.md)). 한미암 위암 코호트는 KOVA·KCDC ancestry baseline + DBAC/nitrosamine/Microvirga signature 매핑으로 한국인 위암 특이 carcinogen-cluster를 추출하는 framework로 참고할 수 있겠습니다.

**한미암 4축**: (A) WGS 변이

**Cited**: [Chang 2026](../sources/chang-2026-integrative-proteogenomics-gastric-cancer-taiwan.md), [Sambath 2026](../sources/sambath-2026-integrated-genomic-proteomic-cervical-cancer-chemoradiation-resistance.md), [Xu 2026](../sources/xu-2026-proteogenomic-characterization-reveals-subtype-specific-therapeutic.md), [Chen 2026](../sources/chen-2026-global-impact-germline-structural-variation-cancer-proteome.md)

**Filed**: `existing`.

## Section B — Phosphoproteome / Kinase signaling (Q11-20)

### Q11. TMT11/16 vs DIA phosphoproteome workflow 비교 — depth, missingness, batch effect, sample 요구량?

**A.** Hsu 2025 osimertinib DTP 연구는 **DIA-MS spectral library** 기반으로 phosphoproteome library가 221,618 phosphopeptide / 53,182 phosphosite / 10,326 protein group을 수록하고, 시료당 평균 ~5,200 protein / 21,500 phosphopeptide를 정량해 DIA가 deep phosphoproteome coverage에 적합함을 보여줍니다 ([Hsu 2025](../sources/hsu-2025-phosphoproteomics-osimertinib-tolerant-persister-cells-reveals.md)). Lehe 2026 review는 SWATH-DIA가 2,964 isoform-specific peptide, Astral DIA가 935 AS event/일, 일반 DDA는 0–10 AS peptide라는 평점 매트릭스를 제시하며 DIA가 missingness·coverage 측면에서 DDA보다 우월함을 종합합니다 ([Lehe 2026](../sources/lehe-2026-mass-spectrometry-alternative-protein-isoforms-review.md)). CPTAC 표준은 TMT 11-plex(예: Song 2024 Korean NSCLC 229명에서 10,788 proteins/40,738 phosphosites)이며 batch effect 보정을 위해 reference-intensity centering·ComBat·DreamAI imputation을 결합합니다 ([Song 2024](../sources/song-2024-proteogenomic-analysis-reveals-non-small-cell.md), [Petralia 2024](../sources/petralia-2024-pan-cancer-proteogenomics-characterization-tumor-immunity.md)). 한미암 위암 코호트에서는 TMT11-plex가 CPTAC compatibility와 batch design 유리, DIA는 sample-by-sample missingness 최소화 유리이므로 1차 cohort는 TMT, 종단·소량 시료는 DIA로 layer하는 방안을 검토해 볼 만합니다.

**한미암 4축**: (B) 인산화단백체

**Cited**: [Hsu 2025](../sources/hsu-2025-phosphoproteomics-osimertinib-tolerant-persister-cells-reveals.md), [Lehe 2026](../sources/lehe-2026-mass-spectrometry-alternative-protein-isoforms-review.md), [Song 2024](../sources/song-2024-proteogenomic-analysis-reveals-non-small-cell.md), [Petralia 2024](../sources/petralia-2024-pan-cancer-proteogenomics-characterization-tumor-immunity.md)

**Filed**: `existing`.

### Q12. Phosphopeptide-level vs phosphosite-level 정량의 적절한 통계 unit은 무엇인가?

**A.** Hsu 2025는 phosphosite localization probability ≥ 0.75를 class I site 기준으로 채택해 osimertinib DTP에서 10,742 unique phosphosite를 분석 단위로 삼고, 동일 단백질 내 phosphopeptide 간에 분기되는 신호는 site-level로 환원해 KSEA · CausalPath inference에 입력합니다 ([Hsu 2025](../sources/hsu-2025-phosphoproteomics-osimertinib-tolerant-persister-cells-reveals.md)). Zhao 2025 CRC kinase inhibitor 분석도 6,213 phosphosite 중 **5,048 class I site**(localization score >0.75)만 유지하고 PTM-SEA·KSEAapp에 입력해 결과 안정성을 보고합니다 ([Zhao 2025](../sources/zhao-2025-phosphoproteomic-acetylomic-characterization-colorectal-cancer.md)). PTM-correction 개념 페이지는 phosphosite를 통계 unit으로 사용하더라도 **per-site λ(protein coupling coefficient)** 가 broad distribution(LUAD median 0.64)을 보여 단순 protein subtraction이 적절치 않음을 명시합니다 ([PTM-correction 개념](../concepts/ptm-correction-confounding-foundations.md)). 한미암 phosphoproteomics 파이프라인에서는 phosphopeptide → site-level mapping을 class I localization 기준으로 진행하되, 단백 추가 정량을 활용한 site-aware correction(ptmanchor 등)을 site 단위로 적용하는 방안을 참고할 수 있겠습니다.

**한미암 4축**: (B) 인산화단백체

**Cited**: [Hsu 2025](../sources/hsu-2025-phosphoproteomics-osimertinib-tolerant-persister-cells-reveals.md), [Zhao 2025](../sources/zhao-2025-phosphoproteomic-acetylomic-characterization-colorectal-cancer.md), [PTM-correction 개념](../concepts/ptm-correction-confounding-foundations.md)

**Filed**: `existing`.

### Q13. Phosphoproteome normalization — protein abundance correction이 왜 필요하며 어떤 방법(IRS, MaxLFQ, ratio)이 표준화되었나?

**A.** PTM-correction 개념 페이지는 CPTAC 7개 phosphoproteome cohort에서 raw-up phosphosite의 **38–55%(평균 46%)** 가 protein-driven으로 재분류되며, LUAD에서 protein-coupling coefficient λ의 median이 0.64로 단순 subtraction(λ ≡ 1)이 위반됨을 정량하여 site-aware correction의 필요성을 입증합니다 ([PTM-correction 개념](../concepts/ptm-correction-confounding-foundations.md)). Zhao 2025는 linear-regression residual correction(protein abundance 회귀잔차)으로 phosphosite·acetylsite를 보정해 22개 same-protein acetyl/phospho cross-talk pair를 식별합니다 ([Zhao 2025](../sources/zhao-2025-phosphoproteomic-acetylomic-characterization-colorectal-cancer.md)). Petralia 2024 CPTAC pan-cancer harmonization은 University of Michigan 파이프라인(MSFragger + Philosopher + TMT-Integrator) 후 **reference-intensity centering + outlier TMT multiplex 제거 + ComBat correction + DreamAI imputation + BCM phosphosite reannotation**을 표준 procedure로 채택합니다 ([Petralia 2024](../sources/petralia-2024-pan-cancer-proteogenomics-characterization-tumor-immunity.md)). 한미암 인산화단백체 파이프라인은 IRS · reference-intensity centering에 더해 ptmanchor-style per-site λ correction을 옵션으로 layer하면 kinase activity inference 해석 신뢰성을 검토할 수 있겠습니다.

**한미암 4축**: (B) 인산화단백체

**Cited**: [PTM-correction 개념](../concepts/ptm-correction-confounding-foundations.md), [Zhao 2025](../sources/zhao-2025-phosphoproteomic-acetylomic-characterization-colorectal-cancer.md), [Petralia 2024](../sources/petralia-2024-pan-cancer-proteogenomics-characterization-tumor-immunity.md)

**Filed**: `existing`.

### Q14. Kinase activity inference (KSEA, IKAP, PhosphoSitePlus, KSDB, ROKAI) — 알고리즘 vs substrate library 중 무엇이 정확도를 더 결정하는가?

**A.** Müller-Dott 2025 `benchmarKIN` 패키지는 perturbation + CPTAC tumor benchmark로 비교한 결과, **inference algorithm 선택보다 substrate library 선택이 성능을 더 좌우**하며 curated kinase-substrate resource(특히 PhosphoSitePlus + NetworKIN-derived 예측 보완)가 일반적으로 우월하다고 보고합니다 ([Müller-Dott 2025](../sources/muller-dott-2025-phosphoproteomic-kinase-activity-inference.md)). Jiang 2025 CoPheeKSA는 1,195 tumor × 11 cancer type의 co-regulation network로 26,280 phosphosite를 매핑하고, **24,015개 새로운 KSA + 26개 understudied kinase**(CDK12/SGK3/SMG1/NUAK1 등)를 추가해 substrate library 확장이 inference 정확도를 직접 끌어올림을 입증합니다 ([Jiang 2025](../sources/jiang-2025-dark-cancer-phosphoproteome-coregulation.md)). Kinase Activity Inference 합성 페이지는 site-aware correction과 substrate library 확장이 결합되면 **7개 kinase(BRAF/CSNK2A1/HIPK2/MAPK13/PRKCG/TBK1/TTK) 회복 + 16개 kinase 제거**라는 call layer 변화를 보고합니다 ([Kinase Inference 합성](../syntheses/kinase-activity-inference-under-ptm-correction.md)). 한미암 인산화단백체 kinase inference는 (i) PhosphoSitePlus + Kinase Library + CoPheeKSA library를 multi-source로 결합, (ii) KSEA·NetworKIN·KEA3를 ensemble로 운영하는 설계가 가능성 측면에서 참고할 수 있겠습니다.

**한미암 4축**: (B) 인산화단백체

**Cited**: [Müller-Dott 2025](../sources/muller-dott-2025-phosphoproteomic-kinase-activity-inference.md), [Jiang 2025](../sources/jiang-2025-dark-cancer-phosphoproteome-coregulation.md), [Kinase Inference 합성](../syntheses/kinase-activity-inference-under-ptm-correction.md)

**Filed**: `existing`.

### Q15. Dark phosphoproteome (annotation 부족 phosphosite) 의 co-regulation network 기반 functional 해석?

**A.** Jiang 2025의 CoPheeMap은 1,195 CPTAC tumor × 11 cancer type phosphoproteomics로 **26,280개 phosphosite의 co-regulation network**를 machine-learning으로 구축하고, 이를 feature로 사용한 CoPheeKSA가 24,015개 kinase-substrate association(9,399 phosphosite × 104 S/T kinase)을 새로 매핑해 dark phosphoproteome를 network learning 문제로 재정의합니다 ([Jiang 2025](../sources/jiang-2025-dark-cancer-phosphoproteome-coregulation.md)). Khan 2026은 3,825개 public phosphoproteomics dataset을 통합 메타분석해 TPD52 family의 conserved phosphosite(S171/S176/S149/S12/S166)와 **CAMK2D를 shared regulator**로 nominate하는 network 기반 dark-site functional 해석 사례를 제시합니다 ([Khan 2026](../sources/khan-2026-integrative-phosphoproteomic-network-analysis-identifies.md)). Kinase Inference 합성 페이지는 CoPheeKSA가 Kinase Library percentile에서 NetworKIN/LinkPhinder/PDT 대비 p≤0.0001로 우월하며, 56개 prediction이 PubMed text-mining에서 확증됨을 정리합니다 ([Kinase Inference 합성](../syntheses/kinase-activity-inference-under-ptm-correction.md)). 한미암 위암 인산화단백체에서 CoPheeMap/CoPheeKSA를 적용해 한국인 위암 특이 co-regulation module을 추출하면 dark-site functional 가설 발굴에 검토해 볼 만합니다.

**한미암 4축**: (B) 인산화단백체

**Cited**: [Jiang 2025](../sources/jiang-2025-dark-cancer-phosphoproteome-coregulation.md), [Khan 2026](../sources/khan-2026-integrative-phosphoproteomic-network-analysis-identifies.md), [Kinase Inference 합성](../syntheses/kinase-activity-inference-under-ptm-correction.md)

**Filed**: `existing`.

### Q16. Drug perturbation phosphoproteomics (CRC kinase inhibitor, osimertinib DTP 등) 에서 off-target signaling과 PTM crosstalk을 어떻게 분리?

**A.** Zhao 2025는 HCT116 CRC 세포주에 7개 kinase inhibitor(lapatinib/refametinib/PIK-93/Ro-3306/AT7519/ZSTK474/AS-605240) 1 μM 12시간 처리 후 TMTpro 6,147 protein + 5,048 class I phosphosite + 185 acetyl site를 측정해, PTM-SEA/KSEA가 **on-target effect(lapatinib→ERBB2 억제, AT7519→CDK1/2/6 억제)와 off-target signal(lapatinib→CDK4 활성화, PIK-93→CDK1/4 활성화)을 분리**함을 입증합니다 ([Zhao 2025](../sources/zhao-2025-phosphoproteomic-acetylomic-characterization-colorectal-cancer.md)). PTM crosstalk은 protein abundance에 대해 linear-regression residual로 보정 후 동일-단백질 acetyl/phospho pair 22개의 유의 상관(HNRNPA1 K350-S337, HSPD1 K72-S70 등)을 식별합니다. Hsu 2025 osimertinib DTP에서는 PCA로 DMSO/acute/DTP 상태를 분리(PC1 52.3%, PC2 13.4%)하고 KSEA + CausalPath로 acute에 억제되었던 PI3K-AKT/MAPK/PKA/PKC 신호가 DTP에서 reactivation됨을 확인해 phenotype-state별 signaling을 분리합니다 ([Hsu 2025](../sources/hsu-2025-phosphoproteomics-osimertinib-tolerant-persister-cells-reveals.md)). 한미암 약물 perturbation 분석에서는 protein abundance correction → KSEA → causal network 순서로 layer해 off-target과 PTM crosstalk을 분리하는 워크플로를 참고할 수 있겠습니다.

**한미암 4축**: (B) 인산화단백체 + (E) 치료반응 예측

**Cited**: [Zhao 2025](../sources/zhao-2025-phosphoproteomic-acetylomic-characterization-colorectal-cancer.md), [Hsu 2025](../sources/hsu-2025-phosphoproteomics-osimertinib-tolerant-persister-cells-reveals.md)

**Filed**: `existing`.

### Q17. PP2A / phosphatase axis 가 weak genomic driver 환경에서 종양 phenotype을 구동하는 evidence?

**A.** Asuzu 2025는 pituitary adenoma의 15%만 somatic mutation이 발견되는 weak-driver 환경에서, Cushing's disease(CD) adenoma 환자에서 **PPP1R17(PP2A 내인성 inhibitor) 과발현이 epigenetic reactivation을 통해 hyperphosphorylation phenotype을 구동**함을 multi-omics(ATAC + methylation + transcriptome + proteome + phosphoproteome)로 보였고, **FDA-approved PP2A agonist 소분자가 PPP1R17-매개 종양형성을 in vitro/in vivo에서 reversible**하게 억제함을 입증합니다 ([Asuzu 2025](../sources/asuzu-2025-phosphoproteomic-dysregulation-drives-tumor-proliferation.md)). 이는 driver mutation이 약한 종양에서도 **kinase-phosphatase balance(PP2A axis)** 가 직접 표적 가능한 lever임을 의미합니다. PTM-correction 개념 페이지는 phosphosite의 ~46%가 protein-driven으로 재분류된다는 점을 고려하면 phosphatase axis 검출에는 site-aware correction이 필수임을 시사합니다 ([PTM-correction 개념](../concepts/ptm-correction-confounding-foundations.md)). 한미암 위암 코호트에서 weak-driver 또는 microsatellite-stable 환자군에 PP2A regulator(PPP2R1A/PPP2R2B/PPP1R17) RNA·단백 발현을 layer하면 phosphatase axis 기반 환자층화 가설을 검토해 볼 만합니다.

**한미암 4축**: (B) 인산화단백체

**Cited**: [Asuzu 2025](../sources/asuzu-2025-phosphoproteomic-dysregulation-drives-tumor-proliferation.md), [PTM-correction 개념](../concepts/ptm-correction-confounding-foundations.md)

**Filed**: `existing`.

### Q18. PIM kinase / NDRG1 S330 / SHMT1 등 metabolic-signaling crosstalk을 phosphoproteome으로 어떻게 매핑?

**A.** Zhao 2026 CRLM proteogenomics는 LM 단백체에서 **SHMT1-formate-AMPK 축**(SHMT1 KD ↑p-AMPK, formate ↓, AICAR ↑↑, 125 mM formate drinking water ↑tumor burden in vivo)과 **NDRG1 S330p ubiquitin-degradation 축**(NDRG1 S330 ↔ actin cytoskeleton ρ=0.43 p=0.013; S330A 변이는 KAP intrasplenic 모델에서 ↓liver metastasis)을 mechanistic하게 동시 입증합니다 ([Zhao 2026](../sources/zhao-2026-proteogenomic-characterization-reveals-metabolic-vulnerabilities.md)). PIM family(PIM1/2/3)는 Johnson 2023 Kinase Library에서 NDRG1 S330 phosphorylation 후보 1위로 예측되며, **TP-3654 3 μM(pan-PIM inhibitor)** 처리가 NDRG1 S330p ↓, migration/invasion ↓, p-AMPK ↑를 유발해 PIM이 AMPK 음 조절과 NDRG1 degradation을 동시 매개하는 dual axis임을 보입니다. 기본 KSEA DB로는 PIM activity detection 실패해 **PhosphoSitePlus v6.7.5 확장 DB**로 PIM1 LM activity ↑(Wilcoxon p<0.001) 검출함을 명시합니다. 한미암 위암 인산화단백체에서 SHMT1·NDRG1 S330·PIM family를 metabolic-kinase crosstalk module로 검토하고, 확장 substrate library로 KSEA inference detection sensitivity를 보강하는 방안을 참고할 수 있겠습니다.

**한미암 4축**: (B) 인산화단백체 + (E) 치료반응 예측

**Cited**: [Zhao 2026](../sources/zhao-2026-proteogenomic-characterization-reveals-metabolic-vulnerabilities.md)

**Filed**: `existing`.

### Q19. AURKB, GRK2, CDK4 등 actionable kinase target을 phosphoproteome으로 우선순위화하는 framework?

**A.** Lee 2026 Korean TNBC 50명 코호트는 PTM-SEA phospho-kinase activity로 **GRK2 + GRK5 + RAPAMYCIN + CDK2 cluster를 non-pCR에 enrich**시키고, paired pre/post 분석에서 residual tumor에 **AURKB phosphoproteome 신호**가 지속됨을 확인한 뒤 (i) GRK2 inhibitor(βARK1) + paclitaxel은 MDA-MB-231 Bliss synergy 8.08, (ii) **barasertib(Aurora B inhibitor) 10 nM + paclitaxel은 MDA-MB-468/HCC1937/SBO-72 organoid에서 cell viability 감소**를 in vitro로 검증해 phospho-driven target prioritization framework를 완성합니다 ([Lee 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md)). Chang 2026 Taiwanese GC 154명은 **CDK4를 actionable hub**로 nominate해 IHC-positive + proteome-defined-positive(HER2/PD-L1/CLDN18.2 high) + IHC-negative(49.2%) 3 subgroup 공통 candidate로 palbociclib/ribociclib repurposing 후보 제시합니다 ([Chang 2026](../sources/chang-2026-integrative-proteogenomics-gastric-cancer-taiwan.md)). Savage 2024 CPTAC pan-cancer 1,043 tumor 분석도 **protein overexpression/hyperactivation-driven dependency**를 cell-line genetic screen·drug response와 통합해 우선순위화하는 framework를 정립했습니다 ([Savage 2024](../sources/savage-2024-pan-cancer-proteogenomics-expands-landscape-therapeutic.md)). 한미암 위암 인산화단백체에서 PTM-SEA + 외부 DepMap dependency + organoid functional validation의 3-layer prioritization을 검토할 수 있겠습니다.

**한미암 4축**: (B) 인산화단백체 + (E) 치료반응 예측

**Cited**: [Lee 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md), [Chang 2026](../sources/chang-2026-integrative-proteogenomics-gastric-cancer-taiwan.md), [Savage 2024](../sources/savage-2024-pan-cancer-proteogenomics-expands-landscape-therapeutic.md)

**Filed**: `existing`.

### Q20. Lactylome (Xu 2026 HER2-low breast)이 cancer signaling 해석에 추가하는 차원과 phospho와의 crosstalk?

**A.** Xu 2026 중국 HER2-low breast 코호트(prospective 115 tumor)는 phosphoproteome 43,963 site와 동시에 **lactylome 18,214 site / 1,644 protein**(timsTOF Pro + IMAC + PTM-1404 antibody)을 정량해 cancer multi-PTM landscape에 lactylation 차원을 추가합니다 ([Xu 2026](../sources/xu-2026-proteogenomic-characterization-reveals-subtype-specific-therapeutic.md)). 핵심 phospho-lactyl crosstalk으로 (i) **PRKDC K2694/K2908 lactylation ↔ kinase activity ↑ + PFS ↓**(DNA-PK 의존 저항), (ii) **STAT1 K193 lactylation + T727 phosphorylation ↔ STAT1 TF activity**(VIPER+DoRothEA), (iii) AURKB lactylation 매개 조절을 보고합니다. 3개 lactylomic subtype LS1/2/3은 PFS log-rank p=0.00172로 strong prognostic stratification을 보였고, histone Kla H2B K5/H3 K27 등 50+ site는 HER2-high에서 더 높은 패턴을 보입니다. Zhao 2025 CRC perturbation 분석은 같은 단백질 내 acetyl/phospho 22 pair에서 cross-talk 상관을 확인해 multi-PTM crosstalk framework의 일반성을 시사합니다 ([Zhao 2025](../sources/zhao-2025-phosphoproteomic-acetylomic-characterization-colorectal-cancer.md)). 한미암 위암 코호트에서 phospho + acetyl + lactyl 다중 PTM layer를 결합하면 metabolic-signaling crosstalk 해석에 검토해 볼 만합니다.

**한미암 4축**: (B) 인산화단백체

**Cited**: [Xu 2026](../sources/xu-2026-proteogenomic-characterization-reveals-subtype-specific-therapeutic.md), [Zhao 2025](../sources/zhao-2025-phosphoproteomic-acetylomic-characterization-colorectal-cancer.md)

**Filed**: `existing`.

## Section C — WGS-Proteome integration / pQTL / ppQTL (Q21-30)

### Q21. pQTL vs eQTL — 같은 driver variant이 RNA와 protein layer에서 다르게 매핑되는 빈도와 그 의미?

**A.** Chen 2026 germline SV 분석은 364개 recurrent SV-altered gene 중 **17%(129/364)만 mRNA+protein concordant**, **33%는 protein-only direction**(reverse, mRNA 변화 약함)이며 MS-based proteomics가 mRNA-only로 못 잡는 cis-effect를 포착함을 명시합니다 ([Chen 2026](../sources/chen-2026-global-impact-germline-structural-variation-cancer-proteome.md)). Savage 2024 CPTAC pan-cancer 1,043 tumor 분석은 gene-wise mRNA-protein correlation이 cohort별·gene class별로 폭이 매우 크며 secreted protein/다른 biology가 weak correlation을 유도하므로 **transcript-only heuristic보다 protein-level target selection**이 필수임을 입증합니다 ([Savage 2024](../sources/savage-2024-pan-cancer-proteogenomics-expands-landscape-therapeutic.md)). Li 2023 pan-cancer proteogenomics는 oncogenic driver의 cis/trans-effect를 RNA·protein·phosphoprotein 3 layer에서 정량해 **driver별로 RNA만 / protein 양쪽 / phospho까지 영향이 다르게 분기**됨을 정리합니다 ([Li 2023](../sources/li-2023-pan-cancer-proteogenomics-connects-oncogenic-drivers.md)). 한미암 위암 코호트에서 pQTL/ppQTL 분석은 eQTL과 별도 layer로 산출하고, 동일 SNV/SV의 RNA-only vs protein-also 분기 패턴을 카테고리화해 driver consequence 해석에 활용할 수 있겠습니다.

**한미암 4축**: (C) WGS-단백체 통합

**Cited**: [Chen 2026](../sources/chen-2026-global-impact-germline-structural-variation-cancer-proteome.md), [Savage 2024](../sources/savage-2024-pan-cancer-proteogenomics-expands-landscape-therapeutic.md), [Li 2023](../sources/li-2023-pan-cancer-proteogenomics-connects-oncogenic-drivers.md)

**Filed**: `existing`.

### Q22. Copy-number-to-protein effect의 cis vs trans hotspot — 어느 chromosomal region이 가장 강하게 trans-acting?

**A.** Sambath 2026 인도 자궁경부암 코호트는 **CNA-protein trans hotspot으로 6q / 9q / 11p / 22q**를 명시하며, EGFR 7p amp + STK11 SV deletion + chromothripsis가 결합된 저항 환자군에서 단백체 top5 up(SERPINB7/STX3/LBP/EMILIN2/NQO2; STX3는 IHC 32명 validation 일관 elevated)이 별도 chromosomal hotspot trans-effect의 후보임을 시사합니다 ([Sambath 2026](../sources/sambath-2026-integrated-genomic-proteomic-cervical-cancer-chemoradiation-resistance.md)). Petralia 2024 CPTAC 1,056 tumor pan-cancer immunity 분석은 **9p21 loss (CDKN2A/B + MTAP)** 가 wound-healing/proliferative immune-cold state와 연결됨을 보여 9p21이 trans-acting immune phenotype hotspot임을 정리합니다 ([Petralia 2024](../sources/petralia-2024-pan-cancer-proteogenomics-characterization-tumor-immunity.md)). Xu 2026 HER2-low breast는 **TP53 mut + 9p loss (MTAP cis)** 가 HER2-low 한정 poor prognosis임을 입증해 9p loss의 임상 trans-effect를 추가합니다 ([Xu 2026](../sources/xu-2026-proteogenomic-characterization-reveals-subtype-specific-therapeutic.md)). 한미암 위암 코호트도 GISTIC2 + 단백체로 cis(같은 chr 단백)와 trans(원거리 chromosome 단백) hotspot을 별도 매핑해 trans-acting CNA의 immune·signaling 영향을 검토할 수 있겠습니다.

**한미암 4축**: (A) WGS 변이 + (C) WGS-단백체 통합

**Cited**: [Sambath 2026](../sources/sambath-2026-integrated-genomic-proteomic-cervical-cancer-chemoradiation-resistance.md), [Petralia 2024](../sources/petralia-2024-pan-cancer-proteogenomics-characterization-tumor-immunity.md), [Xu 2026](../sources/xu-2026-proteogenomic-characterization-reveals-subtype-specific-therapeutic.md)

**Filed**: `existing`.

### Q23. Driver-to-functional-state mapping: KRAS G12C, EGFR L858R, TP53 mut 같은 driver가 어떤 protein/phospho functional state로 번역되는가?

**A.** Li 2023 pan-cancer proteogenomics는 oncogenic driver의 cis/trans-effect를 RNA·protein·phosphoprotein layer에서 정량하고, **다수 cancer gene이 sequence-based kinase activity profile로 정의된 유사 molecular state로 수렴**한다는 driver-to-functional-state convergence 패턴을 보고합니다 ([Li 2023](../sources/li-2023-pan-cancer-proteogenomics-connects-oncogenic-drivers.md)). Petralia 2024는 STK11 mutation이 `CD8-/IFNG+` immune subtype, BAP1/CASP8가 `CD8+/IFNG+`, KEAP1/NFE2L2가 wound-healing immune-cold phenotype과 연관됨을 정량합니다 ([Petralia 2024](../sources/petralia-2024-pan-cancer-proteogenomics-characterization-tumor-immunity.md)). Song 2024 Korean NSCLC 229명은 EGFR mutation을 Subtype 1(metabolic, female-dominant, WGD-frequent)과 Subtype 2(alveolar-like, no WGD)로 분기시키고, KRAS-enriched immunogenic Subtype 5(adjuvant therapy benefit)와 hypoxic Subtype 4(CSNK2A1/GSK3B 활성, SLK S347/LRRFIP1 S581 phospho-marker)를 정의합니다 ([Song 2024](../sources/song-2024-proteogenomic-analysis-reveals-non-small-cell.md)). 한미암 위암 코호트에서 TP53/CDH1/RHOA/HER2 driver별로 단백체-인산화단백체 functional state mapping을 수행하면 driver convergence vs divergence 패턴을 한국인 위암에서 검토할 수 있겠습니다.

**한미암 4축**: (A) WGS 변이 + (C) WGS-단백체 통합

**Cited**: [Li 2023](../sources/li-2023-pan-cancer-proteogenomics-connects-oncogenic-drivers.md), [Petralia 2024](../sources/petralia-2024-pan-cancer-proteogenomics-characterization-tumor-immunity.md), [Song 2024](../sources/song-2024-proteogenomic-analysis-reveals-non-small-cell.md)

**Filed**: `existing`.

### Q24. CGI methylation 매개 SV → protein 저발현 mechanism (Chen 2026)이 cancer susceptibility gene (CSG) screening에 주는 시사점?

**A.** Chen 2026은 **688개 cancer susceptibility gene 중 31개**(CDH13/CDKN2A/MSR1/SDHA/SMAD4/SMARCB1 포함)에 LoF germline SV 보유자에서 단백 저발현이 enrich되며, **101명(전체 6%)** 이 최소 1개 CSG LoF SV를 보유함을 보고합니다 ([Chen 2026](../sources/chen-2026-global-impact-germline-structural-variation-cancer-proteome.md)). CGI methylation 매개 sub-rosa cis-mechanism으로 **1,237개 CGI probe** FDR<10%, 233/2,686 positive methylation → negative mRNA 방향, 28개 protein concordant(CES1/GGACT/PTDSS2)와 **109 enhancer methylation pair (41 CBTN reproducible, p<1E-22)** 가 식별되어, CSG screening이 단순 coding SNV·LoF SV에 더해 CGI/enhancer methylation 매개 silencing까지 포함해야 sensitivity가 유지됨을 시사합니다. 한미암 한국인 위암 CSG screening은 (i) WGS Delly ∩ SVABA LoF SV call + (ii) 450K/EPIC methylation array를 보조 modality로 결합 + (iii) MS-based 단백체 evidence 통합하는 3-layer 워크플로를 검토할 수 있겠습니다. 특히 CDH13/CDKN2A/SMAD4/SMARCB1는 한국인 위암 후보 패널에 우선 포함될 만한 유전자로 사료됩니다.

**한미암 4축**: (A) WGS 변이 + (C) WGS-단백체 통합

**Cited**: [Chen 2026](../sources/chen-2026-global-impact-germline-structural-variation-cancer-proteome.md)

**Filed**: `existing`.

### Q25. Ancestry-enriched SV/CNA → protein effect (African/Asian/European 특이 gene) 의 precision oncology implication?

**A.** Chen 2026 1KGP-projection 기반 ancestry 분석에서 **69개 concordant cis-regulated gene 중 31개(45%)** 가 ancestry-enriched SV로 설명되며, **10 African(FSCN1) / 8 Asian(TIGAR) / 13 European(CTSW)** 으로 분기됨을 정량합니다 ([Chen 2026](../sources/chen-2026-global-impact-germline-structural-variation-cancer-proteome.md)). SIDT2 등 일부 gene은 ancestry 그 자체만으로 explain되어, ancestry 보정 후 SV effect가 사라지므로 **ancestry-aware analysis가 cis-cancer effect 식별에 필수**임을 입증합니다. Xu 2026 중국 HER2-low breast 코호트는 TP53 mut + 9p loss가 HER2-low 한정 poor prognosis(HER2-high에서는 비유의)임을 보여 동아시아 cohort 특이 co-occurrence를 제시합니다 ([Xu 2026](../sources/xu-2026-proteogenomic-characterization-reveals-subtype-specific-therapeutic.md)). Chang 2026 Taiwanese GC는 DBAC PAH signature가 TCGA에서는 부재하고 Taiwanese·Japanese cohort에서만 재현됨을 명시합니다 ([Chang 2026](../sources/chang-2026-integrative-proteogenomics-gastric-cancer-taiwan.md)). 한미암 한국인 위암 코호트는 KOVA·KCDC를 ancestry baseline으로 두고, 1KGP East Asian super-population referencing으로 한국 특이 SV/CNA → protein effect를 분리해 precision oncology biomarker 발굴에 검토해 볼 만합니다.

**한미암 4축**: (A) WGS 변이 + (C) WGS-단백체 통합

**Cited**: [Chen 2026](../sources/chen-2026-global-impact-germline-structural-variation-cancer-proteome.md), [Xu 2026](../sources/xu-2026-proteogenomic-characterization-reveals-subtype-specific-therapeutic.md), [Chang 2026](../sources/chang-2026-integrative-proteogenomics-gastric-cancer-taiwan.md)

**Filed**: `existing`.

### Q26. Proteogenomic NMF subtype (PT1-PT4, PS1-PS3 등) vs WGS-based subtype의 임상 prognostic concordance?

**A.** Chang 2026 Taiwanese GC는 **4개 tumour proteome cluster(PT1–PT4) + 5개 immune cluster(IM1–IM5)** Sankey 통합에서 PT1-IM3가 **stage IV 사망률 초과**(분기 p=0.025)를 보이며 PT1↔Bormann type 3(p=0.002), PT2↔HP+(p=0.003), PT3↔diffuse(p=0.02), PT4↔intestinal(p=0.01)으로 단순 WGS·histology 분류와 partial concordance만 유지함을 입증합니다 ([Chang 2026](../sources/chang-2026-integrative-proteogenomics-gastric-cancer-taiwan.md)). Xu 2026 HER2-low breast는 **3 proteomic subtype(PS1 estrogen / PS2 angiogenesis / PS3 proliferation+HER2-high-like)** 가 IHC HER2-low/HER2-high 단순 분류 위에 별도 prognostic stratification을 추가하고, RWD 14명 항혈관신생 치료 PS2 3/4 CR/PR vs PS1+PS3 1/10으로 임상 분기를 입증합니다 ([Xu 2026](../sources/xu-2026-proteogenomic-characterization-reveals-subtype-specific-therapeutic.md)). Lee 2026 Korean TNBC NMF 5 subtype도 Lehmann 분류와 부분 일치만 보이며 METABRIC 외부 검증(n=258, 76.3% mappable)에서 동일 prognostic pattern을 재현합니다 ([Lee 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md)). 한미암 위암 코호트도 proteogenomic NMF subtype을 WGS-based subtype(예: TCGA STAD 4-class)과 cross-tabulate해 concordance와 추가 prognostic information을 정량할 수 있겠습니다.

**한미암 4축**: (C) WGS-단백체 통합 + (E) 치료반응 예측

**Cited**: [Chang 2026](../sources/chang-2026-integrative-proteogenomics-gastric-cancer-taiwan.md), [Xu 2026](../sources/xu-2026-proteogenomic-characterization-reveals-subtype-specific-therapeutic.md), [Lee 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md)

**Filed**: `existing`.

### Q27. Driver-rare gene (CSG, low-frequency mutated) 에서 protein-level evidence가 mRNA evidence보다 강한 사례?

**A.** Chen 2026 분석은 364 recurrent SV-altered gene 중 **33%(약 120개)가 reverse direction(protein 변화 우세, mRNA 변화 약함)** 으로 MS-based proteomics만 cis-effect를 잡아내는 사례를 카탈로그하고, 대표 mRNA·protein concordant LoF locus로 CA8/PTGR1을 명시합니다 ([Chen 2026](../sources/chen-2026-global-impact-germline-structural-variation-cancer-proteome.md)). Zhao 2026 CRLM도 **ARG1 protein-only LM ↑ → poor OS T+LM**, **SOD2 (DepMap CRC/HCC dependency, protein-only) discovery p=0.098 → validation n=87 IHC p=0.0331**로 protein-only evidence가 prognostic biomarker로 살아남는 driver-rare 사례를 보고합니다 ([Zhao 2026](../sources/zhao-2026-proteogenomic-characterization-reveals-metabolic-vulnerabilities.md)). Sambath 2026 인도 자궁경부암은 단백체 top5 up SERPINB7/STX3/LBP/EMILIN2/NQO2 중 **STX3가 IHC 32명에서 일관 elevated**한 protein-level resistance marker로 입증되었으나 RNA-only로는 약한 신호임을 시사합니다 ([Sambath 2026](../sources/sambath-2026-integrated-genomic-proteomic-cervical-cancer-chemoradiation-resistance.md)). 한미암 위암 코호트도 low-frequency mutated gene에서 protein-only direction을 별도 카테고리로 분리해 prognostic discovery에 활용할 수 있겠습니다.

**한미암 4축**: (C) WGS-단백체 통합

**Cited**: [Chen 2026](../sources/chen-2026-global-impact-germline-structural-variation-cancer-proteome.md), [Zhao 2026](../sources/zhao-2026-proteogenomic-characterization-reveals-metabolic-vulnerabilities.md), [Sambath 2026](../sources/sambath-2026-integrated-genomic-proteomic-cervical-cancer-chemoradiation-resistance.md)

**Filed**: `existing`.

### Q28. AS event (alternative splicing)의 protein-level validation rate와 cancer-specific AS biology 사례?

**A.** Sinitcyn 2023 ENCODE 6 세포주 × 6 protease ultra-deep DDA 분석은 **AS event 13,450개 중 34.3%(양방향 6,145개 중 18.6%)가 단백 검출**, frame-preserving 64%, XGBoost AUC 0.83(top features: transcript abundance + PSI + frame status; PSI ~33%가 최적)으로 RNA-predicted AS의 protein-level validation rate를 정량합니다 ([Sinitcyn 2023](../sources/sinitcyn-2023-global-detection-human-variants-isoforms-deep-proteome.md)). Lehe 2026 review는 SWATH-DIA 2,964 isoform-specific peptide / Astral DIA 935 AS event/일 / IS-PRM 77 long-read-predicted isoform peptide / 일반 DDA 0–10 AS peptide의 acquisition 매트릭스를 정리합니다 ([Lehe 2026](../sources/lehe-2026-mass-spectrometry-alternative-protein-isoforms-review.md)). Awasthi 2026 PEXMap는 cancer pooled proteome 1.15M peptide에서 **EGFR truncated NP_958441.1**(EXj 17–19 supported, kinase-domain peptide 부재 — Lynch/Paez 2004 exon-19 deletion 정합)과 **FLNA exon-30 skipped NP_001447.2** 사례를 EXj 증거로 입증합니다 ([Awasthi 2026](../sources/awasthi-2026-pexmap-proteogenomic-exon-isoform-mapping.md)). Zhao 2026 CRLM은 226,107 AS event 중 148개가 C1/C2 cluster 차이 / 98개가 prognostic(KHK/RPP21/U2AF1L4 top)이며 GRB7 AS와 splicing factor C2 ↑(DHX9/PRPF8/SNRPD1) cancer dependency 연관을 보고합니다 ([Zhao 2026](../sources/zhao-2026-proteogenomic-characterization-reveals-metabolic-vulnerabilities.md)). 한미암 위암 코호트에서 long-read RNA-seq + DIA-MS + PEXMap을 결합해 cancer-specific AS isoform의 protein-level evidence를 추적할 수 있겠습니다.

**한미암 4축**: (C) WGS-단백체 통합

**Cited**: [Sinitcyn 2023](../sources/sinitcyn-2023-global-detection-human-variants-isoforms-deep-proteome.md), [Lehe 2026](../sources/lehe-2026-mass-spectrometry-alternative-protein-isoforms-review.md), [Awasthi 2026](../sources/awasthi-2026-pexmap-proteogenomic-exon-isoform-mapping.md), [Zhao 2026](../sources/zhao-2026-proteogenomic-characterization-reveals-metabolic-vulnerabilities.md)

**Filed**: `existing`.

### Q29. Pan-cancer CPTAC scale의 driver-to-functional-state landscape (Li 2023, Petralia 2024, Savage 2024)을 한미암 위암 코호트에 어떻게 transfer?

**A.** Li 2023 pan-cancer proteogenomics는 driver cis/trans-effect 정량과 sequence-based kinase activity convergence를 제시해 한미암 위암 코호트의 driver call을 동일 framework로 cis/trans · kinase profile · convergence 3 layer로 표현하는 reference로 활용 가능합니다 ([Li 2023](../sources/li-2023-pan-cancer-proteogenomics-connects-oncogenic-drivers.md)). Petralia 2024 7 immune subtype(`CD8+/IFNG+` 외 6) + STK11/KEAP1/BAP1/CASP8 driver-immune association + OAK atezolizumab arm validation은 위암 ICI 반응 예측의 immune-context branch로 transfer 가능합니다 ([Petralia 2024](../sources/petralia-2024-pan-cancer-proteogenomics-characterization-tumor-immunity.md)). Savage 2024 2,863 druggable protein/synthetic lethality/공공 neoantigen(mutant KRAS peptide) prioritization 워크플로는 LinkedOmicsKB·target portal을 직접 활용해 위암 단백체에 druggable target landscape를 매핑할 수 있습니다 ([Savage 2024](../sources/savage-2024-pan-cancer-proteogenomics-expands-landscape-therapeutic.md)). Chang 2026 Taiwanese GC는 동일 framework가 위암에서 실제 작동함을 보여준 동아시아 검증 사례입니다 ([Chang 2026](../sources/chang-2026-integrative-proteogenomics-gastric-cancer-taiwan.md)). 한미암은 (i) CPTAC 동일 파이프라인 채택(MSFragger + TMT-Integrator + reference centering + BCM phosphosite reannotation), (ii) 위암 7-cancer (Chang) NMF cluster mapping, (iii) Savage druggable target portal cross-link 3단계로 transfer 설계를 검토할 수 있겠습니다.

**한미암 4축**: (C) WGS-단백체 통합 + (E) 치료반응 예측

**Cited**: [Li 2023](../sources/li-2023-pan-cancer-proteogenomics-connects-oncogenic-drivers.md), [Petralia 2024](../sources/petralia-2024-pan-cancer-proteogenomics-characterization-tumor-immunity.md), [Savage 2024](../sources/savage-2024-pan-cancer-proteogenomics-expands-landscape-therapeutic.md), [Chang 2026](../sources/chang-2026-integrative-proteogenomics-gastric-cancer-taiwan.md)

**Filed**: `existing`.

### Q30. Long-read WGS (PacBio, Nanopore) vs short-read의 SV calling gap이 cancer proteome에서 missed cis-effect로 나타나는 추정?

**A.** Chen 2026은 paired SV caller(Delly v3.1.1 ∩ SVABA v1.2.0)가 **short-read 한계로 일부 LoF SV가 잘림**(paired caller LoF 일부 누락 + Delly/SVABA short-read limitation)을 한계로 본문 명시하며, **long-read WGS는 적용되지 않음**을 분명히 합니다 ([Chen 2026](../sources/chen-2026-global-impact-germline-structural-variation-cancer-proteome.md)). Ramberger 2024 multiple myeloma는 **nanopore WGS(CNV) + TMT phosphoproteomics**로 CNA-기능상태 연결과 phosphoproteomic risk stratification 사례를 제시해 long-read WGS의 proteogenomic integration potential을 시사합니다 ([Ramberger 2024 (analyses page reference via topic hub)](../topics/cancer-multiomics-literature.md)). Awasthi 2026 PEXMap는 long-read RNA-seq 기반 isoform DB를 활용해 EGFR truncated/FLNA exon-30 skipped 같은 cancer-specific isoform을 EXj 단위로 supported, short-read 기반 reference에서 놓치는 isoform-level proteomic evidence를 회수합니다 ([Awasthi 2026](../sources/awasthi-2026-pexmap-proteogenomic-exon-isoform-mapping.md)). 한미암 위암 코호트에서 PacBio HiFi 또는 ONT long-read WGS를 일부 환자(예: EGFR/MYC/ERBB2 high amplification, 의심 ecDNA 환자)에 한정 적용하면 short-read 미검출 SV → protein cis-effect gap을 정량할 수 있겠습니다.

**한미암 4축**: (A) WGS 변이 + (C) WGS-단백체 통합

**Cited**: [Chen 2026](../sources/chen-2026-global-impact-germline-structural-variation-cancer-proteome.md), [Awasthi 2026](../sources/awasthi-2026-pexmap-proteogenomic-exon-isoform-mapping.md)

**Filed**: `existing`.

## Section D — Spatial / single-cell multi-omics (Q31-40)

### Q31. Visium / Xenium / CosMx / Open-ST의 sensitivity, specificity, spatial resolution 차이와 spillover/off-target probe binding 문제?

**A.** Bilous 2026 Nat Methods는 10x Xenium 공간전사체 플랫폼에서 transcript spillover가 TME 해석을 왜곡할 수 있음을 체계적으로 정량하고 **RCTD 기반 signal purification 방법 SPLIT**으로 cell-type purity와 tumor-proximal T-cell exhaustion signal을 개선합니다 ([Bilous 2026](../sources/bilous-2026-xenium-sensitivity-specificity-signal-contamination.md)). Hallinan 2026 eLife는 Off-target Probe Tracker(OPT) 도구로 Xenium **human breast 313-gene panel 중 14개 이상이 protein-coding gene off-target binding 영향**을 받음을 식별하고, 동일 tumor block의 Xenium·Visium CytAssist·3' scRNA-seq 비교로 일부 유전자 신호가 target+off-target aggregate를 반영함을 입증합니다 ([Hallinan 2026](../sources/hallinan-2026-evidence-off-target-probe-binding-affecting.md)). Janesick 2023 Nat Commun은 FFPE human breast에서 Xenium(in situ) + Visium(spot) + 3' scRNA-seq 통합으로 TME 이질성을 분석하는 reference workflow를 제공합니다 ([Janesick 2023](../sources/janesick-2023-high-resolution-mapping-tumor-microenvironment.md)). 한미암 위암 spatial transcriptomics 적용 시 (i) custom panel 설계 단계 OPT QC, (ii) Xenium·Visium·scRNA-seq cross-platform validation, (iii) SPLIT 같은 spillover correction을 표준 워크플로로 검토할 수 있겠습니다.

**한미암 4축**: (D) 신항원-면역(공간 layer)

**Cited**: [Bilous 2026](../sources/bilous-2026-xenium-sensitivity-specificity-signal-contamination.md), [Hallinan 2026](../sources/hallinan-2026-evidence-off-target-probe-binding-affecting.md), [Janesick 2023](../sources/janesick-2023-high-resolution-mapping-tumor-microenvironment.md)

**Filed**: `existing`.

### Q32. Spatial transcriptomics → spatial proteomics → spatial multi-omics로의 stepwise transition: 각 단계의 신호 보존도?

**A.** Yeo 2026 cHL은 **spatial proteomics + spatial transcriptomics 결합**으로 EBV+/EBV- subtype 차이를 cellular neighborhood 단위로 정량하고, HRS proximity·LMP1 발현 distance-dependent로 CD8 T cell terminal exhaustion이 강화됨을 입증합니다 ([Yeo 2026](../sources/yeo-2026-epstein-barr-virus-orchestrates-spatial-reorganization.md)). Wu 2026 iCLAP는 TSA 기반 iterative amplification + fluorophore inactivation으로 FFPE에서 **40개 이상 marker 통합 검출**이 가능하며 IMC·CyCIF·CODEX와 결합되어 low-abundance protein(transcription factor·secreted protein·senescence marker)을 in situ로 잡아냅니다 ([Wu 2026](../sources/wu-2026-iclap-innovative-method-integrable-detection-low.md)). Sussman 2026 pediatric HGG는 snRNA + snATAC + WGS + CODEX spatial proteomics 4-modality longitudinal atlas 사례를 제시합니다 ([Sussman 2026](../sources/sussman-2026-longitudinal-single-cell-spatial-multiomic-atlas.md)). Barone 2026 lung adenocarcinoma는 spatial proteomics에서 CD4+AICL+와 CD8+KLRF1+가 non-tumor region에 enrich되며 tumor 내부에서 감소함을 정량해 multi-omics layer 간 신호 일치성을 입증합니다 ([Barone 2026](../sources/barone-2026-aicl-klrf-axis-supports-cell-communication.md)). 한미암 위암 다층 공간 분석은 spatial transcriptomics → CODEX/iCLAP proteomics → snRNA-seq 통합 stepwise 설계로 layer 간 신호 보존도를 검토할 수 있겠습니다.

**한미암 4축**: (D) 신항원-면역(공간 layer)

**Cited**: [Yeo 2026](../sources/yeo-2026-epstein-barr-virus-orchestrates-spatial-reorganization.md), [Wu 2026](../sources/wu-2026-iclap-innovative-method-integrable-detection-low.md), [Sussman 2026](../sources/sussman-2026-longitudinal-single-cell-spatial-multiomic-atlas.md), [Barone 2026](../sources/barone-2026-aicl-klrf-axis-supports-cell-communication.md)

**Filed**: `existing`.

### Q33. Spatial cell ecotype (TME state, immune cluster) 정의가 prognosis 예측력에 추가하는 정보량?

**A.** Zhang 2026 Nature(Spatial EcoTyper / Liquid EcoTyper)는 다수 암종의 공간전사체와 단일세포 데이터를 통합해 **9개 TME spatial ecotype**을 정의하고, Liquid EcoTyper로 plasma cfDNA methylation에서 회수해 **melanoma ICI response 예측**에 활용한 사례를 제시합니다 ([Zhang 2026 EcoTypes](../sources/zhang-2026-non-invasive-tumour-microenvironment-spatial-ecotypes.md)). Chang 2026 Taiwanese GC는 **4 proteome cluster(PT1–PT4) + 5 immune cluster(IM1–IM5)** Sankey 통합에서 PT1-IM3가 stage IV 사망률 초과(p=0.025)이며 단일 PT1만 보면 잡히지 않는 prognostic stratification을 추가함을 입증합니다 ([Chang 2026](../sources/chang-2026-integrative-proteogenomics-gastric-cancer-taiwan.md)). Petralia 2024 7 immune subtype은 CPTAC pan-cancer 1,056 tumor에서 OAK atezolizumab arm에서 `CD8+/IFNG+` subtype이 PFS benefit과 연관됨을 입증합니다 ([Petralia 2024](../sources/petralia-2024-pan-cancer-proteogenomics-characterization-tumor-immunity.md)). 한미암 위암 코호트에서 single-cell + spatial deconvolution으로 spatial ecotype을 정의하고 PT × IM × cfDNA Liquid EcoTyper의 3-layer 통합을 검토하면 prognosis 예측력 추가 정보량을 정량할 수 있겠습니다.

**한미암 4축**: (D) 신항원-면역 + (E) 치료반응 예측

**Cited**: [Zhang 2026 EcoTypes](../sources/zhang-2026-non-invasive-tumour-microenvironment-spatial-ecotypes.md), [Chang 2026](../sources/chang-2026-integrative-proteogenomics-gastric-cancer-taiwan.md), [Petralia 2024](../sources/petralia-2024-pan-cancer-proteogenomics-characterization-tumor-immunity.md)

**Filed**: `existing`.

### Q34. Single-cell + spatial 통합으로 tumor heterogeneity의 transcriptional vs spatial axis를 어떻게 layer?

**A.** Wang 2026 cSCLC는 multi-region WES(95 region/16명) + ST(6명) + snRNA-seq(12명) 통합으로 동일 환자 내 SCLC/NSCLC 성분이 **monoclonal origin은 공유하지만 mutation·CNA 패턴은 분기**하며 COL11A1+ CAF가 종양 도메인 경계에서 immune exclusion을 매개함을 보여줍니다 ([Wang 2026](../sources/wang-2026-spatial-multi-omics-unveils-monoclonal-origin.md)). Zhang 2026 cross-species CRC atlas는 인간 CRC와 Apc-min 생쥐의 N-A-C 단계 scRNA + ST 통합으로 **EFNA1-EPHA4 axis가 TAM immunosuppression + 종양 stemness를 매개**함을 도출합니다 ([Zhang 2026 CRC](../sources/zhang-2026-cross-species-single-cell-spatial-transcriptomic.md)). Yang 2026 NSCLC 53명은 snRNA-seq + GeoMx DSP + CosMx SMI 통합으로 IGHG1+ MEC와 myCAF가 invasive front에서 r=0.900으로 공간 co-localize, MIF-CD74/APP-CD74 axis가 brain metastasis HR=5.495를 매개함을 정량합니다 ([Yang 2026](../sources/yang-2026-ighg-malignant-epithelial-cell-mycaf-crosstalk.md)). Quail 2026 Cell review는 cancer ecosystem을 분자→세포→조직→organismal→temporal scale로 통합하는 framework를 제시합니다 ([Quail 2026](../sources/quail-2026-cancer-ecosystems-dynamic-interplay-across-scales.md)). 한미암 위암 코호트는 단일세포 transcriptional state × spatial niche 두 축을 layer해 heterogeneity 좌표를 정의할 수 있겠습니다.

**한미암 4축**: (D) 신항원-면역(공간)

**Cited**: [Wang 2026](../sources/wang-2026-spatial-multi-omics-unveils-monoclonal-origin.md), [Zhang 2026 CRC](../sources/zhang-2026-cross-species-single-cell-spatial-transcriptomic.md), [Yang 2026](../sources/yang-2026-ighg-malignant-epithelial-cell-mycaf-crosstalk.md), [Quail 2026](../sources/quail-2026-cancer-ecosystems-dynamic-interplay-across-scales.md)

**Filed**: `existing`.

### Q35. 비실측 spatial이 없는 sample에서 histology + foundation model로 spatial gene expression을 imputing하는 정확도?

**A.** Tran 2026 Phoenix는 routine H&E 병리 슬라이드에서 Xenium-like **single-cell spatial gene expression을 deep learning foundation model로 imputing**해, 대규모 병리 아카이브를 치료반응·예후·공간 TME biomarker 탐색 자원으로 전환하는 pan-cancer virtual spatial transcriptomics framework를 제시합니다 ([Tran 2026](../sources/tran-2026-phoenix-pan-cancer-virtual-spatial-transcriptomics.md)). Cui 2026 Haiku는 H&E + mIF + clinical text를 tri-modal contrastive foundation model로 정렬해 cross-modal retrieval, 임상 예측, zero-shot biomarker 추론을 동시에 강화합니다 ([Cui 2026](../sources/cui-2026-haiku-tri-modal-spatial-biology-histology.md)). Hoang 2024 Nat Cancer는 deep learning framework로 histopathology image에서 **imputed transcriptomics**를 거쳐 cancer treatment response를 예측하는 architecture를 제시해 spatial-blind sample에서도 transcriptional signal 회수가 가능함을 시사합니다 ([Hoang 2024](../sources/hoang-2024-deep-learning-framework-predict-cancer.md)). 한미암 위암 코호트의 large 병리 archive(FFPE H&E)에 Phoenix·Haiku 같은 모델을 적용해 비실측 spatial transcriptomics를 보강하는 방안을 검토할 수 있겠습니다.

**한미암 4축**: (D) 신항원-면역(공간) + (E) 치료반응 예측

**Cited**: [Tran 2026](../sources/tran-2026-phoenix-pan-cancer-virtual-spatial-transcriptomics.md), [Cui 2026](../sources/cui-2026-haiku-tri-modal-spatial-biology-histology.md), [Hoang 2024](../sources/hoang-2024-deep-learning-framework-predict-cancer.md)

**Filed**: `existing`.

### Q36. Spatial multi-omics가 chemoresistance (CAF, POSTN+ CAF, IGHG1+ epithelial-myCAF crosstalk 등)를 어떻게 dissect?

**A.** Sakai 2026 직장암 single-cell spatial multiomics는 **POSTN+ CAF가 chemoradiotherapy resistance**의 핵심 driver임을 분리해내며 stromal cell-tumour interaction을 spatial 단위로 정의합니다 ([Sakai 2026](../sources/sakai-2026-postn-cafs-chemoradiotherapy-resistance-rectal-cancer.md)). Yang 2026 NSCLC 53명은 IGHG1+ malignant epithelial cell-myCAF crosstalk이 invasive front에서 MIF-CD74/APP-CD74 axis로 brain metastasis HR=5.495를 매개함을 spatial multiomics로 입증합니다 ([Yang 2026](../sources/yang-2026-ighg-malignant-epithelial-cell-mycaf-crosstalk.md)). Wang 2026 cSCLC는 COL11A1+ aggressive fibroblast subtype이 종양 도메인 경계를 형성해 immune exclusion을 매개함을 보고합니다 ([Wang 2026](../sources/wang-2026-spatial-multi-omics-unveils-monoclonal-origin.md)). Agirre-Lizaso 2026 iCCA는 MARCO+ TAM이 TH2-skewed immune response + collagen deposition + worse survival을 매개하며 Marco-/-/anti-MARCO 항체 처치로 종양 성장 억제됨을 입증해 macrophage-driven chemoresistance niche를 dissect하는 사례를 제시합니다 ([Agirre-Lizaso 2026](../sources/agirrelizaso-2026-marco-promotes-cholangiocarcinogenesis-inducing-immunosuppression-its.md)). 한미암 위암 spatial multiomics 분석에서 CAF subtype(POSTN+/COL11A1+/myCAF) + TAM subtype(MARCO+)를 spatial niche 단위로 매핑하면 chemoresistance 메커니즘 가설을 검토할 수 있겠습니다.

**한미암 4축**: (D) 신항원-면역 + (E) 치료반응 예측

**Cited**: [Sakai 2026](../sources/sakai-2026-postn-cafs-chemoradiotherapy-resistance-rectal-cancer.md), [Yang 2026](../sources/yang-2026-ighg-malignant-epithelial-cell-mycaf-crosstalk.md), [Wang 2026](../sources/wang-2026-spatial-multi-omics-unveils-monoclonal-origin.md), [Agirre-Lizaso 2026](../sources/agirrelizaso-2026-marco-promotes-cholangiocarcinogenesis-inducing-immunosuppression-its.md)

**Filed**: `existing`.

### Q37. CAR-T efficacy + spatial transcriptomics — TIL infiltration pattern과 임상 outcome의 spatial signature?

**A.** Wang 2026 CD19/20 CAR-T phase I/II 32명 코호트(R/R B-NHL, NCT04723914)는 best ORR 74%/CR 58%, mPFS 6.8 mo, mOS 22.1 mo, CAR-T expansion peak day 7–17, long-term responder persistence 500일 초과의 임상 결과를 보였고, pretreatment biopsy 5명의 spatial single-cell transcriptomics에서 **두 가지 tumor architecture**를 식별합니다 ([Wang 2026 CAR-T](../sources/wang-2026-clinical-outcomes-spatial-transcriptomic-profiles-car.md)). (1) **B-cell-dominant phenotype**에서는 malignant B cell의 apoptotic competence가 durable response의 결정인자, (2) **fibroblast/monocyte/macrophage-enriched phenotype**에서는 chemokine-rich T-cell-permissive microenvironment가 durable response의 결정인자임을 보여, dual-axis stratification framework를 제시합니다. Normal LDH 환자에서 response rate가 더 높아 baseline LDH가 보조 stratification factor로 시사됩니다. Zou 2026 commentary는 NSCLC ICI 효능 예측에서 CD8+ TIL **tumor nest proximity**가 aggregate density보다 우월하며 CD73 upregulation 포함 3-variable spatial composite가 PD-L1보다 substantial하게 더 잘 예측함을 정리합니다 ([Zou 2026](../sources/zou-2026-understanding-immune-checkpoint-inhibitor-efficacy-through.md)). 한미암 위암 CAR-T·면역치료 후보군에서도 pretreatment biopsy spatial profiling으로 tumor architecture를 분류하고 outcome 결정인자를 dual-axis로 평가하는 설계를 참고할 수 있겠습니다.

**한미암 4축**: (D) 신항원-면역 + (E) 치료반응 예측

**Cited**: [Wang 2026 CAR-T](../sources/wang-2026-clinical-outcomes-spatial-transcriptomic-profiles-car.md), [Zou 2026](../sources/zou-2026-understanding-immune-checkpoint-inhibitor-efficacy-through.md)

**Filed**: `existing`.

### Q38. Patient-derived organoid + spatial multi-omics가 treatment response 예측에 주는 추가 정보?

**A.** Lee 2026 Korean TNBC는 patient-derived organoid **SBO-72**(IRB 4-2023-0098)에서 barasertib(10 nM Aurora B inhibitor) + paclitaxel 시너지를 MDA-MB-468·HCC1937와 함께 검증해 phospho-driven target hypothesis(AURKB)를 PDO-level functional readout으로 closing the loop합니다 ([Lee 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md)). Xu 2026 HER2-low breast는 17개 patient-derived organoid (PDO)에서 PS1↑tamoxifen·toremifen / PS2↑bevacizumab·apatinib / PS3↑trastuzumab·T-DM1로 **subtype-specific drug response를 PDO에서 직접 검증**하고, RWD 14명 anti-angiogenic 코호트 PS2 3/4 CR/PR vs PS1+PS3 1/10으로 RWD validation까지 연결합니다 ([Xu 2026](../sources/xu-2026-proteogenomic-characterization-reveals-subtype-specific-therapeutic.md)). Zhao 2026 CRLM KAP organoid(Villin-CreERT2; Kras-LSL-G12D; Apc-min/+; Trp53-flox/flox) intrasplenic 모델은 Shmt1 KD ↓liver metastasis, NDRG1 S330A 변이도 ↓liver metastasis로 mechanistic vulnerability를 검증합니다 ([Zhao 2026](../sources/zhao-2026-proteogenomic-characterization-reveals-metabolic-vulnerabilities.md)). 한미암 위암 코호트에서 PDO + 단백체/인산화단백체 + spatial multiomics 결합으로 subtype-specific drug sensitivity를 검증하는 closed-loop framework를 참고할 수 있겠습니다.

**한미암 4축**: (E) 치료반응 예측

**Cited**: [Lee 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md), [Xu 2026](../sources/xu-2026-proteogenomic-characterization-reveals-subtype-specific-therapeutic.md), [Zhao 2026](../sources/zhao-2026-proteogenomic-characterization-reveals-metabolic-vulnerabilities.md)

**Filed**: `existing`.

### Q39. Spatial deconvolution algorithm (GraphST, Cell2location, RCTD, ultra-precision deconvolution) 비교?

**A.** Xu 2026 UCASpatial(Shannon entropy weighting + WNNLS)은 simulated ST 750 spot 벤치마크에서 median RMSE 0.051로 **RCTD 0.058 (10%↓), SPOTlight 0.066 (21%↓), CARD/Spotiphy 0.075 (31%↓), cell2location 0.081 (36%↓), stereoscope 0.080 (35%↓)** 대비 일관 우월하며, fine-grained 20개 cell subpopulation reference 조건과 5~20 cells/spot 범위에서도 robust한 성능을 보고합니다 ([Xu 2026 UCASpatial](../sources/xu-2026-ultra-precision-deconvolution-spatial-transcriptomics-decodes.md)). Long 2023 GraphST는 graph neural network + self-supervised contrastive learning으로 spatial clustering·integration·deconvolution 3개 task를 동시에 처리하며 기존 method보다 우월함을 보고합니다 ([Long 2023](../sources/long-2023-spatially-informed-clustering-integration-deconvolution.md)). Bilous 2026은 RCTD 기반 **SPLIT signal purification**으로 Xenium spillover를 보정해 cell-type purity·tumor-proximal T-cell exhaustion signal을 개선하는 reference를 추가합니다 ([Bilous 2026](../sources/bilous-2026-xenium-sensitivity-specificity-signal-contamination.md)). 한미암 위암 spatial 분석은 UCASpatial(low-abundance immune subset 우월) → GraphST(다중 task 통합) → SPLIT(spillover correction)의 다단계 layer로 deconvolution 결과 신뢰성을 정량할 수 있겠습니다.

**한미암 4축**: (D) 신항원-면역(공간)

**Cited**: [Xu 2026 UCASpatial](../sources/xu-2026-ultra-precision-deconvolution-spatial-transcriptomics-decodes.md), [Long 2023](../sources/long-2023-spatially-informed-clustering-integration-deconvolution.md), [Bilous 2026](../sources/bilous-2026-xenium-sensitivity-specificity-signal-contamination.md)

**Filed**: `existing`.

### Q40. Pediatric brain tumor / 소아 cancer longitudinal spatial atlas의 design lesson과 성인 cohort 적용 가능성?

**A.** Sussman 2026 pediatric high-grade glioma 16명 longitudinal atlas는 **snRNA-seq(400,000+ cells) + snATAC-seq(110,000+ cells, 평균 2,280 gene/19,094 unique fragment) + WGS + CODEX spatial proteomics**를 1차 절제·재발/진행·autopsy 3 timepoint에 결합해, post-therapy interferon/oligodendrocyte/myeloid shift와 in vitro Danusertib 같은 malignant cell-intrinsic target까지 검증한 closed-loop discovery 사례입니다 ([Sussman 2026](../sources/sussman-2026-longitudinal-single-cell-spatial-multiomic-atlas.md)). Chen 2026 germline SV 연구도 **CBTN(Children's Brain Tumor Network)** cohort에서 41개 enhancer-methylation SV가 p<1E-22로 reproduce되어 성인 cancer에서 발견된 germline SV cis-mechanism이 소아·희귀암으로 transfer 가능함을 입증합니다 ([Chen 2026](../sources/chen-2026-global-impact-germline-structural-variation-cancer-proteome.md)). Wang 2026 CAR-T B-NHL 코호트(성인)도 longitudinal sampling + spatial 결합의 효용성을 보여줍니다 ([Wang 2026 CAR-T](../sources/wang-2026-clinical-outcomes-spatial-transcriptomic-profiles-car.md)). 한미암 위암 코호트도 1차 진단 → 치료 후 reassessment → progression/autopsy 3 timepoint longitudinal sampling 설계와 snRNA + snATAC + WGS + spatial proteomics multi-modality framework를 참고할 수 있겠습니다.

**한미암 4축**: (D) 신항원-면역 + (E) 치료반응 예측

**Cited**: [Sussman 2026](../sources/sussman-2026-longitudinal-single-cell-spatial-multiomic-atlas.md), [Chen 2026](../sources/chen-2026-global-impact-germline-structural-variation-cancer-proteome.md), [Wang 2026 CAR-T](../sources/wang-2026-clinical-outcomes-spatial-transcriptomic-profiles-car.md)

**Filed**: `existing`.

## Section E — Response prediction / Resistance / Clinical translation (Q41-50)

### Q41. Primary vs acquired resistance를 multi-omic layer로 어떻게 분리해 비교하는가 (CRC anti-EGFR + KRAS G12Ci, NSCLC osimertinib DTP, breast TNBC NAC 등)?

**A.** Lee 2026 Korean TNBC는 baseline n=41과 paired post-treatment residual tumor n=22를 WES+RNA+TMT+phospho 4-layer로 측정해, **non-pCR(1차 내성)** 메커니즘은 estrogen response + GRK2 PTM-SEA + ITGB8 7p21 + AKR1C2 + ABCA13 5축으로, **residual tumor(잔존 종양)에서는 AURKB phospho + EMT/myogenesis enriched** 신호로 분리합니다 ([Lee 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md)). Hsu 2025 osimertinib DTP는 PCA로 DMSO/acute/DTP/recovery 4 상태를 분리(PC1 52.3%, PC2 13.4%), KSEA + CausalPath로 acute 억제 후 DTP에서 PI3K-AKT/MAPK/PKA/PKC re-activation, CDK1 substrate signaling, BAD S99/S118 hyperphospho를 **drug-tolerant persister(2차 내성 전 단계) 시그니처**로 정의합니다 ([Hsu 2025](../sources/hsu-2025-phosphoproteomics-osimertinib-tolerant-persister-cells-reveals.md)). Memon 2024 NSCLC 1,201명 코호트는 PD-(L)1 acquired resistance(initial responder 60%↑)에서 **IFNγ signature "stable" vs "increase" stratification + B2M loss + 항원제시 결함**을 paired pre/post WES + transcriptome으로 분리합니다 ([Memon 2024](../sources/memon-2024-clinical-molecular-features-acquired-resistance.md)). 한미암 위암 1차 vs 2차 내성 분석은 baseline–residual–progression 3 timepoint sampling + WES/WGS+RNA+단백체+phospho multi-layer에서 axis별로 (driver mutation / phospho-program / immune state) 분리해 비교할 수 있겠습니다.

**한미암 4축**: (E) 치료반응 예측

**Cited**: [Lee 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md), [Hsu 2025](../sources/hsu-2025-phosphoproteomics-osimertinib-tolerant-persister-cells-reveals.md), [Memon 2024](../sources/memon-2024-clinical-molecular-features-acquired-resistance.md)

**Filed**: `existing`.

### Q42. RECIST / pCR / OS / PFS endpoint vs molecular endpoint (signaling activation, immune signature)의 prediction model 통합 strategy?

**A.** Lee 2026 Korean TNBC는 임상 endpoint(pCR)와 molecular endpoint(estrogen GSVA + GRK2 PTM-SEA + ITGB8 7p21 + AKR1C2 + ABCA13)를 logistic regression에 통합해 **non-pCR AUC 0.946**로 Lehmann 분류(AUC 0.781) + Lehmann+ESTIMATE(AUC 0.818)를 능가하는 사례를 제시합니다 ([Lee 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md)). Sambath 2026 인도 자궁경부암은 RECIST CCRT sens 19/res 17 binary classification으로 OncoKB Level 1 33% / 2 11% / 3A 25% / 4 5%를 매핑하며, EGFR amp Level 3 약물·DNA repair pathway hyperactivation을 mechanism으로 layer합니다 ([Sambath 2026](../sources/sambath-2026-integrated-genomic-proteomic-cervical-cancer-chemoradiation-resistance.md)). Petralia 2024는 OAK trial RNA-classified `CD8+/IFNG+` 75/344명에서 atezolizumab arm PFS benefit이 docetaxel arm에서는 없음을 입증해 **treatment-specific molecular endpoint stratification**의 임상 검증을 제시합니다 ([Petralia 2024](../sources/petralia-2024-pan-cancer-proteogenomics-characterization-tumor-immunity.md)). Chang 2026은 decision tree EFS(stage+DBAC), OS(stage+C3+PT1+IM2/3)로 임상 변수 + molecular feature 통합 prognostic model을 제시합니다 ([Chang 2026](../sources/chang-2026-integrative-proteogenomics-gastric-cancer-taiwan.md)). 한미암 위암 코호트는 (i) 임상 endpoint(RECIST/pCR/OS/PFS) + (ii) molecular endpoint(phospho-driven kinase activity + immune subtype + driver mutation) ensemble model로 AUC 비교 및 SHAP feature ranking을 검토할 수 있겠습니다.

**한미암 4축**: (E) 치료반응 예측

**Cited**: [Lee 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md), [Sambath 2026](../sources/sambath-2026-integrated-genomic-proteomic-cervical-cancer-chemoradiation-resistance.md), [Petralia 2024](../sources/petralia-2024-pan-cancer-proteogenomics-characterization-tumor-immunity.md), [Chang 2026](../sources/chang-2026-integrative-proteogenomics-gastric-cancer-taiwan.md)

**Filed**: `existing`.

### Q43. Drug-tolerant persister (DTP) cell state의 phosphoproteome signature와 임상 minimal residual disease와의 관계?

**A.** Hsu 2025는 PC9 EGFR exon19del NSCLC 세포주에서 osimertinib 160 nM·21일 처리로 reversible drug-tolerant persister 상태를 형성하고, DIA-MS 기반 21,500 phosphopeptide/condition 측정으로 acute–DTP–recovery transition을 분리해 **CDK1 substrate(PML S518, SAMHD1 T592) + mTOR/S6 + YAP1/CYR61 + BAD S99/S118 hyperphosphorylation + MAPK/PI3K/PKA/PKC rebound**을 DTP-specific phosphoproteome signature로 정의합니다 ([Hsu 2025](../sources/hsu-2025-phosphoproteomics-osimertinib-tolerant-persister-cells-reveals.md)). 저자들은 KSEA + CausalPath로 acute 억제 후 DTP에서 anti-apoptotic survival program이 재활성됨을 보이고 vistusertib / NSC-663428 / CRISPR CDK1·CDK2 KO로 DTP-specific vulnerability를 in vitro 검증해, DTP가 단순 cell line artifact가 아닌 **임상 minimal residual disease(MRD)와 가장 가까운 reversible adaptive state**로 해석될 수 있음을 시사합니다. Lee 2026 한국인 TNBC는 paired pre/post NAC sampling(baseline n=41, residual n=22)에서 residual tumor가 **AURKB phosphoproteome + EMT/myogenesis enriched** 상태로 수렴함을 보여, 임상 잔존 종양에서도 DTP-like phospho-program이 검출 가능함을 직접 입증하며 barasertib + paclitaxel synergy로 targetability까지 제시합니다 ([Lee 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md)). 한미암 위암 코호트에서는 baseline → on-treatment(ctDNA MRD-positive 시점) → progression의 longitudinal sampling에 phospho-DTP feature set(CDK1·AURKB·BAD·mTOR·YAP1) 정량을 추가해, MRD 단계에서 reversible vulnerability를 선제적으로 표적할 수 있는 phospho-MRD framework를 검토할 수 있겠습니다.

**한미암 4축**: (B) 인산화단백체 + (E) 치료반응 예측

**Cited**: [Hsu 2025](../sources/hsu-2025-phosphoproteomics-osimertinib-tolerant-persister-cells-reveals.md), [Lee 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md)

**Filed**: `existing`.

### Q44. ICI resistance — KEAP1/STK11 변이, B2M loss, IFN-γ pathway disruption, neoantigen-loss escape, T cell exhaustion의 multi-omic 통합 readout?

**A.** Skoulidis 2018·2024는 KRAS-mutant LUAD에서 **STK11/LKB1 + KEAP1** co-alteration이 PD-(L)1 monotherapy에 대한 primary resistance를 일으키고(PCP cohort KEAP1 mut median PFS 2.7 vs WT 5.7 mo, OS 7.6 vs 16.6 mo; HR PFS 2.07 / OS 2.24), CTLA-4 co-blockade(durvalumab+tremelimumab POSEIDON arm)가 myeloid 억제 → CD4 effector 재활성으로 부분 reversal을 일으킬 수 있음을 입증합니다 ([Skoulidis 2018](../sources/skoulidis-2018-stk11-lkb1-pd1-resistance-kras-lung.md), [Skoulidis 2024](../sources/skoulidis-2024-ctla4-abrogates-keap1-stk11-resistance.md)). Memon 2024는 1,201명 NSCLC ICI 코호트의 acquired resistance(initial responder 60%↑)를 paired pre/post WES(n=22) + transcriptome(n=29)로 분석해 **IFNγ-response stable vs increase 2분층 + B2M LoF / class I HLA 단백 감소**의 antigen presentation 결함을 핵심 mechanism으로 보고하며, "deserted/excluded"가 아닌 **persistently inflamed but altered IFN response**라는 새 분류를 제시합니다 ([Memon 2024](../sources/memon-2024-clinical-molecular-features-acquired-resistance.md)). Petralia 2024는 CPTAC 1,056 종양의 pan-cancer 7-immune subtype 분석에서 KEAP1/NFE2L2를 wound-healing/IFNG-low cluster에, STK11을 `CD8-/IFNG+` cluster에 매핑하고 OAK trial 외부 검증으로 `CD8+/IFNG+` subtype이 atezolizumab arm PFS benefit과는 일치하지만 docetaxel arm에서는 그렇지 않음을 보여, **multi-omic immune subtype이 treatment-specific stratifier**임을 입증합니다 ([Petralia 2024](../sources/petralia-2024-pan-cancer-proteogenomics-characterization-tumor-immunity.md)). Chen 2026 germline SV proteome 분석은 LoF SV가 야기하는 1,847 low-protein outlier에서 **MHC class I antigen binding / antigen processing**가 핵심 enriched category임을 보여, germline level antigen presentation 취약성도 ICI resistance multi-omic readout에 추가 layer로 통합될 수 있음을 시사합니다 ([Chen 2026](../sources/chen-2026-global-impact-germline-structural-variation-cancer-proteome.md)). 한미암 위암 코호트는 (i) WGS driver(KEAP1/STK11/B2M), (ii) germline SV antigen presentation outlier, (iii) phospho-IFNGR/JAK-STAT signaling, (iv) Petralia 7-subtype immune cluster, (v) paired pre/post IFNγ-response trajectory를 5-layer ensemble readout으로 통합해 primary vs acquired resistance를 분리 평가할 수 있겠습니다.

**한미암 4축**: (A) WGS 변이 + (D) 신항원-면역 + (E) 치료반응 예측

**Cited**: [Skoulidis 2018](../sources/skoulidis-2018-stk11-lkb1-pd1-resistance-kras-lung.md), [Skoulidis 2024](../sources/skoulidis-2024-ctla4-abrogates-keap1-stk11-resistance.md), [Memon 2024](../sources/memon-2024-clinical-molecular-features-acquired-resistance.md), [Petralia 2024](../sources/petralia-2024-pan-cancer-proteogenomics-characterization-tumor-immunity.md), [Chen 2026](../sources/chen-2026-global-impact-germline-structural-variation-cancer-proteome.md)

**Filed**: extends `syntheses/resistance-convergence-framework.md` (ICI multi-layer readout).

### Q45. Basket trial / tumor-agnostic stratification (CPTAC pan-cancer therapeutic target)을 한미암 위암 코호트에 적용하는 framework?

**A.** Savage 2024는 CPTAC 10 종양형 1,043명 코호트에서 2,863개 druggable protein을 정량하고 **mRNA→protein discordance가 cohort마다 크게 변동**함을 보여, target nomination을 transcript-only가 아닌 protein abundance + phospho-activation + genetic screen + drug response 외부 evidence ensemble로 정의해야 함을 명시합니다 ([Savage 2024](../sources/savage-2024-pan-cancer-proteogenomics-expands-landscape-therapeutic.md)). Chakraborty 2024 review는 동일 framework를 "overexpression / hyperactivation-driven druggable dependency" + synthetic lethality + 공유 neoantigen(예: mutant KRAS peptide) 3 axis로 정리하며, 단일 omics layer가 놓치는 lineage-specific vulnerability를 pan-cancer 통합으로 회수할 수 있음을 강조합니다 ([Chakraborty 2024](../sources/chakraborty-2024-pan-cancer-proteogenomics-vulnerabilities-opportunities.md)). Chang 2026 Taiwan GC 코호트(n=154)는 이 logic을 위암에 직접 적용해 **IHC+ (HER2/MMR/CLDN18.2/PD-L1) 50% + proteome-defined high 26% + IHC-negative 24%** 3-tier 환자 stratification에서 **CDK4가 공통 actionable hub**(FOXM1/RB1/RBL2/WDR77 phospho ↑)로 nominated되며, KEA3 location-specific kinase mapping(Loc 2 ABL1/SYK/ROCK, Loc 3 BRAF/CDK4/ERBB2, Loc 4 MET)으로 anatomy-aware basket arm을 설계할 수 있음을 보였습니다 ([Chang 2026](../sources/chang-2026-integrative-proteogenomics-gastric-cancer-taiwan.md)). 한미암 위암 코호트는 (i) Savage 2024 druggable protein 2,863개 dictionary, (ii) Chang 2026 IHC + proteome-defined + IHC-negative 3-tier 분류, (iii) phospho-activation evidence 가중치, (iv) shared neoantigen(KRAS G12C/D peptide) 후보를 결합한 **proteogenomic basket trial framework**로 설계해, 단일 organ 분류가 아닌 functional state 기반 arm 분배(예: CDK4 hub arm, MET arm, CLDN18.2 ADC arm)를 검토할 수 있겠습니다. 단 Chang 2026이 명시한 "CDK4/6 단일제 GI 효과 미미(palbociclib phase II median PFS 1.8 mo)"는 비선택적 적용을 막는 주요 caveat로 사료됩니다.

**한미암 4축**: (C) WGS-단백체 통합 + (E) 치료반응 예측

**Cited**: [Savage 2024](../sources/savage-2024-pan-cancer-proteogenomics-expands-landscape-therapeutic.md), [Chakraborty 2024](../sources/chakraborty-2024-pan-cancer-proteogenomics-vulnerabilities-opportunities.md), [Chang 2026](../sources/chang-2026-integrative-proteogenomics-gastric-cancer-taiwan.md)

**Filed**: `existing`.

### Q46. AI 기반 drug response prediction (foundation model, multimodal histology + omics, LINCS L1000)의 외부 cohort 일반화 성능?

**A.** Liu 2025 MOFS는 IDH-wildtype 신경교종 FAHZZU1(n=122)에서 radiomics(5,929 MRI feature) + pathomics(CellProfiler) + WES + RNA-seq + DIA proteomics 5-layer를 11 fusion algorithm + COCA late fusion으로 통합한 3-subtype 분류(MOFS1/2/3)를, **17-algorithm ensemble transcriptomic classifier로 7개 외부 cohort(CGGA, GEO 6개)** 재현하고 **22-feature DNN radiomics classifier로 imaging-only n=992(FAHZZU3)**에서 log-rank P=0.00025로 prognostic separation을 외부 검증한 사례를 보고합니다 ([Liu 2025](../sources/liu-2025-multimodal-fusion-radio-pathology-proteogenomics-identify.md)). MOFS3 TME-rich subtype은 외부 anti-PD-1 GBM cohort(Zhao 2019, PRJNA482620)에서 responder 군 enriched로 검증되어, **단일 modality clustering은 외부 prognostic separation 회수 불가**하지만 multimodal fusion은 일반화 가능함을 입증합니다. Cui 2026 Haiku는 H&E + mIF + clinical text를 tri-modal contrastive embedding으로 정렬해 cross-modal retrieval / clinical prediction / zero-shot biomarker inference 성능을 동시에 끌어올린 foundation model 후보로 surface되었지만, 외부 cohort 정량 검증치는 본 wiki page에 아직 추출 안 된 상태입니다 ([Cui 2026](../sources/cui-2026-haiku-tri-modal-spatial-biology-histology.md)). Guo 2026 scaling benchmark는 drug discovery foundation model의 "larger=better" 가정을 22개 endpoint로 시험해 calibration 측면에서 단순 scaling이 항상 우수하지 않음을 시사하지만 deep-dive는 미진행입니다 ([Guo 2026](../sources/guo-2026-larger-models-scaling-benchmark-drug-discovery.md)). Chen 2024 UNI는 general-purpose pathology foundation model로 surface되었으나 외부 drug response cohort 일반화 정량치는 wiki 본 페이지에 아직 미정리입니다 ([Chen 2024](../sources/chen-2024-towards-general-purpose-foundation-model.md)). 한미암 위암 코호트는 (i) 자체 omics+H&E로 학습한 모델을 (ii) CPTAC pan-cancer + Chang 2026 Taiwan GC + Mun 2019 Korean EOGC 외부 cohort에서 ensemble classifier로 transfer 검증 후, (iii) MRI-only DNN surrogate를 통해 routine 임상 변수 단독 deployment 가능성을 단계적으로 평가하는 framework를 검토할 수 있겠습니다.

**한미암 4축**: (E) 치료반응 예측

**Cited**: [Liu 2025](../sources/liu-2025-multimodal-fusion-radio-pathology-proteogenomics-identify.md), [Cui 2026](../sources/cui-2026-haiku-tri-modal-spatial-biology-histology.md), [Chen 2024](../sources/chen-2024-towards-general-purpose-foundation-model.md), [Guo 2026](../sources/guo-2026-larger-models-scaling-benchmark-drug-discovery.md)

**Filed**: `evidence-gap` (Cui 2026 / Chen 2024 / Guo 2026 deep-dive 미진행 — 외부 cohort 정량치 후속 보강 필요).

### Q47. Patient stratification logistic / Cox model 의 feature 우선순위 — 환자 층화 시 어떤 protein/phospho feature가 가장 robust한가?

**A.** Lee 2026 한국인 TNBC는 5-feature logistic regression(**estrogen response GSVA high / GRK2 PTM-SEA high / no ITGB8 deep loss / AKR1C2 high / ABCA13 high**)이 non-pCR 예측 AUC **0.946**으로 Lehmann 분류(0.781)·Lehmann+ESTIMATE(0.818)를 능가하며, 5 feature 모두 (i) global proteome 시그니처, (ii) phosphosite-level kinase activity, (iii) 7p21 CN status, (iv) doxorubicin metabolism / efflux mRNA의 mixed-layer 구성이 stratification robustness의 핵심임을 보였습니다 ([Lee 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md)). Chang 2026 Taiwan GC는 Cox multivariable에서 stage + DBAC contribution이 EFS decision tree top split이며, **Loc 4 antrum-specific 5 protein/phospho biomarker(SHROOM1 / p-LYST S2627 / XYLT1 / CRIP1 / SPATS2L)** 가 KM Plotter 외부 cohort(n=118–875)에서 일관 검증되어 anatomy-conditional feature가 단일 feature보다 robust함을 시사합니다 ([Chang 2026](../sources/chang-2026-integrative-proteogenomics-gastric-cancer-taiwan.md)). Sambath 2026 인도 자궁경부암 코호트는 single-marker로 **STX3 단백 증가**가 추가 32명 IHC validation에서 resistant 환자에 일관 elevated, **EGFR 7p amplification**(OncoKB Level 3)이 resistant 환자 6/17에 cluster되어 actionable protein-CNA feature가 RECIST resistant 예측에 기여함을 보고합니다 ([Sambath 2026](../sources/sambath-2026-integrated-genomic-proteomic-cervical-cancer-chemoradiation-resistance.md)). Zhao 2026 CRLM은 LM proteome unsupervised clustering으로 C1(metabolism) / C2(RNA function) 2 subtype을 정의하고 **FTCD / GPD1 / SOD2 / EIF4B S422 phospho** 4-feature를 independent n=87 IHC cohort에서 OS/PFS log-rank p<0.05로 재현해, subtype + phospho biomarker hybrid가 robust임을 입증합니다 ([Zhao 2026](../sources/zhao-2026-proteogenomic-characterization-reveals-metabolic-vulnerabilities.md)). 공통 패턴은 **(a) single layer single feature보다 mixed-layer ensemble이 AUC를 일관 상승시키고, (b) anatomy/subtype/race conditional split이 globally averaged feature보다 외부 cohort 재현성이 높으며, (c) phospho-driven kinase activity(GRK2, p-LYST, EIF4B S422)가 protein abundance만으로 잡히지 않는 vulnerability를 보강**한다는 것입니다. 한미암 위암 코호트에서는 stage + anatomy(Chang Loc) + protein subtype + phospho-kinase activity의 4-layer ensemble Cox/logistic 모델 + SHAP feature ranking으로 외부 cohort cross-validation을 검토할 수 있겠습니다.

**한미암 4축**: (E) 치료반응 예측

**Cited**: [Lee 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md), [Chang 2026](../sources/chang-2026-integrative-proteogenomics-gastric-cancer-taiwan.md), [Sambath 2026](../sources/sambath-2026-integrated-genomic-proteomic-cervical-cancer-chemoradiation-resistance.md), [Zhao 2026](../sources/zhao-2026-proteogenomic-characterization-reveals-metabolic-vulnerabilities.md)

**Filed**: `existing` (recurring features documented; promote to concept page if 한미암 코호트가 추가 cross-cancer feature를 add하면 `concepts/cancer-multiomics-stratification-features.md` 분리 검토).

### Q48. Druggable target prioritization (Savage 2024) framework — synthetic lethality, dependency, surface targetability를 어떻게 통합?

**A.** Savage 2024는 CPTAC 10-cohort 1,043 종양에서 2,863개 druggable protein dictionary를 정의하고, target nomination 의사결정을 (i) **tumor proteomics + phosphoproteomics 기반 overexpression / hyperactivation evidence**, (ii) cell-line **genetic screen + drug response (e.g., DepMap, GDSC) dependency evidence**, (iii) **TSG loss → synthetic lethal partner mapping**, (iv) **MHC binding prediction 기반 shared(public) neoantigen 후보** (예: mutant KRAS peptide) 4 layer ensemble로 통합하는 framework를 제시합니다 ([Savage 2024](../sources/savage-2024-pan-cancer-proteogenomics-expands-landscape-therapeutic.md)). Hamilton 2024는 neuroblastoma surfaceome study에서 **proteomic + transcriptomic + epigenomic** 통합으로 60개 high-confidence surface immunotherapy target candidate를 nominate하고 DLK1(super-enhancer 연동)을 우선순위화한 뒤 ADCT-701 ADC로 xenograft 효능을 검증해, surface targetability axis가 단순 mRNA 단독으로는 신뢰할 수 없고 protein-level surface 정량이 필수임을 보였습니다 ([Hamilton 2024](../sources/hamilton-2024-proteogenomic-surfaceome-study-identifies-dlk1.md)). Lee 2026 TNBC는 동일 framework를 한국인 코호트에 적용해 **7p21 CN + Cancer Surfaceome Atlas 교집합 3개(ITGB8, THSD7A, TSPAN13)** 를 ADC 표적 후보로 nominate하고 SGN-B6A integrin-targeting ADC 개발 reference를 명시합니다 ([Lee 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md)). Han 2026은 HCT-116 CRC 세포주에서 ERK2 / PLK1 / PIK3CA / PAK4 CRISPR KO 각각의 phospho-rewiring을 KSEA + TMT 7,531 protein/10,877 phosphopeptide 통합으로 측정해 **ERK2 loss + RPS6KB1 inhibition의 synthetic lethal interaction**을 직접 nominate하며, dependency layer가 cell-line perturbation으로 보강될 수 있음을 보였습니다 ([Han 2026](../sources/han-2026-proteomics-phosphoproteomics-human-colorectal-cancer.md)). 한미암 위암 코호트에서는 (i) Savage 2024 druggable dictionary 매핑, (ii) Cancer Surfaceome Atlas 교차로 surface targetability sub-list 추출, (iii) DepMap dependency overlay, (iv) CDH1/TP53/ARID1A LoF → synthetic lethal partner inference, (v) shared neoantigen 후보(KRAS, mutant CDH1 등) prediction의 5-layer ensemble로 표적 우선순위표를 작성할 수 있겠습니다.

**한미암 4축**: (C) WGS-단백체 통합 + (D) 신항원-면역

**Cited**: [Savage 2024](../sources/savage-2024-pan-cancer-proteogenomics-expands-landscape-therapeutic.md), [Hamilton 2024](../sources/hamilton-2024-proteogenomic-surfaceome-study-identifies-dlk1.md), [Lee 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md), [Han 2026](../sources/han-2026-proteomics-phosphoproteomics-human-colorectal-cancer.md)

**Filed**: `existing`.

### Q49. EBV / HBV / HPV-associated cancer의 viral-driven proteome reshape이 면역치료 반응 예측에 주는 시사점?

**A.** Gao 2019는 HBV-related HCC paired tumor/NAT 159 환자 코호트에서 proteomic subgrouping으로 **3개 subtype**을 정의해 환자 생존·tumor thrombus·CTNNB1/TP53 변이 신호와 연결하고, mutated CTNNB1 → ALDOA phosphorylation → glycolysis 가속이라는 **HBV-driven metabolic reshape** 축을 검증해 viral-driven 종양의 면역치료 stratification이 단순 viral status 이항이 아닌 metabolic subtype별로 분리되어야 함을 시사합니다 ([Gao 2019](../sources/gao-2019-integrated-proteogenomic-characterization-hbv-related-hepatocellular.md)). Huang 2021은 HPV-negative HNSCC 108 코호트(WES+WGS+RNA+proteome+phospho)에서 **immune-cold tumors는 항원 부족이 아니라 IFNGR2/JAK2/IRF1 CN deletion 매개 antigen presentation machinery 결함이 핵심**이며, 통합 NMF로 정의된 Immune subtype은 multiple checkpoint/suppressor protein 동시 발현으로 PD-1 monotherapy보다 combination ICB를 시사함을 명시합니다 ([Huang 2021](../sources/huang-2021-proteogenomic-insights-biology-treatment-hpv-negative.md)). Sambath 2026 HPV-positive 인도 자궁경부암 36명은 SBS2/SBS13 APOBEC signature(84-92% 환자)와 PIK3CA helical/C2 변이가 co-occur하며, resistant 17명에 EGFR 7p amplification + STK11 SV deletion이 enriched되어 **HPV-driven APOBEC mutagenesis가 neoantigen 부담 + PI3K-AKT hyperactivation → CCRT resistance** 축을 동시에 만든다는 viral-driven proteome reshape mechanism을 보고합니다 ([Sambath 2026](../sources/sambath-2026-integrated-genomic-proteomic-cervical-cancer-chemoradiation-resistance.md)). Petralia 2024 pan-cancer 분석은 7-immune subtype 중 **`CD8-/IFNG+` subtype이 East Asian 환자에서 European 환자보다 enriched**임을 보여, viral-associated GC(EBV+) 같은 동아시아 특이 컨텍스트에서 IFNG signaling은 활성이지만 CD8 infiltration이 낮은 dissociated phenotype이 ICI 반응 예측에 중요한 layer임을 시사합니다 ([Petralia 2024](../sources/petralia-2024-pan-cancer-proteogenomics-characterization-tumor-immunity.md)). 한미암 위암 코호트는 EBV+ GC subset 식별 후 (i) HBV/HPV 사례 reference로 metabolic + antigen presentation + IFNG signaling 3-layer reshape를 분석하고, (ii) APOBEC signature와 phospho-PI3K-AKT axis 정량을 결합한 viral-driven ICI response predictor를 검토할 수 있겠습니다.

**한미암 4축**: (D) 신항원-면역 + (E) 치료반응 예측

**Cited**: [Gao 2019](../sources/gao-2019-integrated-proteogenomic-characterization-hbv-related-hepatocellular.md), [Huang 2021](../sources/huang-2021-proteogenomic-insights-biology-treatment-hpv-negative.md), [Sambath 2026](../sources/sambath-2026-integrated-genomic-proteomic-cervical-cancer-chemoradiation-resistance.md), [Petralia 2024](../sources/petralia-2024-pan-cancer-proteogenomics-characterization-tumor-immunity.md)

**Filed**: `existing` (Gao 2019 Key Points pending deep-dive — 단백 subtype 세부는 보강 여지).

### Q50. 한국인 / 동아시아 cohort specific finding (Korean NSCLC, Korean TNBC, Chinese HER2-low, Taiwanese GC, Indian cervical)을 한미암 위암 코호트에 비교 분석하는 방법론?

**A.** 다섯 개 Asia/South Asia cohort 모두 WES/WGS + RNA + TMT proteome + phosphoproteome 동일 4-layer protocol을 채택하고 raw data를 controlled-access(dbGaP / CPTAC PDC / NCBI BioProject)로 공개해 한미암 위암 코호트와 cross-cohort 재분석이 직접 가능합니다 ([Chen 2020 Taiwan NSCLC](../sources/chen-2020-proteogenomics-non-smoking-lung-cancer-east.md): PDC000219/220 + dbGaP phs001954; [Song 2024 Korean NSCLC](../sources/song-2024-proteogenomic-analysis-reveals-non-small-cell.md); [Lee 2026 Korean TNBC](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md): PDC000695/696 + PRJNA1422844/45; [Jiang 2024 Chinese 773 BC](../sources/jiang-2024-integrated-multiomic-profiling-breast-cancer.md); [Chang 2026 Taiwan GC](../sources/chang-2026-integrative-proteogenomics-gastric-cancer-taiwan.md): PDC000645/649 + dbGaP phs004447; [Sambath 2026 Indian cervical](../sources/sambath-2026-integrated-genomic-proteomic-cervical-cancer-chemoradiation-resistance.md)). 비교 방법론의 핵심은 (i) **race-specific driver enrichment 검증**(Jiang 2024 Asian AKT1 hotspot mutation enriched; Chang 2026 KMT2D 24% Asian vs TCGA 9-16%; CDH1 in female diffuse GC; PIK3CA 11% lower than Caucasian 12-26%; Chen 2020 EGFR 85% in non-smoking East Asian LUAD vs Western <30%), (ii) **environmental/dietary signature 재현**(Chang 2026 DBAC PAH signature가 Taiwan + Japan에 존재하지만 TCGA Western에는 absent — 한국 grilled meat 소비 패턴과 직접 매핑 검증 가능), (iii) **subtype label transfer**(Lee 2026 NMF 5-cluster + METABRIC k-NN mapping 76.3% assignment; Chang 2026 PT1-IM 분기 한미암 GC에서 stage 단독보다 강한 prognostic value 검증), (iv) **phospho-driven kinase activity cross-validation**(Petralia 2024 `CD8-/IFNG+` subtype이 East Asian에 enriched), (v) **shared regimen 매칭**(Lee 2026 AC→weekly paclitaxel 72% — carboplatin 12%만 사용으로 한국 임상 현실 그대로 반영) 5축으로 정리됩니다 ([Petralia 2024](../sources/petralia-2024-pan-cancer-proteogenomics-characterization-tumor-immunity.md)). 한미암 위암 코호트는 (a) 동일 4-layer protocol(WES/WGS+RNA+TMT+phospho) 채택, (b) Chang 2026 NMF subtype 재할당 + DBAC signature 재현성 검증, (c) Mun 2019 Korean EOGC + Jiao 2025 pangenome reference와 직접 통합 분석, (d) East Asian-specific feature(KMT2D / CDH1 female diffuse / DBAC / `CD8-/IFNG+`)를 한국 위암 cohort에서 priority 검증 target으로 설정하는 방법론을 검토할 수 있겠습니다.

**한미암 4축**: (A) WGS 변이 + (B) 인산화단백체 + (C) WGS-단백체 통합 + (D) 신항원-면역 + (E) 치료반응 예측

**Cited**: [Chen 2020](../sources/chen-2020-proteogenomics-non-smoking-lung-cancer-east.md), [Song 2024](../sources/song-2024-proteogenomic-analysis-reveals-non-small-cell.md), [Lee 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md), [Jiang 2024](../sources/jiang-2024-integrated-multiomic-profiling-breast-cancer.md), [Chang 2026](../sources/chang-2026-integrative-proteogenomics-gastric-cancer-taiwan.md), [Sambath 2026](../sources/sambath-2026-integrated-genomic-proteomic-cervical-cancer-chemoradiation-resistance.md), [Petralia 2024](../sources/petralia-2024-pan-cancer-proteogenomics-characterization-tumor-immunity.md)

**Filed**: `existing` (Jiang 2024 Key Points pending deep-dive — Chinese BC race-specific feature 정량치 후속 보강 여지).

## Connections

- [Cancer Multiomics Literature (topic hub)](../topics/cancer-multiomics-literature.md)
- [Cancer Multiomics Corpus Queue (Target=100)](cancer-multiomics-corpus-queue.md)
- [Drug Response Phospho-Global Proteomics Corpus Queue (Target=100)](drug-response-phospho-global-100-corpus-queue.md)
- [PTM Correction and Kinase Signaling Question Bank](ptm-correction-kinase-signaling-question-bank.md)
- [Four-Topic Question Expansion Map](topic-question-expansion-map.md) (Topic 4)
- [100-Question Wiki Expansion Sprint](100-question-wiki-expansion-sprint.md)
- [Resistance Convergence Framework](../syntheses/resistance-convergence-framework.md)
- [Kinase Activity Inference under PTM Correction](../syntheses/kinase-activity-inference-under-ptm-correction.md)

## Sources

- 14 new source pages from `topic-sweep-2026-05-25` (see topic hub Section "8. 2026-05 Topic Sweep Additions")
- 80+ existing `wiki/sources/` pages linked from cancer-multiomics-literature topic hub
- 한미암 project context: `wiki/_meta/han-mi-am-project-context.md`
