import json
import re

with open('scratch/items_150_raw.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

print("Items with English in kw_name:")
for it in items:
    # find English strings
    eng = re.findall(r'[A-Za-z]+(?:\s+[A-Za-z]+)*', it['kw_name'])
    if eng:
        print(f"{it['num']:3d} | {it['kw_name']} --> Eng: {eng}")
