#!/usr/bin/env python3
"""Conector directo con YouTube: lee tu canal con las APIs oficiales de Google y genera
un JSON que el Radar muestra (vídeos, retención, impresiones, CTR, ingresos, tráfico, audiencia).

Uso:
    python conector/youtube_sync.py [--salida yt_snapshot.json] [--dias 90]

Credenciales (variables de entorno, nunca en el código):
    YT_CLIENT_ID, YT_CLIENT_SECRET   del «ID de cliente OAuth» de tu proyecto de Google Cloud
    YT_REFRESH_TOKEN                 el que te da el OAuth Playground al autorizar tu canal
Guía paso a paso: conector/README.md
"""
import argparse, csv, datetime as dt, io, json, os, re, sys, time

try:
    import requests
except ImportError:
    sys.exit("Falta requests: pip install requests")

DATA = "https://youtube.googleapis.com/youtube/v3"
ANALYTICS = "https://youtubeanalytics.googleapis.com/v2/reports"
REPORTING = "https://youtubereporting.googleapis.com/v1"
REACH = "channel_reach_basic_a1"  # informe diario con impresiones y CTR de miniaturas por vídeo


def log(m):
    print(time.strftime("%H:%M:%S"), m, flush=True)


class YT:
    def __init__(self):
        cid, sec, rt = (os.environ.get(k) for k in ("YT_CLIENT_ID", "YT_CLIENT_SECRET", "YT_REFRESH_TOKEN"))
        if not (cid and sec and rt):
            sys.exit("Faltan YT_CLIENT_ID, YT_CLIENT_SECRET o YT_REFRESH_TOKEN (ver conector/README.md).")
        r = requests.post("https://oauth2.googleapis.com/token", timeout=30,
                          data={"client_id": cid, "client_secret": sec, "refresh_token": rt, "grant_type": "refresh_token"})
        if r.status_code != 200:
            sys.exit(f"Google rechazó las credenciales ({r.status_code}): {r.text[:300]}\n"
                     "Si dice invalid_grant, el refresh token caducó: repite el paso del OAuth Playground.")
        self.h = {"Authorization": "Bearer " + r.json()["access_token"]}
        self.scopes = r.json().get("scope", "")

    def get(self, url, **params):
        for attempt in range(4):
            r = requests.get(url, headers=self.h, params=params, timeout=60)
            if r.status_code in (429, 500, 503):
                time.sleep(5 * (attempt + 1))
                continue
            if r.status_code >= 400:
                raise RuntimeError(f"{url.split('/')[-1]} {r.status_code}: {r.text[:300]}")
            return r.json()
        raise RuntimeError(f"{url} sin respuesta")

    def report(self, start, end, metrics, dimensions=None, sort=None, max_results=None, filters=None):
        p = {"ids": "channel==MINE", "startDate": start, "endDate": end, "metrics": metrics}
        if dimensions:
            p["dimensions"] = dimensions
        if sort:
            p["sort"] = sort
        if max_results:
            p["maxResults"] = max_results
        if filters:
            p["filters"] = filters
        d = self.get(ANALYTICS, **p)
        cols = [c["name"] for c in d.get("columnHeaders", [])]
        return [dict(zip(cols, row)) for row in d.get("rows", []) or []]


def iso_minutes(s):
    m = re.match(r"P(?:(\d+)D)?T?(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?", s or "")
    if not m:
        return None
    d, h, mi, se = (int(x or 0) for x in m.groups())
    return round((d * 86400 + h * 3600 + mi * 60 + se) / 60, 2)


def reach_data(yt, days=28):
    """Impresiones y CTR por vídeo desde la YouTube Reporting API. La primera vez crea el trabajo;
    Google tarda 24-48 h en generar los primeros informes."""
    jobs = yt.get(f"{REPORTING}/jobs").get("jobs", [])
    job = next((j for j in jobs if j.get("reportTypeId") == REACH), None)
    if not job:
        r = requests.post(f"{REPORTING}/jobs", headers=yt.h, timeout=30, json={"reportTypeId": REACH, "name": "radar-reach"})
        if r.status_code >= 400:
            return {"estado": f"no se pudo crear el informe de alcance: {r.text[:200]}"}, {}
        return {"estado": "informe de impresiones y CTR creado; Google lo genera en 24-48 h"}, {}
    since = (dt.datetime.utcnow() - dt.timedelta(days=days + 3)).strftime("%Y-%m-%dT%H:%M:%SZ")
    reports, token = [], None
    while True:
        p = {"createdAfter": since}
        if token:
            p["pageToken"] = token
        d = yt.get(f"{REPORTING}/jobs/{job['id']}/reports", **p)
        reports += d.get("reports", [])
        token = d.get("nextPageToken")
        if not token:
            break
    if not reports:
        return {"estado": "esperando a que Google genere el primer informe (24-48 h desde que se creó)"}, {}
    per = {}
    for rep in sorted(reports, key=lambda x: x.get("startTime", "")):
        r = requests.get(rep["downloadUrl"], headers=yt.h, timeout=120)
        if r.status_code >= 400:
            continue
        rows = csv.DictReader(io.StringIO(r.content.decode("utf-8-sig")))
        for row in rows:
            vid = row.get("video_id")
            if not vid:
                continue
            imp_key = next((k for k in row if k.endswith("impressions") and "ctr" not in k), None)
            ctr_key = next((k for k in row if k.endswith("impressions_ctr")), None)
            imp = float(row.get(imp_key) or 0) if imp_key else 0
            ctr = float(row.get(ctr_key) or 0) if ctr_key else 0
            a = per.setdefault(vid, {"imp": 0.0, "clicks": 0.0})
            a["imp"] += imp
            a["clicks"] += imp * (ctr if ctr <= 1 else ctr / 100)
    out = {v: {"imp28": int(a["imp"]), "ctr28": round(a["clicks"] / a["imp"] * 100, 2) if a["imp"] else None} for v, a in per.items()}
    return {"estado": f"ok · {len(reports)} informes diarios", "desde": since[:10]}, out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--salida", default="yt_snapshot.json")
    ap.add_argument("--dias", type=int, default=90)
    a = ap.parse_args()
    yt = YT()
    today = dt.date.today()
    end = today.isoformat()
    start = (today - dt.timedelta(days=a.dias)).isoformat()
    avisos = []

    ch = yt.get(f"{DATA}/channels", part="snippet,statistics,contentDetails", mine="true")["items"][0]
    created = ch["snippet"]["publishedAt"][:10]
    log(f"Canal: {ch['snippet']['title']} · {ch['statistics'].get('subscriberCount')} inscritos")

    ids, token = [], None
    uploads = ch["contentDetails"]["relatedPlaylists"]["uploads"]
    while True:
        p = {"part": "contentDetails", "playlistId": uploads, "maxResults": 50}
        if token:
            p["pageToken"] = token
        d = yt.get(f"{DATA}/playlistItems", **p)
        ids += [x["contentDetails"]["videoId"] for x in d.get("items", [])]
        token = d.get("nextPageToken")
        if not token:
            break
    vids = {}
    for i in range(0, len(ids), 50):
        d = yt.get(f"{DATA}/videos", part="snippet,statistics,contentDetails", id=",".join(ids[i:i + 50]))
        for v in d.get("items", []):
            st = v.get("statistics", {})
            t = v["snippet"]["title"]
            vids[v["id"]] = {"id": v["id"], "t": t, "d": v["snippet"]["publishedAt"][:10],
                             "dur": iso_minutes(v["contentDetails"].get("duration")), "views": int(st.get("viewCount", 0)),
                             "likes": int(st.get("likeCount", 0)), "comments": int(st.get("commentCount", 0)),
                             "length": len(t), "caps": sum(c.isupper() for c in t) > 0.6 * sum(c.isalpha() for c in t)}
    log(f"Vídeos: {len(vids)}")

    life = yt.report(created, end, "views,estimatedMinutesWatched,averageViewDuration,averageViewPercentage,subscribersGained",
                     "video", "-views", 200)
    for r in life:
        v = vids.get(r["video"])
        if v:
            v["avd"] = int(r["averageViewDuration"])
            v["ret"] = round(float(r["averageViewPercentage"]), 1)
            v["subs"] = int(r["subscribersGained"])
            v["min"] = int(r["estimatedMinutesWatched"])
    recent = yt.report(start, end, "views,averageViewDuration,subscribersGained", "video", "-views", 200)
    for r in recent:
        v = vids.get(r["video"])
        if v:
            v["v90"] = int(r["views"])
            v["subs90"] = int(r["subscribersGained"])
    try:
        rev = yt.report(start, end, "estimatedRevenue,playbackBasedCpm", "video", "-estimatedRevenue", 200)
        for r in rev:
            v = vids.get(r["video"])
            if v:
                v["rev90"] = round(float(r["estimatedRevenue"]), 2)
                v["cpm"] = round(float(r["playbackBasedCpm"]), 2)
    except Exception as e:
        avisos.append("ingresos no disponibles (falta el permiso yt-analytics-monetary o el canal no está monetizado)")

    daily = yt.report((today - dt.timedelta(days=120)).isoformat(), end, "views,subscribersGained,subscribersLost,estimatedMinutesWatched", "day", "day")
    traffic = yt.report(start, end, "views", "insightTrafficSourceType", "-views")
    demo = yt.report(start, end, "viewerPercentage", "ageGroup,gender")

    try:
        reach_state, reach = reach_data(yt)
    except Exception as e:
        reach_state, reach = {"estado": f"error: {str(e)[:200]}"}, {}
    for vid, r in reach.items():
        if vid in vids:
            vids[vid].update(r)

    TR = {"RELATED_VIDEO": "Vídeos sugeridos", "SUBSCRIBER": "Suscriptores (inicio/feed)", "YT_OTHER_PAGE": "Otras páginas de YouTube",
          "NO_LINK_OTHER": "Directo / sin enlace", "YT_SEARCH": "Búsqueda de YouTube", "EXT_URL": "Sitios externos",
          "YT_CHANNEL": "Página del canal", "PLAYLIST": "Listas", "END_SCREEN": "Pantalla final", "NOTIFICATION": "Notificaciones", "SHORTS": "Shorts"}
    age, gender = {}, {}
    for r in demo:
        g = r["ageGroup"].replace("age", "").replace("-", "–")
        g = g[:-1] + "+" if g.endswith("–") else g
        age[g] = age.get(g, 0) + float(r["viewerPercentage"])
        k = "Mujeres" if r["gender"] == "female" else "Hombres" if r["gender"] == "male" else None
        if k:
            gender[k] = gender.get(k, 0) + float(r["viewerPercentage"])
    weekly = {}
    for r in daily:
        d = dt.date.fromisoformat(r["day"])
        wk = (d - dt.timedelta(days=d.weekday())).isoformat()
        weekly[wk] = weekly.get(wk, 0) + int(r["views"])

    def s(n):
        return sum(int(r["views"]) for r in daily[-n:]), sum(int(r["subscribersGained"]) - int(r["subscribersLost"]) for r in daily[-n:])
    (v7, s7), (v30, s30), (v90, s90) = s(7), s(30), s(90)
    out = {
        "at": dt.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"), "source": "youtube-api", "scopes": yt.scopes,
        "channel": {"id": ch["id"], "title": ch["snippet"]["title"], "subs": int(ch["statistics"].get("subscriberCount", 0)),
                    "views": int(ch["statistics"].get("viewCount", 0)), "videos": int(ch["statistics"].get("videoCount", 0)),
                    "period": {"v7": v7, "v30": v30, "v90": v90, "s7": s7, "s30": s30, "s90": s90},
                    "weekly": sorted(weekly.items())[-17:],
                    "daily": [[r["day"], int(r["views"]), int(r["subscribersGained"]) - int(r["subscribersLost"])] for r in daily[-30:]],
                    "traffic": sorted(([TR.get(r["insightTrafficSourceType"], r["insightTrafficSourceType"]), int(r["views"])] for r in traffic), key=lambda x: -x[1])[:10],
                    "age": [[k, round(v, 1)] for k, v in age.items()], "gender": [[k, round(v, 1)] for k, v in gender.items()]},
        "videos": sorted(vids.values(), key=lambda v: v["d"], reverse=True),
        "reach": reach_state, "avisos": avisos,
    }
    json.dump(out, open(a.salida, "w", encoding="utf-8"), ensure_ascii=False)
    con_ctr = sum(1 for v in vids.values() if v.get("ctr28") is not None)
    log(f"Listo: {a.salida} · {len(vids)} vídeos · {con_ctr} con CTR · alcance: {reach_state.get('estado')}" + (f" · avisos: {'; '.join(avisos)}" if avisos else ""))


if __name__ == "__main__":
    main()
