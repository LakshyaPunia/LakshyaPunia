"""Refresh a compact footer from public GitHub repository metadata."""
import datetime as dt
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
    languages=sorted({r['language'] for r in repos if r.get('language')})
    now=dt.datetime.now(dt.timezone.utc).strftime('%d %b %Y')
    body=f'<p align="center"><sub>{len(repos)} public projects · Updated {now} UTC</sub></p>'
    readme=ROOT/'README.md'
    original=readme.read_text(encoding='utf-8')
    updated,count=re.subn(r'<!-- ACTIVITY:START -->.*?<!-- ACTIVITY:END -->',f'<!-- ACTIVITY:START -->\n{body}\n<!-- ACTIVITY:END -->',original,flags=re.S)
    if count != 1:
        raise RuntimeError('Expected exactly one activity marker pair; refusing to change the README')
    # No file changes until every API request and content validation succeeds.
    readme.write_text(updated,encoding='utf-8')
    print(f'Refreshed {len(repos)} public projects, {len(languages)} primary languages')

if __name__=='__main__':
    main()
