import json

with open(r'G:\내 드라이브\ANTI GRAVITY\전문상담임용고시\kice-300-wordbook\kice_150_core_table_a4.html', 'r', encoding='utf-8') as f:
    text = f.read()
start = text.find('DATA = [') + len('DATA = ')
end = text.find('];', start) + 1
items_150 = json.loads(text[start:end])

with open(r'G:\내 드라이브\ANTI GRAVITY\전문상담임용고시\kice-300-wordbook\kice_55_core_compressed.html', 'r', encoding='utf-8') as f:
    text55 = f.read()
start55 = text55.find('let items = [') + len('let items = ')
end55 = text55.find('];', start55) + 1
items_55 = json.loads(text55[start55:end55])

kws_150 = set(i['kw'].strip() for i in items_150)
missing_from_150 = [i for i in items_55 if i['kw'].strip() not in kws_150]
print(f'Total items in 150 dataset: {len(items_150)}')
print(f'Total items in 55 dataset: {len(items_55)}')
print(f'Items in 55 dataset not in 150 dataset: {len(missing_from_150)}')
if missing_from_150:
    for m in missing_from_150:
        print('  Missing:', m['num'], m['kw'])
