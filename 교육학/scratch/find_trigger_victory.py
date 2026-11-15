# -*- coding: utf-8 -*-
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='backslashreplace')

html = open(r'C:\Users\LENOVO\Desktop\sam3_update.html', 'r', encoding='utf-8', errors='ignore').read()

pos = html.find('initHexBattleUnits')
print('End of initHexBattleUnits:')
print(html[pos+8400:pos+9500])

print('\n--- ALL triggerVictory CALLS ---')
for m in re.finditer(r'triggerVictory\s*\(', html):
    p = m.start()
    print('At', p, ':', html[max(0, p-120):min(len(html), p+180)].replace('\n', ' '))
