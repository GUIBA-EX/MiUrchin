# MiUrchin · 仅3′半段简并、每引物≤8变体

> 历史分析记录；当前引物、指标与验证见 [中文 README](../README.zh-CN.md)、[English README](../README.md) 和 [VALIDATION](VALIDATION.md)。 / Historical analysis; see the linked current README and validation.

计算设计与复核记录，2026-10-28。候选用于研究和实验验证，四个D单对已选为当前方案。

## 设计要求和搜索范围

正反引物分别计算 IUPAC 理论变体数，均≤8；仅引物 5′→3′ 序列的后半段允许简并，前半段为 A/C/G/T。奇数长度时后半段多一个碱基。S/M/L/XL 的 F、R 长度和 NC_001453.1 端点与各自正式普通、A、B、D 引物一致。正式 D 基准仅用于比较，不强制满足此次新条件。

借鉴 Anth-28S 在有证据的谱系变异处使用简并，而非复制其序列或声称本次完成 95% 共识筛选。参考面板和旧候选的具体变体作为种子，在相同 5′ 半段前提下合并可观察的 3′ 半段变异，允许末端简并，同时保留无末端同聚三联、末端3 nt至少1个GC、末端5 nt为1–4 GC、无超过4 nt同聚物的现行规则。经排序和按目保留 869 条引物、47,638 组配对。

先按目间覆盖、目间完全匹配、标签覆盖、较低简并度排序；各长度逐一背景复核前1000个候选，另补充最多200个低简并候选，去重后共4,270组。严格 WC/GT 各≤20，宽松 WC3/GT2 分20/50/100条档；入选引物未加接头的所有具体变体通过 Primer3 两种浓度情景下发卡/二聚体 Tm<55°C、双端Tm范围中点差≤5°C。S/M另保留严格背景20档内完全匹配优先候选。计算搜索有候选和排序截断，不代表全局最优。

共同面板 80 条参考、49 名称标签、11 个 WoRMS 目；目标原库1,401条、背景6,045条。覆盖为两端各≤2错配且末端3 nt兼容；完全匹配两端零错配。先按目计算至少一条参考命中的标签比例，再对目等权。严格背景 WC/GT 使用2错配与末端约束；宽松WC3/GT2不限定末端。背景数为记录数，不能视作实测扩增比例。

## 基准与新候选

| 方案 | 目间覆盖% | 目间完全匹配% | 覆盖标签 | 完全匹配标签 | F/R简并度 | 严格WC/GT | 宽松WC3/GT2 |
|---|---:|---:|---:|---:|---:|---:|---:|
| SD 正式基准 | 64.18 | 20.78 | 38/49 | 11/49 | 108/108 | 0/0 | 4/0 |
| S-3P8-20 | 43.83 | 0.32 | 29/49 | 1/49 | 6/6 | 0/0 | 0/0 |
| S-3P8-exact | 37.45 | 9.09 | 14/49 | 1/49 | 6/6 | 0/0 | 0/0 |
| S 组合 A+B（分管并集） | 64.18 | 0.32 | 38/49 | 1/49 | 6/8 + 6/6 | 0/0 | 0/0 |
| MD 正式基准 | 85.39 | 67.53 | 43/49 | 33/49 | 16/96 | 0/0 | 0/0 |
| M-3P8-20 | 84.09 | 18.94 | 39/49 | 10/49 | 2/8 | 0/0 | 0/0 |
| M-3P8-exact | 79.55 | 23.81 | 38/49 | 13/49 | 2/6 | 0/0 | 0/0 |
| LD 正式基准 | 90.58 | 16.77 | 46/49 | 22/49 | 2/128 | 0/0 | 12/1 |
| L-3P8-20 | 91.56 | 13.85 | 42/49 | 13/49 | 4/8 | 2/12 | 12/12 |
| XLD 正式基准 | 100.00 | 80.74 | 49/49 | 38/49 | 48/64 | 3/20 | 12/22 |
| XL-3P8-20 | 98.70 | 22.73 | 45/49 | 4/49 | 2/2 | 0/4 | 6/6 |
| XL-3P8-50 | 98.70 | 42.42 | 45/49 | 8/49 | 2/8 | 2/19 | 12/21 |

S 双对：从 S 中已筛且单对宽松 WC3/GT2 各≤20 的1,184对中，评估双对组合，保留目间覆盖不低于正式 SD 的22组，按并集目间覆盖、完全匹配和简并度排序并逐对检查热力学。A、B 为各自分管后的并集；未检查四条引物同管交互或竞争。所得组合覆盖标签新增 Pseudoboletia maculata，失去 Pseudocentrotus depressus；完全匹配失去 Astriclypeus mannii, Caenopedina pulchella, Colobocentrotus mertensii, Echinometra mathaei, Echinus esculentus, Heterocentrotus mammillatus, Loxechinus albus, Paracentrotus lividus, Parechinus angulosus, Pygmaeocidaris prionigera。其目间覆盖持平 SD，但完全匹配从20.78%降至0.32%，因此不是无代价替换。

L-3P8-20 严格 WC 2条、GT 12条背景记录均为海星；XL-3P8-20 的严格 GT 4条及 XL-3P8-50 的严格 WC 2条、GT 19条均为海百合。各数字为背景记录数。

## 分类群变化

- S-3P8-20：覆盖新增 Pseudoboletia maculata；覆盖丢失 Araeosoma owstoni, Arbacia lixula, Asthenosoma ijimai, Diadema antillarum, Diadema setosum, Echinothrix calamaris, Echinothrix diadema, Pseudocentrotus depressus, Salmacis sphaeroides, Temnopleurus toreumaticus；完全匹配新增 无；完全匹配丢失 Astriclypeus mannii, Caenopedina pulchella, Colobocentrotus mertensii, Echinometra mathaei, Echinus esculentus, Heterocentrotus mammillatus, Loxechinus albus, Paracentrotus lividus, Parechinus angulosus, Pygmaeocidaris prionigera。
- M-3P8-20：覆盖新增 无；覆盖丢失 Echinus esculentus, Loxechinus albus, Paracentrotus lividus, Parechinus angulosus；完全匹配新增 无；完全匹配丢失 Araeosoma owstoni, Astriclypeus mannii, Caenopedina pulchella, Clypeaster virescens, Colobocentrotus mertensii, Diadema antillarum, Echinometra mathaei, Echinothrix calamaris, Echinothrix diadema, Eucidaris tribuloides, Heterocentrotus mammillatus, Lytechinus pictus, Lytechinus variegatus, Phormosoma bursarium, Prionocidaris baculosa, Pseudoboletia maculata, Pseudocentrotus depressus, Strongylocentrotus purpuratus, Stylocidaris reini, Temnopleurus toreumaticus, Toxopneustes pileolus, Tripneustes gratilla, Tripneustes kermadecensis。
- L-3P8-20：覆盖新增 Echinocardium cordatum, Nacospatangus altus；覆盖丢失 Astriclypeus mannii, Echinothrix calamaris, Echinus esculentus, Loxechinus albus, Paracentrotus lividus, Parechinus angulosus；完全匹配新增 Eucidaris tribuloides；完全匹配丢失 Allocentrotus fragilis, Hemicentrotus pulcherrimus, Mesocentrotus franciscanus, Mesocentrotus nudus, Prionocidaris baculosa, Pseudocentrotus depressus, Sterechinus neumayeri, Strongylocentrotus droebachiensis, Strongylocentrotus intermedius, Strongylocentrotus pallidus。
- XL-3P8-50：覆盖新增 无；覆盖丢失 Lytechinus pictus, Lytechinus variegatus, Pseudoboletia maculata, Temnopleurus reevesii；完全匹配新增 无；完全匹配丢失 Allocentrotus fragilis, Araeosoma owstoni, Colobocentrotus mertensii, Diadema antillarum, Diadema setosum, Echinometra mathaei, Echinothrix calamaris, Echinothrix diadema, Eucidaris tribuloides, Heliocidaris crassispina, Hemicentrotus pulcherrimus, Heterocentrotus mammillatus, Mesocentrotus franciscanus, Mesocentrotus nudus, Nacospatangus altus, Phormosoma bursarium, Pseudocentrotus depressus, Pygmaeocidaris prionigera, Salmacis sphaeroides, Stomopneustes variolaris, Strongylocentrotus droebachiensis, Strongylocentrotus intermedius, Strongylocentrotus pallidus, Strongylocentrotus purpuratus, Temnopleurus hardwickii, Temnopleurus reevesii, Temnopleurus toreumaticus, Toxopneustes pileolus, Tripneustes gratilla, Tripneustes kermadecensis。

## 序列、方向及位点

| 名称 | F，5′→3′ | R，5′→3′ | F/R简并度 | F坐标 | R坐标 |
|---|---|---|---:|---:|---:|
| S-3P8-20 | `CGTGTATAATGGATTAACRAGH` | `GCTTAGCTCAAACTAATTTCYTDG` | 6/6 | 185–206 | 349–372 |
| M-3P8-20 | `CGTTAGACGAGAAGACCCTR` | `CTTTGATCACCKKRGTGGATCA` | 2/8 | 1033–1052 | 1239–1260 |
| L-3P8-20 | `GTCTCCTAAATAGAGACTAGYATGAAYGGC` | `GCGGTAACTTGTTCYTTTGATCRCY` | 4/8 | 932–961 | 1250–1274 |
| XL-3P8-20 | `AAGTAGGCCTARAAGCAGCC` | `CCGTCTTGCCATTCATACCAGTCTY` | 2/2 | 529–548 | 944–968 |
| XL-3P8-50 | `AAGTAGGCCTARAAGCAGCC` | `CCGTCTTGCCATTCATRCYAGTCTY` | 2/8 | 529–548 | 944–968 |
| S-3P8-exact | `TGTGTATAATGGATTWACAAGH` | `GCTTAGCTAACACTAATTTCYTDG` | 6/6 | 185–206 | 349–372 |
| M-3P8-exact | `CGTTAGACGAGAAGACCCTR` | `CTTTGATCACCKDAGTGGATCA` | 2/6 | 1033–1052 | 1239–1260 |
| S-3P8-combo-A | `TGTGTATAATGGATTAACAASH` | `GCTTAGCTTAGACYAATTTCTYRG` | 6/8 | 185–206 | 349–372 |
| S-3P8-combo-B | `CGTGTATAATGGATTAACRAGH` | `GCTTAGCTCAAACTAATTTCYTDG` | 6/6 | 185–206 | 349–372 |

坐标为 NC_001453.1、1-based、两端包含。对每个候选分别提供原始比对列的碱基图 `base_matching_名称.svg` 和 PNG；蓝色表示 IUPAC 兼容，橙色错配，灰色缺失，方框为3′末端3 nt。E/C状态来自原序列成对扫描，参考列中插入以 +n 标示。

## 复核与限制

覆盖优先5对、完全匹配优先2对、S组合2对均使用 C++ 原序列穷举与独立 Python 位并行实现复核：共1,440项目标判定、36个严格/完全背景集合、45个背景计数，零差异。两种实现共享参考，不是独立物种留出或湿实验。

候选热力学检查针对未加尾寡核苷酸；尚未评估加接头全长结构、S双对同管交叉二聚体或竞争。尚未测定各长度条码的物种分辨率；三个目各仅一条名称标签，对目间评分敏感。应补充参考及物种/谱系留出，再用组织DNA、含海星的 mock 和实际eDNA测试。

文件：`all_verified_comparison.csv`、`all_by_order.csv`、`all_by_taxon.csv`、`all_independent_checks.csv`、`selection_all.json`、`S_combination_comparison.json`、`thermal_audit.csv`、`base_matching.csv`。工作脚本依赖本工作区原数据与共用模块，并非独立安装包；`input_hashes.json`记录输入。

来源：[Anth-28S 论文](https://doi.org/10.7717/peerj.18607)；[edna-primer-design skill](https://github.com/GUIBA-EX/edna_primer_designer/blob/main/SKILL.md)。


Current D assays: SD=S-3P8-20, MD=M-3P8-20, LD=L-3P8-20, XLD=XL-3P8-50. The S combination is an exploratory separate-PCR comparison.

[当前序列 / Sequences](../sequences/primer_pairs.csv) · [当前统计 / Metrics](../results/current/taxonomic_comparison.csv) · [独立复核 / Verification](../results/D_3prime8/verification.json) · [历史基准 / Prior evidence](../results/D_optimization/selected_D.json)
