# -*- coding: utf-8 -*-
with open('build_master.js', 'r', encoding='utf-8') as f:
    text = f.read()

body_start = text.find('<body')
with open('body_dump.txt', 'w', encoding='utf-8') as out:
    if body_start != -1:
        out.write(text[body_start:body_start+3000])
    else:
        out.write("<body not found")

print("Wrote body_dump.txt")
