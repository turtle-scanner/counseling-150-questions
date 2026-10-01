import sys, json, re
sys.stdout.reconfigure(encoding='utf-8')

target_path = 'G:/내 드라이브/ANTI GRAVITY/전문상담임용고시/kice-300-wordbook/index.html'

with open(target_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Extract allData
pos_start = text.find('const allData = [')
pos_end = text.find('];', pos_start) + 1
data_str = text[pos_start + len('const allData = '):pos_end]

data = json.loads(data_str)
print('Total items in allData:', len(data))

from collections import Counter
periods = Counter(item.get('period') for item in data)
print('Periods count:', periods)

domains = Counter(item.get('domain') for item in data)
print('Domains count:', domains)

# Inspect examView and examTexts
pos_exam = text.find('id="examView"')
print('examView found at:', pos_exam)
pos_exam_texts = text.find('const examTexts =')
if pos_exam_texts != -1:
    print('examTexts found at:', pos_exam_texts)
    pos_exam_texts_end = text.find('};', pos_exam_texts)
    print('examTexts preview:', text[pos_exam_texts:pos_exam_texts+400])
else:
    print('examTexts not found directly')
