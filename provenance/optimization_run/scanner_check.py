from pathlib import Path
import subprocess,csv,random
p=Path('work/scanner_test');p.mkdir(exist_ok=True);F='ACGATTCGAGTCGATCGTAC';R='GTCAGATCGTACCTAGTCGA';rc=lambda s:s.translate(str.maketrans('ACGT','TGCA'))[::-1]
def mutate(s,idx):
 t=list(s)
 for i in idx:t[i]=next(x for x in 'ACGT' if x!=t[i])
 return ''.join(t)
base=F+'A'*35+rc(R);records={'exact':base,'reverse':rc(base),'internal2':mutate(F,[2,7])+'A'*35+rc(R),'terminal':mutate(F,[19])+'A'*35+rc(R),'internal3':mutate(F,[2,7,11])+'A'*35+rc(R),'ambiguous':'N'+base[1:]}
(p/'independent_primers.tsv').write_text('test\t'+F+'\t'+R+'\n');(p/'target.fasta').write_text(''.join('>'+k+'\n'+v+'\n' for k,v in records.items()));(p/'background.fasta').write_text('>negative\n'+'C'*150+'\n');subprocess.run(['work/scan',str(p)],check=True,capture_output=True)
h={r['accession']:r for r in csv.DictReader((p/'independent_hits.tsv').open(),delimiter='\t') if r['role']=='target'}
assert h['exact']['exact']=='1' and h['reverse']['exact']=='1';assert h['internal2']['le2last3']=='1';assert h['terminal']['le2last3']=='0';assert 'internal3' not in h or h['internal3']['le2last3']=='0';assert h['ambiguous']['ambiguous']=='1' and h['ambiguous']['le2last3']=='0'
print('PASS: exact/reverse/internal2/terminal/internal3/ambiguous controls')
