import sys

with open(r'C:/Users/LENOVO/Desktop/삼국지_황제의결단_웹게임.html', 'r', encoding='utf-8') as f:
    text = f.read()

pos_grid = text.find('const GRID_COLS =')
print('GRID_COLS pos:', pos_grid)
if pos_grid != -1:
    sys.stdout.buffer.write(text[pos_grid:pos_grid+1000].encode('utf-8'))
