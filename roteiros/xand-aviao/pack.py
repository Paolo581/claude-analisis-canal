import re, html
TITLE="O Que ACONTECEU com XAND AVIÃO? A Verdade CRUEL Por Trás do Fim do Aviões do Forró"
files=['parte1.txt','parte2.txt','parte3.txt','parte4.txt','parte5.txt']
paras=[]
for f in files:
    for p in open(f).read().split('\n\n'):
        p=p.strip()
        if p: paras.append(re.sub(r'^[RA]: ','',p))
# voice html
body=''.join(f'<p>{html.escape(p)}</p>\n' for p in paras)
open('XandAviao_Roteiro_Voz.html','w').write(f'''<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(TITLE)}</title>
<style>body{{background:#fff;color:#000;font-family:Georgia,serif;font-size:20px;line-height:1.7;max-width:760px;margin:0 auto;padding:32px 16px}}h1{{font-size:24px;line-height:1.3;margin-bottom:32px}}p{{margin:0 0 18px}}</style>
</head><body>
<h1>{html.escape(TITLE)}</h1>
{body}</body></html>''')
# chapters
CH=[('R: Xand Avião era a voz','O fim que o Brasil não viu','Xand no palco (foto de imprensa, com crédito) × ônibus de banda vazio à noite · Texto: "A VERDADE CRUEL"'),
('Vinte e oito de fevereiro de dois mil e dezessete.','A última noite','Palco de Carnaval à noite em Luís Correia (ilustrativo) · Foto do último show Xand e Solange (imprensa, com crédito)'),
('Vinte e quatro de março de mil novecentos e oitenta e dois.','O menino de Exu','Sertão de Itaú/Exu (imagens de arquivo) · Violão simples em cadeira de madeira (2.º objeto, ilustrativo) · Luiz Gonzaga (arquivo, com crédito)'),
('Dois mil e dois.','Fortaleza','Fortaleza anos 2000 (arquivo) · Placa "Aviões do Forró" (ilustrativo)'),
('Agosto de dois mil e dois.','Nasce o Aviões','Capa do 1.º CD (com crédito) · Letreiros "200 mil / 500 mil / 700 mil cópias"'),
('Em dois mil e seis, parte desses empresários','A3 Entretenimento','Organograma ilustrativo: rádios, casas de show, bandas · Fachadas de casas de forró (arquivo)'),
('Dois mil e dez.','O contrato de 2010','Contrato antigo com cláusula destacada (3.º objeto, ilustrativo, sem nomes reais)'),
('Dois mil e onze.','O auge e a guerra do forró','Trechos curtos de TV (com crédito) · Letreiro "guerra silenciosa"'),
('Em dois mil e quinze','A proposta recusada','Xand e Solange em palco (arquivo, com crédito) · Letreiro "Eu não senti segurança"'),
('Dezoito de outubro de dois mil e dezesseis.','Operação For All','Viaturas da PF ao amanhecer (arquivo genérico) · Letreiros "260 policiais · 76 mandados · R$ 500 milhões"'),
('Numa das empresas do grupo','R$ 600 mil em dinheiro vivo','Maço de dinheiro sobre mesa (ilustrativo) · Letreiro "163 imóveis bloqueados"'),
('A: Entre os nomes','Os vocalistas na PF','Fachada da sede da PF em Fortaleza (arquivo) · Letreiro "conduzidos para depor · liberados · à disposição da Justiça"'),
('Três de maio de dois mil e dezenove.','Carreira solo','DVD "Errejota" (capa, com crédito) · Rio de Janeiro, Baía de Guanabara'),
('Junho de dois mil e dezenove.','A investigação do MPF','Pasta com carimbo "INQUÉRITO" (4.º objeto, ilustrativo) · Letreiro "ARQUIVADO POR FALTA DE PROVAS" sempre junto'),
('Quando o processo de Solange chegou à Justiça','R$ 5 milhões × R$ 17 milhões','Martelo de juiz · Letreiros "R$ 5 mi × R$ 17 mi → R$ 500 mil"'),
('Março de dois mil e vinte.','Pandemia e acusações','Letreiro "457 t × 80 t (segundo Leo Dias)" · Estúdio de live vazio'),
('Agosto de dois mil e vinte e um. Dia dos Pais.','Os filhos e o pai','Print da postagem SEM rosto dos filhos (desfocado) · Casa simples no sertão (ilustrativo)'),
('Sete de dezembro de dois mil e vinte e um.','O abraço','Reencontro na Farofa da Gkay (trecho curto, com crédito)'),
('Naquele mesmo ano de dois mil e vinte e um','De cantor a empresário','Logo genérico de produtora (sem marca real) · Escritório'),
('Sete de junho de dois mil e vinte e cinco.','R$ 700 mil em Mossoró','Multidão de São João (arquivo) · Letreiro "R$ 700 mil · MP Eleitoral apura"'),
('A: Dezenove de janeiro de dois mil e vinte e seis.','O quarto de hotel','Corredor de hotel e porta fechada (5.º objeto, ilustrativo) · Trecho curto do Sem Censura (com crédito)'),
('Agora junte todas as peças.','O preço da fama','Montagem dos 5 objetos: tatuagem, violão, contrato, pasta, quarto de hotel'),
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
DESC='''Xand Avião era a voz do maior fenômeno do forró brasileiro. Mas por trás do fim do Aviões do Forró existem uma operação da Polícia Federal, uma investigação do MPF, um processo de milhões e um quarto de hotel onde, segundo Solange Almeida, a despedida teve roteiro pronto.

Todas as acusações citadas neste vídeo são apresentadas com as respectivas fontes e as versões de defesa. Até onde se sabe, Xand Avião não foi condenado por nenhum dos crimes investigados.

#XandAvião #AviõesDoForró #SolangeAlmeida'''
TAGS='xand avião, aviões do forró, solange almeida, fim do aviões do forró, xand e solange, xand avião polêmica, operação for all, a3 entretenimento, xand avião história, solange almeida sem censura, o que aconteceu com xand avião, forró, vybbe, xand avião solange briga'
rows=''.join(f'<tr><td class="t">{t}</td><td><b>{html.escape(n)}</b><br>{html.escape(i)}</td></tr>\n' for t,n,i in out)
chap=html.escape('\n'.join(f'{t} {n}' for t,n,_ in out))
open('XandAviao_Pacote_Producao.html','w').write(f'''<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Pacote de Produção — Xand Avião</title>
<style>body{{background:#fff;color:#111;font-family:system-ui,Segoe UI,Arial,sans-serif;max-width:860px;margin:0 auto;padding:24px 16px;line-height:1.55}}h1{{font-size:24px}}h2{{font-size:19px;margin-top:32px;border-bottom:2px solid #eee;padding-bottom:4px}}pre{{white-space:pre-wrap;background:#f6f6f6;padding:12px;border-radius:6px;font-family:inherit}}table{{width:100%;border-collapse:collapse}}td{{border-bottom:1px solid #eee;padding:8px;vertical-align:top}}td.t{{font-weight:700;white-space:nowrap;width:60px}}.note{{color:#555;font-size:14px}}li{{margin-bottom:6px}}</style></head><body>
<h1>Pacote de Produção: Xand Avião</h1>
<p><b>Título:</b> {html.escape(TITLE)}</p>
<h2>Descrição (SEO)</h2><pre>{html.escape(DESC)}</pre>
<h2>Tags</h2><pre>{html.escape(TAGS)}</pre><p class="note">{len(TAGS)} caracteres (limite do YouTube: 500).</p>
<h2>Capítulos (colar na descrição)</h2><pre>{chap}</pre>
<p class="note">Tempos calculados a 195 palavras por minuto (~{round(w/195)} min no total). Ajuste pelo áudio real depois de gravar.</p>
<h2>Lista de imagens para o editor</h2><table>{rows}</table>
<h2>Cuidados na edição (Xand está vivo: risco jurídico alto)</h2><ul>
<li>Toda acusação com a fonte na tela: "segundo a PF", "segundo o MPF", "segundo Leo Dias", "segundo Solange", "segundo a imprensa local".</li>
<li>Investigação do MPF (homicídio, tráfico etc.): sempre junto do letreiro "arquivado por falta de provas; banda nega". Nunca letreiro afirmando crime.</li>
<li>Operação For All: "investigação, sem julgamento". Não usar a palavra "sonegador" nem "criminoso" em letreiros.</li>
<li>Filhos: não mostrar rostos dos filhos (principalmente menores) nem a postagem original legível.</li>
<li>Trechos de TV (Sem Censura, Rede TV, Band, Fantástico, Farofa): curtos e com crédito.</li>
<li>Músicas do Aviões/Xand: não usar como trilha (Content ID); só trechos muito curtos, se necessário.</li>
<li>Thumbnail: sem rosto gerado por IA do Xand ou da Solange; usar foto real licenciada ou silhueta. Nada de "CRIMINOSO" ou "PRESO".</li>
</ul>
<h2>Thumbnails</h2><p>Thumb1_FOI_OBRIGADA_A_MENTIR.jpg · Thumb2_A_BANDA_FOI_EMBORA.jpg (na mesma pasta). Só silhuetas, sem rostos reais. A frase da Thumb1 resume a versão da própria Solange ("eu tive que dizer… tive que seguir o roteiro").</p>
</body></html>''')
