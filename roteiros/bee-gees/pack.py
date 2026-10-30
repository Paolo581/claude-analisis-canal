import re, html, json
TITLE="Assim FOI a VIDA dos BEE GEES — O Segredo SOMBRIO Que Destruiu os Irmãos Mais Famosos do Mundo"
WPM=135
raw=[]
for n in range(1,10):
    for p in open(f'bloco{n}.txt').read().split('\n\n'):
        if p.strip(): raw.append(p.strip())
paras=[re.sub(r'^[RA]: ','',p) for p in raw]
open('roteiro_completo.txt','w').write('\n\n'.join(raw)+'\n')
open('voz.txt','w').write('\n\n'.join(paras)+'\n')
W=sum(len(p.split()) for p in paras)
CH=[('Nos anos setenta, não havia pista','Os irmãos que fizeram o mundo dançar','Bee Gees no auge, anos 70 (foto pública, com crédito)'),
('Primeiro de setembro de mil novecentos e quarenta e seis.','Ilha de Man, 1946','Douglas, Ilha de Man, anos 40 (arquivo)'),
('Barry tinha quase dois anos.','Vinte minutos de vida','Bule de chá antigo (ilustrativo)'),
('Vinte e dois de dezembro de mil novecentos e quarenta e nove.','Os gêmeos','Foto pública dos irmãos crianças (com crédito)'),
('Manchester, mil novecentos e cinquenta e cinco.','Manchester','Manchester anos 50 (arquivo)'),
('Dezembro de mil novecentos e cinquenta e sete.','O disco quebrado','Cinema antigo (ilustrativo)'),
('Fora do palco, porém, a vida dos meninos','O carrinho e a Justiça','Carrinho de pedal antigo (ilustrativo)'),
('Em mil novecentos e cinquenta e oito, os Gibb tomaram','A viagem para a Austrália','Navio de imigrantes anos 50 (arquivo)'),
('Uma pista de corrida de carros, o Redcliffe Speedway.','O nome Bee Gees','Pista de corrida australiana anos 50 (arquivo)'),
('Na Austrália, os Bee Gees foram crescendo devagar.','Spicks and Specks','Foto pública dos Bee Gees jovens (com crédito)'),
('Janeiro de mil novecentos e sessenta e sete.','Londres e Stigwood','Londres anos 60 (arquivo)'),
('O nome dela era Massachusetts.','Massachusetts','Disco de vinil (ilustrativo)'),
('Cinco de novembro de mil novecentos e sessenta e sete.','O trem de Hither Green','Arquivo de jornal do acidente (com crédito)'),
('Robin tinha uma das vozes mais marcantes do grupo.','Os ciúmes','Foto pública de Robin (com crédito)'),
('Dezenove de março de mil novecentos e sessenta e nove.','A guerra de 1969','Manchetes de jornal (ilustrativo)'),
('Segundo Maurice Gibb, num documentário','Os apelidos dos vícios','Estúdio vazio (ilustrativo)'),
('Em mil novecentos e setenta, Barry se casou com Linda Gray','Linda','Foto pública de Barry e Linda (com crédito)'),
('Segundo Maurice, quem apresentou a ele o uísque','Maurice e a bebida','Copo de uísque (ilustrativo)'),
('Primeiro de dezembro de mil novecentos e sessenta e nove.','O fim do grupo','Palco vazio (ilustrativo)'),
('Barry estava de férias na Espanha quando o telefone tocou.','O telefonema','Telefone antigo (ilustrativo)'),
('Miami, mil novecentos e setenta e cinco.','Miami e o falsete','Miami anos 70 (arquivo)'),
('O filme se chamava Saturday Night Fever.','Os Embalos de Sábado à Noite','Cartaz do filme (com crédito)'),
('Sete músicas escritas pelos irmãos Gibb','O topo do mundo','Discos de ouro (ilustrativo)'),
('Andy Gibb tinha crescido.','Andy, o caçula','Foto pública de Andy (com crédito)'),
('Doze de julho de mil novecentos e setenta e nove. Chicago.','A fogueira de Chicago','Arquivo da Disco Demolition Night (com crédito)'),
('Andy Gibb tinha conhecido a cocaína.','A queda de Andy','Holofote apagado (ilustrativo)'),
('Cinco de março de mil novecentos e oitenta e oito.','A morte de Andy','Velas (ilustrativo)'),
('Barry disse que as últimas palavras de Andy','As últimas palavras','Foto pública de Barry e Andy (com crédito)'),
('O homem que nunca se recuperou da morte de Andy','O pai','Foto pública de Hugh Gibb (com crédito)'),
('Em mil novecentos e oitenta, Barry e Robin compuseram','Sucessos para outros','Capas de discos (com crédito)'),
('Mil novecentos e noventa e um.','A arma','Casa à noite (ilustrativo, sem arma)'),
('Maurice foi para uma clínica de reabilitação.','A sobriedade','Nascer do sol (ilustrativo)'),
('Dois mil e três. Miami.','A morte de Maurice','Fachada de hospital (ilustrativo)'),
('Robin era casado com Dwina Murphy','A vida secreta de Robin','Foto pública de Robin (com crédito)'),
('Robin tinha cantado em São Paulo em dois mil e cinco.','Os shows cancelados no Brasil','Arquivo de jornal brasileiro (com crédito)'),
('Vinte de maio de dois mil e doze.','A morte de Robin','Flores (ilustrativo)'),
('Barry disse que ele e Robin funcionavam na música.','Irmãos, mas não amigos','Barry sozinho (foto pública, com crédito)'),
('Barry Gibb ficou sozinho.','O último Bee Gee','Barry em show recente (foto pública, com crédito)'),
('Barry disse que, por ser o mais velho','Culpa de sobrevivente','Documentário HBO (frame com crédito)'),
('Primeiro de setembro de dois mil e vinte e seis.','Oitenta anos','Estátua dos Bee Gees em Douglas (foto pública)'),
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
DESC='''Eles fizeram o mundo inteiro dançar e se apaixonar. Mas, longe dos palcos, os irmãos Gibb guardavam uma rivalidade e vícios que foram derrubando a família, um irmão atrás do outro. Hoje, só Barry Gibb está vivo, aos 80 anos, e ele contou o que realmente destruiu os Bee Gees.

Neste documentário: a queimadura que quase matou Barry aos 2 anos; Manchester e a viagem para a Austrália; o nome nascido numa pista de corrida; Massachusetts e o desastre de trem de Robin; a guerra de 1969; os apelidos dos vícios; Os Embalos de Sábado à Noite; a noite de Chicago em 1979; a queda e a morte de Andy Gibb; a arma de Maurice e a sobriedade; as mortes de Maurice e Robin; e a culpa de sobrevivente de Barry.

Informações de entrevistas de Barry Gibb (CBS, Rolling Stone, The Guardian/Irish Times, The Times), do documentário "The Bee Gees: How Can You Mend a Broken Heart" (HBO, 2020), da revista Mojo, BBC, CBS News, ABC News, People e Manx Radio. Relatos são atribuídos às pessoas que os fizeram. Informações disponíveis até 30/10/2026.

{CHAPS}

#BeeGees #BarryGibb #AndyGibb'''.replace('{CHAPS}',CHAPS)
TAGS='bee gees, barry gibb, robin gibb, maurice gibb, andy gibb, bee gees história, bee gees documentário, os embalos de sábado à noite, stayin alive, how deep is your love, último bee gee, morte de andy gibb, irmãos gibb, assim foi a vida, disco music'
assert len(TAGS)<=500
open('desc.txt','w').write(DESC+'\n'); open('tags.txt','w').write(TAGS+'\n')
rows=''.join(f'<tr><td class="t">{t}</td><td><b>{html.escape(n)}</b><br>{html.escape(i)}</td></tr>\n' for t,n,i in out)
CAUT='''<li>Barry Gibb está vivo: nenhuma informação de saúde além de "saudável e feliz" (família, maio de 2026). Não usar vídeos de boatos de morte.</li>
<li>Andy: causa da morte = miocardite; a família negou overdose. Nunca escrever "overdose".</li>
<li>Delitos de infância e pena suspensa: sempre "segundo a revista Mojo".</li>
<li>Maurice e a arma (1991): sem imagem de arma; usar ilustração neutra.</li>
<li>Hospital de Maurice: acusação dos irmãos, sem processo concluído.</li>
<li>Robin: filha com a governanta só como fato; causa da morte com as duas versões (imprensa e filho).</li>
<li>Disco Demolition Night: não afirmar que discos dos Bee Gees foram queimados.</li>
<li>Nunca rosto gerado por IA. Fotos reais com crédito.</li>'''
json.dump({'title':TITLE,'desc':DESC,'tags':TAGS,'chaps':CHAPS,'rows':rows,'caut':CAUT,'paras':paras,'words':W},open('pack.json','w'),ensure_ascii=False)
print(CHAPS); print(W, round(W/WPM,1), len(TAGS))
