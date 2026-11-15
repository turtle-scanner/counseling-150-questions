# -*- coding: utf-8 -*-
import json
import re

# 1. Check counseling_data.json
with open('counseling_data.json', 'r', encoding='utf-8') as f:
    cd = json.load(f)

print(f"counseling_data.json has {len(cd)} items")
print("Topic 1 title:", cd[0].get('title'))
print("Topic 2 title:", cd[1].get('title'))

# 2. Check top55_extracted.json
with open('교육학/scratch/top55_extracted.json', 'r', encoding='utf-8') as f:
    top55 = json.load(f)

print(f"top55_extracted.json has {len(top55)} items")
for idx, item in enumerate(top55):
    q = item.get('question', '')
    if '자폐' in q or 'ADHD' in q or '주의력결핍' in q:
        print(f"Top55 [{idx+1}]: {q[:40]}")
