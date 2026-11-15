# -*- coding: utf-8 -*-
import sys, io, re, shutil, subprocess

target_html_path = r'C:\Users\LENOVO\Desktop\sam3_update.html'
html = open(target_html_path, 'r', encoding='utf-8', errors='ignore').read()

# Replace any repeated let declarations with window. properties or var
html = re.sub(r'let\s+selectedMyOfficerIdx\s*=\s*0;', 'var selectedMyOfficerIdx = 0;', html)
html = re.sub(r'let\s+selectedDuelMyOfficerId\s*=\s*1;', 'var selectedDuelMyOfficerId = 1;', html)
html = re.sub(r'let\s+selectedEnemyOfficerName\s*=\s*null;', 'var selectedEnemyOfficerName = null;', html)
html = re.sub(r'let\s+selectedEnemyProvId\s*=\s*null;', 'var selectedEnemyProvId = null;', html)

open(target_html_path, 'w', encoding='utf-8').write(html)

scripts = re.findall(r'<script(?:\s+[^>]*)?>(.*?)</script>', html, re.DOTALL)
has_err = False
for idx, sc in enumerate(scripts):
    tmp = f'temp_curr_{idx}.js'
    open(tmp, 'w', encoding='utf-8').write(sc)
    r = subprocess.run(['node', '--check', tmp], capture_output=True)
    if r.returncode != 0:
        has_err = True
        print(f'Error in script {idx}:', r.stderr.decode('utf-8', errors='replace')[:400])
    else:
        print(f'Script {idx} is Valid JS! Length: {len(sc)}')

if not has_err:
    targets = [
        r'C:\Users\LENOVO\Desktop\삼국지_황제의결단_웹게임.html',
        r'G:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\index.html',
        r'G:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\samgukji.html',
        r'G:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\교육학\index.html',
        r'G:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\교육학\samgukji.html'
    ]
    for tgt in targets:
        shutil.copy2(target_html_path, tgt)
    print('All 6 files updated and 100% Valid JS!')
