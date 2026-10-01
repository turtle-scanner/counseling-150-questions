import sys, re
sys.stdout.reconfigure(encoding='utf-8')

target_path = 'G:/내 드라이브/ANTI GRAVITY/전문상담임용고시/kice-300-wordbook/index.html'

with open(target_path, 'r', encoding='utf-8') as f:
    text = f.read()

pos_exam_texts = text.find('const examTexts =')
pos_exam_end = text.find('];', pos_exam_texts)

# Find all backtick strings or items in examTexts
items = re.findall(r'`([\s\S]*?)`', text[pos_exam_texts:pos_exam_end+2])
print('examTexts count:', len(items))
for i, item in enumerate(items):
    lines = item.strip().split('\n')
    print(f'Exam {i}: length {len(item)} chars, first line: {lines[0] if lines else ""}')
