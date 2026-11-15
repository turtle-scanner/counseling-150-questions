# -*- coding: utf-8 -*-
import sys, io, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='backslashreplace')
html = open(r'C:\Users\LENOVO\Desktop\sam3_update.html', 'r', encoding='utf-8', errors='ignore').read()

matches = list(re.finditer(r'id=["\']troop-promotion-modal["\']', html))
print('Count of id="troop-promotion-modal":', len(matches))
for m in matches:
    print('At', m.start(), ':', html[m.start()-50:m.start()+200])

# Also check ALL duplicate IDs in the entire HTML!
ids = re.findall(r'\bid=["\']([^"\']+)["\']', html)
from collections import Counter
dups = {k: v for k, v in Counter(ids).items() if v > 1}
print('ALL DUPLICATE IDs IN HTML:', dups)
