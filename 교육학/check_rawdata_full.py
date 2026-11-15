# -*- coding: utf-8 -*-
import json

with open('g:/내 드라이브/ANTI GRAVITY/전문상담임용고시/exam_master_2027.html', 'r', encoding='utf-8') as f:
    content = f.read()

idx = content.find('const rawData =')
end_idx = content.find('let currentTab', idx)

json_str = content[idx+len('const rawData ='):end_idx].strip()
if json_str.endswith(';'):
    json_str = json_str[:-1].strip()

try:
    d = json.loads(json_str)
    print("rawData JSON successfully parsed!")
    print("top55 count:", len(d.get('top55', [])))
    print("pedagogy domains:", len(d.get('pedagogy', {}).get('domains', [])))
    print("questions_a count:", len(d.get('questions_a', [])))
    print("questions_b count:", len(d.get('questions_b', [])))
    
    # 1교시 교육학 문항 수
    print("pedagogy domains:", [dm['name'] for dm in d.get('pedagogy', {}).get('domains', [])])
    
    # 전공 A 문항 번호
    qa_nums = [q['num'] for q in d.get('questions_a', [])]
    print("Questions A nums:", qa_nums)
    
    # 전공 B 문항 번호
    qb_nums = [q['num'] for q in d.get('questions_b', [])]
    print("Questions B nums:", qb_nums)

except Exception as e:
    print("JSON parsing error:", e)
