import re, html, json
TITLE="Assim FOI a VIDA de NEY MATOGROSSO — A Verdade SOMBRIA Que Ele Escondeu Por 50 Anos Atrás da Maquiagem"
WPM=135
raw=[]
for n in range(1,10):
    for p in open(f'bloco{n}.txt').read().split('\n\n'):
        if p.strip(): raw.append(p.strip())
paras=[re.sub(r'^[RA]: ','',p) for p in raw]
open('roteiro_completo.txt','w').write('\n\n'.join(raw)+'\n')
open('voz.txt','w').write('\n\n'.join(paras)+'\n')
W=sum(len(p.split()) for p in paras)
CH=[('Mil novecentos e setenta e três. Em plena','O rosto pintado','Foto pública dos Secos e Molhados na TV, 1973 (com crédito)'),
('Primeiro de agosto de mil novecentos e quarenta e um.','Bela Vista, 1941','Cidade de fronteira anos 40 (ilustrativo)'),
('O medo tinha motivo.','O pai militar','Farda militar antiga (ilustrativo)'),
('Ainda criança, Ney descobriu','O medo da morte','Menino olhando janela (ilustrativo, sem rosto)'),
('Na adolescência, o desejo de ser artista','Filho meu não vai ser artista','Casa simples do interior (ilustrativo)'),
('Até que, aos dezessete anos','A briga e a Aeronáutica','Quartel anos 50 (arquivo)'),
('Mas a farda não era o destino dele.','O Hospital de Base','Brasília anos 60 (arquivo)'),
('O nome dela era Luzinete.','A menina Luzinete','Corredor de hospital antigo (ilustrativo, sem criança)'),
('Fora do hospital, Brasília também deu a Ney','A voz nos corais','Coral anos 60 (ilustrativo)'),
('Mil novecentos e sessenta e seis. Ney juntou','Hippie no Rio','Rio de Janeiro anos 60 (arquivo)'),
('Mil novecentos e setenta e dois. Ney já tinha','Secos e Molhados','Capa do primeiro disco (com crédito)'),
('Ney subia ao palco com o rosto coberto','A maquiagem','Foto pública de Ney maquiado (com crédito)'),
('O sucesso dos Secos e Molhados cresceu','Os censores','Carimbo de censura (ilustrativo)'),
('Dez de fevereiro de mil novecentos e setenta e quatro.','Maracanãzinho, 1974','Ginásio do Maracanãzinho (arquivo)'),
('Pouco tempo depois, a banda fez uma viagem ao México.','O contrato rasgado','Papel rasgado (ilustrativo)'),
('Onze de agosto de mil novecentos e setenta e quatro.','O fim da banda','TV antiga (ilustrativo)'),
('Ney decidiu seguir sozinho.','Bandido','Foto pública de show nos anos 70 (com crédito)'),
('A música se chamava Homem com H.','Homem com H','Disco de vinil (ilustrativo)'),
('O nome dele era Cazuza.','Cazuza','Foto pública de Cazuza (com crédito)'),
('Enquanto isso, outra história da vida de Ney','A paz com o pai','Mãos dadas de idosos (ilustrativo)'),
('No começo dos anos oitenta, os jornais brasileiros','A doença sem nome','Manchetes de jornal anos 80 (arquivo)'),
('Sete de julho de mil novecentos e noventa.','A morte de Cazuza','Velas (ilustrativo)'),
('O nome dele era Marco de Maria.','Marco de Maria','Quarto com cama hospitalar (ilustrativo)'),
('Ney chegou perto da cama.','A última noite','Janela à noite (ilustrativo)'),
('Lá no começo desta história, ficou guardado um número.','Três enterros numa semana','Cemitério ao entardecer (ilustrativo)'),
('Dizia-se que Ney Matogrosso tinha sido estudado','Dei sorte','Laboratório (ilustrativo)'),
('Contou que tinha tomado LSD mais de vinte vezes.','As revelações de 2024','Floresta (ilustrativo)'),
('O jornalista se chamava Julio Maria.','A biografia','Capa da biografia (com crédito)'),
('Primeiro de maio de dois mil e vinte e cinco.','O filme','Cartaz oficial de Homem com H (com crédito)'),
('A segunda polêmica foi a nudez.','As polêmicas','Claquete (ilustrativo)'),
('Era a Imperatriz Leopoldinense.','Ney na Sapucaí','Fotos públicas do desfile 2026 (com crédito)'),
('Dezessete de março de dois mil e vinte e seis.','Dona Beita, 103 anos','Flores brancas (ilustrativo)'),
('A primeira foi no dia primeiro de agosto','85 anos','Bolo/velas (ilustrativo)'),
('A mulher era Xuxa.','Xuxa','Estúdio de TV (ilustrativo)'),
('Ele não revelou qual foi o procedimento.','A cirurgia','Palco vazio (ilustrativo)'),
('Oitenta e Cinco Anos de Ousadia.','A turnê','Foto pública de show recente (com crédito)'),
('Por trás da maquiagem que parou o Brasil','O segredo','Foto pública de Ney (com crédito)'),
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
DESC='''Em 1973, em plena ditadura militar, um homem de rosto pintado e peito nu parou o Brasil. Por trás daquela maquiagem havia um menino com pavor do pai militar e uma dor que Ney Matogrosso levou décadas para contar.

Neste documentário: a infância em Bela Vista; a briga com o pai aos 17 anos; o Hospital de Base de Brasília e a menina Luzinete; os Secos e Molhados e a censura; a noite em que ele enfrentou a polícia no Maracanãzinho; o contrato rasgado e o fim da banda; Bandido e Homem com H; o romance com Cazuza; a reconciliação com o pai; a AIDS, o pedido de Cazuza e a última noite com Marco de Maria; a semana dos três enterros; o filme Homem com H, o Carnaval da Imperatriz, a morte de dona Beita aos 103 anos, os 85 anos e a turnê 85 Anos de Ousadia.

Informações da biografia "Ney Matogrosso: A Biografia", de Julio Maria (Companhia das Letras, 2021), e de entrevistas e reportagens da Rolling Stone Brasil, CNN Brasil, Folha de S.Paulo, Metrópoles, Billboard Brasil, A Tarde, A Gazeta e TV Fama. Relatos íntimos são apresentados como versão do próprio Ney ou da biografia. Informações disponíveis até 25/10/2026.

{CHAPS}

#NeyMatogrosso #SecosEMolhados #MPB'''.replace('{CHAPS}',CHAPS)
TAGS='ney matogrosso, ney matogrosso vida, ney matogrosso história, secos e molhados, homem com h, ney matogrosso cazuza, marco de maria, ney matogrosso pai, ney matogrosso ditadura, ney matogrosso 85 anos, ney matogrosso documentário, ney matogrosso mãe beita, ney matogrosso verdade, assim foi a vida, mpb'
assert len(TAGS)<=500
open('desc.txt','w').write(DESC+'\n'); open('tags.txt','w').write(TAGS+'\n')
rows=''.join(f'<tr><td class="t">{t}</td><td><b>{html.escape(n)}</b><br>{html.escape(i)}</td></tr>\n' for t,n,i in out)
CAUT='''<li>Ney está vivo: tudo atribuído a ele, à biografia ou à imprensa. Cirurgia de out/2026 sempre com "não é nada grave", nas palavras dele. Nada que sugira doença séria.</li>
<li>Luzinete: nenhuma imagem de criança; abuso só como relato da biografia.</li>
<li>Marco de Maria: data da morte em conflito (1990, 1992 ou 1993); manter "começo dos anos noventa".</li>
<li>Cazuza: cusparada, tapa e pedido do AZT só como relatos de Ney.</li>
<li>Xuxa e ex-integrantes dos Secos e Molhados: só fatos, sem julgamento; a polêmica termina na reconciliação.</li>
<li>Drogas: só o que Ney contou em 2024 (LSD, ayahuasca); sem dependência.</li>
<li>Nunca rosto gerado por IA. Fotos reais com crédito.</li>'''
json.dump({'title':TITLE,'desc':DESC,'tags':TAGS,'chaps':CHAPS,'rows':rows,'caut':CAUT,'paras':paras,'words':W},open('pack.json','w'),ensure_ascii=False)
print(CHAPS); print(W, round(W/WPM,1), len(TAGS))
