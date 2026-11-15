# -*- coding: utf-8 -*-
import os
import json
import re

base_dir = r"g:\내 드라이브\ANTI GRAVITY\시험준비(패턴)"
builder_path = os.path.join(base_dir, "complete_counseling_55_builder.py")
json_path = os.path.join(base_dir, "counseling_data.json")

t14_answers = [
    "시공간 지표의 2가지 핵심 소검사는 토막짜기와 시각퍼즐로 구성된다. (38자)",
    "유동추론 지표의 2가지 핵심 소검사는 행렬추론과 무게비교가 해당한다. (39자)",
    "시각-운동 협응을 통한 부분-전체 관계 분석 및 정신적 회전·합성을 측정한다. (44자)",
    "새로운 시각 자극의 귀납적 규칙 발견과 양적 개념에 기반한 연역 추론을 평가한다. (46자)"
]

# 1. Update counseling_data.json
with open(json_path, 'r', encoding='utf-8') as f:
    c_data = json.load(f)

for t in c_data:
    if t['num'] == 14:
        t['model_answer'] = t14_answers
        print("Updated Topic 14 in counseling_data.json")

with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(c_data, f, ensure_ascii=False, indent=2)

# 2. Update complete_counseling_55_builder.py
with open(builder_path, 'r', encoding='utf-8') as f:
    code = f.read()

# Replace Topic 14 model_answer
pat_t14 = r'("num":\s*14,[\s\S]*?"model_answer":\s*\[)[\s\S]*?(\],\s*"rubric":)'
rep_t14 = r'\1' + "\n" + ",\n".join([f'            {json.dumps(a, ensure_ascii=False)}' for a in t14_answers]) + "\n        " + r'\2'
code = re.sub(pat_t14, rep_t14, code, count=1)

# Update validation exemption: exempt custom topics [1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
new_val = "if t['num'] not in [1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] and (length < 38 or length > 45):"
code = re.sub(r"if t\['num'\] not in \[.*?\] and \(length < 38 or length > 45\):", new_val, code)

with open(builder_path, 'w', encoding='utf-8') as f:
    f.write(code)

print("Updated complete_counseling_55_builder.py Topic 14 successfully.")
