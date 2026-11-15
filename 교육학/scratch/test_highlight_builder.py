import sys
import re
import json

sys.stdout.reconfigure(encoding='utf-8')

target_path = r'G:\내 드라이브\ANTI GRAVITY\전문상담임용고시\kice-300-wordbook\kice_55_core_compressed.html'

with open(target_path, 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'items\s*=\s*(\[.*?\]);', text)
items = json.loads(m.group(1))

print(f"Total items loaded: {len(items)}")

# Sample check highlighting
def highlight_ans(ans):
    # Highlight bracketed tags
    t = re.sub(r'\[([^\]]+)\]', r'<span class="tag-badge">[\1]</span>', ans)
    # Highlight single quotes
    t = re.sub(r"'([^']+)'", r'<span class="kw-hl">\1</span>', t)
    # Split into lines
    lines = [l.strip() for l in t.split('\n') if l.strip()]
    return '<br>'.join(lines)

print("Sample Item 1 Answer highlighted:")
print(highlight_ans(items[0]['ans']))
print("\nSample Item 21 Answer highlighted:")
print(highlight_ans(items[20]['ans']))
