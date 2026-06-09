---
title: "Immunotherapy Resistance & Immune Evasion — Topic Questions (Answered)"
tags:
  - question-bank
  - resistance
  - answered
date: 2026-06-08
status: answered-2026-06
---

# Immunotherapy Resistance & Immune Evasion — Topic Questions (Answered)

위키 확장 질문에 로컬 `wiki/sources/` 논문 근거로 답을 단 sprint. 답·근거는 그래프(`interactives/llm-wiki-all.html`)에 질문 노드로 자동 반영된다.

## Section A — Immunotherapy resistance & immune evasion (Q1-100)

### Q1. primary resistance와 acquired resistance는 각 논문에서 어떤 기준으로 구분되는가?
**A.** 논문들은 면역치료 반응의 **시간 축**을 기준으로 primary와 acquired resistance를 구분한다. [Sharma 2017](../sources/sharma-2017-primary-adaptive-acquired-resistance-cancer.md)는 종양세포와 면역계의 상호작용이 종양 발생부터 전이까지 연속적·동적으로 진화한다고 보며, 치료에 처음부터 반응하지 못하는 primary(및 adaptive) 내성과 치료로 일단 반응했다가 이후 진행하는 acquired 내성을 별개의 기전 범주로 둔다. [Schoenfeld 2020](../sources/schoenfeld-2020-acquired-resistance-immune-checkpoint-inhibitors.md)은 acquired resistance를 "초기 반응 후 나중에 진행"으로 명시적으로 정의하며, [Zaretsky 2016](../sources/zaretsky-2016-acquired-resistance-pd1-melanoma.md)은 pembrolizumab에 객관적 퇴축을 보인 뒤 진행한 흑색종에서 면역반응이 이미 일어난 뒤 선택된 변이(JAK1/2·B2M)를 acquired의 근거로 제시해, baseline 면역무지(primary)와 immunoediting 기반 선택(acquired)을 구분한다.

**Cited**: [Sharma 2017](../sources/sharma-2017-primary-adaptive-acquired-resistance-cancer.md), [Schoenfeld 2020](../sources/schoenfeld-2020-acquired-resistance-immune-checkpoint-inhibitors.md), [Zaretsky 2016](../sources/zaretsky-2016-acquired-resistance-pd1-melanoma.md)

### Q2. response, stable disease, hyperprogression, relapse를 다루는 endpoint 정의는 논문마다 어떻게 다른가?
**A.** response/relapse 같은 endpoint 정의는 논문이 다루는 치료 단계에 따라 달라진다. [Memon 2024](../sources/memon-2024-clinical-molecular-features-acquired-resistance.md)는 NSCLC 1,201명에서 acquired resistance(relapse)를 "초기 반응자에서의 방사선학적 진행"으로 잡고, post-treatment 조직을 진행 시점 이후·새 전신치료 시작 전에 채취해 IFNγ 반응이 stable인지 increase인지로 relapse 종양을 다시 층화한다. 반면 [Schoenfeld 2020](../sources/schoenfeld-2020-acquired-resistance-immune-checkpoint-inhibitors.md)은 acquired resistance가 임상 보고마다 정의가 제각각이고 표준화가 미흡하다는 점을 한계로 지적한다. hyperprogression은 별도 endpoint로 다뤄지는데, [Xu-Monette 2018](../sources/xumonette-2018-pd-1-expression-clinical-pd-1-blockade.md)은 B세포 림프종 PD-1 차단 맥락에서 hyperprogression을 반응·독성과 함께 논의 대상으로 명시한다.

**Cited**: [Memon 2024](../sources/memon-2024-clinical-molecular-features-acquired-resistance.md), [Schoenfeld 2020](../sources/schoenfeld-2020-acquired-resistance-immune-checkpoint-inhibitors.md), [Xu-Monette 2018](../sources/xumonette-2018-pd-1-expression-clinical-pd-1-blockade.md)

### Q3. tumor-intrinsic resistance와 microenvironment-mediated resistance를 가르는 근거는 무엇인가?
**A.** tumor-intrinsic와 microenvironment-mediated resistance를 가르는 근거는 **결함이 종양세포 유전형에 있는지, 기질·면역 구조에 있는지**다. [Shin 2017](../sources/shin-2017-primary-resistance-pd1-jak-mutations.md)은 JAK1/2 loss-of-function으로 종양세포가 IFN-γ를 감지하지 못하는 세포내재적(tumor-intrinsic) 회로를, [Gettinger 2017](../sources/gettinger-2017-hla-antigen-presentation-checkpoint-lung.md)은 B2M 소실로 인한 class I 항원제시 결함을 보여, 종양이 "종이 위에서는" 항원성을 가져도 인식·이펙터 회로에서 차단됨을 입증한다. 반대로 [Mariathasan 2018](../sources/mariathasan-2018-tgfb-pdl1-blockade-tcell-exclusion.md)은 요로상피암 비반응이 섬유아세포의 TGF-β 신호와 연결되어 CD8 T세포가 종양 실질로 못 들어가고 주변 기질에 갇히는 immune-excluded 표현형임을 보여, 일부 내성은 종양 유전형이 아니라 기질 구조 문제임을 시사한다.

**Cited**: [Shin 2017](../sources/shin-2017-primary-resistance-pd1-jak-mutations.md), [Gettinger 2017](../sources/gettinger-2017-hla-antigen-presentation-checkpoint-lung.md), [Mariathasan 2018](../sources/mariathasan-2018-tgfb-pdl1-blockade-tcell-exclusion.md)

### Q4. immunotherapy resistance를 checkpoint blockade, CAR-T, bispecific, ADC, targeted therapy 이후 immune remodeling으로 나누면 어떤 지도가 생기는가?
**A.** 치료 modality별로 내성 이후 immune remodeling을 나누면, **항원 인식 차단(checkpoint·CAR-T)** 축과 **항원 방출·innate 면역 활성화(ADC)** 축이 대비되는 지도가 생긴다. checkpoint blockade 쪽에서는 [Zaretsky 2016](../sources/zaretsky-2016-acquired-resistance-pd1-melanoma.md)이 IFN 신호·항원제시 소실을, CAR-T 쪽에서는 [Sotillo 2015](../sources/sotillo-2015-cd19-mutations-alternative-splicing-cart19.md)이 CD19 exon2 skipping·돌연변이를 통한 항원 escape를 보여 "표적 인식 상실"로 수렴한다. [Ruella 2023](../sources/ruella-2023-cart-resistance-haematological-malignancies.md)은 CAR-T 내성을 세포제품 기능부전·종양내재·면역억제 미세환경 세 층으로 정리한다. 반대로 [Oh 2024](../sources/oh-2024-tdxd-cgas-sting-gastric-cancer.md)는 trastuzumab deruxtecan이 DNA 손상으로 cGAS-STING·제1형 IFN을 켜고 PD-L1을 올려, ADC가 항원 방출/IFN 신호를 통해 종양 면역원성을 재편하고 checkpoint와 연결될 수 있음을 보여 별도 가지를 형성한다.

**Cited**: [Zaretsky 2016](../sources/zaretsky-2016-acquired-resistance-pd1-melanoma.md), [Sotillo 2015](../sources/sotillo-2015-cd19-mutations-alternative-splicing-cart19.md), [Ruella 2023](../sources/ruella-2023-cart-resistance-haematological-malignancies.md), [Oh 2024](../sources/oh-2024-tdxd-cgas-sting-gastric-cancer.md)

### Q5. cancer-immunity cycle의 어느 단계가 각 resistance mechanism에서 막히는가?
**A.** cancer-immunity cycle를 기준틀로 쓰면 각 내성 기전이 **사이클의 어느 단계를 끊는지** 매핑할 수 있다. [Chen 2013](../sources/chen-2013-cancer-immunity-cycle.md)은 항원 방출→제시→T세포 priming→trafficking→침윤→인식→살해의 단계 모델을 제시하며, 성공적 면역치료는 종양마다 어느 단계가 망가졌는지 식별하는 데 달려 있고 PD-L1 차단은 사이클의 한 브레이크만 제거함을 강조한다. 이 틀에 비춰보면 [Mariathasan 2018](../sources/mariathasan-2018-tgfb-pdl1-blockade-tcell-exclusion.md)의 TGF-β 매개 immune exclusion은 **trafficking·침윤** 단계 차단, [Gettinger 2017](../sources/gettinger-2017-hla-antigen-presentation-checkpoint-lung.md)의 B2M/class I 소실은 **인식(recognition)** 단계 차단, [Shin 2017](../sources/shin-2017-primary-resistance-pd1-jak-mutations.md)의 JAK1/2 결함은 IFN 감지 실패로 이펙터 단계가 막히는 사례로 배치된다.

**Cited**: [Chen 2013](../sources/chen-2013-cancer-immunity-cycle.md), [Mariathasan 2018](../sources/mariathasan-2018-tgfb-pdl1-blockade-tcell-exclusion.md), [Gettinger 2017](../sources/gettinger-2017-hla-antigen-presentation-checkpoint-lung.md), [Shin 2017](../sources/shin-2017-primary-resistance-pd1-jak-mutations.md)

### Q6. immune set point 개념은 single biomarker보다 어떤 설명력을 주는가?
**A.** immune set point 개념은 단일 biomarker보다 **다변수 임계값**으로 반응을 설명하는 힘을 준다. [Chen 2017](../sources/chen-2017-cancer-immune-set-point.md)은 cancer-immune set point를 생산적 항종양 면역이 나타나려면 넘어야 하는 유효 임계값으로 정의하고, 종양 유전체·항원성·checkpoint 신호·숙주 상태·미생물총·감염력·환경 노출이 모두 그 임계값에 기여한다고 본다. 이 관점은 종양을 immune-inflamed/excluded/desert 표현형으로 묶고 PD-L1을 유용하지만 불완전한 표지자로 취급하며, 단일 표지자 예측 대신 복합 면역 프로파일링을 주장한다. 실제로 [Cristescu 2018](../sources/cristescu-2018-pan-tumor-genomic-biomarkers-pd1-blockade.md)이 TMB와 T세포 염증 GEP가 서로 약하게만 상관함을 보인 것은 단일 변수로 환원되지 않는 set point 논리를 뒷받침한다.

**Cited**: [Chen 2017](../sources/chen-2017-cancer-immune-set-point.md), [Cristescu 2018](../sources/cristescu-2018-pan-tumor-genomic-biomarkers-pd1-blockade.md)

### Q7. TMB, PD-L1, MSI-H, dMMR, IFN signature 중 어떤 biomarker가 어떤 상황에서 실패하는가?
**A.** 각 biomarker는 그것이 포착하지 못하는 **다른 생물학적 축**이 작동할 때 실패한다. [Cristescu 2018](../sources/cristescu-2018-pan-tumor-genomic-biomarkers-pd1-blockade.md)은 TMB(항원성)와 T세포 염증 GEP(기존 면역 활성화)가 서로 약하게만 상관하므로, 돌연변이는 많지만 염증이 없는 종양(또는 그 반대)에서 한쪽 biomarker가 빗나감을 보여준다. TMB·MSI-H의 한계는 [Shin 2017](../sources/shin-2017-primary-resistance-pd1-jak-mutations.md)이 직접 보여주는데, 높은 돌연변이 부담에도 JAK1/2 결함으로 IFN을 감지 못하는 흑색종·dMMR 대장암은 PD-1에 반응하지 않아 hypermutation을 충분조건으로 보면 안 된다고 경고한다. MSI-H 자체도 균질하지 않아서, [Yang 2021](../sources/yang-2021-msih-gastric-cancer-heterogeneity-worse-survival.md)은 MSI-H 위암을 면역억제 특성이 풍부한 예후 불량 아형(MSI-H1)과 다른 아형으로 나눠, MSI-H가 자동으로 양호한 예후나 균일한 checkpoint 감수성을 뜻하지 않음을 보인다.

**Cited**: [Cristescu 2018](../sources/cristescu-2018-pan-tumor-genomic-biomarkers-pd1-blockade.md), [Shin 2017](../sources/shin-2017-primary-resistance-pd1-jak-mutations.md), [Yang 2021](../sources/yang-2021-msih-gastric-cancer-heterogeneity-worse-survival.md)

### Q8. pan-tumor biomarker와 cancer-specific biomarker는 어떤 조건에서 충돌하는가?
**A.** pan-tumor biomarker와 cancer-specific biomarker는 **암종 내부의 이질성**이 pan-tumor 라벨을 무너뜨릴 때 충돌한다. [Cristescu 2018](../sources/cristescu-2018-pan-tumor-genomic-biomarkers-pd1-blockade.md)은 22개 암종 300여 검체에서 TMB와 GEP가 범종양적으로 반응을 예측함을 보여 pan-tumor 표지자의 근거를 제시하지만, 두 축이 약하게만 상관해 한 변수로 종양을 묶을 수 없음도 함께 보인다. [Yang 2021](../sources/yang-2021-msih-gastric-cancer-heterogeneity-worse-survival.md)은 같은 MSI-H라도 위암에서 면역억제 특성에 따라 예후가 갈리는 아형이 존재함을 보여, pan-tumor 라벨(MSI-H)이 cancer-specific 맥락에서 더 세밀한 면역 주석을 필요로 함을 시사한다. 즉 충돌은 pan-tumor 표지자가 양성이어도 특정 암종의 미세환경·아형이 반응을 뒤집을 때 발생한다.

**Cited**: [Cristescu 2018](../sources/cristescu-2018-pan-tumor-genomic-biomarkers-pd1-blockade.md), [Yang 2021](../sources/yang-2021-msih-gastric-cancer-heterogeneity-worse-survival.md)

### Q9. 같은 biomarker-positive tumor 안에서 response heterogeneity가 생기는 이유는 무엇인가?
**A.** 같은 biomarker-positive 종양 안에서도 response heterogeneity가 생기는 큰 이유는 **항원의 클론성·아클론 분포(intratumoral heterogeneity)**다. [Roerden 2024](../sources/roerden-2024-neoantigen-architectures-define-immunogenicity-drive.md)는 neoantigen의 동시발현과 clonality가 만드는 "NeoAg architecture"가 개별 항원의 면역원성을 좌우하며, 이질적 항원 발현 종양에서는 cDC1 매개 T세포 반응들이 서로 경쟁해 종양 가지(branch)에 대한 반응이 억제되고 이것이 ICB 내성을 유발한다고 보여, 같은 종양 안에서 반응이 갈리는 메커니즘을 제시한다. 이는 [Cristescu 2018](../sources/cristescu-2018-pan-tumor-genomic-biomarkers-pd1-blockade.md)이 TMB 같은 bulk 표지자가 양성이어도 면역 활성화 축이 따로 노는 점, [Yang 2021](../sources/yang-2021-msih-gastric-cancer-heterogeneity-worse-survival.md)이 MSI-H 라벨 내부에 면역억제 아형이 숨어 있음을 보인 점과 부합한다.

**Cited**: [Roerden 2024](../sources/roerden-2024-neoantigen-architectures-define-immunogenicity-drive.md), [Cristescu 2018](../sources/cristescu-2018-pan-tumor-genomic-biomarkers-pd1-blockade.md), [Yang 2021](../sources/yang-2021-msih-gastric-cancer-heterogeneity-worse-survival.md)

### Q10. resistance 논문에서 pre-treatment sample과 on-treatment sample의 해석 차이는 무엇인가?
**A.** resistance 논문에서 pre-treatment 검체는 **baseline 면역무지/primary 내성**을, on-treatment(또는 진행 후) 검체는 **치료로 선택·재편된 상태(acquired)**를 읽는 데 쓰이며 해석이 다르다. [Memon 2024](../sources/memon-2024-clinical-molecular-features-acquired-resistance.md)는 paired pre/post 조직을 진행 후·새 치료 전에 채취해, acquired resistance가 immune-excluded/deserted가 아니라 IFNγ 반응이 지속·증가하는 "진행 중이지만 변형된 IFN 반응" 상태이고 일부에서 post-treatment B2M 소실이 나타남을 보여 시점별 해석 차이를 명시한다. [Zaretsky 2016](../sources/zaretsky-2016-acquired-resistance-pd1-melanoma.md)도 paired biopsy로 초기 반응 후 진행 시점에 JAK1/2·B2M 변이가 선택됨을 보여, 이를 immunoediting의 증거로 해석한다(pre-treatment만으로는 알 수 없음). [Sharma 2017](../sources/sharma-2017-primary-adaptive-acquired-resistance-cancer.md)은 면역-종양 상호작용이 동적으로 진화하므로 단일 시점이 아니라 시간 축에서 내성을 읽어야 한다는 틀을 제공한다.

**Cited**: [Memon 2024](../sources/memon-2024-clinical-molecular-features-acquired-resistance.md), [Zaretsky 2016](../sources/zaretsky-2016-acquired-resistance-pd1-melanoma.md), [Sharma 2017](../sources/sharma-2017-primary-adaptive-acquired-resistance-cancer.md)

### Q11. B2M loss, HLA loss, antigen processing defect는 ICI resistance에서 어떻게 구분되는가?
**A.** 세 결함은 **항원제시 회로에서 망가진 위치와 결과의 범위**로 구분된다. [Gettinger 2017](../sources/gettinger-2017-hla-antigen-presentation-checkpoint-lung.md)이 보인 B2M 소실은 class I 중쇄의 표면 안정화를 담당하는 공통 부품이 사라지는 것이라 모든 HLA 대립유전자의 표면 제시가 한꺼번에 붕괴하고(전면적 class I 음성), [Zaretsky 2016](../sources/zaretsky-2016-acquired-resistance-pd1-melanoma.md)도 흑색종 진행 종양에서 truncating B2M 변이 시 표면 MHC-I이 사라짐을 확인했다. 반면 [McGranahan 2017](../sources/mcgranahan-2017-allele-specific-hla-loss-lung-cancer.md)의 HLA loss(LOH)는 특정 대립유전자만 선택적으로 잃는 부분적 결함이라 그 allele이 제시하던 neoantigen만 안 보이고 나머지 제시는 유지되며, 이는 항원처리(TAP/B2M) 결함과 달리 LOHHLA로 대립유전자 카피수 소실을 따로 입증해야 드러난다. 즉 B2M·항원처리 결함은 '전면적·기능적' 소실, allele-specific HLA loss는 '국소적·구조적' 소실로 읽힌다.

**Cited**: [Gettinger 2017](../sources/gettinger-2017-hla-antigen-presentation-checkpoint-lung.md), [Zaretsky 2016](../sources/zaretsky-2016-acquired-resistance-pd1-melanoma.md), [McGranahan 2017](../sources/mcgranahan-2017-allele-specific-hla-loss-lung-cancer.md)

### Q12. allele-specific HLA loss는 neoantigen burden이 높은 tumor에서 어떤 immune escape 경로를 만든다?
**A.** neoantigen 부담이 높을수록 종양은 모든 항원을 한꺼번에 숨기기보다 **가장 위협적인 제시 통로만 외과적으로 제거**하는 escape를 택한다. [McGranahan 2017](../sources/mcgranahan-2017-allele-specific-hla-loss-lung-cancer.md)은 폐암의 약 40%에서 allele-specific HLA loss(LOH)가 나타나고, 이것이 높은 subclonal neoantigen 부담·APOBEC 변이·세포독성 활성과 동반되어 면역압력이 그 소실을 선택했음을 시사한다고 보고한다. 핵심은 종양이 면역원성을 유지할 만큼 항원성을 갖고도 그 항원을 제시하는 특정 HLA 대립유전자만 지움으로써 인식을 회피한다는 점이며, 이는 흔히 subclonal·공간적 이질성으로 나타나 종양 가지마다 다른 회피를 만든다. [Tran 2016](../sources/tran-2016-kras-tcell-transfer-hla-loss.md)은 그 단일 사례 증명으로, KRAS G12D 항원은 그대로 둔 채 이를 제시하던 HLA-C*08:02 일배체형(6번 염색체)만 잃은 병변이 T세포 인식을 빠져나감을 보여 'allele 단위 제시 맥락 제거'라는 경로를 직접 입증한다.

**Cited**: [McGranahan 2017](../sources/mcgranahan-2017-allele-specific-hla-loss-lung-cancer.md), [Tran 2016](../sources/tran-2016-kras-tcell-transfer-hla-loss.md)

### Q13. JAK1/2 mutation과 IFN pathway defect는 tumor killing과 antigen presentation을 각각 어떻게 방해하는가?
**A.** JAK1/2 변이로 인한 IFN 경로 결함은 **하나의 회로 차단이 두 축을 동시에 무너뜨린다**. [Shin 2017](../sources/shin-2017-primary-resistance-pd1-jak-mutations.md)은 JAK1/2 loss-of-function 종양세포가 IFN-γ 자극 후에도 PD-L1을 포함한 IFN 반응 프로그램을 켜지 못함을 보여, 종양이 이펙터 사이토카인(IFN-γ) 신호 자체를 감지하지 못해 IFN-γ 매개 성장정지·살해 효과가 차단됨을 입증한다. 동시에 IFN-γ는 항원제시 기구(HLA class I, 면역프로테아좀, TAP)를 상향시키는 주요 자극이므로 [Zaretsky 2016](../sources/zaretsky-2016-acquired-resistance-pd1-melanoma.md)에서처럼 JAK1/2 결함은 이 IFN 유도성 항원제시 증폭을 못 받아 표면 항원 디스플레이도 위축된다. [Duong 2022](../sources/duong-2022-type-i-interferon-activates-mhc.md)는 제1형 IFN이 종양유래 peptide-MHC-I을 받아 제시하는 ISG+ 수지상세포를 활성화해 CD8 반응을 지탱함을 보여, IFN 신호 붕괴가 살해뿐 아니라 교차제시 기반 priming까지 약화시킴을 보완한다.

**Cited**: [Shin 2017](../sources/shin-2017-primary-resistance-pd1-jak-mutations.md), [Zaretsky 2016](../sources/zaretsky-2016-acquired-resistance-pd1-melanoma.md), [Duong 2022](../sources/duong-2022-type-i-interferon-activates-mhc.md)

### Q14. MHC-I downregulation이 genetic loss인지 reversible suppression인지 구분하려면 어떤 evidence가 필요한가?
**A.** MHC-I downregulation이 **불가역적 유전 소실인지 가역적 억제인지**는 DNA 수준 병변과 회복 가능성을 함께 봐야 가른다. [Gettinger 2017](../sources/gettinger-2017-hla-antigen-presentation-checkpoint-lung.md)은 같은 코호트 안에서 homozygous B2M 소실(완전 유전적 knockout, 표면 HLA 완전 음성)과 단순 B2M downregulation(전사·발현 감소)을 모두 관찰해, 표면 음성만으로는 둘을 구분할 수 없고 B2M/HLA의 변이·카피수 소실(WES/LOH) 증거가 있어야 '유전적 소실'로 확정됨을 시사한다. [Sari 2023](../sources/sari-2023-tumor-immune-evasion-through-loss.md)은 항원제시 불활성화 기전이 돌연변이부터 가역적 억제까지 다양하며 일부는 되돌릴 수 있다고 정리해, 회복 실험이 판별에 필요함을 제시한다. 실제로 [Liu 2026](../sources/liu-2026-usp22-ezh2-mhc1-checkpoint-resistance.md)은 USP22-EZH2 매개 후성유전적 MHC-I 억제를 약물로 풀면 발현이 되살아남을 보여, IFN-γ 자극이나 표적 억제제로 표면 MHC-I이 복구되면 그것은 유전적 소실이 아니라 가역적 억제라는 결정적 근거가 된다.

**Cited**: [Gettinger 2017](../sources/gettinger-2017-hla-antigen-presentation-checkpoint-lung.md), [Sari 2023](../sources/sari-2023-tumor-immune-evasion-through-loss.md), [Liu 2026](../sources/liu-2026-usp22-ezh2-mhc1-checkpoint-resistance.md)

### Q15. autophagy-mediated MHC-I degradation은 classical antigen presentation defect와 어떻게 다르게 해석되는가?
**A.** autophagy 매개 MHC-I 분해는 **유전형은 멀쩡한데 단백질이 표면에서 사후적으로 치워지는** 결함이라 고전적 항원제시 결함과 다르게 해석된다. [Yamamoto 2020](../sources/yamamoto-2020-autophagy-promotes-immune-evasion-pancreatic.md)은 췌장암에서 MHC-I 소실 돌연변이나 LOH가 드문데도 MHC-I 표면 발현이 흔히 낮고, 그 이유가 NBR1 cargo 수용체를 통해 MHC-I이 선택적으로 autophagosome·lysosome으로 끌려가 분해되기 때문임을 보였다. 따라서 B2M/HLA 변이 같은 '생합성·구조' 결함과 달리 이것은 '분해·turnover' 결함이며, autophagy를 억제(클로로퀸 등)하면 표면 MHC-I과 항원제시가 회복되고 CD8 반응이 살아나 가역적이라는 점이 핵심 차이다. [Sari 2023](../sources/sari-2023-tumor-immune-evasion-through-loss.md)도 항원제시 결함을 합성 단계뿐 아니라 분해를 포함한 여러 단계로 나눠, autophagy성 소실을 되돌릴 수 있는 별도 범주로 다룬다.

**Cited**: [Yamamoto 2020](../sources/yamamoto-2020-autophagy-promotes-immune-evasion-pancreatic.md), [Sari 2023](../sources/sari-2023-tumor-immune-evasion-through-loss.md)

### Q16. epigenetic silencing of MHC-I 또는 retroelement suppression은 어떤 치료 조합으로 되돌릴 수 있는가?
**A.** MHC-I의 후성유전적 침묵은 구조적 소실과 달리 **억제 인자를 약물로 풀면 발현이 되돌아오므로 표적·조합치료가 성립**한다. [Liu 2026](../sources/liu-2026-usp22-ezh2-mhc1-checkpoint-resistance.md)은 USP22가 EZH2를 안정화해 MHC-I 경로 유전자를 전사적으로 억압함을 규명하고, USP22를 유전적·약리적으로 억제하면 종양 면역원성과 anti-PD-1 감수성이 회복됨을 보여 'EZH2 축 차단 + checkpoint' 조합의 근거를 제시한다(EZH2 억제제로 MHC-I 재발현을 노리는 전략과 직결). [Meng 2025](../sources/meng-2025-reversal-tumour-immune-evasion-enhanced.md)은 다른 가역적 축으로, MHC-I 분해를 촉진하는 PCSK9를 siRNA로 녹다운하면 항원제시 효율이 최대 6배 오르고 종양항원 mRNA 백신과 결합해 CD8·NK 침윤을 늘려 면역치료 효과를 끌어올림을 보여, 후성유전·발현 수준 억제는 표적 RNA/소분자 + 백신·ICI 조합으로 되돌릴 수 있음을 뒷받침한다.

**Cited**: [Liu 2026](../sources/liu-2026-usp22-ezh2-mhc1-checkpoint-resistance.md), [Meng 2025](../sources/meng-2025-reversal-tumour-immune-evasion-enhanced.md)

### Q17. 9p21 alteration, STING suppression은 immune-cold tumor와 어떻게 연결되는가?
**A.** 9p21 소실과 STING 억제는 **종양이 내인성 IFN·chemokine을 못 만들어 면역세포를 불러오지 못하는 immune-cold 상태**로 수렴한다. [Zhao 2025](../sources/zhao-2025-interferon-epsilon-9p21-immune-cold-tumors.md)은 9p21 결손이 단지 유명 종양억제유전자(CDKN2A 등) 소실에 그치지 않고 제1형 IFN, 특히 IFN-epsilon 소실을 통해 내인성 CXCL9/10 유도를 무너뜨려 수지상세포·CD8 T세포 모집을 차단하는 기전적 다리임을 제시하며, 이것이 일견 면역치료 표지자가 있어도 cold·checkpoint 내성으로 가는 이유를 설명한다. [Zhang 2021](../sources/zhang-2021-met-amplification-inhibits-sting-immunotherapy.md)은 같은 innate-sensing 축의 다른 입구로, MET 증폭이 UPF1 인산화를 통해 종양세포 STING 발현을 낮춰 T세포 침윤이 줄고 ICI 반응·PFS가 나빠짐을 보여, STING 억제가 곧 innate 감지 실패→cold TME→checkpoint 둔감으로 이어짐을 입증한다.

**Cited**: [Zhao 2025](../sources/zhao-2025-interferon-epsilon-9p21-immune-cold-tumors.md), [Zhang 2021](../sources/zhang-2021-met-amplification-inhibits-sting-immunotherapy.md)

### Q18. tumor antigen loss와 antigen presentation loss는 치료 선택에서 어떻게 다른 문제인가?
**A.** 두 문제는 **항원 자체가 사라졌는지, 항원은 있는데 보여주는 창구가 막혔는지**가 달라 치료 선택이 갈린다. [Tran 2016](../sources/tran-2016-kras-tcell-transfer-hla-loss.md)에서 보듯 antigen presentation loss(HLA 일배체형 소실)는 표적 항원(KRAS G12D)이 그대로 남아 있어 같은 항원을 노리는 백신·TCR/TIL을 다시 줘도 제시가 안 되면 무력하므로, 제시 회로(IFN 유도·후성유전 억제 해제) 복구나 MHC 비의존 전략(NK·ADC)으로 방향을 틀어야 한다. 반대로 tumor antigen loss는 표적 자체가 없어진 것이라 [Grasso 2018](../sources/grasso-2018-genetic-mechanisms-immune-evasion-colorectal-cancer.md)이 대장암에서 보인 면역편집처럼 다른 항원·다클론 표적으로 갈아타야 한다. [Sari 2023](../sources/sari-2023-tumor-immune-evasion-through-loss.md)은 제시 결함 중 가역적인 것(억제·분해)과 불가역적인 것(B2M/HLA 변이)을 나눠, 제시 손실이 가역적이면 복구치료가, 불가역적이면 MHC 비의존 접근이 합리적이라는 선택 기준을 제공한다.

**Cited**: [Tran 2016](../sources/tran-2016-kras-tcell-transfer-hla-loss.md), [Grasso 2018](../sources/grasso-2018-genetic-mechanisms-immune-evasion-colorectal-cancer.md), [Sari 2023](../sources/sari-2023-tumor-immune-evasion-through-loss.md)

### Q19. antigen escape 이후 CD8 T cell response가 유지되는지 붕괴되는지 어떻게 확인하는가?
**A.** antigen escape 이후 CD8 반응이 **유지되는지 붕괴했는지는 미세환경의 IFN·염증 상태와 T세포 분화 상태를 함께 읽어** 확인한다. [Memon 2024](../sources/memon-2024-clinical-molecular-features-acquired-resistance.md)는 NSCLC 진행 종양을 paired pre/post 조직의 전사체로 분석해, 획득내성이 immune-excluded/deserted가 아니라 IFNγ 반응이 '안정' 또는 '증가'하며 면역세포가 계속 침윤하는 '지속적이지만 변형된 IFN 반응' 상태일 수 있음을 보여, IFNγ-response 유전자 시그니처와 침윤 정도로 반응 잔존 여부를 층화한다. [Castiglioni 2023](../sources/castiglioni-2023-combined-pd-l1tgf-blockade-allows-expansion.md)은 단순 침윤 수가 아니라 stem cell-like vs 말단분화(exhausted) CD8의 비율이 반응 지속성을 좌우함을 보여, 표현형 분석이 '유지 대 붕괴' 판별의 핵심임을 시사한다. [Duong 2022](../sources/duong-2022-type-i-interferon-activates-mhc.md)는 진행 종양에서 ISG+ DC·제1형 IFN 회로가 살아 있으면 CD8 반응이 보존됨을 보여, IFN·DC 활성 지표를 보조 판별 근거로 쓸 수 있게 한다.

**Cited**: [Memon 2024](../sources/memon-2024-clinical-molecular-features-acquired-resistance.md), [Castiglioni 2023](../sources/castiglioni-2023-combined-pd-l1tgf-blockade-allows-expansion.md), [Duong 2022](../sources/duong-2022-type-i-interferon-activates-mhc.md)

### Q20. acquired ICI resistance에서 neoantigen loss와 immune exhaustion 중 무엇이 더 직접적인 driver인가?
**A.** 로컬 근거는 **단일 정답보다 맥락 의존**임을 시사하지만, 직접적(causal) driver 쪽으로는 항원/제시 손실의 비중을 높게 둔다. [Sholokhova 2026](../sources/sholokhova-2026-neoantigen-evolution-response-checkpoint-inhibitor-immunotherapy.md)은 대장암 시뮬레이션에서 '강한 clonal neoantigen 1개'의 존재와 minimal neoantigen quality가 durable response의 가장 강력한 예측인자임을 보여, 그 핵심 항원의 소실이 곧 반응 붕괴로 직결되는 직접 동인임을 시사한다. [Łuksza 2022](../sources/uksza-2022-neoantigen-quality-predicts-immunoediting-survivors.md)도 췌장암 장기생존자에서 면역압력이 high-quality neoantigen을 실제로 편집해 재발 종양에서 그 항원이 줄어듦을 보여, neoantigen loss가 면역회피의 인과적 산물임을 뒷받침한다. 다만 [Memon 2024](../sources/memon-2024-clinical-molecular-features-acquired-resistance.md)는 NSCLC 획득내성 다수가 항원제시 변이뿐 아니라 지속 IFN 신호·면역 dysfunction(exhaustion에 가까운 상태)을 동반함을 보여, exhaustion은 종종 항원/제시 손실과 공존하는 동반 요인이며 둘 중 무엇이 직접 driver인지는 종양마다 항원 손실 증거(B2M/HLA·neoantigen 소실)의 유무로 판별해야 함을 시사한다.

**Cited**: [Sholokhova 2026](../sources/sholokhova-2026-neoantigen-evolution-response-checkpoint-inhibitor-immunotherapy.md), [Łuksza 2022](../sources/uksza-2022-neoantigen-quality-predicts-immunoediting-survivors.md), [Memon 2024](../sources/memon-2024-clinical-molecular-features-acquired-resistance.md)

### Q21. CD19 CAR-T resistance에서 antigen mutation, alternative splicing, lineage switch는 어떻게 다르게 발생하는가?
**A.** 세 경로는 같은 "항원 회피"여도 분자 기전과 가역성이 다르다. **Antigen mutation**은 CD19 exon 2~5에 truncating mutation이 생겨 막관통 도메인까지 소실되는 비가역적 구조 결손으로, CD19-음성 재발 세포의 변이 대립유전자 빈도가 음성 분획과 일치할 만큼 클론 우세하게 고정된다([Orlando 2018](../sources/orlando-2018-target-antigen-loss-car19-therapy.md)). **Alternative splicing**은 SRSF3 감소로 exon 2 skipping이 일어나 CAR 인식 에피토프만 제거하면서 부분적 CD19 생물학과 백혈병 fitness는 보존하는, 잠재적으로 가역적인 회피다([Sotillo 2015](../sources/sotillo-2015-cd19-mutations-alternative-splicing-cart19.md)). **Lineage switch**는 항원 자체를 바꾸는 것을 넘어 B-계열 모세포가 골수성(AML)으로 transdifferentiation하는 표현형 전환으로, 창시 병변은 유지된 채 계통이 바뀐다([Qiu 2025](../sources/qiu-2025-lineage-switch-cd19-cart-treatment-ball.md)). 리뷰는 이들을 mutation·deletion·splicing·lineage switch·trogocytosis 등 target-side escape의 별개 갈래로 정리한다([Labanieh 2023](../sources/labanieh-2023-car-immune-cells-design-principles-resistance.md)).

**Cited**: [Orlando 2018](../sources/orlando-2018-target-antigen-loss-car19-therapy.md), [Sotillo 2015](../sources/sotillo-2015-cd19-mutations-alternative-splicing-cart19.md), [Qiu 2025](../sources/qiu-2025-lineage-switch-cd19-cart-treatment-ball.md), [Labanieh 2023](../sources/labanieh-2023-car-immune-cells-design-principles-resistance.md)

### Q22. lineage switch는 selection된 pre-existing clone인가, therapy-induced plasticity인가?
**A.** 로컬 근거는 양쪽 모두를 지지하되, 적어도 일부 사례는 therapy-induced plasticity 쪽에 무게를 둔다. Qiu 2025는 non-KMT2A-r B-ALL에서 CD19 CAR-T 후 AML로 전환된 두 사례를 multi-omic으로 추적해 FLT3-ITD·EP300::ZNF384 같은 창시 driver가 전환 전후로 보존됨을 보였는데, 이는 무관한 제2의 백혈병이 아니라 동일 클론의 reprogramming(잠재적 골수성 형질을 가진 B-전구체가 치료 압력 하에 transdifferentiation)임을 시사한다([Qiu 2025](../sources/qiu-2025-lineage-switch-cd19-cart-treatment-ball.md)). 다만 BCOR/BCORL1 truncating 병변이 전환을 독립적으로 유발하는지, 아니면 허용적 plasticity 상태를 표지할 뿐인지는 미해결로 남아, pre-existing clone 선택과 induced plasticity가 배타적이지 않을 수 있다. 소아 ALL에서 plasticity와 면역회피를 다룬 리뷰도 형질 가소성을 회피 축으로 제시한다([DePasquale 2022](../sources/depasquale-2022-plasticity-immune-evasion-childhood-all.md)). 반면 항원 변이 경로는 변이 빈도가 음성 분획과 일치하는 명백한 clonal selection 양상을 보여([Orlando 2018](../sources/orlando-2018-target-antigen-loss-car19-therapy.md)), lineage switch와는 기전이 구분된다.

**Cited**: [Qiu 2025](../sources/qiu-2025-lineage-switch-cd19-cart-treatment-ball.md), [DePasquale 2022](../sources/depasquale-2022-plasticity-immune-evasion-childhood-all.md), [Orlando 2018](../sources/orlando-2018-target-antigen-loss-car19-therapy.md)

### Q23. CAR-T exhaustion, trafficking failure, persistence failure는 어떤 assay로 구분되는가?
**A.** 로컬 리뷰들은 이 셋을 cell-side failure의 별개 축으로 나누지만, 단일 표준 assay 매핑을 제시하지는 않는다. Labanieh 2023은 target-side escape와 구분되는 cell-side failure를 inadequate potency·persistence·exhaustion으로 분리하고, 이는 costimulatory domain·tonic signaling·T-cell state로 측정·조율된다고 본다([Labanieh 2023](../sources/labanieh-2023-car-immune-cells-design-principles-resistance.md)). Ruella 2023은 CAR-T cell dysfunction을 종양-내재 내성·면역억제 미세환경과 분리해, exhaustion(기능 소진)과 trafficking/infiltration 실패(미세환경 접근 실패)를 서로 다른 failure mode로 위치시킨다([Ruella 2023](../sources/ruella-2023-cart-resistance-haematological-malignancies.md)). 기능적으로는, SynNotch 회로가 tonic signaling과 exhaustion을 회피해 naive/stem cell memory 분획을 높게 유지함을 보인 연구가 "exhaustion 마커·기억 표현형"이 persistence와 연동됨을 보여주어, exhaustion(소진 표현형)·persistence(생착 지속)·trafficking(종양 침투)을 구분하는 판독 축을 시사한다([Choe 2021](../sources/choe-2021-synnotch-car-t-cells-overcome-challenges.md)).

**Cited**: [Labanieh 2023](../sources/labanieh-2023-car-immune-cells-design-principles-resistance.md), [Ruella 2023](../sources/ruella-2023-cart-resistance-haematological-malignancies.md), [Choe 2021](../sources/choe-2021-synnotch-car-t-cells-overcome-challenges.md)

### Q24. solid tumor CAR-T에서 physical barrier와 antigen heterogeneity 중 어느 쪽이 더 큰 병목인가?
**A.** 로컬 근거는 어느 한쪽으로 단정하지 않고 둘이 상호 연결된 병목임을 강조하지만, solid tumor에서는 물리적 장벽/미세환경이 hematologic 성공의 비일반화를 설명하는 핵심으로 더 부각된다. Sterner 2021은 solid tumor CAR-T의 장애를 항원 escape, on-target off-tumor, 불량한 trafficking, 제한된 종양 침투, 면역억제 미세환경으로 나열하며 이들이 독립적이지 않고 서로 얽혀 있어 단일 변수 해법이 실망스럽다고 본다([Sterner 2021](../sources/sterner-2021-cart-current-limitations-potential-strategies.md)). 항원 이질성 쪽으로는, 절대적 종양 특이 항원이 없고 균질하지 않은 glioblastoma에서 SynNotch prime-and-kill 회로가 이질성·특이성·persistence를 동시에 다뤄야 했다는 점이 antigen heterogeneity의 무게를 보여준다([Choe 2021](../sources/choe-2021-synnotch-car-t-cells-overcome-challenges.md)). 물리적/미세환경 장벽 쪽으로는, mCRPC에서 PSMA-CAR-T가 TGF-β 비감수성 무장에도 불구하고 종양 침투 후 다수 미세환경 억제 분자 상향으로 실패한 사례가 TME 장벽의 결정적 역할을 보여준다([Narayan 2022](../sources/narayan-2022-psma-targeting-tgfbeta-insensitive-armored-car-t.md)).

**Cited**: [Sterner 2021](../sources/sterner-2021-cart-current-limitations-potential-strategies.md), [Choe 2021](../sources/choe-2021-synnotch-car-t-cells-overcome-challenges.md), [Narayan 2022](../sources/narayan-2022-psma-targeting-tgfbeta-insensitive-armored-car-t.md)

### Q25. armored CAR(IL-12/IL-18 등)는 어떤 resistance layer를 해결하려는가?
**A.** Armored CAR는 주로 항원 회피와 면역억제 미세환경(TME)이라는 두 내성 층을 동시에 겨냥한다. IL-12를 국소 분비하는 CAR-T는 항원 발현을 끈 antigen-loss 변이세포까지 macrophage·TNF-α 매개 선천면역을 동원해 제거함으로써, 통상 회피하는 항원-음성 병변을 표적화한다([Chmielewski 2011](../sources/chmielewski-2011-il-12-release-engineered-t-cells.md)). IL-18을 분비하는 "iIL18 TRUCK"은 CAR-T를 T-bet^high FoxO1^low 효과세포로 극성화하고 M1 macrophage·NK 증가와 Treg·M2·억제성 DC 감소로 TME를 재편해, 사이토카인 없는 CAR-T에 불응(refractory)이던 진행성 고형종양(췌장·폐)에 활성을 보인다([Chmielewski 2017](../sources/chmielewski-2017-car-t-cells-releasing-il-18.md)). 같은 맥락에서 dominant-negative TGF-β 수용체로 무장한 PSMA-CAR-T는 TGF-β가 주도하는 억제성 TME 층을 직접 무력화하려는 설계다([Narayan 2022](../sources/narayan-2022-psma-targeting-tgfbeta-insensitive-armored-car-t.md)).

**Cited**: [Chmielewski 2011](../sources/chmielewski-2011-il-12-release-engineered-t-cells.md), [Chmielewski 2017](../sources/chmielewski-2017-car-t-cells-releasing-il-18.md), [Narayan 2022](../sources/narayan-2022-psma-targeting-tgfbeta-insensitive-armored-car-t.md)

### Q26. BCMA-targeted therapy에서 antigen density와 soluble antigen은 efficacy를 어떻게 바꾸는가?
**A.** BCMA는 성숙 B림프구에 선택적으로 발현하고 다발골수종에서 과발현·활성화되어 표적 근거가 되며, 그 발현·가용성이 BsAb·ADC·CAR-T 효능의 결정 변수로 작동한다([Shah 2020](../sources/shah-2020-b-cell-maturation-antigen-bcma-multiple.md)). 항원 밀도(density) 측면에서, 리뷰는 antigen density threshold를 설계 파라미터로 다루며 수용체 구조를 항원-저(低) 회피 상태를 포착하도록 조율할 수 있다고 보아, 낮은 BCMA 밀도가 효능 저하·회피 경로가 됨을 시사한다([Labanieh 2023](../sources/labanieh-2023-car-immune-cells-design-principles-resistance.md)). 가용성 항원(soluble antigen) 자체에 대한 정량적 로컬 데이터는 제한적이나, 표적 항원 전사·발현 감소가 획득 내성과 결부됨은 anti-CD38 daratumumab에서 종양 세포의 CD38 전사 감소와 T세포 소진이 동반된 사례로 뒷받침된다([Wang 2025](../sources/wang-2025-bone-marrow-immune-ecosystem-shapes.md)). 즉 로컬 근거상 항원 밀도 저하·발현 소실은 효능을 직접 떨어뜨리는 기전으로 확인되며, soluble BCMA의 정량 효과는 본 코퍼스에서 직접 측정되지는 않았다.

**Cited**: [Shah 2020](../sources/shah-2020-b-cell-maturation-antigen-bcma-multiple.md), [Labanieh 2023](../sources/labanieh-2023-car-immune-cells-design-principles-resistance.md), [Wang 2025](../sources/wang-2025-bone-marrow-immune-ecosystem-shapes.md)

### Q27. bispecific antibody는 CAR-T와 비교해 target loss에 더 강한가 약한가?
**A.** 로컬 근거상 BsAb는 target loss에 "더 강하다"기보다 CAR-T와 거의 동일한 항원 회피 취약성을 공유한다. Falchi 2023은 CD20×CD3 BsAb의 주요 내성 기전으로 항원 escape(CD20 loss)를 꼽으며, 이는 CAR-T의 CD19 loss와 직접 평행을 이룬다고 명시한다([Falchi 2023](../sources/falchi-2023-bispecific-antibodies-treatment-b-cell-lymphoma.md)). CD19 음성 재발이 변이로 클론 우세하게 고정될 수 있다는 점([Orlando 2018](../sources/orlando-2018-target-antigen-loss-car19-therapy.md))을 고려하면, 두 양식 모두 단일 표적 소실에 취약하다. 다만 BsAb는 off-the-shelf로 재투여·표적 전환이 용이하고, 리뷰들은 multispecific·dual-target 구성이 단일 표적 대비 회피를 줄일 수 있다고 보아([Goebeler 2024](../sources/goebeler-2024-bispecific-multispecific-antibodies-oncology.md)) 운용상 대응이 유연한 편이다. 단, CD20-loss가 CD19-loss처럼 clonal selection인지 일시적 적응인지는 미해결로, "더 강함"을 단정할 수는 없다.

**Cited**: [Falchi 2023](../sources/falchi-2023-bispecific-antibodies-treatment-b-cell-lymphoma.md), [Orlando 2018](../sources/orlando-2018-target-antigen-loss-car19-therapy.md), [Goebeler 2024](../sources/goebeler-2024-bispecific-multispecific-antibodies-oncology.md)

### Q28. BsAb에서 T cell fitness, exhaustion, cytokine toxicity는 어떻게 trade-off를 만든다?
**A.** BsAb는 내인성 T세포를 MHC 비제한적으로 재유도하지만, 그 효력이 T세포 상태에 의존하면서 fitness·exhaustion·사이토카인 독성 사이에 trade-off가 생긴다. Falchi 2023은 다수 전치료된 환자에서 T세포 소진(exhaustion)이 주요 내성 기전이며, 독성은 T세포 과활성에서 비롯한 CRS·ICANS가 지배함을 지적한다 — 즉 강한 재유도는 효능과 동시에 사이토카인 독성을 키운다([Falchi 2023](../sources/falchi-2023-bispecific-antibodies-treatment-b-cell-lymphoma.md)). 이 긴장을 완화하려고 CD3 affinity 조정·step-up dosing·피하 투여·prodrug형 설계 같은 CRS 경감 전략이 동원되는데, 이는 곧 자극 강도를 낮추는 방향이라 효력과의 절충을 내포한다([Goebeler 2024](../sources/goebeler-2024-bispecific-multispecific-antibodies-oncology.md)). 임상적으로도 BCMA-CD3 redirection(teclistamab)의 독성은 고도 신경독성보다 CRS·혈구감소·감염으로 나타나, 효능을 얻는 대가로 면역활성 독성과 T세포 부담을 관리해야 함을 보여준다([Moreau 2022](../sources/moreau-2022-teclistamab-relapsed-refractory-multiple-myeloma.md)).

**Cited**: [Falchi 2023](../sources/falchi-2023-bispecific-antibodies-treatment-b-cell-lymphoma.md), [Goebeler 2024](../sources/goebeler-2024-bispecific-multispecific-antibodies-oncology.md), [Moreau 2022](../sources/moreau-2022-teclistamab-relapsed-refractory-multiple-myeloma.md)

### Q29. hematologic malignancy와 solid tumor에서 T-cell redirection resistance는 어떤 구조적 차이를 보이는가?
**A.** 로컬 근거상 가장 큰 구조적 차이는 "표적 선택 가능성과 미세환경 접근"에 있다. 혈액암에서는 CD19·CD20·BCMA 같은 계열 항원으로 효과적 재유도가 가능하고, 내성은 주로 항원 escape·T세포 exhaustion·미세환경 인자로 수렴한다([Falchi 2023](../sources/falchi-2023-bispecific-antibodies-treatment-b-cell-lymphoma.md)). 반면 고형종양에서는 종양 특이성과 정상조직 보존을 분리하기 어려운 target selection이 중심 병목이며, 억제성 미세환경 신호와 물리적 접근이 추가 장벽으로 작용한다고 리뷰는 강조한다([Goebeler 2024](../sources/goebeler-2024-bispecific-multispecific-antibodies-oncology.md)). CAR-T 쪽에서도 같은 비대칭이 관찰되는데, Sterner 2021은 혈액암의 성공이 고형종양으로 즉시 일반화되지 못한 이유를 불량한 trafficking·제한된 침투·면역억제 미세환경 등 서로 얽힌 장벽으로 설명한다([Sterner 2021](../sources/sterner-2021-cart-current-limitations-potential-strategies.md)). 즉 혈액암 내성은 주로 항원·세포 기능 축, 고형종양 내성은 표적 선택+물리적/미세환경 접근 축으로 구조가 갈린다.

**Cited**: [Falchi 2023](../sources/falchi-2023-bispecific-antibodies-treatment-b-cell-lymphoma.md), [Goebeler 2024](../sources/goebeler-2024-bispecific-multispecific-antibodies-oncology.md), [Sterner 2021](../sources/sterner-2021-cart-current-limitations-potential-strategies.md)

### Q30. ADC는 target expression의 “binary 기준”을 어떻게 무너뜨렸는가?
**A.** ADC는 "표적 양성/음성"의 이분법 기준을 임상적으로 무너뜨렸다. DESTINY-Breast04는 기존에 HER2-음성으로 분류되던 HER2-low 전이유방암에서 trastuzumab deruxtecan이 PFS·OS를 유의하게 늘려, 비교적 낮은 HER2 양으로도 이득이 가능함을 보이며 HER2-low를 서술적 병리 라벨에서 치료 가능 상태로 전환시켰다([Modi 2022](../sources/modi-2022-trastuzumab-deruxtecan-her2-low-advanced-breast-cancer.md)). DESTINY-Breast06는 이를 HER2-ultralow까지 확장해 고정된 HER2 역치 개념 자체를 약화시키고, 단일 baseline IHC 판정보다 동적 표적 발현·결합 효율·공간 이질성이 더 중요해짐을 시사한다([Bardia 2024](../sources/bardia-2024-trastuzumab-deruxtecan-after-endocrine-therapy-metastatic-breast-cancer.md)). 기전적으로도 내성은 일반적 약물내성보다 표적 매개로 재정의되어, payload 감수성이 남아도 HER2 발현 감소·결합 계면 변이(V597M, P593R)로 internalization·전달이 실패하면 효능이 사라진다 — 즉 항원 밀도·에피토프 보존·내재화 동역학이 연속 변수가 된다([Chen 2026](../sources/chen-2026-trastuzumab-deruxtecan-resistance-her2-expression-binding.md)).

**Cited**: [Modi 2022](../sources/modi-2022-trastuzumab-deruxtecan-her2-low-advanced-breast-cancer.md), [Bardia 2024](../sources/bardia-2024-trastuzumab-deruxtecan-after-endocrine-therapy-metastatic-breast-cancer.md), [Chen 2026](../sources/chen-2026-trastuzumab-deruxtecan-resistance-her2-expression-binding.md)

### Q31. ADC resistance에서 target loss와 payload resistance는 어떻게 구분되는가?
**A.** ADC 내성은 payload 자체에 대한 내성과 target 전달 실패를 구분해야 한다. [Chen 2026](../sources/chen-2026-trastuzumab-deruxtecan-resistance-her2-expression-binding.md)은 trastuzumab deruxtecan 진행 검체의 49%에서 HER2가 크게 감소(그 중 52%는 완전 소실)하고, V597M·P593R 같은 trastuzumab 결합부위 세포외도메인 변이가 결합을 방해함을 보여 — 이는 항원 밀도·epitope·internalization 동역학이 핵심 변수인 'target-mediated' 내성이다. 결정적으로 내성 세포가 동일 deruxtecan payload를 다른 target(예: TROP2)으로 전달하면 여전히 죽었으므로, payload 감수성이 유지된 채 전달만 실패한 경우(target loss)와 payload 내성(전달돼도 안 죽음)이 구분된다. 따라서 [Modi 2022](../sources/modi-2022-trastuzumab-deruxtecan-her2-low-advanced-breast-cancer.md)처럼 낮은 HER2로도 반응하는 상황에서는 이후 HER2 하향조절·결합 변화가 주된 escape 경로가 된다.

**Cited**: [Chen 2026](../sources/chen-2026-trastuzumab-deruxtecan-resistance-her2-expression-binding.md), [Modi 2022](../sources/modi-2022-trastuzumab-deruxtecan-her2-low-advanced-breast-cancer.md)

### Q32. ADC bystander effect는 heterogeneity 문제를 얼마나 보완하는가?
**A.** 로컬 근거는 bystander effect를 직접 정량화하기보다, target 이질성에 대한 ADC의 보완을 'payload는 듣는데 전달이 문제'라는 틀로 설명한다. [Modi 2022](../sources/modi-2022-trastuzumab-deruxtecan-her2-low-advanced-breast-cancer.md)의 DESTINY-Breast04는 비교적 낮은 HER2(HER2-low)만으로도 trastuzumab deruxtecan 생존 이득(PFS 5.4→10.1개월)이 나와, 일부 항원 발현 세포로도 효과가 확장될 수 있음을 시사한다. 다만 [Chen 2026](../sources/chen-2026-trastuzumab-deruxtecan-resistance-her2-expression-binding.md)은 HER2가 충분히 소실되면 internalization이 줄고 성장억제 농도가 크게 올라가 단일 target ADC만으로는 이질성을 완전히 메우지 못함을 보이며, 동일 payload를 HER2+TROP2 등 여러 target으로 저용량 전달하는 multi-target ADC 조합을 보완책으로 제시한다. 즉 bystander/저항원 전략은 이질성을 부분적으로 보완하나 완전 항원소실에는 한계가 있다.

**Cited**: [Modi 2022](../sources/modi-2022-trastuzumab-deruxtecan-her2-low-advanced-breast-cancer.md), [Chen 2026](../sources/chen-2026-trastuzumab-deruxtecan-resistance-her2-expression-binding.md)

### Q33. ADC 치료가 antigen release/IFN signaling을 통해 ICI와 연결될 수 있는가?
**A.** 예, ADC가 DNA 손상→innate 면역 활성화를 통해 ICI와 연결될 수 있다는 로컬 근거가 있다. [Oh 2024](../sources/oh-2024-tdxd-cgas-sting-gastric-cancer.md)는 trastuzumab deruxtecan이 위암세포에서 DNA 손상·apoptosis를 유도하면서 cGAS-STING 경로와 type I interferon 반응을 켜고 PD-L1 발현 및 interferon 관련 유전자 프로그램을 상향시켜, ADC가 종양 면역원성을 재편함을 보여준다. 이는 HER2 표적 ADC와 checkpoint 차단을 병용할 기전적 근거가 되며, ADC를 순수 세포자율 약물로만 보는 관점을 복잡하게 만든다. 다만 [Chen 2026](../sources/chen-2026-trastuzumab-deruxtecan-resistance-her2-expression-binding.md)이 보이듯 HER2 소실로 전달이 끊기면 이 면역활성화 자체가 약해질 수 있어, 항원 유지가 ADC-ICI 연결의 전제가 된다.

**Cited**: [Oh 2024](../sources/oh-2024-tdxd-cgas-sting-gastric-cancer.md), [Chen 2026](../sources/chen-2026-trastuzumab-deruxtecan-resistance-her2-expression-binding.md)

### Q34. EGFR-mutant NSCLC에서 ICI benefit이 낮은 이유는 어디에 더 가까운가(TMB, TME, oncogene signaling)?
**A.** 로컬 근거는 EGFR-mutant NSCLC의 낮은 ICI 이득이 단일 TMB 부족보다 종양 면역생물학(TME)과 oncogene 신호 쪽에 더 가깝다고 본다. [Offin 2019](../sources/offin-2019-tumor-mutation-burden-egfr-tki-efficacy.md)에 따르면 EGFR-mutant 종양은 전반적 TMB가 낮지만, TMB가 높은 하위군은 오히려 TKI 예후가 더 나빠 'TMB 낮아서'만으로 단순화할 수 없음을 보인다. [Lai 2022](../sources/lai-2022-nivolumab-versus-nivolumab-ipilimumab-egfr-mutant-nsclc.md)의 전향 무작위 시험에서는 nivolumab±ipilimumab이 무용성으로 조기 종료됐고 PD-L1·TMB 어느 것도 반응 하위군을 식별하지 못해, biomarker만으로 설명되지 않는 기전적 장벽을 시사한다. [Xu 2021](../sources/xu-2021-pd-l2-glycosylation-promotes-immune-evasion.md)은 EGFR/STAT3 신호가 PD-L2 당화·안정화를 통해 면역회피를 일으킴을 보여, oncogene 신호가 면역억제로 직접 번역되는 축을 제시한다.

**Cited**: [Offin 2019](../sources/offin-2019-tumor-mutation-burden-egfr-tki-efficacy.md), [Lai 2022](../sources/lai-2022-nivolumab-versus-nivolumab-ipilimumab-egfr-mutant-nsclc.md), [Xu 2021](../sources/xu-2021-pd-l2-glycosylation-promotes-immune-evasion.md)

### Q35. EGFR TKI failure 이후 tumor microenvironment는 어떤 방향으로 재편되는가?
**A.** EGFR TKI(osimertinib) 실패 후 TME는 면역이 빠지고 억제성 골수계가 늘어나는 'cold' 방향으로 재편된다. [Han 2023](../sources/han-2023-tumour-microenvironment-changes-osimertinib-resistance.md)은 osimertinib 내성 종양에서 침윤 T세포가 감소하고 M2형 대식세포 분극이 증가하며, 내성세포 유래 exosome이 대식세포를 M2로 유도해 능동적으로 면역을 재배선함을 보였다. 다만 사전 활성화된 PBMC는 내성세포에 대한 살해능을 유지해 이 억제가 절대적이지 않고 가역적일 수 있음을 시사한다. 즉 표적치료 내성과 immune-cold 생물학이 함께 진화하므로 유전체 시퀀싱만으로는 ICI/병용 실패 이유를 설명하기 어렵다.

**Cited**: [Han 2023](../sources/han-2023-tumour-microenvironment-changes-osimertinib-resistance.md)

### Q36. KRAS G12C inhibitor resistance는 tumor-intrinsic adaptation과 immune ecosystem change를 어떻게 동시에 만든다?
**A.** KRAS G12C 억제제 내성은 종양 내인성 적응과 면역 생태계 변화를 동시에 만든다. [Xue 2020](../sources/xue-2020-rapid-nonuniform-adaptation-kras-g12c-inhibition.md)은 약물이 GDP 결합 비활성 KRAS에 붙기 때문에 새로 합성된 KRAS와 상위 신호(EGFR·AURKA)가 escape를 좌우하며, 세포가 정지(quiescence)와 신호 회복으로 비균일하게 갈라지는 빠른 적응 이질성을 보였다. [Manabe 2022](../sources/manabe-2022-remodeling-tumor-microenvironment-kras-g12c-resistance.md)의 rapid-autopsy 연구는 임상 내성 시 KRAS 변이 분율이 줄고 MAPK가 재활성화되는 한편, 보체·응고·혈관신생 프로그램과 면역회피 같은 비세포자율적 생태계 재편이 동반됨을 보였다. 따라서 단일 target에서 시작했어도 내성 종착점은 내인성 신호 적응과 TME 재편이 맞물린 생태학적으로 복합적인 상태가 된다.

**Cited**: [Xue 2020](../sources/xue-2020-rapid-nonuniform-adaptation-kras-g12c-inhibition.md), [Manabe 2022](../sources/manabe-2022-remodeling-tumor-microenvironment-kras-g12c-resistance.md)

### Q37. STK11/LKB1 mutation은 PD-1 resistance를 어떤 immune axis로 설명하는가?
**A.** STK11/LKB1 변이는 PD-1 내성을 'non-T-cell-inflamed' 면역축으로 설명한다. [Skoulidis 2018](../sources/skoulidis-2018-stk11-lkb1-pd1-resistance-kras-lung.md)은 KRAS-mutant 폐선암에서 STK11/LKB1 변이 동반 종양이 PD-1 축 차단에 반응·생존이 현저히 나쁘고, 이를 PD-L1만으로 설명되지 않는 비T세포-염증성 미세환경(면역 관여 감소)과 연결해 종양억제 유전자 맥락이 면역기질 자체를 결정함을 보였다. 후속 [Skoulidis 2024](../sources/skoulidis-2024-ctla4-abrogates-keap1-stk11-resistance.md)는 이 표현형을 억제성 골수계 우세와 CD8 고갈(상대적 CD4 effector 보존)로 더 구체화하고, CTLA-4 병용이 CD4 effector 동원과 골수계를 iNOS+ 살종양 표현형으로 재프로그래밍해 내성을 일부 우회함을 제시한다.

**Cited**: [Skoulidis 2018](../sources/skoulidis-2018-stk11-lkb1-pd1-resistance-kras-lung.md), [Skoulidis 2024](../sources/skoulidis-2024-ctla4-abrogates-keap1-stk11-resistance.md)

### Q38. KEAP1/NFE2L2 축은 면역억제/대사 재편과 어떻게 연결되는가?
**A.** KEAP1/NFE2L2 축은 NRF2 항산화 경로 과활성화를 매개로 면역억제와 대사 재편에 연결된다. [Zavitsanou 2023](../sources/zavitsanou-2023-keap1-mutation-lung-adenocarcinoma-promotes.md)은 KEAP1 변이 폐선암에서 NRF2 hyperactivation이 수지상세포·T세포 반응을 약화시켜 immunotherapy 내성을 일으키며, glutaminase 억제를 checkpoint 차단과 병용하면 면역억제가 역전됨을 보여 대사(글루타민) 의존성과 면역회피가 맞물려 있음을 입증한다. [Skoulidis 2024](../sources/skoulidis-2024-ctla4-abrogates-keap1-stk11-resistance.md)는 KEAP1(및 STK11) 변이를 억제성 골수계 우세·CD8 고갈의 불리한 미세환경과 연결하고(예: PCP 코호트 KEAP1 변이 OS 7.6 vs WT 16.6개월), CTLA-4 병용이 이 골수계 병목을 재프로그래밍해 이득을 회복함을 제시한다.

**Cited**: [Zavitsanou 2023](../sources/zavitsanou-2023-keap1-mutation-lung-adenocarcinoma-promotes.md), [Skoulidis 2024](../sources/skoulidis-2024-ctla4-abrogates-keap1-stk11-resistance.md)

### Q39. TGF-β driven immune exclusion은 어떤 tumor class에서 가장 반복적으로 관찰되는가?
**A.** TGF-β 매개 immune exclusion(CD8 T세포가 종양 실질로 못 들어가고 peritumoral stroma에 갇히는 표현형)은 fibroblast가 풍부한 stroma-rich 종양에서 반복 관찰된다. 대표적으로 [Mariathasan 2018](../sources/mariathasan-2018-tgfb-pdl1-blockade-tcell-exclusion.md)은 전이성 요로상피암에서 비반응이 fibroblast 연관 TGF-β 신호 및 immune-excluded 표현형과 강하게 연관되고, TGF-β 차단+anti-PD-L1 병용이 T세포 침투와 퇴축을 유도함을 보였다. 대장암에서도 [Henriques 2025](../sources/henriques-2025-tgf--builds-dual-immune-barrier.md)가 간전이에서 TGF-β가 CD8 동원을 막고 SPP1+ 대식세포·collagen 침착으로 이중 면역장벽을 세움을 보였고, 폐암에서는 [Matsuda 2023](../sources/matsuda-2023-tgf--microenvironment-induces-physiologically-occurring.md)이 TGF-β/hypoxia 유발 senescence·SASP가 면역억제 침윤과 ICI 불량 PFS에 연결됨을 보고했다. 즉 요로상피암·대장암 간전이·폐암 등 fibroblast/기질 주도 종양에서 가장 반복적이다.

**Cited**: [Mariathasan 2018](../sources/mariathasan-2018-tgfb-pdl1-blockade-tcell-exclusion.md), [Henriques 2025](../sources/henriques-2025-tgf--builds-dual-immune-barrier.md), [Matsuda 2023](../sources/matsuda-2023-tgf--microenvironment-induces-physiologically-occurring.md)

### Q40. CAF/myeloid barrier는 원인인가 결과인가(인과 방향을 어떻게 판단할 것인가)?
**A.** 로컬 근거는 CAF/myeloid 장벽이 단순한 결과가 아니라 능동적 원인으로 작동할 수 있음을 보여주며, 인과 방향은 '교란(perturbation) 후 면역·종양 변화 관찰'로 판단한다. [Kumar 2017](../sources/kumar-2017-cancer-associated-fibroblasts-neutralize-anti-tumor-effect.md)은 CAF가 과립구 모집 chemokine의 주요 공급원이고, CSF1R 억제가 이 CAF-종양 crosstalk를 깨뜨려 PMN-MDSC 침윤을 급증시켜 항종양 효과를 무력화함을 보였다 — CXCR2 길항제 추가로 이를 차단하면 효과가 회복되므로(개입→효과 변화) CAF/myeloid 축이 인과적 driver임을 시사한다. [Foster 2022](../sources/foster-2022-multiomic-analysis-reveals-conservation-cancer-associated.md)는 checkpoint 억제가 CAF 아집단 분포(특히 immunomodulatory CAF)를 이동시켜 종양 성장에 영향을 줌을 보여 면역치료가 CAF 상태를 바꾸는 역방향도 존재함을 시사하므로, CAF/myeloid 장벽은 양방향적이며 인과는 표적 교란 실험으로 확정해야 한다. [Elyada 2019](../sources/elyada-2019-apcafs-pancreatic-cancer.md)가 보인 apCAF처럼 CAF 상태가 가역적·상호전환적이라는 점도 단순 인과 단정에 주의를 요한다.

**Cited**: [Kumar 2017](../sources/kumar-2017-cancer-associated-fibroblasts-neutralize-anti-tumor-effect.md), [Foster 2022](../sources/foster-2022-multiomic-analysis-reveals-conservation-cancer-associated.md), [Elyada 2019](../sources/elyada-2019-apcafs-pancreatic-cancer.md)

### Q41. gut microbiota와 ICI response는 재현성이 얼마나 강하며 어떤 메커니즘이 가장 견고한가?
**A.** 로컬 리뷰들은 gut microbiota가 항종양 면역 톤과 checkpoint 반응·독성에 영향을 준다는 신호는 부정하기 어렵지만, 구체적 taxa 시그니처는 대부분 코호트-특이적이라 재현성이 약하다고 본다([Simpson 2023](../sources/simpson-2023-gut-microbiota-enhance-checkpoint-efficacy.md)). 가장 견고한 메커니즘은 미생물 조성이 개별 균주보다 'T세포 재활성화 상위의 숙주-맥락 변수'로서 전신 면역을 형성한다는 것이며, dysbiosis(항생제·식이·장벽기능 이상)는 항원제시·T세포 priming·골수계 조절을 약화시켜 면역내성의 숙주측 위험인자로 작동한다([Almonte 2026](../sources/almonte-2026-gut-dysbiosis-oncology-immunoresistance.md)). 다만 같은 인자가 반응뿐 아니라 면역관련 독성도 바꾸므로 단순 'pro-immunity 스위치'는 아니다([Simpson 2023](../sources/simpson-2023-gut-microbiota-enhance-checkpoint-efficacy.md)).

**Cited**: [Simpson 2023](../sources/simpson-2023-gut-microbiota-enhance-checkpoint-efficacy.md), [Almonte 2026](../sources/almonte-2026-gut-dysbiosis-oncology-immunoresistance.md)

### Q42. hyperprogression은 독립적 생물학인가, 측정/선택 편향인가?
**A.** 이 위키의 로컬 논문 중 hyperprogression을 독립 생물학 대 측정/선택 편향이라는 질문으로 직접 검증한 cancer proteomics 논문은 사실상 없다. 관련 언급은 B세포 림프종 PD-1 차단 리뷰에서 combination therapy·biomarker와 함께 hyperprogression을 논의 주제로 짧게 거론하는 수준에 그쳐, 독립 메커니즘인지 편향인지 판정할 근거는 제공하지 못한다([Xu-Monette 2018](../sources/xumonette-2018-pd-1-expression-clinical-pd-1-blockade.md)). 따라서 현재 로컬 근거만으로는 결론을 내릴 수 없다.

**Cited**: [Xu-Monette 2018](../sources/xumonette-2018-pd-1-expression-clinical-pd-1-blockade.md)

### Q43. immunotherapy 후 “immune editing”은 어떤 수준(클론/항원/세포상태)에서 관찰되는가?
**A.** 로컬 근거는 immune editing이 여러 수준에서 동시에 관찰됨을 보여준다. 항원/클론 수준에서는 장기생존 췌장암 환자에서 T세포 활성이 강한 종양일수록 재발 종양이 고품질 neoantigen이 적고 클론적으로 덜 이질적으로 진화해, 면역계가 항원을 실제로 편집한다는 증거가 제시된다([Uksza 2022](../sources/uksza-2022-neoantigen-quality-predicts-immunoediting-survivors.md)). 세포상태 수준에서는 흑색종 원발병소를 공간적으로 분석하면 invasion과 immunoediting이 수 mm 내에서 공존하며 종양-기질 경계에 MHC-II·IDO1·PD1-PDL1 매개 억제 niche가 형성된다([Nirmal 2022](../sources/nirmal-2022-spatial-landscape-progression-immunoediting-primary.md)). 나아가 immunoediting은 c-Myc 상향과 대사 재프로그래밍 같은 종양 내인적 상태 변화까지 유도해 면역회피를 강화한다([Tsai 2023](../sources/tsai-2023-immunoediting-instructs-tumor-metabolic-reprogramming.md)).

**Cited**: [Łuksza 2022](../sources/uksza-2022-neoantigen-quality-predicts-immunoediting-survivors.md), [Nirmal 2022](../sources/nirmal-2022-spatial-landscape-progression-immunoediting-primary.md), [Tsai 2023](../sources/tsai-2023-immunoediting-instructs-tumor-metabolic-reprogramming.md)

### Q44. tumor mutational process(APOBEC 등)가 resistance와 연결되는 경로는 무엇인가?
**A.** 로컬 프로테오게노믹스 근거에서 APOBEC 변이 과정은 면역맥락과 양면적으로 연결된다. 비흡연 폐선암에서는 환자의 44%가 APOBEC-high였고 APOBEC3 단백이 빈번히 상향되었으며, 외부 진행성 NSCLC 병용 면역치료 코호트에서 APOBEC-high가 PFS를 다소 연장하는 보조적 맥락이 관찰되어 변이부담을 통한 면역원성 증가 경로와 닿는다([Chen 2020](../sources/chen-2020-proteogenomics-non-smoking-lung-cancer-east.md)). 반대로 고악성 난소암에서는 상동재조합 결핍 등 특정 변이 과정이 지속적 immunoediting과 HLA 다양성 손실·기능부전 CD8 T세포를 동반하거나, foldback-inversion 종양은 TGFβ 상향과 면역배제를 보여, 변이 과정의 종류가 항원제시 손실과 면역내성 표현형을 결정하는 경로로 작동한다([Vázquez-García 2022](../sources/vzquezgarca-2022-ovarian-cancer-mutational-processes-drive.md)).

**Cited**: [Chen 2020](../sources/chen-2020-proteogenomics-non-smoking-lung-cancer-east.md), [Vázquez-García 2022](../sources/vzquezgarca-2022-ovarian-cancer-mutational-processes-drive.md)

### Q45. epigenetic therapy가 immune visibility를 회복한다는 주장은 어떤 조건에서 성립하는가?
**A.** 로컬 근거는 epigenetic therapy의 'immune visibility 회복' 주장이 조건부임을 분명히 한다. 단순한 전반적 DNA 탈메틸화 자체는 오히려 면역회피 시그니처와 상관하고 변이부담의 기여를 상쇄해 면역치료 내성을 키울 수 있어, 탈메틸화=가시성 회복이라는 등식은 성립하지 않는다([Jung 2019](../sources/jung-2019-dna-methylation-loss-promotes-immune.md)). 회복이 성립하는 핵심 조건은 ISG 전사를 억압하는 특정 억제축을 풀어줄 때인데, 흑색종에서 Mi-2β가 EZH2를 통해 H3K27me3로 ISG를 억제하므로 이를 표적하면 내성 종양이 ICI 감수성으로 전환되고([Li 2024](../sources/li-2024-mi-2-promotes-immune-evasion-melanoma.md)), NSD1 결손 편평세포암처럼 H3K27me3 획득으로 인터페론 반응이 꺼진 경우 EZH2 억제가 면역침윤을 회복시킨다([Li 2022](../sources/li-2022-histone-methylation-antagonism-drives-tumor.md)).

**Cited**: [Jung 2019](../sources/jung-2019-dna-methylation-loss-promotes-immune.md), [Li 2024](../sources/li-2024-mi-2-promotes-immune-evasion-melanoma.md), [Li 2022](../sources/li-2022-histone-methylation-antagonism-drives-tumor.md)

### Q46. antigen presentation 회복을 목표로 하는 치료 조합은 어떤 것들이 있는가?
**A.** 로컬 근거에 나타난 항원제시 회복 조합은 크게 두 갈래다. 첫째, MHC-I 자체를 복원해 mRNA 백신과 결합하는 전략으로, HCC에서 MHC-I 분해를 매개하는 PCSK9를 siRNA로 억제하면 항원제시 효율이 최대 6배 증가하고 종양항원 mRNA와 함께 LNP로 전달해 CD8·NK 침윤과 항종양 면역을 강화한다([Meng 2025](../sources/meng-2025-reversal-tumour-immune-evasion-enhanced.md)). 둘째, MHC-I/B2M·IFN-γ 감지가 소실된 종양을 우회하는 전략으로, cIAP1/2 antagonist로 비정규 NF-κB를 켜면 T세포 유래 lymphotoxin이 대식세포를 종양살해형으로 재프로그램하며 CD47 차단과 병용 시 효과가 증강된다([Roehle 2021](../sources/roehle-2021-ciap12-antagonism-eliminates-mhc-class.md)).

**Cited**: [Meng 2025](../sources/meng-2025-reversal-tumour-immune-evasion-enhanced.md), [Roehle 2021](../sources/roehle-2021-ciap12-antagonism-eliminates-mhc-class.md)

### Q47. interferon pathway를 강화하는 전략은 종양 성장도 함께 촉진할 수 있는가?
**A.** 로컬 근거의 무게중심은 인터페론 신호가 checkpoint 효능에 필수라는 쪽이다. 종양이 JAK1/2 소실 등으로 IFN-γ를 감지하지 못하면 변이부담이 높아도 PD-1 차단에 1차 무반응하거나 초기 반응 후 획득내성으로 escape하며([Shin 2017](../sources/shin-2017-primary-resistance-pd1-jak-mutations.md); [Zaretsky 2016](../sources/zaretsky-2016-acquired-resistance-pd1-melanoma.md)), 종양 유래 type I IFN은 ISG+ 수지상세포 상태를 유도해 CD8 T세포를 활성화하는 등 인터페론 강화는 주로 항종양적으로 작동한다([Duong 2022](../sources/duong-2022-type-i-interferon-activates-mhc.md)). 다만 같은 근거가 종양-내인적 양면성도 시사하는데, JAK 경로가 온전한 종양은 IFN-γ 자극에 PD-L1을 상향 유도하므로([Shin 2017](../sources/shin-2017-primary-resistance-pd1-jak-mutations.md)) 인터페론 강화가 적응적 면역회피(PD-L1 induction)로 이어질 수 있다.

**Cited**: [Shin 2017](../sources/shin-2017-primary-resistance-pd1-jak-mutations.md), [Zaretsky 2016](../sources/zaretsky-2016-acquired-resistance-pd1-melanoma.md), [Duong 2022](../sources/duong-2022-type-i-interferon-activates-mhc.md)

### Q48. myeloid targeting(CSF1R 등)은 왜 임상에서 자주 실패하는가?
**A.** 로컬 근거는 myeloid targeting이 단독으로는 부족하기 때문에 임상에서 자주 실패함을 시사한다. 전임상 PDAC에서 CSF1R 차단은 대식세포를 항원제시형으로 재프로그램하지만 동시에 PD-L1·CTLA4 같은 checkpoint 분자를 보상적으로 상향시켜 단독 효과가 제한되고, PD1/CTLA4 병용 시에만 강한 퇴축이 나타났다([Zhu 2014](../sources/zhu-2014-csf1r-blockade-pancreatic-cancer-models.md)). 실제 임상에서도 anti-CSF1R(emactuzumab)+atezolizumab phase 1b는 관리 가능한 안전성에도 ICB-경험 환자의 객관적 반응률이 5.6~12.5%에 그쳤고, 특히 ICB-경험군에서는 ICB-naive군보다 TAM 감소가 약했다([Gómez-Roca 2022](../sources/gomezroca-2022-anti-csf-1r-emactuzumab-combination-anti-pd-l1-atezolizumab.md)). 즉 골수계 표적은 새 의존성을 드러내는 priming 단계에 가깝다.

**Cited**: [Zhu 2014](../sources/zhu-2014-csf1r-blockade-pancreatic-cancer-models.md), [Gomez-Roca 2022](../sources/gomezroca-2022-anti-csf-1r-emactuzumab-combination-anti-pd-l1-atezolizumab.md)

### Q49. TGF-β blockade가 임상에서 실패한 사례에서 핵심 실패 원인은 무엇인가?
**A.** 로컬 근거에서 TGF-β 차단의 대표적 임상 실패는 bifunctional TGF-β trap/anti-PD-L1인 bintrafusp alfa다. PD-L1-high 진행성 NSCLC 1차 치료 phase 3에서 bintrafusp alfa는 pembrolizumab 대비 PFS·OS 우월성을 보이지 못하고 중간분석에서 조기 중단되었으며, grade 3-4 치료관련 이상반응이 42.4% 대 13.2%로 훨씬 높았다([Cho 2023](../sources/cho-2023-bintrafusp-alfa-pembrolizumab-patients-treatment-naive.md)). 핵심 실패 원인은 (1) 전임상에서 TGF-β가 T세포 배제를 푸는 1차 면역회피 기전으로 명확했음에도([Tauriello 2018](../sources/tauriello-2018-tgf-drives-immune-evasion-genetically.md); [Mariathasan 2018](../sources/mariathasan-2018-tgfb-pdl1-blockade-tcell-exclusion.md)) 인간 종양에서 단독 효능 전환으로 이어지지 못한 점, (2) TGF-β 전신 차단에 따른 독성 부담 증가로 해석된다.

**Cited**: [Cho 2023](../sources/cho-2023-bintrafusp-alfa-pembrolizumab-patients-treatment-naive.md), [Tauriello 2018](../sources/tauriello-2018-tgf-drives-immune-evasion-genetically.md), [Mariathasan 2018](../sources/mariathasan-2018-tgfb-pdl1-blockade-tcell-exclusion.md)

### Q50. immune checkpoint가 아닌 metabolic checkpoint(adenosine, tryptophan 등)는 resistance에서 어떤 비중을 갖는가?
**A.** 로컬 근거는 metabolic checkpoint가 면역내성에서 상당한 비중을 차지하며 PD-L1만으로 포착되지 않는 축임을 보여준다. tryptophan 측에서는 HCC에서 악성세포가 만든 tryptophan-enriched 대사 미세환경이 TLS 성숙을 빗나가게 해 면역치료 반응 niche 형성을 막고, tryptophan 대사 억제가 TLS를 성숙시키며 anti-PD-1과 상승작용한다([Tang 2025](../sources/tang-2025-spatial-transcriptomics-reveals-tryptophan-metabolism.md)). adenosine 측에서는 EGFR-mutant NSCLC에서 CD73 상향을 포함한 3-변수 공간 composite가 PD-L1보다 ICI 효능 예측력에서 유의하게 우월해, adenosine 경로가 반응 결정에 실질적으로 기여함을 시사한다([Zou 2026](../sources/zou-2026-understanding-immune-checkpoint-inhibitor-efficacy-through.md)). 흑색종 원발병소 공간분석에서도 억제 niche에 IDO1이 PD1-PDL1과 함께 배치된다([Nirmal 2022](../sources/nirmal-2022-spatial-landscape-progression-immunoediting-primary.md)).

**Cited**: [Tang 2025](../sources/tang-2025-spatial-transcriptomics-reveals-tryptophan-metabolism.md), [Zou 2026](../sources/zou-2026-understanding-immune-checkpoint-inhibitor-efficacy-through.md), [Nirmal 2022](../sources/nirmal-2022-spatial-landscape-progression-immunoediting-primary.md)

### Q51. hypoxia는 immune exclusion과 어떤 방식으로 연결되는가?
**A.** Hypoxia는 비정상적 종양 혈관을 통해 저산소 환경을 만들고, 이로 인해 유도된 VEGF가 항원제시·effector 분화를 억제하며 면역세포를 억제 표현형으로 편향시켜 면역회피를 조장한다([Huang 2013](../sources/huang-2013-vascular-normalization-emerging-strategy-enhance.md)). 또한 저산소성 해당과정의 산물인 lactate가 축적되면 종양이 여전히 항원성을 가져도 CD8 T·NK의 effector 기능이 약화되고 골수계·조절T 억제 프로그램이 강화되어, 유전적 병변 없이도 immune-excluded 상태가 유지된다([Harmon 2020](../sources/harmon-2020-immune-consequences-lactate-tumor-microenvironment.md)). 실제로 checkpoint 비반응 종양에서는 CD8 T세포가 종양 실질로 들어가지 못하고 주변 기질에 갇히는 immune-excluded 표현형이 관찰된다([Mariathasan 2018](../sources/mariathasan-2018-tgfb-pdl1-blockade-tcell-exclusion.md)).

**Cited**: [Huang 2013](../sources/huang-2013-vascular-normalization-emerging-strategy-enhance.md), [Harmon 2020](../sources/harmon-2020-immune-consequences-lactate-tumor-microenvironment.md), [Mariathasan 2018](../sources/mariathasan-2018-tgfb-pdl1-blockade-tcell-exclusion.md)

### Q52. vascular normalization(anti-angiogenic)과 ICI 병용은 어떤 조건에서 효과적인가?
**A.** Vascular normalization은 고용량 항혈관제로 혈관을 파괴하는 것이 아니라, 더 낮은 '정상화' 용량으로 비정상 혈관을 재구성해 저산소·VEGF 매개 면역억제를 완화할 때 면역치료와의 병용 효과가 가장 커진다([Huang 2013](../sources/huang-2013-vascular-normalization-emerging-strategy-enhance.md)). 즉 효과 조건은 혈관 정상화로 effector T세포의 종양 내 침투와 산소·관류가 개선되는 창(window)을 확보하는 것이다. 이는 면역세포가 기질에 배제된 immune-excluded 종양에서 물리적 접근성을 회복시키는 것이 반응 전환의 핵심임을 보여주는 근거와 부합한다([Mariathasan 2018](../sources/mariathasan-2018-tgfb-pdl1-blockade-tcell-exclusion.md)).

**Cited**: [Huang 2013](../sources/huang-2013-vascular-normalization-emerging-strategy-enhance.md), [Mariathasan 2018](../sources/mariathasan-2018-tgfb-pdl1-blockade-tcell-exclusion.md)

### Q53. antigen density를 올리는 전략(표적 증가)은 실제로 가능한가?
**A.** 표적 자체의 절대량을 올리기보다, 낮은 항원 밀도에서도 인식이 성립하도록 결합 친화도를 높이는 전략이 부분적으로 가능하다. p53 R175H 같은 저밀도 MANA를 표적할 때 bispecific의 scFv 친화도를 nM 수준으로 올리면 특이성을 유지하면서 살상과 종양 제어가 개선됐다([DiNapoli 2026](../sources/dinapoli-2026-bispecific-antibodies-car-t-cells.md)). 다만 이는 modality 의존적이어서, 같은 scFv를 CAR에 붙이면 오히려 친화도 상승이 T세포 활성화를 떨어뜨려 기능이 저하됐다. 더욱이 치료 압력 자체가 HER2 발현 소실·결합부 변이를 유도해 항원 밀도를 떨어뜨리므로([Chen 2026](../sources/chen-2026-trastuzumab-deruxtecan-resistance-her2-expression-binding.md)), 항원 밀도 증대는 보편적 해법이 아니라 표적·플랫폼별로 신중히 설계해야 한다.

**Cited**: [DiNapoli 2026](../sources/dinapoli-2026-bispecific-antibodies-car-t-cells.md), [Chen 2026](../sources/chen-2026-trastuzumab-deruxtecan-resistance-her2-expression-binding.md)

### Q54. bispecific/ADC에서 target heterogeneity는 어떤 threshold에서 치명적인가?
**A.** 단일 임계값보다는 표적 밀도가 면역 시냅스 형성과 살상에 필요한 수준 아래로 떨어지는 지점이 치명적이며, 이는 친화도·에피토프 위치·내재화 동역학에 따라 표적마다 달라진다([Falchi 2023](../sources/falchi-2023-bispecific-antibodies-treatment-b-cell-lymphoma.md)). ADC에서는 페이로드 감수성이 남아 있어도 HER2 발현 소실이나 결합부 변이로 표적 결합·내재화가 무너지면 전달 실패로 내성이 생기므로, 항원 밀도·에피토프 보존·내재화가 핵심 변수가 된다([Chen 2026](../sources/chen-2026-trastuzumab-deruxtecan-resistance-her2-expression-binding.md)). bispecific도 MANA처럼 항원 밀도가 본질적으로 낮으면 효능이 제한되며, 친화도 조정으로 임계 밀도를 일부 끌어내릴 수 있다([DiNapoli 2026](../sources/dinapoli-2026-bispecific-antibodies-car-t-cells.md)).

**Cited**: [Falchi 2023](../sources/falchi-2023-bispecific-antibodies-treatment-b-cell-lymphoma.md), [Chen 2026](../sources/chen-2026-trastuzumab-deruxtecan-resistance-her2-expression-binding.md), [DiNapoli 2026](../sources/dinapoli-2026-bispecific-antibodies-car-t-cells.md)

### Q55. CAR-T에서 persistence를 늘리면 toxicity와 어떤 trade-off가 생기는가?
**A.** Persistence를 높이려고 효능·지속성을 강화하면 표적 항원을 공유하는 정상 조직에 대한 on-target/off-tumor 독성과 cytokine release syndrome(CRS)·신경독성 위험이 함께 커지는 trade-off가 생긴다([Sterner 2021](../sources/sterner-2021-cart-current-limitations-potential-strategies.md)). 특히 AML처럼 표적이 정상 조혈모·전구세포와 겹치는 경우, 강한 지속성은 장기 골수억제 위험을 키워 안전한 표적 부재 문제를 악화시키므로 logic-gate·안전 스위치 같은 제어 장치가 요구된다([Zugasti 2025](../sources/zugasti-2025-cart-cancer-current-challenges-future-directions.md)). 그래서 수용체 구조 설계는 저항원 탈출을 잡으려 민감도를 올리는 방향과 정상조직 안전성을 확보하는 방향 사이의 조정 문제로 다뤄진다([Labanieh 2023](../sources/labanieh-2023-car-immune-cells-design-principles-resistance.md)).

**Cited**: [Sterner 2021](../sources/sterner-2021-cart-current-limitations-potential-strategies.md), [Zugasti 2025](../sources/zugasti-2025-cart-cancer-current-challenges-future-directions.md), [Labanieh 2023](../sources/labanieh-2023-car-immune-cells-design-principles-resistance.md)

### Q56. CAR-T/BsAb의 공통 실패 축(antigen/effector/traffic)은 무엇인가?
**A.** CAR-T 실패는 크게 CAR-T 세포 기능부전(effector), 종양 내재적 내성(antigen), 면역억제 미세환경(traffic/TME)의 세 축으로 정리되며, 이들은 독립적이기보다 상호 연결돼 있어 단일 변수 해법이 잘 듣지 않는다([Ruella 2023](../sources/ruella-2023-cart-resistance-haematological-malignancies.md)). 같은 맥락에서 항원 탈출, 불충분한 침투·trafficking, 면역억제 미세환경이 공통 장벽으로 지목된다([Sterner 2021](../sources/sterner-2021-cart-current-limitations-potential-strategies.md)). bispecific도 HLA 비의존적 T세포 재유도라는 기전을 공유하기에 CD20 같은 항원 소실, 과치료 환자의 T세포 소진, TME 인자라는 동일한 실패 축을 갖는다([Falchi 2023](../sources/falchi-2023-bispecific-antibodies-treatment-b-cell-lymphoma.md)).

**Cited**: [Ruella 2023](../sources/ruella-2023-cart-resistance-haematological-malignancies.md), [Sterner 2021](../sources/sterner-2021-cart-current-limitations-potential-strategies.md), [Falchi 2023](../sources/falchi-2023-bispecific-antibodies-treatment-b-cell-lymphoma.md)

### Q57. “effector dysfunction”을 T cell intrinsic과 extrinsic으로 나누면 어떤 분류가 되는가?
**A.** Effector dysfunction은 T세포 내재적(intrinsic) 축과 외재적(extrinsic) 축으로 나눌 수 있다. 내재적 축은 progenitor-exhausted·dysfunctional 상태로 고정되는 세포 자체의 분화 프로그램으로, PD-L1/TGFβ 신호가 stem cell-like CD8의 확장과 비소진 effector로의 교체를 막아 소진 상태를 유지시킨다([Castiglioni 2023](../sources/castiglioni-2023-combined-pd-l1tgf-blockade-allows-expansion.md)). 외재적 축은 세포 외부 환경에 의한 억제로, 종양 경계의 ECM 관련 CAF가 면역세포를 배제하고 LGALS9/TIM-3 같은 checkpoint 리간드-수용체로 소진 CD8을 조절하거나([Du 2024](../sources/du-2024-integration-pan-cancer-single-cell-spatial-transcriptomics.md)), lactate 같은 대사 산물이 effector 기능을 약화시키는 경우다([Harmon 2020](../sources/harmon-2020-immune-consequences-lactate-tumor-microenvironment.md)).

**Cited**: [Castiglioni 2023](../sources/castiglioni-2023-combined-pd-l1tgf-blockade-allows-expansion.md), [Du 2024](../sources/du-2024-integration-pan-cancer-single-cell-spatial-transcriptomics.md), [Harmon 2020](../sources/harmon-2020-immune-consequences-lactate-tumor-microenvironment.md)

### Q58. PD-1/CTLA4 외 checkpoint axis(LAG3, TIGIT 등)는 resistance를 어떻게 설명하는가?
**A.** PD-1/CTLA-4 외 LAG3·TIGIT·TIM-3 등 co-inhibitory 축은 소진 T세포가 단일 수용체가 아니라 다중 억제 수용체를 동시 발현한다는 점에서 내성을 설명한다. 범암 단일세포 분석에서 PD-1⁺TIM-3⁺CD39⁺ 같은 다중 억제 표지 소진 CD8 아형이 반복적으로 검출되며, 이것이 수렴적 내성 축으로 제시된다([Vallée 2025](../sources/valle-2025-pan-cancer-convergence-tumour-immune-microenvironment-motifs.md)). 나아가 TIM-3는 단순 표지를 넘어 종양세포에서 β-catenin/IL-1β를 통해 면역억제 γδ T를 유도하고 CD8을 줄여 미세전이의 면역회피를 능동적으로 '허가'하기도 한다([Rozalén 2025](../sources/rozaln-2025-tim3-breast-cancer-cells-license.md)). 따라서 단일 PD-1 차단 실패는 보완적 억제 축의 잔존으로 부분 설명된다.

**Cited**: [Vallée 2025](../sources/valle-2025-pan-cancer-convergence-tumour-immune-microenvironment-motifs.md), [Rozalén 2025](../sources/rozaln-2025-tim3-breast-cancer-cells-license.md)

### Q59. co-inhibitory receptors는 원인인가, 이미 실패한 면역의 결과 표지자인가?
**A.** Co-inhibitory 수용체는 원인과 결과 표지의 두 측면을 모두 가진다. 결과 표지 측면에서는, 예컨대 CLL의 PD-1⁺ T세포가 진성 소진이라기보다 pseudo-exhaustion이나 복제노화 표현형을 보이는 등 발현이 곧 기능 차단을 뜻하지 않아 단순 마커로 해석될 수 있다([Xu-Monette 2018](../sources/xumonette-2018-pd-1-expression-clinical-pd-1-blockade.md)). 그러나 원인 측면도 분명해서, PD-L1/TGFβ 신호는 T 구획을 dysfunctional 상태로 능동적으로 묶어두고 차단 시 비소진 effector로의 전환이 일어난다([Castiglioni 2023](../sources/castiglioni-2023-combined-pd-l1tgf-blockade-allows-expansion.md)). TIM-3 역시 종양세포에서 면역회피를 직접 구동하므로 결과 표지에 그치지 않는다([Rozalén 2025](../sources/rozaln-2025-tim3-breast-cancer-cells-license.md)).

**Cited**: [Xu-Monette 2018](../sources/xumonette-2018-pd-1-expression-clinical-pd-1-blockade.md), [Castiglioni 2023](../sources/castiglioni-2023-combined-pd-l1tgf-blockade-allows-expansion.md), [Rozalén 2025](../sources/rozaln-2025-tim3-breast-cancer-cells-license.md)

### Q60. “immune cold”가 단일 상태가 아니라면 가장 실용적인 세부 분류는 무엇인가?
**A.** 'Immune cold'는 단일 상태가 아니며, 가장 실용적인 세부 분류는 T세포가 종양 실질에 없는 immune-desert와 T세포가 주변 기질에 갇혀 들어가지 못하는 immune-excluded를 구분하는 것이다([Mariathasan 2018](../sources/mariathasan-2018-tgfb-pdl1-blockade-tcell-exclusion.md)). 메커니즘적으로는 9p21 결손에 동반된 IFN-epsilon 손실로 CXCL9/10 케모카인 유도가 무너져 수지상세포·CD8 모집 자체가 실패하는 chemokine-poor/IFN-cold 아형을 따로 둘 수 있다([Zhao 2025](../sources/zhao-2025-interferon-epsilon-9p21-immune-cold-tumors.md)). 공간 분석은 macrophage-T cell exclusion zone 같은 배제 구조와 반복 면역 motif로 이 세분을 뒷받침한다([Vallée 2025](../sources/valle-2025-pan-cancer-convergence-tumour-immune-microenvironment-motifs.md)).

**Cited**: [Mariathasan 2018](../sources/mariathasan-2018-tgfb-pdl1-blockade-tcell-exclusion.md), [Zhao 2025](../sources/zhao-2025-interferon-epsilon-9p21-immune-cold-tumors.md), [Vallée 2025](../sources/valle-2025-pan-cancer-convergence-tumour-immune-microenvironment-motifs.md)

### Q61. 병용요법이 실패한 경우, 실패의 원인을 어떤 축(visibility/access/effector)로 기록할 것인가?
**A.** 병용요법 실패는 cancer-immunity cycle의 어느 단계가 막혔는지로 분해해 기록하는 것이 합리적이다. [Chen 2013](../sources/chen-2013-cancer-immunity-cycle.md)은 항종양 면역을 항원 방출·제시(visibility), 트래피킹·침윤(access), 인식·살해(effector)로 이어지는 순환으로 보고, 치료 실패는 "어느 step이 깨졌는가"로 규정해야 한다고 주장한다. 이 축은 면역회피 기전 분류와도 대응되는데, [Galassi 2024](../sources/galassi-2024-hallmarks-cancer-immune-evasion.md)는 회피를 camouflage(면역 인식 회피=visibility 저하)·coercion(효과세포 방해=effector 저하)·cytoprotection(세포독성 차단)으로 나눈다. 따라서 실패 원인을 visibility/access/effector 중 어디에 귀속시킬지 paired biopsy·미세환경 지표와 함께 기록하면, [Schoenfeld 2020](../sources/schoenfeld-2020-acquired-resistance-immune-checkpoint-inhibitors.md)이 지적한 "획득내성 기전 이해 부족"을 줄이고 다음 조합 선택의 근거가 된다.

**Cited**: [Chen 2013](../sources/chen-2013-cancer-immunity-cycle.md), [Galassi 2024](../sources/galassi-2024-hallmarks-cancer-immune-evasion.md), [Schoenfeld 2020](../sources/schoenfeld-2020-acquired-resistance-immune-checkpoint-inhibitors.md)

### Q62. “visibility”를 올리는 조합(방사선/바이러스 등)은 어떤 부작용을 유발하는가?
**A.** visibility를 올리는 조합(방사선/oncolytic virus 등)은 DNA 손상·면역원성 세포사를 통해 면역 인식을 높이지만, 동시에 적응성 억제 회로를 켜는 부작용이 있다. [Oh 2024](../sources/oh-2024-tdxd-cgas-sting-gastric-cancer.md)는 DNA 손상을 일으키는 ADC(trastuzumab deruxtecan)가 cGAS-STING·제1형 인터페론 반응으로 종양 면역원성을 높이는 한편 PD-L1을 상향조절함을 보여, visibility 증가가 곧바로 체크포인트 브레이크를 유발함을 시사한다. 또한 [Groeneveldt 2020](../sources/groeneveldt-2020-immunotherapeutic-potential-tgf--inhibition-oncolytic.md)은 oncolytic virus가 immune-silent 종양의 면역원성을 끌어올리지만 TGF-β 매개 면역배제 같은 미세환경 장벽이 남아 체크포인트 병용 시 약효가 제한될 수 있다고 정리한다. 즉 visibility 증강의 대표 부작용은 보상적 PD-L1 상향과 잔존 면역배제로, 추가 차단 없이는 효과가 상쇄된다.

**Cited**: [Oh 2024](../sources/oh-2024-tdxd-cgas-sting-gastric-cancer.md), [Groeneveldt 2020](../sources/groeneveldt-2020-immunotherapeutic-potential-tgf--inhibition-oncolytic.md)

### Q63. “access”를 올리는 조합(ECM/혈관)은 어떤 바이오마커로 선택해야 하는가?
**A.** access(ECM/혈관)를 올리는 조합은 TGF-β 매개 기질과 비정상 혈관이라는 배제 표현형을 바이오마커로 선택하는 것이 근거가 있다. [Tauriello 2018](../sources/tauriello-2018-tgf-drives-immune-evasion-genetically.md)은 TGF-β로 활성화된 기질과 T세포 배제가 anti-PD-1 무반응을 예측하며, TGF-β 차단이 종양을 다시 anti-PD-1 감수성으로 만든다고 보여, "TGF-β 활성 기질 signature"가 access 조합 선택의 후보 마커임을 시사한다([Ganesh 2018](../sources/ganesh-2018-tgf--inhibition-immunotherapy-checkmate.md)도 기질 TGF-β를 면역배제 결정인자로 정리). 혈관 축에서는 [Allen 2017](../sources/allen-2017-antiangiogenic-pdl1-hev-formation.md)이 항혈관(anti-VEGFR2)+anti-PD-L1이 high endothelial venule(HEV) 형성과 림프구 유입을 유도함을 보였고, 적응성 PD-L1 상향과 LTβR 신호·HEV 형성능이 반응 종양을 가른다고 보고해 이들이 access 조합의 선택/반응 마커가 될 수 있다.

**Cited**: [Tauriello 2018](../sources/tauriello-2018-tgf-drives-immune-evasion-genetically.md), [Ganesh 2018](../sources/ganesh-2018-tgf--inhibition-immunotherapy-checkmate.md), [Allen 2017](../sources/allen-2017-antiangiogenic-pdl1-hev-formation.md)

### Q64. “effector”를 올리는 조합(IL-2/IL-15 등)은 어떤 안전성 문제가 있는가?
**A.** effector를 올리는 조합(IL-2/IL-15 등 사이토카인·세포치료)은 강한 면역 활성화에 따르는 독성과 전신 염증이 핵심 안전성 문제다. [Beck 2024](../sources/beck-2024-long-lasting-mrna-encoded-interleukin-2-restores-cd8.md)는 장기지속 mRNA-encoded IL-2가 MHC-I 결손 종양에서 IFNγ 분비 CD8 T세포와 강한 전염증성(proinflammatory) 미세환경을 복원해 효과세포 기능을 되살린다고 보여, 효과 자체가 광범위한 전신 염증 신호를 동반함을 시사한다. 세포치료 effector 축에서는 [Sterner 2021](../sources/sterner-2021-cart-current-limitations-potential-strategies.md)이 CAR-T의 주요 장벽으로 on-target off-tumor 효과와 치료 관련 독성을 명시하며, 이런 부작용들이 서로 얽혀 단일 변수 해법이 듣지 않는다고 정리한다. 따라서 effector 강화 조합은 사이토카인 유발 전신 염증과 표적 외 독성을 안전성 한계로 두고 설계해야 한다.

**Cited**: [Beck 2024](../sources/beck-2024-long-lasting-mrna-encoded-interleukin-2-restores-cd8.md), [Sterner 2021](../sources/sterner-2021-cart-current-limitations-potential-strategies.md)

### Q65. acquired resistance에서 종양이 택하는 가장 흔한 “cost-effective” 전략은 무엇인가?
**A.** acquired resistance에서 종양이 택하는 가장 흔한 "cost-effective" 전략은 인터페론 감지나 항원제시 경로를 단일·소수 변이로 무력화하는 것이다. [Zaretsky 2016](../sources/zaretsky-2016-acquired-resistance-pd1-melanoma.md)은 pembrolizumab에 초기 반응 후 진행한 흑색종에서 JAK1/JAK2 절단형 변이(+나머지 wild-type allele 소실)로 IFNγ 반응을 없애거나 B2M 절단으로 표면 MHC-I를 잃는 escape를 보고했다. 이는 광범위한 면역침윤을 모두 차단하기보다 효과세포 인식·신호의 길목 하나를 끊는 경제적 전략으로, [Schoenfeld 2020](../sources/schoenfeld-2020-acquired-resistance-immune-checkpoint-inhibitors.md)이 정리한 ICI 획득내성의 대표 패턴과 일치한다. [Galassi 2024](../sources/galassi-2024-hallmarks-cancer-immune-evasion.md)의 틀에서는 MHC-I 소실(camouflage)과 IFN 신호 차단(coercion)이 이런 저비용 회피에 해당한다.

**Cited**: [Zaretsky 2016](../sources/zaretsky-2016-acquired-resistance-pd1-melanoma.md), [Schoenfeld 2020](../sources/schoenfeld-2020-acquired-resistance-immune-checkpoint-inhibitors.md), [Galassi 2024](../sources/galassi-2024-hallmarks-cancer-immune-evasion.md)

### Q66. primary resistance에서 종양이 이미 갖고 있는 “baseline immune escape”의 대표 패턴은 무엇인가?
**A.** primary resistance에서 종양이 이미 갖고 있는 baseline immune escape의 대표 패턴은 치료 전부터 존재하는 인터페론 경로 무능과 HLA/항원제시 결손이다. [Shin 2017](../sources/shin-2017-primary-resistance-pd1-jak-mutations.md)은 종양변이부담이 높아도 JAK1/JAK2 기능소실 변이로 IFNγ에 반응하지 못하는 종양이 PD-1 차단에 1차 무반응함을 보여, "항원성은 있으나 효과 사이토카인 경로에 절연된" baseline 상태를 제시한다. 또 [McGranahan 2017](../sources/mcgranahan-2017-allele-specific-hla-loss-immune-escape.md)은 NSCLC의 40%에서 allele-specific HLA LOH가 일어나 신항원 제시 능력을 떨어뜨림을 보고했고, [Rosenthal 2019](../sources/rosenthal-2019-neoantigen-directed-immune-escape-lung-cancer.md)은 미치료 초기 폐암에서 HLA LOH·신항원 발현 소실·프로모터 과메틸화 등 다중 회피 경로가 이미 작동함을 보여 baseline escape의 패턴을 뒷받침한다.

**Cited**: [Shin 2017](../sources/shin-2017-primary-resistance-pd1-jak-mutations.md), [McGranahan 2017](../sources/mcgranahan-2017-allele-specific-hla-loss-immune-escape.md), [Rosenthal 2019](../sources/rosenthal-2019-neoantigen-directed-immune-escape-lung-cancer.md)

### Q67. single-cell/spatial이 resistance 해석을 실제로 바꿔놓은 대표 사례는 무엇인가?
**A.** single-cell/spatial이 resistance 해석을 실제로 바꿔놓은 대표 사례는 "평균값(bulk)으로는 보이지 않던 국소 immunoediting"의 가시화다. [Nirmal 2022](../sources/nirmal-2022-spatial-landscape-progression-immunoediting-primary.md)은 원발 흑색종을 high-plex imaging과 공간 전사체로 분석해, 침습부 종양-기질 경계에 IDO1·MHC-II·PD1-PDL1 접촉으로 이뤄진 억제 환경이 형성되는 한편 불과 수 mm 옆에서는 세포독성 T세포가 종양을 죽이는 퇴축 영역이 공존함을 보였다. 즉 같은 검체 안에서 invasion과 immunoediting이 millimeter 단위로 나뉘어, bulk로는 상쇄되어 사라질 신호를 드러낸다. 이는 [Rosenthal 2019](../sources/rosenthal-2019-neoantigen-directed-immune-escape-lung-cancer.md)이 다영역 분석에서 발견한 종양 내(intra-tumour) 면역침윤 이질성과도 맞물려, resistance가 단일 상태가 아니라 공간적으로 분기함을 보여준다.

**Cited**: [Nirmal 2022](../sources/nirmal-2022-spatial-landscape-progression-immunoediting-primary.md), [Rosenthal 2019](../sources/rosenthal-2019-neoantigen-directed-immune-escape-lung-cancer.md)

### Q68. bulk 기반 signature는 어떤 조건에서 충분하고, 어떤 조건에서 반드시 single-cell/spatial이 필요한가?
**A.** bulk 기반 signature는 종양 간 평균적 면역 톤이나 한 영역의 우세 기전을 잡는 데는 충분하지만, 종양 내 공간 이질성이 결과를 가르는 경우에는 single-cell/spatial이 필요하다. [Rosenthal 2019](../sources/rosenthal-2019-neoantigen-directed-immune-escape-lung-cancer.md)은 88개 폐암의 258개 영역을 bulk RNA-seq로 분석해 면역침윤이 종양 간뿐 아니라 종양 내에서도 크게 다르고 영역마다 다른 회피 기전(HLA LOH, 신항원 소실 등)이 우세함을 보여, 다영역 표본이 없으면 평균 신호가 오도될 수 있음을 시사한다. [Nirmal 2022](../sources/nirmal-2022-spatial-landscape-progression-immunoediting-primary.md)은 한발 더 나아가, 억제 환경과 종양 퇴축이 수 mm 안에서 공존하는 구조는 세포 단위 공간 해상도로만 분해된다고 보여준다. 따라서 비교적 균질하고 우세 기전이 분명한 종양에선 bulk가 실용적이고, 경계부 미세구조·국소 effector 활성·드문 회피 클론이 의사결정에 중요한 종양에선 single-cell/spatial이 요구된다.

**Cited**: [Rosenthal 2019](../sources/rosenthal-2019-neoantigen-directed-immune-escape-lung-cancer.md), [Nirmal 2022](../sources/nirmal-2022-spatial-landscape-progression-immunoediting-primary.md)

### Q69. 같은 암종에서도 치료 라인/이전 치료가 면역 상태를 얼마나 바꾸는가?
**A.** 같은 암종이라도 이전 치료(치료 라인)는 면역 상태를 상당히 바꾼다. [Han 2023](../sources/han-2023-tumour-microenvironment-changes-osimertinib-resistance.md)은 osimertinib 내성 NSCLC가 단순한 변이 변화가 아니라 침윤 T세포 감소와 M2형 대식세포 증가로 면역학적으로 재편됨을 보였고, 내성세포 유래 exosome이 능동적으로 M2 분극을 유도해 cold 표현형을 만든다고 보고했다. 이는 1차 표적치료 경험 자체가 후속 면역치료의 출발 면역 상태를 바꾼다는 증거다. 다만 [Han 2023](../sources/han-2023-tumour-microenvironment-changes-osimertinib-resistance.md)은 사전 활성화된 PBMC가 여전히 내성세포를 죽일 수 있어 억제가 절대적이지 않음도 보였고, [Onkar 2023](../sources/onkar-2023-great-immune-escape-understanding-divergent.md)은 같은 유방암 안에서도 아형마다 면역반응이 크게 갈린다고 정리해 "같은 암종"이라는 묶음 안의 면역 상태 변동성을 강조한다.

**Cited**: [Han 2023](../sources/han-2023-tumour-microenvironment-changes-osimertinib-resistance.md), [Onkar 2023](../sources/onkar-2023-great-immune-escape-understanding-divergent.md)

### Q70. steroids/antibiotics 같은 동반 약물이 ICI 결과에 미치는 영향은 어느 정도까지 조정되었는가?
**A.** steroids/antibiotics 같은 동반 약물의 ICI 영향은 로컬 근거상 "기전적으로 인정되지만 표준화·완전 조정에는 이르지 못한" 단계다. [Simpson 2023](../sources/simpson-2023-gut-microbiota-enhance-checkpoint-efficacy.md)은 장내 미생물 조성이 항종양 면역 톤·체크포인트 반응·면역관련 독성에 영향을 주며 항생제 회피가 내성 예방 전략의 하나라고 보면서도, 많은 signature가 코호트 특이적이어서 번역 병목이 크다고 명시한다. [Almonte 2026](../sources/almonte-2026-gut-dysbiosis-oncology-immunoresistance.md)은 항생제·식이·염증으로 인한 dysbiosis를 면역내성의 숙주 수준 위험인자로 규정하지만, 이것이 시스템 수준 문제라 표준화하기 어렵다고 지적한다. 즉 동반 약물 효과는 보정 대상으로 인식되고 일부는 통제 가능하나, 두 리뷰 모두 정착된 개입 지침이 아닌 프레임워크 수준으로 읽어야 한다고 본다.

**Cited**: [Simpson 2023](../sources/simpson-2023-gut-microbiota-enhance-checkpoint-efficacy.md), [Almonte 2026](../sources/almonte-2026-gut-dysbiosis-oncology-immunoresistance.md)

### Q71. tumor mutational burden가 높지만 ICI에 실패하는 대표 설명은 무엇인가?
**A.** 높은 TMB가 곧 ICI 반응을 보장하지 않는다는 점은 로컬 근거에서 분명하다. 전이성 요로상피암 atezolizumab 코호트에서 반응은 CD8 effector·neoantigen/TMB와 상관했지만, 비반응은 fibroblast 유래 TGF-beta 신호와 강하게 연관되어 CD8 T세포가 종양 실질로 들어가지 못하고 주변 stroma에 갇히는 immune-excluded 표현형으로 설명되었다 ([Mariathasan 2018](../sources/mariathasan-2018-tgfb-pdl1-blockade-tcell-exclusion.md)). 또한 hypermutated·면역침윤 종양조차 B2M·HLA 양대립유전자 소실 같은 antigen-presentation 결손으로 escape할 수 있고 ([Grasso 2018](../sources/grasso-2018-genetic-mechanisms-immune-evasion-colorectal-cancer.md)), 초기 반응 후 JAK1/2 또는 B2M 절단변이로 내성이 진화하기도 한다 ([Zaretsky 2016](../sources/zaretsky-2016-acquired-resistance-pd1-melanoma.md)). 즉 높은 TMB가 있어도 stromal 배제나 항원제시 결손이 동반되면 실패한다.

**Cited**: [Mariathasan 2018](../sources/mariathasan-2018-tgfb-pdl1-blockade-tcell-exclusion.md), [Grasso 2018](../sources/grasso-2018-genetic-mechanisms-immune-evasion-colorectal-cancer.md), [Zaretsky 2016](../sources/zaretsky-2016-acquired-resistance-pd1-melanoma.md)

### Q72. PD-L1이 높지만 실패하는 대표 설명은 무엇인가?
**A.** PD-L1이 높아도 실패하는 대표 설명은 (1) T세포가 종양으로 진입하지 못하는 immune-excluded 상태와 (2) 항원제시/IFN 신호 결손이다. 전이성 요로상피암에서 PD-L1 발현·TMB가 있어도 fibroblast 유래 TGF-beta 신호가 강하면 비반응으로 이어졌고, 이는 checkpoint 발현 자체보다 stroma 구조 문제로 재해석된다 ([Mariathasan 2018](../sources/mariathasan-2018-tgfb-pdl1-blockade-tcell-exclusion.md)). B세포 림프종 리뷰는 9p24.1 변이로 PD-L1이 높은 종양조차 질환별 ORR이 크게 다르고 hyperprogression·내성 사례가 있음을 정리한다 ([Xu-Monette 2018](../sources/xumonette-2018-pd-1-expression-clinical-pd-1-blockade.md)). 나아가 PD-1 차단에 처음엔 반응해도 B2M 소실로 표면 MHC class I이 사라지면 CD8 인식이 무력화되어 실패한다 ([Zaretsky 2016](../sources/zaretsky-2016-acquired-resistance-pd1-melanoma.md)).

**Cited**: [Mariathasan 2018](../sources/mariathasan-2018-tgfb-pdl1-blockade-tcell-exclusion.md), [Xu-Monette 2018](../sources/xumonette-2018-pd-1-expression-clinical-pd-1-blockade.md), [Zaretsky 2016](../sources/zaretsky-2016-acquired-resistance-pd1-melanoma.md)

### Q73. MSI-H인데 실패하는 경우의 대표 메커니즘은 무엇인가?
**A.** MSI-H인데 실패하는 대표 메커니즘은 항원제시 기구의 hard genetic lesion이다. 1,211예 대장암(MSI-H 179예) 분석에서 MSI-H 종양은 copy-number loss와 copy-neutral LOH를 통한 B2M·HLA 양대립유전자 소실 같은 immune-editing 병변을 자주 보였고, 이것이 MSI-H가 checkpoint에 반응하면서도 면역회피로 진화하는 이유로 제시된다 ([Grasso 2018](../sources/grasso-2018-genetic-mechanisms-immune-evasion-colorectal-cancer.md)). 또 MSI-H 위암 안에서도 면역억제 특성이 풍부하고 예후가 나쁜 아형(MSI-H1)이 존재해, MSI-H가 균일하게 강한 반응성을 의미하지 않는다 ([Yang 2021](../sources/yang-2021-msih-gastric-cancer-heterogeneity-worse-survival.md)). MMR 결손이 만드는 dynamic neoantigen이 면역감시를 유도한다는 점을 고려하면 ([Germano 2017](../sources/germano-2017-inactivation-dna-repair-triggers-neoantigen.md)), 항원제시 소실은 이 감시를 무력화하는 핵심 탈출구다.

**Cited**: [Grasso 2018](../sources/grasso-2018-genetic-mechanisms-immune-evasion-colorectal-cancer.md), [Yang 2021](../sources/yang-2021-msih-gastric-cancer-heterogeneity-worse-survival.md), [Germano 2017](../sources/germano-2017-inactivation-dna-repair-triggers-neoantigen.md)

### Q74. organ-specific immune context(간/뇌 등)가 resistance를 결정하는 사례는 무엇인가?
**A.** organ-specific immune context가 내성을 결정하는 대표 사례는 간 전이다. 대장암 quadruple-mutant 마우스에서 간 전이 병변은 TGF-beta로 활성화된 stroma와 T세포 배제를 보여 PD-1/PD-L1 단독 차단에는 제한적으로만 반응했고, TGF-beta 차단을 더했을 때 비로소 anti-PD-1/PD-L1에 민감해졌다 ([Tauriello 2018](../sources/tauriello-2018-tgf-drives-immune-evasion-genetically.md)). NSCLC IMpower150 탐색 분석에서도 간·뇌 전이 하위군에서 bevacizumab을 포함한 ABCP가 BCP 대비 이점 신호를 보여 장기별 맥락이 면역화학요법 효과를 좌우함을 시사한다 ([Nogami 2022](../sources/nogami-2022-impower150-egfr-liver-brain-subgroups.md)). 췌장암 공간전사체 연구는 원발과 전이 부위에서 면역억제 ecotype 분포가 서로 다르게 enrich됨을 보여 국소 환경 적응을 뒷받침한다 ([Khaliq 2024](../sources/khaliq-2024-spatial-transcriptomic-analysis-primary-metastatic.md)).

**Cited**: [Tauriello 2018](../sources/tauriello-2018-tgf-drives-immune-evasion-genetically.md), [Nogami 2022](../sources/nogami-2022-impower150-egfr-liver-brain-subgroups.md), [Khaliq 2024](../sources/khaliq-2024-spatial-transcriptomic-analysis-primary-metastatic.md)

### Q75. metastasis site별로 immune escape가 다르다는 근거는 얼마나 강한가?
**A.** 전이 부위별로 immune escape가 다르다는 근거는 로컬 자료상 spatial 수준에서 비교적 일관되지만 임상 결과와의 직접 연결은 아직 정황적이다. 췌장암 matched 원발·전이 공간전사체에서 fibrotic·대사·면역억제 ecotype이 부위 간에 서로 다른 enrichment를 보여 국소 환경 적응이 관찰되었다 ([Khaliq 2024](../sources/khaliq-2024-spatial-transcriptomic-analysis-primary-metastatic.md)). 흑색종 공간 분석은 전구·in situ·침습 단계 축을 따라 면역억제와 면역편집이 변하며 침습부 경계에 국한된 억제 환경이 형성됨을 보여, escape가 위치 의존적임을 시사한다 ([Nirmal 2022](../sources/nirmal-2022-spatial-landscape-progression-immunoediting-primary.md)). 또 간 전이에서 TGF-beta 매개 T세포 배제가 두드러진다는 결과는 부위 특이적 회피를 뒷받침하나 ([Tauriello 2018](../sources/tauriello-2018-tgf-drives-immune-evasion-genetically.md)), 이들은 대체로 단일 코호트·전임상 기반이라 부위별 차이의 일반화는 추가 검증이 필요하다.

**Cited**: [Khaliq 2024](../sources/khaliq-2024-spatial-transcriptomic-analysis-primary-metastatic.md), [Nirmal 2022](../sources/nirmal-2022-spatial-landscape-progression-immunoediting-primary.md), [Tauriello 2018](../sources/tauriello-2018-tgf-drives-immune-evasion-genetically.md)

### Q76. circulating biomarkers(ctDNA, proteomics)은 resistance 조기 탐지에 쓸 수 있는가?
**A.** 순환 바이오마커가 조기 탐지에 쓰일 수 있다는 정황 근거는 있다. mCRPC에서 순환 PMN-MDSC 비율이 질병 진행에 따라 상승하고 높은 군이 생존이 유의하게 짧아(중앙 159일 대 768일) 독립 예후인자로 나타났다 ([Kobayashi 2024](../sources/kobayashi-2024-increased-circulating-polymorphonuclear-myeloid-derived-suppressor.md)). nivolumab+ipilimumab 전립선암 시험에서도 baseline 순환 IL-6·IL-7·IL-17과 혈청 sPD-L1 같은 단백 지표가 면역요법 결과와 연관되어 혈액 기반 stratification 가능성을 보였다 ([Shenderov 2021](../sources/shenderov-2021-nivolumab-plus-ipilimumab-without-enzalutamide.md)). 전이성 요로상피암에서 혈중 RNA와 ctDNA를 통합해 면역요법 반응을 반영했다는 보고도 있으나 ([van 2025](../sources/van-2025-multimodal-integration-blood-rna-ctdna.md)), 로컬 본문이 abstract 단계라 세부는 제한적이며 전향적 검증이 필요하다.

**Cited**: [Kobayashi 2024](../sources/kobayashi-2024-increased-circulating-polymorphonuclear-myeloid-derived-suppressor.md), [Shenderov 2021](../sources/shenderov-2021-nivolumab-plus-ipilimumab-without-enzalutamide.md), [van 2025](../sources/van-2025-multimodal-integration-blood-rna-ctdna.md)

### Q77. neoantigen 변화 추적을 resistance monitoring에 쓰려면 무엇이 필요할까?
**A.** neoantigen 변화 추적을 monitoring에 쓰려면 단순 개수가 아니라 'quality'와 clonal 구조를 정량할 framework가 필요하다. 췌장암 장기 생존자 연구는 non-selfness(기지 항원과의 유사성)와 selfness(야생형 대비 MHC 결합/T세포 활성화에 필요한 항원 거리)로 neoantigen 면역원성을 추정하고, 면역압이 고품질 neoantigen을 깎아내는 immunoediting을 시계열로 예측했다 ([Łuksza 2022](../sources/uksza-2022-neoantigen-quality-predicts-immunoediting-survivors.md)). 대장암 checkpoint 시뮬레이션에서는 '강한 clonal neoantigen 1개'의 유무와 반응 동역학에 기여하는 모든 neoantigen 중 minimal neoantigen quality가 durable response의 가장 강력한 예측인자였다 ([Sholokhova 2026](../sources/sholokhova-2026-neoantigen-evolution-response-checkpoint-inhibitor-immunotherapy.md)). 또 MMR 결손이 만드는 dynamic neoantigen renewal을 고려하면 ([Germano 2017](../sources/germano-2017-inactivation-dna-repair-triggers-neoantigen.md)), 반복 시료에서 clonal·고품질 neoantigen의 소실을 추적하는 설계가 핵심이다.

**Cited**: [Łuksza 2022](../sources/uksza-2022-neoantigen-quality-predicts-immunoediting-survivors.md), [Sholokhova 2026](../sources/sholokhova-2026-neoantigen-evolution-response-checkpoint-inhibitor-immunotherapy.md), [Germano 2017](../sources/germano-2017-inactivation-dna-repair-triggers-neoantigen.md)

### Q78. antigen presentation loss를 치료 중 모니터링할 수 있는 방법은 무엇인가?
**A.** antigen presentation loss는 치료 중 표면 MHC class I과 그 조절경로를 추적해 모니터링할 수 있다. 흑색종 paired biopsy에서 PD-1 차단 후 B2M 절단변이로 표면 MHC class I이 소실된 사례가 직접 확인되어, 반복 생검의 B2M/MHC-I 상태가 획득 내성 지표가 됨을 보여준다 ([Zaretsky 2016](../sources/zaretsky-2016-acquired-resistance-pd1-melanoma.md)). 간세포암에서는 환자 종양의 MHC-I 하향조절이 예후·면역요법 반응 저하와 상관했고 여러 조절자 중 PCSK9이 유의하게 연관되어, MHC-I과 그 조절자(PCSK9)를 모니터링·표적 후보로 제시한다 ([Meng 2025](../sources/meng-2025-reversal-tumour-immune-evasion-enhanced.md)). 대장암에서도 copy-number/LOH 기반 B2M·HLA 소실이 측정 가능한 lesion으로 보고되어 유전체 수준 추적이 가능하다 ([Grasso 2018](../sources/grasso-2018-genetic-mechanisms-immune-evasion-colorectal-cancer.md)).

**Cited**: [Zaretsky 2016](../sources/zaretsky-2016-acquired-resistance-pd1-melanoma.md), [Meng 2025](../sources/meng-2025-reversal-tumour-immune-evasion-enhanced.md), [Grasso 2018](../sources/grasso-2018-genetic-mechanisms-immune-evasion-colorectal-cancer.md)

### Q79. immune-related adverse event(irAE)와 efficacy는 항상 같이 가는가?
**A.** 로컬 근거에 따르면 irAE와 efficacy가 항상 같이 가지는 않는다. AR-V7 양성 전립선암 nivolumab+ipilimumab 시험에서는 grade 3/4 부작용이 두 코호트에서 각각 46%·53%로 상당했으나 PSA 반응은 13%/0%, ORR은 25%/0%로 효능은 미미해, 높은 독성이 곧 효능을 의미하지 않음을 보여준다 ([Shenderov 2021](../sources/shenderov-2021-nivolumab-plus-ipilimumab-without-enzalutamide.md)). 다만 이 시험은 baseline 순환 cytokine 같은 면역활성 지표가 결과와 연관됨을 시사해, 독성-효능 관계가 단순 비례가 아니라 면역 맥락에 좌우됨을 암시한다. B세포 림프종 PD-1 차단 리뷰도 효능과 별개로 치료관련 부작용·hyperprogression을 함께 다뤄 둘이 분리될 수 있음을 정리한다 ([Xu-Monette 2018](../sources/xumonette-2018-pd-1-expression-clinical-pd-1-blockade.md)).

**Cited**: [Shenderov 2021](../sources/shenderov-2021-nivolumab-plus-ipilimumab-without-enzalutamide.md), [Xu-Monette 2018](../sources/xumonette-2018-pd-1-expression-clinical-pd-1-blockade.md)

### Q80. toxicity를 줄이면서 efficacy를 유지하는 공학적/임상적 전략은 무엇인가?
**A.** 독성을 줄이면서 효능을 유지하는 전략은 로컬 자료상 주로 단백질·세포 공학과 표적 설계에서 제시된다. CD20xCD3 이중특이항체 리뷰는 knobs-into-holes 기반 사슬 페어링, CD20 affinity tuning, epitope geometry 조정 같은 공학 선택과 CRS/ICANS 완화 전략을 통해 효능을 지키며 T세포 과활성 독성을 관리하는 방향을 정리한다 ([Falchi 2023](../sources/falchi-2023-bispecific-antibodies-treatment-b-cell-lymphoma.md)). CAR-T 리뷰는 on-target off-tumor 독성과 antigen escape를 별개 실패 모드로 보고, dual/tandem targeting·regional delivery·미세환경 조절·반복적 수용체 공학을 각 모드에 맞춘 대응으로 제시한다 ([Sterner 2021](../sources/sterner-2021-cart-current-limitations-potential-strategies.md)). 임상적으로는 baseline 순환 cytokine·sPD-L1 같은 지표로 환자를 선별해 효능 가능성이 낮은 군의 불필요한 독성 노출을 줄이는 stratification도 시사된다 ([Shenderov 2021](../sources/shenderov-2021-nivolumab-plus-ipilimumab-without-enzalutamide.md)).

**Cited**: [Falchi 2023](../sources/falchi-2023-bispecific-antibodies-treatment-b-cell-lymphoma.md), [Sterner 2021](../sources/sterner-2021-cart-current-limitations-potential-strategies.md), [Shenderov 2021](../sources/shenderov-2021-nivolumab-plus-ipilimumab-without-enzalutamide.md)

### Q81. resistance를 줄이기 위해 치료 순서를 바꾸는 전략(priming→ICI)은 어떤 근거가 있는가?
**A.** 치료 순서·조합으로 면역 병목을 먼저 푸는 priming 전략은 로컬 근거가 비교적 탄탄하다. [Skoulidis 2024](../sources/skoulidis-2024-ctla4-abrogates-keap1-stk11-resistance.md)는 PD-(L)1 단독에 잘 안 듣는 KEAP1/STK11 변이 NSCLC에서 CTLA-4 병용(POSEIDON의 durvalumab+tremelimumab)이 억제성 골수세포 우위와 CD8 고갈로 막힌 미세환경을 재편해 CD4 effector와 iNOS+ 종양살해 골수세포를 동원함으로써 내성을 부분적으로 우회한다고 보고했고, 이 임상 신호는 [Johnson 2023](../sources/johnson-2023-poseidon-first-line-metastatic-nsclc.md)의 1차 dual-ICB+화학요법 결과와 일치한다. 또 [Castiglioni 2023](../sources/castiglioni-2023-combined-pd-l1tgf-blockade-allows-expansion.md)은 immune-excluded 종양에서 TGFβ를 함께 차단해야 stem cell-like CD8 T세포가 팽창·분화하며 고갈 세포를 비고갈 effector로 교체할 수 있음을 보여, ICI 단독보다 '장벽 해제 후 활성화'라는 순차/조합 논리를 뒷받침한다.

**Cited**: [Skoulidis 2024](../sources/skoulidis-2024-ctla4-abrogates-keap1-stk11-resistance.md), [Johnson 2023](../sources/johnson-2023-poseidon-first-line-metastatic-nsclc.md), [Castiglioni 2023](../sources/castiglioni-2023-combined-pd-l1tgf-blockade-allows-expansion.md)

### Q82. “priming failure” vs “exhaustion”을 구분하는 최소 지표는 무엇인가?
**A.** 로컬 근거로는 '얼마나 stem-like/progenitor 풀이 남아있고 그것이 비고갈 effector로 교체되는가'가 두 상태를 가르는 핵심 지표로 제시된다. [Castiglioni 2023](../sources/castiglioni-2023-combined-pd-l1tgf-blockade-allows-expansion.md)은 TGFβ와 PD-L1이 stem cell-like CD8(TSCL) 팽창과 progenitor-exhausted·기능부전 CD8의 비고갈 IFNγ-high effector로의 교체를 억제한다고 보아, TSCL 보존 여부·IFNγ-high effector 축적·고갈 표현형 잔존을 측정 가능한 분기점으로 본다. 다만 이 corpus에는 'priming failure(항원 제시·T세포 동원 자체의 실패)'와 'exhaustion(동원된 T세포의 점진적 기능소실)'을 직접 대비해 정의한 전용 논문은 드물며, [Sterner 2021](../sources/sterner-2021-cart-current-limitations-potential-strategies.md) 같은 리뷰는 trafficking·침투 실패와 T세포 기능부전을 별개의 실패 모드로 구분해 다룬다.

**Cited**: [Castiglioni 2023](../sources/castiglioni-2023-combined-pd-l1tgf-blockade-allows-expansion.md), [Sterner 2021](../sources/sterner-2021-cart-current-limitations-potential-strategies.md)

### Q83. tumor antigenicity를 높이는 전략(예: epigenetic reactivation)은 언제 도움이 되는가?
**A.** 후성유전학적 reactivation은 종양이 MHC-I/항원제시를 '돌연변이 없이 가역적으로 침묵'시켜 immune-cold가 된 경우에 가장 유용하다. [Burr 2019](../sources/burr-2019-evolutionarily-conserved-function-polycomb-silences.md)는 PRC2/H3K27me3가 MHC-I 항원처리 경로를 bivalent 크로마틴으로 침묵시켜 기저 발현과 사이토카인 유도 상향을 막으므로 PRC2(EZH2) 억제가 항원성을 되살릴 수 있음을 보였고, [Li 2022](../sources/li-2022-histone-methylation-antagonism-drives-tumor.md)는 NSD1 결손 SCC에서 H3K36me2 소실·H3K27me3 획득으로 면역 배제가 생기지만 EZH2 억제가 면역 침윤을 회복시킴을 보여 같은 논리를 강화한다. 반면 [Jung 2019](../sources/jung-2019-dna-methylation-loss-promotes-immune.md)는 전역적 DNA 메틸화 소실이 면역회피 시그니처와 연관됨을 보여 후성유전 개입은 침묵 기전(억제성 vs 탈메틸화)을 확인한 맥락에서 골라야 함을 시사한다.

**Cited**: [Burr 2019](../sources/burr-2019-evolutionarily-conserved-function-polycomb-silences.md), [Li 2022](../sources/li-2022-histone-methylation-antagonism-drives-tumor.md), [Jung 2019](../sources/jung-2019-dna-methylation-loss-promotes-immune.md)

### Q84. STING agonist는 왜 사람에서 어려운가(전달/독성/효과)?
**A.** 로컬 corpus에 STING agonist 자체의 임상 실패를 직접 다룬 논문은 드물지만, 관련 기전 논문들은 왜 종양 내 cGAS-STING 활성화가 까다로운지를 간접적으로 보여준다. [Pantelidou 2019](../sources/pantelidou-2019-parp-inhibitor-efficacy-depends-cd8.md)는 효과적인 CD8 동원이 '종양세포 내부'의 cGAS/STING/TBK1/IRF3 활성화와 수지상세포의 paracrine 활성화에 의존하며 종양세포 STING을 없애면 T세포 침윤이 사라진다고 보여, 효과를 내려면 적절한 세포·구획에서 경로가 켜져야 함을 시사한다. [Oh 2024](../sources/oh-2024-tdxd-cgas-sting-gastric-cancer.md)는 직접 STING agonist 대신 T-DXd가 DNA 손상을 통해 종양세포에서 cGAS-STING·I형 인터페론을 유도하는 우회 전달 전략을 보여, 강한 STING 활성화를 '국소적으로' 일으키는 것이 핵심 난제임을 보여준다.

**Cited**: [Pantelidou 2019](../sources/pantelidou-2019-parp-inhibitor-efficacy-depends-cd8.md), [Oh 2024](../sources/oh-2024-tdxd-cgas-sting-gastric-cancer.md)

### Q85. oncolytic virus는 어떤 조건에서 작동하고 왜 자주 실패하는가?
**A.** Oncolytic virus는 면역-침묵/배제형 고형종양을 immune-hot으로 전환할 때 작동하지만, 숙주의 항바이러스 방어가 바이러스 복제와 항종양 면역을 동시에 막아 자주 실패한다. [Hong 2023](../sources/hong-2023-pkr-induces-tgf--limits-oncolytic.md)은 PKR이 oncolytic HSV 복제를 가장 강하게 제한하는 장벽이자, 동시에 TGFβ 면역억제 신호를 유도해 항원특이 CD8 반응을 누르는 '이중 장애물'임을 보였고, PKR을 표적한 oHSV가 복제·면역을 모두 개선해 생존을 늘렸다. [Groeneveldt 2020](../sources/groeneveldt-2020-immunotherapeutic-potential-tgf--inhibition-oncolytic.md)도 TGFβ 유도 면역 배제와 면역원성 부족이 OV 효과를 제한하므로 TGFβ 억제·체크포인트 차단과 병용해야 효능이 커진다고 정리한다. 즉 OV는 적절한 면역원성·낮은 항바이러스 억제·병용 면역조절이 갖춰질 때 작동한다.

**Cited**: [Hong 2023](../sources/hong-2023-pkr-induces-tgf--limits-oncolytic.md), [Groeneveldt 2020](../sources/groeneveldt-2020-immunotherapeutic-potential-tgf--inhibition-oncolytic.md)

### Q86. IL-12 같은 강한 cytokine 전략이 다시 부상하려면 무엇이 필요할까?
**A.** IL-12 같은 강한 사이토카인 전략이 다시 부상하려면 전신 독성을 피하는 '국소·표적 전달'과 항원소실 종양까지 닿는 작용기전이 핵심으로 보인다. [Chmielewski 2011](../sources/chmielewski-2011-il-12-release-engineered-t-cells.md)은 CAR 결합 시에만 종양 병변에서 IL-12를 유도방출하는 T세포가, 대식세포·TNF-α 의존 선천면역을 동원해 항원소실(antigen-loss) 종양세포까지 제거하면서 전신 독성을 줄였음을 보여 이 방향의 원형을 제시한다. [Chmielewski 2017](../sources/chmielewski-2017-car-t-cells-releasing-il-18.md)의 IL-18 분비 CAR-T(TRUCK)는 T-bet-high·FoxO1-low effector로 분극되어 M2 대식세포·Treg를 줄이고 미세환경을 재편하며, [Beck 2024](../sources/beck-2024-long-lasting-mrna-encoded-interleukin-2-restores-cd8.md)의 장기지속 mRNA-IL-2는 MHC-I 결핍 종양에서도 macrophage 교차제시 기반 CD8 반응을 되살려, 사이토카인을 송달·표적화하는 플랫폼(공학 세포·mRNA)이 부활의 전제임을 시사한다.

**Cited**: [Chmielewski 2011](../sources/chmielewski-2011-il-12-release-engineered-t-cells.md), [Chmielewski 2017](../sources/chmielewski-2017-car-t-cells-releasing-il-18.md), [Beck 2024](../sources/beck-2024-long-lasting-mrna-encoded-interleukin-2-restores-cd8.md)

### Q87. tumor-intrinsic oncogenic signaling이 면역회피를 구동하는 대표 축은 무엇인가(WNT, MAPK 등)?
**A.** 로컬 근거에서 종양세포 내재 oncogenic signaling이 면역회피를 구동하는 대표 축은 WNT/β-catenin과 PTEN-loss/PI3K-STAT3 축이다. [Grasso 2018](../sources/grasso-2018-genetic-mechanisms-immune-evasion-colorectal-cancer.md)은 대장암에서 WNT/β-catenin 경로 변이가 흔하고 활성화된 WNT 신호가 T세포 침윤 감소와 상관함을 보였으며, [Malladi 2016](../sources/malladi-2016-metastatic-latency-immune-evasion-through.md)은 잠복 전이세포가 autocrine WNT 억제(DKK1)로 느린 분열 상태에 들어가 NK 리간드를 낮춰 선천면역을 회피함을 보여 WNT 축의 양면성을 보여준다. [Bergholz 2023](../sources/bergholz-2023-pi3k-controls-immune-evasion-pten-deficient.md)은 PTEN 결손 유방암에서 PI3Kβ가 STAT3를 통해 면역회피를 제어하며 PI3Kβ 억제가 면역자극 분자를 늘려 항종양 면역을 회복시킴을 보여, oncogene-driven 면역회피가 종종 가역적·표적가능한 축임을 시사한다(MAPK 등 다른 축도 corpus에 존재).

**Cited**: [Grasso 2018](../sources/grasso-2018-genetic-mechanisms-immune-evasion-colorectal-cancer.md), [Malladi 2016](../sources/malladi-2016-metastatic-latency-immune-evasion-through.md), [Bergholz 2023](../sources/bergholz-2023-pi3k-controls-immune-evasion-pten-deficient.md)

### Q88. EMT/plasticity는 면역회피의 원인인가 결과인가?
**A.** 로컬 근거는 EMT/plasticity가 면역회피의 '원인'으로 작동할 수 있음을 비교적 직접적으로 보여준다. [Kim 2024](../sources/kim-2024-plasticity-induced-repression-irf6-underlies-acquired.md)는 췌장암 면역치료 후 재발에서 ZEB1·SNAIL이 주도하는 EMT가 면역억제나 항원제시 기계 손상 없이도 Irf6를 후성유전적으로 침묵시켜 종양세포를 TNF-α 매개 T세포 살해에 저항하게 만든다고 보여, 가소성 프로그램 자체가 내성의 인과 동인임을 보인다. 다만 [Mullins 2022](../sources/mullins-2022-epithelial-mesenchymal-plasticity-tumor-immune-evasion.md)는 EMP-면역 상호작용이 양방향(면역세포가 EMP를 유도하기도 함)임을 강조하고, [Lou 2016](../sources/lou-2016-emt-inflammatory-signals-multiple-checkpoints-lung.md)은 mesenchymal 폐선암이 PD-L1·TIM-3·CTLA-4 등 다중 체크포인트와 Treg를 함께 띠어 EMT가 면역억제 회로와 공존함을 보여, '주로 원인이지만 면역압력에 의해 강화되는 가역적 상태'로 정리된다.

**Cited**: [Kim 2024](../sources/kim-2024-plasticity-induced-repression-irf6-underlies-acquired.md), [Mullins 2022](../sources/mullins-2022-epithelial-mesenchymal-plasticity-tumor-immune-evasion.md), [Lou 2016](../sources/lou-2016-emt-inflammatory-signals-multiple-checkpoints-lung.md)

### Q89. lineage plasticity는 면역세포 치료(CAR-T/BsAb)에서 왜 치명적인가?
**A.** Lineage plasticity는 표적 항원 자체를 발현하지 않는 다른 계통으로 종양이 갈아타게 만들어 단일 항원에 묶인 세포치료를 무력화하기 때문에 치명적이다. [Qiu 2025](../sources/qiu-2025-lineage-switch-cd19-cart-treatment-ball.md)는 CD19 CAR-T 후 비-KMT2A B-ALL이 창시 변이(FLT3-ITD, EP300::ZNF384 등)를 유지한 채 AML로 lineage switch해 재발하는 사례를 보여, 같은 종양이 myeloid로 transdifferentiation하면 CD19 표적이 통째로 사라짐을 입증한다. [Ruella 2023](../sources/ruella-2023-cart-resistance-haematological-malignancies.md)은 lineage plasticity를 항원음성 재발·accessory ligand 소실과 함께 CAR-T 내성의 종양 내재적 실패 모드로 분류하고, 이런 도피를 막기 위해 다중표적 구조 같은 공학적 대응이 필요하다고 정리한다.

**Cited**: [Qiu 2025](../sources/qiu-2025-lineage-switch-cd19-cart-treatment-ball.md), [Ruella 2023](../sources/ruella-2023-cart-resistance-haematological-malignancies.md)

### Q90. antigen loss가 reversible adaptation일 수 있는 조건은 무엇인가?
**A.** Antigen loss는 그것이 유전적 결손이 아니라 후성유전적·전사적 침묵이나 분해 조절에 의한 경우에 reversible adaptation일 수 있다. [Burr 2019](../sources/burr-2019-evolutionarily-conserved-function-polycomb-silences.md)는 MHC-I 항원처리 경로가 PRC2/H3K27me3 기반 bivalent 크로마틴으로 침묵된 것이라면 EZH2 억제로 되살릴 수 있음을 보여 가역성의 조건을 제시하고, [Meng 2025](../sources/meng-2025-reversal-tumour-immune-evasion-enhanced.md)는 PCSK9가 MHC-I 분해를 매개하므로 PCSK9 knockdown으로 항원제시를 최대 6배 회복시켜 분해 기반 소실도 되돌릴 수 있음을 보여준다. [Sari 2023](../sources/sari-2023-tumor-immune-evasion-through-loss.md) 리뷰도 일부 항원제시 결함은 가역적이라 정리한다. 반대로 [McGranahan 2017](../sources/mcgranahan-2017-allele-specific-hla-loss-immune-escape.md)의 HLA LOH처럼 대립유전자 자체가 소실된 구조적 손상은 비가역적이어서, 침묵·분해형은 가역, 결손·돌연변이형은 비가역이라는 경계가 나뉜다.

**Cited**: [Burr 2019](../sources/burr-2019-evolutionarily-conserved-function-polycomb-silences.md), [Meng 2025](../sources/meng-2025-reversal-tumour-immune-evasion-enhanced.md), [Sari 2023](../sources/sari-2023-tumor-immune-evasion-through-loss.md), [McGranahan 2017](../sources/mcgranahan-2017-allele-specific-hla-loss-immune-escape.md)

### Q91. antigen loss가 clonal selection일 수 있는 조건은 무엇인가?
**A.** antigen loss가 단순한 우연이 아니라 clonal selection이려면, 그 항원이 실제 면역압(immune pressure)을 받고 있었고 그 압력 아래에서 항원-결손 클론이 선택적으로 살아남았다는 증거가 필요하다. [McGranahan 2017](../sources/mcgranahan-2017-allele-specific-hla-loss-lung-cancer.md)은 allele-specific HLA loss가 subclonal하면서 subclonal neoantigen burden·APOBEC·cytolytic activity·PD-L1 양성이 높은(즉 면역압이 클) 영역에 enriche된다는 점을 selection의 근거로 제시했고, [Rosenthal 2019](../sources/rosenthal-2019-neoantigen-directed-immune-escape-lung-cancer.md)은 면역 침윤이 많은 영역에서 HLA LOH나 발현 neoantigen 고갈 같은 ongoing immunoediting이, 침윤이 적은 영역에서는 과거 editing의 흔적(neoantigen editing 약화·이전 clonal neoantigen의 copy-number loss)이 관찰됨을 보였다. 따라서 antigen loss를 clonal selection으로 부르려면 종양이 한때 면역원성을 띠고 면역반응을 유발했다는 정황(active immune response 이후의 escape)과 해당 결손이 시간/공간적으로 면역압과 같은 곳에 몰려 있다는 점이 함께 충족되어야 하며, [Zaretsky 2016](../sources/zaretsky-2016-acquired-resistance-pd1-melanoma.md)의 초기 반응 후 B2M·JAK 결손에 의한 escape가 그 전형적 사례다.

**Cited**: [McGranahan 2017](../sources/mcgranahan-2017-allele-specific-hla-loss-lung-cancer.md), [Rosenthal 2019](../sources/rosenthal-2019-neoantigen-directed-immune-escape-lung-cancer.md), [Zaretsky 2016](../sources/zaretsky-2016-acquired-resistance-pd1-melanoma.md)

### Q92. 치료 전부터 존재하는 minor clone이 치료 후 지배하는 시나리오는 어떤 데이터로 확인되는가?
**A.** 치료 전부터 존재하던 minor clone이 치료 후 지배하는 시나리오는 무엇보다 동일 환자의 치료 전·후(matched pre/post) 종양을 비교한 데이터로 확인된다. [Schiantarelli 2025](../sources/schiantarelli-2025-genomic-mediators-acquired-resistance-immunotherapy.md)은 전이성 흑색종 환자 25명의 치료 전·내성 후 짝지은 생검을 비교해 B2M·JAK1/2 결손과 SEC24C/D 변이 같은 내성 매개 변이가 내성 시점에 드러남을 보였고, 이런 paired 설계가 "치료가 어떤 클론을 선택했는가"를 직접 보여준다. 공간적으로는 [Rosenthal 2019](../sources/rosenthal-2019-neoantigen-directed-immune-escape-lung-cancer.md)의 다영역(multi-region) 분석처럼 종양 내 영역별로 neoantigen·HLA 상태가 다르다는 점이 minor clone의 사전 존재를 시사하며, CAR-T에서는 [Sotillo 2015](../sources/sotillo-2015-cd19-mutations-alternative-splicing-cart19.md)가 CD19 exon2 변이·exon skipping이 재발 시 수렴적으로 나타나는 항원-결손 클론의 outgrowth를 분자 수준에서 기록했다. 따라서 핵심 데이터는 (1) 동일 환자 시계열/짝 생검, (2) 다영역 sampling, (3) 재발 시점 항원/유전자 상태의 분자적 특성화다.

**Cited**: [Schiantarelli 2025](../sources/schiantarelli-2025-genomic-mediators-acquired-resistance-immunotherapy.md), [Rosenthal 2019](../sources/rosenthal-2019-neoantigen-directed-immune-escape-lung-cancer.md), [Sotillo 2015](../sources/sotillo-2015-cd19-mutations-alternative-splicing-cart19.md)

### Q93. resistance 논문을 위키로 정리할 때 최소 메타데이터(치료제/암종/endpoint/시점)는 무엇인가?
**A.** 로컬 resistance 논문들이 일관되게 구분 가능한 정보를 보면, 최소 메타데이터는 (1) 치료제/계열(예: anti-PD-1 pembrolizumab, CD19 CAR-T), (2) 암종, (3) endpoint 성격(초기 반응 후 진행=acquired인지 처음부터 무반응=primary인지), (4) 시점/표본 설계(치료 전·후 짝 생검인지 단면인지)다. [Zaretsky 2016](../sources/zaretsky-2016-acquired-resistance-pd1-melanoma.md)이 "흑색종·pembrolizumab·초기 객관적 반응 후 지연 진행·짝지은 생검"이라는 네 축을 모두 명시하기 때문에 primary 내성 연구와 다르게 인용되며, [Schiantarelli 2025](../sources/schiantarelli-2025-genomic-mediators-acquired-resistance-immunotherapy.md) 역시 "전이성 흑색종·ICI·치료 전후 matched 생검(n=25)·acquired"로 정리된다. 위키 카드에는 이 네 칸(치료제·암종·primary vs acquired endpoint·표본 시점)을 고정 필드로 두면 같은 면역회피 축이라도 시점이 다른 연구를 혼동하지 않고 비교할 수 있다.

**Cited**: [Zaretsky 2016](../sources/zaretsky-2016-acquired-resistance-pd1-melanoma.md), [Schiantarelli 2025](../sources/schiantarelli-2025-genomic-mediators-acquired-resistance-immunotherapy.md)

### Q94. resistance를 한 장짜리 그림으로 그릴 때 visibility/access/effector는 어떻게 배치하는가?
**A.** 한 장짜리 그림은 면역반응을 단일 사건이 아니라 단계적 cycle로 보는 [Chen 2013](../sources/chen-2013-cancer-immunity-cycle.md)의 cancer-immunity cycle을 가로축(좌→우)으로 깔고, 그 위에 visibility/access/effector 세 칸을 순서대로 배치하는 것이 자연스럽다. 즉 visibility=항원 제시(neoantigen 생성·MHC-I/HLA 제시) 단계, access=T세포 trafficking·infiltration(기질/혈관 장벽) 단계, effector=인식·killing(IFN 감지·세포독성) 단계로 대응시키고, 각 칸 아래에 그 단계를 끊는 대표 결손을 라벨로 붙인다(예: visibility에 HLA LOH·B2M, access에 TGF-β 매개 exclusion, effector에 JAK1/2 결손). 결손 위치를 [Galassi 2024](../sources/galassi-2024-hallmarks-cancer-immune-evasion.md)의 camouflage(숨기기)·coercion(효과세포 방해)·cytoprotection(세포독성 회피) 색으로 묶으면 "어느 단계가, 어떤 방식으로 깨졌는가"가 한눈에 읽힌다.

**Cited**: [Chen 2013](../sources/chen-2013-cancer-immunity-cycle.md), [Galassi 2024](../sources/galassi-2024-hallmarks-cancer-immune-evasion.md)

### Q95. 이 토픽에서 만들어야 할 “표준 메커니즘 taxonomy”는 어떤 구조가 좋은가?
**A.** 표준 메커니즘 taxonomy는 2단계 계층으로 잡는 것이 좋다: 상위 축은 [Galassi 2024](../sources/galassi-2024-hallmarks-cancer-immune-evasion.md)의 "three Cs"—camouflage(면역 인식 회피), coercion(효과세포 직간접 방해), cytoprotection(세포독성으로부터 보호)—를 쓰고, 그 아래에 [Chen 2013](../sources/chen-2013-cancer-immunity-cycle.md) cancer-immunity cycle의 어느 단계가 깨졌는지를 매핑한다. 예컨대 HLA LOH·B2M 결손([McGranahan 2017](../sources/mcgranahan-2017-allele-specific-hla-loss-lung-cancer.md))은 camouflage/항원제시 단계, JAK1/2 결손([Shin 2017](../sources/shin-2017-primary-resistance-pd1-jak-mutations.md))은 coercion/effector 감지 단계에 놓인다. 여기에 각 노드마다 "primary vs acquired" 시점 태그와 "tumor-intrinsic vs microenvironmental" 구분을 직교 속성으로 달면, 같은 단계라도 사전 결손인지 치료 중 선택된 것인지를 분리해 비교할 수 있다.

**Cited**: [Galassi 2024](../sources/galassi-2024-hallmarks-cancer-immune-evasion.md), [Chen 2013](../sources/chen-2013-cancer-immunity-cycle.md), [McGranahan 2017](../sources/mcgranahan-2017-allele-specific-hla-loss-lung-cancer.md), [Shin 2017](../sources/shin-2017-primary-resistance-pd1-jak-mutations.md)

### Q96. 위키에서 가장 먼저 확장해야 할 concept page 5개는 무엇인가?
**A.** 로컬 근거가 가장 두껍게 모여 있어 먼저 확장할 가치가 큰 concept page 5개는 (1) 항원제시/인터페론 축인 MHC-I·HLA loss와 interferon 결손([McGranahan 2017](../sources/mcgranahan-2017-allele-specific-hla-loss-lung-cancer.md), [Shin 2017](../sources/shin-2017-primary-resistance-pd1-jak-mutations.md)), (2) 세포치료 항원 escape·lineage switch([Sotillo 2015](../sources/sotillo-2015-cd19-mutations-alternative-splicing-cart19.md), [Qiu 2025](../sources/qiu-2025-lineage-switch-cd19-cart-treatment-ball.md)), (3) 전체 틀을 잡아주는 cancer-immunity cycle([Chen 2013](../sources/chen-2013-cancer-immunity-cycle.md))과 (4) 그 상위 분류인 immune-evasion hallmarks([Galassi 2024](../sources/galassi-2024-hallmarks-cancer-immune-evasion.md)), (5) 시점 구분의 기준점이 되는 acquired ICI resistance([Zaretsky 2016](../sources/zaretsky-2016-acquired-resistance-pd1-melanoma.md), [Schiantarelli 2025](../sources/schiantarelli-2025-genomic-mediators-acquired-resistance-immunotherapy.md))다. 이 다섯은 다른 거의 모든 resistance 논문이 참조점으로 삼는 노드여서, 먼저 살을 붙이면 위키 전체의 연결 밀도가 가장 크게 올라간다.

**Cited**: [McGranahan 2017](../sources/mcgranahan-2017-allele-specific-hla-loss-lung-cancer.md), [Shin 2017](../sources/shin-2017-primary-resistance-pd1-jak-mutations.md), [Sotillo 2015](../sources/sotillo-2015-cd19-mutations-alternative-splicing-cart19.md), [Qiu 2025](../sources/qiu-2025-lineage-switch-cd19-cart-treatment-ball.md), [Chen 2013](../sources/chen-2013-cancer-immunity-cycle.md), [Galassi 2024](../sources/galassi-2024-hallmarks-cancer-immune-evasion.md), [Zaretsky 2016](../sources/zaretsky-2016-acquired-resistance-pd1-melanoma.md), [Schiantarelli 2025](../sources/schiantarelli-2025-genomic-mediators-acquired-resistance-immunotherapy.md)

### Q97. 현재 위키에서 가장 약한 연결(빈 링크)은 어떤 메커니즘 축에 있는가?
**A.** 가장 약한(근거가 비어 있는) 연결은 "치료 중 시간에 따라 선택되는 acquired resistance" 축에 있다. 이 축의 핵심 논문 다수가 아직 deep-dive 전 상태로 Key Points가 'Awaiting deep-dive' 플레이스홀더이고 abstract만 채워져 있어([Schiantarelli 2025](../sources/schiantarelli-2025-genomic-mediators-acquired-resistance-immunotherapy.md), [Schoenfeld 2020](../sources/schoenfeld-2020-acquired-resistance-immune-checkpoint-inhibitors.md), [Rosenthal 2019](../sources/rosenthal-2019-neoantigen-directed-immune-escape-lung-cancer.md)), 사례별 분자 메커니즘이 cancer-immunity cycle 단계 노드와 아직 촘촘히 연결되어 있지 않다. 특히 [Schoenfeld 2020](../sources/schoenfeld-2020-acquired-resistance-immune-checkpoint-inhibitors.md) 자신이 acquired resistance 메커니즘 이해가 "remarkably limited"라고 적은 만큼, 시점(primary vs acquired)과 메커니즘 단계를 잇는 cross-link가 이 위키에서 가장 비어 있는 부분이다.

**Cited**: [Schiantarelli 2025](../sources/schiantarelli-2025-genomic-mediators-acquired-resistance-immunotherapy.md), [Schoenfeld 2020](../sources/schoenfeld-2020-acquired-resistance-immune-checkpoint-inhibitors.md), [Rosenthal 2019](../sources/rosenthal-2019-neoantigen-directed-immune-escape-lung-cancer.md)

### Q98. 다음 ingest batch에서 clinical trial, mechanism paper, review paper의 비율을 어떻게 잡을 것인가?
**A.** 다음 ingest batch는 mechanism paper를 중심(대략 절반)으로 두고 clinical trial과 review를 보조로 잡는 것이 현재 위키의 공백과 맞다. 이유는 메커니즘 노드(예: 항원제시 결손, 효과세포 감지 결손)를 채우는 [Zaretsky 2016](../sources/zaretsky-2016-acquired-resistance-pd1-melanoma.md)·[Shin 2017](../sources/shin-2017-primary-resistance-pd1-jak-mutations.md) 류의 일차 논문이 cycle 단계 매핑의 실제 근거가 되기 때문이고, review는 [Galassi 2024](../sources/galassi-2024-hallmarks-cancer-immune-evasion.md)처럼 taxonomy 골격을 주는 소수(한 batch당 1~2편)면 충분하며 과다하면 일차 근거 없이 라벨만 늘어난다. clinical trial은 메커니즘을 환자 시점(primary vs acquired)·endpoint에 묶는 역할이므로 mechanism의 절반 정도 비율로 넣어, 대략 mechanism:trial:review ≈ 5:3:2 정도가 균형점이다.

**Cited**: [Zaretsky 2016](../sources/zaretsky-2016-acquired-resistance-pd1-melanoma.md), [Shin 2017](../sources/shin-2017-primary-resistance-pd1-jak-mutations.md), [Galassi 2024](../sources/galassi-2024-hallmarks-cancer-immune-evasion.md)

### Q99. 이 주제를 교수진/공동연구자에게 공유할 때 어떤 3문장 구조가 가장 효과적인가?
**A.** 교수진/공동연구자에게는 "틀→증거→공백" 3문장 구조가 효과적이다: (1) 면역회피를 cancer-immunity cycle의 어느 단계가 깨지는가로 본다는 공통 틀을 제시하고([Chen 2013](../sources/chen-2013-cancer-immunity-cycle.md), [Galassi 2024](../sources/galassi-2024-hallmarks-cancer-immune-evasion.md)), (2) 그 틀에 들어맞는 단단한 증거 한두 개—초기 반응 후 B2M·JAK 결손에 의한 acquired escape—를 짚고([Zaretsky 2016](../sources/zaretsky-2016-acquired-resistance-pd1-melanoma.md)), (3) 아직 비어 있는 질문(acquired resistance의 시점-메커니즘 연결이 limited하다는 점, [Schoenfeld 2020](../sources/schoenfeld-2020-acquired-resistance-immune-checkpoint-inhibitors.md))을 던져 협업 지점을 만든다. 이 순서는 상대가 큰 그림을 먼저 잡고, 신뢰할 증거로 닻을 내린 뒤, 기여할 빈칸을 보게 해 준다.

**Cited**: [Chen 2013](../sources/chen-2013-cancer-immunity-cycle.md), [Galassi 2024](../sources/galassi-2024-hallmarks-cancer-immune-evasion.md), [Zaretsky 2016](../sources/zaretsky-2016-acquired-resistance-pd1-melanoma.md), [Schoenfeld 2020](../sources/schoenfeld-2020-acquired-resistance-immune-checkpoint-inhibitors.md)

### Q100. 이 topic을 읽은 사람이 최종적으로 설명해야 하는 resistance logic은 무엇인가?
**A.** 이 topic을 읽은 사람이 최종적으로 설명해야 할 resistance logic은 "종양은 면역에게 보여야 하고(visibility), 접근당해야 하며(access), 죽임당해야(effector) 면역치료가 듣는데, 내성은 이 사슬 중 어느 한 고리를 끊어 성립한다"는 한 줄이다([Chen 2013](../sources/chen-2013-cancer-immunity-cycle.md), [Galassi 2024](../sources/galassi-2024-hallmarks-cancer-immune-evasion.md)). 더 중요한 둘째 논리는 같은 고리라도 끊기는 시점이 다르다는 것—처음부터 인터페론을 감지 못해 무반응인 primary([Shin 2017](../sources/shin-2017-primary-resistance-pd1-jak-mutations.md))와, 면역반응이 일어난 뒤 항원/감지 결손 클론이 선택되어 escape하는 acquired([Zaretsky 2016](../sources/zaretsky-2016-acquired-resistance-pd1-melanoma.md), [McGranahan 2017](../sources/mcgranahan-2017-allele-specific-hla-loss-lung-cancer.md))를 구분할 수 있어야 한다. 즉 "어느 단계가, tumor-intrinsic인지 미세환경 때문인지, 언제(사전 vs 치료 중 선택) 깨졌는가"를 한 환자 사례에 대해 말할 수 있으면 이 위키의 핵심 logic을 이해한 것이다.

**Cited**: [Chen 2013](../sources/chen-2013-cancer-immunity-cycle.md), [Galassi 2024](../sources/galassi-2024-hallmarks-cancer-immune-evasion.md), [Shin 2017](../sources/shin-2017-primary-resistance-pd1-jak-mutations.md), [Zaretsky 2016](../sources/zaretsky-2016-acquired-resistance-pd1-melanoma.md), [McGranahan 2017](../sources/mcgranahan-2017-allele-specific-hla-loss-lung-cancer.md)
