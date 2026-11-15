# -*- coding: utf-8 -*-
import sys, io, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='backslashreplace')
html = open(r'C:\Users\LENOVO\Desktop\sam3_update.html', 'r', encoding='utf-8', errors='ignore').read()

for m in re.finditer(r'</?script[^>]*>', html):
    print(m.start(), m.group(0))

print('--- ALL closeModal definitions ---')
for m in re.finditer(r'function\s+closeModal\s*\([^)]*\)', html):
    print(m.start(), html[m.start():m.start()+250])

print('--- ALL openModal definitions ---')
for m in re.finditer(r'function\s+openModal\s*\([^)]*\)', html):
    print(m.start(), html[m.start():m.start()+250])
