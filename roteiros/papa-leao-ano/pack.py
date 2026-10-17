import re, html, json
TITLE="PAPA LEÃO XIV: A Verdade HORRÍVEL Sobre o Câncer Que Cresceu em Silêncio"
WPM=135
raw=[]
for n in range(1,9):
    for p in open(f'bloco{n}.txt').read().split('\n\n'):
        if p.strip(): raw.append(p.strip())
paras=[re.sub(r'^[RA]: ','',p) for p in raw]
open('roteiro_completo.txt','w').write('\n\n'.join(raw)+'\n')
open('voz.txt','w').write('\n\n'.join(paras)+'\n')
W=sum(len(p.split()) for p in paras)
CH=[('Ele entrou no hospital andando','A porta do hospital','Fachada do Gemelli (arquivo licenciado) · Papa acenando (foto de agência com crédito)'),
('Mas, antes de chegar àquela porta','A casa de Dolton','Subúrbio de Chicago anos 1960 (arquivo) · Terço sobre a mesa de jantar'),
('Pegava a tábua de passar roupa','O altar de brincadeira','Tábua de passar com lençol branco · Copo de plástico · Balinhas (ilustrativo)'),
('E teve um dia, na frente de casa','A profecia da vizinha','Rua de bairro americano anos 1960 (ilustrativo)'),
('Com uns seis anos, Robert virou coroinha','O coroinha das seis e meia','Igreja ao amanhecer · Missal em latim'),
('Ele saiu de casa.','O seminário','Seminário agostiniano (arquivo) · Letreiro "60 meninos, 5 padres"'),
('Quando saiu do seminário','Matemática e Roma','Villanova (arquivo) · Ordenação em Roma (foto de imprensa)'),
('Mil novecentos e oitenta e cinco.','Chulucanas','Norte do Peru (arquivo)'),
('Uma bomba explodiu','A bomba na porta da igreja','Porta de igreja danificada (ilustrativo)'),
('Em mil novecentos e oitenta e oito','Padre Roberto','Trujillo, periferia (arquivo)'),
('Junho de mil novecentos e noventa.','As perdas','Vela acesa · Fotos antigas de família'),
('Em mil novecentos e noventa e nove','Superior geral','Agostinianos pelo mundo (arquivo)'),
('Novembro de dois mil e catorze.','Bispo de Chiclayo','Catedral de Chiclayo (arquivo)'),
('Dois mil e vinte. A pandemia','O bispo do oxigênio','Cilindros de oxigênio · Filas no Peru 2020 (arquivo)'),
('Março de dois mil e vinte e três.','A enchente','Fotos de Prevost na enchente (Cáritas Chiclayo, com crédito) · Botas de borracha'),
('Vinte e um de abril','O conclave','Capela Sistina (arquivo)'),
('Oito de maio de dois mil e vinte e cinco.','A fumaça branca','Chaminé · Praça em festa (arquivo)'),
('Em Illinois, o irmão John','A frase se cumpriu','TV antiga com a sacada (ilustrativo)'),
('Nada indicava que Leão XIV','O exame de rotina','Tomografia de pulmão genérica (ilustrativo) · Letreiro "exame de rotina"'),
('Domingo, onze de outubro.','O anúncio','Janela do Angelus (arquivo licenciado)'),
('Dois dias depois, terça-feira','Não tenham medo','Estátua de João Paulo II no Gemelli (arquivo licenciado)'),
('Os médicos não abriram o peito','A cirurgia','Ilustração médica: pulmão com três lobos · cirurgia por vídeo (ilustrativo)'),
('Era a palavra que todo mundo tem medo de ouvir.','A palavra','Tela preta · Letreiro "Câncer"'),
('O tipo que encontraram no Papa','O câncer silencioso','Ilustração do pulmão · Letreiro com os sinais de alerta'),
('O nódulo de Leão XIV foi encontrado cedo.','Descoberto cedo','Gráfico simples: tarde x cedo'),
('Até agora, o Vaticano não revelou','A pergunta sem resposta','Letreiro "estágio: não revelado"'),
('Quarta-feira, catorze de outubro.','As velas','Velas e santinhos na estátua (arquivo licenciado)'),
('Ele não gravou vídeo','A carta','Papel de carta sobre mesa (ilustrativo)'),
('Nos dias seguintes','A recuperação','Corredor de hospital · Primeiras fotos da missa (Vatican Media, com crédito)'),
('Seis de novembro.','A volta ao Peru','Mapa da América do Sul · Avião papal (arquivo)'),
('O câncer que mais mata no mundo é aquele','O que ele ensinou','Recapitulação das imagens-chave · Estátua ao entardecer'),
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
DESC='''Ele entrou no hospital andando e acenou para quem esperava na porta. Horas depois, com o Papa ainda anestesiado, o laboratório mandou a resposta: câncer de pulmão, o câncer que mais mata no mundo e que quase sempre cresce em silêncio.

Neste documentário: o menino de Dolton que montava um altar com a tábua de passar roupa; o padre que ficou no Peru quando uma bomba destruiu a porta da igreja; o bispo que pediu oxigênio para os doentes na pandemia; o exame de rotina que encontrou a mancha no pulmão; a cirurgia no Hospital Gemelli; a carta que ele escreveu do quarto do hospital; e o que ainda falta saber.

As informações vêm de comunicados do Vaticano e de reportagens (Vatican News, AP/PBS, CNN, CBS, NBC, Catholic World Report, OSV News). Dados de sobrevivência: Sociedade Americana do Câncer e OMS. Este vídeo não substitui orientação médica. A situação de saúde do Papa pode ter mudado depois da gravação.

{CHAPS}

#PapaLeãoXIV #CâncerDePulmão #Vaticano'''.replace('{CHAPS}',CHAPS)
TAGS='papa leão xiv, papa leão xiv câncer, câncer de pulmão, papa leão xiv cirurgia, papa leão xiv pulmão, papa leão xiv saúde, robert prevost, adenocarcinoma de pulmão, hospital gemelli, papa leão xiv história, papa leão xiv notícia, sintomas câncer de pulmão, papa leão xiv documentário'
assert len(TAGS)<=500
open('desc.txt','w').write(DESC+'\n'); open('tags.txt','w').write(TAGS+'\n')
rows=''.join(f'<tr><td class="t">{t}</td><td><b>{html.escape(n)}</b><br>{html.escape(i)}</td></tr>\n' for t,n,i in out)
CAUT='''<li>Pessoa viva: o "horrível" do título é a notícia; nunca ligar palavras pesadas à pessoa dele.</li>
<li>Nunca dizer ou sugerir em letreiros que ele tem pouca chance de viver: os especialistas falam em chances excelentes. Os números de sobrevivência baixa são só para casos descobertos tarde.</li>
<li>Saúde: antes de publicar, conferir se ele teve alta, se saiu o resultado pendente e se a viagem de 6 de novembro foi confirmada.</li>
<li>Câncer: ilustração médica neutra; sem imagens de cirurgia real.</li>
<li>Rostos reais: só fotos de arquivo/agência com crédito; nunca rosto gerado por IA.</li>'''
json.dump({'title':TITLE,'desc':DESC,'tags':TAGS,'chaps':CHAPS,'rows':rows,'caut':CAUT,'paras':paras,'words':W},open('pack.json','w'),ensure_ascii=False)
print(CHAPS); print(W, round(W/WPM,1), len(TAGS))
