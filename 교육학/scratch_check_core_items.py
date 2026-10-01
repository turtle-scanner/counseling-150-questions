import sys, json
sys.stdout.reconfigure(encoding='utf-8')

target_path = 'G:/내 드라이브/ANTI GRAVITY/전문상담임용고시/kice-300-wordbook/index.html'

with open(target_path, 'r', encoding='utf-8') as f:
    text = f.read()

pos_start = text.find('const allData = [')
pos_end = text.find('];', pos_start) + 1
data_str = text[pos_start + len('const allData = '):pos_end]
all_data = json.loads(data_str)

core_items = [item for item in all_data if item.get('isCore150')]
print('Total core_items count:', len(core_items))

# Check domains distribution
from collections import Counter
domains = Counter(item['domain'] for item in core_items)
print('Core items domains distribution:')
for d, c in domains.most_common():
    print(f' - {d}: {c}')
