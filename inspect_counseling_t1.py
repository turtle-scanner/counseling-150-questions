# -*- coding: utf-8 -*-
import json

with open('counseling_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print(f"Total topics in counseling_data.json: {len(data)}")
t1 = data[0]
with open('counseling_t1.txt', 'w', encoding='utf-8') as out:
    json.dump(t1, out, ensure_ascii=False, indent=2)

print("Wrote counseling_t1.txt")
