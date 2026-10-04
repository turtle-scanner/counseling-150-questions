import json

with open(r'G:\내 드라이브\ANTI GRAVITY\전문상담임용고시\kice-300-wordbook\kice_150_core_table_a4.html', 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('DATA = [') + len('DATA = ')
end = text.find('];', start) + 1
items = json.loads(text[start:end])

with open('scratch/items_1_to_10.json', 'w', encoding='utf-8') as out:
    json.dump(items[:10], out, ensure_ascii=False, indent=2)

print('Dumped items 1 to 10.')
