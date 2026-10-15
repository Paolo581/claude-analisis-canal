import re, html, json
TITLE="ANA MARIA BRAGA: 10% de Chance de Viver — A Verdade HORRÍVEL Que a Globo Não Mostrou"
WPM=135
raw=[]
for n in range(1,8):
    for p in open(f'bloco{n}.txt').read().split('\n\n'):
        if p.strip(): raw.append(p.strip())
paras=[re.sub(r'^[RA]: ','',p) for p in raw]
open('roteiro_completo.txt','w').write('\n\n'.join(raw)+'\n')
open('voz.txt','w').write('\n\n'.join(paras)+'\n')
W=sum(len(p.split()) for p in paras)
CH=[('Dez por cento.','Dez por cento','Estúdio de cozinha de TV vazio de madrugada (ilustrativo) · Letreiro "10%"'),
('Mas antes de chegar àquele estúdio','O pai armado','Cidade do interior paulista anos 50 (arquivo genérico) · Chapéu e terno de linho (ilustrativo)'),
('Boa parte da infância','O colégio interno','Corredor de colégio interno antigo (ilustrativo)'),
('Numa entrevista em dois mil e quinze','A fuga pela janela','Janela aberta à noite · Letreiro "18 anos"'),
('Foi lá que o pai apareceu.','O revólver 38','Letreiro com a frase do Roda Viva · Porta de casa antiga (ilustrativo). Nunca mostrar arma apontada'),
('Anos setenta.','TV Tupi','Trecho curto do vídeo da Tupi (com crédito) · Logo histórico da Tupi'),
('Naquela época, ela tinha uma companhia','O cigarro','Cigarro em cinzeiro, fumaça (ilustrativo)'),
('Muitos anos depois, no Roda Viva, ela contou um episódio','A escada','Escada de prédio comercial antigo (ilustrativo) · Letreiro "Quebrei o braço"'),
('Mil novecentos e noventa e um.','O primeiro câncer','Letreiro "1991 · câncer de pele" · Praia italiana com sol forte (ilustrativo)'),
('Começo dos anos noventa.','As panelas da Record','Panelas antigas numa bancada (ilustrativo) · Trecho curto do Note e Anote (com crédito)'),
('Até o dia em que ela resolveu cobrar','"A porta da rua"','Letreiro com a frase · Porta de emissora fechada (genérica)'),
('Junho de mil novecentos e noventa e nove.','O nome do papagaio','Trecho da estreia do Mais Você (com crédito) · Letreiro "José"'),
('O câncer voltou.','Morfina todo dia','Corredor de hospital à noite (ilustrativo) · Letreiro "morfina todo dia"'),
('Ela mesma contou ao vivo, no Mais Você, como foi.','Seis milímetros','Tomografia de pulmão genérica · Letreiro "6 mm"'),
('Sexta-feira, vinte e quatro de janeiro de dois mil e vinte.','O anúncio de 2020','Trecho curto do anúncio no Mais Você (com crédito)'),
('Primeiro de agosto de dois mil e vinte e três.','O número','Letreiro "10% a 20%" · Fundo escuro'),
('Sexta-feira, sete de fevereiro de dois mil e vinte.','O casamento na quimioterapia','Alianças sobre mesa (ilustrativo)'),
('Março de dois mil e vinte. A pandemia.','A pandemia','Ruas vazias de São Paulo em 2020 (arquivo)'),
('Domingo, primeiro de novembro de dois mil e vinte.','Tom Veiga','Foto de imprensa de Tom Veiga (com crédito) · Fantoche verde em silhueta'),
('A aliança tinha sumido.','A aliança que sumiu','Mão sem aliança em close (ilustrativo)'),
('Primeiro de julho de dois mil e vinte e um.','O diário','Caderno fechado com cadeado (ilustrativo) · Letreiros "versão da promotora: em tese" / "Johnny nega"'),
('Abril de dois mil e vinte e quatro.','O segredo do cigarro','Letreiro "não parei de fumar"'),
('Última semana de dezembro de dois mil e vinte e quatro.','Alta total','Letreiro "Alta total" · Céu claro'),
('Sexta-feira, quatro de abril de dois mil e vinte e cinco.','O quinto casamento','Fotos públicas do casamento (com crédito)'),
('Domingo, vinte e oito de junho de dois mil e vinte e seis.','"Eu decidi viver"','Letreiro com a frase'),
('Sexta-feira, trinta e um de julho de dois mil e vinte e seis.','O helicóptero','Helicóptero sobre São Paulo (imagem de banco) · Girassóis'),
('Lembra da conversa que ela nunca teve com o pai?','"Ele nunca mais me reconheceu"','Cadeira vazia numa sala antiga (ilustrativo) · Letreiro com a frase'),
('Louro José.','O nome do pai','Fantoche verde em silhueta · Letreiro "José"'),
('Quase todo mundo tem uma conversa','A conversa pendente','Telefone antigo sobre mesa (ilustrativo)'),
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
DESC='''Em 2020, o câncer de pulmão de Ana Maria Braga voltou com metástase. A chance de dar certo, segundo o próprio oncologista, era de 10% a 20%. Três dias depois da primeira sessão de tratamento, ela estava ao vivo no Mais Você, sorrindo. Neste documentário: o pai que foi buscá-la com um revólver quando ela fugiu para estudar, as panelas que ela levava de casa para a Record, a morfina que ninguém viu, a morte de Tom Veiga, o Louro José, a aliança que sumiu, o diário do ex-marido, o cigarro que ela não largou e a dor que ela esconde até hoje atrás do sorriso.

As falas citadas foram dadas pela própria Ana Maria Braga em entrevistas e programas (Roda Viva, Podpah, Conversa com Bial, Fantástico, Mais Você). Sobre o diário de Johnny Lucet, apresentamos a opinião da promotora em tese e a versão dele, que nega as acusações publicadas.

{CHAPS}

#AnaMariaBraga #MaisVocê #LouroJosé'''.replace('{CHAPS}',CHAPS)
TAGS='ana maria braga, ana maria braga câncer, ana maria braga história, ana maria braga pai, louro josé, tom veiga, mais você, ana maria braga johnny lucet, ana maria braga cigarro, ana maria braga fábio arruda, ana maria braga 2026, ana maria braga câncer de pulmão, ana maria braga alta total, ana maria braga record'
assert len(TAGS)<=500
open('desc.txt','w').write(DESC+'\n'); open('tags.txt','w').write(TAGS+'\n')
rows=''.join(f'<tr><td class="t">{t}</td><td><b>{html.escape(n)}</b><br>{html.escape(i)}</td></tr>\n' for t,n,i in out)
CAUT='''<li>O pai: nunca encenar arma apontada; usar só letreiro com a frase dela. Tom de memória, sem vilão.</li>
<li>Diário de Johnny Lucet: letreiros "a promotora falou em tese" e "Johnny nega" sempre juntos. Não inventar conteúdo do diário.</li>
<li>Tom Veiga: tom de tributo. Nada de imagens do local da morte.</li>
<li>Câncer: sem imagens médicas chocantes; nada de sugerir que ela está doente hoje (teve alta total em 2024).</li>
<li>Julho de 2026: deixar claro que eram exames de rotina e que ela teve alta no mesmo dia.</li>
<li>Família: não mencionar o processo da filha (segredo de justiça).</li>
<li>Rostos reais: só fotos de imprensa ou publicações com crédito; nunca rosto gerado por IA. Trechos de TV curtos e com crédito.</li>'''
json.dump({'title':TITLE,'desc':DESC,'tags':TAGS,'chaps':CHAPS,'rows':rows,'caut':CAUT,'paras':paras,'words':W},open('pack.json','w'),ensure_ascii=False)
print(CHAPS); print(W, round(W/WPM,1), len(TAGS))
