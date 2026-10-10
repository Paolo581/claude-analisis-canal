import re, html
TITLE="EDUARDO COSTA: Por Que a Justiça Pediu a PRISÃO Dele"
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
open('EduardoCosta_Roteiro_Voz.html','w').write(f'''<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(TITLE)}</title>
<style>body{{background:#fff;color:#000;font-family:Georgia,serif;font-size:20px;line-height:1.7;max-width:760px;margin:0 auto;padding:32px 16px}}h1{{font-size:24px;line-height:1.3;margin-bottom:32px}}p{{margin:0 0 18px}}</style>
</head><body>
<h1>{html.escape(TITLE)}</h1>
{body}</body></html>''')
CH=[('Eduardo Costa saiu de casa ainda criança','Do palco à Justiça','Silhueta de cantor de chapéu sob holofote · Grades e martelo de juiz (ilustrativo)'),
('Para entender como um menino','O menino de Belo Horizonte','Bairro simples de BH (banco de imagens) · Folia de Reis (arquivo, com crédito)'),
('Rodou pelo interior','A rodoviária','Rodoviária vazia à noite (banco de imagens)'),
('Aos catorze anos, Eduardo','A estrada','Palco pequeno de bar no interior (ilustrativo)'),
('Até que, em dois mil e sete','Me Apaixonei','Capas de discos (com crédito) · Rádio antigo'),
('Em dois mil e catorze, veio','Cabaré','Trechos curtos do DVD Cabaré (com crédito)'),
('Em dois mil e quinze, ele fechou','A casa de 9 milhões','Fachada genérica de mansão (sem identificar o imóvel real) · Letreiro "R$ 9 milhões"'),
('Foi nesse ambiente que ele conheceu','Victória','Fotos públicas do casal (com crédito)'),
('Fevereiro de dois mil e dezoito.','O vídeo do Carnaval','Celular com perfil genérico (sem fotos reais) · Letreiro "segundo Victória"'),
('Eduardo negou tudo.','A defesa ao lado do padre','Trecho curto do vídeo de Eduardo (com crédito) · Letreiro "Eduardo nega"'),
('Maio de dois mil e dezoito.','O noivado','Alianças sobre mesa (ilustrativo)'),
('Outubro de dois mil e dezoito.','A lagosta e a eleição','Prato de lagosta (banco de imagens) · Urna eletrônica (arquivo)'),
('Havia mais uma coisa acontecendo em silêncio','A troca de imóveis','Lago de Furnas, Capitólio (banco de imagens) · Barco e jet ski'),
('Catorze de maio de dois mil e dezenove.','O fim do noivado','Fotos apagadas de rede social (ilustrativo)'),
('Depois do fim do noivado','Clayton e o irmão','Foto de imprensa da dupla Clayton e Romário (com crédito)'),
('Seis de janeiro de dois mil e vinte.','Os áudios','Ondas de áudio em tela de celular (ilustrativo) · Letreiro "segundo Victória"'),
('Para entender o pedido de prisão','Amor & Sexo','Trecho curto do encerramento do programa (com crédito)'),
('Eduardo foi para as redes sociais.','O post','Mão digitando num celular no escuro (ilustrativo) · Letreiros com trechos documentados'),
('Nos dias seguintes, Eduardo mudou o tom.','O pedido de desculpas','Trecho curto do Conversa com Bial (com crédito)'),
('Fernanda entrou na Justiça.','Dois processos','Fachada do TJ-RJ (arquivo)'),
('Primeiro de maio de dois mil e vinte.','A live com Leonardo','Trecho curto da live Cabaré em Casa (com crédito)'),
('Julho de dois mil e vinte e um.','A confissão','Microfone de podcast (ilustrativo)'),
('Dois mil e vinte e um.','A denúncia','Fachada do MPMG (arquivo) · Letreiro "acusação, sem sentença conhecida"'),
('Dos dois processos abertos por Fernanda','As condenações','Letreiros "8 meses" e "R$ 70 mil"'),
('No meio de tudo isso','A Lei Rouanet','Letreiro "quase R$ 1 milhão"'),
('Cinco de fevereiro de dois mil e vinte e cinco.','O pedido de prisão','Manchetes genéricas de portais · Letreiro "05/02/2025"'),
('A resposta dele veio pelas redes sociais.','Fake news?','Letreiro "Eduardo: fake news" · Fachada do TJ-RJ'),
('Janeiro de dois mil e vinte e seis.','165 mil pessoas','Imagens do show em Matinhos (com crédito)'),
('Existe uma coisa que a história de Eduardo Costa ensina','O peso das palavras','Celular com tela apagada sobre mesa'),
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
DESC='''Eduardo Costa saiu de casa ainda criança para virar cantor, chegou ao topo do sertanejo e, em fevereiro de 2025, viu o Ministério Público do Rio pedir a prisão dele. Da infância pobre em Belo Horizonte ao Cabaré com Leonardo, das acusações da ex-noiva Victória Villarim ao post de 2018 contra Fernanda Lima que virou condenação por difamação.

Aviso: as acusações de Victória Villarim (vazamento de fotos e áudios de ameaça atribuídos ao irmão do cantor) são a versão dela; Eduardo negou o vazamento e deu explicações sobre os áudios. A denúncia de estelionato do Ministério Público de Minas é uma acusação, sem sentença conhecida até a publicação. O pedido de prisão de 2025 foi feito pelo MP do Rio por suposto descumprimento da pena alternativa; Eduardo chamou as notícias de fake news, e não há notícia de que ele tenha sido preso. Os relatos sobre a live com Leonardo vêm de fontes ouvidas pela imprensa.

{CHAPS}

#EduardoCosta #Sertanejo #HistóriaReal'''.replace('{CHAPS}',CHAPS)
TAGS='eduardo costa, eduardo costa prisão, eduardo costa fernanda lima, eduardo costa condenado, eduardo costa victória villarim, eduardo costa leonardo, cabaré leonardo eduardo costa, eduardo costa polêmica, eduardo costa história, eduardo costa biografia, sertanejo, fernanda lima amor e sexo'
assert len(TAGS)<=500, len(TAGS)
open('desc.txt','w').write(DESC+'\n'); open('tags.txt','w').write(TAGS+'\n')
rows=''.join(f'<tr><td class="t">{t}</td><td><b>{html.escape(n)}</b><br>{html.escape(i)}</td></tr>\n' for t,n,i in out)
CAUT='''<li>Victória Villarim: sempre letreiro "segundo Victória" nas acusações e "Eduardo nega" logo em seguida. Nunca mostrar as fotos íntimas nem simular imagens.</li>
<li>Weliton Costa: os áudios são "atribuídos" a ele; não usar foto dele com letreiros acusatórios.</li>
<li>Estelionato: letreiro "acusação do MP, sem sentença conhecida". Não mostrar a casa real.</li>
<li>Pedido de prisão: nunca dizer ou sugerir em imagem que ele foi preso; mostrar a resposta dele ("fake news").</li>
<li>Fernanda Lima: mostrar os posts como fatos documentados no processo; nada de novos ataques nem montagens com o rosto dela.</li>
<li>Leonardo: a decisão de se afastar vem de "fontes ouvidas pela imprensa"; Leonardo não falou diretamente.</li>
<li>Rostos reais: só fotos de imprensa ou arquivo com crédito; nunca rosto gerado por IA.</li>
<li>Músicas: só trechos curtos, com crédito; preferir trilha livre de direitos.</li>'''
SEC=lambda h,i,c: f'<h2>{h} <button data-t="{i}">Copiar</button></h2><pre id="{i}">{html.escape(c)}</pre>'
open('EduardoCosta_Pacote_Producao.html','w').write(f'''<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Pacote de Produção — Eduardo Costa</title>
<style>body{{background:#fff;color:#111;font-family:system-ui,Segoe UI,Arial,sans-serif;max-width:860px;margin:0 auto;padding:24px 16px;line-height:1.55}}h1{{font-size:24px}}h2{{font-size:19px;margin-top:32px;border-bottom:2px solid #eee;padding-bottom:4px}}pre{{white-space:pre-wrap;background:#f6f6f6;padding:12px;border-radius:6px;font-family:inherit}}table{{width:100%;border-collapse:collapse}}td{{border-bottom:1px solid #eee;padding:8px;vertical-align:top}}td.t{{font-weight:700;white-space:nowrap;width:60px}}.note{{color:#555;font-size:14px}}li{{margin-bottom:6px}}button{{font-size:13px;margin-left:8px}}</style></head><body>
<h1>Pacote de Produção: Eduardo Costa</h1>
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
