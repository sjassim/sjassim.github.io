#!/usr/bin/env python3
"""Check generated pages and local links before publishing: python3 check.py."""
import json
import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parent
class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.urls = []
        self.h1 = 0
        self.refresh = None
        self.canonical = None
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.h1 += tag == 'h1'
        if tag == 'meta' and attrs.get('http-equiv', '').lower() == 'refresh':
            self.refresh = attrs.get('content')
        if tag == 'link' and attrs.get('rel') == 'canonical':
            self.canonical = attrs.get('href')
        for name in ['href', 'src']:
            if name in attrs:
                self.urls.append(attrs[name])

def check():
    errors = []
    pages = json.loads((ROOT / 'src/pages.json').read_text())
    redirects = json.loads((ROOT / 'src/redirects.json').read_text())
    routes = {page['route'] for page in pages}
    domain = (ROOT / 'CNAME').read_text().strip()
    for page in pages:
        file = ROOT / page['route'].strip('/') / 'index.html'
        parser = Page()
        parser.feed(file.read_text())
        if parser.h1 != 1:
            errors.append(f'{file.relative_to(ROOT)}: expected one page heading')
        for url in parser.urls:
            if not url.startswith('/') or url.startswith('//'):
                continue
            path = unquote(urlsplit(url).path)
            if path.rstrip('/') + '/' in redirects:
                errors.append(f'{file.relative_to(ROOT)}: link still uses old address {url}')
            target = ROOT / path.lstrip('/')
            if target.is_dir():
                target /= 'index.html'
            if not target.is_file():
                errors.append(f'{file.relative_to(ROOT)}: missing {url}')
        if re.search(r'--(?:area(?:-wide)?|rows(?:-wide)?)\s*:', file.read_text()) or 'class="layout-grid"' in file.read_text():
            errors.append(f'{file.relative_to(ROOT)}: numbered layout grid remains')
        if re.search(r'class="[^"]*(?:sqs-|fe-block|fluid-engine)', file.read_text()):
            errors.append(f'{file.relative_to(ROOT)}: old editor markup remains')
    for old, target in redirects.items():
        if old in routes or target not in routes:
            errors.append(f'Invalid redirect: {old} -> {target}')
            continue
        file = ROOT / old.strip('/') / 'index.html'
        if not file.is_file():
            errors.append(f'Missing redirect page: {old}')
            continue
        parser = Page()
        parser.feed(file.read_text())
        if parser.refresh != '0;url=' + target or parser.canonical != 'https://' + domain + target or target not in parser.urls:
            errors.append(f'Redirect target mismatch: {old} -> {target}')
    for css in (ROOT / 'assets').glob('*.css'):
        for url in re.findall(r'url\([\"\']?([^\)\"\']+)', css.read_text()):
            if url.startswith('/') and not (ROOT / url.lstrip('/')).is_file():
                errors.append(f'{css.name}: missing {url}')
    if errors:
        raise SystemExit('\n'.join(errors))
    print(f'Checked {len(pages)} pages and {len(redirects)} redirects: headings, links, images, styles and redirect targets pass.')

if __name__ == '__main__':
    check()
