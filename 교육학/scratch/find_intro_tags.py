# -*- coding: utf-8 -*-
with open(r"C:\Users\LENOVO\Desktop\삼국지_황제의결단_웹게임.html", "r", encoding="utf-8") as f:
    text = f.read()

import re
matches = re.findall(r'<img id="intro-face-[^"]+"[^>]*>', text)
for m in matches:
    print(m)
