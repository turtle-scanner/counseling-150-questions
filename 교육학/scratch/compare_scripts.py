# -*- coding: utf-8 -*-
import os, re

files = [
    r'G:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\교육학\scratch\temp_script.js',
    r'G:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\교육학\scratch\temp_script1.js',
    r'G:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\교육학\scratch\extracted_script_2.js',
]

for f in files:
    if os.path.exists(f):
        txt = open(f, 'r', encoding='utf-8', errors='ignore').read()
        fns = re.findall(r'function\s+([A-Za-z_$][\w$]*)\s*\(', txt)
        print(os.path.basename(f), 'size:', len(txt), 'functions:', len(set(fns)))

cur_html = open(r'C:\Users\LENOVO\Desktop\sam3_update.html', 'r', encoding='utf-8', errors='ignore').read()
cur_fns = set(re.findall(r'function\s+([A-Za-z_$][\w$]*)\s*\(', cur_html))
print('sam3_update.html functions:', len(cur_fns))

for f in files:
    if os.path.exists(f):
        txt = open(f, 'r', encoding='utf-8', errors='ignore').read()
        fns = set(re.findall(r'function\s+([A-Za-z_$][\w$]*)\s*\(', txt))
        diff = sorted(fns - cur_fns)
        print(f'Functions in {os.path.basename(f)} NOT in sam3_update.html ({len(diff)}):', diff)
