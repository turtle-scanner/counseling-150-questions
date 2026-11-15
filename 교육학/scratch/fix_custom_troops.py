with open(r'C:\Users\LENOVO\Desktop\삼국지_황제의결단_웹게임.html', 'r', encoding='utf-8') as f:
    text = f.read()

target = 'const userSet = customTroopSettings[off.id] || {};'
replacement = 'const userSet = (typeof customTroopSettings !== "undefined" && customTroopSettings[off.id]) ? customTroopSettings[off.id] : {};'

if target in text:
    text = text.replace(target, replacement, 1)
    with open(r'C:\Users\LENOVO\Desktop\삼국지_황제의결단_웹게임.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print('SUCCESS: Made customTroopSettings safe')
else:
    print('Target not found')
