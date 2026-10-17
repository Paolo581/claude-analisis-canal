#!/usr/bin/env python3
"""Miniaturas: compone una miniatura de YouTube estilo «telediario» (1280×720).

Formato: presentador a la izquierda sobre un plató azul de noticias, la foto de la
persona en el recuadro del centro (lo único que cambia en cada vídeo), etiqueta roja
(«URGENTE») y titular grande en negro sobre una franja blanca.

Uso:
    python miniaturas/miniatura.py ficha.json [--salida carpeta] [--foto persona.jpg]
    python miniaturas/miniatura.py --nombre "Rick" --titular "NOTÍCIA MUITO TRISTE" \
        --escena "man in his late 50s lying in a hospital bed, oxygen cannula, worried"

La ficha .json admite: nombre, titulo, intro, etiqueta, titular, escena (prompt en
inglés de la imagen del medio), foto (ruta a una foto real que sustituye a la IA),
presentador (ruta a un PNG propio del presentador sobre el plató; si falta se genera
una vez con ai33 y se guarda en miniaturas/assets/presentador.png).

Clave: AI33_API_KEY o la credencial de ai33 inyectada en el entorno de Claude.
Todo lo generado queda en caché en la carpeta de salida: si falla, vuelve a lanzarlo.
"""
import argparse, hashlib, json, os, sys, time

try:
    import requests
    from PIL import Image, ImageDraw, ImageFilter, ImageFont
except ImportError:
    sys.exit("Faltan dependencias: pip install requests pillow")

AQUI = os.path.dirname(os.path.abspath(__file__))
FONT_TITULAR = os.path.join(AQUI, "fonts", "Anton-Regular.ttf")
FONT_ETIQUETA = [FONT_TITULAR, "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"]
ASSETS = os.path.join(AQUI, "assets")
W, H = 1280, 720

# Geometría (medida sobre la miniatura de referencia, escalada a 1280×720)
RECUADRO = (505, 40, 1265, 470)       # x0, y0, x1, y1 de la foto del medio
BORDE_RECUADRO = 5
ETIQUETA_XY = (22, 532)               # esquina superior izquierda de la etiqueta roja
ETIQUETA_ALTO = 62
FRANJA = (0, 598, W, 712)             # franja blanca del titular
TITULAR_X = 96                        # el titular empieza aquí (deja sitio al reloj de YouTube a la derecha)
TITULAR_MAX_W = W - TITULAR_X - 40

PROMPT_PRESENTADOR = (
    "Brazilian television news anchor, serious man in his fifties with short dark hair, dark navy suit, "
    "white shirt and blue tie, speaking to the camera mid-sentence with a concerned expression, framed from the "
    "chest up and placed on the LEFT third of the frame, the rest of the frame is an empty blue breaking-news "
    "studio background with glowing world map graphics and light streaks, no text, no captions, no logos, "
    "photorealistic broadcast still, sharp, 16:9")

ESCENA_SUFIJO = (", photorealistic press photo, natural lighting, sharp focus, framed from the chest up looking "
                 "towards the camera, no text, no captions, no watermark")


def log(msg):
    print(time.strftime("%H:%M:%S"), msg, flush=True)


def key(*parts):
    return hashlib.sha1("|".join(map(str, parts)).encode()).hexdigest()[:12]


# ---------------------------------------------------------------- ai33.pro
AI33 = "https://api.ai33.pro"
PROXY = "(credencial del entorno)"


def ai33_key():
    k = os.environ.get("AI33_API_KEY")
    if k:
        return k
    try:
        r = requests.get(AI33 + "/v1/credits", timeout=20)
        if r.status_code == 200 and r.json().get("success") is not False:
            return PROXY
    except Exception:
        pass
    return None


def ai33_req(method, path, api_key, **kw):
    for attempt in range(8):
        hdr = {} if api_key == PROXY else {"xi-api-key": api_key}
        r = requests.request(method, AI33 + path, headers=hdr, timeout=120, **kw)
        if r.status_code in (429, 503):
            time.sleep(float(r.headers.get("Retry-After") or 5 * (attempt + 1)))
            continue
        if r.status_code >= 400:
            raise RuntimeError(f"ai33 {path} respondió {r.status_code}: {r.text[:300]}")
        return r.json()
    raise RuntimeError(f"ai33 {path}: demasiados reintentos")


def first_url(meta, exts):
    found = []

    def walk(x):
        if isinstance(x, str) and x.startswith("http"):
            found.append(x)
        elif isinstance(x, dict):
            for v in x.values():
                walk(v)
        elif isinstance(x, list):
            for v in x:
                walk(v)
    walk(meta)
    for u in found:
        if any(u.split("?")[0].lower().endswith(e) for e in exts):
            return u
    return found[0] if found else None


def ai33_image(prompt, out, aspect, api_key, model):
    if os.path.exists(out) and os.path.getsize(out) > 1000:
        return out
    d = ai33_req("POST", "/v1i/task/generate-image", api_key, data={
        "prompt": prompt, "model_id": model, "generations_count": "1",
        "model_parameters": json.dumps({"aspect_ratio": aspect, "resolution": "2K"})})
    t0 = time.time()
    while time.time() - t0 < 900:
        s = ai33_req("GET", f"/v1/task/{d['task_id']}", api_key)
        if s.get("status") == "done":
            url = first_url(s.get("metadata") or {}, (".jpg", ".jpeg", ".png", ".webp"))
            if not url:
                raise RuntimeError(f"ai33 no devolvió imagen: {str(s)[:200]}")
            open(out, "wb").write(requests.get(url, timeout=120).content)
            return out
        if s.get("status") in ("error", "failed", "fail"):
            raise RuntimeError(f"ai33 no pudo generar la imagen: {s.get('error_message')}")
        time.sleep(3)
    raise RuntimeError("ai33 tardó más de 15 min")


# ---------------------------------------------------------------- composición
def font(path_or_list, size):
    for p in (path_or_list if isinstance(path_or_list, list) else [path_or_list]):
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()


def cover(img, w, h):
    """Recorta y escala la imagen para llenar w×h sin deformar (como object-fit: cover)."""
    img = img.convert("RGB")
    r = max(w / img.width, h / img.height)
    img = img.resize((round(img.width * r), round(img.height * r)), Image.LANCZOS)
    x = (img.width - w) // 2
    y = (img.height - h) // 2
    return img.crop((x, y, x + w, y + h))


def texto_ajustado(draw, texto, fuente, size, max_w, min_size=40):
    while size > min_size:
        f = font(fuente, size)
        if draw.textlength(texto, font=f) <= max_w:
            return f
        size -= 4
    return font(fuente, min_size)


def componer(base, foto, etiqueta, titular, salida):
    lienzo = cover(Image.open(base), W, H)
    d = ImageDraw.Draw(lienzo)

    # Recuadro del medio: sombra suave + borde blanco + foto
    x0, y0, x1, y1 = RECUADRO
    sombra = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(sombra).rectangle((x0 + 6, y0 + 10, x1 + 6, y1 + 10), fill=(0, 0, 0, 150))
    sombra = sombra.filter(ImageFilter.GaussianBlur(14))
    lienzo = Image.alpha_composite(lienzo.convert("RGBA"), sombra).convert("RGB")
    d = ImageDraw.Draw(lienzo)
    d.rectangle((x0 - BORDE_RECUADRO, y0 - BORDE_RECUADRO, x1 + BORDE_RECUADRO, y1 + BORDE_RECUADRO),
                fill=(255, 255, 255))
    lienzo.paste(cover(Image.open(foto), x1 - x0, y1 - y0), (x0, y0))
    d = ImageDraw.Draw(lienzo)

    # Franja blanca con el titular en negro
    fx0, fy0, fx1, fy1 = FRANJA
    d.rectangle((fx0, fy0, fx1, fy1), fill=(255, 255, 255))
    ft = texto_ajustado(d, titular, FONT_TITULAR, 118, TITULAR_MAX_W)
    bb = d.textbbox((0, 0), titular, font=ft)
    ty = fy0 + (fy1 - fy0 - (bb[3] - bb[1])) // 2 - bb[1]
    d.text((TITULAR_X, ty), titular, font=ft, fill=(10, 10, 10))

    # Etiqueta roja («URGENTE») con texto blanco, encima de la franja
    if etiqueta:
        fe = font(FONT_ETIQUETA, 52)
        bb = d.textbbox((0, 0), etiqueta, font=fe)
        ex, ey = ETIQUETA_XY
        ew = (bb[2] - bb[0]) + 36
        d.rectangle((ex, ey, ex + ew, ey + ETIQUETA_ALTO), fill=(214, 20, 20))
        d.text((ex + 18 - bb[0], ey + (ETIQUETA_ALTO - (bb[3] - bb[1])) // 2 - bb[1]), etiqueta, font=fe,
               fill=(255, 255, 255))

    lienzo.save(salida, quality=92)
    return salida


# ---------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("ficha", nargs="?", help="ficha .json con nombre, titular, escena…")
    ap.add_argument("--nombre")
    ap.add_argument("--titulo")
    ap.add_argument("--intro")
    ap.add_argument("--etiqueta")
    ap.add_argument("--titular")
    ap.add_argument("--escena", help="prompt (en inglés) de la imagen del medio")
    ap.add_argument("--foto", help="foto real de la persona para el recuadro (sustituye a la IA)")
    ap.add_argument("--presentador", help="PNG/JPG propio del presentador sobre el plató (1280×720)")
    ap.add_argument("--modelo", default=os.environ.get("AI33_IMAGE_MODEL", "bytedance-seedream-4.5"))
    ap.add_argument("--salida", default="miniaturas/salida")
    a = ap.parse_args()

    ficha = json.load(open(a.ficha, encoding="utf-8")) if a.ficha else {}
    for k in ("nombre", "titulo", "intro", "etiqueta", "titular", "escena", "foto", "presentador"):
        if getattr(a, k) is not None:
            ficha[k] = getattr(a, k)
    ficha.setdefault("etiqueta", "URGENTE")
    if not ficha.get("titular"):
        sys.exit("Falta el titular (--titular o «titular» en la ficha).")
    if not ficha.get("escena") and not ficha.get("foto"):
        sys.exit("Falta la imagen del medio: --escena (prompt) o --foto (foto real).")

    os.makedirs(a.salida, exist_ok=True)
    os.makedirs(ASSETS, exist_ok=True)
    api = None
    if not ficha.get("foto") or not ficha.get("presentador"):
        api = ai33_key()

    presentador = ficha.get("presentador") or os.path.join(ASSETS, "presentador.png")
    if not os.path.exists(presentador):
        if not api:
            sys.exit("No hay clave de ai33 para generar el presentador; pásalo con --presentador.")
        log("Generando el presentador sobre el plató (una sola vez)…")
        ai33_image(PROMPT_PRESENTADOR, presentador, "16:9", api, a.modelo)

    foto = ficha.get("foto")
    if not foto:
        if not api:
            sys.exit("No hay clave de ai33 para generar la imagen del medio; pásala con --foto.")
        foto = os.path.join(a.salida, f"escena-{key(ficha['escena'], a.modelo)}.png")
        log(f"Generando la imagen del medio: {ficha['escena'][:80]}…")
        ai33_image(ficha["escena"] + ESCENA_SUFIJO, foto, "16:9", api, a.modelo)

    nombre = (ficha.get("nombre") or "miniatura").lower().replace(" ", "-")
    out = os.path.join(a.salida, f"{nombre}-{key(ficha['titular'], ficha['etiqueta'], foto)}.jpg")
    componer(presentador, foto, ficha["etiqueta"], ficha["titular"], out)
    log(f"Lista: {out}")


if __name__ == "__main__":
    main()
