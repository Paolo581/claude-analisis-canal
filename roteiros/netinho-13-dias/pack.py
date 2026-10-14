import re, html, json
TITLE="OS ÚLTIMOS 13 DIAS DE NETINHO: O Que Ninguém Teve Coragem de Contar"
WPM=135
raw=[]
for n in range(1,9):
    for p in open(f'bloco{n}.txt').read().split('\n\n'):
        if p.strip(): raw.append(p.strip())
paras=[re.sub(r'^[RA]: ','',p) for p in raw]
open('roteiro_completo.txt','w').write('\n\n'.join(raw)+'\n')
open('voz.txt','w').write('\n\n'.join(paras)+'\n')
W=sum(len(p.split()) for p in paras)
CH=[('Trinta de setembro de dois mil e vinte e seis. O homem','O silêncio de setembro','Celular com a tela apagada · Letreiro "30/09/2026"'),
('Mil novecentos e sessenta e seis. Santo Antônio','Ernesto, 1966','Imagens de Santo Antônio de Jesus · Letreiro "1966"'),
('Anos oitenta.','O sorriso em cima do trio','Arquivo do Carnaval de Salvador (com crédito) · Trio e multidão'),
('Mil novecentos e noventa e seis. Aracaju','Milla','Capa do disco Netinho ao Vivo (com crédito) · Letreiro "3 milhões" · Trecho curto de Milla'),
('Dois mil e três.','A pausa pela filha','Letreiro "2003" · Fotos de imprensa (com crédito)'),
('Abril de dois mil e treze. Salvador.','O banco','Banco vazio num palco · Letreiro com a frase dele'),
('Sábado, vinte e cinco de maio de dois mil e treze.','O boletim com o nome Ernesto','Boletim recriado em letreiro, frase exata'),
('Quarta-feira, vinte e nove de maio.','A visita da Ivete','Corredor de hospital à tarde (genérico) · Letreiro "29/05/2013"'),
('Segunda-feira, treze de maio de dois mil e treze.','O segredo','Manchete recriada do Jornal do Brasil (sem logo)'),
('Sexta-feira, trinta e um de janeiro de dois mil e catorze.','A confissão no Faustão','Trecho curto do Faustão (com crédito) · Letreiros com as frases'),
('Sábado, oito de fevereiro de dois mil e catorze.','A foto da vitória','NÃO mostrar a foto entubado: letreiro "a foto da vitória" e "Nada Como Viver!"'),
('Sexta-feira, catorze de agosto de dois mil e quinze.','A volta no Castro Alves','Fachada do Teatro Castro Alves · Trecho do Palco Viva (com crédito)'),
('Roberto Kalil Filho, o cardiologista','O que o médico revelou','Letreiro com a descrição do quadro de 2013'),
('Segunda-feira, trinta de novembro de dois mil e quinze.','Está tudo certo','Letreiro "Está tudo certo" · Janela de hospital à noite'),
('Abril de dois mil e dezoito.','O trio de 2018','Arquivo da Micareta (com crédito)'),
('Fevereiro de dois mil e vinte e cinco.','A dor de 2025','Fantasias de Carnaval penduradas · Letreiro "6 shows cancelados"'),
('Dois dias depois, no domingo, vinte e três de março','Linfoma','Letreiro "LINFOMA" · Comunicado recriado'),
('Sexta-feira, nove de maio de dois mil e vinte e cinco.','A planta e a voz','Vaso com planta junto à janela de hospital (ilustrativo)'),
('Vinte e quatro de setembro de dois mil e vinte e cinco.','Livre do câncer','Letreiro "livre do câncer desde 6 de junho"'),
('Maio de dois mil e vinte e seis.','O exame dos rins','Exame de imagem desfocado (genérico) · Letreiro "obstrução no rim esquerdo"'),
('Domingo, doze de julho de dois mil e vinte e seis.','60 anos e o show 1966','Folha de papel com "1966" (ilustrativo) · Bolo com vela apagada'),
('Sexta-feira, trinta e um de julho de dois mil e vinte e seis.','A toalha','Toalha dobrada sobre mármore molhado (ilustrativo) · Post recriado em letreiro'),
('Dia um.','Os 13 dias','Contador "Dia 1 … Dia 13" · Celular sem notificações'),
('Dia treze.','A nota','Amanhecer em Salvador · Nota em letreiro · 2 segundos de silêncio'),
('Lembra da Bruna?','A despedida','Letreiro "Te amo para sempre" (sem reproduzir fotos da família)'),
('A fama cobra um preço','Está tudo certo?','Montagem de arquivo da carreira (com crédito) · Milla ao fundo, curta'),
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
DESC='''Em 30 de setembro de 2026, o homem que mostrava cada sessão de quimioterapia aos fãs sumiu das redes. Treze dias depois, Netinho, a voz de "Milla", morreu em Salvador, aos 60 anos. Neste documentário em homenagem a ele: o banco de onde ele não conseguiu levantar em 2013, o boletim médico com o nome Ernesto, a visita de Ivete Sangalo horas antes do segundo AVC, a confissão no Faustão, a "foto da vitória", a volta chorando no Castro Alves, o linfoma de 2025, o exame dos rins que encontrou o câncer de volta, o sonho do show "1966" e o que estava escrito na nota final.

Todas as falas citadas foram publicadas por Netinho em entrevistas e redes sociais, ou reproduzidas pela imprensa (Correio Braziliense, Jornal do Brasil, G1, Bahia Notícias, O Tempo e outros). Este vídeo é uma homenagem à vida e à carreira dele.

{CHAPS}

#Netinho #Milla #AxéMusic'''.replace('{CHAPS}',CHAPS)
TAGS='netinho, netinho morreu, últimos dias de netinho, morte de netinho, netinho milla, netinho cantor, netinho linfoma, netinho câncer, netinho 1966, netinho ivete sangalo, netinho anabolizantes, rei do axé, netinho filha bruna, netinho história, netinho salvador'
assert len(TAGS)<=500
open('desc.txt','w').write(DESC+'\n'); open('tags.txt','w').write(TAGS+'\n')
rows=''.join(f'<tr><td class="t">{t}</td><td><b>{html.escape(n)}</b><br>{html.escape(i)}</td></tr>\n' for t,n,i in out)
CAUT='''<li>Tom de homenagem do começo ao fim. Trilha dramática, mas respeitosa.</li>
<li>Morte recente: sem caixão, velório ou família (a despedida foi reservada, a pedido dele). Não reproduzir as fotos pessoais da filha.</li>
<li>Não mostrar a foto dele entubado nem imagens dele doente. Usar letreiros.</li>
<li>Anabolizantes: sempre como confissão dele. Não nomear nem sugerir o endocrinologista.</li>
<li>Posts e mensagens: recriar em letreiro, sem prints com dados de terceiros.</li>
<li>Rostos reais: só fotos de imprensa ou arquivo com crédito; nunca rosto gerado por IA.</li>'''
json.dump({'title':TITLE,'desc':DESC,'tags':TAGS,'chaps':CHAPS,'rows':rows,'caut':CAUT,'paras':paras,'words':W},open('pack.json','w'),ensure_ascii=False)
print(CHAPS); print(W, round(W/WPM,1), len(TAGS))
