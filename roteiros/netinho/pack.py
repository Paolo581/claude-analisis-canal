import re, html, json
TITLE="NETINHO: 13 Anos Entre a Vida e a Morte — A Luta HORRÍVEL Que o Rei do Axé Escondeu Com Um Sorriso"
WPM=135
files=['parte1.txt','parte2.txt','parte3.txt','parte4.txt','parte5.txt']
raw=[]
for f in files:
    for p in open(f).read().split('\n\n'):
        p=p.strip()
        if p: raw.append(p)
paras=[re.sub(r'^[RA]: ','',p) for p in raw]
open('voz.txt','w').write('\n\n'.join(paras)+'\n')
open('roteiro_completo.txt','w').write('\n\n'.join(raw)+'\n')
W=sum(len(p.split()) for p in paras)
CH=[('Treze de outubro de dois mil e vinte e seis. Uma terça-feira de manhã, em Salvador','A manhã de 13 de outubro','Fachada de hospital ao amanhecer (genérica, sem nome) · Letreiro "13/10/2026"'),
('Mil novecentos e sessenta e seis. Santo Antônio','O menino do Recôncavo','Imagens de Santo Antônio de Jesus e do Recôncavo · Letreiro "1966"'),
('Mil novecentos e oitenta e seis.','Banda Beijo e o nascimento do axé','Arquivo do Carnaval de Salvador anos 80 (com crédito) · Trio elétrico e multidão'),
('Mil novecentos e noventa e seis. Aracaju','Milla','Capa do disco Netinho ao Vivo (com crédito) · Trecho curto de Milla · Rádio antigo, padaria, praia'),
('Exatamente dezessete anos.','O preço do auge','Letreiro "1996 → 2013" · Palco vazio ao fim de um show'),
('Dois mil e dois.','A pausa e a pressão','Trio elétrico sob sol forte · Letreiro "40 anos"'),
('Dois verões.','A confissão','Manchete do Correio Braziliense de 2014 (com crédito) · Receita médica genérica desfocada'),
('Abril de dois mil e treze. Salvador.','O ensaio de abril de 2013','Sala de ensaio com instrumentos · Letreiro "26/04/2013 · Hospital Aliança"'),
('Vinte e cinco de maio de dois mil e treze.','Entre a vida e a morte','Corredor de UTI desfocado · Lista na tela: 3 AVCs, hemorragia, hidrocefalia, trombose, visão dupla, perda da fala'),
('Mas, numa publicação nas redes sociais','"A culpa é toda minha"','Letreiro com a frase dele (texto, não print)'),
('Só que a frase não terminava ali.','"Vi a morte de muito perto"','Letreiro com a frase completa · Música suave'),
('Trinta de novembro de dois mil e quinze.','A tontura','Letreiro com a mensagem dele · Janela de hospital à noite'),
('Oito de fevereiro de dois mil e catorze.','A foto da vitória','NÃO mostrar a foto entubado: usar letreiro "a foto da vitória" e o título do livro "Nada Como Viver!"'),
('Quatorze de agosto de dois mil e quinze.','A volta no Teatro Castro Alves','Fachada do Teatro Castro Alves · Trecho do Globo de Ouro Palco Viva (com crédito)'),
('Fevereiro de dois mil e dezessete.','Carnaval de 2017','Arquivo do Carnaval de Salvador 2017 (com crédito) · Letreiro "O que foi isso?"'),
('Primeiro de maio de dois mil e vinte e um.','Milla e a polêmica','Avenida Paulista genérica · Letreiro neutro, sem bandeiras nem rostos de políticos'),
('Fevereiro de dois mil e vinte e cinco. A agenda','A dor nas costas','Fantasias de Carnaval penduradas · Letreiro "6 shows cancelados"'),
('Março de dois mil e vinte e cinco.','O diagnóstico','Letreiro "LINFOMA" em destaque · Comunicado em texto'),
('Vinte e quatro de setembro de dois mil e vinte e cinco.','Livre do câncer','Letreiro "livre do câncer desde 6 de junho" · Céu de Salvador'),
('Maio de dois mil e vinte e seis.','O exame dos rins','Exame de imagem genérico desfocado · Letreiro "obstrução no rim esquerdo"'),
('Poucos dias depois, ele recebeu alta','O sonho 1966','Letreiro grande "1966" · Palco com luzes apagadas'),
('Doze de julho de dois mil e vinte e seis.','60 anos','Bolo com vela apagada (ilustrativo) · Frases do post em letreiro'),
('Trinta e um de julho de dois mil e vinte e seis.','A queda no banheiro','Toalha dobrada sobre mármore (ilustrativo) · Post em letreiro: "Isso é hora, Sr. Netinho?"'),
('Trinta de setembro de dois mil e vinte e seis.','O silêncio','Celular com a tela apagada · Letreiro com o comunicado'),
('Treze de outubro de dois mil e vinte e seis. Uma terça-feira de manhã.','A despedida','Amanhecer em Salvador · Nota em letreiro · Silêncio de 2 segundos'),
('Mas os fãs e os amigos não ficaram em silêncio.','As homenagens','Frases dos artistas em letreiro (sem prints reais)'),
('Agora pensa por um instante','O que ele deixou','Montagem de arquivo da carreira (com crédito) · Milla ao fundo, curta'),
]
cum=[];w=0
for p in paras:
    cum.append(w); w+=len(p.split())
out=[];last=-1
for key,name,img in CH:
    i=next(k for k,p in enumerate(paras) if k>last and p.startswith(key))
    last=i
    s=0 if not out else round(cum[i]/WPM*60)
    out.append((f'{s//60}:{s%60:02d}',name,img))
CHAPS='\n'.join(f'{t} {n}' for t,n,_ in out)
open('chapters.txt','w').write(CHAPS+'\n')
DESC='''Netinho fez o Brasil inteiro cantar "Milla". Mas, por trás do sorriso do rei do axé, existiu uma luta de 13 anos que começou com uma dor na coxa durante um ensaio em Salvador, em abril de 2013. Neste documentário em homenagem a ele: a confissão corajosa sobre os anabolizantes, os três AVCs e a perda da fala, a "foto da vitória", a volta emocionada no Teatro Castro Alves, o linfoma de 2025, o exame dos rins que revelou a volta do câncer em 2026, o sonho do show "1966" e a despedida em 13 de outubro de 2026.

Todas as falas de Netinho citadas no vídeo foram publicadas por ele em entrevistas e nas redes sociais, ou reproduzidas pela imprensa. Este vídeo é uma homenagem à vida e à carreira dele.

Deixe nos comentários onde você estava a primeira vez que ouviu "Milla".

{CHAPS}

#Netinho #Milla #AxéMusic'''.replace('{CHAPS}',CHAPS)
TAGS='netinho, netinho morreu, morte de netinho, netinho milla, netinho cantor, netinho axé, netinho linfoma, netinho câncer, netinho 1966, netinho banda beijo, cantor netinho história, rei do axé, milla netinho, netinho anabolizantes, netinho salvador'
assert len(TAGS)<=500, len(TAGS)
open('desc.txt','w').write(DESC+'\n'); open('tags.txt','w').write(TAGS+'\n')
rows=''.join(f'<tr><td class="t">{t}</td><td><b>{html.escape(n)}</b><br>{html.escape(i)}</td></tr>\n' for t,n,i in out)
CAUT='''<li>Tom de homenagem do começo ao fim. Nada de trilha de terror ou efeitos sensacionalistas; música dramática, mas respeitosa.</li>
<li>Morte recente: não usar imagens de caixão, velório ou família (a despedida foi reservada, a pedido dele).</li>
<li>Não mostrar a foto dele entubado nem imagens dele doente no hospital. Usar letreiros com as frases.</li>
<li>Anabolizantes: sempre como confissão dele, com as palavras dele. Não nomear nem sugerir o médico.</li>
<li>Política (2021–2022): imagens neutras, sem bandeiras, sem rostos de políticos e sem a deputada.</li>
<li>Posts e mensagens dele: recriar em letreiro, não usar prints reais com nome de usuário de terceiros.</li>
<li>Rostos reais: só fotos de imprensa ou arquivo com crédito; nunca rosto gerado por IA. Trechos de Milla e de TV curtos e com crédito.</li>
<li>Homenagens de artistas: frases em letreiro com o nome; sem prints.</li>'''
json.dump({'title':TITLE,'desc':DESC,'tags':TAGS,'chaps':CHAPS,'rows':rows,'caut':CAUT,'paras':paras,'words':W},open('pack.json','w'),ensure_ascii=False)
print(CHAPS); print('palavras',W,'min',round(W/WPM,1),'tags',len(TAGS))
