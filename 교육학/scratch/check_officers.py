import sys

with open(r'C:/Users/LENOVO/Desktop/삼국지_황제의결단_웹게임.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos_my = text.find('const MY_OFFICERS = [')
pos_enemy = text.find('const ENEMY_OFFICERS_BY_RULER = {')

print('MY_OFFICERS found at:', pos_my)
print('ENEMY_OFFICERS_BY_RULER found at:', pos_enemy)

if pos_my != -1:
    sys.stdout.buffer.write(text[pos_my:pos_my+1500].encode('utf-8'))
