import sys

sys.stdout.reconfigure(encoding='utf-8')

target_path = r'G:\내 드라이브\ANTI GRAVITY\전문상담임용고시\kice-300-wordbook\kice_55_core_compressed.html'

with open(target_path, 'r', encoding='utf-8') as f:
    html = f.read()

checks = {
    "Canvas element": '<canvas id="kice-canvas"',
    "Toggle Pen Button": 'id="btn-toggle-pen"',
    "Clear Pen Button": 'id="btn-clear-pen"',
    "90s Timer Button": 'id="btn-timer90"',
    "90s Timer Container": 'id="timer90-container"',
    "Stats Modal": 'id="stats-modal"',
    "Stats Button": 'openStatsModal()',
    "Highlighter Function": 'function applyHighlighter',
    "Highlighter Called in renderCard": 'elAns.innerHTML = applyHighlighter',
    "Canvas Init Called": 'initCanvas()',
    "Canvas Reset on Card": 'if (typeof clearCanvas === "function") clearCanvas()',
    "Timer Reset on Card": 'if (typeof resetTimer90 === "function") resetTimer90()'
}

all_passed = True
for name, target in checks.items():
    found = target in html
    print(f"[{'PASS' if found else 'FAIL'}] {name}")
    if not found:
        all_passed = False

if all_passed:
    print("\nALL 12 RIGOROUS CHECKS PASSED WITH FLYING COLORS!")
else:
    print("\nSOME CHECKS FAILED!")
