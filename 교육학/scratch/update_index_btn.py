# -*- coding: utf-8 -*-
import sys

p = r"G:\내 드라이브\ANTI GRAVITY\전문상담임용고시\kice-300-wordbook\index.html"
with open(p, "r", encoding="utf-8") as f:
    text = f.read()

target = '<button class="btn active" id="btnModeCard"'
replacement = '<button class="btn" style="background: linear-gradient(135deg, #f59e0b, #d97706); border-color: #fbbf24; color: #000; font-weight: 900; box-shadow: 0 0 12px rgba(245, 158, 11, 0.4);" onclick="window.open(\'exam_2027_kice_ab.html\', \'_blank\')">🏛️ [2027 실전 웹시험지] 전공 A·B형 풀세트 (암호: 371400)</button>\n      <button class="btn active" id="btnModeCard"'

if target in text:
    new_text = text.replace(target, replacement, 1)
    with open(p, "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Button successfully added to index.html!")
else:
    print("Target not found")
