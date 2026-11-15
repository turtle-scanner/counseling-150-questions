import sys

with open(r'C:/Users/LENOVO/Desktop/삼국지_황제의결단_웹게임.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos_state = text.find('const gameState = {')
print('gameState pos:', pos_state)
if pos_state != -1:
    sys.stdout.buffer.write(text[pos_state:pos_state+1200].encode('utf-8'))
