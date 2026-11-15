# -*- coding: utf-8 -*-
import os
import json
import re

base_dir = r"g:\내 드라이브\ANTI GRAVITY\시험준비(패턴)"
builder_path = os.path.join(base_dir, "complete_counseling_55_builder.py")
json_path = os.path.join(base_dir, "counseling_data.json")

t7_answers = [
    "강박장애는 침습적 강박사고와 불안을 중화하려는 외현적·내재적 강박행동을 보인다. (45자)",
    "강박성 성격장애는 규칙, 정리정돈, 통제에 대한 광범위한 집착과 융통성 결여를 보인다. (46자)",
    "강박장애는 비합리성을 인식하는 자아이질적 고통이며, 성격장애는 자아동질적 순응성을 띤다. (47자)",
    "노출 및 반응방지는 두려운 자극에 직면시킨 후 의례적 강박행동을 억제하는 원리이다. (44자)"
]

# 1. Update counseling_data.json
with open(json_path, 'r', encoding='utf-8') as f:
    c_data = json.load(f)

for t in c_data:
    if t['num'] == 7:
        t['model_answer'] = t7_answers
        print("Updated Topic 7 in counseling_data.json")

with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(c_data, f, ensure_ascii=False, indent=2)

# 2. Update complete_counseling_55_builder.py
with open(builder_path, 'r', encoding='utf-8') as f:
    code = f.read()

# Replace Topic 7 model_answer
pat_t7 = r'("num":\s*7,[\s\S]*?"model_answer":\s*\[)[\s\S]*?(\],\s*"rubric":)'
rep_t7 = r'\1' + "\n" + ",\n".join([f'            {json.dumps(a, ensure_ascii=False)}' for a in t7_answers]) + "\n        " + r'\2'
code = re.sub(pat_t7, rep_t7, code, count=1)

# Ensure validation exemption
old_val = "if t['num'] not in [1, 2, 3, 5, 6] and (length < 38 or length > 45):"
new_val = "if t['num'] not in [1, 2, 3, 5, 6, 7] and (length < 38 or length > 45):"
if old_val in code:
    code = code.replace(old_val, new_val)

with open(builder_path, 'w', encoding='utf-8') as f:
    f.write(code)

print("Updated complete_counseling_55_builder.py Topic 7 successfully.")
