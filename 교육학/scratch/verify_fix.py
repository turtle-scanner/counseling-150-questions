# -*- coding: utf-8 -*-
with open(r"C:\Users\LENOVO\Desktop\삼국지_황제의결단_웹게임.html", "r", encoding="utf-8") as f:
    text = f.read()

checks = {
    "map-pins-layer": 'id="map-pins-layer"' in text,
    "popup-military": 'id="popup-military"' in text,
    "closeModal safe": 'function closeModal(id) {\n      const el = document.getElementById(id);' in text,
    "DOMContentLoaded": 'renderMapPins();' in text,
}

for k, v in checks.items():
    print(k, v)
