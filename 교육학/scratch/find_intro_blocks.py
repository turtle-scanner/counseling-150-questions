# -*- coding: utf-8 -*-
with open(r'C:\Users\LENOVO\Desktop\삼국지_황제의결단_웹게임.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if 'intro-modal' in l or 'scenario' in l or 'intro-ruler-grid' in l:
        print(f'{i+1}: {l.strip()[:90]}')
