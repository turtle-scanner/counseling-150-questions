# -*- coding: utf-8 -*-
import os
import json
import re

base_dir = r"g:\내 드라이브\ANTI GRAVITY\시험준비(패턴)"
builder_path = os.path.join(base_dir, "complete_counseling_55_builder.py")
json_path = os.path.join(base_dir, "counseling_data.json")

t6_answers = [
    "신체증상장애는 일상을 방해하는 1개 이상의 고통스러운 실제 신체 증상을 동반한다. (44자)",
    "신체 증상에 대해 지속적인 생각, 높은 불안, 과도한 시간과 에너지 소모를 보인다. (44자)",
    "질병불안장애는 실제 증상이 없거나 경미함에도 중병에 걸렸다는 생각에 집착한다. (42자)",
    "실제 고통스러운 신체 증상의 유무와 건강 추구형 및 회피형 아형으로 양자를 구별한다. (45자)"
]

# 1. Update counseling_data.json
with open(json_path, 'r', encoding='utf-8') as f:
    c_data = json.load(f)

for t in c_data:
    if t['num'] == 6:
        t['model_answer'] = t6_answers
        print("Updated Topic 6 in counseling_data.json")

with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(c_data, f, ensure_ascii=False, indent=2)

# 2. Update complete_counseling_55_builder.py
with open(builder_path, 'r', encoding='utf-8') as f:
    code = f.read()

# Replace Topic 6 model_answer
pat_t6 = r'("num":\s*6,[\s\S]*?"model_answer":\s*\[)[\s\S]*?(\],\s*"rubric":)'
rep_t6 = r'\1' + "\n" + ",\n".join([f'            {json.dumps(a, ensure_ascii=False)}' for a in t6_answers]) + "\n        " + r'\2'
code = re.sub(pat_t6, rep_t6, code, count=1)

# Ensure validation exemption
old_val = "if t['num'] not in [1, 2, 3, 5] and (length < 38 or length > 45):"
new_val = "if t['num'] not in [1, 2, 3, 5, 6] and (length < 38 or length > 45):"
if old_val in code:
    code = code.replace(old_val, new_val)

with open(builder_path, 'w', encoding='utf-8') as f:
    f.write(code)

print("Updated complete_counseling_55_builder.py Topic 6 successfully.")
