import re, html, json
TITLE="CHARLIE CHAPLIN: O Segredo REPUGNANTE Por Trás do Homem Que Fez o Mundo Rir"
WPM=135
raw=[]
for n in range(1,10):
    for p in open(f'bloco{n}.txt').read().split('\n\n'):
        if p.strip(): raw.append(p.strip())
paras=[re.sub(r'^[RA]: ','',p) for p in raw]
open('roteiro_completo.txt','w').write('\n\n'.join(raw)+'\n')
open('voz.txt','w').write('\n\n'.join(paras)+'\n')
W=sum(len(p.split()) for p in paras)
CH=[('Ele fez o mundo inteiro rir','O homem que fez o mundo rir','Montagem de cenas clássicas do Carlitos (domínio público/licenciadas) · Chapéu-coco e bengala'),
('Mas, para entender esse segredo','A primeira mulher','Londres vitoriana (arquivo) · Cartaz de teatro de variedades'),
('Mil oitocentos e noventa e quatro.','A noite da voz','Palco vitoriano à luz de gás (ilustrativo) · Moedas no chão do palco'),
('Sem os palcos, Hannah passou a costurar','A pobreza','Máquina de costura antiga · Ruelas de Londres 1890 (arquivo)'),
('O asilo de pobres.','O asilo de pobres','Fotos de época de workhouses (arquivo) · Uniformes'),
('Três semanas depois','A escola de órfãos','Escola de Hanwell (arquivo) · Corredor vazio'),
('Foi nesse vai e vem','O hospício','Cane Hill (arquivo) · Janela com grades'),
('Sem pai, sem mãe e sem casa','O teatro','Jornais antigos, teatro de época'),
('O irmão Sydney também tinha virado ator.','Fred Karno','Cartaz da trupe de Karno (arquivo)'),
('A trupe de Fred Karno levou Charlie','Hollywood','Navio transatlântico · Keystone Studios (arquivo)'),
('Logo nos primeiros filmes','Nasce o Carlitos','Primeiras imagens do personagem (domínio público)'),
('O Carlitos virou uma febre.','A fama','Filas de cinema dos anos 1910 (arquivo)'),
('O nome dela era Mildred Harris.','Mildred Harris','Foto de imprensa de Mildred Harris (arquivo)'),
('Julho de mil novecentos e dezenove.','O Pequeno Rato','Berço vazio em penumbra (ilustrativo) · Lápide genérica'),
('Pouco depois da morte do bebê','O Garoto','Cenas de O Garoto (domínio público)'),
('O nome dela era Lillita MacMurray.','A menina das asas de anjo','Asas de figurino em fundo escuro (ilustrativo) · Letreiro "12 anos"'),
('Mil novecentos e vinte e quatro. O filme se chamava','Em Busca do Ouro','Cenas de Em Busca do Ouro (domínio público)'),
('Vinte e quatro de novembro de mil novecentos e vinte e quatro.','O casamento no México','Mapa de Sonora · Letreiro "16 anos"'),
('Dez de janeiro de mil novecentos e vinte e sete.','O processo','Manchetes de jornal 1927 (arquivo) · Letreiro "42 páginas"'),
('O cinema estava mudando.','Luzes da Cidade','Cenas de Luzes da Cidade / Tempos Modernos (licenciadas)'),
('E, em mil novecentos e quarenta, Charlie Chaplin fez a coisa mais corajosa','O Grande Ditador','Cenas de O Grande Ditador (licenciadas)'),
('O nome dela era Joan Barry.','Joan Barry','Foto de imprensa (arquivo)'),
('Dezesseis de junho de mil novecentos e quarenta e três.','Oona','Fotos de imprensa do casamento (arquivo) · Letreiro "18 e 54"'),
('A resposta veio de um laboratório.','O exame de sangue','Tubos de ensaio antigos · Letreiro "A ciência disse não. O júri disse sim."'),
('O nome dele era J. Edgar Hoover.','O FBI','Fotos de Hoover (arquivo) · Fichas datilografadas'),
('Setembro de mil novecentos e cinquenta e dois.','O navio','Queen Elizabeth no mar (arquivo)'),
('Dezenove de setembro','O exílio','Carimbo "permissão cancelada" (ilustrativo) · Lago Léman'),
('Abril de mil novecentos e setenta e dois.','A volta','Imagens do Oscar de 1972 (licenciadas)'),
('A mãe dele. Hannah,','A mãe','Casa à beira-mar (ilustrativo)'),
('Vinte e cinco de dezembro de mil novecentos e setenta e sete.','O Natal de 1977','Árvore de Natal à noite · Cemitério de Corsier-sur-Vevey'),
('Começo de março de mil novecentos e setenta e oito.','O túmulo vazio','Sepultura aberta (ilustrativo) · Cabine telefônica antiga'),
('Um milharal,','O milharal','Milharal ao entardecer'),
('E é aqui que tudo se encaixa.','O que ficou','Chapéu-coco sozinho num palco vazio'),
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
DESC='''Charlie Chaplin fez o mundo inteiro rir sem dizer uma palavra. Mas o homem por trás do Carlitos carregava uma infância de miséria (a mãe que perdeu a voz no palco e acabou num hospício, o asilo de pobres aos sete anos) e um padrão que Hollywood tentou abafar: as meninas que ele levou ao altar. Neste documentário: Mildred Harris, casada aos 16; Lita Grey, que ele escalou aos 12 como o anjo de O Garoto e com quem se casou grávida aos 16; o exame de sangue que provou que ele não era pai e o júri que decidiu o contrário; o FBI e o exílio no meio do mar; e o túmulo que dois homens abriram em 1978.

As informações vêm de biografias, registros públicos e reportagens (History.com, Wikipedia, CharlieChaplin.com, Workhouses.org.uk, ABA Journal, EBSCO). Idades e datas seguem as fontes citadas; quando divergem, usamos a aproximação.

{CHAPS}

#CharlieChaplin #Carlitos #HistóriaDoCinema'''.replace('{CHAPS}',CHAPS)
TAGS='charlie chaplin, carlitos, charlie chaplin história, charlie chaplin esposas, lita grey, oona oneill, charlie chaplin corpo roubado, charlie chaplin exílio, charlie chaplin mãe, charlie chaplin infância, o garoto chaplin, charlie chaplin fbi, documentário chaplin, cinema mudo'
assert len(TAGS)<=500
open('desc.txt','w').write(DESC+'\n'); open('tags.txt','w').write(TAGS+'\n')
rows=''.join(f'<tr><td class="t">{t}</td><td><b>{html.escape(n)}</b><br>{html.escape(i)}</td></tr>\n' for t,n,i in out)
CAUT='''<li>Nunca usar a palavra "vagabundo" em letreiros ou capítulos; usar Carlitos.</li>
<li>Meninas (Mildred, Lita, Oona): só fotos de imprensa da época com crédito; nada sexualizado; idades em letreiro neutro.</li>
<li>Joan Barry e Carol Ann: sem sugerir culpa de ninguém; mostrar o exame e o veredito como fatos.</li>
<li>Roubo do corpo: sem imagens reais do corpo; caixão e milharal ilustrativos.</li>
<li>Filmes de Chaplin: os anteriores a 1929 estão em domínio público em vários países; os demais precisam de licença ou uso curto com crédito.</li>
<li>Rostos reais: só fotos de arquivo com crédito; nunca rosto gerado por IA.</li>'''
json.dump({'title':TITLE,'desc':DESC,'tags':TAGS,'chaps':CHAPS,'rows':rows,'caut':CAUT,'paras':paras,'words':W},open('pack.json','w'),ensure_ascii=False)
print(CHAPS); print(W, round(W/WPM,1), len(TAGS))
