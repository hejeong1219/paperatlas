---
title: "Memon 2024 - Acquired Resistance to PD-(L)1 Blockade in NSCLC"
tags:
  - cancer-multiomics
  - wgs
  - immunotherapy
  - resistance
  - slack-digest
themes:
  - immune-evasion
  - acquired-resistance
  - interferon-signaling
  - antigen-presentation
---
# Memon 2024 - Acquired Resistance to PD-(L)1 Blockade in NSCLC

## 논문 정보 (저자 / 저널 / DOI / Wiki 경로)

- 저자: Memon et al.
- 저널: Cancer Cell (2024)
- DOI: 10.1016/j.ccell.2023.12.013
- Wiki 경로:
  - Source: `wiki/sources/memon-2024-clinical-molecular-features-acquired-resistance.md`
  - Cancer Multiomics brief: `wiki/analyses/cancer-multiomics-literature/memon-2024-clinical-molecular-features-acquired-resistance.md`
- Local PDF: `raw/inbox/papers/memon-2024-clinical-molecular-features-acquired-resistance.pdf`

## 한 줄 요약

NSCLC에서 PD-(L)1 치료 후 획득내성은 흔하며, 재발 병변은 “IFNγ 반응 증가/지속 + 항원제시 경로 이상(예: B2M 변이/단백 발현 저하)”로 특징지어지는 **persistently inflamed but dysfunctional** 상태로 분기된다.

## 과제 관련성 (Cancer Multiomics)

- **WGS/변이 해석 축**: 치료 전후(특히 진행 시점) 종양에서 항원제시 경로(B2M/HLA 등) 변이/LOH/구조변이/복제수 변화가 획득내성과 함께 나타날 수 있음을 “cohort-scale”로 프레이밍한다(본 논문은 WES 중심).
- **면역/저항성 feature 축**: “IFNγ signature stable vs increase”처럼 치료 후 전사체 기반 면역 상태 변화가 내성 경로 분기와 연결될 수 있음을 제시해, Cancer Multiomics에서 multi-layer feature(유전체+전사체+단백/인산화) 통합 모델 설계 질문으로 연결된다.
- **임상 샘플링 축**: 진행 직후(예: radiographic progression 후 수 주 내) 생검과 lesion-level(oligoprogression) 해석의 중요성을 명시적으로 보여줘, Cancer Multiomics 파일럿에서 표준 메타데이터(시점/병변/이전치료)를 고정해야 하는 근거가 된다.

## 주요 결과

- 치료 맥락:
  - 암종/치료: NSCLC, PD-1 blockade 기반(임상 코호트: MSK)
  - 라벨: 초기 반응 후 진행 = acquired resistance (AR)
  - 샘플 타이밍: 진행 병변은 radiographic progression 이후 채취(분석 코호트에서 progression→채취 중앙값 3.7주)
- 데이터 레이어:
  - 임상 코호트: 1,201명(NSCLC, PD-1 blockade) 중 초기 반응 243명(20%)
  - 분자 프로파일링 subset:
    - 전사체(whole transcriptome microarray): 29명에서 42개 종양 샘플(치료 전 13, 치료 후 29)
    - 유전체(WES): 22명에서 34개 종양 샘플(치료 전 15, 치료 후 19)
  - 추가: 치료 후 후기 재발을 모사한 murine AR 모델(anti-PD-(L)1 반복 노출)
- 데이터 공개:
  - (PDF Data Availability 기준) PMC 본문/보충표 중심으로 확인 필요(Cancer Multiomics 위키에서는 “PDF 확인 필요”로 유지).
- 임상적 관찰:
  - AR 누적 발생률: 5년 추적 경쟁위험(competing risk) 모델에서 61% (95% CI 36%–85%)
  - AR 발생 시점: 52% (≤1년), 39% (1–2년), 11% (>2년)
  - AR vs primary resistance 비교: baseline PD-L1 단백 발현이 AR군에서 더 흔함(55% vs 28%); 진행 패턴도 상이(예: liver metastasis: primary 31% vs AR 7%)
  - 진행 후 생존: AR이 primary progression보다 길었음(중앙값 18.9개월 vs 4.4개월)
- 전사체 기반 내성 경로(치료 전후 paired 비교):
  - ssGSEA에서 치료 후 IFN alpha/gamma response, oxidative phosphorylation, DNA repair pathway가 상승(FDR < 0.1)
  - CIBERSORT 기반 deconvolution에서 치료 후 CD8+ T cell infiltration 증가 신호
  - 치료 후 IFNγ response 변화에 따라 “stable” vs “increase”로 분류 가능하며, increase 군에서 **지속적 IFN signaling + immune dysfunction** 성격이 두드러짐
- 유전체 기반 내성 후보:
  - 치료 후(AR) 종양에서 항원제시 경로 유전자 이상이 선택적으로 관찰/강화되는 패턴을 제시
  - 예시로 post-treatment에서 B2M nonsense/frameshift가 관찰된 케이스가 언급되며, IFNγ 증가 군에서 항원제시 경로 이상이 더 흔한 방향성을 제시

## Slack 메시지 초안

1) (NSCLC, PD-(L)1) 1,201명 코호트에서 초기 반응자 243명 중 AR이 흔하고(5년 누적 61%), AR은 진행 이후에도 생존이 길어 “면역이 완전히 사라진 상태”라기보다 **persistently inflamed** 프레임이 맞는 듯합니다.  
2) 전사체 paired 분석(29명, 42샘플)에서 치료 후 IFNα/IFNγ signature가 올라가고 CD8 infiltration도 증가 신호가 있는데, IFNγ response가 “stable vs increase”로 갈라지며 increase 군에서 immune dysfunction/지속 IFN signaling 양상이 더 강합니다.  
3) WES paired(22명, 34샘플)에서는 AR 병변에서 항원제시 경로 이상(예: B2M 변이/발현 저하)이 선택 압력 하에 나타날 수 있음을 보여줘, Cancer Multiomics에서 WGS 기반 항원제시 feature + 면역상태 변화(전사체/단백체)를 함께 모델링할 근거가 됩니다.  
4) 실무 포인트: AR 해석은 lesion-level(oligoprogression)·진행 직후 생검(중앙값 3.7주) 같은 **표준 메타데이터 고정**이 핵심이라, Cancer Multiomics 파일럿에서도 시점/병변/이전치료 기록을 템플릿에 강제하는 게 좋겠습니다.

