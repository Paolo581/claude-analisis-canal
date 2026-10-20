import re, html, json
TITLE="LUA BLANCO — A Doença HORRÍVEL Que Levou a Estrela de Rebelde aos 39 Anos"
WPM=135
raw=[]
for n in range(1,8):
    for p in open(f'bloco{n}.txt').read().split('\n\n'):
        if p.strip(): raw.append(p.strip())
paras=[re.sub(r'^[RA]: ','',p) for p in raw]
open('roteiro_completo.txt','w').write('\n\n'.join(raw)+'\n')
open('voz.txt','w').write('\n\n'.join(paras)+'\n')
W=sum(len(p.split()) for p in paras)
CH=[('Dezoito de outubro','A notícia','Vela acesa · Celular com tela apagada (ilustrativo)'),
('Mas, antes de chegar àquela mensagem','O avô Billy Blanco','Foto de arquivo de Billy Blanco (com crédito) · Belém antiga'),
('O nome dele era Tom Jobim.','Tom Jobim e a bossa nova','Rio anos 1950/60 (arquivo)'),
('O primeiro grande sucesso','As músicas do avô','Discos de vinil antigos (ilustrativo)'),
('Cinco de março','Nasce Lua','Casa com instrumentos musicais (ilustrativo)'),
('Dois mil e oito.','Três Irmãs','Foto de imprensa de Lua jovem (com crédito)'),
('Malhação.','Malhação','Guitarra elétrica (ilustrativo)'),
('Outubro de dois mil e dez.','O AVC do avô','Corredor de hospital (ilustrativo)'),
('Vinte e um de março de dois mil e onze.','Rebelde','Logotipo/abertura de Rebelde (com crédito)'),
('A banda se chamava Rebeldes.','A banda Rebeldes','Fotos de shows (imprensa, com crédito)'),
('Oito de julho de dois mil e onze.','A morte do avô','Piano fechado (ilustrativo)'),
('Em entrevistas, ela falou sobre o que foi viver Rebelde','O preço da fama','Mala de viagem num quarto de hotel (ilustrativo)'),
('O nome dele era Arthur Aguiar.','Arthur Aguiar','Fotos de imprensa da época (com crédito)'),
('Quatro de novembro de dois mil e vinte e três.','O almoço','Mesa de churrascaria (ilustrativo)'),
('Depois de Rebelde, Lua não parou.','A carreira','Fotos de imprensa (com crédito)'),
('Dois mil e dezesseis.','Mão no Sonho','Capa do disco (com crédito)'),
('Em dois mil e dezesseis, Lua assumiu','Leandro e o sonho de ser mãe','Duas xícaras numa mesa (ilustrativo)'),
('Segundo a tia de Lua','O diagnóstico','Letreiro neutro com os sinais de alerta'),
('Quem contou como foram aqueles dois meses','Os dois meses','Mãos dadas (ilustrativo)'),
('E existe uma mensagem que mostra','A última mensagem','Celular com mensagem genérica (ilustrativo)'),
('Domingo, dezoito de outubro de dois mil e vinte e seis.','18 de outubro','Céu ao entardecer · Letreiro com a data'),
('Arthur Aguiar estava fazendo uma transmissão','A despedida','Velório: fotos públicas com crédito (sem caixão em close)'),
('Naquele mesmo domingo','Benito e Lua','Duas velas acesas (ilustrativo)'),
('A história de Lua deixa uma lição','O que ela deixou','Mesa posta para duas pessoas · Telefone (ilustrativo)'),
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
DESC='''Em 18 de outubro de 2026, aos 39 anos, Lua Blanco, a Roberta de "Rebelde", partiu. Fazia só dois meses que ela tinha descoberto a doença.

Uma homenagem à vida de Lua Blanco: a neta de Billy Blanco, parceiro de Tom Jobim; os primeiros passos na Globo; a febre "Rebelde" e a morte do avô no mesmo ano; o preço escondido da fama; o almoço que fez as pazes com Arthur Aguiar depois de 11 anos; o sonho de ser mãe; e os dois meses que ela atravessou com fé, cercada por mais de 80 pessoas.

Informações de Terra, Metrópoles, CNN Brasil, Caras, Purepeople, Jornal do Brasil e Catraca Livre. O tipo de câncer foi informado pela imprensa; a família não divulgou detalhes. Este vídeo não substitui orientação médica.

{CHAPS}

#LuaBlanco #Rebelde #Homenagem'''.replace('{CHAPS}',CHAPS)
TAGS='lua blanco, lua blanco morre, lua blanco câncer, lua blanco homenagem, rebelde, roberta rebelde, rebeldes banda, arthur aguiar lua blanco, billy blanco, lua blanco história, lua blanco família, câncer de intestino, lua blanco despedida'
assert len(TAGS)<=500
open('desc.txt','w').write(DESC+'\n'); open('tags.txt','w').write(TAGS+'\n')
rows=''.join(f'<tr><td class="t">{t}</td><td><b>{html.escape(n)}</b><br>{html.escape(i)}</td></tr>\n' for t,n,i in out)
CAUT='''<li>Família pediu respeito ao luto: tom de homenagem, nada sensacionalista em letreiros.</li>
<li>Câncer: sempre "segundo a imprensa"; nenhuma imagem de hospital real.</li>
<li>Velório: sem close de caixão; só fotos públicas de imprensa com crédito.</li>
<li>Mensagem à amiga: não mostrar print com nome/foto da amiga.</li>
<li>Trechos de Rebelde, músicas de Billy Blanco e de Lua: curtos, licenciados ou com crédito.</li>
<li>Rostos reais: só fotos de arquivo/imprensa com crédito; nunca rosto gerado por IA.</li>'''
json.dump({'title':TITLE,'desc':DESC,'tags':TAGS,'chaps':CHAPS,'rows':rows,'caut':CAUT,'paras':paras,'words':W},open('pack.json','w'),ensure_ascii=False)
print(CHAPS); print(W, round(W/WPM,1), len(TAGS))
