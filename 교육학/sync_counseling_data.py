# -*- coding: utf-8 -*-
import json
import re

builder_path = 'g:/내 드라이브/ANTI GRAVITY/시험준비(패턴)/complete_counseling_55_builder.py'
with open(builder_path, 'r', encoding='utf-8') as f:
    code = f.read()

# builder에서 counseling_55_topics 추출
idx = code.find('counseling_55_topics = [')
end_idx = code.find('\n\n# Validation check', idx)
if end_idx == -1:
    end_idx = code.find('\nerrors = 0', idx)

topics_block = code[idx+len('counseling_55_topics = '):end_idx].strip()
# json으로 파싱하기 위해 Python 딕셔너리 안전 평가
import ast
topics = ast.literal_eval(topics_block)

data_path = 'g:/내 드라이브/ANTI GRAVITY/시험준비(패턴)/counseling_data.json'
with open(data_path, 'r', encoding='utf-8') as f:
    c_data = json.load(f)

for t in topics:
    num = t['num']
    # c_data에서 해당 num 찾기
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

print("Synchronized counseling_data.json with all 55 topics perfectly!")
