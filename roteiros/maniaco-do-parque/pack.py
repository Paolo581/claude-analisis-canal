import re, html, json
TITLE="Assim FOI o CASO do MANÍACO DO PARQUE — A Verdade SOMBRIA Que Ninguém Te Contou em 1998"
WPM=135
raw=[]
for n in range(1,10):
    for p in open(f'bloco{n}.txt').read().split('\n\n'):
        if p.strip(): raw.append(p.strip())
paras=[re.sub(r'^[RA]: ','',p) for p in raw]
open('roteiro_completo.txt','w').write('\n\n'.join(raw)+'\n')
open('voz.txt','w').write('\n\n'.join(paras)+'\n')
W=sum(len(p.split()) for p in paras)
CH=[('Agosto de mil novecentos e noventa e oito. O rosto','O rosto na TV','Manchetes e imagens de TV de 1998 (arquivo, com crédito)'),
('O nome dele era Francisco de Assis Pereira.','A infância','Estrada de terra no interior paulista (ilustrativo)'),
('Ainda jovem, Francisco deixou o interior.','O motoboy','Motoboys em São Paulo anos 90 (arquivo)'),
('O parque se chamava Parque do Estado.','O Parque do Estado','Mata do Parque do Estado (foto pública)'),
('Segundo a investigação, ele circulava pela regi','A armadilha do caça-talentos','Estação Jabaquara anos 90 (arquivo)'),
('O nome dela é Lícia.','Lícia, a que escapou','Trilha na mata (ilustrativo, sem pessoas)'),
('Lá no começo desta história, ficou guardado um','O cheque e a delegacia','Fachada de delegacia (ilustrativo)'),
('Os nomes daquelas mulheres estão nos processos.','As vítimas','Velas acesas (ilustrativo; sem fotos das vítimas)'),
('Dentro da mata do Parque do Estado, longe das tril','A descoberta','Fita de isolamento policial (ilustrativo)'),
('Foi aí que a investigação deu a virada que falt','As sobreviventes','Retrato falado de 1998 (arquivo, com crédito)'),
('Lá no começo deste vídeo, ficou guardado um car','O cartão de visita','Cartão de visita (ilustrativo)'),
('A cidade se chamava Itaqui.','Itaqui','Rio Uruguai em Itaqui (foto pública)'),
('Quatro de agosto de mil novecentos e noventa e oit','A prisão','Jornal Nacional 05/08/1998 (arquivo, com crédito)'),
('Segundo as reportagens da época, no começo Franc','A confissão','Sala de interrogatório (ilustrativo)'),
('Mais de vinte e cinco anos depois da prisão, uma','As fitas','Gravador antigo (ilustrativo)'),
('Francisco passou por avaliações psiquiátricas.','Os laudos','Documentos de laudo (ilustrativo)'),
('Muitos anos mais tarde, Francisco deu uma entrevis','A entrevista','Estúdio de TV (ilustrativo)'),
('Francisco de Assis Pereira foi julgado em três j','Taubaté','Muros de presídio (ilustrativo)'),
('Vinte e quatro de julho de dois mil e dois. São P','O júri de 2002','Fachada do Fórum (foto pública)'),
('Na época dos crimes, a lei brasileira dizia que n','O limite de 30 anos','Martelo de juiz (ilustrativo)'),
('Segundo o autor de um livro sobre o assunto, Franc','As cartas de amor','Pilha de cartas (ilustrativo)'),
('Desde dois mil e nove, Francisco está preso numa','A vida na cadeia','Agulhas de tricô (ilustrativo)'),
('Em outubro de dois mil e vinte e quatro, estreou','O filme e a série','Cartazes oficiais (com crédito)'),
('Era a mãe de Francisco, Maria Helena.','A mãe','Casa simples (ilustrativo)'),
('Em dois mil e vinte e cinco, a advogada que repres','Os patins','Patins antigos (ilustrativo)'),
('Lá no começo deste vídeo, ficou guardada uma data','11 de agosto de 2028','Calendário (ilustrativo)'),
('Primeiro de julho de dois mil e vinte e seis.','O pedido de internação','Fachada do MP-SP (foto pública)'),
('Lícia, a moça de Diadema que escapou correndo','As sobreviventes hoje','Flores (ilustrativo)'),
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
DESC='''Em 1998, o rosto de um motoboy apareceu em todas as TVs do Brasil e o país passou a chamá-lo de Maníaco do Parque. Mas, antes de ser descoberto, ele já tinha estado numa delegacia e saído pela porta da frente. E existe uma data marcada na Justiça em que ele pode voltar às ruas.

Neste documentário: a infância de Francisco de Assis Pereira; o golpe do falso caça-talentos no Parque do Estado; a fuga de Lícia e o caso registrado como roubo; o cheque de uma vítima que passou pela delegacia; a descoberta de julho de 1998; as sobreviventes e o cartão de visita; a prisão em Itaqui; as gravações dos depoimentos; os laudos e o júri de 2002; as cartas de amor; a vida na prisão; a data de 11/08/2028 e o pedido de internação do Ministério Público em 2026.

Em respeito às vítimas e às famílias, este vídeo não descreve detalhes dos crimes. Informações de reportagens (Metrópoles, O Globo, DGABC, O Povo, Terra, Aventuras na História, Rolling Stone, Canaltech), da série documental "Maníaco do Parque: A História Não Contada" (Prime Video, 2024) e de registros judiciais citados pela imprensa. Informações disponíveis até 01/11/2026.

{CHAPS}

#ManiacoDoParque #TrueCrime #CasosReais'''.replace('{CHAPS}',CHAPS)
TAGS='maníaco do parque, francisco de assis pereira, caso maníaco do parque, maníaco do parque 1998, parque do estado, serial killer brasileiro, crimes reais, true crime brasil, maníaco do parque soltura, maníaco do parque 2028, assim foi o caso, casos policiais, história do crime'
assert len(TAGS)<=500
open('desc.txt','w').write(DESC+'\n'); open('tags.txt','w').write(TAGS+'\n')
rows=''.join(f'<tr><td class="t">{t}</td><td><b>{html.escape(n)}</b><br>{html.escape(i)}</td></tr>\n' for t,n,i in out)
CAUT='''<li>Nada gráfico: nenhuma imagem de corpos, cenas de crime ou fotos de vítimas na miniatura. Usar ilustrações neutras.</li>
<li>Vítimas: só nomes já públicos, com respeito. Sobreviventes só com imagens públicas que elas mesmas autorizaram (série/entrevistas).</li>
<li>Francisco está vivo e preso: falas sempre atribuídas (depoimentos, Record, imprensa). Sem frases sobre antropofagia ou sexualidade.</li>
<li>Soltura: sempre "pode sair"; há pedido de internação sem decisão (até out/2026).</li>
<li>Números com conflito: "condenado por 7 mortes, confessou 10 a 11"; pena "quase 286 anos".</li>
<li>Reconhecimento em Itaqui: duas versões; nome do pescador não confirmado.</li>
<li>Monetização: evitar sons/imagens de violência; manter tom documental.</li>
<li>Nunca rosto gerado por IA. Fotos reais da imprensa com crédito.</li>'''
json.dump({'title':TITLE,'desc':DESC,'tags':TAGS,'chaps':CHAPS,'rows':rows,'caut':CAUT,'paras':paras,'words':W},open('pack.json','w'),ensure_ascii=False)
print(CHAPS); print(W, round(W/WPM,1), len(TAGS))
