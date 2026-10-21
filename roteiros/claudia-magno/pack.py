import re, html, json
TITLE="CLÁUDIA MAGNO: A Suspeita HORRÍVEL Que a Família Negou Até o Fim — O Que Matou a Silvana de Tieta"
WPM=135
raw=[]
for n in range(1,9):
    for p in open(f'bloco{n}.txt').read().split('\n\n'):
        if p.strip(): raw.append(p.strip())
paras=[re.sub(r'^[RA]: ','',p) for p in raw]
open('roteiro_completo.txt','w').write('\n\n'.join(raw)+'\n')
open('voz.txt','w').write('\n\n'.join(paras)+'\n')
W=sum(len(p.split()) for p in paras)
CH=[('Janeiro de mil novecentos e noventa e quatro.','A morte da Silvana de Tieta','Foto de arquivo de Cláudia em Tieta (com crédito) · Clínica em tom frio (ilustrativo)'),
('Mas, antes de chegar àquela clínica','A bailarina','Sapatilhas de balé · Nova York anos 70 (arquivo)'),
('Cláudia entrou para a linha de shows','Linha de shows da Globo','Bailarinas de TV anos 70/80 (arquivo, com crédito)'),
('O filme se chamava Menino do Rio.','Menino do Rio','Cartaz/cenas do filme (com crédito) · Praia carioca'),
('Só que o romance de Patrícia e Valente','André De Biase','Fotos de imprensa da época (com crédito) · Jipe na praia'),
('A partir de Menino do Rio','A Menina do Rio','Praia de Ipanema anos 80 (arquivo)'),
('A música se chamava Bete Balanço.','Bete Balanço e os clipes','Trechos curtos dos clipes (licenciados/crédito)'),
('Em mil novecentos e oitenta e quatro, a TV Manchete','Manchete e teatro','Logo da TV Manchete (crédito) · Palco de teatro'),
('E, em mil novecentos e oitenta e seis, ganhou um papel','Roda de Fogo','Foto de Roda de Fogo (com crédito)'),
('O nome dele era Marcelo Ibrahim.','Marcelo Ibrahim','Foto de arquivo de Marcelo Ibrahim (com crédito)'),
('No dia dois de julho de mil novecentos e oitenta e seis','A morte de Marcelo','Fachada genérica de clínica (ilustrativo) · Letreiro "Clínica São Vicente"'),
('Em mil novecentos e oitenta e oito, entrou em Fera Radical','Presença de Marisa e o prêmio','Troféu (ilustrativo) · Foto do filme (com crédito)'),
('A novela se chamava Tieta.','Tieta','Abertura/fotos de Tieta (com crédito)'),
('Na trama, Silvana se envolvia','Silvana, Dário e Laura','Fotos de Tieta com Flávio Galvão e Cláudia Alencar (com crédito)'),
('Depois de Tieta, Cláudia não parou.','Depois de Tieta','Fotos de imprensa (com crédito)'),
('O programa era o Você Decide','O Direito de Morrer','Telefone antigo (ilustrativo) · Letreiro com o título'),
('Foi em setembro de mil novecentos e noventa e três.','O cansaço','Mulher de costas olhando a janela (ilustrativo, sem rosto)'),
('No dia sete de dezembro','A internação','Corredor de hospital (ilustrativo)'),
('Cláudia Magno morreu às seis e meia','5 de janeiro de 1994','Letreiro com data e causa oficial'),
('No dia seguinte, o jornal O Globo','Menina do Rio na manchete','Recorte de jornal (com crédito, sem montagem)'),
('A frase saiu na Folha de São Paulo','A frase da clínica','Letreiro com a frase · Máquina de escrever (ilustrativo)'),
('No dia treze de janeiro','A manchete e o exame','Recorte da Folha (com crédito) · Envelope de exame lacrado (ilustrativo)'),
('O nome dele é Ricardo Magno.','A denúncia do irmão','Letreiro com a fala narrada · Estetoscópio (ilustrativo)'),
('Na época, a especulação ligou','O laudo de Marcelo','Documento genérico com carimbo "NEGATIVO" (ilustrativo)'),
('Era quarta-feira, cinco de janeiro','Gravando na hora do enterro','Claquete (ilustrativo) · Cemitério ao longe'),
('A sinopse original tinha um plano','Josefina desaparece','Cadeira vazia num set (ilustrativo)'),
('No fim de dois mil e vinte e quatro','A volta de Tieta','Foto de Silvana em Tieta (com crédito)'),
('E a história de Cláudia deixa duas lições','O que fica','Praia ao pôr do sol (ilustrativo)'),
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
DESC='''Em 5 de janeiro de 1994, Cláudia Magno, a Silvana de "Tieta" e a eterna "Menina do Rio", morreu aos 35 anos na Clínica São Vicente, no Rio. Os médicos tinham uma suspeita, a família recusou o exame e o irmão fez uma denúncia no dia do enterro.

Neste documentário, a história completa: a bailarina que estudou em Nova York e dançou na linha de shows da Globo; "Menino do Rio" e o namoro com André De Biase; os clipes de "Bete Balanço" e "Meu Erro"; o prêmio de melhor atriz em Brasília; Silvana Pitombo e o triângulo com Dário e Laura em "Tieta"; a morte de Marcelo Ibrahim na mesma clínica, sete anos antes; o cansaço que os exames não explicavam; a manchete da Folha e o laudo que desmonta a especulação. Uma homenagem que separa o que se sabe do que nunca foi confirmado.

Informações de Folha de S.Paulo (06, 09 e 13/01/1994), O Globo/Extra, Cinemateca Brasileira, Teledramaturgia, NaTelinha, Metrópoles e Correio Braziliense. A causa oficial da morte foi insuficiência respiratória aguda por infecção respiratória e choque séptico; a suspeita de HIV nunca foi confirmada.

{CHAPS}

#ClaudiaMagno #Tieta #MeninoDoRio'''.replace('{CHAPS}',CHAPS)
TAGS='claudia magno, claudia magno morte, silvana tieta, tieta novela, atriz de tieta morreu, menino do rio, menina do rio, andré de biase, marcelo ibrahim, clínica são vicente, sonho meu novela, geração saúde, atrizes dos anos 80, vale a pena ver de novo tieta, o que aconteceu com claudia magno'
assert len(TAGS)<=500
open('desc.txt','w').write(DESC+'\n'); open('tags.txt','w').write(TAGS+'\n')
rows=''.join(f'<tr><td class="t">{t}</td><td><b>{html.escape(n)}</b><br>{html.escape(i)}</td></tr>\n' for t,n,i in out)
CAUT='''<li>Nunca afirmar em letreiro, thumbnail ou capítulo que ela morreu de Aids: sempre "suspeita nunca confirmada".</li>
<li>Marcelo Ibrahim: mostrar que o laudo deu negativo; não sugerir ligação entre as mortes.</li>
<li>Recortes de jornal (Folha, O Globo): reais, com crédito, sem montagem nem manchete inventada.</li>
<li>Trechos de Menino do Rio, Tieta, clipes e músicas: curtos, licenciados ou com crédito.</li>
<li>Rostos reais: só fotos de arquivo/imprensa com crédito; nunca rosto gerado por IA.</li>
<li>Cidade natal (Itaperuna ou Rio) tem conflito: não colocar em letreiro.</li>
<li>Namoro com Lúcia Veríssimo e pedido de ajuda à Globo são rumores: não usar.</li>'''
json.dump({'title':TITLE,'desc':DESC,'tags':TAGS,'chaps':CHAPS,'rows':rows,'caut':CAUT,'paras':paras,'words':W},open('pack.json','w'),ensure_ascii=False)
print(CHAPS); print(W, round(W/WPM,1), len(TAGS))
