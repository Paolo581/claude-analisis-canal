import re, html, json
TITLE="Assim FOI a VIDA de EL MENCHO — O Segredo Que Levou o Homem Mais Procurado do México à Morte"
WPM=135
raw=[]
for n in range(1,9):
    for p in open(f'bloco{n}.txt').read().split('\n\n'):
        if p.strip(): raw.append(p.strip())
paras=[re.sub(r'^[RA]: ','',p) for p in raw]
open('roteiro_completo.txt','w').write('\n\n'.join(raw)+'\n')
open('voz.txt','w').write('\n\n'.join(paras)+'\n')
W=sum(len(p.split()) for p in paras)
CH=[('Vinte e dois de fevereiro de dois mil e vinte e seis. Um domingo.','Tapalpa, 22 de fevereiro','Montanhas de pinheiros ao amanhecer (ilustrativo)'),
('Aguililla fica no sudoeste','A Terra Quente','Paisagem de Michoacán (arquivo)'),
('A maioria das fontes fala','O menino Rubén','Plantação de abacate (ilustrativo)'),
('Naquela região, a maconha e a papoula','As plantações escondidas','Morros cobertos de mato (ilustrativo)'),
('De Aguililla, muita gente partia','Rumo ao norte','Fronteira México-EUA (arquivo)'),
('São Francisco, mil novecentos e oitenta e seis.','Preso em São Francisco','São Francisco anos 80 (arquivo)'),
('Setembro de mil novecentos e noventa e dois.','A armadilha de Sacramento','Tribunal americano (ilustrativo)'),
('A Justiça americana condenou Rubén','Prisão no Texas','Muro de penitenciária (ilustrativo)'),
('O homem que tinha acabado de sair','A farda de policial','Viatura antiga de polícia mexicana (ilustrativo)'),
('O grupo se chamava Cartel do Milênio.','O Cartel do Milênio','Guadalajara anos 2000 (arquivo)'),
('Ele se casou com Rosalinda','Os Cuinis','Notas de dólar (ilustrativo)'),
('Em algum momento dessa trajetória','El Mencho','Cartaz de procurado da DEA (oficial, com crédito)'),
('Vinte e nove de julho de dois mil e dez.','A morte de Nacho Coronel','Zapopan (arquivo)'),
('Essa facção ganhou um nome','Nasce o CJNG','Mapa de Jalisco (ilustrativo)'),
('Boca del Río, no estado de Veracruz.','Boca del Río, 2011','Viaduto vazio (ilustrativo, sem vítimas)'),
('O segredo do crescimento do Cartel Jalisco','A metanfetamina e os portos','Porto de contêineres (ilustrativo)'),
('Em dois mil e doze, uma operação militar','A fuga de Tonaya','Estrada de serra (ilustrativo)'),
('Em dois mil e quinze, o Departamento do Tesouro','As cabanas de Tapalpa','Cabanas entre pinheiros (ilustrativo)'),
('A primavera daquele ano foi','A guerra de 2015','Comboio policial (arquivo)'),
('Primeiro de maio de dois mil e quinze.','O helicóptero derrubado','Helicóptero militar em voo (ilustrativo)'),
('A segunda maior cidade do México parou.','Jalisco em chamas','Guadalajara com fumaça ao longe (arquivo)'),
('Lá no começo desta história, Rubén assumiu','A família','Retrato de família desfocado (ilustrativo)'),
('Janeiro de dois mil e catorze.','El Menchito','Algemas (ilustrativo)'),
('Rosalinda González Valencia foi presa','La Jefa','Zapopan (arquivo)'),
('Fevereiro de dois mil e vinte.','O tribunal de Washington','Tribunal federal de Washington (foto pública)'),
('Diziam que ele estava muito doente.','Os boatos','Manchetes de jornal (ilustrativo)'),
('Vinte e seis de junho de dois mil e vinte.','O atentado contra Harfuch','Avenida Reforma (foto pública)'),
('Outubro de dois mil e vinte e quatro.','O sobrevivente no poder','Foto oficial de García Harfuch (com crédito)'),
('Em dezembro de dois mil e vinte e quatro','15 milhões e terrorismo','Cartaz de recompensa (oficial, com crédito)'),
('Sete de março de dois mil e vinte e cinco.','Prisão perpétua','Martelo de juiz (ilustrativo)'),
('Março de dois mil e vinte e cinco. Um grupo de mães','O Rancho Izaguirre','Sapatos abandonados (foto de imprensa, com crédito)'),
('Durante mais de quinze anos, El Mencho tinha escapado','O ponto fraco','Estrada de montanha à noite (ilustrativo)'),
('Vinte de fevereiro de dois mil e vinte e seis.','Dois dias de vigilância','Carro em estrada de serra (ilustrativo)'),
('Vinte e um de fevereiro.','A cabana','Cabana no bosque (ilustrativo)'),
('Na madrugada seguinte','A operação','Helicópteros militares (arquivo)'),
('E, pouco depois, os militares encontraram','O fim no ar','Helicóptero ao entardecer (ilustrativo)'),
('Vinte e dois e vinte e três de fevereiro','O México em chamas','Estrada bloqueada (foto de imprensa, com crédito)'),
('Vinte e três de fevereiro. A Procuradoria','O DNA e o nome verdadeiro','Laboratório (ilustrativo)'),
('Três de março de dois mil e vinte e seis.','O caixão dourado','Cemitério ao longe (ilustrativo)'),
('Mas a morte do chefe não significou','O herdeiro','Bandeira do México (ilustrativo)'),
('Olhando para trás','As peças que se encaixam','Montagem com fotos oficiais (com crédito)'),
('Mas o ponto final desta história','As vítimas','Mães buscadoras (foto de imprensa, com crédito)'),
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
DESC='''Durante mais de 15 anos, ele foi o homem mais procurado do México. Os EUA ofereciam 15 milhões de dólares por ele. Mas, em 22 de fevereiro de 2026, El Mencho foi encontrado por causa de um segredo. Esta é a história real de Nemesio Oseguera Cervantes, o chefe do Cartel Jalisco Nova Geração: do menino pobre da Terra Quente ao ex-policial que construiu um império e terminou a vida dentro de um helicóptero do Exército.

Neste documentário: Aguililla e o nome verdadeiro; as prisões na Califórnia e a culpa assumida pelo irmão; a farda de policial; o Cartel do Milênio e os Cuinis; o nascimento do CJNG; o helicóptero derrubado em 2015; a queda da família; o atentado contra García Harfuch; o Rancho Izaguirre; Tapalpa; o DNA; o herdeiro nascido na Califórnia; e as vítimas.

Conteúdo documental e jornalístico, sem apologia ao crime. Fontes: Procuradoria-Geral da República (FGR), Departamento de Estado e Tesouro dos EUA, NCTC, Reuters, Al Jazeera, CBS News, Mexico News Daily, Zeta Tijuana, El Financiero, La Jornada, EFE e outras reportagens. Informações disponíveis até 02/11/2026.

{CHAPS}

#ElMencho #CJNG #México'''.replace('{CHAPS}',CHAPS)
TAGS='el mencho, el mencho morte, el mencho história, nemesio oseguera, cartel jalisco nova geração, cjng, el mencho tapalpa, morte de el mencho, cartel mexicano documentário, garcía harfuch, el menchito, rancho izaguirre, assim foi a vida, narcotráfico méxico'
assert len(TAGS)<=500
open('desc.txt','w').write(DESC+'\n'); open('tags.txt','w').write(TAGS+'\n')
rows=''.join(f'<tr><td class="t">{t}</td><td><b>{html.escape(n)}</b><br>{html.escape(i)}</td></tr>\n' for t,n,i in out)
CAUT='''<li>Sem imagens de corpos, sangue, armas apontadas ou violência explícita (monetização). Não glorificar: o tom é documental e o fim é dedicado às vítimas.</li>
<li>A companheira não é nomeada (as fontes divergem; versão oficial: "uma de suas companheiras").</li>
<li>Mortos na operação: só "vários" e "militares atingidos" (números divergentes). Os 25 guardas nacionais: "segundo o secretário de Segurança".</li>
<li>Rancho Izaguirre: crematório é versão dos coletivos de busca, contestada pela Procuradoria. Usar apenas a imagem dos sapatos.</li>
<li>Doença nos rins, clínica secreta, plástica no rosto e valor do caixão: sempre como boato ou não confirmado.</li>
<li>Rosalinda, Jessica e El 03: só processos, condenações e apontamentos oficiais. Para El 03, sempre "seria" ou "segundo os EUA".</li>
<li>Ex-policial: "segundo reportagens e investigações".</li>
<li>Usar fotos oficiais (DEA, FGR) e de imprensa com crédito. Nunca rosto gerado por IA.</li>'''
json.dump({'title':TITLE,'desc':DESC,'tags':TAGS,'chaps':CHAPS,'rows':rows,'caut':CAUT,'paras':paras,'words':W},open('pack.json','w'),ensure_ascii=False)
print(CHAPS); print(W, round(W/WPM,1), len(TAGS))
