---
title: "Cancer Multiomics Proteogenomic Atlas — Topic Questions (Answered)"
tags:
  - question-bank
  - cancer-multiomics
  - answered
date: 2026-06-08
status: answered-2026-06
---

# Cancer Multiomics Proteogenomic Atlas — Topic Questions (Answered)

위키 확장 질문에 로컬 `wiki/sources/` 논문 근거로 답을 단 sprint. 답·근거는 그래프(`interactives/llm-wiki-all.html`)에 질문 노드로 자동 반영된다.

## Section A — Cancer multiomics integration (Q1-100)

### Q1. 이 논문이 다루는 임상 맥락은 무엇인가(암종, 치료제 class, 라인, 반응 라벨)?
**A.** 로컬 proteogenomic 코호트들은 임상 맥락을 (암종 / 치료제 class / 라인 / 반응 라벨)로 명시한다. [Lee 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md)은 stage II–III 삼중음성 유방암(TNBC) 50명에서 anthracycline+taxane 기반 neoadjuvant chemotherapy(주로 AC→weekly paclitaxel, carboplatin은 12%만)를 받은 환자를 pCR(ypT0ypN0, 38%) 대 non-pCR로 라벨링한다. [Zhang 2023](../sources/zhang-2023-proteogenomics-clear-cell-renal-response-tyrosine-kinase-inhibitor.md)은 수술 후 sunitinib(TKI, 50mg 4주 on/2주 off)을 받은 투명세포 신세포암(ccRCC) 115명을 RECIST 기준 responder(CR/PR, n=27) 대 non-responder(SD/PD, n=88)로 정의한다. [Chang 2026](../sources/chang-2026-integrative-proteogenomics-gastric-cancer-taiwan.md)은 치료 미경험 위암 154명을 다루며 라인보다는 병인·병기·표적(HER2/PD-L1/CLDN18.2) 맥락을 강조한다.

**Cited**: [Lee DK 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md), [Zhang 2023](../sources/zhang-2023-proteogenomics-clear-cell-renal-response-tyrosine-kinase-inhibitor.md), [chang-2026-integrative-proteogenomics-gastric-cancer-taiwan](../sources/chang-2026-integrative-proteogenomics-gastric-cancer-taiwan.md)

### Q2. primary resistance와 acquired resistance를 논문은 어떤 기준으로 구분하는가(시간/시점/정의)?
**A.** 로컬 논문에서 primary와 acquired resistance를 가르는 핵심 기준은 '초기 반응의 유무와 시점(timing)'이다. [Shin 2017](../sources/shin-2017-primary-resistance-pd1-jak-mutations.md)은 높은 변이부담에도 PD-1 차단에 처음부터 반응하지 못한 종양을 primary resistance로 정의하고 그 기전으로 사전 존재하는 JAK1/2 loss-of-function(인터페론 무감수성)을 제시한다. 반대로 [Zaretsky 2016](../sources/zaretsky-2016-acquired-resistance-pd1-melanoma.md)은 pembrolizumab에 초기 객관적 퇴축을 보인 뒤 지연 진행한 흑색종을 acquired resistance로 명시하고, 이미 활성 면역반응이 일어난 뒤 선택된 JAK1/2·B2M 절단변이(immunoediting)를 그 근거로 든다. 즉 '치료 전 비반응'은 primary, '내구성 초기반응 후 진행'은 acquired로 시점을 기준으로 구분한다.

**Cited**: [Shin 2017](../sources/shin-2017-primary-resistance-pd1-jak-mutations.md), [Zaretsky 2016](../sources/zaretsky-2016-acquired-resistance-pd1-melanoma.md)

### Q3. 샘플링 시점(pre/on/post)과 바이옵시 위치/방법이 결과 해석에 어떤 제약을 만드는가?
**A.** 샘플링 시점과 바이옵시 설계는 해석 가능 범위를 직접 제약한다. [Zhang 2023](../sources/zhang-2023-proteogenomics-clear-cell-renal-response-tyrosine-kinase-inhibitor.md)은 sunitinib 노출 전 수술 시점의 treatment-naive 종양만 프로파일링했으므로 '반응 예측의 baseline 결정요인'은 볼 수 있어도 치료 중 적응이나 acquired resistance의 종단 변화는 관찰할 수 없는 한계가 있다. 반면 [Lee 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md)은 baseline biopsy와 화학요법 후 surgical residual tumor를 paired(단백 수준 n=22)로 확보해 pre/post 변화(EMT·AURKB phosphoproteome enrich)를 직접 비교할 수 있었다. 다만 non-pCR 환자에게서만 잔존 종양이 남으므로 post-treatment 비교는 비반응 subset에 편향되는 제약이 따른다.

**Cited**: [Zhang 2023](../sources/zhang-2023-proteogenomics-clear-cell-renal-response-tyrosine-kinase-inhibitor.md), [Lee DK 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md)

### Q4. WGS/WES에서 변이 범위를 어디까지 포함하는가(SNV/indel/CNV/SV/noncoding/germline)?
**A.** 변이 범위는 논문마다 다른데, SNV/indel만 보면 arm-level CNV·SV 신호를 놓친다는 점이 반복적으로 드러난다. [Zhang 2023](../sources/zhang-2023-proteogenomics-clear-cell-renal-response-tyrosine-kinase-inhibitor.md)은 WES(n=113)로 somatic SNV(VHL 65%, PBRM1 35% 등)뿐 아니라 arm-level SCNA(3p deletion 75%, 7q gain 32%)까지 포함했고, 7q gain이 mTOR 활성화를 통해 내성과 연결됨을 cis-effect로 보였다. [Lee 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md)은 WES로 25,988개 gene의 CNA를 GISTIC2로 산출해 7p21(ITGB8) copy gain을 내성 축으로 도출했다. germline 층까지 보는 [Chen 2026](../sources/chen-2026-global-impact-germline-structural-variation-cancer-proteome.md)은 CPTAC WGS에서 germline structural variation(704,263개 SV; deletion/duplication/inversion/insertion)을 정량해, SNV 중심 분석이 비SNV·germline SV 결정요인을 사각지대로 남긴다는 점을 보여준다.

**Cited**: [Zhang 2023](../sources/zhang-2023-proteogenomics-clear-cell-renal-response-tyrosine-kinase-inhibitor.md), [Lee DK 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md), [Chen 2026](../sources/chen-2026-global-impact-germline-structural-variation-cancer-proteome.md)

### Q5. HLA typing은 어떤 입력과 도구로 수행했는가(정확도/불확실성 근거 포함)?
**A.** 로컬 논문 중 HLA typing 입력·도구를 명시적으로 기술하는 것은 neoantigen 파이프라인 논문이다. [Huber 2025](../sources/huber-2025-comprehensive-proteogenomic-pipeline-neoantigen-discovery.md)의 NeoDisc는 HLA typing을 germline 및 tumor WES와 RNA-seq 데이터로부터 함께 도출한다고 기술한다. 이 파이프라인은 antigen processing/presentation machinery(APPM) 결함과 HLA LOH를 명시적으로 식별해 neoantigen 해석의 'failure mode'로 표면화하므로, HLA 호출의 불확실성(allele loss·presentation 결함)을 다운스트림 항원 품질 판단 전에 감사할 수 있게 한다. 대다수 다른 로컬 proteogenomic 논문은 HLA typing 도구·정확도를 별도로 보고하지 않는다.

**Cited**: [Huber 2025](../sources/huber-2025-comprehensive-proteogenomic-pipeline-neoantigen-discovery.md)

### Q6. neoantigen을 다루는가? 다룬다면 prediction-only인가, immunopeptidomics/proteogenomics 검증이 있는가?
**A.** 로컬 corpus에서 neoantigen을 prediction에 그치지 않고 proteogenomics/immunopeptidomics로 검증하는 대표 사례는 [Huber 2025](../sources/huber-2025-comprehensive-proteogenomic-pipeline-neoantigen-discovery.md)의 NeoDisc다. 이 파이프라인은 in silico HLA-binding 예측에 더해 immunopeptidomics(HLA-I/HLA-II, DDA·DIA) MS 데이터로 HLA-결합 펩타이드를 직접 검출하고, 후보를 IFNγ ELISpot로 기능 검증한다. 자궁경부 선암 사례(CESC-1)에서 66개 HLA-I 후보 중 11개가 면역원성으로 확인됐고 immunopeptidomics가 검증된 neoantigen을 직접 검출·재순위화하는 데 쓰였다. 즉 prediction-only를 넘어 펩타이드 수준 검증을 포함하는 end-to-end 사례다.

**Cited**: [Huber 2025](../sources/huber-2025-comprehensive-proteogenomic-pipeline-neoantigen-discovery.md)

### Q7. neoantigen 후보 필터는 무엇인가(binding, expression, clonality, processing, stability, RT prediction)?
**A.** [Huber 2025](../sources/huber-2025-comprehensive-proteogenomic-pipeline-neoantigen-discovery.md)의 NeoDisc는 neoantigen 후보를 여러 단계로 필터링한다. 우선 변이 신뢰도를 4개 caller의 앙상블로 통제해(단일 caller 호출=low-confidence, ≥2 caller=high-confidence) 기본 설정에서는 high-confidence 변이만 in silico 예측에 사용하고, RNA-seq 발현 근거를 추가 evidence로 활용한다. 이후 HLA-binding 예측 후 HLA-I 후보는 rule-based 랭킹과 공개 면역원성 데이터로 학습한 ML 모델로 재순위화하며, APPM 결함·HLA LOH 같은 presentation failure를 표면화해 후보 해석에 반영한다. 다만 clonality나 RT(retention time)·stability 같은 추가 필터는 이 페이지에 명시되어 있지 않다.

**Cited**: [Huber 2025](../sources/huber-2025-comprehensive-proteogenomic-pipeline-neoantigen-discovery.md)

### Q8. MHC-I와 MHC-II를 분리해 분석하는가? 분리하지 않으면 어떤 위험이 생기는가?
**A.** [Huber 2025](../sources/huber-2025-comprehensive-proteogenomic-pipeline-neoantigen-discovery.md)의 NeoDisc는 MHC-I과 MHC-II를 분리해 처리한다. immunopeptidomics를 HLA-I과 HLA-II로 구분해 취득하고, HLA-I 후보는 공개 면역원성 데이터로 학습한 ML 랭킹 모델을 적용하는 반면, HLA-II는 견고한 ML 학습에 충분한 공개 면역원성 데이터가 없어 rule-based 랭킹만 쓴다고 명시한다. 이 비대칭 자체가 두 class를 합치면 안 되는 이유를 보여준다 — class별 binding 규칙·예측 신뢰도·검증 가능성이 다르므로, 분리하지 않으면 데이터가 빈약한 HLA-II 예측을 HLA-I 수준 신뢰도로 오인하는 위험이 생긴다.

**Cited**: [Huber 2025](../sources/huber-2025-comprehensive-proteogenomic-pipeline-neoantigen-discovery.md)

### Q9. immune evasion feature를 어떤 층에서 측정/추정하는가(HLA LOH, B2M, JAK/IFN, antigen processing 등)?
**A.** immune evasion feature는 유전체·단백체·표현형의 여러 층에서 측정·추정된다. [McGranahan 2017](../sources/mcgranahan-2017-allele-specific-hla-loss-lung-cancer.md)은 LOHHLA 도구로 종양 시퀀싱에서 allele-specific HLA LOH를 추정해 비소세포폐암의 약 40%에서 관찰했고, [Shin 2017](../sources/shin-2017-primary-resistance-pd1-jak-mutations.md)은 JAK1/2 loss-of-function이 IFNγ 자극 후 PD-L1·인터페론 반응 유도 실패로 이어짐을 기능적으로 보였다. [Grasso 2018](../sources/grasso-2018-genetic-mechanisms-immune-evasion-colorectal-cancer.md)은 대장암 1,211례에서 MSI-high 종양의 B2M·HLA biallelic loss(copy loss + copy-neutral LOH)를 antigen-presentation 실패 축으로, WNT 활성화를 T세포 배제 축으로 분리한다. 단백/표현형 층 근거로 [Lee 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md)은 ITGB8 과발현이 종양세포의 IFN-α/γ·염증 시그니처를 직접 억압함을 보여, antigen processing·IFN·HLA LOH가 서로 다른 층에서 잡힘을 종합한다.

**Cited**: [McGranahan 2017](../sources/mcgranahan-2017-allele-specific-hla-loss-lung-cancer.md), [Shin 2017](../sources/shin-2017-primary-resistance-pd1-jak-mutations.md), [Grasso 2018](../sources/grasso-2018-genetic-mechanisms-immune-evasion-colorectal-cancer.md), [Lee DK 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md)

### Q10. proteogenomics/phosphoproteomics 레이어가 있으면 측정 깊이(단백질/사이트 수)는 어떻게 보고되는가?
**A.** proteogenomics/phosphoproteomics 층의 측정 깊이는 식별된 단백질 수와 phosphosite 수(및 그 site가 매핑된 단백질 수, coverage 필터 후 보존 수)로 보고하는 것이 표준이다. [Lee 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md)은 TMT 11-plex로 10,457개 단백질과 31,258개 phosphosite(5,373개 단백질)를 보고한다. [Zhang 2023](../sources/zhang-2023-proteogenomics-clear-cell-renal-response-tyrosine-kinase-inhibitor.md)은 label-free로 12,310개 단백질(분석에 7,451개 사용)과 37,055개 phosphosite(7,502개 phosphoprotein) 중 25% coverage 필터 후 6,749개 site를 남겼다고 명시해, raw 식별 수와 분석에 실제 사용한 수를 구분 보고한다. [Chang 2026](../sources/chang-2026-integrative-proteogenomics-gastric-cancer-taiwan.md)도 TMT proteome >10,000 protein group과 phosphoproteome 30,000 phosphosite로 깊이를 기술한다.

**Cited**: [Lee DK 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md), [Zhang 2023](../sources/zhang-2023-proteogenomics-clear-cell-renal-response-tyrosine-kinase-inhibitor.md), [chang-2026-integrative-proteogenomics-gastric-cancer-taiwan](../sources/chang-2026-integrative-proteogenomics-gastric-cancer-taiwan.md)

### Q11. kinase activity inference를 수행하는가? 방법(KSEA/PTM-SEA/network)과 근거는 무엇인가?
**A.** 로컬 proteogenomics 논문들은 인산화단백체로부터 kinase 활성을 추론하며, 방법은 크게 substrate-set 기반 KSEA와 PTM-SEA, 그리고 network 기반 KEA3로 나뉜다. ccRCC sunitinib 코호트는 KSEA/ssGSEA로 non-responder에서 MTOR·MAP2K1, responder에서 CDK1/2 활성을 지목했고, sunitinib 표적 RTK의 abundance/activity 자체는 반응군을 가르지 못해 'drug target보다 pathway/kinase state가 반응을 더 잘 설명한다'는 근거를 제시한다([Zhang 2023](../sources/zhang-2023-proteogenomics-clear-cell-renal-response-tyrosine-kinase-inhibitor.md)). 한국인 TNBC 코호트는 phosphosite 수준 PTM-SEA로 non-pCR의 GRK2/GRK5·CDK2와 잔존 종양의 AURKB 신호를 도출했고([Lee 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md)), 위암 atlas는 KEA3로 해부학적 위치별 upstream kinase(MET/CDK4 등)와 CDK4 phosphorylation→FOXM1/RB1 기질 활성을 연결했다([Chang 2026](../sources/chang-2026-integrative-proteogenomics-gastric-cancer-taiwan.md)).

**Cited**: [Zhang 2023](../sources/zhang-2023-proteogenomics-clear-cell-renal-response-tyrosine-kinase-inhibitor.md), [Lee DK 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md), [chang-2026-integrative-proteogenomics-gastric-cancer-taiwan](../sources/chang-2026-integrative-proteogenomics-gastric-cancer-taiwan.md)

### Q12. protein abundance confounding(PTM correction)을 명시적으로 다루는가? 안 다루면 어떤 caveat를 남길 것인가?
**A.** 로컬 논문들은 protein abundance가 phosphosite 신호를 오염시키는 문제를 주로 (1) class I(localization score 통과) phosphosite만 downstream에 사용하고 (2) Ochoa 2020 functional score(>0.5) 같은 기능성 필터로 의미 있는 site에 초점을 맞추는 방식으로 다룬다; 예컨대 CRLM 연구는 16,300개 class I site만 분석하고 functional score 임계로 NDRG1 S330·EIF4B S422 등을 선별했다([Zhao 2026](../sources/zhao-2026-proteogenomic-characterization-reveals-metabolic-vulnerabilities.md)). 다만 대부분은 phosphosite를 모(母)단백량으로 명시적으로 normalize하지 않으므로, abundance-driven 변화와 진짜 stoichiometry 변화를 분리하지 못한다는 점은 남는 caveat이며, EIF4B S422가 mRNA·protein 차이 없이 phospho만 상승한 사례처럼 protein-level 변화 동반 여부를 함께 보고하는 것이 보완책이다([Zhao 2026](../sources/zhao-2026-proteogenomic-characterization-reveals-metabolic-vulnerabilities.md)). KSEA 추론도 기본 substrate DB 한계로 indirect axis를 놓칠 수 있어 확장 DB(Sun et al.)로 재계산하는 보정이 권고된다([Zhao 2026](../sources/zhao-2026-proteogenomic-characterization-reveals-metabolic-vulnerabilities.md)).

**Cited**: [Wensi Zhao 2026](../sources/zhao-2026-proteogenomic-characterization-reveals-metabolic-vulnerabilities.md)

### Q13. multi-omics integration은 어떤 목표로 수행했는가(subtype, driver→state, prediction model)?
**A.** 로컬 multi-omics 통합의 목표는 크게 (1) 분자 아형 정의, (2) driver/variant→기능 상태 연결, (3) 반응·예후 예측 모델로 나뉜다. 한국인 TNBC 연구는 CNA+RNA+protein+phosphoprotein 4-layer를 NMF로 통합해 5개 proteogenomic subtype을 정의하는 것이 일차 목표였고([Lee 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md)), CRLM 연구는 proteome 기반 unsupervised clustering으로 C1(대사)·C2(RNA) 아형을 만들고 SHMT1-formate-AMPK, PIM-NDRG1 같은 driver→state 축을 기능 검증까지 연결했다([Zhao 2026](../sources/zhao-2026-proteogenomic-characterization-reveals-metabolic-vulnerabilities.md)). ccRCC 연구는 통합의 최종 목표를 sunitinib responder/non-responder를 가르는 예측 분류기 구축에 두었다([Zhang 2023](../sources/zhang-2023-proteogenomics-clear-cell-renal-response-tyrosine-kinase-inhibitor.md)).

**Cited**: [Lee DK 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md), [Wensi Zhao 2026](../sources/zhao-2026-proteogenomic-characterization-reveals-metabolic-vulnerabilities.md), [Zhang 2023](../sources/zhang-2023-proteogenomics-clear-cell-renal-response-tyrosine-kinase-inhibitor.md)

### Q14. prediction model이 있으면 학습/검증 설계는 무엇인가(외부 검증, CV, prospective)?
**A.** 예측 모델을 만든 로컬 논문들은 대체로 same-cohort 학습/검증과 별도 외부 코호트 검증을 병행한다. ccRCC sunitinib 연구는 데이터를 70/30 train/test로 나누고 학습 단계에서 5-fold cross-validation을 적용한 random forest로 multi-omics 분류기(test AUC 0.98)를 만들되, 단일기관 후향 코호트라 prospective 검증이 필요하다고 명시했다([Zhang 2023](../sources/zhang-2023-proteogenomics-clear-cell-renal-response-tyrosine-kinase-inhibitor.md)). 한국인 TNBC 연구는 5개 저항인자 logistic regression(AUC 0.946)을 만들고 NMF subtype을 METABRIC 258 TNBC에 k-NN 매핑해 외부 재현했지만, AUC 0.946 자체는 same-cohort 결과이고 외부 prospective AUC는 미보고임을 한계로 적었다([Lee 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md)).

**Cited**: [Zhang 2023](../sources/zhang-2023-proteogenomics-clear-cell-renal-response-tyrosine-kinase-inhibitor.md), [Lee DK 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md)

### Q15. feature importance/해석(SHAP 등)을 제공하는가? 제공한다면 어떤 레이어가 상위에 오는가?
**A.** 검토한 로컬 proteogenomics 논문들은 SHAP 같은 사후(post-hoc) 설명기법을 명시적으로 사용하기보다, 해석 가능한 모델 자체나 선별된 feature 목록으로 중요도를 제시한다. ccRCC 연구는 proteome-only RF는 18개 단백질, multi-omics RF는 임상(LDH·PLT·종양크기)+변이(VHL·KMT2C)+CNA(7q·3p)+전사체+단백체 feature를 명시했으나 feature별 기여도를 SHAP로 분해하지는 않았다([Zhang 2023](../sources/zhang-2023-proteogenomics-clear-cell-renal-response-tyrosine-kinase-inhibitor.md)). 한국인 TNBC 모델은 estrogen GSVA·GRK2·ITGB8·AKR1C2·ABCA13 다섯 인자를 직접 해석 가능한 logistic 항으로 나열했고([Lee 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md)), 위암 atlas는 black-box 대신 stage+DBAC+proteome-immune state를 쓰는 interpretable decision-tree로 예후를 설명했다([Chang 2026](../sources/chang-2026-integrative-proteogenomics-gastric-cancer-taiwan.md)). 상위에 오는 레이어는 연구마다 다르지만 단백체/인산화단백체 기반 pathway·kinase feature와 CNA가 반복적으로 강한 예측자로 등장한다.

**Cited**: [Zhang 2023](../sources/zhang-2023-proteogenomics-clear-cell-renal-response-tyrosine-kinase-inhibitor.md), [Lee DK 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md), [chang-2026-integrative-proteogenomics-gastric-cancer-taiwan](../sources/chang-2026-integrative-proteogenomics-gastric-cancer-taiwan.md)

### Q16. 데이터 레이어의 공개 수준은 무엇인가(raw/processed/supplement/portal/code)?
**A.** 로컬 논문들의 데이터 공개 수준은 대체로 'processed가 아닌 raw 수준 + 다중 repository 분산' 형태다. 한국인 TNBC 연구는 WES/RNA-seq를 NCBI BioProject(PRJNA1422845/1422844), proteome·phosphoproteome를 CPTAC PDC(PDC000695/696)에 공개했고([Lee 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md)), TNBC 화학요법 연구는 genomics를 dbGaP(phs002505), 단백체/PDX raw를 PDC(PDC000408-410)+MassIVE(MSV000089758)에 올렸다([Anurag 2022](../sources/anurag-2022-proteogenomic-markers-chemotherapy-resistance-response.md)). 다만 환자 시퀀싱 데이터는 controlled-access인 경우가 많고(위암 atlas는 dbGaP phs004447 + PDC000645/649, 원본 code 없음), CRLM 연구도 iProx/GSA raw는 공개하되 'original code 없음'을 명시해 portal/raw는 있어도 분석 코드까지 공개되는 사례는 드물다([Chang 2026](../sources/chang-2026-integrative-proteogenomics-gastric-cancer-taiwan.md); [Zhao 2026](../sources/zhao-2026-proteogenomic-characterization-reveals-metabolic-vulnerabilities.md)).

**Cited**: [Lee DK 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md), [Anurag 2022](../sources/anurag-2022-proteogenomic-markers-chemotherapy-resistance-response.md), [chang-2026-integrative-proteogenomics-gastric-cancer-taiwan](../sources/chang-2026-integrative-proteogenomics-gastric-cancer-taiwan.md), [Wensi Zhao 2026](../sources/zhao-2026-proteogenomic-characterization-reveals-metabolic-vulnerabilities.md)

### Q17. 재현을 위해 꼭 필요한 파일/파라미터가 공개되었는가?
**A.** 재현에 필요한 raw 시퀀싱/MS 파일과 도구 체인은 대체로 공개되지만, 분석 파라미터와 코드의 완전성은 논문마다 편차가 크다. 자궁경부암 CCRT 연구는 BWA-MEM→MUTECT2→ANNOVAR, CNVkit→GISTIC2, MANTA→AnnotSV→Starfish, MutationalPatterns(COSMIC v3), Proteome Discoverer v2.1 등 파이프라인 단계와 버전을 Methods에 비교적 구체적으로 적고 proteomics raw를 ProteomeXchange PXD058817로 공개했다([Sambath 2026](../sources/sambath-2026-integrated-genomic-proteomic-cervical-cancer-chemoradiation-resistance.md)). 반면 CRLM 연구는 iProx/GSA에 raw를 올렸으나 'original code 없음'을 명시했고 KSEA를 확장 DB로 재계산하는 등 일부 분석은 표준 도구 밖이라, 핵심 NMF·clustering·biomarker 선별 파라미터까지 완전 재현하려면 supplementary에 의존해야 한다([Zhao 2026](../sources/zhao-2026-proteogenomic-characterization-reveals-metabolic-vulnerabilities.md)). 즉 raw 데이터와 도구명은 대개 확보되지만 코드·정확한 cutoff는 부분적으로만 공개되는 것이 일반적이다.

**Cited**: [Janani Sambath 2026](../sources/sambath-2026-integrated-genomic-proteomic-cervical-cancer-chemoradiation-resistance.md), [Wensi Zhao 2026](../sources/zhao-2026-proteogenomic-characterization-reveals-metabolic-vulnerabilities.md)

### Q18. cohort 규모와 MS depth 사이의 trade-off를 논문은 어떻게 설계했는가?
**A.** 로컬 논문들은 cohort 규모와 MS 깊이 사이의 trade-off를 흔히 '깊은 단백체는 소수에서만, 나머지는 IHC로 검증'하는 2단계 설계로 해결한다. 자궁경부암 CCRT 연구는 genomic layer는 WGS 26+WES 10으로 넓히되 deep TMT proteome은 sensitive 5+resistant 5(=10)에만 적용하고, 후보(STX3)를 추가 32명 FFPE IHC 코호트로 검증해 작은 deep-MS 표본의 한계를 보완했다([Sambath 2026](../sources/sambath-2026-integrated-genomic-proteomic-cervical-cancer-chemoradiation-resistance.md)). 한국인 TNBC 연구도 baseline 50명 중 41명에서만 WES+RNA+TMT를 모두 확보하고 paired pre/post 단백체 분석은 n=22로 좁히되 METABRIC로 외부 검증했다([Lee 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md)). CRLM 연구는 discovery n=34의 통계 power 부족(SOD2 p=0.098)을 인정하고 n=87 IHC validation cohort(p=0.0331)로 보강하는 동일한 전략을 썼다([Zhao 2026](../sources/zhao-2026-proteogenomic-characterization-reveals-metabolic-vulnerabilities.md)).

**Cited**: [Janani Sambath 2026](../sources/sambath-2026-integrated-genomic-proteomic-cervical-cancer-chemoradiation-resistance.md), [Lee DK 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md), [Wensi Zhao 2026](../sources/zhao-2026-proteogenomic-characterization-reveals-metabolic-vulnerabilities.md)

### Q19. 샘플 준비(FFPE/frozen), 라벨링(TMT/DIA), enrichment(IMAC 등), 기기(instrument)는 무엇인가?
**A.** 로컬 논문들의 단백체 워크플로우는 주로 TMT 다중화 라벨링 + IMAC 계열 인산화 enrichment + Orbitrap 계열 기기 조합이다. 자궁경부암 CCRT 연구는 treatment-naïve tumor를 trypsin 분해 후 TMT 10-plex 라벨링, bRPLC 분획, Q Exactive HF-X Orbitrap LC-MS/MS로 측정했다(WGS/WES는 Illumina NovaSeq 6000)([Sambath 2026](../sources/sambath-2026-integrated-genomic-proteomic-cervical-cancer-chemoradiation-resistance.md)). CRLM 연구는 TMT proteome + Ti4+-IMAC phosphoproteome(고분해능 MS)을 썼고([Zhao 2026](../sources/zhao-2026-proteogenomic-characterization-reveals-metabolic-vulnerabilities.md)), 한국인 TNBC 연구는 TMT 11-plex를 사용했다([Lee 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md)). 샘플 형태는 연구별로 달라 TNBC chemo 연구는 OCT-포매 frozen core biopsy를 교대 층으로 cryosection해 한 조직에서 WES/RNA/proteome/phospho를 뽑은 반면([Anurag 2022](../sources/anurag-2022-proteogenomic-markers-chemotherapy-resistance-response.md)), 검증 단계에서는 FFPE 조직이 IHC에 쓰였다([Sambath 2026](../sources/sambath-2026-integrated-genomic-proteomic-cervical-cancer-chemoradiation-resistance.md)).

**Cited**: [Janani Sambath 2026](../sources/sambath-2026-integrated-genomic-proteomic-cervical-cancer-chemoradiation-resistance.md), [Wensi Zhao 2026](../sources/zhao-2026-proteogenomic-characterization-reveals-metabolic-vulnerabilities.md), [Lee DK 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md), [Anurag 2022](../sources/anurag-2022-proteogenomic-markers-chemotherapy-resistance-response.md)

### Q20. tumor purity/immune infiltration 조정은 어떤 방식으로 했는가(병리/추정/모델)?
**A.** tumor purity는 주로 사전 필터링과 RNA/proteome 추정치 교차확인으로, immune infiltration은 deconvolution 스코어로 조정한다. TNBC chemo 연구는 추정 tumor content가 45% 미만인 샘플을 RNA-protein 상관 저하를 근거로 downstream 분석에서 제외했다([Anurag 2022](../sources/anurag-2022-proteogenomic-markers-chemotherapy-resistance-response.md)). 한국인 TNBC 연구는 RNA 추정 purity와 proteomic 추정 purity가 높은 상관을 보임을 확인하고 ESTIMATE stromal score가 핵심 저항인자 분포에 영향을 주지 않음을 점검했다([Lee 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md)). ccRCC 연구는 proteome 프로파일에 xCell(64 cell types)과 ESTIMATE류 immune/stromal score를 적용해 T-cell infiltrated·cold·progenitor-infiltrated 면역 클러스터로 종양을 층화했다([Zhang 2023](../sources/zhang-2023-proteogenomics-clear-cell-renal-response-tyrosine-kinase-inhibitor.md)).

**Cited**: [Anurag 2022](../sources/anurag-2022-proteogenomic-markers-chemotherapy-resistance-response.md), [Lee DK 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md), [Zhang 2023](../sources/zhang-2023-proteogenomics-clear-cell-renal-response-tyrosine-kinase-inhibitor.md)

### Q21. immune-hot/cold 정의는 무엇인가(GEP/CD8/IFN/TIL/단백질 면역마커)?
**A.** 로컬 근거에서 immune-hot은 종양 실질로 침투한 CD8 T-effector 시그니처와 높은 neoantigen/TMB로 정의되고, 반대로 nonresponse는 CD8 T세포가 종양실질이 아닌 종양주변 기질에 갇히는 'immune-excluded'(TGF-β/섬유아세포 기질) 또는 침윤 자체가 없는 cold 상태로 나뉜다 [Mariathasan 2018](../sources/mariathasan-2018-tgfb-pdl1-blockade-tcell-exclusion.md). 면역원성이 높아도 B2M·HLA 양대립유전자 소실 같은 항원제시 결함으로 cold가 되는 경로와, WNT/β-catenin 활성으로 T세포 침윤이 줄어드는 exclusion 경로가 구분된다 [Grasso 2018](../sources/grasso-2018-genetic-mechanisms-immune-evasion-colorectal-cancer.md). 단백체 기반으로도 종양을 T-cell infiltrated, cold, progenitor-cell infiltrated 군으로 분류할 수 있어, GEP/CD8/IFN/TIL 같은 전사·단백 면역마커가 hot/cold 정의의 축임을 보여준다 [Zhang 2023](../sources/zhang-2023-proteogenomics-clear-cell-renal-response-tyrosine-kinase-inhibitor.md).

**Cited**: [Mariathasan 2018](../sources/mariathasan-2018-tgfb-pdl1-blockade-tcell-exclusion.md), [Grasso 2018](../sources/grasso-2018-genetic-mechanisms-immune-evasion-colorectal-cancer.md), [Zhang 2023](../sources/zhang-2023-proteogenomics-clear-cell-renal-response-tyrosine-kinase-inhibitor.md)

### Q22. proteomics가 transcriptome 대비 제공하는 추가 설명력은 무엇이라고 주장하는가?
**A.** 로컬 proteogenomics 연구들은 단백체/인산화체가 전사체만으로는 보이지 않는 기능적 신호를 추가로 드러낸다고 주장한다. 유방암 105례 분석에서 mRNA 수준에서는 잘 잡히지 않던 GPCR 인산화 클러스터가 인산화체 경로분석에서 식별되고, 5q 결손의 trans-효과(CETN3/SKP1 소실→EGFR·SRC 상승)나 ERBB2 외 고인산화 kinase(CDK12, PAK1, PTK2 등)가 단백 수준에서만 좁혀졌다 [Mertins 2016](../sources/mertins-2016-proteogenomics-connects-somatic-mutations-signalling.md). 소아 뇌종양 218례에서도 단백체가 전사체에 드러나지 않는 체세포변이·CNV의 하류 기능 효과를 보여줬다 [Petralia 2020](../sources/petralia-2020-integrated-proteogenomic-characterization-across-major.md). 다만 TNBC 코호트에서는 mRNA-단백 상관이 양의 상관 93.8%(그중 62%가 P<0.01)로 상당 부분 일치해, 단백체의 추가 설명력은 상관이 약한 유전자군과 PTM 층에 집중됨을 시사한다 [Lee 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md).

**Cited**: [Mertins 2016](../sources/mertins-2016-proteogenomics-connects-somatic-mutations-signalling.md), [Petralia 2020](../sources/petralia-2020-integrated-proteogenomic-characterization-across-major.md), [Lee DK 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md)

### Q23. phosphoproteome이 면역 상태와 연결된다고 주장하면 어떤 경로/모듈을 제시하는가?
**A.** 로컬 근거에서 인산화체-면역 연결은 주로 종양세포 내재 신호 모듈을 통해 제시된다. TNBC paired 분석에서 비반응 종양은 PTM-SEA로 GRK2·GRK5·CDK2 인산화 모듈이 활성이었고, 7p21 증폭 표면단백 ITGB8 과발현은 IFN-α(NES -1.73)·IFN-γ(-2.31)·inflammatory(-2.52)·TNF-α/NF-κB(-3.06) 시그니처를 직접 억압해 인산화/표면신호가 면역 cold 상태와 연결됨을 보여준다 [Lee 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md). 소아 뇌종양 pan-cancer proteogenomics는 kinase-substrate 연관·공발현 네트워크 분석을 면역 미세환경 특성과 함께 제시해, 인산화 신호 모듈이 종양별 면역경관과 맞물려 있음을 시사한다 [Petralia 2020](../sources/petralia-2020-integrated-proteogenomic-characterization-across-major.md).

**Cited**: [Lee DK 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md), [Petralia 2020](../sources/petralia-2020-integrated-proteogenomic-characterization-across-major.md)

### Q24. 표적치료 맥락에서 kinase activation mode를 어떻게 구분하는가(리간드, mutation, phosphorylation)?
**A.** 로컬 근거는 kinase 활성화 양식을 크게 (1) 유전적 활성화—gain-of-function mutation, genomic amplification, chromosomal rearrangement, autocrine(리간드) 활성—로 구분한다 [Du 2018](../sources/du-2018-mechanisms-receptor-tyrosine-kinase-activation.md). 그러나 표적치료 맥락에서는 단백·인산화 활성이 더 중요한데, ccRCC sunitinib 연구에서 표적 RTK의 단백 양/활성 자체는 반응자와 비반응자를 가르지 못했고 대신 KSEA/ssGSEA로 추론한 MTOR·MAP2K1 인산화 활성이 비반응에서 높았다(7q 증폭→S6K 인산화 실험검증) [Zhang 2023](../sources/zhang-2023-proteogenomics-clear-cell-renal-response-tyrosine-kinase-inhibitor.md). 즉 mutation/amplification 같은 유전 양식과 별개로, 인산화체에서 KSEA로 추론한 kinase 활성이 활성화 양식을 구분하는 핵심 축으로 쓰인다 [Casado 2013](../sources/casado-2013-kinase-substrate-enrichment-analysis-provides-insights.md).

**Cited**: [Du 2018](../sources/du-2018-mechanisms-receptor-tyrosine-kinase-activation.md), [Zhang 2023](../sources/zhang-2023-proteogenomics-clear-cell-renal-response-tyrosine-kinase-inhibitor.md), [Casado 2013](../sources/casado-2013-kinase-substrate-enrichment-analysis-provides-insights.md)

### Q25. 치료 전 상태(baseline) vs 치료 후 상태(on-treatment)에서 어떤 레이어가 가장 크게 변하는가?
**A.** 로컬 근거 중 baseline과 on-treatment(잔존종양)를 paired로 비교한 TNBC 연구가 가장 직접적이다. 항암화학 후 잔존 종양(paired n=22)에서는 EMT/myogenesis 시그니처와 함께 특히 AURKB 인산화체 신호가 일관되게 enrich되어, 치료 후 가장 두드러진 변화가 인산화/신호 층에서 나타났다 [Lee 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md). 같은 연구는 baseline 단계에서도 mRNA-단백 상관이 높아(양의 상관 93.8%) 전사체 변화만으로는 잡히지 않는 잔존종양 신호 재배선을 인산화체가 포착함을 보여준다. 다만 이는 단일 화학요법 코호트의 paired 단백/인산화 비교에 근거한 것으로, 어느 한 층이 보편적으로 가장 크게 변한다고 일반화하기에는 로컬 longitudinal 근거가 제한적이다.

**Cited**: [Lee DK 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md)

### Q26. longitudinal 샘플이 있으면 내성을 어떤 레이어 변화로 설명하는가(유전 선택, signaling rewiring, immune remodeling)?
**A.** 로컬 근거에서 longitudinal 다중오믹스는 내성을 단일 층이 아니라 여러 층의 변화로 설명한다. 소아 고악성도 신경교종 16명에서 1차 절제·재발/진행·autopsy 시점에 snRNA-seq·snATAC-seq·WGS·CODEX 공간단백체를 결합한 atlas는 치료 후 oligodendrocyte 증가와 proneural 종양세포의 공간 모티프 형성, myeloid의 microglia→macrophage 표현형 이동, interferon 반응 상향 같은 immune remodeling을 시간축으로 포착했다 [Sussman 2026](../sources/sussman-2026-longitudinal-single-cell-spatial-multiomic-atlas.md). TKI 맥락의 단면 proteogenomics도 7q 증폭→mTOR 활성이라는 유전 선택과 signaling rewiring(KSEA로 MTOR/MAP2K1 활성)을 비반응과 연결해, longitudinal 설계가 유전 선택·신호 재배선·면역 재구성을 함께 추적할 수 있음을 보여준다 [Zhang 2023](../sources/zhang-2023-proteogenomics-clear-cell-renal-response-tyrosine-kinase-inhibitor.md).

**Cited**: [Sussman 2026](../sources/sussman-2026-longitudinal-single-cell-spatial-multiomic-atlas.md), [Zhang 2023](../sources/zhang-2023-proteogenomics-clear-cell-renal-response-tyrosine-kinase-inhibitor.md)

### Q27. neoantigen burden/quality 변화가 내성과 연결된다고 주장하는가? 근거는 무엇인가?
**A.** 로컬 근거는 neoantigen burden과 quality 변화가 모두 면역회피·내성과 연결된다고 주장한다. 초기 NSCLC 258구역 분석에서 면역 침윤이 적은 종양은 과거 immune editing의 흔적으로 clonal neoantigen의 copy-number 소실을 보였고, 침윤된 구역은 진행형 immunoediting으로 HLA LOH 또는 발현 neoantigen 고갈, 항원성 변이 유전자의 프로모터 과메틸화를 보여 다양한 회피 경로가 무병생존 악화를 예측했다 [Rosenthal 2019](../sources/rosenthal-2019-neoantigen-directed-immune-escape-lung-cancer.md). 췌장암 장기생존자 70명 추적에서는 단순 burden이 아니라 neoantigen quality(non-selfness/selfness 기반)가 높을수록 면역압으로 제거되어 재발종양에서 high-quality neoantigen이 줄어, 면역계가 자연적으로 neoantigen을 편집함을 보였다 [Lukza 2022](../sources/uksza-2022-neoantigen-quality-predicts-immunoediting-survivors.md). HLA 대립유전자별 소실(약 40%의 초기 NSCLC, 흔히 subclonal)도 subclonal neoantigen 부담과 상관해 면역압 하 선택을 뒷받침한다 [McGranahan 2017](../sources/mcgranahan-2017-allele-specific-hla-loss-lung-cancer.md).

**Cited**: [Rosenthal 2019](../sources/rosenthal-2019-neoantigen-directed-immune-escape-lung-cancer.md), [Łuksza 2022](../sources/uksza-2022-neoantigen-quality-predicts-immunoediting-survivors.md), [McGranahan 2017](../sources/mcgranahan-2017-allele-specific-hla-loss-lung-cancer.md)

### Q28. immunopeptidomics가 있으면 peptide 검출 FDR/검증을 어떻게 통제하는가?
**A.** 로컬 근거에서 immunopeptidomics는 종양에서 용출한 HLA 결합 펩타이드를 LC-MS/MS로 측정해 동정하는데, noncanonical 후보를 포함해 참조 DB를 확장하면 spectral matching의 위양성 위험이 커지므로 엄격한 FDR 통제와 전사체·ribosome profiling 같은 직교 근거, 표적·기능 검증이 필요하다고 강조한다 [Chong 2022](../sources/chong-2022-identification-tumor-antigens-immunopeptidomics.md). 임상 파이프라인 NeoDisc는 HLA-I/II 펩타이드(DDA·DIA)에 더해 변이를 4개 caller 앙상블로 처리해 2개 이상에서 지지된 high-confidence 변이만 기본 예측에 쓰고, HLA LOH·항원제시기구(APPM) 결함을 'failure mode'로 명시해 검출·해석을 통제한다 [Huber 2025](../sources/huber-2025-comprehensive-proteogenomic-pipeline-neoantigen-discovery.md).

**Cited**: [Chong 2022](../sources/chong-2022-identification-tumor-antigens-immunopeptidomics.md), [Huber 2025](../sources/huber-2025-comprehensive-proteogenomic-pipeline-neoantigen-discovery.md)

### Q29. variant peptide(proteogenomics) 탐지가 있으면 search space/FDR 문제를 어떻게 다루는가?
**A.** 로컬 근거는 variant/non-canonical 펩타이드 탐지의 핵심 난점이 검색공간 팽창과 그로 인한 FDR 문제라고 본다. moPepGen은 그래프 기반으로 germline·somatic 변이, noncoding ORF, RNA fusion·circularization에서 비정규 펩타이드를 선형시간에 망라 생성해 개인화 검색 DB를 만든다 [Zhu 2025](../sources/zhu-2025-identification-non-canonical-peptides-mopepgen.md). 다만 비정규 참조로 DB를 키우면 위양성이 늘기 때문에, 엄격한 FDR 통제와 전사체·리보솜 프로파일링 같은 직교 증거가 권고되고 [Chong 2022](../sources/chong-2022-identification-tumor-antigens-immunopeptidomics.md), BamQuery는 동정된 MHC-I 펩타이드에 정상/종양 조직의 RNA 발현을 망라적으로 귀속시켜 여러 유전체 영역에서 유래하거나 정상조직에서도 풍부히 발현되는 후보를 걸러 actionable target을 구분한다 [Cuevas 2023](../sources/cuevas-2023-bamquery-proteogenomic-tool-explore-immunopeptidome.md).

**Cited**: [Zhu 2025](../sources/zhu-2025-identification-non-canonical-peptides-mopepgen.md), [Chong 2022](../sources/chong-2022-identification-tumor-antigens-immunopeptidomics.md), [Cuevas 2023](../sources/cuevas-2023-bamquery-proteogenomic-tool-explore-immunopeptidome.md)

### Q30. 공유 neoantigen(shared)을 주장하면 HLA 제한 조건과 확장성 제약은 무엇인가?
**A.** 로컬 근거에서 shared neoantigen 전략은 환자별 변이 대신 공통 driver mutation 유래 neoepitope를 쓰지만, HLA 제한이 본질적 제약이다. shared neoantigen 백신 phase 1에서는 공통 driver(대부분 KRAS) 유래 20개 shared neoantigen을 encoding하되 환자를 HLA-matched 종양 변이 기준으로 선별해야 했고, 이는 특정 neoepitope-HLA 쌍을 가진 환자에게만 off-the-shelf 적용이 가능함을 보여준다 [Rappaport 2024](../sources/rappaport-2024-shared-neoantigen-vaccine-checkpoint-blockade.md). immunopeptidomics 리뷰도 shared(특히 비정규) 항원이 off-the-shelf 표적으로 매력적이지만 종양특이성·검증을 충족해야 하며 HLA 대립유전자 커버리지가 검출 항원 집합을 좌우한다고 지적해, 확장성은 driver 변이 빈도와 HLA 다형성에 의해 제한됨을 시사한다 [Chong 2022](../sources/chong-2022-identification-tumor-antigens-immunopeptidomics.md).

**Cited**: [Rappaport 2024](../sources/rappaport-2024-shared-neoantigen-vaccine-checkpoint-blockade.md), [Chong 2022](../sources/chong-2022-identification-tumor-antigens-immunopeptidomics.md)

### Q31. WGS 기반 neoantigen prediction이 임상 표적이 되려면 어떤 추가 실험이 필요하다고 말하는가?
**A.** 로컬 근거는 WGS/WES 변이로부터 예측한 neoantigen을 임상 표적으로 옮기려면 in silico 예측만으로는 부족하고 **실제 presentation·면역원성 확인 실험**이 필요하다고 본다. [Huber 2025](../sources/huber-2025-comprehensive-proteogenomic-pipeline-neoantigen-discovery.md)의 NeoDisc 파이프라인은 예측 후보에 immunopeptidomics(HLA-I/II MS)를 결합하고 HLA LOH·antigen-processing(APPM) 결함을 '실패 모드'로 surface하며, [Shapiro 2025](../sources/shapiro-2025-sensitive-neoantigen-discovery-mutamome-guided-immunopeptidomics.md)는 MS 기반 immunopeptidomics를 순수 계산 예측 위에 얹는 검증 레이어로 위치시켜 실제 HLA 제시 펩타이드 확인을 추가 실험으로 제시한다. 임상 단계에서는 [Yarchoan 2024](../sources/yarchoan-2024-personalized-neoantigen-vaccine-pembrolizumab-advanced.md)처럼 ELISpot으로 neoantigen-특이 T세포 반응을 측정하고 TCRβ/scTCR로 종양 침윤 클론을 추적해 예측→제시→T세포 반응 루프를 닫아야 하며, 이 논문은 'encoding(예측) ≠ presentation'임을 명시해 제시·면역원성 검증의 필요성을 직접 강조한다.

**Cited**: [Huber 2025](../sources/huber-2025-comprehensive-proteogenomic-pipeline-neoantigen-discovery.md), [Shapiro 2025](../sources/shapiro-2025-sensitive-neoantigen-discovery-mutamome-guided-immunopeptidomics.md), [Yarchoan 2024](../sources/yarchoan-2024-personalized-neoantigen-vaccine-pembrolizumab-advanced.md)

### Q32. 환자 분류(subtype)에서 유전체 기반 vs 단백질/인산화 기반 subtype은 어떤 차이를 보이는가?
**A.** 로컬 논문들은 단백/인산화 기반 subtype이 유전체 경계를 가로질러 형성되며 genomic subtype과 1:1로 겹치지 않는다고 일관되게 보고한다. [Jayavelu 2022](../sources/jayavelu-2022-proteogenomic-subtypes-acute-myeloid-leukemia.md)는 AML 252명에서 5개 proteomic subtype을 정의했는데 어느 것도 특정 genomic aberration에만 묶이지 않았고, 그중 Mito-AML은 오직 proteome에서만 잡히면서 venetoclax 반응·예후를 갈랐다. [Petralia 2024](../sources/petralia-2024-pan-cancer-proteogenomics-characterization-tumor-immunity.md) 역시 CPTAC pan-cancer에서 DNA 변이 경계를 넘는 7개 immune subtype을 단백/인산화·kinase 활성으로 정의했고, [Chen 2020](../sources/chen-2020-proteogenomics-non-smoking-lung-cancer-east.md)은 폐선암 proteomic subtyping이 임상 병기와 무관하게 일부 조기 종양을 'late-like'로 재분류함을 보였다. 즉 유전체 기반 분류가 놓치는 발현·신호 상태를 단백/인산화 subtype이 추가로 포착한다.

**Cited**: [Jayavelu 2022](../sources/jayavelu-2022-proteogenomic-subtypes-acute-myeloid-leukemia.md), [Petralia 2024](../sources/petralia-2024-pan-cancer-proteogenomics-characterization-tumor-immunity.md), [Chen 2020](../sources/chen-2020-proteogenomics-non-smoking-lung-cancer-east.md)

### Q33. driver가 같아도 단백질/인산화 상태가 달라지는 사례를 논문은 보여주는가?
**A.** 그렇다. 로컬 근거는 동일 driver를 공유해도 단백/인산화 상태가 달라지는 사례를 보여준다. [Chen 2020](../sources/chen-2020-proteogenomics-non-smoking-lung-cancer-east.md)은 폐선암에서 MAPK 경로 활성이 EGFR-mutant와 EGFR-WT 종양 모두에서 폭넓게 변동하고(KRAS-mutant·EGFR-WT가 종종 high-MAPK), RNA-단백 상관이 낮아(median gene-wise Spearman 0.14) 유전형만으로 신호 상태가 결정되지 않음을 직접 보였다. [Jayavelu 2022](../sources/jayavelu-2022-proteogenomic-subtypes-acute-myeloid-leukemia.md)는 AML proteomic subtype 중 어느 것도 특정 genomic aberration에 배타적으로 대응하지 않았고 proteome에서만 드러나는 Mito-AML이 별도 예후를 가져, 같은 유전 변이라도 단백 수준 상태가 분기함을 시사한다.

**Cited**: [Chen 2020](../sources/chen-2020-proteogenomics-non-smoking-lung-cancer-east.md), [Jayavelu 2022](../sources/jayavelu-2022-proteogenomic-subtypes-acute-myeloid-leukemia.md)

### Q34. ppQTL/pQTL을 보고하는가? 있다면 cis/trans와 해석은 무엇인가?
**A.** 로컬 근거는 명시적 ppQTL보다는 germline/somatic 변이가 단백 수준에 미치는 cis-효과(pQTL 성격)를 보고한다. [Chen 2026](../sources/chen-2026-global-impact-germline-structural-variation-cancer-proteome.md)은 CPTAC pan-cancer(1,637명)에서 germline structural variation이 cis-regulatory 방식으로 단백체에 작용함을 정량화해, 25,781개 LoF SV가 512 유전자에서 cis-correlated 단백 저발현을 만들고 364개 recurrent gene 중 129개(17%)가 mRNA·단백 모두에서 같은 방향의 concordant cis-조절을 보였으며 일부는 단백 변화가 더 우세한(mRNA로는 안 잡히는) 효과를 보였다. [Chen 2020](../sources/chen-2020-proteogenomics-non-smoking-lung-cancer-east.md)은 폐선암에서 TP53 mutation을 'eQTL/pQTL hotspot'으로 직접 기술하며 cell-cycle 단백·TOP2A 증가, KIT 감소, DNA 손상반응 단백 인산화 증가와 연결했다. 따라서 cis 해석이 중심이며, trans-수준 ppQTL 카탈로그를 표방한 로컬 논문은 확인되지 않았다.

**Cited**: [Chen 2026](../sources/chen-2026-global-impact-germline-structural-variation-cancer-proteome.md), [Chen 2020](../sources/chen-2020-proteogenomics-non-smoking-lung-cancer-east.md)

### Q35. ppQTL이 면역 phenotype 또는 치료 반응과 연결되는가?
**A.** 직접적인 'ppQTL→반응' 연결을 표방한 로컬 논문은 드물지만, 단백/인산화 기반 상태가 면역 phenotype·치료 반응과 연결되는 근거는 있다. [Petralia 2024](../sources/petralia-2024-pan-cancer-proteogenomics-characterization-tumor-immunity.md)는 단백·인산화·kinase 활성으로 정의한 immune subtype 중 CD8+/IFNG+ 아형이 OAK 시험의 atezolizumab arm에서 PFS 개선을 예측했으나 docetaxel arm에서는 그렇지 않아 면역 단백 상태가 ICI 반응과 특이적으로 연결됨을 보였다. [Zhang 2023](../sources/zhang-2023-proteogenomics-clear-cell-renal-response-tyrosine-kinase-inhibitor.md)도 ccRCC에서 proteome-추론 immune cluster(T세포 침윤/cold/progenitor)가 sunitinib 반응 비율과 연관되고 progenitor 침윤군이 TGFB1-연관·최저 반응을 보임을 보고했다. 다만 이들은 면역 단백 phenotype↔반응 연관이며 phosphosite 유전변이좌(ppQTL) 자체를 반응에 연결한 것은 아니다.

**Cited**: [Petralia 2024](../sources/petralia-2024-pan-cancer-proteogenomics-characterization-tumor-immunity.md), [Zhang 2023](../sources/zhang-2023-proteogenomics-clear-cell-renal-response-tyrosine-kinase-inhibitor.md)

### Q36. 데이터가 공용 코호트(CPTAC 등)인가, 기관 코호트인가, 임상시험 코호트인가?
**A.** 세 유형이 모두 로컬 코퍼스에 존재한다. 공용 코호트로는 [Chen 2026](../sources/chen-2026-global-impact-germline-structural-variation-cancer-proteome.md)과 [Petralia 2024](../sources/petralia-2024-pan-cancer-proteogenomics-characterization-tumor-immunity.md)이 CPTAC pan-cancer 1,000여 종양의 WGS/RNA/proteome/phospho를 harmonized pipeline으로 재분석한 사례다. 기관(단일센터) 코호트로는 [Chen 2020](../sources/chen-2020-proteogenomics-non-smoking-lung-cancer-east.md)의 대만 National Taiwan University Hospital 비흡연 폐선암 103명, [Zhang 2023](../sources/zhang-2023-proteogenomics-clear-cell-renal-response-tyrosine-kinase-inhibitor.md)의 중국 단일센터 ccRCC 115명이 있다. 임상시험 코호트로는 [Yarchoan 2024](../sources/yarchoan-2024-personalized-neoantigen-vaccine-pembrolizumab-advanced.md)의 GT-30(NCT04251117) phase 1/2 HCC 36명이 해당한다.

**Cited**: [Chen 2026](../sources/chen-2026-global-impact-germline-structural-variation-cancer-proteome.md), [Petralia 2024](../sources/petralia-2024-pan-cancer-proteogenomics-characterization-tumor-immunity.md), [Chen 2020](../sources/chen-2020-proteogenomics-non-smoking-lung-cancer-east.md), [Yarchoan 2024](../sources/yarchoan-2024-personalized-neoantigen-vaccine-pembrolizumab-advanced.md)

### Q37. 임상시험 코호트라면 arm/병용/라인 구성과 라벨 정의는 무엇인가?
**A.** 로컬 임상시험 코호트는 arm/라인/라벨 정의를 비교적 명확히 기술한다. [Yarchoan 2024](../sources/yarchoan-2024-personalized-neoantigen-vaccine-pembrolizumab-advanced.md)의 GT-30은 단일-arm open-label phase 1/2로, multi-TKI(주로 lenvatinib) 진행 후 2차 라인 진입 시점의 진행성 HCC 환자에게 개인맞춤 neoantigen 백신(GNOS-PV02 + pIL12)을 표준용량 pembrolizumab에 병용했고, 반응 라벨은 RECIST 1.1 기반 ORR/CR로 정의했다(대조군 없이 historical pembrolizumab 12-18%와 비교). 치료-정의 코호트인 [Zhang 2023](../sources/zhang-2023-proteogenomics-clear-cell-renal-response-tyrosine-kinase-inhibitor.md)은 수술 후 sunitinib을 받은 ccRCC에서 RECIST CR/PR을 responder(n=27), SD/PD를 non-responder(n=88)로 라벨링했다. 즉 단일-arm·병용·2차라인 구성과 RECIST 기반 반응 라벨이 핵심이다.

**Cited**: [Yarchoan 2024](../sources/yarchoan-2024-personalized-neoantigen-vaccine-pembrolizumab-advanced.md), [Zhang 2023](../sources/zhang-2023-proteogenomics-clear-cell-renal-response-tyrosine-kinase-inhibitor.md)

### Q38. MSI-H/dMMR 같은 특수 집단은 별도로 다루는가(heterogeneity 관점 포함)?
**A.** 로컬 근거는 MSI-H/dMMR을 단일 범주로 보지 않고 내부 이질성을 별도로 다룬다. [Yang 2021](../sources/yang-2021-msih-gastric-cancer-heterogeneity-worse-survival.md)은 TCGA와 아시아 검증 코호트의 MSI-H 위암을 consensus clustering으로 MSI-H1/MSI-H2 두 아형으로 나눠, 면역억제 특성이 강한 MSI-H1이 더 나쁜 예후를 보임을 보였고 'MSI-H=좋은 예후/일관된 ICI 감수성'이라는 단축 가정을 직접 반박한다. 즉 MSI-H 내에서도 면역 프로그램 차이로 heterogeneity가 존재하며 더 세밀한 immune annotation이 필요하다는 입장이다.

**Cited**: [Yang 2021](../sources/yang-2021-msih-gastric-cancer-heterogeneity-worse-survival.md)

### Q39. HLA LOH/antigen presentation loss를 WGS만으로 추정하는가, 단백질/표현형 근거가 있는가?
**A.** 로컬 근거는 HLA LOH를 WGS만으로 추정하는 방법과, 단백/표현형 수준 근거를 모두 제시한다. [McGranahan 2017](../sources/mcgranahan-2017-allele-specific-hla-loss-lung-cancer.md)은 LOHHLA로 종양 시퀀싱에서 allele-specific HLA copy-number loss를 추론(NSCLC의 ~40%, subclonal·공간이질적)하는 시퀀싱 기반 접근을 도입했다. 그러나 [Huber 2025](../sources/huber-2025-comprehensive-proteogenomic-pipeline-neoantigen-discovery.md)는 HLA LOH와 antigen-processing(APPM) 결함을 neoantigen 해석의 'failure mode'로 surface하면서 immunopeptidomics로 실제 HLA 제시를 확인해 시퀀싱 추정을 단백 수준에서 보강한다. 또 [Chen 2026](../sources/chen-2026-global-impact-germline-structural-variation-cancer-proteome.md)은 LoF SV가 MHC class I antigen binding·antigen processing 단백의 저발현과 cis-연관됨을 정량 단백체로 보여, 항원제시 손실을 단백 측정으로도 뒷받침한다.

**Cited**: [McGranahan 2017](../sources/mcgranahan-2017-allele-specific-hla-loss-lung-cancer.md), [Huber 2025](../sources/huber-2025-comprehensive-proteogenomic-pipeline-neoantigen-discovery.md), [Chen 2026](../sources/chen-2026-global-impact-germline-structural-variation-cancer-proteome.md)

### Q40. immune exclusion(TGF-β/ECM/CAF) 신호를 어떤 레이어로 측정하는가?
**A.** 로컬 근거는 immune exclusion(TGF-β/ECM/CAF) 신호를 주로 전사체와 단백/인산화 레이어, 그리고 공간 위치 정보로 측정한다. [Mariathasan 2018](../sources/mariathasan-2018-tgfb-pdl1-blockade-tcell-exclusion.md)은 요로상피암 atezolizumab 코호트에서 transcriptomic fibroblast-연관 TGF-β signature와 CD8 T세포의 peritumoral stroma 잔류(공간 phenotype)로 exclusion을 정의했고, [Tauriello 2018](../sources/tauriello-2018-tgf-drives-immune-evasion-genetically.md)은 microsatellite-stable 대장암 모델에서 TGF-β-activated stroma와 T세포 배제를 기능적으로 측정했다. 단백/인산화 레이어에서는 [Petralia 2024](../sources/petralia-2024-pan-cancer-proteogenomics-characterization-tumor-immunity.md)가 CPTAC proteome·phospho·kinase 활성으로 fibroblast/TGF-β immune subtype을 정의해, 같은 exclusion 축을 다층(전사체+단백+공간)으로 잡아낸다.

**Cited**: [Mariathasan 2018](../sources/mariathasan-2018-tgfb-pdl1-blockade-tcell-exclusion.md), [Tauriello 2018](../sources/tauriello-2018-tgf-drives-immune-evasion-genetically.md), [Petralia 2024](../sources/petralia-2024-pan-cancer-proteogenomics-characterization-tumor-immunity.md)

### Q41. myeloid suppression(MDSC/TAM) 관련 신호는 어떤 근거로 제시되는가?
**A.** 로컬 근거에서 myeloid 억제 신호는 주로 단일세포·공간전사체와 단백질(CyTOF/IMC) 층에서 제시된다. [Ghosh 2026](../sources/ghosh-2026-chemokine-defined-macrophage-niches-establish-spatial.md)는 lung cancer에서 tumor 내 Ccl2+ interstitial macrophage가 protumorigenic Ly6c2+Fn1+Vcan+ recruited macrophage를 동원하고 종양배출림프절의 Ly6C+CD11b+ moDC가 면역억제 APC로 작동함을 scRNA/spatial로 보였고, [Vallée 2025](../sources/valle-2025-pan-cancer-convergence-tumour-immune-microenvironment-motifs.md)는 pan-cancer CyTOF/IMC에서 CD163+HLA-DR- 억제성 macrophage와 'CD38+ TAM barrier' motif를 반복 관찰 신호로 정리한다. proteome 기반으로는 [Zhang 2023](../sources/zhang-2023-proteogenomics-clear-cell-renal-response-tyrosine-kinase-inhibitor.md)이 단백체로 추정한 'progenitor-cell infiltrated' 면역 클러스터(platelet/coagulation 특성, 최저 반응률)를 myeloid 편향 억제 환경의 간접 근거로 제시한다.

**Cited**: [Ghosh 2026](../sources/ghosh-2026-chemokine-defined-macrophage-niches-establish-spatial.md), [Vallée 2025](../sources/valle-2025-pan-cancer-convergence-tumour-immune-microenvironment-motifs.md), [Zhang 2023](../sources/zhang-2023-proteogenomics-clear-cell-renal-response-tyrosine-kinase-inhibitor.md)

### Q42. T cell exhaustion signature는 어떤 층에서 측정되는가(전사체/단백질/기능)?
**A.** T cell exhaustion signature는 로컬 논문에서 단백질 층(질량세포측정)과 전사체 추정 층 양쪽에서 측정된다. [Vallée 2025](../sources/valle-2025-pan-cancer-convergence-tumour-immune-microenvironment-motifs.md)는 CyTOF에서 PD-1+TIM-3+CD39+ 같은 exhausted CD8+ T세포 아집단을 단백질 마커 조합으로 직접 정량하는 사례를 반복 motif로 정리하고, [Helmink 2020](../sources/helmink-2020-b-cells-tertiary-lymphoid-structures.md)도 mass cytometry와 다중 IF로 CD8+/FOXP3+ T세포 상태를 표현형 수준에서 측정한다. 단백체-only 코호트인 [Zhang 2023](../sources/zhang-2023-proteogenomics-clear-cell-renal-response-tyrosine-kinase-inhibitor.md)에서는 별도 기능 측정 없이 proteome로 추정한 'T-cell infiltrated' 클러스터로만 잡히므로, 기능적 소진 여부는 단백/유세포 마커가 함께 있을 때 더 단정할 수 있다.

**Cited**: [Vallée 2025](../sources/valle-2025-pan-cancer-convergence-tumour-immune-microenvironment-motifs.md), [Helmink 2020](../sources/helmink-2020-b-cells-tertiary-lymphoid-structures.md), [Zhang 2023](../sources/zhang-2023-proteogenomics-clear-cell-renal-response-tyrosine-kinase-inhibitor.md)

### Q43. B cell/TLS 시그니처가 feature로 등장하는가? 등장한다면 어떤 근거가 가장 강한가?
**A.** B cell/TLS 시그니처는 feature로 분명히 등장하며, 가장 강한 근거는 [Helmink 2020](../sources/helmink-2020-b-cells-tertiary-lymphoid-structures.md)이다. 이 논문은 neoadjuvant melanoma ICB에서 T세포가 아니라 B세포 유전자(MZB1, JCHAIN, IGLL5 등)가 반응자에서 차등발현 상위를 차지하고, 성숙 TLS(CD21+ FDC·CD23+ germinal-center B세포) 밀도와 BCR 클론성이 반응과 연결됨을 여러 코호트·TCGA 생존에서 재현했다. 위암 맥락에서는 [Hu 2024](../sources/hu-2024-tertiary-lymphoid-structure-associated-b-cells.md)가 TLS 연관 B세포가 CXCL13+CD103+CD8+ Trm를 lymphotoxin-α/TNFR2 축으로 강화해 항-PD-1 반응을 높인다는 기전적 근거를 더한다.

**Cited**: [Helmink 2020](../sources/helmink-2020-b-cells-tertiary-lymphoid-structures.md), [Hu 2024](../sources/hu-2024-tertiary-lymphoid-structure-associated-b-cells.md)

### Q44. 논문이 TLS/neoantigen을 직접 다루지 않으면, 위키에서 어떤 연결은 “추론”으로만 남겨야 하는가?
**A.** 논문이 TLS/neoantigen을 직접 측정하지 않으면, 그 항원 특이성·인과 연결은 위키에서 '추론'으로만 남겨야 한다. [Helmink 2020](../sources/helmink-2020-b-cells-tertiary-lymphoid-structures.md)조차 B세포·TLS와 반응의 인과는 환자 B세포 고갈 실험이 없어 'inferred, not proven'이라고 명시하고, 반응자 B세포가 어떤 종양항원(neoantigen 대 self-antigen)을 인지하는지는 보여주지 못해 neoantigen 연결을 implicit로 남긴다. 마찬가지로 [Tanaka 2024](../sources/tanaka-2024-proteogenomic-characterization-primary-colorectal-cancer.md)는 전이에서 항원제시 기구 억제(immune-cold)를 단백체로 관찰할 뿐 neoantigen 제시 자체를 측정하지 않으므로, 'neoantigen 가용성 저하'는 관찰이 아닌 해석적 추론으로 표기해야 한다.

**Cited**: [Helmink 2020](../sources/helmink-2020-b-cells-tertiary-lymphoid-structures.md), [tanaka-2024-proteogenomic-characterization-primary-colorectal-cancer](../sources/tanaka-2024-proteogenomic-characterization-primary-colorectal-cancer.md)

### Q45. signaling 결과가 타깃 제안으로 이어질 때 약물 가능성/임상 근거를 무엇으로 판단할 것인가?
**A.** signaling 결과가 타깃 제안으로 이어질 때, 약물 가능성·임상 근거는 '단백/인산화 활성 → 외부 기능 증거(유전자 스크린·약물반응·MHC 결합) → 실제 검증/임상개발 상태'로 판단해야 한다. [Savage 2024](../sources/savage-2024-pan-cancer-proteogenomics-expands-landscape-therapeutic.md)는 CPTAC 단백체의 과발현/과활성 신호를 cell-line genetic screen·drug-response 및 MHC 결합 예측과 통합해 druggable dependency와 'public' neoantigen(예: mutant KRAS)을 우선순위화한다. [Lee 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md)은 GRK2/AURKB phospho 신호를 barasertib·βARK 저해제 시너지(in vitro)로 검증하고 ITGB8을 개발 중 ADC(SGN-B6A) 표적으로 연결하되 시너지는 세포주/organoid 수준임을 명시하며, [Zhang 2023](../sources/zhang-2023-proteogenomics-clear-cell-renal-response-tyrosine-kinase-inhibitor.md)은 KSEA로 MTOR·MAP2K1 활성을 비반응자 신호로 지목한다. 즉 신호 → 표적성 근거 단계와 임상 검증 수준(전임상/임상)을 구분해 기록해야 한다.

**Cited**: [Savage 2024](../sources/savage-2024-pan-cancer-proteogenomics-expands-landscape-therapeutic.md), [Lee DK 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md), [Zhang 2023](../sources/zhang-2023-proteogenomics-clear-cell-renal-response-tyrosine-kinase-inhibitor.md)

### Q46. 내성 기전 주장에 대해 “관찰 기반”과 “인과 기반(perturbation)”을 어떻게 분리해 기록할 것인가?
**A.** 내성 기전은 '관찰 기반(상관)'과 '인과 기반(perturbation)'을 분리해 기록해야 하며, 로컬 논문들이 두 단계를 명확히 구분한다. [Chen 2026](../sources/chen-2026-global-impact-germline-structural-variation-cancer-proteome.md)은 germline SV→mRNA→단백 cis-상관을 먼저 관찰하고, 이를 DepMap essentiality·생존과 교차 검증(FABP5, NEDD1, TOP2A)해 단순 상관과 기능적 의존성을 구분한다. [Lee 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md)은 estrogen/GRK2·ITGB8·AURKB를 비반응 상관으로 관찰한 뒤 βARK 저해제·barasertib 병용과 ITGB8 과발현 실험으로 인과를 검증하고, [Zhang 2023](../sources/zhang-2023-proteogenomics-clear-cell-renal-response-tyrosine-kinase-inhibitor.md)도 7q gain–저생존 상관을 LAMTOR4 등의 S6K 인산화 증가 실험으로 mTORC1 활성화라는 인과로 끌어올린다. 따라서 위키는 관찰된 연관과 perturbation으로 입증된 인과를 별도 항목으로 표기해야 한다.

**Cited**: [Chen 2026](../sources/chen-2026-global-impact-germline-structural-variation-cancer-proteome.md), [Lee DK 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md), [Zhang 2023](../sources/zhang-2023-proteogenomics-clear-cell-renal-response-tyrosine-kinase-inhibitor.md)

### Q47. 한 논문에서 endpoint(생존/반응/재발)가 여러 개인 경우, Cancer Multiomics 요약은 무엇을 우선할까?
**A.** 한 논문에 endpoint가 여러 개면, Cancer Multiomics 요약은 그 논문이 일차 분석축으로 삼은 치료반응 endpoint를 우선하고 생존(재발/전이)은 보조 검증으로 둔다. [Lee 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md)은 NAC pCR을 일차 결과로 5개 저항인자 모델(AUC 0.946)을 세우고 RFS/OS와 전이 사례는 외부·후속 검증으로 배치하며, [Zhang 2023](../sources/zhang-2023-proteogenomics-clear-cell-renal-response-tyrosine-kinase-inhibitor.md)도 RECIST 반응(CR/PR vs SD/PD)을 주 분류 endpoint로 두고 VHL·7q와 생존을 보강 근거로 쓴다. 반면 [Tanaka 2024](../sources/tanaka-2024-proteogenomic-characterization-primary-colorectal-cancer.md)처럼 약물반응이 없는 연구는 원발–전이 진행 자체가 일차 endpoint가 되므로, 요약은 '과제 의사결정(반응 예측)에 가장 직접 연결되는 endpoint'를 기준으로 정렬하는 것이 합리적이다.

**Cited**: [Lee DK 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md), [Zhang 2023](../sources/zhang-2023-proteogenomics-clear-cell-renal-response-tyrosine-kinase-inhibitor.md), [tanaka-2024-proteogenomic-characterization-primary-colorectal-cancer](../sources/tanaka-2024-proteogenomic-characterization-primary-colorectal-cancer.md)

### Q48. Cancer Multiomics 과제 deliverable(예측모델/바이오마커/통합 파이프라인) 중 어디에 직접 연결되는가?
**A.** 로컬 논문들은 과제 deliverable 중 예측모델·바이오마커·통합 파이프라인 모두에 직접 연결된다. [Lee 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md)은 WGS/RNA/단백체/인산화 통합으로 5-인자 non-pCR 예측모델(AUC 0.946)과 druggable target(AURKB·GRK2·ITGB8 ADC)을 함께 내놓아 예측모델+바이오마커+표적의 세 deliverable을 동시에 채우고, [Zhang 2023](../sources/zhang-2023-proteogenomics-clear-cell-renal-response-tyrosine-kinase-inhibitor.md)은 proteome-only 18-단백 RF(AUC 0.85)와 multi-omics RF(AUC 0.98)로 예측모델/바이오마커 deliverable에 직결된다. [Savage 2024](../sources/savage-2024-pan-cancer-proteogenomics-expands-landscape-therapeutic.md)는 CPTAC pan-cancer를 표적 portal로 정리한 통합 파이프라인/타깃 카탈로그형 deliverable을 대표한다.

**Cited**: [Lee DK 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md), [Zhang 2023](../sources/zhang-2023-proteogenomics-clear-cell-renal-response-tyrosine-kinase-inhibitor.md), [Savage 2024](../sources/savage-2024-pan-cancer-proteogenomics-expands-landscape-therapeutic.md)

### Q49. Slack 공유용 “한 줄 요약”에 꼭 포함해야 하는 요소는 무엇인가(암종/레이어/핵심 주장)?
**A.** Slack 한 줄 요약에는 최소 (1) 암종/코호트, (2) 측정 레이어(WGS/RNA/proteome/phospho 중 무엇), (3) 핵심 주장(반응/내성 결과 또는 표적)이 들어가야 한다. 예컨대 [Lee 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md)은 '한국인 TNBC 50명 WES+RNA+단백체+인산화 → GRK2·ITGB8·AURKB 기반 NAC 비반응 예측(AUC 0.946)'처럼 세 요소가 모두 담겨야 정보가 살고, [Zhang 2023](../sources/zhang-2023-proteogenomics-clear-cell-renal-response-tyrosine-kinase-inhibitor.md)도 'ccRCC 115명, 단백체+인산화, 7q gain→mTORC1 sunitinib 내성'처럼 암종·레이어·주장을 묶어야 한다. 가능하면 검증 수준(세포주/임상)이나 endpoint를 한 단어로 덧붙이면 과대해석을 막을 수 있다.

**Cited**: [Lee DK 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md), [Zhang 2023](../sources/zhang-2023-proteogenomics-clear-cell-renal-response-tyrosine-kinase-inhibitor.md)

### Q50. Slack 메시지는 어떤 구조(문제→핵심 결과→과제 연결)가 가장 전달력이 좋은가?
**A.** Slack 메시지는 '문제(왜 보는가) → 핵심 결과(무엇을 찾았나) → 과제 연결(우리에 무슨 의미)' 3단 구조가 전달력이 가장 좋고, 이는 로컬 proteogenomics 논문의 요약 구성과 일치한다. [Lee 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md)과 [Tanaka 2024](../sources/tanaka-2024-proteogenomic-characterization-primary-colorectal-cancer.md)는 모두 'TNBC NAC 내성/CRC 전이라는 임상 문제 → 통합 오믹스로 도출한 핵심 결과(저항인자·진행 시그니처) → 과제 활용(예측모델·표적·환자 stratification)' 흐름으로 정리되어 있다. [Savage 2024](../sources/savage-2024-pan-cancer-proteogenomics-expands-landscape-therapeutic.md)도 'mRNA로 안 보이는 표적이라는 문제 → 단백/인산화 기반 표적 우선순위 결과 → 표적 portal/후속 검증 연결'로 같은 구조를 따르므로, 결과만 나열하기보다 문제·과제 연결을 양 끝에 붙이는 편이 낫다.

**Cited**: [Lee DK 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md), [tanaka-2024-proteogenomic-characterization-primary-colorectal-cancer](../sources/tanaka-2024-proteogenomic-characterization-primary-colorectal-cancer.md), [Savage 2024](../sources/savage-2024-pan-cancer-proteogenomics-expands-landscape-therapeutic.md)

### Q51. “당장 적용 가능한 아이디어” 1개를 뽑는 기준은 무엇인가?
**A.** "당장 적용 가능"의 기준은 (i) 우리 4축(WGS/RNA/proteome/phospho)으로 재현 가능한 분석 단계인지, (ii) 표적이 단순 상관이 아니라 in-vitro/organoid 기능검증까지 닿아 있는지로 본다. 예컨대 [Lee 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md)은 한국인 TNBC 50명에서 5개 비반응인자를 묶은 로지스틱 모델이 non-pCR을 AUC 0.946으로 예측하고, GRK2 inhibitor+paclitaxel(Bliss 8.08)·Aurora B inhibitor barasertib를 환자 유래 organoid에서 검증해 "한미암 코호트에 바로 옮길 수 있는" 분석·표적 형태를 제시한다. [Xu 2026](../sources/xu-2026-proteogenomic-characterization-reveals-subtype-specific-therapeutic.md)처럼 subtype별로 trastuzumab/T-DM1 같은 기존 승인약을 연결하는 결과도 임상 라인이 이미 존재해 적용 우선순위가 높다. 즉 "기존 약·검증된 표적·우리 데이터로 재현 가능" 세 조건을 충족할수록 actionable로 뽑는다.

**Cited**: [Lee DK 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md), [Xu S 2026](../sources/xu-2026-proteogenomic-characterization-reveals-subtype-specific-therapeutic.md)

### Q52. “조심해야 할 caveat” 1개를 뽑는 기준은 무엇인가?
**A.** "조심해야 할 caveat"는 한 layer의 신호가 다른 layer나 임상 해석으로 자동 연결된다고 단정할 때 가장 잘 깨지는 지점을 고른다. 대표적으로 [Chen 2026](../sources/chen-2026-global-impact-germline-structural-variation-cancer-proteome.md)은 recurrent SV-altered gene 364개 중 mRNA·protein이 함께 일치하는 cis-effect는 약 17%뿐이고 33%는 protein-only라고 보고해, RNA 변화만으로 단백 결과를 추정하는 것이 위험함을 정량한다(자매 논문 [Chen 2023](../sources/chen-2023-global-impact-somatic-structural-variation-cancer-proteome.md)도 SV→단백 반영 ~25%). 신항원 쪽에서는 [Huber 2025](../sources/huber-2025-comprehensive-proteogenomic-pipeline-neoantigen-discovery.md)가 HLA LOH·항원제시기구(APPM) 결함을 "failure mode"로 명시해, 예측된 neoantigen이 실제로 제시되지 않을 수 있음을 경고한다. 따라서 caveat는 layer 간 불일치율·결측·제시 실패처럼 결론을 뒤집을 수 있는 가정에서 1개를 택한다.

**Cited**: [Chen 2026](../sources/chen-2026-global-impact-germline-structural-variation-cancer-proteome.md), [Chen 2023](../sources/chen-2023-global-impact-somatic-structural-variation-cancer-proteome.md), [Huber 2025](../sources/huber-2025-comprehensive-proteogenomic-pipeline-neoantigen-discovery.md)

### Q53. 수치(단백질 수/사이트 수/샘플 수)가 main vs supplement에서 다르면 어떤 값을 택할 것인가?
**A.** 기본 원칙은 본문(main)에 보고된 headline 수치를 노드의 대표값으로 쓰고, supplement의 더 정밀한/세분화된 수치는 괄호나 하위 bullet로 함께 적어 둘의 출처를 분리 표기하는 것이다. 예를 들어 [Chang 2026](../sources/chang-2026-integrative-proteogenomics-gastric-cancer-taiwan.md)은 본문에서 단백체 ">10,000 protein groups", phosphoproteome "30,000 phosphosites"처럼 반올림된 값을 제시하므로 대표값은 이를 따르되 정확한 식별 수는 supplement 기준으로 보강한다. [Lee 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md)처럼 baseline n=41 vs paired residual protein n=22(수집 31) 같이 샘플 수가 단계별로 다른 경우, 분석에 실제 쓰인 paired 수를 우선하고 collected 수는 병기한다. 즉 "분석에 사용된 정의"가 무엇인지로 값을 택하고, main/supplement가 다르면 둘 다 적되 어느 쪽을 대표로 삼았는지 명시한다.

**Cited**: [chang-2026-integrative-proteogenomics-gastric-cancer-taiwan](../sources/chang-2026-integrative-proteogenomics-gastric-cancer-taiwan.md), [Lee DK 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md)

### Q54. Cancer Multiomics 표준 추출 체크리스트에 포함해야 할 최소 필드는 무엇인가(치료/레이어/공개/방법)?
**A.** 최소 필드는 topic hub 표준 체크리스트대로 (1) 치료 맥락: 암종/치료제 class/라인/반응 라벨(Primary·Acquired 등)/샘플 타이밍, (2) 데이터 레이어: WGS·WES/RNA-seq/proteome/phospho/acetyl/immunopeptidomics/spatial 중 무엇을 실제로 측정했는가, (3) 데이터 공개: raw/processed/supplement/code 접근 경로(Data Availability 기준)를 고정한다. [Lee 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md)은 'anthracycline+taxane neoadjuvant, stage II–III TNBC, baseline+residual paired, WES+RNA+TMT global+phospho'처럼 치료·레이어 필드가 한 문장에 다 들어가는 좋은 예다. [Chang 2026](../sources/chang-2026-integrative-proteogenomics-gastric-cancer-taiwan.md)은 라이선스(BMJ proprietary)까지, [Huber 2025](../sources/huber-2025-comprehensive-proteogenomic-pipeline-neoantigen-discovery.md)는 입력 데이터(WES/RNA/immunopeptidomics)와 코드 가용성을 명시해 공개 필드의 기준점이 된다. 모르는 필드는 비워두지 말고 "PDF 확인 필요"로 표기한다.

**Cited**: [Lee DK 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md), [chang-2026-integrative-proteogenomics-gastric-cancer-taiwan](../sources/chang-2026-integrative-proteogenomics-gastric-cancer-taiwan.md), [Huber 2025](../sources/huber-2025-comprehensive-proteogenomic-pipeline-neoantigen-discovery.md)

### Q55. 논문을 읽고 반드시 업데이트해야 하는 페이지는 무엇인가(토픽 허브, 소스 페이지, 컨셉 페이지)?
**A.** 논문 1편을 읽으면 최소 3종 페이지를 갱신한다: (a) source page(`wiki/sources/<slug>.md`)에 Summary·Key Points·치료/레이어/공개 메타를 채우고, (b) 해당 주제 topic hub([Cancer Multiomics Literature](../topics/cancer-multiomics-literature.md))의 분류 목록에 한 줄 링크+핵심 포인트를 추가하며, (c) 그 논문이 기존 개념을 확장·반증하면 concept/synthesis 페이지를 갱신한다. 예컨대 [Lee 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md)은 source page에 full-text 근거를 적재하는 동시에 'response/내성 예측' 축의 hub 항목과 acquired-resistance 해석 노드에 반영되어야 한다. [Chen 2026](../sources/chen-2026-global-impact-germline-structural-variation-cancer-proteome.md)처럼 layer 일치율 같은 durable한 수치는 concept 페이지로 승격해 다른 질문에서 재인용되게 한다. 즉 source(사실)→hub(목록·공유)→concept(재사용 가능한 일반화) 세 층을 함께 업데이트한다.

**Cited**: [Lee DK 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md), [Chen 2026](../sources/chen-2026-global-impact-germline-structural-variation-cancer-proteome.md)

### Q56. Cancer Multiomics 하위 페이지와 source page 사이의 역할 분리를 어떻게 유지할 것인가?
**A.** 역할 분리의 원칙은 source page는 "논문 단위 사실 컨테이너"(Summary, Key Points, 치료/레이어/공개 메타, 정확한 수치)로 자기완결적이어야 하고, Cancer Multiomics 하위 페이지(또는 topic hub 항목)는 "과제 4축 관점의 분류·연결·Slack용 핵심 포인트"만 담아 중복 본문을 두지 않는 것이다. topic hub가 명시하듯 "각 논문은 하위 페이지로 정리하고, hub에는 분류별 링크와 핵심 포인트만 남긴다". 예를 들어 [Chang 2026](../sources/chang-2026-integrative-proteogenomics-gastric-cancer-taiwan.md)의 7개 mutational signature·CDK4 hub 같은 상세 수치는 source page에 두고, hub에서는 'WGS-단백체 통합' 축에 한 줄로 연결한다. [Lee 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md)도 동일하게 상세는 source, 'response 예측' 분류와 다음 질문은 hub/analysis 쪽에 둔다. 하위 페이지가 source의 수치를 재서술하기 시작하면 분리가 깨진 신호로 보고 링크로 되돌린다.

**Cited**: [chang-2026-integrative-proteogenomics-gastric-cancer-taiwan](../sources/chang-2026-integrative-proteogenomics-gastric-cancer-taiwan.md), [Lee DK 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md)

### Q57. source page에 “Cancer Multiomics relevance”를 추가할지, 하위 페이지만 유지할지 어떤 기준으로 결정할까?
**A.** source page에 "Cancer Multiomics relevance" 섹션을 추가할지 여부는 그 논문이 우리 과제 4축(WGS/RNA/proteome/phospho 통합, 신항원, 반응예측)에 직접 닿는지로 결정한다. 닿으면 relevance를 붙여 어떤 축·어떤 질문에 쓰이는지 한 줄로 명시하고, 순수 도구/방법론이면 하위 분류만 유지한다. 예컨대 [Huber 2025](../sources/huber-2025-comprehensive-proteogenomic-pipeline-neoantigen-discovery.md)는 genomics→HLA-bound peptide 근거를 잇고 APPM/HLA-LOH 실패모드를 가시화해 'Practical Relevance' 섹션이 정당화되며 신항원·면역 축으로 연결된다. [PEXMap(Awasthi 2026)](../sources/awasthi-2026-pexmap-proteogenomic-exon-isoform-mapping.md)도 isoform-level proteogenomics 통합 축(cm_axis: integration)에 들어가 relevance를 단다. 반면 [moPepGen(Zhu 2025)](../sources/zhu-2025-identification-non-canonical-peptides-mopepgen.md)처럼 일반 비정규 펩타이드 생성 알고리즘은 과제 특이 relevance가 약하면 분류 태그만 두고 별도 relevance 섹션은 생략할 수 있다.

**Cited**: [Huber 2025](../sources/huber-2025-comprehensive-proteogenomic-pipeline-neoantigen-discovery.md), [Deepanshi Awasthi 2026](../sources/awasthi-2026-pexmap-proteogenomic-exon-isoform-mapping.md), [Zhu 2025](../sources/zhu-2025-identification-non-canonical-peptides-mopepgen.md)

### Q58. “high-impact” 기준을 Cancer Multiomics 모니터링에서 어떻게 operationalize 할까(저널/데이터/임상 연결)?
**A.** "high-impact"는 세 신호로 operationalize한다: (i) 저널/위상 — 4축에 핵심인 high-tier 저널인지, (ii) 데이터 — raw+supplement+code가 재현 가능하게 공개됐는지, (iii) 임상 연결 — 결과가 환자 stratification·치료선택·예후로 이어지는지. [Lee 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md)은 Genome Biology 게재 + 한국인 NAC 코호트 + non-pCR 예측 모델·druggable 표적(AURKB/GRK2/ITGB8)으로 세 축을 모두 만족해 high-impact로 분류된다. [Chang 2026](../sources/chang-2026-integrative-proteogenomics-gastric-cancer-taiwan.md)은 Gut 게재 + stage·DBAC·proteome-immune state를 묶은 survival decision-tree로 임상 연결이 강하고, [Qu 2024](../sources/qu-2024-integrated-proteogenomic-metabolomic-characterization-papillary.md)도 102명 5-layer로 재발위험 stratification과 후보표적을 연결해 임상축 점수가 높다. 세 신호 중 임상 연결을 가장 무겁게 가중해 우선순위를 매긴다.

**Cited**: [Lee DK 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md), [chang-2026-integrative-proteogenomics-gastric-cancer-taiwan](../sources/chang-2026-integrative-proteogenomics-gastric-cancer-taiwan.md), [qu-2024-integrated-proteogenomic-metabolomic-characterization-papillary](../sources/qu-2024-integrated-proteogenomic-metabolomic-characterization-papillary.md)

### Q59. WGS-only 논문과 proteogenomics/phosphoproteomics 논문을 같은 큐에서 어떻게 우선순위화할까?
**A.** 같은 큐에서는 "우리 4축 중 몇 개 layer를 덮고, 기능/임상 readout에 얼마나 가까운가"로 우선순위를 매겨, WGS-only보다 proteome/phospho까지 통합한 논문을 대체로 위에 둔다. 근거로 [Chen 2026](../sources/chen-2026-global-impact-germline-structural-variation-cancer-proteome.md)은 SV의 단백 결과가 cis-concordant ~17%에 그쳐, WGS-only 신호는 단백 layer로 확인되기 전엔 기능 결론이 불확실함을 보인다. 반대로 [Lee 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md)·[Chang 2026](../sources/chang-2026-integrative-proteogenomics-gastric-cancer-taiwan.md)처럼 phosphoproteome로 kinase 활성(AURKB·GRK2, KEA3 기반 CDK4)을 읽는 논문은 변이를 "기능 상태"로 바로 연결해 우선순위가 높다. 다만 WGS-only라도 enhancer hijacking·germline SV 같은 우리 미해결 질문을 직접 채우면 가중치를 올려, '미해결 질문 적합도 + layer 깊이'를 함께 본다.

**Cited**: [Chen 2026](../sources/chen-2026-global-impact-germline-structural-variation-cancer-proteome.md), [Lee DK 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md), [chang-2026-integrative-proteogenomics-gastric-cancer-taiwan](../sources/chang-2026-integrative-proteogenomics-gastric-cancer-taiwan.md)

### Q60. 파이프라인/방법론 논문(neoantigen pipeline 등)은 어떤 추가 메타를 템플릿에 넣어야 할까?
**A.** 파이프라인/방법론 논문에는 표준 메타 외에 (1) 입력 데이터 요구(WES/WGS·RNA·MS 등)와 지원 변이/펩타이드 타입, (2) 참조 DB·버전, (3) 코드/라이선스/저장소, (4) 계산 비용(런타임·OS), (5) 명시된 failure mode와 벤치마크 성능을 추가 필드로 넣는다. [Huber 2025](../sources/huber-2025-comprehensive-proteogenomic-pipeline-neoantigen-discovery.md)(NeoDisc)는 4개 variant caller 앙상블(≥2 caller=high-confidence), WES/RNA 기반 HLA typing, APPM 결함·HLA LOH를 failure mode로, CESC-1에서 11/66 immunogenic 같은 벤치마크를 제공해 이 필드들을 그대로 채울 수 있다. [PEXMap(Awasthi 2026)](../sources/awasthi-2026-pexmap-proteogenomic-exon-isoform-mapping.md)은 ENACTdb v0.5 버전·GitHub 코드·CC BY-NC-ND 라이선스·DB build ~4분+검색 ~2분(Linux)·99.4% gene 정확도까지 명시하고, [moPepGen(Zhu 2025)](../sources/zhu-2025-identification-non-canonical-peptides-mopepgen.md)은 germline/somatic variant·noncoding ORF·RNA fusion·circRNA 등 지원하는 비정규 펩타이드 입력 타입을 메타로 적어 둔다.

**Cited**: [Huber 2025](../sources/huber-2025-comprehensive-proteogenomic-pipeline-neoantigen-discovery.md), [Deepanshi Awasthi 2026](../sources/awasthi-2026-pexmap-proteogenomic-exon-isoform-mapping.md), [Zhu 2025](../sources/zhu-2025-identification-non-canonical-peptides-mopepgen.md)

### Q61. WGS feature와 proteomics feature 통합에서 leakage/overfitting 위험을 어떻게 점검할까?
**A.** 로컬 근거는 leakage/overfitting 점검을 (1) 교차검증 + 외부코호트 + ablation, (2) shortcut-bias 진단으로 나눠 제시한다. [Duan 2026](../sources/duan-2026-discovering-proteo-transcriptomic-networks-heterogeneous-graph-learning.md)은 CPTAC 4개 소규모 코호트(n=73~92)에서 5-fold cross-validation C-index와 fold 간 edge-weight Pearson 재현성으로 안정성을 보고, biological prior·edge-aware weighting을 제거하는 ablation으로 성능 의존성을 분해했다(prior 제거 시 PDAC 0.74→0.47). [Jiang 2025](../sources/jiang-2025-deciphering-dark-cancer-phosphoproteome-using.md)는 kinase activity score 계산 시 해당 site 자체를 substrate 집합에서 제외해 명시적으로 leakage를 차단했다. 한 발 더 나아가 [Zhang 2026](../sources/zhang-2026-cross-task-interpretability-through-unified-modeling.md)은 통합 해석을 통해 deep-learning 예측기가 intra-HLA 라벨 불균형에 기인한 shortcut 상관을 학습했음을 정보이론 지표로 정량화하고 mutation-level 일반화로 점검할 것을 제안한다.

**Cited**: [duan-2026-discovering-proteo-transcriptomic-networks-heterogeneous-graph-learning](../sources/duan-2026-discovering-proteo-transcriptomic-networks-heterogeneous-graph-learning.md), [Jiang 2025](../sources/jiang-2025-deciphering-dark-cancer-phosphoproteome-using.md), [Zhang 2026](../sources/zhang-2026-cross-task-interpretability-through-unified-modeling.md)

### Q62. 모델이 batch를 학습하는 위험을 논문은 어떻게 회피했는가(또는 회피하지 못했는가)?
**A.** 로컬 논문은 주로 실험·정량 단계에서 batch 신호를 줄이는 방식으로 회피했다. [Chang 2026](../sources/chang-2026-analysis-isobaric-quantitative-proteomic-data.md)은 TMT/iTRAQ isobaric labeling으로 여러 샘플을 동시 측정해 run-to-run 변이를 제거하고, FragPipe+TMT-Integrator 조합이 MaxQuant 대비 batch effect가 감소함을 ccRCC 데이터로 보고했다. [Tüshaus 2025](../sources/tshaus-2025-towards-routine-proteome-profiling-ffpe.md)는 1,220 FFPE 검체를 3년에 걸쳐 측정하면서 코호트 간 동일·재현 가능한 sample loading을 보장하는 새 정규화 방법이 필요함을 핵심 발견으로 제시한다. 다만 이들은 측정·정규화 수준의 통제이며, 모델이 batch를 학습하지 않았는지에 대한 직접적 검증(예: batch에 대한 예측 가능성 점검)을 별도로 보고한 로컬 근거는 제한적이다.

**Cited**: [chang-2026-analysis-isobaric-quantitative-proteomic-data](../sources/chang-2026-analysis-isobaric-quantitative-proteomic-data.md), [Tüshaus 2025](../sources/tshaus-2025-towards-routine-proteome-profiling-ffpe.md)

### Q63. response prediction에서 “설명가능성”을 주장할 때 어떤 검증이 있어야 하는가?
**A.** response 예측의 '설명가능성' 주장에는 (i) 모델이 짚은 feature가 독립 코호트·실험으로 재현되는지, (ii) 해석이 인공적 shortcut이 아닌지에 대한 검증이 필요하다. [Lee 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md)은 non-pCR을 설명하는 5개 인자(estrogen/GRK2/ITGB8/AKR1C2/ABCA13)를 PTM-SEA·GSVA로 해석한 뒤 METABRIC 외부코호트에서 prognostic 패턴을 재현하고 GRK2·AURKB·ITGB8을 세포주·organoid in vitro로 기능 검증했다. 반대로 [Zhang 2026](../sources/zhang-2026-cross-task-interpretability-through-unified-modeling.md)은 해석 가능한 모델조차 intra-HLA 불균형 기반 shortcut 상관을 학습할 수 있음을 보이며, 설명가능성 주장 시 mutual-information 기반 debiasing과 일반화 점검을 함께 요구한다. 즉 인라인 해석 + 외부검증 + 기능검증 + bias 진단이 결합돼야 한다.

**Cited**: [Lee DK 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md), [Zhang 2026](../sources/zhang-2026-cross-task-interpretability-through-unified-modeling.md)

### Q64. kinase activity feature는 protein confounding 통제를 어떻게 요구하는가?
**A.** kinase activity feature는 phosphosite 신호가 kinase 자체의 활성이 아니라 단백질 abundance나 결측 annotation에 의해 교란될 수 있어 통제가 필요하다. [Yılmaz 2021](../sources/ylmaz-2021-robust-inference-kinase-activity-using.md)의 RoKAI는 functional neighborhood 정보를 통합해 누락된 annotation·정량에 robust하게 만들어 협응적 신호를 포착함으로써 추론 정확도를 높인다. [Casado 2013](../sources/casado-2013-kinase-substrate-enrichment-analysis-provides-insights.md)의 KSEA는 기질 집합의 phosphorylation 농축으로 kinase 경로 활성을 추정하지만, [Savage 2020](../sources/savage-2020-phosphoproteomics-bioinformatics-comprehensive-guide.md)은 기질 집합의 절반 이상이 10개 미만이고 PEG/MELK·PDPK1/PDK1·PTPN11 같은 ID-mapping 오류가 하류로 전파됨을 지적한다. 따라서 protein-level 보정, 기질 수·annotation 품질 점검, 도구 간 교차검증이 confounding 통제로 요구된다.

**Cited**: [Yılmaz 2021](../sources/ylmaz-2021-robust-inference-kinase-activity-using.md), [Casado 2013](../sources/casado-2013-kinase-substrate-enrichment-analysis-provides-insights.md), [Savage 2020](../sources/savage-2020-phosphoproteomics-bioinformatics-comprehensive-guide.md)

### Q65. neoantigen feature는 어떤 ground truth 문제를 갖는가(검증 부재, 정의 불일치)?
**A.** neoantigen feature의 ground truth는 면역원성 검증의 부재와 정의 불일치 문제를 갖는다. [Huber 2025](../sources/huber-2025-comprehensive-proteogenomic-pipeline-neoantigen-discovery.md)의 NeoDisc는 in silico 예측 다수 중 실제 IFNγ ELISpot 면역원성은 일부에 그쳤고(CESC-1에서 66개 중 11개만 면역원성), HLA-LOH·antigen-presentation machinery 결함을 명시적 failure mode로 표시하며 immunopeptidomics로 자연 제시 펩타이드를 검증해야 신뢰도가 올라간다고 본다. [Tejaswi 2025](../sources/tejaswi-2025-computational-neoantigen-prediction-cancer-immunotherapy.md)도 neoantigen이 genomic/transcriptomic/proteomic 수준에서 다르게 정의될 수 있어 proteome 기반 검증이 실험적 확증으로 필요함을 강조한다. 나아가 [Zhang 2026](../sources/zhang-2026-cross-task-interpretability-through-unified-modeling.md)은 면역원성 예측기가 intra-HLA 라벨 불균형 shortcut을 학습해 ground-truth 라벨 자체가 편향됨을 보인다.

**Cited**: [Huber 2025](../sources/huber-2025-comprehensive-proteogenomic-pipeline-neoantigen-discovery.md), [Tejaswi 2025](../sources/tejaswi-2025-computational-neoantigen-prediction-cancer-immunotherapy.md), [Zhang 2026](../sources/zhang-2026-cross-task-interpretability-through-unified-modeling.md)

### Q66. immune composition feature는 원자료(IHC/flow)와의 일치 여부를 확인했는가?
**A.** 일부 로컬 연구는 omics 기반 immune composition을 IHC/flow 같은 원자료와 직접 대조해 일치를 확인했다. [Wu 2025](../sources/wu-2025-artificial-intelligence-multimodality-data-integration.md)는 위암에서 scRNA-seq로 도출한 면역 회로(CD8+ TRM–B세포 CXCL13-CXCR5 축)를 multiplex IHC, flow cytometry, 공배양 기능 assay로 교차 검증했다. [Satpathy 2021](../sources/satpathy-2021-proteogenomic-portrait-lung-squamous-cell.md)은 LSCC에서 xCell 기반 면역/스트로마 deconvolution으로 Hot/Warm/Cold 상태를 정의하고, ARHGDIB K135 아세틸화 같은 신호를 IHC로 침윤 면역·중간엽 세포에 국재화해 확인했다. 다만 [Soltis 2022](../sources/soltis-2022-proteogenomic-analysis-lung-adenocarcinoma-reveals.md)처럼 RNA/단백 상관이 tumor purity·면역세포 프로필과 연동됨을 보고하되 IHC/flow 대조까지는 다루지 않은 경우도 있어, 일치 확인 여부는 연구마다 다르다.

**Cited**: [Wu 2025](../sources/wu-2025-artificial-intelligence-multimodality-data-integration.md), [Satpathy 2021](../sources/satpathy-2021-proteogenomic-portrait-lung-squamous-cell.md), [soltis-2022-proteogenomic-analysis-lung-adenocarcinoma-reveals](../sources/soltis-2022-proteogenomic-analysis-lung-adenocarcinoma-reveals.md)

### Q67. small-n/high-p 문제에서 논문은 어떤 차원축소/정규화 전략을 쓰는가?
**A.** small-n/high-p 상황에서 로컬 논문은 비지도 차원축소와 prior 기반 정규화를 함께 쓴다. [Lee 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md)은 n=50 TNBC 코호트에서 CNA+RNA+protein+phospho 4개 layer를 NMF로 통합 클러스터링(k=5)해 차원을 압축하고, 최종 예측은 단 5개 저항인자만 쓰는 절제된 logistic regression(AUC 0.946)으로 구성한 뒤 METABRIC로 외부 검증했다. [Duan 2026](../sources/duan-2026-discovering-proteo-transcriptomic-networks-heterogeneous-graph-learning.md)은 노드를 KEGG pathway 유전자로 제한하고 STRING PPI(≥700) edge prior로 그래프를 제약하며 L2 정규화·early stopping을 적용해 73~92명 규모에서 과적합을 억제한다(prior 제거 시 성능 급락). 즉 NMF/그래프 prior로 p를 줄이고 정규화·외부검증으로 보강하는 전략이다.

**Cited**: [Lee DK 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md), [duan-2026-discovering-proteo-transcriptomic-networks-heterogeneous-graph-learning](../sources/duan-2026-discovering-proteo-transcriptomic-networks-heterogeneous-graph-learning.md)

### Q68. multi-omics layer 간 missingness가 다를 때 통합 모델은 어떻게 구성하는가?
**A.** 로컬 근거에서 통합 모델은 대체로 결측이 일정 수준 이하인 feature만 남기고 layer별 측정 가능 샘플 수에 따라 가중·정렬하는 방식으로 구성한다. [Duan 2026](../sources/duan-2026-discovering-proteo-transcriptomic-networks-heterogeneous-graph-learning.md)은 layer별로 결측 20% 초과 feature를 제거한 뒤 z-score 표준화하고 mRNA/protein/phosphoprotein을 별도 node type으로 둔 heterogeneous graph로 결합하되, 환자별 모든 modality 측정을 가정하며 partial/missing-modality 입력 확장은 향후 과제로 남긴다. [Jiang 2025](../sources/jiang-2025-deciphering-dark-cancer-phosphoproteome-using.md)는 layer 간 dynamic 상관 feature를 양쪽 측정값이 ≥20 샘플에서 동시 존재할 때만 계산하고 overlap이 작은 코호트는 패널티를 받게 해 layer별 missingness 차이를 모델 단계에서 명시적으로 다룬다.

**Cited**: [duan-2026-discovering-proteo-transcriptomic-networks-heterogeneous-graph-learning](../sources/duan-2026-discovering-proteo-transcriptomic-networks-heterogeneous-graph-learning.md), [Jiang 2025](../sources/jiang-2025-deciphering-dark-cancer-phosphoproteome-using.md)

### Q69. sample type(FFPE)과 turnaround time은 임상 적용에 어떤 제약을 만드는가?
**A.** FFPE와 turnaround time은 routine 적용에 정규화·소프트웨어·재현성 제약을 만든다. [Tüshaus 2025](../sources/tshaus-2025-towards-routine-proteome-profiling-ffpe.md)는 6개 암종 1,220 FFPE 검체를 3년에 걸쳐 측정한 결과, 코호트 간 동일·재현 가능한 sample loading을 위한 새 정규화 방법이 필요했고 평균 >4,000 단백질 깊이가 가능했으나 기존 소프트웨어가 대규모 ion-mobility 온라인 분획 데이터를 처리하지 못하는 한계를 보고한다. 즉 장기 운영 시 워크플로우 성능·정규화 일관성이 임상 적용의 병목이 된다. 보조적으로 [Li 2025](../sources/li-2025-sonication-assisted-protein-extraction-improves-proteomic.md)은 조직 lysis 단계의 sonication 추가가 막단백·DNA결합 단백 검출 coverage를 높임을 보여, 검체 처리 프로토콜이 검출 가능 feature 범위를 좌우함을 시사한다.

**Cited**: [Tüshaus 2025](../sources/tshaus-2025-towards-routine-proteome-profiling-ffpe.md), [li-2025-sonication-assisted-protein-extraction-improves-proteomic](../sources/li-2025-sonication-assisted-protein-extraction-improves-proteomic.md)

### Q70. clinical phosphoproteomics를 routine으로 쓰기 위한 핵심 병목은 무엇인가(sample amount, enrichment reproducibility 등)?
**A.** clinical phosphoproteomics의 핵심 병목은 시료 처리·정량 재현성과 dark phosphoproteome의 기능 해석 부재다. [Li 2025](../sources/li-2025-sonication-assisted-protein-extraction-improves-proteomic.md)은 CPTAC 표준 프로토콜에서도 단백 추출·lysis 방식(urea±sonication)이 막단백·DNA결합 단백 검출 coverage를 좌우함을 보여 sample prep 단계가 결과를 결정함을 시사한다. [Chang 2026](../sources/chang-2026-analysis-isobaric-quantitative-proteomic-data.md)은 TMT enrichment·정량의 재현성과 run 간 변이 제거를 위해 isobaric labeling과 전용 처리 도구가 필요함을 보고한다. 또한 [Jiang 2025](../sources/jiang-2025-deciphering-dark-cancer-phosphoproteome-using.md)는 검출 phosphosite의 >95%가 upstream kinase·기능 annotation이 없어, 측정해도 임상 해석으로 잇기 어려운 점을 핵심 장애물로 제시한다.

**Cited**: [li-2025-sonication-assisted-protein-extraction-improves-proteomic](../sources/li-2025-sonication-assisted-protein-extraction-improves-proteomic.md), [chang-2026-analysis-isobaric-quantitative-proteomic-data](../sources/chang-2026-analysis-isobaric-quantitative-proteomic-data.md), [Jiang 2025](../sources/jiang-2025-deciphering-dark-cancer-phosphoproteome-using.md)

### Q71. Cancer Multiomics 과제에서 추가로 확보해야 할 데이터 레이어는 무엇인가(immunopeptidomics/spatial 등)?
**A.** 현재 스택(WGS/WES + RNA + global proteome + phospho)이 잡지 못하는 두 층을 우선 보강해야 한다. 첫째 **immunopeptidomics(HLA-presented peptide)** — [Huber 2025](../sources/huber-2025-comprehensive-proteogenomic-pipeline-neoantigen-discovery.md)의 NeoDisc는 immunopeptidomics를 genomics·transcriptomics와 결합해야 canonical SNV 신항원을 넘어 viral·noncanonical·splice 유래 항원까지 후보에 포함되고, [Nature 2021](../sources/nature-2021-proteogenomic-discovery-neoantigens-brain-tumors.md)은 mutational burden이 낮은 종양에서 aberrant splice junction이 신항원의 주요 원천이라 MS 기반 검증 층이 필수임을 보였다. 둘째 **공간(spatial) 층** — [Petralia 2024](../sources/petralia-2024-pan-cancer-proteogenomics-characterization-tumor-immunity.md)는 bulk phospho가 종양·면역·기질 신호를 섞기 때문에 deconvolution과 H&E 조직병리를 함께 써서 cell-type별 활성을 분리했고, methylation 층도 흡연 등 노출의 면역 매개효과 해석에 동원했다. 즉 immunopeptidome, DNA methylation, 그리고 cell-type 분해를 위한 spatial/histopathology가 다음 확보 대상이다.

**Cited**: [Huber 2025](../sources/huber-2025-comprehensive-proteogenomic-pipeline-neoantigen-discovery.md), [Rivero-Hinojosa 2021](../sources/nature-2021-proteogenomic-discovery-neoantigens-brain-tumors.md), [Petralia 2024](../sources/petralia-2024-pan-cancer-proteogenomics-characterization-tumor-immunity.md)

### Q72. WGS만으로 약한 질문을 phosphoproteome이 어떻게 보완할 수 있는가?
**A.** WGS는 어떤 변이가 있는지는 보여주지만 그 변이가 실제로 신호경로를 켰는지는 알려주지 못하는데, phosphoproteome이 이 기능 상태를 직접 메운다. [Lee 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md)의 TNBC 코호트에서 ER/PR이 IHC 음성이라 유전체로는 호르몬 신호가 없다고 보이지만, PTM-SEA가 non-pCR에서 GRK2·CDK2 인산화 활성을, 잔존종양에서 AURKB 인산화 신호를 잡아내 약물 표적(barasertib+paclitaxel 시너지)으로 이어졌다. [Petralia 2024](../sources/petralia-2024-pan-cancer-proteogenomics-characterization-tumor-immunity.md)도 CD8-/IFNG+ 처럼 변이·침윤만으로는 안 보이는 면역회피 상태를 kinase 활성(TBK1/IKK/Src-family, PTK2/FAK)으로 구분했다. 즉 WGS가 표적의 '존재'만 말할 때 phospho는 그 표적이 '작동 중'인지를 보강한다.

**Cited**: [Lee DK 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md), [Petralia 2024](../sources/petralia-2024-pan-cancer-proteogenomics-characterization-tumor-immunity.md)

### Q73. phosphoproteome만으로 약한 질문을 WGS가 어떻게 보완할 수 있는가?
**A.** 반대로 phospho/proteome 신호만으로는 그 단백 변화의 근본 원인(유전적 driver)이나 환자 층화 기준을 못 잡을 때 WGS가 이를 보강한다. [Chen 2026](../sources/chen-2026-global-impact-germline-structural-variation-cancer-proteome.md)은 germline structural variation의 LoF가 512개 유전자에서 단백 저발현을 cis-방식으로 일으킴을 보였는데, 이런 exon-level deletion은 SNV 패널이나 단백 측정만으로는 원인 규명이 불가능하고 WGS의 SV calling이 있어야 설명된다. [Lee 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md)에서도 ITGB8 단백 발현 차이의 배경이 7p21 cytoband copy gain/loss라는 CNA였고, CN deep loss군은 pCR 80% vs gain군 0%로 WGS 기반 copy number가 정량적 층화 변수를 제공했다. 즉 phospho가 '무엇이 바뀌었나'를 보일 때 WGS는 '왜 바뀌었나'와 '누구에서'를 채운다.

**Cited**: [Chen 2026](../sources/chen-2026-global-impact-germline-structural-variation-cancer-proteome.md), [Lee DK 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md)

### Q74. 논문 subtype이 실제 치료 선택으로 이어지려면 어떤 단계가 필요한가?
**A.** 논문 subtype이 치료 선택으로 이어지려면 (1) subtype별 약물 표적을 동반 검증하고 (2) 외부 코호트에서 재현하며 (3) 임상 의사결정 입력값으로 환자를 명확히 stratify해야 한다. [Lee 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md)은 NMF 5-subtype을 정의하는 데 그치지 않고 각 저항 메커니즘마다 표적(GRK2·AURKB·ITGB8)을 cell line·organoid로 검증하고, METABRIC에서 재현하고, ITGB8 CN 상태별 pCR률(deep loss 80% vs gain 0%)로 'ADC 추가가 정당한 환자(gain/diploid)'까지 특정했다. [Petralia 2024](../sources/petralia-2024-pan-cancer-proteogenomics-characterization-tumor-immunity.md)는 CD8+/IFNG+ subtype이 OAK trial의 atezolizumab arm에서만 PFS 이득을 주고 docetaxel arm에서는 아니어서, subtype이 '치료-특이적' 맥락 feature일 때만 처방에 연결됨을 보였다. 즉 표적 동반검증·외부재현·treatment-specific 입증이 전제 단계다.

**Cited**: [Lee DK 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md), [Petralia 2024](../sources/petralia-2024-pan-cancer-proteogenomics-characterization-tumor-immunity.md)

### Q75. 논문 표적/바이오마커가 과제에서 재현 가능한지 판단하는 기준은 무엇인가?
**A.** 재현 가능성 판단 기준은 (a) 독립·외부 코호트에서 같은 방향이 나오는지, (b) 측정 modality에 따라 신호가 흔들리지 않는지, (c) 기능 검증이 동반되는지다. [Lee 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md)은 5-인자 모델을 same-cohort AUC 0.946으로 보고하면서도 외부 prospective AUC는 미보고라고 한계로 명시했고, AKR1C2·ITGB8 등을 METABRIC·TCGA에서 별도 검증해 통과 여부를 표시했다(METABRIC IM에서 AKR1C2 RFS P=0.0033). [Chen 2026](../sources/chen-2026-global-impact-germline-structural-variation-cancer-proteome.md)은 364개 recurrent SV-altered gene 중 mRNA·protein이 동시에 같은 방향인 concordant는 17%뿐이고 33%는 protein-only라, mRNA만으로 마커를 채택/기각하면 안 되며 단백 층 재현이 별도로 필요함을 보였다. 따라서 same-cohort 통계만으로는 부족하고 외부 코호트 + 다중 modality 일치 + 기능 검증이 기준이 된다.

**Cited**: [Lee DK 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md), [Chen 2026](../sources/chen-2026-global-impact-germline-structural-variation-cancer-proteome.md)

### Q76. 공개 데이터로 “Cancer Multiomics 파일럿 재분석”이 가능한가? 무엇이 부족한가?
**A.** 공개 데이터만으로 파일럿 재분석은 상당 부분 가능하다. [Savage 2024](../sources/savage-2024-pan-cancer-proteogenomics-expands-landscape-therapeutic.md)는 raw proteomics를 CPTAC/PDC, genomics/transcriptomics를 GDC, 가공 데이터를 LinkedOmicsKB에서 받아 10개 암종 1,043 종양을 harmonize했고, [Chen 2026](../sources/chen-2026-global-impact-germline-structural-variation-cancer-proteome.md)도 dbGaP(phs001287)·PDC·GDC로 WGS+RNA+proteome 1,637명을 재분석했다. 부족한 부분은 명확하다 — 환자별 자체 신규 layer(특히 immunopeptidomics와 spatial)는 공개 데이터에 거의 없고, [Petralia 2024](../sources/petralia-2024-pan-cancer-proteogenomics-characterization-tumor-immunity.md)가 지적했듯 CPTAC pan-cancer 코호트는 상세 치료정보가 빠져 있어 생존 연관이 직접적 치료반응 모델링과 동치가 아니며, controlled-access(dbGaP) 승인 절차도 선결 조건이다. 즉 표적 우선순위·subtype 재현은 가능하나 면역·공간 층과 임상 치료반응 검증은 자체 데이터가 추가로 필요하다.

**Cited**: [Savage 2024](../sources/savage-2024-pan-cancer-proteogenomics-expands-landscape-therapeutic.md), [Chen 2026](../sources/chen-2026-global-impact-germline-structural-variation-cancer-proteome.md), [Petralia 2024](../sources/petralia-2024-pan-cancer-proteogenomics-characterization-tumor-immunity.md)

### Q77. 재분석을 한다면 가장 먼저 재현해야 할 figure/table은 무엇인가?
**A.** 가장 먼저 재현할 것은 통합 클러스터링으로 정의한 **subtype 할당 표/그림**과 그 subtype-결과(생존·반응) 연관이다. [Lee 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md)의 경우 NMF 5-subtype(brunet, k=5, 4 modality concat) 분류와 subtype별 pCR 분포가 핵심 figure이고, 이것이 재현돼야 하위 저항 메커니즘·예측모델이 의미를 갖는다. [Petralia 2024](../sources/petralia-2024-pan-cancer-proteogenomics-characterization-tumor-immunity.md)는 BayesDeBulk로 7개 면역 subtype을 정의한 뒤 CD8+/IFNG+의 OAK atezolizumab PFS 연관을 핵심 검증 그림으로 제시하므로, immune subtype 분류표 + OAK 생존곡선이 1차 재현 대상이다. 즉 '통합 subtype 분류 → subtype별 임상 연관' 그림을 먼저 복제한 뒤 마커·표적 figure로 내려가는 순서가 합리적이다.

**Cited**: [Lee DK 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md), [Petralia 2024](../sources/petralia-2024-pan-cancer-proteogenomics-characterization-tumor-immunity.md)

### Q78. 재분석을 위해 우선 확인해야 할 supplement/데이터 가용성 단서는 무엇인가?
**A.** 재분석 전 우선 확인할 단서는 (1) raw 데이터 accession이 layer별로 모두 등록돼 있는지, (2) controlled vs open 접근 구분, (3) 도구·버전과 가공 산출물 위치다. [Lee 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md)은 WES PRJNA1422845·RNA-seq PRJNA1422844(NCBI Bioproject), proteome PDC000695·phospho PDC000696(CPTAC PDC)로 4개 layer accession을 모두 명시해 즉시 확인 가능하다. [Chen 2026](../sources/chen-2026-global-impact-germline-structural-variation-cancer-proteome.md)은 dbGaP phs001287.v21.p6/phs000178.v11.p8(controlled-access)와 PDC/GDC, 그리고 SV calling 도구(Delly v3.1.1, SVABA v1.2.0)·CSG reference 스냅샷(csgs.sequenxe.com May 2024)·figshare 시각화까지 supplement에 적어, 어떤 데이터가 승인 필요하고 어떤 버전으로 콜링했는지가 재현의 첫 체크포인트임을 보여준다. 따라서 각 modality의 accession·접근권한·도구 버전을 supplement에서 먼저 점검해야 한다.

**Cited**: [Lee DK 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md), [Chen 2026](../sources/chen-2026-global-impact-germline-structural-variation-cancer-proteome.md)

### Q79. 같은 결론을 유전체와 단백질/인산화로 각각 주장할 때, 어느 쪽 근거가 더 강한가?
**A.** 같은 결론이라면 일반적으로 단백/인산화 근거가 유전체 근거보다 기능적 의미에서 더 강하지만, 둘은 상호보완이며 어느 한쪽도 단독으로 충분치 않다. [Chen 2026](../sources/chen-2026-global-impact-germline-structural-variation-cancer-proteome.md)은 SV가 mRNA·protein 양쪽에서 같은 방향으로 나타난 concordant가 364개 중 17%뿐이고 33%는 protein 변화가 우세(mRNA 약함)여서 MS 단백체가 유전체/전사체만으로 안 잡히는 cis-effect를 포착함을 정량적으로 보였다. [Savage 2024](../sources/savage-2024-pan-cancer-proteogenomics-expands-landscape-therapeutic.md)도 gene-wise mRNA-protein 상관이 코호트마다 크게 흔들려 transcript 기반 휴리스틱 대신 protein-level 표적 선정을 권고했다. 다만 [Lee 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md)의 7p21 CNA→ITGB8 사례처럼 유전체 근거가 환자 층화의 정량 기준을 주므로, '단백이 기능을 입증하고 유전체가 원인·층화를 입증'할 때 두 근거가 합쳐질 때 가장 강하다.

**Cited**: [Chen 2026](../sources/chen-2026-global-impact-germline-structural-variation-cancer-proteome.md), [Savage 2024](../sources/savage-2024-pan-cancer-proteogenomics-expands-landscape-therapeutic.md), [Lee DK 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md)

### Q80. 용어(immune-hot, subtype 등)가 논문마다 다른 정의로 쓰일 때 위키는 어떻게 표준화할까?
**A.** 용어 표준화는 '라벨'이 아니라 '정의에 쓰인 측정 축'을 명시하는 방식으로 해야 한다. [Petralia 2024](../sources/petralia-2024-pan-cancer-proteogenomics-characterization-tumor-immunity.md)는 immune-hot을 단일 점수로 합치지 말라고 명시하며, CD8 침윤과 IFNG 경로활성이 어긋나는 CD8-/IFNG+ subtype을 그 근거로 들어 면역상태를 7개 subtype으로 분해하고 각각을 cell 조성·경로활성·DNA 변이·단백·kinase 활성으로 정의했다. subtype도 마찬가지로 [Lee 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md)의 NMF 5-subtype은 IHC 기반 Lehmann 분류와 부분적으로만 일치했고(예: Lehmann IM 안에서도 36.8% non-pCR로 분기), 같은 단어라도 정의 방법이 다르면 다른 환자군을 가리킨다. 따라서 위키는 각 용어에 '어떤 modality·임계값·도구로 정의됐는가'를 메타데이터로 붙이고, 논문 간 라벨을 동일 정의로 매핑할 수 있을 때만 합치는 표준화가 필요하다.

**Cited**: [Petralia 2024](../sources/petralia-2024-pan-cancer-proteogenomics-characterization-tumor-immunity.md), [Lee DK 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md)

### Q81. 토픽 허브에서 논문을 어떤 카테고리로 분류하는 것이 좋은가(통합/kinase/neoantigen/모델)?
**A.** 로컬 seed가 실제로 갈라지는 축을 그대로 쓰는 것이 좋다. seed 논문은 (1) WGS/proteogenomics 통합(예: germline SV가 cancer proteome로 cis-반영되는 정량 — [Chen 2026](../sources/chen-2026-global-impact-germline-structural-variation-cancer-proteome.md)), (2) druggable target/통합 분석(CPTAC pan-cancer에서 protein/phospho 상태로 표적·synthetic lethality·항원 후보를 우선순위화한 [Savage 2024](../sources/savage-2024-pan-cancer-proteogenomics-expands-landscape-therapeutic.md)), (3) 치료반응 모델(non-pCR 예측 AUC 0.946 + AURKB/GRK2 druggable의 [Lee 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md))로 자연스럽게 나뉜다. 따라서 '통합 / kinase·인산화 / neoantigen·면역회피 / 반응예측'의 4분류를 1차로 두고, 한 논문이 여러 축에 걸치면(예: Savage는 통합+neoantigen) 주축 하나에 두고 나머지는 cross-link로 처리하는 것이 seed 분포와 일치한다.

**Cited**: [Chen 2026](../sources/chen-2026-global-impact-germline-structural-variation-cancer-proteome.md), [Savage 2024](../sources/savage-2024-pan-cancer-proteogenomics-expands-landscape-therapeutic.md), [Lee DK 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md)

### Q82. 새로운 논문이 들어오면 기존 seed 중 어떤 것과 먼저 연결할지(“근연” 규칙)는 무엇인가?
**A.** 새 논문은 '같은 분류축(통합/kinase/neoantigen/반응) + 같은 데이터 레이어 스택 + 같은 반응 라벨/코호트 인종'이 가장 많이 겹치는 seed에 먼저 붙이는 것이 근연 규칙으로 적절하다. 실제 seed들도 이 방식으로 연결되어 있어, [Lee 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md)은 동일한 TNBC neoadjuvant·반응예측 맥락 때문에 Anurag 2022(carboplatin 100% 대비)를 명시적 비교 seed로 잡고, [Chang 2026](../sources/chang-2026-integrative-proteogenomics-gastric-cancer-taiwan.md)은 East Asian 위암·WES+RNA+proteome+phospho 스택이 겹치는 Mun(한국 EOGC)·Jiao(pangenome) 쪽에 East-Asia 레퍼런스 사다리로 연결한다. 즉 제목 키워드보다 cm_axis·암종·modality·response-label·인종 코호트의 일치도를 우선 매칭하는 것이 안전하다.

**Cited**: [Lee DK 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md), [chang-2026-integrative-proteogenomics-gastric-cancer-taiwan](../sources/chang-2026-integrative-proteogenomics-gastric-cancer-taiwan.md)

### Q83. Cancer Multiomics 하위 페이지 “주요 결과”는 몇 개 bullet이 적정한가?
**A.** 하위 페이지의 '주요 결과'는 핵심만 추린 3~5개 bullet이 적정하다. 실제로 deep-dive가 끝난 seed 페이지를 보면 [Lee 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md)은 코호트→데이터 레이어→저항 메커니즘(estrogen/GRK2·ITGB8·AKR1C2/ABCA13·AURKB)→통합 예측모델→한계로 묶여 사실상 5개 안팎의 결과 덩어리로 정리되고, [Chang 2026](../sources/chang-2026-integrative-proteogenomics-gastric-cancer-taiwan.md)도 DBAC carcinogen·microbiome·proteome-immune·anatomy·CDK4 hub의 소수 핵심 축으로 압축된다. 세부 수치는 본문/Key Points에 두고, 상단 '주요 결과'에는 교수진이 한눈에 읽을 4±1개 bullet만 남기는 것이 위키 운영과 일치한다.

**Cited**: [Lee DK 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md), [chang-2026-integrative-proteogenomics-gastric-cancer-taiwan](../sources/chang-2026-integrative-proteogenomics-gastric-cancer-taiwan.md)

### Q84. “주요 결과” bullet의 권장 순서는 무엇인가(데이터→핵심 발견→과제 연결→한계)?
**A.** 권장 순서는 '데이터(코호트·레이어) → 핵심 발견 → 과제 연결 → 한계'이며, 이는 잘 정리된 seed 페이지의 실제 구조와 같다. [Lee 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md)은 환자 50명·WES+RNA+TMT proteome+phospho 같은 데이터 맥락을 먼저 고정하고, 5개 저항인자와 non-pCR AUC 0.946 발견을 제시한 뒤, 한미암 코호트 활용 가능성으로 이어가고 마지막에 'n=50 단일기관·AUC는 same-cohort·검증은 in vitro 수준' 같은 한계를 명시한다. [Chang 2026](../sources/chang-2026-integrative-proteogenomics-gastric-cancer-taiwan.md)도 154명 4-layer 데이터 → DBAC/CDK4 발견 → 한국인 비교 활용 → 'DBAC는 동아시아 특이, 직접 검증 미수행' 한계 순서를 따른다. 데이터를 먼저 깔고 한계로 닫는 이 순서가 발견의 해석 범위를 분명히 한다.

**Cited**: [Lee DK 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md), [chang-2026-integrative-proteogenomics-gastric-cancer-taiwan](../sources/chang-2026-integrative-proteogenomics-gastric-cancer-taiwan.md)

### Q85. 교수진 공유에서 디테일 vs 단순화의 균형을 어떻게 잡을까?
**A.** 교수진 공유에서는 '핵심 수치 1개 + 그 수치의 해석 범위(한계) 1개'를 한 쌍으로 묶어 단순화하되, 정량 앵커는 버리지 않는 것이 균형점이다. 예를 들어 [Lee 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md)은 'non-pCR 예측 AUC 0.946(Lehmann 0.781 대비)'이라는 한 수치를 앞세우되 same-cohort logistic regression·외부 prospective AUC 미보고라는 단서를 함께 두고, [Chang 2026](../sources/chang-2026-integrative-proteogenomics-gastric-cancer-taiwan.md)은 'DBAC HR 2.36–3.16, 환자 49.2%가 IHC-음성→CDK4 hub'를 핵심으로 두면서 CDK4/6 단독제는 상부 GI에서 효과 미미(palbociclib PFS 1.8개월)라는 조합 필요 caveat를 붙인다. 즉 세부 방법은 하위 페이지로 내리고 공유 슬라이드에는 대표 수치와 그 한계만 동반시키는 방식이 디테일과 단순화를 모두 만족한다.

**Cited**: [Lee DK 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md), [chang-2026-integrative-proteogenomics-gastric-cancer-taiwan](../sources/chang-2026-integrative-proteogenomics-gastric-cancer-taiwan.md)

### Q86. Slack 메시지에서 피해야 할 표현(과장, 확정 인과)은 무엇인가?
**A.** Slack에서는 과장("유전체만으로 부족", "layer를 쌓아 표적 발굴")과 확정 인과(in vitro/관찰 결과를 임상 효능처럼 단정)를 피해야 한다. 근거 논문들도 스스로 인과를 제한해서, [Lee 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md)은 AURKB·GRK2·ITGB8 시너지를 모두 cell line/organoid 수준으로 한정하고 AUC 0.946도 same-cohort 결과라 외부 검증이 필요하다고 못박으며, [Chang 2026](../sources/chang-2026-integrative-proteogenomics-gastric-cancer-taiwan.md)은 DBAC–microbiome 공존을 '관찰적(observational)'이라 명시하고 CDK4/6 비선택적 사용에 명시적으로 경고한다. 따라서 Slack 문장은 'A가 B를 유발한다'가 아니라 'A는 B와 연관 관찰되었고 임상 검증은 아직'이라는 톤을 쓰는 것이 안전하다.

**Cited**: [Lee DK 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md), [chang-2026-integrative-proteogenomics-gastric-cancer-taiwan](../sources/chang-2026-integrative-proteogenomics-gastric-cancer-taiwan.md)

### Q87. 관찰 기반 결과를 전달할 때 “관찰” caveat를 짧게 넣는 문장 패턴은 무엇인가?
**A.** 관찰 기반 결과는 '[관찰] X에서 Y가 ~와 연관 관찰되었다(통계). 다만 이는 단면/관찰 데이터이며 인과·임상효능은 별도 검증이 필요하다'는 2-clause 패턴으로 적는 것이 좋다. 이는 seed 논문의 서술과 동일한데, [Chang 2026](../sources/chang-2026-integrative-proteogenomics-gastric-cancer-taiwan.md)은 'SA가 위액에서 IM 56.9%→cancer 86.4%로 증가했다(관찰)'를 보고하면서 SA–barrier 관계의 기계론적 인과는 in vivo 모델이 없다고 단서를 달고, [Lee 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md)은 'estrogen GSVA high에서 pCR 14.3% vs 48.1%(P=0.0328)'라는 연관을 제시한 뒤 검증은 외부 코호트/세포주 수준임을 밝힌다. 즉 수치를 먼저 적고 곧바로 '관찰·연관, 인과 아님'을 짧게 덧붙이는 형식이 일관된다.

**Cited**: [chang-2026-integrative-proteogenomics-gastric-cancer-taiwan](../sources/chang-2026-integrative-proteogenomics-gastric-cancer-taiwan.md), [Lee DK 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md)

### Q88. seed 논문들을 기반으로 Cancer Multiomics 과제 통합 스토리라인 1장을 만들면 어떤 구조가 되는가?
**A.** seed들을 한 장으로 묶으면 'WGS/germline·SV 변이 → 단백체·인산화단백체 functional state → druggable target/반응 예측'이라는 종단 스토리라인이 된다. 토대는 germline SV가 cancer proteome로 cis-반영됨을 정량화한 [Chen 2026](../sources/chen-2026-global-impact-germline-structural-variation-cancer-proteome.md)이 깔고, 가운데를 CPTAC pan-cancer에서 mRNA로는 안 보이는 표적을 protein/phospho 상태로 우선순위화한 [Savage 2024](../sources/savage-2024-pan-cancer-proteogenomics-expands-landscape-therapeutic.md)가 잇고, 끝을 임상 반응 라벨에서 저항인자→non-pCR 예측모델로 닫는 [Lee 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md)이 맡는 구조다. 즉 '유전 변이 → 기능 상태 → 임상 의사결정'의 3단 골격에 각 단계 대표 seed를 배치하면 통합 1장이 완성된다.

**Cited**: [Chen 2026](../sources/chen-2026-global-impact-germline-structural-variation-cancer-proteome.md), [Savage 2024](../sources/savage-2024-pan-cancer-proteogenomics-expands-landscape-therapeutic.md), [Lee DK 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md)

### Q89. 스토리라인에서 WGS, phosphoproteome, neoantigen, immune evasion, prediction은 어떤 순서가 좋은가?
**A.** 정보 흐름상 'WGS → phosphoproteome → neoantigen → immune evasion → prediction' 순서가 자연스럽고, seed 내부 논리와도 맞는다. [Savage 2024](../sources/savage-2024-pan-cancer-proteogenomics-expands-landscape-therapeutic.md)는 genomic 이벤트를 protein/phospho 상태(hyperactivation)로 해석한 뒤 그 위에서 MHC binding 예측으로 mutant KRAS 같은 neoantigen 후보로 넘어가는 동일한 단계 진행을 보여주고, [Lee 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md)은 ITGB8 발현이 종양세포의 IFN/염증 시그니처를 억압하는 immune-evasion 축을 거쳐 마지막에 non-pCR 예측모델(AUC 0.946)로 수렴한다. 즉 WGS(변이·항원성 잠재력)로 시작해 phospho(활성 상태)·neoantigen(가시성)·immune evasion(회피)을 거쳐 최종 prediction으로 닫는 흐름이 근거 흐름과 일치한다.

**Cited**: [Savage 2024](../sources/savage-2024-pan-cancer-proteogenomics-expands-landscape-therapeutic.md), [Lee DK 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md)

### Q90. 현재 seed 세트에서 가장 비어 있는 축은 무엇인가(임상 반응예측, immunopeptidomics 등)?
**A.** 현재 seed는 통합·기전·데이터 레이어 쪽은 두꺼우나, 임상 반응예측 모델과 immunopeptidomics 측정 축이 가장 비어 있다. 반응예측 쪽은 [Lee 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md)·[Zhang 2023](../sources/zhang-2023-proteogenomics-clear-cell-renal-response-tyrosine-kinase-inhibitor.md)처럼 response 라벨이 붙은 코호트가 소수에 그쳐 SHAP-style feature 해석·basket-trial 분류·cloud-scale 처리로 채울 여지가 크고, neoantigen 축도 [Huber 2025](../sources/huber-2025-comprehensive-proteogenomic-pipeline-neoantigen-discovery.md)는 강력한 immunopeptidomics 파이프라인이지만 예제에서 WGS는 구현하지 않았고 [Chen 2026](../sources/chen-2026-global-impact-germline-structural-variation-cancer-proteome.md)의 germline SV→항원제시 연결도 실제 MHC peptide 측정이 아니라 proteome 추론에 머문다. 따라서 가장 빈 축은 'WGS 기반 후보와 실제 immunopeptidomics 측정을 같은 환자에서 잇는 임상 반응예측' 쪽이다.

**Cited**: [Lee DK 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md), [Zhang 2023](../sources/zhang-2023-proteogenomics-clear-cell-renal-response-tyrosine-kinase-inhibitor.md), [Huber 2025](../sources/huber-2025-comprehensive-proteogenomic-pipeline-neoantigen-discovery.md), [Chen 2026](../sources/chen-2026-global-impact-germline-structural-variation-cancer-proteome.md)

### Q91. 다음 ingest는 어떤 축을 먼저 채워야 하는가(예측모델 vs 면역회피 유전기전 vs phosphosignaling)?
**A.** 현재 seed 분포를 보면 다음 ingest는 '면역회피 유전기전 → 임상 반응예측' 축을 먼저 채우는 것이 맞다. 통합·기전 축은 이미 두꺼워서 germline SV의 cis-proteome 영향을 정량한 [Chen 2026](../sources/chen-2026-global-impact-germline-structural-variation-cancer-proteome.md)(cm_axis=integration)과 protein/phospho 상태로 표적을 우선순위화한 [Savage 2024](../sources/savage-2024-pan-cancer-proteogenomics-expands-landscape-therapeutic.md)(cm_axis=integration)가 받치고, phosphosignaling도 sunitinib 반응에서 mTOR/7q를 본 [Zhang 2023](../sources/zhang-2023-proteogenomics-clear-cell-renal-response-tyrosine-kinase-inhibitor.md)(cm_axis=phospho)이 있다. 반면 면역회피를 유전·항원제시 결함 수준에서 측정하는 seed는 [Huber 2025](../sources/huber-2025-comprehensive-proteogenomic-pipeline-neoantigen-discovery.md)(NeoDisc)가 거의 유일하고 그조차 예제에서 WGS는 미구현이며, response 라벨이 붙은 코호트는 [Lee 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md)(cm_axis=response) 정도로 희소하다. 따라서 'WGS 기반 HLA LOH·B2M·APPM 결함을 실제 항원제시 측정과 잇는 면역회피 유전기전'과 '반응 라벨 코호트'를 우선 ingest해 가장 빈 두 축을 메우는 것이 좋다.

**Cited**: [Chen 2026](../sources/chen-2026-global-impact-germline-structural-variation-cancer-proteome.md), [Savage 2024](../sources/savage-2024-pan-cancer-proteogenomics-expands-landscape-therapeutic.md), [Zhang 2023](../sources/zhang-2023-proteogenomics-clear-cell-renal-response-tyrosine-kinase-inhibitor.md), [Huber 2025](../sources/huber-2025-comprehensive-proteogenomic-pipeline-neoantigen-discovery.md), [Lee DK 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md)

### Q92. Cancer Multiomics 토픽이 “읽은 논문 리스트”로만 남지 않게 하려면 어떤 표준 산출물이 필요할까?
**A.** 단순 '읽은 논문 리스트'를 넘으려면, 논문마다 동일한 형식으로 재사용 가능한 표준 산출물을 남겨야 한다. seed 페이지들이 실제로 그 형식을 보여주는데, [Lee 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md)·[Chang 2026](../sources/chang-2026-integrative-proteogenomics-gastric-cancer-taiwan.md)는 (1) Summary 한 줄, (2) 과제 관련성(Cancer Multiomics relevance), (3) 주요 결과 bullet, (4) 데이터 공개(Data availability: Lee는 PRJNA1422845/4·PDC000695/696, Chang은 dbGaP phs004447·PDC000645/649), (5) Slack 메시지 초안을 고정 섹션으로 갖는다. 따라서 표준 산출물은 '논문당 고정 템플릿(요약·과제연결·결과·데이터접근·Slack초안) + 이를 한 줄씩 모은 메타테이블(암종/치료맥락/데이터레이어/축)'이며, 이 둘이 있어야 토픽이 검색·재분석 가능한 자산으로 남는다.

**Cited**: [Lee DK 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md), [chang-2026-integrative-proteogenomics-gastric-cancer-taiwan](../sources/chang-2026-integrative-proteogenomics-gastric-cancer-taiwan.md)

### Q93. 한 논문당 표준적으로 남겨야 하는 “Cancer Multiomics relevance” 3줄은 무엇인가?
**A.** 'Cancer Multiomics relevance' 3줄은 (1) 과제의 어느 축에 닿는지(통합/phospho/neoantigen·면역회피/반응예측), (2) 재사용할 구체적 데이터·코호트, (3) 한미암 코호트에서 무엇을 cross-validate할지로 쓰는 것이 표준이다. seed 페이지가 정확히 이 3줄 구조를 따르는데, [Lee 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md)은 '한국인 TNBC NAC reference → 동일 modality(WES+RNA+TMT proteome+phospho) → NMF 5-subtype·pCR 분포 재현 검증'으로, [Chang 2026](../sources/chang-2026-integrative-proteogenomics-gastric-cancer-taiwan.md)은 'East Asia 위암 reference(n=154) → 동일 protocol 4-layer → TP53/ARID1A mutual exclusion·KMT2D 24% 등 한국 GC cohort 1차 cross-validation target'으로 명시한다. 즉 축 연결·재사용 데이터·검증 포인트를 각각 한 줄로 적는 것이 relevance 3줄의 표준이다.

**Cited**: [Lee DK 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md), [chang-2026-integrative-proteogenomics-gastric-cancer-taiwan](../sources/chang-2026-integrative-proteogenomics-gastric-cancer-taiwan.md)

### Q94. 한 논문당 표준적으로 남겨야 하는 “Methods for reuse” 3줄은 무엇인가?
**A.** 'Methods for reuse' 3줄은 (1) 데이터 레이어·획득 방법(WGS/WES, RNA-seq, proteome, phospho enrichment, instrument), (2) 측정 깊이·정량 방식, (3) 핵심 분석 도구를 재현 가능하게 적는 것이 표준이다. seed 페이지가 이 수준으로 기술하는데, [Lee 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md)은 'WES+RNA-seq+TMT global proteome 10,457개 + phosphoproteome 31,258 site/5,373 protein, NMF 통합 클러스터링·PTM-SEA·GSVA·logistic regression'을 명시하고, [Zhang 2023](../sources/zhang-2023-proteogenomics-clear-cell-renal-response-tyrosine-kinase-inhibitor.md)은 'label-free proteome 12,310개(분석 7,451)·phospho 37,055 site 중 25% coverage 필터 후 6,749 site, WES SNV+arm-level SCNA'처럼 raw 식별 수와 분석 사용 수를 구분 보고한다. 즉 modality·깊이·도구를 각각 한 줄로, 재현에 필요한 수치까지 포함해 적는 것이 reuse용 methods 3줄이다.

**Cited**: [Lee DK 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md), [Zhang 2023](../sources/zhang-2023-proteogenomics-clear-cell-renal-response-tyrosine-kinase-inhibitor.md)

### Q95. 한 논문당 표준적으로 남겨야 하는 “Data availability” 2줄은 무엇인가?
**A.** 'Data availability' 2줄은 (1) genomics/transcriptomics 접근 경로(GDC/dbGaP/SRA accession), (2) proteomics/phospho 접근 경로(CPTAC PDC accession 등 controlled-access 여부)를 각각 한 줄로 적는 것이 표준이다. seed 페이지가 그대로 따르는데, [Lee 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md)은 'WES PRJNA1422845 / RNA-seq PRJNA1422844 (NCBI BioProject)'와 'proteome PDC000695 / phosphoproteome PDC000696 (CPTAC PDC)'로 두 줄로 분리하고, [Chang 2026](../sources/chang-2026-integrative-proteogenomics-gastric-cancer-taiwan.md)은 'WES+RNA-seq: GDC+dbGaP phs004447.v1.p1 (controlled-access)'와 'proteome+phospho: PDC000645+PDC000649'로 적는다. 즉 시퀀싱 layer와 단백체 layer의 accession을 한 줄씩, 접근 제한(controlled-access)까지 명시하는 것이 data availability 2줄이다.

**Cited**: [Lee DK 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md), [chang-2026-integrative-proteogenomics-gastric-cancer-taiwan](../sources/chang-2026-integrative-proteogenomics-gastric-cancer-taiwan.md)

### Q96. seed 8편 중에서 현재 위키에서 “source page deep-dive가 필요한” 논문은 무엇인가?
**A.** seed 중 'source page deep-dive가 필요한' 대표 논문은 [Savage 2024](../sources/savage-2024-pan-cancer-proteogenomics-expands-landscape-therapeutic.md)다. 이 페이지는 frontmatter가 batch_ingest_status: pdf-text-extracted 상태이고, 본문 Batch PDF Ingest Status에 '자동 local-PDF 텍스트 ingest이며 아직 수동 full-text deep-dive가 아니다(not yet a manual full-text deep-dive)'와 'downstream scientific claims should use this page only after source-specific Key Points are manually promoted or rechecked against the local PDF'라는 evidence boundary가 명시되어 있다. 반면 [Lee 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md)·[Chang 2026](../sources/chang-2026-integrative-proteogenomics-gastric-cancer-taiwan.md)·[Chen 2026](../sources/chen-2026-global-impact-germline-structural-variation-cancer-proteome.md)는 이미 수치까지 들어간 정독 페이지다. 따라서 Savage 2024가 PDF 정독으로 Key Points를 승격해야 할 1순위 deep-dive 대상이다.

**Cited**: [Savage 2024](../sources/savage-2024-pan-cancer-proteogenomics-expands-landscape-therapeutic.md), [Lee DK 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md), [chang-2026-integrative-proteogenomics-gastric-cancer-taiwan](../sources/chang-2026-integrative-proteogenomics-gastric-cancer-taiwan.md), [Chen 2026](../sources/chen-2026-global-impact-germline-structural-variation-cancer-proteome.md)

### Q97. seed 8편 중에서 현재 위키에서 “Cancer Multiomics 요약 보강이 필요한” 논문은 무엇인가?
**A.** seed 중 'Cancer Multiomics 요약 보강이 필요한' 논문은 [Huber 2025](../sources/huber-2025-comprehensive-proteogenomic-pipeline-neoantigen-discovery.md)(NeoDisc)다. 이 source 페이지는 frontmatter topic이 ptmanchor / extra_topics가 bcell-neoantigen로 잡혀 있고, Cancer Multiomics 요약을 본문에 직접 쓰지 않고 별도 분석 subpage(analyses/.../huber-2025-neodisc-neoantigen-pipeline.md) 링크로만 미룬다. 즉 다른 seed들이 본문에 '## Cancer Multiomics Project Relevance / 과제 관련성'을 채워둔 것과 달리(예: [Savage 2024](../sources/savage-2024-pan-cancer-proteogenomics-expands-landscape-therapeutic.md)는 본문에 WGS→functional state→약물표적 프레임으로 관련성을 명시) Huber 2025는 neoantigen·pipeline 관점 Key Points만 있고 Cancer Multiomics 축(반응예측·면역회피 통합) 요약이 비어 있다. 따라서 Huber 2025가 과제 관점 요약을 보강해야 할 대상이다.

**Cited**: [Huber 2025](../sources/huber-2025-comprehensive-proteogenomic-pipeline-neoantigen-discovery.md), [Savage 2024](../sources/savage-2024-pan-cancer-proteogenomics-expands-landscape-therapeutic.md)

### Q98. Cancer Multiomics 토픽 허브에 “표준 체크리스트”를 넣으면 어떤 field가 가장 먼저 도움이 될까?
**A.** 토픽 허브에 '표준 체크리스트'를 넣으면 가장 먼저 도움이 되는 field는 '치료 맥락(암종 / 치료제 class / 라인 / 반응 라벨 / 샘플 타이밍)'이다. seed들이 갈라지는 1차 축이 바로 이 맥락이라서, [Lee 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md)은 'TNBC / anthracycline+taxane NAC / pCR vs non-pCR / baseline+post-treatment paired'로, [Zhang 2023](../sources/zhang-2023-proteogenomics-clear-cell-renal-response-tyrosine-kinase-inhibitor.md)은 'ccRCC / sunitinib(TKI) / RECIST responder vs non-responder / treatment-naive 단일 시점'으로 정의되며, 이 맥락만으로도 어떤 반응예측·내성 질문에 쓸 수 있는지가 갈린다. 실제로 토픽 허브의 표준 메타데이터 체크리스트도 첫 bullet을 '치료 맥락'으로 두고 있어, 이 field가 논문을 과제 축에 배치하는 데 가장 먼저 효과를 낸다.

**Cited**: [Lee DK 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md), [Zhang 2023](../sources/zhang-2023-proteogenomics-clear-cell-renal-response-tyrosine-kinase-inhibitor.md)

### Q99. 교수진 Slack 공유용 “주간 digest”를 만들면 어떤 4개 섹션이 좋을까?
**A.** 교수진 Slack 공유용 주간 digest는 (1) 헤더(주차·날짜) → (2) 이번 주 핵심 논문 1~2편의 citation+무엇을 했는지·핵심 결과 → (3) 각 논문의 '한미암 활용 가능성'(시사·참고 톤) → (4) 다음 ingest·열린 질문, 이렇게 4개 섹션이 좋다. 이는 seed 페이지가 이미 보유한 'Slack 메시지 초안' 형식과 일치하는데, [Lee 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md)·[Chang 2026](../sources/chang-2026-integrative-proteogenomics-gastric-cancer-taiwan.md) 같은 논문은 핵심 수치 1개(예: Lee non-pCR AUC 0.946, Chang DBAC HR 2.36–3.16)와 그 한계를 짝지어 제시하므로 digest의 결과 섹션에 그대로 옮길 수 있다. 톤은 '적용하세요'가 아니라 '참고해볼 수 있겠다·시사한다'는 큐레이션 어조로, 관찰 결과에는 '관찰·연관, 인과 아님' caveat를 붙이는 것이 교수진 공유에 적합하다.

**Cited**: [Lee DK 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md), [chang-2026-integrative-proteogenomics-gastric-cancer-taiwan](../sources/chang-2026-integrative-proteogenomics-gastric-cancer-taiwan.md)

### Q100. 이 토픽을 통해 다음으로 만들어야 할 durable 산출물은 무엇인가(체크리스트/메타테이블/재분석 노트)?
**A.** 이 토픽에서 다음으로 만들 durable 산출물은 '표준 추출 체크리스트 + 논문 메타테이블 + 한국인 코호트 재분석 노트' 세 가지다. 체크리스트는 치료맥락/데이터레이어/데이터공개/핵심방법/과제연결을 고정하고, 메타테이블은 그 줄들을 한 행씩 모아 [Lee 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md)(TNBC·response 축·PRJNA1422845/PDC000695)·[Chang 2026](../sources/chang-2026-integrative-proteogenomics-gastric-cancer-taiwan.md)(GC·통합 축·dbGaP phs004447/PDC000645)·[Zhang 2023](../sources/zhang-2023-proteogenomics-clear-cell-renal-response-tyrosine-kinase-inhibitor.md)(ccRCC·phospho 축)을 한눈에 비교 가능하게 한다. 재분석 노트는 이들 공개 데이터(예: PDC000695/696의 phospho 5,373 protein·31,258 site)를 한미암 baseline에 매핑해 NMF subtype·pCR 분포·kinase activity가 재현되는지 검증하는 실행 문서로, 단순 요약을 넘어 다음 분석으로 이어지는 자산이 된다.

**Cited**: [Lee DK 2026](../sources/lee-2026-proteogenomic-decoding-chemotherapy-resistance-tnbc.md), [chang-2026-integrative-proteogenomics-gastric-cancer-taiwan](../sources/chang-2026-integrative-proteogenomics-gastric-cancer-taiwan.md), [Zhang 2023](../sources/zhang-2023-proteogenomics-clear-cell-renal-response-tyrosine-kinase-inhibitor.md)
