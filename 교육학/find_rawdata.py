# -*- coding: utf-8 -*-

content = open('g:/내 드라이브/ANTI GRAVITY/시험준비(패턴)/exam_master_2027.html', encoding='utf-8').read()

import re
matches = [m.start() for m in re.finditer(r'top55\s*:\s*\[|const rawData', content)]
print("Matches for top55: [ or const rawData:", matches)
for idx in matches:
    print(content[idx:idx+300])
    print("="*40)
