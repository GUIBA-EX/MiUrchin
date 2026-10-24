# Reproduction / 复现

## Check published files / 检查发布文件

```sh
python check_release.py
python scripts/check_compact.py
```

The root checker validates the frozen baseline and manifest; the compact checker validates the current 1–2-pair exports. 根目录检查器校验冻结基线及文件清单；compact检查器校验当前1–2对方案。

## Rebuild compact candidates / 重算精简方案

Use Python 3.12 and a C++17 compiler. Install `requirements-compact.txt`, then extract [the source bundle](../results/compact/reproduction_sources.zip) into a fresh directory and run from its root:

使用Python 3.12与C++17编译器，安装`requirements-compact.txt`后，将源码包解压至新目录，在解压根目录执行：

```sh
python work/miurchin_mifish/discover.py
python work/miurchin_mifish/specific/prepare.py
c++ -O3 -std=c++17 -pthread work/miurchin_mifish/specific/scan_sites.cpp -o work/miurchin_mifish/specific/scan_sites
work/miurchin_mifish/specific/scan_sites work/miurchin_mifish/specific
python work/miurchin_mifish/specific/optimize_pairs.py
python work/miurchin_mifish/verify.py
python work/miurchin_mifish/summarize.py
python work/miurchin_mifish/audit_selected.py
python work/miurchin_mifish/specific/svg_plot.py
```

Outputs / 输出：`work/miurchin_mifish/release/`.

The background site scanner uses a seven-base early-rejection filter: a window is skipped only when that subset already exceeds the full-primer mismatch limit. It scans four threads; output row order can vary, while accession sets are deterministic. The independent final scanner does not use this filter. Reference sequences are frozen; this workflow performs no new database retrieval.

背景位点扫描使用7位早停：仅当这7位的错配已经超过整条引物上限时排除窗口。四线程输出的行序可不同，但命中集合确定。独立最终扫描不使用此预筛选。参考序列冻结，不重新下载数据库。

## Baseline / 基线

`python revalidate.py` reproduces the previous six-pair/mixed-pool validation. Its scope is the retained baseline, not the compact candidate search.

`python revalidate.py`复核保留的6对与混池基线，不执行当前精简搜索。


## S/M ordinary–degenerate comparison / 普通与简并比较

[Source bundle](../results/sm_optimization/reproduction_sources.zip). Extract to a fresh directory with `requirements-compact.txt` installed. The frozen candidate pool includes target states and background accession sets; the selection and full-sequence verification can be rerun without fetching databases. It does not rerun the upstream discovery/background-cache generation.

解压至新目录并安装`requirements-compact.txt`。冻结候选池包含目标状态及背景accession集合，可重算组合选择及全序列独立复核；本入口不重新运行上游候选发现和背景缓存生成。

```sh
python work/miurchin_sm/optimize.py
mkdir -p work/miurchin_mifish/verify
c++ -O3 -std=c++17 work/micucumber_nondegenerate/independent_scan.cpp -o work/miurchin_mifish/verify/scanner
python work/miurchin_sm/verify.py
python work/miurchin_sm/summarize.py
python work/miurchin_sm/plot.py
```

Outputs / 输出：`work/miurchin_sm/release/`.

Run `python scripts/check_current.py` to recalculate current portfolio metrics from the published scan records and verify IUPAC degeneracy and sequence assignments. 使用该命令从发布扫描记录重算当前指标，并检查简并度与配对关系。
