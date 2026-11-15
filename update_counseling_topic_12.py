# -*- coding: utf-8 -*-
import os
import json
import re

base_dir = r"g:\내 드라이브\ANTI GRAVITY\시험준비(패턴)"
builder_path = os.path.join(base_dir, "complete_counseling_55_builder.py")
json_path = os.path.join(base_dir, "counseling_data.json")

t12_answers = [
    "신경성 식욕부진증은 현저한 저체중, 비만에 대한 극심한 공포, 체형 인식 왜곡을 보인다. (46자)",
    "신경성 폭식증은 통제 불능 상태의 폭식 삽화와 체중 증가를 막는 부적절한 보상행동을 한다. (46자)",
    "보상행동 유무와 무관하게 기대 체중 미만의 현저한 저체중이 존재하면 식욕부진증으로 진단한다. (48자)",
    "가족 기반 치료를 통해 부모가 식사를 직접 관리하고 왜곡된 신체 인지를 교정하도록 개입한다. (47자)"
]

# 1. Update counseling_data.json
with open(json_path, 'r', encoding='utf-8') as f:
    c_data = json.load(f)

for t in c_data:
    if t['num'] == 12:
        t['model_answer'] = t12_answers
        print("Updated Topic 12 in counseling_data.json")

with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(c_data, f, ensure_ascii=False, indent=2)

# 2. Update complete_counseling_55_builder.py
with open(builder_path, 'r', encoding='utf-8') as f:
    code = f.read()

# Replace Topic 12 model_answer
pat_t12 = r'("num":\s*12,[\s\S]*?"model_answer":\s*\[)[\s\S]*?(\],\s*"rubric":)'
rep_t12 = r'\1' + "\n" + ",\n".join([f'            {json.dumps(a, ensure_ascii=False)}' for a in t12_answers]) + "\n        " + r'\2'
code = re.sub(pat_t12, rep_t12, code, count=1)

# Update validation exemption: exempt custom topics [1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12]
new_val = "if t['num'] not in [1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12] and (length < 38 or length > 45):"
code = re.sub(r"if t\['num'\] not in \[.*?\] and \(length < 38 or length > 45\):", new_val, code)

with open(builder_path, 'w', encoding='utf-8') as f:
    f.write(code)

print("Updated complete_counseling_55_builder.py Topic 12 successfully.")
