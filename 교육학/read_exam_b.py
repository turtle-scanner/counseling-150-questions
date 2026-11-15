import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('exam_2027_kice_ab.html', 'r', encoding='utf-8') as f:
    text = f.read()

for qid in ['B8', 'B9', 'B10', 'B11']:
    pos = text.find(f'"id": "{qid}"')
    print(f'=== {qid} ===')
    if pos != -1:
        end = text.find('}, {', pos)
        if end == -1:
            end = text.find('}];', pos)
        print(text[pos-1:end+1])
    else:
        print('Not found')
