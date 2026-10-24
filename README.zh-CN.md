# MiUrchin

[English](README.md)

![Binding positions](figures/binding_positions.svg)

每个长度联合选择一个共同位点：普通、A、B、D的正反向起止坐标完全相同。位点内按覆盖率与完全匹配率之和选择普通单对、普通A/B并集和简并单对，三类评分等权平均选择位点。背景门槛为WC≤3及GT≤2各不超过5条记录。所有实际序列变体通过末端规则和两种浓度热力学检查。A/B指标为独立PCR并集，未验证混池；设计与评估共用参考数据，计算覆盖率不代表实测扩增效率。

D表示简并单对；无后缀为普通单对，A/B为同位点普通双对。每个项目12套方案、16对记录、32条序列。

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

宽松错配模型下的背景命中仍可能较高；完整结果和漏检记录见数据文件。

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
