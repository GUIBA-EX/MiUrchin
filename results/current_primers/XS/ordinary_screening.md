# XS ordinary-primer screen / 普通 XS 引物筛选

Fixed reference positions are NC_001453.1 F 183–204 and R 344–363. The ordinary XS and XSD share these endpoints; their 181 bp reference span includes both primers. The ordinary pair is a concrete variant of XSD.

| Candidate | F (5′→3′) | R (5′→3′) | Coverage | Exact | Strict WC / GT | WC≤3 / GT≤2 |
|---|---|---|---:|---:|---:|---:|
| XS, coverage priority | `CTTGTGTATAATGGATTAACGA` | `AAACTAATTTCTTGGGAAAC` | 19/55 | 0/55 | 0 / 0 | 0 / 0 |
| Alternative, exact priority | `CTCGTGTATAATGGATTAACGA` | `AAACTAATTTCTTGGGGAAC` | 16/55 | 1/55 | 0 / 0 | 0 / 0 |
| XSD | `CTTGTGTATAATGGATTRACRA` | `AAACTAATTTCTTGGRRARC` | 35/55 | 6/55 | 0 / 7 | 19 / 7 |

The ordinary candidate was selected for coverage of the species-rich order Camarodonta (19/28). All 19 covered species are also covered by XSD, which covers 25/28 Camarodonta and 10 species in other orders. The ordinary candidate has no exact pair match; the single exact match in the alternative costs three covered species. These are in-silico predictions and do not establish amplification efficiency.

以参考碱基为基础，枚举每条引物最多两个替换，末端 3 nt 与参考一致，并筛除不符合末端条件的序列；共评估 1,592 条正向及 536 条反向序列。按覆盖、完全匹配和目级覆盖保留候选、组合并按实际参考结合位置和结构筛查，82 对进入全序列非目标扫描。此有限搜索并不证明不存在更好的引物。目标覆盖按每条引物最多两个错配且末端 3 nt 兼容计算；55 是可评价物种数，并非全部 165 物种。非目标数为 6,045 条参考记录中的预测命中，不是实际 PCR 次数。所选方案经 C++ 与独立 Python 原始序列扫描核对。

MiFish 以多物种比对寻找两侧保守区和中间变异区，并比较目标类群；本次借鉴其思路，在海胆 16S 区域内固定引物窗口，并加入 3′ 端与非目标筛查。MiFish 原论文研究的是鱼类 12S，不能将其表现直接等同于本候选。[Miya et al. 2015](https://doi.org/10.1098/rsos.150088)
