# Reproducibility / 复现

## Supported validation / 支持的复核

```bash
python -m pip install -r requirements.txt
python revalidate.py
```

Requires Python 3.12 and a C++17 compiler. The runner locates its own repository, scans frozen sequences, checks Python/C++ consistency, recomputes complete scheme unions and thermodynamics, and exports result tables. It overwrites generated analysis/results files. Network access is unnecessary after dependency installation. Independent experiments and a fresh database acquisition are not part of this entrypoint.

需要Python 3.12和C++17编译器。脚本自动定位仓库，扫描冻结序列，核对Python/C++结果，重新汇总组合并集与热力学并导出结果表；会覆盖生成的分析及结果文件。依赖安装后无需联网，不包括新获取数据库或独立实验。

## Directory map / 目录

- `analysis/`: frozen sequences, alignments, metadata, validation code and evidence / 冻结序列、比对、元数据、验证代码与证据。
- `analysis/same_locus/`: expanded candidate oligos, per-region panels, selected trajectories and local exact-match refinement / 扩展候选、各区域面板、组合搜索及完全匹配优化记录。
- `results/`: sequences, assignments, comparison, source-order gaps, non-target accessions / 引物、配对、比较、分类群缺口及非目标记录。
- `figures/`: bilingual PNG/SVG/PDF and machine-readable plot data / 双语图及绘图数据。
- `discovery/`: historical search implementations for inspection, **not a turnkey rediscovery pipeline**; large hit caches and some intermediate search arrays are not distributed / 历史搜索实现供审阅，不是可一键重新发现候选的完整流水线；大型命中缓存及部分中间数组未打包。
- `analysis/final_selected.json`: initial single-pair design seeds, not final composite schemes / 初始单对设计种子，不是最终组合方案。
- `analysis/portfolio_selected.json`: final complete scheme definitions / 最终完整方案定义。

MAFFT 7.526 generated the saved alignments; it is not needed to revalidate frozen selected candidates. The complete genetic reference inputs are included. The published fingerprint file records the release snapshot; regenerate it deliberately when altering inputs/results. Exact byte identity of exported figures is not promised across plotting/font versions.

保存的比对由MAFFT 7.526生成；复核冻结候选不需要再次比对。仓库包含完整本轮参考输入。SHA256记录发布快照；修改输入或结果后应有意重新生成。跨绘图库或字体版本不保证图片字节完全相同。

## Plot reproduction / 绘图

```bash
python -m pip install -r requirements-plot.txt
python plot_regions.py
# Chinese and English figures / 双语图片：
python plot_regions.py --cjk-font /path/to/CJK-font.ttf
```

Without a supplied CJK font, the plotter generates English images; with one, it generates both languages. SVG text is converted to paths. Curves use common-panel equal-label/within-label-haplotype weights. Major-base frequency is conditional on callable A/C/G/T; the dashed curve reports that callable weight. Both curves are centered 11-reference-position means, truncated at plot boundaries. Gaps and ambiguous bases are not counted as conserved; reference insertion columns do not occupy separate x coordinates. Arrows use seed windows, not inferred physical lengths of all variants.

不提供中文字体时生成英文图；提供后生成双语图，SVG文字转为路径。曲线使用共同面板标签等权及标签内单倍型等权；主碱基频率以可判定A/C/G/T为分母，虚线另示可判定权重。两曲线为中心11参考位点滑动均值，边缘缩短窗口。缺口或模糊碱基不算保守，参考插入列不单独占横坐标。箭头采用种子窗口，不以所有变体长度反推坐标。
