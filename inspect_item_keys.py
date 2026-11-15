# -*- coding: utf-8 -*-
import json
import re

with open('교육학/exam_2027_kice_ab.html', 'r', encoding='utf-8') as f:
    text = f.read()

mA = re.search(r'const examDataA = (\[[\s\S]*?\]);', text)
dataA = json.loads(mA.group(1))

print("Keys in item 0:", list(dataA[0].keys()))
print("Item 0:", dataA[0])
print("\n" + "="*50 + "\n")
print("Keys in item 4 (서술형):", list(dataA[4].keys()))
print("Item 4:", dataA[4])
