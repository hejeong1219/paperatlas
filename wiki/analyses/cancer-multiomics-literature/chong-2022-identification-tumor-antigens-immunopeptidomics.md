# Chong 2022 - Identification of Tumor Antigens with Immunopeptidomics

## 논문 정보 (저자 / 저널 / DOI / Wiki 경로)

- 저자: Chong, Coukos, Bassani-Sternberg
- 저널/연도: Nature Biotechnology, 2022 (Review)
- DOI: 10.1038/s41587-021-01038-8
- Wiki 경로: [Identification of tumor antigens with immunopeptidomics](../../sources/chong-2022-identification-tumor-antigens-immunopeptidomics.md)

## 한 줄 요약

면역펩티돔(immunopeptidomics)을 통해 **종양에서 실제로 제시되는(resented) 항원**을 직접 측정하고, canonical·noncanonical 항원까지 확장하는 방법론/한계/검증 프레임을 정리한 리뷰.

## 과제 관련성 (Cancer Multiomics)

- Cancer Multiomics 과제에서 WGS 기반 neoantigen 후보를 만들더라도, 최종적으로는 “실제 제시되는 항원” evidence가 중요하므로 immunopeptidomics 기반 검증 프레임을 정리하는 레퍼런스가 된다.
- SV/비정형 번역/비암호화 영역 등 **noncanonical 항원**을 포함하면 후보 공간은 크게 늘지만 false positive 위험도 커져서, 후보 선정/검증 기준(FDR, orthogonal evidence)이 필요하다는 점을 강조한다.
- 향후 proteogenomics(샘플 특이 DB 구성) + immunopeptidomics를 결합한 파이프라인 설계 시, 어디에서 오류가 커지는지(검색공간 확장 vs 검증) 체크리스트로 활용 가능하다.

## 주요 결과

- canonical 항원(CTA, SNV/indel/fusion 유래 neoantigen)과 noncanonical 항원(대체 ORF, splicing/intron retention, lncRNA/pseudogene, TE/ERV, DRiP, proteasome splicing, PTM peptide 등) 원천을 체계적으로 분류한다.
- noncanonical 후보를 포함하는 proteogenomic 검색은 reference DB가 커져 false positive가 증가할 수 있어, 엄격한 FDR 관리와 orthogonal evidence(전사체/리보솜 프로파일링) 및 추가 검증이 필요함을 논의한다.
- 임상 적용(개인맞춤 백신, TCR-T) 관점에서 항원 “발굴→우선순위화→검증” 전체 흐름의 병목을 정리한다.

## Slack 메시지 초안

Chong et al. Nat Biotech 2022 리뷰는 immunopeptidomics로 종양에서 실제 제시되는 항원을 직접 측정해 canonical뿐 아니라 noncanonical 항원까지 발굴하는 프레임을 정리합니다. Cancer Multiomics 과제에서 WGS 기반 neoantigen 후보를 만들 때도, 검색공간을 넓힐수록 false positive 위험이 커지므로(FDR/검증), immunopeptidomics evidence와 우선순위화·검증 기준을 함께 설계해야 한다는 점을 강조하는 레퍼런스입니다.

