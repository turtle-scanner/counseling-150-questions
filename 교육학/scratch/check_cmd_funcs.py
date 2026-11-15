import sys

with open(r'C:/Users/LENOVO/Desktop/삼국지_황제의결단_웹게임.html', 'r', encoding='utf-8') as f:
    text = f.read()

funcs = ['onCmdAttack', 'onCmdArchery', 'onCmdFire', 'onCmdChaos', 'onCmdFlurry', 'onCmdFormation', 'onCmdDuel', 'onCmdWait']
for fn in funcs:
    print(fn, 'in text:', fn in text)
