import re, html, json
TITLE="DERCY GONÇALVES: É REPUGNANTE O Que Fizeram Com o Caixão Dela DEPOIS da Morte"
files=['parte1.txt','parte2.txt','parte3.txt','parte4.txt','parte5.txt']
raw=[p.strip() for f in files for p in open(f).read().split('\n\n') if p.strip()]
paras=[re.sub(r'^[RA]: ','',p) for p in raw]
open('voz.txt','w').write('\n\n'.join(paras)+'\n')
open('roteiro_completo.txt','w').write('\n\n'.join(raw)+'\n')
W=sum(len(p.split()) for p in paras)
body=''.join(f'<p>{html.escape(p)}</p>\n' for p in paras)
open('Dercy_Roteiro_Voz.html','w').write(f'''<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(TITLE)}</title>
<style>body{{background:#fff;color:#000;font-family:Georgia,serif;font-size:20px;line-height:1.7;max-width:760px;margin:0 auto;padding:32px 16px}}h1{{font-size:24px;line-height:1.3;margin-bottom:32px}}p{{margin:0 0 18px}}</style>
</head><body>
<h1>{html.escape(TITLE)}</h1>
{body}</body></html>''')
CH=[('Dercy Gonçalves morreu em dois mil e oito','O túmulo','Pirâmide de vidro à noite (ilustrativo)'),
('A cidade se chama Santa Maria Madalena.','Santa Maria Madalena','Vista da cidade na serra (arquivo, com crédito)'),
('Começa no dia vinte e três de junho','Dolores','Casa simples antiga, tina de roupa (ilustrativo)'),
('Margarida foi embora.','A mãe que foi embora','Porta entreaberta, silhueta de mulher saindo (ilustrativo)'),
('Na rua, a vida também não era mais fácil.','Negrinha','Rua de cidade pequena antiga, silhueta de menina (ilustrativo)'),
('Dercy precisou trabalhar cedo.','O cinema da cidade','Bilheteria de cinema antigo · filmes mudos (arquivo)'),
('Por volta de mil novecentos e vinte e quatro','O vagão de trem','Rodas de trem a vapor em movimento (ilustrativo)'),
('A fuga deu certo.','Os Pascoalinos','Lona de circo antiga (arquivo/ilustrativo)'),
('O que aconteceu entre aqueles dois','O que ela contou décadas depois','Camisola de pano rústico sobre cama simples (ilustrativo, sem pessoas)'),
('No fim de mil novecentos e trinta e um','A tuberculose','Sanatório antigo (arquivo) · letreiro "Santos Dumont, MG"'),
('E é aqui que entra o homem','O homem casado','Silhueta masculina de chapéu, anos 30 (ilustrativo)'),
('Em mil novecentos e trinta e quatro, nasceu','Decimar','Mãos de mãe segurando bebê (ilustrativo)'),
('Nos anos seguintes, ela ainda tentou insistir','A estrela','Cartazes de teatro de revista (arquivo, com crédito)'),
('Em mil novecentos e sessenta e sete, Dercy estreou','Dercy de Verdade','Imagens de arquivo da TV anos 60 (com crédito)'),
('Guarde esta data. Mil novecentos e sessenta e nove.','A censura','Tesoura cortando fita de filme · carimbo "CENSURADO" (ilustrativo)'),
('Em mil novecentos e setenta, Boni chamou','A demissão','Escritório vazio de emissora anos 70 (ilustrativo)'),
('Mil novecentos e noventa e um.','1991','Carnaval do Rio (arquivo, com crédito; sem nudez)'),
('Naquele mesmo ano, Dercy voltou','A pirâmide','Pirâmide de vidro no cemitério (arquivo, com crédito)'),
('Em julho de dois mil e sete','Em cima do próprio túmulo','Trecho da entrevista de 2007 (com crédito)'),
('Ela tinha um último desejo.','O último desejo','Silhueta de mulher idosa de pé, de costas (ilustrativo)'),
('No dia doze de julho de dois mil e oito','A morte','Corredor de hospital à noite (ilustrativo)'),
('Na cidade, o corpo foi velado','O enterro','Igreja matriz da cidade (arquivo, com crédito)'),
('No dia seguinte ao enterro','O dia seguinte','Portão de cemitério ao amanhecer (ilustrativo)'),
('Fevereiro de dois mil e dezesseis.','Abriram o túmulo','Imagens da Record 2016 (trecho curto, com crédito)'),
('Diante das câmeras, Magdala contou','A amiga','Flor sobre pedra de túmulo (ilustrativo) · letreiro "segundo ela"'),
('Aquela noite na Record ainda guardava','O apagão','Estúdio de TV com luzes se apagando (ilustrativo)'),
('Numa entrevista ao jornal O Globo','A outra versão','Manchete de jornal borrada (ilustrativo) · letreiro "segundo a filha"'),
('Quando morreu, Dercy deixou uma fortuna','A herdeira','Apartamento vazio de frente para o mar (ilustrativo)'),
('Hoje, quem visita o cemitério','O que está lá dentro','Pirâmide de vidro de dia, turistas em silhueta'),
('Existe uma coisa que muita gente esquece','O último pedido','Cadeira vazia com luz de janela (ilustrativo)'),
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
DESC='''Dercy Gonçalves morreu em 2008, aos 101 anos, e foi enterrada dentro de uma pirâmide de vidro que ela mesma construiu em Santa Maria Madalena. Oito anos depois, quando o túmulo foi aberto diante das câmeras, o Brasil descobriu o que tinham feito com o caixão dela logo depois do enterro, contra a última vontade da atriz.

Neste vídeo: a mãe que abandonou sete filhos, a fuga embaixo de um vagão de trem, o primeiro namorado e o que ela só teve coragem de contar décadas depois, o homem casado que pagou o sanatório, a censura da ditadura e a demissão da Globo, a pirâmide de 1991, o último desejo, a abertura do túmulo em 2016 e as duas versões sobre quem decidiu mexer no caixão.

Importante: o relato sobre Eugênio Pascoal é da própria Dercy, em entrevista. As versões sobre a mudança do caixão são atribuídas a quem as contou: a amiga Magdala Feijó, no programa do Gugu (Record, 2016), e a filha Decimar, ao jornal O Globo. Valores do processo contra a Globo e da herança são os citados em reportagens.

{CHAPS}

#DercyGonçalves #Dercy #HistóriasReais'''.replace('{CHAPS}',CHAPS)
TAGS='dercy gonçalves, túmulo de dercy gonçalves, dercy gonçalves caixão, dercy gonçalves enterrada em pé, dercy gonçalves morte, dercy gonçalves história, pirâmide dercy gonçalves, santa maria madalena, gugu túmulo dercy, dercy de verdade, dercy gonçalves censura, filha de dercy gonçalves, assim foi a vida, dercy gonçalves documentário'
assert len(TAGS)<=500, len(TAGS)
open('desc.txt','w').write(DESC+'\n'); open('tags.txt','w').write(TAGS+'\n')
rows=''.join(f'<tr><td class="t">{t}</td><td><b>{html.escape(n)}</b><br>{html.escape(i)}</td></tr>\n' for t,n,i in out)
CAUT='''<li>Relato do estupro: sempre como relato da própria Dercy ("segundo ela"). Nada de reconstituição gráfica; usar só objetos (camisola, cama vazia).</li>
<li>Magdala Feijó e Decimar: as duas versões com letreiro de atribuição. Não chamar ninguém de "traidora" nos letreiros.</li>
<li>Imagens da Record (abertura do túmulo) e da Globo: trechos curtos, com crédito (risco de Content ID).</li>
<li>Carnaval de 1991: não mostrar nudez; usar imagens de arquivo cortadas ou ambientação.</li>
<li>Nada de imagens de restos mortais nem do interior do caixão.</li>
<li>O apagão no programa: tratar como coincidência, sem efeitos de "fantasma".</li>
<li>Thumbnail: sem rosto real ou gerado por IA de Dercy; preferir a pirâmide de vidro e a silhueta.</li>'''
SEC=lambda h,i,c: f'<h2>{h} <button data-t="{i}">Copiar</button></h2><pre id="{i}">{html.escape(c)}</pre>'
open('Dercy_Pacote_Producao.html','w').write(f'''<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Pacote de Produção — Dercy Gonçalves</title>
<style>body{{background:#fff;color:#111;font-family:system-ui,Segoe UI,Arial,sans-serif;max-width:860px;margin:0 auto;padding:24px 16px;line-height:1.55}}h1{{font-size:24px}}h2{{font-size:19px;margin-top:32px;border-bottom:2px solid #eee;padding-bottom:4px}}pre{{white-space:pre-wrap;background:#f6f6f6;padding:12px;border-radius:6px;font-family:inherit}}table{{width:100%;border-collapse:collapse}}td{{border-bottom:1px solid #eee;padding:8px;vertical-align:top}}td.t{{font-weight:700;white-space:nowrap;width:60px}}.note{{color:#555;font-size:14px}}li{{margin-bottom:6px}}button{{font-size:13px;margin-left:8px}}</style></head><body>
<h1>Pacote de Produção: Dercy Gonçalves</h1>
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
