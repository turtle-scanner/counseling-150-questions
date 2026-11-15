import sys
import re

with open(r'C:/Users/LENOVO/Desktop/삼국지_황제의결단_웹게임.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('function executeSkillAction')
if pos != -1:
    chunk = text[pos:pos+3500]
    sys.stdout.buffer.write(chunk.encode('utf-8'))
    sys.stdout.buffer.write(b'\n' + b'='*50 + b'\n')
