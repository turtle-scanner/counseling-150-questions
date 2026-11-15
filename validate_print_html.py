# -*- coding: utf-8 -*-
with open('exam_master_2027.html', 'r', encoding='utf-8') as f:
    html = f.read()

print('Has openPrintModal:', 'openPrintModal' in html)
print('Has print-modal:', 'id="print-modal"' in html)
print('Has @media print:', '@media print' in html)
print('Has print-paper-answer:', 'print-paper-answer' in html)
print('Has print-scope-full:', 'print-scope-full' in html)
