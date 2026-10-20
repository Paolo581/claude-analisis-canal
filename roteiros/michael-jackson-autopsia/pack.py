import re, html, json
TITLE="MICHAEL JACKSON: O Corpo Que Contou Tudo — Os Segredos HORRÍVEIS da Autópsia do Rei do Pop"
WPM=135
raw=[]
for n in range(1,9):
    for p in open(f'bloco{n}.txt').read().split('\n\n'):
        if p.strip(): raw.append(p.strip())
paras=[re.sub(r'^[RA]: ','',p) for p in raw]
open('roteiro_completo.txt','w').write('\n\n'.join(raw)+'\n')
open('voz.txt','w').write('\n\n'.join(paras)+'\n')
W=sum(len(p.split()) for p in paras)
CH=[('Vinte e seis de junho','A sala do legista','Corredor de instituto médico legal genérico (ilustrativo) · sem imagens de corpo'),
('Mas, antes de chegar àquela sala','Gary, Indiana','Gary anos 1950/60 (arquivo) · siderúrgicas'),
('Joseph Jackson trabalhava','A guitarra proibida','Guitarra antiga com corda arrebentada (ilustrativo)'),
('Joseph montou um grupo','Os ensaios','Fotos de arquivo dos Jackson 5 crianças (com crédito)'),
('Um cinto.','O cinto','Cinto sobre cadeira (ilustrativo)'),
('Em mil novecentos e noventa e três, numa entrevista para Oprah','A confissão a Oprah','Trecho curto da entrevista de 1993 (licenciado)'),
('Os Jackson 5 começaram a vencer','Motown','Teatro Apollo · Logotipo Motown (arquivo)'),
('Trinta de novembro de mil novecentos e oitenta e dois.','Thriller','Capa de Thriller (com crédito)'),
('O moonwalk.','O moonwalk','Trecho curto Motown 25 (licenciado) · Luva branca'),
('Vinte e sete de janeiro de mil novecentos e oitenta e quatro.','O fogo da Pepsi','Notícias de 1984 (arquivo) · fogos de palco'),
('Anos depois, o próprio Michael contou','Os remédios','Frascos de remédio genéricos (ilustrativo)'),
('Ainda nos anos oitenta, os fãs','A pele','Fotos de arquivo de várias épocas (com crédito)'),
('As cirurgias.','As cirurgias','Livro Moonwalk (capa, com crédito)'),
('Michael Jackson quase não conseguia dormir.','O leite','Garrafa de leite e frasco branco lado a lado (ilustrativo)'),
('Em mil novecentos e noventa e três, ele foi acusado','As acusações','Letreiro "absolvido de todas as 14 acusações"'),
('Março de dois mil e nove.','This Is It','Anúncio na O2 Arena (arquivo licenciado)'),
('Quarta-feira, vinte e quatro de junho','A última noite','Mansão de Holmby Hills por fora (arquivo) · Relógio 10h40'),
('Quinta-feira, vinte e cinco de junho','25 de junho','Ambulância (arquivo) · Fãs na porta do hospital'),
('Duas semanas depois, o mundo parou de novo.','A despedida','Cerimônia no Staples Center (arquivo licenciado)'),
('Sexta-feira, vinte e seis de junho.','A autópsia','Relatório de 51 páginas (ilustrativo, sem fotos)'),
('No couro cabeludo de Michael Jackson','A tatuagem escondida','Chapéu de feltro sobre mesa (ilustrativo)'),
('Havia cicatrizes atrás das duas orelhas.','As cicatrizes','Letreiros com os achados do relatório'),
('Os médicos encontraram marcas de agulha.','As agulhas','Seringa genérica desfocada (ilustrativo)'),
('O coração de Michael Jackson estava forte.','O coração','Ilustração médica neutra de coração'),
('Homicídio.','Homicídio','Carimbo "homicídio" (ilustrativo)'),
('Setembro de dois mil e onze.','O julgamento','Tribunal de Los Angeles (arquivo licenciado)'),
('Quatro meses depois da morte','Os filmes','Cartazes de This Is It e Michael (com crédito)'),
('Pense em como a vida de Michael Jackson foi estranha.','A última palavra','Recapitulação das imagens-chave · Chapéu e luva sobre palco vazio'),
]
cum=[];w=0
for p in paras: cum.append(w); w+=len(p.split())
out=[];last=-1
for key,name,img in CH:
    i=next(k for k,p in enumerate(paras) if k>last and p.startswith(key)); last=i
    s=0 if not out else round(cum[i]/WPM*60)
    out.append((f'{s//60}:{s%60:02d}',name,img))
CHAPS='\n'.join(f'{t} {n}' for t,n,_ in out)
open('chapters.txt','w').write(CHAPS+'\n')
DESC='''Em 26 de junho de 2009, no Instituto Médico Legal de Los Angeles, a autópsia de Michael Jackson começou a responder as perguntas que perseguiram o Rei do Pop durante a vida inteira. O que encontraram no corpo dele confirmou o que ele dizia e revelou o que ele escondia.

Neste documentário: o pai e o cinto em Gary; a infância roubada; o fogo no comercial da Pepsi; a pele e o vitiligo; o "leite" para dormir; a última noite; e cada descoberta do relatório de 51 páginas, até a palavra "homicídio" e a condenação de Conrad Murray.

Informações do relatório do legista de Los Angeles (divulgado pela AP), do depoimento do patologista Christopher Rogers no julgamento de 2011 e de entrevistas do próprio Michael. Sobre as acusações: Michael Jackson foi absolvido de todas as 14 acusações em 2005 e sempre negou as acusações. O filme "Michael" chega ao Prime Video no Brasil em 23 de outubro de 2026.

{CHAPS}

#MichaelJackson #ReiDoPop #Autópsia'''.replace('{CHAPS}',CHAPS)
TAGS='michael jackson, michael jackson autópsia, morte de michael jackson, michael jackson propofol, conrad murray, michael jackson vitiligo, filme michael, michael jackson prime video, michael jackson história, rei do pop, michael jackson documentário, this is it, michael jackson pai'
assert len(TAGS)<=500
open('desc.txt','w').write(DESC+'\n'); open('tags.txt','w').write(TAGS+'\n')
rows=''.join(f'<tr><td class="t">{t}</td><td><b>{html.escape(n)}</b><br>{html.escape(i)}</td></tr>\n' for t,n,i in out)
CAUT='''<li>NUNCA usar fotos do corpo ou da autópsia; só ilustrações neutras e letreiros.</li>
<li>Acusações: sempre com "absolvido de todas as 14 acusações em 2005" e "sempre negou"; nada gráfico.</li>
<li>Paris Jackson: usar só imagem pública da cerimônia, com crédito.</li>
<li>Trechos de entrevistas, clipes e filmes: curtos, licenciados ou com crédito.</li>
<li>Conrad Murray: condenado por homicídio culposo em 2011; mostrar também que ele sempre negou culpa.</li>
<li>Rostos reais: só fotos de arquivo/imprensa com crédito; nunca rosto gerado por IA.</li>'''
json.dump({'title':TITLE,'desc':DESC,'tags':TAGS,'chaps':CHAPS,'rows':rows,'caut':CAUT,'paras':paras,'words':W},open('pack.json','w'),ensure_ascii=False)
print(CHAPS); print(W, round(W/WPM,1), len(TAGS))
