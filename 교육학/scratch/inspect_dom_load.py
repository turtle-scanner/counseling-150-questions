# -*- coding: utf-8 -*-
with open(r"C:\Users\LENOVO\Desktop\삼국지_황제의결단_웹게임.html", "r", encoding="utf-8") as f:
    text = f.read()

# Let's inspect DOMContentLoaded
idx = text.find("window.addEventListener('DOMContentLoaded', () => {")
print("DOMContentLoaded found at:", idx)
print(text[idx:idx+350])
