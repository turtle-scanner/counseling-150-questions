import json

with open('scratch_150_pages.json', 'r', encoding='utf-8') as f:
    pages_150 = json.load(f)

items_150 = []
for p in pages_150:
    for it in p['items']:
        items_150.append(it)

with open('scratch/new_203_items_curriculum2022.json', 'r', encoding='utf-8') as f:
    items_203 = json.load(f)

print(f"Total 150: {len(items_150)}, Total 203: {len(items_203)}")

# Build a dictionary of items_150 by question similarity or keyword
# Let's inspect which items in 203 are new
def get_clean_kws(text):
    import re
    return re.sub(r'[\s\(\)\,\.\-➔]+', '', text)

map_150 = {}
for it in items_150:
    map_150[get_clean_kws(it['keywords'][:10])] = it

matched = 0
unmatched = []
for i, it203 in enumerate(items_203):
    k = get_clean_kws(it203['kw'][:10])
    if k in map_150:
        matched += 1
    else:
        unmatched.append((i+1, it203['badge'], it203['kw']))

print(f"Matched with 150: {matched}, Unmatched (new in 203): {len(unmatched)}")
print("\n--- New items in 203 ---")
for num, badge, kw in unmatched:
    print(f"[{num}] ({badge}) {kw}")
