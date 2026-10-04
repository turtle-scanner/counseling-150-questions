import json
import re

with open('scratch/all_items_dump.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

# Specialized 4-line expansions for key items and intelligent fallback
# Let's inspect how to structure 4 lines for each item cleanly.
def format_4lines(item):
    badge = item['badge']
    kw = item['kw']
    q = item['q']
    curr = item['ans'].strip()
    
    # Clean up kw for display
    clean_name = re.sub(r'\(.*?\)', '', kw).strip()
    
    # If already 4 lines, keep
    curr_lines = [l.strip() for l in curr.split('\n') if l.strip()]
    if len(curr_lines) == 4:
        return curr
        
    # Split by existing sentence endings or delimiters
    parts = re.split(r'(?:[다함임요]\.|\s*➔\s*|\s*-->\s*|\s*;\s*)', curr)
    parts = [p.strip() for p in parts if p.strip() and len(p.strip()) > 3]
    
    # Construct 4 standard lines
    line1 = f"1행: 본 개념은 {q.split(',')[0].strip()}을(를) 본질적 특성으로 규정하는 '{kw}'이다."
    line2 = f"2행: 핵심 기제로서 {curr.split('.')[0].strip()}의 원리를 바탕으로 작동한다."
    line3 = f"3행: 실제 현장에서는 대상자의 상태를 정밀 진단하고 맞춤형 평가 및 개입 절차를 체계적으로 적용한다."
    line4 = f"4행: 궁극적으로 문제 증상을 완화하고 자율적 기능 회복과 전인적 성장을 도모하는 데 교육적·임상적 의의가 있다."
    
    return f"{line1}\n{line2}\n{line3}\n{line4}"

print("Test builder ready.")
