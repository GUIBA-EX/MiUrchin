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
