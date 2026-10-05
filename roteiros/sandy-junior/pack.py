import re, html, json
TITLE="Assim FOI a VIDA de SANDY & JUNIOR — A Verdade SOMBRIA Por Trás da Dupla Mais Pura do Brasil"
files=['parte1.txt','parte2.txt','parte3.txt','parte4.txt','parte5.txt']
raw=[p.strip() for f in files for p in open(f).read().split('\n\n') if p.strip()]
paras=[re.sub(r'^[RA]: ','',p) for p in raw]
open('voz.txt','w').write('\n\n'.join(paras)+'\n')
open('roteiro_completo.txt','w').write('\n\n'.join(raw)+'\n')
W=sum(len(p.split()) for p in paras)
body=''.join(f'<p>{html.escape(p)}</p>\n' for p in paras)
open('SJ_Roteiro_Voz.html','w').write(f'''<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(TITLE)}</title>
<style>body{{background:#fff;color:#000;font-family:Georgia,serif;font-size:20px;line-height:1.7;max-width:760px;margin:0 auto;padding:32px 16px}}h1{{font-size:24px;line-height:1.3;margin-bottom:32px}}p{{margin:0 0 18px}}</style>
</head><body>
<h1>{html.escape(TITLE)}</h1>
{body}</body></html>''')
CH=[('Sandy e Junior passaram dezoito anos','O segredo entre os irmãos','Duas silhuetas de crianças num palco antigo, de costas uma para a outra (ilustrativo)'),
('Para entender como dois irmãos','A casa em Campinas','Fotos de arquivo de Campinas nos anos 80 · Chitãozinho & Xororó (imprensa, com crédito)'),
('Fim de mil novecentos e oitenta e nove.','O Som Brasil e Maria Chiquinha','Trecho curto do Som Brasil de 1989 (arquivo, com crédito)'),
('O programa foi ao ar.','A fita que virou máquina','Fita cassete e rádio antigo (ilustrativo) · Letreiro "Disco de Ouro"'),
('Depois do primeiro disco','Um disco por ano','Capas dos discos de 1991 a 1997 (com crédito)'),
('Era a segunda metade dos anos noventa.','Expulsos do programa','Corredor de camarim vazio com seguranças em silhueta (ilustrativo)'),
('Mil novecentos e noventa e sete.','A pergunta aos 14 anos','Microfone de entrevista diante de uma cadeira vazia · Letreiro "14 ANOS"'),
('Enquanto isso, a dupla ficava cada vez maior.','A série e os milhões','Abertura da série (arquivo, com crédito) · Letreiro "quase 3 milhões"'),
('Houve um momento em que Sandy estava','As 14 capas','Parede de revistas desfocadas sem marca legível (ilustrativo)'),
('Dezenove de janeiro de dois mil e um.','Rock in Rio 2001','Imagens de arquivo do Rock in Rio 3 (com crédito)'),
('Dois meses depois, a vida de Sandy','Estrela-Guia e a cena engavetada','Gaveta de arquivo fechada com fita VHS (ilustrativo) · Letreiro "ESTRELA-VIRGEM"'),
('No ano seguinte, os irmãos tentaram','Internacional e o fim da série','Capa do disco Internacional (com crédito)'),
('O irmão que sofria em silêncio era Junior.','O irmão que sofria','Silhueta masculina na sombra de um holofote · baquetas sobre a bateria'),
('Antes disso, Junior precisava fazer uma coisa.','A decisão de 2007','Mesa de jantar vazia (ilustrativo) · Letreiro "abril de 2007"'),
('Dezoito de dezembro de dois mil e sete.','O último show','Palco vazio com luzes se apagando (ilustrativo)'),
('Dois mil e oito.','Nove Mil Anjos','Fotos de imprensa da banda (com crédito) · capa do disco 9MA'),
('Doze de setembro de dois mil e oito.','O casamento e o invasor','Portão fechado de fazenda à noite (ilustrativo)'),
('Março de dois mil e onze. Carnaval.','Devassa','Letreiro "US$ 1 milhão" · garrafa de cerveja genérica sem marca'),
('Fim de julho de dois mil e onze.','A capa da Playboy','Banca de jornal desfocada (ilustrativo, sem a capa real) · Letreiro "2º no mundo"'),
('Seis de março de dois mil e treze.','2013','Calendário de 2013 com três datas marcadas'),
('Cinco de maio de dois mil e treze.','O ano que ele nunca esqueceu','Guitarra e baixo encostados num estúdio vazio (sem detalhes da morte)'),
('A dor não terminou ali.','O que veio depois','Prato de comida intocado sobre a mesa (ilustrativo)'),
('Dois mil e catorze.','A volta de 2019','Imagens de imprensa da turnê Nossa História (com crédito) · Letreiro "100 mil pessoas"'),
('Lembra de Maria Chiquinha?','O fim da música','Letreiro com a letra resumida em tela escura (sem cantar a música)'),
('Setembro de dois mil e vinte e três.','O fim de 24 anos','Duas alianças sobre uma mesa (ilustrativo)'),
('Vinte e quatro de setembro de dois mil e vinte e seis.','S&J 2027','Letreiro "S&J · São Paulo · 2027"'),
('Talvez essa seja a lição mais dura','O preço da fama','Duas crianças em silhueta saindo de um palco iluminado'),
]
cum=[];w=0
for p in paras:
    cum.append(w); w+=len(p.split())
out=[]
for key,name,img in CH:
    m=[k for k,p in enumerate(paras) if p.startswith(key)]
    assert len(m)==1,(key,m)
    s=round(cum[m[0]]/195*60)
    out.append((f'{s//60}:{s%60:02d}',name,img))
CHAPS='\n'.join(f'{t} {n}' for t,n,_ in out)
open('chapters.txt','w').write(CHAPS+'\n')
print(CHAPS); print('total min',round(w/195,1), W)
DESC='''Sandy e Junior passaram 18 anos sendo a dupla de irmãos mais amada do Brasil. Mas, longe dos palcos, um dos dois sofria em silêncio por viver à sombra do outro.

Neste vídeo: a música macabra que eles cantaram aos 6 e 5 anos no Som Brasil, a pergunta sobre virgindade feita a Sandy aos 14 anos, a paródia "Estrela-Virgem" que a Globo engavetou, o irmão chamado de "sombra", a decisão que acabou com a dupla em 2007, o escândalo da Devassa e da Playboy em 2011, a tragédia da Nove Mil Anjos em 2013, as crises de pânico dos dois irmãos e o mistério do projeto S&J 2027.

Importante: todas as informações vêm de entrevistas dadas pelos próprios artistas, da série documental "Sandy & Junior: A História" (Globoplay) e de reportagens publicadas, citadas no vídeo.

Este vídeo menciona suicídio. Se você estiver passando por um momento difícil, o CVV atende 24 horas pelo telefone 188 ou em cvv.org.br.

{CHAPS}

#SandyeJunior #Sandy #JuniorLima'''.replace('{CHAPS}',CHAPS)
TAGS='sandy e junior, sandy, junior lima, sandy e junior história, sandy e junior 2027, sandy e junior volta, maria chiquinha, sandy virgem, sandy playboy, nove mil anjos, champignon, sandy e lucas lima, xororó, assim foi a vida, sandy e junior documentário'
assert len(TAGS)<=500, len(TAGS)
open('desc.txt','w').write(DESC+'\n'); open('tags.txt','w').write(TAGS+'\n')
rows=''.join(f'<tr><td class="t">{t}</td><td><b>{html.escape(n)}</b><br>{html.escape(i)}</td></tr>\n' for t,n,i in out)
CAUT='''<li>Suicídio (Peu Sousa e Champignon): nunca mostrar método, local ou imagens da morte; usar só fotos de imprensa em vida, com crédito. Manter o aviso do CVV na descrição e, se possível, num letreiro no trecho.</li>
<li>Não sugerir causa entre as mortes de 2013 e o pânico de Junior: o roteiro diz que ele nunca ligou uma coisa à outra; o letreiro deve respeitar isso.</li>
<li>Playboy: não mostrar a capa real nem a frase em destaque; Sandy não posou e disse que a frase não foi bem a resposta dela.</li>
<li>Maria Chiquinha: não tocar a gravação com o final violento; usar a letra resumida em tela e o trecho em que Junior para a música, se houver imagem licenciada.</li>
<li>Xororó e Noely aparecem como apoio dos filhos; nenhum letreiro deve sugerir culpa dos pais.</li>
<li>Theo, Otto e Lara (filhos): não mostrar rosto de crianças.</li>
<li>Invasor de 2010, fãs obsessivos e o diretor de A Praça É Nossa: não mostrar rostos nem nomes além do que está no roteiro.</li>
<li>Thumbnail: nada de rosto gerado por IA de Sandy ou Junior; preferir silhuetas.</li>'''
SEC=lambda h,i,c: f'<h2>{h} <button data-t="{i}">Copiar</button></h2><pre id="{i}">{html.escape(c)}</pre>'
open('SJ_Pacote_Producao.html','w').write(f'''<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Pacote de Produção — Sandy & Junior</title>
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
json.dump({'title':TITLE,'desc':DESC,'tags':TAGS,'chaps':CHAPS,'rows':rows,'caut':CAUT,'paras':paras,'words':W},open('pack.json','w'),ensure_ascii=False)
