# -*- coding: utf-8 -*-
import json
import re

html_path = 'g:/내 드라이브/ANTI GRAVITY/전문상담임용고시/counseling_55_topics.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

m = re.search(r'const topics = (\[[\s\S]*?\]);', html_content)
topics = json.loads(m.group(1))

data_path = 'g:/내 드라이브/ANTI GRAVITY/시험준비(패턴)/counseling_data.json'
with open(data_path, 'r', encoding='utf-8') as f:
    c_data = json.load(f)

for t in topics:
    num = t['num']
    for item in c_data:
        if item.get('num') == num:
            item['model_answer'] = t['model_answer']
            item['four_lines'] = [re.sub(r'\s*\(\d+자\)$', '', line).strip() for line in t['model_answer']]
            item['rubric'] = t.get('rubric', [])
            item['sub_questions'] = t.get('sub_questions', [])
            item['keywords'] = t.get('keywords', [])
            break

with open(data_path, 'w', encoding='utf-8') as f:
    json.dump(c_data, f, ensure_ascii=False, indent=2)

print("Synchronized counseling_data.json via HTML topics successfully!")
