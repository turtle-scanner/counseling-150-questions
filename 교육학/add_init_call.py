import sys
sys.stdout.reconfigure(encoding='utf-8')

target_path = 'G:/내 드라이브/ANTI GRAVITY/전문상담임용고시/kice-300-wordbook/index.html'

with open(target_path, 'r', encoding='utf-8') as f:
    text = f.read()

pos = text.find('applyFilter();\n  \n    // ===')
if pos == -1:
    pos = text.find('applyFilter();')
    print('Context around applyFilter:')
    print(text[pos:pos+300])

text = text.replace(
    "applyFilter();\n  \n    // ===",
    "applyFilter();\n    renderInteractiveExam();\n  \n    // ==="
)

with open(target_path, 'w', encoding='utf-8') as f:
    f.write(text)

print('Added renderInteractiveExam() to initial load.')
