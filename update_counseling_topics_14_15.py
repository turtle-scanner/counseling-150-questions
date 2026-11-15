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

t15_answers = [
    "무선 반응인 가변적 비일관성과 고정 반응인 고정적 비일관성으로 무관련 반응을 탐지한다. (47자)",
    "비전형 척도는 드문 반응을 측정하여 심각한 정신병리의 과장 보고 및 부정적 왜곡을 감별한다. (48자)",
    "드문 미덕 척도는 사소한 결점을 부인하고 비현실적 도덕성을 주장하는 소박한 과소보고를 잰다. (48자)",
    "조정 척도가 높으면 세련된 방어성으로 심리적 적응을 과장하여 임상 척도가 위축 왜곡된다. (46자)"
]

# 1. Update counseling_data.json
with open(json_path, 'r', encoding='utf-8') as f:
    c_data = json.load(f)

for t in c_data:
    if t['num'] == 14:
        t['model_answer'] = t14_answers
        print("Updated Topic 14 in counseling_data.json")
    elif t['num'] == 15:
        t['model_answer'] = t15_answers
        print("Updated Topic 15 in counseling_data.json")

with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(c_data, f, ensure_ascii=False, indent=2)

# 2. Update complete_counseling_55_builder.py
with open(builder_path, 'r', encoding='utf-8') as f:
    code = f.read()

# Replace Topic 14 model_answer
pat_t14 = r'("num":\s*14,[\s\S]*?"model_answer":\s*\[)[\s\S]*?(\],\s*"rubric":)'
rep_t14 = r'\1' + "\n" + ",\n".join([f'            {json.dumps(a, ensure_ascii=False)}' for a in t14_answers]) + "\n        " + r'\2'
code = re.sub(pat_t14, rep_t14, code, count=1)

# Replace Topic 15 model_answer
pat_t15 = r'("num":\s*15,[\s\S]*?"model_answer":\s*\[)[\s\S]*?(\],\s*"rubric":)'
rep_t15 = r'\1' + "\n" + ",\n".join([f'            {json.dumps(a, ensure_ascii=False)}' for a in t15_answers]) + "\n        " + r'\2'
code = re.sub(pat_t15, rep_t15, code, count=1)

# Update validation exemption: exempt custom topics [1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
new_val = "if t['num'] not in [1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] and (length < 38 or length > 45):"
code = re.sub(r"if t\['num'\] not in \[.*?\] and \(length < 38 or length > 45\):", new_val, code)

with open(builder_path, 'w', encoding='utf-8') as f:
    f.write(code)

print("Updated complete_counseling_55_builder.py Topics 14, 15 successfully.")
