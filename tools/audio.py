# -*- coding: utf-8 -*-
"""Erzeugt die MP3s mit edge-tts. Aufruf:  python tools/audio.py [dateiname ...]"""
import asyncio, os, sys
import edge_tts
sys.path.insert(0, os.path.dirname(__file__))
from content import STOPS

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VOICE = "de-DE-SeraphinaMultilingualNeural"
RATE = "-6%"


async def main(only):
    for s in STOPS:
        a = s["audio"]
        if only and a["file"] not in only:
            continue
        out = os.path.join(ROOT, "assets", "audio", a["file"] + ".mp3")
        await edge_tts.Communicate(a["text"], VOICE, rate=RATE).save(out)
        print(a["file"], os.path.getsize(out) // 1024, "KB")


asyncio.run(main(set(sys.argv[1:])))
