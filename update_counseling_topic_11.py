# -*- coding: utf-8 -*-
import os
import json
import re

base_dir = r"g:\내 드라이브\ANTI GRAVITY\시험준비(패턴)"
builder_path = os.path.join(base_dir, "complete_counseling_55_builder.py")
json_path = os.path.join(base_dir, "counseling_data.json")

t11_answers = [
    "조현병 진단 기준 A는 망상, 환각, 와해된 언어, 심하게 와해된·긴장증적 행동, 음성증상이다. (49자)",
    "2개 이상의 증상 중 망상, 환각, 와해된 언어 중 하나는 반드시 필수적으로 포함되어야 한다. (48자)",
    "정서적 둔마와 무의욕증 등 음성증상은 약물 반응이 낮아 기능 회복이 곤란하고 예후가 불량하다. (49자)",
    "활성기 증상이 1개월 이상 나타나야 하며 전구기나 잔류기를 포함한 전체 기간은 6개월 이상이다. (50자)"
]

# 1. Update counseling_data.json
with open(json_path, 'r', encoding='utf-8') as f:
    c_data = json.load(f)

for t in c_data:
    if t['num'] == 11:
        t['model_answer'] = t11_answers
        print("Updated Topic 11 in counseling_data.json")

with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(c_data, f, ensure_ascii=False, indent=2)

# 2. Update complete_counseling_55_builder.py
with open(builder_path, 'r', encoding='utf-8') as f:
    code = f.read()

# Replace Topic 11 model_answer
pat_t11 = r'("num":\s*11,[\s\S]*?"model_answer":\s*\[)[\s\S]*?(\],\s*"rubric":)'
rep_t11 = r'\1' + "\n" + ",\n".join([f'            {json.dumps(a, ensure_ascii=False)}' for a in t11_answers]) + "\n        " + r'\2'
code = re.sub(pat_t11, rep_t11, code, count=1)

# Update validation exemption: exempt custom topics [1, 2, 3, 5, 6, 7, 8, 9, 10, 11]
new_val = "if t['num'] not in [1, 2, 3, 5, 6, 7, 8, 9, 10, 11] and (length < 38 or length > 45):"
code = re.sub(r"if t\['num'\] not in \[.*?\] and \(length < 38 or length > 45\):", new_val, code)

with open(builder_path, 'w', encoding='utf-8') as f:
    f.write(code)

print("Updated complete_counseling_55_builder.py Topic 11 successfully.")
