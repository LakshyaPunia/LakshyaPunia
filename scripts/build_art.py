"""Rebuild the original photographic banner. Requires Pillow; fonts may be overridden."""
from pathlib import Path
import math
import os
from PIL import Image, ImageDraw, ImageFont, ImageOps, ImageFilter

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / 'assets'
W, H = 1200, 570
DISPLAY = os.environ.get('PROFILE_DISPLAY_FONT', 'C:/Windows/Fonts/bahnschrift.ttf')
BODY = os.environ.get('PROFILE_BODY_FONT', 'C:/Windows/Fonts/segoeui.ttf')

def font(size, display=False):
    return ImageFont.truetype(DISPLAY if display else BODY, size)

def hero():
    base = Image.new('RGB', (W, H), '#091D2A')
    photo = Image.open(ASSETS / 'sydney-harbour.jpg').convert('RGB')
    photo = ImageOps.fit(photo, (650, H), centering=(0.52, 0.63))
    base.paste(photo, (550, 0))
    shade = Image.new('RGBA', (W,H))
    draw = ImageDraw.Draw(shade)
    for x in range(W):
        opacity = round(255 * max(0.08, min(1, (850-x)/350)))
        draw.line((x,0,x,H), fill=(9,29,42,opacity))
    base = Image.alpha_composite(base.convert('RGBA'), shade)
    d = ImageDraw.Draw(base)
    d.rounded_rectangle((48,36,88,76), radius=12, fill='#163D50')
    d.text((57,42),'lp',font=font(22,True),fill='#A5E8F0')
    d.text((102,44),'Lakshya Punia / Sydney',font=font(19),fill='#D2E4EC')
    d.text((45,120),'Lakshya',font=font(88,True),fill='#F1F6F8')
    d.text((45,208),'Punia.',font=font(88,True),fill='#F1F6F8')
    d.text((50,327),'Turning data into',font=font(30),fill='#DBEAF0')
    d.text((50,366),'things people use.',font=font(30),fill='#DBEAF0')
    d.text((50,439),'Machine learning  /  Full-stack development',font=font(19),fill='#A9CEDB')
    d.rounded_rectangle((953,35,1154,74),radius=19,fill=(9,29,42,210))
    d.ellipse((970,50,978,58),fill='#F5B98D')
    d.text((988,42),'Built with purpose',font=font(16),fill='#F5E7DC')
    d.line((50,510,1150,510),fill='#416375',width=2)
    for x in [50,415,780,1150]:
        d.ellipse((x-4,506,x+4,514),fill='#89D9E6')
    d.text((50,528),'Explore the work below',font=font(16),fill='#B5D1DD')
    return base.convert('RGB')

base = hero()
base.save(ASSETS / 'hero.png', optimize=True)
frames=[]
# Keep photography and type still; only a small signal moves along the route.
palette = base.quantize(colors=240)
for i in range(60):
    frame = base.copy()
    d = ImageDraw.Draw(frame)
    t=i/60
    x=50+1100*t
    for j in range(45,0,-1):
        k=(1-j/45)
        color=tuple(round(a+(b-a)*k) for a,b in zip((65,99,117),(137,217,230)))
        d.line((max(50,x-j*2),510,x,510),fill=color,width=3)
    d.ellipse((x-4,506,x+4,514),fill='#E8FAFF')
    frames.append(frame.quantize(palette=palette,dither=Image.Dither.FLOYDSTEINBERG))
frames[0].save(ASSETS/'hero.gif',save_all=True,append_images=frames[1:],duration=100,loop=0,optimize=True,disposal=1)
print('Built hero.png and hero.gif')
