import os
import json
import re

json_path = r'scratch/final_55_compressed.json'
with open(json_path, 'r', encoding='utf-8') as f:
    items = json.load(f)

# Compact the answers into "답안지 서술형 (개조식 명사 종결)"
for it in items:
    ans = it['ans']
    # Change common endings to compact forms
    ans = ans.replace('모형이다.', '모형임.')
    ans = ans.replace('기법이다.', '기법임.')
    ans = ans.replace('것이다.', '것임.')
    ans = ans.replace('평가이다.', '평가임.')
    ans = ans.replace('한다.', '함.')
    ans = ans.replace('된다.', '됨.')
    ans = ans.replace('이다.', '임.')
    ans = ans.replace('있다.', '있음.')
    # Strip unnecessary trailing spaces
    it['ans'] = ans.strip()

with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(items, f, ensure_ascii=False, indent=2)

items_json_str = json.dumps(items, ensure_ascii=False)

html_path = r'G:\내 드라이브\ANTI GRAVITY\전문상담임용고시\kice-300-wordbook\kice_55_core_compressed.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update the JSON embedded in HTML
# The regex looks for `let items = [...];` and replaces it.
html = re.sub(r'let items = \[.*?\];', f'let items = {items_json_str};', html, flags=re.DOTALL)

# 2. Aggressively fix the print CSS
# Find the @media print block and replace it
print_css = """@media print {
      * { background: transparent !important; color: #000 !important; box-shadow: none !important; text-shadow: none !important; }
      body { background: #fff !important; color: #000 !important; font-size: 10pt !important; }
      .app-header, .controls, #mode-anki, .table-nav, #add-modal, .modal-overlay { display: none !important; }
      #mode-table { display: block !important; width: 100% !important; max-width: none !important; }
      .table-container { border: none !important; box-shadow: none !important; overflow: visible !important; background: #fff !important; }
      table { border: 2px solid #000 !important; width: 100% !important; page-break-inside: auto; background: #fff !important; }
      tr { page-break-inside: avoid; page-break-after: auto; background: #fff !important; }
      tr.table-row { display: table-row !important; background: #fff !important; }
      th { background: #f0f0f0 !important; color: #000 !important; border: 1px solid #000 !important; padding: 8px !important; }
      td { border: 1px solid #000 !important; color: #000 !important; background: #fff !important; padding: 8px !important; }
      .td-badge { color: #333 !important; border: none !important; padding: 0 !important; display: inline !important; margin-right: 5px !important; }
      .td-kw { color: #000 !important; font-weight: bold !important; display: inline !important; font-size: 10pt !important; }
      .td-q { color: #000 !important; font-size: 10pt !important; }
      .td-ans { color: #000 !important; background: transparent !important; border: none !important; padding: 0 !important; font-size: 10pt !important; }
    }"""

# Replace the existing @media print block
# Use regex to find @media print { ... }
html = re.sub(r'@media print\s*\{.*?\}(?=\s*</style>)', print_css, html, flags=re.DOTALL)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Fixed print CSS and compacted answers!")
