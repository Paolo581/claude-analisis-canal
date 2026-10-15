import re, html, json
TITLE="EDUARDO COSTA: O Acidente HORRÍVEL Que Destruiu o Seu Rosto"
WPM=135
raw=[]
for n in range(1,11):
    for p in open(f'bloco{n}.txt').read().split('\n\n'):
        if p.strip(): raw.append(p.strip())
paras=[re.sub(r'^[RA]: ','',p) for p in raw]
open('roteiro_completo.txt','w').write('\n\n'.join(raw)+'\n')
open('voz.txt','w').write('\n\n'.join(paras)+'\n')
W=sum(len(p.split()) for p in paras)
CH=[('Sexta-feira, sete de outubro de dois mil e onze.','O pouso','Jatinho pequeno no céu do fim de tarde (banco de imagens) · Serras de Minas'),
('Ele estava a caminho de Simonésia','O cinto','Cinto de segurança de avião solto (ilustrativo) · Cabine em penumbra'),
('Naquela noite, as notícias falaram','O show daquela noite','Palco de interior à noite (ilustrativo)'),
('Zona rural de Abre Campo','A roça','Paisagem rural de Minas · Estrada de terra'),
('Um dia, os pais decidiram','O pai foi embora','Porta de casa simples entreaberta (ilustrativo)'),
('Ele tinha nove anos quando foi para a rua','O menino do picolé','Carrinho/caixa de picolé numa rua de BH (ilustrativo, sem rosto)'),
('No meio de toda essa dor','A voz','Folia de Reis (arquivo genérico) · Viola'),
('Enquanto o sonho não pagava as contas','A estrada','Bar de interior à noite · Rodoviária vazia'),
('O sucesso de verdade só chegou','Me Apaixonei','Capa do disco (com crédito) · Trecho curto de show'),
('Volta comigo para aquela sexta-feira','Manhuaçu','Mapa da Zona da Mata · Pista pequena entre serras'),
('O piloto deu a versão dele','A versão do piloto','Letreiro "falha no reverso?" · Turbina de jato (banco). Não nomear o piloto'),
('Enquanto isso, Eduardo seguia a vida','O rosto que mudou','Comparativo de fotos públicas por ano (com crédito)'),
('Enquanto o rosto mudava','Cabaré','Trechos curtos do DVD Cabaré (com crédito)'),
('Março de dois mil e vinte e um.','A noite em que ele contou','Trecho curto do The Noite (com crédito) · Letreiro "nunca contei"'),
('Os ossos precisavam de tratamento','O maxilar afundado','Ilustração de crânio com fratura no maxilar (genérica)'),
('A investigação ficou a cargo do Cenipa','A investigação','Logo/fachada genérica de investigação aeronáutica · Letreiro "freios usados tarde"'),
('Cinco pessoas estavam naquele avião.','Só um se machucou','Letreiro "5 a bordo · 1 ferido"'),
('Anos depois, falando sobre aquela tarde','"Era para ter sido fatal"','Letreiro com a frase · Fundo escuro'),
('Anabolizantes.','A bomba','Frascos e seringas genéricos no escuro (sem marcas)'),
('O nome dela é trembolona.','Lixo espiritual','Letreiro "lixo espiritual" · Espelho embaçado'),
('O corpo também cobrou.','O preço no corpo','Fotos públicas de 2025 (com crédito)'),
('Abril de dois mil e vinte e três.','O casamento','Fotos públicas do casamento (com crédito)'),
('Sábado, oito de abril','As duas mães','Mãos dadas em silhueta (ilustrativo) · Fazenda ao entardecer'),
('Maio de dois mil e vinte e três.','O homem no portão','Portão de casa simples · Caixa de correio com cartas (ilustrativo)'),
('Julho de dois mil e vinte e três.','Edson Wander','Foto de imprensa de Edson Wander (com crédito) · Letreiro "sem DNA"'),
('Dois anos antes, em dois mil e vinte e um','A mulher que dizia ser sua mãe','Letreiro com a frase narrada · Envelope de exame lacrado'),
('Agora volta para aquela pista em Manhuaçu.','A mesma origem','Montagem lenta: pista, picolé, palco'),
('Quase todo mundo conhece alguém assim.','Quem nunca para','Mãos calejadas segurando uma xícara (ilustrativo)'),
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
DESC='''Em 7 de outubro de 2011, o jatinho que levava Eduardo Costa para um show em Simonésia (MG) não parou na pista de Manhuaçu e terminou no meio de um cafezal. Das cinco pessoas a bordo, só ele se feriu. Os jornais falaram em susto. Dez anos depois, ele contou o que realmente quebrou, e a investigação apontou que a culpa não foi da máquina. Neste documentário: o cinto solto nos últimos segundos, o show feito com o rosto quebrado, o maxilar que afundou, os anabolizantes que ele chama de "lixo espiritual", o menino que vendia picolé aos nove anos e as duas mães no dia do casamento.

As informações vêm de entrevistas do próprio cantor (The Noite, Domingo Espetacular, canal André Piunti, Band) e de reportagens. A conclusão da investigação (Cenipa) foi obtida em bases públicas de acidentes aéreos; o piloto deu outra versão na época. As alegações de paternidade de terceiros nunca foram comprovadas; a mãe do cantor as nega.

{CHAPS}

#EduardoCosta #Sertanejo #Documentário'''.replace('{CHAPS}',CHAPS)
TAGS='eduardo costa, eduardo costa acidente, eduardo costa avião, eduardo costa rosto, eduardo costa antes e depois, eduardo costa anabolizantes, eduardo costa mãe, eduardo costa infância, eduardo costa história, eduardo costa leonardo cabaré, eduardo costa careca, eduardo costa 2026, acidente aéreo manhuaçu'
assert len(TAGS)<=500
open('desc.txt','w').write(DESC+'\n'); open('tags.txt','w').write(TAGS+'\n')
rows=''.join(f'<tr><td class="t">{t}</td><td><b>{html.escape(n)}</b><br>{html.escape(i)}</td></tr>\n' for t,n,i in out)
CAUT='''<li>Piloto: nunca nomear nem mostrar foto. Usar sempre "segundo a investigação" e citar a versão dele (pane no reverso).</li>
<li>Acidente: não encenar feridos nem sangue. Fraturas só em ilustração genérica.</li>
<li>Mãe e Ângela: tom de respeito; nunca insinuar dúvida sobre a paternidade. Os homens são "diziam ser o pai"; a negativa da mãe aparece completa.</li>
<li>Homem das cartas e Maria de Lourdes Soares: sem fotos; Maria de Lourdes só pelo nome que ela mesma deu à imprensa.</li>
<li>Anabolizantes: sem marcas de produtos; sem glamourizar.</li>
<li>Rostos reais: só fotos de imprensa ou publicações com crédito; nunca rosto gerado por IA. Trechos de TV curtos e com crédito.</li>'''
json.dump({'title':TITLE,'desc':DESC,'tags':TAGS,'chaps':CHAPS,'rows':rows,'caut':CAUT,'paras':paras,'words':W},open('pack.json','w'),ensure_ascii=False)
print(CHAPS); print(W, round(W/WPM,1), len(TAGS))
