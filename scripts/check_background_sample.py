"""Cross-check sampled background records with a separate regex-based matcher.

Samples include records with archived strict WC/GT hits and records from the
start of each input library. This is not an exhaustive specificity validation.
"""
import argparse
import collections
import csv
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'results/reviewer_revision'
BASES = dict(zip('ACGTRYSWKMBDHVN', ['A','C','G','T','AG','CT','CG','AT','GT','AC','CGT','AGT','ACT','ACG','ACGT']))
COMPLEMENT = str.maketrans('ACGTRYMKSWBDHVN', 'TGCAYRKMSWVHDBN')


def read_fasta(path):
    records = {}
    for line in path.read_text().splitlines():
        if line.startswith('>'):
            name = line[1:].split()[0]
            if name in records:
                raise ValueError(f'Duplicate FASTA identifier: {name}')
            records[name] = ''
        else:
            records[name] += line.strip().upper()
    return records


def locate(query, sequence, reverse, gt):
    allowed = []
    for symbol in query:
        letters = set(BASES[symbol])
        if gt:
            for source, target in (('C','T'), ('A','G')) if reverse else (('G','A'), ('T','C')):
                if source in letters:
                    letters.add(target)
        allowed.append(letters)
    tail = allowed[:3] if reverse else allowed[-3:]
    motif = '(?=(' + ''.join('[' + ''.join(sorted(x)) + ']' for x in tail) + '))'
    for match in re.finditer(motif, sequence):
        pos = match.start() if reverse else match.start() - len(query) + 3
        if pos < 0:
            continue
        fragment = sequence[pos:pos + len(query)]
        if len(fragment) != len(query) or set(fragment) - set('ACGT'):
            continue
        if sum(base not in allowed[i] for i, base in enumerate(fragment)) <= 2:
            yield pos


def paired(sequence, forward, reverse, gt):
    for seq in (sequence, sequence.translate(COMPLEMENT)[::-1]):
        left = list(locate(forward, seq, False, gt))
        right = list(locate(reverse, seq, True, gt))
        if any(0 <= r - f - len(forward) <= 1000 for f in left for r in right):
            return True
    return False


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--full', action='store_true', help='check every archived background record')
    args = parser.parse_args()
    catalog = json.loads((ROOT/'results/catalog.json').read_text())
    rows = catalog['originals'] + catalog['assays']
    output = {'method': 'Independent regex terminal-triplet and two-mismatch matching; up to 1000 internal bases; both orientations.', 'sampling': 'First 10 records plus up to 10 lexically sorted records with archived strict hits per marker; deterministic, not representative.', 'markers': {}}
    if args.full:
        output['sampling'] = 'All archived background records, including ambiguous binding sites excluded by both implementations.'
    for gene in ('16S', '12S', 'COI', '28S'):
        source = ROOT/'data'/gene/'background.fasta'
        seqs = read_fasta(source)
        hits = collections.defaultdict(set)
        with (OUT/gene/'independent_hits.tsv').open() as handle:
            for hit in csv.DictReader(handle, delimiter='\t'):
                if hit['role'] == 'background' and hit['le2last3'] == '1':
                    hits[(hit['name'], hit['model'])].add(hit['accession'])
        sampled = set(seqs) if args.full else set(list(seqs)[:10]) | set(sorted(set().union(*hits.values()))[:10])
        if sampled - seqs.keys():
            raise ValueError(f'{gene}: archived hit identifiers missing from background library')
        checks = 0
        for row in (r for r in rows if r['gene'] == gene):
            reverse = row['R'].translate(COMPLEMENT)[::-1]
            for model in ('WC', 'GT'):
                expected = hits[(row['id'], model)] & sampled
                actual = {name for name in sampled if paired(seqs[name], row['F'], reverse, model == 'GT')}
                if actual != expected:
                    raise ValueError(f"{gene} {row['id']} {model}: expected {sorted(expected)}, got {sorted(actual)}")
                checks += 1
        output['markers'][gene] = {'accessions': sorted(sampled), 'assay_model_checks': checks, 'background_sha256': hashlib.sha256(source.read_bytes()).hexdigest(), 'status': 'PASS'}
        print(gene, len(sampled), checks, 'PASS', flush=True)
    output['status'] = 'PASS'
    filename = 'background_full_verification.json' if args.full else 'background_sample_verification.json'
    (OUT/filename).write_text(json.dumps(output, indent=2)+'\n')


if __name__ == '__main__':
    main()
