# MiUrchin

[中文](README.zh-CN.md)

![Binding positions](figures/binding_positions.svg)

Each length uses one shared locus: ordinary, A, B and D have identical forward and reverse start/end coordinates. At each locus, ordinary single, ordinary A/B union and degenerate single are selected by coverage plus exact matching; their scores are averaged equally to select the locus. Background limits are WC≤3 ≤5 and GT≤2 ≤5 accessions. All concrete variants pass terminal rules and both thermodynamic scenarios. A/B results are separate-PCR unions, not experimentally validated multiplex results. References are reused for design and evaluation; coverage is computational, not measured PCR efficiency.

D denotes a degenerate single pair; no suffix denotes an ordinary single pair; A/B are ordinary same-locus alternatives. Each project has 12 portfolios, 16 pair records and 32 sequences.

| Scheme | Coverage % | Exact % | WC≤3 | GT≤2 | WC≤4 |
|---|---:|---:|---:|---:|---:|
| SD | 63.27 | 16.33 | 0 | 0 | 8 |
| S | 26.53 | 4.08 | 0 | 0 | 1 |
| SA+SB | 26.53 | 4.08 | 0 | 0 | 1 |
| MD | 87.76 | 48.98 | 0 | 1 | 0 |
| M | 59.18 | 16.33 | 0 | 0 | 0 |
| MA+MB | 59.18 | 30.61 | 0 | 0 | 0 |
| LD | 87.76 | 34.69 | 2 | 1 | 162 |
| L | 75.51 | 19.39 | 2 | 1 | 161 |
| LA+LB | 75.51 | 33.67 | 2 | 1 | 161 |
| XLD | 85.71 | 6.12 | 2 | 0 | 11 |
| XL | 81.63 | 18.37 | 3 | 5 | 11 |
| XLA+XLB | 91.84 | 24.49 | 3 | 5 | 16 |

Background hits can remain substantial under relaxed mismatch models; see the complete results and missed-reference records.

[Sequences](sequences/primer_pairs.csv) · [FASTA](sequences/primers.fasta) · [Results](results/terminal_optimization/comparison.csv) · [Verification](results/terminal_optimization/verification.json) · [Full base matching](results/terminal_optimization/base_matching.html)

## S

| Name | F (5′→3′) | R (5′→3′) |
|---|---|---|
| SD | `YGTGTATAATGGATTAACRAGH` | `GCTTAGCTHARACTAATTTCTYGG` |
| S | `TGTGTATAATGGATTAACGAGA` | `GCTTAGCTAAAACTAATTTCTTGG` |
| SA | `CGTGTATAATGGATTAACAAGA` | `GCTTAGCTAAAACTAATTTCTTGG` |
| SB | `TGTGTATAATGGATTAACGAGA` | `GCTTAGCTAAAACTAATTTCTTGG` |

![SD base matching](figures/base_matching_SD.svg)

![S base matching](figures/base_matching_S.svg)
## M

| Name | F (5′→3′) | R (5′→3′) |
|---|---|---|
| MD | `CGYHAGACGAGAAGACCCTR` | `CTTTGATCAYCTDRRTGGATCA` |
| M | `CGTTAGACGAGAAGACCCTG` | `CTTTGATCACCTTAGTGGATCA` |
| MA | `CGCTAGACGAGAAGACCCTG` | `CTTTGATCACCTTAGTGGATCA` |
| MB | `CGTTAGACGAGAAGACCCTG` | `CTTTGATCACCTTAGTGGATCA` |

![MD base matching](figures/base_matching_MD.svg)

![M base matching](figures/base_matching_M.svg)
## L

| Name | F (5′→3′) | R (5′→3′) |
|---|---|---|
| LD | `GTCTCCTAAATAGAGACTAGTATGAATGGC` | `GCGGTAACTTGTTYCTTTGRTCAYC` |
| L | `GTCTCCTAAATAGAGACTAGTATGAATGGC` | `GCGGTAACTTGTTCCTTTGATCACC` |
| LA | `GTCTCCTAAATAGAGACTAGTATGAATGGC` | `GCGGTAACTTGTTCCTTTGATCACC` |
| LB | `GTCTCCTAAATAGAGACTAGTATGAATGGC` | `GCGGTAACTTGTTTCTTTGATCACC` |

![LD base matching](figures/base_matching_LD.svg)

![L base matching](figures/base_matching_L.svg)
## XL

| Name | F (5′→3′) | R (5′→3′) |
|---|---|---|
| XLD | `RAGTAGGCCTAGAAGCAGCC` | `CCGTCTTGCCATTCATACCAGTCTC` |
| XL | `GAATAGGCCTAGAAGCAGCC` | `CCGTCTTGCCATTCATACTAGTCTC` |
| XLA | `GAATAGGCCTAGAAGCAGCC` | `CCGTCTTGCCATTCATACTAGTCTC` |
| XLB | `AAGTAGGCCTAGAAGCAGCC` | `CCGTCTTGCCATTCATACCAGTCTC` |

![XLD base matching](figures/base_matching_XLD.svg)

![XL base matching](figures/base_matching_XL.svg)

Independent target checks: 2560; disagreements: 0. Background set checks: 32; disagreements: 0.

[Copyright / 著作权声明](COPYRIGHT.md)
