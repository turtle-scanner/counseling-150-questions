import json

with open('scratch_150_pages.json', 'r', encoding='utf-8') as f:
    pages = json.load(f)

all_items = []
for p in pages:
    for it in p['items']:
        all_items.append(it)

print(f"Total items: {len(all_items)}")

# Check if any field is empty or missing
for i, it in enumerate(all_items):
    num = i + 1
    domain = it.get('domain', '')
    keywords = it.get('keywords', '')
    question = it.get('question', '')
    ans = it.get('answer', '')
    if not domain or not keywords or not question or not ans:
        print(f"Missing in item {num}: domain={bool(domain)}, keywords={bool(keywords)}, question={bool(question)}, ans={bool(ans)}")

print("Validation completed.")
