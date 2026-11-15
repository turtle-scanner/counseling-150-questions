import sys
import re

with open(r'C:/Users/LENOVO/Desktop/삼국지_황제의결단_웹게임.html', 'r', encoding='utf-8') as f:
    text = f.read()

matches = [m.start() for m in re.finditer(r'checkUnification', text)]
print('checkUnification calls count:', len(matches))
for m in matches:
    print('Call at:', m)
    sys.stdout.buffer.write(text[m-50:m+150].encode('utf-8') + b'\n---\n')
