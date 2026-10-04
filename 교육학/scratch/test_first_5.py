import json

with open('scratch/all_items_dump.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

# Inspect first 5 items
for it in items[:5]:
    print(f"[{it['num']}] {it['kw']}")
    print("  Q:", it['q'])
    print("  ANS:", it['ans'])
    print("-" * 50)
