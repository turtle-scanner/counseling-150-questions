# -*- coding: utf-8 -*-
with open(r"C:\Users\LENOVO\Desktop\삼국지_황제의결단_웹게임.html", "r", encoding="utf-8") as f:
    text = f.read()

# Find all occurrences of DOMContentLoaded
import re
for m in re.finditer(r"DOMContentLoaded", text):
    start = max(0, m.start() - 50)
    end = min(len(text), m.end() + 250)
    print("--- DOMContentLoaded at", m.start(), "---")
    print(text[start:end])
