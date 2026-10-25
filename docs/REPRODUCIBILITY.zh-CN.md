# Reproduction / 复现

## Current D / 当前D

Extract [reproduction_sources.zip](../results/D_optimization/reproduction_sources.zip) into an empty directory and run:

```sh
python3 verify.py
```

Requires Python 3.10+ and a C++17 compiler; no network or Python packages. The bundle freezes target/background FASTA, panel taxonomy, eight selected/baseline pairs, and independent C++/Python scanners. Output `rerun/` reproduces target states, background sets/counts and order metrics. Frozen taxonomy is used rather than refetching a potentially changed classification.

解压到独立目录后复核8对新旧D方案，使用冻结分类映射，无需联网；输出逐参考、逐标签、逐目指标及非目标记录。候选搜索参数与来源见[D optimization](D_OPTIMIZATION.md)。完整搜索也提供[独立冻结包](../results/D_optimization/search_reproduction.zip)：解压后运行 `python3 run.py`，需numpy、biopython、primer3-py及C++17；冻结原始种子、坐标和分类，无需原工作目录或联网。 / The frozen search bundle reproduces the candidate search and verification without the original workspace.

## Release checks / 发布检查

```sh
python3 scripts/check_D.py
python3 scripts/check_current.py
python3 scripts/check_joint.py
python3 scripts/check_terminal.py
python3 scripts/check_ab.py
python3 check_release.py
```

## Original search evidence / 原始搜索证据

The older [terminal bundle](../results/terminal_optimization/reproduction_sources.zip) preserves the pre-D-optimization selection and unchanged ordinary/A/B design history; it does not generate current D sequences. Current canonical sequences are in `sequences/`, current metrics in `results/current/`, and current combined raw hits in `results/terminal_optimization/independent_hits.tsv`.

旧末端复现包用于原始选配及普通/A/B证据；当前D以本页首个复现包为准。

## Base plots / 碱基匹配图

`python3 scripts/plot_base_matching.py` regenerates all 16 SVG/PNG plots and the base table from current sequences, fixed alignment columns and verified raw-hit states. Requires biopython, Pillow and matplotlib.

Full-search clean-directory reproduction regenerated the same 400 oligos, 10,394 pair evaluations and eight candidate/baseline selections, with identical verified outputs. / 独立目录完整重跑搜索与复核，候选表和最终选择完全一致。See [record](../results/D_optimization/full_search_reproduction_check.json). Install search dependencies from `requirements-D.txt`.
