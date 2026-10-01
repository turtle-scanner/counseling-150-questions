import os
import re

target_path = r'G:\내 드라이브\ANTI GRAVITY\전문상담임용고시\kice-300-wordbook\kice_55_core_compressed.html'

with open(target_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Remove the window 'blur' event listener
html = re.sub(r"// SECURITY: Detect window blur[\s\S]*?\}\);", "", html)

# 2. Relax the alert message slightly to reflect the removal of "화면 이탈"
old_handle_violation = """function handleViolation(reason) {
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
    }"""

new_handle_violation = """function handleViolation(reason) {
      if (isTerminated) return;
      if (document.getElementById('auth-screen').style.display !== 'none') return;

      warningCount++;
      if (warningCount >= MAX_WARNINGS) {
        isTerminated = true;
        localStorage.removeItem('kice_auth_pin'); 
        alert(`🚨 [보안 경고 3회 누적] ${reason}\\n\\n콘텐츠 무단 복제/캡쳐 시도가 감지되어 프로그램 접속을 차단합니다.`);
        document.body.innerHTML = '<div style="background:#000; color:red; width:100vw; height:100vh; display:flex; justify-content:center; align-items:center; font-size:2rem; font-weight:bold; font-family:sans-serif;">보안 정책 위반으로 접속이 차단되었습니다.<br><br>새로고침 후 다시 로그인해주세요.</div>';
      } else {
        alert(`⚠️ [보안 경고 ${warningCount}/${MAX_WARNINGS}] ${reason}\\n\\n무단 복사 및 화면 캡쳐는 금지되어 있습니다. 3회 누적 시 강제 종료됩니다.`);
      }
    }"""

html = html.replace(old_handle_violation, new_handle_violation)

with open(target_path, 'w', encoding='utf-8') as f:
    f.write(html)
    
print("Removed blur detection and relaxed warnings.")
