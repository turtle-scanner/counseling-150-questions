# -*- coding: utf-8 -*-
with open(r"C:\Users\LENOVO\Desktop\삼국지_황제의결단_웹게임.html", "r", encoding="utf-8") as f:
    text = f.read()

# Find PORTRAITS
p_idx = text.find("const PORTRAITS =")
print("p_idx:", p_idx)
if p_idx != -1:
    print("PORTRAITS snippet:", text[p_idx:p_idx+150])

# Find setupIntroFaces
s_idx = text.find("function setupIntroFaces()")
print("s_idx:", s_idx)

# Find where setupIntroFaces is called
c_idx = text.find("setupIntroFaces();")
print("c_idx:", c_idx)
