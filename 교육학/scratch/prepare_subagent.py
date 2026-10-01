import json
import re

with open('scratch/final_55_compressed.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

# The items are currently fine, but let's make sure the prompt to the subagent is clear.
# We will save this as a task for the subagent to read and overwrite.
with open('scratch/task_compress_ans.json', 'w', encoding='utf-8') as f:
    json.dump(items, f, ensure_ascii=False, indent=2)

print("Saved task items")
