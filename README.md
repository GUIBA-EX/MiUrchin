![MiUrchin — representative echinoid diversity](figures/MiUrchin_overview.png)

# MiUrchin

[中文](README.zh-CN.md)

Candidate mitochondrial 16S rRNA primers for echinoid eDNA in four windows: S, M, L and XL. Ordinary, A, B and D share identical endpoints within each length. D is one degenerate pair; A/B are ordinary pairs evaluated as separate-PCR unions. Reference spans are 188, 228, 343 and 440 bp.

Primary metrics use **equal order weighting**: calculate the detected species-label fraction within each order, then average across 11 orders. Any matching reference detects its label; exact matching uses the same hierarchy. The common panel contains 80 references and 49 labels with WoRMS-verified accepted orders. Three orders have one label each; full panel coverage does not imply coverage of every species.

[分类映射 / Taxonomy](results/D_3prime8/panel.csv) · [图片来源 / Photo references](figures/overview_design.md)

![Binding positions](figures/binding_positions.svg)

## Current performance

| Scheme | Order coverage % | Order exact % | WC≤3 | GT≤2 | WC≤4 |
|---|---:|---:|---:|---:|---:|
| SD | 43.83 | 0.32 | 0 | 0 | 1 |
| S | 4.22 | 0.65 | 0 | 0 | 1 |
| SA+SB | 11.04 | 0.97 | 0 | 0 | 7 |
| MD | 84.09 | 18.94 | 0 | 0 | 0 |
| M | 47.73 | 6.82 | 0 | 0 | 0 |
| MA+MB | 47.73 | 9.09 | 0 | 0 | 0 |
| LD | 91.56 | 13.85 | 12 | 12 | 247 |
| L | 68.83 | 3.25 | 2 | 1 | 161 |
| LA+LB | 68.83 | 5.52 | 2 | 1 | 161 |
| XLD | 98.70 | 42.42 | 12 | 21 | 49 |
| XL | 77.49 | 2.92 | 3 | 5 | 11 |
| XLA+XLB | 98.70 | 21.10 | 3 | 5 | 16 |

Coverage requires ≤2 mismatches per primer and compatible terminal 3 nt; exact matching requires zero mismatches at both ends. WC3/GT2 count permissive non-target hits without the terminal constraint in 6,045 background records.

## D-assay tradeoffs

Each D oligo has at most eight variants, with ambiguity confined to its 3′ half. Exact matching is limited in the shorter assays. L has 12 strict-GT sea-star background records; XL has 19 strict-GT crinoid records. See [selection and verification](docs/D_OPTIMIZATION.md) for order and label gains and losses.

[A/B complementarity](docs/AB_COMPLEMENTARITY.md)

<details>
<summary>Secondary comparison: original reference-weighted metrics</summary>

| Scheme | Coverage % | Exact % | WC≤3 | GT≤2 | WC≤4 |
|---|---:|---:|---:|---:|---:|
| SD | 58.16 | 2.04 | 0 | 0 | 1 |
| S | 26.53 | 4.08 | 0 | 0 | 1 |
| SA+SB | 41.84 | 6.12 | 0 | 0 | 7 |
| MD | 79.59 | 20.41 | 0 | 0 | 0 |
| M | 59.18 | 16.33 | 0 | 0 | 0 |
| MA+MB | 59.18 | 30.61 | 0 | 0 | 0 |
| LD | 85.71 | 25.51 | 12 | 12 | 247 |
| L | 75.51 | 19.39 | 2 | 1 | 161 |
| LA+LB | 75.51 | 33.67 | 2 | 1 | 161 |
| XLD | 91.84 | 16.33 | 12 | 21 | 49 |
| XL | 81.63 | 18.37 | 3 | 5 | 11 |
| XLA+XLB | 91.84 | 24.49 | 3 | 5 | 16 |

This table weights labels equally and references equally within labels; it differs from the primary order-balanced metric.

</details>

## S

| Name | F (5′→3′) | R (5′→3′) |
|---|---|---|
| SD | `CGTGTATAATGGATTAACRAGH` | `GCTTAGCTCAAACTAATTTCYTDG` |
| S | `TGTGTATAATGGATTAACGAGA` | `GCTTAGCTAAAACTAATTTCTTGG` |
| SA | `TGTGTATAATGGATTAACAAGC` | `GCTTAGCTTAAACTAATTTCTTGG` |
| SB | `TGTGTATAATGGATTAACGAGA` | `GCTTAGCTAAAACTAATTTCTTGG` |

![SD base matching](figures/base_matching_SD.svg)

## M

| Name | F (5′→3′) | R (5′→3′) |
|---|---|---|
| MD | `CGTTAGACGAGAAGACCCTR` | `CTTTGATCACCKKRGTGGATCA` |
| M | `CGTTAGACGAGAAGACCCTG` | `CTTTGATCACCTTAGTGGATCA` |
| MA | `CGCTAGACGAGAAGACCCTG` | `CTTTGATCACCTTAGTGGATCA` |
| MB | `CGTTAGACGAGAAGACCCTG` | `CTTTGATCACCTTAGTGGATCA` |

![MD base matching](figures/base_matching_MD.svg)

## L

| Name | F (5′→3′) | R (5′→3′) |
|---|---|---|
| LD | `GTCTCCTAAATAGAGACTAGYATGAAYGGC` | `GCGGTAACTTGTTCYTTTGATCRCY` |
| L | `GTCTCCTAAATAGAGACTAGTATGAATGGC` | `GCGGTAACTTGTTCCTTTGATCACC` |
| LA | `GTCTCCTAAATAGAGACTAGTATGAATGGC` | `GCGGTAACTTGTTCCTTTGATCACC` |
| LB | `GTCTCCTAAATAGAGACTAGTATGAATGGC` | `GCGGTAACTTGTTTCTTTGATCACC` |

![LD base matching](figures/base_matching_LD.svg)

## XL

| Name | F (5′→3′) | R (5′→3′) |
|---|---|---|
| XLD | `AAGTAGGCCTARAAGCAGCC` | `CCGTCTTGCCATTCATRCYAGTCTY` |
| XL | `GAATAGGCCTAGAAGCAGCC` | `CCGTCTTGCCATTCATACTAGTCTC` |
| XLA | `AAGTAGGCCTAGAAGCAGCC` | `CCGTCTTGCCATTCATACCAGTCTC` |
| XLB | `GAATAGGCCTAGAAGCAGCC` | `CCGTCTTGCCATTCATACTAGTCTC` |

![XLD base matching](figures/base_matching_XLD.svg)

Each plot row is one reference, grouped by accepted order. F/R are shown in primer 5′→3′ orientation; boxes mark the final 3 nt and +n marks inserted bases between reference columns. E/C indicate full-sequence exact/covered states.

[全部16对碱基匹配图 / All 16 base plots](results/terminal_optimization/base_matching.html)

## Methods and verification

The fixed-coordinate search generated 47,638 pairs; candidates were ranked by order-balanced coverage, exact matching and background. D oligos contain at most eight variants with ambiguity in the 3′ half. Independent C++/Python scans agree on 800 target decisions, 20 background sets and 25 background counts for five candidates. D denotes one pair; A/B denotes a separate-PCR union. All assays await experimental validation.

[Sequences](sequences/primer_pairs.csv) · [FASTA](sequences/primers.fasta) · [Results](results/current/taxonomic_comparison.csv) · [Methods](docs/METHODS.md) · [Reproduction](docs/REPRODUCIBILITY.md) · [Validation](docs/VALIDATION.md)

[Copyright / 著作权声明](COPYRIGHT.md)
