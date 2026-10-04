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

with open('scratch/diff_out.txt', 'w', encoding='utf-8') as out:
    for m in items_55[:2]:
        out.write(f"55 item {m['num']}: {m['kw']}\n")
    for m in items_150[:5]:
        out.write(f"150 item {m['num']}: {m['kw']}\n")
