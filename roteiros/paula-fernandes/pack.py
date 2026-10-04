import re, html
TITLE="PAULA FERNANDES: O Segredo HORRÍVEL Que Ela Escondeu Atrás do Sucesso"
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
open('Paula_Roteiro_Voz.html','w').write(f'''<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(TITLE)}</title>
<style>body{{background:#fff;color:#000;font-family:Georgia,serif;font-size:20px;line-height:1.7;max-width:760px;margin:0 auto;padding:32px 16px}}h1{{font-size:24px;line-height:1.3;margin-bottom:32px}}p{{margin:0 0 18px}}</style>
</head><body>
<h1>{html.escape(TITLE)}</h1>
{body}</body></html>''')
CH=[('Paula Fernandes passou mais','O segredo horrível','Silhueta de cantora de chapéu sob holofote · Letreiro "O SEGREDO"'),
('Para entender aquela noite','A menina da casa sem luz','Fazenda simples no interior de Minas (banco de imagens) · Botina gasta no pasto'),
('Aos oito anos, Paula','O disco de vinil','Disco de vinil antigo girando (ilustrativo) · Fotos de infância licenciadas, se houver'),
('Com apenas onze anos','Caixa de som nos rodeios','Arena de rodeio anos 90, poeira, peão no touro (arquivo/banco de imagens)'),
('Os anos foram passando.','O sonho que não chegava','Estrada à noite, mala de viagem'),
('Era o começo dos anos dois mil.','O sofá','Sofá em sala escura (ilustrativo, sem rosto)'),
('Paula sobreviveu àquele período','Desistir da música','Campus universitário em BH · Barzinho com mesas de plástico'),
('Paula voltou a compor.','Ave Maria Natureza','Trecho curto da abertura de América (com crédito) · Capa de Canções do Vento Sul'),
('Pela Universal, Paula','Jeito de Mato','Capa de Pássaro de Fogo · Almir Sater (foto de imprensa com crédito)'),
('Até que chegou a noite de vinte e cinco','Copacabana, 700 mil pessoas','Imagens do especial de Roberto Carlos 2010 (trecho curto, com crédito)'),
('Quando o ano de dois mil e onze','O disco mais vendido do Brasil','Letreiros "1,6 milhão de DVDs" e "220 shows" · Fotos de shows (com crédito)'),
('O silêncio durou até','O acidente','Foto pública do carro capotado (post dela, com crédito) · Rodovia à noite'),
('Na comemoração do aniversário','O boato dos "poucos dias de vida"','Tela de celular com vídeo viral genérico · Selo "FALSO" de checagem'),
('Setembro de dois mil e vinte e dois.','O podcast','Microfone de podcast em estúdio (ilustrativo)'),
('Paula contou que, naquela época','A noite que ela escondeu','Janela aberta à noite com cortina ao vento (ilustrativo, sem pessoa)'),
('Em dois mil e vinte e seis, aos quarenta e um','O outro segredo','Bastidores escuros de palco · Letreiro "BBC News Brasil"'),
('Para entender o tamanho disso','A fama de antipática','Manchetes da época com "antipática" (com crédito)'),
('Em fevereiro de dois mil e treze','O boicote religioso','Post em rede social genérico · DVD quebrado (ilustrativo)'),
('Abril de dois mil e dezesseis','Faustão e Bocelli','Trechos curtos do Faustão e do show de Bocelli (com crédito)'),
('Foi também em dois mil e dezesseis','O celular','Celular com mensagens borradas (ilustrativo, sem simular print real)'),
('Os anos passaram, e o rótulo','Roberta Miranda no Roda Viva','Trecho curto do Roda Viva (com crédito)'),
('Agosto de dois mil e vinte e seis.','A entrevista à BBC','Letreiro "3 mulheres entre 22 artistas"'),
('Na entrevista, Paula disse que as pessoas','O que acontecia nos bastidores','Camarim vazio com espelho iluminado · Letreiro "5 namorados em 7 dias"'),
('Quinta-feira, vinte e sete de agosto','Ave Maria em Barretos','Vídeo da Ave Maria a cavalo em Barretos 2026 (com crédito)'),
('E é aqui que aparece, finalmente','A resposta de dona Dulce','Fotos públicas de Paula com a mãe (com crédito)'),
('A gente costuma olhar para as estrelas','Quem fica do nosso lado','Mão segurando outra mão (banco de imagens)'),
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
DESC='''Paula Fernandes passou anos sendo aplaudida como a voz mais doce do sertanejo. Mas, longe dos palcos, ela guardou um segredo horrível: aos 18 anos, antes da fama, ela viveu uma noite em que quase não sobreviveu. Da menina da casa sem luz em Sete Lagoas ao especial de Roberto Carlos para 700 mil pessoas, do disco mais vendido do Brasil ao rótulo de "antipática", e do assédio nos bastidores que ela só revelou em 2026 à volta a Barretos, cantando Ave Maria a cavalo. E a frase que a mãe dela, dona Dulce, repetia quando ninguém mais acreditava.

Os relatos sobre depressão, assédio e bastidores são da própria Paula Fernandes, em entrevistas ao podcast Papo com Clê (2022) e à BBC News Brasil (2026).

Se você ou alguém próximo está passando por um momento difícil, procure ajuda. O CVV atende de graça, 24 horas, pelo telefone 188 ou pelo site cvv.org.br.

{CHAPS}

#PaulaFernandes #Sertanejo #HistóriaReal'''.replace('{CHAPS}',CHAPS)
TAGS='paula fernandes, paula fernandes história, paula fernandes depressão, paula fernandes janela, paula fernandes mãe, paula fernandes assédio, paula fernandes antipática, paula fernandes barretos, paula fernandes bbc, paula fernandes roberta miranda, paula fernandes bocelli, sertanejo, assim foi a vida, biografia paula fernandes'
assert len(TAGS)<=500, len(TAGS)
open('desc.txt','w').write(DESC+'\n'); open('tags.txt','w').write(TAGS+'\n')
rows=''.join(f'<tr><td class="t">{t}</td><td><b>{html.escape(n)}</b><br>{html.escape(i)}</td></tr>\n' for t,n,i in out)
CAUT='''<li>Suicídio: não mostrar pessoa na janela nem simular o ato; usar só janela vazia e cortina. Manter o CVV 188 na descrição e, se possível, num letreiro final.</li>
<li>Assédio: Paula não nomeia ninguém. Nunca colocar foto de outro artista ou empresário junto do tema assédio.</li>
<li>Roberta Miranda: mostrar a acusação e a resposta de Paula com o mesmo peso; sem letreiros como "humilhadora".</li>
<li>Boato da doença: deixar claro na tela que é FALSO (selo de checagem).</li>
<li>Rosto de Paula e da mãe: só fotos reais licenciadas ou de imprensa com crédito; nunca rosto gerado por IA.</li>
<li>Trechos de TV (América, Faustão, Bocelli, Roda Viva, Barretos): cortes curtos e com crédito.</li>
<li>Músicas dela: evitar usar as gravações originais por mais de alguns segundos; preferir trilha livre de direitos.</li>'''
SEC=lambda h,i,c: f'<h2>{h} <button data-t="{i}">Copiar</button></h2><pre id="{i}">{html.escape(c)}</pre>'
open('Paula_Pacote_Producao.html','w').write(f'''<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Pacote de Produção — Paula Fernandes</title>
<style>body{{background:#fff;color:#111;font-family:system-ui,Segoe UI,Arial,sans-serif;max-width:860px;margin:0 auto;padding:24px 16px;line-height:1.55}}h1{{font-size:24px}}h2{{font-size:19px;margin-top:32px;border-bottom:2px solid #eee;padding-bottom:4px}}pre{{white-space:pre-wrap;background:#f6f6f6;padding:12px;border-radius:6px;font-family:inherit}}table{{width:100%;border-collapse:collapse}}td{{border-bottom:1px solid #eee;padding:8px;vertical-align:top}}td.t{{font-weight:700;white-space:nowrap;width:60px}}.note{{color:#555;font-size:14px}}li{{margin-bottom:6px}}button{{font-size:13px;margin-left:8px}}</style></head><body>
<h1>Pacote de Produção: Paula Fernandes</h1>
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
