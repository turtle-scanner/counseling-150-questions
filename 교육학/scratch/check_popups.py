# -*- coding: utf-8 -*-
with open(r"C:\Users\LENOVO\Desktop\삼국지_황제의결단_웹게임.html", "r", encoding="utf-8") as f:
    text = f.read()

# Let's inspect togglePopup
p_idx = text.find("function togglePopup")
print("togglePopup definition:")
print(text[p_idx:p_idx+300])

# Let's inspect closeAllPopups
c_idx = text.find("function closeAllPopups")
print("closeAllPopups definition:")
print(text[c_idx:c_idx+300])
