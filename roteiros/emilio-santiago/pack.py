import re, html
TITLE="Assim FOI a VIDA de EMÍLIO SANTIAGO — O Segredo REPUGNANTE Que Só Apareceu Depois da Morte"
files=['parte1.txt','parte2.txt','parte3.txt','parte4.txt','parte5.txt']
paras=[]
for f in files:
    for p in open(f).read().split('\n\n'):
        p=p.strip()
        if p: paras.append(re.sub(r'^[RA]: ','',p))
# voice html
body=''.join(f'<p>{html.escape(p)}</p>\n' for p in paras)
open('EmilioSantiago_Roteiro_Voz.html','w').write(f'''<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(TITLE)}</title>
<style>body{{background:#fff;color:#000;font-family:Georgia,serif;font-size:20px;line-height:1.7;max-width:760px;margin:0 auto;padding:32px 16px}}h1{{font-size:24px;line-height:1.3;margin-bottom:32px}}p{{margin:0 0 18px}}</style>
</head><body>
<h1>{html.escape(TITLE)}</h1>
{body}</body></html>''')
# chapters
CH=[('R: Emílio Santiago vendeu milhões','O segredo que só apareceu depois da morte','Emílio no palco cantando (arquivo, com crédito) × cemitério à noite · Texto: "ABRIRAM O CAIXÃO DELE"'),
('Março de dois mil e treze.','O último show','Fachada do Teatro Net Rio · Agenda de shows riscada · Corredor de hospital (ilustrativo)'),
('Seis de dezembro de mil novecentos e quarenta e seis.','O menino do Catete','Catete anos 50 (arquivo) · Berço vazio (ilustrativo)'),
('Nos anos sessenta, o menino do Catete','O diplomata que virou cantor','Faculdade Nacional de Direito (fachada) · Itamaraty · Palco de festival universitário anos 60'),
('Depois do festival, Emílio foi tentar a sorte','Calouro e crooner','Flávio Cavalcanti na TV Tupi (arquivo, com crédito) · Orquestra de baile anos 70 · Capa do LP de 1975'),
('Muito antes das frases difíceis','O nome falso','Compacto de vinil antigo com o nome "Teddy" em letreiro · Charles Gavin/Canal Brasil (trecho curto, com crédito)'),
('Mil novecentos e oitenta e oito.','Aquarela Brasileira','Capa do LP "Aquarela Brasileira" (2.º objeto) · Estúdio de gravação anos 80 · Roberto Menescal (arquivo)'),
('Com as "Aquarelas", Emílio ficou rico.','Dez milhões de reais','Fachadas genéricas: Flamengo, Copacabana, Petrópolis · Discos de platina'),
('Uma reportagem publicada na semana do AVC','A irmã na plateia','Plateia de teatro vista de trás (ilustrativo) · Frase "ele dizia que não tinha parentes" em letreiro'),
('A imprensa adorava Emílio.','"Prefiro não levantar bandeiras"','Frase de Emílio em letreiro · Porta de apartamento fechada (ilustrativo)'),
('Vinte e oito de junho de dois mil e treze.','O pedido secreto','Fachada do Tribunal de Justiça do RJ · Jornal O Dia (recorte, com crédito)'),
('Vinte e um de março de dois mil e treze.','O "filho" no velório','Câmara de Vereadores do Rio (fachada) · Duas crianças de mãos dadas, de costas (ilustrativo) · UTI (ilustrativo)'),
('Com três pessoas disputando a herança','A gravação','Gravador antigo e papel manuscrito (1.º objeto, ilustrativo)'),
('O professor se chamava Márcio Tadeu','O amor escondido','Duas taças numa mesa, casa vazia (ilustrativo) · Martelo de juiz · Letreiro "união estável reconhecida"'),
('Para entender por que um homem chega','Vinte de março','Calendário com 20 de março marcado duas vezes (2004 / 2013) · Roda de samba (arquivo genérico)'),
('Abril de dois mil e dezessete.','A exumação determinada','Manchetes de 2017 (com crédito) · Tela de vaquinha on-line (ilustrativo, sem dados reais)'),
('Vinte e sete de outubro de dois mil e vinte e dois.','O túmulo aberto','Cemitério Memorial do Carmo, Caju (fachada/portão) · Túmulo genérico fechado (3.º objeto), SEM restos mortais'),
('No começo de dois mil e vinte e três, Hercília','As acusações e Alcione','Documento com assinatura (4.º objeto, ilustrativo, sem nome legível) · Alcione (foto licenciada, com crédito)'),
('Trinta e um de janeiro de dois mil e vinte e três.','Zero por cento','Envelope de laboratório e laudo com "0%" (5.º objeto, ilustrativo)'),
('Na mesma entrevista em que afirmou','A profecia','Frase "a união só garante a questão jurídica" em letreiro · Caneta sobre papel em branco'),
('Agora junte todas as peças.','O lugar que ninguém teve','Montagem dos 5 objetos: gravador, LP Aquarela, túmulo, assinatura, laudo · Emílio cantando "Saigon" (trecho curto)'),
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
DESC='''Emílio Santiago vendeu milhões de discos cantando o amor e escondeu o dele a vida inteira. Depois da morte, uma herança de R$ 10 milhões virou guerra na Justiça: um companheiro secreto, uma irmã que ele dizia não ter e um suposto filho que mandou abrir o túmulo.

#EmílioSantiago #AquarelaBrasileira #Saigon'''
TAGS='emílio santiago, emilio santiago, emílio santiago herança, emílio santiago exumação, emílio santiago filho, emílio santiago companheiro, emílio santiago dna, emílio santiago morte, emílio santiago saigon, aquarela brasileira, emílio santiago vida, emílio santiago segredo, alcione emílio santiago, o que aconteceu com emílio santiago'
rows=''.join(f'<tr><td class="t">{t}</td><td><b>{html.escape(n)}</b><br>{html.escape(i)}</td></tr>\n' for t,n,i in out)
chap=html.escape('\n'.join(f'{t} {n}' for t,n,_ in out))
open('EmilioSantiago_Pacote_Producao.html','w').write(f'''<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Pacote de Produção — Emílio Santiago</title>
<style>body{{background:#fff;color:#111;font-family:system-ui,Segoe UI,Arial,sans-serif;max-width:860px;margin:0 auto;padding:24px 16px;line-height:1.55}}h1{{font-size:24px}}h2{{font-size:19px;margin-top:32px;border-bottom:2px solid #eee;padding-bottom:4px}}pre{{white-space:pre-wrap;background:#f6f6f6;padding:12px;border-radius:6px;font-family:inherit}}table{{width:100%;border-collapse:collapse}}td{{border-bottom:1px solid #eee;padding:8px;vertical-align:top}}td.t{{font-weight:700;white-space:nowrap;width:60px}}.note{{color:#555;font-size:14px}}li{{margin-bottom:6px}}</style></head><body>
<h1>Pacote de Produção: Emílio Santiago</h1>
<p><b>Título:</b> {html.escape(TITLE)}</p>
<h2>Descrição (SEO)</h2><pre>{html.escape(DESC)}</pre>
<h2>Tags</h2><pre>{html.escape(TAGS)}</pre><p class="note">{len(TAGS)} caracteres (limite do YouTube: 500).</p>
<h2>Capítulos (colar na descrição)</h2><pre>{chap}</pre>
<p class="note">Tempos calculados a 195 palavras por minuto (~{round(w/195)} min no total). Ajuste pelo áudio real depois de gravar.</p>
<h2>Lista de imagens para o editor</h2><table>{rows}</table>
<h2>Cuidados na edição</h2><ul>
<li>Orientação sexual: sempre com respeito, como "o amor que ele não pôde assumir". Nada de tom de escândalo nas imagens ou nos letreiros.</li>
<li>Exumação: nunca mostrar restos mortais, caixão aberto ou coisas do tipo. Usar portão do cemitério, túmulo fechado e laudo ilustrativo.</li>
<li>Márcio Tadeu, Hercília, Aleksander e Alcione estão vivos. Acusações sempre como "segundo Hercília" ou "segundo a defesa", sem sugerir culpa. Não há condenação.</li>
<li>Filhos de Aleksander (menores na época): nunca mostrar; usar só silhuetas ilustrativas.</li>
<li>Não mostrar documentos reais do processo (segredo de Justiça); só reproduções genéricas sem nomes legíveis.</li>
<li>Trechos de TV/shows (Canal Brasil, Flávio Cavalcanti, apresentações): curtos e com crédito.</li>
<li>Thumbnail: usar foto real licenciada de Emílio na silhueta; não gerar o rosto dele com IA.</li>
</ul>
<h2>Thumbnails</h2><p>Thumb1_ABRIRAM_O_CAIXAO_DELE.jpg · Thumb2_ELE_ESCONDEU_POR_18_ANOS.jpg (na mesma pasta). As silhuetas são espaço para as fotos reais.</p>
</body></html>''')
