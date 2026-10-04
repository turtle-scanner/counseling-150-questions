import json
import re

target_path = r'G:\내 드라이브\ANTI GRAVITY\전문상담임용고시\kice-300-wordbook\kice_55_core_compressed.html'

with open(target_path, 'r', encoding='utf-8') as f:
    html = f.read()

with open('scratch/new_203_items.json', 'r', encoding='utf-8') as f:
    new_items = json.load(f)

# Find items array
m = re.search(r'let items = (\[[\s\S]*?\]);\s*// Load custom items', html)
if not m:
    print('Failed to find items array')
    exit(1)

new_json_str = json.dumps(new_items, ensure_ascii=False)
replacement = f'let items = {new_json_str};\n      // Load custom items'

html = html[:m.start(0)] + replacement + html[m.end(0):]

# Ensure answer-text has line-height and pre-wrap that perfectly spaces 4 lines
css_upgrade = """
    /* 4-LINE OFFICIAL ANSWER FORMATTING */
    .answer-text {
      white-space: pre-wrap !important;
      line-height: 1.8 !important;
      font-size: 1.35rem !important;
      letter-spacing: -0.3px !important;
    }
"""
if '/* 4-LINE OFFICIAL ANSWER FORMATTING */' not in html:
    html = html.replace('</style>', css_upgrade.strip() + '\n  </style>')

with open(target_path, 'w', encoding='utf-8') as f:
    f.write(html)

print('Successfully injected 203 items with 4-line official answers!')
