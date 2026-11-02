"""Fetch public GitHub metadata and generate a local, dependency-free activity panel."""
import datetime as dt
import html
import json
import os
from pathlib import Path
import re
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
USER = 'LakshyaPunia'

def api(path):
    headers = {'Accept': 'application/vnd.github+json', 'User-Agent': 'LakshyaPunia-profile'}
    token = os.environ.get('GH_TOKEN') or os.environ.get('GITHUB_TOKEN')
    if token:
        headers['Authorization'] = f'Bearer {token}'
    request = urllib.request.Request('https://api.github.com/' + path, headers=headers)
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.load(response)

def main():
    repos=[]
    page=1
    while True:
        batch=api(f'users/{USER}/repos?type=owner&per_page=100&page={page}')
        repos.extend(r for r in batch if not r.get('private') and not r['fork'] and r['name'].lower()!=USER.lower())
        if len(batch)<100:
            break
        page+=1
    recent=sorted((r for r in repos if r.get('pushed_at')),key=lambda r:r['pushed_at'],reverse=True)[:3]
    languages=sorted({r['language'] for r in repos if r.get('language')})
    now=dt.datetime.now(dt.timezone.utc).strftime('%d %b %Y')
    esc=html.escape
    parts=[f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="390" viewBox="0 0 1200 390" role="img" aria-labelledby="title desc">
<title id="title">Lakshya's public workbench</title><desc id="desc">{len(repos)} original public project repositories. {len(languages)} primary repository languages. Refreshed {now} UTC.</desc>
<rect width="1200" height="390" rx="18" fill="#091D2A"/>
<g font-family="Segoe UI,Arial,sans-serif" fill="#E8F1F5">
<text x="40" y="48" font-size="24">Always building.</text>
<text x="1160" y="47" text-anchor="end" font-size="16" fill="#A9CEDB">Refreshed {now} UTC</text>
<text x="40" y="121" font-size="49">{len(repos):02}</text><text x="125" y="104" font-size="19">public projects</text><text x="125" y="131" font-size="15" fill="#A9CEDB">Original repositories, excluding this profile</text>
<text x="650" y="121" font-size="49">{len(languages):02}</text><text x="735" y="104" font-size="19">primary languages</text><text x="735" y="131" font-size="15" fill="#A9CEDB">{esc(' / '.join(languages))}</text>
<path d="M40 160H1160" stroke="#315366"/>
<text x="40" y="198" font-size="17" fill="#89D9E6">Recent repository pushes</text>''']
    for i,repo in enumerate(recent):
        y=242+i*46
        name=esc(repo['name'])
        date=repo['pushed_at'][:10]
        parts.append(f'<circle cx="46" cy="{y-6}" r="4" fill="#F5B98D"/><text x="66" y="{y}" font-size="20">{name}</text><text x="1160" y="{y}" text-anchor="end" font-size="17" fill="#A9CEDB">{date}</text>')
    parts.append('</g></svg>')
    svg='\n'.join(parts)
    body=f'**{len(repos)} public projects** · **{len(languages)} primary languages** · Updated {now} (UTC).\n\n'
    body+='\n'.join(f"- [{r['name']}]({r['html_url']}) — last pushed {r['pushed_at'][:10]}." for r in recent)
    readme=ROOT/'README.md'
    original=readme.read_text(encoding='utf-8')
    updated,count=re.subn(r'<!-- ACTIVITY:START -->.*?<!-- ACTIVITY:END -->',f'<!-- ACTIVITY:START -->\n{body}\n<!-- ACTIVITY:END -->',original,flags=re.S)
    if count != 1:
        raise RuntimeError('Expected exactly one activity marker pair; refusing to change the README')
    # No file changes until every API request and content validation succeeds.
    (ROOT/'assets'/'pulse.svg').write_text(svg,encoding='utf-8')
    readme.write_text(updated,encoding='utf-8')
    print(f'Refreshed {len(repos)} public projects, {len(languages)} primary languages')

if __name__=='__main__':
    main()
