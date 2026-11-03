import re, html, json
TITLE="Assim FOI a VIDA de JACKIE KENNEDY — O Segredo SOMBRIO Que Ela Escondeu Atrás do Sorriso Mais Famoso do Mundo"
WPM=135
raw=[]
for n in range(1,9):
    for p in open(f'bloco{n}.txt').read().split('\n\n'):
        if p.strip(): raw.append(p.strip())
paras=[re.sub(r'^[RA]: ','',p) for p in raw]
open('roteiro_completo.txt','w').write('\n\n'.join(raw)+'\n')
open('voz.txt','w').write('\n\n'.join(paras)+'\n')
W=sum(len(p.split()) for p in paras)
CH=[('Ela virou primeira-dama','O sorriso mais famoso','Jackie sorrindo, anos 60 (foto pública, com crédito)'),
('Vinte e oito de julho de mil novecentos e vinte e nove.','Southampton, 1929','Praia dos Hamptons antiga (arquivo)'),
('O nome dele era John Vernou Bouvier','Black Jack','Foto pública de John Bouvier III (com crédito)'),
('Os cavalos. A mãe era uma amazona','A menina no cavalo','Jackie criança a cavalo (foto pública, com crédito)'),
('Enquanto a filha ganhava prêmios','O escândalo dos pais','Jornal antigo (ilustrativo)'),
('O nome dele era Hugh Auchincloss.','O padrasto rico','Hammersmith Farm, Newport (foto pública)'),
('Aos dezoito anos, Jackie','Debutante do ano','Baile de debutantes anos 40 (arquivo)'),
('Em mil novecentos e cinquenta e um, a revista Vogue','O prêmio recusado','Paris anos 50 (arquivo)'),
('Ela virou a garota da câmera do jornal.','A garota da câmera','Câmera fotográfica antiga (ilustrativo)'),
('O nome dele era John Fitzgerald Kennedy.','John Kennedy','JFK senador (foto pública, com crédito)'),
('Doze de setembro de mil novecentos e cinquenta e três.','O casamento do ano','Casamento Kennedy, Newport 1953 (arquivo)'),
('Black Jack, o pai que ela adorava','O pai que não veio','Igreja vazia (ilustrativo)'),
('Para o público, John Kennedy era a imagem da saúde.','A doença escondida','Quarto de hospital anos 50 (ilustrativo)'),
('Segundo vários livros escritos sobre o casal','O silêncio','Janela com cortina (ilustrativo)'),
('Agosto de mil novecentos e cinquenta e seis.','O iate e o hospital','Mar Mediterrâneo (ilustrativo)'),
('Jackie queria dar à filha','O túmulo "Filha"','Flores sobre lápide (ilustrativo)'),
('E é desse período que vem','O boato do dinheiro','Notas antigas de dólar (ilustrativo)'),
('Agosto de mil novecentos e cinquenta e sete.','Black Jack e Caroline','Foto pública de Jackie com Caroline bebê (com crédito)'),
('Mil novecentos e sessenta. John Kennedy entrou','A campanha','Campanha de 1960 (arquivo)'),
('Vinte de janeiro de mil novecentos e sessenta e um.','A Casa Branca','Posse de 1961 (arquivo)'),
('Em fevereiro de mil novecentos e sessenta e dois, ela abriu','O tour pela TV','Tour pela Casa Branca, 1962 (arquivo)'),
('Paris, maio de mil novecentos e sessenta e um.','Paris aos pés dela','Jackie em Paris, 1961 (arquivo)'),
('O nome dele era Max Jacobson.','O Doutor Bem-Estar','Seringa antiga (ilustrativo)'),
('O verão de mil novecentos e sessenta e dois','A estagiária','Corredor da Casa Branca (arquivo)'),
('Ela se chamava Judith Campbell.','A mulher da máfia','Chicago anos 60 (arquivo)'),
('Dezenove de maio de mil novecentos e sessenta e dois.','Marilyn','Madison Square Garden anos 60 (arquivo)'),
('Sete de agosto de mil novecentos e sessenta e três.','Patrick','Berço vazio (ilustrativo)'),
('Em outubro, a irmã dela, Lee','O cruzeiro de Onassis','Iate no mar Egeu (ilustrativo)'),
('Vinte e dois de novembro de mil novecentos e sessenta e três.','Dallas','Love Field, Dallas 1963 (arquivo)'),
('Poucos minutos depois, o carro entrou','Dealey Plaza','Dealey Plaza hoje (foto pública)'),
('Pouco depois, a bordo do avião presidencial','O juramento no avião','Air Force One (arquivo)'),
('Vinte e cinco de novembro de mil novecentos e sessenta e três.','O funeral','Funeral de JFK (arquivo)'),
('Era o aniversário de três anos','A continência','Foto da continência de John Jr. (arquivo, com crédito)'),
('No fim de novembro, Jackie chamou','Camelot','Castelo medieval (ilustrativo)'),
('E a roupa cor-de-rosa. Ela nunca foi lavada.','A roupa de 2103','Arquivos Nacionais dos EUA (foto pública)'),
('Depois do funeral, Jackie deixou','Georgetown','Casa em Georgetown (arquivo)'),
('Nesse período, Jackie conversava','A confissão ao padre','Igreja vazia ao entardecer (ilustrativo)'),
('Em mil novecentos e sessenta e oito, Robert','Robert Kennedy','Foto pública de Robert Kennedy (com crédito)'),
('Vinte de outubro de mil novecentos e sessenta e oito.','Onassis','Capela em ilha grega (ilustrativo)'),
('O nome dele era Ron Galella.','O paparazzo','Fotógrafo com câmera (ilustrativo)'),
('Em janeiro de mil novecentos e setenta e três','A queda de Onassis','Avião antigo (ilustrativo)'),
('Em mil novecentos e setenta e cinco, Jackie foi trabalhar','A editora','Livros e escrivaninha (ilustrativo)'),
('O nome dele era Maurice Tempelsman.','Maurice Tempelsman','Central Park (foto pública)'),
('Jackie passava os fins de semana montando','A volta aos cavalos','Cavalo no campo (ilustrativo)'),
('Janeiro de mil novecentos e noventa e quatro.','O diagnóstico','Janela de apartamento em Nova York (ilustrativo)'),
('Dezenove de maio de mil novecentos e noventa e quatro.','A despedida','Cemitério de Arlington (foto pública)'),
('Dezesseis de julho de mil novecentos e noventa e nove.','John Jr.','Mar ao entardecer (ilustrativo)'),
('A filha de Caroline, Tatiana','Tatiana','Flores brancas (ilustrativo)'),
('Olhando para trás','As duas histórias','Montagem de fotos públicas de Jackie (com crédito)'),
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
DESC='''Ela foi a mulher mais admirada do mundo. Mas, atrás do sorriso mais famoso do século, Jackie Kennedy escondia uma vida de perdas e segredos: o pai alcoólatra, as traições do marido, os bebês que ela enterrou e um pensamento que só veio à tona décadas depois, nas anotações de um padre.

Neste documentário: a infância em Southampton e Black Jack Bouvier; o prêmio da Vogue recusado; a garota da câmera; o casamento de 1953; a doença escondida de JFK; a filha nascida morta e o túmulo "Filha"; Paris, 1961; o Doutor Bem-Estar; as traições; Patrick; Dallas e a roupa cor-de-rosa guardada até 2103; Camelot; a confissão ao padre; Onassis; o paparazzo; a editora; e as tragédias que continuaram até 2025.

Fontes: JFK Library, Arquivos Nacionais dos EUA, Comissão Warren, diário de Lady Bird Johnson, anotações do padre Richard McSorley (Universidade de Georgetown), livros de Mimi Alford e Robert Dallek, Comissão Church, History.com, ABC News, PBS e reportagens da época. Relatos são atribuídos a quem os fez. Informações disponíveis até 03/11/2026.

{CHAPS}

#JackieKennedy #JFK #Kennedy'''.replace('{CHAPS}',CHAPS)
TAGS='jackie kennedy, jacqueline kennedy onassis, jackie kennedy história, john kennedy, jfk, família kennedy, maldição kennedy, dallas 1963, roupa rosa jackie, aristóteles onassis, john kennedy jr, assim foi a vida, primeira dama, documentário'
assert len(TAGS)<=500
open('desc.txt','w').write(DESC+'\n'); open('tags.txt','w').write(TAGS+'\n')
rows=''.join(f'<tr><td class="t">{t}</td><td><b>{html.escape(n)}</b><br>{html.escape(i)}</td></tr>\n' for t,n,i in out)
CAUT='''<li>Dallas: sem imagens do momento dos tiros, nem do sangue no tecido. Usar fotos do aeroporto antes do desfile e do funeral.</li>
<li>Pensamento suicida: só como está nas anotações do padre McSorley (liberadas em 2003), sem detalhes e com tom respeitoso.</li>
<li>Fotos de nudez em Skorpios: só mencionar como invasão de privacidade. Nunca mostrar nem descrever.</li>
<li>Marilyn e JFK, Robert e Jackie, dinheiro de Joseph Kennedy: sempre como boatos nunca provados.</li>
<li>Caroline Kennedy e Jack Schlossberg estão vivos: nenhuma especulação. Tatiana: só o que ela escreveu e o que a família divulgou.</li>
<li>Audiência do tour pela TV: "dezenas de milhões". Herança de Onassis: "entre 20 e 26 milhões de dólares".</li>
<li>Fotos reais com crédito. Nunca rosto gerado por IA.</li>'''
json.dump({'title':TITLE,'desc':DESC,'tags':TAGS,'chaps':CHAPS,'rows':rows,'caut':CAUT,'paras':paras,'words':W},open('pack.json','w'),ensure_ascii=False)
print(CHAPS); print(W, round(W/WPM,1), len(TAGS))
