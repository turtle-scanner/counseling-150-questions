# -*- coding: utf-8 -*-
import sys, io, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='backslashreplace')
html = open(r'C:\Users\LENOVO\Desktop\sam3_update.html', 'r', encoding='utf-8', errors='ignore').read()

print('ALL duel modal containers:')
for m in re.finditer(r'<div[^>]*id=["\'](duel[a-zA-Z0-9_\-]*)["\']', html):
    pos = m.start()
    print('ID:', m.group(1), 'at', pos, ':', html[pos:pos+200].replace('\n', ' '))
