# Reproduction / 复现

## Current D / 当前D

Extract [the frozen verification bundle](../results/D_3prime8/reproduction_sources.zip) into an empty directory and run `python3 verify.py`. Python 3.10+ and a C++17 compiler are required. The bundle independently verifies five 3′-half candidates using the frozen panel and background. / 解压后运行，复核5对候选的参考命中与背景；分类映射和序列已冻结。

```sh
python3 check_release.py
```

`python3 scripts/plot_base_matching.py` regenerates the 16 plots and base table with biopython, Pillow and matplotlib. / 可重绘16对碱基图。

The prior [D optimization bundle](../results/D_optimization/reproduction_sources.zip) and [full-search bundle](../results/D_optimization/search_reproduction.zip) document the earlier design and do not reproduce current D. / 旧复现包仅对应历史方案。The current exploratory search scripts and input hashes are archived in [D_3prime8](../results/D_3prime8); their workspace imports and paths require adaptation before reuse. / 当前搜索脚本依赖工作区路径。
