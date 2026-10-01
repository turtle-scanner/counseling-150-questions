import json

with open('scratch/items_150_raw.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

# Let's write all 150 items to a file so we can view them completely
with open('scratch/all_items_full.txt', 'w', encoding='utf-8') as f:
    for it in items:
        f.write(f"=== {it['num']:3d} | [{it['badge']}] {it['kw_name']} ===\n")
        f.write(f"Q: {it['question']}\n")
        f.write(f"A: {it['answer']}\n\n")

print("Saved scratch/all_items_full.txt")
