import os
import glob
import re

dir_path = r'G:\내 드라이브\ANTI GRAVITY\전문상담임용고시\kice-300-wordbook'
for f in glob.glob(os.path.join(dir_path, '*.html')):
    with open(f, 'r', encoding='utf-8', errors='ignore') as fp:
        content = fp.read()
    nums = re.findall(r'"num":\s*\d+', content)
    trs = re.findall(r'<tr>\s*<td>\d+</td>', content)
    print(f'{os.path.basename(f)}: "num" count = {len(nums)}, "tr" count = {len(trs)}')
