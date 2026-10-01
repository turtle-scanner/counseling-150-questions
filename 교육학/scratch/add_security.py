import os
import re

target_path = r'G:\내 드라이브\ANTI GRAVITY\전문상담임용고시\kice-300-wordbook\kice_55_core_compressed.html'

with open(target_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. HTML Overlay for Auth Screen
auth_html = """
<div id="auth-screen" style="position:fixed; top:0; left:0; width:100vw; height:100vh; background:#0f172a; z-index:9999999; display:flex; flex-direction:column; justify-content:center; align-items:center; font-family:'Malgun Gothic', sans-serif;">
  <div style="background:#1e293b; padding:40px; border-radius:12px; box-shadow:0 10px 25px rgba(0,0,0,0.5); text-align:center; max-width:90%; width:400px; border:1px solid #334155;">
    <h2 style="color:#f8fafc; margin-top:0; margin-bottom:10px; font-size:1.5rem;">🔒 보안 접속 인증</h2>
    <p style="color:#94a3b8; font-size:0.95rem; margin-bottom:25px; line-height:1.5;">KICE 300 시스템에 접속하려면<br>부여받은 6자리 암호를 입력해주세요.<br><span style="color:#ef4444; font-size:0.8rem; font-weight:bold;">(주의: 1인 1암호 원칙, 화면 이탈/캡쳐 엄격 금지)</span></p>
    <input type="password" id="auth-input" maxlength="6" placeholder="******" style="width:100%; padding:15px; font-size:2rem; text-align:center; letter-spacing:10px; border-radius:8px; border:2px solid #3b82f6; background:#0f172a; color:#facc15; font-weight:900; margin-bottom:20px; box-sizing:border-box;">
    <button onclick="submitAuth()" style="width:100%; padding:15px; font-size:1.1rem; font-weight:bold; background:#3b82f6; color:#fff; border:none; border-radius:8px; cursor:pointer; transition:0.3s;">인증하기 (Enter)</button>
    <p id="auth-error" style="color:#ef4444; font-size:0.9rem; margin-top:15px; display:none;">❌ 올바르지 않은 암호입니다.</p>
  </div>
</div>
"""

if 'id="auth-screen"' not in html:
    html = html.replace('<body>', '<body>\n' + auth_html)


# 2. JS Logic for Auth & Anti-Cheat Security
security_js = """
    // --- AUTHENTICATION & SECURITY LOGIC ---
    const VALID_PINS = [
      '371400', // 선생님 마스터 암호
      '825193', '491027', '637284', '159203', '748391', // 회원용 발급 암호 1~5
      '204958', '513842', '960175', '382469', '112233'  // 회원용 발급 암호 6~10
    ];

    let warningCount = 0;
    const MAX_WARNINGS = 3;
    let isTerminated = false;

    function handleViolation(reason) {
      if (isTerminated) return;
      // Do not count violations if they haven't logged in yet
      if (document.getElementById('auth-screen').style.display !== 'none') return;

      warningCount++;
      if (warningCount >= MAX_WARNINGS) {
        isTerminated = true;
        localStorage.removeItem('kice_auth_pin'); // Revoke access
        alert(`🚨 [보안 경고 3회 누적] ${reason}\\n\\n부정 사용(캡쳐/이탈)이 감지되어 프로그램 접속을 영구 차단 및 강제 종료합니다.`);
        document.body.innerHTML = '<div style="background:#000; color:red; width:100vw; height:100vh; display:flex; justify-content:center; align-items:center; font-size:2rem; font-weight:bold; font-family:sans-serif;">보안 정책 위반으로 접속이 영구 차단되었습니다.</div>';
      } else {
        alert(`⚠️ [보안 경고 ${warningCount}/${MAX_WARNINGS}] ${reason}\\n\\n화면 캡쳐 및 다른 창(화면) 이동은 엄격히 금지되어 있습니다.\\n3회 누적 시 강제 종료됩니다!`);
      }
    }

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

    // Attach enter key for auth input
    document.addEventListener('DOMContentLoaded', () => {
      document.getElementById('auth-input')?.addEventListener('keydown', function(e) {
        if (e.key === 'Enter') submitAuth();
      });
    });

    // SECURITY: Detect window blur (switching tabs, clicking other apps)
    window.addEventListener('blur', () => {
      handleViolation("화면 이탈(다른 창 이동)이 감지되었습니다.");
    });

    // SECURITY: Disable Right Click
    document.addEventListener('contextmenu', e => {
      e.preventDefault();
      handleViolation("마우스 우클릭(복사/저장 시도)이 감지되었습니다.");
    });

    // SECURITY: Detect common screenshot/copy shortcuts
    document.addEventListener('keydown', e => {
      if (document.getElementById('auth-screen').style.display !== 'none') return;
      
      // PrintScreen key
      if (e.key === 'PrintScreen' || e.keyCode === 44) {
        handleViolation("PrintScreen 캡쳐 단축키가 감지되었습니다.");
      }
      // Ctrl+C, Ctrl+S, Ctrl+P
      if (e.ctrlKey && (e.key === 'c' || e.key === 'C' || e.key === 's' || e.key === 'S' || e.key === 'p' || e.key === 'P')) {
        e.preventDefault();
        handleViolation("복사/저장/인쇄 단축키가 감지되었습니다.");
      }
      // Mac Meta+Shift+3,4,5 (Screenshot) or Meta+C
      if (e.metaKey && e.shiftKey) {
        e.preventDefault();
        handleViolation("화면 캡쳐 단축키가 감지되었습니다.");
      }
    });

    // Protect CSS: Prevent text selection
    const noSelectStyle = document.createElement('style');
    noSelectStyle.innerHTML = `body { user-select: none; -webkit-user-select: none; -moz-user-select: none; -ms-user-select: none; } .kice-textarea { user-select: text; -webkit-user-select: text; }`;
    document.head.appendChild(noSelectStyle);

    checkAuth();
"""

if 'const VALID_PINS' not in html:
    html = html.replace('// INIT', security_js + '\n    // INIT')

with open(target_path, 'w', encoding='utf-8') as f:
    f.write(html)
    
print("Auth and Anti-Cheat applied.")
