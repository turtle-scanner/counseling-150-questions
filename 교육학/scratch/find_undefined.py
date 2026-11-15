# -*- coding: utf-8 -*-
import sys, io, re, json
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='backslashreplace')
from playwright.sync_api import sync_playwright

PATH = sys.argv[1] if len(sys.argv) > 1 else r'C:\Users\LENOVO\Desktop\sam3_update.html'
html = open(PATH, 'r', encoding='utf-8', errors='ignore').read()
scripts = re.findall(r'<script(?:\s+[^>]*)?>(.*?)</script>', html, re.DOTALL)
code = max(scripts, key=len)

# 문자열/주석 제거 후 '이름(' 호출 추출 ('.' 뒤 메서드, 'function 이름(' 선언 제외)
stripped = re.sub(r'//[^\n]*', '', code)
stripped = re.sub(r'/\*.*?\*/', '', stripped, flags=re.DOTALL)
calls = set()
for m in re.finditer(r'(?<![\w$.])([A-Za-z_$][\w$]*)\s*\(', stripped):
    name = m.group(1)
    pre = stripped[max(0, m.start() - 9):m.start()]
    if pre.rstrip().endswith('function'):
        continue
    calls.add(name)
KW = {'if','for','while','switch','catch','return','function','typeof','new','await','async','else','do','try','void','delete','in','of','super','import','case','throw','with','yield'}
calls -= KW

with sync_playwright() as p:
    b = p.chromium.launch(headless=True)
    pg = b.new_page()
    pg.on('dialog', lambda d: d.accept())
    pg.goto('file:///' + PATH.replace('\\', '/'))
    pg.wait_for_timeout(2000)
    res = pg.evaluate("""(names) => names.filter(n => { try { return eval('typeof ' + n) === 'undefined'; } catch(e) { return true; } })""", sorted(calls))
    b.close()

# 메서드/로컬 변수일 수 있는 오탐 줄이기: 선언(const/let/var/파라미터)이 코드에 있으면 제외
really = []
for n in res:
    if re.search(r'(?:const|let|var)\s+' + re.escape(n) + r'\b', code):
        continue
    if re.search(r'[(,]\s*' + re.escape(n) + r'\s*[,)=]', code) and not re.search(r'\b' + re.escape(n) + r'\s*\(', code):
        continue
    cnt = len(re.findall(r'(?<![\w$.])' + re.escape(n) + r'\s*\(', stripped))
    really.append((n, cnt))
really.sort(key=lambda x: -x[1])
print('UNDEFINED CALLED NAMES:', len(really))
for n, c in really:
    print(f'  {n}  (calls: {c})')
json.dump([n for n, _ in really], open(r'g:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\교육학\scratch\undefined_names.json', 'w'))
