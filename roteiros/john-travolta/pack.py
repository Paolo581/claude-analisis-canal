import re, html
TITLE="JOHN TRAVOLTA: A HORRÍVEL Maldição Que Levou Todas as Mulheres Que Ele Amou"
files=['parte1.txt','parte2.txt','parte3.txt','parte4.txt','parte5.txt']
raw=[]
for f in files:
    for p in open(f).read().split('\n\n'):
        p=p.strip()
        if p: raw.append(p)
paras=[re.sub(r'^[RA]: ','',p) for p in raw]
open('voz.txt','w').write('\n\n'.join(paras)+'\n')
W=sum(len(p.split()) for p in paras)
body=''.join(f'<p>{html.escape(p)}</p>\n' for p in paras)
open('Travolta_Roteiro_Voz.html','w').write(f'''<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(TITLE)}</title>
<style>body{{background:#fff;color:#000;font-family:Georgia,serif;font-size:20px;line-height:1.7;max-width:760px;margin:0 auto;padding:32px 16px}}h1{{font-size:24px;line-height:1.3;margin-bottom:32px}}p{{margin:0 0 18px}}</style>
</head><body>
<h1>{html.escape(TITLE)}</h1>
{body}</body></html>''')
CH=[('John Travolta passou a vida inteira','A maldição','Silhueta dançando sob luzes de discoteca · Rosas murchas sobre mesa escura'),
('Para entender essa maldição','A primeira mulher','Englewood, Nova Jersey (arquivo/banco de imagens) · Palco de teatro escolar vazio'),
('Em mil novecentos e setenta e um, aos dezessete anos','Nova York','Ponte sobre o rio Hudson anos 70 · Marquises da Broadway (arquivo)'),
('Mil novecentos e setenta e cinco.','Vinnie Barbarino','Trecho curto de Welcome Back, Kotter (com crédito)'),
('Foi assim que, no ano seguinte','A bolha de plástico','Cena de O Menino da Bolha de Plástico (com crédito)'),
('John tinha vinte e dois anos. Diana tinha quarenta.','Diana','Fotos de imprensa de Travolta e Diana Hyland (com crédito)'),
('No começo de mil novecentos e setenta e sete','A casa que nunca existiu','Casa vazia com placa de venda (ilustrativo)'),
('Vinte e sete de março de mil novecentos e setenta e sete.','Nos braços dele','Quarto de hospital à meia-luz, sem pessoas · Letreiro "27/03/1977"'),
('As filmagens de Os Embalos','O terno branco','Pista de dança iluminada (ilustrativo) · Trecho curto de Os Embalos (com crédito)'),
('Meses depois, em setembro','O Emmy','Estatueta do Emmy (imagem de imprensa) · Foto da cerimônia de 1977, se licenciada'),
('Dezembro de mil novecentos e setenta e sete.','Os Embalos de Sábado à Noite','Pôster do filme (com crédito) · Filas de cinema anos 70'),
('Existe um detalhe naquele filme','A mãe na loja de tintas','Frame da cena da loja de tintas com Helen (com crédito)'),
('Dezembro de mil novecentos e setenta e oito.','Helen','Foto pública de Helen Travolta (com crédito) · Letreiro "dezembro de 1978"'),
('Quando a dor apertava','O céu','Boeing 707 de Travolta (imagem de imprensa) · Pista de pouso em casa'),
('Os anos oitenta foram cruéis','A queda','Manchetes de crítica negativa genéricas'),
('No fim dos anos oitenta, John conheceu','Kelly','Fotos de imprensa do casal (com crédito)'),
('Treze de abril de mil novecentos e noventa e dois.','Jett','Avião com o nome "Jett" na fuselagem (imagem de imprensa)'),
('Mil novecentos e noventa e quatro.','Pulp Fiction','Trecho curto da dança de Pulp Fiction (com crédito)'),
('Dezembro de dois mil e oito.','Old Bahama Bay','Marina em Grand Bahama (banco de imagens)'),
('Dois de janeiro de dois mil e nove.','A manhã nas Bahamas','Escada de casa de praia vazia · Letreiro "02/01/2009 · 10h15"'),
('Jett não respondia.','O papel','Ambulância à noite (ilustrativo) · Formulário em branco com caneta (sem simular documento real)'),
('Para entender essa ameaça','25 milhões','Letreiro "US$ 25 milhões" · Telefone tocando (ilustrativo)'),
('A polícia montou uma armadilha.','A armadilha','Corredor de hotel com câmera escondida (ilustrativo)'),
('Setembro de dois mil e nove.','O depoimento','Fachada do tribunal em Nassau (arquivo) · Fotos de imprensa de Travolta chegando (com crédito)'),
('Outubro de dois mil e nove.','A frase que anulou tudo','Microfone num palanque político genérico'),
('Enquanto o caso ainda corria na Justiça','Benjamin','Berço vazio iluminado (ilustrativo)'),
('Para entender o segredo de Kelly','Os anos de paz','Fotos públicas da família (com crédito)'),
('Dois mil e dezoito.','Gotti','Pôster de Gotti (com crédito) · Tapete vermelho'),
('Dois anos antes de morrer, Kelly','O segredo de Kelly','Laço rosa do câncer de mama · Janela com cortina fechada'),
('Doze de julho de dois mil e vinte.','12 de julho de 2020','Tela de celular com post genérico (sem simular o post real) · Letreiro "12/07/2020"'),
('Volte comigo até mil novecentos e setenta e seis.','O que liga todas as mortes','Montagem com as fotos de Diana, Helen e Kelly (com crédito)'),
('Hoje, John Travolta tem mais de setenta anos.','Quem ficou','Avião decolando ao entardecer'),
('Existe uma coisa que a vida de John Travolta ensina','O tempo que resta','Mãos dadas (banco de imagens)'),
]
cum=[];w=0
for p in paras:
    cum.append(w); w+=len(p.split())
out=[]
for key,name,img in CH:
    i=next(k for k,p in enumerate(paras) if p.startswith(key))
    s=round(cum[i]/195*60)
    out.append((f'{s//60}:{s%60:02d}',name,img))
CHAPS='\n'.join(f'{t} {n}' for t,n,_ in out)
open('chapters.txt','w').write(CHAPS+'\n')
print(CHAPS); print('total min',round(w/195,1))
DESC='''John Travolta passou a vida inteira dançando e sorrindo nas telas do mundo inteiro, enquanto uma maldição horrível levava, uma por uma, as mulheres que ele mais amou. Diana Hyland, que morreu nos braços dele em 1977, no ano de Os Embalos de Sábado à Noite. A mãe, Helen, um ano e meio depois. O filho Jett, numa manhã nas Bahamas em 2009, e o papel assinado naquele dia que virou centro de uma acusação de extorsão de 25 milhões de dólares. E Kelly Preston, que escondeu do mundo inteiro, por dois anos, a doença que a levou em 2020.

Sobre o caso das Bahamas: o paramédico Tarino Lightbourne e a ex-senadora Pleasant Bridgewater foram acusados de tentativa de extorsão e se declararam inocentes. O julgamento foi anulado em 2009 e as acusações foram retiradas em 2010, a pedido da família. Os dois nunca foram condenados. A informação de que Helen Travolta teve câncer de mama e escondeu a doença do filho vem de reportagens não confirmadas oficialmente.

Se você ou alguém da sua família está enfrentando um câncer, procure informação e apoio. O INCA (www.gov.br/inca) e a FEMAMA (femama.org.br) têm orientações sobre prevenção e diagnóstico precoce do câncer de mama.

{CHAPS}

#JohnTravolta #KellyPreston #HistóriaReal'''.replace('{CHAPS}',CHAPS)
TAGS='john travolta, john travolta maldição, john travolta história, john travolta biografia, kelly preston, kelly preston câncer, diana hyland, jett travolta, john travolta filho, john travolta bahamas, john travolta extorsão, os embalos de sábado à noite, grease, pulp fiction'
assert len(TAGS)<=500, len(TAGS)
open('desc.txt','w').write(DESC+'\n'); open('tags.txt','w').write(TAGS+'\n')
rows=''.join(f'<tr><td class="t">{t}</td><td><b>{html.escape(n)}</b><br>{html.escape(i)}</td></tr>\n' for t,n,i in out)
CAUT='''<li>Lightbourne e Bridgewater: sempre como "acusados", com letreiro "nunca foram condenados" no fim do bloco. Nada de música de vilão ou zoom nos rostos deles.</li>
<li>Morte de Jett: nunca encenar a convulsão nem a cena do banheiro. Usar escada vazia, ambulância e letreiros. Deixar claro que Travolta não teve culpa.</li>
<li>Autismo: mostrar só como Travolta descreveu no tribunal, com respeito; nada de imagens que estigmatizem.</li>
<li>Helen e o câncer de mama escondido: letreiro "segundo algumas reportagens".</li>
<li>Cientologia: apenas os fatos citados; nenhuma imagem sugerindo culpa da igreja.</li>
<li>Post de Kelly e Travolta no Instagram: não recriar o post como se fosse real; usar tela genérica com letreiro.</li>
<li>Rostos reais: só fotos de imprensa ou arquivo com crédito; nunca rosto gerado por IA.</li>
<li>Trechos de filmes (Os Embalos, Grease, Pulp Fiction, Gotti) e músicas dos Bee Gees: só cortes de poucos segundos, com crédito.</li>'''
SEC=lambda h,i,c: f'<h2>{h} <button data-t="{i}">Copiar</button></h2><pre id="{i}">{html.escape(c)}</pre>'
open('Travolta_Pacote_Producao.html','w').write(f'''<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Pacote de Produção — John Travolta</title>
<style>body{{background:#fff;color:#111;font-family:system-ui,Segoe UI,Arial,sans-serif;max-width:860px;margin:0 auto;padding:24px 16px;line-height:1.55}}h1{{font-size:24px}}h2{{font-size:19px;margin-top:32px;border-bottom:2px solid #eee;padding-bottom:4px}}pre{{white-space:pre-wrap;background:#f6f6f6;padding:12px;border-radius:6px;font-family:inherit}}table{{width:100%;border-collapse:collapse}}td{{border-bottom:1px solid #eee;padding:8px;vertical-align:top}}td.t{{font-weight:700;white-space:nowrap;width:60px}}.note{{color:#555;font-size:14px}}li{{margin-bottom:6px}}button{{font-size:13px;margin-left:8px}}</style></head><body>
<h1>Pacote de Produção: John Travolta</h1>
<p><b>Título:</b> {html.escape(TITLE)}</p>
{SEC('Descrição (SEO, já com capítulos)','desc',DESC)}
{SEC('Tags','tags',TAGS)}<p class="note">{len(TAGS)} caracteres (limite do YouTube: 500).</p>
{SEC('Capítulos','chap',CHAPS)}
<p class="note">Tempos calculados a 195 palavras por minuto (~{round(w/195)} min). Ajuste pelo áudio real.</p>
<h2>Lista de imagens para o editor</h2><table>{rows}</table>
<h2>Cuidados na edição</h2><ul>{CAUT}</ul>
<script>document.querySelectorAll('button[data-t]').forEach(b=>b.onclick=()=>{{navigator.clipboard.writeText(document.getElementById(b.dataset.t).textContent).then(()=>{{b.textContent='Copiado';setTimeout(()=>b.textContent='Copiar',1500)}})}})</script>
</body></html>''')
import json; json.dump({'title':TITLE,'desc':DESC,'tags':TAGS,'chaps':CHAPS,'rows':rows,'caut':CAUT,'paras':paras,'words':W},open('pack.json','w'),ensure_ascii=False)
