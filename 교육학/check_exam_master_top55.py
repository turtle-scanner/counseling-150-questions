# -*- coding: utf-8 -*-

content = open('g:/내 드라이브/ANTI GRAVITY/시험준비(패턴)/exam_master_2027.html', encoding='utf-8').read()

# rawData 또는 top55 데이터 찾기
import re
print("exam_master_2027.html length:", len(content))
m = re.findall(r'top55Data\s*=|top55\s*=|rawData\.top55', content)
print("top55 occurrences:", m)

idx = content.find('top55')
if idx != -1:
    print(content[idx:idx+400])
