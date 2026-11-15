# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')
with open(r'C:\Users\LENOVO\Desktop\삼국지_황제의결단_웹게임.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(1160, 1260):
    if i < len(lines):
        line = lines[i]
        if 'selectIntroRuler' in line or 'card-' in line or 'intro-ruler-card' in line or 'font-black' in line:
            print(f"{i+1}: {line.strip()}")
