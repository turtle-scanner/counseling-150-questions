# -*- coding: utf-8 -*-
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='backslashreplace')

html = open(r'C:\Users\LENOVO\Desktop\sam3_update.html', 'r', encoding='utf-8', errors='ignore').read()

pos = html.find("'장로': [")
if pos != -1:
    print(html[pos:pos+400])
else:
    print('장로 entry not found')
