import re
import os

target_path = r'G:\내 드라이브\ANTI GRAVITY\전문상담임용고시\kice-300-wordbook\kice_55_core_compressed.html'

with open(target_path, 'r', encoding='utf-8') as f:
    html = f.read()

new_images = "const rewardImages = ['images/go1.png', 'images/go2.jpg', 'images/go3.png', 'images/go4.jpg', 'images/go5.jpg'];"
html = re.sub(r"const rewardImages = \[.*?\];", new_images, html)

build_path = r'g:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\교육학\scratch\build_55_unified.py'
with open(build_path, 'r', encoding='utf-8') as f:
    build_code = f.read()
build_code = re.sub(r"const rewardImages = \[.*?\];", new_images, build_code)

with open(build_path, 'w', encoding='utf-8') as f:
    f.write(build_code)

with open(target_path, 'w', encoding='utf-8') as f:
    f.write(html)
    
print("Updated successfully!")
