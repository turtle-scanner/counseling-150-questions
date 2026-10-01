import sys, json, re
sys.stdout.reconfigure(encoding='utf-8')

print('Executing full injection script...')

target_path = 'G:/내 드라이브/ANTI GRAVITY/전문상담임용고시/kice-300-wordbook/index.html'

with open(target_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Load exam questions JSON
with open('scratch_exam_questions04.json', 'r', encoding='utf-8') as f:
    exam_questions_json = f.read()

# 2. Add isCore150 to allData
# Let's extract allData, parse it, set isCore150 on the 150 items
pos_start = html.find('const allData = [')
pos_end = html.find('];', pos_start) + 1
data_str = html[pos_start + len('const allData = '):pos_end]
all_data = json.loads(data_str)

# Select exactly 150 items
# All 55 freeze keywords matching items + up to 38 pedagogy, up to 72 major A, up to 40 major B = 150 items
pos_fk = html.find('const freezeKeywords =')
pos_fk_end = html.find('];', pos_fk) + 1
fk_str = html[pos_fk + len('const freezeKeywords = '):pos_fk_end]
freeze_keywords = json.loads(fk_str)

core_ids = set()
for item in all_data:
    txt = item['keywords'] + ' ' + item['question'] + ' ' + item['domain']
    if any(k in txt for k in freeze_keywords):
        core_ids.add(item['id'])

for item in all_data:
    if len(core_ids) >= 150:
        break
    if item['period'].startswith('1교시') and item['id'] <= 38:
        core_ids.add(item['id'])

for item in all_data:
    if len(core_ids) >= 150:
        break
    if '전공 A' in item['period']:
        core_ids.add(item['id'])

for item in all_data:
    if len(core_ids) >= 150:
        break
    if '전공 B' in item['period']:
        core_ids.add(item['id'])

print(f'Selected core_ids count: {len(core_ids)}')
assert len(core_ids) == 150

for item in all_data:
    item['isCore150'] = (item['id'] in core_ids)

updated_all_data_str = json.dumps(all_data, ensure_ascii=False)

# Replace allData in html
html = html[:pos_start + len('const allData = ')] + updated_all_data_str + html[pos_end:]
print('Updated allData with isCore150.')

# 3. Add examQuestions04 data in JavaScript
pos_exam_texts = html.find('const examTexts =')
injection_code = f"""
    // ============================================================
    // 2027 KICE 실전 모의고사 0906_04회 24문항 인터랙티브 데이터
    // ============================================================
    const examQuestions04 = {exam_questions_json};
"""
html = html[:pos_exam_texts] + injection_code + html[pos_exam_texts:]
print('Injected examQuestions04 array.')

# Save progress check
with open('test_progress_html.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Progress saved, size:', len(html))
