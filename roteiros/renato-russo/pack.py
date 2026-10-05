import re, html, json
TITLE="Assim FOI a VIDA de RENATO RUSSO — Por que o Seu Legado Está Sumindo?"
files=['parte1.txt','parte2.txt','parte3.txt','parte4.txt','parte5.txt']
raw=[p.strip() for f in files for p in open(f).read().split('\n\n') if p.strip()]
paras=[re.sub(r'^[RA]: ','',p) for p in raw]
open('voz.txt','w').write('\n\n'.join(paras)+'\n')
open('roteiro_completo.txt','w').write('\n\n'.join(raw)+'\n')
W=sum(len(p.split()) for p in paras)
body=''.join(f'<p>{html.escape(p)}</p>\n' for p in paras)
open('Renato_Roteiro_Voz.html','w').write(f'''<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(TITLE)}</title>
<style>body{{background:#fff;color:#000;font-family:Georgia,serif;font-size:20px;line-height:1.7;max-width:760px;margin:0 auto;padding:32px 16px}}h1{{font-size:24px;line-height:1.3;margin-bottom:32px}}p{{margin:0 0 18px}}</style>
</head><body>
<h1>{html.escape(TITLE)}</h1>
{body}</body></html>''')
CH=[('Renato Russo morreu há quase trinta anos.','As 91 fitas apreendidas','Fachada genérica de depósito à noite (ilustrativo) · Letreiro "91 FITAS"'),
('Para entender como a obra','O garoto na cama','Quarto de adolescente anos 70, cama e cadernos (ilustrativo)'),
('Renato não tinha nascido em Brasília.','Rio, Nova York e Brasília','Fotos de época de Brasília nos anos 70 (arquivo, com crédito)'),
('Em mil novecentos e setenta e oito, Renato finalmente','Aborto Elétrico','Fotos da cena punk de Brasília (arquivo, com crédito)'),
('Ainda em mil novecentos e oitenta e dois, Renato chamou','Nasce a Legião Urbana','Fotos de imprensa da Legião nos anos 80 (com crédito)'),
('Em mil novecentos e oitenta e quatro, a Legião assinou','A dor escondida','Estúdio de gravação vazio, baixo encostado (ilustrativo; sem mostrar ferimentos)'),
('Dezoito de junho de mil novecentos e oitenta e oito.','A noite do Mané Garrincha','Fotos/vídeo de arquivo do show de 1988 (com crédito) · Letreiros "400 feridos · 64 ônibus"'),
('Em mil novecentos e oitenta e nove, nasceu Giuliano','O filho e As Quatro Estações','Capa do disco As Quatro Estações (com crédito)'),
('Mil novecentos e noventa.','O papel do exame','Envelope de laboratório fechado sobre a mesa (ilustrativo)'),
('Em mil novecentos e noventa e dois, os boatos','A pergunta do jornalista','Gravador de fita e microfone de entrevista (ilustrativo)'),
('Cazuza.','O medo de virar capa','Pilha de revistas antigas sem capa identificável (ilustrativo)'),
('Renato bebia muito. Usava drogas.','A clínica e os discos solo','Corredor de clínica vazio · capas de Stonewall e Equilíbrio Distante (com crédito)'),
('Catorze de janeiro de mil novecentos e noventa e cinco.','O último show','Palco pequeno com luzes acesas e lata no chão (ilustrativo)'),
('O papel que Renato recebeu','O segredo de seis anos','Letreiro "HIV POSITIVO · 1990" sobre fundo escuro'),
('Nessa época, Renato morava','O pedido ao pai','Janela de apartamento em Ipanema à noite (ilustrativo)'),
('Sexta-feira, onze de outubro de mil novecentos e noventa e seis.','A madrugada de 11 de outubro','Relógio marcando 1h15 · capa de A Tempestade (com crédito)'),
('Carminha sabia que o filho tinha morrido.','A mãe e a televisão','TV de tubo ligada numa sala escura (ilustrativo, sem imagem de telejornal real)'),
('Outubro de mil novecentos e noventa e seis.','O herdeiro de sete anos','Gaveta aberta com fitas cassete e cadernos (ilustrativo)'),
('Em mil novecentos e noventa e sete, os avós','A guerra pela guarda','Fachada do STJ (arquivo) · Letreiro "2004 · unanimidade"'),
('Aos dezoito anos, Giuliano','A empresa e a família','Letreiro "48 imóveis · Jornal de Brasília"'),
('Dado Villa-Lobos e Marcelo Bonfá.','Dado e Bonfá contra o herdeiro','Fotos de imprensa de Dado e Bonfá (com crédito)'),
('Vinte e nove de junho de dois mil e vinte e um.','3 a 2 no STJ','Martelo de juiz · Letreiro "3 x 2"'),
('Outubro de dois mil e vinte e um.','A série proibida','Tela de streaming com aviso "indisponível" (genérico, sem logotipo)'),
('Vinte e quatro de outubro de dois mil e vinte e três.','Os 20 milhões','Planilhas e notas de dinheiro (ilustrativo) · Letreiro "R$ 20 MILHÕES · sob sigilo"'),
('A história das fitas começa na internet.','Operação Será','Tela de celular com perfil borrado · Letreiro "30 músicas inéditas"'),
('Nove de dezembro de dois mil e vinte.','Operação Tempo Perdido','Prateleiras de arquivo com caixas (ilustrativo) · fitas master e cassetes'),
('O legado de Renato Russo está sumindo por um motivo simples.','Por que o legado está sumindo','Cadeado sobre caixa de fitas (ilustrativo)'),
('Onze de outubro de dois mil e vinte e seis.','30 anos sem Renato','Jardim do Sítio Burle Marx (arquivo, com crédito) · Letreiro "1996 · 2026"'),
]
cum=[];w=0
for p in paras:
    cum.append(w); w+=len(p.split())
out=[]
for key,name,img in CH:
    m=[k for k,p in enumerate(paras) if p.startswith(key)]
    assert len(m)==1,(key,m)
    s=round(cum[m[0]]/195*60)
    out.append((f'{s//60}:{s%60:02d}',name,img))
CHAPS='\n'.join(f'{t} {n}' for t,n,_ in out)
open('chapters.txt','w').write(CHAPS+'\n')
print(CHAPS); print('total min',round(w/195,1), W)
DESC='''Renato Russo morreu há 30 anos, em 11 de outubro de 1996. Em dezembro de 2020, a polícia do Rio entrou num depósito na Zona Norte e apreendeu 91 fitas ligadas a ele e à Legião Urbana. Elas são só uma parte da guerra que se formou em volta da obra do cantor.

Neste vídeo: o garoto que inventou uma banda num caderno em Brasília, a noite violenta de 1988 no Mané Garrincha, o diagnóstico de HIV que ele escondeu por seis anos até da própria mãe, a disputa pela guarda do filho, a batalha de Dado Villa-Lobos e Marcelo Bonfá pelo nome Legião Urbana no STJ, a série da Globoplay que nunca foi ao ar, a investigação sobre um possível desvio de R$ 20 milhões e o destino das 91 fitas.

Importante: as informações sobre processos, auditoria e investigações vêm de reportagens e decisões públicas e são atribuídas às fontes no vídeo. A investigação sobre a empresa corre em sigilo e ninguém foi apontado publicamente como culpado. Giuliano Manfredini, Dado Villa-Lobos, Marcelo Bonfá e a Universal Music têm suas posições apresentadas no vídeo.

Se você estiver passando por um momento difícil, o CVV atende 24 horas pelo telefone 188 ou em cvv.org.br.

{CHAPS}

#RenatoRusso #LegiaoUrbana #30AnosSemRenatoRusso'''.replace('{CHAPS}',CHAPS)
TAGS='renato russo, legião urbana, renato russo 30 anos, morte de renato russo, renato russo fitas inéditas, renato russo filho, giuliano manfredini, dado villa-lobos, marcelo bonfá, legião urbana stj, renato russo aids, renato russo história, renato russo documentário, assim foi a vida, legado de renato russo'
assert len(TAGS)<=500, len(TAGS)
open('desc.txt','w').write(DESC+'\n'); open('tags.txt','w').write(TAGS+'\n')
rows=''.join(f'<tr><td class="t">{t}</td><td><b>{html.escape(n)}</b><br>{html.escape(i)}</td></tr>\n' for t,n,i in out)
CAUT='''<li>Giuliano Manfredini não foi acusado de nada: nunca usar letreiros como "ladrão", "desviou" ou "culpado". O desvio de R$ 20 milhões é uma denúncia feita por ele mesmo, sobre a empresa, e a investigação corre em sigilo, sem nomes divulgados.</li>
<li>O produtor investigado na Operação Será não deve ser nomeado nem mostrado; ele nega irregularidade.</li>
<li>Fitas: a Universal afirma que o material é dela; sempre que o letreiro disser "apreendidas", evitar "roubadas" ou "escondidas".</li>
<li>Episódio de 1984 (pulsos): só ambientação neutra, sem sangue, faca ou reconstituição. Manter o aviso do CVV na descrição.</li>
<li>HIV: tratar com respeito; nada de imagens de pessoas doentes, hospitais dramatizados ou caveiras. Não usar a capa real da revista com Cazuza.</li>
<li>Mãe biológica de Giuliano: não citar nome nem mostrar imagem.</li>
<li>Músicas da Legião: usar só trechos curtíssimos ou nenhum, porque a empresa do herdeiro e a Universal fazem reivindicações de direitos (risco de Content ID).</li>
<li>Fotos de Renato, Dado e Bonfá: só fotos de imprensa com crédito; nada de rosto gerado por IA.</li>
<li>Recomendado: revisão jurídica antes de publicar.</li>'''
SEC=lambda h,i,c: f'<h2>{h} <button data-t="{i}">Copiar</button></h2><pre id="{i}">{html.escape(c)}</pre>'
open('Renato_Pacote_Producao.html','w').write(f'''<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Pacote de Produção — Renato Russo</title>
<style>body{{background:#fff;color:#111;font-family:system-ui,Segoe UI,Arial,sans-serif;max-width:860px;margin:0 auto;padding:24px 16px;line-height:1.55}}h1{{font-size:24px}}h2{{font-size:19px;margin-top:32px;border-bottom:2px solid #eee;padding-bottom:4px}}pre{{white-space:pre-wrap;background:#f6f6f6;padding:12px;border-radius:6px;font-family:inherit}}table{{width:100%;border-collapse:collapse}}td{{border-bottom:1px solid #eee;padding:8px;vertical-align:top}}td.t{{font-weight:700;white-space:nowrap;width:60px}}.note{{color:#555;font-size:14px}}li{{margin-bottom:6px}}button{{font-size:13px;margin-left:8px}}</style></head><body>
<h1>Pacote de Produção: Renato Russo</h1>
<p><b>Título:</b> {html.escape(TITLE)}</p>
{SEC('Descrição (SEO, já com capítulos)','desc',DESC)}
{SEC('Tags','tags',TAGS)}<p class="note">{len(TAGS)} caracteres (limite do YouTube: 500).</p>
{SEC('Capítulos','chap',CHAPS)}
<p class="note">Tempos calculados a 195 palavras por minuto (~{round(w/195)} min). Ajuste pelo áudio real.</p>
<h2>Lista de imagens para o editor</h2><table>{rows}</table>
<h2>Cuidados na edição</h2><ul>{CAUT}</ul>
<script>document.querySelectorAll('button[data-t]').forEach(b=>b.onclick=()=>{{navigator.clipboard.writeText(document.getElementById(b.dataset.t).textContent).then(()=>{{b.textContent='Copiado';setTimeout(()=>b.textContent='Copiar',1500)}})}})</script>
</body></html>''')
json.dump({'title':TITLE,'desc':DESC,'tags':TAGS,'chaps':CHAPS,'rows':rows,'caut':CAUT,'paras':paras,'words':W},open('pack.json','w'),ensure_ascii=False)
