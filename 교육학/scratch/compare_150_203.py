import json, os, sys
sys.stdout.reconfigure(encoding='utf-8')

# Load 150 items
with open('scratch_150_pages.json', 'r', encoding='utf-8') as f:
    pages_150 = json.load(f)

items_150 = []
for p in pages_150:
    for it in p['items']:
        items_150.append(it)

# Load 203 items
with open('scratch/new_203_items_curriculum2022.json', 'r', encoding='utf-8') as f:
    items_203 = json.load(f)

print(f"Total 150 items: {len(items_150)}")
print(f"Total 203 items: {len(items_203)}")

# Check matching by keyword or question
# Let's inspect how items_203 answers are written
for i in [0, 16, 50, 152, 170, 200]:
    if i < len(items_203):
        print(f"\nItem 203 #{i+1}: ({items_203[i]['badge']}) {items_203[i]['kw']}")
        print(f"  Ans:\n{items_203[i]['ans']}")
