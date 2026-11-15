import sys

with open(r'C:/Users/LENOVO/Desktop/삼국지_황제의결단_웹게임.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('보병 (기본)')
if pos != -1:
    sys.stdout.buffer.write(text[pos-600:pos].encode('utf-8'))
