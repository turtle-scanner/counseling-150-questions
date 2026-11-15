import sys
sys.stdout.reconfigure(encoding='utf-8')

path = 'G:/내 드라이브/ANTI GRAVITY/전문상담임용고시/kice-300-wordbook/kice_150_core_table_a4.html'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

print('Length:', len(text))
print('page-sheet count:', text.count('class="page-sheet"'))
print('td-num count:', text.count('class="td-num"'))
import re
titles = re.findall(r'<div class="page-sub-title">(.*?)</div>', text)
for i, t in enumerate(titles, 1):
    print(f'Page {i}: {t}')
