import re, html, json
TITLE="Nelson Ned: Confessou o Que Fazia Com as Mulheres… e Morreu Esquecido"
WPM=135
raw=[]
for n in range(1,10):
    for p in open(f'bloco{n}.txt').read().split('\n\n'):
        if p.strip(): raw.append(p.strip())
paras=[re.sub(r'^[RA]: ','',p) for p in raw]
open('roteiro_completo.txt','w').write('\n\n'.join(raw)+'\n')
open('voz.txt','w').write('\n\n'.join(paras)+'\n')
W=sum(len(p.split()) for p in paras)
CH=[('Ele media um metro e doze.','O Pequeno Gigante','Nelson Ned no auge, de smoking (foto pública, com crédito)'),
('Dois de março de mil novecentos e quarenta e se','Ubá, 1947','Ubá-MG antiga (arquivo)'),
('E dona Ned tomou uma decisão que ia moldar o re','A lição da mãe','Escada de madeira (ilustrativo)'),
('Mas, fora de casa, o mundo era bem menos justo d','O anãozinho da escola','Pátio de escola antiga (ilustrativo)'),
('Ainda criança, ele começou a se apresentar na ','A cadeira na rádio','Rádio antigo / microfone (ilustrativo)'),
('Mil novecentos e sessenta.','Belo Horizonte e a Lacta','Caminhão de entrega anos 60 (arquivo)'),
('Mil novecentos e sessenta e quatro.','A fita métrica','Capa do LP de 1964 (com crédito)'),
('Nelson se mudou para São Paulo.','Chacrinha e Silvio Santos','Programa de auditório anos 60 (arquivo)'),
('Mil novecentos e sessenta e oito.','Tamanho Não É Documento','Disco de vinil (ilustrativo)'),
('O nome dela era Tudo Passará.','Tudo Passará','Capa do LP Tudo Passará (com crédito)'),
('Mas havia uma parte do Brasil que olhava para Ne','O rótulo de brega','Jornais antigos (ilustrativo)'),
('Nova York, mil novecentos e setenta.','Nova York, 1970','Nova York anos 70 (arquivo)'),
('E no México aconteceu algo que até hoje parece','México e Colômbia','Cassino antigo (ilustrativo)'),
('O país era Angola.','A escada do avião','Aeroporto anos 70 (arquivo)'),
('Lá no começo deste vídeo, apareceu um nome. O','Carnegie Hall','Fachada do Carnegie Hall (foto pública)'),
('O escritor era o colombiano Gabriel García Már','García Márquez','Foto pública de García Márquez (com crédito)'),
('A forma de nanismo de Nelson Ned trazia um probl','A dor e a morfina','Frascos de remédio antigos (ilustrativo)'),
('E foi aí que surgiu um dos objetos mais assusta','O cofre','Cofre antigo (ilustrativo)'),
('Pelé.','O revólver Pelé','Silhueta de revólver (ilustrativo, sem violência)'),
('Pablo Escobar.','Pablo Escobar','Medellín anos 80 (arquivo)'),
('E havia as mulheres.','As mulheres','Taças de champanhe (ilustrativo)'),
('Os três filhos de Nelson Ned nasceram com nanis','Os filhos','Foto pública de família (com crédito)'),
('A frase foi dita por Veca, a filha de Nelson Ned','Manicômio, prisão ou caixão','Janela escura (ilustrativo)'),
('Mil novecentos e oitenta e oito. São Paulo.','A noite de 1988','Casa à noite (ilustrativo)'),
('Lá no começo deste vídeo, ficou prometida uma','A confissão','Foto pública de Nelson Ned (com crédito)'),
('Em mil novecentos e oitenta e quatro, Nelson Ned','O Globo Repórter','Imagem do Globo Repórter 1984 (arquivo, com crédito)'),
('O sertanejo.','A queda','Rádio antigo desligado (ilustrativo)'),
('Um incêndio atingiu a casa de Nelson Ned em Sã','O incêndio','Fumaça (ilustrativo)'),
('Mas Nelson Ned nunca perdeu uma coisa.','Cafetões da miséria','Microfone de entrevista (ilustrativo)'),
('Mil novecentos e setenta e seis.','A primeira conversão','Bíblia aberta (ilustrativo)'),
('Nelson Ned virou cantor gospel.','O gospel e o livro','Capa da autobiografia (com crédito)'),
('Dois mil e três.','O AVC','Cadeira de rodas (ilustrativo)'),
('Quem ficou ao lado dele foram as irmãs.','As irmãs','Chácara em Cotia (ilustrativo)'),
('A frase foi dita a um repórter do jornal Estado','Saudades de mim mesmo','Foto pública de Nelson Ned idoso (com crédito)'),
('Cinco de janeiro de dois mil e catorze.','A despedida','Velas (ilustrativo)'),
('Muitos vídeos na internet dizem que Nelson Ned m','A verdade inteira','Foto pública de Nelson Ned jovem (com crédito)'),
('Em dois mil e vinte e um, o jornalista André Bar','O filme recusado','Claquete (ilustrativo)'),
('Hoje, Nelson Ned continua mais lembrado no Méxi','O legado','Capa da biografia de 2023 (com crédito)'),
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
DESC='''Ele media 1,12 m e lotou o Carnegie Hall. Mas, longe dos palcos, Nelson Ned levava uma vida que ele mesmo chamaria de depravada: um cofre com cocaína e armas, e mulheres sem conta. No fim, o homem que vendeu dezenas de milhões de discos morreu esquecido pelo Brasil.

Neste documentário: a infância em Ubá e a lição da mãe; a fita métrica do primeiro disco; o festival de Buenos Aires e "Tudo Passará"; o rótulo de brega; Nova York, México, Angola e o Carnegie Hall; García Márquez; a morfina, a cocaína e o revólver "Pelé"; Pablo Escobar; a noite de 1988; a confissão; a queda e o incêndio; a fé; o AVC; as irmãs; "Tenho saudades de mim mesmo"; e a verdade sobre o mito de que ele morreu abandonado.

Informações da biografia "Tudo Passará – A Vida de Nelson Ned" (André Barcinski, Companhia das Letras, 2023), de reportagens do Estado de Minas, Rolling Stone, Folhapress, CartaCapital, Gazeta do Povo e do Dicionário Cravo Albin. Relatos são atribuídos a quem os fez. Informações disponíveis até 02/11/2026.

{CHAPS}

#NelsonNed #TudoPassará #MúsicaBrasileira'''.replace('{CHAPS}',CHAPS)
TAGS='nelson ned, nelson ned história, nelson ned tudo passará, pequeno gigante da canção, nelson ned morte, nelson ned documentário, nelson ned cocaína, nelson ned pablo escobar, cantores brega, música romântica brasileira, domingo à tarde, assim foi a vida, nelson ned biografia'
assert len(TAGS)<=500
open('desc.txt','w').write(DESC+'\n'); open('tags.txt','w').write(TAGS+'\n')
rows=''.join(f'<tr><td class="t">{t}</td><td><b>{html.escape(n)}</b><br>{html.escape(i)}</td></tr>\n' for t,n,i in out)
CAUT='''<li>Episódio de 1988 (esposa ferida): só "acidente com arma de fogo, ele negou ter atirado e foi processado". Sem imagem de arma ou violência.</li>
<li>Cofre, cocaína, Escobar, violência em casa: sempre "segundo a biografia de André Barcinski".</li>
<li>Filhos e ex-esposas (vivos): só falas públicas (Flip 2023). Nada sobre ordem dos casamentos.</li>
<li>Não usar "morreu abandonado": as irmãs cuidaram dele; o vídeo derruba esse mito.</li>
<li>Saúde: perda da visão de um olho (não cegueira total).</li>
<li>Números: "dezenas de milhões de discos", "1 milhão nos EUA segundo os biógrafos", "Carnegie Hall mais de uma vez".</li>
<li>Nanismo: tratar com respeito; nunca usar imagens que ridicularizem.</li>
<li>Nunca rosto gerado por IA. Fotos reais com crédito.</li>'''
json.dump({'title':TITLE,'desc':DESC,'tags':TAGS,'chaps':CHAPS,'rows':rows,'caut':CAUT,'paras':paras,'words':W},open('pack.json','w'),ensure_ascii=False)
print(CHAPS); print(W, round(W/WPM,1), len(TAGS))
