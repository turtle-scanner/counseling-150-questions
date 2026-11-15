# -*- coding: utf-8 -*-
import sys, io, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='backslashreplace')

html = open(r'C:\Users\LENOVO\Desktop\sam3_update.html', 'r', encoding='utf-8', errors='ignore').read()

print('=== 1. 침공작전 개시 / openWarModal / renderWarTargetList ===')
for kw in ['침공작전 개시', 'function openWarModal', 'function openWarTargetSelectModal', 'function executeAlliance']:
    pos = html.find(kw)
    print(f'--- {kw} at {pos} ---')
    if pos != -1:
        print(html[max(0, pos-100):min(len(html), pos+900)])
