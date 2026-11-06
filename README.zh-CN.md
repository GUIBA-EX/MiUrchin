![MiUrchin](figures/MiUrchin_overview.png)

# MiUrchin: in silico design and evaluation of mitochondrial and nuclear primers for sea urchin (Echinoidea) eDNA metabarcoding

**Fei Xia**

[正體中文](README.md) · [English](README.en.md) · [简体中文](README.zh-CN.md)

**原始不分分类群方案优先展示 · 分支方案作为补充**

修订稿件（2026-11-06） · [PDF](publications/manuscript_20261106/MiUrchin_manuscript.pdf) · [Word](publications/manuscript_20261106/MiUrchin_manuscript.docx) · [Markdown](publications/manuscript_20261106/MiUrchin_manuscript.md)

原来的 **32 对不按分类群拆分的引物（普通及 D）**继续作为主方案保留，优先展示如下，序列及原始评价结果均保持不变。76 对分支／分类群限定引物作为补充优化方案保留，不替代原方案。

[主方案 FASTA](sequences/non_partitioned.fasta) · [主方案 CSV](sequences/non_partitioned_pairs.csv) · [原方案预印本](legacy/v1.2/publications/MiUrchin_preprint.pdf)

原方案表格使用原有可评价物种分母；补充分支方案使用筛选后的设计记录面板，两者百分比不能直接互换。这里不宣称两套方案已经湿实验验证。

## 如何选择窗口

选择窗口时，可分别考虑预测覆盖和双端完全匹配。每个基因独立建库，同一窗口的普通与 D 引物使用相同物种比较。

- **16S**：在五个窗口均可评价的 49 个物种中，XLD 覆盖最多（45/49），LD 的双端完全匹配最多（19/49）。在各窗口完整面板中，MD 对 Spatangoida 的覆盖为 0/37，LD 为 36/38。
- **12S**：在 249 bp 的 M 窗口，MD 相比普通 M 将覆盖从 25/69 提高到 61/69，完全匹配从 0 种增至 24 种。允许鸟嘌呤–胸腺嘧啶配对的严格非目标命中从 1 种增至 2 种。
- **COI**：152 bp 的 XSD 覆盖 79/106 种，其中 3 种完全匹配。209 bp 的 SD 覆盖 63/105 种，其中 6 种完全匹配。COI 库有 314 个物种，各保留窗口仅有 103–106 种可评价。本轮 L 和 XL 候选均未通过背景门槛。
- **28S.** 核 28S 的 MD 在 111 个可评价物种中覆盖 108 种，双端完全匹配 72 种。短片段 SD 适合检出海胆，但在 99 个取得条码的物种中，仅 8 种具有独有的内部序列。

## 引物序列与预测表现

FASTA 名称包含基因、方案和方向。例如，`MiUrchin-12S_MD_F` 表示 12S 的 M 窗口简并正向引物。序列均按 5′→3′ 书写。参考跨度按相应基因内部的坐标计算，包含两端引物；内部条码长度仅计算两引物之间的序列。 线粒体使用 NC_001453.1，核 28S 使用 XR_004063668.1。

**读表说明。** “覆盖”和“完全匹配”均为命中物种数 / 该窗口可评价物种数。“严格非目标”栏的两个数依次表示 **仅沃森–克里克配对 / 另允许鸟嘌呤–胸腺嘧啶配对** 下的命中数。例如，0 / 7 表示第一种模型命中 0 条、第二种模型命中 7 条（16S XSD）。

### 16S

非目标背景为 6,045 条参考记录。

| 方案 | F（5′→3′） | R（5′→3′） | 跨度（bp） | 覆盖 | 完全匹配 | 严格非目标 | 碱基匹配图 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| XS | `CTTGTGTATAATGGATTAACGA` | `AAACTAATTTCTTGGGAAAC` | 181 | 19/55 | 0/55 | 0 / 0 | [查看](legacy/v1.2/results/current_primers/XS/base_matching_XS.svg) |
| XSD | `CTTGTGTATAATGGATTRACRA` | `AAACTAATTTCTTGGRRARC` | 181 | 35/55 | 6/55 | 0 / 7 | [查看](legacy/v1.2/results/current_primers/XS/base_matching_XSD.svg) |
| S | `TGTGTATAATGGATTAACGAGA` | `GCTTAGCTAAAACTAATTTCTTGG` | 188 | 13/55 | 2/55 | 0 / 0 | [查看](legacy/v1.2/results/current_primers/S/base_matching_S.svg) |
| SD | `TGTGTATAATGGATTAACRAGH` | `GCTTAGCTTAAACYAATTTCTYGR` | 188 | 29/55 | 3/55 | 0 / 0 | [查看](legacy/v1.2/results/current_primers/S/base_matching_SD.svg) |
| M | `CGTTAGACGAGAAGACCCTG` | `CTTTGATCACCTTAGTGGATCA` | 228 | 85/158 | 12/158 | 0 / 0 | [查看](legacy/v1.2/results/current_primers/M/base_matching_M.svg) |
| MD | `CGTTAGACGAGAAGACCCTR` | `CTTTGATCACCTDARTGGATCA` | 228 | 110/158 | 28/158 | 0 / 0 | [查看](legacy/v1.2/results/current_primers/M/base_matching_MD.svg) |
| L | `GTCTCCTAAATAGAGACTAGTATGAATGGC` | `GCGGTAACTTGTTCCTTTGATCACC` | 343 | 103/159 | 18/159 | 0 / 0 | [查看](legacy/v1.2/results/current_primers/L/base_matching_L.svg) |
| LD | `GTCTCCTAAATAGAGACTAGHATGAATGGC` | `GCGGTAACTTGTTYCTTTGRTCACY` | 343 | 141/159 | 30/159 | 2 / 12 | [查看](legacy/v1.2/results/current_primers/L/base_matching_LD.svg) |
| XL | `GAATAGGCCTAGAAGCAGCC` | `CCGTCTTGCCATTCATACTAGTCTC` | 440 | 41/55 | 9/55 | 2 / 3 | [查看](legacy/v1.2/results/current_primers/XL/base_matching_XL.svg) |
| XLD | `AAGTAGGCCTARAAGCAGCC` | `CCGTCTTGCCATTCATACCAGTCTY` | 440 | 51/55 | 6/55 | 0 / 4 | [查看](legacy/v1.2/results/current_primers/XL/base_matching_XLD.svg) |

### 12S

非目标背景为 459 种棘皮动物，每种取一条代表序列。

| 方案 | F（5′→3′） | R（5′→3′） | 跨度（bp） | 覆盖 | 完全匹配 | 严格非目标 | 碱基匹配图 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| XS | `TGCCACATGCAAGCTTATTAG` | `TTTAGCACTGCAGATGTGG` | 153 | 27/67 | 0/67 | 0 / 0 | [查看](legacy/v1.2/markers/12S_COI/figures/12S_XS.svg) |
| XSD | `TGCCACATGCAAGCYWAYTAG` | `TTTAGCACTGCAGDYGTGG` | 153 | 32/67 | 19/67 | 0 / 0 | [查看](legacy/v1.2/markers/12S_COI/figures/12S_XSD.svg) |
| S | `GTCCTAGTCCCAATTTTAAC` | `AATGTTTAGCACTGCAGTTG` | 188 | 27/64 | 1/64 | 0 / 1 | [查看](legacy/v1.2/markers/12S_COI/figures/12S_S.svg) |
| SD | `GTCCTAGTCCCAAYWTTARC` | `AATGTTTAGCACTGCAGDYG` | 188 | 56/64 | 19/64 | 0 / 1 | [查看](legacy/v1.2/markers/12S_COI/figures/12S_SD.svg) |
| M | `CGGTTTTCCAAACCTCCCT` | `ACTGCTGAATCCAGTTTCT` | 249 | 25/69 | 0/69 | 1 / 1 | [查看](legacy/v1.2/markers/12S_COI/figures/12S_M.svg) |
| MD | `CGGTTTTCCAWAYCTCCCT` | `ACTGCTGAATCCARTTTCN` | 249 | 61/69 | 24/69 | 2 / 2 | [查看](legacy/v1.2/markers/12S_COI/figures/12S_MD.svg) |
| L | `ACCCTGTTATACTTAGACGT` | `GCATTCCAGAGCTCTCTTCA` | 347 | 23/69 | 0/69 | 0 / 0 | [查看](legacy/v1.2/markers/12S_COI/figures/12S_L.svg) |
| LD | `ACCCTGTTATACTTAGMHGT` | `GCATTCCAGAGCTSWYTTCA` | 347 | 56/69 | 17/69 | 0 / 3 | [查看](legacy/v1.2/markers/12S_COI/figures/12S_LD.svg) |
| XL | `CCACATGCAAGCTAACTAGC` | `AAACCGCCAAGTCCTTTGAG` | 452 | 32/67 | 15/67 | 0 / 0 | [查看](legacy/v1.2/markers/12S_COI/figures/12S_XL.svg) |
| XLD | `CCACATGCAAGYYAAYTAGC` | `AAACCGCCAARTCCTTTGAR` | 452 | 40/67 | 21/67 | 2 / 3 | [查看](legacy/v1.2/markers/12S_COI/figures/12S_XLD.svg) |

### COI

非目标背景为 1,719 种棘皮动物，每种取一条代表序列。

| 方案 | F（5′→3′） | R（5′→3′） | 跨度（bp） | 覆盖 | 完全匹配 | 严格非目标 | 碱基匹配图 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| XS | `TCAAACCTACAATGAGAAAC` | `ACATAGTGGAAGTGAGCTAC` | 152 | 34/106 | 0/106 | 0 / 1 | [查看](legacy/v1.2/markers/12S_COI/figures/COI_XS.svg) |
| XSD | `TCAAACCTACARTGRGARAC` | `ACATAGTGGAAGTGDGCWAC` | 152 | 79/106 | 3/106 | 0 / 1 | [查看](legacy/v1.2/markers/12S_COI/figures/COI_XSD.svg) |
| S | `CAAGGATCAAACCTACAATG` | `AATCAGTGAGTAAATCCTGC` | 209 | 28/105 | 3/105 | 0 / 0 | [查看](legacy/v1.2/markers/12S_COI/figures/COI_S.svg) |
| SD | `CAAGGATCAAAYYTACARTG` | `AATCAGTGAGTRAAYCCWGC` | 209 | 63/105 | 6/105 | 1 / 1 | [查看](legacy/v1.2/markers/12S_COI/figures/COI_SD.svg) |
| M | `TCAAACCTACAATGGGAAAC` | `ACCTTTCCTCATAGTGGGTG` | 248 | 22/103 | 0/103 | 0 / 0 | [查看](legacy/v1.2/markers/12S_COI/figures/COI_M.svg) |
| MD | `TCAAACCTACARTGRGARAC` | `ACCTTTCCTCAWAGYGGRTG` | 248 | 57/103 | 1/103 | 0 / 0 | [查看](legacy/v1.2/markers/12S_COI/figures/COI_MD.svg) |

### 28S

28S 面板按 122 个海胆双名各取一条序列，依据目标模板的变异在引物后半段加入简并位点。832 条非目标序列包含其他四纲棘皮动物和常见海洋动物。海参仅有 3–4 条序列完整覆盖各窗口两端。匹配图显示全部 122 条模板，NA 表示不可评价。

| 方案 | F（5′→3′） | R（5′→3′） | 跨度（bp） | 覆盖 | 完全匹配 | 严格非目标 | 碱基匹配图 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S | `GCCTGGAGCCACCAAGAGTC` | `TTGTCTGCTATCGGTCTCGT` | 102 | 99/101 | 78/101 | 0 / 0 | [碱基匹配](legacy/v1.2/markers/28S/figures/S.svg) |
| SD | `GCCTGGAGCCRCCAAGARTC` | `TTGTCTGCTATCGGTCTCGT` | 102 | 99/101 | 83/101 | 0 / 0 | [碱基匹配](legacy/v1.2/markers/28S/figures/SD.svg) |
| M | `AAGAGCCCATCGCTGAATCC` | `CCGACTCTTGGTGGCTCCAG` | 176 | 104/111 | 49/111 | 0 / 1 | [碱基匹配](legacy/v1.2/markers/28S/figures/M.svg) |
| MD | `AAGAGCCCATCGCYGAATCS` | `CCGACTCTTGGYGRCTCCMG` | 176 | 108/111 | 72/111 | 0 / 2 | [碱基匹配](legacy/v1.2/markers/28S/figures/MD.svg) |
| L | `AAGCTGGGCGCCTGCTCGAC` | `AATCGCTGCGGACCTCCACC` | 282 | 88/91 | 82/91 | 0 / 0 | [碱基匹配](legacy/v1.2/markers/28S/figures/L.svg) |
| LD | `AAGCTGGGCGCCTGYTCGAC` | `AATCGCTGCGGACCTCCACC` | 282 | 89/91 | 82/91 | 0 / 0 | [碱基匹配](legacy/v1.2/markers/28S/figures/LD.svg) |

[16S CSV](legacy/v1.2/results/current_primers/comparison.csv) · [12S / COI CSV](legacy/v1.2/markers/12S_COI/candidates.csv) · [28S CSV](legacy/v1.2/markers/28S/selected.csv)


## 补充：分支／分类群优化方案

[分支优化预印本](publications/MiUrchin_preprint.pdf) · [分支证据清单](results/catalog.json)

<details>
<summary>展开 76 对补充分支引物及方法说明</summary>

## 如何选择窗口

先选择适用分类群，再选择基因和原方案。优先方案在两种浓度下的结构温度余量均至少为 5°C；条件备选需要进一步评估。32 组原方案不再意味着普通／D引物具有相同坐标或包含关系。

## 引物序列与预测表现

序列均按 5′→3′ 书写。“覆盖”和“完全匹配”为各行设计面板的参考记录数；“严格非目标”为 WC / GT 两种模型的计数。面板内计算匹配不等于实验检出率。

### 16S

| 方案／分类群 | 分级 | F（5′→3′） | R（5′→3′） | 覆盖 | 完全匹配 | 严格非目标 |
| --- | --- | --- | --- | --- | --- | --- |
| L / Arbacioida | 优先 | `GTCTCCTAAATAGAGACTAGTATGAATGGC` | `GCGGTAACTTTTTCCTTTAATCGCC` | 4/4 | 2/4 | 0 / 0 |
| LD / Aulodonta | 优先 | `GTCTCCTAAATAGAGACTAGCATGAATGGC` | `GCGGTAACTTTTTCCTTTGATCAYC` | 15/15 | 0/15 | 0 / 0 |
| LD / Cidaroidea | 优先 | `TCTCCTAAATAGAGACTAGYATGAAYGGC` | `GCGGTAACTTRTTCYTTTGATCAYC` | 10/10 | 10/10 | 0 / 0 |
| LD / Arbacioida | 优先 | `GTCTCCTAAATAGAGACTAGTATGAATGGC` | `GCGGTAACTTDTTCCTTTRATCGCC` | 4/4 | 4/4 | 0 / 0 |
| M / Clypeasteroida | 优先 | `GCCAGACGAGAAGACCCTG` | `CTTTGATCACCTAAGTGGATCA` | 4/4 | 2/4 | 0 / 0 |
| MD / Irregularia | 条件备选 | `CGYYAGACGAGAAGACCCTR` | `CTTTGATCACCDDRGTGGATCA` | 29/29 | 27/29 | 0 / 0 |
| MD / Aulodonta | 条件备选 | `CGYYAGACGAGAAGACCCTR` | `YTTTGATCACCKDRRTGGATCA` | 15/15 | 13/15 | 0 / 0 |
| S / Diadematoida | 优先 | `TGTGTATAATGGATTGACTAGA` | `GGCTAAGACCAATTTCTCGG` | 4/4 | 2/4 | 0 / 0 |
| SD / Camarodonta | 优先 | `GTGTATAATGGATTAACRAGH` | `TTAGCTYARACTAATTTYTYGG` | 28/28 | 14/28 | 0 / 0 |
| SD / Diadematoida | 优先 | `TGTGTATAATGGATTRACTAGA` | `GCTAAGACCAATTTCTCGG` | 4/4 | 4/4 | 0 / 0 |
| SD / Cidaroidea | 优先 | `GTGTATAATGGATTAGCAAGA` | `GGCTTAGACCAATTTTRCRA` | 3/3 | 3/3 | 0 / 0 |
| SD / Echinothurioida | 优先 | `TGTGTATAATGGATTAACAAGW` | `GCTTAGCTTAGACTAATTTCTYRR` | 3/3 | 0/3 | 0 / 0 |
| XS / Holasteroida | 优先 | `CTCGTGTATAATGGATTAACAA` | `AAGCTAATTTTTTGGGGAAC` | 6/6 | 2/6 | 0 / 0 |
| XSD / Diadematoida | 优先 | `CTTGTGTATAATGGATTRACTA` | `ACCAATTTCTCGGYGAAC` | 4/4 | 4/4 | 0 / 2 |
| XL / Diadematoida | 优先 | `GGCCTAGAAGCAGCCACTTCAG` | `CCCGTCTTGCCATTCATGCCAGTCTC` | 4/4 | 3/4 | 0 / 0 |
| XL / Cidaroidea | 优先 | `CCAAGTAGGCCTAGAAGCAGC` | `GACAGTTTAGTTCCGTCTTGCC` | 3/3 | 2/3 | 0 / 2 |
| XLD / Irregularia | 优先 | `GTAGGCCTARAAGCAGCCRACTWW` | `GYTCCGTCTTGCCATTCATDCCAGTC` | 11/11 | 10/11 | 0 / 0 |
| XLD / Diadematoida | 优先 | `GGCCYAGAAGCAGCCACTTCAGH` | `CCCCGTCTTGCCATTCATGCCAGTCTC` | 4/4 | 4/4 | 0 / 0 |
| XLD / Cidaroidea | 优先 | `GCCYAGAAGCAGCCAACYT` | `GACAGTTTAGTTCCGTCTTGCCRTT` | 3/3 | 3/3 | 0 / 0 |

### 12S

| 方案／分类群 | 分级 | F（5′→3′） | R（5′→3′） | 覆盖 | 完全匹配 | 严格非目标 |
| --- | --- | --- | --- | --- | --- | --- |
| LD / Holasteroida | 条件备选 | `ACCCTGYTATACTTAGMYGT` | `GTATTCCAGAGCTSTYTTCA` | 18/18 | 18/18 | 0 / 1 |
| LD / Clypeasteroida | 优先 | `ACCCTGCTATACTCAGAMGT` | `GCATTYCAGAGCTCTYTTCA` | 3/3 | 3/3 | 0 / 0 |
| LD / Cidaroidea | 条件备选 | `ACCCTGTTATACTTAGCCGT` | `GCATYCCAGAGCTRRCTTCA` | 3/3 | 3/3 | 0 / 1 |
| M / Diadematoida | 优先 | `CGGTTTTCCATATCTACCT` | `ACTACTGAATCCGATTTCA` | 4/4 | 3/4 | 0 / 0 |
| M / Cidaroidea | 条件备选 | `CGGTTTCCCAAACCTACCT` | `ACTGCTGAATCCAGTTTCA` | 3/3 | 2/3 | 0 / 0 |
| MD / Diadematoida | 优先 | `CGGTTTTCCAWATCTACCT` | `ACTACTGAATCCGRTTTCA` | 4/4 | 4/4 | 0 / 0 |
| MD / Cidaroidea | 条件备选 | `CGGTTTCCCAAAYCTACCT` | `ACTGCTGAATCCAGTTTCA` | 3/3 | 3/3 | 0 / 0 |
| SD / Aulodonta | 优先 | `GTCCTAGTCCCAACTTTARC` | `AATGTTTAGCACTGCAGWYG` | 10/10 | 3/10 | 0 / 1 |
| SD / Cidaroidea | 优先 | `GTCCTAGTCCCGATCTTAAC` | `AATGTTTAGCACTGCAGRTG` | 3/3 | 2/3 | 0 / 0 |
| XL / Echinothurioida | 优先 | `CCACATGCAAGCTAACTAGC` | `AAACCGCCAAGTCCTTTGAG` | 3/3 | 2/3 | 0 / 0 |
| XLD / Echinothurioida | 优先 | `CCACATGCAAGYYAACTAGC` | `AAACCGCCAAGTCCTTTGAG` | 3/3 | 3/3 | 1 / 1 |
| XSD / Echinothurioida | 条件备选 | `TGCCACATGCAAGYYAACTAG` | `TYTAGCACTGCAGWTGTGR` | 3/3 | 3/3 | 0 / 0 |
| L / Holasteroida | 优先 | `GATTAGATACCCTGCTATACTTAG` | `CGTATTCCAGAGCTGTCTTCA` | 18/18 | 8/18 | 0 / 0 |
| L / Cidaroidea | 优先 | `GATACCCTGTTATACTTAGCCGTAAAC` | `GAGTGACGGGCGATGTGTACG` | 3/3 | 3/3 | 0 / 0 |
| S / Irregularia | 优先 | `CCGATTTGGTCCTAGTCCC` | `TCTAATGTTTAGCACTGCAGT` | 19/19 | 11/19 | 0 / 0 |
| S / Temnopleuroida | 优先 | `CGATTTGGTCCTAGTCCC` | `CACTGCAGTTGTGGCGTAT` | 11/11 | 7/11 | 0 / 0 |
| S / Diadematoida | 优先 | `GTCCCAACTTTAACTAGCT` | `AATGTTTAGCACTGCAGA` | 4/4 | 3/4 | 0 / 0 |
| S / Cidaroidea | 优先 | `CGATTTGGTCCTAGTCCCGATCTTAAC` | `CTCTAATTGTCTAATGTTTAGCACTGC` | 3/3 | 2/3 | 0 / 0 |
| S / Echinothurioida | 优先 | `CCGATTTGGTCCTAGTCCCA` | `CCTGATTGTCTAATGTTTAGCACTGC` | 3/3 | 1/3 | 0 / 0 |
| XS / Holasteroida | 优先 | `GCCACATGCAAGCTAACTAGC` | `TCTAATGTTTAGCACTGCAGT` | 16/16 | 8/16 | 0 / 0 |
| XS / Diadematoida | 优先 | `AACTAGCAAACCAGTGAAGT` | `CCCTAATTGTCCAATGTTTAGCACT` | 4/4 | 3/4 | 0 / 0 |
| XS / Echinothurioida | 优先 | `CCACATGCAAGCTAACTAG` | `CCTGATTGTCTAATGTTTAGCACTG` | 3/3 | 1/3 | 0 / 0 |

### COI

| 方案／分类群 | 分级 | F（5′→3′） | R（5′→3′） | 覆盖 | 完全匹配 | 严格非目标 |
| --- | --- | --- | --- | --- | --- | --- |
| MD / Cidaroidea | 条件备选 | `TCAAACCTTCAATGAGARAC` | `ACCTTTCTTCABAGDGGGTG` | 7/7 | 2/7 | 0 / 0 |
| SD / Cidaroidea | 条件备选 | `CARGGVTCAAAYCTYCAATG` | `AATCARTGWGARAAYCCDGC` | 7/7 | 5/7 | 0 / 1 |
| SD / Echinothurioida | 优先 | `CAAGGGTCYAAYCTRCARTG` | `AATCAGTGGGTRAAKCCDGC` | 3/3 | 1/3 | 0 / 0 |
| XSD / Cidaroidea | 条件备选 | `TCAAACCTTCAATGAGARAC` | `CRTAGTGRAAGTGGGCHAC` | 7/7 | 2/7 | 0 / 0 |
| XSD / Echinothurioida | 优先 | `TCTAACCTACAATGAGARAC` | `ACGTAATGAAAGTGTGCWAC` | 3/3 | 0/3 | 0 / 0 |
| M / Cidaroidea | 优先 | `AGGATCAAACCTTCAATG` | `CCTTTCTTCATAGAGGGTG` | 7/7 | 0/7 | 0 / 0 |
| XS / Echinothurioida | 优先 | `GTCTAACCTACAATGAGA` | `CTACATAGTAAGTGTCGTGA` | 3/3 | 0/3 | 0 / 0 |
| S / Holasteroida | 优先 | `TCAAACCTCCAATGAGAAAC` | `GCCAAATACAGCACCCAT` | 6/6 | 2/6 | 0 / 0 |
| S / genus_Lytechinus | 优先 | `TTCAGATGAATGGCCACACTACAAGG` | `GCGGGTGTAGGCTGTATCC` | 5/5 | 4/5 | 0 / 0 |
| S / genus_Echinometra | 优先 | `ATGGCAACCCTTCAAGGCTCAAA` | `AGTGGGTGTAGGTTGTATCCAGAGAAT` | 4/4 | 3/4 | 0 / 0 |
| S / genus_Clypeaster | 优先 | `TCAAACCTTCAATGAGAAAC` | `ACAGCTCCCATGGATAGT` | 4/4 | 2/4 | 0 / 0 |
| S / genus_Temnopleurus | 优先 | `TCCAACAGGAATTAAGGT` | `CTTCATAGGGGGTGTAAACTATA` | 3/3 | 1/3 | 0 / 0 |

### 28S

| 方案／分类群 | 分级 | F（5′→3′） | R（5′→3′） | 覆盖 | 完全匹配 | 严格非目标 |
| --- | --- | --- | --- | --- | --- | --- |
| L / Echinacea | 优先 | `AAGCTGGGCGCCTGCTCGAC` | `AATCGCTGCGGACCTCCACC` | 12/12 | 12/12 | 0 / 0 |
| L / Aulodonta | 优先 | `AAGCTGGGCGCCTGCTCGAC` | `AATCGCTGCGGACCTCCACC` | 9/9 | 8/9 | 0 / 0 |
| L / Clypeasteroida | 优先 | `AAGCTGGGCGCCTGCTCGAC` | `AATCGCTGCGGACCTCCACC` | 5/5 | 5/5 | 0 / 0 |
| L / Cidaroidea | 优先 | `AAGCTGGGCGCCTGCTCGAC` | `AATCGCTGCGGACCTCCACC` | 3/3 | 3/3 | 0 / 0 |
| LD / Echinacea | 优先 | `AAGCTGGGCGCCTGCTCGAC` | `AATCGCTGCGGACCTCCACC` | 12/12 | 12/12 | 0 / 0 |
| LD / Aulodonta | 优先 | `AAGCTGGGCGCCTGCTCGAC` | `AATCGCTGCGGACCTCCACC` | 9/9 | 8/9 | 0 / 0 |
| LD / Clypeasteroida | 优先 | `AAGCTGGGCGCCTGCTCGAC` | `AATCGCTGCGGACCTCCACC` | 5/5 | 5/5 | 0 / 0 |
| LD / Cidaroidea | 优先 | `AAGCTGGGCGCCTGCTCGAC` | `AATCGCTGCGGACCTCCACC` | 3/3 | 3/3 | 0 / 0 |
| M / Echinacea | 优先 | `AAGAGCCCATCGCCGAATCC` | `CCGACTCTTGGTGGCTCCAG` | 12/12 | 9/12 | 0 / 1 |
| M / Holasteroida | 优先 | `AAGAGCCCATCGCTGAATCC` | `CCGACTCTTGGTGGCTCCAG` | 11/11 | 9/11 | 0 / 1 |
| M / Diadematoida | 优先 | `AAGAGCCCATCGCCGAATCC` | `CCGACTCTTGGCGGCTCCAG` | 6/6 | 4/6 | 0 / 1 |
| M / Clypeasteroida | 优先 | `AATAGCCCATCGCTGAATCC` | `CCGACTCTTGGTGGCTCCAG` | 5/5 | 3/5 | 0 / 1 |
| MD / Cidaroidea | 优先 | `AAGAGCCCATCGCTGAATCC` | `CCGACTCTTGGTGGCTCCMR` | 17/17 | 15/17 | 0 / 2 |
| MD / Echinacea | 优先 | `AWRAGCCCATCGCCGAATCC` | `CYGACTCTTGGTGRCTCCAG` | 12/12 | 12/12 | 0 / 1 |
| MD / Holasteroida | 条件备选 | `AAGAGCCYATCGCYGAATCC` | `CCGACTCTTGGTGGCTCCAG` | 11/11 | 11/11 | 0 / 1 |
| MD / Diadematoida | 优先 | `AAGAGCCCAKCGCYGAATCC` | `CCGACTCTTGGYGGCTCCAG` | 6/6 | 6/6 | 0 / 1 |
| MD / Clypeasteroida | 优先 | `AAKAGCCCATCGCTGAATCC` | `CCGACTCTTGGTGGCTCCAG` | 5/5 | 5/5 | 0 / 1 |
| S / Irregularia | 优先 | `GCCTGGAGCCACCAAGAGTC` | `TTGTCTGCTATCGGTCTCGT` | 40/40 | 35/40 | 0 / 0 |
| S / Echinacea | 优先 | `GCCTGGAGCCACCAAGAGTC` | `TTGTCTGCTATCGGTCTCGT` | 12/12 | 10/12 | 0 / 0 |
| S / Diadematoida | 优先 | `CCTGGAGCCGCCAAGAGTC` | `TTGTCTGCTATCGGTCTCGT` | 6/6 | 5/6 | 0 / 0 |
| SD / Irregularia | 优先 | `GCCTGGAGCCACCAAGAGTC` | `TTGTCTGCTATCGGTCTCGT` | 40/40 | 35/40 | 0 / 0 |
| SD / Echinacea | 优先 | `GCCTGGAGYCACCAAGAGTC` | `TTGTCTGCTATCGGTCTCGT` | 12/12 | 12/12 | 0 / 0 |
| SD / Aulodonta | 优先 | `CCTGGARCCRCCRWGAGTC` | `TTGTCTGCTATCGGTCTCGT` | 9/9 | 8/9 | 0 / 0 |

[CSV](sequences/primer_pairs.csv) · [FASTA](sequences/all_markers.fasta) · [Priority FASTA](sequences/priority.fasta) · [Conditional FASTA](sequences/conditional.fasta)

## 结合位置与逐碱基匹配

移动后的结合位置依各自参考记录核验。详见[完整证据清单](results/catalog.json)与[原版／新版比较](report.html)；历史坐标和匹配图不作为新引物的结果。

![Exact comparison](figures/exact_comparison.svg)

## 参考面板与筛选规则

双端最后三位须严格 WC 匹配，每端总错配最多两处；四项非目标计数不得高于原引物。全部简并变体在两种浓度下检查结构。[中文方法](docs/METHODS.zh-CN.md) · [重现说明](docs/REPRODUCIBILITY.zh-CN.md)。

## 16S 补充评价

[历史 v1.2](legacy/v1.2/README.zh-CN.md)保留旧版共同面板、留出与条码分析，不用于验证新序列。目前尚无独立留出或湿实验验证。子引物不可直接混合，交叉配对仍可命中非目标。

## 引用与著作权

[CITATION.cff](CITATION.cff) · [BibTeX](CITATION.bib) · [COPYRIGHT](COPYRIGHT.md)

## 参考文献

[MiFish](https://doi.org/10.1098/rsos.150088) · [Anth-28S](https://doi.org/10.7717/peerj.18607) · [Echinoid phylogenomics](https://doi.org/10.7554/eLife.72460)

</details>
