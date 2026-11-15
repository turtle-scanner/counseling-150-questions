# -*- coding: utf-8 -*-
import sys, io, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='backslashreplace')
html = open(r'C:\Users\LENOVO\Desktop\sam3_update.html', 'r', encoding='utf-8', errors='ignore').read()

for kw in ['officer-deploy-modal', 'function confirmOfficerDeployment', 'function renderDeployOfficerList', 'function toggleOfficerDeploy']:
    for m in re.finditer(re.escape(kw), html):
        pos = m.start()
        print(f'=== {kw} at {pos} ===')
        print(html[max(0, pos-80):min(len(html), pos+1100)])
