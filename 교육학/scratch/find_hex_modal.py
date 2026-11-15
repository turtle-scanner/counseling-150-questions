# -*- coding: utf-8 -*-
with open(r'C:\Users\LENOVO\Desktop\삼국지_황제의결단_웹게임.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
m = re.search(r'id=["\']hex-battle-modal["\'][\s\S]{0,1200}', text)
if m:
    print(m.group(0))
