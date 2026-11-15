# -*- coding: utf-8 -*-
import json
import re

with open('exam_master_2027.html', 'r', encoding='utf-8') as f:
    html = f.read()

match = re.search(r'const rawData = (\{[\s\S]*?\});\n', html)
if match:
    data = json.loads(match.group(1))
    qa = data.get('questions_a', [])
    qb = data.get('questions_b', [])
    print(f"Loaded questions_a: {len(qa)} items")
    print(f"Loaded questions_b: {len(qb)} items")
    
    with open('qa_qb_summary.txt', 'w', encoding='utf-8') as out:
        out.write("=== 전공 A형 (총 12문항 / 40점) ===\n")
        for item in qa:
            out.write(f"\n[A형 {item['num']}번] {item['type']} ({item['score']}점)\n")
            out.write(f"제목: {item.get('title','')}\n")
            out.write(f"지문(앞 150자): {item.get('content','')[:150]}...\n")
            out.write(f"모범답안: {item.get('model_answer','')}\n")
            out.write(f"채점표: {item.get('rubric', [])}\n")
            
        out.write("\n\n=== 전공 B형 (총 11문항 / 40점) ===\n")
        for item in qb:
            out.write(f"\n[B형 {item['num']}번] {item['type']} ({item['score']}점)\n")
            out.write(f"제목: {item.get('title','')}\n")
            out.write(f"지문(앞 150자): {item.get('content','')[:150]}...\n")
            out.write(f"모범답안: {item.get('model_answer','')}\n")
            out.write(f"채점표: {item.get('rubric', [])}\n")
    print("Saved qa_qb_summary.txt")
else:
    print("Match failed")
