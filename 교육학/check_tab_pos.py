# -*- coding: utf-8 -*-
with open('g:/내 드라이브/ANTI GRAVITY/전문상담임용고시/exam_master_2027.html', 'r', encoding='utf-8') as f:
    content = f.read()

idx = content.find('const rawData =')
end_idx = content.find('let currentTab', idx)
print("Distance between 'const rawData =' and 'let currentTab':", end_idx - idx)
snippet = content[end_idx-50:end_idx+50]
print("Snippet around 'let currentTab':")
print(snippet)
