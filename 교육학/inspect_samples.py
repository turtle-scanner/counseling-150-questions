# -*- coding: utf-8 -*-
with open(r'G:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\교육학\scratch\temp_script1.js', 'r', encoding='utf-8', errors='ignore') as f:
    code = f.read()

# Let's inspect executeTraining, openDuelSelectModal, openInfoModal
targets = ['executeTraining', 'openDuelSelectModal', 'openInfoModal', 'openReorganizeModal']
for t in targets:
    pos = code.find(f'function {t}')
    print(f"\n--- {t} ---")
    if pos != -1:
        snippet = code[pos:pos+400]
        print(snippet.encode('ascii', errors='backslashreplace').decode('ascii'))
