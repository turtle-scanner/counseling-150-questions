# -*- coding: utf-8 -*-
import os
import json
import re

base_dir = r"g:\내 드라이브\ANTI GRAVITY\시험준비(패턴)"
builder_path = os.path.join(base_dir, "complete_counseling_55_builder.py")
json_path = os.path.join(base_dir, "counseling_data.json")

t19_answers = [
    "전체 반응과 인간운동 반응의 비율은 인지적 포부와 이를 뒷받침하는 지적 자원의 균형이다. (49자)",
    "조직화 점수는 복잡한 자극들의 관계를 유의미하게 통합·구조화하려는 인지적 동기를 뜻한다. (47자)",
    "전통적 형태질 점수는 외부 현실을 관습적·규범적 형태로 왜곡 없이 지각하는 능력을 잰다. (46자)",
    "형태질 저하와 왜곡 형태 급증 시 망상 등 사고장애와 현실검증력 손상을 감별 평가한다. (45자)"
]

# 1. Update counseling_data.json
with open(json_path, 'r', encoding='utf-8') as f:
    c_data = json.load(f)

for t in c_data:
    if t['num'] == 19:
        t['model_answer'] = t19_answers
        print("Updated Topic 19 in counseling_data.json")

with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(c_data, f, ensure_ascii=False, indent=2)

# 2. Update complete_counseling_55_builder.py
with open(builder_path, 'r', encoding='utf-8') as f:
    code = f.read()

# Replace Topic 19 model_answer
pat_t19 = r'("num":\s*19,[\s\S]*?"model_answer":\s*\[)[\s\S]*?(\],\s*"rubric":)'
rep_t19 = r'\1' + "\n" + ",\n".join([f'            {json.dumps(a, ensure_ascii=False)}' for a in t19_answers]) + "\n        " + r'\2'
code = re.sub(pat_t19, rep_t19, code, count=1)

# Update validation exemption: exempt custom topics up to 19
new_val = "if t['num'] not in [1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19] and (length < 38 or length > 45):"
code = re.sub(r"if t\['num'\] not in \[.*?\] and \(length < 38 or length > 45\):", new_val, code)

with open(builder_path, 'w', encoding='utf-8') as f:
    f.write(code)

print("Updated complete_counseling_55_builder.py Topic 19 successfully.")
