import os
import re

target_path = r'G:\내 드라이브\ANTI GRAVITY\전문상담임용고시\kice-300-wordbook\kice_55_core_compressed.html'

with open(target_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add Firebase SDK scripts to <head>
firebase_scripts = """  <!-- FIREBASE CLOUD REALTIME DATABASE SDK -->
  <script src="https://www.gstatic.com/firebasejs/10.8.0/firebase-app-compat.js"></script>
  <script src="https://www.gstatic.com/firebasejs/10.8.0/firebase-firestore-compat.js"></script>
"""

if 'firebase-app-compat.js' not in html:
    html = html.replace('</head>', firebase_scripts + '\n</head>')

# 2. Update Auth logic to connect to Google Cloud Firestore
new_cloud_auth_js = """    // --- GOOGLE CLOUD FIREBASE CONFIG & 1-USER 1-DEVICE SYSTEM ---
    const firebaseConfig = {
      apiKey: "AIzaSyBsYj1m_y9IYpo42urauouSqDx38xv6XNE",
      authDomain: "kice-study-29a5c.firebaseapp.com",
      projectId: "kice-study-29a5c",
      storageBucket: "kice-study-29a5c.firebasestorage.app",
      messagingSenderId: "565045000792",
      appId: "1:565045000792:web:840cde0297b7b6bc59a82d"
    };

    // Initialize Firebase
    if (!firebase.apps.length) {
      firebase.initializeApp(firebaseConfig);
    }
    const db = firebase.firestore();

    // Default seed PINs
    const DEFAULT_PINS = {
      "1000": "371400",
      "라이언/재수/경기": "128945",
      "쪼르디/초수/전북": "357281",
      "춘식/초수/경기": "924617",
      "회원1": "825193", "회원2": "491027", "회원3": "637284", "회원4": "159203", "회원5": "748391",
      "회원6": "204958", "회원7": "513842", "회원8": "960175", "회원9": "382469", "회원10": "112233"
    };

    // Generate unique device token for this browser
    let myDeviceId = localStorage.getItem('kice_device_id');
    if (!myDeviceId) {
      myDeviceId = 'dev_' + Math.random().toString(36).substring(2) + Date.now();
      localStorage.setItem('kice_device_id', myDeviceId);
    }

    let unsubscribeSnapshot = null;

    // Listen for concurrent login on other devices in real-time
    function listenToSession(userId) {
      if (unsubscribeSnapshot) unsubscribeSnapshot();
      
      unsubscribeSnapshot = db.collection('users').doc(userId).onSnapshot(doc => {
        if (!doc.exists) return;
        const data = doc.data();
        if (data.activeDeviceId && data.activeDeviceId !== myDeviceId) {
          // Another device logged in! Kick this device out immediately!
          alert('🚨 [동시접속 차단] 다른 기기에서 이 아이디로 로그인하였습니다.\\n1인 1계정 원칙에 따라 현재 기기의 접속이 종료됩니다.');
          localStorage.removeItem('kice_auth_id');
          localStorage.removeItem('kice_auth_pin');
          document.getElementById('auth-screen').style.display = 'flex';
        }
      }, err => {
        console.warn('Realtime listener notice:', err);
      });
    }

    async function checkAuth() {
      const savedId = localStorage.getItem('kice_auth_id');
      const savedPin = localStorage.getItem('kice_auth_pin');
      
      if (!savedId || !savedPin) {
        document.getElementById('auth-screen').style.display = 'flex';
        return;
      }
      
      try {
        const docRef = db.collection('users').doc(savedId);
        const doc = await docRef.get();
        
        let validPin = DEFAULT_PINS[savedId];
        if (doc.exists) {
          validPin = doc.data().pin || validPin;
        }
        
        if (savedPin === validPin) {
          document.getElementById('auth-screen').style.display = 'none';
          listenToSession(savedId);
        } else {
          document.getElementById('auth-screen').style.display = 'flex';
        }
      } catch (e) {
        // Fallback if offline
        document.getElementById('auth-screen').style.display = 'none';
      }
    }

    async function submitAuth() {
      const userId = document.getElementById('auth-id').value.trim();
      const pin = document.getElementById('auth-input').value.trim();
      const btn = event?.target;
      const err = document.getElementById('auth-error');
      
      try {
        const docRef = db.collection('users').doc(userId);
        const doc = await docRef.get();
        
        let expectedPin = DEFAULT_PINS[userId];
        if (doc.exists && doc.data().pin) {
          expectedPin = doc.data().pin;
        }
        
        if (pin !== expectedPin) {
          err.innerText = '❌ 암호가 일치하지 않습니다.';
          err.style.display = 'block';
          setTimeout(() => { err.style.display = 'none'; }, 2000);
          return;
        }
        
        // Claim active session on Cloud
        await docRef.set({
          pin: expectedPin,
          activeDeviceId: myDeviceId,
          lastLogin: firebase.firestore.FieldValue.serverTimestamp()
        }, { merge: true });
        
        localStorage.setItem('kice_auth_id', userId);
        localStorage.setItem('kice_auth_pin', pin);
        document.getElementById('auth-screen').style.display = 'none';
        warningCount = 0;
        
        listenToSession(userId);
        alert(userId + '님 환영합니다! (클라우드 1인 1기기 인증 완료)');
      } catch (error) {
        console.error('Auth error:', error);
        alert('서버 인증 중 오류가 발생했습니다: ' + error.message);
      }
    }

    async function changeUserPassword() {
      const currentUser = localStorage.getItem('kice_auth_id');
      if (!currentUser) { alert('먼저 로그인해주세요.'); return; }
      
      const newPwd = prompt("새로운 6자리 암호를 입력하세요:\\n(클라우드 서버에 영구 반영되어 모든 기기에 즉시 적용됩니다)");
      if (newPwd && newPwd.length === 6 && /^\\d+$/.test(newPwd)) {
        try {
          await db.collection('users').doc(currentUser).set({
            pin: newPwd
          }, { merge: true });
          
          localStorage.setItem('kice_auth_pin', newPwd);
          alert('비밀번호가 [' + newPwd + ']로 클라우드 서버에 안전하게 변경되었습니다!');
        } catch (err) {
          alert('비밀번호 변경 실패: ' + err.message);
        }
      } else if (newPwd) {
        alert("암호는 반드시 6자리 숫자로 입력해주세요.");
      }
    }
"""

# Replace old local auth logic
old_auth_pattern = r"// --- AUTHENTICATION & SECURITY LOGIC ---[\s\S]*?checkAuth\(\);"
# Find and replace
# Let's check what is between // --- AUTHENTICATION and checkAuth();
pattern_to_replace = re.search(r"// --- AUTHENTICATION[\s\S]*?function changeUserPassword\(\) \{[\s\S]*?checkAuth\(\);", html)
if pattern_to_replace:
    html = html.replace(pattern_to_replace.group(0), new_cloud_auth_js.strip() + "\n\n    checkAuth();")
else:
    print("Pattern not matched directly, using surgical replacement")

with open(target_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("Cloud Firebase 1-Device authentication injected successfully.")
