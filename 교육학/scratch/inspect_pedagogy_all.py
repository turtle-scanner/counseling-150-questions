import json, os, sys
sys.stdout.reconfigure(encoding='utf-8')

script_dir = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(script_dir, 'new_203_items_curriculum2022.json')

with open(json_path, 'r', encoding='utf-8') as f:
    items = json.load(f)

print("--- Items 1-16 (교육과정) ---")
for idx in range(16):
    print(f"{idx+1}: ({items[idx]['badge']}) {items[idx]['kw']}")

print("\n--- Items 152-166 & 202-203 (교육학) ---")
for idx in list(range(151, 166)) + [201, 202]:
    print(f"{idx+1}: ({items[idx]['badge']}) {items[idx]['kw']}")
