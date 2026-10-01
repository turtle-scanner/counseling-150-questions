import sys
sys.stdout.reconfigure(encoding='utf-8')

target_path = 'G:/내 드라이브/ANTI GRAVITY/전문상담임용고시/kice-300-wordbook/index.html'

with open(target_path, 'r', encoding='utf-8') as f:
    text = f.read()

pos_exam = text.find('id="examView"')
pos_exam_end = text.find('</div>\n\n  </main>', pos_exam)
if pos_exam_end == -1:
    pos_exam_end = text.find('</main>', pos_exam)

print('Exact examView block in index.html:')
print(repr(text[pos_exam-20:pos_exam_end+10]))
