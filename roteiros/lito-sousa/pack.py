import re, html
TITLE="O Que ACONTECEU com LITO SOUSA? O Diagnóstico CRUEL Que Chocou o Brasil"
files=['parte1.txt','parte2.txt','parte3.txt','parte4.txt','parte5.txt']
paras=[]
for f in files:
    for p in open(f).read().split('\n\n'):
        p=p.strip()
        if p: paras.append(re.sub(r'^[RA]: ','',p))
# voice html
body=''.join(f'<p>{html.escape(p)}</p>\n' for p in paras)
open('LitoSousa_Roteiro_Voz.html','w').write(f'''<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(TITLE)}</title>
<style>body{{background:#fff;color:#000;font-family:Georgia,serif;font-size:20px;line-height:1.7;max-width:760px;margin:0 auto;padding:32px 16px}}h1{{font-size:24px;line-height:1.3;margin-bottom:32px}}p{{margin:0 0 18px}}</style>
</head><body>
<h1>{html.escape(TITLE)}</h1>
{body}</body></html>''')
# chapters
CH=[('R: Lito Sousa passou mais de trinta anos','A notícia mais cruel','Lito no hangar/cabine (foto real licenciada) × corredor de hospital à noite · Texto: "O DIAGNÓSTICO CRUEL"'),
('Vinte e cinco de janeiro de mil novecentos e sessenta e sete.','O menino Joselito','Natal anos 60 (arquivo) · Estrada Paraíba–RN (ilustrativo)'),
('Nos anos noventa, Lito recebeu uma missão','Os aviões do Zaire','Lockheed Electra da Varig (arquivo, com crédito) · Capa do livro "Onde Morrem os Aviões" (1.º objeto)'),
('Em dois mil e quatro, Lito abriu um blog.','Aviões e Músicas','Prints antigos do blog/canal (com crédito)'),
('Março de dois mil e vinte.','O tio do Brasil','Aeroportos vazios na pandemia (arquivo) · Lito explicando em vídeo (trecho curto, com crédito)'),
('Lito voltou às tragédias','As quedas que ele explicou','Manchetes antigas dos acidentes (recortes, com crédito) · Nada de imagens de vítimas ou destroços com corpos'),
('Cinco de novembro de dois mil e vinte e um.','Marília Mendonça','Cachoeira de Piedade de Caratinga (paisagem) · Trecho curto do vídeo de Lito (com crédito)'),
('Ainda em dois mil e vinte e um, Lito realizou','Decola Lito','Licença de piloto (2.º objeto, ilustrativo) · Trechos da série "Decola Lito" (com crédito)'),
('Lito foi parar numa UTI.','O primeiro aviso','Corredor de UTI desfocado · Letreiro "2025 · duas pneumonias"'),
('Até que, no dia dezenove de julho','Manutenção, não queda','Trecho curto do vídeo de 19/07 (com crédito) · Letreiro "Estou em manutenção, não em queda"'),
('Vinte de julho de dois mil e vinte e seis.','A internação','Fachada do Hospital Einstein (arquivo) · Letreiro "inflamação no sistema nervoso central"'),
('Vinte e um de agosto de dois mil e vinte e seis.','O diagnóstico','Post de Mila (print sem dados pessoais) · Animação simples de proteína dobrando (sem gore)'),
('Mila não esperou.','Me ajudem','Celular com comentário "Preciso salvar o amor da minha vida" (recriado, sem marca) · Letreiros "Ionis: não · Broad: grupo de controle · Harvard: 20/10"'),
('Primeiro de setembro de dois mil e vinte e seis.','Cuidados paliativos','Casa à noite com luz acesa (ilustrativo) · Letreiro "Eu vou ser o primeiro no mundo"'),
('A: Enquanto Lito estava em casa','A corrida pelo remédio','Laboratório (banco de imagens) · Letreiro "ALN-6457 · nunca usado em humanos"'),
('A: No dia quatro de setembro, uma sexta-feira','Autorização da Anvisa','Fachada da Anvisa (arquivo) · Letreiro "04/09"'),
('Madrugada de doze de setembro','A caixa de Nova York','Aeroporto de Guarulhos à noite · Helicóptero sobre São Paulo (banco de imagens) · Caixa térmica (3.º objeto, ilustrativo)'),
('O remédio foi aplicado.','O primeiro do mundo','Leito de hospital desfocado, sem paciente identificável · Letreiro "sem intercorrências"'),
('A: Por volta de vinte e um de setembro.','Os ataques a Mila','Carro com placa "vende-se" (ilustrativo) · Comentários genéricos borrados'),
('Vinte e três de setembro.','Zero','Stories de Mila (trecho curto, com crédito) · Letreiro "Não tem nenhuma melhora. Zero."'),
('Segunda-feira, vinte e oito de setembro','O vídeo feito por IA','Trecho do vídeo com o aviso "conteúdo feito com IA" sempre visível (4.º objeto)'),
('Agora junte todas as peças.','Silêncio e tempo','Montagem dos 4 objetos: livro, licença, caixa, vídeo'),
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
DESC='''Lito Sousa passou mais de 30 anos consertando aviões e ensinando o Brasil a entender por que eles caem. Em 2026, foi ele quem recebeu o diagnóstico mais cruel da própria vida: a doença de Creutzfeldt-Jakob. Nesta história: o remédio que nenhum ser humano tinha recebido antes, os ataques contra a esposa Mila Seidl e o vídeo feito com inteligência artificial que dividiu os fãs.

Informações atualizadas até o fim de setembro de 2026, com base em declarações públicas da família e reportagens. Este vídeo não traz orientação médica. Faça seus exames de rotina.

#LitoSousa #AviõesEMúsicas #MilaSeidl'''
TAGS='lito sousa, lito sousa doença, aviões e músicas, mila seidl, creutzfeldt-jakob, lito sousa diagnóstico, lito sousa remédio experimental, lito sousa vídeo ia, o que aconteceu com lito sousa, lito sousa câncer, lito sousa hoje, doença rara, aviação'
rows=''.join(f'<tr><td class="t">{t}</td><td><b>{html.escape(n)}</b><br>{html.escape(i)}</td></tr>\n' for t,n,i in out)
chap=html.escape('\n'.join(f'{t} {n}' for t,n,_ in out))
open('LitoSousa_Pacote_Producao.html','w').write(f'''<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Pacote de Produção — Lito Sousa</title>
<style>body{{background:#fff;color:#111;font-family:system-ui,Segoe UI,Arial,sans-serif;max-width:860px;margin:0 auto;padding:24px 16px;line-height:1.55}}h1{{font-size:24px}}h2{{font-size:19px;margin-top:32px;border-bottom:2px solid #eee;padding-bottom:4px}}pre{{white-space:pre-wrap;background:#f6f6f6;padding:12px;border-radius:6px;font-family:inherit}}table{{width:100%;border-collapse:collapse}}td{{border-bottom:1px solid #eee;padding:8px;vertical-align:top}}td.t{{font-weight:700;white-space:nowrap;width:60px}}.note{{color:#555;font-size:14px}}li{{margin-bottom:6px}}</style></head><body>
<h1>Pacote de Produção: Lito Sousa</h1>
<p><b>Título:</b> {html.escape(TITLE)}</p>
<h2>Descrição (SEO)</h2><pre>{html.escape(DESC)}</pre>
<h2>Tags</h2><pre>{html.escape(TAGS)}</pre><p class="note">{len(TAGS)} caracteres (limite do YouTube: 500).</p>
<h2>Capítulos (colar na descrição)</h2><pre>{chap}</pre>
<p class="note">Tempos calculados a 195 palavras por minuto (~{round(w/195)} min no total). Ajuste pelo áudio real depois de gravar.</p>
<h2>Lista de imagens para o editor</h2><table>{rows}</table>
<h2>Cuidados na edição (Lito está vivo e gravemente doente)</h2><ul>
<li>Nunca prever morte, prazo de vida ou usar trilha/gráfico de "luto". Não usar a palavra "último" sobre ele.</li>
<li>Conteúdo médico: só o que a família e os órgãos oficiais divulgaram. Nada de "cura", "melhora" ou "remédio milagroso" em letreiros.</li>
<li>Não mostrar Lito em momentos de fragilidade (espasmos, leito). Usar fotos públicas dele saudável, com crédito.</li>
<li>Não mostrar o rosto do filho (menor).</li>
<li>Ataques à Mila: comentários sempre borrados e genéricos, sem expor perfis.</li>
<li>Vídeo com IA: se usar trecho, manter o aviso "feito com IA" visível o tempo todo.</li>
<li>Acidentes aéreos: sem imagens de vítimas ou destroços com corpos.</li>
<li>Antes de publicar: conferir as notícias do dia (o quadro muda rápido; dia 20/10 abre o estudo de Harvard).</li>
<li>Thumbnail: foto real licenciada; nunca rosto gerado por IA.</li>
</ul>
<h2>Thumbnails</h2><p>Thumb1_A_DOENCA_QUE_NINGUEM_CURA.jpg · Thumb2_AGORA_A_TRAGEDIA_E_DELE.jpg (na mesma pasta). Sem rostos: a Thumb1 usa silhueta de mecânico; recomenda-se trocar pela foto real licenciada do Lito no hangar.</p>
</body></html>''')
