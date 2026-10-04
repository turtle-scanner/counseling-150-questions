import sys
import json
import re

sys.stdout.reconfigure(encoding='utf-8')

with open(r'G:\내 드라이브\ANTI GRAVITY\전문상담임용고시\kice-300-wordbook\kice_55_core_compressed.html', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'items\s*=\s*(\[.*?\]);', text)
if m:
    items = json.loads(m.group(1))
    badges = set(it.get('badge', '') for it in items)
    print("Distinct badges:", badges)
    badge_counts = {}
    for it in items:
        b = it.get('badge', '')
        badge_counts[b] = badge_counts.get(b, 0) + 1
    print("Badge counts:", badge_counts)
else:
    print("Regex did not match items array")
