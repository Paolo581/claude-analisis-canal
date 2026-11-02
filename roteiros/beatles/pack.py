import re, html, json
TITLE="Assim FOI a VIDA dos BEATLES — O Segredo SOMBRIO Que Destruiu a Maior Banda da História"
WPM=135
raw=[]
for n in range(1,9):
    for p in open(f'bloco{n}.txt').read().split('\n\n'):
        if p.strip(): raw.append(p.strip())
paras=[re.sub(r'^[RA]: ','',p) for p in raw]
open('roteiro_completo.txt','w').write('\n\n'.join(raw)+'\n')
open('voz.txt','w').write('\n\n'.join(paras)+'\n')
W=sum(len(p.split()) for p in paras)
CH=[('Nove de fevereiro de mil novecentos e sessenta e quatro. Setenta','A beatlemania','Beatles no Ed Sullivan, 1964 (arquivo, com crédito)'),
('Liverpool, começo dos anos quarenta.','Liverpool na guerra','Liverpool bombardeada (arquivo)'),
('John foi morar com a tia Mimi','John e a tia Mimi','Casa Mendips, Woolton (foto pública)'),
('A poucos quilômetros dali','Paul e a mãe Mary','Liverpool anos 50 (arquivo)'),
('Seis de julho de mil novecentos e cinquenta e sete.','O encontro na igreja','Igreja de St. Peter, Woolton (foto pública)'),
('Quinze de julho de mil novecentos e cinquenta e oito.','A morte de Julia','Avenida arborizada à noite (ilustrativo)'),
('A banda foi trocando de nome','Stuart e Pete','Foto pública dos Beatles com Stuart, 1960 (com crédito)'),
('Hamburgo, agosto de mil novecentos e sessenta.','Hamburgo','Reeperbahn anos 60 (arquivo)'),
('O cinema se chamava Bambi Kino.','O quarto atrás da tela','Tela de cinema antigo (ilustrativo)'),
('O dono da boate queria barulho','Os comprimidos','Comprimidos (ilustrativo, sem uso)'),
('Uma noite, um jovem artista alemão','Astrid','Câmera fotográfica antiga (ilustrativo)'),
('A vingança veio rápido.','Deportados','Delegacia antiga (ilustrativo)'),
('Nove de fevereiro de mil novecentos e sessenta e um.','O Cavern Club','Escada do Cavern Club (foto pública)'),
('Na primavera de mil novecentos e sessenta e um','Stuart deixa a banda','Ateliê de pintura (ilustrativo)'),
('Dez de abril de mil novecentos e sessenta e dois.','A morte de Stuart','Ambulância antiga (ilustrativo)'),
('E aqui entra a parte desta história','A acusação','Jornal antigo (ilustrativo)'),
('O nome dele era Brian Epstein.','Brian Epstein','Foto pública de Brian Epstein (com crédito)'),
('No último dia de mil novecentos e sessenta e um','A recusa da Decca','Estrada com neve à noite (ilustrativo)'),
('Junho de mil novecentos e sessenta e dois.','Abbey Road','Fachada do estúdio Abbey Road (foto pública)'),
('Dezesseis de agosto de mil novecentos e sessenta e dois.','A demissão de Pete Best','Escritório anos 60 (ilustrativo)'),
('Richard Starkey nasceu','Ringo e os hospitais','Hospital infantil antigo (arquivo)'),
('Vinte e três de agosto de mil novecentos e sessenta e dois.','O casamento secreto','Cartório antigo (ilustrativo)'),
('Em abril, nasceu o filho de John e Cynthia','A viagem à Espanha','Praia espanhola anos 60 (arquivo)'),
('Na Inglaterra daquela época','A vida secreta de Epstein','Rua de Londres à noite (ilustrativo)'),
('O ano era mil novecentos e sessenta e três','O contrato dos 10%','Produtos antigos dos Beatles (foto pública)'),
('Sete de fevereiro de mil novecentos e sessenta e quatro.','A chegada aos EUA','Desembarque em Nova York, 1964 (arquivo)'),
('No fim de agosto, a turnê americana','Forest Hills e Bob Dylan','Foto pública de Bob Dylan (com crédito)'),
('Primavera de mil novecentos e sessenta e cinco.','O LSD no café','Xícaras de café (ilustrativo)'),
('Julho de mil novecentos e sessenta e seis. Manila','Manila','Aeroporto anos 60 (arquivo)'),
('Em março daquele ano','Mais populares que Jesus','Fogueira de discos (arquivo, com crédito)'),
('Vinte e nove de agosto de mil novecentos e sessenta e seis.','O último show','Candlestick Park (arquivo)'),
('E foi lá que começou a fase mais criativa','Sargento Pepper','Capa de Sgt. Pepper (com crédito)'),
('Epstein passou a depender de comprimidos.','A queda de Epstein','Janela com chuva (ilustrativo)'),
('Na estação de Londres','Cynthia na plataforma','Estação de trem antiga (arquivo)'),
('Vinte e sete de agosto de mil novecentos e sessenta e sete.','A morte de Epstein','Porta fechada (ilustrativo)'),
('Sem Epstein, os rapazes','O caos da Apple','Escritório da Apple, Londres (foto pública)'),
('O nome dela era Yoko Ono.','Yoko','Foto pública de John e Yoko (com crédito)'),
('Naquele mesmo ano, John e Yoko passaram','A heroína','Quarto escuro (ilustrativo)'),
('Em mil novecentos e oitenta, poucos meses','A confissão','Gravador de entrevista (ilustrativo)'),
('Agosto de mil novecentos e sessenta e oito.','Ringo sai da banda','Bateria com flores (ilustrativo)'),
('Dez de janeiro de mil novecentos e sessenta e nove.','George vai embora','Show no telhado, 1969 (arquivo)'),
('O nome dele era Allen Klein.','Allen Klein','Contratos e caneta (ilustrativo)'),
('No outono de mil novecentos e sessenta e nove','Paul está morto','Faixa de pedestres de Abbey Road (foto pública)'),
('Trinta e um de dezembro de mil novecentos e setenta.','O processo','Tribunal de Londres (foto pública)'),
('Começo de janeiro de mil novecentos e setenta e seis.','Mal Evans','Foto pública de Mal Evans (com crédito)'),
('Mil novecentos e oitenta. Paul desembarcou','Preso em Tóquio','Aeroporto de Tóquio anos 80 (arquivo)'),
('Oito de dezembro de mil novecentos e oitenta.','8 de dezembro','Edifício Dakota (foto pública)'),
('Trinta de dezembro de mil novecentos e noventa e nove.','O ataque a George','Mansão inglesa à noite (ilustrativo)'),
('Depois da demissão, a vida de Pete Best','O destino de Pete Best','Foto pública de Pete Best (com crédito)'),
('Hoje, dos quatro Beatles','Forest Hills, 2026','Forest Hills Stadium (foto pública)'),
('E a parte mais bonita desta história','As mães','Liverpool ao entardecer (ilustrativo)'),
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
DESC='''Eles mudaram o mundo. Mas, longe das câmeras, os Beatles viveram uma história de drogas, mortes, traições e segredos. Um quarto sem janelas atrás da tela de um cinema. Um Beatle morto antes da fama. Outro expulso na véspera do sucesso. Um empresário que escondia uma vida que na época era crime. E uma confissão de John Lennon sobre a forma como tratava as mulheres.

Neste documentário: a infância de John e Paul e a perda das mães; Hamburgo e os comprimidos; a morte de Stuart Sutcliffe; a demissão de Pete Best; o casamento escondido de John; a vida secreta e a morte de Brian Epstein; o contrato dos 10%; Ed Sullivan e a beatlemania; Bob Dylan e o LSD no café; Manila e "mais populares que Jesus"; Yoko, a heroína e a confissão à Playboy; o processo de 1970; Mal Evans; Tóquio; 8 de dezembro de 1980; o ataque a George; e Ringo de volta a Forest Hills, 62 anos depois.

Fontes: The Beatles Anthology, Beatles Bible, entrevista de John Lennon à Playboy (1980), memórias de Cynthia Lennon, biografias de Mark Lewisohn e Philip Norman, Ultimate Classic Rock, Rolling Stone, Pollstar e reportagens da época. Relatos são atribuídos a quem os fez. Informações disponíveis até 02/11/2026.

{CHAPS}

#Beatles #JohnLennon #PaulMcCartney'''.replace('{CHAPS}',CHAPS)
TAGS='beatles, beatles história, beatles documentário, john lennon, paul mccartney, george harrison, ringo starr, brian epstein, pete best, stuart sutcliffe, yoko ono, fim dos beatles, morte de john lennon, beatles segredos, assim foi a vida, rock anos 60'
assert len(TAGS)<=500
open('desc.txt','w').write(DESC+'\n'); open('tags.txt','w').write(TAGS+'\n')
rows=''.join(f'<tr><td class="t">{t}</td><td><b>{html.escape(n)}</b><br>{html.escape(i)}</td></tr>\n' for t,n,i in out)
CAUT='''<li>Stuart Sutcliffe: causa da hemorragia desconhecida. A acusação contra Lennon é só da irmã, sem confirmação. Nunca afirmar.</li>
<li>Brian Epstein: morte acidental segundo o inquérito. Suicídio ou crime: boatos nunca comprovados.</li>
<li>Viagem à Espanha: só falas públicas (Lennon à Playboy, memórias de Cynthia). Não sugerir romance.</li>
<li>Paul e Ringo estão vivos: atribuir cada fala. Pete Best também vivo: tentativa de suicídio só como "segundo relatos", sem detalhes.</li>
<li>"Paul está morto": sempre como boato.</li>
<li>George: não usar "40 facadas". Agressor com transtorno mental, inimputável. Sem imagens de faca.</li>
<li>Lennon: sem imagens do crime nem do corpo. Não mostrar o rosto do assassino em destaque.</li>
<li>Mal Evans: "começo de janeiro de 1976" (fontes divergem entre os dias 4 e 5).</li>
<li>Forest Hills 2026: "show marcado" (não confirmamos como foi).</li>
<li>Músicas dos Beatles: não usar trechos gravados (direitos autorais). Fotos reais com crédito. Nunca rosto gerado por IA.</li>'''
json.dump({'title':TITLE,'desc':DESC,'tags':TAGS,'chaps':CHAPS,'rows':rows,'caut':CAUT,'paras':paras,'words':W},open('pack.json','w'),ensure_ascii=False)
print(CHAPS); print(W, round(W/WPM,1), len(TAGS))
