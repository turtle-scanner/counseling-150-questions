# -*- coding: utf-8 -*-
import json

with open('full_exam_dump.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

qa = d['questions_a']
qb = d['questions_b']

print("=== A형 ===")
for q in qa:
    print(f"A{q['num']} [{q['type']}, {q['score']}점] {q['title'][:30]}")

print("\n=== B형 ===")
for q in qb:
    print(f"B{q['num']} [{q['type']}, {q['score']}점] {q['title'][:30]}")
