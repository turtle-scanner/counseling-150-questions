import sys
sys.stdout.reconfigure(encoding='utf-8')

target_path = 'G:/내 드라이브/ANTI GRAVITY/전문상담임용고시/kice-300-wordbook/index.html'

with open(target_path, 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace(
    "if (!container || !window.examQuestions04) return;",
    "if (!container || typeof examQuestions04 === 'undefined') return;"
)

text = text.replace(
    "if (window.examQuestions04) {",
    "if (typeof examQuestions04 !== 'undefined') {"
)

with open(target_path, 'w', encoding='utf-8') as f:
    f.write(text)

print('Fixed examQuestions04 variable reference.')
