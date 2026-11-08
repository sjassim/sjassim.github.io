#!/usr/bin/env python3
"""Build the portfolio with Python's standard library. Run: python3 build.py."""
import html
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / 'src'

def render(template, values):
    for key, value in values.items():
        template = template.replace('{{' + key + '}}', str(value))
    return template

def build():
    pages = json.loads((SOURCE / 'pages.json').read_text())
    template = (SOURCE / 'templates/page.html').read_text()
    header = (SOURCE / 'templates/header.html').read_text()
    footer = (SOURCE / 'templates/footer.html').read_text()
    domain = (ROOT / 'CNAME').read_text().strip()
    for page in pages:
        navigation = []
        for url, label in [('/', 'portfolio'), ('/about/', 'om mig')]:
            current = ' aria-current="page"' if page['route'] == url else ''
            navigation.append(f'<a href="{url}"{current}>{label}</a>')
        values = {
            'page_styles': ('<link rel="stylesheet" href="/assets/cases.css?v=' + hashlib.sha256((ROOT / 'assets/cases.css').read_bytes()).hexdigest()[:10] + '">') if page['kind'] == 'case' else '',
            'style_version': hashlib.sha256((ROOT / 'assets/site.css').read_bytes()).hexdigest()[:10],
            'script_version': hashlib.sha256((ROOT / 'assets/site.js').read_bytes()).hexdigest()[:10],
            'font_version': hashlib.sha256((ROOT / 'assets/fonts.css').read_bytes()).hexdigest()[:10],
            'title': html.escape(page['title'], quote=True),
            'heading': html.escape(page['title'].split(' — ')[0]),
            'description': html.escape(page['description'], quote=True),
            'url': 'https://' + domain + page['route'],
            'image': 'https://' + domain + page['image'],
            'kind': page['kind'],
            'header': render(header, {'navigation': '\n'.join(navigation)}),
            'footer': footer,
            'content': (SOURCE / 'pages' / page['file']).read_text(),
        }
        output = ROOT / page['route'].strip('/') / 'index.html'
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text('\n'.join(line.rstrip() for line in render(template, values).splitlines()) + '\n')
    # Keep old bookmarks working without retaining the removed contact page.
    redirect = ROOT / 'kontakt/index.html'
    redirect.parent.mkdir(exist_ok=True)
    redirect.write_text('<!doctype html>\n<html lang="sv-SE"><head><meta charset="utf-8"><meta name="robots" content="noindex"><meta http-equiv="refresh" content="0;url=/"><title>Shervan Jassim</title></head><body><a href="/">Till portfolio</a><script>location.replace("/");</script></body></html>\n')
    print(f'Built {len(pages)} pages and the old contact-page redirect.')

if __name__ == '__main__':
    build()
