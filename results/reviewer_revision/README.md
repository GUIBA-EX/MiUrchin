# Review revision evidence

These additional analyses retain the released primer sequences. They reuse archived references and do **not** constitute independent biological validation. Raw library counts (16S 1,401; 12S 69; COI 314; 28S 122) differ from the historical completeness-filtered species panels. Unmatched raw records include incomplete sequences. Do not overwrite historical result tables with these counts.

## Reproduce

From the repository root, install the pinned `primer3-py==2.4.0` dependency and provide a C++17 compiler:

```sh
python scripts/reviewer_terminal_audit.py
python scripts/reviewer_revision.py
python scripts/reviewer_benchmark.py
python scripts/check_reviewer_revision.py
```

The target/background scanner uses total target products of 60–650 bp and nonoverlapping sites; background products allow 0–1,000 internal bases. Target coverage requires at most two mismatches per end and WC-compatible terminal triplets. The primary structural reanalysis expands every concrete variant and uses the same two concentration scenarios as the supplementary candidate screen. The independent Python implementation checks every target hit, exact hit and extracted insert against the C++ output.

| Manuscript evidence | Input and method | Output |
| --- | --- | --- |
| Primary terminal compatibility | Archived homologous sites; complete ACGT and no insertions | `primary_terminal_audit.csv`, `primary_terminal_paired.csv`, `primary_site_audit.csv` |
| Primary pair structures | 32 original sequences, two concentration scenarios, all variants | `primary_pair_structures.csv` |
| Entire archived input coverage | Original 32 plus supplementary 76, shared target geometry | `full_target_coverage.csv` |
| Supplementary scope versus parent | Union of separate PCR outcomes; gained and lost records | `separate_PCR_union.csv` |
| Within-echinoid cross matching | All archived target records and archived order labels | `order_cross_matching.csv` |
| Identity among recovered inserts | Paired raw products with primer regions removed | `recovered_insert_identity.csv`, `recovered_inserts.csv` |
| Published COI comparison | Three verified pairs, six originals, same raw inputs; 56-record site-complete intersection | `COI_literature_comparison.csv`, `COI_benchmark_panels.json` |
| Provenance and implementation agreement | Frozen input hashes and independently reconstructed target products | `summary.json`, `terminal_input_hashes.json`, `verification.json` |

The per-gene folders and `benchmark_COI/` retain raw hits and inserts. No ambiguity or inosine is silently treated as a fully matching concrete base at a primer site. For the COI benchmark, original coordinates are retained; external sites are uniquely mapped on NC_001453.1 with a permissive coordinate-location search (up to eight mismatches per end), independently of the strict evaluation gate. Binding-site completeness requires called bases at all projected columns. Different amplicon lengths and broad-metazoan versus echinoid design goals prevent a blanket superiority claim. Uni-Minibar sequences follow Meusnier 2008; the source manifest records a conflicting later table.

## Evidence still needed

- A genuinely external, overlap-audited sequence test set; archived records outside a selected panel are not external validation.
- Expanded complete-site references for close non-target taxa, especially Holothuroidea at 28S.
- Full-library discrimination and within-species variation: uniqueness among recovered records can be optimistic because competing undetected taxa are absent.
- Verified literature comparators for 16S, 12S and 28S.
- Experimental performance if detection, efficiency or field sensitivity claims are intended.

The scientific conclusions must retain these boundaries even when all implementation checks pass.
