import re, html
TITLE="SANDY & JUNIOR: O Que Eles NUNCA Contaram Sobre o Fim da Dupla (e Por Que Voltam em 2027)"
files=['parte1.txt','parte2.txt','parte3.txt','parte4.txt','parte5.txt']
raw=[]
for f in files:
    for p in open(f).read().split('\n\n'):
        p=p.strip()
        if p: raw.append(p)
paras=[re.sub(r'^[RA]: ','',p) for p in raw]
open('voz.txt','w').write('\n\n'.join(paras)+'\n')
W=sum(len(p.split()) for p in paras)
body=''.join(f'<p>{html.escape(p)}</p>\n' for p in paras)
open('SJ27_Roteiro_Voz.html','w').write(f'''<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(TITLE)}</title>
<style>body{{background:#fff;color:#000;font-family:Georgia,serif;font-size:20px;line-height:1.7;max-width:760px;margin:0 auto;padding:32px 16px}}h1{{font-size:24px;line-height:1.3;margin-bottom:32px}}p{{margin:0 0 18px}}</style>
</head><body>
<h1>{html.escape(TITLE)}</h1>
{body}</body></html>''')
CH=[('Sandy e Junior estavam no auge','O segredo do fim','Duas silhuetas de costas num palco vazio · Letreiro "2007"'),
('Abril de dois mil e sete.','O anúncio de 2007','Manchetes genéricas de jornal (sem logos) · Fotos de imprensa da dupla (com crédito)'),
('Para entender o que aconteceu naquela conversa','A casa em Campinas','Casa de interior ao entardecer (banco de imagens) · Fotos de Chitãozinho & Xororó (com crédito)'),
('Fim de mil novecentos e oitenta e nove.','O Som Brasil e Maria Chiquinha','Trecho curto do Som Brasil (com crédito) · Letreiro "Sandy 6 anos · Junior 5"'),
('O programa foi ao ar.','A fita que virou máquina','Fita cassete e rádio antigo (ilustrativo)'),
('Depois do primeiro disco','Um disco por ano','Capas dos discos (com crédito) · Calendário passando rápido'),
('Era a segunda metade dos anos noventa.','Expulsos do programa','Corredor de estúdio de TV vazio (ilustrativo)'),
('Mil novecentos e noventa e sete.','A pergunta aos 14 anos','Microfone de TV antigo · Letreiro "14 anos"'),
('Enquanto isso, a dupla não parava de crescer.','A série e os milhões','Trecho curto da série (com crédito) · Letreiros "2 milhões" e "3 milhões"'),
('Houve uma época em que Sandy','As 14 capas','Banca de revistas genérica (sem capas reais identificáveis)'),
('Dezenove de janeiro de dois mil e um.','Rock in Rio 2001','Imagens de arquivo do Rock in Rio (com crédito)'),
('Dois meses depois, a vida de Sandy','Estrela-Guia','Trecho curto da novela (com crédito)'),
('O Casseta e Planeta era o programa','A fita engavetada','Fita de vídeo numa gaveta com selo "VETADO" (ilustrativo)'),
('No ano seguinte, os irmãos tentaram','Internacional e o cansaço','Capa do disco Internacional (com crédito)'),
('O irmão que carregava esse peso era Junior.','A sombra da Sandy','Trecho do documentário de 2020 (com crédito) · Bateria no escuro'),
('Para a família, foi um choque.','A reação dos pais','Fotos de Xororó e Noely (com crédito) · Letreiro "se dependesse de mim"'),
('Em abril de dois mil e sete, veio o anúncio','O último show','Trecho do Acústico MTV (com crédito) · Letreiro "18/12/2007"'),
('Dois mil e oito.','Nove Mil Anjos','Fotos de imprensa da banda (com crédito)'),
('Doze de setembro de dois mil e oito.','O casamento e o invasor','Alianças (ilustrativo) · Porta entreaberta à noite'),
('Março de dois mil e onze. Carnaval.','Devassa e Playboy','Letreiros "US$ 1 milhão" e "2.º no Twitter mundial" (sem reproduzir a capa)'),
('Seis de março de dois mil e treze.','2013','Palco vazio com instrumentos apagados (ilustrativo) · CVV 188 na tela'),
('A dor não terminou ali.','O pânico de Junior','Prato de comida intocado · Letreiro "perto dos 30 anos"'),
('Dois mil e catorze.','A volta de 2019','Imagens da turnê Nossa História (com crédito) · Letreiro "R$ 120 milhões"'),
('Lá em mil novecentos e oitenta e nove, Junior fazia Genaro','O final de Maria Chiquinha','Letreiro com a letra parafraseada · Trecho do show em que Junior para (com crédito)'),
('Setembro de dois mil e vinte e três.','Os recomeços','Fotos de imprensa (com crédito)'),
('Vinte e quatro de setembro de dois mil e vinte e seis.','S&J 2027','Print do post oficial (com crédito) · Letreiro "novembro"'),
('Existe uma diferença enorme','Por que 2027','Linha do tempo 1989 · 2007 · 2027'),
]
cum=[];w=0
for p in paras:
    cum.append(w); w+=len(p.split())
out=[]
for key,name,img in CH:
    i=next(k for k,p in enumerate(paras) if p.startswith(key))
    s=round(cum[i]/195*60)
    out.append((f'{s//60}:{s%60:02d}',name,img))
CHAPS='\n'.join(f'{t} {n}' for t,n,_ in out)
open('chapters.txt','w').write(CHAPS+'\n')
print(CHAPS); print('total min',round(w/195,1))
DESC='''Em abril de 2007, Sandy e Junior anunciaram o fim da dupla no auge, sem briga pública e sem explicar o verdadeiro motivo. Só em 2020, no documentário "Sandy & Junior: A História", veio a público quem levou a decisão aos pais, e a frase cruel que essa pessoa ouvia nos bastidores. Neste vídeo: a fita do Som Brasil, a pergunta feita a Sandy aos 14 anos, a paródia que a Globo engavetou, a reação de Xororó, a banda Nove Mil Anjos e o ano de 2013, o pânico escondido antes da volta de 2019, o final de "Maria Chiquinha" e o mistério do projeto S&J 2027.

Importante: as informações vêm de entrevistas dadas pelos próprios artistas, do documentário "Sandy & Junior: A História" (Globoplay) e de reportagens publicadas. Até a produção deste vídeo, o projeto de 2027 não tinha formato, turnê ou data confirmados; os irmãos prometeram contar tudo em novembro de 2026.

Este vídeo menciona suicídio. Se você estiver passando por um momento difícil, o CVV atende 24 horas pelo telefone 188 ou em cvv.org.br.

{CHAPS}

#SandyEJunior #SandyEJunior2027 #HistóriaReal'''.replace('{CHAPS}',CHAPS)
TAGS='sandy e junior, sandy e junior 2027, sandy e junior volta, sandy e junior fim da dupla, por que sandy e junior se separaram, sandy e junior novembro, junior lima, sandy, nove mil anjos, maria chiquinha, xororó, sandy e junior a história, sandy e junior nossa história'
assert len(TAGS)<=500, len(TAGS)
open('desc.txt','w').write(DESC+'\n'); open('tags.txt','w').write(TAGS+'\n')
rows=''.join(f'<tr><td class="t">{t}</td><td><b>{html.escape(n)}</b><br>{html.escape(i)}</td></tr>\n' for t,n,i in out)
CAUT='''<li>Mortes de 2013: não mostrar locais, não descrever o método e manter o CVV 188 na tela.</li>
<li>Maria Chiquinha: mostrar a letra só parafraseada e nunca encenar a ameaça.</li>
<li>Playboy: não reproduzir a capa; usar só letreiros.</li>
<li>Projeto 2027: nunca escrever "turnê confirmada"; usar "projeto anunciado".</li>
<li>Rostos reais: só fotos de imprensa ou arquivo com crédito, nunca rosto gerado por IA. Trechos de TV e de música curtos e com crédito.</li>
<li>Invasor de 2010 e fãs: imagens neutras, sem dramatização.</li>'''
SEC=lambda h,i,c: f'<h2>{h} <button data-t="{i}">Copiar</button></h2><pre id="{i}">{html.escape(c)}</pre>'
open('SJ27_Pacote_Producao.html','w').write(f'''<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Pacote de Produção — Sandy & Junior</title>
<style>body{{background:#fff;color:#111;font-family:system-ui,Segoe UI,Arial,sans-serif;max-width:860px;margin:0 auto;padding:24px 16px;line-height:1.55}}h1{{font-size:24px}}h2{{font-size:19px;margin-top:32px;border-bottom:2px solid #eee;padding-bottom:4px}}pre{{white-space:pre-wrap;background:#f6f6f6;padding:12px;border-radius:6px;font-family:inherit}}table{{width:100%;border-collapse:collapse}}td{{border-bottom:1px solid #eee;padding:8px;vertical-align:top}}td.t{{font-weight:700;white-space:nowrap;width:60px}}.note{{color:#555;font-size:14px}}li{{margin-bottom:6px}}button{{font-size:13px;margin-left:8px}}</style></head><body>
<h1>Pacote de Produção: Sandy & Junior</h1>
<p><b>Título:</b> {html.escape(TITLE)}</p>
{SEC('Descrição (SEO, já com capítulos)','desc',DESC)}
{SEC('Tags','tags',TAGS)}<p class="note">{len(TAGS)} caracteres (limite do YouTube: 500).</p>
{SEC('Capítulos','chap',CHAPS)}
<p class="note">Tempos calculados a 195 palavras por minuto (~{round(w/195)} min). Ajuste pelo áudio real.</p>
<h2>Lista de imagens para o editor</h2><table>{rows}</table>
<h2>Cuidados na edição</h2><ul>{CAUT}</ul>
<script>document.querySelectorAll('button[data-t]').forEach(b=>b.onclick=()=>{{navigator.clipboard.writeText(document.getElementById(b.dataset.t).textContent).then(()=>{{b.textContent='Copiado';setTimeout(()=>b.textContent='Copiar',1500)}})}})</script>
</body></html>''')
import json; json.dump({'title':TITLE,'desc':DESC,'tags':TAGS,'chaps':CHAPS,'rows':rows,'caut':CAUT,'paras':paras,'words':W},open('pack.json','w'),ensure_ascii=False)
