import re, html, json
TITLE="MARCOS MION: A Tragédia HORRÍVEL Que Ele Esconde Atrás do Sorriso Há 30 Anos"
WPM=135
raw=[]
for n in range(1,8):
    for p in open(f'bloco{n}.txt').read().split('\n\n'):
        if p.strip(): raw.append(p.strip())
paras=[re.sub(r'^[RA]: ','',p) for p in raw]
open('roteiro_completo.txt','w').write('\n\n'.join(raw)+'\n')
open('voz.txt','w').write('\n\n'.join(paras)+'\n')
W=sum(len(p.split()) for p in paras)
CH=[('Uma noite de comemoração na Avenida Paulista.','A noite no MASP','Avenida Paulista à noite · MASP iluminado (imagem de banco) · Letreiro "18 anos"'),
('São Paulo. Marcos Chaib Mion','Dois irmãos','Fotos de infância só se publicadas por ele (com crédito) · Casa paulistana à noite'),
('Ele começou pelo quarto.','O quarto fechado','Porta de quarto fechada · Corredor escuro'),
('Ela tomou uma decisão.','O teatro','Palco pequeno de escola de teatro (ilustrativo) · Letreiro "A arte me deu a vida"'),
('Dezoito anos. Num dia comum','A conta dos 18 anos','Letreiro "18 = 18"'),
('Mil novecentos e noventa e nove.','Da Globo à MTV','Trecho curto de Sandy e Junior e Piores Clipes (com crédito)'),
('Dois mil e dois.','Descontrole','Letreiro "Descontrole → Sobcontrole"'),
('Em dois mil e dez, o Mion trocou','Legendários e A Fazenda','Trechos curtos (com crédito)'),
('São Paulo, nos dias depois do enterro','Os olhos da mãe','Close de olhos sorrindo em silhueta (ilustrativo) · Letreiro com a frase da GQ'),
('Lembra da obsessão de ser pai','Romeo','Fotos públicas de Mion com Romeo (com crédito)'),
('Miami. Um quarto de hotel.','O quarto de hotel','Quarto de hotel na penumbra (ilustrativo) · Letreiro "câncer de mama"'),
('Autismo.','O diagnóstico','Letreiro "Autismo" · Laço de quebra-cabeça (símbolo do autismo)'),
('Dezembro de dois mil e quinze.','A escova de dentes azul','Escova de dentes azul em close (ilustrativo) · Capa do livro (com crédito)'),
('Segundo o Mion contou ao site Metrópoles','"Eu não quero ser autista"','Letreiro com a frase · Fundo escuro'),
('Janeiro de dois mil e vinte e um.','A demissão','Letreiro "11 meses antes do fim do contrato"'),
('A ligação que mudou tudo','A volta à Globo','Trecho curto da estreia do Caldeirão (com crédito)'),
('Quarta-feira, quatro de fevereiro de dois mil e vinte e seis.','O show não para','Letreiro "O show não para"'),
('Abril de dois mil e vinte e seis.','A homenagem ao Didi','Letreiro com os comentários (sem prints com nomes)'),
('Bento Ribeiro, humorista','O processo','Fachada de fórum genérica · Letreiros "versão do Bento" / "Mion nega" / "segredo de justiça"'),
('Dois mil e vinte e quatro. Revista GQ.','O luto que não acaba','Letreiro com a frase · Paulista ao amanhecer'),
('Quase toda família tem alguém assim.','Quem ficou','Mesa de almoço de domingo vazia (ilustrativo)'),
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
DESC='''Uma noite de comemoração na Avenida Paulista terminou em tragédia: Marcelo, irmão mais velho de Marcos Mion, tinha acabado de passar em Medicina e morreu ao cair do vão livre do MASP. Mion tinha 14 anos. Neste documentário: o quarto de onde ele não conseguia sair, o que a mãe fez para salvá-lo, a conta assustadora que ele fez aos 18 anos, o filho Romeo e o diagnóstico de autismo, a escova de dentes azul, o câncer da esposa, a demissão da Record e a crise de 2026 na Globo.

As falas citadas foram dadas pelo próprio Marcos Mion em entrevistas (GQ, André Vasco, Metrópoles e outras). No caso envolvendo Bento Ribeiro, apresentamos a versão de cada lado; Marcos Mion nega as acusações e o processo corre em segredo de justiça.

{CHAPS}

#MarcosMion #Caldeirão #Autismo'''.replace('{CHAPS}',CHAPS)
TAGS='marcos mion, marcos mion irmão, marcos mion masp, marcos mion história, marcos mion filho autista, romeo mion, lei romeo mion, marcos mion bento ribeiro, marcos mion globo, caldeirão com mion, marcos mion record, suzana gullo, marcos mion depressão, a escova de dentes azul'
assert len(TAGS)<=500
open('desc.txt','w').write(DESC+'\n'); open('tags.txt','w').write(TAGS+'\n')
rows=''.join(f'<tr><td class="t">{t}</td><td><b>{html.escape(n)}</b><br>{html.escape(i)}</td></tr>\n' for t,n,i in out)
CAUT='''<li>A morte do Marcelo: nunca encenar a queda nem mostrar o local com marcações. Usar o MASP à noite em plano aberto.</li>
<li>Caso Bento Ribeiro: letreiros "versão do Bento" e "Mion nega" sempre juntos; mencionar o segredo de justiça. Sem trilha de vilão para nenhum dos dois.</li>
<li>Romeo: só imagens que o próprio Mion publicou; nada que exponha crises. Tom de respeito ao autismo.</li>
<li>Câncer da Suzana: sem imagens médicas; ela é tratada como sobrevivente.</li>
<li>Rostos reais: só fotos de imprensa ou publicações com crédito; nunca rosto gerado por IA. Trechos de TV curtos e com crédito.</li>'''
json.dump({'title':TITLE,'desc':DESC,'tags':TAGS,'chaps':CHAPS,'rows':rows,'caut':CAUT,'paras':paras,'words':W},open('pack.json','w'),ensure_ascii=False)
print(CHAPS); print(W, round(W/WPM,1), len(TAGS))
