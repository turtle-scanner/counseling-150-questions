import sys

with open(r'C:/Users/LENOVO/Desktop/삼국지_황제의결단_웹게임.html', 'r', encoding='utf-8') as f:
    text = f.read()

# updateActionCommands 함수 확인
pos = text.find('function updateActionCommands()')
print('updateActionCommands pos:', pos)
if pos != -1:
    sys.stdout.buffer.write(text[pos:pos+2500].encode('utf-8'))
