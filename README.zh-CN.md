![MiUrchin](figures/MiUrchin_overview.png)

# MiUrchin

[English](README.md)

## 摘要

海胆环境 DNA 线粒体 16S rRNA 引物，包含 XS、S、M、L、XL 五个长度。每个长度保留普通单对和简并单对 D；同一长度使用相同参考坐标。
参考面板包含 165 个物种，XS、S、M、L、XL 区域分别有 55、55、158、159、55 个可评价物种；缺失结合区域不计为漏检。图示使用旧分类体系，新面板的目级名称以 WoRMS 为准。

在 55 个物种的 XS 面板中，XS 和 XSD 分别覆盖 19 和 35 个物种，完全匹配数分别为 0 和 6；其特异性和扩增表现仍需实验验证。

## 引言

海胆环境 DNA 宏条形码引物需要兼顾目标类群覆盖、结合兼容性和非目标扩增。MiUrchin 比较五个线粒体 16S 窗口，每个窗口均包含共享参考坐标的普通和简并引物。 海洋环境 DNA 宏条形码研究显示，标记和参考数据库的选择会影响检测结果（Gold 等，2022）；MiFish 则提供了基于序列比对设计鱼类引物的实例（Miya 等，2015）。线粒体标记也曾用于调查营养关系样品中的海胆 DNA（Sutera 等，2025）。

[参考面板 / Reference panel](results/species_qc/panel.csv) · [审核 / Reference curation](results/species_qc/README.md)

![Reference binding positions](figures/amplicon_regions.zh.svg)

## 方法

### 参考数据与序列比对

目标数据库包含 1,401 条海胆线粒体序列，非目标数据库包含 6,045 条参考记录。经序列质量和分类审核，每个可确认物种保留一条代表，共 165 个物种。代表序列依据结合窗口完整性、模糊碱基和参考位点覆盖情况选择，不以引物匹配结果为筛选依据。保留序列使用 MAFFT 7.526（Katoh & Standley，2013）重新比对，参考坐标采用去除空位的线粒体 16S rRNA 序列 NC_001453.1，从 1 开始计数。清理后的物种面板中，正、反向窗口均需跨越参考区域，A/C/G/T 数量达到参考位点数的 90% 且无模糊碱基，允许比对空位；符合条件的物种才纳入该窗口的评价分母。可评价物种数为 XS、S、M、L、XL 分别为 55、55、158、159、55 个。缺失窗口不计为漏检，筛选标准及 accession 记录见[参考序列审核](results/species_qc/README.md)。

### 引物设计与筛选

在固定的正、反向参考窗口内比较普通和简并候选。S–XL 每个长度的普通引物与 D 引物使用相同参考起止坐标。每条 D 引物最多包含 8 种具体序列，IUPAC 简并碱基限于 3′ 半段。末端筛查排除末端三连和超过 4 bp 的同聚物，要求末端 3 nt 至少含一个 G 或 C。Primer3（Untergasser 等，2012）计算采用单价盐 50 mM、Mg²⁺ 1.5 mM、dNTP 0.6 mM，分别评估每变体 50 nM 和每方向总浓度 200 nM 两种情景。S–XL 的结构筛查要求预测结构最高 Tm 低于 55 °C，正、反向双链 Tm 区间中点之差不超过 5 °C。XS 与 XSD 在参考序列上的实际结合坐标均为 F 183–204、R 344–363。普通 XS 搜索在参考结合序列附近枚举碱基替换，固定与参考一致的末端 3 nt，并筛查目标匹配、末端性质、引物结构与非目标命中。XS 目标扫描要求产物长 70–500 bp，双引物之间的内部长度至少 20 bp。

### 计算评价

预测覆盖要求每条引物最多 2 个错配，且末端 3 nt 与模板按 IUPAC 规则兼容；完全匹配要求两个结合位点均无错配。S–XL 目标双引物扫描要求产物长 150–500 bp、双引物之间的内部长度至少 50 bp；非目标扫描允许内部距离 0–1,000 bp。严格 Watson–Crick（WC）和 G–T 模型保留末端约束；WC≤3 和 GT≤2 为不施加末端约束的宽松筛查。覆盖率和完全匹配率对可评价物种等权，并分别汇总各目结果；非目标数字为参考记录数。使用 C++ 与 Python 对同一参考数据的目标及严格非目标命中集合进行独立算法复核。结果为计算预测，仍需实验验证。

[详细方法](docs/METHODS.zh-CN.md) · [验证](docs/VALIDATION.md)

## 结果

### 预测表现

| Name | Coverage | Exact | Strict WC / GT | WC≤3 / GT≤2 |
|---|---:|---:|---:|---:|
| XS | 19/55 (34.55%) | 0/55 (0%) | 0 / 0 | 0 / 0 |
| XSD | 35/55 (63.64%) | 6/55 (10.91%) | 0 / 7 | 19 / 7 |
| S | 13/55 (23.64%) | 2/55 (3.64%) | 0 / 0 | 0 / 0 |
| SD | 29/55 (52.73%) | 3/55 (5.45%) | 0 / 0 | 3 / 0 |
| M | 85/158 (53.80%) | 12/158 (7.59%) | 0 / 0 | 0 / 0 |
| MD | 110/158 (69.62%) | 28/158 (17.72%) | 0 / 0 | 0 / 0 |
| L | 103/159 (64.78%) | 18/159 (11.32%) | 0 / 0 | 2 / 1 |
| LD | 141/159 (88.68%) | 30/159 (18.87%) | 2 / 12 | 12 / 12 |
| XL | 41/55 (74.55%) | 9/55 (16.36%) | 2 / 3 | 3 / 5 |
| XLD | 51/55 (92.73%) | 6/55 (10.91%) | 0 / 4 | 6 / 6 |

覆盖要求每条引物最多 2 个错配且末端 3 nt 兼容；完全匹配要求两条引物零错配。严格 WC/GT 使用末端约束；WC≤3 / GT≤2 是不施加末端约束的非目标筛查。

简并引物每条最多 8 个具体变体，简并位点限于 3′ 半段。结果为计算预测，仍需实验验证。

### XS

| Name | F (5′→3′) | R (5′→3′) |
|---|---|---|
| XS | `CTTGTGTATAATGGATTAACGA` | `AAACTAATTTCTTGGGAAAC` |
| XSD | `CTTGTGTATAATGGATTRACRA` | `AAACTAATTTCTTGGRRARC` |

两对引物在 NC_001453.1 上均结合于 F 183–204、R 344–363，参考扩增区间为 181 bp，比 S 短 7 bp。普通 XS 在 55 个可评价物种中没有正反引物均完全匹配的物种；其预测覆盖允许错配。XSD 反向引物倒数第 4 位使用 R（A/G），覆盖率更高。非目标数字为参考序列记录数。

![XS base matching](results/current_primers/XS/base_matching_XS.svg)

![XSD base matching](results/current_primers/XS/base_matching_XSD.svg)

[XS 各目匹配](results/current_primers/XS/XS_by_order.csv) · [XS 各物种匹配](results/current_primers/XS/XS_by_taxon.csv) · [XSD 各目匹配](results/current_primers/XS/XSD_by_order.csv) · [XSD 各物种匹配](results/current_primers/XS/XSD_by_taxon.csv) · [普通候选比较](results/current_primers/XS/ordinary_screening.md)

### S

| Name | F (5′→3′) | R (5′→3′) |
|---|---|---|
| S | `TGTGTATAATGGATTAACGAGA` | `GCTTAGCTAAAACTAATTTCTTGG` |
| SD | `TGTGTATAATGGATTAACRAGH` | `GCTTAGCTTAAACYAATTTCTYGR` |

![S base matching](results/current_primers/S/base_matching_S.svg)

![SD base matching](results/current_primers/S/base_matching_SD.svg)

[S 各目匹配](results/current_primers/S/SD_by_order.csv) · [S 各物种匹配](results/current_primers/S/SD_by_taxon.csv)

### M

| Name | F (5′→3′) | R (5′→3′) |
|---|---|---|
| M | `CGTTAGACGAGAAGACCCTG` | `CTTTGATCACCTTAGTGGATCA` |
| MD | `CGTTAGACGAGAAGACCCTR` | `CTTTGATCACCTDARTGGATCA` |

![M base matching](results/current_primers/M/base_matching_M.svg)

![MD base matching](results/current_primers/M/base_matching_MD.svg)

[M 各目匹配](results/current_primers/M/MD_by_order.csv) · [M 各物种匹配](results/current_primers/M/MD_by_taxon.csv)

### L

| Name | F (5′→3′) | R (5′→3′) |
|---|---|---|
| L | `GTCTCCTAAATAGAGACTAGTATGAATGGC` | `GCGGTAACTTGTTCCTTTGATCACC` |
| LD | `GTCTCCTAAATAGAGACTAGHATGAATGGC` | `GCGGTAACTTGTTYCTTTGRTCACY` |

![L base matching](results/current_primers/L/base_matching_L.svg)

![LD base matching](results/current_primers/L/base_matching_LD.svg)

[L 各目匹配](results/current_primers/L/LD_by_order.csv) · [L 各物种匹配](results/current_primers/L/LD_by_taxon.csv)

### XL

| Name | F (5′→3′) | R (5′→3′) |
|---|---|---|
| XL | `GAATAGGCCTAGAAGCAGCC` | `CCGTCTTGCCATTCATACTAGTCTC` |
| XLD | `AAGTAGGCCTARAAGCAGCC` | `CCGTCTTGCCATTCATACCAGTCTY` |

![XL base matching](results/current_primers/XL/base_matching_XL.svg)

![XLD base matching](results/current_primers/XL/base_matching_XLD.svg)

[XL 各目匹配](results/current_primers/XL/XLD_by_order.csv) · [XL 各物种匹配](results/current_primers/XL/XLD_by_taxon.csv)

## 讨论

XS 和 XSD 的参考扩增区间均为 181 bp，但预测匹配不同：XS 覆盖 19/55 个可评价物种且无完全匹配，XSD 覆盖 35/55 个，其中 6 个完全匹配，并有 7 条严格 G–T 非目标记录。XSD 以更多非目标命中换取较高预测覆盖。上述结果基于有限参考面板，不能直接推断实验扩增或环境样品检出情况。

[Copyright / 著作权](COPYRIGHT.md)

## 参考文献

1. Gold, Z., Wall, A. R., Schweizer, T. M., et al. (2022). A manager’s guide to using eDNA metabarcoding in marine ecosystems. *PeerJ*, 10, e14071. https://doi.org/10.7717/peerj.14071

2. Miya, M., Sato, Y., Fukunaga, T., et al. (2015). MiFish, a set of universal PCR primers for metabarcoding environmental DNA from fishes: detection of more than 230 subtropical marine species. *Royal Society Open Science*, 2, 150088. https://doi.org/10.1098/rsos.150088

3. Sutera, A., Bonaviri, C., Di Trapani, F., et al. (2025). Unravelling hidden trophic interactions among sea urchin juveniles and macroinvertebrates by DNA amplification. *Molecular Ecology*, 34, e70163. https://doi.org/10.1111/mec.70163

4. Katoh, K., & Standley, D. M. (2013). MAFFT multiple sequence alignment software version 7: improvements in performance and usability. *Molecular Biology and Evolution*, 30, 772–780. https://doi.org/10.1093/molbev/mst010

5. Untergasser, A., Cutcutache, I., Koressaar, T., et al. (2012). Primer3—new capabilities and interfaces. *Nucleic Acids Research*, 40, e115. https://doi.org/10.1093/nar/gks596
