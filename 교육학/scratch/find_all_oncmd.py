import sys

with open(r'C:/Users/LENOVO/Desktop/삼국지_황제의결단_웹게임.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = [m.start() for m in re.finditer(r'onCmdArchery', text)]
print('Matches:', matches)
for m in matches:
    print('Match at', m, text[m-20:m+50])
