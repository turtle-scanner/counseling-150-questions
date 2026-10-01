import json

with open('scratch_150_pages.json', 'r', encoding='utf-8') as f:
    pages = json.load(f)

total = 0
for idx, page in enumerate(pages):
    cnt = len(page['items'])
    total += cnt
    title = page.get('pageTitle', '')
    print(f"Page {idx+1}: {cnt} items - {title}")

print(f"Total: {total}")

# inspect first 2 items
print("Sample item 0:", pages[0]['items'][0])
