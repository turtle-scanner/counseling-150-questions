import sys

with open(r'C:/Users/LENOVO/Desktop/삼국지_황제의결단_웹게임.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('const formObj = FORMATIONS[unit.formation];')
print('formObj pos:', pos)
if pos != -1:
    sys.stdout.buffer.write(text[pos-200:pos+300].encode('utf-8'))
