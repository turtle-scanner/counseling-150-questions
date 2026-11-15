# -*- coding: utf-8 -*-
with open(r'C:\Users\LENOVO\Desktop\삼국지_황제의결단_웹게임.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if 'executeDirectAttack' in l:
        print(f"executeDirectAttack found at line {i+1}")
        for j in range(i, min(len(lines), i + 50)):
            print(f"{j+1}: {repr(lines[j])}")
        break
