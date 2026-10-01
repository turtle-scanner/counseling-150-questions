import sys, json
sys.stdout.reconfigure(encoding='utf-8')

target_path = 'G:/내 드라이브/ANTI GRAVITY/전문상담임용고시/kice-300-wordbook/index.html'

with open(target_path, 'r', encoding='utf-8') as f:
    text = f.read()

pos_start = text.find('const allData = [')
pos_end = text.find('];', pos_start) + 1
data_str = text[pos_start + len('const allData = '):pos_end]
data = json.loads(data_str)

# Find freezeKeywords in index.html
pos_fk = text.find('const freezeKeywords =')
pos_fk_end = text.find('];', pos_fk) + 1
fk_str = text[pos_fk + len('const freezeKeywords = '):pos_fk_end]
freeze_keywords = json.loads(fk_str)

print('Freeze keywords count:', len(freeze_keywords))

# Select 150 items:
# 1) all items matching freeze_keywords
# 2) fill up to 150 with highest yield items from pedagogy (up to 25), major A (up to 65), major B (up to 60)
core_ids = set()
for item in data:
    txt = item['keywords'] + ' ' + item['question'] + ' ' + item['domain']
    if any(k in txt for k in freeze_keywords):
        core_ids.add(item['id'])

print('Items matching freeze_keywords:', len(core_ids))

# Fill up to 150
# Add pedagogy items (id 1..30)
for item in data:
    if len(core_ids) >= 150:
        break
    if item['period'].startswith('1교시') and item['id'] <= 35:
        core_ids.add(item['id'])

# Add Major A items
for item in data:
    if len(core_ids) >= 150:
        break
    if '전공 A' in item['period']:
        core_ids.add(item['id'])

# Add Major B items
for item in data:
    if len(core_ids) >= 150:
        break
    if '전공 B' in item['period']:
        core_ids.add(item['id'])

print('Final core_ids count:', len(core_ids))
ped_count = sum(1 for item in data if item['id'] in core_ids and '1교시' in item['period'])
a_count = sum(1 for item in data if item['id'] in core_ids and '전공 A' in item['period'])
b_count = sum(1 for item in data if item['id'] in core_ids and '전공 B' in item['period'])
print(f'Distribution: 교육학 {ped_count}개, 전공 A {a_count}개, 전공 B {b_count}개 = 총 {ped_count+a_count+b_count}개')
