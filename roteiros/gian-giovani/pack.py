import re, html, json
TITLE="Assim FOI a VIDA de GIAN & GIOVANI — A Verdade SOMBRIA Por Trás dos Irmãos Que Fizeram o Brasil Chorar de Amor"
WPM=135
raw=[]
for n in range(1,10):
    for p in open(f'bloco{n}.txt').read().split('\n\n'):
        if p.strip(): raw.append(p.strip())
paras=[re.sub(r'^[RA]: ','',p) for p in raw]
open('roteiro_completo.txt','w').write('\n\n'.join(raw)+'\n')
open('voz.txt','w').write('\n\n'.join(paras)+'\n')
W=sum(len(p.split()) for p in paras)
CH=[('Durante mais de trinta anos, dois irmãos','O ano que destruiu tudo','Fotos públicas da dupla nos anos 90 (com crédito)'),
('Vinte de janeiro de mil novecentos e sessenta e sete.','A roça e a fome','Cafezal e casa de chão batido (ilustrativo)'),
('Naquela casa sem nada, havia uma coisa','O violão proibido','Violão antigo em cima de armário (ilustrativo)'),
('Mas, naquela casa de chão batido, ninguém imaginava','O Dia das Mães','Rádio antigo (ilustrativo)'),
('Vinte e cinco quilômetros de subida a pé.','A Serrinha e a bicicleta','Estrada de terra em subida (ilustrativo)'),
('Mas, nos anos oitenta, Gian e Giovani só queriam um palco.','O bar do tio Milton','Bar de interior anos 80 (ilustrativo)'),
('Mas a prova mais dura daquela fase','O festival perdido','Palco de clube antigo (ilustrativo)'),
('O nome daquele homem era Mário.','O pai de Chitãozinho e Xororó','Caminhonete azul antiga (ilustrativo)'),
('Naquela caminhonete, a vontade de desistir','"Está muito ruim"','Estúdio antigo (ilustrativo)'),
('Uma casa popular no Jardim Liporace','A casa vendida','Casa popular (ilustrativo)'),
('Faltava pagar a conta.','As noites de gala','Mesas de gala (ilustrativo)'),
('Mas, em mil novecentos e oitenta e oito, o problema era outro.','O primeiro disco','Capa do LP de 1988 (com crédito)'),
('A saída foi fazer o trabalho com as próprias mãos.','O Fusca vermelho','Fusca vermelho na estrada (ilustrativo)'),
('Essa música passou mais de dois anos sem fazer sucesso.','Nem Dormindo Consigo Te Esquecer','Capa do disco de 1990 (com crédito)'),
('Os anos noventa foram a década de ouro do sertanejo.','O auge dos anos 90','Fotos públicas de shows (com crédito)'),
('Mas, no fim dos anos noventa, a dupla estava prestes','Convite de Casamento','Envelope de convite de casamento (ilustrativo)'),
('Só faltava uma vitrine à altura.','O Faustão em Franca','Parque de exposições lotado (ilustrativo)'),
('Mas, naquela virada do milênio, a vida pessoal de Giovani','A família de Giovani','Estrada à noite (ilustrativo)'),
('E, em dois mil e dez, veio um convite que Giovani nunca esqueceu.','Com Roberto Carlos','Trecho curto do especial (com crédito)'),
('Setembro de dois mil e doze.','As acusações de 2012','Letreiro: acusação x resposta'),
('Treze de janeiro de dois mil e catorze','A madrugada de 14 de janeiro','Avenida à noite, sem carros acidentados (ilustrativo)'),
('A ligação daquela manhã de janeiro','A ligação de Daniel','Telefone antigo (ilustrativo)'),
('Giovani tomou uma decisão naqueles dias.','O silêncio do pai','Janela com chuva (ilustrativo)'),
('O homem de chapéu era Sérgio Reis.','O abraço de Sérgio Reis','Foto pública de Sérgio Reis (com crédito)'),
('Julho de dois mil e catorze. O show tinha terminado.','A noite no ônibus','Ônibus de banda parado à noite (ilustrativo)'),
('Mas existe outra versão para essa mesma noite.','A versão de Gian','Letreiro: versão de Gian x versão de Giovani'),
('Vinte e nove de setembro de dois mil e catorze.','O AVC de Gian','Corredor de hospital (ilustrativo)'),
('Outubro de dois mil e catorze.','O fim da dupla','Palco vazio (ilustrativo)'),
('Mas, em dois mil e quinze, ninguém pensava em tragédia.','Os anos separados','Bandeira dos EUA / estrada (ilustrativo)'),
('Até que ele fez um convite a um cantor','Giovani e Rick','Foto pública de Rick & Giovani (com crédito)'),
('Durante os anos de separação, Gian repetia','"Estou bem, mas não estou feliz"','Hotel (ilustrativo)'),
('Seu Francisco, o pai que guardava o violão','O pedido do pai','Mãos de idoso (ilustrativo)'),
('Antes de anunciar a volta, Gian ainda precisava','O anúncio da volta','Post do anúncio de 15/03/2018 (com crédito)'),
('Mas, em dois mil e dezoito, era hora de comemorar.','Barretos 2018','Arena de Barretos (foto pública)'),
('Outubro de dois mil e vinte.','A penhora','Martelo de juiz (ilustrativo)'),
('E aquele ano de dois mil e vinte ainda tinha uma surpresa.','As lives','Tela de live (ilustrativo)'),
('Trinta e um de julho de dois mil e vinte e um.','O capotamento na Dutra','Rodovia (ilustrativo, sem o acidente)'),
('Os anos seguintes pareciam de calmaria.','O divórcio','Aliança sobre a mesa (ilustrativo)'),
('No meio desse furacão, Giovani completou','Gian ao lado do irmão','Fotos públicas recentes da dupla (com crédito)'),
('Mas setembro ainda não tinha terminado.','A morte de Rick','Céu ao entardecer (ilustrativo)'),
('Enquanto tudo isso acontecia, a dupla lançava','Planeta Sonho e o pedido cumprido','Capa de Planeta Sonho (com crédito)'),
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
DESC='''A história completa de Gian & Giovani, os irmãos de Franca que fizeram o Brasil chorar com "Nem Dormindo Consigo Te Esquecer" e "Convite de Casamento".

Da fome na roça e do violão escondido do pai ao festival perdido e ao encontro com o pai de Chitãozinho & Xororó; a casa vendida para pagar o primeiro disco; o Fusca vermelho; o auge dos anos 90 e o Faustão ao vivo de Franca; 2014, o ano em que Giovani perdeu a filha Gessyca, os irmãos brigaram no ônibus da banda e Gian sofreu um AVC; os anos separados; o pedido do pai que reuniu a dupla; Barretos 2018; e o turbulento 2026.

Informações de entrevistas da própria dupla (André Piunti, Domingo Show, Programa do Porchat, Programa do Gugu) e de Purepeople, UAI, Metrópoles, Jovem Pan, BNews, Bahia Notícias, Billboard Brasil, Diário do Pará, Correio e Poder360. Números de vendas são declarados pela dupla. Nos episódios com versões diferentes, mostramos as duas. Gian e Giovani estão vivos; informações disponíveis até 24/10/2026.

{CHAPS}

#GianeGiovani #Sertanejo #ConviteDeCasamento'''.replace('{CHAPS}',CHAPS)
TAGS='gian e giovani, gian & giovani, giovani, gian, gian e giovani história, nem dormindo consigo te esquecer, convite de casamento, gian e giovani briga, giovani filha gessyca, gian avc, giovani divórcio, giovani anna carolina, rick e giovani, sertanejo anos 90, assim foi a vida'
assert len(TAGS)<=500
open('desc.txt','w').write(DESC+'\n'); open('tags.txt','w').write(TAGS+'\n')
rows=''.join(f'<tr><td class="t">{t}</td><td><b>{html.escape(n)}</b><br>{html.escape(i)}</td></tr>\n' for t,n,i in out)
CAUT='''<li>Os dois estão vivos: nenhuma insinuação de morte em letreiro, thumbnail ou capítulo.</li>
<li>Gessyca: nunca imagens do acidente nem do velório; não citar o nome do motorista; tom de respeito.</li>
<li>Briga no ônibus: sempre as duas versões na tela; não usar "Gian agrediu" como fato.</li>
<li>Acusações de 2012 e prisão decretada de Gian: só como acusação/decisão noticiada, com a resposta e sem afirmar desfecho.</li>
<li>Divórcio: versão de Anna e nota da assessoria; não usar boatos (remédios, vasectomia, "amante", traição).</li>
<li>Penhora: valores como noticiados; desfecho desconhecido.</li>
<li>Rick: imagens públicas com crédito; nunca imagens dos destroços.</li>
<li>Vendas: sempre "segundo a dupla". Nunca rosto gerado por IA.</li>'''
json.dump({'title':TITLE,'desc':DESC,'tags':TAGS,'chaps':CHAPS,'rows':rows,'caut':CAUT,'paras':paras,'words':W},open('pack.json','w'),ensure_ascii=False)
print(CHAPS); print(W, round(W/WPM,1), len(TAGS))
