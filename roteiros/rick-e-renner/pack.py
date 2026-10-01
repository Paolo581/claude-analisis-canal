import re, html
TITLE="Assim FOI a VIDA de RICK E RENNER — 40 Anos, Duas Separações e Um Fim CRUEL"
files=['parte1.txt','parte2.txt','parte3.txt','parte4.txt','parte5.txt']
paras=[]
for f in files:
    for p in open(f).read().split('\n\n'):
        p=p.strip()
        if p: paras.append(re.sub(r'^[RA]: ','',p))
# voice html
body=''.join(f'<p>{html.escape(p)}</p>\n' for p in paras)
open('RickRenner_Roteiro_Voz.html','w').write(f'''<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(TITLE)}</title>
<style>body{{background:#fff;color:#000;font-family:Georgia,serif;font-size:20px;line-height:1.7;max-width:760px;margin:0 auto;padding:32px 16px}}h1{{font-size:24px;line-height:1.3;margin-bottom:32px}}p{{margin:0 0 18px}}</style>
</head><body>
<h1>{html.escape(TITLE)}</h1>
{body}</body></html>''')
# chapters
CH=[('R: Rick e Renner cantaram juntos','O helicóptero que levou um dos dois','Dupla no palco (foto real licenciada) × serra catarinense com neblina, sem destroços · Texto: "UM FIM CRUEL"'),
('Cinco de dezembro de mil novecentos e sessenta e seis.','Geraldo e Ivair','Porto Nacional (arquivo) · Brasília anos 80 (arquivo)'),
('O encontro dos dois aconteceu por acaso.','O telefonema','Telefone antigo de parede (ilustrativo) · Bar noturno de Brasília (ilustrativo)'),
('Em mil novecentos e oitenta e nove, gravaram','O disco independente','LP independente (1.º objeto, ilustrativo) · Foto de Zezé Di Camargo & Luciano anos 90 (com crédito)'),
('Abril de mil novecentos e noventa e oito.','Ela é Demais','Capa "Mil Vezes Cantarei" (com crédito) · Trecho curto de TV anos 90 (com crédito)'),
('Na noite da virada para o ano dois mil','300 mil na Esplanada','Esplanada dos Ministérios lotada (arquivo) · Letreiro "300 mil pessoas"'),
('Antes disso, Rick escreveu','Filha','CD caseiro com etiqueta "Filha" (2.º objeto, ilustrativo) · Festa de 15 anos (banco de imagens, sem rostos)'),
('Em agosto daquele ano, numa segunda-feira','20 de agosto de 2001','Rodovia de dia (banco de imagens) · Relógio 8h55'),
('Rodovia Luiz de Queiroz','A moto','Capacete caído na beira da estrada (3.º objeto, ilustrativo, sem sangue) · Recorte da manchete de 2001'),
('Em dois mil e cinco, quatro anos depois','A condenação','Martelo de juiz · Letreiros "3 anos e 6 meses · 2 mil salários mínimos"'),
('Em dois mil e dez, o cantor resolveu','O candidato','Urna eletrônica · Letreiro "76.410 votos"'),
('Primeiro de janeiro de dois mil e onze.','Happy End','Palco de Ano Novo em Gaspar (ilustrativo) · Capa "Happy End" (com crédito)'),
('Setembro de dois mil e doze.','A primeira volta','Capa "Inacreditável Poder do Amor" (com crédito)'),
('Sexta-feira, vinte e seis de dezembro','26 de dezembro de 2014','Avenida à noite com poste torto (ilustrativo) · Trecho curto do vídeo da época, borrado (4.º objeto)'),
('Três dias depois, Rick apareceu','Mil vezes perdão','Print do post de Rick (com crédito) · Clínica (ilustrativo) · Telefone (5.º objeto)'),
('A: Domingo, quatro de janeiro de dois mil e quinze.','Só vou até aqui','Texto do post de 2015 em letreiros · Nunca mostrar a frase "uma vida passando depressa" aqui (é o payoff)'),
('Fevereiro de dois mil e dezesseis.','O ponto de interrogação','Trechos curtos do Domingo Show (com crédito) · Letreiro "Eu coloco um ponto de interrogação aí"'),
('Doze de agosto de dois mil e dezoito.','Seguir em Frente','Trecho curto do Faustão (com crédito) · Fotos da turnê internacional'),
('Sexta-feira, dezoito de setembro de dois mil e vinte e seis.','O último palco','Festa de 15 anos genérica, sem rostos · Letreiro "Sorriso (MT) · 19/09"'),
('Segunda-feira, vinte e um de setembro','O voo','Mapa Porto Belo → São Joaquim · Serra com neblina (sem destroços)'),
('O helicóptero era um Bell 430','A investigação','Fachada do CENIPA (arquivo) · Letreiro "causa ainda não determinada"'),
('Quinta-feira, vinte e quatro de setembro.','Sorocaba','Flores e velas (ilustrativo) · Foto pública do cortejo, sem close de familiares chorando'),
('A: Volte ao texto de quatro de janeiro','Uma vida passando depressa','Letreiro com a frase completa de 2015 · Trecho do podcast "O Rick é minha vida" (com crédito)'),
('Enquanto isso, o meio sertanejo se despedia.','Ela é Demais, de novo','Posts de Zezé e Chitãozinho & Xororó (prints com crédito) · Arena Pantanal (trecho curto, com crédito)'),
('Agora junte todas as peças.','Quem segurou você','Montagem dos 5 objetos: LP, CD de "Filha", capacete, vídeo, telefone'),
]
pos=0; idx={}
for p in paras:
    pass
words=0; starts=[]
raw=[]
for f in files:
    for p in open(f).read().split('\n\n'):
        p=p.strip()
        if p: raw.append(p)
cum=[];w=0
for p in raw:
    cum.append(w); w+=len(re.sub(r'^[RA]: ','',p).split())
out=[]
for key,name,img in CH:
    i=next(k for k,p in enumerate(raw) if p.startswith(key) or re.sub(r'^[RA]: ','',p).startswith(key))
    s=round(cum[i]/195*60)
    out.append((f'{s//60}:{s%60:02d}',name,img))
open('chapters.txt','w').write('\n'.join(f'{t} {n}' for t,n,_ in out)+'\n')
print('\n'.join(f'{t} {n}' for t,n,_ in out)); print('total min',round(w/195,1))
DESC='''Rick e Renner cantaram juntos durante 40 anos. Do telefonema que uniu os dois em Brasília ao helicóptero que levou Rick na serra de Santa Catarina, esta é a história completa da dupla: o sucesso de "Ela é Demais", o acidente de 2001, as duas separações, a frase de Rick que ninguém notou e o último show cantando "Filha".

Nossa homenagem e respeito às famílias de Rick, Bruno Avelar, Paulo Soares, Antônio Roberto Nóbrega de Araújo e Leopoldo Barros Teixeira, e às de Eveline Soares Rossi e Luiz Antônio.

#RickERenner #Rick #Renner'''
TAGS='rick e renner, rick e renner história, morte do rick, rick sollo, renner, rick e renner helicóptero, rick e renner separação, ela é demais, filha rick e renner, renner acidente, assim foi a vida, sertanejo, rick e renner 40 anos'
rows=''.join(f'<tr><td class="t">{t}</td><td><b>{html.escape(n)}</b><br>{html.escape(i)}</td></tr>\n' for t,n,i in out)
chap=html.escape('\n'.join(f'{t} {n}' for t,n,_ in out))
open('RickRenner_Pacote_Producao.html','w').write(f'''<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Pacote de Produção — Rick e Renner</title>
<style>body{{background:#fff;color:#111;font-family:system-ui,Segoe UI,Arial,sans-serif;max-width:860px;margin:0 auto;padding:24px 16px;line-height:1.55}}h1{{font-size:24px}}h2{{font-size:19px;margin-top:32px;border-bottom:2px solid #eee;padding-bottom:4px}}pre{{white-space:pre-wrap;background:#f6f6f6;padding:12px;border-radius:6px;font-family:inherit}}table{{width:100%;border-collapse:collapse}}td{{border-bottom:1px solid #eee;padding:8px;vertical-align:top}}td.t{{font-weight:700;white-space:nowrap;width:60px}}.note{{color:#555;font-size:14px}}li{{margin-bottom:6px}}</style></head><body>
<h1>Pacote de Produção: Rick e Renner</h1>
<p><b>Título:</b> {html.escape(TITLE)}</p>
<h2>Descrição (SEO)</h2><pre>{html.escape(DESC)}</pre>
<h2>Tags</h2><pre>{html.escape(TAGS)}</pre><p class="note">{len(TAGS)} caracteres (limite do YouTube: 500).</p>
<h2>Capítulos (colar na descrição)</h2><pre>{chap}</pre>
<p class="note">Tempos calculados a 195 palavras por minuto (~{round(w/195)} min no total). Ajuste pelo áudio real depois de gravar.</p>
<h2>Lista de imagens para o editor</h2><table>{rows}</table>
<h2>Cuidados na edição</h2><ul>
<li>Respeito às sete vítimas citadas: nenhuma imagem de destroços, corpos, moto real do acidente ou rostos de familiares em sofrimento.</li>
<li>Acidente de 2001 e prisão de 2014: como fatos registrados (imprensa e Justiça). Sem adjetivos sobre a pessoa do Renner em letreiros.</li>
<li>Causa da queda: "ainda não determinada pelo CENIPA". Nada de especular sobre o piloto.</li>
<li>Músicas da dupla: trechos curtos (Content ID); não usar como trilha contínua.</li>
<li>Trechos de TV (Faustão, Domingo Show, Domingo Espetacular, Planeta Xuxa): curtos e com crédito.</li>
<li>Thumbnail: foto real licenciada da dupla; nunca rostos gerados por IA.</li>
</ul>
<h2>Thumbnails</h2><p><b>Thumb1_AGORA_ELE_CANTA_SOZINHO.jpg</b> (recomendada): dupla abraçada no palco lotado × um homem sozinho no palco escuro com um banquinho vazio. <b>Thumb2_UMA_VIDA_PASSANDO_DEPRESSA.jpg</b>: dupla cantando × serra com neblina e helicóptero distante, sem destroços. Ambas usam silhuetas geradas por IA; se quiser rostos reais, use apenas foto licenciada.</p>
</body></html>''')
