import re
from collections import Counter

with open(r'G:\내 드라이브\ANTI GRAVITY\전문상담임용고시\kice-300-wordbook\kice_150_core_table_a4.html', 'r', encoding='utf-8') as f:
    text = f.read()

badges = re.findall(r'kw-badge">([^<]+)<', text)
print(f"Total badges in 150 HTML: {len(badges)}")
for b, c in Counter(badges).most_common():
    print(f"  {b}: {c}")
