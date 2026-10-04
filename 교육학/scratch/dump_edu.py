import json

with open('scratch/all_items_dump.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

with open('scratch/edu_items.txt', 'w', encoding='utf-8') as out:
    for it in items:
        badge = it['badge']
        if any(w in badge for w in ['교육', '교수', '학습', '평가', '행정']):
            out.write(f"[{it['num']}] {it['kw']}\n")
            out.write(f"  Q: {it['q']}\n")
            out.write(f"  ANS: {it['ans']}\n\n")

print("Dumped educational items to scratch/edu_items.txt")
