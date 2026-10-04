with open(r'G:\내 드라이브\ANTI GRAVITY\전문상담임용고시\kice-300-wordbook\kice_55_core_compressed.html', 'r', encoding='utf-8') as f:
    html = f.read()

checks = [
    ('id="cat-pills"', 'cat-pills element'),
    ('id="c-trap"', 'c-trap element'),
    ('printSummaryA4()', 'printSummaryA4 function/button'),
    ('.badge-grade', 'badge-grade CSS'),
    ('function filterByCategory', 'filterByCategory JS function'),
    ('function getTrapTip', 'getTrapTip JS function'),
    ('function getGradeInfo', 'getGradeInfo JS function')
]

all_passed = True
for target, desc in checks:
    present = target in html
    print(f"[{'PASS' if present else 'FAIL'}] {desc}")
    if not present:
        all_passed = False

print("All verifications passed:", all_passed)
