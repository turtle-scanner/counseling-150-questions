# -*- coding: utf-8 -*-
import sys, io, re, os, glob, json, subprocess
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='backslashreplace')

BASE = r'G:\내 드라이브\ANTI GRAVITY\시험준비(패턴)'
names = json.load(open(BASE + r'\교육학\scratch\undefined_names.json'))
names = [n for n in names if n != 'rgba']  # rgba 는 CSS 문자열 오탐

cands = glob.glob(BASE + r'\교육학\scratch\*.js') + glob.glob(BASE + r'\교육학\scratch\*.txt') \
      + glob.glob(BASE + r'\교육학\*.html') + [r'C:\Users\LENOVO\Desktop\sam3_update.html']
cands = [c for c in cands if os.path.isfile(c) and os.path.getsize(c) < 30_000_000]

def has_def(txt, n):
    return re.search(r'function\s+' + re.escape(n) + r'\s*\(', txt) or re.search(r'(?:const|let|var)\s+' + re.escape(n) + r'\s*=', txt)

found = {n: [] for n in names}
for c in cands:
    try:
        t = open(c, 'r', encoding='utf-8', errors='ignore').read()
    except Exception:
        continue
    for n in names:
        if has_def(t, n):
            found[n].append(os.path.basename(c))
for n in names:
    print(n, '->', found[n][:6] if found[n] else 'NOT IN ANY LOCAL FILE')

# git 이력에서도 탐색
print('\n--- git history search for names with no local source ---')
missing = [n for n in names if not found[n]]
os.chdir(BASE + r'\교육학')
revs = subprocess.run(['git', 'log', '--format=%h', '-n', '40', '--', 'index.html', 'samgukji.html', '../index.html', '../samgukji.html'], capture_output=True, text=True).stdout.split()
print('revs:', revs[:15])
