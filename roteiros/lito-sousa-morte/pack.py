import re, html
TITLE="LITO SOUSA: Os 40 Dias CRUÉIS Entre o Diagnóstico e a Morte"
files=['parte1.txt','parte2.txt','parte3.txt','parte4.txt','parte5.txt']
paras=[]
for f in files:
    for p in open(f).read().split('\n\n'):
        p=p.strip()
        if p: paras.append(re.sub(r'^[RA]: ','',p))
# voice html
body=''.join(f'<p>{html.escape(p)}</p>\n' for p in paras)
open('LitoSousa40_Roteiro_Voz.html','w').write(f'''<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(TITLE)}</title>
<style>body{{background:#fff;color:#000;font-family:Georgia,serif;font-size:20px;line-height:1.7;max-width:760px;margin:0 auto;padding:32px 16px}}h1{{font-size:24px;line-height:1.3;margin-bottom:32px}}p{{margin:0 0 18px}}</style>
</head><body>
<h1>{html.escape(TITLE)}</h1>
{body}</body></html>''')
# chapters
CH=[('R: Lito Sousa passou','O último voo','Foto real licenciada de Lito no canal × céu ao entardecer com avião subindo · Texto: "40 DIAS"'),
('O nome dele era Joselito','O mecânico','Hangar e manutenção de aeronaves (banco de imagens) · Capa de "Onde Morrem os Aviões" (com crédito)'),
('Em dois mil e dez, Lito levou','Aviões e Músicas','Prints do canal (com crédito) · Letreiro "4 milhões de inscritos"'),
('O primeiro aviso veio','O primeiro aviso','Corredor de hospital desfocado (ilustrativo, sem pacientes)'),
('Dezenove de julho','"Estou em manutenção, não em queda"','Trecho curto do vídeo de 19/07 (com crédito) · Close ilustrativo de mão/braço · Letreiro com a frase'),
('No dia seguinte, vinte de julho','Einstein','Fachada do Einstein (arquivo) · Letreiro "inflamação no sistema nervoso central"'),
('Vinte e um de agosto','O diagnóstico','Trecho curto do vídeo de Mila (com crédito) · Animação simples de proteínas se deformando'),
('Mila não ficou esperando.','"Preciso salvar o amor da minha vida"','Print do comentário (com crédito) · Letreiro do Ministério da Saúde'),
('As respostas dos laboratórios','As portas se fecham','Letreiros: Ionis × Broad Institute × Harvard "20 de outubro"'),
('Primeiro de setembro','Em casa','Quarto com luz suave (ilustrativo) · Letreiro "Eu vou ser o primeiro..."'),
('Enquanto Lito estava em casa','O frasco','Frasco de laboratório (ilustrativo) · Letreiro "ALN-6457"'),
('O ALN-6457 vinha','Testado só em animais','Laboratório (banco de imagens) · Letreiro "fase pré-clínica"'),
('Sexta-feira, quatro de setembro','A Anvisa','Fachada da Anvisa (arquivo) · Trecho curto do vídeo de 04/09 só se público e com crédito (evitar close do sofrimento)'),
('Madrugada de doze de setembro','A madrugada em Guarulhos','Aeroporto à noite (arquivo) · Helicóptero sobre São Paulo (arquivo/ilustrativo)'),
('A caixa chegou ao hospital','A primeira dose','Seringa/frasco (ilustrativo) · Letreiro "1.º ser humano do mundo"'),
('Por volta de vinte e um de setembro','O carro','Carro com placa "vende-se" (ilustrativo, sem modelo real da família)'),
('Começou a circular um boato','O relógio que não existia','Letreiro "R$ 700 mil?" riscado · Comentários desfocados'),
('Os médicos tinham alertado','"Perdi o direito de adoecer"','Mulher de costas numa janela de hospital (ilustrativo, sem rosto)'),
('Vinte e três de setembro','Duas velocidades','Letreiro com a fala de Mila · Gráfico simples de duas linhas'),
('Nos dias seguintes, começou a circular','A notícia falsa','Print de post falso borrado com selo "FALSO"'),
('A: Vinte e cinco de setembro','"Zero"','Letreiro "ZERO" em tela preta'),
('A: Segunda-feira, vinte e oito','O vídeo feito por máquina','Trecho curto do vídeo com o aviso "feito com IA" visível (com crédito)'),
('A reação dividiu os fãs','Bonito ou desrespeitoso','Comentários dos dois lados (desfocados)'),
('Quinta-feira, primeiro de outubro','1º de outubro','Céu ao entardecer · Letreiro "1º/10/2026"'),
('Mila começa falando','"Olhe para o céu"','Trecho do vídeo de despedida (com crédito) · Letreiros com as frases'),
('O livro que Lito escreveu','Onde morrem os aviões','Capa do livro (com crédito)'),
('Mila escreveu, no meio','O tempo','Relógio, calendário · Céu com avião ao longe no final'),
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
DESC='''Lito Sousa, do canal Aviões e Músicas, morreu em 1º de outubro de 2026, aos 59 anos, cerca de 40 dias depois de a família anunciar o diagnóstico da doença de Creutzfeldt-Jakob. Neste vídeo: o sinal que apareceu no vídeo de julho, a corrida da esposa Mila Seidl por um tratamento, a madrugada em que o remédio experimental ALN-6457 chegou de helicóptero ao Einstein, os ataques e a notícia falsa nas redes e a despedida que emocionou o Brasil.

Nossos sentimentos à Mila, ao Malone e a toda a família.

#LitoSousa #AviõesEMúsicas'''
TAGS='lito sousa, lito sousa morre, morte de lito sousa, aviões e músicas, lito sousa doença, creutzfeldt-jakob, mila seidl, lito sousa remédio, aln-6457, lito sousa despedida, lito sousa 59 anos, assim foi a vida'
rows=''.join(f'<tr><td class="t">{t}</td><td><b>{html.escape(n)}</b><br>{html.escape(i)}</td></tr>\n' for t,n,i in out)
chap=html.escape('\n'.join(f'{t} {n}' for t,n,_ in out))
open('LitoSousa40_Pacote_Producao.html','w').write(f'''<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Pacote de Produção — Lito Sousa 40 dias</title>
<style>body{{background:#fff;color:#111;font-family:system-ui,Segoe UI,Arial,sans-serif;max-width:860px;margin:0 auto;padding:24px 16px;line-height:1.55}}h1{{font-size:24px}}h2{{font-size:19px;margin-top:32px;border-bottom:2px solid #eee;padding-bottom:4px}}pre{{white-space:pre-wrap;background:#f6f6f6;padding:12px;border-radius:6px;font-family:inherit}}table{{width:100%;border-collapse:collapse}}td{{border-bottom:1px solid #eee;padding:8px;vertical-align:top}}td.t{{font-weight:700;white-space:nowrap;width:60px}}.note{{color:#555;font-size:14px}}li{{margin-bottom:6px}}</style></head><body>
<h1>Pacote de Produção: Lito Sousa (40 dias)</h1>
<p><b>Título:</b> {html.escape(TITLE)}</p>
<h2>Descrição (SEO)</h2><pre>{html.escape(DESC)}</pre>
<h2>Tags</h2><pre>{html.escape(TAGS)}</pre><p class="note">{len(TAGS)} caracteres (limite do YouTube: 500).</p>
<h2>Capítulos (colar na descrição)</h2><pre>{chap}</pre>
<p class="note">Tempos calculados a 195 palavras por minuto (~{round(w/195)} min no total). Ajuste pelo áudio real depois de gravar.</p>
<h2>Lista de imagens para o editor</h2><table>{rows}</table>
<h2>Cuidados na edição</h2><ul>
<li>Morte recente, com viúva e filho de 7 anos: nada de imagens de sofrimento, hospital com paciente ou close do Lito doente.</li>
<li>Vídeo de 04/09 e vídeo de IA: usar só trechos curtos, com crédito; no vídeo de IA, manter o aviso "feito com IA" visível.</li>
<li>Remédio: tratar como tentativa experimental. Nunca sugerir que o remédio causou a morte.</li>
<li>Ataques a Mila: mostrar comentários desfocados, sem nome de usuários.</li>
<li>Falas entre aspas: são as de Mila e Lito publicadas na imprensa; manter exatamente como no roteiro.</li>
<li>Thumbnail: foto real licenciada; nunca rosto gerado por IA (o próprio caso tem um vídeo de IA, o que torna isso ainda mais sensível).</li>
</ul>
<h2>Thumbnails</h2><p><b>Thumb1_O_ULTIMO_VOO_DELE.jpg</b> (recomendada): piloto em silhueta na cabine ao amanhecer × pista ao entardecer com avião subindo. <b>Thumb2_40_DIAS.jpg</b>: frasco "ALN-6457" × helicóptero sobre a cidade à noite, com "TESTADO SÓ EM ANIMAIS". Ambas sem rosto; se quiser o rosto do Lito, use só foto real licenciada.</p>
</body></html>''')
