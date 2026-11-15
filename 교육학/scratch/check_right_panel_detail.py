# -*- coding: utf-8 -*-
with open(r'C:\Users\LENOVO\Desktop\삼국지_황제의결단_웹게임.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
m = re.search(r'id="hexBattleModal"[\s\S]*?(?=id="duelModal"|id="unification-modal")', text)
if m:
    section = m.group(0)
    print("Found hexBattleModal! Length:", len(section))
    # 우측 사이드 패널 부분 찾기
    side_m = re.search(r'<div class="w-72[\s\S]*?</div>\s*</div>\s*</div>\s*</div>', section)
    if side_m:
        print("Side panel found:")
        print(side_m.group(0)[:2500])
    else:
        print("Could not find side panel exactly, printing first 1500 chars of section:")
        print(section[:1500])
