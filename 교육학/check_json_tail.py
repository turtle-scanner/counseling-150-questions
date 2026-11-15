# -*- coding: utf-8 -*-
with open('g:/내 드라이브/ANTI GRAVITY/전문상담임용고시/exam_master_2027.html', 'r', encoding='utf-8') as f:
    content = f.read()

idx = content.find('const rawData =')
end_idx = content.find('let currentTab', idx)

json_str = content[idx+len('const rawData ='):end_idx].strip()
print("Total length of json_str:", len(json_str))
print("Chars around 47076:")
print(repr(json_str[47060:47090]))
