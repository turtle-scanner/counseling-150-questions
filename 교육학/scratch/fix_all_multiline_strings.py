# -*- coding: utf-8 -*-
with open(r'C:/Users/LENOVO/Desktop/삼국지_황제의결단_웹게임.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re

# alert("...") 내부에 실제 개행이 있는 패턴을 백틱(`...`)으로 치환
def fix_multiline_string(match):
    s = match.group(0)
    # alert("...") 형식이면 alert(`...`)으로 치환
    if s.startswith('alert("') and s.endswith('");'):
        content = s[7:-3]
        return f'alert(`{content}`);'
    return s

text = re.sub(r'alert\("[\s\S]*?"\);', fix_multiline_string, text)

# 파일 저장 및 전역 동기화
with open(r'C:/Users/LENOVO/Desktop/삼국지_황제의결단_웹게임.html', 'w', encoding='utf-8') as f:
    f.write(text)

with open(r'C:/Users/LENOVO/Desktop/sam3_update.html', 'w', encoding='utf-8') as f:
    f.write(text)

with open(r'g:/내 드라이브/ANTI GRAVITY/시험준비(패턴)/교육학/samgukji.html', 'w', encoding='utf-8') as f:
    f.write(text)

with open(r'g:/내 드라이브/ANTI GRAVITY/시험준비(패턴)/samgukji.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("All multiline alerts fixed globally!")
