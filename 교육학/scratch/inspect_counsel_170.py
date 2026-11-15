import json, os, sys
sys.stdout.reconfigure(encoding='utf-8')

script_dir = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(script_dir, 'new_203_items_curriculum2022.json')

with open(json_path, 'r', encoding='utf-8') as f:
    items = json.load(f)

edu_badges = ['교육과정', '교육행정', '교수학습', '교육평가', '교육심리', '교육방법·학습', '교육심리·특수']
counsel_list = [it for it in items if it['badge'] not in edu_badges]

print(f"Total counsel items: {len(counsel_list)}")

# Print domain breakdown
from collections import Counter
badges = [it['badge'] for it in counsel_list]
for b, c in Counter(badges).most_common():
    print(f"  {b}: {c}")
