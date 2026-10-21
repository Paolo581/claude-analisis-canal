import re, html, json
TITLE="OS ÚLTIMOS MESES DE LUA BLANCO: A Doença Que Ela Enfrentou em Segredo"
WPM=135
raw=[]
for n in range(1,13):
    for p in open(f'bloco{n}.txt').read().split('\n\n'):
        if p.strip(): raw.append(p.strip())
paras=[re.sub(r'^[RA]: ','',p) for p in raw]
open('roteiro_completo.txt','w').write('\n\n'.join(raw)+'\n')
open('voz.txt','w').write('\n\n'.join(paras)+'\n')
W=sum(len(p.split()) for p in paras)
CH=[('Nos últimos meses de vida','Os últimos meses','Vela acesa · Céu ao entardecer (ilustrativo)'),
('Mas, para entender como alguém','Uma infância sem televisão','Casa simples com instrumentos musicais (ilustrativo)'),
('Dentro de casa, os filhos','Inglês, sem açúcar','Livros infantis em inglês · Frutas na mesa (ilustrativo)'),
('O pai de Lua se chamava','Cantando nos restaurantes','Restaurante antigo no Rio (ilustrativo)'),
('O grupo se chamava Família Blanco.','Família Blanco','Capa do disco "É Natal" (com crédito)'),
('Em dois mil e seis, Lua entrou na PUC','Lágrima Flor','Campus universitário · Guitarra (ilustrativo)'),
('E, enquanto isso, uma outra porta','Os primeiros palcos','Cortina de teatro (ilustrativo)'),
('A novela se chamava Rebelde.','Rebelde','Abertura/logotipo de Rebelde (com crédito)'),
('Só que, poucos meses depois da estreia','A morte do avô','Foto de arquivo de Billy Blanco (com crédito) · Piano fechado'),
('Lua seguiu em frente.','O furacão Rebeldes','Fotos de shows (imprensa, com crédito)'),
('Muitos anos depois, já longe daquela loucura','O preço escondido','Mala num quarto de hotel (ilustrativo)'),
('E, como se o cansaço não bastasse','Arthur e o fim da novela','Fotos de imprensa da época (com crédito)'),
('Lua não parou.','Depois de Rebelde','Fotos de imprensa (com crédito)'),
('Em setembro de dois mil e dezesseis','Leandro e a depressão','Mar aberto (ilustrativo, "oceano de liberdade")'),
('Ela entrou na segunda temporada do Popstar','O zero no Popstar','Telão com número genérico (ilustrativo)'),
('O projeto ganhou um nome','Órbita','Capa do disco Órbita (com crédito) · Lua no céu'),
('A família nunca divulgou os detalhes','O diagnóstico','Letreiro com os dados do INCA'),
('O pedido foi discrição.','O segredo','Porta fechada · Janela com luz (ilustrativo)'),
('Quem revelou foi a tia','Mais de oitenta pessoas','Mãos dadas (ilustrativo)'),
('A família de Lua sempre teve raízes cristãs.','A fé','Bíblia aberta (ilustrativo)'),
('A amiga se chama Ewellyn Laura.','A confissão','Celular com mensagem genérica (ilustrativo)'),
('Foi cerca de cinco dias antes do fim.','O último post','Letreiro "Momentos de gratidão" (sem print real)'),
('Lua Blanco morreu no dia dezoito','18 de outubro','Céu ao amanhecer · Letreiro com a data'),
('A tia, Maria Cândida','O último dia','Vela acesa (ilustrativo)'),
('O velório aconteceu na segunda-feira','O velório com música','Violão encostado (ilustrativo)'),
('Lembra dos cinco nomes?','Os cinco Rebeldes','Fotos públicas do elenco no velório (com crédito, sem close de caixão)'),
('Arthur Aguiar soube da morte','Arthur e Dulce María','Fotos de imprensa (com crédito)'),
('O nome dele é Leandro Soares.','A decisão de Leandro','Fachada da Casa de Cultura Laura Alvim (com crédito)'),
('Quando Billy Blanco morreu','O canto permanece','Palco vazio com um foco de luz (ilustrativo)'),
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
DESC='''Em 18 de outubro de 2026, aos 39 anos, Lua Blanco, a Roberta de "Rebelde", partiu. Da descoberta da doença até a despedida, foram cerca de dois meses. E ela escolheu atravessar tudo em segredo.

Neste documentário, a história completa: a infância numa casa sem televisão, a menina tímida que o pai fazia cantar de surpresa em restaurantes, a banda batizada com uma canção do avô Billy Blanco, a febre "Rebelde" e o preço escondido da fama, a depressão que ela só revelou depois, o disco "Órbita" e os últimos meses, cercada por mais de 80 pessoas. A mensagem de fé que ela escreveu a uma amiga, o velório com música, o reencontro dos cinco ex-Rebeldes e a decisão de Leandro Soares de subir ao palco dias depois do adeus.

Informações de CNN Brasil, Terra, Folha de Pernambuco, Metrópoles, O Globo/Extra, Correio, O Liberal, Exame, Purepeople, Popline e Jornal do Brasil. O tipo de câncer foi confirmado pela tia de Lua; a família não divulgou detalhes do tratamento. Dados: INCA e The Lancet Oncology (2024). Este vídeo não substitui orientação médica.

{CHAPS}

#LuaBlanco #Rebelde #Homenagem'''.replace('{CHAPS}',CHAPS)
TAGS='lua blanco, lua blanco últimos meses, lua blanco câncer, lua blanco morre, lua blanco segredo, lua blanco velório, rebelde, roberta rebelde, rebeldes reencontro, arthur aguiar lua blanco, leandro soares, billy blanco, lua blanco fé, câncer de intestino, lua blanco homenagem'
assert len(TAGS)<=500
open('desc.txt','w').write(DESC+'\n'); open('tags.txt','w').write(TAGS+'\n')
rows=''.join(f'<tr><td class="t">{t}</td><td><b>{html.escape(n)}</b><br>{html.escape(i)}</td></tr>\n' for t,n,i in out)
CAUT='''<li>Família pediu respeito ao luto: tom de homenagem, nada sensacionalista em letreiros.</li>
<li>Câncer: atribuir à tia (Maria Cândida); hospital e tratamento não foram divulgados, sem imagens de hospital real.</li>
<li>Mensagens às amigas (Ewellyn Laura, Fernanda Sutil): não mostrar prints com nome/foto das amigas.</li>
<li>"Sol": o Metrópoles diz irmã, a Vanity diz irmão; o roteiro usa "um dos irmãos".</li>
<li>Velório: só fotos públicas de imprensa com crédito, sem close de caixão.</li>
<li>Peça "A Coisa": data das sessões tem conflito (20 ou 21/10); o roteiro diz "dias depois do adeus".</li>
<li>Rostos reais: só fotos de arquivo/imprensa com crédito; nunca rosto gerado por IA.</li>'''
json.dump({'title':TITLE,'desc':DESC,'tags':TAGS,'chaps':CHAPS,'rows':rows,'caut':CAUT,'paras':paras,'words':W},open('pack.json','w'),ensure_ascii=False)
print(CHAPS); print(W, round(W/WPM,1), len(TAGS))
