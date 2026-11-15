# -*- coding: utf-8 -*-
import os
import json
import re

base_dir = r"g:\내 드라이브\ANTI GRAVITY\시험준비(패턴)"
builder_path = os.path.join(base_dir, "complete_counseling_55_builder.py")
json_path = os.path.join(base_dir, "counseling_data.json")

t1_answers = [
    "자폐스펙트럼장애는 사회적 상호작용 및 정서적 상호성 결함으로 관계 형성이 어렵다. (43자)",
    "사회적 의사소통장애는 자폐스펙트럼장애와 달리 상동증적 제한·반복 행동이 없다. (42자)",
    "자폐스펙트럼장애의 반복 행동에는 상동증적 동작과 동일성에 대한 고집이 포함된다. (42자)",
    "증상은 초기 발달기에 시작되며 사회적·직업적 기능의 손상 여부로 장애를 평가한다. (42자)"
]

t2_answers = [
    "부주의 증상 6개 이상 또는 과잉행동-충동성 증상 6개 이상이 6개월간 지속된다. (45자)",
    "아형은 복합형, 주의력결핍 우세형, 과잉행동-충동성 우세형의 세 가지로 구분한다. (44자)",
    "증상은 12세 이전에 발현하며 가정과 학교 등 둘 이상의 환경에서 기능 손상을 준다. (45자)",
    "환경 구조화로 방해 자극을 줄이고 목표 행동 시 토큰 경제로 즉각적인 강화를 준다. (44자)"
]

# 1. Update counseling_data.json
with open(json_path, 'r', encoding='utf-8') as f:
    c_data = json.load(f)

for t in c_data:
    if t['num'] == 1:
        t['model_answer'] = t1_answers
        print("Updated Topic 1 in counseling_data.json")
    elif t['num'] == 2:
        t['model_answer'] = t2_answers
        print("Updated Topic 2 in counseling_data.json")

with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(c_data, f, ensure_ascii=False, indent=2)

# 2. Update complete_counseling_55_builder.py
with open(builder_path, 'r', encoding='utf-8') as f:
    code = f.read()

# Replace Topic 1 model_answer
pat_t1 = r'("num":\s*1,[\s\S]*?"model_answer":\s*\[)[\s\S]*?(\],\s*"rubric":)'
rep_t1 = r'\1' + "\n" + ",\n".join([f'            {json.dumps(a, ensure_ascii=False)}' for a in t1_answers]) + "\n        " + r'\2'
code = re.sub(pat_t1, rep_t1, code, count=1)

# Replace Topic 2 model_answer
pat_t2 = r'("num":\s*2,[\s\S]*?"model_answer":\s*\[)[\s\S]*?(\],\s*"rubric":)'
rep_t2 = r'\1' + "\n" + ",\n".join([f'            {json.dumps(a, ensure_ascii=False)}' for a in t2_answers]) + "\n        " + r'\2'
code = re.sub(pat_t2, rep_t2, code, count=1)

with open(builder_path, 'w', encoding='utf-8') as f:
    f.write(code)

print("Updated complete_counseling_55_builder.py Topic 1 & Topic 2 successfully.")
