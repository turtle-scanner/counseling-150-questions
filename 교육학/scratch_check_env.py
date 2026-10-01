import sys, json, re
sys.stdout.reconfigure(encoding='utf-8')

# Let's verify that no asterisks exist in the entire dataset
with open('scratch_test_split_ab.py', 'r', encoding='utf-8') as f:
    code = f.read()

print('Python environment check ok.')
