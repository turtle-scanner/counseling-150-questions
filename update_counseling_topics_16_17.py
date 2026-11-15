# -*- coding: utf-8 -*-
import os
import json
import re

base_dir = r"g:\내 드라이브\ANTI GRAVITY\시험준비(패턴)"
builder_path = os.path.join(base_dir, "complete_counseling_55_builder.py")
json_path = os.path.join(base_dir, "counseling_data.json")

t16_answers = [
    "3대 상위차원 척도는 정서적·내재화, 사고, 행동·외현화 기능이상으로 구성된다. (44자)",
    "의기소침 척도는 전반적인 불행감, 무력감 등 심리적 고통의 공통 요인을 반영한다. (44자)",
    "정서적·내재화는 불안과 우울을, 행동·외현화는 충동성과 물질남용 문제를 시사한다. (45자)",
    "사고 기능이상 척도 상승 시 기태적 사고와 망상, 현실검증력 손상을 감별 평가한다. (45자)"
]

t17_answers = [
    "자살사고 척도 상승은 최근의 구체적 자살 계획과 과거 시도력 등 긴급 위기를 시사한다. (48자)",
    "충동성 및 물질남용 동반 시 인지적 억제 실패로 충동적 행동화와 치명도가 급증한다. (46자)",
    "가족 불화와 대인관계 수동성이 결합하면 지지체계 부재로 청소년 자살 취약성이 증폭된다. (48자)",
    "비밀보장 예외를 고지하고 보호자에게 즉시 인계하며 구체적 안전계획서를 작성한다. (45자)"
]

# 1. Update counseling_data.json
with open(json_path, 'r', encoding='utf-8') as f:
    c_data = json.load(f)

for t in c_data:
    if t['num'] == 16:
        t['model_answer'] = t16_answers
        print("Updated Topic 16 in counseling_data.json")
    elif t['num'] == 17:
        t['model_answer'] = t17_answers
        print("Updated Topic 17 in counseling_data.json")

with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(c_data, f, ensure_ascii=False, indent=2)

# 2. Update complete_counseling_55_builder.py
with open(builder_path, 'r', encoding='utf-8') as f:
    code = f.read()

# Replace Topic 16 model_answer
pat_t16 = r'("num":\s*16,[\s\S]*?"model_answer":\s*\[)[\s\S]*?(\],\s*"rubric":)'
rep_t16 = r'\1' + "\n" + ",\n".join([f'            {json.dumps(a, ensure_ascii=False)}' for a in t16_answers]) + "\n        " + r'\2'
code = re.sub(pat_t16, rep_t16, code, count=1)

# Replace Topic 17 model_answer
pat_t17 = r'("num":\s*17,[\s\S]*?"model_answer":\s*\[)[\s\S]*?(\],\s*"rubric":)'
rep_t17 = r'\1' + "\n" + ",\n".join([f'            {json.dumps(a, ensure_ascii=False)}' for a in t17_answers]) + "\n        " + r'\2'
code = re.sub(pat_t17, rep_t17, code, count=1)

# Update validation exemption: exempt custom topics up to 17
new_val = "if t['num'] not in [1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17] and (length < 38 or length > 45):"
code = re.sub(r"if t\['num'\] not in \[.*?\] and \(length < 38 or length > 45\):", new_val, code)

with open(builder_path, 'w', encoding='utf-8') as f:
    f.write(code)

print("Updated complete_counseling_55_builder.py Topics 16, 17 successfully.")
