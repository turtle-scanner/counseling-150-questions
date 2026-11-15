# -*- coding: utf-8 -*-
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='backslashreplace')
html = open(r'C:\Users\LENOVO\Desktop\sam3_update.html', 'r', encoding='utf-8', errors='ignore').read()

pos = html.find('id="duelResultBar"')
if pos != -1:
    print(html[pos-100:pos+800])
else:
    print("duelResultBar not found!")

pos2 = html.find('function closeDuelModal')
print('\n=== closeDuelModal ===\n', html[pos2:pos2+800])
