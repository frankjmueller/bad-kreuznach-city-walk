# Bad Kreuznach — Offline-Guide für Sandra

Ein ruhiger Spaziergang ab dem **St. Franziska-Stift** durch Salinental, Roseninsel,
Kurpark, Pauluskirche, Brückenhäuser und Eiermarkt (plus Bonus: Römerhalle, Kauzenburg).
Mobile-first, komplett offline nutzbar (PWA), mit deutschen Audio-Geschichten.

Live: https://frankjmueller.github.io/bad-kreuznach-city-walk/
Druck-Handout mit QR-Code: `/handout.html`

- Kein Backend, keine Datenbank — HTML + Service Worker.
- Bilder, Audio und Schrift werden beim ersten Besuch vollständig vorgeladen.
- Google-Maps-Buttons arbeiten mit Koordinaten (funktionieren mit Offline-Karten).

## Inhalte ändern

Alle Texte, Koordinaten und Audio-Skripte stehen in `tools/content.py`.

```
python tools/build.py        # erzeugt index.html, sw.js, ATTRIBUTION.md
python tools/audio.py        # alle MP3s neu (oder: audio.py salinental eiermarkt)
python tools/icons.py        # Icons + QR-Code
```

**Bei jeder Inhaltsänderung `VERSION` in `tools/content.py` hochzählen** (v1 → v2) —
sonst holen die Handys die neue Fassung nicht. Danach committen und pushen;
GitHub Pages veröffentlicht automatisch.

Voraussetzungen: Python 3, `pip install edge-tts pillow qrcode`.
Stimme: `de-DE-SeraphinaMultilingualNeural`, Tempo −6 %.

## Fotos

Alle Fotos von Wikimedia Commons, Lizenzen in `ATTRIBUTION.md`.
