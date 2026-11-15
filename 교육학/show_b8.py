import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('b8_b11_clean.txt', 'r', encoding='utf-8') as f:
    text = f.read()

parts = text.split('='*50)
for p in parts:
    if p.strip():
        # print first line
        lines = p.strip().split('\n')
        print('=== ' + lines[0] + ' ===')
        for l in lines[1:]:
            print(l)
        print('-'*50)
