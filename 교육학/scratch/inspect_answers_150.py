import json, os, sys
sys.stdout.reconfigure(encoding='utf-8')

script_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(script_dir)
json_path = os.path.join(parent_dir, 'scratch_150_pages.json')

with open(json_path, 'r', encoding='utf-8') as f:
    pages = json.load(f)

for p in pages[:2]:
    print(f"Page {p['pageNum']}: {p['pageTitle']}")
    for it in p['items'][:3]:
        print(f"  [{it['id']}] {it['keywords']}")
        print(f"    Q: {it['question'][:50]}...")
        print(f"    A: {it['answer'][:60]}...")
