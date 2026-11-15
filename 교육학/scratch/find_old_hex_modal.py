import sys

with open(r'C:/Users/LENOVO/Desktop/삼국지_황제의결단_웹게임.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = [m.start() for m in re.finditer(r'10턴 결전: 적 군량고 습격', text)]
print('Matches:', matches)
for m in matches:
    print('Match at:', m)
    sys.stdout.buffer.write(text[m-200:m+400].encode('utf-8') + b'\n---\n')
