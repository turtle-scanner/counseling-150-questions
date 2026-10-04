import json

with open('scratch/all_items_dump.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

with open('scratch/keywords_list.txt', 'w', encoding='utf-8') as out:
    for it in items:
        out.write(f"{it['num']:3d} | [{it['badge']}] {it['kw']}\n")

print(f"Exported {len(items)} keywords to scratch/keywords_list.txt")
