"""Create a local approximation of GitHub's README rendering for visual review."""
from pathlib import Path
from markdown_it import MarkdownIt

root = Path(__file__).resolve().parents[1]
md = MarkdownIt('commonmark', {'html': True}).enable('table')
body = md.render((root / 'README.md').read_text(encoding='utf-8'))
for title in ['Selected work', 'The toolkit', 'On the workbench']:
    body = body.replace(f'<h2>{title}</h2>', f'<h2 id="{title.lower().replace(" ", "-")}">{title}</h2>')
page = '''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Lakshya Punia — Profile preview</title>
<style>
*{box-sizing:border-box}body{margin:0;background:#0d1117;color:#e6edf3;font:16px/1.6 -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif}main{max-width:980px;margin:36px auto;border:1px solid #30363d;border-radius:6px;padding:32px}img{max-width:100%;height:auto}a{color:#79c0ff;text-decoration:none}a:hover{text-decoration:underline}a:focus-visible{outline:2px solid #79c0ff;outline-offset:3px}h2{font-size:24px;padding-bottom:8px;border-bottom:1px solid #30363d;margin-top:32px}h3{font-size:20px;margin-top:28px}p{margin:0 0 16px}code{padding:3px 6px;border-radius:6px;background:#21262d;font-size:13px}hr{height:3px;border:0;background:#30363d;margin:28px 0}table{border-collapse:collapse}th,td{padding:8px 13px;border:1px solid #30363d;text-align:left}summary{cursor:pointer}sub{font-size:12px}li{margin:5px 0}details{margin-top:28px}@media(max-width:600px){main{margin:12px;border:0;padding:12px}body{font-size:14px}h2{font-size:22px}}
@media(prefers-color-scheme:light){body{background:#fff;color:#1f2328}main,th,td,h2{border-color:#d1d9e0}a{color:#0969da}code{background:#eff1f3}hr{background:#d1d9e0}}</style><main>''' + body + '</main></html>'
(root / 'preview.html').write_text(page, encoding='utf-8')
print('Created preview.html')
