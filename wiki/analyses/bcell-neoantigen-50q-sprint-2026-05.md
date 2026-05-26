---
title: B-Cell / Neoantigen 50-Question Sprint (2026-05-25)
tags:
  - question-bank
  - wiki-expansion
  - b-cell-neoantigen
  - neoantigen-discovery
  - tls-biology
  - clinical-translation
themes:
  - neoantigen
  - b-cells
  - tls
  - vaccine
  - immunopeptidomics
date: 2026-05-25
status: completed-2026-05-25
---

# B-Cell / Neoantigen 50-Question Sprint (2026-05-25)

`b-cell-neoantigen-human-cancer` topic hub의 신착 28편(`topic-sweep-2026-05-25`) + 기존 230+ 시드를 활용해 50개 질문에 답하면서 wiki 확장. 답은 로컬 wiki pages + 신착 source pages 근거. 웹 외부 evidence 금지.

## 답변 정책

- Each answer cites at least one `wiki/sources/` page or `wiki/concepts/` page
- 답이 durable value를 만들면 별도 concept/synthesis page로 승격
- 답이 단발성이면 이 페이지에만 남김
- 답이 충분치 않으면 "evidence gap" 으로 표기하고 corpus queue에 후보 등록

## Section A — Neoantigen discovery & prioritization (Q1-12)

### Q1. Canonical SNV-derived neoantigen 후보 풀과 noncanonical (cryptic) antigen 풀은 한 환자에서 어떻게 비교되는가?
**A.** 한 환자 immunopeptidome에서 SNV-derived neoantigen은 보통 환자당 한 자릿수에서 수십 개 수준으로 매우 적게 검출되는 반면, noncanonical/cryptic peptide pool은 환자별 수십~수백 개로 훨씬 풍부하게 관찰될 수 있습니다. Raja 2025 ovarian cancer 연구는 5명 metastatic OC 환자에서 환자당 cryptic peptide 40~83개(총 311개)를 식별했고, 이들이 전체 peptide의 1% 미만임에도 known TSA/TAA보다 면역 우세한 antigen class임을 시사했습니다 ([Raja 2025](../sources/raja-2025-immunogenic-cryptic-peptides-dominate-antigenic.md)). PDAC에서도 ncHLAp의 약 30%가 cancer-restricted translation으로 검증되어 SNV 기반 풀과 별개로 환자 간 shared subset이 존재합니다 ([Ely 2025](../sources/ely-2025-pancreatic-cancer-restricted-cryptic-antigens-targets.md)). 즉 환자 한 명에서 cryptic pool이 SNV pool보다 수배 더 broad한 후보 자원으로 작용할 수 있겠습니다 ([Kina 2025](../sources/kina-2025-cryptic-immunopeptidome-health-disease.md)).

**Cited**: [Raja 2025](../sources/raja-2025-immunogenic-cryptic-peptides-dominate-antigenic.md), [Ely 2025](../sources/ely-2025-pancreatic-cancer-restricted-cryptic-antigens-targets.md), [Kina 2025](../sources/kina-2025-cryptic-immunopeptidome-health-disease.md)

**Filed**: existing

### Q2. RNA editing, alternative splicing, frameshift indel, gene fusion 각각이 신항원 풀에 기여하는 비율은 한 코호트에서 어떻게 분해되는가?
**A.** 단일 코호트에서 각 source class를 분해한 직접 비교는 드물지만, Tretter 2023 pan-tumor 32명 코호트는 multi-omics + immunopeptidomics로 후보 32개를 검증하면서 대다수가 RNA 차원의 variant에서 비롯됨을 보여 RNA-centered detection의 비중을 강조합니다 ([Tretter 2023](../sources/tretter-2023-proteogenomic-analysis-reveals-rna-source.md)). mRCC 101명에서는 ICI 반응군 간 461개 differentially spliced event가 식별되고 intron retention이 dominant motif였으며, IFFO1·ZNF692 splice-derived peptide가 후보로 부상해 splicing의 기여가 매우 큼을 시사합니다 ([Govindarajan 2026](../sources/govindarajan-2026-characterization-aberrant-alternative-splicing-landscape-patients.md)). POLAR HRD PC trial에서는 frameshift indel neoantigen enrichment가 PARP-ICB durable benefit과 연관되었고, Vendramin 2026은 NMD 억제로 frameshift/PTC 유래 후보가 high-TMB 수준까지 확장될 수 있음을 보고합니다 ([Park 2026](../sources/park-2026-pembrolizumab-olaparib-homologous-recombination-deficient-metastatic.md), [Vendramin 2026](../sources/vendramin-2026-nonsense-mediated-mrna-decay-inhibition-reshapes.md)). Fusion·RNA editing 정량은 cohort-level 비교가 본 corpus에서 thin해 보여집니다.

**Cited**: [Tretter 2023](../sources/tretter-2023-proteogenomic-analysis-reveals-rna-source.md), [Govindarajan 2026](../sources/govindarajan-2026-characterization-aberrant-alternative-splicing-landscape-patients.md), [Park 2026](../sources/park-2026-pembrolizumab-olaparib-homologous-recombination-deficient-metastatic.md), [Vendramin 2026](../sources/vendramin-2026-nonsense-mediated-mrna-decay-inhibition-reshapes.md)

**Filed**: existing

### Q3. NMD (nonsense-mediated decay) 억제가 cancer immunopeptidome을 어떻게 reshape하는지, 임상 적용 가능한 perturbation 전략은 무엇인가?
**A.** Vendramin 2026은 1,000명+ 환자 multi-omics·CPI 코호트에서 NMD 경로 핵심 kinase SMG1의 활성 감소가 ICI 반응 개선의 예측인자임을 보였고, SMG1 표적 억제가 premature termination codon(PTC) 포함 transcript(대부분 non-mutational origin)를 안정화해 MHC class I immunopeptidome을 high-TMB 수준까지 재편함을 입증했습니다 ([Vendramin 2026](../sources/vendramin-2026-nonsense-mediated-mrna-decay-inhibition-reshapes.md)). 기능적으로 NMD 억제는 antigen-dependent T cell mediated killing, tissue-resident T cell 활성화, in vivo ICI 효능 향상을 모두 유도하여 canonical mutant + non-canonical (frameshift, alternative ORF) epitope을 동시에 활용할 수 있는 axis를 제시합니다. 임상 적용 측면에서는 SMG1 inhibitor 약리학적 개발과 low-TMB·MSS 종양에서 ICI 병용을 비롯한 stratification 후보로 검토할 수 있는 전략으로 사료됩니다.

**Cited**: [Vendramin 2026](../sources/vendramin-2026-nonsense-mediated-mrna-decay-inhibition-reshapes.md)

**Filed**: existing

### Q4. Noncoding ORF / cryptic peptide의 신항원 잠재력을 immunopeptidomics로 검증한 사례는?
**A.** Ely 2025는 PDAC immunopeptidome을 high-resolution MS로 분석해 cancer-restricted noncanonical HLA-I-bound peptide(ncHLAp)를 다수 식별하고, 그중 약 30%가 cancer-restricted translation으로 검증되며 ex vivo T cell priming + TCR-redirected T cell이 patient-derived organoid에 cytotoxicity를 보임을 입증했습니다 ([Ely 2025](../sources/ely-2025-pancreatic-cancer-restricted-cryptic-antigens-targets.md), 해설 [Feng 2025](../sources/feng-2025-illuminating-cancer-therapy-cryptic-antigens.md)). Raja 2025 ovarian cancer 코호트는 311개 cryptic peptide를 immunopeptidomics + RNA-seq로 검증했고 prioritized cryptic peptide의 약 70%가 autologous CD8 T cell을 활성화(4-1BB, IFN-γ 상승)했습니다 ([Raja 2025](../sources/raja-2025-immunogenic-cryptic-peptides-dominate-antigenic.md)). Chong 2020·moPepGen 등은 ribosome profiling + WES/RNA-seq + dual MS/MS search로 ABCB5 downstream ORF 등 면역원성 ncHLAp를 sensitive하게 식별하는 proteogenomic pipeline을 제시합니다 ([Chong 2020](../sources/chong-2020-integrated-proteogenomic-deep-sequencing-analytics.md)).

**Cited**: [Ely 2025](../sources/ely-2025-pancreatic-cancer-restricted-cryptic-antigens-targets.md), [Raja 2025](../sources/raja-2025-immunogenic-cryptic-peptides-dominate-antigenic.md), [Chong 2020](../sources/chong-2020-integrated-proteogenomic-deep-sequencing-analytics.md), [Feng 2025](../sources/feng-2025-illuminating-cancer-therapy-cryptic-antigens.md)

**Filed**: existing

### Q5. 같은 환자 종양에서 immunopeptidomics-confirmed neoantigen과 predicted-only neoantigen의 ratio는 일반적으로 어느 정도인가?
**A.** Predicted candidate 수백~수천 개 중 MS로 confirm되는 비율은 보통 1% 이하로 보고되며, CRC organoid immunopeptidomics에서는 HLA class I neoantigen landscape가 매우 sparse하고 IFN/MEK inhibitor 처치로도 큰 증가가 관찰되지 않았다는 사례가 대표적입니다 ([Newey 2019](../sources/newey-2019-immunopeptidomics-colorectal-cancer-organoids-reveals.md)). Tretter 2023 32명 pan-tumor 코호트도 MS-validated neoantigen이 환자당 0~수 개 수준으로 prediction pool 대비 극소수임을 보여 일관된 패턴을 나타냅니다 ([Tretter 2023](../sources/tretter-2023-proteogenomic-analysis-reveals-rna-source.md)). Shapiro 2025 NeoDiscMS는 real-time mutanome-guided acquisition으로 low-abundance neoantigen 검출 sensitivity를 끌어올렸지만 여전히 predicted > MS-confirmed라는 구조는 유지되며, mass-spec evidence를 가진 후보를 우선순위 layer로 두는 것이 합리적이라 사료됩니다 ([Shapiro 2025](../sources/shapiro-2025-sensitive-neoantigen-discovery-mutamome-guided-immunopeptidomics.md)).

**Cited**: [Newey 2019](../sources/newey-2019-immunopeptidomics-colorectal-cancer-organoids-reveals.md), [Tretter 2023](../sources/tretter-2023-proteogenomic-analysis-reveals-rna-source.md), [Shapiro 2025](../sources/shapiro-2025-sensitive-neoantigen-discovery-mutamome-guided-immunopeptidomics.md)

**Filed**: existing

### Q6. Proximal variant (한 codon 또는 reading frame 내 multiple variants)이 신항원 예측 정확도에 미치는 영향은?
**A.** Hundal 2019은 430명 종양에서 환자당 평균 241개 missense variant 중 약 5%가 in-phase missense proximal variant를 가짐을 확인했고, proximal variant correction을 생략하면 길이 8~11mer MHC class I neoantigen에서 false discovery rate 약 6.9%, false negative rate 약 2.6%가 발생함을 정량했습니다 ([Hundal 2019](../sources/hundal-2019-accounting-proximal-variants-improves-neoantigen.md)). 즉 proximal somatic·germline variant를 phase 정보와 함께 통합해야 peptide sequence가 정확히 재구성되며, 그렇지 않으면 spurious neoantigen이 생성되거나 진짜 strong-binding 후보를 놓칠 수 있겠습니다. ImmunoNX 같은 최신 personalized vaccine workflow도 phasing-aware variant calling을 표준 단계로 포함시켜 trial-grade 우선순위 설정에 활용한다는 점에서 참고할 만합니다 ([Singhal 2025](../sources/singhal-2025-immunonx-robust-bioinformatics-workflow-support.md)).

**Cited**: [Hundal 2019](../sources/hundal-2019-accounting-proximal-variants-improves-neoantigen.md), [Singhal 2025](../sources/singhal-2025-immunonx-robust-bioinformatics-workflow-support.md)

**Filed**: existing

### Q7. Phosphorylated / glycosylated MHC peptide의 enrichment 방법과 신항원으로서의 가치는?
**A.** Chen 2026 methods chapter는 immunopeptidome에서 PTM peptide를 두 단계 enrichment로 분리하는 표준 workflow를 제시합니다. MHC IP로 immunopeptidome을 회수한 뒤 HILIC SPE로 glycopeptide를, TiO₂ nanoparticle로 phosphopeptide를 sequential하게 enrich하고 LC-MS/MS + database search로 식별합니다 ([Chen 2026](../sources/chen-2026-enrichment-phosphorylated-glycosylated-mhc-peptides.md)). 보고된 패턴으로는 glycopeptide가 MHC class II에, phosphopeptide가 MHC class I 분획에 우세하게 분포합니다. Kacen 2023은 PTM이 tumor immunopeptidome의 antigenic landscape를 광범위하게 reshape함을 보였고, 이들 peptide는 bioinformatic 도구로 예측이 어렵기 때문에 MS-기반 enrichment가 신항원 후보를 발굴하는 거의 유일한 경로로 작용할 수 있겠습니다 ([Kacen 2023](../sources/kacen-2023-post-translational-modifications-reshape-antigenic-landscape.md)).

**Cited**: [Chen 2026](../sources/chen-2026-enrichment-phosphorylated-glycosylated-mhc-peptides.md), [Kacen 2023](../sources/kacen-2023-post-translational-modifications-reshape-antigenic-landscape.md)

**Filed**: existing

### Q8. HLA loss of heterozygosity (HLA-LOH)가 신항원 presentation을 어떻게 narrow시키며, 환자 층화에 어떻게 활용되는가?
**A.** McGranahan 2017은 LOHHLA 알고리즘으로 초기 NSCLC의 약 40%에서 allele-specific HLA loss를 확인했고, HLA-LOH는 subclonal neoantigen burden 증가, APOBEC mutagenesis, cytolytic activity, PD-L1 양성과 함께 enrich되어 면역압력 하의 selective escape 패턴을 시사함을 보였습니다 ([McGranahan 2017](../sources/mcgranahan-2017-allele-specific-hla-loss-lung-cancer.md)). 따라서 LOH된 HLA allele에 의존하는 신항원은 종양 표면에서 사라져 presentation pool이 좁아지며, vaccine·TCR-T 디자인 시 잔존 HLA allele restricted 후보만 우선순위에 두는 stratification이 합리적입니다. Bandlamudi 2026은 54,331 종양에서 HLA-restricted driver neoantigen의 ancestry-specific 차이와 cancer-type-specific somatic HLA loss를 정량하여 TCR therapy 적합성 평가의 axis로 제시합니다 ([Bandlamudi 2026](../sources/bandlamudi-2026-cancer-type-specific-variation-patterns-driver.md)).

**Cited**: [McGranahan 2017](../sources/mcgranahan-2017-allele-specific-hla-loss-lung-cancer.md), [Bandlamudi 2026](../sources/bandlamudi-2026-cancer-type-specific-variation-patterns-driver.md)

**Filed**: existing

### Q9. Neoantigen quality score (예: Łuksza 2022 NetMHC-derived quality)와 단순 neoantigen count의 임상 예측력 차이는?
**A.** Łuksza 2022는 70명 PDAC long-term survivor 코호트에서 "non-selfness"(known antigen 유사도) + "selfness"(WT 대비 binding/T cell 활성화 거리)로 신항원 quality를 정의하고, 강한 T cell pressure가 immunogenic clone을 능동적으로 edit out하여 high-quality neoantigen이 적게 남는 immunoediting의 직접 증거를 제시했습니다 ([Łuksza 2022](../sources/uksza-2022-neoantigen-quality-predicts-immunoediting-survivors.md)). Sholokhova 2026의 CRC branching-process + tumor-immune dynamical system 모델은 "강한 clonal neoantigen 1개"의 존재와 minimal neoantigen quality가 단순 count보다 durable ICI response의 더 강력한 예측인자임을 시사합니다 ([Sholokhova 2026](../sources/sholokhova-2026-neoantigen-evolution-response-checkpoint-inhibitor-immunotherapy.md)). Han 2024 HAPS도 binding affinity·allele divergence를 통합한 quality score가 단순 mutation count보다 pan-cancer ICI survival benefit과 더 잘 연관됨을 보여 quality 기반 정량의 임상 가치를 보강합니다 ([Han 2024](../sources/han-2024-assessment-human-leukocyte-antigen-based-neoantigen.md)).

**Cited**: [Łuksza 2022](../sources/uksza-2022-neoantigen-quality-predicts-immunoediting-survivors.md), [Sholokhova 2026](../sources/sholokhova-2026-neoantigen-evolution-response-checkpoint-inhibitor-immunotherapy.md), [Han 2024](../sources/han-2024-assessment-human-leukocyte-antigen-based-neoantigen.md)

**Filed**: existing

### Q10. Public/shared neoantigen (KRAS G12D/V, PIK3CA hotspot, p53 hotspot) 표적 임상 데이터 진행 상황은?
**A.** KRAS G12V·G12D 표적 TCR-T·peptide vaccine은 colorectal·pancreatic·lung cancer에서 임상 진입 단계로, Tran 2016 HLA-C 기반 KRAS G12D TCR이 PDAC tumor 퇴축을 보였고 ([Tran 2016](../sources/tran-2016-kras-tcell-transfer-hla-loss.md)), 후속 연구는 KRAS G12V TCR(Lu·Shen)와 affinity-enhanced KRAS G12D TCR(Luo·Poole)을 보고하여 solid tumor TCR-T 후보군을 확장하고 있습니다 ([Lu 2023](../sources/lu-2023-kras-g12v-neoantigen-specific-t.md), [Shen 2025](../sources/shen-2025-therapeutic-potential-t-cell-receptor-targeting.md), [Luo 2025](../sources/luo-2025-functional-avidity-enhancement-t-cell-receptor.md), [Poole 2022](../sources/poole-2022-therapeutic-high-affinity-t-cell.md)). PIK3CA hotspot 유래 public neoantigen은 Chandran 2022가 HLA 다양성을 가로질러 다수 환자가 공유함을 보였고 TCR gene therapy로 표적화 가능합니다 ([Chandran 2022](../sources/chandran-2022-immunogenicity-therapeutic-targeting-public-neoantigen.md)). p53 R175H 표적 bispecific antibody/CAR-T는 DiNapoli 2026이 affinity engineering 시 상이한 요구를 보이고 affinity 증가가 BsAb killing은 향상시키나 CAR-T 기능은 감소시킴을 보여 modality-specific 디자인이 필요함을 시사합니다 ([DiNapoli 2026](../sources/dinapoli-2026-bispecific-antibodies-car-t-cells.md), [Shen 2026](../sources/shen-2026-t-cell-receptor-engineered-t-cells.md)).

**Cited**: [Tran 2016](../sources/tran-2016-kras-tcell-transfer-hla-loss.md), [Lu 2023](../sources/lu-2023-kras-g12v-neoantigen-specific-t.md), [Chandran 2022](../sources/chandran-2022-immunogenicity-therapeutic-targeting-public-neoantigen.md), [DiNapoli 2026](../sources/dinapoli-2026-bispecific-antibodies-car-t-cells.md), [Shen 2026](../sources/shen-2026-t-cell-receptor-engineered-t-cells.md)

**Filed**: existing

### Q11. Pan-cancer 50,000+ 환자 scale에서 driver alteration 패턴의 cancer type-specific variation이 신항원 prioritization에 주는 시사점은?
**A.** Bandlamudi 2026은 MSKCC 주도의 54,331 종양·48,179명 환자·448 histological subtype 코호트에서 164개 novel hotspot을 식별하고 driver의 약 33%가 non-canonical context에서 발생하며 subclonality 증가·후기 등장·divergent biological property를 보임을 정량했습니다 ([Bandlamudi 2026](../sources/bandlamudi-2026-cancer-type-specific-variation-patterns-driver.md)). 또한 HLA-restricted driver neoantigen의 ancestry-specific 차이와 cancer-type-specific somatic HLA loss 패턴을 보고하여 TCR therapy 적합성·intrinsic resistance가 환자 ancestry와 cancer type에 따라 달라짐을 시사합니다. Kalyva 2026 preview는 driver의 효과와 timing이 tissue context에 따라 달라지므로 vaccine·TCR-T target 우선순위 설정 시 cancer-type-conditioned driver clonality와 ancestry-matched HLA presentation을 함께 고려해야 함을 강조합니다 ([Kalyva 2026](../sources/kalyva-2026-redefining-cancer-drivers-tissue-specific-context.md)).

**Cited**: [Bandlamudi 2026](../sources/bandlamudi-2026-cancer-type-specific-variation-patterns-driver.md), [Kalyva 2026](../sources/kalyva-2026-redefining-cancer-drivers-tissue-specific-context.md)

**Filed**: existing

### Q12. Healthy donor T cell receptor가 cancer neoantigen을 인식하는 frequency와 임상 활용 가능성은?
**A.** Teo 2026은 personalized neoantigen vaccine을 접종받은 cancer 환자 PBMC와 HLA-matched healthy donor의 naïve CD8+ T cell을 동일 neoepitope panel에 대해 head-to-head로 비교했고, vaccination에도 patient T cell은 predicted neoantigen 중 극소수만 인식한 반면 donor T cell은 더 broad·robust한 IFN-γ·expansion 반응을 보였습니다 ([Teo 2026](../sources/teo-2026-healthy-donor-cell-receptors-expand-functional.md)). 또 allogeneic donor naïve CD8 pool에서 expand한 TCR이 환자 TIL이 engage하지 못한 target까지 인식했으며, 환자 측 한계 요인으로 chemotherapy-induced T cell depletion, immunoediting, dysfunctional TIL이 지목됩니다. 임상적으로는 chemotherapy 후 환자 T cell fitness가 약화된 경우 HLA-matched donor pool에서 neoantigen-reactive TCR을 isolation·engineering해 vaccine을 보완하는 hybrid 전략의 근거가 마련된다고 사료됩니다.

**Cited**: [Teo 2026](../sources/teo-2026-healthy-donor-cell-receptors-expand-functional.md)

**Filed**: existing

## Section B — B-cell / TLS biology (Q13-22)

### Q13. TLS maturation stage (early aggregate → primary follicle → secondary follicle with GC)는 어떻게 평가되며 cancer prognosis와의 상관은?
**A.** 통상 H&E + multiplex IF에서 CD20+ B cell aggregate, CD21+ FDC network, Ki-67+ GC, 그리고 CXCL13/CD23 marker를 함께 stain해 early aggregate → primary follicle → secondary follicle with GC로 단계화하며, 최근에는 deep-learning WSI classifier로 정량 가능합니다 ([Wu 2025](../sources/wu-2025-artificial-intelligence-multimodality-data-integration.md)). Vanhersecke 2021은 3개 cohort retrospective 분석에서 mature TLS의 존재 자체가 PD-L1과 CD8 density와 독립적으로 ORR·PFS·OS와 연관됨을 보였고 ([Vanhersecke 2021](../sources/vanhersecke-2021-mature-tertiary-lymphoid-structures-predict.md)), Cabrita 2020 melanoma는 CD8+CD20+ co-occurrence가 우월한 생존과 ICI 반응에 연관됨을 입증했습니다 ([Cabrita 2020](../sources/cabrita-2020-tertiary-lymphoid-structures-improve-immunotherapy.md)). 위암 253명 코호트에서는 transformer 기반 maturity score가 높을수록 생존이 개선되는 일관된 패턴이 확인되어 mature TLS가 prognostic biomarker임을 시사합니다 ([Wu 2025](../sources/wu-2025-artificial-intelligence-multimodality-data-integration.md)).

**Cited**: [Vanhersecke 2021](../sources/vanhersecke-2021-mature-tertiary-lymphoid-structures-predict.md), [Cabrita 2020](../sources/cabrita-2020-tertiary-lymphoid-structures-improve-immunotherapy.md), [Wu 2025](../sources/wu-2025-artificial-intelligence-multimodality-data-integration.md)

**Filed**: existing

### Q14. TLS의 maturity와 abundance가 항암제 (anti-PD-1, neoadjuvant chemoimmunotherapy)에 대한 반응을 얼마나 예측하는가?
**A.** Vanhersecke 2021의 pan-cancer ICI 코호트에서 mature TLS의 유무가 PD-L1 status와 무관하게 ORR·PFS·OS 개선과 연관되어 TLS-based stratification의 임상 효용을 시사했습니다 ([Vanhersecke 2021](../sources/vanhersecke-2021-mature-tertiary-lymphoid-structures-predict.md)). resectable NSCLC neoadjuvant chemo + anti-PD-1 코호트에서는 TLS abundance와 maturity가 major pathologic response와 양의 상관을 보였고 ([Sun 2022](../sources/sun-2022-tls-neoadjuvant-chemoimmunotherapy-resectable-nsclc.md)), du 2025 TLS gene signature는 advanced NSCLC ICI + chemo 반응 예측에 기여합니다 ([du 2025](../sources/du-2025-tls-gene-signature-advanced-nsclc.md)). NADIM/NADIM II 123명 분석에서는 TLS density 단독은 CPR과 유의하지 않았지만 mature TLS의 plasmacytoid DC·Tfh·plasma cell 풍부도가 CPR과 연관되어 maturity가 단순 density보다 더 informative한 metric임을 보여줍니다 ([Sierra-Rodero 2026](../sources/sierrarodero-2026-decoding-cell-signatures-complete-pathologic-response.md)).

**Cited**: [Vanhersecke 2021](../sources/vanhersecke-2021-mature-tertiary-lymphoid-structures-predict.md), [Sun 2022](../sources/sun-2022-tls-neoadjuvant-chemoimmunotherapy-resectable-nsclc.md), [Sierra-Rodero 2026](../sources/sierrarodero-2026-decoding-cell-signatures-complete-pathologic-response.md), [du 2025](../sources/du-2025-tls-gene-signature-advanced-nsclc.md)

**Filed**: existing

### Q15. Myofibroblast가 TLS 형성을 차단하는 mechanism은?
**A.** Kirschstein 2026은 LTBR agonist에 반응해 일부 PDAC 모델만 TLS-like aggregate가 형성되는 이유를 cancer-associated fibroblast(CAF) 분획 차이로 설명합니다. TLS-resistant 모델은 myofibroblastic CAF(myCAF)가 우세하고 TLS-permissive 모델은 reticular CAF(rCAF)가 풍부했으며, TGFβ-driven myCAF 분화가 LTBR/TNFα-매개 chemokine 상향과 reticular fibroblast 프로그래밍을 차단해 림프구 이주와 TLS organizing FRC 분화를 막았습니다 ([Kirschstein 2026](../sources/kirschstein-2026-myofibroblast-programming-blocks-differentiation-tls-organizing.md)). TGFβR1 antagonist + αLTBR 병용이 rCAF 회복·T·B cell recruitment·tumor 제어를 유도했고 인간 PDAC에서도 rCAF가 TLS 근접, myCAF가 distal에 분포해 translational relevance가 확인되었습니다. 따라서 stromal TGFβ axis가 TLS 형성의 핵심 gatekeeper로 작용한다고 사료됩니다.

**Cited**: [Kirschstein 2026](../sources/kirschstein-2026-myofibroblast-programming-blocks-differentiation-tls-organizing.md)

**Filed**: existing

### Q16. Tumor-infiltrating B cell의 plasmablast / memory B / regulatory B 분획 비율과 임상 outcome의 관계는?
**A.** Yang 2024 pan-cancer 649명·19 cancer type scRNA-seq atlas는 TIB가 cancer 간 매우 heterogeneous하지만 stress-response memory B cell과 tumor-associated atypical B cell(TAAB)이 pan-cancer 공통 enriched subset이며 TAAB가 clonal expansion·CD4 T 상호작용을 통해 ICI 반응 예측력을 가짐을 보고합니다 ([Yang 2024](../sources/yang-2024-pan-cancer-single-cell-dissection-reveals-phenotypically.md)). TNBC에서는 class-switched IgG-biased clonally expanded TIB가 생존 향상과 연관되었고, IgG isotype switching이 우호적 outcome marker로 보고됩니다 ([Harris 2021](../sources/harris-2021-tumor-infiltrating-b-lymphocyte-profiling-identifies.md)). 반면 IGLL5+ B cell처럼 LTβR signaling을 차단해 TLS를 disassemble시키는 regulatory-유사 B cell subset은 면역치료 효능을 저해할 수 있어 plasmablast/IgG class-switched 분획 vs regulatory subset의 비율이 outcome과 양·음 양쪽으로 작용함을 시사합니다 ([Chen 2026](../sources/chen-2026-b-cells-disrupt-tertiary-lymphoid.md)). Melcher 2022는 B cell-mediated regulatory mechanism이 종양-촉진 intestinal inflammation을 제어하는 또 다른 사례를 제시합니다 ([Melcher 2022](../sources/melcher-2022-b-cell-mediated-regulatory-mechanisms-control.md)).

**Cited**: [Yang 2024](../sources/yang-2024-pan-cancer-single-cell-dissection-reveals-phenotypically.md), [Harris 2021](../sources/harris-2021-tumor-infiltrating-b-lymphocyte-profiling-identifies.md), [Chen 2026](../sources/chen-2026-b-cells-disrupt-tertiary-lymphoid.md), [Melcher 2022](../sources/melcher-2022-b-cell-mediated-regulatory-mechanisms-control.md)

**Filed**: existing

### Q17. CCL19/CCL21/CXCL13 producing stromal/fibroblast cell이 TLS 형성에 미치는 영향은?
**A.** Zhang 2024는 colorectal cancer liver metastasis(CRLM)에서 scRNA + Stereo-seq로 CCL19-producing fibroblast lineage가 림프구 trafficking을 TLS로 유도하고, CCL19 처치가 mouse model에서 TLS neogenesis를 촉진해 IgG+ PC-기반 tumor 제어를 가능하게 함을 보였습니다 ([Zhang 2024](../sources/zhang-2024-ccl19-producing-fibroblasts-promote-tertiary-lymphoid.md)). Rodriguez 2021은 다양한 cancer에서 CAF가 림프구 동원 chemokine 분비로 TLS orchestration에 핵심 역할을 함을 보고하고 ([Rodriguez 2021](../sources/rodriguez-2021-immune-mechanisms-orchestrate-tertiary-lymphoid.md)), Ghosh 2026은 Cxcl13+/Cxcl9+/Cxcl10+ CD206hi interstitial macrophage가 bronchovascular niche에서 TLS 형성·림프구 동원·tumor 제어를 추진하는 반면 Ccl2+ IM은 pro-tumor recMac을 유도해 상반된 niche를 만든다는 chemokine 정의 macrophage 축을 제시합니다 ([Ghosh 2026](../sources/ghosh-2026-chemokine-defined-macrophage-niches-establish-spatial.md)). 즉 CXCL13/CCL19 production이 stromal CAF뿐 아니라 IM에서도 일어나며 cell type-specific niche가 함께 TLS organizing 환경을 결정한다고 사료됩니다.

**Cited**: [Zhang 2024](../sources/zhang-2024-ccl19-producing-fibroblasts-promote-tertiary-lymphoid.md), [Rodriguez 2021](../sources/rodriguez-2021-immune-mechanisms-orchestrate-tertiary-lymphoid.md), [Ghosh 2026](../sources/ghosh-2026-chemokine-defined-macrophage-niches-establish-spatial.md)

**Filed**: existing

### Q18. Endogenous neoantigen-specific antibody (tumor-reactive B cell이 생산)가 antitumor immunity에 기여하는 mechanism은?
**A.** Sodhi 2026 syngeneic 마우스 모델 + TCGA pan-cancer 분석은 membrane-localized neoantigen이 class-switched IgG 반응, myeloid activation, CD8 T 비의존적 tumor 제어를 유도한 반면 cytoplasmic neoantigen은 그렇지 못함을 보였습니다 ([Sodhi 2026](../sources/sodhi-2026-endogenous-neoantigen-specific-antibodies-mediate-antitumor.md)). 효과 메커니즘은 CD4 T cell help, antigen-specific IgG의 직접 결합, Fc receptor engagement에 의존하며 CXCL13(B cell recruitment)·IL-21(B cell help) 공동 발현 시 최대화되었습니다. Trop2 T256R 점돌연변이는 막 국재화를 손상시켜 vaccine 효능을 떨어뜨려 antigen subcellular localization이 humoral 반응 효능의 결정인자임을 입증합니다. 임상적으로 Meylan 2022는 RCC TLS+ tumor에서 IgG-producing PC가 IgG-stained·apoptotic cancer cell과 동반되어 ICI PFS와 연관됨을 보여 endogenous antibody arm의 직접적 antitumor 기여를 시사합니다 ([Meylan 2022](../sources/meylan-2022-tertiary-lymphoid-structures-generate-propagate.md)).

**Cited**: [Sodhi 2026](../sources/sodhi-2026-endogenous-neoantigen-specific-antibodies-mediate-antitumor.md), [Meylan 2022](../sources/meylan-2022-tertiary-lymphoid-structures-generate-propagate.md)

**Filed**: existing

### Q19. Th-CXCL13 / Tfh cell이 TLS에 B cell을 recruit하는 기전과 GC 형성과의 관계는?
**A.** Li 2021 nasopharyngeal carcinoma 연구는 PD-1+CXCR5−CD4+ Th-CXCL13 subset이 CXCL13의 주요 source임을 식별하고, TLR4-activated monocyte가 가장 효율적으로 이들을 expansion시키며 TGF-β1·Sox4 활성이 induction의 핵심 단계임을 보였습니다 ([Li 2021](../sources/li-2021-pd-1cxcr5-cd4-th-cxcl13-cell-subset-drives.md)). Th-CXCL13가 recruit한 tumor-associated B cell은 IL-21·CD84 상호작용을 통해 plasma cell 분화·Ig 생산으로 이어져 TLS 내 GC-like 기능을 지원하며, 이는 환자 생존 개선과 연관됩니다. Li 2025 HNSCC 연구는 mature TLS가 progenitor exhausted CD4+ T cell을 통해 intra-tumoral T·B cell 반응을 유발함을 추가로 시사합니다 ([Li 2025](../sources/li-2025-mature-tertiary-lymphoid-structures-evoke.md)). 따라서 Th-CXCL13–B cell 회로는 GC formation과 antibody class switching의 in situ 출발점으로 작동한다고 사료됩니다.

**Cited**: [Li 2021](../sources/li-2021-pd-1cxcr5-cd4-th-cxcl13-cell-subset-drives.md), [Li 2025](../sources/li-2025-mature-tertiary-lymphoid-structures-evoke.md)

**Filed**: existing

### Q20. Spatial transcriptomics가 TLS 구조와 functional state를 in situ로 어떻게 dissect하는가?
**A.** Spatial transcriptomics는 TLS aggregate를 in situ에서 cell-type composition·maturity·주변 niche와 함께 dissect할 수 있게 합니다. Meylan 2022는 RCC spatial transcriptomics로 TLS 내 B cell이 모든 maturation stage를 거쳐 plasma cell로 분화하고 IgG·IgA PC가 fibroblastic track을 따라 tumor bed로 분포해 IgG-stained tumor cell과 PFS가 연관됨을 보였고 ([Meylan 2022](../sources/meylan-2022-tertiary-lymphoid-structures-generate-propagate.md)), Wang 2025 gastric cancer 연구는 single-cell + spatial로 TLS density와 spatial distribution이 단순 존재 여부보다 prognosis와 더 강하게 연관됨을 보고합니다 ([Wang 2025](../sources/wang-2025-single-cell-spatial-transcriptomics-gastric-tls.md)). Tang 2025 HCC 연구는 near single-cell spatial mapping으로 TLS를 conforming vs deviating immature subtype으로 분류하고 tryptophan-rich metabolic microenvironment가 TLS maturation을 deviation시키는 factor임을 확인했고 ([Tang 2025](../sources/tang-2025-spatial-transcriptomics-reveals-tryptophan-metabolism.md)), Liu 2024 NPC 연구는 spatial transcriptome으로 TLS가 progression·immunotherapy 반응과 연결됨을 보였습니다 ([Liu 2024](../sources/liu-2024-single-cell-and-spatial-transcriptome.md)).

**Cited**: [Meylan 2022](../sources/meylan-2022-tertiary-lymphoid-structures-generate-propagate.md), [Wang 2025](../sources/wang-2025-single-cell-spatial-transcriptomics-gastric-tls.md), [Tang 2025](../sources/tang-2025-spatial-transcriptomics-reveals-tryptophan-metabolism.md), [Liu 2024](../sources/liu-2024-single-cell-and-spatial-transcriptome.md)

**Filed**: existing

### Q21. Cholangiocarcinoma, HCC, pancreatic, gastric cancer 등 GI cancers에서 TLS 빈도와 prognosis의 차이는?
**A.** Cholangiocarcinoma에서는 TLS와 TIL의 비교적 영향이 다르지만 mature TLS 존재가 우월한 outcome과 연관됨이 보고되었고 ([Chung 2025](../sources/chung-2025-comparative-impact-tertiary-lymphoid-structures.md)), HCC에서는 TLS maturity가 tryptophan metabolism에 의해 부분적으로 차단됨에도 conforming/mature TLS가 ICI 반응·생존과 연관됩니다 ([Tang 2025](../sources/tang-2025-spatial-transcriptomics-reveals-tryptophan-metabolism.md)). PDAC는 historically immunologically cold이며 intratumoral TLS 빈도가 낮지만 mature TLS가 tumor-specific 면역 반응의 핵심 niche로 작동해 long survival과 연관되고 ([Kinker 2023](../sources/kinker-2023-mature-tertiary-lymphoid-structures-key.md), [Zou 2023](../sources/zou-2023-characterization-intratumoral-tertiary-lymphoid-structures.md)), IL-33-activated ILC2가 PDAC TLS neogenesis를 유도해 prognosis 개선 가능성을 시사합니다 ([Amisaki 2025](../sources/amisaki-2025-il33-ilc2-tertiary-lymphoid-structures-pancreatic-cancer.md)). Gastric cancer에서는 spatial TLS density·spatial distribution이 prognostic이며 mature TLS가 CD8 TRM·activated B cell circuit을 통해 cytotoxicity를 증가시킵니다 ([Wang 2025](../sources/wang-2025-single-cell-spatial-transcriptomics-gastric-tls.md), [Wu 2025](../sources/wu-2025-artificial-intelligence-multimodality-data-integration.md)).

**Cited**: [Chung 2025](../sources/chung-2025-comparative-impact-tertiary-lymphoid-structures.md), [Tang 2025](../sources/tang-2025-spatial-transcriptomics-reveals-tryptophan-metabolism.md), [Kinker 2023](../sources/kinker-2023-mature-tertiary-lymphoid-structures-key.md), [Amisaki 2025](../sources/amisaki-2025-il33-ilc2-tertiary-lymphoid-structures-pancreatic-cancer.md), [Wang 2025](../sources/wang-2025-single-cell-spatial-transcriptomics-gastric-tls.md)

**Filed**: existing

### Q22. Pediatric cancer / 저TMB cancer (예: low TMB ccRCC, GBM)에서도 TLS-mediated B cell response가 임상 의미를 갖는가?
**A.** 저TMB ccRCC에서 mature TLS 존재가 ICI 반응 개선과 연관됨이 multiple cohort에서 보고되어 mutation count가 적어도 organized B cell response가 outcome을 좌우할 수 있음을 시사합니다 ([Wang 2024](../sources/wang-2024-integrated-analysis-tertiary-lymphoid-structures.md), [Meylan 2022](../sources/meylan-2022-tertiary-lymphoid-structures-generate-propagate.md)). RCC adjuvant 백신·HIF-hERV neoantigen 연구는 RCC가 TMB는 낮아도 TLS·B cell biology를 통해 면역치료에 반응할 수 있는 대표 cancer type임을 보여줍니다 ([Braun 2025](../sources/braun-2025-neoantigen-vaccine-generates-antitumour-immunity.md), [Salgia 2025](../sources/salgia-2025-hifs-hervs-neoantigen-generation-kidney.md)). pediatric cancer 데이터는 본 corpus에 thin하지만 brain tumor proteogenomic 신항원 연구가 발견 단계에서 진행 중입니다 ([Rivero-Hinojosa 2021](../sources/riverohinojosa-2021-proteogenomic-discovery-neoantigens-facilitates-personalized.md)). GBM에서 personalized vaccine은 intratumoral T cell 반응을 유도했으나 환자 수·TLS 정량은 제한적이라 pediatric/GBM B-cell 반응 평가는 향후 corpus 보강이 필요할 만한 evidence gap이 있습니다.

**Cited**: [Wang 2024](../sources/wang-2024-integrated-analysis-tertiary-lymphoid-structures.md), [Meylan 2022](../sources/meylan-2022-tertiary-lymphoid-structures-generate-propagate.md), [Braun 2025](../sources/braun-2025-neoantigen-vaccine-generates-antitumour-immunity.md), [Rivero-Hinojosa 2021](../sources/riverohinojosa-2021-proteogenomic-discovery-neoantigens-facilitates-personalized.md)

**Filed**: evidence-gap (pediatric cancer 관련 source 부족, 후속 corpus 보강 후보)

## Section C — Clinical translation / Vaccine & TCR-T (Q23-32)

### Q23. mRNA neoantigen 백신 (V940/mRNA-4157 KEYNOTE-942/603, NEO-PV-01, EVX-01 등) 1상-2상 readout 비교: 면역원성, 임상 efficacy, 안전성?
**A.** 본 corpus는 mRNA-4157 KEYNOTE-942의 1차 결과를 직접 다룬 deep-dive 페이지는 없으나, NEO-PV-01의 NSCLC phase Ib는 chemo + pembrolizumab과 병용 시 grade ≥3 TRAE 없이 de novo neoantigen-specific CD4+/CD8+ 반응과 KRAS G12C/G12V epitope spread를 유도했고 ([Awad 2022](../sources/awad-2022-personalized-neoantigen-vaccine-neo-pv-01-chemotherapy.md)), EVX-01 dose escalation은 metastatic melanoma에서 peptide-based 디자인의 안전성과 면역원성을 검증했습니다 ([EVX-01](../sources/mrk-2024-dose-escalation-study-personalized-peptide-based.md)). HCC GT-30(GNOS-PV02 DNA + pIL-12 + pembrolizumab) 1/2상에서는 ORR 30.6%(3 CR), 86.4%에서 vaccine-specific T cell 반응이 검출되어 효능·면역원성·안전성을 한꺼번에 보여주는 deep-dive 사례입니다 ([Yarchoan 2024](../sources/yarchoan-2024-personalized-neoantigen-vaccine-pembrolizumab-advanced.md)). May 2024 리뷰는 mRNA platform의 personalized vaccine revolution을 정리하며 mRNA-4157 phase 2 melanoma adjuvant 데이터를 맥락화합니다 ([May 2024](../sources/may-2024-how-mrna-powering-personalized-vaccine.md)).

**Cited**: [Awad 2022](../sources/awad-2022-personalized-neoantigen-vaccine-neo-pv-01-chemotherapy.md), [Yarchoan 2024](../sources/yarchoan-2024-personalized-neoantigen-vaccine-pembrolizumab-advanced.md), [EVX-01](../sources/mrk-2024-dose-escalation-study-personalized-peptide-based.md), [May 2024](../sources/may-2024-how-mrna-powering-personalized-vaccine.md)

**Filed**: existing

### Q24. Peptide-based personalized neoantigen vaccine (PGV001, Severance, Ott 2017 등)의 임상 efficacy와 면역원성?
**A.** Ott 2017 melanoma 1상은 환자별 long peptide pool + poly-ICLC가 안전·면역원성을 입증하고 일부 환자에서 epitope spread·tumor 통제가 관찰된 첫 deep-dive 사례로, peptide-based PCV의 conceptual 출발점입니다 ([Ott 2017](../sources/ott-2017-immunogenic-personal-neoantigen-vaccine-patients.md)). PGV001 phase I(13명 adjuvant·다양한 solid·hematologic)에서는 OpenVax 예측 기반 peptide pool이 광범위한 TMB에서 면역원성을 보였고 GBM·urothelial·prostate 후속 trial을 촉발했습니다 ([Saxena 2025](../sources/saxena-2025-pgv001-multi-peptide-personalized-neoantigen-vaccine.md)). Atezolizumab + PGV001 urothelial 1상은 12명 중 10명이 vaccine 제조 완료, on-treatment에서 모든 환자가 neoantigen-specific T cell 반응을 보였고 adjuvant cohort 3/4에서 ~39.5개월 median follow-up까지 recurrence-free였습니다 ([Saxena 2025 atezolizumab](../sources/atezolizumab-2025-personalized-neoantigen-vaccination-urothelial-cancer.md)). RCC adjuvant peptide vaccine(Braun 2025)는 9/9 환자에서 vaccine-specific T cell 반응과 median follow-up 40.2개월까지 재발 없는 신호를 보였습니다 ([Braun 2025](../sources/braun-2025-neoantigen-vaccine-generates-antitumour-immunity.md)).

**Cited**: [Ott 2017](../sources/ott-2017-immunogenic-personal-neoantigen-vaccine-patients.md), [Saxena 2025](../sources/saxena-2025-pgv001-multi-peptide-personalized-neoantigen-vaccine.md), [Saxena 2025 atezolizumab](../sources/atezolizumab-2025-personalized-neoantigen-vaccination-urothelial-cancer.md), [Braun 2025](../sources/braun-2025-neoantigen-vaccine-generates-antitumour-immunity.md)

**Filed**: existing

### Q25. Adjuvant setting (RCC, melanoma, urothelial) vs metastatic setting의 신항원 백신 efficacy 차이는?
**A.** Adjuvant setting은 tumor burden이 minimal하고 immune system이 비교적 intact해 vaccine-driven T cell expansion이 oncologic benefit으로 더 잘 translate되는 경향이 보고됩니다. RCC adjuvant phase I에서 ipilimumab 병용 peptide PCV가 9/9 환자에서 vaccine-specific T cell 반응을 유도하고 median 40.2개월까지 재발 없음(소규모·대조군 없음)을 보였고 ([Braun 2025](../sources/braun-2025-neoantigen-vaccine-generates-antitumour-immunity.md)), urothelial atezolizumab + PGV001 adjuvant cohort 3/4가 ~39.5개월 recurrence-free였습니다 ([Saxena 2025 atezolizumab](../sources/atezolizumab-2025-personalized-neoantigen-vaccination-urothelial-cancer.md)). melanoma adjuvant PCV(Ott·EVX-01·Ninmer 6MHP+mBRAF)도 면역원성과 안전성 신호가 일관됩니다 ([Ott 2017](../sources/ott-2017-immunogenic-personal-neoantigen-vaccine-patients.md), [Ninmer 2026](../sources/ninmer-2026-phase-clinical-trial-melanoma-vaccine-targeting.md)). 반면 metastatic HCC GT-30(2L)에서 ORR 30.6%로 historical pembrolizumab 단독 12–18%의 약 2배 신호가 관찰되었고 ([Yarchoan 2024](../sources/yarchoan-2024-personalized-neoantigen-vaccine-pembrolizumab-advanced.md)), Khaddour 2026 review는 PCV가 metastatic ICI-refractory 종양보다 adjuvant/MRD setting에서 가장 큰 benefit을 줄 가능성을 시사한다고 정리합니다 ([Khaddour 2026](../sources/khaddour-2026-bridging-clinical-gaps-personalized-cancer-neoantigen.md)).

**Cited**: [Braun 2025](../sources/braun-2025-neoantigen-vaccine-generates-antitumour-immunity.md), [Saxena 2025 atezolizumab](../sources/atezolizumab-2025-personalized-neoantigen-vaccination-urothelial-cancer.md), [Yarchoan 2024](../sources/yarchoan-2024-personalized-neoantigen-vaccine-pembrolizumab-advanced.md), [Khaddour 2026](../sources/khaddour-2026-bridging-clinical-gaps-personalized-cancer-neoantigen.md), [Ninmer 2026](../sources/ninmer-2026-phase-clinical-trial-melanoma-vaccine-targeting.md)

**Filed**: existing

### Q26. Combinatorial 백신 + ICI (anti-PD-1, anti-CTLA-4)의 synergy mechanism과 임상 readout?
**A.** Liu 2022는 vaccine과 ICB의 concurrent delivery가 T cell dynamics를 변화시켜 antitumor immunity를 강화하는 메커니즘적 근거를 제시하며 ([Liu 2022](../sources/liu-2022-concurrent-delivery-immune-checkpoint-blockade.md)), Chen 2022 preclinical HCC 모델에서는 vaccine + PD-1 차단이 CD8+ tissue-resident memory T cell infiltration을 증가시킴을 보였습니다 ([Chen 2022](../sources/chen-2022-personalized-neoantigen-vaccine-combined-pd-1.md)). 임상 readout으로는 HCC GT-30(GNOS-PV02 DNA + pIL-12 + pembrolizumab)에서 ORR 30.6%(2L에서 historical 약 2배)와 86.4% immunogenicity ([Yarchoan 2024](../sources/yarchoan-2024-personalized-neoantigen-vaccine-pembrolizumab-advanced.md)), NEO-PV-01 + chemo + pembrolizumab NSCLC 1상에서 grade ≥3 TRAE 없이 epitope spreading + 안정적 신호 ([Awad 2022](../sources/awad-2022-personalized-neoantigen-vaccine-neo-pv-01-chemotherapy.md)), atezolizumab + PGV001 urothelial 1상에서 모든 환자 immunogenicity ([Saxena 2025 atezolizumab](../sources/atezolizumab-2025-personalized-neoantigen-vaccination-urothelial-cancer.md)), RCC adjuvant peptide + ipilimumab cohort에서 vaccine-specific T cell + 재발 없음 ([Braun 2025](../sources/braun-2025-neoantigen-vaccine-generates-antitumour-immunity.md))이 보고됩니다. Rappaport 2024 shared neoantigen + ICB phase 1 interim에서도 신항원 백신 + 면역치료 병용의 임상 feasibility를 보여줍니다 ([Rappaport 2024](../sources/rappaport-2024-shared-neoantigen-vaccine-checkpoint-blockade.md)).

**Cited**: [Liu 2022](../sources/liu-2022-concurrent-delivery-immune-checkpoint-blockade.md), [Yarchoan 2024](../sources/yarchoan-2024-personalized-neoantigen-vaccine-pembrolizumab-advanced.md), [Awad 2022](../sources/awad-2022-personalized-neoantigen-vaccine-neo-pv-01-chemotherapy.md), [Braun 2025](../sources/braun-2025-neoantigen-vaccine-generates-antitumour-immunity.md), [Saxena 2025 atezolizumab](../sources/atezolizumab-2025-personalized-neoantigen-vaccination-urothelial-cancer.md)

**Filed**: existing

### Q27. Adoptive TCR-T cell therapy: KRAS G12V, PIK3CA, TP53 mutation 표적의 임상 진행 상황?
**A.** KRAS G12V 표적 TCR은 colorectal·lung·pancreatic cancer 모델에서 효능을 보이는 multiple lead candidate가 보고되었고 ([Lu 2023](../sources/lu-2023-kras-g12v-neoantigen-specific-t.md), [Shen 2025](../sources/shen-2025-therapeutic-potential-t-cell-receptor-targeting.md)), Parkhurst 2024는 metastatic CRC에서 personalized neoantigen-reactive TCR-transduced T cell의 phase 2 interim을 보고했습니다 ([Parkhurst 2024](../sources/parkhurst-2024-adoptive-transfer-personalized-neoantigen-reactive-tcr-transduced.md)). PIK3CA hotspot 유래 public neoantigen은 Chandran 2022가 HLA 다양성을 가로지르는 TCR gene therapy 타당성을 보였고 ([Chandran 2022](../sources/chandran-2022-immunogenicity-therapeutic-targeting-public-neoantigen.md)), TP53 R248Q·R175H TCR-engineered T cell이 인간 cancer 모델에서 antitumor effect를 보였습니다 ([Shen 2026](../sources/shen-2026-t-cell-receptor-engineered-t-cells.md)). DiNapoli 2026은 TP53 R175H를 표적으로 하는 BsAb와 CAR-T가 affinity 요구치에서 discordant함을 보여 modality-specific 디자인 고려가 필요함을 시사하고 ([DiNapoli 2026](../sources/dinapoli-2026-bispecific-antibodies-car-t-cells.md)), Lenkala 2026 NEO-STIM은 personalized neoantigen-specific adoptive T cell therapy를 advance하는 platform 진전을 정리합니다 ([Lenkala 2026](../sources/lenkala-2026-neo-stim-advances-personalized-neoantigen-specific-adoptive.md)).

**Cited**: [Lu 2023](../sources/lu-2023-kras-g12v-neoantigen-specific-t.md), [Parkhurst 2024](../sources/parkhurst-2024-adoptive-transfer-personalized-neoantigen-reactive-tcr-transduced.md), [Chandran 2022](../sources/chandran-2022-immunogenicity-therapeutic-targeting-public-neoantigen.md), [Shen 2026](../sources/shen-2026-t-cell-receptor-engineered-t-cells.md), [DiNapoli 2026](../sources/dinapoli-2026-bispecific-antibodies-car-t-cells.md)

**Filed**: existing

### Q28. Bispecific antibody와 TCR-T cell의 affinity 요구치 차이가 neoantigen targeting 전략에 미치는 영향?
**A.** DiNapoli 2026은 동일한 TP53 R175H/HLA-A*02:01 MANA를 표적으로 한 H2 scFv 변이체를 BsAb와 CD28z CAR(또는 CD3γ/TCR) 두 modality에 그대로 부착해 비교했고, BsAb는 affinity를 low-nanomolar 범위까지 올렸을 때 cancer cell killing과 마우스 종양 통제가 향상되고 specificity가 보존된 반면 CAR-T는 affinity 증가가 모든 CAR format에서 기능 저하(T cell 활성화 감소)로 이어짐을 보여 modality-specific discordance를 입증했습니다 ([DiNapoli 2026](../sources/dinapoli-2026-bispecific-antibodies-car-t-cells.md)). Chen 2026 catch-bond engineering은 affinity 자체가 아니라 bond lifetime이 핵심임을 mechanism 차원에서 보강하며, TCR-T 디자인에서는 affinity tuning보다 force-aware engineering이 효과적일 수 있음을 시사합니다 ([Chen 2026](../sources/chen-2026-overcoming-cell-tolerance-tumor-self-antigens.md)). 따라서 low-density MANA를 표적할 때 BsAb는 affinity 강화, TCR-T는 affinity-신중·specificity-보존이 권장되는 분기점이 사료됩니다.

**Cited**: [DiNapoli 2026](../sources/dinapoli-2026-bispecific-antibodies-car-t-cells.md), [Chen 2026](../sources/chen-2026-overcoming-cell-tolerance-tumor-self-antigens.md)

**Filed**: existing

### Q29. Vaccine + Regorafenib / lymphodepleting chemo 같은 microenvironment 조정 병용의 mechanism rationale?
**A.** Sagie 2025는 lymphodepleting chemotherapy가 immunoproteasome 활성과 HLA-I 표면 발현을 상향시키고 antigenic landscape를 reshape(peptide abundance·hydrophobicity 증가, cleavage preference 변화)함으로써 KRAS G12V TCR-T, TIL, T-cell engager의 종양 통제를 강화함을 보여 "antigen presentation 정상화 + 림프구 공간 확보" 이중 기전을 제시합니다 ([Sagie 2025](../sources/sagie-2025-lymphodepleting-chemotherapy-potentiates-neoantigen-directed-t.md)). MSS-CRC liver metastasis에서 personalized neoantigen vaccine + regorafenib(RegoNeo) 조합은 Rgs2+CD8+ T cell population을 확장하고 immunosuppressive TME를 reprogramming해 종양 통제와 durable immune memory를 달성했습니다 ([Chen 2025](../sources/chen-2025-personalized-neoantigen-vaccine-plus-regorafenib.md)). Treg depletion도 약한 면역원성 vaccine의 T cell 반응을 증강함이 보고되어, microenvironment 조정 병용은 antigen presentation 회복, 면역억제 셀 제거, T cell niche 확장이라는 3축으로 정리할 수 있겠습니다 ([Huang 2025](../sources/huang-2025-depletion-regulatory-t-cells-enhances.md)).

**Cited**: [Sagie 2025](../sources/sagie-2025-lymphodepleting-chemotherapy-potentiates-neoantigen-directed-t.md), [Chen 2025](../sources/chen-2025-personalized-neoantigen-vaccine-plus-regorafenib.md), [Huang 2025](../sources/huang-2025-depletion-regulatory-t-cells-enhances.md)

**Filed**: existing

### Q30. Manufacturing TAT, cost, scalability — personalized vs shared neoantigen vaccine 비교?
**A.** Personalized vaccine manufacturing TAT는 platform·workflow에 따라 차이가 큽니다. atezolizumab + PGV001 urothelial 1상에서는 vaccine 성공 제조 10/12, median end-to-end time 20.3주가 보고되어 second-line decision window와 맞물리는 운영 부담을 시사하고 ([Saxena 2025 atezolizumab](../sources/atezolizumab-2025-personalized-neoantigen-vaccination-urothelial-cancer.md)), GT-30 HCC trial은 모든 36명에서 second-line 시점까지 vaccine을 제공함으로써 operational scalability를 입증했습니다 ([Yarchoan 2024](../sources/yarchoan-2024-personalized-neoantigen-vaccine-pembrolizumab-advanced.md)). Chen 2026 TEV-based scaffold vaccine은 환자 검체에서 TEV만 추출해 사용함으로써 neoantigen 예측·합성 파이프라인 자체를 우회해 cost·time을 줄이는 우회 전략의 가능성을 보였습니다 ([Chen 2026 TEV](../sources/chen-2026-spatiotemporally-engineered-tumor-derived-extracellular-vesicle.md)). Shared neoantigen 백신(KRAS hotspot, mBRAF)은 환자별 합성 없이 off-the-shelf로 제공 가능해 TAT·cost가 본질적으로 낮고, Khaddour 2026 review는 monovalent shared vs polyvalent personalized 디자인을 적응증에 맞춰 선택할 framework를 제시합니다 ([Khaddour 2026](../sources/khaddour-2026-bridging-clinical-gaps-personalized-cancer-neoantigen.md), [Rappaport 2024](../sources/rappaport-2024-shared-neoantigen-vaccine-checkpoint-blockade.md)).

**Cited**: [Saxena 2025 atezolizumab](../sources/atezolizumab-2025-personalized-neoantigen-vaccination-urothelial-cancer.md), [Yarchoan 2024](../sources/yarchoan-2024-personalized-neoantigen-vaccine-pembrolizumab-advanced.md), [Chen 2026 TEV](../sources/chen-2026-spatiotemporally-engineered-tumor-derived-extracellular-vesicle.md), [Khaddour 2026](../sources/khaddour-2026-bridging-clinical-gaps-personalized-cancer-neoantigen.md)

**Filed**: existing

### Q31. CAR-T (CD19, BCMA, FLT3 등 lineage antigen)의 antigen loss / lineage switch escape 빈도와 mitigation 전략?
**A.** CD19-CAR (CTL019) B-ALL relapse 코호트에서 Orlando 2018은 CD19-negative relapse 환자의 모든 사례에서 CD19 mutation을 식별했고, exon 2~5에 truncating·transmembrane 손상 mutation이 산재하며 mutant allele frequency가 CD19-null 분획과 일치해 clonal selection 패턴이 입증됩니다 ([Orlando 2018](../sources/orlando-2018-target-antigen-loss-car19-therapy.md)). BCMA·multiple myeloma에서는 BCMA가 plasma cell maturation lineage antigen으로 표적 가치가 높지만 epitope shedding·downregulation을 통한 escape가 보고됩니다 ([Shah 2020](../sources/shah-2020-b-cell-maturation-antigen-bcma-multiple.md)). Mitigation으로는 dual-target/multispecific CAR, lower antigen-density threshold, logic-gated design 등 antigen escape concept이 본 wiki concept page에 정리되어 있어 single-antigen 의존을 줄이는 디자인이 권장됩니다 ([antigen-loss concept](../concepts/antigen-loss-lineage-switch-and-target-escape.md), [Zugasti 2025](../sources/zugasti-2025-cart-cancer-current-challenges-future-directions.md)). FLT3 등 myeloid lineage antigen에 대한 deep-dive는 본 corpus에서 상대적으로 thin해 보입니다.

**Cited**: [Orlando 2018](../sources/orlando-2018-target-antigen-loss-car19-therapy.md), [Shah 2020](../sources/shah-2020-b-cell-maturation-antigen-bcma-multiple.md), [Zugasti 2025](../sources/zugasti-2025-cart-cancer-current-challenges-future-directions.md), [antigen-loss concept](../concepts/antigen-loss-lineage-switch-and-target-escape.md)

**Filed**: evidence-gap (FLT3 lineage antigen·myeloid CAR-T escape는 corpus 보강 후보)

### Q32. 신항원 백신과 corticosteroid (dexamethasone) 동시 투여의 면역반응 억제 정도 — clinical practice implication?
**A.** 본 corpus에서 dexamethasone 동시 투여의 vaccine-specific T cell 반응 억제 정도를 정량한 직접적 trial-level 데이터는 thin합니다. 다만 Sagie 2025가 lymphodepleting chemotherapy가 antigen presentation을 강화함을 보인 것처럼, 면역억제제·corticosteroid 사용은 T cell expansion 및 antigen presentation에 부정적인 영향을 줄 가능성이 mechanistic 측면에서 시사됩니다 ([Sagie 2025](../sources/sagie-2025-lymphodepleting-chemotherapy-potentiates-neoantigen-directed-t.md)). 임상시험 디자인에서는 vaccine 접종 직전·직후 corticosteroid 사용을 회피하거나 prophylactic dose로 제한하고, irAE 관리를 위한 corticosteroid가 필요할 경우 vaccine 면역원성과의 trade-off를 monitoring하는 것이 합리적이라 사료됩니다. 단, 본 질문에 대한 corpus 내 직접 증거는 thin하므로 prospective trial 보고가 보강될 가치가 있겠습니다.

**Cited**: [Sagie 2025](../sources/sagie-2025-lymphodepleting-chemotherapy-potentiates-neoantigen-directed-t.md)

**Filed**: evidence-gap (dexamethasone × neoantigen vaccine 직접 trial 데이터 부족, 후속 corpus 보강 후보)

## Section D — Biomarkers & response models (Q33-41)

### Q33. HLA-based neoantigen presentation score (Han 2024)와 단순 TMB의 pan-cancer ICI 반응 예측 비교?
**A.** Han 2024는 885명 pan-cancer ICI 코호트에서 neoantigen-HLA binding affinity와 HLA-I allele divergence를 통합한 HAPS(HLA tumor-Antigen Presentation Score)를 개발했고, 높은 HAPS가 단순 TMB보다 ICI survival benefit과 더 잘 연관됨을 보고했습니다. HAPS-high 환자는 antigen presentation pathway가 enriched되었고, neoantigen production·presentation·recognition factor를 통합한 neural network이 ICI benefit 예측에 추가적 정보를 제공했습니다 ([Han 2024](../sources/han-2024-assessment-human-leukocyte-antigen-based-neoantigen.md)). Cristescu 2018은 TMB와 T-cell-inflamed GEP가 각각 ICI 반응을 부분적으로 예측하며 약한 상관만 가지므로 mutation load와 immune activation이 서로 다른 차원임을 보였고, HAPS 같은 presentation-aware score는 두 axis 사이를 다리 놓는 정보를 추가한다고 사료됩니다 ([Cristescu 2018](../sources/cristescu-2018-pan-tumor-genomic-biomarkers-pd1-blockade.md)). Zhang 2025의 MHC-I-dependent neoantigen presentation pathway score도 같은 방향성을 제시합니다 ([Zhang 2025](../sources/zhang-2025-mhc-i-dependent-neoantigen-presentation-pathway-predicts.md)).

**Cited**: [Han 2024](../sources/han-2024-assessment-human-leukocyte-antigen-based-neoantigen.md), [Cristescu 2018](../sources/cristescu-2018-pan-tumor-genomic-biomarkers-pd1-blockade.md), [Zhang 2025](../sources/zhang-2025-mhc-i-dependent-neoantigen-presentation-pathway-predicts.md)

**Filed**: existing

### Q34. TLS score / B-cell signature가 ICI 반응 예측에서 PD-L1, TMB, MSI 외에 추가하는 정보량?
**A.** Vanhersecke 2021은 3개 ICI cohort에서 mature TLS의 유무가 PD-L1 status와 CD8 density에 독립적으로 ORR·PFS·OS와 연관됨을 보여 TLS가 PD-L1·CD8 외의 incremental information을 제공함을 입증했습니다 ([Vanhersecke 2021](../sources/vanhersecke-2021-mature-tertiary-lymphoid-structures-predict.md)). Cabrita 2020 melanoma는 CD8+CD20+ TLS 신호 + B-cell gene signature가 다른 임상 변수에 독립적으로 ICI 반응 예측에 기여함을 보였고 ([Cabrita 2020](../sources/cabrita-2020-tertiary-lymphoid-structures-improve-immunotherapy.md)), Yang 2024 pan-cancer atlas는 TAAB·class-switched memory B subset이 ICI 반응 예측력에 기여하는 B-cell-side biomarker임을 시사합니다 ([Yang 2024](../sources/yang-2024-pan-cancer-single-cell-dissection-reveals-phenotypically.md)). du 2025 TLS gene signature는 advanced NSCLC chemo + ICI 반응 예측에 추가 정보를 제공하고 ([du 2025](../sources/du-2025-tls-gene-signature-advanced-nsclc.md)), Sierra-Rodero 2026 NADIM 분석은 BCR repertoire clonality·class-switched clone이 TLS density 단독보다 CPR과 더 강하게 연관됨을 보여 B-cell-centric metric의 가치를 강조합니다 ([Sierra-Rodero 2026](../sources/sierrarodero-2026-decoding-cell-signatures-complete-pathologic-response.md)).

**Cited**: [Vanhersecke 2021](../sources/vanhersecke-2021-mature-tertiary-lymphoid-structures-predict.md), [Cabrita 2020](../sources/cabrita-2020-tertiary-lymphoid-structures-improve-immunotherapy.md), [Yang 2024](../sources/yang-2024-pan-cancer-single-cell-dissection-reveals-phenotypically.md), [du 2025](../sources/du-2025-tls-gene-signature-advanced-nsclc.md), [Sierra-Rodero 2026](../sources/sierrarodero-2026-decoding-cell-signatures-complete-pathologic-response.md)

**Filed**: existing

### Q35. Pre/post-treatment paired sample design에서 신항원 reshape pattern을 어떻게 추적하는가?
**A.** Pre/post 쌍을 직접 활용한 대표 사례로 Sierra-Rodero 2026 NADIM/NADIM II 코호트는 baseline·surgery·6개월 adjuvant 시점의 tissue·blood를 BCR repertoire, mIF, bulk/spatial/scRNA-seq로 평행하게 추적해 ChIO 동안 B cell·TLS 시그니처가 어떻게 reshape되는지 정량했습니다 ([Sierra-Rodero 2026](../sources/sierrarodero-2026-decoding-cell-signatures-complete-pathologic-response.md)). Awad 2022 NEO-PV-01 phase Ib에서는 38명 NSCLC에서 baseline tumor immune infiltration과 on-treatment ctDNA, post-vaccination biopsy를 paired로 측정해 de novo CD4/CD8 반응과 epitope spread(KRAS G12C/G12V)를 추적했습니다 ([Awad 2022](../sources/awad-2022-personalized-neoantigen-vaccine-neo-pv-01-chemotherapy.md)). Vendramin 2026은 1,000명+ ICI 코호트에서 NMD 활성과 PTC 유래 immunopeptidome의 reshape을 longitudinal frame으로 연결해 치료 전후 신항원 풀의 expand 양상을 시사합니다 ([Vendramin 2026](../sources/vendramin-2026-nonsense-mediated-mrna-decay-inhibition-reshapes.md)). 이러한 paired 디자인을 multi-omics(BCR/TCR + immunopeptidomics + ctDNA)와 결합하는 framework가 신항원 reshape 추적의 표준으로 자리잡고 있다고 사료됩니다.

**Cited**: [Sierra-Rodero 2026](../sources/sierrarodero-2026-decoding-cell-signatures-complete-pathologic-response.md), [Awad 2022](../sources/awad-2022-personalized-neoantigen-vaccine-neo-pv-01-chemotherapy.md), [Vendramin 2026](../sources/vendramin-2026-nonsense-mediated-mrna-decay-inhibition-reshapes.md)

**Filed**: existing

### Q36. Single-cell TCR + neoantigen tetramer dual readout이 vaccine response 정량에 주는 advantage?
**A.** Blass 2025는 melanoma 10명에게 ipilimumab + nivolumab 병용 personalized 백신을 투여 후 환자당 수백 개 circulating/intratumoral TCR clonotype을 식별했고, neoantigen-specific 클론을 single-cell phenotype과 연결해 intratumoral T cell repertoire의 백신 유도 remodeling을 정량할 수 있음을 보였습니다 ([Blass 2025](../sources/blass-2025-multi-adjuvant-personal-neoantigen-vaccine-generates.md)). Braun 2025 RCC 백신 시험에서도 TCR 동역학 추적으로 새 클론이 수 주 안에 평균 166배 확장되고 다년간 지속됨을 정량했으며 7/9 환자에서 autologous tumor 인지 반응을 paired로 확인했습니다 ([Braun 2025](../sources/braun-2025-neoantigen-vaccine-generates-antitumour-immunity.md)). Fuchsl 2024는 high-resolution single-cell readout으로 neoantigen-specific TCR 활성화 강도와 engineered T cell resilience를 정량적으로 연결해 tetramer + sc-TCR 결합이 vaccine T cell quality·persistence를 단순 ELISpot보다 깊이 해석할 수 있음을 시사합니다 ([Fuchsl 2024](../sources/fchsl-2024-high-resolution-profile-neoantigen-specific-tcr-activation.md)).

**Cited**: [Blass 2025](../sources/blass-2025-multi-adjuvant-personal-neoantigen-vaccine-generates.md), [Braun 2025](../sources/braun-2025-neoantigen-vaccine-generates-antitumour-immunity.md), [Fuchsl 2024](../sources/fchsl-2024-high-resolution-profile-neoantigen-specific-tcr-activation.md)

**Filed**: existing

### Q37. Liquid biopsy / ctDNA 기반 minimal residual disease와 신항원 백신 efficacy timeline 매칭?
**A.** Cai 2021 HCC 백신 시험은 10명 환자에서 개별 신항원 mutation을 ctDNA panel로 추적해 백신 투여 도중·이후 시점에 corresponding neoantigen mutation의 ctDNA dynamics가 RFS·임상 반응과 실시간으로 동조함을 보여 MRD 모니터링과 vaccine timeline의 직접적 매칭이 가능함을 입증했습니다 ([Cai 2021](../sources/cai-2021-personalized-neoantigen-vaccine-prevents-postoperative.md)). Awad 2022 NEO-PV-01 시험에서도 on-treatment ctDNA 수준이 clinical response와 강하게 상관해 백신 효능의 초기 surrogate로 활용될 수 있음을 보고했습니다 ([Awad 2022](../sources/awad-2022-personalized-neoantigen-vaccine-neo-pv-01-chemotherapy.md)). Khaddour 2026 review는 adjuvant/perioperative MRD 환자가 PCV로부터 최대 benefit을 얻을 가능성이 가장 큰 임상 영역임을 framework로 정리하면서 ctDNA-MRD 기반 patient selection·timing이 핵심 translational gap임을 강조합니다 ([Khaddour 2026](../sources/khaddour-2026-bridging-clinical-gaps-personalized-cancer-neoantigen.md)). CNNeoPP의 cfDNA proof-of-concept은 비침습 neoantigen 예측·검증을 액체생검 차원에서 연계할 가능성을 시사합니다 ([Cai 2026](../sources/cai-2026-cnneopp-large-language-model-enhanced-deep.md)).

**Cited**: [Cai 2021](../sources/cai-2021-personalized-neoantigen-vaccine-prevents-postoperative.md), [Awad 2022](../sources/awad-2022-personalized-neoantigen-vaccine-neo-pv-01-chemotherapy.md), [Khaddour 2026](../sources/khaddour-2026-bridging-clinical-gaps-personalized-cancer-neoantigen.md), [Cai 2026](../sources/cai-2026-cnneopp-large-language-model-enhanced-deep.md)

**Filed**: existing

### Q38. Thymic health / 노년 환자에서 ICI 효능 저하 메커니즘 — TCR repertoire 다양성과의 관계?
**A.** Bernatz 2026은 routine CT 영상에 deep-learning foundation model을 적용해 pan-cancer 3,476명 ICI 코호트에서 thymic health score(0–100)를 정량화했고, NSCLC에서 thymic health가 높을수록 progression·all-cause mortality 위험이 감소했으며 이 연관은 PD-L1·TMB 보정 후에도 유지되었습니다 ([Bernatz 2026](../sources/bernatz-2026-thymic-health-immunotherapy-outcomes-patients-cancer.md)). 전향적 TRACERx lung 코호트(n=464)에서 thymic health는 TCR diversity, T cell receptor excision circles(TRECs), immune-signaling pathway와 양의 상관을 보여 흉선 활동 저하가 naive T cell 공급 감소·repertoire narrowing으로 ICI 효능을 제한할 수 있는 기전적 단서를 제공합니다. melanoma·breast·renal 분석으로 pan-cancer 관련성이 확인되어, host-side aging biomarker로서 tumor-centric biomarker를 보완할 수 있는 축으로 사료됩니다.

**Cited**: [Bernatz 2026](../sources/bernatz-2026-thymic-health-immunotherapy-outcomes-patients-cancer.md)

**Filed**: existing

### Q39. Tumor evolution 시점별 (primary, metastasis, post-treatment) 신항원 landscape 변화의 임상 의미?
**A.** Hessey 2026은 TRACERx + PEACE에서 NSCLC 24명·501샘플 분석으로 metastasis genome이 ancestral primary와 현저히 diverge하며 dissemination 이후 추가 driver alteration과 genome doubling이 발생함을 보였고, 환자 62.5%에서 polyclonal seeding과 metastasis-to-metastasis spread가 관찰되어 단일 metastasis biopsy로는 후보 antigen pool을 과소 추정할 가능성을 시사합니다 ([Hessey 2026](../sources/hessey-2026-evolutionary-characterization-lung-cancer-metastasis.md)). Sholokhova 2026 CRC simulation은 "강한 clonal neoantigen 1개"의 존재와 minimal neoantigen quality가 durable response의 가장 강력한 예측인자임을 보여 truncal·clonal high-quality neoantigen에 시점별로 가중치를 두어야 함을 시사합니다 ([Sholokhova 2026](../sources/sholokhova-2026-neoantigen-evolution-response-checkpoint-inhibitor-immunotherapy.md)). Marine 2026 review는 genetic·epigenetic·proteomic·immunopeptidomic 다층 ITH의 시점별 통합 측정 필요성을 강조하여 primary–metastasis–post-treatment 시계열 design이 vaccine/TCR-T target 재선정의 핵심임을 정리합니다 ([Marine 2026](../sources/marine-2026-mapping-intratumor-heterogeneity-across-layers-advancing.md)).

**Cited**: [Hessey 2026](../sources/hessey-2026-evolutionary-characterization-lung-cancer-metastasis.md), [Sholokhova 2026](../sources/sholokhova-2026-neoantigen-evolution-response-checkpoint-inhibitor-immunotherapy.md), [Marine 2026](../sources/marine-2026-mapping-intratumor-heterogeneity-across-layers-advancing.md)

**Filed**: existing

### Q40. Pathologic CR (pCR) 환자의 B cell signature가 non-pCR과 어떻게 다른가 (perioperative ICI in NSCLC, breast)?
**A.** Sierra-Rodero 2026 NADIM/NADIM II 123명 NSCLC 코호트에서 CPR tumor는 baseline에서 더 clonal한 BCR repertoire(AUC 0.775, p=0.030)를 보였고 ChIO 동안 잘 conserved·reinvigorated되었으며 혈액에서는 class-switched clone이 풍부한 repertoire(AUC 0.833, p=0.008)와 activation 관련 transcriptional program 상향을 보였습니다 ([Sierra-Rodero 2026](../sources/sierrarodero-2026-decoding-cell-signatures-complete-pathologic-response.md)). TLS density 단독은 CPR과 유의하지 않았으나(p=0.129) mature TLS에서는 antigen-presenting pathway·Tfh·plasmacytoid DC·plasma cell이 풍부했고, low-B cell 영역에서는 CD8+ T·NK·macrophage가 풍부했습니다. Sun 2022 NSCLC와 Harris 2021 TNBC도 mature TLS 풍부도와 class-switched IgG-biased clonally expanded TIL-B가 favorable outcome과 연관됨을 보여 ([Sun 2022](../sources/sun-2022-tls-neoadjuvant-chemoimmunotherapy-resectable-nsclc.md), [Harris 2021](../sources/harris-2021-tumor-infiltrating-b-lymphocyte-profiling-identifies.md)), perioperative 세팅에서 B cell-centric metric이 pCR predictive biomarker로 promising함을 시사합니다.

**Cited**: [Sierra-Rodero 2026](../sources/sierrarodero-2026-decoding-cell-signatures-complete-pathologic-response.md), [Sun 2022](../sources/sun-2022-tls-neoadjuvant-chemoimmunotherapy-resectable-nsclc.md), [Harris 2021](../sources/harris-2021-tumor-infiltrating-b-lymphocyte-profiling-identifies.md)

**Filed**: existing

### Q41. Mass-spec confirmed neoantigen vs predicted neoantigen의 prognostic value 차이?
**A.** Tretter 2023 pan-tumor 32명 코호트는 multi-omics + immunopeptidomics로 후보 32개 신항원을 MS-검증해, in silico predicted neoantigen 다수가 naturally presented되지 않을 수 있고 MS 검증을 거친 후보가 immunogenicity·임상적 관련성에서 더 의미 있는 우선순위를 줄 수 있음을 시사합니다 ([Tretter 2023](../sources/tretter-2023-proteogenomic-analysis-reveals-rna-source.md)). Chong 2020은 proteogenomic deep sequencing으로 수백 개 non-canonical HLA peptide를 MS 직접 확인해 prediction-only pipeline이 놓치는 antigen class까지 prognostic·therapeutic frame에 추가할 수 있음을 보였습니다 ([Chong 2020](../sources/chong-2020-integrated-proteogenomic-deep-sequencing-analytics.md)). Łuksza 2022는 MS-confirmed가 아닌 quality-aware predicted neoantigen 모델로 long-term PDAC survivor의 면역편집과 재발 종양의 high-quality neoantigen 감소를 정량해 prognostic value를 보였으며, MS 검증이 prediction prognostic signal을 더 정교화하는 보완적 layer로 작동함을 사료할 수 있겠습니다 ([Łuksza 2022](../sources/uksza-2022-neoantigen-quality-predicts-immunoediting-survivors.md)).

**Cited**: [Tretter 2023](../sources/tretter-2023-proteogenomic-analysis-reveals-rna-source.md), [Chong 2020](../sources/chong-2020-integrated-proteogenomic-deep-sequencing-analytics.md), [Łuksza 2022](../sources/uksza-2022-neoantigen-quality-predicts-immunoediting-survivors.md)

**Filed**: existing

## Section E — Methods / Pipelines / Resources (Q42-50)

### Q42. Immunopeptidomics workflow (IP-MS, MHCquant2, Comet, MSFragger, MaxQuant) 비교 — sensitivity vs FDR 격차?
**A.** Scheid 2025 MHCquant2는 OpenMS·DeepLC·MS2PIP를 nf-core Nextflow로 통합한 modular pipeline으로, diverse MS platform 전반에서 peptide identification을 최대 ~27% 개선하면서 global FDR을 standardized하게 적용해 reproducibility를 확보했습니다 ([Scheid 2025](../sources/scheid-2025-mhcquant2-refines-immunopeptidomics-tumor-antigen.md)). PCI-DB는 동일 MHCquant2·epitopeprediction nf-core 파이프라인으로 10,000+ raw 파일을 처리해 6.6M HLA-I + 3.4M HLA-II peptide를 global FDR 기반으로 통일·관리했습니다 ([Lemke 2025](../sources/lemke-2025-pci-db-novel-primary-tissue-immunopeptidome.md)). Chong 2020은 두 MS/MS search tool을 조합하여 non-canonical peptide에 대한 FDR control을 강화한 reference이며 ([Chong 2020](../sources/chong-2020-integrated-proteogenomic-deep-sequencing-analytics.md)), Wen 2020 NeoFlow는 deep-learning retention time(AutoRT) 기반 metric으로 search engine 간 QC 차이를 정량해 single-pipeline 선택이 변이 peptide 수와 putative neoantigen 수를 substantially 달리할 수 있음을 보였습니다 ([Wen 2020](../sources/wen-2020-cancer-neoantigen-prioritization-through-sensitive.md)). MaxQuant/MSFragger/Comet의 직접 head-to-head benchmark는 본 corpus에서 부분적이므로 향후 보강이 필요한 evidence-gap으로도 작용합니다.

**Cited**: [Scheid 2025](../sources/scheid-2025-mhcquant2-refines-immunopeptidomics-tumor-antigen.md), [Lemke 2025](../sources/lemke-2025-pci-db-novel-primary-tissue-immunopeptidome.md), [Chong 2020](../sources/chong-2020-integrated-proteogenomic-deep-sequencing-analytics.md), [Wen 2020](../sources/wen-2020-cancer-neoantigen-prioritization-through-sensitive.md)

**Filed**: existing

### Q43. De novo peptide identification (Casanovo, PepNet, pNovo3, SMSNet)의 cancer immunopeptidome 적용에서의 강점과 한계?
**A.** 본 corpus에서 Casanovo·PepNet·pNovo3·SMSNet 자체의 직접 head-to-head benchmark는 thin하지만, Lehe 2026 review는 splice/isoform peptide 영역에서 CNovo/SpliceNovo·DIAVariant 같은 de novo·library-free 도구가 DDA library-based search가 놓치는 단일 아미노산 변이까지 회수할 수 있음을 정리하면서, de novo 접근의 강점이 cancer-specific variant peptide 검출과 reference database 의존성 해소에 있다고 설명합니다 ([Lehe 2026](../sources/lehe-2026-mass-spectrometry-alternative-protein-isoforms-review.md)). 한계로는 immunopeptidome의 짧은 비-tryptic peptide·낮은 abundance·spectrum quality 의존성으로 잘못된 sequence 호출이 늘어날 수 있고, FDR control이 standardized search engine보다 부족하다는 점이 review에서 시사됩니다. Chong 2020은 두 search tool을 결합해 non-canonical peptide의 false positive를 억제하는 보수적 전략을 보여, de novo 결과를 proteogenomic database + 보조 search와 cross-check하는 hybrid workflow가 현재로선 적합한 운용 방식으로 사료됩니다 ([Chong 2020](../sources/chong-2020-integrated-proteogenomic-deep-sequencing-analytics.md)).

**Cited**: [Lehe 2026](../sources/lehe-2026-mass-spectrometry-alternative-protein-isoforms-review.md), [Chong 2020](../sources/chong-2020-integrated-proteogenomic-deep-sequencing-analytics.md)

**Filed**: evidence-gap (Casanovo·PepNet·pNovo3·SMSNet 자체에 대한 cancer immunopeptidome head-to-head benchmark가 본 corpus에 없음 — proteogenomic de novo 도구 비교 paper 추가 필요)

### Q44. Proteogenomic neoantigen pipeline (NeoFlow, NeoDisc, Wen 2020 NeoFlow, iPepGen, ImmunoNX) 비교?
**A.** Wen 2020 NeoFlow는 AutoRT(retention time deep learning) 기반 QC metric을 표준화해 287 tumor에서 변이 peptide·putative neoantigen 식별의 sensitivity·reliability를 정량 평가하는 proteogenomic 베이스라인을 정립했습니다 ([Wen 2020](../sources/wen-2020-cancer-neoantigen-prioritization-through-sensitive.md)). Shapiro 2025 NeoDiscMS는 NeoDisc 임상 antigen discovery 파이프라인에 real-time NGS-guided immunopeptidomics를 통합해 inclusion list·chimeric-spectrum deconvolution(MSFragger DDA+)으로 TAA 검출 ~20%를 개선하는 acquisition-side 강점을 제공합니다 ([Shapiro 2025](../sources/shapiro-2025-sensitive-neoantigen-discovery-real-time-mutanome-guided.md)). Mehta 2025 iPepGen은 cloud gateway 기반 modular pipeline으로 prediction → identification → verification → prioritization을 비전문가도 접근 가능하게 만들었고 ([Mehta 2025](../sources/mehta-2025-modular-immunopeptidogenomic-ipepgen-analysis-pipeline.md)), Singhal 2025 ImmunoNX는 WDL/Cromwell·pVACtools·pVACview·IGV manual review로 11개 임상시험·185명+ 환자의 vaccine design을 3개월 내 가능케 한 trial-grade workflow입니다 ([Singhal 2025](../sources/singhal-2025-immunonx-robust-bioinformatics-workflow-support.md)). 즉 NeoFlow는 QC 표준화, NeoDisc는 임상 immunopeptidomics 통합, iPepGen은 접근성, ImmunoNX는 clinical-grade vaccine design에 차별화된 강점을 가진다고 정리할 수 있겠습니다.

**Cited**: [Wen 2020](../sources/wen-2020-cancer-neoantigen-prioritization-through-sensitive.md), [Shapiro 2025](../sources/shapiro-2025-sensitive-neoantigen-discovery-real-time-mutanome-guided.md), [Mehta 2025](../sources/mehta-2025-modular-immunopeptidogenomic-ipepgen-analysis-pipeline.md), [Singhal 2025](../sources/singhal-2025-immunonx-robust-bioinformatics-workflow-support.md)

**Filed**: existing

### Q45. Real-time NGS-guided immunopeptidomics (Shapiro 2025 NeoDiscMS, inclusion list)의 sensitivity 게인과 TAT 단축?
**A.** Shapiro 2025 NeoDiscMS는 3초 cycle을 MS1·targeted real-time search(inclusion list 매칭 시 high-sensitivity scan trigger)·discovery DDA로 분할하여, NGS-derived candidate에 대해 측정 sensitivity를 높이면서 global peptide coverage를 보존하는 acquisition 설계를 제안합니다 ([Shapiro 2025](../sources/shapiro-2025-sensitive-neoantigen-discovery-real-time-mutanome-guided.md)). Discovery 브랜치는 wider isolation windows(3.2 Th)와 MSFragger DDA+ chimeric-spectrum deconvolution으로 co-isolated precursor에서도 식별을 회수했고, TAA 검출이 gold-standard acquisition 대비 최대 ~20% 증가했다고 보고되었습니다. Uveal melanoma 3개 lesion 사례에서는 lesion당 11,968–16,033 unique peptide가 단일 NeoDiscMS run에서 식별되어 NGS→candidate list→MS acquisition→prioritization 사이클을 임상 TAT 제약 안에 통합 가능함을 보여, real-time NGS-guided 전략이 sensitivity gain과 TAT 단축을 동시에 노릴 수 있는 reference design으로 사료됩니다.

**Cited**: [Shapiro 2025](../sources/shapiro-2025-sensitive-neoantigen-discovery-real-time-mutanome-guided.md)

**Filed**: existing

### Q46. 신항원 prediction algorithm (NetMHC, MHCflurry, EpiMII, CNNeoPP, NeoGuider) 비교 — feature space와 cross-task interpretability?
**A.** 본 corpus의 최신 모델은 feature space가 매우 다릅니다. Yuan 2025 EpiMII는 142,934개 MHC-II epitope 구조를 학습한 Graph Neural Network로 구조 feature에 집중해 ProteinMPNN 대비 4.2배 sequence recovery 개선(78.0%)을 보였고, HCC 사례에서 5/5 designed epitope가 CD4 활성화·IFN-γ·TNF-α 분비를 유도했습니다 ([Yuan 2025](../sources/yuan-2025-epimii-integrating-structure-graph-neural.md)). Cai 2026 CNNeoPP는 large language model 기반 sequence representation + multi-modal feature integration으로 TESLA 검증 + ELISpot 실험·cfDNA 응용을 결합한 prediction-to-monitoring 파이프라인을 제시합니다 ([Cai 2026](../sources/cai-2026-cnneopp-large-language-model-enhanced-deep.md)). Zhao 2025 NeoGuider는 custom kernel density estimation + centered isotonic regression의 supervised feature transformation으로 7 cohort·113명·635 immunogenic candidate에서 기존 도구를 outperform했습니다 ([Zhao 2025](../sources/zhao-2025-neoguider-neoepitope-prediction-using-advanced.md)). Zhang 2026 ImmUni는 binding·presentation·activation 3단계를 통합한 transformer로, 현 immunogenicity predictor가 intra-HLA label imbalance에서 비롯된 shortcut bias를 학습하고 있음을 information-theoretic metric으로 정량화하고 debiasing 전략을 제안해 cross-task interpretability를 진단·개선하는 framework를 제공합니다 ([Zhang 2026](../sources/zhang-2026-cross-task-interpretability-through-unified-modeling.md)).

**Cited**: [Yuan 2025](../sources/yuan-2025-epimii-integrating-structure-graph-neural.md), [Cai 2026](../sources/cai-2026-cnneopp-large-language-model-enhanced-deep.md), [Zhao 2025](../sources/zhao-2025-neoguider-neoepitope-prediction-using-advanced.md), [Zhang 2026](../sources/zhang-2026-cross-task-interpretability-through-unified-modeling.md)

**Filed**: existing

### Q47. PCI-DB / Cancer Surfaceome Atlas / OncoKB 같은 reference database를 신항원 prioritization에 어떻게 통합하는가?
**A.** Lemke 2025 PCI-DB(https://pci-db.org/)는 10,000+ raw MS 파일·3,000+ tissue를 MHCquant2 + epitopeprediction nf-core 파이프라인으로 통일 처리해 HLA-I 6.6M·HLA-II 3.4M peptide(40+ tissue·cancer entity)를 global FDR 기반으로 제공하며, 이를 통해 cross-tumor와 entity-specific TAA, frequent mutation 유래 neoepitope, 그리고 benign tissue presentation 검증으로 on-target/off-tumor 위험을 통합적으로 평가할 수 있는 reference로 자리잡았습니다 ([Lemke 2025](../sources/lemke-2025-pci-db-novel-primary-tissue-immunopeptidome.md)). Scheid 2025 MHCquant2의 benign reference(420 HLA-I 샘플·213,462 unique binder + 415 HLA-II 샘플·423,438 peptide)는 putative TAA 필터링·tumor-exclusive peptide 우선화의 직접 input으로 통합됩니다 ([Scheid 2025](../sources/scheid-2025-mhcquant2-refines-immunopeptidomics-tumor-antigen.md)). Singhal 2025 ImmunoNX는 consensus variant call + pVACtools 예측을 pVACview·IGV manual review로 prioritize하면서 reference database·matched normal 정보를 표준 절차로 통합하는 trial-grade framework를 제시합니다 ([Singhal 2025](../sources/singhal-2025-immunonx-robust-bioinformatics-workflow-support.md)).

**Cited**: [Lemke 2025](../sources/lemke-2025-pci-db-novel-primary-tissue-immunopeptidome.md), [Scheid 2025](../sources/scheid-2025-mhcquant2-refines-immunopeptidomics-tumor-antigen.md), [Singhal 2025](../sources/singhal-2025-immunonx-robust-bioinformatics-workflow-support.md)

**Filed**: existing

### Q48. Spatial omics (Xenium, CosMx, Visium HD, Open-ST)의 TLS spatial analysis 적용 비교?
**A.** Rademacher 2025는 같은 tumor cryosection에서 RNAscope HiPlex·Molecular Cartography·Merscope·Xenium·Visium 5개 platform을 비교하며 imaging-based 방법이 미세 microanatomy delineation·cell-type-specific transcriptome 측정에 강하고, slide reimaging으로 cell segmentation·multi-modal readout을 보완할 수 있음을 정량적으로 보였습니다 ([Rademacher 2025](../sources/rademacher-2025-comparison-spatial-transcriptomics-technologies-using.md)). Schott 2024 Open-ST는 sequencing 기반 high-resolution + 3D 재구성으로 head and neck tumor·lymph node에서 면역·stroma·tumor population을 공간적으로 포착하고 2D에서 보이지 않던 contiguous 3D 구조를 식별해 TLS 같은 조직 architecture 분석에 새로운 차원을 제공합니다 ([Schott 2024](../sources/schott-2024-open-st-high-resolution-spatial-transcriptomics-3d.md)). Bilous 2026은 Xenium 활용 시 transcript spillover가 TME 해석을 왜곡할 수 있음을 체계적으로 보이고 RCTD 기반 SPLIT으로 tumor-proximal T cell exhaustion signal을 개선해 TLS 인근 spatial purity 확보의 필요성을 시사합니다 ([Bilous 2026](../sources/bilous-2026-xenium-sensitivity-specificity-signal-contamination.md)). Wang 2025·Liu 2024 등 TLS-specific 응용은 spatial + scRNA 통합이 TLS density·organization을 prognostic frame으로 정립함을 보여줍니다 ([Wang 2025](../sources/wang-2025-single-cell-spatial-transcriptomics-gastric-tls.md)).

**Cited**: [Rademacher 2025](../sources/rademacher-2025-comparison-spatial-transcriptomics-technologies-using.md), [Schott 2024](../sources/schott-2024-open-st-high-resolution-spatial-transcriptomics-3d.md), [Bilous 2026](../sources/bilous-2026-xenium-sensitivity-specificity-signal-contamination.md), [Wang 2025](../sources/wang-2025-single-cell-spatial-transcriptomics-gastric-tls.md)

**Filed**: existing

### Q49. AI/ML 모델 (foundation pathology models, multimodal embeddings) 이 TLS detection / B cell quantification에 주는 정확도 향상?
**A.** Wu 2025는 whole-slide image에서 TLS maturity를 정량할 수 있는 transformer-based deep learning 모델을 만들어 gastric cancer 253명 코호트에 적용, 높은 TLS maturity가 향상된 환자 생존과 상관함을 보였고 17명 scRNA + multiplex IHC + flow + functional coculture와 통합해 CD8 TRM–activated B cell 회로(CXCL13–CXCR5, granzyme B)를 식별해 임상 적용 가능한 AI tool 가능성을 입증했습니다 ([Wu 2025](../sources/wu-2025-artificial-intelligence-multimodality-data-integration.md)). Long 2024 HCC 660명 다기관 연구는 baseline MRI radiomic feature + machine learning으로 peritumoral TLS density를 예측해 외부 검증 AUC 0.91을 달성했고, OS·RFS·면역치료 반응 stratification에서도 prognostic 가치를 보였습니다 ([Long 2024](../sources/long-2024-spatial-patterns-mri-based-radiomic-prediction.md)). Bernatz 2026의 CT 기반 self-supervised foundation model 또한 host-side thymic health를 정량해 TCR diversity·면역치료 outcome과 연결하여 multimodal embedding이 면역 구조의 비침습 정량에 기여할 수 있는 framework를 시사합니다 ([Bernatz 2026](../sources/bernatz-2026-thymic-health-immunotherapy-outcomes-patients-cancer.md)).

**Cited**: [Wu 2025](../sources/wu-2025-artificial-intelligence-multimodality-data-integration.md), [Long 2024](../sources/long-2024-spatial-patterns-mri-based-radiomic-prediction.md), [Bernatz 2026](../sources/bernatz-2026-thymic-health-immunotherapy-outcomes-patients-cancer.md)

**Filed**: existing

### Q50. clonotype-resolved single-cell multi-omic 분석이 tumor-infiltrating B cell의 antigen specificity 매핑에 어떤 강점을 주는가?
**A.** Yang 2024 pan-cancer atlas는 649명·19 cancer type scRNA를 통합해 tumor-enriched stress-response memory B cell과 TAAB 같은 prognostic subset을 정의하고, TAAB의 높은 clonal expansion·proliferation·CD4 T cell 상호작용을 single-cell 차원에서 면역치료 반응성과 연결할 수 있게 했습니다 ([Yang 2024](../sources/yang-2024-pan-cancer-single-cell-dissection-reveals-phenotypically.md)). Sierra-Rodero 2026은 NADIM/NADIM II에서 BCR repertoire(n=87 tissue, n=25 blood) + mIF + bulk/spatial/scRNA-seq를 paired로 통합해 class-switched·clonally expanded BCR clone과 mature TLS 내 Tfh·plasmacytoid DC·plasma cell phenotype을 clonotype-resolved 차원에서 CPR과 연결했습니다 ([Sierra-Rodero 2026](../sources/sierrarodero-2026-decoding-cell-signatures-complete-pathologic-response.md)). Harris 2021 TNBC는 IgG-biased·clonally expanded TIL-B와 BCR pathway 활성·IgG-narrow repertoire를 antigen-driven humoral 반응의 표지로 정의해 single-cell clonotype + transcriptome 결합이 TIB antigen specificity 추론에 강점을 제공함을 보였습니다 ([Harris 2021](../sources/harris-2021-tumor-infiltrating-b-lymphocyte-profiling-identifies.md)). Sodhi 2026은 nuclear-localized vs membrane-localized neoantigen에 따라 endogenous IgG·humoral 반응이 결정됨을 보여 clonotype + sc-multiomics가 antigen feature와 vaccine 효능을 잇는 framework로 사료됩니다 ([Sodhi 2026](../sources/sodhi-2026-endogenous-neoantigen-specific-antibodies-mediate-antitumor.md)).

**Cited**: [Yang 2024](../sources/yang-2024-pan-cancer-single-cell-dissection-reveals-phenotypically.md), [Sierra-Rodero 2026](../sources/sierrarodero-2026-decoding-cell-signatures-complete-pathologic-response.md), [Harris 2021](../sources/harris-2021-tumor-infiltrating-b-lymphocyte-profiling-identifies.md), [Sodhi 2026](../sources/sodhi-2026-endogenous-neoantigen-specific-antibodies-mediate-antitumor.md)

**Filed**: existing

## Connections

- [B-Cell Neoantigen Research Map (topic)](../topics/b-cell-neoantigen-human-cancer.md)
- [B-Cell Neoantigen Research Map (synthesis)](../syntheses/b-cell-neoantigen-research-map.md)
- [Neoantigen Discovery and Prioritization](../concepts/neoantigen-discovery-and-prioritization.md)
- [B-Cell and TLS Context for Neoantigen Research](../concepts/b-cell-and-tls-context-for-neoantigen-research.md)
- [Clinical Translation of Neoantigen Research](../concepts/clinical-translation-of-neoantigen-research.md)
- [Biomarkers and Response Models](../concepts/biomarkers-and-response-models.md)
- [Four-Topic Question Expansion Map](topic-question-expansion-map.md) (Topic 1)
- [100-Question Wiki Expansion Sprint](100-question-wiki-expansion-sprint.md)

## Sources

- 28 new source pages from `topic-sweep-2026-05-25` (see topic hub Section "2026-05 Topic Sweep Additions")
- 230+ existing `wiki/sources/` pages linked from topic hub
