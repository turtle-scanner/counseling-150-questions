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

print('Items in 150/200 dataset:', len(items_150))
print('Keys in 150/200 dataset item 0:', list(items_150[0].keys()))
print('Items in 55 dataset:', len(items_55))
print('Keys in 55 dataset item 0:', list(items_55[0].keys()))

# Check if all keys match
keys_match = set(items_150[0].keys()) == set(items_55[0].keys())
print('Keys match exactly:', keys_match)
