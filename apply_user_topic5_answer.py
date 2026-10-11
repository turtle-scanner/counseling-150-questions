# -*- coding: utf-8 -*-
import os
import json
import re

base_dir = r"g:\내 드라이브\ANTI GRAVITY\시험준비(패턴)"
js_path = os.path.join(base_dir, "build_pedagogy_16_html.js")
json_path = os.path.join(base_dir, "pedagogy_data.json")

t5_lines = [
    "수업 전 디딤영상으로 기본 개념을 사전 학습하여 개별 속도에 맞춘 기초 지식을 형성한다. (45자)",
    "수업 중 토의·토론 및 문제해결 등 협력 탐구를 수행하며 교사는 오개념을 교정하고 비계를 준다. (46자)",
    "교사는 순회 지도를 통해 즉각적 피드백을 제공하여 학습자의 심층적 이해와 적용을 촉진한다. (44자)",
    "수업 후 성찰일지로 자신의 이해도를 점검하고 학습 과정을 조절하는 메타인지를 신장한다. (43자)"
]

# 1. Update pedagogy_data.json PED_02
with open(json_path, 'r', encoding='utf-8') as f:
    ped = json.load(f)

for d in ped['domains']:
    if d['id'] == 'PED_02':
        d['compact_answers'] = t5_lines
        print("Updated pedagogy_data.json PED_02")

with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(ped, f, ensure_ascii=False, indent=2)

# 2. Update build_pedagogy_16_html.js Topic 5
with open(js_path, 'r', encoding='utf-8') as f:
    code = f.read()

# Replace Topic 5 model_answer
pat_t5 = r'(num:\s*5,[\s\S]*?model_answer:\s*\[)[\s\S]*?(\],\s*rubric:)'
rep_t5 = r'\1' + "\n" + ",\n".join([f'      {json.dumps(l, ensure_ascii=False)}' for l in t5_lines]) + "\n    " + r'\2'
code = re.sub(pat_t5, rep_t5, code, count=1)

# Allow topic 5 in validation
code = code.replace("![1, 3].includes(t.num)", "![1, 3, 5].includes(t.num)")

with open(js_path, 'w', encoding='utf-8') as f:
    f.write(code)

print("Updated build_pedagogy_16_html.js Topic 5 user answers.")
