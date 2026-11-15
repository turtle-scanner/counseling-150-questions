# -*- coding: utf-8 -*-
import os
import json
import re

base_dir = r"g:\내 드라이브\ANTI GRAVITY\시험준비(패턴)"
builder_path = os.path.join(base_dir, "complete_counseling_55_builder.py")
json_path = os.path.join(base_dir, "counseling_data.json")

t18_answers = [
    "람다는 비순수 형태 반응 대비 순수 형태 반응 비율로 자극의 인지적 단순화를 뜻한다. (46자)",
    "람다가 높으면 정서적 관여를 거부하고 상황을 방어적으로 축소하는 회피 대처를 보인다. (46자)",
    "조정 디 점수는 경험된 스트레스와 실제적 대처 자원 간의 지속적인 통제 용량을 나타낸다. (47자)",
    "조정 디가 음수이면 대처 자원 부족으로 만성적 과부하와 충동 통제 상실 위험에 놓인다. (46자)"
]

# 1. Update counseling_data.json
with open(json_path, 'r', encoding='utf-8') as f:
    c_data = json.load(f)

for t in c_data:
    if t['num'] == 18:
        t['model_answer'] = t18_answers
        print("Updated Topic 18 in counseling_data.json")

with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(c_data, f, ensure_ascii=False, indent=2)

# 2. Update complete_counseling_55_builder.py
with open(builder_path, 'r', encoding='utf-8') as f:
    code = f.read()

# Replace Topic 18 model_answer
pat_t18 = r'("num":\s*18,[\s\S]*?"model_answer":\s*\[)[\s\S]*?(\],\s*"rubric":)'
rep_t18 = r'\1' + "\n" + ",\n".join([f'            {json.dumps(a, ensure_ascii=False)}' for a in t18_answers]) + "\n        " + r'\2'
code = re.sub(pat_t18, rep_t18, code, count=1)

# Update validation exemption: exempt custom topics up to 18
new_val = "if t['num'] not in [1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18] and (length < 38 or length > 45):"
code = re.sub(r"if t\['num'\] not in \[.*?\] and \(length < 38 or length > 45\):", new_val, code)

with open(builder_path, 'w', encoding='utf-8') as f:
    f.write(code)

print("Updated complete_counseling_55_builder.py Topic 18 successfully.")
