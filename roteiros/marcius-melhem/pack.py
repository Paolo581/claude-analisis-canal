import re, html
TITLE="MARCIUS MELHEM: O Escândalo Que a Globo Nunca Explicou"
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
open('Melhem_Roteiro_Voz.html','w').write(f'''<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(TITLE)}</title>
<style>body{{background:#fff;color:#000;font-family:Georgia,serif;font-size:20px;line-height:1.7;max-width:760px;margin:0 auto;padding:32px 16px}}h1{{font-size:24px;line-height:1.3;margin-bottom:32px}}p{{margin:0 0 18px}}</style>
</head><body>
<h1>{html.escape(TITLE)}</h1>
{body}</body></html>''')
CH=[('Marcius Melhem comandava todo o humor','O escândalo','Silhueta de homem num estúdio de TV escuro · Letreiro "17 ANOS"'),
('Para entender esse silêncio','O jornalista que virou humorista','Redação antiga de jornal (banco de imagens) · Palco de teatro vazio'),
('No começo dos anos dois mil, chegou','Zorra Total e Os Caras de Pau','Trechos curtos de Os Caras de Pau (com crédito)'),
('Dois mil e catorze.','Tá no Ar e o Emmy','Trecho curto do Tá no Ar (com crédito) · Estatueta genérica de prêmio'),
('Ao mesmo tempo, a Globo decidiu reformular','O novo Zorra e Dani Calabresa','Fotos de imprensa do elenco do Zorra (com crédito)'),
('Até que, em dois mil e dezoito','O chefe de todo o humor','Corredor de emissora (ilustrativo) · Cadeira de diretor vazia'),
('Catorze de agosto de dois mil e vinte.','O comunicado de agosto','Letreiro "em comum acordo" · Fachada da emissora (arquivo)'),
('Para entender o que estava escondido','A primeira queixa','Mesa de reunião vazia (ilustrativo) · Letreiro "segundo a reportagem"'),
('Dani não desistiu.','O compliance','Pastas e documentos sigilosos (ilustrativo)'),
('Foi nesse período que um grupo de artistas','A carta e Marcelo Adnet','Fotos de imprensa de Adnet (com crédito)'),
('Então veio agosto de dois mil e vinte.','O e-mail e a advogada','Tela de e-mail genérica · Letreiro "cerca de 30 profissionais"'),
('Existe uma pergunta que atravessa','Poder e silêncio','Corredor escuro de estúdio · Letreiros com a diferença entre assédio sexual e moral'),
('Quatro de dezembro de dois mil e vinte.','A reportagem da piauí','Revista sobre mesa (sem reproduzir páginas) · Letreiros "43 entrevistas" e "12 casos"'),
('Melhem tinha recusado dar entrevista','A versão de Melhem','Letreiro "Melhem nega" · Trecho de entrevista (com crédito)'),
('Oito de dezembro de dois mil e vinte.','A nota no Jornal Nacional','Trecho curto do JN (com crédito) · Letreiro "razões não serão tornadas públicas"'),
('A reportagem tinha saído numa sexta-feira.','O país dividido','Montagem de telas de redes sociais genéricas (sem perfis reais)'),
('Dezembro de dois mil e vinte. Menos de duas semanas','As mensagens','Celular com balões de conversa desfocados · Ondas de áudio (ilustrativo)'),
('Janeiro de dois mil e vinte e um.','Os processos','Fachada do TJ-SP (arquivo) · Letreiro "R$ 246 mil"'),
('Durante quase três anos, promotores','Réu por assédio sexual','Fachada do TJ-RJ (arquivo) · Letreiro "réu não é culpado"'),
('O motivo era o tempo.','A prescrição','Ampulheta (ilustrativo) · Letreiro "prescrito"'),
('Outubro de dois mil e vinte e três.','Leandro Hassum','Foto de imprensa de Hassum (com crédito)'),
('Depois que Marcius Melhem virou réu','A fase lenta','Pilhas de processos (ilustrativo)'),
('Maio de dois mil e vinte e cinco.','O pedido de arquivamento','Letreiro "falta de justa causa" · Martelo de juiz'),
('Julho de dois mil e vinte e cinco.','O segundo processo','Letreiro "violência psicológica e perseguição" · "segredo de Justiça"'),
('Vinte e quatro de setembro de dois mil e vinte e seis.','O acordo de R$ 8 mil','Letreiros "transação penal" e "não é confissão" · Fachada genérica de instituição'),
('Até onde se sabe, a Globo nunca','O que a Globo nunca explicou','Fachada da emissora à noite (arquivo)'),
('Agora volte ao começo.','Quem estava falando a verdade','Retrospectiva rápida das imagens do vídeo · Ligue 180 na tela'),
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
DESC='''Marcius Melhem comandava todo o humor da Globo quando, em agosto de 2020, deixou a emissora depois de 17 anos, num anúncio de "comum acordo" sem nenhum motivo. Quatro meses depois, uma reportagem da revista piauí, com 43 entrevistas, trouxe relatos de assédio nos bastidores do departamento de humor, entre eles o de Dani Calabresa. Do Tá no Ar ao banco dos réus, das mensagens de WhatsApp à prescrição, até o acordo de setembro de 2026 que encerrou o processo sem julgamento.

Aviso importante: Marcius Melhem nega todas as acusações e nunca foi condenado. As acusações citadas são atribuídas à reportagem da piauí, às denunciantes e aos processos públicos. A prescrição não é condenação nem absolvição. A transação penal aceita em setembro de 2026 encerra o processo sem julgamento do mérito e, pela lei, não representa admissão de culpa. O processo por violência psicológica e perseguição citado no vídeo seguia em andamento até a produção deste conteúdo, e os réus negam as acusações.

Se você está passando por assédio no trabalho, ligue 180 (Central de Atendimento à Mulher, gratuito, 24 horas).

{CHAPS}

#MarciusMelhem #DaniCalabresa #Globo'''.replace('{CHAPS}',CHAPS)
TAGS='marcius melhem, marcius melhem dani calabresa, marcius melhem globo, caso marcius melhem, marcius melhem acordo, marcius melhem réu, dani calabresa, marcelo adnet, leandro hassum, zorra, tá no ar, os caras de pau, escândalo globo, revista piauí'
assert len(TAGS)<=500, len(TAGS)
open('desc.txt','w').write(DESC+'\n'); open('tags.txt','w').write(TAGS+'\n')
rows=''.join(f'<tr><td class="t">{t}</td><td><b>{html.escape(n)}</b><br>{html.escape(i)}</td></tr>\n' for t,n,i in out)
CAUT='''<li>Toda acusação com letreiro "segundo a reportagem" ou "segundo a denunciante", e "Melhem nega" logo em seguida.</li>
<li>Nunca dramatizar nem encenar os episódios relatados (festa, gravações). Usar imagens neutras e desfocadas.</li>
<li>Mensagens de WhatsApp: nunca reproduzir prints reais; usar balões desfocados genéricos.</li>
<li>Denunciantes anônimas: não sugerir identidade com fotos de atrizes do elenco.</li>
<li>Prescrição e transação penal: letreiros "não é condenação" e "não é confissão". Nunca usar a palavra "culpado" em tela.</li>
<li>Processo de 2025 (com Ricardo Feltrin): está em segredo de Justiça e em andamento. Só o que foi publicado na imprensa.</li>
<li>Rostos reais: só fotos de imprensa ou arquivo com crédito; nunca rosto gerado por IA. Trechos de TV curtos e com crédito.</li>
<li>Ligue 180 na tela durante o fechamento.</li>'''
SEC=lambda h,i,c: f'<h2>{h} <button data-t="{i}">Copiar</button></h2><pre id="{i}">{html.escape(c)}</pre>'
open('Melhem_Pacote_Producao.html','w').write(f'''<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Pacote de Produção — Marcius Melhem</title>
<style>body{{background:#fff;color:#111;font-family:system-ui,Segoe UI,Arial,sans-serif;max-width:860px;margin:0 auto;padding:24px 16px;line-height:1.55}}h1{{font-size:24px}}h2{{font-size:19px;margin-top:32px;border-bottom:2px solid #eee;padding-bottom:4px}}pre{{white-space:pre-wrap;background:#f6f6f6;padding:12px;border-radius:6px;font-family:inherit}}table{{width:100%;border-collapse:collapse}}td{{border-bottom:1px solid #eee;padding:8px;vertical-align:top}}td.t{{font-weight:700;white-space:nowrap;width:60px}}.note{{color:#555;font-size:14px}}li{{margin-bottom:6px}}button{{font-size:13px;margin-left:8px}}</style></head><body>
<h1>Pacote de Produção: Marcius Melhem</h1>
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
