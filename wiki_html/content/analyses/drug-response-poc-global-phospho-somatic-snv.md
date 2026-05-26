---
title: Drug Response Proof-of-Concept with Global Proteome, Phosphoproteome, and Somatic SNV
tags:
  - analysis-plan
  - drug-response
  - proteogenomics
  - phosphoproteomics
  - somatic-snv
  - cancer-multiomics
---

# Drug Response Proof-of-Concept with Global Proteome, Phosphoproteome, and Somatic SNV

항암제 반응성 논문을 쓰기 전에, 보유한 global proteome, phosphoproteome, somatic SNV 데이터를 이용해 “유전체 단독보다 단백체/인산화 신호가 반응성 해석을 얼마나 보강하는가”를 검증하기 위한 proof-of-concept 분석 흐름.

## Key Points

- 핵심 질문은 **somatic SNV/driver alteration만으로 설명되지 않는 반응성 차이를 global proteome과 phosphoproteome/kinase activity가 추가 설명하는가**이다.
- 첫 POC는 큰 모델보다 작은 비교가 좋다: `clinical + SNV baseline` → `+ global proteome` → `+ phospho/kinase`의 incremental value를 보여준다.
- Phosphoproteome은 raw site abundance만 쓰지 말고, 가능하면 **protein abundance correction / modification:protein ratio / kinase activity inference**를 함께 비교해야 한다.
- 논문 흐름은 예측 성능보다 해석 가능성이 먼저다: 반응성 예측 lift가 작아도 특정 signaling axis가 치료 기전과 맞으면 manuscript POC가 된다.
- 외부 검증이 어렵다면, strict cross-validation, permutation label test, block-wise feature importance, case-level molecular vignette로 과적합 위험을 줄인다.

## Recommended POC Question

> Given matched global proteome, phosphoproteome, and somatic SNV data, can phosphoproteomic signaling explain anticancer drug response beyond somatic mutation status and global protein abundance?

한국어로는 다음 문장으로 잡으면 좋다.

> “동일 환자/샘플에서 somatic SNV, global proteome, phosphoproteome을 통합했을 때, phospho-derived pathway/kinase activity가 항암제 반응성의 독립적인 설명층으로 작동하는지 검증한다.”

## Analysis Flow

### 1. Endpoint and Cohort Freeze

- 반응성 endpoint를 먼저 고정한다: pCR/non-pCR, RECIST responder/non-responder, RCB, PFS/OS, drug sensitivity AUC/IC50 중 하나.
- 치료제를 하나로 묶을 수 있는지 확인한다. Regimen이 섞여 있으면 `drug class`, `line`, `combination`, `prior treatment`를 covariate로 둔다.
- 최소 metadata: cancer type, treatment, endpoint, sampling time(pre-treatment / on-treatment / post-treatment), tumor purity, batch/TMT plex, missingness.
- POC의 첫 버전은 binary endpoint가 가장 명확하다. Lee 2026 TNBC, Anurag 2022 TNBC, Sambath 2026 cervical cancer, Zhang 2023 ccRCC가 모두 response-labeled 구조를 사용한다.

### 2. Feature Blocks

**Clinical / technical block**

- age, stage, subtype, treatment regimen, batch, tumor purity, sample type.
- batch와 purity는 model input 또는 sensitivity analysis에 반드시 포함한다.

**Somatic SNV block**

- Driver mutation presence: TP53, PIK3CA, KRAS, EGFR, STK11, KEAP1 등 암종/치료제 관련 유전자.
- Pathway-level mutation burden: PI3K/AKT, MAPK, DNA damage repair, chromatin remodeling, antigen presentation.
- TMB 또는 nonsynonymous mutation count.
- Mutational signature가 가능하면 APOBEC, HRD/MMR, smoking-like 등 treatment-relevant signature를 별도 feature로 둔다.
- SNV만 있으면 CNA/SV-driven resistance를 놓칠 수 있다. Sambath 2026과 Zhang 2023은 EGFR amplification, STK11 SV deletion, 7q gain 같은 copy-number/structural layer가 반응성 해석에 중요했다. CNA가 없다면 “SNV-only genomics”로 명시한다.

**Global proteome block**

- Pathway scores: Hallmark, Reactome, KEGG, DNA repair, cell cycle, EMT, immune/IFN, metabolism, angiogenesis.
- Drug target / pathway protein abundance: EGFR, ERBB2, AURKB, PRKDC, mTOR pathway proteins, DNA repair proteins.
- Protein subtype: NMF/consensus clustering 또는 published subtype classifier projection.
- Lee 2026처럼 IHC negative라도 estrogen response protein signature가 non-pCR과 연결될 수 있으므로, transcript/IHC status와 protein pathway status를 분리한다.

**Phosphoproteome block**

- Site-level differential signal: responder vs non-responder phosphosite comparison.
- Protein-aware signal: phosphosite / matched protein ratio, residual-based correction, 또는 MSstatsPTM-like modeling.
- Kinase / pathway activity: KSEA, PTM-SEA, Kinase Library, NetworKIN, CoPheeKSA 중 데이터 규모에 맞게 선택.
- Substrate coverage and caveat: kinase substrate 수가 적은 kinase는 별도 flag를 둔다.
- PTM correction sensitivity: raw phosphosite score와 corrected phosphosite score가 같은 결론인지 비교한다. ptmanchor/Q3 synthesis는 correction이 kinase call을 바꿀 수 있음을 보여주는 근거로 사용한다.

### 3. Model Ladder

첫 POC는 복잡한 multi-omics deep learning보다 아래 4단계가 더 논문 설득력이 좋다.

| Model | Inputs | Question |
|---|---|---|
| M0 | clinical + batch/purity | 임상/기술 요인만으로 얼마나 설명되는가? |
| M1 | M0 + somatic SNV/pathway | 유전체 alteration이 반응성을 설명하는가? |
| M2 | M1 + global proteome pathway/subtype | 단백질 발현층이 추가 설명력을 주는가? |
| M3 | M2 + phospho/kinase activity | signaling activity가 독립적인 lift를 주는가? |

권장 모델:

- 표본 수가 작으면 elastic net logistic regression, Firth logistic regression, random forest는 보조로만.
- 표본 수가 매우 작으면 leave-one-out 또는 repeated stratified k-fold, 그리고 permutation label test를 같이 보고한다.
- feature selection은 training fold 안에서만 수행한다. 전체 데이터에서 top feature를 고른 뒤 CV를 돌리면 leakage다.
- 성능 지표는 AUROC 하나만 쓰지 말고 AUPRC, balanced accuracy, calibration, confidence interval을 함께 둔다.
- 주요 질문은 `M3 - M1` 또는 `M3 - M2`의 incremental gain이다.

### 4. Biology-First Interpretation

모델 결과는 다음 순서로 해석한다.

1. Response-associated SNV/pathway alteration이 있는가?
2. 같은 pathway가 global protein abundance에서도 움직이는가?
3. 같은 pathway가 phosphosite/kinase activity에서 더 선명해지는가?
4. phospho signal이 protein abundance 증가만 반영하는가, protein-corrected 후에도 남는가?
5. drug target 또는 resistance bypass pathway와 연결되는가?
6. cell line, PDO, PDX, public perturbation dataset으로 검증 가능한가?

### 5. Minimal Figures for POC

- Figure 1: cohort and data matrix. Samples × layers × response label × missingness.
- Figure 2: model ladder. M0/M1/M2/M3 performance and block-wise feature contribution.
- Figure 3: pathway/kinase map. Response-associated global protein pathway vs phospho-derived kinase activity.
- Figure 4: selected mechanism. 예: DNA repair hyperactivation, mTOR/7q, AURKB, GRK2, PRKDC, angiogenesis subtype.
- Figure 5: patient-level vignettes. Responder/non-responder 2–4명에서 SNV + protein + phospho가 어떻게 서로 맞거나 어긋나는지 보여준다.

## Existing Local-Paper Templates to Follow

### Lee 2026 TNBC

- 구조: WES + RNA-seq + TMT global proteome + phosphoproteome, pCR/non-pCR, pre/post residual tumor.
- 따라할 점: resistance factors를 pathway/signaling/target 후보로 압축한 뒤 logistic regression으로 통합.
- 특히 좋은 POC 포인트: estrogen protein signature + GRK2 PTM-SEA, ITGB8/7p21 copy gain, AKR1C2/ABCA13, post-treatment AURKB phosphoproteome.
- 주의: AUC 0.946은 same-cohort 모델이므로 외부 검증 전 과장하면 안 된다.

### Anurag 2022 TNBC

- 구조: pretreatment biopsy에서 WES/RNA/proteome/phosphoproteome을 pCR/RCB와 연결.
- 따라할 점: carboplatin/docetaxel 반응성에서 DNA repair, immune/IFN, cell-cycle, phosphoproteome signal을 병렬로 본다.
- POC에 유용한 포인트: response label을 고정한 뒤 `clinical/purity` → `SNV/signature` → `global proteome pathway` → `phosphosite/PTM-SEA kinase` 순서로 incremental model을 세우는 구조를 거의 그대로 따라할 수 있다.
- 특히 중요한 caveat: 이 논문의 강한 resistance marker는 point mutation이 아니라 19q13.31-33 copy-number loss(LIG1/POLD1/XRCC1)였다. 사용자의 데이터가 somatic SNV-only라면, SNV block의 한계를 명시하고 proteome/phosphoproteome이 SNV-only 모델의 빈틈을 보강하는지를 핵심 질문으로 삼는 편이 좋다.
- 따라할 feature 예시: proteome-level OXPHOS/fatty-acid/adipogenesis scores, immune/IFN score, PD-L1 protein/phosphoprotein, G2-M/E2F/DNA-repair scores, PTM-SEA kinase targets(CDK1/2/7, CDC7, PRKDC, MARK2), mutation burden/signature proxies.

### Zhang 2023 ccRCC Sunitinib

- 구조: therapy-specific response cohort에서 proteome/phosphoproteome이 response classifier와 mechanism을 만든다.
- 따라할 점: chromosome 7q gain과 mTOR pathway activation을 non-response program으로 연결하고 multi-omics classifier로 확장.
- POC에 유용한 포인트: TKI 반응성에서는 phosphoproteome/kinase pathway가 특히 직접적인 해석층이다.
- full-read 보강 후 핵심 lesson: drug target RTK abundance/activity 자체는 responder/non-responder를 가르지 못했지만, KSEA/ssGSEA의 MTOR/MAP2K1/CDK 축과 proteome pathway/TME 상태가 반응성을 설명했다.
- 사용자의 POC에 적용: targeted therapy 데이터라면 drug target protein만 보는 figure보다 `target abundance vs kinase pathway activity vs response`를 나란히 비교하는 figure가 더 설득력 있다.
- 모델 feature 예시: LDH/PLT/tumor size, VHL/KMT2C mutation, mutational signature, CNA 3p/7q, mTOR/MAPK/CDK kinase score, platelet/coagulation/TGFB1/T-cell proteome features.

### Ji 2023 LICOB Liver Cancer Organoids

- 구조: patient-derived liver cancer organoid biobank에서 WES/CNV/RRBS/RNA/DIA proteome, 76-drug screen, elastic-net drug-response prediction, combination validation을 연결한다.
- 따라할 점: baseline multiomics로 drug AUC를 예측한 뒤, 예측된 combination을 실제 organoid/PDX와 6시간 perturbation phosphoproteomics로 검증한다.
- POC에 유용한 포인트: “유전체/SNV만으로 반응성을 설명하기 어렵고, proteome/phosphoproteome/pathway state가 pharmacologic response를 더 직접적으로 설명한다”는 논문 spine에 맞다.
- 특히 좋은 POC 포인트: lenvatinib resistance는 EGFR-TKI resistance feature, KRT19/NDN mRNA, thromboxane pathway, ADH1C/CES1/VEGF-pathway protein abundance와 연결되었고, temsirolimus 병합은 23,754 phosphosite perturbation profiling으로 bypass signaling 억제를 보여줬다.
- 사용자의 POC에 적용: 임상 반응 endpoint만 있다면 M0/M1/M2/M3 model ladder를 먼저 만들고, 가능하면 소수 샘플/모델에서 drug perturbation phosphoproteomics나 ex vivo assay로 top pathway를 확인하는 방식이 가장 설득력 있다.
- 주의: LICOB는 SNV뿐 아니라 CNV, methylation, RNA, proteome, phosphoproteome, drug-screen phenotype을 쓴다. 사용자 데이터가 somatic SNV-only라면 CNA/SV/methylation 부재를 limitation이 아니라 “proteome/phosphoproteome이 SNV-only의 빈틈을 보강하는가”라는 질문으로 전환하는 편이 좋다.

### Holt 2025 MIBC Chemoresistance

- 구조: cisplatin-based NAC를 받은 muscle-invasive bladder cancer에서 WES/RNA/TMT proteome/phosphoproteome을 chemotherapy-sensitive/resistant 상태와 연결한다.
- 따라할 점: DDR mutation status만으로 반응성이 안 잡힐 때, DNA-repair/G2M protein pathway와 phosphosite activity가 기능적 response state를 드러내는지 비교한다.
- POC에 유용한 포인트: somatic DDR gene mutation은 chemoresistance와 유의하게 연결되지 않았지만, sensitive tumor에서는 protein-level DNA repair/G2M hallmark가 보였고 resistant tumor에서는 EMT/WNT/KRAS/hypoxia/apoptosis 및 GSK3B activity 축이 나타났다.
- 특히 좋은 POC 포인트: GSK3B-S9 phosphosite는 total GSK3B protein 변화 없이 response와 연결되므로, `protein abundance correction 후에도 남는 phosphosite activity` 예시로 쓰기 좋다.
- 사용자의 POC에 적용: Figure 하나를 `DDR/SNV alteration -> DNA repair protein score -> GSK3B/RAF phosphosite or kinase score -> response` 순서로 만들면 SNV-only 모델의 빈틈과 phosphoproteome의 독립 가치를 명확히 보여줄 수 있다.
- 주의: main pretreatment n이 작고 bulk MIBC는 muscle/stromal contamination caveat가 크므로, purity/subtype adjustment와 permutation 또는 nested CV가 필수다.

### Jaehnig 2025 CALGB 40601 HER2+ Breast Cancer

- 구조: randomized neoadjuvant anti-HER2 trial의 pretreatment biopsy에서 WES/RNA/TMT proteome/phosphoproteome을 pCR/non-pCR와 연결한다.
- 따라할 점: clinical target status를 그대로 믿지 말고, ERBB2 copy number, HER2 RNA, HER2 protein, HER2 phosphosite/activation proxy가 실제로 맞는지 먼저 QC한다.
- POC에 유용한 포인트: 임상적으로 HER2+였지만 proteogenomic ERBB2/HER2 evidence가 약한 false-positive 후보가 non-pCR에 몰렸고, 이후 confirmed HER2+ 안에서는 EMT/ECM/WNT/TGF-beta/PRKD/GSK3 계열 resistance state와 immune/cell-cycle pCR state가 갈렸다.
- 특히 좋은 POC 포인트: GPRC5A와 TPBG는 3개 proteomic dataset과 10개 RNA neoadjuvant anti-HER2 regimen meta-analysis에서 non-pCR와 재현성 있게 연결된 membrane-associated resistance markers다.
- 사용자의 POC에 적용: targeted therapy라면 `drug target genomic status -> target protein abundance -> target phospho/activation -> bypass pathway/immune state`를 하나의 QC+biology ladder로 두는 것이 좋다.
- 주의: phospho-derived kinase signature는 treatment arm별 sample size가 작으므로 discovery로 두고, GPRC5A/TPBG 같은 cross-cohort marker는 validation tier로 분리한다.

### Krug 2020 CPTAC Breast Cancer

- 구조: PTM 보존 프로토콜로 수집한 treatment-naive breast cancer 122 tumors에서 WES/RNA/TMT proteome/phosphoproteome/acetylome을 통합해 HER2, immune, Rb/CDK4/6, kinase vulnerability를 재해석한다.
- 따라할 점: 임상 receptor/genomic status를 그대로 feature로 쓰기 전에, target protein과 phosphosite activation으로 functional target status를 다시 정의한다.
- POC에 유용한 포인트: ERBB2 amplification이 있어도 ERBB2 protein이 낮은 pseudo-ERBB2+ 사례가 있었고, 일부는 TOP2A amplification/protein overexpression이 대체 amplicon driver처럼 보였다.
- CDK4/6 포인트: RB1 mutation/deletion은 중요한 exclusion feature지만 충분하지 않다. TNBC에서 RB1 wild-type이어도 Rb protein loss가 있으면 palbociclib response가 낮았고, Rb protein abundance가 response와 상관됐다.
- phospho 포인트: HR+/ERBB2-에서는 phospho-Rb가 proliferation과 total Rb보다 더 강하게 맞았고, TNBC에서는 phospho-Rb-high subgroup의 CDK4/6 activity가 높았다. 즉 `RB1 genotype -> Rb protein -> phospho-Rb -> CDK4/6 PTM-SEA -> response` ladder가 좋다.
- 면역/내성 적용: luminal tumor에서도 APOBEC, low SSBR/NER protein scores, PD-L1/immune-modulator protein signatures가 immune-active state와 연결되어, 면역치료 후보군을 TNBC로만 제한하지 않는 feature block을 설계할 수 있다.
- 주의: 치료 전 atlas라 직접 response model은 아니지만, HER2와 CDK4/6처럼 임상 target이 명확한 축에서는 사용자 데이터의 response-label POC에 바로 가져갈 수 있는 QC/feature blueprint다.

### Song 2024 Korean NSCLC Multiomics

- 구조: Korean NSCLC surgical cohort 229명에서 WES/RNA/TMT proteome/phosphoproteome/acetylome으로 five-subtype map을 만들고, immune landscape와 adjuvant therapy survival benefit을 연결한다.
- 따라할 점: response label이 직접적인 drug AUC가 아니어도, subtype x adjuvant treatment interaction을 통해 치료 benefit이 어느 molecular state에 집중되는지 볼 수 있다.
- POC에 유용한 포인트: subtype feature의 80%(911/1,134)가 phosphoproteome에서 왔다. 즉 phosphoproteome이 단순 annotation이 아니라 sample stratification의 주도층이 될 수 있음을 보여준다.
- 특히 좋은 POC 포인트: Subtype 4는 PI3K-Akt/hypoxia/CSNK2A1/GSK3B 및 SLK S347/LRRFIP1 S581 phosphosite로 poor-prognosis/metastatic biology를 설명했고, Subtype 5는 immune-hot/APM/TIL 상태에서 adjuvant chemotherapy 또는 chemoradiation benefit이 커졌다.
- 사용자의 POC에 적용: 치료제 반응성이 이분형 endpoint가 아니라 RFS/OS라면, `SNV-defined group`보다 `phospho/proteome-defined subtype + treatment` interaction을 우선 시험해볼 만하다.
- 주의: adjuvant therapy 분석은 retrospective이며 subtype 안에서 randomized된 것이 아니므로, stage/nodal status/histology/treatment selection adjustment가 필수다.

### Satpathy 2021 LSCC

- 구조: CPTAC LSCC 108 tumors/99 NAT에서 WGS/WES/CNA/methylation/RNA/TMT proteome/phosphoproteome/acetylome 및 K-GG subset을 통합해 치료 취약성 가설을 만든다.
- 따라할 점: mutation/amplification 하나로 drug target을 확정하지 않고, target protein, ligand, downstream phosphosite, subtype, immune state를 단계적으로 확인한다.
- POC에 유용한 포인트: FGFR1-amplified LSCC에서 NSD3가 더 그럴듯한 driver로 올라오고, CDKN2A/CCND1/RB1 상태보다 phospho-Rb가 CDK4/6 inhibitor sensitivity와 더 직접적으로 연결된다.
- 특히 좋은 POC 포인트: EGFR amplification은 EGFR pathway activity와 잘 맞지 않았고, EGFR ligand abundance가 activity와 더 잘 맞았다. targeted therapy 데이터라면 `target alteration -> target protein -> ligand/bypass protein -> phospho/kinase activity -> response` QC ladder를 넣는 것이 좋다.
- 면역/내성 적용: Hot/Warm/Cold immune state, checkpoint/IDO1/FOXP3 abundance, CSF1R CBPE, Wnt signaling, SOX2-high/JAK-STAT-low 관계를 immune evasion/resistance feature block으로 둘 수 있다.
- 주의: 치료 전 primary tumor atlas라 직접 response cohort는 아니다. 따라서 이 논문은 classifier 성능 근거가 아니라 feature design과 mechanistic vignette의 blueprint로 쓰는 편이 맞다.

### Sambath 2026 Cervical Cancer CCRT

- 구조: WGS/WES + TMT proteome + 동일 코호트 phosphoproteome + IHC validation.
- 따라할 점: DNA repair pathway hyperactivation을 genomic alteration, proteome upregulation, phosphorylation activation으로 수렴시킨다.
- POC에 유용한 포인트: EGFR amplification, STK11 SV deletion, STX3 protein/IHC, CSNK2A1/SMC1A phosphorylation 같은 cross-layer convergence.
- 주의: proteome discovery n=10이라, discovery 후 validation layer를 따로 두는 방식이 중요하다.

### Xu 2026 HER2-Low Breast Cancer

- 구조: WES + RNA + global proteome + phosphoproteome + lactylome, subtype classifier, PDO/RWD drug response.
- 따라할 점: proteomic subtype을 치료 가설로 연결하고 PDO/RWD로 약물 반응성을 보강.
- POC에 유용한 포인트: PS1 estrogen, PS2 angiogenesis, PS3 HER2-high-like; PRKDC lactylation/kinase activity; JNK phospho signaling.

### Zhao 2025 CRC Kinase-Inhibitor Perturbation

- 구조: cell-line kinase inhibitor perturbation에서 proteome/phosphoproteome/acetylome의 drug-specific molecular response를 해석.
- 따라할 점: 환자 코호트에서 발견한 kinase/pathway 후보를 perturbation 방향성으로 점검할 때 사용.
- full-read 보강 후 핵심 lesson: lapatinib은 기대한 ERBB2 억제와 함께 CDK4 활성화를 보였고, PIK-93/refametinib/AS-605240도 nominal target 외 kinase activity 변화를 만들었다. 즉 phosphoproteomics는 target engagement와 bypass/off-target reprogramming을 동시에 확인하는 실험층이다.
- 사용자의 POC에 적용: 환자 데이터에서 top kinase axis가 나오면, 바로 “예측 모델 feature”라고 주장하기보다 관련 inhibitor perturbation에서 target suppression, compensatory kinase activation, mitochondrial/metabolic proteome shift, PTM crosstalk을 확인하는 validation figure로 이어간다.
- 주의: 환자 cohort가 아니라 HCT116 perturbation이므로 prediction model training reference가 아니라 mechanistic validation reference로 둔다. 12시간/1 uM 단일 조건이라 dose-time generalization은 제한적이다.

### Chmielecki 2023 FLAURA Osimertinib Resistance

- 구조: EGFR-mutant advanced NSCLC FLAURA phase III trial의 first-line osimertinib vs comparator EGFR-TKI에서 paired plasma ctDNA와 baseline tissue NGS로 acquired/baseline resistance를 분석.
- 따라할 점: targeted therapy에서도 “driver mutation presence”만으로 반응/내성 해석이 끝나지 않는다는 점을 먼저 수치화한다.
- POC에 유용한 포인트: osimertinib-arm acquired-resistance subset에서 38/109(35%)만 plasma ctDNA 후보 mechanism이 있었고 71/109(65%)는 detectable candidate mechanism이 없었다. MET amplification 16%, EGFR C797S 6%, T790M 0%라는 명확한 genomic escape pattern도 있지만, 더 큰 메시지는 unexplained resistance fraction이다.
- 사용자의 POC에 적용: somatic SNV block으로 설명 가능한 샘플과 설명되지 않는 샘플을 먼저 분리하고, unexplained fraction에서 global proteome/phosphoproteome/kinase activity가 resistance state를 설명하는지 검정한다.
- 주의: 이 논문은 global proteome/phosphoproteome 논문이 아니라 ctDNA/tissue NGS resistance context다. 따라서 core training template이 아니라 SNV-only limitation과 non-genetic layer 필요성을 정당화하는 근거로 둔다.

### Gillette 2020 CPTAC LUAD

- 구조: treatment-naive LUAD 110 tumors + 101 matched NAT에서 WES/WGS/RNA/miRNA/methylation/global proteome/phosphoproteome/acetylome을 통합한 CPTAC atlas.
- 따라할 점: driver mutation을 endpoint처럼 쓰지 말고, mutation이 protein/PTM 기능 상태로 번역되는지 확인한다. 특히 `EGFR mutation -> PTPN11 Y62 phosphorylation`, `KRAS mutation -> SOS1 S1161 phosphorylation`, `ALK fusion -> ALK Y1507 phosphorylation`처럼 phosphosite가 RNA/protein보다 더 직접적인 vulnerability가 될 수 있다.
- POC에 유용한 포인트: EGFR-mutant tumors에서 PTPN11/Shp2 Y62 phosphorylation은 RNA/protein 변화 없이 보였고, SHP2 inhibitor target population 가설로 이어졌다. 이것은 사용자의 POC에서 “phospho layer가 SNV + global protein block 이후 독립 신호를 주는가”를 보여줄 대표 figure 구조다.
- 또 하나의 포인트: STK11-mutant LUAD의 immune-cold state는 neutrophil degranulation proteome program으로 잡혔고 RNA에서는 잘 보이지 않았다. 즉 global proteome layer가 SNV와 RNA 사이의 기능적 면역/내성 상태를 보강할 수 있다.
- 사용자의 POC에 적용: EGFR/KRAS/STK11/KEAP1/TP53 같은 driver block별로 `mutation status -> target/bypass protein abundance -> phosphosite or kinase outlier -> response`를 ladder로 만들고, protein-corrected phosphosite signal이 유지되는지 반드시 확인한다.
- 주의: treatment-response cohort가 아니므로 예측 모델의 학습 템플릿이라기보다 driver-to-signaling/vulnerability nomination 템플릿으로 둔다.

### Chen 2020 East Asian Never-Smoker LUAD

- 구조: Taiwanese treatment-naive early-stage LUAD에서 WES/RNA/global proteome/phosphoproteome을 tumor/NAT paired design으로 통합한다.
- 따라할 점: EGFR mutation status를 하나로 묶지 말고 L858R, Del19, TP53 co-mutation, KRAS WT/Mut, MAPK phosphosite activity를 분리한다.
- POC에 유용한 포인트: EGFR activating mutation은 total EGFR abundance보다 EGFR S1064/Y1197 phosphorylation 및 EGFR-MEK-ERK phosphosite chain으로 더 직접적으로 해석된다.
- 특히 좋은 figure 구조: `EGFR/KRAS/TP53 mutation -> EGFR pY1197/MAP2K2 pT394/MAPK3 pT198-T202 -> MAPK activity rank -> stage/progression or response`.
- TP53 포인트: TP53 mutation은 TOP2A/MCM/cell-cycle protein abundance와 ABRAXAS1 S406/UIMC1 S101 같은 DNA-damage phosphosite state에 연결되어, DNA-damage/topoisomerase therapeutic hypothesis를 만든다.
- APOBEC/면역 포인트: APOBEC-high young female EGFR-WT subgroup과 CDK1/CDK2/AurB/CK2 kinase signals는 immunotherapy 혹은 cell-cycle targeting branch의 후보 feature로 둘 수 있다. 다만 immunotherapy association은 외부 advanced NSCLC cohort에서 marginal PFS signal이라 supporting tier로 둔다.
- 주의: 직접 drug-response cohort가 아니므로 EGFR-L858R vs Del19 and proteomic late-like class는 outcome/risk stratification template이고, predictive drug-response claim은 사용자 데이터에서 별도로 검증해야 한다.

### Huang 2021 HPV-Negative HNSCC

- 구조: HPV-negative HNSCC 108 tumors에서 WES/WGS/RNA/miRNA/methylation/global proteome/phosphoproteome을 통합해 CDK4/6 inhibitor, EGFR mAb, immunotherapy 후보군을 제안.
- 따라할 점: genomic alteration이 pathway activity를 충분히 설명하는지 항상 phosphoproteome으로 검증한다. CDKN2A/CCND1 altered samples 중에도 Rb phosphosite score가 낮은 샘플이 있었고, PDX abemaciclib response는 CCND1/CDKN2A보다 phospho-Rb S807/811과 더 맞았다.
- POC에 유용한 포인트: EGFR에서는 receptor amplification/protein abundance가 아니라 AREG/TGFA/EREG/EPGN/HBEGF ligand abundance와 downstream phosphosite cascade가 EGFR pathway activity 및 cetuximab/panitumumab response signal과 더 잘 맞았다.
- 면역 쪽 포인트: immune-cold tumors는 antigen source 부족이 아니라 IFNGR2/JAK2/IRF1 같은 immune regulator copy-number deletion과 APM failure로 설명했고, immune-hot tumors는 multiple checkpoint/suppressor co-upregulation 때문에 PD-1 단독보다 combination checkpoint profiling이 필요하다고 해석했다.
- 사용자의 POC에 적용: `SNV/CNA alteration -> protein target abundance -> phosphosite pathway activity -> response-supporting external evidence`를 한 축으로 만들고, 특히 CDK4/6-Rb와 EGFR ligand/receptor discordance를 case-level vignette로 보여주면 좋다.
- 주의: treatment-naive atlas 기반 treatment hypothesis라 prospective response validation은 아니며, 외부 PDX/trial reanalysis는 supporting evidence로 분리해야 한다.

### Petralia 2024 Pan-Cancer Tumor Immunity

- 구조: CPTAC 10개 암종 treatment-naive 1,056 tumors에서 WGS/RNA/DNA methylation/global proteome/phosphoproteome/H&E를 통합해 tumor immunity와 immune-evasion subtype을 정의한다.
- 따라할 점: 면역치료 반응성 POC에서는 단순 TMB/SNV나 immune score 하나가 아니라, `cell composition + IFNG/pathway activity + DNA alteration + phospho-kinase activity`를 분리해서 본다.
- POC에 유용한 포인트: `CD8+/IFNG+` subtype은 OAK NSCLC atezolizumab arm에서 PFS benefit과 연결되었지만 docetaxel arm에서는 연결되지 않았다. 즉 immune subtype은 generic prognosis가 아니라 treatment-class-specific feature로 다뤄야 한다.
- 특히 좋은 POC 포인트: `CD8-/IFNG+` subtype은 IFNG signaling은 강하지만 CD8/B-cell infiltration은 낮아, bulk pathway activity와 실제 immune-cell access가 어긋날 수 있음을 보여준다.
- phospho 쪽 포인트: immune-hot state는 MAPKAPK/IKK-beta/TBK1 및 LYN/HCK/Src-family kinase signals와 연결되고, cold/proliferative state는 CDK1/CDK2/CDK1-6 activation과 연결된다. PTK2/FAK는 hot tumor-cell compartment에서 높아 LSCC 쪽 immunotherapy-combination hypothesis로 제시된다.
- 사용자의 POC에 적용: immunotherapy 또는 immune-evasion endpoint가 있다면 `STK11/KEAP1/BAP1/CASP8/9p21 alteration -> immune proteome state -> phospho kinase state -> response` ladder를 만들고, `CD8+/IFNG+`와 `CD8-/IFNG+`를 구분하는 figure를 넣는 것이 좋다.
- 주의: CPTAC pan-cancer cohort 자체는 detailed treatment 정보가 부족하므로, 직접 response model training template이 아니라 immune-resistance/TME branch와 external OAK validation reference로 둔다.

### Vasaikar 2019 Colon Cancer Proteogenomics

- 구조: treatment-naive colon cancer 110명에서 tumor/NAT/blood를 전향적으로 수집하고 WXS/CNA/RNA/miRNA/label-free proteome/TMT global proteome/phosphoproteome을 통합한다.
- 따라할 점: mutation-only 해석이 틀릴 수 있는 예시를 먼저 찾고, 단백체/인산화층이 그 해석을 어떻게 교정하는지 보여준다. 이 논문은 SOX9 truncation을 mutation-only rule로는 tumor suppressor처럼 볼 수 있지만 protein abundance는 oncogenic stabilization 쪽을 지지했다.
- POC에 유용한 포인트: RB1 amplification과 Rb protein overexpression만으로 끝내지 않고, phospho-Rb T373/S807/S811/T826이 E2F1/CDK2/H3.1 phosphorylation 및 apoptosis hallmark와 연결되는지를 보여준다.
- 특히 좋은 figure 구조: `RB1 CNA -> Rb protein abundance -> phospho-Rb ratio/activity -> E2F/CDK2/proliferation/apoptosis -> CDK2 inhibitor hypothesis`.
- 면역 쪽 포인트: MSI subtype은 cytotoxic immune enrichment가 있지만 protein-level glycolysis가 높고, MSI 안에서 glycolytic activity가 activated CD8 T-cell infiltration과 음의 상관을 보였다. 즉 TMB/MSI-high만으로 checkpoint response-ready라고 가정하면 안 된다.
- 사용자의 POC에 적용: CRC 또는 immunotherapy endpoint가 있다면 `MSI/SNV burden -> glycolysis proteome score(PKM2/SLC2A3 등) -> CD8/IFN score -> response/resistance` ladder를 만들고, phosphoproteome에서는 CDK2/Rb 축을 별도 mechanism으로 테스트한다.
- 주의: 직접 치료반응 코호트는 아니므로 checkpoint/glycolysis와 CDK2 억제는 hypothesis tier로 두고, 실제 사용자 데이터에서 반응 label과 연결될 때만 predictive claim으로 올린다.

### Cao 2021 PDAC Proteogenomics

- 구조: CPTAC PDAC 140 tumors + 67 NATs + 9 normal ducts에서 WGS/WES/methylation/RNA/miRNA/global proteome/phosphoproteome/glycoproteome을 통합한다.
- 따라할 점: PDAC처럼 purity/stroma가 강한 암종에서는 모델보다 먼저 neoplastic cellularity, KRAS VAF, methylation/RNA deconvolution, histology review를 합쳐 분석대상을 정의한다.
- POC에 유용한 포인트: KRAS 자체보다 downstream kinase-substrate axis를 phosphoproteome에서 잡는다. 이 논문은 CDK7-MCM2, AKT1-FLNA, PAK1-BAD S134, PAK2-MAPK6 S189, SRC-STAT3 축을 therapeutic hypothesis로 제시한다.
- 면역 쪽 포인트: immune-cold PDAC는 endothelial adhesion 감소, VEGF/hypoxia 증가, glycolysis 증가, cell-junction phosphorylation 증가와 연결된다. 즉 immune resistance feature는 SNV보다 proteome/phosphoproteome/TME module로 보는 편이 낫다.
- subtype 포인트: RNA subtype만 쓰면 purity/cell composition confounding이 커지고, sufficient-purity 105 tumors에서 C1/C2 proteogenomic subtype이 Moffitt RNA subtype보다 survival separation이 강했다.
- 사용자의 POC에 적용: KRAS/TP53/CDKN2A/SMAD4 alteration을 baseline block으로 두고, `PAK/MET/RAC1`, `AKT/mTOR/ERK`, `VEGF-hypoxia-glycolysis`, `junction phosphosite` feature가 response를 추가 설명하는지 본다.
- 주의: glycoproteomics는 사용자 데이터에 없다면 보조 target/biomarker context로만 쓰고, core POC feature는 global proteome + phosphoproteome + SNV에 맞춘다.

## Proposed Manuscript Spine

1. **Problem**: SNV-driven precision oncology misses response states controlled by protein abundance and signaling activity.
2. **Dataset**: matched global proteome, phosphoproteome, and somatic SNV with drug response labels.
3. **POC Test**: compare genomics-only vs proteogenomic vs phospho-signaling models.
4. **Mechanism**: identify one or two cross-layer axes where SNV/protein/phospho converge or disagree.
5. **Validation**: internal CV/permutation + external public cohort/protein perturbation/PDO if available.
6. **Claim**: phosphoproteome-derived signaling provides an interpretable response layer beyond somatic SNV and global proteome.

## Practical Starting Checklist

- [ ] Define response endpoint and freeze included samples.
- [ ] Build sample × layer matrix with missingness.
- [ ] Summarize SNV features into driver/pathway/signature blocks.
- [ ] Compute global proteome pathway scores and unsupervised subtypes.
- [ ] Compute phosphosite differential signal and protein-corrected PTM signal.
- [ ] Run at least one kinase activity method and record substrate coverage.
- [ ] Fit M0/M1/M2/M3 model ladder with nested or repeated CV.
- [ ] Test `M3 > M1` and `M3 > M2` using permutation or paired fold-level comparison.
- [ ] Select 1–2 mechanisms for figure-level storytelling.
- [ ] Mark whether each key claim is observational, predictive, or perturbation-supported.

## Open Questions

- Does “global” mean global proteome in the current dataset, or another global molecular layer? This page assumes global proteome.
- Are CNA/SV available? If not, the genomics block should be labeled somatic-SNV-only, because several local reference papers rely on CNA/SV for response interpretation.
- Is the drug one agent, one class, or multiple regimens? Mixed treatment can still work, but the first POC should avoid mixing mechanisms unless sample size forces it.
- Are phosphosite-to-protein mappings available for correction? If not, raw phosphosite and kinase activity claims need stronger caveats.

## Connections

- [100-Question Wiki Expansion Sprint](100-question-wiki-expansion-sprint.md)
- [Cancer Multiomics Proteogenomic Atlas](../topics/cancer-multiomics-literature.md)
- [PTM Correction and Kinase Signaling in Cancer Proteomics](../topics/ptm-correction-and-kinase-signaling-in-cancer-proteomics.md)
- [Kinase Activity Inference Under PTM Correction](../syntheses/kinase-activity-inference-under-ptm-correction.md)
- [PTM Correction and Kinase Signaling Question Bank](ptm-correction-kinase-signaling-question-bank.md)

## Sources

- [Lee 2026 — Proteogenomic decoding of chemotherapy resistance in TNBC](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md)
- [Anurag 2022 — Proteogenomic markers of chemotherapy resistance and response in TNBC](../sources/anurag-2022-proteogenomic-markers-chemotherapy-resistance-response.md)
- [Zhang 2023 — Proteogenomics of ccRCC response to tyrosine kinase inhibitor](../sources/zhang-2023-proteogenomics-clear-cell-renal-response-tyrosine-kinase-inhibitor.md)
- [Ji 2023 — Pharmaco-proteogenomic characterization of liver cancer organoids](../sources/ji-2023-pharmaco-proteogenomic-characterization-liver-cancer-organoids.md)
- [Holt 2025 — Proteogenomic characterization of MIBC chemoresistance](../sources/holt-2025-proteogenomic-characterization-unveils-biomarkers-associated.md)
- [Jaehnig 2025 — CALGB 40601 HER2+ neoadjuvant trial proteogenomics](../sources/jaehnig-2025-proteogenomic-analysis-calgb-40601-alliance.md)
- [Song 2024 — Korean NSCLC proteogenomic subtype and adjuvant therapy signal](../sources/song-2024-proteogenomic-analysis-reveals-non-small-cell.md)
- [Sambath 2026 — Integrated genomic and proteomic profiling of cervical cancer chemoradiation resistance](../sources/sambath-2026-integrated-genomic-proteomic-cervical-cancer-chemoradiation-resistance.md)
- [Xu 2026 — HER2-low breast cancer proteogenomic subtype-specific therapeutic potential](../sources/xu-2026-proteogenomic-characterization-reveals-subtype-specific-therapeutic.md)
- [Zhao 2025 — Phosphoproteomic and acetylomic characterization of CRC cells treated with kinase inhibitors](../sources/zhao-2025-phosphoproteomic-acetylomic-characterization-colorectal-cancer.md)
- [Chmielecki 2023 — Candidate mechanisms of acquired resistance to first-line osimertinib](../sources/chmielecki-2023-acquired-resistance-first-line-osimertinib.md)
- [Gillette 2020 — CPTAC LUAD proteogenomic therapeutic vulnerabilities](../sources/gillette-2020-proteogenomic-characterization-reveals-therapeutic-vulnerabilities.md)
- [Chen 2020 — East Asian never-smoker LUAD proteogenomics](../sources/chen-2020-proteogenomics-non-smoking-lung-cancer-east.md)
- [Huang 2021 — HPV-negative HNSCC proteogenomic treatment hypotheses](../sources/huang-2021-proteogenomic-insights-biology-treatment-hpv-negative.md)
- [Petralia 2024 — Pan-cancer proteogenomics characterization of tumor immunity](../sources/petralia-2024-pan-cancer-proteogenomics-characterization-tumor-immunity.md)
- [Vasaikar 2019 — Proteogenomic analysis of human colon cancer](../sources/vasaikar-2019-proteogenomic-analysis-human-colon-cancer.md)
- [Cao 2021 — Proteogenomic characterization of PDAC](../sources/cao-2021-proteogenomic-characterization-pancreatic-ductal-adenocarcinoma.md)
