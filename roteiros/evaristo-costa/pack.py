import re, html
TITLE="EVARISTO COSTA Perdeu 22 KG em 3 Semanas — A Verdade CRUEL Que o Brasil Não Viu"
files=['parte1.txt','parte2.txt','parte3.txt','parte4.txt','parte5.txt']
paras=[]
for f in files:
    for p in open(f).read().split('\n\n'):
        p=p.strip()
        if p: paras.append(re.sub(r'^[RA]: ','',p))
# voice html
body=''.join(f'<p>{html.escape(p)}</p>\n' for p in paras)
open('EvaristoCosta_Roteiro_Voz.html','w').write(f'''<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(TITLE)}</title>
<style>body{{background:#fff;color:#000;font-family:Georgia,serif;font-size:20px;line-height:1.7;max-width:760px;margin:0 auto;padding:32px 16px}}h1{{font-size:24px;line-height:1.3;margin-bottom:32px}}p{{margin:0 0 18px}}</style>
</head><body>
<h1>{html.escape(TITLE)}</h1>
{body}</body></html>''')
# chapters
CH=[('Evaristo Costa passou treze anos','A verdade que o Brasil não viu','Evaristo sorrindo na bancada do Jornal Hoje (arquivo) × corte seco para leito de hospital escuro · Texto: "−22 KG EM 3 SEMANAS"'),
('Evaristo de Oliveira Costa Merigo nasceu','O menino da bancada','São José dos Campos anos 80 · Sala de aula com mesa escolar (1.º objeto, ilustrativo) · Cabine de rádio antiga'),
('A TV Vanguarda, afiliada','TV Vanguarda e Globo','Fachada TV Vanguarda · Evaristo repórter no "Mais Você" e no "TV Trabalho" (arquivo, com crédito) · Mapa do tempo'),
('Dois de fevereiro de dois mil e quatro','A bancada do Jornal Hoje','Evaristo e Sandra Annenberg na bancada (arquivo) · Cena da caneta (2014) · Gafe "Acre e Pará no Nordeste"'),
('Jornal ao vivo não perdoa erro','O preço do ao vivo','Estúdio com luzes · Relógio marcando meio-dia · Frase de Sandra na tela'),
('Quinta-feira, vinte e sete de julho de dois mil e dezessete','A despedida','Vídeo da despedida de 27/07/2017 (trecho curto, com crédito) · Cadeira vazia na bancada'),
('O motivo concreto se chamava Amália','Cambridge','Universidade de Cambridge · Bicicletas nas ruas de Cambridge · Chad em "Os Incríveis 2" (trailer oficial)'),
('Em dois mil e dezenove, a CNN estava chegando','A CNN','Logo CNN Brasil 2020 · Chamadas do "CNN Séries Originais" · Cidade vazia na pandemia'),
('Até que chegou setembro de dois mil e vinte e um','Demitido pela TV','TV mostrando grade de programação (2.º objeto, ilustrativo) · Frases "sabotagem" e "porta dos fundos" em letreiro · Post do "olhar de peixe morto"'),
('Para entender essa guerra','Os primeiros sintomas','Evaristo engraçado no Instagram (posts públicos) · Campanha de Black Friday 2017 · Homem sentado na cama de manhã, sem força (ilustrativo)'),
('No consultório, contou do cansaço','O comprimido','Cartela de comprimidos (3.º objeto) · Consultório médico · Desenho de estômago × intestino'),
('R: Agora você vai descobrir, finalmente, qual foi o erro','O diagnóstico errado','Frase "Por um ano, ele me tratou como se eu tivesse gastrite" em letreiro · Endoscopia/colonoscopia (ilustrativo) · Ilustração da doença de Crohn'),
('Em dois mil e vinte, Evaristo finalmente tinha um nome','Doença de Crohn','Ilustração do sistema imune · Frase sobre imunidade baixa em letreiro'),
('Novembro de dois mil e vinte e três','Erisipela em São Paulo','Post do hospital em SP (público, com crédito) · Bolsa de antibiótico na veia (4.º objeto) · Avião cancelado'),
('Nos primeiros dias de janeiro de dois mil e vinte e quatro','A UTI em Cambridge','Hospital em Cambridge (fachada genérica) · UTI com monitor · Frase "a alta não veio" em letreiro'),
('A: Ao longo do tratamento','Os 22 quilos','Balança (5.º objeto) 99 → 77 kg · Trecho do PodCringe (com crédito) · Frase "Eu me sinto definhando"'),
('A história dessa resposta começa','"Não recebi diagnóstico terminal"','Evaristo na Record com crachá (post público) · Manchetes sobre o boato'),
('Até que chegou o dia vinte e seis de fevereiro de dois mil e vinte e cinco','A remissão','Post da remissão (print) · Pastel de feira · Itália (ilustrativo)'),
('Fevereiro de dois mil e vinte e seis.','O reality que não aconteceu','Logo "Casa do Patrão"/Record (notícias) · Frase "Evaristo Costa segue de férias"'),
('Naquela mesma semana de fevereiro','"Não é da sua conta"','Print do comentário com nome e foto BORRADOS · Resposta de Evaristo em letreiro'),
('Quarta-feira, dezenove de agosto de dois mil e vinte e seis','O falso "conteúdo adulto"','Trecho do vídeo (com crédito) · Lista da pauta: dor nas costas, colesterol'),
('Agora junte todas as peças','A verdade cruel','Montagem dos 5 objetos: bancada, tela de TV, comprimido, bolsa de antibiótico, balança · Evaristo com as filhas (só fotos públicas)'),
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
DESC='''Evaristo Costa deixou o Jornal Hoje no auge e, longe das câmeras, perdeu 22 kg em 3 semanas. Um ano tratando a doença errada, UTI na Inglaterra, sepse e a demissão que ele descobriu pela TV. A verdade que o Brasil não viu.

#EvaristoCosta #JornalHoje #DoençaDeCrohn'''
TAGS='evaristo costa, evaristo costa doença, evaristo costa crohn, evaristo costa hoje, o que aconteceu com evaristo costa, evaristo costa uti, evaristo costa 22 kg, evaristo costa jornal hoje, evaristo costa globo, evaristo costa cnn, doença de crohn, sandra annenberg, evaristo costa inglaterra, evaristo costa definhando'
rows=''.join(f'<tr><td class="t">{t}</td><td><b>{html.escape(n)}</b><br>{html.escape(i)}</td></tr>\n' for t,n,i in out)
chap=html.escape('\n'.join(f'{t} {n}' for t,n,_ in out))
open('EvaristoCosta_Pacote_Producao.html','w').write(f'''<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Pacote de Produção — Evaristo Costa</title>
<style>body{{background:#fff;color:#111;font-family:system-ui,Segoe UI,Arial,sans-serif;max-width:860px;margin:0 auto;padding:24px 16px;line-height:1.55}}h1{{font-size:24px}}h2{{font-size:19px;margin-top:32px;border-bottom:2px solid #eee;padding-bottom:4px}}pre{{white-space:pre-wrap;background:#f6f6f6;padding:12px;border-radius:6px;font-family:inherit}}table{{width:100%;border-collapse:collapse}}td{{border-bottom:1px solid #eee;padding:8px;vertical-align:top}}td.t{{font-weight:700;white-space:nowrap;width:60px}}.note{{color:#555;font-size:14px}}li{{margin-bottom:6px}}</style></head><body>
<h1>Pacote de Produção: Evaristo Costa</h1>
<p><b>Título:</b> {html.escape(TITLE)}</p>
<h2>Descrição (SEO)</h2><pre>{html.escape(DESC)}</pre>
<h2>Tags</h2><pre>{html.escape(TAGS)}</pre><p class="note">{len(TAGS)} caracteres (limite do YouTube: 500).</p>
<h2>Capítulos (colar na descrição)</h2><pre>{chap}</pre>
<p class="note">Tempos calculados a 195 palavras por minuto (~{round(w/195)} min no total). Ajuste pelo áudio real depois de gravar.</p>
<h2>Lista de imagens para o editor</h2><table>{rows}</table>
<h2>Cuidados na edição (Evaristo está vivo)</h2><ul>
<li>Saúde: usar só o que ele próprio publicou ou disse em entrevista. Não mostrar exames ou imagens médicas como se fossem dele.</li>
<li>Comentário homofóbico: borrar nome e foto da autora.</li>
<li>Unfollow de 2025: tratar só como boato sem confirmação. Nada de insinuar separação ou orientação sexual.</li>
<li>Trechos de TV, podcast e posts: curtos e com crédito (Globo, CNN Brasil, PodCringe/Record, TV Brasil).</li>
<li>Filhas: só imagens que ele mesmo publicou, sem close em rosto de menor.</li>
<li>Thumbnail: usar foto real licenciada na silhueta; não gerar o rosto dele com IA.</li>
</ul>
<h2>Thumbnails</h2><p>Thumb1_LONGE_DO_BRASIL_QUASE_MORREU.jpg · Thumb2_ELE_ESTA_DEFINHANDO.jpg (na mesma pasta). As silhuetas são espaço para as fotos reais.</p>
</body></html>''')
