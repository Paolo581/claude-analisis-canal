import re, html
TITLE="Assim FOI a VIDA de ERASMO CARLOS — O HORRÍVEL Segredo Que Ele Levou Para o Túmulo"
files=['parte1.txt','parte2.txt','parte3.txt','parte4.txt','parte5.txt','parte6.txt']
raw=[]
for f in files:
    for p in open(f).read().split('\n\n'):
        p=p.strip()
        if p: raw.append(p)
paras=[re.sub(r'^[RA]: ','',p) for p in raw]
open('voz.txt','w').write('\n\n'.join(paras)+'\n')
W=sum(len(p.split()) for p in paras)
body=''.join(f'<p>{html.escape(p)}</p>\n' for p in paras)
open('Erasmo_Roteiro_Voz.html','w').write(f'''<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(TITLE)}</title>
<style>body{{background:#fff;color:#000;font-family:Georgia,serif;font-size:20px;line-height:1.7;max-width:760px;margin:0 auto;padding:32px 16px}}h1{{font-size:24px;line-height:1.3;margin-bottom:32px}}p{{margin:0 0 18px}}</style>
</head><body>
<h1>{html.escape(TITLE)}</h1>
{body}</body></html>''')
CH=[('Erasmo Carlos foi o Tremendão','A maldição do Tremendão','Silhueta de cantor grande com violão sob holofote · Casa à noite com uma janela acesa'),
('Cinco de junho de mil novecentos e quarenta e um.','O menino sem pai','Casarão antigo da Tijuca (arquivo/banco de imagens) · Porta de madeira fechada'),
('Havia uma rua na Tijuca','A Turma do Matoso','Placa da Rua do Matoso · Fotos de imprensa de Tim Maia e Jorge Ben jovens (com crédito)'),
('Era a segunda metade dos anos cinquenta.','Elvis e Roberto','Disco de Elvis (ilustrativo) · Papel com letra escrita à mão (sem reproduzir letra real)'),
('Carlos Imperial enxergou','O Tremendão','Trechos curtos da Jovem Guarda na TV Record (arquivo, com crédito)'),
('Mil novecentos e sessenta e sete.','A briga com Roberto','Fita de rolo antiga (ilustrativo) · Letreiro "Eu Sou Terrível"'),
('Mil novecentos e setenta.','A ditadura','Relatório datilografado genérico com carimbo "CENSURA" (sem simular documento real)'),
('Foi nos anos setenta que uma mulher','Narinha','Fotos públicas de Erasmo e Narinha (com crédito) · Jardim'),
('Mas, dentro daquela casa, havia um armário.','O armário','Porta de armário entreaberta na penumbra (ilustrativo, sem arma)'),
('Os anos setenta foram de reinvenção','Detalhes','Capas de Carlos, Erasmo e Sonhos e Memórias (com crédito)'),
('Em mil novecentos e oitenta e um, ele lançou','Mulher','Capa do disco Mulher (com crédito)'),
('Mil novecentos e oitenta e quatro.','Roberta Close e o boato','Capa da Manchete (com crédito) · Bancas de jornal anos 80'),
('Era uma segunda-feira.','4 de junho de 1984','Escada de casa vazia · Letreiro "04/06/1984"'),
('Narinha tinha sido atingida','O barulho','Tela preta com letreiro · Corredor de hospital (sem pessoas feridas)'),
('Para entender aquela decisão','Rock in Rio 1985','Imagens de arquivo do Rock in Rio 1985 (com crédito)'),
('Dezembro de mil novecentos e noventa e cinco.','Um dia depois do Natal','Árvore de Natal apagada · Letreiro "26/12/1995"'),
('Erasmo recebeu a notícia','A pergunta sem resposta','Violão encostado num quarto vazio'),
('Em dois mil e quatro, perdeu a mãe.','Mãe e pai','Foto pública de Erasmo com a mãe, se houver (com crédito)'),
('Dois anos depois, em outubro de dois mil e onze','A volta ao Rock in Rio','Imagens do Rock in Rio 2011 com Arnaldo Antunes (com crédito)'),
('O nome dela era Fernanda.','Fernanda','Fotos públicas do casal (com crédito) · Letreiro "06/01/2019"'),
('Sete de maio de dois mil e catorze.','Alexandre','Avenida à beira-mar de madrugada · Capacete no asfalto (ilustrativo)'),
('Outubro de dois mil e vinte e dois.','O Grammy','Troféu do Grammy Latino (imagem de imprensa) · Capa do disco'),
('Na segunda-feira, vinte e um de novembro','O mesmo hospital','Fachada do hospital (vista pública) · Letreiro "22/11/2022"'),
('Para entender essa guerra','A herança','Cofre e papéis sobre mesa (ilustrativo) · Letreiro "R$ 15 a 25 milhões"'),
('Vinte e dois de novembro de dois mil e vinte e dois.','O extrato','Extrato bancário borrado (ilustrativo, sem dados reais) · Letreiro "ALEGAÇÃO DOS FILHOS"'),
('Em agosto de dois mil e vinte e seis','O arquivamento','Fachada do MPRJ (vista pública) · Letreiro "MP arquivou"'),
('Existe um nome nessa história','Roberto Carlos','Fita de rolo (callback) · Foto de imprensa de Roberto (com crédito)'),
('Só que ainda falta a última peça.','A última peça','Gaveta de escritório vazia · Folha em branco'),
('Existe uma coisa que esta história ensina','O que não se diz','Mão escrevendo um bilhete (banco de imagens)'),
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
DESC='''Erasmo Carlos foi o Tremendão, o parceiro inseparável de Roberto Carlos e um dos homens mais amados do Brasil. Mas, longe dos palcos, uma tragédia atrás da outra atingiu as pessoas que ele mais amava. O menino que cresceu sem pai na Tijuca, o tiro dentro de casa em 1984, a morte de Narinha em 1995, o acidente do filho Alexandre em 2014, o Grammy Latino cinco dias antes de morrer e a guerra pela herança que começou no dia da morte dele.

Sobre 1984: segundo as reportagens da época, a própria Narinha confirmou que o tiro foi um acidente, e a polícia não abriu investigação. Sobre a herança: a transferência de R$ 300 mil é uma alegação dos filhos de Erasmo; em agosto de 2026 o Ministério Público do Rio decidiu não abrir investigação contra a viúva, Fernanda, que nunca foi acusada formalmente de nenhum crime. O depoimento de Roberto Carlos foi noticiado pela revista IstoÉ com base em fontes não identificadas, num processo em segredo de Justiça. A minuta de testamento desaparecida foi noticiada pela coluna Gente, da revista Veja.

Se você ou alguém próximo está passando por um momento difícil, procure ajuda. O CVV atende de graça, 24 horas, pelo telefone 188 ou pelo site cvv.org.br.

{CHAPS}

#ErasmoCarlos #JovemGuarda #HistóriaReal'''.replace('{CHAPS}',CHAPS)
TAGS='erasmo carlos, erasmo carlos segredo, erasmo carlos história, erasmo carlos biografia, erasmo carlos narinha, erasmo carlos filho alexandre, erasmo carlos herança, erasmo carlos testamento, erasmo carlos roberto carlos, erasmo carlos fernanda, erasmo carlos morte, tremendão, jovem guarda, minha fama de mau'
assert len(TAGS)<=500, len(TAGS)
open('desc.txt','w').write(DESC+'\n'); open('tags.txt','w').write(TAGS+'\n')
rows=''.join(f'<tr><td class="t">{t}</td><td><b>{html.escape(n)}</b><br>{html.escape(i)}</td></tr>\n' for t,n,i in out)
CAUT='''<li>Tiro de 1984: sempre como acidente, confirmado pela própria Narinha. Nunca mostrar arma apontada, encenação de disparo ou pessoa ferida. Nunca usar imagem de Erasmo junto da palavra "tiro" como se ele fosse responsável.</li>
<li>Suicídio de Narinha: não mostrar veneno, frasco ou método. Manter o CVV 188 na descrição e num letreiro final.</li>
<li>Fernanda: sempre com letreiro "alegação dos filhos" nos R$ 300 mil e "MP arquivou" logo em seguida. Nunca usar trilha de suspense ou zoom dramático sobre o rosto dela.</li>
<li>Roberto Carlos: o depoimento é "segundo a IstoÉ, com fontes não identificadas". Nada de letreiros como "traição" ou "contra os filhos".</li>
<li>Roberta Close: deixar claro na tela que o caso nunca existiu.</li>
<li>Alexandre: sem simular acidente com pessoa; usar só avenida vazia e capacete.</li>
<li>Rostos reais: só fotos de imprensa ou arquivo com crédito; nunca rosto gerado por IA.</li>
<li>Músicas de Erasmo e Roberto: só trechos de poucos segundos; preferir trilha livre de direitos.</li>'''
SEC=lambda h,i,c: f'<h2>{h} <button data-t="{i}">Copiar</button></h2><pre id="{i}">{html.escape(c)}</pre>'
open('Erasmo_Pacote_Producao.html','w').write(f'''<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Pacote de Produção — Erasmo Carlos</title>
<style>body{{background:#fff;color:#111;font-family:system-ui,Segoe UI,Arial,sans-serif;max-width:860px;margin:0 auto;padding:24px 16px;line-height:1.55}}h1{{font-size:24px}}h2{{font-size:19px;margin-top:32px;border-bottom:2px solid #eee;padding-bottom:4px}}pre{{white-space:pre-wrap;background:#f6f6f6;padding:12px;border-radius:6px;font-family:inherit}}table{{width:100%;border-collapse:collapse}}td{{border-bottom:1px solid #eee;padding:8px;vertical-align:top}}td.t{{font-weight:700;white-space:nowrap;width:60px}}.note{{color:#555;font-size:14px}}li{{margin-bottom:6px}}button{{font-size:13px;margin-left:8px}}</style></head><body>
<h1>Pacote de Produção: Erasmo Carlos</h1>
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
