# -*- coding: utf-8 -*-
import sys, io, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='backslashreplace')

html = open(r'C:\Users\LENOVO\Desktop\sam3_update.html', 'r', encoding='utf-8', errors='ignore').read()

pos = html.find('function initHexBattleUnits')
if pos == -1: pos = html.find('initHexBattleUnits')
print('=== initHexBattleUnits ===')
print(html[pos:pos+2500])

pos2 = html.find('function openHexBattle')
print('\n=== openHexBattle ===\n', html[pos2:pos2+2000])
