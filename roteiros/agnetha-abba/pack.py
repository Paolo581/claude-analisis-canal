import re, html, json
TITLE="Assim É a VIDA de AGNETHA do ABBA Aos 76 Anos — O Segredo SOMBRIO Que a Fez Desaparecer"
WPM=135
raw=[]
for n in range(1,9):
    for p in open(f'bloco{n}.txt').read().split('\n\n'):
        if p.strip(): raw.append(p.strip())
paras=[re.sub(r'^[RA]: ','',p) for p in raw]
open('roteiro_completo.txt','w').write('\n\n'.join(raw)+'\n')
open('voz.txt','w').write('\n\n'.join(paras)+'\n')
W=sum(len(p.split()) for p in paras)
CH=[('Nos anos setenta, ela era a voz','A loira do ABBA','Agnetha nos anos 70 (foto pública, com crédito)'),
('Cinco de abril de mil novecentos e cinquenta.','Jönköping, 1950','Jönköping e o lago Vättern (foto pública)'),
('Desde muito pequena, Agnetha vivia cantando','A menina que compunha','Piano antigo (ilustrativo)'),
('Aos quinze anos, Agnetha tomou','A telefonista dos bailes','Salão de baile antigo (ilustrativo)'),
('A canção se chamava, em sueco','O primeiro sucesso','Disco de vinil (ilustrativo)'),
('O nome dele era Björn Ulvaeus.','Björn','Foto pública de Björn Ulvaeus jovem (com crédito)'),
('O nome dela era Anni-Frid Lyngstad.','Frida','Foto pública de Frida jovem (com crédito)'),
('Seis de julho de mil novecentos e setenta e um.','O casamento','Igreja de Verum (foto pública)'),
('Em mil novecentos e setenta e dois, lançaram','Nasce o ABBA','Estúdio de gravação anos 70 (ilustrativo)'),
('Seis de abril de mil novecentos e setenta e quatro.','Waterloo','ABBA no Eurovision 1974 (arquivo, com crédito)'),
('O ABBA cantou Dancing Queen pela primeira vez','Dancing Queen e o rei','Palácio Real de Estocolmo (foto pública)'),
('A imprensa não falava só da voz dela.','Tratada como objeto','Flashes de fotógrafos (ilustrativo)'),
('Décadas depois, num documentário da BBC','A confissão','Agnetha em foto pública (com crédito)'),
('Em dezembro de mil novecentos e setenta e sete','Os filhos','Carrinho de bebê antigo (ilustrativo)'),
('Para entender aquela noite','A separação','Aliança sobre a mesa (ilustrativo)'),
('Três de outubro.','O avião na tempestade','Céu de tempestade à noite (ilustrativo)'),
('A partir dali, Agnetha passou a ter pavor','O medo de voar','Janela de avião (ilustrativo)'),
('O nome da música era The Winner Takes It All.','A música do divórcio','Capa do single de 1980 (com crédito)'),
('Benny e Frida tinham se casado','O outro casal','Foto pública dos quatro (com crédito)'),
('Em dezembro daquele ano, o ABBA','A pausa','Palco vazio (ilustrativo)'),
('Logo depois da pausa do ABBA','A carreira solo','Microfone antigo (ilustrativo)'),
('No fim dos anos oitenta','Ekerö','Paisagem de Ekerö (foto pública)'),
('Mil novecentos e noventa e quatro. Em Jönköping','A perda dos pais','Vela acesa (ilustrativo)'),
('Em mil novecentos e noventa e sete, Agnetha decidiu','O livro','Livro aberto (ilustrativo)'),
('O nome dele era Gert van der Graaf.','O desconhecido','Estrada no campo sueco (ilustrativo)'),
('No ano dois mil, a Justiça sueca agiu.','A perseguição','Porteira fechada (ilustrativo)'),
('E aquela história ainda ia voltar a assombrá-la.','O documentário','Claquete (ilustrativo)'),
('Em dois mil e quatro, quase vinte anos depois','A volta','Estúdio de gravação (ilustrativo)'),
('Em dois mil e treze, Agnetha fez','O voo de 2013','Avião decolando ao entardecer (ilustrativo)'),
('Em setembro de dois mil e vinte e um','Voyage','Capa do álbum Voyage (com crédito)'),
('Em maio de dois mil e vinte e dois, em Londres','Os avatares','ABBA Arena, Londres (foto pública)'),
('O rei Carl Gustaf','A homenagem do rei','Palácio Real de Estocolmo (foto pública)'),
('Em dois mil e vinte e seis, o grupo viveu uma perda.','Görel Hanser','Flores brancas (ilustrativo)'),
('Hoje, Agnetha Fältskog tem setenta e seis anos.','Agnetha hoje','Agnetha em foto pública recente (com crédito)'),
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
DESC='''Ela era a voz e o rosto mais famosos da música pop. Mas, de repente, Agnetha Fältskog, a loira do ABBA, desapareceu. Esta é a história real por trás do sumiço: o medo nascido numa tempestade no céu dos Estados Unidos, a música do próprio divórcio que ela cantou para o mundo, a perda dos pais e o desconhecido que invadiu o refúgio dela. E como, aos 76 anos, ela voltou ao palco sem sair de casa.

Neste documentário: a infância em Jönköping; o primeiro sucesso aos 17 anos; Björn, Benny e Frida; Waterloo e a fama mundial; a imprensa que a tratou como objeto; o avião de 1979; The Winner Takes It All; a pausa do ABBA; a ilha de Ekerö; a perseguição; o voo de 2013; ABBA Voyage; a homenagem do rei em 2024; e o bilhão de reproduções em 2026.

Fontes: Wikipedia, BBC (ABBA: Against the Odds, 2024), The Guardian/NME, SVT, Expressen, AP, Pollstar, fã-clube oficial ABBA Intermezzo e biografias. Relatos são atribuídos a quem os fez. Informações disponíveis até 09/11/2026.

Se você está passando por um momento difícil, procure ajuda: CVV, 188 (Brasil).

{CHAPS}

#ABBA #Agnetha #AgnethaFältskog'''.replace('{CHAPS}',CHAPS)
TAGS='abba, agnetha faltskog, agnetha abba, abba história, abba documentário, the winner takes it all, abba voyage, björn ulvaeus, frida abba, benny andersson, waterloo abba, dancing queen, assim é a vida, música anos 70'
assert len(TAGS)<=500
open('desc.txt','w').write(DESC+'\n'); open('tags.txt','w').write(TAGS+'\n')
rows=''.join(f'<tr><td class="t">{t}</td><td><b>{html.escape(n)}</b><br>{html.escape(i)}</td></tr>\n' for t,n,i in out)
CAUT='''<li>Os quatro integrantes estão vivos: nada de insinuar doença. Não usar sites/vídeos de IA com notícias falsas (ex.: "Frida hospitalizada").</li>
<li>Morte da mãe (1994): só "tirou a própria vida", sem método nem imagens. Manter o aviso do CVV (188) no vídeo e na descrição.</li>
<li>Perseguidor: só fatos de imprensa e Justiça (relacionamento 1997–1999, ordem de restrição, expulsão 2000, prisão 2003, 2005). Sem especular motivos. Não usar cenas do documentário de 2024 sem licença.</li>
<li>"The Winner Takes It All": sempre com a versão de Björn de que não é sobre os dois.</li>
<li>Avião de 1979: detalhes (raios, ventos) como "os relatos variam".</li>
<li>"Prêmio do bumbum": "suposto", origem incerta. Não usar imagens que sexualizem.</li>
<li>Músicas do ABBA: não usar trechos gravados (direitos autorais). Fotos reais com crédito. Nunca rosto gerado por IA.</li>'''
json.dump({'title':TITLE,'desc':DESC,'tags':TAGS,'chaps':CHAPS,'rows':rows,'caut':CAUT,'paras':paras,'words':W},open('pack.json','w'),ensure_ascii=False)
print(CHAPS); print(W, round(W/WPM,1), len(TAGS))
