import re, html
TITLE="Assim FOI a VIDA de LENO — O Disco PROIBIDO Que Destruiu Sua Carreira"
files=['parte1.txt','parte2.txt','parte3.txt','parte4.txt','parte5.txt']
paras=[]
for f in files:
    for p in open(f).read().split('\n\n'):
        p=p.strip()
        if p: paras.append(re.sub(r'^[RA]: ','',p))
# voice html
body=''.join(f'<p>{html.escape(p)}</p>\n' for p in paras)
open('Leno_Roteiro_Voz.html','w').write(f'''<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(TITLE)}</title>
<style>body{{background:#fff;color:#000;font-family:Georgia,serif;font-size:20px;line-height:1.7;max-width:760px;margin:0 auto;padding:32px 16px}}h1{{font-size:24px;line-height:1.3;margin-bottom:32px}}p{{margin:0 0 18px}}</style>
</head><body>
<h1>{html.escape(TITLE)}</h1>
{body}</body></html>''')
# chapters
CH=[('R: Leno era um dos rostos','O ídolo que o Brasil esqueceu','Foto real licenciada de Leno jovem (anos 60) × silhueta de idoso de costas · Texto: "O DISCO PROIBIDO"'),
('Vinte e cinco de abril de mil novecentos e quarenta e nove.','O menino de Copacabana','Natal anos 50 (arquivo) · Copacabana anos 50 (arquivo) · TV em preto e branco (ilustrativo)'),
('Em mil novecentos e sessenta e cinco, com dezesseis anos','A Jovem Guarda','Programa Jovem Guarda (trecho curto, com crédito) · Foto de Renato e Seus Blue Caps (com crédito)'),
('Em mil novecentos e sessenta e seis, saiu o primeiro compacto.','Pobre Menina','Compacto de 1966 (1.º objeto: capa real, com crédito) · Trecho curto de "Pobre Menina"'),
('Em mil novecentos e sessenta e oito, a dupla Leno e Lílian acabou.','O fim no auge','Fotos de Leno e Lílian em 1967 (com crédito) · Recorte de revista da época (ilustrativo)'),
('Naquele mesmo período, Lílian se casou.','O boato','Foto de Os Vips (com crédito) · Letreiro: "Leno sempre quis cantar sozinho"'),
('Em mil novecentos e sessenta e oito, saiu o primeiro LP solo dele.','A Pobreza','Capa do LP "Leno" 1968 (com crédito) · Letreiro "1.º lugar no Brasil"'),
('Por volta dessa época, a CBS organizou','O baiano agitado','Foto de Raul Seixas jovem com Os Panteras (com crédito) · Urca à noite (ilustrativo)'),
('Naquele mesmo ano de mil novecentos e setenta','Dentro da CBS','Fachada/estúdio da CBS anos 70 (arquivo) · Leno e Raul juntos (foto com crédito, se houver)'),
('É preciso entender o Brasil daquele momento.','O AI-5','Manchete do AI-5, 13/12/1968 (arquivo público) · Carimbo "VETADO" sobre letra (ilustrativo)'),
('Em novembro de mil novecentos e setenta, Leno e Raul','Oito canais','Mesa de som e fita de rolo (2.º objeto, ilustrativo) · Letreiro "1.º disco do Brasil em 8 canais"'),
('Leno deu ao disco um nome estranho.','Johnny McCartney','Capa de "Vida e Obra de Johnny McCartney" (com crédito) · Letreiro das músicas proibidas'),
('As letras voltaram da censura cortadas.','A censura','Documento de censura (ilustrativo, sem simular documento oficial) · Letreiro "metade das letras vetada"'),
('Leno contou, décadas depois, o que ouviu da gravadora.','"Não tem nada a ver com sua imagem"','Letreiros com as falas reais de Leno · Foto de Roberto Carlos anos 70 (com crédito)'),
('A: Mas a gravadora não parou por aí.','A ordem de apagar a fita','Fita de rolo sendo rebobinada em close (ilustrativo) · Letreiro "a fita seria apagada"'),
('Leno contou anos depois como reagiu.','O limbo','Compacto duplo de 1971 (3.º objeto, com crédito) · Letreiro "Fiquei com o disco na mão, num limbo"'),
('Em mil novecentos e setenta e um, a TV Globo organizava','Sentado no Arco-Íris','Festival Internacional da Canção 1971 (trecho curto, com crédito)'),
('Raul continuou trabalhando na CBS.','Raul vira lenda','Raul no FIC 1972 (trecho curto, com crédito) · Capa de "Krig-ha, Bandolo!" (com crédito)'),
('Para entender esse detalhe, é preciso voltar','O jornal que uniu Raul e Paulo Coelho','Jornal alternativo dos anos 70 (4.º objeto, ilustrativo) · Foto de Raul e Paulo Coelho (com crédito)'),
('Num dos papéis guardados por ele','"Meus mestres"','Página manuscrita (ilustrativa, sem imitar a letra do Raul) · Capa do livro "O Baú do Raul Revirado" (com crédito)'),
('Em mil novecentos e setenta e seis, depois de cinco anos','Meu Nome É Gileno','Capa "Meu Nome É Gileno" (com crédito)'),
('Enquanto isso, a vida de Raul Seixas seguia','A morte de Raul','Manchete de 21/08/1989 (arquivo) · Sem imagens do corpo'),
('Os anos noventa trouxeram uma onda de nostalgia.','A caixa com o nome "Leno"','Depósito de arquivo (ilustrativo) · Caixa com "LENO" escrito (5.º objeto, ilustrativo) · Capa do CD de 1995 (com crédito)'),
('Um fã escreveu na internet','"Um disco de Raul sem Raul"','Letreiro do comentário · Letreiros com a resposta de Leno'),
('A: E foi aí que a segunda ferida se abriu.','"Censurou a gente"','Pôster de "Raul, o Início, o Fim e o Meio" (com crédito) · Cadeira vazia diante de câmera (ilustrativo)'),
('No começo dos anos dois mil, Leno voltou para Natal','A volta a Natal','Natal hoje (banco de imagens) · Capa "Canções com Raulzito" (com crédito)'),
('No dia vinte e um de junho de dois mil e quinze','O reencontro','Leno e Lílian na Virada Cultural 2015 (foto com crédito)'),
('Leno estava doente.','O réquiem','Mensagens em letreiro · Corredor de hospital desfocado (ilustrativo, sem pacientes)'),
('Para entender, é preciso voltar ao começo.','8 de dezembro','Montagem: compacto de 1966, fita, compacto duplo, jornal, caixa · Edifício Dakota (arquivo, sem cena do crime) · Letreiro "8/12/1980 · 8/12/2022"'),
('Pouco mais de dois anos depois','Lílian','Foto de Lílian (com crédito) · Letreiro "22/02/2025"'),
('Leno passou a vida inteira tentando ser ouvido','O preço da imagem','Foto final de Leno jovem e Leno idoso lado a lado (fotos reais licenciadas)'),
]
pos=0; idx={}
for p in paras:
    pass
words=0; starts=[]
raw=[]
for f in files:
    for p in open(f).read().split('\n\n'):
        p=p.strip()
        if p: raw.append(p)
cum=[];w=0
for p in raw:
    cum.append(w); w+=len(re.sub(r'^[RA]: ','',p).split())
out=[]
for key,name,img in CH:
    i=next(k for k,p in enumerate(raw) if p.startswith(key) or re.sub(r'^[RA]: ','',p).startswith(key))
    s=round(cum[i]/195*60)
    out.append((f'{s//60}:{s%60:02d}',name,img))
open('chapters.txt','w').write('\n'.join(f'{t} {n}' for t,n,_ in out)+'\n')
print('\n'.join(f'{t} {n}' for t,n,_ in out)); print('total min',round(w/195,1))
DESC='''Leno foi ídolo da Jovem Guarda aos 17 anos com "Pobre Menina", ao lado de Lílian. Em 1971, gravou com um Raul Seixas ainda desconhecido o disco "Vida e Obra de Johnny McCartney". A censura da ditadura vetou as letras, a gravadora engavetou o disco e mandou avisar que as fitas seriam apagadas. Nesta história: o fim da dupla Leno e Lílian, o encontro com Raul Seixas, o jornal que levou Raul até Paulo Coelho, a caixa encontrada 25 anos depois e a coincidência arrepiante do dia em que Leno morreu.

Em memória de Leno Azevedo (1949–2022) e Lílian Knapp (1948–2025).

#Leno #JovemGuarda #RaulSeixas'''
TAGS='leno, leno e lilian, leno azevedo, jovem guarda, raul seixas, vida e obra de johnny mccartney, disco proibido, censura ditadura música, pobre menina, lilian knapp, morte do leno, assim foi a vida, raul seixas paulo coelho'
rows=''.join(f'<tr><td class="t">{t}</td><td><b>{html.escape(n)}</b><br>{html.escape(i)}</td></tr>\n' for t,n,i in out)
chap=html.escape('\n'.join(f'{t} {n}' for t,n,_ in out))
open('Leno_Pacote_Producao.html','w').write(f'''<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Pacote de Produção — Leno</title>
<style>body{{background:#fff;color:#111;font-family:system-ui,Segoe UI,Arial,sans-serif;max-width:860px;margin:0 auto;padding:24px 16px;line-height:1.55}}h1{{font-size:24px}}h2{{font-size:19px;margin-top:32px;border-bottom:2px solid #eee;padding-bottom:4px}}pre{{white-space:pre-wrap;background:#f6f6f6;padding:12px;border-radius:6px;font-family:inherit}}table{{width:100%;border-collapse:collapse}}td{{border-bottom:1px solid #eee;padding:8px;vertical-align:top}}td.t{{font-weight:700;white-space:nowrap;width:60px}}.note{{color:#555;font-size:14px}}li{{margin-bottom:6px}}</style></head><body>
<h1>Pacote de Produção: Leno</h1>
<p><b>Título:</b> {html.escape(TITLE)}</p>
<h2>Descrição (SEO)</h2><pre>{html.escape(DESC)}</pre>
<h2>Tags</h2><pre>{html.escape(TAGS)}</pre><p class="note">{len(TAGS)} caracteres (limite do YouTube: 500).</p>
<h2>Capítulos (colar na descrição)</h2><pre>{chap}</pre>
<p class="note">Tempos calculados a 195 palavras por minuto (~{round(w/195)} min no total). Ajuste pelo áudio real depois de gravar.</p>
<h2>Lista de imagens para o editor</h2><table>{rows}</table>
<h2>Cuidados na edição</h2><ul>
<li>Fotos reais de Leno, Lílian, Raul e Paulo Coelho: só material licenciado ou com crédito. Nada de rostos gerados por IA.</li>
<li>Documentos de censura: usar ilustração claramente estilizada; nunca imitar um documento oficial real.</li>
<li>Falas entre aspas: são as palavras de Leno e Lílian em entrevistas (Farofafá, Lucinha Zanetti, Furia 2112). Manter exatamente como no roteiro.</li>
<li>Documentário de Walter Carvalho: apresentar como relato de Leno ("segundo Leno"), sem atacar o diretor em letreiros.</li>
<li>Morte de John Lennon e de Raul: sem imagens da cena do crime ou do corpo.</li>
<li>Músicas (Leno, Raul, Beatles): só trechos curtos por causa do Content ID; não usar como trilha contínua. Trechos de TV curtos e com crédito.</li>
</ul>
<h2>Thumbnails (a gerar)</h2><p><b>Thumb1 "ELES APAGARAM A VOZ DELE"</b> (recomendada): dupla dos anos 60 em silhueta num palco de TV colorido × fita de rolo dentro de uma caixa abandonada num arquivo escuro. <b>Thumb2 "O BRASIL ESQUECEU DELE"</b>: ídolo jovem cercado de fãs × homem idoso de costas olhando o mar. Usar silhuetas; rostos reais só com foto licenciada.</p>
</body></html>''')
