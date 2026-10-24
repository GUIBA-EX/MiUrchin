# Methods

[中文](METHODS.zh-CN.md)

Using extracted 16S NC_001453.1 coordinates, search 20–30 nt primers within ±15 nt of four seed starts. Generate WC and G–T-compatible consensus sequences from common-panel base frequencies, adding the three most frequent observed binding sequences per window. Filter to 35–65% GC and exclude six-base homopolymers. Target terminal three bases must match exactly.

Primer3: 50 mM monovalent salt, 1.5 mM Mg²⁺, 0.6 mM dNTP and 200 nM per oligo. Hairpin, homodimer and pair heterodimer Tm must be below 55°C; F/R Tm difference ≤5°C.

Background scans cover both strands, correct orientation and 0–1,000 nt internal distance. Each portfolio permits ≤5 WC≤3 and ≤5 GT≤2 accessions. Maximize common-panel coverage, then exact matching. Enumerate feasible single and two-pair states, collapsing identical target/background states.

Independently rescan complete paired products: target length 150–500 bp with ≥50 nt internal sequence, and background as above. The bounded search does not establish a genome-wide optimum. Frozen references and baseline evidence remain under analysis/.

[Miya et al. 2015](https://doi.org/10.1098/rsos.150088)
