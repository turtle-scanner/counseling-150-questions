import sys, json
sys.stdout.reconfigure(encoding='utf-8')

target_path = 'G:/내 드라이브/ANTI GRAVITY/전문상담임용고시/kice-300-wordbook/index.html'

with open(target_path, 'r', encoding='utf-8') as f:
    text = f.read()

pos_start = text.find('const allData = [')
pos_end = text.find('];', pos_start) + 1
data_str = text[pos_start + len('const allData = '):pos_end]
all_data = json.loads(data_str)

print('Total all_data items:', len(all_data))
for p in ['1교시 교육학', '2교시 전공 A형', '3교시 전공 B형']:
    p_items = [it for it in all_data if it['period'] == p]
    from collections import Counter
    c = Counter(it['domain'] for it in p_items)
    print(f'=== {p} (총 {len(p_items)}개) ===')
    for dom, cnt in c.items():
        print(f'  - {dom}: {cnt}')
