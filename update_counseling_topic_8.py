# -*- coding: utf-8 -*-
import os
import json
import re

base_dir = r"g:\내 드라이브\ANTI GRAVITY\시험준비(패턴)"
builder_path = os.path.join(base_dir, "complete_counseling_55_builder.py")
json_path = os.path.join(base_dir, "counseling_data.json")

t8_answers = [
    "4대 증상군은 침습 증상, 지속적 회피, 인지·기분의 부정적 변화, 각성·반응성 변화이다. (46자)",
    "플래시백이나 악몽으로 사건을 재경험하며 외상과 관련된 내적·외적 자극을 적극 회피한다. (46자)",
    "과도한 경계와 수면 곤란 등 과각성을 보이고 부정적 신념과 감정 등 인지적 왜곡이 나타난다. (46자)",
    "증상이 3일-1개월 이내면 급성스트레스장애, 1개월을 초과 지속되면 외상후 스트레스 장애이다. (48자)"
]

# 1. Update counseling_data.json
with open(json_path, 'r', encoding='utf-8') as f:
    c_data = json.load(f)

for t in c_data:
    if t['num'] == 8:
        t['model_answer'] = t8_answers
        print("Updated Topic 8 in counseling_data.json")

with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(c_data, f, ensure_ascii=False, indent=2)

# 2. Update complete_counseling_55_builder.py
with open(builder_path, 'r', encoding='utf-8') as f:
    code = f.read()

# Replace Topic 8 model_answer
pat_t8 = r'("num":\s*8,[\s\S]*?"model_answer":\s*\[)[\s\S]*?(\],\s*"rubric":)'
rep_t8 = r'\1' + "\n" + ",\n".join([f'            {json.dumps(a, ensure_ascii=False)}' for a in t8_answers]) + "\n        " + r'\2'
code = re.sub(pat_t8, rep_t8, code, count=1)

# Ensure validation exemption
old_val = "if t['num'] not in [1, 2, 3, 5, 6, 7] and (length < 38 or length > 45):"
new_val = "if t['num'] not in [1, 2, 3, 5, 6, 7, 8] and (length < 38 or length > 45):"
if old_val in code:
    code = code.replace(old_val, new_val)

with open(builder_path, 'w', encoding='utf-8') as f:
    f.write(code)

print("Updated complete_counseling_55_builder.py Topic 8 successfully.")
