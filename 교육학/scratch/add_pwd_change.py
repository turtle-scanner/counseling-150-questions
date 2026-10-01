import os
import re

target_path = r'G:\내 드라이브\ANTI GRAVITY\전문상담임용고시\kice-300-wordbook\kice_55_core_compressed.html'

with open(target_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update the Auth Logic to support custom local passwords
old_check_auth = """function checkAuth() {
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
    }"""

new_check_auth = """function checkAuth() {
      const savedId = localStorage.getItem('kice_auth_id');
      const savedPin = localStorage.getItem('kice_auth_pin');
      const customPwds = JSON.parse(localStorage.getItem('kice_custom_pwds') || '{}');
      
      if (savedId) {
        const expectedPin = customPwds[savedId] || USERS[savedId];
        if (expectedPin === savedPin) {
          document.getElementById('auth-screen').style.display = 'none';
          return;
        }
      }
      document.getElementById('auth-screen').style.display = 'flex';
    }

    function submitAuth() {
      const userId = document.getElementById('auth-id').value.trim();
      const pin = document.getElementById('auth-input').value.trim();
      
      const customPwds = JSON.parse(localStorage.getItem('kice_custom_pwds') || '{}');
      const expectedPin = customPwds[userId] || USERS[userId];
      
      if (expectedPin && expectedPin === pin) {
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
    
    function changeUserPassword() {
      const currentUser = localStorage.getItem('kice_auth_id');
      if (!currentUser) { alert('먼저 로그인해주세요.'); return; }
      
      const newPwd = prompt("새로운 6자리 암호를 입력하세요:\\n(주의: 기기에 저장되므로 브라우저 초기화 시 초기 암호로 리셋될 수 있습니다)");
      if (newPwd && newPwd.length === 6 && /^\\d+$/.test(newPwd)) {
        const customPwds = JSON.parse(localStorage.getItem('kice_custom_pwds') || '{}');
        customPwds[currentUser] = newPwd;
        localStorage.setItem('kice_custom_pwds', JSON.stringify(customPwds));
        localStorage.setItem('kice_auth_pin', newPwd);
        alert('비밀번호가 [' + newPwd + ']로 성공적으로 변경되었습니다!');
      } else if (newPwd) {
        alert("암호는 반드시 6자리 숫자로 입력해주세요.");
      }
    }
    """

html = html.replace(old_check_auth, new_check_auth)

# 2. Add the "Change Password" button to the UI (inside app-title or next to it)
old_app_title = '<div class="app-title">🐢 2027 KICE 초압축 55선</div>'
new_app_title = '<div class="app-title" style="display:flex; justify-content:space-between; align-items:center;"><span>🐢 2027 KICE 초압축 55선</span> <button onclick="changeUserPassword()" style="font-size:0.7rem; padding:4px 8px; background:#475569; color:white; border:none; border-radius:4px; cursor:pointer;">🔒 비번변경</button></div>'
html = html.replace(old_app_title, new_app_title)


with open(target_path, 'w', encoding='utf-8') as f:
    f.write(html)
    
print("Added change password logic.")
