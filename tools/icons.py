# -*- coding: utf-8 -*-
"""Zeichnet das App-Icon (Gradierwerk-Wand mit Tropfen) und das QR-Handout-Bild."""
import os
from PIL import Image, ImageDraw
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def draw(size, pad):
    S=1024; im=Image.new('RGB',(S,S),'#204A4A'); d=ImageDraw.Draw(im)
    for y in range(S):  # sanfter Verlauf
        t=y/S; d.line([(0,y),(S,y)],fill=(int(32+20*t),int(74+36*t),int(74+30*t)))
    m=int(S*pad)
    # Gradierwerk-Wand
    x0,y0,x1,y1=m+60,m+250,S-m-60,S-m-120
    d.rounded_rectangle((x0,y0,x1,y1),radius=36,fill='#5A4631')
    for x in range(x0+30,x1,46):  # Reisig-Struktur
        d.line([(x,y0+16),(x-26,y1-16)],fill='#7A6244',width=9)
        d.line([(x-20,y0+16),(x+6,y1-16)],fill='#3F3121',width=6)
    d.rounded_rectangle((x0-20,y0-36,x1+20,y0+24),radius=22,fill='#C79A3B')  # Rinne oben
    for cx in (x0+190,(x0+x1)//2,x1-190):  # Tropfen
        cy=y0-150
        d.polygon([(cx,cy-80),(cx-48,cy+10),(cx+48,cy+10)],fill='#F1F6F4')
        d.ellipse((cx-48,cy-34,cx+48,cy+62),fill='#F1F6F4')
    return im.resize((size,size),Image.LANCZOS)
os.makedirs(os.path.join(ROOT,'icons'),exist_ok=True)
for n,s,p in [('icon-192',192,.05),('icon-512',512,.05),('apple-touch-icon',180,.05),('icon-maskable-512',512,.14)]:
    draw(s,p).save(os.path.join(ROOT,'icons',n+'.png'))
import qrcode
from content import SITE_URL
q=qrcode.QRCode(box_size=10,border=2,error_correction=qrcode.constants.ERROR_CORRECT_M); q.add_data(SITE_URL); q.make(fit=True)
q.make_image(fill_color='#204A4A',back_color='white').save(os.path.join(ROOT,'qr-code.png'))
print('ok')
