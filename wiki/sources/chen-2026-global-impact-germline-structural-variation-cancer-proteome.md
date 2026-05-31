---
title: Global impact of germline structural variation on the cancer proteome
authors:
  - "Chen"
  - "Vasaikar"
  - "Reva"
  - "Lim"
  - "Wen"
  - "Liao"
  - "Zhang"
year: 2026
journal: "Nature Communications"
doi: "10.1038/s41467-026-71967-y"
paper_kind: proteogenomic
cancer_types:
  - pan-cancer
modalities:
  - whole-genome-sequencing
  - rna-seq
  - proteomics
  - dna-methylation
themes:
  - structural-variation
  - germline
  - cis-regulatory
  - dna-methylation
  - cpg-island
  - enhancer
  - cancer-susceptibility-gene
  - ancestry
  - tumour-type-specific
  - top2a
  - nedd1
  - fabp5
tags:
  - source
  - structural-variation
  - germline
  - proteogenomics
pdf: "raw/inbox/papers/chen-2026-global-impact-germline-structural-variation-cancer-proteome.pdf"
pdf_status: complete
discovery_method: user-shared
topic: cancer-multiomics
cm_axis: integration
---
# Global impact of germline structural variation on the cancer proteome

## Summary

CPTAC 11개 종양형 1,637명의 normal sample paired WGS·RNA-seq·정량 단백체(±DNA methylation)를 결합해 **germline structural variation(SV)이 cis-regulatory 방식으로 cancer proteome에 미치는 영향**을 처음으로 pan-cancer 규모로 정량화한 연구. Delly v3.1.1 + SVABA v1.2.0 paired SV calling으로 704,263개 distinct germline SV(86% singleton, 73% DGV, 58% gnomAD, 55% TOPMed에서 catalog됨)을 식별하고, 이 중 25,781개 LoF SV가 12,442개 paired proteomics 측정에서 1,847개 저발현 사건(512 genes / 786 patients)을 만든다는 것을 확인. 31개 cancer susceptibility gene(CSG)의 LoF SV가 101명(전체 6%)에서 발견됐고(CDH13, CDKN2A, MSR1, SDHA, SMAD4, SMARCB1 포함), 364개 recurrently SV-altered gene 중 129개(17%)가 mRNA·protein 양쪽에서 concordant cis-regulation을 보임. CpG island/enhancer methylation을 매개로 한 추가 sub-rosa cis-mechanism(1,237 CGI probe + 109 enhancer-methylation SV), tumour-type-specific 효과(137 genes only concordant in single tissue), ancestry-enriched SV(31/69 concordant genes ancestry-specific; FSCN1-African, TIGAR-Asian, CTSW-European), 그리고 DepMap essentiality·survival 교차 검증(FABP5, NEDD1, TOP2A)을 통해 germline SV가 cancer 발현형의 비SNV 결정요인임을 입증한다.

## Key Points

### Cohort과 SV compendium 규모

- 1,637명 cancer patient × 11개 tumour type (BR breast / CCRCC / CO colon / GBM / HN head and neck / LUAD / LSCC / OV / PDA / UCEC / GBM 별 CPTAC 코호트 통합) + CBTN pediatric brain tumour validation cohort.
- Paired SV caller(Delly v3.1.1 ∩ SVABA v1.2.0) normal WGS에서 **704,263개 distinct germline SV** 발견; 86%가 singleton(코호트 내 1회 관찰), 73%가 DGV·58%가 gnomAD·55%가 TOPMed catalog에 등재, **84%가 최소 1개 reference catalog에 등재**.
- 신규 SV(no catalog 등재) 평균 18,776개/patient, breakdown: deletion 51% / duplication 24% / inversion 16% / insertion 9%. 평균 SV 길이 ≈ 950 bp(deletion median 320 bp / duplication 1.1 kb).

### LoF SV → low-protein cis-impact

- 114,684개 rare/singleton SV 중 **25,781 LoF SV**(SVAnnotate 기준 frameshift·exon-deletion·stop-gain 등). 이 중 12,442개가 paired proteomics에서 단백 정량 가능.
- **1,847 low-protein outlier event**(분위수 기반, FDR<10%) → **512 genes × 786 patients**에서 LoF SV가 단백 발현 저하와 cis-correlated. Hypergeometric enrichment에서 MHC class I antigen binding / antigen processing / exosome / mitochondrial matrix / Golgi membrane 카테고리가 유의.
- **CSG enrichment**: 688개 cancer susceptibility gene(csgs.sequenxe.com May 2024 reference) 중 31개가 LoF SV 보유자에서 단백 저발현; **CDH13 / CDKN2A / MSR1 / SDHA / SMAD4 / SMARCB1** 포함. 101명 환자(전체 1,637명의 **6%**)에서 최소 1개 CSG LoF SV 보유 → germline SV가 cancer predisposition의 무시할 수 없는 비SNV 컴포넌트.

### Gene-level recurrent cis-regulation

- 364 recurrently SV-altered gene(코호트 내 ≥3명) 중 **129 (17%)** 에서 SV → mRNA → protein concordant cis-regulation(relaxed FDR 기준, mRNA·protein 같은 방향). 17% 중 **CA8 / PTGR1**이 대표 mRNA-protein concordant LoF locus.
- 동일 set에서 33%는 reverse direction(protein 변화 우세, mRNA 변화 약함) → MS-based proteomics가 mRNA만으로 잡히지 않는 cis-effect를 포착함.

### DNA methylation 매개 sub-rosa cis-regulation

- **1,237개 CGI(CpG island) probe** FDR<10%에서 SV → methylation cis-association; 233/2,686 probe에서 positive methylation → negative mRNA 방향, 28개에서 단백 발현까지 concordant(CES1, GGACT, PTDSS2 등).
- **Enhancer methylation**: 109개 SV-enhancer methylation FDR<10% pair 중 41개가 CBTN pediatric brain tumour cohort에서 reproducible(p<1E-22); ECHDC1 / SH3GLB2 / MAMDC2가 대표 enhancer-methylation 매개 cis-target.

### Tumour-type-specific cis-effect

- 11 tumour type별로 별도 분석 시, **137개 gene이 단일 tissue에서만 mRNA+protein concordant**(반면 pan-tissue analysis에서는 17개만 잡힘) → tumour-type-specific germline SV impact가 pan-cancer analysis로 평균화되는 사각지대 존재.
- 대표 tissue-specific: **CDK2 (GBM)**, **RHOH (LUAD)**, **ARIH1 (renal/CCRCC)**; 60개 CGI probe도 tissue-specific methylation 매개.

### Ancestry-enriched germline SV

- PCA 기반 1KGP ancestry assignment(African / Asian / European / mixed)에서 SV spectrum이 ancestry로 분리됨.
- 69개 concordant cis-regulated gene 중 **31개 (45%)** 가 ancestry-enriched SV로 설명됨. **10 African (FSCN1 포함)**, **8 Asian (TIGAR 포함)**, **13 European (CTSW 포함)**.
- SIDT2 등 일부 gene은 ancestry 그 자체만으로 explained(즉, ancestry 보정 후 SV effect 사라짐) → ancestry-aware analysis가 cis-cancer effect 식별에 필수.

### Essential gene · 생존 교차 검증 (FABP5 / NEDD1 / TOP2A)

- DepMap essential gene + survival association 양쪽에서 통과한 cis-SV target은 **FABP5, NEDD1, TOP2A**. TOP2A는 common germline SV가 코호트 환자의 약 **25–30%**에 존재 → essential gene의 germline SV 보유자가 일정 비율 존재함.
- 추가로 UALCAN portal expression 검증 + figshare에 SV-expression pattern 데이터 공개.

### 데이터 소스 / 접근

- Genomics: **dbGaP phs001287.v21.p6 (CPTAC pan-cancer WGS)**, **phs003011.v1.p1**, **phs000178.v11.p8** (TCGA WGS).
- Proteomics: PDC (Proteomic Data Commons), GDC (Genomic Data Commons).
- Pediatric validation: CBTN (Children's Brain Tumor Network, Cavatica).
- Methylation: CPTAC 450K array 데이터.
- Portal: UALCAN; SV-expression 시각화는 figshare에 공개.

## Methods

- **샘플**: 11 tumour type CPTAC 코호트의 1,637 cancer patient(BR 122 / CCRCC 96 / CO 110 / GBM 99 / HN 109 / LUAD 110 / LSCC 108 / OV 174 / PDA 140 / UCEC 95 / 추가 GBM cohort 등; 정확한 분포는 paper Table S1 참조). 모든 환자에서 normal WGS + tumour RNA-seq + tumour proteomics 정량 사용 가능.
- **SV calling**: Delly v3.1.1 ∩ SVABA v1.2.0 paired normal vs reference(hg38) → 양쪽 모두에서 콜된 SV만 retain. CBTN cohort는 Manta v1.4.0 + SVABA v1.1.0 사용. SV 간 200 bp slop overlap → unique SV set 정의.
- **Catalog cross-reference**: DGV, gnomAD, TOPMed로 known SV vs novel 분류.
- **LoF annotation**: SVAnnotate(coding region overlap → frameshift / exon deletion / start-stop interruption / structural disruption 등).
- **CSG reference**: csgs.sequenxe.com (May 2024 snapshot, 688 genes).
- **Cis-association**: SVExpress-like quantile-based outlier test로 SV → mRNA / protein / methylation 효과 추정, BH FDR 10% cutoff.
- **Ancestry**: 1KGP PCA projection으로 African / Asian / European / Mixed 할당.
- **Reproducibility**: 일부 LoF·enhancer methylation SV → CBTN pediatric brain tumour cohort에서 독립 validation.
- **외부 검증**: DepMap essentiality + tumour survival 교차 분석; UALCAN expression 시각화.

## Cancer Multiomics Project Relevance

(한미약품·한미약품그룹/한미사이언스 산하 한미정밀의학(가칭, 이하 "한미암") cancer multiomics 과제에 대한 5축 적용)

### 1. Germline SV 패널 디자인 (한국인 코호트 적용 시 ancestry-enriched SV 우선)

- 본 논문 ancestry analysis에서 **Asian-enriched SV (TIGAR 포함 8개)** 와 **European/African-enriched SV(13/10개)** 가 cis-cancer effect를 별도로 설명함이 입증됨 → 한미암 한국인 환자 코호트에서 ancestry-specific SV panel(특히 Asian-enriched LoF SV in CSG)을 우선 sequencing 후보로 삼을 근거가 됨.
- CSG 31개 중 **CDH13, CDKN2A, SDHA, SMAD4, SMARCB1**은 이미 한미암 후보 cancer susceptibility 패널에 포함될 만한 유전자 → germline LoF SV(특히 exon-level deletion)를 SNV panel과 동시에 콜링하도록 분석 파이프라인 보강 필요.

### 2. SV → 단백 cis-effect 사전 검증 워크플로우

- 364 recurrent SV-altered gene 중 17%만 mRNA+protein concordant → 한미암 자체 단백체 코호트에서 cis-SV 후보를 우선화할 때 본 논문의 concordant list(특히 CA8, PTGR1, ECHDC1, SH3GLB2, MAMDC2, FABP5, NEDD1, TOP2A)를 priority validation set으로 활용 가능.
- Reverse direction(33%, protein-only effect) 비중이 큼 → 한미암 분석에서 mRNA-only QC로 SV impact를 reject하면 안 됨. MS-based 단백체가 cis-effect 발굴에 필수적임이 본 논문에서 증명.

### 3. 한국인 ancestry-stratified pQTL/svQTL 구축

- 본 논문은 1KGP 기반 ancestry로 31/69 concordant genes를 ancestry-stratified로 설명 → 한미암이 향후 한국인 cancer cohort pQTL/sQTL을 구축하려면, 1KGP East Asian super-population을 baseline으로 두고 **Korean-specific SV catalog**(KOVA, KCDC 등)을 referencing하는 ancestry-aware analysis pipeline 설계가 필요. SIDT2처럼 ancestry로 설명되는 SV는 false-positive risk가 큼.

### 4. CpG island/enhancer methylation 매개 sub-rosa cis-mechanism 통합

- SV가 직접 coding region에 영향이 없어도 CGI/enhancer methylation을 통해 단백 발현을 변경(1,237 + 109 사건)함이 입증 → 한미암 multi-omics 통합 파이프라인에서 **WGS-only 분석**으로 SV impact를 평가하지 말고, **methylation 450K/EPIC array 또는 WGBS**를 보조 modality로 결합해야 SV → expression 매개 메커니즘을 빠뜨리지 않음.

### 5. Pediatric/희귀암 코호트 확장 시 SV 메커니즘 reproducibility

- 본 논문은 CBTN(소아 뇌종양) cohort에서 41개 enhancer-methylation SV(p<1E-22)를 독립 reproduce → 성인 cancer에서 발견된 germline SV cis-mechanism이 **소아·희귀암 코호트로도 transfer 가능**한 통계적 power가 있음을 시사. 한미암이 한국 소아암 cohort(가령 어린이병원 IRB 협력)을 별도 코호트로 다룰 때 CBTN-style validation을 모방하는 분석 디자인이 가능.

## Connections

- [Cancer Multiomics Corpus Queue (Target=100)](../analyses/cancer-multiomics-corpus-queue.md)
- [Cancer Multiomics Proteogenomic Atlas](../topics/cancer-multiomics-literature.md)
- [Chen 2023 — Global impact of somatic structural variation on the cancer proteome](./chen-2023-global-impact-somatic-structural-variation-cancer-proteome.md) (자매 논문, somatic SV → 단백체 cis-effect)
- [Martins Rodrigues 2025 — CPTAC pan-cancer germline SNP impact study](./martins-rodrigues-2025-pan-cancer-germline-variant.md) (germline SNP/짧은 변이체 대응 분석; SNP 측면)

## Sources

- Local PDF: `raw/inbox/papers/chen-2026-global-impact-germline-structural-variation-cancer-proteome.pdf`
- Journal: Nature Communications (2026)
- DOI: [10.1038/s41467-026-71967-y](https://doi.org/10.1038/s41467-026-71967-y)
- Data:
  - dbGaP `phs001287.v21.p6` (CPTAC pan-cancer WGS)
  - dbGaP `phs003011.v1.p1`
  - dbGaP `phs000178.v11.p8` (TCGA WGS)
  - Proteomic Data Commons (PDC)
  - Genomic Data Commons (GDC)
  - CBTN / Cavatica (pediatric brain tumour validation)
  - UALCAN portal (expression cross-check)
  - figshare (SV-expression pattern 시각화 데이터)
- Reference catalog: csgs.sequenxe.com (May 2024 CSG snapshot)
- Tools: Delly v3.1.1, SVABA v1.2.0/v1.1.0, Manta v1.4.0, SVAnnotate, SVExpress, DGV, gnomAD, TOPMed

## 함께 인용된 논문

위키 분석·합성 페이지에서 이 논문과 함께 인용된 논문들 (co-citation).

- [[cao-2021-proteogenomic-characterization-pancreatic-ductal-adenocarcinoma|Cao 2021]]
- [[chang-2026-integrative-proteogenomics-gastric-cancer-taiwan|Chang 2026]]
- [[chen-2019-pan-cancer-molecular-subtypes-proteomic-characterization|Chen 2019]]
- [[chen-2023-global-impact-somatic-structural-variation-cancer-proteome|Chen 2023]]
- [[chmielecki-2023-acquired-resistance-first-line-osimertinib|Chmielecki 2023]]
- [[gillette-2020-proteogenomic-characterization-reveals-therapeutic-vulnerabilities|Gillette 2020]]
- [[holt-2025-proteogenomic-characterization-unveils-biomarkers-associated|Holt 2025]]
- [[huang-2021-proteogenomic-insights-biology-treatment-hpv-negative|Huang 2021]]
- [[jaehnig-2025-proteogenomic-analysis-calgb-40601-alliance|Jaehnig 2025]]
- [[lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc|Lee 2026]]
