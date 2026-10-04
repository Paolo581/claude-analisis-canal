import re, html
TITLE="TONY TORNADO: O Passado SOMBRIO Que Ele Escondeu Por Décadas"
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
open('Tony_Roteiro_Voz.html','w').write(f'''<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(TITLE)}</title>
<style>body{{background:#fff;color:#000;font-family:Georgia,serif;font-size:20px;line-height:1.7;max-width:760px;margin:0 auto;padding:32px 16px}}h1{{font-size:24px;line-height:1.3;margin-bottom:32px}}p{{margin:0 0 18px}}</style>
</head><body>
<h1>{html.escape(TITLE)}</h1>
{body}</body></html>''')
CH=[('Tony Tornado passou','O passado sombrio','Silhueta de homem negro idoso num palco escuro, cabelo black · Letreiro "O PASSADO SOMBRIO"'),
('Para entender como um homem chega','Uma rua e onze carros','Estrada de terra vermelha no interior paulista (banco de imagens) · Mapa: Mirante do Paranapanema'),
('Antônio foi de carona','O menino engraxate','Fotos de arquivo do Rio anos 40: Central do Brasil, engraxates (com crédito)'),
('Na rua, havia outro problema','"Me arrumem uma escola"','Rua do Rio antigo à noite · Letreiro com a frase'),
('Quando completou a idade','Paraquedista com Silvio Santos','Arquivo de paraquedistas em Deodoro (com crédito) · Foto pública de Silvio Santos jovem (com crédito)'),
('Em mil novecentos e cinquenta e sete, recebeu','Missão de paz no Egito','Arquivo do Batalhão Suez / capacetes azuis da ONU (com crédito)'),
('Antes de chegar a esse bairro','Tony Checker','Arquivo de twist anos 60 · Chubby Checker (com crédito)'),
('Em mil novecentos e sessenta e três, apareceu','O passaporte confiscado','Navio/aeroporto anos 60 · Passaporte antigo genérico'),
('O lugar onde ele foi parar','O Harlem','Fotos de arquivo do Harlem anos 60, Rua 125, Teatro Apollo (com crédito)'),
('Enquanto lutava para sobreviver','Malcolm X e o Black Power','Arquivo: Harlem 1964, Malcolm X discursando, Stokely Carmichael (com crédito)'),
('Foi nesse Harlem que aconteceu','Tim Maia na cadeia','Fotos de Tim Maia jovem (com crédito) · Letreiro "Ô, Comfort..."'),
('O Harlem respirava música','"Ou você canta ou trafica"','Ray Charles e James Brown no Apollo (arquivo, com crédito) · Letreiro com a frase'),
('"Morei na Rua cento e vinte e cinco','O segredo do Harlem','Rua do Harlem à noite · Cadillac branco anos 60 (banco de imagens) · Lava-jato antigo'),
('Mil novecentos e sessenta e oito.','De volta à ditadura','Arquivo: tanques e AI-5, manchetes de dezembro de 1968 (com crédito)'),
('Numa boate de Copacabana','Johnny Bradford','Boate dos anos 60, Copacabana à noite (arquivo)'),
('O Festival Internacional da Canção','BR-3 no Maracanãzinho','Trecho curto do FIC 1970 (com crédito) · Rodovia na serra de Petrópolis'),
('Tony e Arlete viveram','Arlete Salles e o racismo','Fotos públicas do casal anos 70 (com crédito) · Letreiro "recados ofensivos no meu carro"'),
('Ibrahim Sued era','A frase de Ibrahim Sued','Jornal antigo genérico · Letreiro com a frase atribuída por Tony'),
('Naquela noite, quem estava no palco','Algemado no palco','Elis Regina no Maracanãzinho (arquivo, com crédito) · Punho erguido (silhueta) · Algemas'),
('"Canta aí, rodopia."','O DOPS e a melancia','Prédio do DOPS no Rio (arquivo) · Melancia cortada (ilustrativo)'),
('A primeira parada foi ali do lado','O exílio','Mapa animado: Uruguai, Tchecoslováquia, Cuba'),
('Nos anos setenta, nos subúrbios','Black Rio','Fotos de bailes black anos 70 (com crédito)'),
('Em mil novecentos e setenta e seis, ele gravou','Deus Negro','Compacto de vinil quebrado (ilustrativo) · Letreiro "Se Jesus fosse um homem de cor"'),
('Esse outro palco era a televisão.','Da prisão às novelas','Trechos curtos de Quilombo, Roque Santeiro e Agosto (com crédito)'),
('Domingo, seis de setembro','Rock in Rio aos 96 anos','Imagens do Rock in Rio 2026, Palco Sunset na chuva (com crédito) · Tony e Lincoln cantando Sossego'),
('Ao longo desse vídeo','O tamanho do caminho','Montagem com as fases da vida dele · Medalha Tiradentes (Alerj, com crédito)'),
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
DESC='''Antes de virar o rosto querido das novelas, Tony Tornado guardou durante décadas um passado que quase ninguém conhecia. Menino de rua aos 11 anos no Rio, paraquedista do Exército ao lado de Silvio Santos e soldado da ONU no Egito, ele foi parar no Harlem, em Nova York, sem passaporte. Lá, segundo ele mesmo contou, virou cafetão, andou de Cadillac branco e tirou Tim Maia da cadeia.

Deportado em 1968, venceu o Festival Internacional da Canção com BR-3, sofreu racismo pelo romance com Arlete Salles, foi atacado por Ibrahim Sued, saiu algemado de um palco ao lado de Elis Regina, passou nove vezes pelo DOPS e foi para o exílio. Décadas depois, aos 96 anos, voltou ao Rock in Rio para cantar Sossego, de Tim Maia, ao lado do filho Lincoln.

Os relatos sobre o Harlem e a ditadura são do próprio Tony Tornado, em entrevistas a veículos como Trip, ELLE, Valor Econômico, Sesc e O Globo.

{CHAPS}

#TonyTornado #TimMaia #HistóriaDoBrasil'''.replace('{CHAPS}',CHAPS)
TAGS='tony tornado, tony tornado história, tony tornado harlem, tony tornado cafetão, tony tornado tim maia, tony tornado ditadura, tony tornado preso, tony tornado rock in rio, tony tornado br-3, tony tornado arlete salles, tony tornado elis regina, black rio, tim maia, assim foi a vida, biografia tony tornado'
assert len(TAGS)<=500, len(TAGS)
open('desc.txt','w').write(DESC+'\n'); open('tags.txt','w').write(TAGS+'\n')
rows=''.join(f'<tr><td class="t">{t}</td><td><b>{html.escape(n)}</b><br>{html.escape(i)}</td></tr>\n' for t,n,i in out)
CAUT='''<li>Os crimes do Harlem são relato do próprio Tony: manter sempre "segundo ele contou" nos letreiros; nada de "criminoso" ou "traficante" como rótulo fixo na tela.</li>
<li>A frase de Ibrahim Sued é atribuída por Tony (entrevista ao Valor, 2002); no letreiro, escrever "segundo Tony Tornado".</li>
<li>Arlete Salles: mostrar as duas versões (sete anos para ele, alguns meses para ela); não chamar de "esposa" em letreiro.</li>
<li>Exílio: as fontes divergem sobre os países; no mapa, usar só Uruguai, Tchecoslováquia e Cuba.</li>
<li>Rosto do Tony: só fotos reais licenciadas ou de imprensa com crédito; nunca rosto gerado por IA.</li>
<li>Trechos de TV (FIC, novelas, Rock in Rio): cortes curtos e com crédito, para evitar reivindicação de direitos.</li>
<li>Música: não usar a gravação original de BR-3 nem de Sossego por mais de alguns segundos; preferir trilha livre de direitos.</li>'''
SEC=lambda h,i,c: f'<h2>{h} <button data-t="{i}">Copiar</button></h2><pre id="{i}">{html.escape(c)}</pre>'
open('Tony_Pacote_Producao.html','w').write(f'''<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Pacote de Produção — Tony Tornado</title>
<style>body{{background:#fff;color:#111;font-family:system-ui,Segoe UI,Arial,sans-serif;max-width:860px;margin:0 auto;padding:24px 16px;line-height:1.55}}h1{{font-size:24px}}h2{{font-size:19px;margin-top:32px;border-bottom:2px solid #eee;padding-bottom:4px}}pre{{white-space:pre-wrap;background:#f6f6f6;padding:12px;border-radius:6px;font-family:inherit}}table{{width:100%;border-collapse:collapse}}td{{border-bottom:1px solid #eee;padding:8px;vertical-align:top}}td.t{{font-weight:700;white-space:nowrap;width:60px}}.note{{color:#555;font-size:14px}}li{{margin-bottom:6px}}button{{font-size:13px;margin-left:8px}}</style></head><body>
<h1>Pacote de Produção: Tony Tornado</h1>
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
