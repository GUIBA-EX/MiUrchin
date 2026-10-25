![MiUrchin — representative echinoid diversity](figures/MiUrchin_overview.png)

# MiUrchin

[中文](README.zh-CN.md)

Candidate mitochondrial 16S rRNA primers for echinoid eDNA in four windows: S, M, L and XL. Ordinary, A, B and D share identical endpoints within each length. D is one degenerate pair; A/B are ordinary pairs evaluated as separate-PCR unions. Reference spans are 188, 228, 343 and 440 bp.

Primary metrics use **equal order weighting**: calculate the detected species-label fraction within each order, then average across 11 orders. Any matching reference detects its label; exact matching uses the same hierarchy. The common panel contains 80 references and 49 labels with WoRMS-verified accepted orders. Three orders have one label each; full panel coverage does not imply coverage of every species.

[分类映射 / Taxonomy](results/D_optimization/panel.csv) · [图片来源 / Photo references](figures/overview_design.md)

![Binding positions](figures/binding_positions.svg)

## Current performance

| Scheme | Order coverage % | Order exact % | WC≤3 | GT≤2 | WC≤4 |
|---|---:|---:|---:|---:|---:|
| SD | 64.18 | 20.78 | 4 | 0 | 30 |
| S | 4.22 | 0.65 | 0 | 0 | 1 |
| SA+SB | 11.04 | 0.97 | 0 | 0 | 7 |
| MD | 85.39 | 67.53 | 0 | 0 | 1 |
| M | 47.73 | 6.82 | 0 | 0 | 0 |
| MA+MB | 47.73 | 9.09 | 0 | 0 | 0 |
| LD | 90.58 | 16.77 | 12 | 1 | 246 |
| L | 68.83 | 3.25 | 2 | 1 | 161 |
| LA+LB | 68.83 | 5.52 | 2 | 1 | 161 |
| XLD | 100.00 | 80.74 | 12 | 22 | 84 |
| XL | 77.49 | 2.92 | 3 | 5 | 11 |
| XLA+XLB | 98.70 | 21.10 | 3 | 5 | 16 |

Coverage requires ≤2 mismatches per primer and compatible terminal 3 nt; exact matching requires zero mismatches at both ends. WC3/GT2 count permissive non-target hits without the terminal constraint in 6,045 background records.

## D-assay tradeoffs

- **SD**: order coverage rises from 42.10 to 64.18%; seven labels gained and five lost, at 108/108 degeneracy.
- **MD**: coverage is unchanged. The 33/49 exact labels are more evenly distributed across orders, raising order exact matching from 41.88 to 67.53%.
- **LD**: coverage is unchanged; three exact labels are gained, with reverse degeneracy increasing from 16 to 128.
- **XLD**: 49/49 labels remain covered; exact labels rise from 28 to 38/49 and order exact matching from 62.01 to 80.74%.

[D完整选择与逐类群增减 / D selection and taxon changes](docs/D_OPTIMIZATION.md) · [A/B互补性 / A/B complementarity](docs/AB_COMPLEMENTARITY.md)

<details>
<summary>Secondary comparison: original reference-weighted metrics</summary>

| Scheme | Coverage % | Exact % | WC≤3 | GT≤2 | WC≤4 |
|---|---:|---:|---:|---:|---:|
| SD | 77.55 | 22.45 | 4 | 0 | 30 |
| S | 26.53 | 4.08 | 0 | 0 | 1 |
| SA+SB | 41.84 | 6.12 | 0 | 0 | 7 |
| MD | 87.76 | 67.35 | 0 | 0 | 1 |
| M | 59.18 | 16.33 | 0 | 0 | 0 |
| MA+MB | 59.18 | 30.61 | 0 | 0 | 0 |
| LD | 93.88 | 42.86 | 12 | 1 | 246 |
| L | 75.51 | 19.39 | 2 | 1 | 161 |
| LA+LB | 75.51 | 33.67 | 2 | 1 | 161 |
| XLD | 100.00 | 77.55 | 12 | 22 | 84 |
| XL | 81.63 | 18.37 | 3 | 5 | 11 |
| XLA+XLB | 91.84 | 24.49 | 3 | 5 | 16 |

This table weights labels equally and references equally within labels; it differs from the primary order-balanced metric.

</details>

## S

| Name | F (5′→3′) | R (5′→3′) |
|---|---|---|
| SD | `YGTGTATAATGGATTDACDASH` | `GCTTAGCTHAVACYAATTTCTYDG` |
| S | `TGTGTATAATGGATTAACGAGA` | `GCTTAGCTAAAACTAATTTCTTGG` |
| SA | `TGTGTATAATGGATTAACAAGC` | `GCTTAGCTTAAACTAATTTCTTGG` |
| SB | `TGTGTATAATGGATTAACGAGA` | `GCTTAGCTAAAACTAATTTCTTGG` |

![SD base matching](figures/base_matching_SD.svg)

## M

| Name | F (5′→3′) | R (5′→3′) |
|---|---|---|
| MD | `SGYYAGACGAGAAGACCCTR` | `YTTTGATCAYCKDRRTGGATCA` |
| M | `CGTTAGACGAGAAGACCCTG` | `CTTTGATCACCTTAGTGGATCA` |
| MA | `CGCTAGACGAGAAGACCCTG` | `CTTTGATCACCTTAGTGGATCA` |
| MB | `CGTTAGACGAGAAGACCCTG` | `CTTTGATCACCTTAGTGGATCA` |

![MD base matching](figures/base_matching_MD.svg)

## L

| Name | F (5′→3′) | R (5′→3′) |
|---|---|---|
| LD | `GTCTCCTAAATAGAGACTAGYATGAATGGC` | `RCGGTAACTTRTTYCTYTGRTCRYC` |
| L | `GTCTCCTAAATAGAGACTAGTATGAATGGC` | `GCGGTAACTTGTTCCTTTGATCACC` |
| LA | `GTCTCCTAAATAGAGACTAGTATGAATGGC` | `GCGGTAACTTGTTCCTTTGATCACC` |
| LB | `GTCTCCTAAATAGAGACTAGTATGAATGGC` | `GCGGTAACTTGTTTCTTTGATCACC` |

![LD base matching](figures/base_matching_LD.svg)

## XL

| Name | F (5′→3′) | R (5′→3′) |
|---|---|---|
| XLD | `DRRTAGGCCYARAAGCAGCC` | `CCSTCTYGCCRTTCATRCYAGTCTY` |
| XL | `GAATAGGCCTAGAAGCAGCC` | `CCGTCTTGCCATTCATACTAGTCTC` |
| XLA | `AAGTAGGCCTAGAAGCAGCC` | `CCGTCTTGCCATTCATACCAGTCTC` |
| XLB | `GAATAGGCCTAGAAGCAGCC` | `CCGTCTTGCCATTCATACTAGTCTC` |

![XLD base matching](figures/base_matching_XLD.svg)

Each plot row is one reference, grouped by accepted order. F/R are shown in primer 5′→3′ orientation; boxes mark the final 3 nt and +n marks inserted bases between reference columns. E/C indicate full-sequence exact/covered states.

[全部16对碱基匹配图 / All 16 base plots](results/terminal_optimization/base_matching.html)

## Methods and verification

The search compared 10,394 coordinate-fixed pairs with degeneracy ≤128 per direction and allowed 3′ ambiguity. Order coverage takes priority with order- and label-level exact-matching safeguards. All concrete variants pass terminal and two-concentration thermodynamic checks. Independent C++/Python scans of eight baseline/candidate D pairs agree on 1,280 target decisions and 32 background sets. The release contains 12 portfolios, 16 pairs and 32 oligos. These computational results require experimental validation.

[Sequences](sequences/primer_pairs.csv) · [FASTA](sequences/primers.fasta) · [Results](results/current/taxonomic_comparison.csv) · [Methods](docs/METHODS.md) · [Reproduction](docs/REPRODUCIBILITY.md) · [Validation](docs/VALIDATION.md)

[Copyright / 著作权声明](COPYRIGHT.md)
