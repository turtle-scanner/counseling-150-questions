import re

with open('scratch/dump_150_all.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for line in lines:
    if line.startswith('['):
        # check if English letters exist
        if re.search(r'[A-Za-z]', line):
            print(line.strip())
