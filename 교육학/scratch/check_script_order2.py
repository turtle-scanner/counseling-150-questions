# -*- coding: utf-8 -*-
with open(r"C:\Users\LENOVO\Desktop\삼국지_황제의결단_웹게임.html", "r", encoding="utf-8") as f:
    text = f.read()

dom_idx = text.find("setupIntroFaces();")
out = text[dom_idx-100:dom_idx+400]
with open("scratch/dom_out.txt", "w", encoding="utf-8") as f:
    f.write(out)

print("Saved dom_out.txt")
