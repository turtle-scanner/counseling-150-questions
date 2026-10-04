import re

with open(r'G:\내 드라이브\ANTI GRAVITY\전문상담임용고시\kice-300-wordbook\kice_55_core_compressed.html', 'r', encoding='utf-8') as f:
    text = f.read()

# find occurrences of 55
matches = [m.start() for m in re.finditer(r'\b55\b', text)]
print(f'Total occurrences of "55": {len(matches)}')
for pos in matches:
    print('Context:', text[max(0, pos-40):min(len(text), pos+40)].replace('\n', ' '))
