import json, sys

with open('scratch/new_203_items_curriculum2022.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

with open('scratch/inspect_203_detailed.txt', 'w', encoding='utf-8') as out:
    for i, it in enumerate(data):
        out.write(f"[{i+1}] ({it.get('badge')}) {it.get('kw')}\n")
        out.write(f"  Q: {it.get('q')}\n")
        out.write(f"  A: {it.get('ans')}\n\n")

print(f"Written {len(data)} items to inspect_203_detailed.txt")
