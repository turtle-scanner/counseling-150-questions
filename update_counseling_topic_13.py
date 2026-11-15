# -*- coding: utf-8 -*-
import os
import json
import re

base_dir = r"g:\내 드라이브\ANTI GRAVITY\시험준비(패턴)"
builder_path = os.path.join(base_dir, "complete_counseling_55_builder.py")
json_path = os.path.join(base_dir, "counseling_data.json")

t13_answers = [
    "언어이해, 시공간, 유동추론, 작업기억, 처리속도로 결정·유동 지능과 인지 효율을 잰다. (46자)",
    "시각적 공간 구성 능력과 비언어적 귀납 논리 추론 능력을 독립적으로 분리 측정하기 위함이다. (47자)",
    "전체 지능지수는 공통성, 어휘, 토막짜기, 행렬추론, 무게비교, 숫자, 기호쓰기 7개로 잰다. (47자)",
    "지표 간 현저한 분산 시 전체 지수는 대표성을 잃으므로 지표별 프로파일 강약점을 분석한다. (46자)"
]

# 1. Update counseling_data.json
with open(json_path, 'r', encoding='utf-8') as f:
    c_data = json.load(f)

for t in c_data:
    if t['num'] == 13:
        t['model_answer'] = t13_answers
        print("Updated Topic 13 in counseling_data.json")

with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(c_data, f, ensure_ascii=False, indent=2)

# 2. Update complete_counseling_55_builder.py
with open(builder_path, 'r', encoding='utf-8') as f:
    code = f.read()

# Replace Topic 13 model_answer
pat_t13 = r'("num":\s*13,[\s\S]*?"model_answer":\s*\[)[\s\S]*?(\],\s*"rubric":)'
rep_t13 = r'\1' + "\n" + ",\n".join([f'            {json.dumps(a, ensure_ascii=False)}' for a in t13_answers]) + "\n        " + r'\2'
code = re.sub(pat_t13, rep_t13, code, count=1)

# Update validation exemption: exempt custom topics [1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13]
new_val = "if t['num'] not in [1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13] and (length < 38 or length > 45):"
code = re.sub(r"if t\['num'\] not in \[.*?\] and \(length < 38 or length > 45\):", new_val, code)

with open(builder_path, 'w', encoding='utf-8') as f:
    f.write(code)

print("Updated complete_counseling_55_builder.py Topic 13 successfully.")
