from pathlib import Path
import subprocess,sys
p=Path(__file__).resolve().parent/'analysis'
def run(*args):subprocess.run(args,cwd=p,check=True)
run(sys.executable,'validate_targets.py')
run('c++','-O3','-std=c++17','independent_scan.cpp','-o','independent_scan')
run(str(p/'independent_scan'),str(p))
for n in ['check_independent.py','evaluate_portfolios.py','thermal_pairs.py','thermal_portfolios.py','portfolio_evidence.py','validate_portfolios.py','export_tables.py']:run(sys.executable,n)
print('PASS: selected candidate revalidation complete')
