# -*- coding: utf-8 -*-
with open(r"C:\Users\LENOVO\Desktop\삼국지_황제의결단_웹게임.html", "r", encoding="utf-8") as f:
    text = f.read()

u_idx = text.find("function updateRightPanel(provId)")
with open("scratch/updateRightPanel.txt", "w", encoding="utf-8") as f:
    f.write(text[u_idx:u_idx+2000])

print("Saved updateRightPanel.txt")
