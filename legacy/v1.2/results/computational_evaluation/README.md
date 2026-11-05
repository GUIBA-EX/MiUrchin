# Computational evaluation

Frozen inputs, common-panel comparisons, primer-free barcode identity and genus-blocked conditional sequence-selection tests. The released primers are unchanged.

```sh
python3 scripts/analyze.py
python3 scripts/distances.py
python3 scripts/sensitivity.py
python3 scripts/validate.py
```

Run from this directory with Python 3.10+. Numerical scripts use the standard library; `python3 scripts/plot.py` additionally requires matplotlib. Inputs are frozen under `inputs/`, outputs under `results/`; the manifest records input hashes.

See the main bilingual README for methods, results and interpretation. Window discovery preceded fold splitting; fold candidates allow local offsets and have not passed the formal thermal/background gates. Exact barcode identity conflicts are retained for source review.
