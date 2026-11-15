with open(r'C:\Users\LENOVO\Desktop\삼국지_황제의결단_웹게임.html', 'r', encoding='utf-8') as f:
    text = f.read()

with open(r'g:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\교육학\scratch\apply_duel_random_and_fatigue.js', 'r', encoding='utf-8') as f:
    js_code = f.read()

# js_code에서 duelSelectionJs 부분 추출
start_tag = 'const duelSelectionJs = `'
end_tag = '`;'
idx1 = js_code.find(start_tag) + len(start_tag)
idx2 = js_code.find(end_tag, idx1)
duel_js = js_code[idx1:idx2]

target = 'function openModal(id) {'
if target in text and 'function openDuelSelectModal()' not in text:
    text = text.replace(target, duel_js + '\n    ' + target, 1)
    with open(r'C:\Users\LENOVO\Desktop\삼국지_황제의결단_웹게임.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print('SUCCESS: Injected openDuelSelectModal above openModal(id)!')
else:
    print('Already present or target not found')
