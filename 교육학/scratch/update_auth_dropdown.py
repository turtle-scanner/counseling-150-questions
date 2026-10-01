import os
import re

target_path = r'G:\내 드라이브\ANTI GRAVITY\전문상담임용고시\kice-300-wordbook\kice_55_core_compressed.html'

with open(target_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Replace the <input type="text" id="auth-id"> with a <select> dropdown
old_input = '<input type="text" id="auth-id" placeholder="아이디 입력" style="width:100%; padding:15px; font-size:1.2rem; text-align:center; border-radius:8px; border:2px solid #3b82f6; background:#0f172a; color:#f8fafc; font-weight:bold; margin-bottom:10px; box-sizing:border-box;">'

new_select = """<select id="auth-id" style="width:100%; padding:15px; font-size:1.2rem; text-align:center; border-radius:8px; border:2px solid #3b82f6; background:#0f172a; color:#f8fafc; font-weight:bold; margin-bottom:15px; box-sizing:border-box; appearance:none; cursor:pointer;">
      <option value="천개의문">👑 천개의문</option>
      <option value="라이언/재수/경기">👤 라이언/재수/경기</option>
      <option value="쪼르디/초수/전북">👤 쪼르디/초수/전북</option>
      <option value="춘식/초수/경기">👤 춘식/초수/경기</option>
      <option value="회원1">👤 회원1</option>
      <option value="회원2">👤 회원2</option>
      <option value="회원3">👤 회원3</option>
      <option value="회원4">👤 회원4</option>
      <option value="회원5">👤 회원5</option>
      <option value="회원6">👤 회원6</option>
      <option value="회원7">👤 회원7</option>
      <option value="회원8">👤 회원8</option>
      <option value="회원9">👤 회원9</option>
      <option value="회원10">👤 회원10</option>
    </select>"""

html = html.replace(old_input, new_select)

# 2. Update USERS object to include '천개의문'
old_users = '"1000개의 문": "371400",'
new_users = '"1000개의 문": "371400", "천개의문": "371400",'
html = html.replace(old_users, new_users)

with open(target_path, 'w', encoding='utf-8') as f:
    f.write(html)
    
print("Converted Auth ID to a dropdown menu.")
