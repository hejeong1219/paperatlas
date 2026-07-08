---
title: "Proteogenomics of Hypertrophic Cardiomyopathy Reveals Subtype-Specific Therapy"
authors:
  - "Ma"
  - "Yang"
  - "Guo"
  - "Li"
  - "Dong"
  - "Li"
year: 2026
journal: "Circulation Research"
doi: "10.1161/CIRCRESAHA.126.328300"
paper_kind: proteogenomic
pdf: "raw/inbox/papers/ma-2026-proteogenomics-hypertrophic-cardiomyopathy-subtype-specific-therapy.pdf"
topic: "multiomics-proteomics-ptm-identification"
tags:
  - "proteogenomics"
  - "hypertrophic-cardiomyopathy"
  - "cardiovascular"
  - "non-cancer"
  - "fatty-acid-oxidation"
  - "molecular-subtyping"
  - "drug-repurposing"
  - "hiPSC-CM"
  - "local-pdf-ingest"
themes:
  - "multiomics-identification"
  - "molecular-subtyping"
  - "therapy-target-nomination"
disease_area: cardiovascular
ingest_status: full-text-read
ingested_on: 2026-07-07
cm_axis: multiomics
---
# Proteogenomics of Hypertrophic Cardiomyopathy Reveals Subtype-Specific Therapy

_Circulation Research, 2026;139:e328300._ Open Access (CC BY-NC-ND). DOI: [10.1161/CIRCRESAHA.126.328300](https://doi.org/10.1161/CIRCRESAHA.126.328300).

ClinicalTrials.gov: NCT03076580. Corresponding: Yulin Li, Jianzeng Dong, Xin-liang Ma (Beijing Anzhen Hospital, Capital Medical University). First authors (equal): Ke Ma, Jie Yang, Hongchang Guo, Ping Li.

> **주의 — 비암(non-cancer) 논문**: 이 논문은 종양이 아니라 **비후성 심근병증(hypertrophic cardiomyopathy, HCM)** 심장 조직의 proteogenomic 연구다. 위키의 암 corpus와 별개이며, 방법론(WES+RNA-seq+proteome → 분자 아형 → 약물)이 사용자의 multiomics 파이프라인과 겹치기 때문에 methodology 레퍼런스로 보관한다.

## Summary

비후성 심근병증(HCM) 환자 **132명의 심근(중격) 조직**을 **WES + RNA-seq + proteomics**로 통합 분석해, 임상 예후와 직결되는 **2개의 단백체 기반 분자 아형(severe / mild)** 을 규명한 proteogenomic 연구다. 심각형(severe) 아형은 **지방산 산화(fatty acid oxidation, FAO)와 산화적 인산화(OXPHOS)의 광범위한 하향조절**을 특징으로 하며, 임상적으로 더 심한 비대·나쁜 예후를 보인다. 저자들은 rare functional variant enrichment, GWAS common variant, pQTL의 세 가지 유전 증거로 **FAO 감소가 HCM 병태생리의 인과 요인**임을 입증했고, 이 대사 signature를 독립 심근·hiPSC-CM 코호트에서 검증했다. 마지막으로 in silico 도킹으로 **baicalin(황금 유래 천연물, CPT1 작용제)**을 FAO 촉진제로 선별해, severe-subtype hiPSC-CM과 Myh6^R404Q/+ HCM 마우스에서 대사·비대 표현형을 개선함을 보였다 — 즉 **아형 특이(subtype-specific) 정밀치료** 전략을 제시했다.

## Key Points

- **코호트 구조**: Discovery 132명 폐쇄성(obstructive) HCM 심근(46.2% male, 50.9±12.0y, myectomy). Validation 1 = 별도 폐쇄성 HCM 48명 심근(proteomic, QE HF-X). Validation 2 = HCM hiPSC-CM 23 라인(TIMSTOF). + 정상 대조 심장조직 10개(explanted healthy donor). 3개 multi-omics = WES + RNA-seq + DIA proteomics.
- **분자 스케일**: WES 718,240 SNV + 167,399 indel → 3,791 rare functional variant. RNA 12,879 expressed gene(82 specimen). Proteome **2,827 정량 단백**(>75% 샘플 존재). 
- **유전자형은 예후를 못 가른다**: 14개 HCM-병인 유전자에서 P/LP variant 46/132명(34.8%). MYH7(변이양성의 41.3%, missense 89.5%) + MYBPC3(37.0%, truncating 88.2%) 우세; 추가 FLNC/TNNT2/MYL2/TPM1/FHOD3/CSRP3. 그러나 mutation 유무·개별 유전자(MYBPC3/MYH7)는 MACE 예후와 무관(P=0.69/0.68/0.36). PCA에서도 mutation-based 군은 겹침.
- **2개 단백체 아형 severe(S, n=101) / mild(M, n=31)**: NMF 비지도 클러스터링. **오직 proteomic 하위군만 예후 유의차**(P=0.038; RNA 하위군은 P=0.84). MACE 6.5%(Pro1/mild) vs 23.8%(Pro2/severe). Severe = 낮은 LVEF, 두꺼운 IVSd, 높은 LVOTG·LVMI → 임상적으로 더 심한 비대·나쁜 예후로 "severe"로 명명.
- **550 signature 단백**(severe feature 397 + mild feature 153). Severe 특이: **FAO + OXPHOS 하향**(adjusted P<0.01), EMT·complement·apoptosis·hypoxia 상향(HF·중증도 반영). 중요한 점 — FAO/OXPHOS 감소는 **HCM 전반이 아니라 severe 아형에 국한**(mild는 HC와 차이 없음).
- **FAO 축**: FA metabolism 유전자 22/28이 FAO+TCA와 연관. 핵심 효소 ACADS·ACAT1·CRAT·ECH1·ECHS1·HADH·HADHB가 severe에서 유의 감소. WGCNA 7 모듈 중 **turquoise(OXPHOS/FA metabolism)** 는 IVSd·LVOTG·LVMI와 음상관·severe에서 하향, **blue(complement/coagulation/ECM/cytoskeleton)** 는 양상관. 모듈은 외부 코호트(Maike 2021 / Ramin 2023)에서 preservation Z>10로 재현.
- **독립 검증**: Validation 1(48명) severe 아형 예후 나쁨(P=0.022), 두꺼운 IVSd·높은 LVOTG·LVMI. 다변량 Cox에서 **proteomic subtype = 독립 예후인자 HR 3.24(95% CI 1.08–9.69, P=0.036)**. 63 FAO + 134 OXPHOS core 단백 중 50개 signature 일관; 6개 Western blot 검증(FAO: SLC25A20/ACADVL/ECH1, OXPHOS: NDUFB6/UQCRH/ATP5F1A) — HC→mild→severe 점진적 감소.
- **hiPSC-CM 검증**: HC 9 + 폐쇄성 HCM 4 + 비폐쇄성 HCM 19 → 23 라인을 severe-concordant 12 / mild 11로 층화. Severe hiPSC-CM = 더 큰 세포, hypertrophy marker(MYH7/MYH6/NPPA/NPPB)↑, 수축력↑·이완속도↓, 5개 대사단백(UQCRH/SLC25A20/ECH1/NDUFB6/ATP5F1A) 점진 감소.
- **FAO 인과성(3중 유전 증거)**: (1) rare functional variant — 2,928 유전자 enrichment에서 FA metabolism 유의; 63 FAO 유전자 중 21개(33.3%)가 rare variant 보유, severe 21.8% vs mild 12.9%. (2) GWAS common variant(GCST90018861/90296069/90436069) FA metabolism 일관 enrich. (3) **pQTL** — HCM vs control MAF 차이 pQTL 392개 중 **343개(87.5%)가 target 발현과 음상관(beta<1)·HCM과 양상관(OR>1)** → FAO 감소가 인과.
- **Baicalin = FAO 촉진 치료제**: CPT1(FAO 율속효소, CPT1A/B)을 표적. TCM 라이브러리(HY-L163) in silico 도킹 → FDA 승인 공유 3종(deserpidine/hesperidin/baicalin). **SPR에서 baicalin이 최저 KD(CPT1A 1.84×10⁻⁶ M) = 최강 결합**. Severe hiPSC-CM에서 baicalin(100μM): FAO 효소↑, 세포면적↓, 비대유전자↓, 수축능 개선; 효과는 severe(6.4%)>mild(3.9%)로 아형 특이, P/LP 변이 배경과 무관.
- **In vivo(Myh6^R404Q/+ = 인간 MYH7 p.R403Q)**: baicalin 200 mg/kg/day 8주 → acylcarnitine·acylCoA↑(CPT1 활성; long-chain >C12 CPT1 의존), R404Q에서 하향된 1,728 단백 중 >1,300이 WT 방향 복원(top 15 pathway = FA 대사). Serial echo·cardiac MRI: 비대 진행 억제(8주 최대 효과), LVPWd·IVSd·전벽 감소, cardiomyocyte 단면적 감소.

## Data & Code Availability
- Exome(WES) 원자료는 **중국 인간유전자원 규정으로 공개 불가**; 단백 abundance/expression matrix는 Supplemental Material 제공. Raw data는 저자 요청·IRB 승인·data access agreement 하에 제공.
- Registration: ClinicalTrials.gov **NCT03076580**. GWAS 대조: GCST90018861 / GCST90296069 / GCST90436069; pQTL 대조 ChinaMap.

## 방법론 활용 가능성 (사용자 multiomics 파이프라인 관점)
- **"proteome-based subtype이 genotype보다 예후를 잘 가른다"** 는 핵심 교훈: mutation-based 층화(MYH7/MYBPC3)는 예후 무관, NMF proteomic 아형만 독립 예후인자(HR 3.24). 사용자의 코호트에서도 유전형 분류 vs 단백체 분류의 예후 분별력을 나란히 비교하는 프레임으로 직접 이식 가능.
- **인과성 삼각검증 템플릿**: rare variant enrichment + GWAS common variant + **pQTL(exome×proteome)** 세 축으로 "대사 경로 하향이 원인인가 결과인가"를 논증하는 설계는, 단백체 signature를 단순 상관에서 인과 주장으로 끌어올리는 재사용 가능한 논리 사다리.
- **signature → target → 검증** 파이프라인: 550 signature → FAO/OXPHOS 축 → CPT1 표적 → in silico 도킹 + SPR 친화도 → hiPSC-CM + 마우스 표현형 검증(baicalin). Cancer 과제의 표적 발굴·약물 repurposing 워크플로우와 구조가 동일.
- **주의/한계**: 폐쇄성 HCM 심근(myectomy) 중심 단일기관 코호트, WES 원자료 비공개, baicalin은 아형 특이 효과지만 임상 검증 전 단계. 암 corpus와 생물학은 무관하므로 결론(FAO/baicalin)을 암 맥락으로 전이하지 말 것.

## Connections
- [Multiomics Proteomics PTM Identification](../topics/multiomics-proteomics-ptm-identification.md)
- [[chu-2026-integrated-proteogenomic-metabolomic-profiling-aml-subtypes|Chu 2026 (CPTAC AML — proteogenomic subtyping + metabolic axis + target validation, 방법론 유사)]]
- [[anurag-2022-proteogenomic-markers-chemotherapy-resistance-response|Anurag 2022 (proteome이 mutation보다 예후/반응을 설명하는 사례)]]

## Sources
- Local PDF: `raw/inbox/papers/ma-2026-proteogenomics-hypertrophic-cardiomyopathy-subtype-specific-therapy.pdf`
- DOI: <https://doi.org/10.1161/CIRCRESAHA.126.328300>
