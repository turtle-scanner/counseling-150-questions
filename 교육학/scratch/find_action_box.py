import sys

with open(r'C:/Users/LENOVO/Desktop/삼국지_황제의결단_웹게임.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('이달의 전략')
while pos != -1:
    print('Found at:', pos)
    sys.stdout.buffer.write(text[pos-50:pos+300].encode('utf-8') + b'\n---\n')
    pos = text.find('이달의 전략', pos + 1)
