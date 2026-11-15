# -*- coding: utf-8 -*-
with open(r"C:\Users\LENOVO\Desktop\삼국지_황제의결단_웹게임.html", "r", encoding="utf-8") as f:
    text = f.read()

# Let's inspect DOMContentLoaded block
idx = text.find("window.addEventListener('DOMContentLoaded', () => {")
print("DOMContentLoaded block:")
print(text[idx:idx+600])

# Let's inspect changeRuler function definition
c_idx = text.find("function changeRuler(")
print("\nchangeRuler definition:")
print(text[c_idx:c_idx+350])
