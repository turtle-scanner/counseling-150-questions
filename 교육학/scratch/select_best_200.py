import json, re

# Load 203 items
with open('scratch/new_203_items_curriculum2022.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

print(f"Total source items: {len(items)}")

# We need exactly 200 items. Let's see if there are 3 items that can be pruned or if we select the best 200.
# Let's inspect all items and their badges.
# In the 203 list:
# Items 1-16: 교육과정 (16)
# Items 17-151: 전공상담 (135)
# Items 152-166: 교육학 (교육행정 7, 교육평가 3, 교수학습 4, 교육심리 1) -> 15 items
# Items 167-201: 전공상담 (35)
# Items 202-203: 교육방법 1, 교육심리 1 -> 2 items

# Total 교육학 items = 16 + 15 + 2 = 33 items.
# Total 전공상담 items = 135 + 35 = 170 items.
# 33 + 170 = 203 items.

# If we make 교육학 exactly 30 items (or 32 items) and 전공상담 170 (or 168 items), total is exactly 200 items!
# Let's see which 3 items might be redundant or lower frequency.
