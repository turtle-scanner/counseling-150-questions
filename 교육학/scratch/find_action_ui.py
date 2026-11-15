import sys

with open(r'C:/Users/LENOVO/Desktop/삼국지_황제의결단_웹게임.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = [m.start() for m in re.finditer(r'이달의 전략|actionPoints|executeRest|턴 넘김', text)]
print('Matches count:', len(matches))
for m in matches[:10]:
    sys.stdout.buffer.write(text[m-30:m+150].encode('utf-8') + b'\n---\n')
