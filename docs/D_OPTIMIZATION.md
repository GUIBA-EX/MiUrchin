# D引物优化 / D-primer optimization

四个长度各保留一对D，普通/A/B/D的F、R起止坐标完全相同。主指标按每目内有至少一条参考命中的物种标签比例计算，再对11个目等权平均；完全匹配采用同一层级。物种标签内的部分/完整匹配另列。/ Each length retains one D pair at the shared ordinary/A/B coordinates. Primary coverage averages the fraction of detected species labels within each of 11 orders equally; any matching reference detects its label. Exact matching uses the same hierarchy; within-label completeness is reported separately.

## 当前选择 / Current selection

| D | Order coverage: before → after % | Order exact: before → after % | F/R degeneracy | Strict WC / GT | Broad WC3 / GT2 |
|---|---:|---:|---:|---:|---:|
| SD | 42.10 → 64.18 | 14.72 → 20.78 | 108/108 | 0 / 0 | 4 / 0 |
| MD | 85.39 → 85.39 | 41.88 → 67.53 | 16/96 | 0 / 0 | 0 / 0 |
| LD | 90.58 → 90.58 | 10.39 → 16.77 | 2/128 | 0 / 0 | 12 / 1 |
| XLD | 100.00 → 100.00 | 62.01 → 80.74 | 48/64 | 3 / 20 | 12 / 22 |

- **S：覆盖收益伴随类群替换。** 目间覆盖42.10→64.18%，物种标签检出36→38/49；新增7个标签、丢失5个，Aspidodiadematoida的唯一参考失去覆盖。F/R简并度54/48→108/108；200 nM/方向时每变体约1.85 nM。
- **M：完全匹配分布更均衡。** 覆盖与覆盖标签不变，完全匹配仍为33/49，但从部分Camarodonta转移到5个其他谱系标签，使目间完全匹配41.88→67.53%。这不是完全匹配物种总数增加。F/R为16/96。
- **L：覆盖不变，完全匹配增加。** 新增3个完全匹配标签，无既有完全匹配标签丢失；F/R从1/16升至2/128，主要代价在反向引物的变体稀释。每方向200 nM时，R每变体1.5625 nM。
- **XL：完全匹配改善最清楚。** 保持49/49标签覆盖；完全匹配28→38/49，新增11、丢失1（Aspidodiadema arcitum）。目间完全匹配62.01→80.74%，严格GT背景22→20条；F/R为48/64。

S improves breadth while exchanging taxa, including loss of the sole Aspidodiadematoida reference. M redistributes, rather than increases, the 33 exactly matched labels across orders. L gains three exact labels without losses, at higher reverse-primer degeneracy. XL retains full panel coverage and gains ten exact labels net; the single exact-label loss remains covered with mismatches. Each assay is a separate PCR candidate, not a multiplex formulation.

## 参考与分类 / Reference panel and taxonomy

目标全库1,401条记录，主比较采用80条参考、49个物种名称标签的共同面板；背景6,045条记录。全部49个名称经WoRMS官方API核对接受名与完整分类树（2026-10-25），采用rank=Order字段。四个名称有接受名更新，但未造成标签合并；保留原序列标签及接受名对照。

The target library contains 1,401 records; comparisons use 80 references representing 49 species-name labels, with 6,045 background records. WoRMS accepted-name/classification responses were frozen for all 49 names on 2026-10-25. The rank=Order field defines the groups. Four accepted-name changes do not merge labels; sequence labels remain traceable.

Temnopleuroida面板成员并入Camarodonta；Phymosomatoida成员归入Stomopneustoida；Astriclypeus和Sinaechinocyamus依当前WoRMS归入Echinolampadacea（Scutelloida列为亚目），Clypeaster仍属Clypeasteroida。因此仍是11个目，但并非直接沿用旧11组名称。旧图中的分类文字不决定统计分组。

Former Temnopleuroida entries join Camarodonta; former Phymosomatoida entries belong to Stomopneustoida. WoRMS places Astriclypeus and Sinaechinocyamus in order Echinolampadacea, with Scutelloida as a suborder; Clypeaster remains in Clypeasteroida. The resulting 11 orders differ from the initial 11 grouping labels. Illustration labels do not define the statistical groups.

[WoRMS classification API](https://www.marinespecies.org/rest/) · [Frozen official responses](../results/D_optimization/taxonomy.json) · [Per-reference mapping](../results/D_optimization/panel.csv)

| Order | Species labels | Reference records |
|---|---:|---:|
| Arbacioida | 2 | 2 |
| Aspidodiadematoida | 1 | 1 |
| Camarodonta | 28 | 55 |
| Cidaroida | 3 | 6 |
| Clypeasteroida | 1 | 1 |
| Diadematoida | 4 | 4 |
| Echinolampadacea | 2 | 2 |
| Echinothurioida | 3 | 3 |
| Pedinoida | 1 | 2 |
| Spatangoida | 2 | 2 |
| Stomopneustoida | 2 | 2 |

三个目仅各一个物种标签，目间分数对它们的单个匹配状态较敏感。该面板不代表每目全部物种。/ Three orders have a single species label each, so macro scores are sensitive to individual matches. The panel does not enumerate every species in an order.

## 搜索与约束 / Search and constraints

从固定结合坐标的观测单倍型、分目共识和已有候选出发，按目等权碱基支持度扩展IUPAC集合。支持度≥0.2%，随机种子20261025，简并度档8/32/128，并保留中间扩展状态；每方向保留全局高分、低简并度、分目优先及原D候选。最终400条单引物组成10,394组同坐标配对。

Starting from observed haplotypes, order-specific consensuses and existing candidates, IUPAC sets are expanded using order-balanced base support ≥0.2%, seed 20261025 and degeneracy tiers 8/32/128, including intermediate states. Global, low-degeneracy, order-specific and original-D oligos are retained. The final pool contains 400 oligos and 10,394 coordinate-fixed pairs.

筛选规则：每方向简并度≤128；严格WC/GT各≤20条、宽松WC3/GT2各≤100条；目间和物种标签完全匹配均不得低于原D，标签覆盖最多允许下降4个百分点。按目间覆盖、目间完全匹配、标签覆盖、较低简并度依次排序，并比较20/50/100条宽松背景门槛。最终S、M、L符合20条门槛，XL需要50条档。旧XLD严格GT为22条，保留在比较表中，未当作通过新门槛的候选。

Per-direction degeneracy is ≤128. Strict WC/GT counts are ≤20 each and broad WC3/GT2 ≤100 each. Order- and label-level exact scores cannot fall below baseline; label coverage can fall by at most four percentage points. Ranking uses order coverage, order exact, label coverage, then lower summed degeneracy. Broad caps of 20/50/100 are compared; S/M/L meet 20 and XL uses the 50 tier. The baseline XLD has 22 strict-GT hits and is retained only as a baseline comparison.

覆盖：每条引物≤2错配且末端3 nt兼容；完全匹配：两端无错配。目标产物150–500 bp，内段≥50 bp；背景配对内段0–1,000 bp，双链扫描。背景WC3/GT2不强制末端兼容，WC4为更宽松敏感性检查。背景数字是记录数，不是实验扩增比例。

Coverage allows ≤2 mismatches per primer with compatible terminal 3 nt; exact matching requires zero mismatches at both ends. Target products are 150–500 bp with ≥50 bp internal sequence; background internal spacing is 0–1,000 bp, scanning both strands. Broad WC3/GT2 omit the terminal constraint; WC4 is a broader sensitivity check. Background counts are records, not experimental amplification fractions.

所有具体变体要求：无末端三连，末端3 nt至少一个GC，末端5 nt含1–4个GC，无超过4 nt的同聚物；允许3′简并。Primer3：50 mM单价盐、1.5 mM Mg²⁺、0.6 mM dNTP；每变体50 nM及每方向200 nM两场景。检查变体内及变体间全部发卡/二聚体，结构Tm<55°C，F/R双链Tm范围中点差≤5°C。

All concrete variants pass terminal/homopolymer rules. Primer3 evaluates 50 mM monovalent salt, 1.5 mM Mg²⁺ and 0.6 mM dNTP, at 50 nM per variant and 200 nM per direction. All intra-/inter-variant hairpins and dimers must have Tm<55°C, with F/R duplex-Tm midpoint difference ≤5°C. Terminal degeneracy is allowed. These are bounded-search selections on reused design references, not a global optimum or wet-lab validation.

## 各目检出与完全匹配 / Detection and exact matching by order

Each cell is detected / exact / total labels. 每格为检出 / 完全匹配 / 总标签数。

| Order | SD | MD | LD | XLD |
|---|---:|---:|---:|---:|
| Arbacioida | 2 / 1 / 2 | 1 / 0 / 2 | 2 / 1 / 2 | 2 / 2 / 2 |
| Aspidodiadematoida | 0 / 0 / 1 | 1 / 1 / 1 | 1 / 0 / 1 | 1 / 0 / 1 |
| Camarodonta | 25 / 8 / 28 | 25 / 19 / 28 | 27 / 19 / 28 | 28 / 20 / 28 |
| Cidaroida | 0 / 0 / 3 | 3 / 3 / 3 | 3 / 2 / 3 | 3 / 3 / 3 |
| Clypeasteroida | 1 / 0 / 1 | 1 / 1 / 1 | 1 / 0 / 1 | 1 / 1 / 1 |
| Diadematoida | 4 / 0 / 4 | 4 / 3 / 4 | 4 / 0 / 4 | 4 / 4 / 4 |
| Echinolampadacea | 2 / 1 / 2 | 2 / 1 / 2 | 2 / 0 / 2 | 2 / 1 / 2 |
| Echinothurioida | 2 / 0 / 3 | 3 / 3 / 3 | 3 / 0 / 3 | 3 / 2 / 3 |
| Pedinoida | 1 / 1 / 1 | 1 / 1 / 1 | 1 / 0 / 1 | 1 / 1 / 1 |
| Spatangoida | 0 / 0 / 2 | 0 / 0 / 2 | 0 / 0 / 2 | 2 / 2 / 2 |
| Stomopneustoida | 1 / 0 / 2 | 2 / 1 / 2 | 2 / 0 / 2 | 2 / 2 / 2 |

## 逐标签增减 / Label-level gains and losses

- SD coverage_hits: gained: Araeosoma owstoni, Arbacia lixula, Astriclypeus mannii, Caenopedina pulchella, Clypeaster virescens, Sinaechinocyamus mai, Stomopneustes variolaris; lost: Aspidodiadema arcitum, Glyptocidaris crenularis, Phormosoma bursarium, Temnopleurus hardwickii, Temnopleurus reevesii
- SD exact_hits: gained: Astriclypeus mannii, Caenopedina pulchella; lost: Glyptocidaris crenularis, Phormosoma bursarium
- MD coverage_hits: gained: none; lost: none
- MD exact_hits: gained: Araeosoma owstoni, Caenopedina pulchella, Clypeaster virescens, Eucidaris tribuloides, Phormosoma bursarium; lost: Echinus esculentus, Loxechinus albus, Paracentrotus lividus, Parechinus angulosus, Sterechinus neumayeri
- LD coverage_hits: gained: none; lost: none
- LD exact_hits: gained: Mesocentrotus nudus, Prionocidaris baculosa, Stylocidaris reini; lost: none
- XLD coverage_hits: gained: none; lost: none
- XLD exact_hits: gained: Araeosoma owstoni, Arbacia lixula, Colobocentrotus mertensii, Diadema setosum, Echinocardium cordatum, Eucidaris tribuloides, Heliocidaris crassispina, Nacospatangus altus, Stomopneustes variolaris, Temnopleurus reevesii, Tripneustes kermadecensis; lost: Aspidodiadema arcitum

## 独立复核 / Independent verification

8对新旧方案由C++全窗口扫描与Python位并行扫描独立计算：1,280项目标判定、32个严格/完全背景集合、40项背景计数，差异0。新D替换后，普通/A/B序列和匹配状态保持不变。独立算法共用同一参考库，不是独立生物样本验证。

Eight baseline/candidate pairs agree across independent exhaustive C++ and bit-parallel Python scans: 1,280 target decisions, 32 strict/exact background sets and 40 background counts, with zero disagreements. Ordinary/A/B sequences and states are unchanged. Independent algorithms share the same reference data.

[候选全表 / All candidates](../results/D_optimization/candidate_comparison.csv) · [复核表 / Verified metrics](../results/D_optimization/verified_comparison.csv) · [逐标签结果 / By label](../results/D_optimization/by_taxon.csv) · [增减 / Changes](../results/D_optimization/taxon_changes.csv) · [碱基表 / Bases](../results/D_optimization/base_matching.csv) · [原始命中 / Raw hits](../results/D_optimization/independent_hits.tsv) · [独立复现 / Reproduction](../results/D_optimization/reproduction_sources.zip)
