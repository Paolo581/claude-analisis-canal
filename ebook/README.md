# E-book: *The Hollywood Secret to Aging Beautifully*

Libro en inglés americano para mujeres estadounidenses de 65 años o más, pensado como regalo del canal nuevo de secretos y curiosidades de famosos. Subtítulo: *The Daily Habits of the Stars Who Stayed Sharp, Strong and Gorgeous Past 80, 90 and 100*.

## Qué es

Quince capítulos. Cada uno abre con una estrella que envejeció de forma admirable y cuenta su rutina real (qué come, cómo se mueve, qué hace al despertar, qué hizo cuando perdió la vista, la voz o al marido), con el tono de "secreto" del canal. Después explica en lenguaje sencillo qué dice la ciencia de esa costumbre y termina con **tres cosas que hacer esta semana**. Al final hay una rutina de mañana de una página, un plan suave de 30 días, las preguntas para llevar al médico y los teléfonos gratuitos de EE. UU.

| Parte | Capítulos |
|---|---|
| 1. Keep Moving | Dick Van Dyke (gimnasio a los 100), Helen Mirren (rutina de 12 minutos), Jane Fonda (fuerza y caídas) |
| 2. Eat Like a Star | Sophia Loren (dieta mediterránea y sueño), Betty White (moderación, humor, mascotas), Martha Stewart (jardín, verduras, azúcar) |
| 3. Skin, Hair and Style | Joan Collins (sol y piel), Iris Apfel (vestirse, color, zapatos seguros) |
| 4. A Sharp Mind | Olivia de Havilland (crucigramas, idiomas, oído), Kirk Douglas (ictus, señales FAST), Judi Dench (vista), Goldie Hawn (meditación) |
| 5. Heart and Spirit | Rita Moreno (depresión y terapia), Dolly Parton (propósito, fe, viudez), June Squibb (nunca es tarde) |

Extensión: unas 16.000 palabras, 101 páginas en formato 6×9 pulgadas con letra grande (14 pt en papel, 21 px en pantalla).

## Archivos

- `manuscrito/` — un archivo Markdown por capítulo, numerados. Edita aquí.
- `construir.py` — une los capítulos y genera `salida/libro.md`, `salida/libro.html` (letra grande, modo oscuro automático) y `salida/libro.pdf` (Chromium). Ejecutar `python3 ebook/construir.py`.
- `salida/` — los archivos listos para entregar.

## Antes de publicarlo

1. **Sustituir `[CHANNEL NAME]`** (aparece en la portada, la bienvenida y la despedida) por el nombre del canal, y añadir el enlace al canal en la última página.
2. **Portada.** No está hecha. Idea: fondo crema, título en serif granate como el interior, y un collage o ilustración de siluetas de estrellas clásicas; o una sola imagen de archivo libre de derechos de una mujer mayor elegante con sombrero (guiño al capítulo de Joan Collins). Evitar fotos reales de las estrellas (derechos de imagen).
3. **Comprobar estos datos**, que escribí de memoria y conviene confirmar antes de imprimir:
   - Dick Van Dyke: cumplió 100 el 13 de diciembre de 2025; va al gimnasio tres días por semana con Arlene; se casaron en 2012.
   - Helen Mirren: la rutina es el plan XBX de la Royal Canadian Air Force (12 minutos); la foto del bikini rojo es de 2008.
   - Jane Fonda: prótesis de cadera y rodilla; dejó el alcohol en sus ochenta; linfoma en 2022.
   - Sophia Loren: *Women & Beauty* (1984); nueve horas de sueño; *The Life Ahead* (2020) a los 86.
   - Betty White: murió el 31 de diciembre de 2021, 17 días antes de cumplir 100; perritos calientes, patatas, regaliz rojo y vodka; crucigramas a diario; Allen Ludden murió en 1981.
   - Martha Stewart: portada de *Sports Illustrated* en mayo de 2023 a los 81; zumo verde diario; Pilates; cinco meses de prisión federal en 2004-2005.
   - Joan Collins: "nunca tomé el sol"; *The Joan Collins Beauty Book* (1980); boda con Percy Gibson en 2002; 92 años en 2026.
   - Iris Apfel: exposición del Met en 2005 a los 84; contrato con IMG en 2019 a los 97; murió el 1 de marzo de 2024 a los 102.
   - Olivia de Havilland: demanda contra FX por *Feud* en 2017 a los 101 (perdió); murió en julio de 2020 a los 104; crucigrama diario; lectora en la American Cathedral de París; "love, laughter and light".
   - Kirk Douglas: ictus en enero de 1996 a los 79; *My Stroke of Luck* (2002); más de 400 parques infantiles; murió en febrero de 2020 a los 103; 65 años casado con Anne.
   - Judi Dench: degeneración macular anunciada en 2012; tatuaje "Carpe Diem" a los 81; nominación al Óscar por *Belfast* a los 87; Michael Williams murió en 2001.
   - Goldie Hawn: medita desde 1972; *10 Mindful Minutes* (2011); con Kurt Russell desde 1983.
   - Rita Moreno: intento de suicidio en 1961 contado en su memoria (2013); 45 años casada con Leonard Gordon; EGOT; *West Side Story* (2021) como productora ejecutiva.
   - Dolly Parton: se levanta a las 3; boda con Carl Dean el 30 de mayo de 1966; Carl murió el 3 de marzo de 2025; Imagination Library desde 1995, más de 200 millones de libros.
   - June Squibb: *Thelma* (2024) a los 94, primer papel protagonista, hizo sus escenas en el scooter; *Eleanor the Great* (2025) dirigida por Scarlett Johansson.
   - Ciencia citada: 1 de cada 4 mayores de 65 se cae cada año (CDC); audífonos y deterioro cognitivo (ensayo ACHIEVE, 2023); verduras de hoja y cerebro "11 años más joven" (estudio MAP de Chicago, 2018); creencias positivas sobre la vejez y 7,5 años más de vida (Levy, Yale, 2002); bilingüismo y unos 4 años de retraso de la demencia.
   - Teléfonos: 988; Eldercare Locator 1-800-677-1116; 1-800-QUIT-NOW; 1-800-MEDICARE; Alzheimer's Association 1-800-272-3900.
4. **Aviso legal.** Está en la primera página. Si lo vendes en Amazon, conviene que lo revise alguien, porque el libro da consejos de salud.

## Cómo usarlo

- **Regalo a cambio del correo.** Enlace en la descripción de cada vídeo y comentario fijado: "Free book: the daily habits of the stars who lived past 100". Una página sencilla con el formulario y el PDF.
- **Amazon KDP.** El PDF ya está en 6×9. Para Kindle, sube `salida/libro.html` o el Markdown convertido a EPUB con pandoc (`pandoc salida/libro.md -o libro.epub`).
- **Vídeos.** Cada capítulo es también un guion corto: "At 100, Dick Van Dyke still goes to the gym. This is his morning", "The one thing Joan Collins refused to do for 70 years". Sirven como vídeos de 8 a 12 minutos entre los documentales largos.
- **Comentarios.** El libro pide al final que digan qué capítulo les ayudó y qué estrella quieren ver. Es la forma de medir qué personajes funcionan.

## Página de ventas (`web/`)

- `web/index.html` — la página completa, lista para subir a cualquier hosting (Netlify, Vercel, Hostinger, Lovable…). Un solo archivo, sin dependencias salvo las fuentes de Google.
- `web/body.html` — la misma página sin la cabecera HTML, que es la que se publica como artifact de Claude para previsualizar.
- Estructura calcada de la página de Car Care Garage: barra con botón, titular con cifra, precio, tres «dónde se pierden los años», qué hay dentro (las cinco partes y las 15 estrellas), tarjeta de oferta, por qué lo escribimos, garantía de 60 días, «última llamada» con y sin el libro, preguntas frecuentes y pie con aviso legal.
- **Antes de publicarla:** (1) sustituir `[CHANNEL NAME]`; (2) pegar el enlace de pago de Payhip o Gumroad en la variable `BUY_URL` del `<script>` final, que rellena todos los botones de compra; (3) revisar el precio, que está puesto en 19 $ con 29 $ tachados, y cambiarlo en los cuatro sitios donde aparece si decides otro; (4) si tienes una portada real, sustituir el mockup de libro de la cabecera (bloque `.book`) por una imagen.
