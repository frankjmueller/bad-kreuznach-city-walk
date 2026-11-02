# -*- coding: utf-8 -*-
"""Erzeugt index.html, sw.js, manifest.json und ATTRIBUTION.md aus content.py.
Aufruf (aus dem Repo-Root):  python tools/build.py"""
import json, os, sys
from urllib.parse import quote_plus
sys.path.insert(0, os.path.dirname(__file__))
from content import STOPS, HOME, EATS, EATS_INTRO, MORE, MORE_INTRO, SITE_URL, REPO_URL, VERSION

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PIN = '<svg viewBox="0 0 24 24"><path d="M12 2C8.1 2 5 5.1 5 9c0 5.2 7 13 7 13s7-7.8 7-13c0-3.9-3.1-7-7-7zm0 9.5A2.5 2.5 0 1 1 12 6.5a2.5 2.5 0 0 1 0 5z"/></svg>'
PLAY = '<svg viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg>'


def maps_url(lat=None, lon=None, query=None):
    """Koordinaten bevorzugt (funktionieren mit Offline-Karten), sonst Textsuche."""
    if lat is not None:
        return f"https://www.google.com/maps/search/?api=1&query={lat}%2C{lon}"
    return "https://www.google.com/maps/search/?api=1&query=" + quote_plus(query)


def card(s):
    boxes = "".join(f'<div class="{k}">{t}</div>\n          ' for k, t in s["boxes"])
    moment = f'<div class="moment"><b>🍃 Moment:</b> {s["moment"]}</div>\n          ' if s["moment"] else ""
    body = "\n          ".join(f"<p>{p}</p>" for p in s["body"])
    a = s["audio"]
    lazy = "" if s["id"] == "start" else ' loading="lazy"'
    cls = {"start": "stop transit", "stop": "stop", "bonus": "stop bonus"}[s["kind"]]
    return f'''    <li class="{cls}" id="{s["id"]}">
      <div class="bead"{' aria-hidden="true"' if s["kind"] == "start" else ""}>{s["bead"]}</div>
      <article class="card">
        <img src="assets/img/{s["img"]}.webp" alt="{s["alt"]}" style="object-position:{s["pos"]}"{lazy}>
        <div class="pad">
          <p class="eyebrow">{s["eyebrow"]}</p>
          <h2>{s["title"]}</h2>
          <p class="walk">{s["walk"]}</p>
          {body}
          {boxes}{moment}<div class="player" data-src="assets/audio/{a["file"]}.mp3">
            <button aria-label="Abspielen: {a["label"]}">{PLAY}</button>
            <div class="meta"><p class="label">🎧 {a["label"]}</p>
            <div class="bar"><div class="fill"></div></div></div>
            <span class="time">–:–</span>
          </div>
          <a class="maps" href="{maps_url(s["lat"], s["lon"], s.get("query"))}" target="_blank" rel="noopener">
            {PIN}
            {s["maps"]}</a>
        </div>
      </article>
    </li>
'''


def home_card():
    h = HOME
    s0 = STOPS[0]
    return f'''    <li class="stop transit" id="home">
      <div class="bead" aria-hidden="true">🏠</div>
      <article class="card">
        <div class="pad">
          <p class="eyebrow">Zurück · Ganz in Ruhe</p>
          <h2>{h["title"]}</h2>
          <p class="walk">{h["walk"]}</p>
          <p>{h["body"]}</p>
          <div class="tip">{h["tip"]}</div>
          <a class="maps" href="{maps_url(s0["lat"], s0["lon"])}" target="_blank" rel="noopener">
            {PIN}
            Zurück zum St. Franziska-Stift</a>
        </div>
      </article>
    </li>
'''


def svg_map():
    """Schlangenlinie in 3 Spalten: Zeile für Zeile, jede zweite Zeile rückwärts."""
    xs = [40, 180, 320]
    rows = (len(STOPS) + 2) // 3
    ys = [60 + 115 * r for r in range(rows)]
    pts = []
    for i in range(len(STOPS)):
        row, col = divmod(i, 3)
        if row % 2 == 1:
            col = 2 - col
        pts.append((xs[col], ys[row]))
    d = f"M{pts[0][0]},{pts[0][1]}"
    for r in range(rows):
        first, last = r * 3, min(r * 3 + 2, len(STOPS) - 1)
        d += f" H{pts[last][0]}"
        if r < rows - 1:
            d += f" V{ys[r + 1]}"
    out = [f'<path d="{d}" fill="none" stroke="#C79A3B" stroke-width="5" stroke-linejoin="round" '
           f'stroke-linecap="round" stroke-dasharray="1 9"/>']
    for i, ((x, y), s) in enumerate(zip(pts, STOPS)):
        bonus = s["kind"] == "bonus"
        fill = "#7B2D3B" if bonus else "#2F6B6B"
        row, col = divmod(i, 3)
        # Wo die Linie am Zeilenende nach unten weiterläuft, steht die Beschriftung über der Perle
        row_end = (col == 2 and i < len(STOPS) - 1)
        lines = s["map"]
        if row_end:
            label_y = y - 24 - 11 * (len(lines) - 1)
        else:
            label_y = y + 30
        txt = "".join(
            f'<text x="{x}" y="{label_y + 11 * j}" font-size="10.5" fill="currentColor" text-anchor="middle">{l}</text>'
            for j, l in enumerate(lines))
        out.append(f'<a href="#{s["id"]}"><circle cx="{x}" cy="{y}" r="14" fill="{fill}" stroke="#C79A3B" stroke-width="2.5"/>'
                   f'<text x="{x}" y="{y + 4.5}" font-size="12" fill="#fff" text-anchor="middle" font-weight="bold">{s["bead"]}</text>{txt}</a>')
    return "\n      ".join(out), 60 + 115 * (rows - 1) + 60


def list_html(intro, groups):
    """Gruppierte Liste (Pausen & Essen, Weitere Ziele); Maps-Button nur bei Ortsangabe."""
    parts = [f'<p class="eats-intro">{intro}</p>']
    for g in groups:
        parts.append(f'<h3 class="eats-group">{g["group"]}</h3>')
        for it in g["items"]:
            has_loc = it.get("lat") is not None or it.get("query")
            btn = ""
            if has_loc:
                url = maps_url(it.get("lat"), it.get("lon"), it.get("query"))
                btn = (f'<a class="eat-map" href="{url}" target="_blank" rel="noopener" '
                       f'aria-label="{it["name"]} in Google Maps">{PIN}</a>')
            parts.append(
                f'<div class="eat"><div><b>{it["name"]}</b><span class="where">{it["where"]}</span>'
                f'<p>{it["note"]}</p></div>{btn}</div>')
    return "\n      ".join(parts)


def build_html():
    tpl = open(os.path.join(os.path.dirname(__file__), "template.html"), encoding="utf-8").read()
    route = "\n".join(card(s) for s in STOPS) + "\n" + home_card()
    svg, height = svg_map()
    return (tpl.replace("{{ROUTE}}", route).replace("{{MAP}}", svg).replace("{{MAPH}}", str(height))
               .replace("{{EATS}}", list_html(EATS_INTRO, EATS))
               .replace("{{MORE}}", list_html(MORE_INTRO, MORE))
               .replace("{{VERSION}}", VERSION).replace("{{REPO}}", REPO_URL))


def build_sw():
    img = sorted({f"./assets/img/{s['img']}.webp" for s in STOPS})
    aud = [f"./assets/audio/{s['audio']['file']}.mp3" for s in STOPS]
    assets = ["./", "./index.html", "./manifest.json", "./assets/fonts/bricolage.woff2",
              "./icons/icon-192.png", "./icons/icon-512.png", "./icons/apple-touch-icon.png",
              "./icons/icon-maskable-512.png"] + img + aud
    lst = ",\n  ".join(f"'{a}'" for a in assets)
    tpl = open(os.path.join(os.path.dirname(__file__), "sw.template.js"), encoding="utf-8").read()
    return tpl.replace("{{VERSION}}", VERSION).replace("{{ASSETS}}", lst)


def build_attr():
    meta = json.load(open(os.path.join(os.path.dirname(__file__), "photo-meta.json"), encoding="utf-8"))
    files = sorted({s["img"] for s in STOPS}, key=[s["img"] for s in STOPS].index)
    lines = ["# Foto-Nachweise", "", "Alle Fotos stammen von [Wikimedia Commons](https://commons.wikimedia.org/) "
             "und wurden verkleinert und als WebP gespeichert.", ""]
    for k in files:
        m = meta[k]
        lines.append(f"- **{m['title'][5:]}** (`assets/img/{k}.webp`) — {m['artist']}, {m['license']}. [Quelle]({m['page']})")
    return "\n".join(lines) + "\n"


if __name__ == "__main__":
    for name, content in [("index.html", build_html()), ("sw.js", build_sw()), ("ATTRIBUTION.md", build_attr())]:
        open(os.path.join(ROOT, name), "w", encoding="utf-8", newline="\n").write(content)
        print("geschrieben:", name)
