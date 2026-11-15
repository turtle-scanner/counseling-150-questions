import sys
import re

with open(r'C:/Users/LENOVO/Desktop/삼국지_황제의결단_웹게임.html', 'r', encoding='utf-8') as f:
    text = f.read()

matches = [m.start() for m in re.finditer(r'천하통일|ending|unification|즉위식', text, re.IGNORECASE)]
print('Matches count:', len(matches))
for m in matches[:8]:
    sys.stdout.buffer.write(text[m-50:m+200].encode('utf-8') + b'\n---\n')
