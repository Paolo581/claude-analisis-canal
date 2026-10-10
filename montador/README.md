# Montador

Convierte un proyecto de la **Fábrica** del Radar en un vídeo MP4 listo para subir: voz de ElevenLabs, una imagen por escena (Pexels o IA con Flux), zoom lento, texto en pantalla, música de fondo opcional y subtítulos quemados, más un `.srt` para subir a YouTube.

## 1. Claves (una sola vez)

Guárdalas como variables de entorno, nunca en el código ni en el chat:

| Variable | Para qué | Dónde se saca |
|---|---|---|
| `AI33_API_KEY` | voz (voces de ElevenLabs, MiniMax…) **e** imágenes IA con una sola clave — sustituye a ElevenLabs y Replicate | ai33.pro → API key |
| `AI33_VOICE_ID` | la voz de ai33, con prefijo (ej. `elevenlabs_pNInz6obpgDQGcFmaJgB`) | `python montador/montar.py --listar-voces Portuguese` |
| `AI33_IMAGE_MODEL` | modelo de imagen (opcional, por defecto `bytedance-seedream-4.5`) | ai33.pro |
| `ELEVENLABS_API_KEY` | la voz directa de ElevenLabs (si no usas ai33) | elevenlabs.io → Profile → API Keys |
| `ELEVENLABS_VOICE_ID` | la voz elegida (opcional) | elevenlabs.io → Voices → «Copy voice ID» |
| `PEXELS_API_KEY` | fotos de stock (gratis) | pexels.com/api |
| `REPLICATE_API_TOKEN` | imágenes IA con Flux (opcional, ~0,003 US$/imagen) | replicate.com → Account → API tokens |

En una sesión de Claude Code en la nube: menú del entorno en la barra de título → Edit → variables de entorno. Si la red del entorno está limitada, permite `api.ai33.pro` (y los dominios desde los que sirve sus audios e imágenes), `api.elevenlabs.io`, `api.pexels.com`, `images.pexels.com`, `api.replicate.com` y `replicate.delivery`.

## 2. Usarlo

1. En la Fábrica, termina el guion y el plan visual y pulsa **«Descargar para el Montador (.json)»**.
2. Ejecuta:

```bash
pip install -r montador/requirements.txt
python montador/montar.py montador-mi-video.json
# opciones: --voz VOICE_ID  --musica fondo.mp3  --sin-subtitulos  --salida carpeta
```

3. El resultado queda en `montajes/<titulo>/video.mp4` junto con `subtitulos.srt`.

Prueba sin claves: `python montador/montar.py montador/ejemplo/virginia.json --demo` (voz en silencio e imágenes de texto).

Si se corta a medias, vuelve a lanzarlo: todo lo descargado queda en caché y continúa donde iba.

## Cómo decide cada escena

- **Imágenes IA / Animaciones** con `prompt_ia` → Flux (si hay `REPLICATE_API_TOKEN`); si no, stock.
- **Stock, Mapas, Clips de YouTube** → foto de Pexels con los términos de `busca` (los clips de YouTube no se descargan: tienen derechos).
- Sin resultados → tarjeta con el texto de la escena, para que el vídeo nunca se quede en negro.
- Los tiempos del plan se ajustan a la duración real de la voz, párrafo por párrafo.
