import re, html
TITLE="RENATO ARAGÃO: O Lado REPUGNANTE do Didi Que a Globo Escondeu Por 44 Anos"
files=['parte1.txt','parte2.txt','parte3.txt','parte4.txt','parte5.txt']
paras=[]
for f in files:
    for p in open(f).read().split('\n\n'):
        p=p.strip()
        if p: paras.append(re.sub(r'^[RA]: ','',p))
# voice html
body=''.join(f'<p>{html.escape(p)}</p>\n' for p in paras)
open('RenatoAragao_Roteiro_Voz.html','w').write(f'''<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(TITLE)}</title>
<style>body{{background:#fff;color:#000;font-family:Georgia,serif;font-size:20px;line-height:1.7;max-width:760px;margin:0 auto;padding:32px 16px}}h1{{font-size:24px;line-height:1.3;margin-bottom:32px}}p{{margin:0 0 18px}}</style>
</head><body>
<h1>{html.escape(TITLE)}</h1>
{body}</body></html>''')
# chapters
CH=[('R: Renato Aragão fez o Brasil rir','O lado que ninguém viu','Didi sorrindo (arquivo, com crédito) × silhueta escura nos bastidores · Texto: "O LADO QUE A GLOBO ESCONDEU"'),
('Agosto de dois mil e dezoito.','O documentário proibido','Rolo de filme/HD com cadeado (1.º objeto, ilustrativo) · Letreiro "70 horas · 62 depoimentos"'),
('Treze de janeiro de mil novecentos e trinta e cinco.','O advogado de Sobral','Sobral anos 40 (arquivo) · Diploma de Direito (ilustrativo)'),
('A virada veio pela televisão.','Nasce o Didi','TV Ceará anos 60 (arquivo) · Os Adoráveis Trapalhões (arquivo, com crédito)'),
('Mil novecentos e setenta e quatro.','Os quatro Trapalhões','Fotos de divulgação do quarteto (licenciadas) · Logo antigo da Globo'),
('Mil novecentos e oitenta e três.','O cartaz','Cartaz de "O Cangaceiro Trapalhão" (2.º objeto, com crédito)'),
('Todos os negócios do grupo','82% contra 6%','Contrato antigo com números em destaque (3.º objeto, ilustrativo) · Letreiro "82% × 6%"'),
('Agosto de mil novecentos e oitenta e três.','A coletiva do Teatro Fênix','Fachada de teatro antigo · Microfones de coletiva anos 80 (ilustrativo)'),
('A separação virou uma guerra','Guerra e reconciliação','Cartazes de "O Trapalhão na Arca de Noé" e "Atrapalhando a Suate" (com crédito) · Mesa de almoço'),
('Mil novecentos e oitenta e cinco.','O contrato depois das pazes','Letreiro "79% × 7%" · Cartaz de "Os Trapalhões no Reino da Fantasia"'),
('Mil novecentos e oitenta e seis.','O rosto da solidariedade','Criança Esperança (trechos curtos, com crédito) · Telefone de doação'),
('Dois mil e doze.','As primeiras rachaduras','Manchetes do jornal Extra (recorte) · Frase "vai pagar muito caro" em letreiro'),
('Trinta de junho de dois mil e vinte.','O fim na Globo','Post de Instagram (print, com crédito) · Fachada da Globo'),
('A filha se chamava Juliana','A filha motorista','Carro de aplicativo à noite (ilustrativo, sem rosto) · Página de vaquinha genérica (4.º objeto, sem dados pessoais)'),
('Para entender o que o documentário conta sobre esses','Zacarias e Mussum','Fotos de Zacarias e Mussum (arquivo, com crédito)'),
('Dezoito de março de mil novecentos e noventa.','Dois golpes','Manchetes de 1990 e 1994 (com crédito) · Duas velas'),
('José Lavigne foi diretor','O dono do programa','Frase "dono de programa não rouba, ele pega" em letreiro · Estúdio vazio'),
('Os três parceiros tinham acabado','A frase e a cadeira','Cadeira vazia nos bastidores com bananas (5.º objeto, ilustrativo) · Letreiro "NÃO PRECISO DELES"'),
('Andréa Sorvetão foi paquita','O processo de 2026','Manchete do Metrópoles (print, com crédito) · Martelo de juiz'),
('Em janeiro de dois mil e vinte e seis, Renato Aragão','Os dois últimos Trapalhões','Renato e Dedé no Caldeirão (trecho curto, com crédito)'),
('Agora junte todas as peças.','O preço da fama','Montagem dos 5 objetos: documentário, cartaz, contrato, vaquinha, cadeira'),
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
DESC='''Renato Aragão fez o Brasil rir por mais de 50 anos. Mas contratos, depoimentos de bastidores e um documentário que nenhuma plataforma quis exibir contam outra história: 82% contra 6%, a filha que fez vaquinha e o que viviam Mussum e Zacarias.

#RenatoAragão #OsTrapalhões #Didi'''
TAGS='renato aragão, didi, os trapalhões, renato aragão polêmica, renato aragão filha, renato aragão mussum, renato aragão zacarias, dedé santana, trapalhões documentário, renato aragão globo, o que aconteceu com renato aragão, trapalhões contratos, renato aragão hoje, mussum'
rows=''.join(f'<tr><td class="t">{t}</td><td><b>{html.escape(n)}</b><br>{html.escape(i)}</td></tr>\n' for t,n,i in out)
chap=html.escape('\n'.join(f'{t} {n}' for t,n,_ in out))
open('RenatoAragao_Pacote_Producao.html','w').write(f'''<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Pacote de Produção — Renato Aragão</title>
<style>body{{background:#fff;color:#111;font-family:system-ui,Segoe UI,Arial,sans-serif;max-width:860px;margin:0 auto;padding:24px 16px;line-height:1.55}}h1{{font-size:24px}}h2{{font-size:19px;margin-top:32px;border-bottom:2px solid #eee;padding-bottom:4px}}pre{{white-space:pre-wrap;background:#f6f6f6;padding:12px;border-radius:6px;font-family:inherit}}table{{width:100%;border-collapse:collapse}}td{{border-bottom:1px solid #eee;padding:8px;vertical-align:top}}td.t{{font-weight:700;white-space:nowrap;width:60px}}.note{{color:#555;font-size:14px}}li{{margin-bottom:6px}}</style></head><body>
<h1>Pacote de Produção: Renato Aragão</h1>
<p><b>Título:</b> {html.escape(TITLE)}</p>
<h2>Descrição (SEO)</h2><pre>{html.escape(DESC)}</pre>
<h2>Tags</h2><pre>{html.escape(TAGS)}</pre><p class="note">{len(TAGS)} caracteres (limite do YouTube: 500).</p>
<h2>Capítulos (colar na descrição)</h2><pre>{chap}</pre>
<p class="note">Tempos calculados a 195 palavras por minuto (~{round(w/195)} min no total). Ajuste pelo áudio real depois de gravar.</p>
<h2>Lista de imagens para o editor</h2><table>{rows}</table>
<h2>Cuidados na edição (Renato está vivo e processa)</h2><ul>
<li>Toda acusação vem com a fonte na tela: "segundo Victor Lustosa", "segundo a camareira", "segundo Rafael Spaca". Nunca letreiro afirmando que ele é racista.</li>
<li>Nada de trechos do documentário "Trapalhadas Sem Fim" (não foi lançado; os direitos são do diretor).</li>
<li>Juliana: não mostrar rosto, placa do carro, nome da namorada nem a página real da vaquinha. Usar só ilustrações.</li>
<li>Zacarias: o boato de aids aparece só como boato, sempre com a negativa da ex-mulher.</li>
<li>Trechos de TV (Globo, Viva, Caldeirão, SBT): curtos e com crédito.</li>
<li>Thumbnail: foto real licenciada na silhueta; não gerar o rosto dele com IA.</li>
</ul>
<h2>Thumbnails</h2><p>Thumb1_82_PRA_ELE.jpg · Thumb2_O_LADO_QUE_A_GLOBO_ESCONDEU.jpg (na mesma pasta). As silhuetas são espaço para as fotos reais.</p>
</body></html>''')
