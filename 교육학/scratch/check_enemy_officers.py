import sys

with open(r'C:/Users/LENOVO/Desktop/삼국지_황제의결단_웹게임.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos_enemy = text.find('const ENEMY_OFFICERS_BY_RULER = {')
end_enemy = text.find('};', pos_enemy)
chunk = text[pos_enemy:end_enemy+2]
sys.stdout.buffer.write(chunk.encode('utf-8'))
