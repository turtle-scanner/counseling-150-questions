# -*- coding: utf-8 -*-
import sys, io, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='backslashreplace')
html = open(r'C:\Users\LENOVO\Desktop\sam3_update.html', 'r', encoding='utf-8', errors='ignore').read()

for kw in ['gainTroopExp', 'addTroopExp', 'troop-promotion-modal', 'promo-title']:
    print(f'=== {kw} ===')
    for m in re.finditer(re.escape(kw), html):
        p = m.start()
        print(f'At {p}:', html[max(0, p-120):min(len(html), p+220)].replace('\n', ' '))
