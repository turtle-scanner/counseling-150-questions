import json, os, sys
sys.stdout.reconfigure(encoding='utf-8')

script_dir = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(script_dir, 'new_203_items_curriculum2022.json')

with open(json_path, 'r', encoding='utf-8') as f:
    items = json.load(f)

edu_badges = ['교육과정', '교육행정', '교수학습', '교육평가', '교육심리', '교육방법·학습', '교육심리·특수']

edu_list = []
counsel_list = []

for it in items:
    if it['badge'] in edu_badges:
        edu_list.append(it)
    else:
        counsel_list.append(it)

print(f"Total 교육학: {len(edu_list)}")
print(f"Total 전공상담: {len(counsel_list)}")

print("\n--- 교육학 항목 전체 (33개) ---")
for i, it in enumerate(edu_list):
    print(f"{i+1}. [{it['badge']}] {it['kw']}")

print("\n--- 전공상담 항목 처음 20개 ---")
for i, it in enumerate(counsel_list[:20]):
    print(f"{i+1}. [{it['badge']}] {it['kw']}")
