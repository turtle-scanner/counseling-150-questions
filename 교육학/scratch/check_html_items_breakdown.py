import sys
import re
import json

sys.stdout.reconfigure(encoding='utf-8')

with open(r'G:\내 드라이브\ANTI GRAVITY\전문상담임용고시\kice-300-wordbook\kice_55_core_compressed.html', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'items\s*=\s*(\[.*?\]);', text)
items = json.loads(m.group(1))

print(f"Total items in html: {len(items)}")

# Check badges
from collections import Counter
counts = Counter(it.get('badge', '') for it in items)
for b, c in counts.most_common():
    print(f"  {b}: {c}")
