# -*- coding: utf-8 -*-
import sys, io, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='backslashreplace')

html = open(r'C:\Users\LENOVO\Desktop\sam3_update.html', 'r', encoding='utf-8', errors='ignore').read()

# search for duel victory text and duelModal closing logic
for kw in ['대승 및 적장', '포로 생포', '사로잡았습니다', 'progressDuelRound', 'closeDuelModal', 'duel-modal', 'duelAction']:
    print(f'=== {kw} ===')
    for m in re.finditer(re.escape(kw), html):
        p = m.start()
        print(f'At {p}:', html[max(0, p-100):min(len(html), p+400)].replace('\n', ' '))
