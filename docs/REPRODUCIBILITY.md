# Reproducibility

The primary collection is `sequences/non_partitioned.fasta` and `sequences/non_partitioned_pairs.csv`, checked against archived v1.2; `results/catalog.json` records the primary parents and supplementary catalog. Inputs: `data/<gene>/{target,background}.fasta`. Adopted evidence: `results/evidence/round1.json` and `round2.json`. Current tables and FASTA are generated, not edited independently.

Install `requirements.txt` with Python 3.12 and provide a C++17 compiler. Run from the project root:

```sh
python scripts/revalidate.py --thermal
python scripts/build_release.py  # regenerates supplementary outputs and the earlier branch-focused manuscript source
python scripts/build_paper.py    # builds the earlier branch-focused manuscript PDF
python scripts/stamp_checksums.py
python check_release.py
```

`revalidate.py` writes only a validation report and uses a temporary directory for compiled scans. It verifies all 76 candidate pairs, their 32 original comparators on the same accession sets, four background counts, a separate target-matching implementation and both thermodynamic scenarios. It does not rerun an exhaustive global primer-design search. Finite-search candidate histories are retained in the two evidence JSON files; historical design tools are archived under `legacy/v1.2/`.

Publication and remote tagging are manual. The validation workflow has read-only repository permissions and does not push commits or create releases. The changelog distinguishes the earlier 2.0.0 branch-focused snapshot from subsequent primary-first changes; use a specific commit or archived release when citing.

## Manuscript review revision

The primary-first revised manuscript adds frozen-reference diagnostics without replacing released sequences. See [review revision evidence](../results/reviewer_revision/README.md) for commands and a claim-to-output map. The historical `build_paper.py` command above builds the earlier branch-focused preprint, not the revised primary-first manuscript. New evidence remains retrospective; no independent biological validation is claimed.

Build revised Word documents with `python scripts/build_revised_manuscript.py --package publications/manuscript_20261106` after installing the package’s `requirements-documents.txt`. PDF rendering is a separate step; the delivered PDFs were visually checked.

The primary collection retains its archived FASTA names; `sequences/primary_name_aliases.csv` maps each to a consistent alias without changing released identifiers. `python scripts/check_background_sample.py` independently spot-checks strict WC and GT background hits; sample selection and limitations are documented in `results/reviewer_revision/README.md`.

Use `python scripts/check_background_sample.py --full` to independently cross-check strict WC and GT hits on every archived background record. The routine checks accession sets; it does not independently recalculate relaxed WC/GT models.
