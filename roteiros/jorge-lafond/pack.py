import re, html, json
TITLE="VERA VERÃO: É REPUGNANTE O Que Fizeram Com o Corpo Dele DEPOIS da Morte"
files=['parte1.txt','parte2.txt','parte3.txt','parte4.txt','parte5.txt']
raw=[p.strip() for f in files for p in open(f).read().split('\n\n') if p.strip()]
paras=[re.sub(r'^[RA]: ','',p) for p in raw]
open('voz.txt','w').write('\n\n'.join(paras)+'\n')
open('roteiro_completo.txt','w').write('\n\n'.join(raw)+'\n')
W=sum(len(p.split()) for p in paras)
body=''.join(f'<p>{html.escape(p)}</p>\n' for p in paras)
open('Lafond_Roteiro_Voz.html','w').write(f'''<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(TITLE)}</title>
<style>body{{background:#fff;color:#000;font-family:Georgia,serif;font-size:20px;line-height:1.7;max-width:760px;margin:0 auto;padding:32px 16px}}h1{{font-size:24px;line-height:1.3;margin-bottom:32px}}p{{margin:0 0 18px}}</style>
</head><body>
<h1>{html.escape(TITLE)}</h1>
{body}</body></html>''')
CH=[('Jorge Lafond foi enterrado diante','O túmulo vazio','Portão de cemitério ao entardecer, sem identificação (ilustrativo)'),
('Para uma cidade da Baixada Fluminense','O menino de Nilópolis','Ruas de Nilópolis (arquivo, com crédito) · oficina mecânica antiga'),
('Carregava também um segredo.','O segredo dos seis anos','Silhueta de menino olhando pela janela (ilustrativo)'),
('Existia um lugar onde ele não precisava','A dança e Mercedes Baptista','Foto de Mercedes Baptista (arquivo, com crédito) · sapatilhas de balé'),
('Aos dezessete anos, Jorge recebeu','Dez anos de aplausos lá fora','Teatro europeu com plateia em silhueta (ilustrativo)'),
('A peruca ainda ia demorar','O homem do fundo da cena','Fantástico / Viva o Gordo anos 80 (arquivo, com crédito)'),
('Dois anos depois, na TV Manchete','Madame Satã','Lapa antiga em preto e branco (arquivo, com crédito)'),
('Esse personagem nasceu em mil novecentos e noventa e dois','Nasce a Vera Verão','Banco de praça vazio com peruca em cima (ilustrativo) · logo A Praça É Nossa (com crédito)'),
('Para boa parte do público, Jorge Lafond e a Vera','O homem por trás da peruca','Peruca num suporte diante de espelho de camarim (ilustrativo)'),
('As críticas também chegaram','As críticas','Manchetes de jornal borradas (ilustrativo)'),
('Nos últimos anos de carreira','Aquele domingo','Palco de auditório vazio com luz azul (ilustrativo)'),
('Naquele domingo, no palco do Domingo Legal','Tirado do palco','Cortina de palco se fechando (ilustrativo) · letreiro "o padre sempre negou"'),
('Jorge saiu dos estúdios magoado.','Uma semana depois','Corredor de hospital à noite (ilustrativo)'),
('Na madrugada de onze de janeiro','A morte','Relógio marcando 1:40 (ilustrativo)'),
('Na noite daquele mesmo sábado','A homenagem na Praça','Banco de praça vazio sob luz de palco (ilustrativo)'),
('O corpo foi levado de São Paulo','Cinco mil pessoas em Irajá','Fotos do enterro (arquivo de imprensa, com crédito) · multidão'),
('No meio do empurra-empurra','A sepultura vazia','Tampa de túmulo rachada (ilustrativo)'),
('Dentro daquele caixão havia algo','O que foi enterrado com ele','Joias douradas sobre tecido escuro (ilustrativo) · saco de veludo lacrado'),
('Depois do enterro, o Brasil seguiu','Quinze anos de silêncio','Calendário passando anos (ilustrativo)'),
('Em setembro de dois mil e dezoito','A denúncia','Manchete de 2018 (com crédito) · letreiro "segundo o empresário"'),
('A denúncia de Padula se espalhou','Os papéis que ninguém deixou','Arquivo de documentos vazio (ilustrativo)'),
('Marcelo Padula conheceu Jorge Lafond','Quem era Padula','Duas silhuetas lado a lado (ilustrativo)'),
('Agora lembra da casa','A casa e a herança','Casa em silhueta com chave (ilustrativo) · letreiro "segundo Padula"'),
('Em fevereiro de dois mil e vinte','O destino de Padula','Cadeira vazia num tribunal (ilustrativo)'),
('Em novembro de dois mil e vinte e um','A decisão da Justiça','Fachada do TJSP (arquivo) · martelo de juiz'),
('A resposta para essa pergunta','Onde está Jorge Lafond','Corredor de cemitério sem lápide (ilustrativo)'),
('No dia vinte e nove de março','O Doodle','Doodle do Google de 29/03/2023 (com crédito)'),
('A história de Jorge também chegou aos palcos','Jorge Pra Sempre Verão','Divulgação da peça (com crédito)'),
('No começo deste vídeo, eu disse','O homem que ninguém visita','Flor sobre muro de cemitério (ilustrativo)'),
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
DESC='''Jorge Lafond foi enterrado em 2003 no Cemitério de Irajá, no Rio, diante de cinco mil pessoas. Quinze anos depois, quando foram procurar o corpo dele, a sepultura estava vazia. E até hoje ninguém explicou publicamente para onde levaram o homem por trás da Vera Verão.

Neste vídeo: o menino de Nilópolis que escondia um segredo desde os seis anos, a dança com Mercedes Baptista, o nascimento da Vera Verão em A Praça É Nossa, o domingo em que ele foi tirado do palco do Domingo Legal, a morte dois meses depois, as joias enterradas com ele, a denúncia de 2018, os documentos que ninguém deixou e a guerra pela herança que terminou na Justiça.

Importante: o padre Marcelo Rossi sempre negou ter pedido a retirada de Jorge Lafond do palco. Nenhum médico ligou o episódio à doença do humorista. As informações sobre as joias, a herança e a casa são atribuídas ao empresário Marcelo Padula, conforme as reportagens citadas. A Justiça reconheceu os primos de Jorge como herdeiros legítimos. A concessionária Rio Pax informou que não recebeu documentos da administração anterior.

{CHAPS}

#JorgeLafond #VeraVerão #APraçaÉNossa'''.replace('{CHAPS}',CHAPS)
TAGS='jorge lafond, vera verão, corpo de jorge lafond, jorge lafond cemitério, jorge lafond morte, a praça é nossa, vera verão morte, epa bicha não, jorge lafond padre marcelo, domingo legal, cemitério de irajá, jorge lafond herança, marcelo padula, assim foi a vida, jorge lafond documentário'
assert len(TAGS)<=500, len(TAGS)
open('desc.txt','w').write(DESC+'\n'); open('tags.txt','w').write(TAGS+'\n')
rows=''.join(f'<tr><td class="t">{t}</td><td><b>{html.escape(n)}</b><br>{html.escape(i)}</td></tr>\n' for t,n,i in out)
CAUT='''<li>Padre Marcelo Rossi: sempre com o letreiro "segundo reportagens; o padre sempre negou". Nunca sugerir que o episódio causou a morte.</li>
<li>Sumiço do corpo: nunca usar "roubaram" ou "profanaram". Não culpar Rio Pax, Santa Casa ou Prefeitura; mostrar só a nota oficial.</li>
<li>Joias, herança, casa e a prima: sempre "segundo Padula" na tela. Não mostrar nome nem rosto dos primos herdeiros.</li>
<li>Aline Mohamad (peça): não associar à prima citada por Padula.</li>
<li>Nada de imagens reais de restos mortais, ossadas ou caixão aberto; só ambientação ilustrativa.</li>
<li>Trechos de A Praça É Nossa / Domingo Legal: usar no máximo poucos segundos, com crédito (risco de Content ID do SBT).</li>
<li>Thumbnail: sem rosto real ou gerado por IA de Jorge Lafond; preferir silhuetas e a peruca como símbolo.</li>'''
SEC=lambda h,i,c: f'<h2>{h} <button data-t="{i}">Copiar</button></h2><pre id="{i}">{html.escape(c)}</pre>'
open('Lafond_Pacote_Producao.html','w').write(f'''<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Pacote de Produção — Jorge Lafond</title>
<style>body{{background:#fff;color:#111;font-family:system-ui,Segoe UI,Arial,sans-serif;max-width:860px;margin:0 auto;padding:24px 16px;line-height:1.55}}h1{{font-size:24px}}h2{{font-size:19px;margin-top:32px;border-bottom:2px solid #eee;padding-bottom:4px}}pre{{white-space:pre-wrap;background:#f6f6f6;padding:12px;border-radius:6px;font-family:inherit}}table{{width:100%;border-collapse:collapse}}td{{border-bottom:1px solid #eee;padding:8px;vertical-align:top}}td.t{{font-weight:700;white-space:nowrap;width:60px}}.note{{color:#555;font-size:14px}}li{{margin-bottom:6px}}button{{font-size:13px;margin-left:8px}}</style></head><body>
<h1>Pacote de Produção: Jorge Lafond</h1>
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
