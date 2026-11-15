# -*- coding: utf-8 -*-
import sys, io, re, shutil, subprocess

target_html_path = r'C:\Users\LENOVO\Desktop\sam3_update.html'
html = open(target_html_path, 'r', encoding='utf-8', errors='ignore').read()

# 1. 상단 메뉴바에 [📜 제갈량 삼고초려 & 영웅 영입] 멋진 뱃지 버튼 추가
header_btn_old = '<button onclick="openModal(\'liu-bei-intro-modal\'); playSound(\'select\');" class="px-2.5 py-1 rounded bg-amber-900/90 hover:bg-amber-800 text-yellow-300 border border-yellow-500 font-black text-xs shadow flex items-center gap-1">'

header_btn_new = '''<button onclick="openSangoModal(); playSound('select');" class="px-3 py-1 rounded bg-gradient-to-r from-purple-900 via-indigo-900 to-blue-900 hover:from-purple-800 hover:to-indigo-800 text-yellow-300 border-2 border-yellow-400 font-black text-xs shadow-xl flex items-center gap-1.5 animate-pulse">
        <span>📜</span> <span>제갈량 삼고초려 & 영웅 영입</span>
      </button>
      ''' + header_btn_old

if header_btn_old in html:
    html = html.replace(header_btn_old, header_btn_new, 1)
    print("Added Sango button to header successfully!")
else:
    print("Header button anchor not found directly, finding banner container...")

# 2. HTML 모달 창 추가 (sango-modal)
sango_modal_html = '''
  <!-- ==================== 📜 [삼국지 3] 삼고초려(三顧草廬) & 제갈공명 출사 대하 서사시 모달 ==================== -->
  <div id="sango-modal" class="fixed inset-0 modal-backdrop z-[9999999] hidden flex items-center justify-center p-3 bg-black/95">
    <div class="koei-box w-full max-w-2xl p-5 rounded-xl shadow-2xl border-4 border-amber-400 bg-slate-950 text-white flex flex-col gap-3 max-h-[92vh] overflow-y-auto">
      
      <!-- 헤더 -->
      <div class="flex items-center justify-between border-b-2 border-amber-500 pb-2">
        <div class="flex items-center gap-2">
          <span class="text-3xl animate-bounce">📜</span>
          <div>
            <h2 class="text-base sm:text-lg font-black text-yellow-300 text-pixel tracking-wide" id="sango-modal-title">
              [삼고초려] 남양의 와룡, 천재 군사 제갈량(공명)을 찾아서
            </h2>
            <div class="text-[11px] text-cyan-200" id="sango-modal-subtitle">
              "복룡(伏龍)과 봉추(鳳雛), 둘 중 하나만 얻어도 천하를 평정할 수 있습니다."
            </div>
          </div>
        </div>
        <button onclick="closeModal('sango-modal')" class="text-slate-400 hover:text-white text-xs px-2.5 py-1 border border-slate-600 rounded bg-slate-800">
          ✕ 닫기
        </button>
      </div>

      <!-- 진행 단계 상태 바 (1차 -> 2차 -> 3차 와룡 출려) -->
      <div class="grid grid-cols-3 gap-2 text-center text-xs font-bold py-1">
        <div id="sango-step-1" class="p-1.5 rounded border border-yellow-500 bg-amber-950/80 text-yellow-200">
          ① 1차 방문 (초겨울)
        </div>
        <div id="sango-step-2" class="p-1.5 rounded border border-slate-700 bg-slate-900 text-slate-400">
          ② 2차 방문 (설경)
        </div>
        <div id="sango-step-3" class="p-1.5 rounded border border-slate-700 bg-slate-900 text-slate-400">
          ③ 3차 방문 (천하삼분)
        </div>
      </div>

      <!-- 중앙 컷신 박스 -->
      <div class="p-4 rounded-lg bg-gradient-to-b from-blue-950/80 to-slate-900 border-2 border-yellow-600/70 shadow-inner flex flex-col gap-3">
        <div class="flex items-center gap-3">
          <div class="w-20 h-20 sm:w-24 sm:h-24 rounded-lg border-2 border-amber-400 bg-black flex items-center justify-center text-4xl shadow-xl flex-shrink-0" id="sango-avatar">
            🛖
          </div>
          <div class="flex-1 space-y-1">
            <div class="text-xs text-yellow-400 font-extrabold" id="sango-speaker">융중의 학동</div>
            <div class="text-xs sm:text-sm text-slate-100 font-medium leading-relaxed italic bg-black/50 p-2.5 rounded border border-slate-700" id="sango-dialogue">
              "선생님께서는 학을 타고 세상을 유람하러 나가셨습니다. 언제 돌아오실지는 구름만이 알 뿐입니다..."
            </div>
          </div>
        </div>

        <!-- 유비와 삼형제의 반응 -->
        <div class="bg-amber-950/40 p-3 rounded border border-amber-600/50 text-xs text-amber-200 space-y-1" id="sango-narrative">
          <div>• <strong>장비(익덕):</strong> "형님! 이런 시골뜨기 서생 하나를 만나려고 우리가 형주에서 여기까지 찬바람을 맞고 와야 합니까?"</div>
          <div>• <strong>유비(현덕):</strong> "익덕아, 대업을 이루려면 천하의 대현을 얻어야 하거늘, 예를 다하지 않고 어찌 마음을 얻겠느냐!"</div>
        </div>
      </div>

      <!-- 행동 선택지 버튼들 -->
      <div class="flex flex-col sm:flex-row items-center justify-end gap-2 pt-2 border-t border-slate-800" id="sango-action-buttons">
        <!-- 동적 렌더링 -->
      </div>
    </div>
  </div>
'''

# Insert sango_modal_html before </body> or right after liu-bei-intro-modal
pos_intro = html.find('id="liu-bei-intro-modal"')
if pos_intro != -1:
    pos_end_div = html.find('</div>\n  </div>', pos_intro)
    if pos_end_div != -1:
        html = html[:pos_end_div+14] + '\n\n' + sango_modal_html + html[pos_end_div+14:]
        print("Inserted sango-modal HTML successfully!")
else:
    pos_body = html.rfind('</body>')
    html = html[:pos_body] + '\n' + sango_modal_html + html[pos_body:]
    print("Inserted sango-modal before </body>")

# 3. 자바스크립트 로직 (삼고초려 1차/2차/3차, 제갈량 능력치 100 합류, 방통 등용)
sango_js = '''
    // ==================== 📜 삼고초려(三顧草廬) & 영웅 영입 엔진 ====================
    let sangoStage = 0; // 0: 미시작, 1: 1차완료, 2: 2차완료, 3: 제갈량 합류 완료!
    let pangtongRecruited = false;

    function openSangoModal() {
      closeAllPopups();
      renderSangoStageUI();
      openModal('sango-modal');
      playSfx('select');
    }

    function renderSangoStageUI() {
      const titleEl = document.getElementById('sango-modal-title');
      const subtitleEl = document.getElementById('sango-modal-subtitle');
      const avatarEl = document.getElementById('sango-avatar');
      const speakerEl = document.getElementById('sango-speaker');
      const dialogueEl = document.getElementById('sango-dialogue');
      const narrativeEl = document.getElementById('sango-narrative');
      const btnContainer = document.getElementById('sango-action-buttons');

      const s1 = document.getElementById('sango-step-1');
      const s2 = document.getElementById('sango-step-2');
      const s3 = document.getElementById('sango-step-3');

      // 단계별 하이라이트
      if (s1) s1.className = (sangoStage >= 1) ? 'p-1.5 rounded border-2 border-yellow-400 bg-amber-900 font-black text-yellow-300' : 'p-1.5 rounded border border-yellow-500 bg-amber-950/80 text-yellow-200';
      if (s2) s2.className = (sangoStage >= 2) ? 'p-1.5 rounded border-2 border-yellow-400 bg-amber-900 font-black text-yellow-300' : 'p-1.5 rounded border border-slate-700 bg-slate-900 text-slate-400';
      if (s3) s3.className = (sangoStage >= 3) ? 'p-1.5 rounded border-2 border-yellow-400 bg-emerald-900 font-black text-emerald-300' : 'p-1.5 rounded border border-slate-700 bg-slate-900 text-slate-400';

      if (sangoStage === 0) {
        // 제 1차 방문
        if (titleEl) titleEl.innerText = "[삼고초려 제 1차 방문] 융중의 와룡강, 닫힌 사립문";
        if (avatarEl) avatarEl.innerText = "🛖";
        if (speakerEl) speakerEl.innerText = "융중 초당의 동자";
        if (dialogueEl) dialogueEl.innerText = '"선생님께서는 학을 타고 세상을 유람하러 나가셨습니다. 언제 돌아오실지는 구름만이 알 뿐입니다..."';
        if (narrativeEl) narrativeEl.innerHTML = `
          <div>• <strong>장비(익덕):</strong> "형님! 이런 시골뜨기 서생 하나를 만나려고 우리가 찬바람을 맞고 와야 합니까?"</div>
          <div>• <strong>유비(현덕):</strong> "익덕아, 대업을 이루려면 천하의 대현을 얻어야 하거늘, 예를 다하지 않고 어찌 마음을 얻겠느냐! 다음에 다시 오자."</div>
        `;
        if (btnContainer) {
          btnContainer.innerHTML = `
            <button onclick="advanceSangoStep(1)" class="w-full sm:w-auto px-6 py-2.5 rounded-lg bg-gradient-to-r from-amber-700 to-yellow-600 hover:from-amber-600 hover:to-yellow-500 text-yellow-100 font-black text-xs border border-yellow-300 shadow-xl flex items-center justify-center gap-1.5 cursor-pointer">
              <span>🚶</span> <span>정중히 예를 표하고 회군 (제 1차 방문 완료)</span>
            </button>
          `;
        }

      } else if (sangoStage === 1) {
        // 제 2차 방문
        if (titleEl) titleEl.innerText = "[삼고초려 제 2차 방문] 눈보라 치는 한겨울의 융중";
        if (avatarEl) avatarEl.innerText = "❄️";
        if (speakerEl) speakerEl.innerText = "제갈균 (공명의 아우)";
        if (dialogueEl) dialogueEl.innerText = '"형님께서는 며칠 전 친구들과 시를 읊으러 나가 아직 소식이 없습니다. 날씨가 이리 험한데 찾아주셔서 감사할 따름입니다."';
        if (narrativeEl) narrativeEl.innerHTML = `
          <div>• <strong>유비(현덕):</strong> 정성껏 먹을 갈아 친필 서찰을 남긴다. <em>"한실 종친 유비, 삼가 선생의 고결한 덕망을 흠모하여 천하 백성을 구할 방책을 청하옵니다..."</em></div>
          <div>• <strong>관우(운장):</strong> "형님의 정성이 하늘을 찌르니, 선생도 이 글을 보면 마음을 열 것입니다."</div>
        `;
        if (btnContainer) {
          btnContainer.innerHTML = `
            <button onclick="advanceSangoStep(2)" class="w-full sm:w-auto px-6 py-2.5 rounded-lg bg-gradient-to-r from-blue-700 to-indigo-600 hover:from-blue-600 hover:to-indigo-500 text-cyan-100 font-black text-xs border border-cyan-300 shadow-xl flex items-center justify-center gap-1.5 cursor-pointer">
              <span>📜</span> <span>서찰을 남기고 봄을 기약 (제 2차 방문 완료)</span>
            </button>
          `;
        }

      } else if (sangoStage === 2) {
        // 제 3차 대망의 방문
        if (titleEl) titleEl.innerText = "[삼고초려 제 3차 방문] 봄날의 오수(午睡), 와룡이 눈을 뜨다!";
        if (avatarEl) avatarEl.innerText = "🪭";
        if (speakerEl) speakerEl.innerText = "초당 안의 풍경";
        if (dialogueEl) dialogueEl.innerText = '"대몽을 뉘 먼저 깨달았는가? 평생을 내 스스로 아노라. 초당에 봄잠이 넉넉하니 창밖의 해는 더디게 가네..."';
        if (narrativeEl) narrativeEl.innerHTML = `
          <div>• <strong>장비(익덕):</strong> "이 선생 놈이 우리 형님이 뜰 아래 두 시간이나 서 계시는데 낮잠을 자? 뒤꼍에 불을 질러 깨우겠습니다!"</div>
          <div>• <strong>유비(현덕):</strong> "익덕아 무례하다! 물러서 있거라!" 유비는 공명이 깰 때까지 두 손을 모으고 조용히 기다린다.</div>
          <div class="text-yellow-300 font-bold">• 마침내 깨어난 공명이 유비의 지극한 정성에 감복하여 [천하삼분지계]를 설파합니다!</div>
        `;
        if (btnContainer) {
          btnContainer.innerHTML = `
            <button onclick="recruitZhugeLiangFinal()" class="w-full sm:w-auto px-8 py-3 rounded-lg bg-gradient-to-r from-emerald-600 via-teal-500 to-emerald-600 hover:from-emerald-500 hover:to-teal-400 text-white font-black text-sm border-2 border-yellow-300 shadow-2xl flex items-center justify-center gap-2 animate-bounce cursor-pointer">
              <span>🌟</span> <span>[천하삼분지계 출사] 지력 100 제갈량 아군 영입!</span>
            </button>
          `;
        }

      } else {
        // 합류 완료 상태 (제갈량 보유 & 방통 등용 안내)
        if (titleEl) titleEl.innerText = "[영웅 집결] 천재 군사 제갈공명 출사 완료!";
        if (avatarEl) avatarEl.innerText = "🪭";
        if (speakerEl) speakerEl.innerText = "군사 제갈량 (공명)";
        if (dialogueEl) dialogueEl.innerText = '"주공의 삼고초려 은혜에 보답하고자, 이 한 몸 바쳐 한실을 부흥시키고 천하를 평정하겠습니다!"';
        if (narrativeEl) narrativeEl.innerHTML = `
          <div class="text-emerald-300 font-bold">• 제갈공명이 아군 최고 군사로 전격 취임하였습니다! (지력 100 만점 / 통솔 98 / 신산귀모 대화계 특기 해금)</div>
          <div class="text-slate-300">• 봉추 방통(龐統, 지력 98)도 곧 형주로 찾아올 조짐입니다!</div>
        `;
        if (btnContainer) {
          btnContainer.innerHTML = `
            ${!pangtongRecruited ? `
              <button onclick="recruitPangTongSpecial()" class="px-5 py-2.5 rounded-lg bg-gradient-to-r from-purple-800 to-indigo-700 hover:from-purple-700 hover:to-indigo-600 text-yellow-200 font-black text-xs border border-yellow-400 shadow-xl cursor-pointer">
                <span>🐦</span> <span>[봉추 영입] 지력 98 방통(龐統) 부군사 등용</span>
              </button>
            ` : '<span class="text-xs text-yellow-300 font-bold">✨ 와룡과 봉추를 모두 얻어 천하통일이 눈앞입니다!</span>'}
            <button onclick="closeModal('sango-modal')" class="px-5 py-2.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-white font-bold text-xs border border-slate-600">
              확인 및 전장 복귀
            </button>
          `;
        }
      }
    }

    function advanceSangoStep(step) {
      sangoStage = step;
      playSfx('fanfare');
      if (step === 1) {
        logMessage("📜 [삼고초려 1차 방문] 유비가 융중 와룡강을 찾았으나 공명이 부재중이라 예를 다하고 물러났습니다. (군주 인덕 상승)", "text-yellow-300 font-bold");
      } else if (step === 2) {
        logMessage("❄️ [삼고초려 2차 방문] 눈보라 속에서 유비가 공명에게 간절한 친필 서찰을 남겼습니다. (전군 사기 충천!)", "text-cyan-300 font-bold");
      }
      renderSangoStageUI();
    }

    function recruitZhugeLiangFinal() {
      sangoStage = 3;
      playSound('fanfare');

      // MY_OFFICERS에 제갈량 등록 (이미 없으면 추가)
      const exists = MY_OFFICERS.some(o => o.id === 'zhuge_liang' || o.name.includes('제갈량'));
      if (!exists) {
        MY_OFFICERS.unshift({
          id: 'zhuge_liang',
          name: '제갈량 (공명)',
          war: 65,
          int: 100, // 천하제일 지력 100 만점!
          lead: 98,
          icon: '🪭',
          title: '와룡 선생 (신산귀모)',
          hp: 100,
          fatigue: 0,
          element: 'wind',
          elemIcon: '🌪️',
          elemName: '바람 (風 - 동남풍)',
          level: 5,
          exp: 300,
          troopType: 'tactician',
          troopName: '제갈연노병 (팔진도)'
        });
      }

      // 전국 군사력 & 지력 보너스
      const myProv = getMyCapital();
      if (myProv) {
        myProv.soldiers = Math.min(50000, myProv.soldiers + 5000);
        myProv.order = 100;
      }

      logMessage("🌟🎉 [삼고초려 대성공!] 지력 100 만점의 천재 군사 제갈량(공명)이 유비군에 전격 합류했습니다! (신산귀모 대화계 & 제갈연노병 해금)", "text-yellow-300 font-extrabold text-base");
      alert("🌟 [와룡 출려(臥龍出廬) 삼고초려 대성공!]\\n\\n천재 군사 제갈량(공명)이 유비의 삼고초려에 감복하여 [천하삼분지계]를 올리고 출사표를 던졌습니다!\\n\\n▶ 지력 100 (천하 만점) / 통솔 98\\n▶ 특수 병종: 제갈연노병 & 동남풍 대화계 해금!\\n▶ 지원 의용군 5,000명 즉시 무상 합류!");

      renderSangoStageUI();
      renderMapPins();
      if (myProv) updateRightPanel(myProv.id);
    }

    function recruitPangTongSpecial() {
      pangtongRecruited = true;
      playSound('fanfare');

      const exists = MY_OFFICERS.some(o => o.id === 'pang_tong' || o.name.includes('방통'));
      if (!exists) {
        MY_OFFICERS.push({
          id: 'pang_tong',
          name: '방통 (사원)',
          war: 60,
          int: 98,
          lead: 89,
          icon: '🐦',
          title: '봉추 선생 (연환계)',
          hp: 100,
          fatigue: 0,
          element: 'fire',
          elemIcon: '🔥',
          elemName: '불 (火)',
          level: 4,
          exp: 250,
          troopType: 'tactician',
          troopName: '화계도사부대'
        });
      }

      logMessage("🐦🔥 [봉추 방통 등용] 연환계의 대가 봉추 방통(지력 98)이 유비군의 부군사로 등용되었습니다!", "text-purple-300 font-extrabold");
      alert("🐦 [봉추 방통(龐統) 등용 완료!]\\n\\n지력 98의 기재, 봉추 방통이 부군사로 합류했습니다!\\n\\n와룡(제갈량)과 봉추(방통)를 모두 거느린 유비의 천하통일 대업이 완성됩니다!");

      renderSangoStageUI();
      const myProv = getMyCapital();
      if (myProv) updateRightPanel(myProv.id);
    }

    // 장수 수색 시 삼고초려 안내 연동
    const origExecuteSearchOfficer = window.executeSearchOfficer || executeSearchOfficer;
    function executeSearchOfficer() {
      closeAllPopups();
      playSfx('select');
      if (sangoStage < 3) {
        if (confirm("🔍 [인재 탐문 - 남양 와룡강의 소문]\\n\\n형주 백성들이 '남양 땅 융중에 천하의 대현 제갈공명이 은거하고 있다'고 전합니다!\\n\\n지금 바로 [삼고초려(三顧草廬)]를 떠나시겠습니까?")) {
          openSangoModal();
          return;
        }
      }
      const myProv = getMyCapital();
      const foundNames = ['마량 (백미)', '서서 (원직)', '간옹 (헌화)', '미축 (자중)', '손건 (공우)', '이적 (기백)'];
      const picked = foundNames[Math.floor(Math.random() * foundNames.length)];
      logMessage(`🔍 [장수 수색] ${myProv.name} 일대에서 재야의 현사 '${picked}'을(를) 탐문 발견했습니다!`, 'text-yellow-300 font-bold');
      alert(`🔍 [인재 탐문!]\\n\\n${myProv.name}의 산야에서 은거 중이던 현사 [${picked}]을(를) 찾아내었습니다!\\n군주의 덕망에 이끌려 조만간 출사를 약속했습니다.`);
    }

    // 키보드 단축키 'Z' 또는 'z' 누르면 삼고초려 모달 직행
    document.addEventListener('keydown', (e) => {
      if (['INPUT', 'SELECT', 'TEXTAREA'].includes(e.target.tagName)) return;
      if (e.key === 'z' || e.key === 'Z') {
        e.preventDefault();
        openSangoModal();
      }
    });
'''

# Insert sango_js before closing </script>
last_script_idx = html.rfind('</script>')
html = html[:last_script_idx] + '\n' + sango_js + '\n' + html[last_script_idx:]

open(target_html_path, 'w', encoding='utf-8').write(html)

# Syntax check
scripts = re.findall(r'<script(?:\s+[^>]*)?>(.*?)</script>', html, re.DOTALL)
for idx, sc in enumerate(scripts):
    tmp = f'temp_verify_{idx}.js'
    open(tmp, 'w', encoding='utf-8').write(sc)
    r = subprocess.run(['node', '--check', tmp], capture_output=True)
    if r.returncode != 0:
        print(f'SYNTAX ERROR in script {idx}:', r.stderr.decode('utf-8', errors='replace')[:500])
        sys.exit(1)
print('Node.js syntax check: 100% VALID JS!')

# Copy to all 5 files
targets = [
    r'C:\Users\LENOVO\Desktop\삼국지_황제의결단_웹게임.html',
    r'G:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\index.html',
    r'G:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\samgukji.html',
    r'G:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\교육학\index.html',
    r'G:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\교육학\samgukji.html'
]
for tgt in targets:
    shutil.copy2(target_html_path, tgt)
print('All 6 files updated with Zhuge Liang & Sango system!')
