import sys
import json
import re

sys.stdout.reconfigure(encoding='utf-8')

new_ans_31 = "1. 호기심, 인내심, 융통성, 낙관성, 위험감수의 '계획된 우연'이다.\n2. 우연한 사건을 배움과 성장의 기회로 주체적으로 능동 창출한다.\n3. [상담 개입] 고정된 결정을 탈피하고 새로운 경험에 도전하게 한다.\n4. [상담 효과] 예기치 못한 우연을 배움의 기회로 바꿔 진로를 개척한다."

# 1. Update in new_203_items_curriculum2022.json
json_path = r'g:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\교육학\scratch\new_203_items_curriculum2022.json'
with open(json_path, 'r', encoding='utf-8') as f:
    items = json.load(f)

for it in items:
    if it['num'] == 31:
        it['ans'] = new_ans_31
        print("Updated Item 31 in new_203_items_curriculum2022.json")
        break

with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(items, f, ensure_ascii=False, indent=2)

# 2. Update in kice_55_core_compressed.html
comp_path = r'G:\내 드라이브\ANTI GRAVITY\전문상담임용고시\kice-300-wordbook\kice_55_core_compressed.html'
with open(comp_path, 'r', encoding='utf-8') as f:
    html = f.read()

m = re.search(r'items\s*=\s*(\[.*?\]);', html)
if m:
    comp_items = json.loads(m.group(1))
    for it in comp_items:
        if it['num'] == 31:
            it['ans'] = new_ans_31
            print("Updated Item 31 in comp_items list")
            break
    
    # replace items array
    new_items_json = json.dumps(comp_items, ensure_ascii=False)
    html = html[:m.start(1)] + new_items_json + html[m.end(1):]
    with open(comp_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print("Saved updated kice_55_core_compressed.html")

# 3. Rebuild kice_d54_phase1_wordbook.html
import subprocess
res = subprocess.run(["python", "scratch/build_phase1_wordbook.py"], capture_output=True, text=True, encoding='utf-8')
print("Rebuild script output:", res.stdout)
