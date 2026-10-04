import re
import json

with open(r'G:\내 드라이브\ANTI GRAVITY\전문상담임용고시\kice-300-wordbook\kice_55_core_compressed.html', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'const originalItems = (\[.*?\]);', text, re.DOTALL)
if m:
    items = json.loads(m.group(1))
    print(f"Total items: {len(items)}")
    for i in range(5):
        print(f"--- Item {i+1}: {items[i]['kw']} ---")
        print(items[i]['ans'])
