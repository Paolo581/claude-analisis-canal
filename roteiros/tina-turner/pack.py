import re, html
TITLE="TINA TURNER: O REPUGNANTE Segredo Que Ela Escondeu Durante 16 Anos Atrás do Palco"
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
open('Tina_Roteiro_Voz.html','w').write(f'''<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(TITLE)}</title>
<style>body{{background:#fff;color:#000;font-family:Georgia,serif;font-size:20px;line-height:1.7;max-width:760px;margin:0 auto;padding:32px 16px}}h1{{font-size:24px;line-height:1.3;margin-bottom:32px}}p{{margin:0 0 18px}}</style>
</head><body>
<h1>{html.escape(TITLE)}</h1>
{body}</body></html>''')
CH=[('Tina Turner passou dezesseis anos','O segredo atrás do palco','Silhueta de cantora sob holofote, de costas · Letreiro "16 ANOS"'),
('Vinte e seis de novembro de mil novecentos e trinta e nove','Nutbush','Campo de algodão no sul dos EUA (arquivo/banco de imagens) · Placa de estrada rural'),
('Mil novecentos e cinquenta.','A mãe que foi embora','Estrada de terra vazia, mala velha (ilustrativo)'),
('St. Louis era uma cidade grande','Ike Turner','Clubes noturnos de St. Louis anos 50 (arquivo) · Foto de imprensa de Ike com a banda (com crédito)'),
('Em agosto de mil novecentos e cinquenta e oito','Craig','Berço antigo (ilustrativo) · Letreiro "agosto de 1958"'),
('Naquele mesmo ano, Ike escreveu','O nome que Ike inventou','Microfone de estúdio anos 60 · Letreiro "Anna Mae Bullock → Tina Turner"'),
('Segundo o relato que ela fez anos depois, Ike pegou','O primeiro golpe','Forma de sapato de madeira sobre mesa (ilustrativo, sem pessoa)'),
('No palco, os dois viraram','O casal mais quente da música','Fotos de imprensa da Revue e das Ikettes (com crédito) · Trecho curto de TV'),
('Mil novecentos e sessenta e oito.','Os cinquenta comprimidos','Frasco de remédio vazio (ilustrativo) · Corredor de hospital'),
('Em agosto de mil novecentos e sessenta e nove','Bolic Sound','Estúdio de gravação anos 70 (arquivo/banco de imagens)'),
('Naquele mesmo ano, Tina escreveu','Nutbush City Limits','Capa do single (com crédito) · Placa de Nutbush'),
('Foi em mil novecentos e oitenta e um','A entrevista de 1981','Gravador de fita antigo · Capa da People (com crédito, se licenciada)'),
('Tina contou que, durante quase todo o tempo','O segredo','Camarim vazio com espelho iluminado · Maquiagem sobre a bancada (sem pessoa)'),
('Ike Turner contou outra versão.','A versão de Ike e a carta','Papel de carta dobrado sobre mesa (ilustrativo)'),
('Lembra do nome que Ike deu a ela?','Dona nem do próprio nome','Letreiro "marca registrada: TINA TURNER" (sem simular documento real)'),
('Uma mulher presa a um homem violento','O contrato dos quatro dias','Contrato em papel, caneta (ilustrativo, sem logotipos) · Letreiro "4 dias"'),
('Primeiro de julho de mil novecentos e setenta e seis.','Dallas','Avião anos 70 · Fachada de hotel em Dallas (arquivo)'),
('Daquela vez, Tina revidou.','A fuga com 36 centavos','Moedas na palma da mão · Rodovia à noite com faróis'),
('Segundo os relatos sobre aquela noite, o gerente','O Ramada Inn','Recepção de hotel anos 70 à noite (ilustrativo)'),
('Lembra do nome que Ike tinha registrado como marca?','O que ela exigiu no divórcio','Fachada de tribunal (arquivo) · Letreiro "29/03/1978"'),
('Só que um nome não paga contas.','Sem Ike, ela não era nada','Palco pequeno de hotel em Las Vegas · Salão de convenções vazio'),
('Mil novecentos e setenta e nove.','Private Dancer','Capa de Private Dancer (com crédito) · Trecho curto do Grammy 1985 (com crédito)'),
('Dezesseis de janeiro de mil novecentos e oitenta e oito.','Maracanã: o recorde','Imagens do show no Maracanã 1988 (arquivo, com crédito) · Letreiro "180 mil pessoas"'),
('Antes disso, a vida deu a Tina','Erwin','Fotos públicas do casal (com crédito) · Lago de Zurique'),
('Só que o corpo dela cobrou','O rim','Corredor de hospital · Letreiro "07/04/2017"'),
('Julho de dois mil e dezoito.','Craig e Ronnie','Oceano Pacífico ao entardecer, costa da Califórnia (banco de imagens)'),
('Vinte e quatro de maio de dois mil e vinte e três.','Küsnacht','Casa à beira do lago em Küsnacht (vista pública) · Flores e homenagens'),
('No começo deste vídeo, você ouviu','Por que ela ficou com o nome','Letreiro "TINA TURNER" acendendo · Multidão do Maracanã'),
('Existe muita gente vivendo dentro de casa','Quem esconde dentro de casa','Mão segurando outra mão (banco de imagens)'),
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
DESC='''Tina Turner passou 16 anos sorrindo nos maiores palcos do mundo enquanto escondia um segredo repugnante dentro de casa. Quando finalmente fugiu, com 36 centavos no bolso, abriu mão de quase tudo. E exigiu ficar com uma única coisa que pertencia ao homem de quem estava fugindo. Da menina abandonada em Nutbush ao nome que Ike Turner inventou e registrou, da noite em Dallas em 1976 ao recorde de 180 mil pessoas no Maracanã, do rim doado por Erwin Bach à morte na Suíça em 2023.

Os relatos de violência são da própria Tina Turner, na entrevista à revista People (1981), nas autobiografias e no documentário Tina (2021). Ike Turner negou parte das acusações: admitiu tapas e socos, mas negou que a espancasse. A versão dele também está no vídeo.

Se você ou alguém próximo está passando por um momento difícil, procure ajuda. O CVV atende de graça, 24 horas, pelo telefone 188 ou pelo site cvv.org.br. Em caso de violência contra a mulher, ligue 180 (Central de Atendimento à Mulher, gratuita e sigilosa) ou 190 em emergência.

{CHAPS}

#TinaTurner #HistóriaReal #Documentário'''.replace('{CHAPS}',CHAPS)
TAGS='tina turner, tina turner segredo, tina turner ike turner, tina turner história, tina turner biografia, tina turner documentário, tina turner maracanã, tina turner 1988 rio, tina turner morte, tina turner erwin bach, tina turner filho craig, ike e tina turner, whats love got to do with it, private dancer, tina turner nome'
assert len(TAGS)<=500, len(TAGS)
open('desc.txt','w').write(DESC+'\n'); open('tags.txt','w').write(TAGS+'\n')
rows=''.join(f'<tr><td class="t">{t}</td><td><b>{html.escape(n)}</b><br>{html.escape(i)}</td></tr>\n' for t,n,i in out)
CAUT='''<li>Violência: nunca encenar agressão com atores nem gerar rosto de Tina ou Ike por IA. Usar objetos (forma de sapato, camarim vazio, maquiagem) e letreiros.</li>
<li>Ike Turner: sempre que aparecer acusação, manter na tela "segundo Tina" ou "segundo o relato dela", e mostrar a negação dele com o mesmo peso.</li>
<li>Suicídio (comprimidos em 1968, suicídio assistido, morte de Craig): não mostrar pílulas sendo tomadas nem método; manter CVV 188 na descrição e num letreiro final.</li>
<li>Violência doméstica: incluir o Ligue 180 no letreiro final junto do CVV.</li>
<li>Marca registrada: não simular documento oficial; usar só letreiro.</li>
<li>Fotos de Tina, Ike, Erwin e dos filhos: só imagens de imprensa ou arquivo licenciadas, com crédito.</li>
<li>Trechos de shows, Grammy, Maracanã e do documentário Tina (HBO): cortes curtos e com crédito.</li>
<li>Músicas dela: evitar usar as gravações originais por mais de alguns segundos; preferir trilha livre de direitos.</li>'''
SEC=lambda h,i,c: f'<h2>{h} <button data-t="{i}">Copiar</button></h2><pre id="{i}">{html.escape(c)}</pre>'
open('Tina_Pacote_Producao.html','w').write(f'''<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Pacote de Produção — Tina Turner</title>
<style>body{{background:#fff;color:#111;font-family:system-ui,Segoe UI,Arial,sans-serif;max-width:860px;margin:0 auto;padding:24px 16px;line-height:1.55}}h1{{font-size:24px}}h2{{font-size:19px;margin-top:32px;border-bottom:2px solid #eee;padding-bottom:4px}}pre{{white-space:pre-wrap;background:#f6f6f6;padding:12px;border-radius:6px;font-family:inherit}}table{{width:100%;border-collapse:collapse}}td{{border-bottom:1px solid #eee;padding:8px;vertical-align:top}}td.t{{font-weight:700;white-space:nowrap;width:60px}}.note{{color:#555;font-size:14px}}li{{margin-bottom:6px}}button{{font-size:13px;margin-left:8px}}</style></head><body>
<h1>Pacote de Produção: Tina Turner</h1>
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
