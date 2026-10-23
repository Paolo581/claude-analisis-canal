import re, html, json
TITLE="CARLOS ALBERTO DE NÓBREGA: A Verdade HORRÍVEL Sobre Sua Internação Aos 90 Anos"
WPM=135
raw=[]
for n in range(1,9):
    for p in open(f'bloco{n}.txt').read().split('\n\n'):
        if p.strip(): raw.append(p.strip())
paras=[re.sub(r'^[RA]: ','',p) for p in raw]
open('roteiro_completo.txt','w').write('\n\n'.join(raw)+'\n')
open('voz.txt','w').write('\n\n'.join(paras)+'\n')
W=sum(len(p.split()) for p in paras)
CH=[('Durante meses, Carlos Alberto de Nóbrega sentiu','Os meses de cansaço','Foto pública recente de Carlos Alberto na Praça (com crédito) · Fachada de hospital genérica'),
('Mas, para entender o que estava em jogo','Niterói, 1936','Niterói antiga (arquivo)'),
('Manoel era um homem do rádio.','O banco de Buenos Aires','Banco de praça em Buenos Aires (ilustrativo)'),
('Carlos Alberto foi estudar Direito.','Do Direito ao humor','Rádio antigo (ilustrativo)'),
('Em mil novecentos e cinquenta e seis, a televisão','Golias e a TV Paulista','Foto de arquivo de Ronald Golias (com crédito)'),
('Nos anos seguintes, Carlos Alberto passou por várias emissoras.','Família Trapo','Foto de Família Trapo (com crédito)'),
('O negócio se chamava Baú da Felicidade.','O Baú e Silvio Santos','Carnê antigo (ilustrativo) · Foto de arquivo de Silvio (crédito)'),
('Manoel de Nóbrega morreu em mil novecentos e setenta e seis.','A morte do pai','Foto de arquivo de Manoel de Nóbrega (com crédito)'),
('O programa era Os Trapalhões.','Os Trapalhões','Foto de arquivo dos Trapalhões (com crédito)'),
('Anos depois, ele contou como foi a conversa com Renato Aragão.','"Prefiro ser teu amigo"','Letreiro com a frase'),
('Depois de uma rápida passagem pela Band','Nasce A Praça É Nossa','Abertura da Praça (com crédito)'),
('Onze anos.','Onze anos sem Silvio','Fotos públicas de Carlos e Silvio (com crédito)'),
('Segundo o próprio Carlos Alberto, uma noite ele sonhou','O sonho','Céu noturno (ilustrativo)'),
('Em setembro de dois mil e cinco, Ronald Golias morreu.','Adeus, Golias','Foto de Golias na Escolinha (com crédito)'),
('O nome dele era Batoré.','Batoré','Foto de arquivo de Batoré (com crédito)'),
('Silvio Santos morreu no dia dezessete de agosto','A morte de Silvio','Trecho curto do choro no SBT (com crédito)'),
('O primeiro aviso veio em outubro de dois mil e vinte e um.','Arritmia e covid','Monitor cardíaco (ilustrativo)'),
('Em novembro de dois mil e vinte e três, ele estava no sítio','A queda e a cirurgia','Escada de madeira (ilustrativo)'),
('Desta vez, foi uma virose.','A semi-UTI','Corredor de hospital (ilustrativo)'),
('Em março de dois mil e vinte e seis, poucos dias antes','A pneumonia e os 90 anos','Bolo com velas "90" (ilustrativo)'),
('Sete de março de dois mil e dezenove.','As 8 paradas de Marcelo','Foto pública de Marcelo de Nóbrega (com crédito)'),
('Carlos Alberto foi casado por cerca de trinta e quatro anos','Três casamentos, seis filhos','Fotos públicas da família (com crédito)'),
('Ele tem um carinho especial por cada um.','A herança','Chave de casa (ilustrativo)'),
('A ex era Andréa.','A guerra das ex','Fotos públicas de Andréa e Renata (com crédito)'),
('Outubro de dois mil e vinte e seis.','Outubro de 2026','Letreiro com a data'),
('O diagnóstico foi uma infecção causada por um vírus','O vírus Coxsackie','Ilustração médica genérica do coração'),
('Um marcapasso.','O marcapasso','Ilustração de marcapasso (genérica)'),
('Antes da operação, ele ainda apareceu num vídeo','"Não dói nada"','Letreiro com a fala do áudio'),
('Março de dois mil e vinte e quatro.','O medo revelado','Trecho curto do Chega Mais (com crédito)'),
('Em dois mil e vinte e quatro, uma revista perguntou','"Só Deus me para"','Letreiro com a frase'),
('Num especial de Natal, o SBT usou inteligência artificial','O pai recriado','Trecho curto do especial (com crédito)'),
('Ele conheceu o bisneto, Francisco.','O bisneto','Mão de bebê (ilustrativo)'),
('Ele cuidou do pai até o fim.','O banco que continua','Banco de praça ao pôr do sol (ilustrativo)'),
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
DESC='''Aos 90 anos, Carlos Alberto de Nóbrega, o eterno apresentador de "A Praça É Nossa", foi internado em outubro de 2026 no Hospital Sírio-Libanês. Um vírus agravou a insuficiência cardíaca que ele já tinha, o coração passou a bater devagar demais e ele recebeu um marcapasso.

Neste documentário: o pai, Manoel de Nóbrega, e o banco de praça que nasceu em Buenos Aires; Golias, Jô Soares e a Família Trapo; o Baú da Felicidade e Silvio Santos; a saída dos Trapalhões; os 11 anos sem falar com Silvio e o sonho que os reaproximou; as perdas de Golias, Batoré e Silvio; a sequência de sustos de saúde desde 2021; o filho Marcelo e as 8 paradas cardíacas; a herança passada em vida; a briga pública com a ex Andréa; e a frase que hoje soa como um aviso.

Informações de SBT News, O Tempo/Folhapress, UAI, RepórterMT, Terra/Contigo, CNN Brasil, IstoÉ, Diário do Nordeste, Itatiaia, Folha PE, DOL, Gazeta, Correio Braziliense e Poder360. Carlos Alberto de Nóbrega está vivo; o vídeo traz as informações disponíveis até 23/10/2026.

{CHAPS}

#CarlosAlbertoDeNobrega #APracaENossa #SBT'''.replace('{CHAPS}',CHAPS)
TAGS='carlos alberto de nóbrega, carlos alberto de nobrega internado, carlos alberto marcapasso, carlos alberto de nobrega saúde, a praça é nossa, manoel de nóbrega, silvio santos, ronald golias, renata domingues, andréa de nóbrega, marcelo de nóbrega, carlos alberto 90 anos, sbt, praça da alegria'
assert len(TAGS)<=500
open('desc.txt','w').write(DESC+'\n'); open('tags.txt','w').write(TAGS+'\n')
rows=''.join(f'<tr><td class="t">{t}</td><td><b>{html.escape(n)}</b><br>{html.escape(i)}</td></tr>\n' for t,n,i in out)
CAUT='''<li>Ele está vivo: nenhuma insinuação de morte ou estado terminal em letreiro, thumbnail ou capítulo.</li>
<li>Confirmar a alta (prevista para 23/10/2026) e atualizar o Bloco 7 antes de publicar.</li>
<li>Nunca usar foto dele em leito de hospital; só imagens públicas com crédito.</li>
<li>Briga com Andréa: manter as versões dela, dele e de Renata; "traição" só como o que ela deu a entender.</li>
<li>Herança: só a fala dele ("já passei tudo"); não inventar brigas entre os filhos. Penhora de bens é fofoca: não usar.</li>
<li>Rostos reais: nunca rosto gerado por IA (o pai em IA só como trecho oficial do SBT, com crédito).</li>'''
json.dump({'title':TITLE,'desc':DESC,'tags':TAGS,'chaps':CHAPS,'rows':rows,'caut':CAUT,'paras':paras,'words':W},open('pack.json','w'),ensure_ascii=False)
print(CHAPS); print(W, round(W/WPM,1), len(TAGS))
