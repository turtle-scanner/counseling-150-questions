# -*- coding: utf-8 -*-
with open(r"C:\Users\LENOVO\Desktop\삼국지_황제의결단_웹게임.html", "r", encoding="utf-8") as f:
    text = f.read()

# Inspect renderMapPins
r_idx = text.find("function renderMapPins()")
with open("scratch/renderMapPins.txt", "w", encoding="utf-8") as f:
    f.write(text[r_idx:r_idx+1500])

print("Saved renderMapPins.txt")
