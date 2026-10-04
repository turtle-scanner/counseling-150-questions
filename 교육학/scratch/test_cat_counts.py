import sys
import json
import re

sys.stdout.reconfigure(encoding='utf-8')

with open(r'G:\내 드라이브\ANTI GRAVITY\전문상담임용고시\kice-300-wordbook\kice_55_core_compressed.html', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'items\s*=\s*(\[.*?\]);', text)
items = json.loads(m.group(1))

categories = ['교육', '진로', '심리검사', '가족', '정신병리', '이론', '위기']
for cat in categories:
    matched = []
    for item in items:
        badge = item.get('badge', '')
        kw = item.get('kw', '')
        cond = False
        if cat == '교육': cond = ('교육' in badge or '교수' in badge)
        elif cat == '진로': cond = ('진로' in badge)
        elif cat == '심리검사': cond = ('검사' in badge)
        elif cat == '가족': cond = ('가족' in badge)
        elif cat == '정신병리': cond = ('병리' in badge or '이상' in badge or '장애' in kw)
        elif cat == '이론': cond = ('이론' in badge or '행동' in badge or '성격' in badge or '대인' in badge or '다문화' in badge)
        elif cat == '위기': cond = ('위기' in badge or '법령' in badge or '윤리' in badge or '놀이' in badge or '수퍼비전' in badge)
        if cond:
            matched.append(item['kw'])
    print(f"Category: {cat} --> Count: {len(matched)}")
