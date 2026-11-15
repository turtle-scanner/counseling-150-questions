import sys

with open(r'C:/Users/LENOVO/Desktop/삼국지_황제의결단_웹게임.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find("openModal('unification-ending-modal')")
if pos != -1:
    sys.stdout.buffer.write(text[pos-1000:pos].encode('utf-8'))
