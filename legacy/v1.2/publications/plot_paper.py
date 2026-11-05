"""Publication figures from frozen results; no primer reselection."""
import math,csv,collections
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import SymLogNorm
from Bio import SeqIO
from paper_tables import ROOT,assays,rows,nesting
out=ROOT/'publications/figures';out.mkdir(exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':9,'axes.spines.top':False,'axes.spines.right':False,'svg.fonttype':'path','axes.titleweight':'bold'})
blue,orange='#338ca7','#e8a343'
def save(fig,name):
 fig.savefig(out/name,facecolor='white',bbox_inches='tight');plt.close(fig)
common=[x for x in rows('results/computational_evaluation/results/panel_comparison.csv') if x['panel']=='common']
fig,axs=plt.subplots(1,2,figsize=(11,3.6),layout='constrained')
for ax,metric,title in zip(axs,['covered','exact'],['16S · covered','16S · exact']):
 for i,q in enumerate(common):
  v=int(q[metric]);ax.bar(i,100*v/49,color=orange if q['name'].endswith('D') else blue);ax.text(i,100*v/49+2,str(v),ha='center',fontsize=8)
 ax.set_xticks(range(10),[q['name'] for q in common]);ax.set_ylim(0,106);ax.set_title(title);ax.set_ylabel('Species (%) · N = 49')
save(fig,'review_common_panel.svg')
rr=assays();fig=plt.figure(figsize=(12,11),layout='constrained');subfigs=fig.subfigures(2,2);profile=[]
for sf,gene in zip(subfigs.flat,['16S','12S','COI','28S']):
 path=ROOT/({'16S':'results/species_qc/curated_alignment.fasta','12S':'markers/12S_COI/12S/aligned.fasta','COI':'markers/12S_COI/COI/aligned.fasta','28S':'markers/28S/aligned.fa.out'}[gene]);al={x.id.removeprefix('_R_'):str(x.seq).upper() for x in SeqIO.parse(path,'fasta')};anchor='XR_004063668.1' if gene=='28S' else 'NC_001453.1';ref=al[anchor];cols=[i for i,b in enumerate(ref) if b!='-'];support=[];entropy=[]
 for pos,i in enumerate(cols,1):
  c=collections.Counter(s[i] for s in al.values() if s[i] in 'ACGT');n=sum(c.values());h=-sum(v/n*math.log2(v/n) for v in c.values()) if n>=2 else float('nan');support.append(n);entropy.append(h);profile.append(dict(gene=gene,reference=anchor,position=pos,n_called=n,entropy=h))
 axes=sf.subplots(3,1,sharex=True,gridspec_kw={'height_ratios':[1,.7,1.5]});x=np.arange(1,len(cols)+1);axes[0].plot(x,entropy,color=blue,lw=.7);axes[0].set_ylim(0,2.1);axes[0].set_ylabel('Entropy (bits)');axes[0].set_title(f'{gene} · {anchor} · {len(al)} references');axes[1].fill_between(x,support,color=blue,alpha=.3);axes[1].set_ylabel('Called species');a=[v for v in rr if v['gene']==gene and not v['name'].endswith('D')]
 for y,v in enumerate(a):
  fs,fe,rs,re=[int(v[k]) for k in ['F_start','F_end','R_start','R_end']];axes[2].plot([fe,rs],[y,y],color='#9aafb4',lw=1)
  for start,end in [(fs,fe),(re,rs)]:axes[2].annotate('',(end,y),(start,y),arrowprops=dict(arrowstyle='-|>',color=blue,lw=1.5))
 axes[2].set_yticks(range(len(a)),[v['name'] for v in a]);axes[2].set_ylim(len(a)-.4,-.6);axes[2].set_xlabel('Gene-relative reference position (1-based)')
 for ax in axes:ax.set_xlim(1,len(cols));ax.grid(axis='x',alpha=.12)
save(fig,'review_entropy.svg')
with (ROOT/'publications/evidence/site_profiles.csv').open('w') as f:w=csv.DictWriter(f,fieldnames=list(profile[0]));w.writeheader();w.writerows(profile)
fig,axs=plt.subplots(2,2,figsize=(10,6.2),layout='constrained')
for ax,gene in zip(axs.flat,['16S','12S','COI','28S']):
 ns=[x for x in nesting() if x['gene']==gene];x=np.arange(len(ns))
 for metric,offset,color in [('covered',-.18,blue),('exact',.18,orange)]:
  vals=[int(v['D_'+metric])-int(v['ordinary_'+metric]) for v in ns];ax.bar(x+offset,vals,width=.36,color=color,label=metric.capitalize())
  for j,y in enumerate(vals):ax.annotate(str(y),(j+offset,y),xytext=(0,3 if y>=0 else -10),textcoords='offset points',ha='center',fontsize=8)
 ax.axhline(0,color='#888',lw=.6);ax.set_xticks(x,[v['pair']+('*' if v['nested']=='No' else '') for v in ns]);ax.set_title(gene);ax.set_ylabel('D minus ordinary · species');ax.margins(y=.25)
axs.flat[0].legend(frameon=False);save(fig,'review_nesting.svg')
fig,axs=plt.subplots(2,2,figsize=(10,7.2),layout='constrained');maximum=max(int(v[k]) for v in rr for k in ['WC','GT','WC3','GT2']);norm=SymLogNorm(linthresh=1,vmin=0,vmax=maximum)
for ax,gene in zip(axs.flat,['16S','12S','COI','28S']):
 a=[v for v in rr if v['gene']==gene];data=np.array([[int(v[k]) for k in ['WC','GT','WC3','GT2']] for v in a]);im=ax.imshow(data,cmap='YlOrRd',norm=norm,aspect='auto');ax.set_yticks(range(len(a)),[v['name'] for v in a]);ax.set_xticks(range(4),['WC','GT','WC+','GT+']);ax.set_title(gene)
 for i,row in enumerate(data):
  for j,v in enumerate(row):ax.text(j,i,str(v),ha='center',va='center',color='white' if norm(v)>.7 else '#222',fontsize=8)
fig.colorbar(im,ax=axs.ravel().tolist(),label='Background hits · marker-specific panel',shrink=.8);save(fig,'review_background.svg')
cv=rows('results/computational_evaluation/results/cv_summary.csv');fig,ax=plt.subplots(figsize=(9,3.6),layout='constrained');x=np.arange(5)
for key,off,col in [('covered',-.18,blue),('exact',.18,orange)]:
 vals=[100*int(v[key])/int(v['n']) for v in cv];ax.bar(x+off,vals,.36,color=col,label=key.capitalize())
 for i,v in enumerate(cv):ax.text(i+off,vals[i]+2,f"{v[key]}/{v['n']}",ha='center',fontsize=8)
ax.set_xticks(x,[v['region'] for v in cv]);ax.set_ylim(0,112);ax.set_ylabel('Held-out species (%)');ax.legend(frameon=False);save(fig,'review_holdout.svg')
fig,ax=plt.subplots(figsize=(9,3.3),layout='constrained')
for i,v in enumerate(common):
 n=int(v['covered_identity_unique']);ax.bar(i,100*n/49,color=orange if v['name'].endswith('D') else blue);ax.text(i,100*n/49+2,str(n),ha='center',fontsize=8)
ax.set_xticks(range(10),[v['name'] for v in common]);ax.set_ylim(0,106);ax.set_ylabel('Covered and reference-unique (%) · N = 49');save(fig,'review_joint_resolution.svg')
