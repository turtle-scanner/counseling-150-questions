# -*- coding: utf-8 -*-
with open(r'C:\Users\LENOVO\Desktop\삼국지_황제의결단_웹게임.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
m = re.search(r'function [a-zA-Z0-9_]*DuelSelectModal\b[\s\S]*?(?=function [a-zA-Z0-9_]+\()', text)
if m:
    with open(r'g:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\교육학\scratch\duel_modal_fn.txt', 'w', encoding='utf-8') as out:
        out.write(m.group(0))
    print('Found!')
else:
    print('Not found by regex, searching startDuelFight...')
    m2 = re.search(r'function startDuelFight\b[\s\S]*?(?=function [a-zA-Z0-9_]+\()', text)
    if m2:
        with open(r'g:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\교육학\scratch\duel_modal_fn.txt', 'w', encoding='utf-8') as out:
            out.write(m2.group(0))
        print('Found startDuelFight!')
