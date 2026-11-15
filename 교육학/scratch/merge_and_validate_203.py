# -*- coding: utf-8 -*-
import json
import sys
from collections import Counter
sys.stdout.reconfigure(encoding='utf-8')

from rubric_part1 import RUBRIC_PART1
from rubric_part2 import RUBRIC_PART2
from rubric_part3 import RUBRIC_PART3
from rubric_part4 import RUBRIC_PART4

full_rubric = {}
full_rubric.update(RUBRIC_PART1)
full_rubric.update(RUBRIC_PART2)
full_rubric.update(RUBRIC_PART3)
full_rubric.update(RUBRIC_PART4)

print(f"Total items merged: {len(full_rubric)}")
assert len(full_rubric) == 203, f"Expected 203 items, got {len(full_rubric)}"

# Validate global constraints
errors = []
all_lines = []

for num in range(1, 204):
    if num not in full_rubric:
        errors.append(f"Missing item {num}")
        continue
    ans = full_rubric[num]
    lines = [l.strip() for l in ans.split("\n") if l.strip()]
    if len(lines) != 4:
        errors.append(f"Item {num} has {len(lines)} lines (expected 4)")
    for idx, l in enumerate(lines):
        if len(l) < 30 or len(l) > 42:
            errors.append(f"Item {num} line {idx+1} ({len(l)} chars): {l}")
        if "*" in l:
            errors.append(f"Item {num} line {idx+1} has asterisk: {l}")
        all_lines.append((num, idx+1, l))

# Check for cross-item duplicate lines
line_counts = Counter(l for _, _, l in all_lines)
for l, cnt in line_counts.items():
    if cnt > 1:
        items_with_dup = [f"Item {n} L{idx}" for n, idx, text in all_lines if text == l]
        errors.append(f"DUPLICATE LINE across deck ({cnt} times): '{l}' in {', '.join(items_with_dup)}")

if errors:
    print(f"FOUND {len(errors)} ERRORS:")
    for e in errors:
        print("  ", e)
    sys.exit(1)

print("PERFECTION ACHIEVED! All 203 items, all 812 lines satisfy:")
print("  1. Exactly 30~42 characters per line (Rule 11 B4 answer standard).")
print("  2. ZERO duplicate lines across the entire deck (100% unique, item-specific).")
print("  3. ZERO asterisks anywhere.")

# Now load new_203_items_curriculum2022.json and update ans
json_path = 'scratch/new_203_items_curriculum2022.json'
with open(json_path, 'r', encoding='utf-8') as f:
    items = json.load(f)

for it in items:
    num = it['num']
    if num in full_rubric:
        it['ans'] = full_rubric[num]

with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(items, f, ensure_ascii=False, indent=2)

print(f"Updated and saved {json_path}")
