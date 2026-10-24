# Reproduction / 复现

Extract the reproduction bundle into an empty directory. Current retained sequences are frozen in `work/milily/selected.json` or `work/miurchin_enddesign/selected_strict.json`. Re-run `verify.py`, `summarize.py` and figure scripts against these frozen selections. The earlier `choose_joint.py` selects the baseline and does not reproduce the later Occam retention decisions.

当前保留决策见 `docs/DECISIONS.md`；完整候选比较见 `results/degenerate_expansion`。复现独立扫描后运行 `python scripts/check_joint.py` 检查发布包。
