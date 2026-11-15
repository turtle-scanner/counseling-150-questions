import json, re

path = 'G:/내 드라이브/ANTI GRAVITY/전문상담임용고시/kice-300-wordbook/kice_150_core_table_a4.html'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

print('Length:', len(text))
print('page-sheet count:', text.count('page-sheet'))
print('td-num count:', text.count('td-num'))
for i, t in enumerate(re.findall(r'<div class="page-sub-title">(.*?)</div>', text), 1):
    print(f'Page {i}: {t}')
