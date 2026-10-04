import re, html
TITLE="LUCIANO HUCK: As Mensagens SECRETAS Que a Polícia Federal Encontrou"
files=['parte1.txt','parte2.txt','parte3.txt','parte4.txt','parte5.txt']
paras=[]
for f in files:
    for p in open(f).read().split('\n\n'):
        p=p.strip()
        if p: paras.append(re.sub(r'^[RA]: ','',p))
# voice html
body=''.join(f'<p>{html.escape(p)}</p>\n' for p in paras)
open('Huck_Roteiro_Voz.html','w').write(f'''<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(TITLE)}</title>
<style>body{{background:#fff;color:#000;font-family:Georgia,serif;font-size:20px;line-height:1.7;max-width:760px;margin:0 auto;padding:32px 16px}}h1{{font-size:24px;line-height:1.3;margin-bottom:32px}}p{{margin:0 0 18px}}</style>
</head><body>
<h1>{html.escape(TITLE)}</h1>
{body}</body></html>''')
# chapters
CH=[('R: Luciano Huck passou','O segredo','Foto real licenciada de Huck no Domingão × celular com tela acesa no escuro · Texto: "AS MENSAGENS"'),
('Para entender o tamanho desse segredo','O bom moço do sábado','Trechos curtos do Caldeirão (com crédito) · Casa reformada, família emocionada (sem close de crianças)'),
('Só que o próprio Luciano Huck','O rapaz rico de São Paulo','Fotos de arquivo de Huck jovem (com crédito)'),
('Em dois mil e dezoito, o nome dele','Quase presidente','Manchetes de 2018 e 2022 (com crédito)'),
('Em setembro de dois mil e vinte e um, Faust','O dono do domingo','Abertura do Domingão (trecho curto, com crédito)'),
('O nome dele era Daniel Vorcaro','Daniel Vorcaro','Foto pública de Vorcaro (com crédito) · Avenida Faria Lima à noite'),
('Imagine que você tem um dinheiro guardado','Juros bons demais','Animação simples: dois bancos e duas taxas de juros'),
('Até que, em novembro de dois mil e vinte e cinco','O celular apreendido','Celular em saco de evidência (ilustrativo, sem logotipo da PF real)'),
('Domingo, cinco de novembro de dois mil e vinte e três','A primeira mensagem','Balões de mensagem em letreiro (texto parafraseado, sem simular print)'),
('Fevereiro de dois mil e vinte e quatro','O jatinho','Gulfstream G550 em pista (banco de imagens) · Letreiro "Salvou o dia"'),
('Final de abril e começo de maio','As enchentes','Imagens públicas das enchentes em Canoas (com crédito)'),
('No dia quatro de maio de dois mil e vinte e quatro','Madonna e Zelensky','Show de Copacabana (arquivo, com crédito) · Varsóvia (banco de imagens)'),
('Para entender o dinheiro','O Will Bank','Celular com app de banco genérico (sem logotipo real)'),
('R: E foi aqui que apareceu o número','R$ 26 milhões','Letreiros "R$ 83 milhões" e "R$ 26 milhões" · Cálculo "1.500 anos de salário mínimo"'),
('Existe no Brasil uma espécie de seguro','O Fundo Garantidor','Letreiro "até R$ 250 mil por pessoa"'),
('Além dos conselhos, houve mais','Pizza com Ronaldo','Foto pública de Ronaldo (com crédito)'),
('Numa das mensagens, Huck dá','"Tome as redes da sua narrativa"','Letreiros com as mensagens reais, letra por letra'),
('Dois mil e vinte e cinco foi o ano','O cerco ao Master','Manchetes BRB e Banco Central (com crédito)'),
('Segunda-feira, dezessete de novembro','17 de novembro','Relógio marcando 21h47 · Bancada de telejornal genérica (não usar imagem do JN sem licença)'),
('Na noite daquela segunda-feira','A prisão','Aeroporto à noite, jatinho na pista (ilustrativo) · Manchetes da prisão (com crédito)'),
('Domingo, vinte e sete de setembro','O Tinder eleitoral','Trecho curto do Domingão (com crédito) · Tela de questionário genérica'),
('O padrão que os usuários','A apuração do MPF','Manchetes do MPF (com crédito)'),
('Quarta-feira, trinta de setembro','A semana da Veja','Capa/manchete da Veja (com crédito)'),
('O escritório do apresentador','A resposta de Huck','Letreiro com a nota oficial'),
('Lembra do conselho que ele deu','O conselho que voltou','Letreiro "Senão farão isso por você"'),
('A televisão ensina a gente','Os dois lados de um rosto','Sala de casa com TV ligada (ilustrativo)'),
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
DESC='''Mensagens recuperadas pela Polícia Federal no celular do banqueiro Daniel Vorcaro, do Banco Master, e publicadas pela revista Veja em setembro de 2026 mostram dois anos de amizade e negócios com Luciano Huck: o jatinho, o patrocínio do Will Bank ao Domingão, os conselhos de imagem e a mensagem enviada na noite da prisão de Vorcaro. Na mesma semana, a plataforma "Tem Meu Voto", divulgada no Domingão, virou alvo de apuração do MPF.

Importante: segundo a própria Veja, as mensagens não mostram ilegalidade, e Luciano Huck não é suspeito em nenhuma investigação sobre o Banco Master. A defesa dele afirma que a relação foi apenas comercial, ligada ao patrocínio do Will Bank.

#LucianoHuck #BancoMaster #Vorcaro'''
TAGS='luciano huck, luciano huck vorcaro, mensagens luciano huck, banco master, daniel vorcaro, will bank, domingão com huck, tem meu voto, luciano huck polêmica, luciano huck mpf, vorcaro preso, assim foi a vida'
rows=''.join(f'<tr><td class="t">{t}</td><td><b>{html.escape(n)}</b><br>{html.escape(i)}</td></tr>\n' for t,n,i in out)
chap=html.escape('\n'.join(f'{t} {n}' for t,n,_ in out))
open('Huck_Pacote_Producao.html','w').write(f'''<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Pacote de Produção — Luciano Huck</title>
<style>body{{background:#fff;color:#111;font-family:system-ui,Segoe UI,Arial,sans-serif;max-width:860px;margin:0 auto;padding:24px 16px;line-height:1.55}}h1{{font-size:24px}}h2{{font-size:19px;margin-top:32px;border-bottom:2px solid #eee;padding-bottom:4px}}pre{{white-space:pre-wrap;background:#f6f6f6;padding:12px;border-radius:6px;font-family:inherit}}table{{width:100%;border-collapse:collapse}}td{{border-bottom:1px solid #eee;padding:8px;vertical-align:top}}td.t{{font-weight:700;white-space:nowrap;width:60px}}.note{{color:#555;font-size:14px}}li{{margin-bottom:6px}}</style></head><body>
<h1>Pacote de Produção: Luciano Huck</h1>
<p><b>Título:</b> {html.escape(TITLE)}</p>
<h2>Descrição (SEO)</h2><pre>{html.escape(DESC)}</pre>
<h2>Tags</h2><pre>{html.escape(TAGS)}</pre><p class="note">{len(TAGS)} caracteres (limite do YouTube: 500).</p>
<h2>Capítulos (colar na descrição)</h2><pre>{chap}</pre>
<p class="note">Tempos calculados a 195 palavras por minuto (~{round(w/195)} min no total). Ajuste pelo áudio real depois de gravar.</p>
<h2>Lista de imagens para o editor</h2><table>{rows}</table>
<h2>Cuidados na edição</h2><ul>
<li>Huck não é acusado de crime: nunca usar letreiros como "culpado", "criminoso" ou "esquema de Huck". Manter na tela, quando citado, "segundo a Veja, sem ilegalidade".</li>
<li>Mensagens: usar só o texto publicado na imprensa, em letreiro. Não simular prints falsos de WhatsApp.</li>
<li>Vorcaro: tratar como "preso" e "investigado", sem afirmar condenação.</li>
<li>Plataforma "Tem Meu Voto": apuração em andamento; mostrar a resposta de Huck e dos responsáveis.</li>
<li>Logotipos (Globo, PF, JN, Will Bank, Veja): só em imagens de imprensa com crédito; nada de recriar logotipos.</li>
<li>Thumbnail: foto real licenciada de Huck, ou só silhueta; nunca rosto gerado por IA.</li>
<li>Publicação: depois do primeiro turno (4/10), por envolver tema eleitoral.</li>
</ul>
<h2>Thumbnails</h2><p><b>Thumb1_AS_MENSAGENS_QUE_A_PF_ACHOU.jpg</b> (recomendada): silhueta de apresentador no palco × celular em saco de evidência com "Congrats" na tela. <b>Thumb2_RS_26_MILHOES.jpg</b>: jatinho na pista × dinheiro e contrato. Atenção: a Thumb2 mostra pilhas de dinheiro vivo, e o contrato real foi legal e bancário; para reduzir risco jurídico, prefira a Thumb1.</p>
</body></html>''')
