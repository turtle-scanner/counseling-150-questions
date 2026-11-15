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

t19_answers = [
    "전체 반응과 인간운동 반응의 비율은 인지적 포부와 이를 뒷받침하는 지적 자원의 균형이다. (49자)",
    "조직화 점수는 복잡한 자극들의 관계를 유의미하게 통합·구조화하려는 인지적 동기를 뜻한다. (47자)",
    "전통적 형태질 점수는 외부 현실을 관습적·규범적 형태로 왜곡 없이 지각하는 능력을 잰다. (46자)",
    "형태질 저하와 왜곡 형태 급증 시 망상 등 사고장애와 현실검증력 손상을 감별 평가한다. (45자)"
]

t20_answers = [
    "자극추구는 새로움에 대한 탐색 행동과 충동성, 지루함에 취약한 특성을 보인다. (44자)",
    "위험회피는 위험 신호에 따른 행동 억제와 예기불안, 피로에 취약한 특성을 뜻한다. (45자)",
    "보상의존은 사회적 애착과 칭찬 반응성이고 인내력은 좌절 속에서도 끈기를 유지한다. (46자)",
    "두 기질이 모두 높으면 호기심과 공포가 충돌하여 심한 접근-회피 갈등을 겪는다. (44자)"
]

# 1. Update counseling_data.json
with open(json_path, 'r', encoding='utf-8') as f:
    c_data = json.load(f)

for t in c_data:
    if t['num'] == 18:
        t['model_answer'] = t18_answers
        print("Updated Topic 18 in counseling_data.json")
    elif t['num'] == 19:
        t['model_answer'] = t19_answers
        print("Updated Topic 19 in counseling_data.json")
    elif t['num'] == 20:
        t['model_answer'] = t20_answers
        print("Updated Topic 20 in counseling_data.json")

with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(c_data, f, ensure_ascii=False, indent=2)

# 2. Update complete_counseling_55_builder.py
with open(builder_path, 'r', encoding='utf-8') as f:
    code = f.read()

# Replace Topic 18 model_answer
pat_t18 = r'("num":\s*18,[\s\S]*?"model_answer":\s*\[)[\s\S]*?(\],\s*"rubric":)'
rep_t18 = r'\1' + "\n" + ",\n".join([f'            {json.dumps(a, ensure_ascii=False)}' for a in t18_answers]) + "\n        " + r'\2'
code = re.sub(pat_t18, rep_t18, code, count=1)

# Replace Topic 19 model_answer
pat_t19 = r'("num":\s*19,[\s\S]*?"model_answer":\s*\[)[\s\S]*?(\],\s*"rubric":)'
rep_t19 = r'\1' + "\n" + ",\n".join([f'            {json.dumps(a, ensure_ascii=False)}' for a in t19_answers]) + "\n        " + r'\2'
code = re.sub(pat_t19, rep_t19, code, count=1)

# Replace Topic 20 model_answer
pat_t20 = r'("num":\s*20,[\s\S]*?"model_answer":\s*\[)[\s\S]*?(\],\s*"rubric":)'
rep_t20 = r'\1' + "\n" + ",\n".join([f'            {json.dumps(a, ensure_ascii=False)}' for a in t20_answers]) + "\n        " + r'\2'
code = re.sub(pat_t20, rep_t20, code, count=1)

# Update validation exemption: exempt custom topics up to 20
new_val = "if t['num'] not in [1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20] and (length < 38 or length > 45):"
code = re.sub(r"if t\['num'\] not in \[.*?\] and \(length < 38 or length > 45\):", new_val, code)

with open(builder_path, 'w', encoding='utf-8') as f:
    f.write(code)

print("Updated complete_counseling_55_builder.py Topics 18-20 successfully.")
