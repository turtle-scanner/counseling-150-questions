# -*- coding: utf-8 -*-
import sys, io, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='backslashreplace')
html = open(r'C:\Users\LENOVO\Desktop\sam3_update.html', 'r', encoding='utf-8', errors='ignore').read()

for fn in ['openWarModal', 'confirmOfficerDeployment', 'openHexBattle', 'openOfficerDeployModal']:
    print(f'=== ALL DEFINITIONS OF {fn} ===')
    for m in re.finditer(r'function\s+' + fn + r'\s*\([^)]*\)', html):
        pos = m.start()
        print(f'At {pos}:')
        print(html[pos:pos+750])
        print('-'*40)
