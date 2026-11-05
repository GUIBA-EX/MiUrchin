"""Build the current manuscript PDF from Markdown and generated figures."""
from pathlib import Path
import re,subprocess,json
from xml.sax.saxutils import escape
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,Table,TableStyle,Image,KeepTogether
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
P=Path(__file__).resolve().parents[1];out=P/'publications';pdfmetrics.registerFont(UnicodeCIDFont('STSong-Light'))
styles=getSampleStyleSheet();styles.add(ParagraphStyle(name='BodyPaper',fontName='Times-Roman',fontSize=9.5,leading=13.3,spaceAfter=6));styles.add(ParagraphStyle(name='Chinese',fontName='STSong-Light',fontSize=10,leading=15,spaceAfter=8,wordWrap='CJK'));styles.add(ParagraphStyle(name='CaptionPaper',fontName='Times-Roman',fontSize=8.5,leading=11,spaceAfter=10));styles['Title'].fontSize=18;styles['Title'].leading=22
for n in ['Heading1','Heading2','Heading3']:styles[n].keepWithNext=True
for name in ['catalog_counts','exact_comparison','structure_margin']:
 subprocess.run(['pdftoppm','-scale-to','1500','-singlefile','-png',str(out/'figures'/f'{name}.pdf'),str(out/'figures'/name)],check=True)
def inline(s):
 s=escape(s);s=re.sub(r'\*\*(.+?)\*\*',r'<b>\1</b>',s);s=re.sub(r'`([^`]+)`',r'<font name="Courier">\1</font>',s);s=re.sub(r'\[([^\]]+)\]\(([^)]+)\)',lambda m:m[1]+' ('+m[2]+')',s);return s
lines=(out/'MiUrchin_preprint.md').read_text().splitlines();story=[];i=0
while i<len(lines):
 s=lines[i].strip()
 if not s:i+=1;continue
 if s.startswith('# '):story.append(Paragraph(inline(s[2:]),styles['Title']));i+=1;continue
 if s.startswith('## '):
  text=s[3:];style=styles['Heading1']
  if re.search('[\u4e00-\u9fff]',text):style=ParagraphStyle('ChineseHead',parent=styles['Chinese'],fontSize=14,leading=19,keepWithNext=True)
  story.append(KeepTogether([Paragraph(inline(text),style)]));i+=1;continue
 if s.startswith('### '):story.append(Paragraph(inline(s[4:]),styles['Heading2']));i+=1;continue
 if s.startswith('|'):
  rows=[]
  while i<len(lines) and lines[i].strip().startswith('|'):
   cells=[c.strip() for c in lines[i].strip().strip('|').split('|')]
   if not all(re.fullmatch('[-: ]+',c) for c in cells):rows.append([Paragraph(inline(c),styles['CaptionPaper']) for c in cells])
   i+=1
  t=Table(rows,colWidths=[110]*len(rows[0]),repeatRows=1);t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#dcebef')),('GRID',(0,0),(-1,-1),.3,colors.HexColor('#b5c7ce')),('VALIGN',(0,0),(-1,-1),'TOP'),('BOTTOMPADDING',(0,0),(-1,-1),6)]));story+=[t,Spacer(1,12)];continue
 if s.startswith('!['):
  path=re.search(r'\((.+)\)',s)[1];img=Image(str((out/path).with_suffix('.png')));ratio=img.imageHeight/img.imageWidth;img.drawWidth=400;img.drawHeight=400*ratio;i+=1
  while i<len(lines) and not lines[i].strip():i+=1
  caption=lines[i] if i<len(lines) and lines[i].startswith('**Figure') else ''
  if caption:i+=1
  story.append(KeepTogether([img,Paragraph(inline(caption),styles['CaptionPaper'])]));continue
 para=[s];i+=1
 while i<len(lines) and lines[i].strip() and not lines[i].startswith(('#','|','![')):para.append(lines[i].strip());i+=1
 text=' '.join(para);style=styles['Chinese'] if re.search('[\u4e00-\u9fff]',text) else styles['BodyPaper'];story.append(KeepTogether([Paragraph(inline(text),style)]))
# Keep heading chains with their first content block, including wrapped paragraphs.
grouped=[];j=0
while j<len(story):
 item=story[j]
 if isinstance(item,Paragraph) and getattr(item.style,'keepWithNext',False):
  block=[]
  while j<len(story) and isinstance(story[j],Paragraph) and getattr(story[j].style,'keepWithNext',False):block.append(story[j]);j+=1
  if j<len(story):
   nxt=story[j];block.extend(nxt._content if isinstance(nxt,KeepTogether) else [nxt]);j+=1
  if any(isinstance(x,Paragraph) and x.getPlainText()=='References' for x in block):
   while j<len(story):
    nxt=story[j];block.extend(nxt._content if isinstance(nxt,KeepTogether) else [nxt]);j+=1
  grouped.append(KeepTogether(block))
 else:grouped.append(item);j+=1
story=grouped
def footer(canvas,doc):
 canvas.setFont('Helvetica',8);canvas.setFillColor(colors.HexColor('#607580'));canvas.drawString(48,25,'MiUrchin v2.0.0 | Fei Xia | Local computational manuscript');canvas.drawRightString(547,25,str(doc.page))
doc=SimpleDocTemplate(str(out/'MiUrchin_preprint.pdf'),pagesize=(595.28,841.89),rightMargin=50,leftMargin=50,topMargin=43,bottomMargin=46,title='MiUrchin: terminal-triplet-first, branch-limited primer candidates',author='Fei Xia');doc.build(story,onFirstPage=footer,onLaterPages=footer)
from pypdf import PdfReader
r=PdfReader(out/'MiUrchin_preprint.pdf');assert len(r.pages)>0
(out/'current_pdf_validation.json').write_text(json.dumps({'pages':len(r.pages),'author':r.metadata.author,'status':'text-build-pass; visual review required'},indent=2));print('PDF built',len(r.pages),'pages')
