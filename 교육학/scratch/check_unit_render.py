import sys

with open(r'C:/Users/LENOVO/Desktop/삼국지_황제의결단_웹게임.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('// 2. 부대 렌더링')
print('부대 렌더링 pos:', pos)
if pos != -1:
    sys.stdout.buffer.write(text[pos:pos+2500].encode('utf-8'))
