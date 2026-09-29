# Conector directo con YouTube

`youtube_sync.py` lee **tu canal** con las APIs oficiales de Google (YouTube Data, YouTube Analytics y YouTube Reporting) y guarda en el Radar:

- todos tus vídeos con duración real, vistas, likes y comentarios;
- retención (% visto y duración media), suscriptores ganados y vistas de los últimos 90 días por vídeo;
- **impresiones y CTR** de la miniatura por vídeo (últimos 28 días);
- ingresos y CPM por vídeo, si el canal está monetizado;
- vistas y suscriptores día a día, fuentes de tráfico, edad y sexo de la audiencia.

## Configurarlo (una sola vez, ~20 minutos)

### 1. Proyecto en Google Cloud
1. Entra en **console.cloud.google.com** con la cuenta de Google dueña del canal.
2. Arriba, selector de proyectos → **Proyecto nuevo** → nombre «Radar» → Crear.
3. Menú ☰ → **APIs y servicios → Biblioteca**. Busca y pulsa **Habilitar** en las tres:
   - YouTube Data API v3
   - YouTube Analytics API
   - YouTube Reporting API

### 2. Pantalla de consentimiento
1. **APIs y servicios → Pantalla de consentimiento de OAuth** (o «Google Auth Platform»).
2. Tipo de usuario **Externo** → nombre de la app «Radar», tu correo como soporte y contacto → Guardar.
3. En **Público / Audiencia**, pulsa **Publicar la app** («En producción»). Si la dejas en «Prueba», Google invalida la autorización cada 7 días. No hace falta verificación: al autorizar verás un aviso de «app no verificada»; pulsa *Configuración avanzada → Ir a Radar*.

### 3. ID de cliente
1. **APIs y servicios → Credenciales → Crear credenciales → ID de cliente de OAuth**.
2. Tipo: **Aplicación web**. En «URI de redirección autorizados» añade exactamente:
   `https://developers.google.com/oauthplayground`
3. Crear. Copia el **ID de cliente** y el **Secreto de cliente**.

### 4. Autorizar tu canal (sacar el refresh token)
1. Abre **https://developers.google.com/oauthplayground**.
2. Arriba a la derecha, el engranaje ⚙ → marca **Use your own OAuth credentials** → pega el ID y el secreto.
3. A la izquierda, en «Input your own scopes», pega (separados por espacios):
   `https://www.googleapis.com/auth/youtube.readonly https://www.googleapis.com/auth/yt-analytics.readonly https://www.googleapis.com/auth/yt-analytics-monetary.readonly`
4. **Authorize APIs** → elige la cuenta y, si te pregunta, **el canal Arquivos do Poder** → Permitir.
5. **Exchange authorization code for tokens** → copia el **Refresh token**.

### 5. Guardar las 3 claves en el entorno de Claude
En la sesión de Claude Code: menú del entorno (barra de título) → **Edit** → variables de entorno. Añade:

```
YT_CLIENT_ID=…
YT_CLIENT_SECRET=…
YT_REFRESH_TOKEN=…
```

**No las pegues en el chat.** Si tu entorno solo ofrece «Añadir credencial» (cabeceras), usa la sección de variables de entorno; si no la encuentras, manda una captura.

Si la red del entorno está limitada, permite: `oauth2.googleapis.com`, `youtube.googleapis.com`, `youtubeanalytics.googleapis.com`, `youtubereporting.googleapis.com`.

### 6. Primera sincronización
Abre una **sesión nueva** (las claves se cargan al empezar) y pega:

> Ejecuta `python conector/youtube_sync.py --salida yt_snapshot.json`. Luego guarda ese JSON en la base de datos del artifact https://claude.ai/artifact/MRdDbqoJUXtnCHxivXwCaJ con ArtifactData (action "set", collection "snapshots", doc_id "youtube", file_path yt_snapshot.json; si ya existe, usa if_version). Dime cuántos vídeos, cuántos con CTR y el estado del informe de alcance. Después crea una rutina diaria que haga lo mismo cada mañana.

La primera vez, el informe de impresiones y CTR se **crea** y Google tarda 24-48 h en generarlo; mientras tanto el resto de datos ya aparece. Desde entonces se actualiza cada día.

## Qué ves en el Radar
- **Mis vídeos**: columnas nuevas *Impr. 28 d* y *CTR* (verde ≥ 6 %, rojo < 3 %); duración y % visto reales en todos los vídeos.
- **Panorama**: inscritos, vistas por semana, tráfico y audiencia desde la API; el sello dice «Datos del canal: hoy · API de YouTube».
