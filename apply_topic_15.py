# -*- coding: utf-8 -*-
import os
import json
import re

base_dir = r"g:\내 드라이브\ANTI GRAVITY\시험준비(패턴)"
js_path = os.path.join(base_dir, "build_pedagogy_16_html.js")

# User answers for Topic 15 (교내 자율장학 혁신: 임상장학 & 동료장학)
t15_lines = [
    "수업 전 계획 협의, 객관적 관찰과 자료 수집, 수업 후 피드백 협의회의 연속 단계로 전개된다. (47자)",
    "장학담당자는 감독자가 아닌 대등한 입장에서 수업 고민을 함께 해결하는 수평적 조력자여야 한다. (48자)",
    "동료장학은 교사 간 상호 수업을 참관·협의하여 교수 지식과 실천적 전문성을 나누는 방식이다. (47자)",
    "자율성과 신뢰에 기반한 일상적 수업 나눔을 실천하여 협력적 교원학습공동체로 체계화한다. (46자)"
]

# Update build_pedagogy_16_html.js Topic 15
with open(js_path, 'r', encoding='utf-8') as f:
    code = f.read()

# Replace Topic 15 model_answer
pat_t15 = r'(num:\s*15,[\s\S]*?model_answer:\s*\[)[\s\S]*?(\],\s*rubric:)'
rep_t15 = r'\1' + "\n" + ",\n".join([f'      {json.dumps(l, ensure_ascii=False)}' for l in t15_lines]) + "\n    " + r'\2'
code = re.sub(pat_t15, rep_t15, code, count=1)

# Update validation exception: include 1, 3, 5, 7, 9, 10, 11, 13, 15
code = re.sub(r'!\[.*?\]\.includes\(t\.num\)', '![1, 3, 5, 7, 9, 10, 11, 13, 15].includes(t.num)', code)

with open(js_path, 'w', encoding='utf-8') as f:
    f.write(code)

print("Updated build_pedagogy_16_html.js Topic 15 successfully.")
