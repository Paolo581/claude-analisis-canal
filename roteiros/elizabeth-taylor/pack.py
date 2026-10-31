import re, html, json
TITLE="Assim FOI a VIDA de ELIZABETH TAYLOR — O Segredo HORRÍVEL Que Hollywood Escondeu Por Trás da Mulher Mais Bonita do Mundo"
WPM=135
raw=[]
for n in range(1,10):
    for p in open(f'bloco{n}.txt').read().split('\n\n'):
        if p.strip(): raw.append(p.strip())
paras=[re.sub(r'^[RA]: ','',p) for p in raw]
open('roteiro_completo.txt','w').write('\n\n'.join(raw)+'\n')
open('voz.txt','w').write('\n\n'.join(paras)+'\n')
W=sum(len(p.split()) for p in paras)
CH=[('Durante décadas, ela foi chamada','A mulher mais bonita do mundo','Liz Taylor no auge, anos 50/60 (foto pública, com crédito)'),
('Vinte e sete de fevereiro de mil novecentos e trinta e','Londres, 1932','Londres anos 30 (arquivo)'),
('Abril de mil novecentos e trinta e nove.','A fuga da guerra','Navio transatlântico anos 30 (arquivo)'),
('Em mil novecentos e quarenta e um, com nove anos','Olhos de adulta','Liz criança (foto pública, com crédito)'),
('O homem era o próprio pai.','O pai','Casa à noite (ilustrativo)'),
('Janeiro de mil novecentos e quarenta e três.','MGM e Lassie','Cartaz de Lassie (com crédito)'),
('O filme se chamava National Velvet.','O cavalo','Cena de A Mocidade é Assim Mesmo (com crédito)'),
('O nome dele era Louis B. Mayer.','Contra o chefão da MGM','Estúdios MGM anos 40 (arquivo)'),
('Mil novecentos e cinquenta. Elizabeth tinha dezoito ano','Nicky Hilton','Foto do casamento de 1950 (com crédito)'),
('Em mil novecentos e cinquenta e um, estreou Um Lugar ao','Montgomery Clift e Michael Wilding','Cena de Um Lugar ao Sol (com crédito)'),
('Doze de maio de mil novecentos e cinquenta e seis.','A noite do acidente','Estrada à noite (ilustrativo)'),
('O nome dele era Mike Todd.','Mike Todd','Foto pública de Liz e Mike Todd (com crédito)'),
('No começo de mil novecentos e cinquenta e oito, Elizab','O avião Lucky Liz','Avião bimotor anos 50 (arquivo)'),
('Elizabeth ficou viúva aos vinte e seis anos.','Viúva aos 26','Manchetes de 1958 (arquivo)'),
('Quando a notícia se espalhou, os Estados Unidos ficara','O escândalo Eddie Fisher','Capas de revista 1958 (com crédito)'),
('O estúdio era a 20th Century Fox. O filme, Cleópatra.','Um milhão de dólares','Cartaz de Cleópatra (com crédito)'),
('O filme se chamava Disque Butterfield 8.','O filme que ela odiava','Cartaz de Butterfield 8 (com crédito)'),
('A infecção era tão grave que Elizabeth corria risco','A morte anunciada','Hospital de Londres anos 60 (arquivo)'),
('Abril de mil novecentos e sessenta e um.','O Oscar da traqueostomia','Foto real de Liz com o Oscar, 1961 (com crédito)'),
('As filmagens foram transferidas para Roma.','Cleópatra e Burton','Bastidores de Cleópatra (com crédito)'),
('Na primavera de mil novecentos e sessenta e dois, um jo','O Vaticano','Vaticano (foto pública)'),
('Quinze de março de mil novecentos e sessenta e quatro.','O primeiro casamento com Burton','Foto pública de Liz e Burton (com crédito)'),
('Em mil novecentos e sessenta e nove, ele comprou para e','Os diamantes','Diamante Taylor-Burton (foto pública, com crédito)'),
('O filme se chamava Quem Tem Medo de Virginia Woolf.','Virginia Woolf','Cena do filme (com crédito)'),
('Dez de outubro de mil novecentos e setenta e cinco.','Botsuana','Rio africano ao pôr do sol (ilustrativo)'),
('O casamento com John Warner terminou em mil novecentos','O fundo do poço','Comprimidos sobre mesa (ilustrativo)'),
('A clínica se chamava Betty Ford Center.','Betty Ford','Fachada da clínica (foto pública)'),
('Lá atrás, ficou guardado um nome. Rock Hudson.','Rock Hudson','Foto pública de Liz e Rock Hudson (com crédito)'),
('Naquele mesmo ano, Elizabeth ajudou a fundar uma organi','A luta contra a AIDS','Laço vermelho (ilustrativo)'),
('Trinta e um de maio de mil novecentos e oitenta e sete.','Reagan','Foto pública do jantar da amfAR 1987 (com crédito)'),
('O nome dele era Larry Fortensky.','O último marido','Foto pública do casamento de 1991 (com crédito)'),
('Michael Jackson.','Michael Jackson','Foto pública de Liz e Michael Jackson (com crédito)'),
('Em mil novecentos e noventa e um, ela lançou um perfum','White Diamonds','Frasco de perfume (ilustrativo)'),
('Era um tumor.','O tumor','Corredor de hospital (ilustrativo)'),
('Em dois mil e quatro, os médicos deram a Elizabeth um','O coração','Liz em evento dos anos 2000 (foto pública, com crédito)'),
('O funeral começou com quinze minutos de atraso.','Atrasada até no enterro','Forest Lawn, Glendale (foto pública)'),
('As joias foram vendidas por mais de cento e trinta e se','O leilão','Leilão da Christie\'s 2011 (arquivo, com crédito)'),
('As gravações tinham sido feitas a partir de mil novec','As fitas','Gravador de fita antigo (ilustrativo)'),
('Por trás do rosto mais bonito do mundo, havia uma sobr','A sobrevivente','Liz jovem (foto pública, com crédito)'),
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
DESC='''Durante décadas, Elizabeth Taylor foi chamada de a mulher mais bonita do mundo. Mas, longe das câmeras, ela vivia presa a remédios e à bebida, com uma dor que começou ainda menina. E houve um dia em que o mundo foi informado de que ela estava morta.

Neste documentário: a infância moldada pela mãe e pela MGM; as surras do pai; a queda do cavalo que fraturou sua coluna aos 12 anos; o primeiro marido violento; Montgomery Clift; o avião Lucky Liz; o escândalo com Eddie Fisher e Debbie Reynolds; a traqueostomia, a morte anunciada por engano e o Oscar que ela acreditava ter ganho "por pena"; Cleópatra, Richard Burton e o Vaticano; a clínica Betty Ford; Rock Hudson e a luta contra a AIDS; Michael Jackson; e o pedido para chegar atrasada ao próprio enterro.

Informações da biografia de Elizabeth Taylor, das gravações usadas no documentário "Elizabeth Taylor: The Lost Tapes" (HBO, 2024), da revista Harper's Bazaar (2011), CBS News, PBS, People, AFI, TCM, amfAR e Guinness World Records. Relatos pessoais são atribuídos a quem os fez. Informações disponíveis até 31/10/2026.

{CHAPS}

#ElizabethTaylor #Hollywood #CinemaClássico'''.replace('{CHAPS}',CHAPS)
TAGS='elizabeth taylor, liz taylor, elizabeth taylor história, elizabeth taylor documentário, richard burton, cleópatra, mike todd, eddie fisher, debbie reynolds, rock hudson, michael jackson, elizabeth taylor morte, hollywood clássica, assim foi a vida, oito casamentos'
assert len(TAGS)<=500
open('desc.txt','w').write(DESC+'\n'); open('tags.txt','w').write(TAGS+'\n')
rows=''.join(f'<tr><td class="t">{t}</td><td><b>{html.escape(n)}</b><br>{html.escape(i)}</td></tr>\n' for t,n,i in out)
CAUT='''<li>Aborto causado por Nicky Hilton: sempre "segundo o relato dela" (livro de 1988). Surras do pai: relato dela em entrevista de TV.</li>
<li>Acidente de Montgomery Clift: sem imagens do rosto ferido; detalhes variam entre fontes.</li>
<li>Acidente de Mike Todd: causa não confirmada; não afirmar mau tempo.</li>
<li>Vaticano: "um jornal ligado ao Vaticano", sem cravar data/publicação.</li>
<li>Michael Jackson: só amizade e a frase de defesa; não detalhar acusações.</li>
<li>Filhos e netos (vivos): só fatos públicos; nada sobre saúde de Maria.</li>
<li>Leilão: US$ 137 milhões = joias (não o total de US$ 156 milhões).</li>
<li>Nunca rosto gerado por IA. Fotos reais com crédito.</li>'''
json.dump({'title':TITLE,'desc':DESC,'tags':TAGS,'chaps':CHAPS,'rows':rows,'caut':CAUT,'paras':paras,'words':W},open('pack.json','w'),ensure_ascii=False)
print(CHAPS); print(W, round(W/WPM,1), len(TAGS))
