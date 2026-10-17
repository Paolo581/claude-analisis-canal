import re, html, json
TITLE="PAPA LEÃO XIV: A Notícia HORRÍVEL Que o Vaticano Teve Que Revelar"
WPM=135
raw=[]
for n in range(1,8):
    for p in open(f'bloco{n}.txt').read().split('\n\n'):
        if p.strip(): raw.append(p.strip())
paras=[re.sub(r'^[RA]: ','',p) for p in raw]
open('roteiro_completo.txt','w').write('\n\n'.join(raw)+'\n')
open('voz.txt','w').write('\n\n'.join(paras)+'\n')
W=sum(len(p.split()) for p in paras)
CH=[('Domingo, onze de outubro','O anúncio na praça','Praça São Pedro cheia (arquivo licenciado) · Janela do Vaticano'),
('Dolton.','O menino de Dolton','Subúrbio de Chicago, casas simples (arquivo) · Fotos de família divulgadas pela imprensa'),
('A tábua de passar roupa da mãe virava altar.','O altar de brincadeira','Tábua de passar roupa antiga (ilustrativo) · Balinhas redondas de açúcar'),
('O irmão John contou a cena.','A profecia da vizinha','Rua de bairro americano anos 1960 (ilustrativo)'),
('Antes de chegar a esse lugar','Matemática e Roma','Villanova University (arquivo) · Ordenação em Roma (foto de imprensa)'),
('Mil novecentos e oitenta e cinco.','Chulucanas','Norte do Peru, deserto e Andes (arquivo)'),
('Uma explosão destruiu a porta','A bomba na porta da igreja','Porta de igreja danificada (ilustrativo) · Peru anos 1980 (arquivo)'),
('Em mil novecentos e oitenta e oito','Padre Roberto','Trujillo, bairros da periferia (arquivo)'),
('Junho de mil novecentos e noventa.','As perdas','Vela acesa · Fotos antigas de família'),
('Em mil novecentos e noventa e nove','Superior geral','Agostinianos (arquivo)'),
('Novembro de dois mil e catorze.','Bispo de Chiclayo','Catedral de Chiclayo (arquivo)'),
('Dois mil e vinte. A pandemia','O bispo do oxigênio','Cilindros de oxigênio · Filas no Peru 2020 (arquivo)'),
('Mas, antes disso, o bispo do oxigênio','O chamado de Roma','Vaticano por fora (arquivo)'),
('Março de dois mil e vinte e três.','A enchente','Fotos de Prevost na enchente (Cáritas Chiclayo, com crédito) · Botas de borracha'),
('Vinte e um de abril','A morte de Francisco','Imagens de arquivo do funeral de Francisco'),
('Oito de maio de dois mil e vinte e cinco.','A fumaça branca','Chaminé da Capela Sistina · Praça em festa'),
('Dois dias depois, diante dos cardeais','O nome Leão','Retrato de Leão XIII (domínio público)'),
('Domingo, onze de outubro de dois mil e vinte e seis. Meio-dia.','O Angelus','Praça no Angelus (arquivo licenciado)'),
('Terça-feira, treze de outubro.','A cirurgia','Fachada do Gemelli (arquivo)'),
('Os exames feitos depois da operação','O diagnóstico','Ilustração médica do pulmão · Letreiro "Adenocarcinoma"'),
('Na entrada principal do Gemelli','Não tenham medo','Estátua de João Paulo II com velas (arquivo licenciado)'),
('Abril de dois mil e vinte e dois. Chiclayo','A denúncia de Chiclayo','Chiclayo (arquivo) · Documentos genéricos (ilustrativo)'),
('A diocese de Chiclayo respondeu','A outra versão','Letreiros com as duas versões lado a lado'),
('O jornalista peruano Pedro Salinas','Pedro Salinas','Foto de imprensa de Pedro Salinas (com crédito)'),
('Vinte e sete de setembro','Lourdes','Santuário de Lourdes (arquivo)'),
('Seis de novembro.','A volta ao Peru','Mapa da América do Sul · Avião papal (arquivo)'),
('Um menino de Dolton','O pedido','Recapitulação das imagens-chave · Praça ao entardecer'),
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
DESC='''No dia 11 de outubro de 2026, diante da Praça São Pedro, o Papa Leão XIV fez um anúncio que ninguém esperava. Dois dias depois, estava numa mesa de cirurgia no Hospital Gemelli. E o Vaticano teve que revelar o diagnóstico: um câncer de pulmão, descoberto cedo.

Neste documentário: o menino de Dolton que celebrava missa na tábua de passar roupa da mãe; o jovem padre que ficou no Peru quando uma bomba destruiu a porta da igreja; o bispo de Chiclayo que correu atrás de oxigênio na pandemia; a fumaça branca de 2025; a denúncia de Chiclayo, contada com a versão das denunciantes e a da diocese; e o pedido que ele fez ao mundo.

As informações vêm de reportagens e comunicados oficiais (Vatican News, AP/PBS, CBS, NBC, CNN, Reuters, Crux, ACI Prensa, Maldita.es). Acusações são apresentadas como relatos atribuídos, com a resposta da Igreja. A situação de saúde do Papa pode ter mudado depois da gravação.

{CHAPS}

#PapaLeãoXIV #Vaticano #IgrejaCatólica'''.replace('{CHAPS}',CHAPS)
TAGS='papa leão xiv, papa leão xiv câncer, papa leão xiv cirurgia, papa leão xiv pulmão, papa leão xiv saúde, robert prevost, papa leão xiv história, papa leão xiv chiclayo, papa leão xiv peru, hospital gemelli, vaticano notícia, papa americano, papa leão xiv documentário, papa leão xiv biografia'
assert len(TAGS)<=500
open('desc.txt','w').write(DESC+'\n'); open('tags.txt','w').write(TAGS+'\n')
rows=''.join(f'<tr><td class="t">{t}</td><td><b>{html.escape(n)}</b><br>{html.escape(i)}</td></tr>\n' for t,n,i in out)
CAUT='''<li>Pessoa viva: nunca usar "repugnante" ou "horrível" ligado à pessoa dele em letreiros; o "horrível" do título é a notícia.</li>
<li>Denúncia de Chiclayo: sempre mostrar as duas versões juntas; não mostrar rosto do padre acusado nem citar o nome dele.</li>
<li>Vítimas (Chiclayo, Lourdes, Madrid): sem imagens que as identifiquem além de fotos públicas com crédito; nada gráfico.</li>
<li>Saúde: antes de publicar, conferir se ele já teve alta e se a viagem de 6 de novembro foi confirmada; ajustar a frase "Hoje, o Papa se recupera no Gemelli".</li>
<li>Câncer: ilustração médica neutra; sem imagens de cirurgia real.</li>
<li>Rostos reais: só fotos de arquivo/imprensa com crédito; nunca rosto gerado por IA.</li>'''
json.dump({'title':TITLE,'desc':DESC,'tags':TAGS,'chaps':CHAPS,'rows':rows,'caut':CAUT,'paras':paras,'words':W},open('pack.json','w'),ensure_ascii=False)
print(CHAPS); print(W, round(W/WPM,1), len(TAGS))
