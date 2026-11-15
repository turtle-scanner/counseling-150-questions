import re

content = open('../complete_counseling_55_builder.py', encoding='utf-8').read()
matches = list(re.finditer(r'"num":\s*21\b', content))
if matches:
    start = matches[0].start()
    print(content[start:start+1200])
