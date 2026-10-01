import sys
sys.stdout.reconfigure(encoding='utf-8')

target_path = 'G:/내 드라이브/ANTI GRAVITY/전문상담임용고시/kice-300-wordbook/index.html'

with open(target_path, 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Add state variables near currentMode
old_vars = "let currentMode = 'card';"
new_vars = """let currentMode = 'card';
    let currentExamPeriod = 'all';
    let currentExamRound = 4;
    let isRawExamOpen = false;"""

text = text.replace(old_vars, new_vars, 1)

# 2. Remove duplicate declarations lower down
old_dupe = """    let currentExamPeriod = 'all';
    let currentExamRound = 4;
    let isRawExamOpen = false;"""

# Replace only the second occurrence (the one in the new functions section)
pos_dupe = text.rfind(old_dupe)
if pos_dupe != -1:
    text = text[:pos_dupe] + "// Exam state variables initialized above" + text[pos_dupe + len(old_dupe):]

with open(target_path, 'w', encoding='utf-8') as f:
    f.write(text)

print('Moved exam state variables to top of script.')
