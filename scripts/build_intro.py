"""Build original, theme-aware profile typography and compact tool labels."""
from pathlib import Path
import os
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / 'assets'
FONT = os.environ.get('PROFILE_BODY_FONT', 'C:/Windows/Fonts/segoeui.ttf')
font = ImageFont.truetype(FONT, 34)
lines = [
    'dbt + Snowflake | Analytics Engineering',
    'AWS | IaC | GitHub Actions | CI/CD',
    'Agent Harnesses | Guardrails | PII Protection',
    'Automated Data Pipelines | SQL',
    'Snowflake Cost Analysis',
    'Tableau Automation | Local MCP',
]
W, H = 960, 84
ASSETS.mkdir(exist_ok=True)

for theme, background, ink in [('dark','#0D1117','#79B8FF'),('light','#FFFFFF','#2563EB')]:
    def render(text, caret=False, full_text=None):
        im=Image.new('RGB',(W,H),background)
        draw=ImageDraw.Draw(im)
        width=draw.textlength(full_text or text,font=font)
        x=(W-width)/2
        draw.text((x,18),text,font=font,fill=ink)
        if caret:
            end=x+draw.textlength(text,font=font)+5
            draw.line((end,25,end,53),fill=ink,width=2)
        return im
    render(lines[0]).save(ASSETS/f'intro-{theme}.png')
    frames=[render(lines[0])]
    durations=[2000]
    for line in lines[1:]:
        for n in range(1,len(line)+1):
            frames.append(render(line[:n],True,line))
            durations.append(30)
        frames.append(render(line))
        durations.append(2000)
    frames[0].save(ASSETS/f'intro-{theme}.gif',save_all=True,append_images=frames[1:],duration=durations,loop=0,optimize=True)

for name, color, width in [('SQL','#2F6FEB',69),('dbt','#BF544C',66),('Snowflake','#247C9D',107),('AWS','#8A5200',67),('GitHub Actions','#365A90',143),('IaC','#7254A0',57),('Tableau','#2D648C',87),('MCP','#536879',65)]:
    svg=f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="30" viewBox="0 0 {width} 30" role="img" aria-label="{name}">
<rect x=".5" y=".5" width="{width-1}" height="29" rx="6" fill="{color}"/>
<text x="{width/2}" y="20" text-anchor="middle" font-family="Segoe UI,Arial,sans-serif" font-size="14" font-weight="600" fill="white">{name}</text></svg>'''
    (ASSETS/f'skill-{name.lower().replace(" ", "-")}.svg').write_text(svg,encoding='utf-8')
print('Built original light/dark intro animations, stills, and tool labels')
