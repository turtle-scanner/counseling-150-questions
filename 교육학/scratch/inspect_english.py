import re

with open('kice_150_core_table_a4.html', 'r', encoding='utf-8') as f:
    text = f.read()

kws = re.findall(r'<div class="kw-name">(.*?)</div>', text)
print(f"Total kw items: {len(kws)}")

for i, k in enumerate(kws):
    # Find English words (longer than acronyms like ADHD, MMPI, etc.)
    # or all English in parentheses
    matches = re.findall(r'[A-Za-z]+', k)
    if matches:
        print(f"Item {i+1}: {k}")
