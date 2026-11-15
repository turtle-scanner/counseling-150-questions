# -*- coding: utf-8 -*-
import re

with open('build_pedagogy_16_html.js', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'(num:\s*10,[\s\S]*?rubric:[\s\S]*?\])', text)
if m:
    with open('t10_dump.txt', 'w', encoding='utf-8') as out:
        out.write(m.group(0))
    print("Found and wrote t10_dump.txt")
else:
    print("Not found")
