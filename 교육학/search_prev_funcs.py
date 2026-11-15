# -*- coding: utf-8 -*-
import os, glob

search_files = [
    r'G:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\samgukji.html',
    r'G:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\교육학\samgukji.html',
    r'G:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\교육학\samgukji5.html'
]
search_files.extend(glob.glob(r'G:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\교육학\scratch\*.js'))
search_files.extend(glob.glob(r'G:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\교육학\scratch\*.html'))

target_funcs = ['executeTraining', 'openReorganizeModal', 'openDuelSelectModal', 'executeSearchOfficer', 'executeLandDev']

found_map = {}
for sf in search_files:
    if not os.path.exists(sf): continue
    try:
        with open(sf, 'r', encoding='utf-8', errors='ignore') as f:
            c = f.read()
        for tf in target_funcs:
            if f'function {tf}' in c or f'{tf} =' in c:
                if tf not in found_map: found_map[tf] = []
                found_map[tf].append(sf)
    except Exception as e:
        pass

for tf in target_funcs:
    print(f"{tf}: found in {found_map.get(tf, 'NONE')}")
