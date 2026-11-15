# -*- coding: utf-8 -*-
import json

with open('g:/내 드라이브/ANTI GRAVITY/전문상담임용고시/exam_master_2027.html', 'r', encoding='utf-8') as f:
    content = f.read()

idx = content.find('const rawData =')
end_idx = content.find('let currentTab', idx)

raw_snippet = content[idx+len('const rawData ='):end_idx].strip()
json_str = raw_snippet[:raw_snippet.rfind('}')+1]

d = json.loads(json_str)
print("rawData JSON successfully parsed!")
print("top55 count:", len(d.get('top55', [])))
print("pedagogy domains:", len(d.get('pedagogy', {}).get('domains', [])))
print("questions_a count:", len(d.get('questions_a', [])))
print("questions_b count:", len(d.get('questions_b', [])))
print("questions_a nums:", [q['num'] for q in d.get('questions_a', [])])
print("questions_b nums:", [q['num'] for q in d.get('questions_b', [])])
