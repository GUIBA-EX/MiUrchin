# MiUrchin nuclear 28S

The six candidates share three binding windows on *Strongylocentrotus purpuratus* XR_004063668.1. The 122 aligned target records represent one sequence per NCBI binomial. Background scans use 832 records representing the other four echinoderm classes and nine additional aquatic animal groups. The target and background FASTA headers retain species names and accessions.

[Selected pairs and counts](selected.csv) · [Sequences](primers.fasta) · [All 56 candidate comparisons](comparison.csv) · [Changes relative to ordinary pairs](changes.csv)

To reproduce the six paired scans and the matrices from the repository root:

```sh
c++ -O3 -std=c++17 markers/12S_COI/scripts/raw_scan.cpp -o /tmp/miurchin28s_scan
/tmp/miurchin28s_scan markers/28S
python3 markers/28S/verify_and_plot.py
python3 scripts/plot_regions.py --gene 28S
```

The verification script recomputes the evaluable denominator and checks target coverage, exact matches and four background counts against the selected table before drawing the matrices. Rows follow primer orientation, including reverse complementation of the reverse binding site. The aligned reference projection omits insertions relative to the anchor; paired hits come from the original unaligned records. Selection and verification use the same frozen panel.
