import sys
import re

with open(r'C:/Users/LENOVO/Desktop/삼국지_황제의결단_웹게임.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('canvas.addEventListener("click"')
if pos == -1:
    pos = text.find("battleCanvas.addEventListener")
if pos == -1:
    pos = text.find("canvas.onclick")
if pos == -1:
    pos = text.find("handleCanvasClick")

print('Click handler found at:', pos)
if pos != -1:
    sys.stdout.buffer.write(text[pos:pos+3000].encode('utf-8'))
