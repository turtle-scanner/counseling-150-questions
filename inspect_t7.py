# -*- coding: utf-8 -*-
import json
import re

with open(r'g:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\build_pedagogy_16_html.js', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'(num:\s*7,[\s\S]*?rubric:)', text)
if m:
    with open('t7_dump.txt', 'w', encoding='utf-8') as out:
        out.write(m.group(0))
    print("Found and wrote t7_dump.txt")
else:
    print("Not found")
