import re

with open(r'G:\내 드라이브\ANTI GRAVITY\전문상담임용고시\kice-300-wordbook\kice_55_core_compressed.html', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'let items = (\[[\s\S]*?\]);\s*// Load custom items', text)
if m:
    print('Found items array in kice_55_core_compressed.html!')
    print('Length of items block:', len(m.group(1)))
else:
    print('items array regex not matched')
