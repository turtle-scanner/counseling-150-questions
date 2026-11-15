import json

with open('scratch_150_pages.json', 'r', encoding='utf-8') as f:
    pages = json.load(f)

print('Total pages in scratch_150_pages.json:', len(pages))
for p in pages:
    p_num = p['pageNum']
    p_title = p['pageTitle']
    items = p['items']
    print(f'Page {p_num}: {p_title} ({len(items)} items)')
    for it in items[:1]:
        print('   Item sample:', it.keys())
        print('   Keywords:', it.get('keywords', it.get('kw', '')))
        print('   Question:', it.get('question', it.get('q', ''))[:50])
        print('   Answer:', it.get('answer', it.get('ans', ''))[:50])
