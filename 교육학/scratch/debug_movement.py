import sys

with open(r'C:/Users/LENOVO/Desktop/삼국지_황제의결단_웹게임.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. computeMovementRange 함수 확인
pos_move = text.find('function computeMovementRange')
pos_end_move = text.find('function updateUnitDetailCard', pos_move)
print("=== computeMovementRange ===")
sys.stdout.buffer.write(text[pos_move:pos_end_move].encode('utf-8'))

# 2. handleHexClick 함수 확인
pos_click = text.find('function handleHexClick')
pos_end_click = text.find('function selectUnit', pos_click)
print("\n=== handleHexClick ===")
sys.stdout.buffer.write(text[pos_click:pos_end_click].encode('utf-8'))

# 3. selectUnit 함수 확인
pos_select = text.find('function selectUnit')
pos_end_select = text.find('function deselectUnit', pos_select)
print("\n=== selectUnit ===")
sys.stdout.buffer.write(text[pos_select:pos_end_select].encode('utf-8'))
