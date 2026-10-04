import re, html
TITLE="Assim FOI a VIDA de MARCIUS MELHEM — O Escândalo Que A Globo Não Conseguiu Abafar"
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
CH=[('Marcius Melhem passou anos','O escândalo','Silhueta de homem de terno num estúdio escuro · Letreiro "O ESCÂNDALO"'),
('Para entender como uma história','O rapaz de Nilópolis','Imagens de Nilópolis e da Beija-Flor (arquivo, com crédito)'),
('Em dois mil e cinco, Melhem','Do Zorra a Os Caras de Pau','Trechos curtos de Zorra Total e Os Caras de Pau (com crédito)'),
('Em dois mil e dezoito, Marcius Melhem se tornou','O chefe do humor da Globo','Cadeira de diretor vazia numa sala (ilustrativo)'),
('Um dos programas mais importantes','A festa do Zorra','Salão de festa vazio, luzes baixas (ilustrativo)'),
('Para entender o peso daquela noite','Dani Calabresa','Fotos de imprensa de Dani Calabresa (com crédito)'),
('Foi de lá que ela fez uma ligação.','A ligação de 22 de dezembro','Telefone/celular tocando à noite (ilustrativo)'),
('Enquanto essa conversa acontecia','As duas notas da Globo','Letreiros com as notas de 6 de março e 14 de agosto de 2020'),
('Até outubro.','A advogada e as 2.400 páginas','Pilha de papéis de inquérito (ilustrativo) · Letreiro "2.400 páginas"'),
('Sexta-feira, quatro de dezembro','A reportagem da piauí','Capa/página da piauí (com crédito)'),
('Antes de ouvir o que a reportagem contou','A versão de Melhem','Trecho curto da entrevista na Record (com crédito) · Celular com mensagens borradas'),
('A reportagem começava por aquela noite.','O que a piauí contou','Corredor escuro com porta de banheiro entreaberta (ilustrativo, sem pessoas)'),
('Mas a parte que mais revoltou','A resposta da Globo','Sala de reunião vazia · Letreiro "Terapia"'),
('Agosto de dois mil e vinte e um.','A censura de 172 dias','Revista com tarja "CENSURADO" (ilustrativo) · Letreiro "R$ 500 mil"'),
('Melhem levou a própria defesa','Os vídeos no YouTube','Tela de vídeo genérica (sem logotipo, sem imagem real do canal)'),
('Enquanto isso, o inquérito seguia.','Réu por assédio sexual','Fachada do Tribunal de Justiça do Rio (arquivo)'),
('Os casos de Dani e de outras','O relógio da prescrição','Relógio de areia esvaziando · Letreiro "4 anos"'),
('Maio de dois mil e vinte e cinco.','O promotor e a suspensão','Martelo de juiz parado · Letreiro "processo suspenso"'),
('Abril de dois mil e vinte e seis.','O tempo acabou','Calendário com folhas caindo (ilustrativo)'),
('Quinta-feira, vinte e quatro de setembro','O acordo de R$ 8.105','Letreiro "5 salários mínimos = R$ 8.105" · Fachada do Retiro dos Artistas (com crédito)'),
('Agora volte a cada objeto','Três reais por página','Letreiro "R$ 8.105 ÷ 2.400 páginas = R$ 3,38"'),
('Enquanto o caso de assédio chegava','O processo que continua','Letreiro "4 atrizes · violência psicológica"'),
('A gente costuma imaginar o poder','O poder silencioso','Cadeira de diretor vazia em contraluz'),
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
DESC='''Marcius Melhem passou anos fazendo o Brasil rir e comandando o humor da Globo. Em agosto de 2020, a emissora anunciou o fim de uma parceria de 17 anos "em comum acordo", sem citar nenhuma acusação. Meses depois, uma reportagem da revista piauí, que ouviu 43 pessoas, revelou as denúncias de assédio que tinham chegado à Globo, entre elas a de Dani Calabresa sobre uma festa do Zorra em 2017.

Neste vídeo: a resposta da Globo à denúncia, a defesa de Melhem, a censura de 172 dias à piauí derrubada no STF, a prescrição de seis das sete denúncias e o acordo de R$ 8.105 ao Retiro dos Artistas, em setembro de 2026.

Importante: Marcius Melhem nega todas as acusações e nunca foi condenado. As acusações citadas são atribuídas às reportagens e aos processos públicos. A transação penal não representa admissão de culpa, e a prescrição não é absolvição nem condenação.

{CHAPS}

#MarciusMelhem #DaniCalabresa #Globo'''.replace('{CHAPS}',CHAPS)
TAGS='marcius melhem, marcius melhem dani calabresa, marcius melhem acordo, marcius melhem assédio, caso marcius melhem, marcius melhem globo, dani calabresa, revista piauí melhem, zorra globo, marcius melhem processo, marcius melhem 2026, assim foi a vida, escândalo globo'
assert len(TAGS)<=500, len(TAGS)
open('desc.txt','w').write(DESC+'\n'); open('tags.txt','w').write(TAGS+'\n')
rows=''.join(f'<tr><td class="t">{t}</td><td><b>{html.escape(n)}</b><br>{html.escape(i)}</td></tr>\n' for t,n,i in out)
CAUT='''<li>Melhem não foi condenado: nunca usar letreiros como "assediador", "abusador", "culpado" ou "criminoso". Usar "acusado", "segundo a piauí", "segundo a denúncia".</li>
<li>Toda acusação na tela deve vir com a fonte (piauí, Folha, MP-RJ) e, quando possível, com a frase "Melhem nega".</li>
<li>Cena da festa: só ambientação neutra (corredor, porta); nada de reconstituição com atores ou silhuetas em contato físico.</li>
<li>Vítimas: não mostrar nome nem rosto das mulheres do processo, exceto Dani Calabresa, que é pública; usar fotos de imprensa com crédito.</li>
<li>Mensagens: não recriar prints; usar celular com tela borrada.</li>
<li>Entrevista da Record e trechos da Globo: cortes curtos e com crédito.</li>
<li>Thumbnail: nada de rosto de Melhem ou Dani gerado por IA; preferir silhuetas e números.</li>
<li>Recomendado: revisão jurídica antes de publicar (ele já processou a Dani e obteve censura judicial contra a piauí).</li>'''
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
