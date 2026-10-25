import re, html, json
TITLE="Assim FOI a MORTE de JOHN LENNON — A Verdade SOMBRIA Que Ficou Escondida Por 45 Anos"
WPM=135
raw=[]
for n in range(1,10):
    for p in open(f'bloco{n}.txt').read().split('\n\n'):
        if p.strip(): raw.append(p.strip())
paras=[re.sub(r'^[RA]: ','',p) for p in raw]
open('roteiro_completo.txt','w').write('\n\n'.join(raw)+'\n')
open('voz.txt','w').write('\n\n'.join(paras)+'\n')
W=sum(len(p.split()) for p in paras)
CH=[('Oito de dezembro de mil novecentos e oitenta. Às cinco','O fã na calçada','Foto real de Paul Goresh: Lennon autografando o disco (com crédito)'),
('Um revólver de cinco balas.','As peças do mistério','Fachada do Dakota à noite (foto pública)'),
('Nove de outubro de mil novecentos e quarenta.','Liverpool, 1940','Liverpool na Segunda Guerra (arquivo)'),
('Existe uma versão famosa sobre esse momento','A escolha aos 5 anos','Casa de Mimi em Woolton (foto pública)'),
('Até que, em mil novecentos e cinquenta e cinco, a casa perdeu','O tio George','Rua de subúrbio inglês anos 50 (ilustrativo)'),
('Seis de julho de mil novecentos e cinquenta e sete.','John conhece Paul','Foto dos Quarrymen (com crédito)'),
('Quinze de julho de mil novecentos e cinquenta e oito.','A morte de Julia','Avenida à noite (ilustrativo)'),
('Stuart mal sabia tocar contrabaixo.','Stuart Sutcliffe e Hamburgo','Fotos de Hamburgo 1960 (com crédito)'),
('Enquanto isso, do outro lado do oceano, o menino nascido no Texas','O menino da Geórgia','Subúrbio americano anos 60 (ilustrativo)'),
('Um terno bem cortado.','Brian Epstein','Foto pública de Epstein com os Beatles (com crédito)'),
('Cynthia estava grávida.','O casamento escondido','Igreja / cartório (ilustrativo)'),
('Mas, em mil novecentos e sessenta e três, o mundo não queria saber de Julian.','A beatlemania','Fãs gritando (arquivo, com crédito)'),
('Março de mil novecentos e sessenta e seis.','Mais populares que Jesus','Discos queimados (arquivo, com crédito)'),
('Na Geórgia, Mark Chapman tinha onze anos','O garoto convertido','Igreja do interior americano (ilustrativo)'),
('Mil novecentos e oitenta. Poucos meses antes de morrer','A confissão de John','Capa da revista (com crédito)'),
('Agosto de mil novecentos e sessenta e sete.','A morte de Epstein','Retiro de meditação (arquivo, com crédito)'),
('O nome dela era Yoko Ono.','Yoko Ono','Fotos públicas de John e Yoko (com crédito)'),
('Era Paul McCartney.','Hey Jude','Estrada inglesa (ilustrativo)'),
('Em março de mil novecentos e sessenta e nove, John e Yoko se casaram.','O fim dos Beatles','Bed-in em Amsterdã (arquivo, com crédito)'),
('Nova York, mil novecentos e setenta e um.','O FBI e Nixon','Documentos do FBI (ilustrativo)'),
('O nome dela era May Pang.','O Fim de Semana Perdido','Los Angeles anos 70 (ilustrativo)'),
('Mark Chapman trabalhava como monitor de acampamento','O monitor Nemo','Acampamento de verão (ilustrativo)'),
('Mark se mudou para o Havaí.','O Havaí','Praia de Honolulu (ilustrativo)'),
('E, nessa época, um livro tomou conta da vida dele.','O Apanhador no Campo de Centeio','Capa do livro (com crédito)'),
('Começo de mil novecentos e setenta e cinco.','Sean','Fotos públicas de John com Sean (com crédito)'),
('Enquanto John vivia a fase mais feliz da vida','O livro da biblioteca','Biblioteca (ilustrativo)'),
('Vinte e sete de outubro de mil novecentos e oitenta.','A arma','Revólver em vitrine (ilustrativo, sem violência)'),
('Mark Chapman desistiu.','A primeira viagem','Aeroporto anos 80 (ilustrativo)'),
('Seis de dezembro de mil novecentos e oitenta.','Faltavam dois dias','Calendário (ilustrativo)'),
('Sete de dezembro de mil novecentos e oitenta.','James Taylor no metrô','Estação da Rua 72 (foto pública)'),
('Oito de dezembro de mil novecentos e oitenta. Segunda-feira.','A manhã do dia 8','Quarto de hotel (ilustrativo)'),
('A fotógrafa Annie Leibovitz','A última foto','Capa da Rolling Stone de 1981 (com crédito)'),
('Por volta das cinco da tarde, a porta do Dakota','O autógrafo','Foto real de Paul Goresh (com crédito)'),
('A noite caiu sobre Nova York.','As seis horas','Calçada do Dakota à noite (foto pública)'),
('Yoko passou primeiro pela entrada do prédio.','22h50','Arcada do Dakota (foto pública, sem violência)'),
('O porteiro se chamava José Perdomo.','O livro na calçada','Livro sobre calçada (ilustrativo)'),
('Os policiais Jim Moran e Bill Gamble','A viatura','Viatura antiga do NYPD (arquivo)'),
('No pronto-socorro, uma equipe de médicos','A verdade do hospital','Fachada do Roosevelt Hospital (foto pública)'),
('Mas o mundo descobriu de outro jeito.','O anúncio na TV','Velas na calçada do Dakota (arquivo, com crédito)'),
('Junho de mil novecentos e oitenta e um.','O julgamento que não houve','Tribunal (ilustrativo)'),
('No começo deste vídeo, ficou uma pergunta no ar.','A lista','Lista de papel (ilustrativo)'),
('Até hoje, Chapman já teve o pedido de liberdade negado','Yoko e as cartas','Strawberry Fields, Central Park (foto pública)'),
('Mas a imagem mais forte dessa história','Julian e Sean','Fotos públicas de Julian e Sean (com crédito)'),
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
DESC='''Às cinco da tarde de 8 de dezembro de 1980, John Lennon autografou o disco de um fã na porta do edifício Dakota, em Nova York. Seis horas depois, aquele mesmo fã ainda estava na calçada.

Neste documentário: a infância de John entre a guerra e o abandono; a mãe atropelada por um policial de folga; Stuart Sutcliffe e Brian Epstein; a confissão que o próprio John fez sobre violência contra mulheres; Yoko, Julian e Hey Jude; o FBI e Nixon; o Fim de Semana Perdido; e, em paralelo, a vida do homem que o matou: o monitor de acampamento, a tentativa de suicídio no Havaí, a obsessão por O Apanhador no Campo de Centeio, a primeira viagem a Nova York em que ele desistiu, a esposa que segurou a arma, o encontro com Sean e com James Taylor, o autógrafo, os tiros, o cirurgião que contestou a versão oficial e as confissões nas audiências de liberdade condicional.

Informações de NBC News, CBS News, Fox News, AP, The Guardian, Washington Post, Daily News (Jimmy Breslin), Hawaii News Now, Biography.com, SUNY Upstate, Apple TV+ (John Lennon: Murder Without a Trial) e das biografias de Mark Lewisohn. As teorias de conspiração são apresentadas apenas como teorias. Informações disponíveis até 25/10/2026.

{CHAPS}

#JohnLennon #Beatles #TrueCrime'''.replace('{CHAPS}',CHAPS)
TAGS='john lennon, morte de john lennon, assassinato de john lennon, mark david chapman, john lennon dakota, beatles, john lennon verdade, john lennon história, yoko ono, sean lennon, julian lennon, 8 de dezembro de 1980, o apanhador no campo de centeio, assim foi a morte'
assert len(TAGS)<=500
open('desc.txt','w').write(DESC+'\n'); open('tags.txt','w').write(TAGS+'\n')
rows=''.join(f'<tr><td class="t">{t}</td><td><b>{html.escape(n)}</b><br>{html.escape(i)}</td></tr>\n' for t,n,i in out)
CAUT='''<li>Nenhuma imagem de sangue, do corpo ou da cena do crime com violência. A foto do autógrafo (Paul Goresh) pode ser usada com crédito.</li>
<li>Chapman: usar o mínimo de imagens dele; nada que glorifique. Todas as falas dele são de audiências, com o ano.</li>
<li>Violência de John contra mulheres: só o que ele mesmo admitiu na Playboy (1980).</li>
<li>Yoko, May Pang, Gloria, Sean e Julian estão vivos: só fatos, sem julgamento. A versão de May Pang aparece atribuída a ela.</li>
<li>"Escolha aos 5 anos": dizer que é versão popular contestada por Mark Lewisohn.</li>
<li>Médicos: mostrar as duas versões (Lynn x Halleran); não afirmar quem está certo.</li>
<li>Conspirações: apenas como teorias, sem prova.</li>
<li>Nunca rosto gerado por IA.</li>'''
json.dump({'title':TITLE,'desc':DESC,'tags':TAGS,'chaps':CHAPS,'rows':rows,'caut':CAUT,'paras':paras,'words':W},open('pack.json','w'),ensure_ascii=False)
print(CHAPS); print(W, round(W/WPM,1), len(TAGS))
