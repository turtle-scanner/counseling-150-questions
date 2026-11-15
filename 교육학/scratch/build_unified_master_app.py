# -*- coding: utf-8 -*-
import os, sys, json

sys.stdout.reconfigure(encoding='utf-8')
sys.path.append('scratch')

from test_pedagogy_data import pedagogy_essay
import build_exam_web

with open('scratch/top55_extracted.json', 'r', encoding='utf-8') as f:
    top55_data = json.load(f)

# Prepare top55 clean items
top55_items = []
for idx, item in enumerate(top55_data):
    is_ped = (item.get('type') == 'pedagogy')
    prefix = 'P' if is_ped else 'C'
    cat_name = '교육학 20선' if is_ped else '전공상담 35선'
    
    # Clean keyword
    raw_kw = item.get('keyword', '')
    kws = [k.strip() for k in raw_kw.replace('➔', ',').replace('/', ',').split(',') if k.strip()]
    
    # Clean answer
    clean_a = item.get('clean_ans', item.get('answer', ''))
    clean_a = clean_a.replace('<mark style="background-color: #fff59d; color: #000; padding: 4px 6px; border-radius: 4px; display: inline-block;">', '').replace('</mark>', '').replace('<br>', '\n').strip()
    
    top55_items.append({
        "num": idx + 1,
        "code": f"{prefix}{idx+1:02d}",
        "category": cat_name,
        "type": item.get('type'),
        "domain": item.get('domain', ''),
        "question": item.get('question', ''),
        "keywords": kws,
        "raw_keywords": raw_kw,
        "answer": clean_a
    })

print(f"Loaded {len(top55_items)} top55 items")
print(f"Loaded {len(build_exam_web.questions_a)} QA questions")
print(f"Loaded {len(build_exam_web.questions_b)} QB questions")
