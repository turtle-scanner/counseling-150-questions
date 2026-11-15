# -*- coding: utf-8 -*-
import os
import json
import re

base_dir = r"g:\내 드라이브\ANTI GRAVITY\시험준비(패턴)"
js_path = os.path.join(base_dir, "build_pedagogy_16_html.js")
json_path = os.path.join(base_dir, "pedagogy_data.json")

# User answers for Topic 13 (세르지오바니 도덕적 리더십)
t13_lines = [
    "관료적 권위를 탈피하여 교사의 전문적 책무성과 도덕적 의무감에 권위의 원천을 둔다. (46자)",
    "교사에게 권한과 자율성을 부여하고 책임을 공유하여 스스로를 이끄는 자기지도자로 세운다. (46자)",
    "신뢰를 기반으로 핵심 교육 가치와 비전을 공유하여 유대감 있는 도덕적 공동체를 구축한다. (46자)",
    "외적 보상이나 통제 없이도 자발적 내적 동기와 사명감을 유발하여 학교 효과성을 높인다. (46자)"
]

# 1. Update pedagogy_data.json PED_04
with open(json_path, 'r', encoding='utf-8') as f:
    ped = json.load(f)

for d in ped['domains']:
    if d['id'] == 'PED_04':
        d['compact_answers'] = t13_lines
        print("Updated pedagogy_data.json PED_04")

with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(ped, f, ensure_ascii=False, indent=2)

# 2. Update build_pedagogy_16_html.js Topic 13
with open(js_path, 'r', encoding='utf-8') as f:
    code = f.read()

# Replace Topic 13 model_answer
pat_t13 = r'(num:\s*13,[\s\S]*?model_answer:\s*\[)[\s\S]*?(\],\s*rubric:)'
rep_t13 = r'\1' + "\n" + ",\n".join([f'      {json.dumps(l, ensure_ascii=False)}' for l in t13_lines]) + "\n    " + r'\2'
code = re.sub(pat_t13, rep_t13, code, count=1)

# Update validation exception: include 1, 3, 5, 7, 9, 10, 11, 13
code = re.sub(r'!\[.*?\]\.includes\(t\.num\)', '![1, 3, 5, 7, 9, 10, 11, 13].includes(t.num)', code)

with open(js_path, 'w', encoding='utf-8') as f:
    f.write(code)

print("Updated build_pedagogy_16_html.js Topic 13 successfully.")
