import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('scratch_150_pages.json', 'r', encoding='utf-8') as f:
    text = f.read()

# find asterisks in scratch_150_pages.json
matches = [m.start() for m in re.finditer(r'\*', text)]
print('Asterisks count in scratch_150_pages.json:', len(matches))
for pos in matches[:10]:
    print('Asterisk at pos:', pos, repr(text[pos-30:pos+30]))
