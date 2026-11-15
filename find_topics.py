# -*- coding: utf-8 -*-
import re
import json

with open('build_pedagogy_16_html.js', 'r', encoding='utf-8') as f:
    text = f.read()

matches = re.findall(r'num:\s*(\d+),[\s\S]*?title:\s*"([^"]+)"', text)
with open('topics_list.txt', 'w', encoding='utf-8') as out:
    for num, title in matches:
        out.write(f"{num}: {title}\n")

print("Wrote topics_list.txt")
