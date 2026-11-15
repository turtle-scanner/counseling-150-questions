# -*- coding: utf-8 -*-
with open(r'C:\Users\LENOVO\Desktop\삼국지_황제의결단_웹게임.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
m = re.search(r'id="battleCanvas"[\s\S]{0,4000}', text)
if m:
    with open(r'g:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\교육학\scratch\canvas_output.txt', 'w', encoding='utf-8') as out:
        out.write(m.group(0))
    print("Written canvas output!")
