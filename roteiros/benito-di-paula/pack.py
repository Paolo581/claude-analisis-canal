import re, html, json
TITLE="BENITO DI PAULA: Cantou Até o Fim — A Luta HORRÍVEL Dos Seus Últimos Meses"
WPM=135
raw=[]
for n in range(1,9):
    for p in open(f'bloco{n}.txt').read().split('\n\n'):
        if p.strip(): raw.append(p.strip())
paras=[re.sub(r'^[RA]: ','',p) for p in raw]
open('roteiro_completo.txt','w').write('\n\n'.join(raw)+'\n')
open('voz.txt','w').write('\n\n'.join(paras)+'\n')
W=sum(len(p.split()) for p in paras)
CH=[('Trinta e um de julho','O último palco','Palco com piano sob luz baixa (ilustrativo)'),
('Mas, antes de chegar àquele palco','Nova Friburgo','Nova Friburgo, serra fluminense (arquivo)'),
('O pai.','O pai ferroviário','Trem antigo · Piano antigo (ilustrativo)'),
('O nome desse homem era Alfredo Motta.','Nasce Benito di Paula','Hotel antigo de serra (ilustrativo)'),
('Aos dezessete anos','O Rio de Janeiro','Rio anos 1960 (arquivo)'),
('Começou a procurar trabalho nas casas noturnas.','As boates de Copacabana','Copacabana à noite anos 1960 (arquivo)'),
('A cidade era Santos.','Santos e São Paulo','Santos anos 1960/70 (arquivo)'),
('Mil novecentos e setenta e um.','O disco censurado','Carimbo "censurado" (ilustrativo) · LP de 1971 (capa, com crédito)'),
('Mil novecentos e setenta e três.','Retalhos de Cetim','Capa de "Um Novo Samba" (com crédito) · trecho curto da música (licenciado)'),
('Logo depois veio Charlie Brown.','Charlie Brown','Imagens de arquivo de apresentações (licenciadas)'),
('Meados dos anos setenta.','O sambão-joia','Recortes de jornal antigos (ilustrativo)'),
('Estudiosos da música brasileira','A porta fechada','Biblioteca/estudos acadêmicos (ilustrativo)'),
('E essa coisa começou dentro da própria casa','O filho Rodrigo','Foto de imprensa de Benito e Rodrigo (com crédito)'),
('Dois mil e dezenove.','A perda de André','Vela acesa · Piano fechado (ilustrativo)'),
('Dois mil e vinte. A pandemia.','O cavanhaque raspado','Fotos públicas de 2020 (com crédito)'),
('Novembro de dois mil e vinte e dois.','Benito 80','Capa do disco (com crédito)'),
('Carnaval de dois mil e vinte e cinco.','Águia de Ouro','Desfile no Anhembi 2025 (arquivo licenciado)'),
('Agosto de dois mil e vinte e cinco.','A turnê dos 50 anos','Teatro Guararapes (arquivo)'),
('Benito di Paula estava com câncer.','O diagnóstico','Letreiro neutro "câncer de próstata"'),
('Fim de janeiro de dois mil e vinte e seis.','A dois pianos','Dois pianos frente a frente (ilustrativo)'),
('Sexta-feira, trinta e um de julho','Benito 85','Casa Natura Musical (arquivo) · Foto de imprensa do show (com crédito)'),
('Domingo, dezoito de outubro','18 de outubro','Hospital à noite (ilustrativo) · Letreiro com a data'),
('O lugar escolhido foi o Theatro Municipal','O Theatro Municipal','Fachada do Theatro Municipal de São Paulo (arquivo)'),
('Lembra do ferroviário de Nova Friburgo','Cantou até o fim','Recapitulação das imagens-chave · Piano vazio com luz de palco'),
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
DESC='''Em 31 de julho de 2026, aos 84 anos e em tratamento contra o câncer, Benito di Paula subiu ao palco pela última vez, ao lado do filho Rodrigo Vellozo. Menos de três meses depois, em 18 de outubro, o Brasil se despediu do cantor de "Retalhos de Cetim" e "Charlie Brown".

Uma homenagem à vida de Benito di Paula: o menino de Nova Friburgo, um de 13 irmãos, filho de um ferroviário que tocava piano; as boates de Copacabana; o primeiro disco censurado; o sucesso que atravessou fronteiras; o rótulo cruel de "sambão-joia"; a perda do filho André; o carinho de novas gerações; e o último show.

Informações de Agência Brasil, Diário do Rio, Alô Alô Bahia, IstoÉ, Rolling Stone, Diario de Pernambuco, Portal Tela, Jornal Opção e estudos acadêmicos (USP, Unirio). Números de vendas são estimativas.

{CHAPS}

#BenitoDiPaula #RetalhosDeCetim #Homenagem'''.replace('{CHAPS}',CHAPS)
TAGS='benito di paula, benito di paula morre, benito di paula homenagem, retalhos de cetim, charlie brown benito di paula, benito di paula história, benito di paula câncer, rodrigo vellozo, sambão joia, samba romântico, benito di paula último show, mpb, benito di paula biografia'
assert len(TAGS)<=500
open('desc.txt','w').write(DESC+'\n'); open('tags.txt','w').write(TAGS+'\n')
rows=''.join(f'<tr><td class="t">{t}</td><td><b>{html.escape(n)}</b><br>{html.escape(i)}</td></tr>\n' for t,n,i in out)
CAUT='''<li>Tom de homenagem: família em luto; nada sensacionalista em letreiros.</li>
<li>Doença: não mostrar imagens de hospital reais nem detalhes não divulgados.</li>
<li>André Vellozo: não citar causa da morte (não divulgada nas fontes).</li>
<li>Músicas: usar só trechos curtos, licenciados ou com crédito.</li>
<li>Velório: se publicar depois de 20/10, todas as referências já estão no passado ("foi marcado").</li>
<li>Rostos reais: só fotos de arquivo/imprensa com crédito; nunca rosto gerado por IA.</li>'''
json.dump({'title':TITLE,'desc':DESC,'tags':TAGS,'chaps':CHAPS,'rows':rows,'caut':CAUT,'paras':paras,'words':W},open('pack.json','w'),ensure_ascii=False)
print(CHAPS); print(W, round(W/WPM,1), len(TAGS))
