import os
import re

target_path = r'G:\내 드라이브\ANTI GRAVITY\전문상담임용고시\kice-300-wordbook\kice_55_core_compressed.html'

with open(target_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update HTML Overlay for Auth Screen to include ID
old_auth_html_start = '<input type="password" id="auth-input"'
new_auth_html_inputs = """
    <input type="text" id="auth-id" placeholder="아이디 입력" style="width:100%; padding:15px; font-size:1.2rem; text-align:center; border-radius:8px; border:2px solid #3b82f6; background:#0f172a; color:#f8fafc; font-weight:bold; margin-bottom:10px; box-sizing:border-box;">
    <input type="password" id="auth-input"
"""
html = html.replace(old_auth_html_start, new_auth_html_inputs.strip())


# 2. Update JS Logic to validate ID + PIN map
old_js_logic = """    const VALID_PINS = [
      '371400', // 선생님 마스터 암호
      '825193', '491027', '637284', '159203', '748391', // 회원용 발급 암호 1~5
      '204958', '513842', '960175', '382469', '112233'  // 회원용 발급 암호 6~10
    ];"""

new_js_logic = """    const USERS = {
      "1000개의 문": "371400",
      "회원1": "825193", "회원2": "491027", "회원3": "637284", "회원4": "159203", "회원5": "748391",
      "회원6": "204958", "회원7": "513842", "회원8": "960175", "회원9": "382469", "회원10": "112233"
    };"""
html = html.replace(old_js_logic, new_js_logic)

# Update checkAuth and submitAuth
old_checkAuth = """
    function checkAuth() {
      const savedPin = localStorage.getItem('kice_auth_pin');
      if (VALID_PINS.includes(savedPin)) {
        document.getElementById('auth-screen').style.display = 'none';
      } else {
        document.getElementById('auth-screen').style.display = 'flex';
      }
    }

    function submitAuth() {
      const pin = document.getElementById('auth-input').value.trim();
      if (VALID_PINS.includes(pin)) {
        localStorage.setItem('kice_auth_pin', pin);
        document.getElementById('auth-screen').style.display = 'none';
        warningCount = 0; // reset warnings on fresh login
      } else {
        const err = document.getElementById('auth-error');
        err.style.display = 'block';
        setTimeout(() => { err.style.display = 'none'; }, 2000);
      }
    }
"""

new_checkAuth = """
    function checkAuth() {
      const savedId = localStorage.getItem('kice_auth_id');
      const savedPin = localStorage.getItem('kice_auth_pin');
      
      if (savedId && USERS[savedId] === savedPin) {
        document.getElementById('auth-screen').style.display = 'none';
      } else {
        document.getElementById('auth-screen').style.display = 'flex';
      }
    }

    function submitAuth() {
      const userId = document.getElementById('auth-id').value.trim();
      const pin = document.getElementById('auth-input').value.trim();
      
      if (USERS[userId] && USERS[userId] === pin) {
        localStorage.setItem('kice_auth_id', userId);
        localStorage.setItem('kice_auth_pin', pin);
        document.getElementById('auth-screen').style.display = 'none';
        warningCount = 0; // reset warnings on fresh login
        alert(userId + '님, 환영합니다!');
      } else {
        const err = document.getElementById('auth-error');
        err.innerText = '❌ 아이디 또는 암호가 일치하지 않습니다.';
        err.style.display = 'block';
        setTimeout(() => { err.style.display = 'none'; }, 2000);
      }
    }
"""
html = html.replace(old_checkAuth.strip(), new_checkAuth.strip())

with open(target_path, 'w', encoding='utf-8') as f:
    f.write(html)
    
print("Added ID fields and User mappings.")
