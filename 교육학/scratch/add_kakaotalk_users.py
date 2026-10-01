import os
import re

target_path = r'G:\내 드라이브\ANTI GRAVITY\전문상담임용고시\kice-300-wordbook\kice_55_core_compressed.html'

with open(target_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Current USERS block
old_users_block = """    const USERS = {
      "1000개의 문": "371400",
      "회원1": "825193", "회원2": "491027", "회원3": "637284", "회원4": "159203", "회원5": "748391",
      "회원6": "204958", "회원7": "513842", "회원8": "960175", "회원9": "382469", "회원10": "112233"
    };"""

new_users_block = """    const USERS = {
      "1000개의 문": "371400",
      "라이언/재수/경기": "128945",
      "쪼르디/초수/전북": "357281",
      "춘식/초수/경기": "924617",
      "회원1": "825193", "회원2": "491027", "회원3": "637284", "회원4": "159203", "회원5": "748391",
      "회원6": "204958", "회원7": "513842", "회원8": "960175", "회원9": "382469", "회원10": "112233"
    };"""

html = html.replace(old_users_block, new_users_block)

with open(target_path, 'w', encoding='utf-8') as f:
    f.write(html)
    
print("KakaoTalk users added to auth map.")
