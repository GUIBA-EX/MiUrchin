# MiUrchin XS：反向引物倒数第 4 位简并比较

引物按 5′→3′ 书写；第 4 位从反向引物的 3′ 末端向内计数。固定正向引物 `CTTGTGTATAATGGATTRACRA`，分别将原反向引物的倒数第 4 位 G 扩展为 R（A/G）、S（C/G）或 K（G/T）。原反向引物简并度为 4，改动后均为 8；正向引物简并度为 4。

| 反向引物 | 目标覆盖 | 完全匹配 | 严格非目标 WC / GT | 宽松非目标 WC3 / GT2 |
|---|---:|---:|---:|---:|
| AAACTAATTTCTTGGRGARC（原） | 30/55 | 6/55 | 0 / 7 | 7 / 7 |
| AAACTAATTTCTTGGRRARC（G→R） | 35/55 | 6/55 | 0 / 7 | 19 / 7 |
| AAACTAATTTCTTGGRSARC（G→S） | 30/55 | 6/55 | 0 / 7 | 7 / 7 |
| AAACTAATTTCTTGGRKARC（G→K） | 31/55 | 6/55 | 0 / 7 | 7 / 7 |

覆盖：正反向引物各允许最多两个错配，且各自 3′ 端最后三个碱基兼容；完全匹配：两条引物均无错配。每物种一条参考序列；55 是此窗口可评估的物种数，另有 110 个物种缺少可评估窗口，不能当作漏检。背景为 6,045 条非目标参考记录；数字是记录数，不是物种数或实际 PCR 扩增数。严格 WC 为同覆盖规则下的 Watson–Crick 命中；严格 GT 另允许 G–T 配对。宽松 WC3 为每条最多 3 个错配、GT2 为每条最多 2 个错配，不要求末端 3 个碱基兼容。

G→R 增加 5 种，未丢失原有覆盖物种：*Mesocentrotus franciscanus*、*M. nudus*、*Phormosoma bursarium*、*Pseudocentrotus depressus*、*Temnopleurus toreumaticus*。Camarodonta 从 21/28 增至 25/28，Echinothurioida 从 0/3 增至 1/3。G→K 新增 *Caenopedina pulchella*；G→S 没有新增覆盖。

G→R 通过既定引物末端和 Primer3 结构筛查：两种浓度模型中最大预测结构 Tm 均为 45.7 °C，反向引物各变体 Tm 分别为 47.5–53.4 °C（每变体 50 nM）及 46.6–52.4 °C（每方向总浓度 200 nM）。预测不代替实验。扩展后在参考 NC_001453.1 的有效结合位置仍为 F 183–204、R 344–363，扩增区间 181 bp。实际结合位置和扩增长度因物种而异。

G→R 的目标覆盖、完全匹配及严格背景 WC/GT 命中集合，经 C++ 和独立 Python 原始序列扫描核对，一致。7 条严格 GT 命中均属于海星背景记录；宽松 WC3 增至 19 条，提示放宽末端约束后潜在非目标风险增加。XSD 为计算候选，尚需实验验证。
