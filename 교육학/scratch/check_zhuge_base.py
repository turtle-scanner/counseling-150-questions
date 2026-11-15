# -*- coding: utf-8 -*-
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='backslashreplace')

html = open(r'C:\Users\LENOVO\Desktop\sam3_update.html', 'r', encoding='utf-8', errors='ignore').read()

# Check if zhuge liang or pang tong are in MY_OFFICERS or PORTRAITS
for kw in ['제갈량', '방통', 'MY_OFFICERS', 'executeSearchOfficer', 'openQuestModal']:
    pos = html.find(kw)
    print(f'{kw}: found at {pos}')
    if pos != -1:
        print('  ' + html[pos:pos+300].replace('\n', ' '))
