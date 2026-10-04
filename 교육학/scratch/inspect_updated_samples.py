import json

with open('scratch/new_203_items_curriculum2022.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

test_indices = [1, 3, 10, 20, 35, 78, 92, 105, 130, 159, 164]

with open('scratch/inspect_updated_samples.txt', 'w', encoding='utf-8') as out:
    for it in items:
        if it['num'] in test_indices:
            out.write(f"=== [{it['num']}] {it['kw']} ({it['badge']}) ===\n")
            out.write(it['ans'] + "\n\n")

print("Dumped samples to scratch/inspect_updated_samples.txt")
