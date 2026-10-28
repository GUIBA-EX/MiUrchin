![MiUrchin — representative echinoid diversity](figures/MiUrchin_overview.png)

# MiUrchin

[English](README.md)

海胆16S rRNA环境DNA候选引物，保留S、M、L、XL四个长度。每个长度的普通、A、B、D起止坐标一致；D为一对简并引物，A/B为普通引物分别PCR后的并集。参考跨度为188、228、343、440 bp。

主指标采用**目间等权**：每目内先计算检出物种标签比例，再对11个目取均值；任一参考命中即可检出该标签，完全匹配采用同一层级。共同面板80条参考、49个标签，目级归属已按WoRMS接受分类核对。三个目各只有一个标签，满覆盖不代表覆盖该目所有物种。

[分类映射 / Taxonomy](results/D_3prime8/panel.csv) · [图片来源 / Photo references](figures/overview_design.md)

![Binding positions](figures/binding_positions.svg)

## 当前表现

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

覆盖要求两端各≤2错配且末端3 nt兼容，完全匹配要求两端无错配。WC3/GT2为宽松模型的非目标记录数，不强制末端兼容；背景库6,045条。

## D方案的取舍

D引物每条简并度不超过8，简并位点只在3′半段；短片段完全匹配率较低。L的目间覆盖较高，但严格GT背景包含12条海星记录；XL严格GT背景包含19条海百合记录。各目和标签的得失见[选择与验证](docs/D_OPTIMIZATION.md)。

[A/B互补性 / A/B complementarity](docs/AB_COMPLEMENTARITY.md)

<details>
<summary>次要比较：原参考加权口径</summary>

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

该表先按物种标签等权，再在标签内按参考等权，与主表的目间等权不同。

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

图中每行对应一条参考，按现行目分组；F/R均按引物5′→3′方向显示，方框标记末端3 nt，+n表示参考同源列间插入碱基。左侧E/C表示全序列扫描的完全匹配/覆盖。

[全部16对碱基匹配图 / All 16 base plots](results/terminal_optimization/base_matching.html)

## 方法与复核

同坐标搜索生成47,638对；优先考虑目间覆盖、完全匹配及背景。简并限制为每条≤8且仅在3′半段。五个候选由独立C++/Python扫描复核，800项目标判定、20个背景集合及25项背景计数无差异。D为单对；A/B为分管并集。所有方案尚待实验验证。

[Sequences](sequences/primer_pairs.csv) · [FASTA](sequences/primers.fasta) · [Results](results/current/taxonomic_comparison.csv) · [Methods](docs/METHODS.zh-CN.md) · [Reproduction](docs/REPRODUCIBILITY.md) · [Validation](docs/VALIDATION.md)

[Copyright / 著作权声明](COPYRIGHT.md)
