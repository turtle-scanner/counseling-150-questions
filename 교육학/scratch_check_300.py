import os

target = 'G:/내 드라이브/ANTI GRAVITY/전문상담임용고시/kice-300-wordbook/2027_KICE_300선_핵심단어장_앱.html'
if os.path.exists(target):
    with open(target, 'r', encoding='utf-8') as f:
        content = f.read()
    print('Found in kice-300-wordbook! Size:', len(content))
else:
    print('Not in kice-300-wordbook, checking cwd...')
    if os.path.exists('2027_KICE_300선_핵심단어장_앱.html'):
        with open('2027_KICE_300선_핵심단어장_앱.html', 'r', encoding='utf-8') as f:
            content = f.read()
        print('Found in cwd! Size:', len(content))
