import json
import re

with open('scratch/all_items_dump.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

# Let's write an intelligent 4-line builder for items
def build_4line_answer(item):
    kw = item['kw']
    badge = item['badge']
    q = item['q']
    curr_ans = item['ans'].strip()
    
    # If already has 4 lines separated by \n, keep or refine
    lines = [l.strip() for l in curr_ans.split('\n') if l.strip()]
    if len(lines) == 4 and all(len(l) > 10 for l in lines):
        return '\n'.join(lines)
        
    # Build 4 lines based on item content and domain
    # Remove existing quotes around kw if any
    clean_kw = re.sub(r'[\'\"()]', '', kw).split()[0]
    
    # We will craft domain-specific 4 lines
    return None

print("Checking structure...")
