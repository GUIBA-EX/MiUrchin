# Reproduction / 复现

Extract the reproduction bundle into an empty directory. Current retained sequences are frozen in `work/milily/selected.json` or `work/miurchin_enddesign/selected_strict.json`. Re-run `verify.py`, `summarize.py` and figure scripts against these frozen selections. The earlier `choose_joint.py` selects the baseline and does not reproduce the later Occam retention decisions.

当前保留决策见 `docs/DECISIONS.md`；完整候选比较见 `results/degenerate_expansion`。复现独立扫描后运行 `python scripts/check_joint.py` 检查发布包。

Expanded A/B search / 扩大A/B搜索：`work/ab_expanded/search.py PROJECT` → `refine.py` → `install.py`, followed by each project’s `verify.py`, `summarize.py` and figure scripts. The bundle contains the preceding selection, expanded candidates and final selection. Run `python scripts/check_ab.py` to check mutual contributions and current README values. The search scripts use the multi-project workspace layout; to reproduce only this release, use its frozen selection and per-project verification pipeline. / 搜索脚本依赖三个项目的共同工作目录；单独复核本发布时使用冻结选配结果及项目独立扫描流程。
