import sys
import re

with open(r'C:/Users/LENOVO/Desktop/삼국지_황제의결단_웹게임.html', 'r', encoding='utf-8') as f:
    text = f.read()

matches = [m.start() for m in re.finditer(r'phase\s*=\s*["\']enemy["\']', text)]
print('Matches count:', len(matches))
for m in matches:
    chunk = text[m-100:m+2500]
    sys.stdout.buffer.write(chunk.encode('utf-8'))
    sys.stdout.buffer.write(b'\n' + b'='*50 + b'\n')
