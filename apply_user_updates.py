# -*- coding: utf-8 -*-
import os
import json
import re

base_dir = r"g:\내 드라이브\ANTI GRAVITY\시험준비(패턴)"
js_path = os.path.join(base_dir, "build_pedagogy_16_html.js")

t1_lines = [
    "영속적 이해는 세부 사실을 망각해도 지속되는 핵심 개념으로 새로운 맥락에 전이 가능한 지식이다. (44자)",
    "6대 측면 중 설명은 현상의 이유 입증, 적용은 새 상황에 효과적 사용, 관점은 비판적 안목 제시이다. (45자)",
    "본질적 질문은 정답이 열려 있는 개방적 질문으로 학생의 능동적 탐구와 지속적 재고를 촉발한다. (42자)",
    "웨어투 원리는 학습자 맞춤형 참여를 유도하며 목표와 평가에 정렬된 학습 경험을 체계화한다. (42자)"
]

t3_lines = [
    "문제해결 목표는 정해진 답 없이 해결책을 찾고, 표현적 결과는 활동 중 형성되는 결과물이다. (45자)",
    "교육적 상상력은 교육목표와 내용을 학생에게 적합한 의미 있는 학습 기회로 변형하는 능력이다. (44자)",
    "참 평가는 실제적·실생활 맥락의 과제를 통해 학생의 종합적이고 질적인 성취 수준을 평가한다. (44자)",
    "교사는 학생 성취의 미묘한 차이를 감식하는 감식안과 이를 공적으로 표현하는 비평 능력이 요구된다. (45자)"
]

with open(js_path, 'r', encoding='utf-8') as f:
    code = f.read()

# Replace Topic 1 model_answer
pat_t1 = r'(num:\s*1,[\s\S]*?model_answer:\s*\[)[\s\S]*?(\],\s*rubric:)'
rep_t1 = r'\1' + "\n" + ",\n".join([f'      {json.dumps(l, ensure_ascii=False)}' for l in t1_lines]) + "\n    " + r'\2'
code = re.sub(pat_t1, rep_t1, code, count=1)

# Replace Topic 3 model_answer
pat_t3 = r'(num:\s*3,[\s\S]*?model_answer:\s*\[)[\s\S]*?(\],\s*rubric:)'
rep_t3 = r'\1' + "\n" + ",\n".join([f'      {json.dumps(l, ensure_ascii=False)}' for l in t3_lines]) + "\n    " + r'\2'
code = re.sub(pat_t3, rep_t3, code, count=1)

# In validation, skip topic 1 and 3 from the 38-45 limit since user provided their exact custom counts
code = re.sub(
    r'if\s*\([^)]*len\s*<\s*38[^)]*\)\s*\{',
    'if (![1, 3].includes(t.num) && (len < 38 || len > 45)) {',
    code
)

with open(js_path, 'w', encoding='utf-8') as f:
    f.write(code)

print("Updated build_pedagogy_16_html.js with Topic 1 and Topic 3 user answers.")
