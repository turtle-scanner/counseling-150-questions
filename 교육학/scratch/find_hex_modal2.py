# -*- coding: utf-8 -*-
with open(r'C:\Users\LENOVO\Desktop\삼국지_황제의결단_웹게임.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
m = re.search(r'id=["\']hex-battle-modal["\'][\s\S]{0,1500}', text)
if m:
    with open(r'g:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\교육학\scratch\hex_modal_dump.txt', 'w', encoding='utf-8') as out:
        out.write(m.group(0))
    print('Dumped successfully!')
