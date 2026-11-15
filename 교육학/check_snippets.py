import re

content = open('../complete_counseling_55_builder.py', encoding='utf-8').read()

for tnum in [21, 22, 54, 55]:
    idx = content.find(f'"num": {tnum}')
    if idx != -1:
        snippet = content[idx:idx+800]
        print(f"=== Topic {tnum} ===")
        print(snippet[:snippet.find('}') + 1])
        print()
