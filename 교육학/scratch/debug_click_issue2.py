# -*- coding: utf-8 -*-
with open(r"C:\Users\LENOVO\Desktop\삼국지_황제의결단_웹게임.html", "r", encoding="utf-8") as f:
    text = f.read()

idx = text.find("window.addEventListener('DOMContentLoaded', () => {")
c_idx = text.find("function changeRuler(")

with open("scratch/debug_out.txt", "w", encoding="utf-8") as f:
    f.write("=== DOMContentLoaded ===\n")
    f.write(text[idx:idx+600])
    f.write("\n\n=== changeRuler ===\n")
    f.write(text[c_idx:c_idx+350])

print("Saved debug_out.txt")
