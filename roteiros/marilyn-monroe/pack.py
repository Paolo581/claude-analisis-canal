import re, html
TITLE="Assim FOI a VIDA de MARILYN MONROE — O Segredo REPUGNANTE Que Hollywood Enterrou Com Ela"
files=['parte1.txt','parte2.txt','parte3.txt','parte4.txt','parte5.txt']
paras=[]
for f in files:
    for p in open(f).read().split('\n\n'):
        p=p.strip()
        if p: paras.append(re.sub(r'^[RA]: ','',p))
# voice html
body=''.join(f'<p>{html.escape(p)}</p>\n' for p in paras)
open('MarilynMonroe_Roteiro_Voz.html','w').write(f'''<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(TITLE)}</title>
<style>body{{background:#fff;color:#000;font-family:Georgia,serif;font-size:20px;line-height:1.7;max-width:760px;margin:0 auto;padding:32px 16px}}h1{{font-size:24px;line-height:1.3;margin-bottom:32px}}p{{margin:0 0 18px}}</style>
</head><body>
<h1>{html.escape(TITLE)}</h1>
{body}</body></html>''')
# chapters
CH=[('R: Marilyn Monroe foi a mulher','A mulher que ninguém quis','Marilyn sorrindo (arquivo, licenciada) × berço vazio na penumbra · Texto: "O SEGREDO QUE HOLLYWOOD ENTERROU"'),
('Cinco de agosto de mil novecentos e sessenta e dois.','A porta trancada','Casa de Brentwood à noite (fachada, arquivo) · Porta com luz por baixo · Telefone antigo sobre lençol (1.º objeto, ilustrativo)'),
('Primeiro de junho de mil novecentos e vinte e seis.','Nasce Norma Jeane','Hospital de Los Angeles anos 20 (arquivo) · Fotos de bebê de Norma Jeane (domínio público/licenciadas)'),
('Com doze dias de vida','O travesseiro','Casa de subúrbio anos 20 · Travesseiro em close, desfocado (ilustrativo, sem criança)'),
('Em janeiro de mil novecentos e trinta e quatro','A mãe internada','Corredor de hospital psiquiátrico antigo (arquivo) · Foto de Gladys Baker (com crédito)'),
('Uma amiga da mãe, Grace McKee','O orfanato','Fachada do orfanato de Los Angeles (arquivo) · Dormitório antigo com camas enfileiradas'),
('Dezenove de junho de mil novecentos e quarenta e dois.','Casada aos dezesseis','Foto do casamento com James Dougherty (arquivo, com crédito)'),
('Mil novecentos e quarenta e quatro.','A operária','Foto de David Conover na Radioplane, 1944 (com crédito) · Fábrica em tempo de guerra'),
('Julho de mil novecentos e quarenta e seis.','Nasce Marilyn Monroe','Letreiro da Fox · Teste de câmera (trecho curto, com crédito)'),
('Vinte e sete de maio de mil novecentos e quarenta e nove.','A foto de 50 dólares','Veludo vermelho vazio + recibo de 50 dólares assinado "Mona Monroe" (2.º objeto, ilustrativo). NUNCA mostrar a foto nua'),
('Johnny Hyde era um dos agentes','Johnny Hyde','Foto de Marilyn e Hyde (arquivo) · Frasco de comprimidos desfocado'),
('Março de mil novecentos e cinquenta e dois.','O escândalo do calendário','Manchetes de 1952 (recorte, com crédito) · Máquina de escrever de redação'),
('O nome dele era Hugh Hefner.','Hugh Hefner','Chicago anos 50 · Mesa de cozinha com provas de revista (ilustrativo)'),
('A: Dezembro de mil novecentos e cinquenta e três.','A primeira Playboy','Capa da 1.ª Playboy SÓ a capa, borrada no miolo (3.º objeto). Nada do interior'),
('Catorze de janeiro de mil novecentos e cinquenta e quatro.','Joe DiMaggio','Casamento em San Francisco (arquivo) · Marilyn na Coreia (arquivo, domínio público do exército)'),
('Quinze de setembro de mil novecentos e cinquenta e quatro.','O vestido branco','Cena do metrô em plano aberto (foto de imprensa, com crédito) · Hotel St. Regis'),
('Cinco de novembro de mil novecentos e cinquenta e quatro.','A porta errada','Porta arrombada no escuro (ilustrativo) · Manchete da época'),
('Em Nova York, começou a estudar','Lee Strasberg','Actors Studio (arquivo) · Foto de Lee e Paula Strasberg (com crédito)'),
('Arthur Miller era um dos maiores','Arthur Miller','Casamento com Miller (arquivo) · Caderno aberto sobre mesa (ilustrativo)'),
('Em mil novecentos e sessenta, Marilyn filmou','Os Desajustados','Deserto de Nevada · Foto de Clark Gable (com crédito)'),
('A: Fevereiro de mil novecentos e sessenta e um.','Trancada','Corredor de clínica, porta com visor de vidro (ilustrativo) · Letreiro "Payne Whitney, 1961"'),
('Março de mil novecentos e sessenta e um.','Cursum Perficio','Azulejo "Cursum Perficio" (foto atual, com crédito) · Consultório de psiquiatra anos 60'),
('Peter Lawford era ator','Os Kennedy','Fotos de John e Robert Kennedy (domínio público) · Letreiro "TEORIA" nas partes não comprovadas'),
('Dezenove de maio de mil novecentos e sessenta e dois.','Happy Birthday, Mr. President','Madison Square Garden (trecho curto, com crédito) · Vestido de cristais em close'),
('"Something\'s Got to Give" estava em crise','Demitida','Set de filmagem vazio · Manchetes de junho de 1962'),
('A partir daqui, é preciso separar','O que se sabe e o que se suspeita','Telefone de disco · Letreiro "NUNCA COMPROVADO"'),
('Então chegou o último dia.','O último dia','Casa de Brentwood ao entardecer · Telefone tocando (ilustrativo)'),
('Oito de agosto de mil novecentos e sessenta e dois.','O enterro','Westwood Memorial Park (arquivo) · DiMaggio no enterro (foto de imprensa, com crédito)'),
('Dias depois do enterro','Rosas por vinte anos','Rosas vermelhas diante de gaveta de mármore (4.º objeto)'),
('Marilyn tinha feito um testamento','A herança','Documento de testamento antigo (ilustrativo) · Leilão Christie\'s 1999 (com crédito)'),
('Um empresário de Los Angeles chamado Richard Poncher','A gaveta de cima','Corredor de gavetas de mármore · Página de leilão genérica (ilustrativo)'),
('A: Mil novecentos e noventa e dois.','O homem ao lado dela','Gaveta de Hefner ao lado da de Marilyn (foto do cemitério, com crédito) (5.º objeto)'),
('Ainda havia uma última pergunta','O pai','Fio de cabelo em lâmina de laboratório · Foto de Charles Stanley Gifford (com crédito)'),
('Agora junte todas as peças.','O preço da fama','Montagem dos 5 objetos: telefone, veludo e recibo, capa borrada, rosas, gaveta'),
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
DESC='''Marilyn Monroe foi a mulher mais desejada do mundo. Mas a menina que ninguém quis, a foto de 50 dólares que virou um império e o homem que pagou 75 mil dólares para ficar ao lado dela para sempre contam outra história.

Uma história de abandono, internação, exploração e um segredo que Hollywood enterrou junto com ela.

Se você está passando por um momento difícil, ligue 188 (CVV), 24 horas, de graça.

#MarilynMonroe #Hollywood #HughHefner'''
TAGS='marilyn monroe, marilyn monroe história, marilyn monroe morte, marilyn monroe documentário, hugh hefner marilyn, marilyn monroe túmulo, marilyn monroe playboy, norma jeane, joe dimaggio, marilyn monroe kennedy, marilyn monroe infância, assim foi a vida, marilyn monroe segredo, hollywood'
rows=''.join(f'<tr><td class="t">{t}</td><td><b>{html.escape(n)}</b><br>{html.escape(i)}</td></tr>\n' for t,n,i in out)
chap=html.escape('\n'.join(f'{t} {n}' for t,n,_ in out))
open('MarilynMonroe_Pacote_Producao.html','w').write(f'''<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Pacote de Produção — Marilyn Monroe</title>
<style>body{{background:#fff;color:#111;font-family:system-ui,Segoe UI,Arial,sans-serif;max-width:860px;margin:0 auto;padding:24px 16px;line-height:1.55}}h1{{font-size:24px}}h2{{font-size:19px;margin-top:32px;border-bottom:2px solid #eee;padding-bottom:4px}}pre{{white-space:pre-wrap;background:#f6f6f6;padding:12px;border-radius:6px;font-family:inherit}}table{{width:100%;border-collapse:collapse}}td{{border-bottom:1px solid #eee;padding:8px;vertical-align:top}}td.t{{font-weight:700;white-space:nowrap;width:60px}}.note{{color:#555;font-size:14px}}li{{margin-bottom:6px}}</style></head><body>
<h1>Pacote de Produção: Marilyn Monroe</h1>
<p><b>Título:</b> {html.escape(TITLE)}</p>
<h2>Descrição (SEO)</h2><pre>{html.escape(DESC)}</pre>
<h2>Tags</h2><pre>{html.escape(TAGS)}</pre><p class="note">{len(TAGS)} caracteres (limite do YouTube: 500).</p>
<h2>Capítulos (colar na descrição)</h2><pre>{chap}</pre>
<p class="note">Tempos calculados a 195 palavras por minuto (~{round(w/195)} min no total). Ajuste pelo áudio real depois de gravar.</p>
<h2>Lista de imagens para o editor</h2><table>{rows}</table>
<h2>Cuidados na edição (monetização)</h2><ul>
<li>NUNCA mostrar as fotos nuas (calendário, Playboy, piscina). Veludo vazio, capa borrada no interior, recortes de jornal.</li>
<li>Morte: sem imagens do corpo nem de frascos em close; sem detalhes do método. O CVV 188 fica no fim e na descrição.</li>
<li>Abuso na infância: só a menção narrada, sem encenação e sem imagens de criança em situação de risco.</li>
<li>Kennedy: letreiro "TEORIA" ou "NUNCA COMPROVADO" nas partes de Robert Kennedy e da noite em Palm Springs.</li>
<li>Violência de DiMaggio e o episódio do Cal-Neva: sempre com "segundo relatos" na tela.</li>
<li>Filmes e TV (Fox, Madison Square Garden): trechos curtos e com crédito; preferir fotos de imprensa.</li>
<li>Thumbnail: sem nudez, sem decote exagerado, sem logo da Playboy; foto real licenciada na silhueta.</li>
</ul>
<h2>Thumbnails</h2><p>Thumb1_ENTERRADO_AO_LADO_DELA.jpg · Thumb2_NINGUEM_ATENDEU.jpg (na mesma pasta). Na Thumb1, trocar o rosto gerado por IA por uma foto real licenciada de Marilyn. A Thumb2 usa só silhuetas.</p>
</body></html>''')
