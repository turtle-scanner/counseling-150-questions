import sys, re
sys.stdout.reconfigure(encoding='utf-8')

target_path = 'G:/내 드라이브/ANTI GRAVITY/전문상담임용고시/kice-300-wordbook/index.html'

with open(target_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Find where init is called
matches = [m.start() for m in re.finditer(r'applyFilter\(\)', text)]
print('applyFilter calls at positions:', matches)
for pos in matches:
    print('Context around call:')
    print(text[pos-100:pos+150])
    print('-'*50)
