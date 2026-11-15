# -*- coding: utf-8 -*-
import json
import re

with open('교육학/exam_2027_kice_ab.html', 'r', encoding='utf-8') as f:
    text = f.read()

mA = re.search(r'const examDataA = (\[[\s\S]*?\]);', text)
mB = re.search(r'const examDataB = (\[[\s\S]*?\]);', text)

if mA and mB:
    dataA = json.loads(mA.group(1))
    dataB = json.loads(mB.group(1))
    print(f"examDataA count: {len(dataA)}")
    print(f"examDataB count: {len(dataB)}")
    
    with open('inspect_items.txt', 'w', encoding='utf-8') as out:
        for item in dataA:
            out.write(f"=== A형 {item['num']}번 [{item['type']}] ({item['score']}점) ===\n")
            out.write(f"title: {item['title']}\n")
            out.write(f"content: {item['content'][:120]}...\n")
            out.write(f"model_answer: {item.get('model_answer','')}\n")
            out.write(f"rubric: {item.get('rubric',[])}\n\n")
            
        for item in dataB:
            out.write(f"=== B형 {item['num']}번 [{item['type']}] ({item['score']}점) ===\n")
            out.write(f"title: {item['title']}\n")
            out.write(f"content: {item['content'][:120]}...\n")
            out.write(f"model_answer: {item.get('model_answer','')}\n")
            out.write(f"rubric: {item.get('rubric',[])}\n\n")
    print("Saved inspect_items.txt")
else:
    print("Match failed")
