import json
import re

# 1. Read 200 items from kice_150_core_table_a4.html
with open(r'G:\내 드라이브\ANTI GRAVITY\전문상담임용고시\kice-300-wordbook\kice_150_core_table_a4.html', 'r', encoding='utf-8') as f:
    text_150 = f.read()

start = text_150.find('DATA = [') + len('DATA = ')
end = text_150.find('];', start) + 1
items_200 = json.loads(text_150[start:end])
print(f'Loaded {len(items_200)} items from 150/200 dataset.')

# 2. Read target kice_55_core_compressed.html
target_path = r'G:\내 드라이브\ANTI GRAVITY\전문상담임용고시\kice-300-wordbook\kice_55_core_compressed.html'
with open(target_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace items array
items_json_str = json.dumps(items_200, ensure_ascii=False)
new_items_decl = f'let items = {items_json_str};\n      // Load custom items'

html = re.sub(r'let items = \[[\s\S]*?\];\s*// Load custom items', new_items_decl, html)

# Update title
html = html.replace('2027 KICE 초압축 55선', '2027 KICE 핵심 단어장 (200선)')
html = html.replace('1 / 55', f'1 / {len(items_200)}')

# Update any comments or text referencing 55
html = html.replace('총 55개', f'총 {len(items_200)}개')

with open(target_path, 'w', encoding='utf-8') as f:
    f.write(html)

print(f'Successfully updated kice_55_core_compressed.html with {len(items_200)} items!')
