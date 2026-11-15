# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')
with open(r'C:\Users\LENOVO\Desktop\삼국지_황제의결단_웹게임.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(1250, 1310):
    if i < len(lines):
        print(f"{i+1}: {lines[i]}", end="")
