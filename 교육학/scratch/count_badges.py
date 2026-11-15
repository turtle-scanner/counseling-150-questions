import json
from collections import Counter

with open('scratch/new_203_items_curriculum2022.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

badges = Counter(it['badge'] for it in items)
print("Badge counts:")
for b, c in badges.most_common():
    print(f"  {b}: {c}")
