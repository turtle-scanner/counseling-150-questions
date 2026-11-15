# -*- coding: utf-8 -*-
with open(r"C:\Users\LENOVO\Desktop\삼국지_황제의결단_웹게임.html", "r", encoding="utf-8") as f:
    text = f.read()

# Check setupIntroFaces definition and where it is in relation to PORTRAITS
s_idx = text.find("function setupIntroFaces()")
print("setupIntroFaces definition snippet:")
print(text[s_idx:s_idx+400])

# Check what happens in DOMContentLoaded:
dom_idx = text.find("setupIntroFaces();")
print("DOMContentLoaded snippet:")
print(text[dom_idx-100:dom_idx+300])
