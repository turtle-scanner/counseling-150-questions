import sys

with open(r'C:/Users/LENOVO/Desktop/삼국지_황제의결단_웹게임.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
scripts = list(re.finditer(r'<script[\s\S]*?>([\s\S]*?)</script>', text, re.IGNORECASE))
print(f"Total scripts: {len(scripts)}")

# Script 1에 대해 node로 구문 검사
s1 = scripts[1].group(1)
with open('scratch/temp_script1.js', 'w', encoding='utf-8') as f:
    f.write(s1)

print("Saved scratch/temp_script1.js")
