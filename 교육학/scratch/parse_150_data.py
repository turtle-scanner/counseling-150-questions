import json
import re

with open(r'G:\내 드라이브\ANTI GRAVITY\전문상담임용고시\kice-300-wordbook\kice_150_core_table_a4.html', 'r', encoding='utf-8') as f:
    text = f.read()

# find DATA = [ ... ];
start = text.find('DATA = [')
if start != -1:
    start += len('DATA = ')
    # find ending bracket
    end = text.find('];', start) + 1
    data_json = text[start:end]
    items = json.loads(data_json)
    print(f'Successfully parsed DATA with {len(items)} items!')
    print('Sample 1:', items[0]['num'], items[0]['badge'], items[0]['kw'])
    print('Sample 50:', items[49]['num'], items[49]['badge'], items[49]['kw'])
    print('Sample 100:', items[99]['num'], items[99]['badge'], items[99]['kw'])
    print('Sample 150:', items[149]['num'], items[149]['badge'], items[149]['kw'])
    print('Sample 200:', items[199]['num'], items[199]['badge'], items[199]['kw'])
else:
    print('DATA = [ not found')
