# -*- coding: utf-8 -*-
import sys, io, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='backslashreplace')

html = open(r'C:\Users\LENOVO\Desktop\sam3_update.html', 'r', encoding='utf-8', errors='ignore').read()

print('--- SEARCH FOR alert( with 대승리 ---')
for m in re.finditer(r'alert\([^)]*대승리[^)]*\)', html):
    p = m.start()
    print('At', p, ':', html[p:p+300].replace('\n', ' '))

print('\n--- ALL alert( inside triggerVictory ---')
pos = html.find('function triggerVictory')
print(html[pos:pos+1500])
