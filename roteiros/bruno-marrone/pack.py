import re, html
TITLE='MARRONE Quebrou o SILÊNCIO: "Tive Que Me PROTEGER" de Bruno — A Verdade HORRÍVEL da Dupla'
files=['parte1.txt','parte2.txt','parte3.txt','parte4.txt','parte5.txt']
paras=[]
for f in files:
    for p in open(f).read().split('\n\n'):
        p=p.strip()
        if p: paras.append(re.sub(r'^[RA]: ','',p))
# voice html
body=''.join(f'<p>{html.escape(p)}</p>\n' for p in paras)
open('BrunoMarrone_Roteiro_Voz.html','w').write(f'''<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(TITLE)}</title>
<style>body{{background:#fff;color:#000;font-family:Georgia,serif;font-size:20px;line-height:1.7;max-width:760px;margin:0 auto;padding:32px 16px}}h1{{font-size:24px;line-height:1.3;margin-bottom:32px}}p{{margin:0 0 18px}}</style>
</head><body>
<h1>{html.escape(TITLE)}</h1>
{body}</body></html>''')
# chapters
CH=[('Marrone passou quarenta anos','Marrone quebrou o silêncio','Bruno e Marrone lado a lado no palco (foto de imprensa) · Corte seco para preto · Texto na tela: "TIVE QUE ME PROTEGER"'),
('O nome verdadeiro de Bruno','O menino da farmácia','Goiânia anos 70–80 (arquivo) · Balcão de farmácia antiga (ilustrativo) · Caixas de remédio'),
('O cantor era Leonardo','Leonardo junta a dupla','Leonardo jovem nos anos 80 (arquivo) · Capas de revista com nomes de bebê · Letreiro "Bruno e Marrone"'),
('Durante quase dez anos, os dois cantaram','Quinze anos nos bares','Bar de beira de estrada à noite · Garrafas sobre mesas · Parque de exposição de gado'),
('Dois mil e um.','O Acústico que mudou tudo','Capa do "Acústico ao Vivo" (2001) · Rádio antigo tocando · Contador "1,5 milhão de cópias" · Troféu Grammy Latino'),
('Segunda-feira, dois de maio de dois mil e onze','O helicóptero de 2011','Imagens de TV do acidente em São José do Rio Preto (arquivo de imprensa) · Destroços · Hospital'),
('Naquele mesmo ano de dois mil e onze, num show nos Estados Unidos','"Peixes e piranhas"','Manchetes de 2011 (recortes) · Palco com plateia brasileira nos EUA (ilustrativo)'),
('Sábado, vinte e sete de maio de dois mil e dezessete','Patos de Minas','Vídeo dos fãs na Fenamilho 2017 (trecho curto, com crédito) · Copo de uísque no palco (2.º objeto começa aqui) · Close do rosto de Marrone recusando'),
('Terça-feira, trinta de maio','O vídeo de desculpas','Trecho do vídeo de desculpas de Bruno (2.º objeto) · Frase na tela: "Já bebi no palco e sou muito forte para beber"'),
('A conta de Patos de Minas','O castigo da Fenamilho','Recortes do jornal de Patos de Minas · Carta de repúdio (ilustrativa) · Ingresso de R$ 20 do show beneficente de 2018'),
('José Roberto Ferreira nasceu','Quem é Marrone','Buriti Alegre (GO), vista da cidade · Caminhão de boia-fria na lavoura · Sanfona antiga'),
('Sexta-feira, dez de abril de dois mil e vinte','A live dos 21 milhões','Trechos da live de 10/04/2020 (curtos, com crédito) · Contador subindo até "21 milhões" · Memes da época · Close em Marrone'),
('Junho de dois mil e vinte e um.','"Tive que me proteger"','Trecho da entrevista ao Alma Sertaneja (1.º objeto, com crédito) · Frases de Marrone em letreiro sobre fundo preto · Balde e barco (ilustrativo, sutil)'),
('Para medir o peso dessa confissão','"Aprendi a cantar bêbado"','Trecho do The Noite (abril de 2020, 3.º objeto) · Frase na tela · Volta rápida às imagens dos bares de Goiânia'),
('O primeiro golpe veio em maio de dois mil e vinte e dois','A morte do pai','Foto de família (pública) · Balcão de farmácia vazio · Vela acesa'),
('Enzo puxou o pai','O filho no palco','Enzo Rabelo em shows (foto de imprensa) · Enzo abrindo show do pai'),
('Junho de dois mil e vinte e quatro','O glaucoma','Exame de fundo de olho (ilustrativo) · Efeito de visão com bordas escurecidas · Hospital de olhos'),
('Madrugada de vinte e cinco de dezembro','O Natal de dona Anita','Árvore de Natal com luzes apagando · Nota oficial da dupla (print) · Formatura de Enzo (post público)'),
('Começo de julho de dois mil e vinte e seis','O câncer inventado por IA','Frames dos vídeos falsos DESFOCADOS com carimbo "FALSO" · Vídeo de Bruno desmentindo (trecho curto)'),
('A: Agosto de dois mil e vinte e seis. Festa do Peão','Barretos','Capa de "De Volta aos Bares 2" (4.º objeto) · Arena de Barretos lotada · Placa de cidadão honorário'),
('A: Já era madrugada de sexta-feira','"Ele tem que pedir desculpa pro Marrone"','Arena à noite com holofotes · Placa sob luz forte · Foto de Cuiabano Lima (imprensa) · Frase dele em letreiro'),
('A: Domingo, trinta de agosto','Uberlândia','Vídeos de fãs no Camaru 2026 (curtos, com crédito) · Prints de comentários com nomes borrados · Trecho do Balanço Geral (com crédito)'),
('Segunda-feira, vinte e um de setembro','A queda de Rick','Serra catarinense com neblina · Buscas (imagens de TV) · Rick e Renner no palco (arquivo)'),
('Quinta-feira, vinte e quatro de setembro','O velório e a segunda chance','Marrone falando à imprensa em Sorocaba (trecho com crédito) · Adega com garrafa de vinho (5.º objeto) · Letreiro "SEGUNDA CHANCE"'),
('R: Enquanto Marrone se despedia do amigo','A cirurgia de Bruno','Print do comunicado do cancelamento em Cristalina · Calendário de agosto–setembro com as datas marcadas'),
('R: Chegou a hora de responder','Do que Marrone se protegia','Marrone em silêncio no palco (imprensa) · Frases de 2021 em letreiro · Bruno emocionado falando de Felipe (entrevista André Piunti)'),
('Junho de dois mil e vinte e seis. Dois meses','"O que eu sou em casa, bebendo"','Trecho da entrevista a Leo Dias (2026, com crédito) · Volta às imagens da live de 2020'),
('R: Agora você vai entender por que ele nunca saiu','Por que Marrone ficou','Montagem cronológica dos dois de 1985 a 2026 · Palco vazio com dois microfones · Tela final "Deixa a poeira baixar"'),
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
DESC='''Marrone passou 40 anos ao lado de Bruno e um dia admitiu: "Tive que me proteger." A live dos 21 milhões, Patos de Minas, a briga em Barretos, o show de Uberlândia e a frase de Marrone no velório de Rick. Do que ele se protegia? E por que nunca foi embora?

#BrunoEMarrone #Marrone #Sertanejo'''
TAGS='bruno e marrone, marrone, bruno, tive que me proteger, marrone bruno briga, bruno bêbado, bruno e marrone polêmica, bruno e marrone uberlândia, bruno e marrone barretos, marrone velório rick, bruno e marrone live, bruno e marrone separação, dupla sertaneja, documentário sertanejo, história de bruno e marrone, verdade bruno e marrone'
rows=''.join(f'<tr><td class="t">{t}</td><td><b>{html.escape(n)}</b><br>{html.escape(i)}</td></tr>\n' for t,n,i in out)
chap=html.escape('\n'.join(f'{t} {n}' for t,n,_ in out))
open('BrunoMarrone_Pacote_Producao.html','w').write(f'''<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Pacote de Produção — Bruno &amp; Marrone</title>
<style>body{{background:#fff;color:#111;font-family:system-ui,Segoe UI,Arial,sans-serif;max-width:860px;margin:0 auto;padding:24px 16px;line-height:1.55}}h1{{font-size:24px}}h2{{font-size:19px;margin-top:32px;border-bottom:2px solid #eee;padding-bottom:4px}}pre{{white-space:pre-wrap;background:#f6f6f6;padding:12px;border-radius:6px;font-family:inherit}}table{{width:100%;border-collapse:collapse}}td{{border-bottom:1px solid #eee;padding:8px;vertical-align:top}}td.t{{font-weight:700;white-space:nowrap;width:60px}}.note{{color:#555;font-size:14px}}li{{margin-bottom:6px}}</style></head><body>
<h1>Pacote de Produção: Bruno &amp; Marrone</h1>
<p><b>Título:</b> {html.escape(TITLE)}</p>
<h2>Descrição (SEO)</h2><pre>{html.escape(DESC)}</pre>
<h2>Tags</h2><pre>{html.escape(TAGS)}</pre><p class="note">{len(TAGS)} caracteres (limite do YouTube: 500).</p>
<h2>Capítulos (colar na descrição)</h2><pre>{chap}</pre>
<p class="note">Tempos calculados a 195 palavras por minuto (~{round(w/195)} min no total). Ajuste pelo áudio real depois de gravar.</p>
<h2>Lista de imagens para o editor</h2><table>{rows}</table>
<h2>Cuidados na edição (Bruno e Marrone estão vivos)</h2><ul>
<li>Barretos e Uberlândia: sempre como relato de fãs e de Cuiabano Lima. Nunca legendar "Bruno bêbado" nas imagens.</li>
<li>Vídeos falsos de IA (câncer terminal): mostrar só desfocados, com carimbo "FALSO". Não reproduzir o áudio.</li>
<li>Comentários de redes: borrar nomes e fotos de perfil.</li>
<li>Trechos de entrevistas, TV e lives: curtos, com crédito na tela (Alma Sertaneja, The Noite/SBT, Leo Dias, André Piunti, Record).</li>
<li>Thumbnail: usar fotos reais licenciadas dos dois nas silhuetas; não usar rosto gerado por IA de pessoas reais.</li>
<li>Velório de Rick: sem imagens do caixão ou da família em luto; usar só a fala de Marrone à imprensa.</li>
</ul>
<h2>Thumbnails</h2><p>Thumb1_TIVE_QUE_ME_PROTEGER.jpg · Thumb2_ELE_NUNCA_FOI_EMBORA.jpg (na mesma pasta). As silhuetas são espaço para as fotos reais.</p>
</body></html>''')
