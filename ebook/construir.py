#!/usr/bin/env python3
"""Une los capítulos de ebook/manuscrito en un solo Markdown, genera el HTML de letra grande
(pandoc) y el PDF (Chromium). Uso: python3 ebook/construir.py"""
import glob, os, re, subprocess, sys, html
base = os.path.dirname(os.path.abspath(__file__))
src = sorted(glob.glob(os.path.join(base, 'manuscrito', '*.md')))
out = os.path.join(base, 'salida'); os.makedirs(out, exist_ok=True)
md = '\n\n'.join(open(f, encoding='utf-8').read().strip() for f in src) + '\n'
md_path = os.path.join(out, 'libro.md'); open(md_path, 'w', encoding='utf-8').write(md)
words = len(re.sub(r'[#*|>\-]', ' ', md).split())
css = """
:root{--bg:#fffdf8;--fg:#1c1c1c;--mute:#5f5a52;--accent:#8a2a2a;--line:#e3dccd;--box:#f6efe2}
@media (prefers-color-scheme:dark){:root:not([data-theme=light]){--bg:#17150f;--fg:#efe9dc;--mute:#b3aa98;--accent:#e08a7a;--line:#3a352b;--box:#24211a}}
html{font-size:21px}
body{background:var(--bg);color:var(--fg);font-family:Georgia,'Times New Roman',serif;line-height:1.7;max-width:720px;margin:0 auto;padding:40px 16px}
h1{font-size:2rem;line-height:1.2;color:var(--accent);margin:2.2em 0 .6em;page-break-before:always}
h1:first-of-type{page-break-before:avoid;margin-top:0}
h2{font-size:1.5rem;line-height:1.25;margin:1.6em 0 .5em;page-break-after:avoid}
h3{font-size:1.15rem;margin:1.4em 0 .4em;color:var(--accent);page-break-after:avoid}
h4{font-size:1.05rem;margin:1.2em 0 .3em;page-break-after:avoid}
p{margin:0 0 1em} em{font-style:italic} strong{font-weight:700}
ul,ol{padding-left:1.4em;margin:0 0 1em} li{margin:.35em 0}
hr{border:0;border-top:1px solid var(--line);margin:2em 0}
table{border-collapse:collapse;width:100%;margin:1em 0;font-size:.9rem}
th,td{border:1px solid var(--line);padding:.5em .6em;text-align:left;vertical-align:top}
th{background:var(--box)}
h3 + ol, h3 + ul{background:var(--box);border-radius:10px;padding:1em 1em 1em 2.2em}
@media print{html{font-size:14pt} body{max-width:none;padding:0} h1{page-break-before:always} a{color:inherit;text-decoration:none}}
@page{size:6in 9in;margin:0.75in 0.7in}
"""
title = "The Hollywood Secret to Aging Beautifully"
subprocess.run(['pandoc', md_path, '-f', 'markdown', '-t', 'html5', '-s', '--metadata', f'title={title}',
                '--metadata', 'lang=en-US', '-o', os.path.join(out, 'libro.html'), '--css', 'libro.css'], check=True)
h = open(os.path.join(out, 'libro.html'), encoding='utf-8').read()
h = h.replace('<link rel="stylesheet" href="libro.css" />', f'<style>{css}</style>')
h = re.sub(r'<header id="title-block-header">.*?</header>\n?', '', h, flags=re.S)
open(os.path.join(out, 'libro.html'), 'w', encoding='utf-8').write(h)
chrome = '/opt/pw-browsers/chromium-1194/chrome-linux/chrome'
if os.path.exists(chrome):
    subprocess.run([chrome, '--headless', '--no-sandbox', '--disable-gpu', '--no-pdf-header-footer',
                    '--print-to-pdf=' + os.path.join(out, 'libro.pdf'), 'file://' + os.path.join(out, 'libro.html')],
                   check=True, capture_output=True)
print(f'{len(src)} archivos, {words} palabras → salida/libro.md, libro.html, libro.pdf')
