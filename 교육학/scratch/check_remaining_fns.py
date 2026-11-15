# -*- coding: utf-8 -*-
import re, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='backslashreplace')

html = open(r'C:\Users\LENOVO\Desktop\sam3_update.html', 'r', encoding='utf-8', errors='ignore').read()
ts = open(r'G:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\교육학\scratch\temp_script.js', 'r', encoding='utf-8', errors='ignore').read()
f_fatigue = open(r'G:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\교육학\scratch\apply_duel_random_and_fatigue.js', 'r', encoding='utf-8', errors='ignore').read()

for kw in ['TroopExp', 'HexBattle', 'HexAction', 'MainDisplay', 'RemoteAction', 'EnemyAttack', 'NextEnemy', 'EnemyOfficersWithFatigue']:
    print(f'=== {kw} ===')
    for m in re.finditer(r'function\s+\w*' + kw + r'\w*\s*\([^)]*\)', html):
        print('  in html:', m.group(0))
    for m in re.finditer(r'function\s+\w*' + kw + r'\w*\s*\([^)]*\)', ts):
        print('  in temp_script:', m.group(0))
    for m in re.finditer(r'function\s+\w*' + kw + r'\w*\s*\([^)]*\)', f_fatigue):
        print('  in fatigue_js:', m.group(0))
