import json

with open(r'G:\내 드라이브\ANTI GRAVITY\전문상담임용고시\kice-300-wordbook\kice_55_core_compressed.html', 'r', encoding='utf-8') as f:
    text = f.read()

start = text.find('let items = [') + len('let items = ')
end = text.find('];', start) + 1
items = json.loads(text[start:end])

print(f'Total items: {len(items)}')

with open('scratch/answers_sample.txt', 'w', encoding='utf-8') as out:
    for idx in [0, 1, 2, 5, 10, 20, 50, 80, 120, 160, 200]:
        if idx < len(items):
            it = items[idx]
            out.write(f"=== Item {it['num']}: {it['kw']} ===\n")
            out.write(f"Q: {it['q']}\n")
            out.write(f"ANS: {it['ans']}\n\n")

print('Dumped samples to scratch/answers_sample.txt')
