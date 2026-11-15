# -*- coding: utf-8 -*-
import os
import json
import re

base_dir = r"g:\내 드라이브\ANTI GRAVITY\시험준비(패턴)"
builder_path = os.path.join(base_dir, "complete_counseling_55_builder.py")
json_path = os.path.join(base_dir, "counseling_data.json")

t5_answers = [
    "공황장애는 경미한 신체 감각을 파국적으로 오해석하여 불안이 증폭되는 악순환을 겪는다. (47자)",
    "광장공포증은 대중교통 이용, 열린 공간, 밀폐된 공간 중 2가지 이상에서 극심한 공포를 느낀다. (48자)",
    "공황장애는 발작 자체를 두려워하나, 광장공포증은 탈출 곤란 및 도움 불가 상황을 두려워한다. (47자)",
    "의도적 과호흡 등 내부감각 노출을 실시하여 신체 감각이 위험하지 않다는 신념 수정을 돕는다. (47자)"
]

# 1. Update counseling_data.json
with open(json_path, 'r', encoding='utf-8') as f:
    c_data = json.load(f)

for t in c_data:
    if t['num'] == 5:
        t['model_answer'] = t5_answers
        print("Updated Topic 5 in counseling_data.json")

with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(c_data, f, ensure_ascii=False, indent=2)

# 2. Update complete_counseling_55_builder.py
with open(builder_path, 'r', encoding='utf-8') as f:
    code = f.read()

# Replace Topic 5 model_answer
pat_t5 = r'("num":\s*5,[\s\S]*?"model_answer":\s*\[)[\s\S]*?(\],\s*"rubric":)'
rep_t5 = r'\1' + "\n" + ",\n".join([f'            {json.dumps(a, ensure_ascii=False)}' for a in t5_answers]) + "\n        " + r'\2'
code = re.sub(pat_t5, rep_t5, code, count=1)

# Update validation exemption
old_val = "if t['num'] not in [1, 2, 3] and (length < 38 or length > 45):"
new_val = "if t['num'] not in [1, 2, 3, 5] and (length < 38 or length > 45):"
code = code.replace(old_val, new_val)

with open(builder_path, 'w', encoding='utf-8') as f:
    f.write(code)

print("Updated complete_counseling_55_builder.py Topic 5 successfully.")
