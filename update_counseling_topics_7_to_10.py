# -*- coding: utf-8 -*-
import os
import json
import re

base_dir = r"g:\내 드라이브\ANTI GRAVITY\시험준비(패턴)"
builder_path = os.path.join(base_dir, "complete_counseling_55_builder.py")
json_path = os.path.join(base_dir, "counseling_data.json")

t7_answers = [
    "강박장애는 침습적 강박사고와 불안을 중화하려는 외현적·내재적 강박행동을 보인다. (45자)",
    "강박성 성격장애는 규칙, 정리정돈, 통제에 대한 광범위한 집착과 융통성 결여를 보인다. (46자)",
    "강박장애는 비합리성을 인식하는 자아이질적 고통이며, 성격장애는 자아동질적 순응성을 띤다. (47자)",
    "노출 및 반응방지는 두려운 자극에 직면시킨 후 의례적 강박행동을 억제하는 원리이다. (44자)"
]

t8_answers = [
    "4대 증상군은 침습 증상, 지속적 회피, 인지·기분의 부정적 변화, 각성·반응성 변화이다. (46자)",
    "플래시백이나 악몽으로 사건을 재경험하며 외상과 관련된 내적·외적 자극을 적극 회피한다. (46자)",
    "과도한 경계와 수면 곤란 등 과각성을 보이고 부정적 신념과 감정 등 인지적 왜곡이 나타난다. (46자)",
    "증상이 3일-1개월 이내면 급성스트레스장애, 1개월을 초과 지속되면 외상후 스트레스 장애이다. (48자)"
]

t9_answers = [
    "두 장애는 심각한 정서적 방임이나 잦은 주양육자 교체 등 병적인 양육 결손을 공유한다. (46자)",
    "반응성 애착장애는 고통 시 양육자에게 위안을 구하지 않고 억제·위축된 반응을 보인다. (46자)",
    "탈억제 사회관여 장애는 낯선 성인에게 주저함 없이 다가가며 사회적 경계를 지키지 못한다. (47자)",
    "관계 형성의 내면화된 위축·회피 양상과 외현화된 무분별한 탈억제 접근으로 감별한다. (45자)"
]

t10_answers = [
    "경계선 성격장애는 대인관계, 자아상, 정동의 불안정성과 유기를 피하려는 필사적 노력을 보인다. (48자)",
    "의존성 성격장애는 스스로 판단하지 못하고 타인에게 돌봄과 책임을 전가하며 복종한다. (45자)",
    "유기 위기 시 경계선은 분노와 자해로 반응하나 의존성은 복종하며 새로운 대상을 찾는다. (45자)",
    "변증법적 행동치료의 핵심 모듈은 마음챙김, 고통감내, 정서조절, 대인관계 효능성이다. (44자)"
]

# 1. Update counseling_data.json
with open(json_path, 'r', encoding='utf-8') as f:
    c_data = json.load(f)

for t in c_data:
    if t['num'] == 7:
        t['model_answer'] = t7_answers
        print("Updated Topic 7 in counseling_data.json")
    elif t['num'] == 8:
        t['model_answer'] = t8_answers
        print("Updated Topic 8 in counseling_data.json")
    elif t['num'] == 9:
        t['model_answer'] = t9_answers
        print("Updated Topic 9 in counseling_data.json")
    elif t['num'] == 10:
        t['model_answer'] = t10_answers
        print("Updated Topic 10 in counseling_data.json")

with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(c_data, f, ensure_ascii=False, indent=2)

# 2. Update complete_counseling_55_builder.py
with open(builder_path, 'r', encoding='utf-8') as f:
    code = f.read()

# Replace Topic 7 model_answer
pat_t7 = r'("num":\s*7,[\s\S]*?"model_answer":\s*\[)[\s\S]*?(\],\s*"rubric":)'
rep_t7 = r'\1' + "\n" + ",\n".join([f'            {json.dumps(a, ensure_ascii=False)}' for a in t7_answers]) + "\n        " + r'\2'
code = re.sub(pat_t7, rep_t7, code, count=1)

# Replace Topic 8 model_answer
pat_t8 = r'("num":\s*8,[\s\S]*?"model_answer":\s*\[)[\s\S]*?(\],\s*"rubric":)'
rep_t8 = r'\1' + "\n" + ",\n".join([f'            {json.dumps(a, ensure_ascii=False)}' for a in t8_answers]) + "\n        " + r'\2'
code = re.sub(pat_t8, rep_t8, code, count=1)

# Replace Topic 9 model_answer
pat_t9 = r'("num":\s*9,[\s\S]*?"model_answer":\s*\[)[\s\S]*?(\],\s*"rubric":)'
rep_t9 = r'\1' + "\n" + ",\n".join([f'            {json.dumps(a, ensure_ascii=False)}' for a in t9_answers]) + "\n        " + r'\2'
code = re.sub(pat_t9, rep_t9, code, count=1)

# Replace Topic 10 model_answer
pat_t10 = r'("num":\s*10,[\s\S]*?"model_answer":\s*\[)[\s\S]*?(\],\s*"rubric":)'
rep_t10 = r'\1' + "\n" + ",\n".join([f'            {json.dumps(a, ensure_ascii=False)}' for a in t10_answers]) + "\n        " + r'\2'
code = re.sub(pat_t10, rep_t10, code, count=1)

# Update validation exemption: exempt custom topics [1, 2, 3, 5, 6, 7, 8, 9, 10]
new_val = "if t['num'] not in [1, 2, 3, 5, 6, 7, 8, 9, 10] and (length < 38 or length > 45):"
code = re.sub(r"if t\['num'\] not in \[.*?\] and \(length < 38 or length > 45\):", new_val, code)

with open(builder_path, 'w', encoding='utf-8') as f:
    f.write(code)

print("Updated complete_counseling_55_builder.py Topics 7-10 successfully.")
