# -*- coding: utf-8 -*-
import sys, io, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='backslashreplace')
t = open(r'C:\Users\LENOVO\Desktop\sam3_update.html', 'r', encoding='utf-8', errors='ignore').read()
lines = t.split('\n')
print('total lines', len(lines))
print('--- around line 2571 ---')
for i in range(2555, 2580):
    print(i+1, lines[i][:160])
print('--- logMessage definitions ---')
for m in re.finditer(r'(function\s+logMessage|logMessage\s*=|window\.logMessage)', t):
    ln = t.count('\n', 0, m.start()) + 1
    print('line', ln, t[m.start():m.start()+80].replace('\n', ' '))
print('--- logMessage usage count ---', t.count('logMessage('))
print('--- other base helpers defined? ---')
for fn in ['playSfx', 'getMyCapital', 'updateRightPanel', 'addTroopExp', 'renderMapPins', 'showToast', 'closeAllPopups']:
    ms = [t.count('\n', 0, m.start()) + 1 for m in re.finditer(r'function\s+' + fn + r'\b', t)]
    print(fn, ms)
