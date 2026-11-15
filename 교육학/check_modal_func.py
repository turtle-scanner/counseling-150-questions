# -*- coding: utf-8 -*-
with open(r'C:\Users\LENOVO\Desktop\sam3_update.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

import re

# check closeModal and openModal definitions
funcs = re.findall(r'function\s+(?:closeModal|openModal|playSound)\s*\([^)]*\)\s*\{[^}]*\}', text)
for fn in funcs:
    print(fn.encode('ascii', errors='backslashreplace').decode('ascii'))
    print('-'*40)
