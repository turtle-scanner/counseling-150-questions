# -*- coding: utf-8 -*-
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='backslashreplace')
html = open(r'C:\Users\LENOVO\Desktop\sam3_update.html', 'r', encoding='utf-8', errors='ignore').read()

for kw in ['troop-promotion-modal', '천하통일을 향해 진격하라']:
    pos = 0
    while True:
        p = html.find(kw, pos)
        if p == -1: break
        print(f'=== {kw} at {p} ===')
        print(html[max(0, p-150):min(len(html), p+800)])
        pos = p + 1
