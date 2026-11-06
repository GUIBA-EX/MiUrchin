"""Build revised manuscript and notes DOCX from the retained Markdown and PNG figures. Requires python-docx; inspect rendered pages after rebuilding."""
from pathlib import Path
from docx import Document
from docx.shared import Inches,Pt,RGBColor
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
import re
import argparse
parser=argparse.ArgumentParser();parser.add_argument('--package',type=Path,default=Path(__file__).resolve().parents[1]/'publications/manuscript_20261106');out=parser.parse_args().package
def inline(p,text):
 text=re.sub(r'\[([^]]+)\]\(([^)]+)\)',r'\1 (\2)',text).replace('`','')
 for part in re.split(r'(\*\*[^*]+\*\*|\*[^*]+\*)',text):
  r=p.add_run(part.strip('*') if part.startswith('*') else part)
  if part.startswith('**'):r.bold=True
  elif part.startswith('*'):r.italic=True

def build(text,dest,main=False):
 d=Document();sec=d.sections[0];sec.top_margin=sec.bottom_margin=Inches(.8);sec.left_margin=sec.right_margin=Inches(.8)
 for el in list(d.styles.element.iter()):
  if el.tag==qn('w:pBdr'):el.getparent().remove(el)
 for st in d.styles:
  if st.type==1:
   f=st.element.get_or_add_rPr().get_or_add_rFonts()
   for key in ['asciiTheme','hAnsiTheme','eastAsiaTheme','cstheme']:f.attrib.pop(qn('w:'+key),None)
   f.set(qn('w:ascii'),'Times New Roman');f.set(qn('w:hAnsi'),'Times New Roman');f.set(qn('w:eastAsia'),'Songti SC')
 st=d.styles['Normal'];st.font.size=Pt(11);st.paragraph_format.line_spacing=1.15;st.paragraph_format.space_after=Pt(6)
 for name in ['Title','Heading 1','Heading 2','Heading 3']:d.styles[name].font.color.rgb=RGBColor(0,0,0)
 d.styles['Title'].font.size=Pt(19)
 # Page numbers make reviewer comments traceable.
 footer=sec.footer.paragraphs[0];footer.alignment=2;field=OxmlElement('w:fldSimple');field.set(qn('w:instr'),'PAGE');footer._p.append(field)
 text=text.split('## Figures\n')[0];lines=text.splitlines();i=0
 while i<len(lines):
  line=lines[i].strip()
  if not line:i+=1;continue
  if line.startswith('|'):
   rows=[]
   while i<len(lines) and lines[i].strip().startswith('|'):
    vals=[x.strip() for x in lines[i].strip().strip('|').split('|')]
    if not all(re.fullmatch(r'[:\- ]+',x) for x in vals):rows.append(vals)
    i+=1
   t=d.add_table(rows=0,cols=len(rows[0]));t.style='Table Grid'
   for vals in rows:
    cells=t.add_row().cells
    for c,v in zip(cells,vals):inline(c.paragraphs[0],v)
   for row in t.rows:
    for c in row.cells:
     for p in c.paragraphs:
      p.paragraph_format.space_after=Pt(2);p.paragraph_format.line_spacing=1.0
      for r in p.runs:r.font.size=Pt(9)
   continue
  if line.startswith('# '):p=d.add_paragraph(style='Title');inline(p,line[2:])
  elif line.startswith('### '):p=d.add_heading('',2);inline(p,line[4:])
  elif line.startswith('## '):p=d.add_heading('',1);inline(p,line[3:])
  else:inline(d.add_paragraph(),line)
  i+=1
 if main:
  legends=re.findall(r'^\*\*Figure (\d)\.\*\* (.+)$',text,re.M)
  names=['review_common_panel','review_entropy','review_nesting','review_background','review_holdout','review_joint_resolution']
  for (n,caption),name in zip(legends,names):
   d.add_page_break();inline(d.add_paragraph(),f'Figure {n}. {caption}');d.add_picture(str(out/f'figures/Figure_{n}.png'),width=Inches(6.65))
 d.save(dest)
build((out/'MiUrchin_manuscript.md').read_text(),out/'MiUrchin_manuscript.docx',True)
build((out/'MiUrchin_中文修订说明.md').read_text(),out/'MiUrchin_中文组装说明.docx')
