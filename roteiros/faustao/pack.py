import re, html, json
TITLE="FAUSTÃO: Recluso na Mansão Há 3 Anos — O Que Aconteceu com Ele de Verdade"
WPM=135
raw=[]
for n in range(1,9):
    for p in open(f'bloco{n}.txt').read().split('\n\n'):
        if p.strip(): raw.append(p.strip())
paras=[re.sub(r'^[RA]: ','',p) for p in raw]
open('roteiro_completo.txt','w').write('\n\n'.join(raw)+'\n')
open('voz.txt','w').write('\n\n'.join(paras)+'\n')
W=sum(len(p.split()) for p in paras)
CH=[('Há mais de três anos, o homem que comandou','O sumiço','Foto pública de Faustão no Domingão (com crédito) · Portão fechado (ilustrativo)'),
('Mas, para entender como o homem mais barulhento','O menino do interior','Interior paulista anos 50 (arquivo)'),
('Porque, ainda adolescente, Fausto descobriu','O rádio aos 14 anos','Microfone de rádio antigo (ilustrativo)'),
('Fausto foi para a capital e virou repórter esportivo.','Repórter esportivo','Estádio anos 70 (arquivo)'),
('O programa se chamava Perdidos na Noite.','Perdidos na Noite','Trecho curto do Perdidos na Noite (com crédito)'),
('A Globo queria Fausto Silva nas tardes de domingo.','O Domingão','Abertura do Domingão (com crédito)'),
('E aquele sucesso transformou Faustão num dos homens','A fortuna','Letreiro "estimativa da imprensa"'),
('Abril de dois mil e catorze.','As polêmicas ao vivo','Letreiro neutro com a data'),
('Em dois mil e vinte e três, um ex-diretor do programa','As acusações dos bastidores','Letreiro: acusação x defesa'),
('Um ex-produtor do programa, Renato Moreira Lima','A condenação da Globo','Martelo de juiz (ilustrativo)'),
('O primeiro casamento durou cerca de dez anos.','Três casamentos','Fotos públicas da família (com crédito)'),
('Faustão lutava contra o diabetes e contra a balança.','O diabetes','Glicosímetro (ilustrativo)'),
('Janeiro de dois mil e vinte e um.','A saída da Globo','Fachada da Globo (foto pública)'),
('Lembra do nome que pedimos para você guardar?','Cordélia','Vela (ilustrativo)'),
('Meses depois, Faustão falou pela primeira vez sobre a saída','"Não iam me deixar na vitrine"','Letreiro com a frase'),
('Em janeiro de dois mil e vinte e dois, estreou o Faustão na Band.','O fracasso na Band','Gráfico de audiência caindo (ilustrativo)'),
('O primeiro sinal de que algo estava muito errado','Las Vegas','Corredor de hotel (ilustrativo)'),
('No dia cinco de agosto de dois mil e vinte e três','O coração falha','Monitor cardíaco (ilustrativo)'),
('Boatos sobre a morte dele se espalharam','"Por sorte, ainda não morri"','Trecho do vídeo de 19/08/2023 (com crédito)'),
('No dia dezoito de agosto de dois mil e vinte e três, a Band','A despedida que ele não viu','Estúdio vazio (ilustrativo)'),
('Vinte e sete de agosto de dois mil e vinte e três.','O coração novo','Coração com laço verde (ilustrativo)'),
('O Ministério da Saúde explicou que a fila','Furou a fila?','Letreiro com os dados oficiais'),
('O nome dele era Fábio Cordeiro da Silva.','Fábio, o doador','Foto pública de Fábio, só se autorizada (com crédito) · Praia de Santos'),
('Quatro dias depois do transplante','"Viver de novo"','Trecho do vídeo de 31/08/2023 (com crédito)'),
('A família de Faustão gravou uma campanha','Órgãos não vão para o céu','Campanha oficial do Ministério (com crédito)'),
('Logo depois do transplante, Faustão começou a fazer hemodiálise','O rim','Máquina de hemodiálise (ilustrativo)'),
('Meses depois, no Fantástico, Faustão resumiu tudo','"Coração de atleta"','Trecho curto do Fantástico (com crédito)'),
('Maio de dois mil e vinte e cinco.','A sepse','Corredor de UTI (ilustrativo)'),
('Nos primeiros dias de agosto de dois mil e vinte e cinco','Fígado e rim','Letreiro: 4 transplantes em 2 anos'),
('Um cardiologista que não fazia parte da equipe','"Chances mínimas"','Letreiro com a resposta do filho'),
('Vinte de setembro de dois mil e vinte e cinco.','Lara no altar','Foto pública do casamento (com crédito)'),
('Depois da alta, a vida de Faustão passou a acontecer','A vida reclusa','Janela de casa ao entardecer (ilustrativo)'),
('Faustão estava fazendo reabilitação.','A reabilitação','Halteres leves (ilustrativo)'),
('No dia quinze de setembro de dois mil e vinte e seis','De volta à Globo','Trecho curto do Conversa com Bial (com crédito)'),
('O homem que gritava Ô loco, meu nas tardes','O que aconteceu de verdade','Palco vazio do Domingão (foto pública)'),
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
DESC='''Há mais de três anos longe da TV e quase sem aparecer em público, o que aconteceu com Faustão? Neste documentário, a história completa do homem que comandou os domingos do Brasil por 32 anos, contada a partir do que ele mesmo revelou em 2026: "eu já estava no bico do corvo".

Do menino coroinha e locutor aos 14 anos ao "Perdidos na Noite" e ao Domingão; as polêmicas ao vivo e as acusações dos bastidores; a saída da Globo sem despedida e a morte da mãe na semana seguinte; o fracasso na Band; a insuficiência cardíaca, a polêmica da fila e o doador Fábio, de 35 anos; o rim, a sepse, o fígado e o novo rim (4 transplantes em 2 anos); a filha levada ao altar em cadeira de rodas; e a volta à Globo no Conversa com Bial.

Informações de Correio Braziliense, CNN Brasil, SBT News, Diário do Nordeste, Metrópoles, Jovem Pan, TNH1, Itatiaia, IstoÉ, Meio & Mensagem, Rolling Stone, Band, Gazeta SP e Ministério da Saúde. Valores de salário e patrimônio são estimativas da imprensa. Faustão está vivo; informações disponíveis até 23/10/2026.

{CHAPS}

#Faustao #FaustoSilva #DoacaoDeOrgaos'''.replace('{CHAPS}',CHAPS)
TAGS='faustão, fausto silva, faustão hoje, faustão saúde, faustão transplante, o que aconteceu com faustão, faustão recluso, faustão bial, domingão do faustão, faustão globo, faustão band, doação de órgãos, luciana cardoso, joão guilherme silva, faustão 76 anos'
assert len(TAGS)<=500
open('desc.txt','w').write(DESC+'\n'); open('tags.txt','w').write(TAGS+'\n')
rows=''.join(f'<tr><td class="t">{t}</td><td><b>{html.escape(n)}</b><br>{html.escape(i)}</td></tr>\n' for t,n,i in out)
CAUT='''<li>Ele está vivo: nenhuma insinuação de morte em letreiro, thumbnail ou capítulo.</li>
<li>"Mansão": não citar valor (R$ 40 milhões não confirmado); não mostrar imagens da casa sem autorização.</li>
<li>"Furou a fila": sempre com a explicação oficial do Ministério da Saúde na tela.</li>
<li>Acusações de ex-funcionários: só como acusação, com a defesa; não citar o caso de suicídio.</li>
<li>Doador Fábio: usar só imagens públicas autorizadas pela família; tom de respeito.</li>
<li>Salário e patrimônio: sempre "estimativa".</li>
<li>Nunca foto dele em leito de hospital; nunca rosto gerado por IA.</li>'''
json.dump({'title':TITLE,'desc':DESC,'tags':TAGS,'chaps':CHAPS,'rows':rows,'caut':CAUT,'paras':paras,'words':W},open('pack.json','w'),ensure_ascii=False)
print(CHAPS); print(W, round(W/WPM,1), len(TAGS))
