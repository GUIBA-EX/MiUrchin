"""Fail on drift between adopted evidence, current catalog, FASTA, reports and checksums."""
from pathlib import Path
import collections
import csv
import hashlib
import json
import re
P = Path(__file__).resolve().parent
cat = json.loads((P / 'results/catalog.json').read_text())
rows = cat['assays']
# Fixed release expectations detect accidental catalog truncation; other totals derive from these.
EXPECTED_PRIMARY_PAIRS = 32
EXPECTED_SUPPLEMENTARY_PAIRS = 76
if len(rows) != EXPECTED_SUPPLEMENTARY_PAIRS or len(cat['originals']) != EXPECTED_PRIMARY_PAIRS:
    raise ValueError(f"Catalog size: got {len(rows)} supplementary and {len(cat['originals'])} primary; expected {EXPECTED_SUPPLEMENTARY_PAIRS} and {EXPECTED_PRIMARY_PAIRS}")
if not (len({r['id'] for r in rows}) == EXPECTED_SUPPLEMENTARY_PAIRS and len({(r['gene'], r['parent']) for r in rows}) == EXPECTED_PRIMARY_PAIRS):
    raise ValueError("Validation failed: len({r['id'] for r in rows}) == EXPECTED_SUPPLEMENTARY_PAIRS and len({(r['gene'], r['parent']) for r in rows}) == EXPECTED_PRIMARY_PAIRS")
I = dict(zip('ACGTRYSWKMBDHVN', ['A', 'C', 'G', 'T', 'AG', 'CT', 'CG', 'AT', 'GT', 'AC', 'CGT', 'AGT', 'ACT', 'ACG', 'ACGT']))

def fasta(p):
    d = {}
    for l in p.read_text().splitlines():
        if l.startswith('>'):
            k = l[1:].split()[0]
            if k in d:
                raise ValueError(f'Duplicate FASTA identifier in {p}: {k}')
            d[k] = ''
        else:
            d[k] += l
    return d
primary = fasta(P / 'sequences/non_partitioned.fasta')
archived = fasta(P / 'legacy/v1.2/sequences/all_markers.fasta')
if primary != archived:
    raise ValueError('Primary FASTA differs from archived v1.2 sequences or names')
if len(primary) != 2 * len(cat['originals']):
    raise ValueError(f'Primary FASTA has {len(primary)} oligos; expected {2 * len(cat['originals'])}')
with (P / 'sequences/non_partitioned_pairs.csv').open() as fh:
    primary_rows = list(csv.DictReader(fh))
if primary_rows != cat['originals']:
    raise ValueError('Primary CSV differs from catalog originals')
for row in primary_rows:
    prefix = 'MiUrchin-' + row['gene'] + ('-' if row['gene'] in ('16S', '28S') else '_') + row['parent']
    for direction in ('F', 'R'):
        name = prefix + '_' + direction
        if primary.get(name) != row[direction]:
            raise ValueError(f'Primary FASTA/CSV mismatch: {name}')
for doc in ('README.md', 'README.zh-CN.md', 'README.en.md'):
    text = (P / doc).read_text().split('<details>', 1)[0]
    for row in primary_rows:
        if not any((f'`{row['F']}`' in line and f'`{row['R']}`' in line for line in text.splitlines() if line.startswith('|'))):
            raise ValueError(f'{doc} missing primary pair: {row['id']}')
with (P / 'sequences/primary_name_aliases.csv').open() as fh:
    aliases = list(csv.DictReader(fh))
if len(aliases) != len(primary) or {a['archived_fasta_name'] for a in aliases} != set(primary):
    raise ValueError('Primary alias mapping is incomplete')
if len({a['standard_alias'] for a in aliases}) != len(aliases):
    raise ValueError('Primary aliases are not unique')
for alias in aliases:
    if primary[alias['archived_fasta_name']] != alias['sequence']:
        raise ValueError(f'Incorrect sequence for alias {alias['standard_alias']}')
allfa = fasta(P / 'sequences/all_markers.fasta')
if len(allfa) != 2 * len(rows):
    raise ValueError('Validation failed: len(allfa) == 152')
if not allfa == fasta(P / 'sequences/primers.fasta'):
    raise ValueError("Validation failed: allfa == fasta(P / 'sequences/primers.fasta')")
source = {}
for file in ['round1.json', 'round2.json']:
    for r in json.loads((P / 'results/evidence' / file).read_text())['recommended']:
        source[r['id']] = r
used = collections.defaultdict(set)
for r in rows:
    if not r['covered'] == r['n_records'] == len(r['panel']) >= 3:
        raise ValueError("Validation failed: r['covered'] == r['n_records'] == len(r['panel']) >= 3")
    if not len(set(r['panel'])) == r['n_records']:
        raise ValueError("Validation failed: len(set(r['panel'])) == r['n_records']")
    key = (r['gene'], r['parent'])
    if used[key].intersection(r['panel']):
        raise ValueError("Validation failed: not used[key].intersection(r['panel'])")
    used[key].update(r['panel'])
    for s in ['F', 'R']:
        if not r[s] == allfa[r['id'] + '_' + s] == source[r['id']][s]:
            raise ValueError("Validation failed: r[s] == allfa[r['id'] + '_' + s] == source[r['id']][s]")
        if not set(r[s]) <= set(I):
            raise ValueError('Validation failed: set(r[s]) <= set(I)')
        if r['mode'] == 'ordinary':
            if not set(r[s]) <= set('ACGT'):
                raise ValueError("Validation failed: set(r[s]) <= set('ACGT')")
    for k, v in r['background'].items():
        if not v <= r['original_background'][k]:
            raise ValueError("Validation failed: v <= r['original_background'][k]")
    margin = min((min(t['F_tm'] + t['R_tm']) - t['structure_max'] for t in r['thermal']))
    if not abs(margin - r['minimum_structure_margin']) < 1e-08:
        raise ValueError("Validation failed: abs(margin - r['minimum_structure_margin']) < 1e-08")
    if not r['tier'] == ('priority' if margin >= 5 else 'conditional'):
        raise ValueError("Validation failed: r['tier'] == ('priority' if margin >= 5 else 'conditional')")
    for t in r['thermal']:
        if not (t['structure_max'] < 55 and min(t['F_tm'] + t['R_tm']) >= 45 and (max(t['F_tm'] + t['R_tm']) <= 75) and (t['delta_mid_tm'] <= 5)):
            raise ValueError("Validation failed: t['structure_max'] < 55 and min(t['F_tm'] + t['R_tm']) >= 45 and (max(t['F_tm'] + t['R_tm']) <= 75) and (t['delta_mid_tm'] <= 5)")
    if not r['use'] == 'separate_PCR':
        raise ValueError("Validation failed: r['use'] == 'separate_PCR'")
if not sum((r['tier'] == 'priority' for r in rows)) == 65:
    raise ValueError("Validation failed: sum((r['tier'] == 'priority' for r in rows)) == 65")
for tier in ['priority', 'conditional']:
    f = fasta(P / 'sequences' / f'{tier}.fasta')
    if not f == {r['id'] + '_' + s: r[s] for r in rows if r['tier'] == tier for s in ['F', 'R']}:
        raise ValueError("Validation failed: f == {r['id'] + '_' + s: r[s] for r in rows if r['tier'] == tier for s in ['F', 'R']}")
flat = list(csv.DictReader((P / 'sequences/primer_pairs.csv').open()))
if len(flat) != len(rows):
    raise ValueError('Validation failed: len(flat) == 76')
for a, b in zip(flat, rows):
    if not (a['id'] == b['id'] and a['F'] == b['F'] and (a['R'] == b['R'])):
        raise ValueError("Validation failed: a['id'] == b['id'] and a['F'] == b['F'] and (a['R'] == b['R'])")
v = json.loads((P / 'results/current_validation.json').read_text())
if not v['status'] == 'PASS':
    raise ValueError("Validation failed: v['status'] == 'PASS'")
for k in ['scan_checks', 'independent_checks', 'thermal_checks']:
    if not (len(v[k]) == len(rows) and {r['id'] for r in v[k]} == {r['id'] for r in rows}):
        raise ValueError("Validation failed: len(v[k]) == len(rows) and {r['id'] for r in v[k]} == {r['id'] for r in rows}")
if not 'Local integrated computational manuscript v2.0.0' in (P / 'publications/MiUrchin_preprint.md').read_text():
    raise ValueError("Validation failed: 'Local integrated computational manuscript v2.0.0' in (P / 'publications/MiUrchin_preprint.md').read_text()")
if not (P / 'publications/MiUrchin_preprint.pdf').stat().st_size > 10000:
    raise ValueError("Validation failed: (P / 'publications/MiUrchin_preprint.pdf').stat().st_size > 10000")
for f in [P / 'README.md', P / 'README.en.md', P / 'README.zh-CN.md', *list((P / 'docs').glob('*.md')), P / 'publications/MiUrchin_preprint.md', P / 'publications/MiUrchin_supplement.md']:
    for link in re.findall('\\]\\(([^)]+)\\)', f.read_text()):
        if not link.startswith(('http', '#')):
            if not (f.parent / link.split('#')[0]).exists():
                raise ValueError("Validation failed: (f.parent / link.split('#')[0]).exists()", (f, link))
for name, digest in json.loads((P / 'SHA256SUMS.json').read_text()).items():
    if not hashlib.sha256((P / name).read_bytes()).hexdigest() == digest:
        raise ValueError('Validation failed: hashlib.sha256((P / name).read_bytes()).hexdigest() == digest', name)
print('PASS: 32 primary pairs and 64 oligos, adopted sources,76 pairs,152 named oligos,65/11 tiers,32 parents,raw+thermal validation,links,and checksums')
