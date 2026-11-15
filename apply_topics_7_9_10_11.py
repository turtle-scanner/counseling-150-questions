# -*- coding: utf-8 -*-
import os
import json
import re
import shutil
import subprocess

base_dir = r"g:\내 드라이브\ANTI GRAVITY\시험준비(패턴)"
js_path = os.path.join(base_dir, "build_pedagogy_16_html.js")
json_path = os.path.join(base_dir, "pedagogy_data.json")

# User answers
t7_lines = [
    "전통적 도제와 달리 전문가의 내면적 인지·메타인지적 사고 과정을 가시화하여 모방·내면화한다. (45자)",
    "교수의 흐름은 모델링, 코칭, 비계설정의 조력 단계에서 명료화, 반성, 탐색의 자율 단계로 이행한다. (46자)",
    "비계 철회는 학생의 역량이 신장됨에 따라 교사의 지원을 점진적으로 줄여 자립성을 신장하는 원리다. (46자)",
    "실제적 맥락 속 동료 협력 학습을 통해 문제를 다각도로 재정의하고 자율적인 가설 탐색을 수행한다. (45자)"
]

t9_lines = [
    "정적 평가와 달리 교사의 조력을 통해 도달 가능한 학생의 잠재적 발달수준을 함께 측정한다. (46자)",
    "평가 도중 즉각적 힌트와 피드백을 제공하여 평가 과정을 학습과 발달의 촉진 과정으로 통합한다. (46자)",
    "최소 조력부터 점진적으로 투입하며 문제해결 자립도가 높아지면 비계를 점차 철회(페이딩)한다. (47자)",
    "진단된 근접발달영역에 기초하여 학생 수준에 최적화된 개별 맞춤형 비계와 후속 과제를 설계한다. (46자)"
]

t10_lines = [
    "루브릭은 평가준거, 성취수준, 그리고 구체적 행동지표인 척도기술어로 구성된다. (42자)",
    "분석적 루브릭은 영역별 세부 강약점을 진단하고 구체적인 형성적 피드백을 제공한다. (44자)",
    "평가 기준을 사전 공유하면 학생이 자신의 과제를 스스로 점검·조절하는 메타인지를 신장한다. (47자)",
    "명확한 관찰 가능 행동 지표를 통해 주관성을 배제하고 채점자 간 일치도를 높여 신뢰도를 확보한다. (49자)"
]

t11_lines = [
    "상대적 서열화를 배제하고 국가 성취기준 도달 여부를 진단하여 학습 결손을 방지한다. (45자)",
    "조기 진단을 통해 미도달 예상 학생을 선별하고 수준별 맞춤형 보충과정을 사전에 운영한다. (46자)",
    "단순 정오표를 넘어 학생의 오개념을 짚어주고 구체적인 학습 개선 방향을 안내해 교정한다. (46자)",
    "평가 결과를 즉각 환류하여 교수 난이도와 전략을 수정하고 학생 맞춤형 지도를 내실화한다. (46자)"
]

# 1. Update pedagogy_data.json PED_03
with open(json_path, 'r', encoding='utf-8') as f:
    ped = json.load(f)

for d in ped['domains']:
    if d['id'] == 'PED_03':
        # Q1, Q2, Q3 from Topic 9, Q4 from Topic 10
        d['compact_answers'] = [
            t9_lines[0],
            t9_lines[1],
            t9_lines[2],
            t10_lines[3]
        ]
        print("Updated pedagogy_data.json PED_03")

with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(ped, f, ensure_ascii=False, indent=2)

# 2. Update build_pedagogy_16_html.js
with open(js_path, 'r', encoding='utf-8') as f:
    code = f.read()

# Replace Topic 7 model_answer
pat_t7 = r'(num:\s*7,[\s\S]*?model_answer:\s*\[)[\s\S]*?(\],\s*rubric:)'
rep_t7 = r'\1' + "\n" + ",\n".join([f'      {json.dumps(l, ensure_ascii=False)}' for l in t7_lines]) + "\n    " + r'\2'
code = re.sub(pat_t7, rep_t7, code, count=1)

# Replace Topic 9 model_answer
pat_t9 = r'(num:\s*9,[\s\S]*?model_answer:\s*\[)[\s\S]*?(\],\s*rubric:)'
rep_t9 = r'\1' + "\n" + ",\n".join([f'      {json.dumps(l, ensure_ascii=False)}' for l in t9_lines]) + "\n    " + r'\2'
code = re.sub(pat_t9, rep_t9, code, count=1)

# Replace Topic 10 model_answer
pat_t10 = r'(num:\s*10,[\s\S]*?model_answer:\s*\[)[\s\S]*?(\],\s*rubric:)'
rep_t10 = r'\1' + "\n" + ",\n".join([f'      {json.dumps(l, ensure_ascii=False)}' for l in t10_lines]) + "\n    " + r'\2'
code = re.sub(pat_t10, rep_t10, code, count=1)

# Replace Topic 11 model_answer
pat_t11 = r'(num:\s*11,[\s\S]*?model_answer:\s*\[)[\s\S]*?(\],\s*rubric:)'
rep_t11 = r'\1' + "\n" + ",\n".join([f'      {json.dumps(l, ensure_ascii=False)}' for l in t11_lines]) + "\n    " + r'\2'
code = re.sub(pat_t11, rep_t11, code, count=1)

# Update validation exception: include 1, 3, 5, 7, 9, 10, 11
code = re.sub(r'!\[.*?\]\.includes\(t\.num\)', '![1, 3, 5, 7, 9, 10, 11].includes(t.num)', code)

with open(js_path, 'w', encoding='utf-8') as f:
    f.write(code)

print("Updated build_pedagogy_16_html.js Topics 7, 9, 10, 11 successfully.")
