#!/usr/bin/env python3
"""Montador: convierte un proyecto de la Fábrica del Radar en un vídeo MP4.

Uso:
    python montador/montar.py proyecto.json [--salida carpeta] [--voz VOICE_ID]
                               [--musica fondo.mp3] [--demo] [--sin-subtitulos]

Entrada: el .json que descarga la Fábrica («Descargar proyecto para el Montador»).
Claves (variables de entorno, nunca en el código):
    AI33_API_KEY         ai33.pro / OpenSpeaker: voz (ElevenLabs, MiniMax…) e imágenes IA con una sola clave
    AI33_VOICE_ID        voz de ai33 con prefijo, ej. elevenlabs_pNInz6obpgDQGcFmaJgB (ver --listar-voces)
    AI33_IMAGE_MODEL     modelo de imagen de ai33 (por defecto bytedance-seedream-4.5)
    ELEVENLABS_API_KEY   voz directa de ElevenLabs (alternativa a ai33)
    ELEVENLABS_VOICE_ID  voz por defecto (opcional; --voz la sustituye)
    PEXELS_API_KEY       fotos y vídeos de stock (gratis)
    REPLICATE_API_TOKEN  imágenes IA con Flux (opcional)
Todo lo descargado queda en caché en la carpeta de salida: si se corta, vuelve a lanzarlo y sigue.
"""
import argparse, hashlib, json, os, re, shutil, subprocess, sys, textwrap, time

try:
    import requests
    from PIL import Image, ImageDraw, ImageFilter, ImageFont
    import imageio_ffmpeg
except ImportError:
    sys.exit("Faltan dependencias: pip install -r montador/requirements.txt")

FFMPEG = imageio_ffmpeg.get_ffmpeg_exe()
FPS = 30
DEFAULT_VOICE = "pNInz6obpgDQGcFmaJgB"  # «Adam», voz multilingüe de la biblioteca pública de ElevenLabs
FONT_CANDIDATES = ["/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", "/Library/Fonts/Arial Bold.ttf",
                   "C:/Windows/Fonts/arialbd.ttf", "/System/Library/Fonts/Supplemental/Arial Bold.ttf"]


def log(msg):
    print(time.strftime("%H:%M:%S"), msg, flush=True)


def run(cmd):
    p = subprocess.run(cmd, capture_output=True, text=True)
    if p.returncode != 0:
        raise RuntimeError(f"ffmpeg falló: {' '.join(cmd[:6])}…\n{p.stderr[-1500:]}")
    return p


def media_duration(path):
    p = subprocess.run([FFMPEG, "-hide_banner", "-i", path], capture_output=True, text=True)
    m = re.search(r"Duration: (\d+):(\d+):(\d+\.\d+)", p.stderr)
    if not m:
        raise RuntimeError(f"No pude leer la duración de {path}")
    h, mi, s = m.groups()
    return int(h) * 3600 + int(mi) * 60 + float(s)


def font(size):
    for f in FONT_CANDIDATES:
        if os.path.exists(f):
            return ImageFont.truetype(f, size)
    return ImageFont.load_default()


def key(*parts):
    return hashlib.sha1("|".join(map(str, parts)).encode()).hexdigest()[:12]


# ---------------------------------------------------------------- ai33.pro (OpenSpeaker)
AI33 = "https://api.ai33.pro"


def ai33_req(method, path, api_key, **kw):
    for attempt in range(8):
        r = requests.request(method, AI33 + path, headers={"xi-api-key": api_key}, timeout=120, **kw)
        if r.status_code == 429 or r.status_code == 503:
            time.sleep(float(r.headers.get("Retry-After") or 5 * (attempt + 1)))
            continue
        if r.status_code >= 400:
            raise RuntimeError(f"ai33 {path} respondió {r.status_code}: {r.text[:300]}")
        return r.json()
    raise RuntimeError(f"ai33 {path}: demasiados reintentos")


def ai33_wait(task_id, api_key, what):
    t0 = time.time()
    while time.time() - t0 < 900:
        d = ai33_req("GET", f"/v1/task/{task_id}", api_key)
        st = d.get("status")
        if st == "done":
            return d.get("metadata") or {}
        if st in ("error", "failed", "fail"):
            raise RuntimeError(f"ai33 no pudo generar {what}: {d.get('error_message')}")
        time.sleep(3)
    raise RuntimeError(f"ai33 tardó más de 15 min en {what}")


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


def ai33_tts_submit(text, voice, api_key):
    d = ai33_req("POST", "/v3/text-to-speech", api_key, data={"text": text, "voice_id": voice, "speed": "1"})
    if not d.get("task_id"):
        raise RuntimeError(f"ai33 no devolvió tarea de voz: {d}")
    return d["task_id"]


def ai33_image(prompt, out, aspect, api_key, model):
    d = ai33_req("POST", "/v1i/task/generate-image", api_key, data={
        "prompt": prompt, "model_id": model, "generations_count": "1",
        "model_parameters": json.dumps({"aspect_ratio": aspect, "resolution": "2K"})})
    meta = ai33_wait(d["task_id"], api_key, "la imagen")
    url = first_url(meta, (".jpg", ".jpeg", ".png", ".webp"))
    if not url:
        raise RuntimeError(f"ai33 no devolvió imagen: {str(meta)[:200]}")
    open(out, "wb").write(requests.get(url, timeout=120).content)
    return True


def listar_voces(lang, api_key):
    for prov in ("elevenlabs", "minimax"):
        d = ai33_req("GET", "/v3/voices", api_key, params={"provider": prov, "language": lang, "page_size": 40})
        print(f"\n== {prov} · {lang} ==")
        for v in d.get("data", []):
            print(f"{v.get('voice_id')}\t{v.get('name')}\t{v.get('gender') or ''}\t{v.get('accent') or v.get('description') or ''}"[:160])


# ---------------------------------------------------------------- voz
def tts(text, out, voice, api_key):
    if os.path.exists(out) and os.path.getsize(out) > 1000:
        return
    for attempt in range(4):
        r = requests.post(f"https://api.elevenlabs.io/v1/text-to-speech/{voice}?output_format=mp3_44100_128",
                          headers={"xi-api-key": api_key, "Content-Type": "application/json"},
                          json={"text": text, "model_id": "eleven_multilingual_v2",
                                "voice_settings": {"stability": 0.45, "similarity_boost": 0.8, "style": 0.15}},
                          timeout=180)
        if r.status_code == 200:
            open(out, "wb").write(r.content)
            return
        if r.status_code in (429, 500, 502, 503):
            time.sleep(10 * (attempt + 1))
            continue
        raise RuntimeError(f"ElevenLabs respondió {r.status_code}: {r.text[:300]}")
    raise RuntimeError("ElevenLabs no respondió tras 4 intentos")


def silence(out, secs):
    if not os.path.exists(out):
        run([FFMPEG, "-y", "-f", "lavfi", "-i", "anullsrc=r=44100:cl=mono", "-t", f"{secs:.2f}",
             "-c:a", "libmp3lame", "-b:a", "128k", out])


# ---------------------------------------------------------------- imágenes
def pexels_photo(query, out, orientation, api_key):
    r = requests.get("https://api.pexels.com/v1/search", headers={"Authorization": api_key},
                     params={"query": query, "per_page": 5, "orientation": orientation}, timeout=30)
    r.raise_for_status()
    photos = r.json().get("photos", [])
    if not photos:
        return False
    pick = photos[int(key(query), 16) % len(photos)]
    img = requests.get(pick["src"]["large2x"], timeout=60)
    img.raise_for_status()
    open(out, "wb").write(img.content)
    return True


def flux_image(prompt, out, aspect, token):
    r = requests.post("https://api.replicate.com/v1/models/black-forest-labs/flux-schnell/predictions",
                      headers={"Authorization": f"Bearer {token}", "Prefer": "wait"},
                      json={"input": {"prompt": prompt, "aspect_ratio": aspect, "output_format": "jpg",
                                      "num_outputs": 1}}, timeout=120)
    r.raise_for_status()
    data = r.json()
    for _ in range(40):
        if data.get("status") == "succeeded":
            url = data["output"][0] if isinstance(data["output"], list) else data["output"]
            open(out, "wb").write(requests.get(url, timeout=60).content)
            return True
        if data.get("status") in ("failed", "canceled"):
            raise RuntimeError(f"Replicate: {data.get('error')}")
        time.sleep(2)
        data = requests.get(data["urls"]["get"], headers={"Authorization": f"Bearer {token}"}, timeout=30).json()
    raise RuntimeError("Replicate tardó demasiado")


def card(text, out, size, seed):
    """Imagen de reserva: fondo degradado con el texto de la escena (modo demo o sin resultados)."""
    w, h = size
    hue = int(key(seed), 16) % 360
    img = Image.new("RGB", (w, h))
    d = ImageDraw.Draw(img)
    import colorsys
    for y in range(h):
        r, g, b = colorsys.hsv_to_rgb(hue / 360, 0.55, 0.18 + 0.25 * y / h)
        d.line([(0, y), (w, y)], fill=(int(r * 255), int(g * 255), int(b * 255)))
    f = font(int(h * 0.05))
    lines = textwrap.wrap(text or "", width=28 if w > h else 18)[:6]
    y = h / 2 - len(lines) * f.size * 0.65
    for ln in lines:
        tw = d.textlength(ln, font=f)
        d.text(((w - tw) / 2, y), ln, font=f, fill=(245, 245, 245))
        y += f.size * 1.3
    img.save(out, quality=92)


def fit(src, out, size, overlay=None):
    """Recorta al formato, deja margen para el zoom y dibuja el texto en pantalla."""
    W, H = int(size[0] * 1.25), int(size[1] * 1.25)
    img = Image.open(src).convert("RGB")
    sc = max(W / img.width, H / img.height)
    img = img.resize((int(img.width * sc) + 1, int(img.height * sc) + 1), Image.LANCZOS)
    l, t = (img.width - W) // 2, (img.height - H) // 2
    img = img.crop((l, t, l + W, t + H))
    if overlay:
        d = ImageDraw.Draw(img, "RGBA")
        f = font(int(H * 0.055))
        lines = textwrap.wrap(overlay.upper(), width=24 if W > H else 14)[:3]
        lh = f.size * 1.25
        top = H * 0.16
        box_w = max(d.textlength(x, font=f) for x in lines) + f.size
        d.rectangle([(W - box_w) / 2, top - f.size * 0.4, (W + box_w) / 2, top + lh * len(lines)], fill=(0, 0, 0, 170))
        for i, ln in enumerate(lines):
            tw = d.textlength(ln, font=f)
            d.text(((W - tw) / 2, top + i * lh), ln, font=f, fill=(255, 214, 0))
    img.save(out, quality=93)


# ---------------------------------------------------------------- tiempos
def build_timeline(proj, voice_durs):
    """Lleva los tiempos estimados de la Fábrica a los reales de la voz, párrafo por párrafo."""
    paras = proj["paras"]
    real, acc = [], 0.0
    for p, d in zip(paras, voice_durs):
        real.append((acc, acc + d))
        acc += d

    def mapt(t):
        for p, (a, b) in zip(paras, real):
            if p["ini"] <= t <= p["fim"] + 1e-6:
                span = max(0.01, p["fim"] - p["ini"])
                return a + (t - p["ini"]) / span * (b - a)
        return acc

    scenes = sorted(proj.get("cenas", []), key=lambda c: float(c.get("ini", 0)))
    out = []
    for i, c in enumerate(scenes):
        a = mapt(float(c.get("ini", 0)))
        b = mapt(float(scenes[i + 1]["ini"])) if i + 1 < len(scenes) else acc
        if b - a < 0.8:
            continue
        out.append({**c, "a": a, "b": b})
    if not out:
        out = [{"tipo": "stock", "visual": proj.get("titulo", ""), "busca": proj.get("titulo", ""), "a": 0, "b": acc}]
    out[0]["a"] = 0.0
    out[-1]["b"] = acc
    for i in range(len(out) - 1):  # sin huecos entre escenas
        out[i]["b"] = out[i + 1]["a"]
    return out, real, acc


def srt_time(t):
    ms = int(round(t * 1000))
    return f"{ms // 3600000:02d}:{ms // 60000 % 60:02d}:{ms // 1000 % 60:02d},{ms % 1000:03d}"


def write_srt(proj, real, path):
    n, lines = 1, []
    for p, (a, b) in zip(proj["paras"], real):
        words = p["texto"].split()
        chunks = [" ".join(words[i:i + 8]) for i in range(0, len(words), 8)] or [""]
        tot = sum(len(c) for c in chunks) or 1
        t = a
        for c in chunks:
            d = (b - a) * len(c) / tot
            lines.append(f"{n}\n{srt_time(t)} --> {srt_time(t + d)}\n{c}\n")
            n += 1
            t += d
    open(path, "w", encoding="utf-8").write("\n".join(lines))


# ---------------------------------------------------------------- principal
def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("proyecto", nargs="?")
    ap.add_argument("--listar-voces", metavar="IDIOMA", help="lista voces de ai33, ej. Portuguese o Spanish")
    ap.add_argument("--salida", default=None)
    ap.add_argument("--voz", default=os.environ.get("ELEVENLABS_VOICE_ID", DEFAULT_VOICE))
    ap.add_argument("--musica", default=None, help="mp3 de fondo (se pone a -20 dB bajo la voz)")
    ap.add_argument("--demo", action="store_true", help="sin claves: voz en silencio e imágenes de texto")
    ap.add_argument("--sin-subtitulos", action="store_true")
    a = ap.parse_args()
    ai_key = os.environ.get("AI33_API_KEY")
    if a.listar_voces:
        if not ai_key:
            sys.exit("Falta AI33_API_KEY.")
        listar_voces(a.listar_voces, ai_key)
        return
    if not a.proyecto:
        ap.error("falta el archivo del proyecto")

    proj = json.load(open(a.proyecto, encoding="utf-8"))
    if not proj.get("paras"):
        sys.exit("El proyecto no tiene guion. Escríbelo en la Fábrica antes de montarlo.")
    short = proj.get("formato") == "short"
    size = (1080, 1920) if short else (1920, 1080)
    out_dir = a.salida or os.path.join("montajes", re.sub(r"[^a-z0-9]+", "-", proj.get("titulo", "video").lower()).strip("-")[:60])
    for sub in ("voz", "img", "clips"):
        os.makedirs(os.path.join(out_dir, sub), exist_ok=True)

    el_key, px_key, rp_key = (os.environ.get(k) for k in ("ELEVENLABS_API_KEY", "PEXELS_API_KEY", "REPLICATE_API_TOKEN"))
    use_ai33_voice = bool(ai_key) and not el_key
    voice_id = os.environ.get("AI33_VOICE_ID", "elevenlabs_" + DEFAULT_VOICE) if use_ai33_voice else a.voz
    if use_ai33_voice and a.voz != os.environ.get("ELEVENLABS_VOICE_ID", DEFAULT_VOICE):
        voice_id = a.voz if "_" in a.voz else "elevenlabs_" + a.voz
    img_model = os.environ.get("AI33_IMAGE_MODEL", "bytedance-seedream-4.5")
    if not a.demo and not el_key and not ai_key:
        sys.exit("Falta AI33_API_KEY o ELEVENLABS_API_KEY (o usa --demo para una prueba sin voz).")
    if not a.demo and not px_key and not rp_key and not ai_key:
        log("Aviso: sin PEXELS_API_KEY ni REPLICATE_API_TOKEN, las escenas serán tarjetas de texto.")

    # 1. voz, párrafo por párrafo (sincroniza escenas y subtítulos)
    wpm = 150
    durs, voice_files = [], []
    for i, p in enumerate(proj["paras"]):
        voice_files.append(os.path.join(out_dir, "voz", f"{i:04d}-{key(p['texto'], voice_id)}.mp3"))
    if not a.demo and use_ai33_voice:
        pend = [(i, f) for i, f in enumerate(voice_files) if not (os.path.exists(f) and os.path.getsize(f) > 1000)]
        for k in range(0, len(pend), 6):  # 6 tareas a la vez para no saturar la cuota
            batch = [(i, f, ai33_tts_submit(proj["paras"][i]["texto"], voice_id, ai_key)) for i, f in pend[k:k + 6]]
            for i, f, tid in batch:
                meta = ai33_wait(tid, ai_key, f"la voz del párrafo {i + 1}")
                url = first_url(meta, (".mp3", ".wav", ".m4a"))
                if not url:
                    raise RuntimeError(f"ai33 no devolvió audio: {str(meta)[:200]}")
                raw = f + ".src"
                open(raw, "wb").write(requests.get(url, timeout=120).content)
                run([FFMPEG, "-y", "-i", raw, "-ac", "1", "-ar", "44100", "-c:a", "libmp3lame", "-b:a", "128k", f])
                os.remove(raw)
            log(f"Voz {min(k + 6, len(pend))}/{len(pend)}")
    for i, p in enumerate(proj["paras"]):
        f = voice_files[i]
        if a.demo:
            silence(f, max(1.0, len(p["texto"].split()) / wpm * 60))
        elif not use_ai33_voice:
            log(f"Voz {i + 1}/{len(proj['paras'])}")
            tts(p["texto"], f, voice_id, el_key)
        durs.append(media_duration(f) + 0.25)
    scenes, real, total = build_timeline(proj, durs)
    log(f"Voz lista: {total / 60:.1f} min · {len(scenes)} escenas")

    # 2. imagen de cada escena
    orient = "portrait" if short else "landscape"
    aspect = "9:16" if short else "16:9"
    for i, c in enumerate(scenes):
        tipo = (c.get("tipo") or "").lower()
        raw = os.path.join(out_dir, "img", f"{i:04d}-{key(c.get('visual'), c.get('prompt_ia'), c.get('busca'))}.jpg")
        if not os.path.exists(raw):
            done = False
            try:
                wants_ai = c.get("prompt_ia") and ("ia" in tipo or "anim" in tipo)
                if not a.demo and wants_ai and rp_key:
                    done = flux_image(c["prompt_ia"], raw, aspect, rp_key)
                elif not a.demo and wants_ai and ai_key:
                    done = ai33_image(c["prompt_ia"], raw, aspect, ai_key, img_model)
                if not done and not a.demo and px_key:
                    q = c.get("busca") or c.get("visual") or proj.get("titulo")
                    if "mapa" in tipo and "map" not in q.lower():
                        q = "map " + q
                    done = pexels_photo(q, raw, orient, px_key)
            except Exception as e:  # una escena fallida no para el montaje
                log(f"Escena {i + 1}: {e}")
            if not done:
                card(c.get("visual") or c.get("fala") or "", raw, size, i)
        c["img"] = os.path.join(out_dir, "img", f"{i:04d}-fit.jpg")
        fit(raw, c["img"], size, c.get("texto_tela"))
    log("Imágenes listas")

    # 3. un clip por escena con zoom lento alternando dirección
    clips = []
    for i, c in enumerate(scenes):
        d = c["b"] - c["a"]
        frames = max(2, int(round(d * FPS)))
        clip = os.path.join(out_dir, "clips", f"{i:04d}-{key(c['img'], round(d, 2), size)}.mp4")
        if not os.path.exists(clip):
            z = "min(zoom+0.0006,1.18)" if i % 2 == 0 else "if(eq(on,0),1.18,max(zoom-0.0006,1.0))"
            vf = (f"scale={int(size[0] * 1.25)}:{int(size[1] * 1.25)},zoompan=z='{z}':d={frames}:"
                  f"x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s={size[0]}x{size[1]}:fps={FPS},format=yuv420p")
            run([FFMPEG, "-y", "-loop", "1", "-i", c["img"], "-vf", vf, "-frames:v", str(frames),
                 "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "-an", clip])
        clips.append(clip)
        if (i + 1) % 10 == 0 or i + 1 == len(scenes):
            log(f"Clips {i + 1}/{len(scenes)}")

    # 4. unir vídeo, voz, música y subtítulos
    lst = os.path.join(out_dir, "clips.txt")
    open(lst, "w").write("".join(f"file '{os.path.abspath(c)}'\n" for c in clips))
    alist = os.path.join(out_dir, "voz.txt")
    gap = os.path.join(out_dir, "voz", "pausa.mp3")
    silence(gap, 0.25)
    open(alist, "w").write("".join(f"file '{os.path.abspath(f)}'\nfile '{os.path.abspath(gap)}'\n" for f in voice_files))
    voice = os.path.join(out_dir, "voz-completa.m4a")
    run([FFMPEG, "-y", "-f", "concat", "-safe", "0", "-i", alist, "-af", "aresample=44100,apad=pad_dur=0.5,loudnorm=I=-16:TP=-1.5",
         "-c:a", "aac", "-b:a", "192k", voice])
    srt = os.path.join(out_dir, "subtitulos.srt")
    write_srt(proj, real, srt)
    final = os.path.join(out_dir, "video.mp4")
    cmd = [FFMPEG, "-y", "-f", "concat", "-safe", "0", "-i", lst, "-i", voice]
    if a.musica:
        cmd += ["-stream_loop", "-1", "-i", a.musica]
        af = "[2:a]volume=-20dB[m];[1:a][m]amix=inputs=2:duration=first:dropout_transition=0[a]"
    else:
        af = "[1:a]anull[a]"
    vf = "null"
    if not a.sin_subtitulos:
        fs = 16 if short else 20
        esc = os.path.abspath(srt).replace("\\", "/").replace(":", "\\:")
        vf = f"subtitles='{esc}':force_style='FontName=DejaVu Sans,FontSize={fs},Bold=1,Outline=2,MarginV={90 if short else 40}'"
    cmd += ["-filter_complex", f"[0:v]{vf}[v];{af}", "-map", "[v]", "-map", "[a]", "-c:v", "libx264", "-preset",
            "veryfast", "-crf", "20", "-c:a", "aac", "-b:a", "192k", "-shortest", "-movflags", "+faststart", final]
    log("Montando el vídeo final…")
    run(cmd)
    log(f"Listo: {final} ({media_duration(final) / 60:.1f} min) · subtítulos para YouTube: {srt}")


if __name__ == "__main__":
    main()
