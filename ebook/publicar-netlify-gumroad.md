# Publicar la web y cobrar: Netlify + Gumroad

Sistema del vídeo *Create and Sell An Ebook* (enlaces mencionados: netlify.com y Gumroad), aplicado a la biblioteca de Behind the Fame. Dos piezas y nada más:

| Pieza | Herramienta | Qué hace | Coste |
|---|---|---|---|
| La página de ventas | **Netlify** (Netlify Drop) | Sirve `web/index.html` en una URL con HTTPS. Se sube arrastrando la carpeta, sin servidor ni código. | Plan gratuito (300 créditos, unos 15 GB de tráfico; la web pesa 30 KB, así que da para cientos de miles de visitas) |
| El cobro y la entrega del PDF | **Gumroad** | Aloja los PDF, cobra con tarjeta o PayPal, entrega el archivo, gestiona devoluciones y, desde 2025, los impuestos (es *merchant of record*). | Sin cuota mensual. 10 % + 0,50 $ por venta que llegue desde tu enlace. 30 % si la venta llega desde su buscador «Discover» |

Comparado con Payhip (la opción de `payhip-ficha.md`): Payhip cobra 5 % en el plan gratuito y también hace de *merchant of record*. Gumroad cuesta el doble por venta, pero su *overlay* (la ventana de pago que se abre encima de tu web, sin salir de ella) y su checkout son los más probados con público estadounidense mayor. Las fichas de producto sirven igual para los dos: lo que cambia es dónde se pegan. Si eliges Payhip, salta el bloque 1 y usa `payhip-ficha.md`; el resto de esta guía (Netlify, enlaces en `BUY`, descripción) es idéntico.

Lo que se gana con 19 $ y 37 $ en Gumroad:

| Producto | Precio | Comisión (10 % + 0,50 $) | Te queda |
|---|---|---|---|
| Un libro | 19,00 $ | 2,40 $ | 16,60 $ |
| Pack de tres | 37,00 $ | 4,20 $ | 32,80 $ |

Gumroad descuenta además la comisión del procesador de pago (Stripe o PayPal) en algunos países; confírmalo en tu panel tras la primera venta.

---

## 1. Gumroad: los cuatro productos (30 minutos)

### 1.1 Cuenta
1. Entra en **gumroad.com** → *Start selling*. Cuenta con el correo del canal.
2. **Settings → Profile**: nombre «Behind the Fame», la misma foto que el canal, y en *Username* algo corto, por ejemplo `behindthefame`. Tu tienda quedará en `behindthefame.gumroad.com`.
3. **Settings → Payments**: país, datos de pago (cuenta bancaria o PayPal) y los datos fiscales que pida. Sin esto puedes publicar, pero no cobrar.

### 1.2 Los tres libros
Para cada libro, **Products → New product**:

1. **Type:** *E-book* (o *Digital product*; a efectos de entrega es lo mismo, *E-book* añade el lector dentro de Gumroad).
2. **Name** y **Price:** copia los de `payhip-ficha.md` (19 $). Activa *Allow customers to pay what they want* **no**; lo que sí conviene es poner el precio tachado: en la sección *Pricing* no existe «compare at», así que el 29 $ tachado va solo en la web.
3. **Next: Customize**. En *Description* pega la descripción larga de la ficha más el texto común (garantía de 60 días, aviso legal). Deja los párrafos cortos: la ficha ya está escrita en frases de una línea para letra grande.
4. **Cover:** 1600 × 2400 px no encaja en Gumroad; su portada de producto es horizontal. Usa **1280 × 720 px** (o 2560 × 1440) con el título del libro en letra grande sobre fondo oscuro, misma paleta que la web (`#2a1216`, dorado `#d9a441`, naranja `#c2531f`). Sin fotos reales de las estrellas (derechos de imagen). Una miniatura cuadrada opcional de 600 × 600 px para la tienda.
5. **Content:** sube `libros/<slug>/salida/libro.pdf`. Cada PDF pesa menos de 5 MB; Gumroad admite hasta 5 GB. Marca *PDF stamping* si quieres que cada copia lleve el correo del comprador (desincentiva compartirlo).
6. **Receipt / Thank-you note:** una frase: «Thank you. Your book is attached. If anything in it helps you this week, write to me and tell me which chapter.» Es el mismo pedido de comentarios con que terminan los tres libros.
7. **Settings del producto:** *Allow refunds* dentro de 60 días (la ficha promete 60 días; Gumroad por defecto permite reembolso manual sin límite, así que basta con cumplirlo). URL del producto: `aging-beautifully`, `hollywood-plate`, `love-story`.
8. **Publish**. Copia la URL: `https://behindthefame.gumroad.com/l/aging-beautifully`.

### 1.3 El pack
**Products → New product → Bundle**. Nombre y descripción del producto 4 de `payhip-ficha.md`, precio 37 $, y añade los tres libros ya publicados. Gumroad entrega los tres archivos juntos y, si el cliente ya compró uno, le muestra la mejora al pack. URL: `library`.

### 1.4 Tres ajustes que importan con este público
- **Checkout → Settings:** desactiva «Discover» para los cuatro productos (*Show on Discover* **off**). Si una señora llega desde el buscador de Gumroad, la comisión sube del 10 % al 30 %; todas las tuyas llegan desde YouTube.
- **Checkout → Form:** no pidas más que el correo. Nada de dirección ni teléfono.
- **Emails:** activa el correo de bienvenida y, en **Audience**, exporta la lista cada mes. Esa lista es el canal de venta del siguiente libro.

---

## 2. Netlify: la web en línea (10 minutos)

### 2.1 Subir
1. En el ordenador, ten la carpeta `ebook/web/` con `index.html` dentro (puedes borrar `body.html` de la copia que subas; no molesta, pero no hace falta).
2. Abre **https://app.netlify.com/drop** y arrastra la carpeta. En unos segundos la web está en `https://<nombre-aleatorio>.netlify.app`.
3. Para que no se borre a las 24 h, crea la cuenta cuando Netlify lo pida («Claim this site»). Gratis.
4. **Site configuration → Site details → Change site name:** `behindthefame` → `https://behindthefame.netlify.app`. Con eso ya puedes vender; el dominio propio es opcional.

### 2.2 Actualizar la web
Cada vez que cambies `index.html`: **Deploys** → arrastra otra vez la carpeta a la zona de abajo («drag and drop your site output folder here»). Sustituye la versión anterior en segundos y conserva la URL.

### 2.3 Dominio propio (opcional, unos 12 $ al año)
Un dominio corto es más fácil de leer en voz alta en el vídeo y de teclear a los 70 años. Algo como `thehollywoodsecret.com` o `behindthefamebooks.com`.

1. Compra el dominio donde quieras (Namecheap, Porkbun, Cloudflare).
2. En Netlify: **Domain management → Add a domain** → escribe el dominio. Netlify añade solo las dos versiones (`midominio.com` y `www.midominio.com`).
3. En el registrador, crea dos registros DNS:

| Host | Tipo | Valor |
|---|---|---|
| `@` (raíz) | ALIAS / ANAME / CNAME aplanado, o si no existe, **A** | `apex-loadbalancer.netlify.com` (A: `75.2.60.5`) |
| `www` | CNAME | `behindthefame.netlify.app` |

4. Espera entre una hora y un día. Netlify emite el certificado HTTPS solo (Let's Encrypt) en cuanto el DNS responde. Si a las 24 h no funciona, en *Domain management* pulsa *Verify DNS configuration*.

Netlify también puede venderte el dominio y configurar el DNS él mismo (*Domain management → Register a new domain*); es un paso menos pero suele ser algo más caro.

---

## 3. Conectar los dos: los enlaces en la web (2 minutos)

Abre `web/index.html` y, al final, en el `<script>`, pega las cuatro URL de Gumroad en el objeto `BUY`:

```js
var BUY = {
  bundle: "https://behindthefame.gumroad.com/l/library",
  aging:  "https://behindthefame.gumroad.com/l/aging-beautifully",
  plate:  "https://behindthefame.gumroad.com/l/hollywood-plate",
  love:   "https://behindthefame.gumroad.com/l/love-story"
};
```

Con eso:

- Cada uno de los ocho botones apunta a su producto.
- Si el enlace es de Gumroad, la página carga sola el script del **overlay** (`https://gumroad.com/js/gumroad.js`) y el pago se abre en una ventana encima de la web, sin salir de ella. Para la lectora, la web y el cobro parecen una sola cosa.
- Añade `?wanted=true` al final de cada URL si quieres que el overlay se abra directamente en el formulario de pago, saltándose la ficha de Gumroad (que repite lo que la web ya ha contado). Recomendado: `.../l/library?wanted=true`.
- Si un día pegas enlaces de Payhip u otra tienda, los botones abren en pestaña nueva y no se carga ningún script.

Después, vuelve a arrastrar la carpeta a Netlify (bloque 2.2).

### Comprobar antes de anunciarlo
1. Abre la web en el móvil y pulsa «Get the Bundle — $37». Debe abrirse el overlay con «The Complete Behind the Fame Library» y 37 $.
2. Haz una compra real de un libro con tu tarjeta y devuélvetela desde Gumroad (**Sales → la venta → Refund**). Así ves el correo que recibe la compradora y el PDF que descarga.
3. Comprueba que los tres botones de 19 $ abren el libro correcto, no el pack.
4. Pasa por los seis bloques de la web en modo oscuro del móvil: el overlay de Gumroad se ve igual en los dos.

---

## 4. Lo que va en YouTube

Con el dominio en la mano, se completa `cta.md`: la línea 1 de cada descripción y del canal es

> Stay strong, slim and loved after 65 like the stars did, with The Hollywood Secret to Aging Beautifully: https://behindthefame.netlify.app/

(o el dominio propio). Un único enlace, a la web, nunca directo a Gumroad: la web vende el pack de 37 $ y el enlace de Gumroad solo vendería el libro de 19 $. El clip hablado del minuto 3 no cambia.

Si quieres medir qué vídeo vende, añade al final del enlace de cada vídeo `?v=hackman`, `?v=taylor`, etc. Netlify Analytics (de pago) o Gumroad (**Analytics → Referrers**) te dirán de qué URL llegaron las ventas. Gratis y suficiente al principio: Gumroad muestra el *referrer* de cada venta.

---

## 5. Orden recomendado para el primer día

1. Cuenta de Gumroad y datos de pago (bloque 1.1).
2. Las cuatro portadas horizontales de 1280 × 720 (bloque 1.2, punto 4). Es lo único que hoy no existe.
3. Tres libros y el pack en Gumroad (1.2 y 1.3). Discover desactivado (1.4).
4. Pegar las URL en `BUY` (bloque 3) y subir la carpeta a Netlify Drop (2.1). Nombre `behindthefame`.
5. Compra de prueba y devolución (bloque 3, comprobar).
6. Enlace en la descripción del canal y de los últimos cinco vídeos (bloque 4).
7. Dominio propio cuando haya habido la primera venta real, no antes.
