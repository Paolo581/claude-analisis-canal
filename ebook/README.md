# Behind the Fame: la biblioteca de tres libros

Tres e-books en inglés americano para mujeres estadounidenses de 65 años o más, vendidos sueltos a 19 $ y en pack a 37 $, desde el canal **Behind the Fame** (secretos y curiosidades de famosos).

| | Libro | Qué es | Páginas |
|---|---|---|---|
| 1 | *The Hollywood Secret to Aging Beautifully* | Las rutinas diarias reales de 15 estrellas que llegaron bien a los 80, 90 y 100 (Dick Van Dyke, Helen Mirren, Jane Fonda, Sophia Loren, Betty White, Martha Stewart, Joan Collins, Iris Apfel, Olivia de Havilland, Kirk Douglas, Judi Dench, Goldie Hawn, Rita Moreno, Dolly Parton, June Squibb), lo que dice la ciencia de cada hábito y tres cosas que hacer esa semana. Rutina de mañana y plan de 30 días. | 100 |
| 2 | *The Hollywood Plate* | Lo que comen de verdad 8 estrellas delgadas y fuertes (Sophia Loren, Audrey Hepburn, Julia Child, Jane Fonda, Betty White, Martha Stewart, Dolly Parton, Clint Eastwood), 26 recetas para una o dos personas, cómo perder peso después de los 65 sin perder músculo, y un menú de 4 semanas con listas de la compra. | 82 |
| 3 | *The Golden Years Love Story* | Cómo las estrellas encontraron amor, amistad y compañía después de los 65 (Dick Van Dyke a los 86, Joan Collins a los 68, Carol Burnett, Jane Fonda, Dolly y Carl, Betty White, Diane Keaton): citas con reglas de seguridad, matrimonio largo y jubilación, cuidar al marido enfermo, viudez, hacer amigas a los 70, ser la abuela a la que llaman, y vivir bien sola. Lista de citas seguras, preguntas antes de casarse tarde y plan de 30 días. | 76 |

Cada capítulo abre con la historia real de una estrella, en el tono de "secreto" del canal, y termina con consejos prácticos y tres cosas que hacer esa semana. Letra grande, formato 6×9 pulgadas.

## Archivos

- `libros/<slug>/manuscrito/` — un archivo Markdown por capítulo. Edita aquí.
- `libros/<slug>/salida/` — `libro.md`, `libro.html` (letra grande, modo oscuro automático) y `libro.pdf` listos para entregar.
- `construir.py` — regenera los tres: `python3 ebook/construir.py` (o `python3 ebook/construir.py hollywood-plate` para uno).
- `web/index.html` — la página de ventas completa, un solo archivo, lista para subir a cualquier hosting. `web/body.html` es la misma sin cabecera HTML, publicada como artifact para previsualizar.
- `payhip-ficha.md` — nombre, precio y descripción de los cuatro productos para pegar en Payhip, y cómo crear el pack.
- `cta.md` — el clip hablado del minuto 3, la línea 1 de la descripción del vídeo y del canal, y el cierre fijo, copiados del sistema de Car Care Garage.

## Antes de publicar

1. **Pago.** Crear los cuatro productos en Payhip con `payhip-ficha.md` y pegar los cuatro enlaces en el objeto `BUY` del `<script>` final de `web/index.html`. Cada botón usa el enlace de su producto.
2. **Precios.** 19 $ por libro (29 $ tachados) y 37 $ el pack (57 $ tachados). Están en la web y en las fichas; si cambias uno, cámbialo en los dos sitios.
3. **Portadas.** No están hechas. Recomendado 1600 × 2400 px, sin fotos reales de las estrellas (derechos de imagen); la web usa mockups tipográficos que se pueden sustituir por imágenes en el bloque `.stack`.
4. **Datos.** Las fechas, cifras y anécdotas están escritas de memoria, sin verificar en internet. Antes de imprimir conviene confirmar al menos: fechas de bodas y muertes (Carl Dean, 3 de marzo de 2025; Diane Keaton, octubre de 2025; Dick Van Dyke 100 años en diciembre de 2025), las cifras de estudios citados (CDC caídas, estudio de Harvard, estudio de Chicago sobre verduras, Yale sobre actitud ante la vejez) y los teléfonos de ayuda (988, 1-800-677-1116, 877-908-3360, 800-272-3900, 1-800-772-1213, 1-800-799-7233).
5. **Aviso legal.** Cada libro lleva uno en la primera página y la web en el pie. Si lo vendes, que lo revise alguien, porque los libros dan consejos de salud, dieta y relaciones.

## Cómo usarlo

- **Regalo a cambio del correo:** uno de los tres libros gratis (el primero es el más general) enlazado en la descripción de cada vídeo, y el pack de pago en la web.
- **Amazon KDP:** los PDF ya están en 6×9. Para Kindle, `pandoc libros/<slug>/salida/libro.md -o libro.epub`.
- **Vídeos cortos:** cada capítulo es un guion de 8 a 12 minutos ("At 100, Dick Van Dyke still goes to the gym", "Sophia Loren eats pasta every day. This is her plate", "Dick Van Dyke found love at 86").
- **Comentarios:** los tres libros terminan pidiendo que digan qué capítulo les sirvió y qué estrella quieren ver, para medir qué personajes funcionan.
