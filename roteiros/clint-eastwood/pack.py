import re, html, json
TITLE="CLINT EASTWOOD: Os Filhos SECRETOS e o Lado HORRÍVEL Que Hollywood Escondeu Por Décadas"
WPM=135
raw=[]
for n in range(1,9):
    for p in open(f'bloco{n}.txt').read().split('\n\n'):
        if p.strip(): raw.append(p.strip())
paras=[re.sub(r'^[RA]: ','',p) for p in raw]
open('roteiro_completo.txt','w').write('\n\n'.join(raw)+'\n')
open('voz.txt','w').write('\n\n'.join(paras)+'\n')
W=sum(len(p.split()) for p in paras)
CH=[('Por trás do cowboy mais famoso de Hollywood','O homem que ninguém conheceu','Clint jovem de chapéu (foto de imprensa, com crédito) · Porta trancada'),
('Mas, para entender o homem por trás do mito','O bebê Sansão','San Francisco anos 1930 (arquivo)'),
('Era a Grande Depressão.','A Grande Depressão','Fila de desempregados anos 30 (arquivo)'),
('Clint sempre falou daquela época','A infância contestada','Casa com piscina anos 40 (ilustrativo)'),
('Em mil novecentos e cinquenta e um, os Estados Unidos','O Exército','Base militar anos 50 (arquivo)'),
('Ele tinha conseguido uma carona num avião da Marinha','A queda no Pacífico','Avião militar antigo · Mar revolto (ilustrativo)'),
('Em mil novecentos e cinquenta e três, já fora do Exército','Maggie e a menina de Seattle','Seattle anos 50 (arquivo) · Certidão genérica (ilustrativo)'),
('Em abril de mil novecentos e cinquenta e quatro','A Universal','Portão de estúdio anos 50 (arquivo)'),
('E, em outubro de mil novecentos e cinquenta e cinco, veio o golpe.','Demitido pelo pescoço','Foto de arquivo de Burt Reynolds (com crédito)'),
('Sem contrato, sem salário','As piscinas e Rawhide','Pá e terra (ilustrativo) · Imagem de Rawhide (com crédito)'),
('Naquela época, Clint conheceu uma dublê','A segunda vida','Silhueta de casal (ilustrativo)'),
('Em mil novecentos e sessenta e quatro, um diretor italiano','O Homem Sem Nome','Trecho curto da trilogia dos dólares (licenciado/crédito)'),
('Em mil novecentos e setenta e um, Clint virou','Dirty Harry','Foto de Dirty Harry (com crédito)'),
('Com Maggie, Clint teve dois filhos.','O casamento aberto','Foto de família de arquivo (com crédito)'),
('O pai dele morreu de um ataque do coração.','A morte do pai','Relógio parado (ilustrativo)'),
('O nome dela era Sondra Locke.','Sondra Locke','Foto de arquivo de Sondra Locke (com crédito)'),
('Em mil novecentos e setenta e nove, o casamento','O divórcio','Aliança sobre mesa (ilustrativo)'),
('No fim dos anos setenta, Sondra Locke passou','As acusações de Sondra','Letreiro com a acusação narrada e a negativa dele'),
('O nome dela era Jacelyn Reeves.','A família secreta','Avião comercial anos 80 (ilustrativo)'),
('Na certidão de nascimento das duas crianças','A certidão "Recusado"','Certidão genérica com carimbo (ilustrativo)'),
('Em mil novecentos e oitenta e seis, Clint foi eleito prefeito','Prefeito de Carmel','Carmel-by-the-Sea (foto pública)'),
('Abril de mil novecentos e oitenta e nove.','As fechaduras trocadas','Fechadura nova numa porta (ilustrativo)'),
('Ainda em mil novecentos e oitenta e nove, um tabloide','Os segredos nas bancas','Banca de revistas anos 80 (ilustrativo, sem capas reais)'),
('Sondra entrou na Justiça contra Clint.','O primeiro acordo','Contrato e caneta (ilustrativo)'),
('Em mil novecentos e noventa e cinco, Sondra processou','O tribunal','Tribunal vazio (ilustrativo)'),
('Em mil novecentos e noventa e três, o filme Os Imperdoáveis','O Oscar e Frances Fisher','Estatueta (ilustrativo) · Foto de Frances Fisher (crédito)'),
('Lembra da menina que nasceu em Seattle','Laurie','Letreiro "1954"'),
('Dezembro de dois mil e dezoito.','O tapete vermelho','Foto da estreia de The Mule (com crédito)'),
('Sondra Locke tinha morrido no dia três de novembro','A morte de Sondra','Vela (ilustrativo)'),
('Anos antes, num programa de televisão americano','"Tenho alguns"','Letreiro: 8 filhos, 6 mulheres'),
('Em mil novecentos e noventa e seis, Clint Eastwood se casou de novo.','Dina e Christina','Fotos de imprensa (com crédito)'),
('Em julho de dois mil e vinte e quatro, Christina Sandera morreu.','A perda de Christina','Mission Ranch, Carmel (foto pública)'),
('No aniversário de noventa e cinco anos de Clint','Kathryn e Maggie','Bolo com velas (ilustrativo)'),
('Numa entrevista, o filho Kyle disse','Aposentado ou não?','Foto recente de Clint (com crédito)'),
('Na tela, Clint Eastwood foi o pistoleiro sem nome','As portas fechadas','Porta entreaberta ao pôr do sol (ilustrativo)'),
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
DESC='''Por trás do cowboy mais famoso de Hollywood existia um homem que quase ninguém conheceu. Clint Eastwood, hoje com 96 anos, tem pelo menos 8 filhos de 6 mulheres, e muitos deles ficaram longe dos holofotes por décadas.

Neste documentário: a infância na Grande Depressão (e a versão que a contesta); a queda de avião no Pacífico em 1951; a demissão da Universal por causa do pomo de Adão; o caso de 14 anos com a dublê Roxanne Tunis e a filha Kimber; Sergio Leone e Dirty Harry; os 14 anos com Sondra Locke, as acusações que ela fez e que ele nega veementemente, as fechaduras trocadas e o processo por fraude; os filhos com a comissária Jacelyn Reeves e a certidão com "recusado"; Laurie, entregue para adoção em 1954 e apresentada ao mundo em 2018; e as perdas recentes.

Informações de Wikipedia EN, People, Publishers Weekly, MeTV, ET Online, KSL, Jezebel, WFTV, Euronews, Consequence, Golf Digest e DGA. As acusações de Sondra Locke são relatos dela; Clint Eastwood as nega.

{CHAPS}

#ClintEastwood #Hollywood #Biografia'''.replace('{CHAPS}',CHAPS)
TAGS='clint eastwood, clint eastwood filhos, clint eastwood filhos secretos, clint eastwood sondra locke, sondra locke, clint eastwood 96 anos, clint eastwood vida, clint eastwood biografia, dirty harry, homem sem nome, os imperdoáveis, laurie eastwood, kimber eastwood, maggie johnson, clint eastwood aposentado'
assert len(TAGS)<=500
open('desc.txt','w').write(DESC+'\n'); open('tags.txt','w').write(TAGS+'\n')
rows=''.join(f'<tr><td class="t">{t}</td><td><b>{html.escape(n)}</b><br>{html.escape(i)}</td></tr>\n' for t,n,i in out)
CAUT='''<li>Pessoa viva: acusações de Sondra (abortos, laqueadura, contrato de fachada) sempre como relato dela, com a negativa dele na tela.</li>
<li>Laurie: há conflito sobre se ele sabia da gravidez; manter as duas versões.</li>
<li>Não usar a entrevista falsa do Kurier (2025) nem listas inventadas de outros canais.</li>
<li>Nenhuma insinuação de morte ou doença grave sem fonte.</li>
<li>Capas de tabloides: não reproduzir; usar ilustração genérica.</li>
<li>Trechos de filmes: curtos, licenciados ou com crédito.</li>
<li>Rostos reais: só fotos de imprensa com crédito; nunca rosto gerado por IA.</li>'''
json.dump({'title':TITLE,'desc':DESC,'tags':TAGS,'chaps':CHAPS,'rows':rows,'caut':CAUT,'paras':paras,'words':W},open('pack.json','w'),ensure_ascii=False)
print(CHAPS); print(W, round(W/WPM,1), len(TAGS))
