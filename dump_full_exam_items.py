# -*- coding: utf-8 -*-
import json
import re

with open('교육학/exam_2027_kice_ab.html', 'r', encoding='utf-8') as f:
    text = f.read()

mA = re.search(r'const examDataA = (\[[\s\S]*?\]);', text)
mB = re.search(r'const examDataB = (\[[\s\S]*?\]);', text)

dataA = json.loads(mA.group(1))
dataB = json.loads(mB.group(1))

with open('full_exam_dump.json', 'w', encoding='utf-8') as f:
    json.dump({'questions_a': dataA, 'questions_b': dataB}, f, ensure_ascii=False, indent=2)

print("Dumped full_exam_dump.json successfully.")
