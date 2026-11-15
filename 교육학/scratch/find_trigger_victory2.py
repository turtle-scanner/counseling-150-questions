# -*- coding: utf-8 -*-
import sys, io, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='backslashreplace')

html = open(r'C:\Users\LENOVO\Desktop\sam3_update.html', 'r', encoding='utf-8', errors='ignore').read()

print('--- ALL triggerVictory CALLS ---')
for m in re.finditer(r'triggerVictory\s*\(', html):
    p = m.start()
    print('At', p, ':', html[max(0, p-120):min(len(html), p+180)].replace('\n', ' '))
