import json
import re

with open('scratch/new_203_items_curriculum2022.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

def get_target_terms(kw):
    # remove parenthesized parts or split by slash/comma/dots
    # e.g. "영속적 이해 6대 측면 (설명·해석·적용·관점·감정이입·자기인식)"
    # terms: ["영속적 이해", "설명", "해석", "적용", "관점", "감정이입", "자기인식"]
    raw = kw
    terms = []
    
    # Check for parentheses
    inner = re.findall(r'\((.*?)\)', raw)
    outer = re.sub(r'\(.*?\)', '', raw).strip()
    if outer:
        # clean outer
        for sub in re.split(r'[,·/\s➔]+', outer):
            sub = sub.strip()
            if len(sub) >= 2 and sub not in ['모형', '이론', '과정', '단계', '기법', '원리', '측면', '모델', '유형', '척도', '지표']:
                terms.append(sub)
    for inn in inner:
        for sub in re.split(r'[,·/\s➔]+', inn):
            sub = sub.strip()
            if len(sub) >= 2 and sub not in ['모형', '이론', '과정', '단계', '기법', '원리', '측면', '모델', '유형', '척도', '지표']:
                terms.append(sub)
    
    # Sort by length descending so longer phrases match first
    terms = sorted(list(set(terms)), key=lambda x: len(x), reverse=True)
    return terms

sample_ids = [1, 2, 52, 53, 195]
for it in items:
    if it['num'] in sample_ids:
        print(f"Item {it['num']}: {it['kw']}")
        terms = get_target_terms(it['kw'])
        print(f"  Extracted terms: {terms}")
        ans = it['ans']
        # Highlight in ans
        for t in terms:
            ans = ans.replace(t, f"[{t}]")
        print("  Sample marked ans:")
        for l in ans.split('\n')[:2]:
            print("   ", l)
        print('-'*40)
