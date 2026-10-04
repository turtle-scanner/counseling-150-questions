import sys

sys.stdout.reconfigure(encoding='utf-8')

with open(r'G:\내 드라이브\ANTI GRAVITY\전문상담임용고시\kice-300-wordbook\kice_55_core_compressed.html', 'r', encoding='utf-8') as f:
    text = f.read()

checks = [
    '🎯 마스터 <span id="stat-done" style="color:#6ee7b7;">0</span></span>',
    '<button class="btn-control" id="btn-wrong"',
    '<div class="card-q" id="c-q"',
    '<button onclick="showChosungHint()"',
    '<textarea id="c-input"',
    'elAns.innerHTML = formatText(item.ans);',
    'renderCard(currentIndex);',
    'warningCount = 0;',
    '// --- ADVANCED STUDY FEATURES'
]

for idx, c in enumerate(checks):
    found = c in text
    print(f"Check {idx}: FOUND = {found}")
    if not found:
        print(f"  FAILED string: {repr(c)}")
