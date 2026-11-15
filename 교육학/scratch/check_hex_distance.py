import sys

with open(r'C:/Users/LENOVO/Desktop/삼국지_황제의결단_웹게임.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('function getHexDistance')
print('getHexDistance pos:', pos)
if pos != -1:
    sys.stdout.buffer.write(text[pos:pos+1000].encode('utf-8'))
