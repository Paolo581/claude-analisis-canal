import re, html, json
TITLE="CLAUDINHO: A Verdade HORRÍVEL Sobre a Madrugada em Que Ele Morreu"
files=['parte1.txt','parte2.txt','parte3.txt','parte4.txt','parte5.txt']
raw=[p.strip() for f in files for p in open(f).read().split('\n\n') if p.strip()]
paras=[re.sub(r'^[RA]: ','',p) for p in raw]
open('voz.txt','w').write('\n\n'.join(paras)+'\n')
open('roteiro_completo.txt','w').write('\n\n'.join(raw)+'\n')
W=sum(len(p.split()) for p in paras)
body=''.join(f'<p>{html.escape(p)}</p>\n' for p in paras)
open('Claudinho_Roteiro_Voz.html','w').write(f'''<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(TITLE)}</title>
<style>body{{background:#fff;color:#000;font-family:Georgia,serif;font-size:20px;line-height:1.7;max-width:760px;margin:0 auto;padding:32px 16px}}h1{{font-size:24px;line-height:1.3;margin-bottom:32px}}p{{margin:0 0 18px}}</style>
</head><body>
<h1>{html.escape(TITLE)}</h1>
{body}</body></html>''')
CH=[('Claudinho passou as últimas horas','O pressentimento','Silhueta de cantor sozinho num palco escuro (ilustrativo)'),
('Para entender por que um homem','O menino de São Gonçalo','Ruas da periferia de São Gonçalo (arquivo, com crédito) · ônibus antigo'),
('O nome dele era Claucirlei.','Buchecha','Dois meninos em silhueta numa rua de terra (ilustrativo)'),
('Era o começo dos anos noventa.','O nascimento da dupla','Baile funk anos 90 (arquivo, com crédito)'),
('Mil novecentos e noventa e cinco.','Rap do Salgueiro','Morro do Salgueiro, São Gonçalo (arquivo, com crédito)'),
('O Rap do Salgueiro começou a tocar','Os milhões de discos','Disco de platina genérico · casa simples sendo entregue (ilustrativo)'),
('Na vida pessoal, Claudinho','A filha e o padrinho','Mãos de adulto segurando mão de bebê (ilustrativo)'),
('Dois mil e dois.','A turnê de 2002','Capa do disco Vamos Dançar (com crédito) · mapa Rio–Lorena'),
('Na semana antes daquele show','Os sinais da última semana','Pilha de CDs autografados sobre uma mesa (ilustrativo)'),
('Sexta-feira, doze de julho de dois mil e dois.','Ele não queria ir','Telefone tocando · chave de carro novo sobre a mesa (ilustrativo)'),
('O show aconteceu.','O último show','Palco pequeno com luz baixa, plateia em silhueta (ilustrativo)'),
('A madrugada de sábado começou.','A Serra das Araras','Estrada molhada de serra à noite, faróis (ilustrativo, sem acidente)'),
('Na descida da Serra das Araras','Quilômetro 202','Placa de quilometragem "202" na chuva (ilustrativo) · nada de imagens reais do carro'),
('Só que existe uma parte daquela sexta-feira','O que Buchecha guardou','Silhueta de homem de costas na beira de uma estrada ao amanhecer'),
('Domingo, catorze de julho de dois mil e dois.','O velório','Corredor de cemitério vertical (arquivo, com crédito) · letreiro "mais de mil pessoas"'),
('O enterro terminou.','Buchecha depois da tragédia','Microfone sozinho num pedestal (ilustrativo)'),
('Andressa cresceu sem o pai.','A festa de 15 anos','Salão de festa vazio com bolo (ilustrativo, sem rostos)'),
('Setembro de dois mil e vinte e três.','Nosso Sonho','Cartaz do filme Nosso Sonho (com crédito)'),
('Vinte e um anos depois da morte','A guerra pelo dinheiro','Pilha de documentos e partituras (ilustrativo) · letreiro "segundo a viúva"'),
('Os irmãos de Buchecha, Carla','As acusações','Tela de celular com post borrado (ilustrativo) · letreiro "nenhuma acusação foi decidida pela Justiça"'),
('Para responder essa pergunta','O processo','Fachada de fórum (arquivo) · letreiro "absolvido em 2006"'),
('Vanessa entrou na Justiça','O culpado','Árvore isolada à beira de uma pista molhada (ilustrativo) · letreiro "2 metros"'),
('Existe uma última ironia','A última ironia','Van em silhueta na estrada ao amanhecer'),
('A árvore explica o acidente.','O depois que nunca chegou','Dois meninos em silhueta de costas, cada um indo para um lado'),
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
DESC='''Claudinho passou as últimas horas da vida agindo como se soubesse que algo terrível ia acontecer. Na madrugada de 13 de julho de 2002, ele recusou a van do melhor amigo e voltou de Lorena num carro novo, comprado naquela mesma semana. Às 6h30, na Serra das Araras, o carro bateu numa árvore.

Neste vídeo: os sinais da última semana, os CDs autografados para a filha, a conversa que Buchecha só revelou anos depois, o velório em que um homem foi chamado de assassino, a briga entre a viúva, a afilhada e a família de Buchecha, e quem a Justiça apontou como o verdadeiro culpado.

Importante: o motorista Ivan Manzieri foi absolvido em 2006. As acusações entre a família de Claudinho, Buchecha, os irmãos de Buchecha e a editora ligada ao DJ Marlboro são atribuídas a quem as fez, nas reportagens citadas no vídeo, e nenhuma foi decidida pela Justiça.

{CHAPS}

#Claudinho #ClaudinhoeBuchecha #Buchecha'''.replace('{CHAPS}',CHAPS)
TAGS='claudinho, claudinho e buchecha, morte de claudinho, claudinho acidente, buchecha, claudinho 2002, serra das araras, nosso sonho filme, viúva de claudinho, filha de claudinho, rap do salgueiro, funk melody, assim foi a vida, claudinho documentário, claudinho e buchecha história'
assert len(TAGS)<=500, len(TAGS)
open('desc.txt','w').write(DESC+'\n'); open('tags.txt','w').write(TAGS+'\n')
rows=''.join(f'<tr><td class="t">{t}</td><td><b>{html.escape(n)}</b><br>{html.escape(i)}</td></tr>\n' for t,n,i in out)
CAUT='''<li>Ivan Manzieri foi absolvido: nunca usar letreiros como "culpado" ou "assassino" sobre ele, a não ser citando o grito da multidão no velório, entre aspas e com o contexto.</li>
<li>Nada de fotos reais do carro destruído, do corpo ou do local do acidente; usar só ambientação ilustrativa.</li>
<li>Briga das famílias: toda acusação com a fonte na tela ("segundo a viúva", "segundo os irmãos de Buchecha"), sempre com o letreiro de que nada foi decidido pela Justiça.</li>
<li>Editora ligada ao DJ Marlboro: não mostrar logotipo nem rosto do DJ Marlboro; a denúncia é da viúva e a editora não respondeu nas reportagens.</li>
<li>Músicas da dupla: evitar trechos (os direitos são justamente o centro da disputa e há risco de Content ID).</li>
<li>Andressa e Vanessa: usar só fotos de imprensa com crédito; Andressa criança, só silhueta.</li>
<li>Thumbnail: sem rosto real ou gerado por IA de Claudinho ou Buchecha; preferir silhuetas.</li>'''
SEC=lambda h,i,c: f'<h2>{h} <button data-t="{i}">Copiar</button></h2><pre id="{i}">{html.escape(c)}</pre>'
open('Claudinho_Pacote_Producao.html','w').write(f'''<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Pacote de Produção — Claudinho</title>
<style>body{{background:#fff;color:#111;font-family:system-ui,Segoe UI,Arial,sans-serif;max-width:860px;margin:0 auto;padding:24px 16px;line-height:1.55}}h1{{font-size:24px}}h2{{font-size:19px;margin-top:32px;border-bottom:2px solid #eee;padding-bottom:4px}}pre{{white-space:pre-wrap;background:#f6f6f6;padding:12px;border-radius:6px;font-family:inherit}}table{{width:100%;border-collapse:collapse}}td{{border-bottom:1px solid #eee;padding:8px;vertical-align:top}}td.t{{font-weight:700;white-space:nowrap;width:60px}}.note{{color:#555;font-size:14px}}li{{margin-bottom:6px}}button{{font-size:13px;margin-left:8px}}</style></head><body>
<h1>Pacote de Produção: Claudinho</h1>
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
