import json

with open('scratch_150_pages.json', 'r', encoding='utf-8') as f:
    pages = json.load(f)

print("Number of pages:", len(pages))
all_items = []
for p in pages:
    for item in p['items']:
        all_items.append(item)

print("Total items:", len(all_items))
with open('scratch/sample_items.json', 'w', encoding='utf-8') as f:
    json.dump(all_items[:3], f, ensure_ascii=False, indent=2)

print("Saved sample items.")
