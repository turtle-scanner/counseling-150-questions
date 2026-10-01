import os, re

files = os.listdir('.')
print('Files in current directory:')
for f in files:
    if any(k in f for k in ['150', '핵심', '단어', '키워드', '모의고사', '0906', '0905']):
        print(' -', f)
