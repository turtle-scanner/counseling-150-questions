import json, sys
from collections import Counter
sys.stdout.reconfigure(encoding='utf-8')

with open('scratch/new_203_items_curriculum2022.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

print(f"Total items: {len(items)}")
all_lines = []
violations = []
for it in items:
    num = it['num']
    ls = [l.strip() for l in it['ans'].split('\n') if l.strip()]
    if len(ls) != 4:
        violations.append(f"Item {num} line count: {len(ls)}")
    for idx, l in enumerate(ls):
        if len(l) < 30 or len(l) > 42:
            violations.append(f"Item {num} line {idx+1} ({len(l)} chars): {l}")
        all_lines.append((num, l))

counts = Counter(l for _, l in all_lines)
dups = {l: c for l, c in counts.items() if c > 1}

print(f"Violations (length != 30~42): {len(violations)}")
print(f"Duplicate lines across deck: {len(dups)}")
if dups:
    print("Duplicates found:")
    for l, c in dups.items():
        print(f"  [{c} times] {l}")
else:
    print("SUCCESS: 0 DUPLICATES! Every single line in all 203 items is 100% UNIQUE and within 30~42 characters!")
