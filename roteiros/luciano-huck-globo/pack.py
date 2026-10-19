import re, html, json
TITLE="LUCIANO HUCK: A Investigação HORRÍVEL Que a Própria Globo Abriu Contra Ele"
WPM=135
raw=[]
for n in range(1,10):
    for p in open(f'bloco{n}.txt').read().split('\n\n'):
        if p.strip(): raw.append(p.strip())
paras=[re.sub(r'^[RA]: ','',p) for p in raw]
open('roteiro_completo.txt','w').write('\n\n'.join(raw)+'\n')
open('voz.txt','w').write('\n\n'.join(paras)+'\n')
W=sum(len(p.split()) for p in paras)
CH=[('Oitenta e três milhões','Os dois números','Letreiros "R$ 83 milhões" e "R$ 26 milhões" · Celular sobre a mesa (ilustrativo)'),
('Mas, antes de abrir aquele celular','O rapaz de família rica','São Paulo anos 1970-80 (arquivo)'),
('Estava na noite de São Paulo.','A casa noturna','Noite de São Paulo anos 1990 (arquivo/ilustrativo)'),
('Em mil novecentos e noventa e três','Jornal, rádio e Band','Redação de jornal antiga · Estúdio de rádio (ilustrativo)'),
('O convite veio da Globo.','O Caldeirão','Fachada da Globo (arquivo)'),
('Imagine um sábado à tarde.','Lar Doce Lar','Casa simples reformada (ilustrativo) · Venda nos olhos'),
('O rosto de Luciano Huck estava ficando valioso.','O rosto que vale milhões','Comerciais genéricos de TV (ilustrativo)'),
('O sonho tinha nome.','O sonho da Presidência','Planalto (arquivo)'),
('Faustão.','Os domingos do Faustão','Foto de imprensa com crédito'),
('O nome dele era Daniel Vorcaro.','Daniel Vorcaro','Foto pública de Vorcaro com crédito · Belo Horizonte'),
('Banco Master.','Banco Master','Avenida Faria Lima (arquivo)'),
('Quando você guarda dinheiro num banco','Juros bons demais','Animação simples: dois bancos e um aposentado'),
('No Brasil existe um tipo de seguro','O Fundo Garantidor','Letreiro "até R$ 250 mil por pessoa"'),
('Domingo, cinco de novembro','O primeiro abraço','Celular com mensagem genérica (ilustrativo)'),
('Um avião.','O avião','Jato executivo genérico (ilustrativo)'),
('Maio de dois mil e vinte e quatro.','As enchentes','Imagens públicas das enchentes no RS (com crédito)'),
('Era sobre dinheiro.','O Will Bank','App de banco genérico no celular (ilustrativo)'),
('O primeiro número era da Globo.','R$ 83 milhões','Letreiro "R$ 83 milhões"'),
('Vinte e seis milhões de reais.','Contrato pessoal','Letreiro "R$ 26 milhões" · "1.500 anos de salário mínimo"'),
('Outubro de dois mil e vinte e cinco.','Os dois números lado a lado','Letreiro "R$ 109 milhões"'),
('E é aqui que precisa ficar claro','O outro lado','Letreiro "não é investigado"'),
('Ao longo de dois mil e vinte e quatro, o Banco Master','Os conselhos','Tela de celular desfocada (ilustrativo)'),
('Dois mil e vinte e cinco foi o ano','A crise de 2025','Manchetes BRB/Banco Central (arquivo)'),
('Segunda-feira, dezessete de novembro','A última noite','Relógio marcando 21h47 · Jornal Nacional (arquivo licenciado)'),
('Porque, naquela mesma noite','A prisão no aeroporto','Aeroporto à noite (arquivo)'),
('Terça-feira, vinte e nove de setembro','A investigação em segredo','Corredor de escritório à noite (ilustrativo) · Logotipo da Globo'),
('Frederic Kachar era','O primeiro a cair','Letreiro "demitido"'),
('Sexta-feira, dezesseis de outubro.','R$ 160 milhões ao vivo','Estúdio de sabatina (arquivo licenciado)'),
('Quando as mensagens vieram a público','A versão de Huck','Letreiro com a defesa de Huck'),
('Volte comigo um pouco no tempo.','O que fica','Recapitulação das imagens-chave · Sofá diante da TV'),
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
DESC='''Oitenta e três milhões de reais para a Globo e mais vinte e seis milhões que ele chamou de contrato pessoal: os números estavam numa mensagem de Luciano Huck para o banqueiro Daniel Vorcaro, preso um mês depois. Agora, segundo os bastidores, a própria Globo abriu uma auditoria interna sobre essa relação.

Neste documentário: quem eram os dois antes de se conhecerem; o abraço de 2023; o avião; o patrocínio do Will Bank; os conselhos de imagem; a última mensagem na noite da prisão; o diretor demitido; os "R$ 160 milhões" ditos ao vivo; e a versão completa de Luciano Huck.

Luciano Huck não é investigado no caso Banco Master e nega ter sido sócio de Vorcaro; segundo ele, a relação se limitava ao patrocínio, com contrato, notas e impostos. Valores citados por terceiros sem confirmação estão indicados como tal. Fontes: Veja, Folha, Diário de Pernambuco, Times Brasil, TV Prime, A Tarde, O Antagonista, Bloomberg Línea, InfoMoney. Caso em andamento: a situação pode ter mudado após a gravação.

{CHAPS}

#LucianoHuck #BancoMaster #Vorcaro'''.replace('{CHAPS}',CHAPS)
TAGS='luciano huck, luciano huck vorcaro, caso master, banco master, daniel vorcaro, luciano huck globo, auditoria globo, will bank, domingão com huck, luciano huck polêmica, luciano huck mensagens, luciano huck notícia, vorcaro preso, luciano huck documentário'
assert len(TAGS)<=500
open('desc.txt','w').write(DESC+'\n'); open('tags.txt','w').write(TAGS+'\n')
rows=''.join(f'<tr><td class="t">{t}</td><td><b>{html.escape(n)}</b><br>{html.escape(i)}</td></tr>\n' for t,n,i in out)
CAUT='''<li>Pessoa viva, caso em andamento: nunca escrever em letreiros que Huck cometeu crime; ele não é investigado.</li>
<li>Auditoria e afastamento: sempre "segundo bastidores/colunista"; a Globo não confirmou.</li>
<li>R$ 160 milhões: sempre com "sem confirmação".</li>
<li>Kachar e as festas: atribuir às reportagens.</li>
<li>Ano eleitoral: sem tomar partido; Flávio Bolsonaro aparece só como quem disse o número.</li>
<li>Antes de publicar: conferir resultado da auditoria, eventual afastamento e novas decisões.</li>
<li>Rostos reais: só fotos de arquivo/imprensa com crédito; nunca rosto gerado por IA.</li>'''
json.dump({'title':TITLE,'desc':DESC,'tags':TAGS,'chaps':CHAPS,'rows':rows,'caut':CAUT,'paras':paras,'words':W},open('pack.json','w'),ensure_ascii=False)
print(CHAPS); print(W, round(W/WPM,1), len(TAGS))
