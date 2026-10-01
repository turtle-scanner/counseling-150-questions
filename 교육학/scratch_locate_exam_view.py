import sys, json, re
sys.stdout.reconfigure(encoding='utf-8')

target_path = 'G:/내 드라이브/ANTI GRAVITY/전문상담임용고시/kice-300-wordbook/index.html'

with open(target_path, 'r', encoding='utf-8') as f:
    text = f.read()

print('Current index.html length:', len(text))

# Locate the exact boundaries of examView
pos_exam_start = text.find('<div id="examView"')
assert pos_exam_start != -1, "examView not found"

# Find end of this div
pos_main_end = text.find('</main>', pos_exam_start)
# Backtrack to the </div> right before </main>
pos_exam_end = text.rfind('</div>', pos_exam_start, pos_main_end) + len('</div>')

print('examView range:', pos_exam_start, 'to', pos_exam_end)
print('Current examView preview:', text[pos_exam_start:pos_exam_start+200])
