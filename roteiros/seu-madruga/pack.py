import re, html, json
TITLE="Assim FOI a VIDA de RAMÓN VALDÉS, O SEU MADRUGA — O Fim CRUEL Que Ninguém Mostrou"
WPM=135
raw=[]
for n in range(1,9):
    for p in open(f'bloco{n}.txt').read().split('\n\n'):
        if p.strip(): raw.append(p.strip())
paras=[re.sub(r'^[RA]: ','',p) for p in raw]
open('roteiro_completo.txt','w').write('\n\n'.join(raw)+'\n')
open('voz.txt','w').write('\n\n'.join(paras)+'\n')
W=sum(len(p.split()) for p in paras)
CH=[('Num quarto de hospital na Cidade do México','O quarto de hospital','Corredor de hospital antigo (ilustrativo) · Chapéu do Seu Madruga sobre cadeira'),
('Mas, para entender essa dor','Moncho','Ciudad Juárez anos 1930 (arquivo)'),
('Entre os irmãos de Ramón estavam nomes','Tin Tan e os irmãos Valdés','Fotos de arquivo de Tin Tan e Loco Valdés (com crédito)'),
('Foi Tin Tan quem abriu a primeira porta','À sombra de Tin Tan','Cartaz de Calabacitas Tiernas (com crédito)'),
('Ramón se casou mais de uma vez.','Dois irmãos, duas irmãs','Foto das Hermanas Julián (com crédito)'),
('Quem contou foi o filho, Esteban Valdés.','O aluguel de verdade','Porta de casa simples · Recibo de aluguel (ilustrativo)'),
('O nome dele era Roberto Gómez Bolaños.','Chespirito e "seja você mesmo"','Foto de arquivo de Chespirito e Ramón (com crédito)'),
('Poucos anos depois, Chespirito criou uma vila.','Nasce o Seu Madruga','Cenas curtas de Chaves (licenciadas/crédito) · Barril'),
('Lembra do que o filho de Ramón contou?','O caloteiro da vila','Seu Madruga fugindo do Seu Barriga (trecho curto)'),
('Ramón fumava.','O cigarro','Cinzeiro com cigarro (ilustrativo)'),
('Mil novecentos e setenta e nove.','A saída no auge','Porta da vila fechando (ilustrativo)'),
('O nome dela era Florinda Meza.','A versão da família','Fotos públicas de Florinda e Ramón (com crédito)'),
('Mas essa não é a única versão.','As outras versões','Foto de Kiko (com crédito)'),
('Florinda nunca deu uma explicação direta','O que Florinda disse','Letreiro com a fala narrada'),
('Depois de sair da vila, Ramón pegou a estrada.','O circo','Lona de circo (ilustrativo)'),
('Em mil novecentos e oitenta e um, veio o convite','A volta e Federrico','Fotos de arquivo (com crédito)'),
('E, em mil novecentos e oitenta e cinco, chegou a notícia','O câncer','Letreiro "1985" · Exame genérico (ilustrativo)'),
('Em mil novecentos e oitenta e sete, Ramón aceitou','Ah, Que Kiko!','Foto de Ramón com Villagrán (com crédito)'),
('O país era o Peru.','A última viagem','Lima anos 80 (arquivo)'),
('O câncer tinha avançado.','O hospital','Janela de hospital (ilustrativo)'),
('Ramón olhou para ele e pediu que parasse de chorar.','"Lá te espero"','Letreiro com a frase · Mãos (ilustrativo)'),
('E houve outra visita, segundo o neto de Ramón, Miguel.','A última piada','Foto de Édgar Vivar (com crédito)'),
('Nove de agosto de mil novecentos e oitenta e oito.','9 de agosto de 1988','Letreiro com a data · Vela'),
('Segundo o neto Miguel, apenas uma integrante','Só ela foi ao velório','Foto de Angelines Fernández (com crédito)'),
('Chespirito não foi ao velório de Ramón.','A ausência de Chespirito','Cadeira vazia (ilustrativo)'),
('Um ano antes, em mil novecentos e noventa e três','A cinco metros dele','Mausoleos del Ángel (foto pública, com crédito)'),
('Março de dois mil e dezesseis.','A acusação de 2016','Letreiro com a fala narrada (sem montagem)'),
('Poucos dias depois da entrevista, Florinda voltou atrás.','O pedido de desculpas','Letreiro com o pedido narrado'),
('Em dois mil e dezoito, filhos e netos de Ramón','O amor do Brasil','Fãs brasileiros · Logo do SBT (crédito)'),
('Em dois mil e vinte e cinco, a história dele','A série','Divulgação da série (com crédito)'),
('O aluguel atrasado da vila era o aluguel','O que ele escondia','Chapéu do Seu Madruga ao pôr do sol (ilustrativo)'),
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
DESC='''Ramón Valdés, o eterno Seu Madruga do Chaves, morreu em 9 de agosto de 1988, aos 63 anos, na Cidade do México. Por trás do sorriso do personagem mais amado da vila, existia uma dor que ele nunca mostrou para as câmeras.

Neste documentário, a história completa: o menino Moncho, irmão de Tin Tan; os anos à sombra do irmão famoso; a pobreza real, com o aluguel atrasado "várias vezes", segundo o filho Esteban; o "seja você mesmo" de Chespirito; a saída do Chaves no auge e as versões que não batem; o circo; o câncer de 1985; a última viagem ao Peru; as últimas palavras a Kiko no hospital; o velório quase vazio; e Angelines Fernández, a Bruxa do 71, enterrada a cinco metros dele.

Informações de Wikipedia ES/PT, Folhapress, Excélsior, El Imparcial, TV Azteca, El País Cali, La Kalle, Noticias Caracol, UnoTV, America TV, Trome, El Dínamo, Vistazo, El Universal e The Noite (SBT). Versões em conflito estão atribuídas a quem as contou. A acusação feita por Florinda Meza em 2016 foi retratada por ela própria.

{CHAPS}

#SeuMadruga #RamonValdes #Chaves'''.replace('{CHAPS}',CHAPS)
TAGS='seu madruga, ramón valdés, ramon valdes, seu madruga morte, morte do seu madruga, chaves, el chavo del 8, don ramón, tin tan, florinda meza, kiko, bruxa do 71, angelines fernández, últimas palavras seu madruga, seu madruga história real, chespirito'
assert len(TAGS)<=500
open('desc.txt','w').write(DESC+'\n'); open('tags.txt','w').write(TAGS+'\n')
rows=''.join(f'<tr><td class="t">{t}</td><td><b>{html.escape(n)}</b><br>{html.escape(i)}</td></tr>\n' for t,n,i in out)
CAUT='''<li>Drogas: só como acusação de Florinda (2016), sempre com a retratação dela; nunca em letreiro ou thumbnail.</li>
<li>"Só Angelines foi ao velório" é relato do neto Miguel: manter a atribuição.</li>
<li>Ausência de Chespirito: as versões estão em conflito; não afirmar que Florinda o impediu.</li>
<li>Não dizer que ele "morreu pobre": a pobreza documentada é de antes da fama.</li>
<li>Cigarro e câncer: não afirmar causa; só mostrar que ele fumava.</li>
<li>Trechos de Chaves e Chapolin: curtos, licenciados ou com crédito.</li>
<li>Rostos reais: só fotos de arquivo com crédito; nunca rosto gerado por IA.</li>'''
json.dump({'title':TITLE,'desc':DESC,'tags':TAGS,'chaps':CHAPS,'rows':rows,'caut':CAUT,'paras':paras,'words':W},open('pack.json','w'),ensure_ascii=False)
print(CHAPS); print(W, round(W/WPM,1), len(TAGS))
