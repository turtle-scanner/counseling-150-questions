import re

with open(r'G:\내 드라이브\ANTI GRAVITY\전문상담임용고시\kice-300-wordbook\kice_d54_phase1_wordbook.html', 'r', encoding='utf-8') as f:
    text1 = f.read()

with open(r'G:\내 드라이브\ANTI GRAVITY\전문상담임용고시\kice-300-wordbook\kice_55_core_compressed.html', 'r', encoding='utf-8') as f:
    text2 = f.read()

print('text1 localStorage keys:')
for m in re.finditer(r'localStorage\.(?:getItem|setItem)\([\'"]([^\'"]+)[\'"]', text1):
    print(' ', m.group(1))

print('text2 localStorage keys:')
for m in re.finditer(r'localStorage\.(?:getItem|setItem)\([\'"]([^\'"]+)[\'"]', text2):
    print(' ', m.group(1))
