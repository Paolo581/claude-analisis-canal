import re, html, json
TITLE="Assim FOI a VIDA de JFK JR. — A Verdade Por Trás do Casamento Mais Vigiado da América"
WPM=135
raw=[]
for n in range(1,9):
    for p in open(f'bloco{n}.txt').read().split('\n\n'):
        if p.strip(): raw.append(p.strip())
paras=[re.sub(r'^[RA]: ','',p) for p in raw]
open('roteiro_completo.txt','w').write('\n\n'.join(raw)+'\n')
open('voz.txt','w').write('\n\n'.join(paras)+'\n')
W=sum(len(p.split()) for p in paras)
CH=[('Ele tinha o sobrenome mais famoso','O príncipe da América','JFK Jr. nos anos 90 (foto pública, com crédito)'),
('Vinte e cinco de novembro de mil novecentos e sessenta.','O filho do presidente','Casa Branca, 1961 (arquivo)'),
('Outubro de mil novecentos e sessenta e três.','Embaixo da mesa','Foto de John Jr. sob a mesa do Salão Oval (arquivo, com crédito)'),
('John adorava helicópteros e aviões.','O menino e o helicóptero','Helicóptero no gramado da Casa Branca (arquivo)'),
('Vinte e um de novembro de mil novecentos e sessenta e três.','A última despedida','Base aérea, 1963 (arquivo)'),
('Na saída da igreja','A continência','Foto da continência (arquivo, com crédito)'),
('Em mil novecentos e sessenta e quatro, Jackie deixou','Nova York e as câmeras','Quinta Avenida anos 60 (arquivo)'),
('Na madrugada de cinco de junho','Robert Kennedy','Foto pública de Robert Kennedy (com crédito)'),
('Outubro de mil novecentos e sessenta e oito.','Onassis e as ilhas','Ilha grega (ilustrativo)'),
('O nome dele era Ron Galella.','O paparazzo','Fotógrafo com câmera antiga (ilustrativo)'),
('O padrasto tinha um único filho homem','Alexander Onassis','Pequeno avião antigo (ilustrativo)'),
('No fim dos anos setenta, John foi estudar','Andover e o Wyoming','Fazenda no Wyoming (ilustrativo)'),
('Durante o curso, o grupo dele se perdeu.','Perdido na África','Savana africana (ilustrativo)'),
('Na universidade de Brown','O sonho de ser ator','Palco de teatro vazio (ilustrativo)'),
('Ele foi estudar na Índia','Índia e Madre Teresa','Nova Délhi anos 80 (arquivo)'),
('Estudou na Universidade de Nova York','O exame da Ordem','Sala de prova (ilustrativo)'),
('John foi reprovado pela segunda vez.','O bonitão que levou bomba','Manchetes de jornal (ilustrativo)'),
('Novembro de mil novecentos e noventa. O resultado saiu.','A aprovação','Tribunal de Manhattan (foto pública)'),
('Dois anos antes, em mil novecentos e oitenta e oito','O homem mais sexy do mundo','Central Park (foto pública)'),
('A primeira namorada séria','Christina Haag','Caiaque no mar (ilustrativo)'),
('O segundo grande romance','Daryl Hannah','Flashes de câmeras (ilustrativo)'),
('Jackie tinha visto o que um avião','A promessa','Pequeno avião no hangar (ilustrativo)'),
('Dezenove de maio de mil novecentos e noventa e quatro.','A morte de Jackie','Prédio da Quinta Avenida (foto pública)'),
('Setembro de mil novecentos e noventa e cinco.','A revista George','Capa da George, 1995 (com crédito)'),
('O nome dela era Carolyn Bessette.','Carolyn','Foto pública de Carolyn Bessette (com crédito)'),
('Fevereiro de mil novecentos e noventa e seis.','A briga no parque','Parque de Nova York no inverno (ilustrativo)'),
('O lugar escolhido foi uma ilha quase deserta','Cumberland Island','Igreja de madeira em Cumberland Island (foto pública)'),
('Vinte e um de setembro de mil novecentos e noventa e seis.','O casamento secreto','Velas acesas (ilustrativo)'),
('Na porta do apartamento do casal','O cerco em Tribeca','Rua de Tribeca (foto pública)'),
('Carolyn Bessette nunca tinha pedido','Presa em casa','Janela de apartamento à noite (ilustrativo)'),
('Em setembro de mil novecentos e noventa e sete','O primo Michael','Montanha de esqui (ilustrativo)'),
('Segundo vários biógrafos e pessoas próximas','A crise','Sofá de consultório (ilustrativo)'),
('Em dois mil e três, um jornalista','O boato','Livro fechado (ilustrativo)'),
('Dezembro de mil novecentos e noventa e sete. John começou','O brevê','Cabine de pequeno avião (ilustrativo)'),
('No fim de maio de mil novecentos e noventa e nove','O gesso','Gesso e muletas (ilustrativo)'),
('Naquele mesmo dia, um instrutor','A ajuda recusada','Pista de aeroporto ao entardecer (ilustrativo)'),
('Dezesseis de julho de mil novecentos e noventa e nove.','A última decolagem','Aeroporto à noite (ilustrativo)'),
('Mas, quando a rota passou a cruzar o mar','A noite sem horizonte','Mar escuro com neblina (ilustrativo)'),
('Um ano depois, a investigação oficial','A investigação','Relatório oficial (ilustrativo)'),
('Já passava da meia-noite','A busca','Navio da Guarda Costeira (arquivo)'),
('Vinte e dois de julho de mil novecentos e noventa e nove.','As cinzas no mar','Mar ao amanhecer (ilustrativo)'),
('Ann Freeman entrou na Justiça','A mãe e o processo','Martelo de juiz (ilustrativo)'),
('Em novembro de dois mil e vinte e um','A teoria falsa','Dealey Plaza (foto pública)'),
('Em fevereiro de dois mil e vinte e seis','A série e a família','Claquete (ilustrativo)'),
('Olhando para trás','As câmeras','Montagem de fotos públicas (com crédito)'),
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
DESC='''Ele era o príncipe da América. Mas o casamento mais vigiado do país escondia um lado que os fãs nunca viram: uma briga filmada num parque, uma noiva cercada por fotógrafos, uma terapia de casal e, na última noite, uma ajuda recusada. Esta é a história real de John F. Kennedy Jr.

Neste documentário: a continência no dia do aniversário; o menino e o helicóptero; Robert Kennedy; Onassis e o acidente de Alexander; o sonho de ser ator; as duas reprovações na Ordem; Daryl Hannah; a morte de Jackie e a promessa; a revista George; Carolyn Bessette e o casamento secreto; o cerco em Tribeca; o boato; o gesso; a noite sem horizonte; o processo da família Bessette; a teoria falsa do QAnon; e a série de 2026.

Fontes: relatório do NTSB (NYC99MA178), UPI, Deseret News, Vineyard Gazette, NPS, NBC News, AOPA, ABC/PBS, Wikipedia e biografias citadas no vídeo. Relatos e boatos são atribuídos a quem os fez. Informações disponíveis até 04/11/2026.

{CHAPS}

#JFKJr #CarolynBessette #Kennedy'''.replace('{CHAPS}',CHAPS)
TAGS='jfk jr, john kennedy jr, carolyn bessette, jfk jr acidente, jfk jr casamento, família kennedy, maldição kennedy, love story série, john f kennedy jr história, lauren bessette, jackie kennedy, assim foi a vida, documentário'
assert len(TAGS)<=500
open('desc.txt','w').write(DESC+'\n'); open('tags.txt','w').write(TAGS+'\n')
rows=''.join(f'<tr><td class="t">{t}</td><td><b>{html.escape(n)}</b><br>{html.escape(i)}</td></tr>\n' for t,n,i in out)
CAUT='''<li>Acidente: sem imagens de destroços com corpos nem recriações da queda. Usar mar, céu escuro, aeroporto.</li>
<li>Briga no parque: sempre "segundo quem viu as imagens". Não mostrar o vídeo original sem direitos.</li>
<li>Drogas: só como alegação do livro de Edward Klein, com as negações (amigo próximo, Carole Radziwill).</li>
<li>Promessa a Jackie: fonte única (Christopher Andersen), sempre com essa ressalva.</li>
<li>Processo Bessette: acordo de 2001 com valor não divulgado; os 15 milhões foram negados pelo advogado.</li>
<li>QAnon: sempre como teoria falsa.</li>
<li>Pessoas vivas (Caroline, Ann Freeman, Lisa Bessette, Daryl Hannah, Christina Haag, Carole Radziwill, Jack Schlossberg): só falas e fatos públicos.</li>
<li>Fotos reais com crédito. Nunca rosto gerado por IA. Não usar cenas da série sem licença.</li>'''
json.dump({'title':TITLE,'desc':DESC,'tags':TAGS,'chaps':CHAPS,'rows':rows,'caut':CAUT,'paras':paras,'words':W},open('pack.json','w'),ensure_ascii=False)
print(CHAPS); print(W, round(W/WPM,1), len(TAGS))
