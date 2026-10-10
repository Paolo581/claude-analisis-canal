#!/usr/bin/env python3
"""Gera a versão HTML de leitura de um roteiro .md do canal (## INTRO / ## PARTE n, [VERMELHO], [AZUL]).
Uso: python3 guiones/md2html.py guiones/arquivo.md  →  guiones/arquivo.html"""
import re,html,sys
src=sys.argv[1]; out=re.sub(r'\.md$','.html',src)
t=open(src,encoding='utf-8').read()
title=t.splitlines()[0].lstrip('# ').strip()
head,body=t.split('## INTRO',1); body=('## INTRO'+body).split('\n---\n')[0]
en=bool(re.search(r'^## PART \d',body,re.M)); lang='en' if en else 'pt-BR'
meta=[l.strip() for l in head.splitlines()[1:] if l.strip() and l.strip()!='---' and not l.startswith(('VERMELHO','RED'))]
sections=re.findall(r'## (INTRO|PARTE? \d)\n(.*?)(?=\n## |\Z)',body,re.S)
parts=[];total=0
for name,txt in sections:
    paras=[p.strip() for p in txt.split('\n\n') if p.strip()]
    w=sum(len(re.sub(r'^\[(VERMELHO|AZUL|RED|BLUE)\]\s*','',p).split()) for p in paras); total+=w
    parts.append((name,paras,w))
def para(p):
    m=re.match(r'^\[(VERMELHO|AZUL|RED|BLUE)\]\s*(.*)$',p,re.S)
    cls={'VERMELHO':'vermelho','RED':'vermelho','AZUL':'azul','BLUE':'azul'}
    return f'<p class="{cls[m.group(1)]}">{html.escape(m.group(2))}</p>' if m else f'<p>{html.escape(p)}</p>'
mm=lambda w:f'{w//150}:{int((w/150%1)*60):02d}'
toc=''.join(f'<a href="#s{i}">{html.escape(n)}<small>{round(w/150)} min</small></a>' for i,(n,_,w) in enumerate(parts))
acc=0;secs=[]
for i,(n,paras,w) in enumerate(parts):
    start=acc; acc+=w
    secs.append(f'<section id="s{i}"><h2>{html.escape(n)}<span>{mm(start)} → {mm(acc)} · {w} {"words" if en else "palavras"}</span></h2>'+''.join(para(p) for p in paras)+'</section>')
doc=f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<style>
:root{{--bg:#fff;--fg:#1a1a1a;--mute:#6b6b6b;--red:#b3261e;--blue:#1f4fa3;--line:#e6e6e6}}
@media (prefers-color-scheme:dark){{:root{{--bg:#141414;--fg:#e8e8e8;--mute:#9a9a9a;--red:#ff6b61;--blue:#7fa6ff;--line:#2a2a2a}}}}
body{{background:var(--bg);color:var(--fg);font:18px/1.7 Georgia,serif;max-width:720px;margin:0 auto;padding:32px 16px}}
h1{{font:700 26px/1.3 system-ui,sans-serif;margin:0 0 12px}}
.meta{{font:14px/1.5 system-ui,sans-serif;color:var(--mute);margin:0 0 6px}}
.legend{{font:14px/1.6 system-ui,sans-serif;color:var(--mute);border:1px solid var(--line);border-radius:8px;padding:10px 14px;margin:18px 0}}
.legend b.r{{color:var(--red)}} .legend b.b{{color:var(--blue)}}
nav{{display:flex;flex-wrap:wrap;gap:8px;margin:0 0 28px;font:14px system-ui,sans-serif}}
nav a{{color:var(--fg);text-decoration:none;border:1px solid var(--line);border-radius:999px;padding:4px 12px}}
nav a small{{color:var(--mute);margin-left:6px}}
h2{{font:700 15px/1.4 system-ui,sans-serif;letter-spacing:.08em;text-transform:uppercase;color:var(--mute);border-top:1px solid var(--line);padding-top:22px;margin:36px 0 18px}}
h2 span{{display:block;font-weight:400;letter-spacing:0;text-transform:none;font-size:13px;margin-top:4px}}
p{{margin:0 0 1em}}
p.vermelho{{color:var(--red)}} p.azul{{color:var(--blue)}}
.foot{{font:13px/1.6 system-ui,sans-serif;color:var(--mute);border-top:1px solid var(--line);padding-top:18px;margin-top:40px}}
@media print{{body{{max-width:none;font-size:12.5pt}} nav,.legend{{display:none}} h2{{break-before:page}} h2:first-of-type{{break-before:auto}}}}
</style>
</head>
<body>
<h1>{html.escape(title)}</h1>
{''.join(f'<p class="meta">{html.escape(m)}</p>' for m in meta)}
<p class="meta">{total} {"narrated words" if en else "palavras narradas"} · {total//150} min {"at" if en else "a"} 150 {"wpm" if en else "ppm"} · {round(total/134)} min {"at" if en else "a"} 134 {"wpm" if en else "ppm"}</p>
{"<div class=\"legend\"><b class=\"r\">Red</b> = hook and micro-hooks · <b class=\"b\">Blue</b> = payoff of the 1st hook and 2nd big hook · Black = narration. Tags are not read aloud.</div>" if en else "<div class=\"legend\"><b class=\"r\">Vermelho</b> = hook e microganchos · <b class=\"b\">Azul</b> = revelação do 1º gancho e 2º grande gancho · Preto = narração. As marcas não são narradas.</div>"}
<nav>{toc}</nav>
{''.join(secs)}
<p class="foot">{"Generated from" if en else "Gerado a partir de"} <code>{html.escape(src)}</code>. {"Narrate from the .md; paste the .md into «Medir señales» in the Estudio." if en else "Para a narração, use a versão .md; para o Estudio, cole o .md em «Medir señales»."}</p>
</body>
</html>'''
open(out,'w',encoding='utf-8').write(doc); print(out,total,'palavras',f'{total/150:.1f} min')
