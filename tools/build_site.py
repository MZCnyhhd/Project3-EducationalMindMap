# -*- coding: utf-8 -*-
"""组装 GitHub Pages 站点：把根目录 index.html 拷贝到 docs/（幂等）。"""
import os, shutil, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS = os.path.join(ROOT, 'docs')

def main():
    if os.path.isdir(DOCS):
        shutil.rmtree(DOCS)
    os.makedirs(DOCS)
    src = os.path.join(ROOT, 'index.html')
    if not os.path.isfile(src):
        print('ERROR: index.html not found'); sys.exit(1)
    shutil.copy2(src, os.path.join(DOCS, 'index.html'))
    print('build_site: docs/index.html written (%d bytes)' % os.path.getsize(os.path.join(DOCS, 'index.html')))

if __name__ == '__main__':
    main()
