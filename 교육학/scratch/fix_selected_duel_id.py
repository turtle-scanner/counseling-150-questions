# -*- coding: utf-8 -*-
import sys, io, re, shutil, subprocess

target_html_path = r'C:\Users\LENOVO\Desktop\sam3_update.html'
html = open(target_html_path, 'r', encoding='utf-8', errors='ignore').read()

duel_vars_fix = '''
    let selectedDuelMyOfficerId = 1;
    let selectedMyOfficerIdx = 0;
    let selectedEnemyOfficerName = null;
    let selectedEnemyProvId = null;
'''

# Find where startDuelFight or openDuelSelectModal is defined
pos = html.find('function startDuelFight()')
if pos != -1:
    html = html[:pos] + duel_vars_fix + '\n    ' + html[pos:]
    print('Inserted selectedDuelMyOfficerId before startDuelFight')

open(target_html_path, 'w', encoding='utf-8').write(html)

# Copy to all 5 files
targets = [
    r'C:\Users\LENOVO\Desktop\삼국지_황제의결단_웹게임.html',
    r'G:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\index.html',
    r'G:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\samgukji.html',
    r'G:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\교육학\index.html',
    r'G:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\교육학\samgukji.html'
]
for tgt in targets:
    shutil.copy2(target_html_path, tgt)
print('All 6 files updated with selectedDuelMyOfficerId!')
