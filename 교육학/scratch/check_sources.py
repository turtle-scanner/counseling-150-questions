import json, re, sys, os
sys.stdout.reconfigure(encoding='utf-8')

# Let's inspect all available data sources
with open('scratch_150_pages.json', 'r', encoding='utf-8') as f:
    pages_150 = json.load(f)

items_150 = []
for p in pages_150:
    for it in p['items']:
        items_150.append(it)

with open('scratch/new_203_items_curriculum2022.json', 'r', encoding='utf-8') as f:
    items_203 = json.load(f)

print(f"Loaded 150 items: {len(items_150)}, 203 items: {len(items_203)}")
