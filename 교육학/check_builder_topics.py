import re

content = open('../complete_counseling_55_builder.py', encoding='utf-8').read()
nums = re.findall(r'"num":\s*(\d+)', content)
print("Count of topics in builder:", len(nums))
print("Topic nums:", [int(n) for n in nums])
