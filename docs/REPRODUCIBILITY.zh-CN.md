# Reproduction / 复现

Extract the source bundle into an empty directory. / 将复现包解压到空目录。

Run `choose_joint.py`, then the independent verification, summary and figure scripts in the project work folder. MiUrchin uses `selected_joint.json`; copy this to `selected_strict.json` before running `verify.py`, `summarize.py`, `positions.py`, `plot.py`, and `end_audit.py`. MiLily uses `selected.json` and runs `verify.py`, `summarize.py`, `figures.py`, `extra_audit.py`.

Validate the published files with `python scripts/check_joint.py`.
