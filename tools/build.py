# -*- coding: utf-8 -*-
"""Erzeugt index.html, sw.js, manifest.json und ATTRIBUTION.md aus content.py.
Aufruf (aus dem Repo-Root):  python tools/build.py"""
import json, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from content import STOPS, HOME, SITE_URL, REPO_URL, VERSION

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PIN = '<svg viewBox="0 0 24 24"><path d="M12 2C8.1 2 5 5.1 5 9c0 5.2 7 13 7 13s7-7.8 7-13c0-3.9-3.1-7-7-7zm0 9.5A2.5 2.5 0 1 1 12 6.5a2.5 2.5 0 0 1 0 5z"/></svg>'
PLAY = '<svg viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg>'


def maps_url(lat, lon):
    return f"https://www.google.com/maps/search/?api=1&query={lat}%2C{lon}"


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
          <a class="maps" href="{maps_url(s["lat"], s["lon"])}" target="_blank" rel="noopener">
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
    """3×3-Schlangenlinie: Start,1,2 → 3,4,5 (rückwärts) → 6,7,8."""
    xs = [40, 180, 320]
    ys = [60, 175, 290]
    pts = []
    for i, s in enumerate(STOPS):
        row, col = divmod(i, 3)
        if row % 2 == 1:
            col = 2 - col
        pts.append((xs[col], ys[row]))
    path = "M" + " L".join(f"{x},{y}" for x, y in pts[:3])
    path = f"M{pts[0][0]},{pts[0][1]} H{pts[2][0]} V{pts[3][1]} H{pts[5][0]} V{pts[6][1]} H{pts[8][0]}"
    out = [f'<path d="{path}" fill="none" stroke="#C79A3B" stroke-width="5" stroke-linejoin="round" '
           f'stroke-linecap="round" stroke-dasharray="1 9"/>']
    for i, ((x, y), s) in enumerate(zip(pts, STOPS)):
        bonus = s["kind"] == "bonus"
        fill = "#7B2D3B" if bonus else "#2F6B6B"
        # Wo die Linie nach unten weiterläuft, steht die Beschriftung über der Perle
        label_y = y - 24 if i in (2, 5) else y + 30
        txt = "".join(
            f'<text x="{x}" y="{label_y + 11 * i}" font-size="10.5" fill="currentColor" text-anchor="middle">{l}</text>'
            for i, l in enumerate(s["map"]))
        out.append(f'<a href="#{s["id"]}"><circle cx="{x}" cy="{y}" r="14" fill="{fill}" stroke="#C79A3B" stroke-width="2.5"/>'
                   f'<text x="{x}" y="{y + 4.5}" font-size="12" fill="#fff" text-anchor="middle" font-weight="bold">{s["bead"]}</text>{txt}</a>')
    return "\n      ".join(out)


def build_html():
    tpl = open(os.path.join(os.path.dirname(__file__), "template.html"), encoding="utf-8").read()
    route = "\n".join(card(s) for s in STOPS) + "\n" + home_card()
    return (tpl.replace("{{ROUTE}}", route).replace("{{MAP}}", svg_map())
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
    files = {"stift": "stift", "salinen": "salinen", "roseninsel": "roseninsel", "kurpark": "kurpark",
             "paulus": "paulus", "brueckenhaeuser": "brueckenhaeuser", "nikolaus": "nikolaus",
             "roemerhalle": "roemerhalle", "kauzenburg": "kauzenburg"}
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
