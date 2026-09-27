import re, html
TITLE="Assim FOI a VIDA de MAITÊ PROENÇA — O Crime REPUGNANTE Que a Justiça PERDOOU"
files=['parte1.txt','parte2.txt','parte3.txt','parte4.txt','parte5.txt']
paras=[]
for f in files:
    for p in open(f).read().split('\n\n'):
        p=p.strip()
        if p: paras.append(re.sub(r'^[RA]: ','',p))
# voice html
body=''.join(f'<p>{html.escape(p)}</p>\n' for p in paras)
open('MaiteProenca_Roteiro_Voz.html','w').write(f'''<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(TITLE)}</title>
<style>body{{background:#fff;color:#000;font-family:Georgia,serif;font-size:20px;line-height:1.7;max-width:760px;margin:0 auto;padding:32px 16px}}h1{{font-size:24px;line-height:1.3;margin-bottom:32px}}p{{margin:0 0 18px}}</style>
</head><body>
<h1>{html.escape(TITLE)}</h1>
{body}</body></html>''')
# chapters
CH=[('R: Maitê Proença tinha doze anos','O crime que a Justiça perdoou','Maitê em Dona Beija (arquivo, com crédito) × silhueta de menina num tribunal · Texto: "ELA DEFENDEU O PAI"'),
('Maitê Proença Gallo nasceu','A família perfeita','Campinas anos 60 (arquivo) · Piano de cauda · Livro de Shakespeare aberto em Macbeth (ilustrativo)'),
('Agosto de mil novecentos e setenta.','O revólver','Revólver antigo sobre mesa (1.º objeto, ilustrativo) · Casa de classe alta dos anos 70 à noite'),
('Sábado, sete de novembro de mil novecentos e setenta.','O sábado de novembro','Porta de quarto fechada (2.º objeto, ilustrativo) · Recortes de jornal de 1970 (com crédito)'),
('Durante dez dias, Augusto ficou foragido.','Dez dias foragido','Delegacia anos 70 (ilustrativo) · Manchetes da época'),
('Maitê e o irmão foram mandados','O pensionato luterano','Dormitório de internato antigo · Igreja de Campinas · Mão sobre a orelha de uma criança (ilustrativo)'),
('Para entender aquele tribunal','A carta rasgada','Agência dos Correios antiga · Carta rasgada (4.º objeto, ilustrativo)'),
('O processo contra Augusto','O juiz amigo e o príncipe dos advogados','Fórum de Campinas (fachada) · Martelo de juiz · Foto de arquivo de Waldir Troncoso Peres (com crédito)'),
('O argumento tinha nome','Legítima defesa da honra','Letreiro "LEGÍTIMA DEFESA DA HONRA" · Tribunal do júri vazio · Papel de depoimento datilografado (3.º objeto)'),
('O primeiro júri se reuniu em Campinas.','Absolvido duas vezes','Placar 7x0 e 4x3 em letreiro · Porta do fórum com multidão (ilustrativo)'),
('Depois do crime, segundo Maitê','O manicômio e o padre','Corredor de hospital psiquiátrico antigo (ilustrativo) · Casa paroquial'),
('Pouco tempo depois, Maitê foi embora','Sozinha em Paris','Paris anos 70 · Rua com chuva, adolescente de costas (ilustrativo)'),
('Paris foi só o começo da estrada.','40 países de carona','Estrada na Índia/África anos 70 · Mochileiros pedindo carona · Moeda de 1 dólar'),
('Um homem parou Maitê','O aviso na Índia','Mão segurando outra mão · Mercado indiano · Letreiro com a frase do homem'),
('Em mil novecentos e setenta e nove, estreou','A estreia na TV','Dinheiro Vivo e As Três Marias (arquivo, com crédito) · Raio X de fêmur (ilustrativo)'),
('Mil novecentos e oitenta e seis.','Dona Beija e a Playboy','Cena de Dona Beija (trecho curto, com crédito) · Capa da Playboy de 1987 (5.º objeto) com recorte discreto'),
('E o pai?','O pedido do pai','Quarto de hospital com aparelhos (ilustrativo) · Letreiro "desligue os aparelhos"'),
('A: Zuza, o irmão mais velho','Dois enterros no mesmo ano','Duas velas acesas · Janela de casa vista de fora (ilustrativo)'),
('No ano seguinte, em mil novecentos e noventa','Maria, a pensão e a Justiça','Bebê (ilustrativo) · Manchetes sobre a pensão (Conjur, 2010) · Valor R$ 254 mil em letreiro'),
('Dois mil e cinco.','Exposta no Faustão','Palco de auditório (ilustrativo) · Frase "Fiquei muito chocada" em letreiro'),
('Um ano depois do livro','Portugal e Haiti','Mosteiro dos Jerônimos, Lisboa · Tendas no Haiti pós-terremoto (arquivo, com crédito)'),
('Num texto publicado no próprio site','A frase perturbadora','Tela de site com a crônica (print, com crédito) · Palavra "JUNTOS" em letreiro'),
('A legítima defesa da honra continuou','Doca Street e o STF','Ângela Diniz/Búzios (arquivo) · Cartaz "Quem ama não mata" · Plenário do STF 01/08/2023'),
('Em agosto de dois mil e vinte e quatro','O preço no corpo','Cavalo, moto e escada (ilustrativo, sem acidente) · Sala acolchoada (ilustrativo)'),
('Veio a pandemia, e os teatros fecharam.','O Pior de Mim','Teatro vazio · Cartaz/fotos oficiais da peça (com crédito)'),
('Em dois mil e vinte, o pai da filha dela','Novos capítulos','Manchetes Paulo Marinho × Flávio (2020) · Maitê e Adriana Calcanhotto (só fotos públicas)'),
('A casa da avenida','A casa virou loja','Fachada da loja atual em Nova Campinas · Sítio com horta e cachoeira'),
('Agora junte todas as peças','O perdão','Montagem dos 5 objetos: revólver, porta, depoimento, carta, capa de revista · Porta se abrindo para a luz'),
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
DESC='''Aos 12 anos, Maitê Proença viu o pai matar a mãe e, no tribunal, ficou do lado dele. Ele foi absolvido duas vezes pela "legítima defesa da honra". Depois vieram mais duas mortes, a fama e um segredo exposto na TV.

Se você está passando por um momento difícil, ligue 188 (CVV).

#MaitêProença #LegítimaDefesaDaHonra #DonaBeija'''
TAGS='maitê proença, maite proenca, maitê proença mãe, maitê proença pai, maitê proença história, maitê proença hoje, o que aconteceu com maitê proença, margot proença gallo, legítima defesa da honra, dona beija, maitê proença faustão, o pior de mim, crimes que chocaram o brasil, maitê proença vida'
rows=''.join(f'<tr><td class="t">{t}</td><td><b>{html.escape(n)}</b><br>{html.escape(i)}</td></tr>\n' for t,n,i in out)
chap=html.escape('\n'.join(f'{t} {n}' for t,n,_ in out))
open('MaiteProenca_Pacote_Producao.html','w').write(f'''<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Pacote de Produção — Maitê Proença</title>
<style>body{{background:#fff;color:#111;font-family:system-ui,Segoe UI,Arial,sans-serif;max-width:860px;margin:0 auto;padding:24px 16px;line-height:1.55}}h1{{font-size:24px}}h2{{font-size:19px;margin-top:32px;border-bottom:2px solid #eee;padding-bottom:4px}}pre{{white-space:pre-wrap;background:#f6f6f6;padding:12px;border-radius:6px;font-family:inherit}}table{{width:100%;border-collapse:collapse}}td{{border-bottom:1px solid #eee;padding:8px;vertical-align:top}}td.t{{font-weight:700;white-space:nowrap;width:60px}}.note{{color:#555;font-size:14px}}li{{margin-bottom:6px}}</style></head><body>
<h1>Pacote de Produção: Maitê Proença</h1>
<p><b>Título:</b> {html.escape(TITLE)}</p>
<h2>Descrição (SEO)</h2><pre>{html.escape(DESC)}</pre>
<h2>Tags</h2><pre>{html.escape(TAGS)}</pre><p class="note">{len(TAGS)} caracteres (limite do YouTube: 500).</p>
<h2>Capítulos (colar na descrição)</h2><pre>{chap}</pre>
<p class="note">Tempos calculados a 195 palavras por minuto (~{round(w/195)} min no total). Ajuste pelo áudio real depois de gravar.</p>
<h2>Lista de imagens para o editor</h2><table>{rows}</table>
<h2>Cuidados na edição (monetização e pessoas vivas)</h2><ul>
<li>Nada de imagens gráficas: sem faca, sangue ou reconstituição do crime. Use objetos, portas e sombras.</li>
<li>Suicídio (pai e Zuza): não mostrar método nem arma; deixar o CVV 188 na tela no fim e na descrição.</li>
<li>Abuso aos 10 anos e aborto: só narração, sem imagens ilustrativas explícitas.</li>
<li>Maitê, Paulo Marinho, Flávio Bolsonaro e Adriana Calcanhotto estão vivos: usar só declarações públicas e fotos licenciadas ou de divulgação, com crédito.</li>
<li>René (irmão) e Maria (filha): não mostrar o rosto; netas nunca.</li>
<li>Placar dos júris (7x0/4x3): uma fonte fala em 6x1 em 1975. Se não confirmar, tire o letreiro com os números.</li>
<li>Trechos de novelas, Faustão, Roda Viva e Provoca: curtos e com crédito (Globo, Manchete, TV Cultura).</li>
<li>Capa da Playboy: recorte que não mostre nudez.</li>
<li>Thumbnail: usar foto real licenciada na silhueta; não gerar o rosto dela com IA.</li>
</ul>
<h2>Thumbnails</h2><p>Thumb1_ELA_DEFENDEU_O_PAI.jpg · Thumb2_ELE_FOI_ABSOLVIDO.jpg (na mesma pasta). As silhuetas são espaço para as fotos reais.</p>
</body></html>''')
# chapters
CH=[('R: Maitê Proença tinha doze anos','O crime que a Justiça perdoou','Maitê em Dona Beija (arquivo, com crédito) × silhueta de menina num tribunal · Texto: "ELA DEFENDEU O PAI"'),
('Maitê Proença Gallo nasceu','A família perfeita','Campinas anos 60 (arquivo) · Piano de cauda · Livro de Shakespeare aberto em Macbeth (ilustrativo)'),
('Agosto de mil novecentos e setenta.','O revólver','Revólver antigo sobre mesa (1.º objeto, ilustrativo) · Casa de classe alta dos anos 70 à noite'),
('Sábado, sete de novembro de mil novecentos e setenta.','O sábado de novembro','Porta de quarto fechada (2.º objeto, ilustrativo) · Recortes de jornal de 1970 (com crédito)'),
('Durante dez dias, Augusto ficou foragido.','Dez dias foragido','Delegacia anos 70 (ilustrativo) · Manchetes da época'),
('Maitê e o irmão foram mandados','O pensionato luterano','Dormitório de internato antigo · Igreja de Campinas · Mão sobre a orelha de uma criança (ilustrativo)'),
('Para entender aquele tribunal','A carta rasgada','Agência dos Correios antiga · Carta rasgada (4.º objeto, ilustrativo)'),
('O processo contra Augusto','O juiz amigo e o príncipe dos advogados','Fórum de Campinas (fachada) · Martelo de juiz · Foto de arquivo de Waldir Troncoso Peres (com crédito)'),
('O argumento tinha nome','Legítima defesa da honra','Letreiro "LEGÍTIMA DEFESA DA HONRA" · Tribunal do júri vazio · Papel de depoimento datilografado (3.º objeto)'),
('O primeiro júri se reuniu em Campinas.','Absolvido duas vezes','Placar 7x0 e 4x3 em letreiro · Porta do fórum com multidão (ilustrativo)'),
('Depois do crime, segundo Maitê','O manicômio e o padre','Corredor de hospital psiquiátrico antigo (ilustrativo) · Casa paroquial'),
('Pouco tempo depois, Maitê foi embora','Sozinha em Paris','Paris anos 70 · Rua com chuva, adolescente de costas (ilustrativo)'),
('Paris foi só o começo da estrada.','40 países de carona','Estrada na Índia/África anos 70 · Mochileiros pedindo carona · Moeda de 1 dólar'),
('Um homem parou Maitê','O aviso na Índia','Mão segurando outra mão · Mercado indiano · Letreiro com a frase do homem'),
('Em mil novecentos e setenta e nove, estreou','A estreia na TV','Dinheiro Vivo e As Três Marias (arquivo, com crédito) · Raio X de fêmur (ilustrativo)'),
('Mil novecentos e oitenta e seis.','Dona Beija e a Playboy','Cena de Dona Beija (trecho curto, com crédito) · Capa da Playboy de 1987 (5.º objeto) com recorte discreto'),
('E o pai?','O pedido do pai','Quarto de hospital com aparelhos (ilustrativo) · Letreiro "desligue os aparelhos"'),
('A: Zuza, o irmão mais velho','Dois enterros no mesmo ano','Duas velas acesas · Janela de casa vista de fora (ilustrativo)'),
('No ano seguinte, em mil novecentos e noventa','Maria, a pensão e a Justiça','Bebê (ilustrativo) · Manchetes sobre a pensão (Conjur, 2010) · Valor R$ 254 mil em letreiro'),
('Dois mil e cinco.','Exposta no Faustão','Palco de auditório (ilustrativo) · Frase "Fiquei muito chocada" em letreiro'),
('Um ano depois do livro','Portugal e Haiti','Mosteiro dos Jerônimos, Lisboa · Tendas no Haiti pós-terremoto (arquivo, com crédito)'),
('Num texto publicado no próprio site','A frase perturbadora','Tela de site com a crônica (print, com crédito) · Palavra "JUNTOS" em letreiro'),
('A legítima defesa da honra continuou','Doca Street e o STF','Ângela Diniz/Búzios (arquivo) · Cartaz "Quem ama não mata" · Plenário do STF 01/08/2023'),
('Em agosto de dois mil e vinte e quatro','O preço no corpo','Cavalo, moto e escada (ilustrativo, sem acidente) · Sala acolchoada (ilustrativo)'),
('Veio a pandemia, e os teatros fecharam.','O Pior de Mim','Teatro vazio · Cartaz/fotos oficiais da peça (com crédito)'),
('Em dois mil e vinte, o pai da filha dela','Novos capítulos','Manchetes Paulo Marinho × Flávio (2020) · Maitê e Adriana Calcanhotto (só fotos públicas)'),
('A casa da avenida','A casa virou loja','Fachada da loja atual em Nova Campinas · Sítio com horta e cachoeira'),
('Agora junte todas as peças','O perdão','Montagem dos 5 objetos: revólver, porta, depoimento, carta, capa de revista · Porta se abrindo para a luz'),
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
DESC='''Aos 12 anos, Maitê Proença viu o pai matar a mãe e, no tribunal, ficou do lado dele. Ele foi absolvido duas vezes pela "legítima defesa da honra". Depois vieram mais duas mortes, a fama e um segredo exposto na TV.

Se você está passando por um momento difícil, ligue 188 (CVV).

#MaitêProença #LegítimaDefesaDaHonra #DonaBeija'''
TAGS='maitê proença, maite proenca, maitê proença mãe, maitê proença pai, maitê proença história, maitê proença hoje, o que aconteceu com maitê proença, margot proença gallo, legítima defesa da honra, dona beija, maitê proença faustão, o pior de mim, crimes que chocaram o brasil, maitê proença vida'
rows=''.join(f'<tr><td class="t">{t}</td><td><b>{html.escape(n)}</b><br>{html.escape(i)}</td></tr>\n' for t,n,i in out)
chap=html.escape('\n'.join(f'{t} {n}' for t,n,_ in out))
open('MaiteProenca_Pacote_Producao.html','w').write(f'''<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Pacote de Produção — Maitê Proença</title>
<style>body{{background:#fff;color:#111;font-family:system-ui,Segoe UI,Arial,sans-serif;max-width:860px;margin:0 auto;padding:24px 16px;line-height:1.55}}h1{{font-size:24px}}h2{{font-size:19px;margin-top:32px;border-bottom:2px solid #eee;padding-bottom:4px}}pre{{white-space:pre-wrap;background:#f6f6f6;padding:12px;border-radius:6px;font-family:inherit}}table{{width:100%;border-collapse:collapse}}td{{border-bottom:1px solid #eee;padding:8px;vertical-align:top}}td.t{{font-weight:700;white-space:nowrap;width:60px}}.note{{color:#555;font-size:14px}}li{{margin-bottom:6px}}</style></head><body>
<h1>Pacote de Produção: Maitê Proença</h1>
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
