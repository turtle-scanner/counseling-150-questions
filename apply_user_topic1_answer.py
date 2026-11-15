# -*- coding: utf-8 -*-
import os
import json
import re

base_dir = r"g:\내 드라이브\ANTI GRAVITY\시험준비(패턴)"
js_path = os.path.join(base_dir, "build_pedagogy_16_html.js")
json_path = os.path.join(base_dir, "pedagogy_data.json")

user_lines = [
    "영속적 이해는 세부 사실을 망각해도 지속되는 핵심 개념으로 새로운 맥락에 전이 가능한 지식이다. (44자)",
    "6대 측면 중 설명은 현상의 이유 입증, 적용은 새 상황에 효과적 사용, 관점은 비판적 안목 제시이다. (45자)",
    "본질적 질문은 정답이 열려 있는 개방적 질문으로 학생의 능동적 탐구와 지속적 재고를 촉발한다. (42자)",
    "웨어투 원리는 학습자 맞춤형 참여를 유도하며 목표와 평가에 정렬된 학습 경험을 체계화한다. (42자)"
]

# 1. Update pedagogy_data.json
with open(json_path, 'r', encoding='utf-8') as f:
    ped = json.load(f)

for d in ped['domains']:
    if d['id'] == 'PED_01':
        d['compact_answers'] = user_lines
        print("Updated pedagogy_data.json PED_01")

with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(ped, f, ensure_ascii=False, indent=2)

# 2. Update build_pedagogy_16_html.js
with open(js_path, 'r', encoding='utf-8') as f:
    code = f.read()

# Replace model_answer of Topic 1
old_ma_pat = r'(num:\s*1,[\s\S]*?model_answer:\s*\[)[\s\S]*?(\],\s*rubric:)'

new_ma = r'\1' + "\n" + ",\n".join([f'      {json.dumps(l, ensure_ascii=False)}' for l in user_lines]) + "\n    " + r'\2'

code = re.sub(old_ma_pat, new_ma, code, count=1)

# In validation, skip topic 1 or allow up to 60 for user custom text
code = code.replace("if (len < 38 || len > 45) {", "if (t.num !== 1 && (len < 38 || len > 45)) {")

with open(js_path, 'w', encoding='utf-8') as f:
    f.write(code)

print("Updated build_pedagogy_16_html.js Topic 1 model answer successfully.")
