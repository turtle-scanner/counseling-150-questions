import json

with open('scratch/new_203_items_curriculum2022.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

with open('scratch/all_203_kws.tsv', 'w', encoding='utf-8') as f:
    for it in items:
        f.write(f"{it['num']}\t{it['badge']}\t{it['kw']}\n")

print(f"Dumped {len(items)} items to scratch/all_203_kws.tsv")
