# -*- coding: utf-8 -*-
import os
import json
import re

def build():
    print("=== 삼국지 3 + 삼국지 5 헥스 전장 궁극 마스터 HTML 빌드 시작 ===")

    brain_dir = r"C:\Users\LENOVO\.gemini\antigravity\brain\54a65f4d-a058-4307-83a1-d8dec8bb9bb0"
    assets_json = os.path.join(brain_dir, "samguk_b64_assets.json")

    with open(assets_json, "r", encoding="utf-8") as f:
        assets = json.load(f)

    map_b64 = assets["map_b64"]
    liubei_b64 = assets["portraits"]["liubei"]
    portraits_json = json.dumps(assets["portraits"])

    # 1. runner 스크립트에서 html_code 템플릿 추출
    base_runner_path = r"g:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\교육학\scratch\build_samguk3_war_fixed_runner.py"
    with open(base_runner_path, "r", encoding="utf-8") as f:
        raw_script = f.read()

    start_tag = "html_code = r'''"
    end_tag = "'''\n\n    print(\"Replacing placeholders...\")"
    
    start_pos = raw_script.find(start_tag) + len(start_tag)
    end_pos = raw_script.find(end_tag)

    if start_pos == -1 or end_pos == -1:
        # alternative end tag
        end_tag2 = "'''"
        end_pos = raw_script.rfind("    print(\"Replacing placeholders...\")")
        end_pos = raw_script.rfind("'''", 0, end_pos)
        html_template = raw_script[start_pos:end_pos]
    else:
        html_template = raw_script[start_pos:end_pos]

    print(f"Extracted html_template: {len(html_template):,} chars")

    # 2. sam5 부품 읽기
    with open("scratch/sam5_css.txt", "r", encoding="utf-8") as f:
        sam5_css = f.read()

    with open("scratch/sam5_body.txt", "r", encoding="utf-8") as f:
        sam5_body = f.read()

    with open("scratch/sam5_script.txt", "r", encoding="utf-8") as f:
        sam5_script = f.read()

    # 3. 인트로 12대 군주 선택 모달 HTML
    intro_modal_html = """
  <!-- ==================== 🔥 [오프닝] 12대 군주 선택 & 시나리오 설정 모달 ==================== -->
  <div id="intro-ruler-select-modal" class="fixed inset-0 modal-backdrop z-[999999] flex items-center justify-center p-3 bg-black/95">
    <div class="koei-box w-full max-w-4xl p-5 rounded-lg shadow-2xl border-4 border-amber-400 max-h-[95vh] flex flex-col justify-between overflow-y-auto">
      
      <!-- 헤더 -->
      <div class="border-b-2 border-amber-400 pb-3 mb-3 flex items-center justify-between">
        <div class="flex items-center gap-3">
          <span class="text-3xl animate-bounce">👑</span>
          <div>
            <h1 class="text-xl font-black text-yellow-300 text-pixel tracking-wider">
              삼국지 III (三國志 III) 황제의 결단 : 군웅할거
            </h1>
            <div class="text-xs text-amber-200 mt-0.5">
              서기 194년 봄, 천하가 12군벌로 나뉘었습니다. 천하통일을 이룰 군주를 선택하십시오!
            </div>
          </div>
        </div>
        <div class="text-right">
          <span class="px-3 py-1 bg-blue-950 border border-blue-500 rounded text-xs text-cyan-300 font-bold">
            1. 시나리오 : 2. 난세, 군웅 전토를 할거
          </span>
        </div>
      </div>

      <!-- 난이도 설정 바 -->
      <div class="bg-blue-950/80 border border-amber-500/60 p-3 rounded mb-3 flex items-center justify-between">
        <div class="flex items-center gap-2">
          <span class="text-amber-400 font-bold text-xs">3. 게임레벨 (난이도) :</span>
          <div class="flex gap-2">
            <button onclick="setIntroDifficulty('hard')" id="intro-diff-hard" class="px-3 py-1 text-xs font-black rounded border-2 border-red-500 bg-red-900 text-yellow-200 shadow ring-2 ring-red-400">
              🔥 상급 (어려움)
            </button>
            <button onclick="setIntroDifficulty('normal')" id="intro-diff-normal" class="px-3 py-1 text-xs font-bold rounded border border-blue-500 bg-blue-900 text-slate-200 hover:bg-blue-800">
              ⚖️ 중급 (보통)
            </button>
            <button onclick="setIntroDifficulty('easy')" id="intro-diff-easy" class="px-3 py-1 text-xs font-bold rounded border border-emerald-500 bg-emerald-950 text-slate-300 hover:bg-emerald-900">
              🌱 초급 (쉬움)
            </button>
          </div>
        </div>
        <div class="text-[11px] text-slate-300">
          💡 상급은 적 군벌의 침공과 무력이 강화되어 실전 코에이의 긴장감을 만끽할 수 있습니다.
        </div>
      </div>

      <!-- 12대 군주 선택 카드 그리드 -->
      <div class="mb-3">
        <div class="text-xs text-amber-300 font-bold mb-2 flex items-center justify-between">
          <span>🚩 플레이할 군주를 선택하십시오 (클릭하여 선택):</span>
          <span id="selected-ruler-announce" class="text-yellow-300 font-black">현재 선택: 유비 (형주 8번)</span>
        </div>
        <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-6 gap-2.5" id="intro-ruler-grid">
          <!-- 1. 공손찬 -->
          <div onclick="selectIntroRuler('공손찬', 1, 'gongsongzan')" class="intro-ruler-card p-2 rounded border-2 cursor-pointer transition flex flex-col items-center bg-blue-950/90 border-blue-700 hover:border-yellow-400" id="card-공손찬">
            <img id="intro-face-gongsongzan" class="w-16 h-20 object-cover rounded border border-amber-500/80 mb-1.5 shadow" alt="공손찬">
            <div class="font-black text-xs text-white">1. 공손찬</div>
            <div class="text-[10px] text-amber-300 font-bold bg-amber-950/80 px-2 py-0.5 rounded border border-amber-600 mt-1">북평 (유주)</div>
          </div>
          <!-- 2. 원소 -->
          <div onclick="selectIntroRuler('원소', 2, 'yuanshao_retro')" class="intro-ruler-card p-2 rounded border-2 cursor-pointer transition flex flex-col items-center bg-blue-950/90 border-blue-700 hover:border-yellow-400" id="card-원소">
            <img id="intro-face-yuanshao_retro" class="w-16 h-20 object-cover rounded border border-amber-500/80 mb-1.5 shadow" alt="원소">
            <div class="font-black text-xs text-white">2. 원소</div>
            <div class="text-[10px] text-yellow-300 font-bold bg-yellow-950/80 px-2 py-0.5 rounded border border-yellow-600 mt-1">남피 (기주)</div>
          </div>
          <!-- 3. 공융 -->
          <div onclick="selectIntroRuler('공융', 3, 'gongyong')" class="intro-ruler-card p-2 rounded border-2 cursor-pointer transition flex flex-col items-center bg-blue-950/90 border-blue-700 hover:border-yellow-400" id="card-공융">
            <img id="intro-face-gongyong" class="w-16 h-20 object-cover rounded border border-amber-500/80 mb-1.5 shadow" alt="공융">
            <div class="font-black text-xs text-white">3. 공융</div>
            <div class="text-[10px] text-orange-300 font-bold bg-orange-950/80 px-2 py-0.5 rounded border border-orange-600 mt-1">북해 (청주)</div>
          </div>
          <!-- 4. 유요 -->
          <div onclick="selectIntroRuler('유요', 7, 'liuyao')" class="intro-ruler-card p-2 rounded border-2 cursor-pointer transition flex flex-col items-center bg-blue-950/90 border-blue-700 hover:border-yellow-400" id="card-유요">
            <img id="intro-face-liuyao" class="w-16 h-20 object-cover rounded border border-amber-500/80 mb-1.5 shadow" alt="유요">
            <div class="font-black text-xs text-white">4. 유요</div>
            <div class="text-[10px] text-lime-300 font-bold bg-lime-950/80 px-2 py-0.5 rounded border border-lime-600 mt-1">수춘 (양주)</div>
          </div>
          <!-- 5. 손책 -->
          <div onclick="selectIntroRuler('손책', 7, 'sunce')" class="intro-ruler-card p-2 rounded border-2 cursor-pointer transition flex flex-col items-center bg-blue-950/90 border-blue-700 hover:border-yellow-400" id="card-손책">
            <img id="intro-face-sunce" class="w-16 h-20 object-cover rounded border border-amber-500/80 mb-1.5 shadow" alt="손책">
            <div class="font-black text-xs text-white">5. 손책</div>
            <div class="text-[10px] text-red-300 font-bold bg-red-950/80 px-2 py-0.5 rounded border border-red-600 mt-1">노강 (양주)</div>
          </div>
          <!-- 6. 왕랑 -->
          <div onclick="selectIntroRuler('왕랑', 7, 'wanglang')" class="intro-ruler-card p-2 rounded border-2 cursor-pointer transition flex flex-col items-center bg-blue-950/90 border-blue-700 hover:border-yellow-400" id="card-왕랑">
            <img id="intro-face-wanglang" class="w-16 h-20 object-cover rounded border border-amber-500/80 mb-1.5 shadow" alt="왕랑">
            <div class="font-black text-xs text-white">6. 왕랑</div>
            <div class="text-[10px] text-sky-300 font-bold bg-sky-950/80 px-2 py-0.5 rounded border border-sky-600 mt-1">회계 (양주)</div>
          </div>
          <!-- 7. 원술 -->
          <div onclick="selectIntroRuler('원술', 3, 'yuanshu')" class="intro-ruler-card p-2 rounded border-2 cursor-pointer transition flex flex-col items-center bg-blue-950/90 border-blue-700 hover:border-yellow-400" id="card-원술">
            <img id="intro-face-yuanshu" class="w-16 h-20 object-cover rounded border border-amber-500/80 mb-1.5 shadow" alt="원술">
            <div class="font-black text-xs text-white">7. 원술</div>
            <div class="text-[10px] text-pink-300 font-bold bg-pink-950/80 px-2 py-0.5 rounded border border-pink-600 mt-1">완 (예주)</div>
          </div>
          <!-- 8. 유표 -->
          <div onclick="selectIntroRuler('유표', 8, 'liubiao_retro')" class="intro-ruler-card p-2 rounded border-2 cursor-pointer transition flex flex-col items-center bg-blue-950/90 border-blue-700 hover:border-yellow-400" id="card-유표">
            <img id="intro-face-liubiao_retro" class="w-16 h-20 object-cover rounded border border-amber-500/80 mb-1.5 shadow" alt="유표">
            <div class="font-black text-xs text-white">8. 유표</div>
            <div class="text-[10px] text-cyan-300 font-bold bg-cyan-950/80 px-2 py-0.5 rounded border border-cyan-600 mt-1">양양 (형주)</div>
          </div>
          <!-- 9. 마등 -->
          <div onclick="selectIntroRuler('마등', 11, 'mateng_retro')" class="intro-ruler-card p-2 rounded border-2 cursor-pointer transition flex flex-col items-center bg-blue-950/90 border-blue-700 hover:border-yellow-400" id="card-마등">
            <img id="intro-face-mateng_retro" class="w-16 h-20 object-cover rounded border border-amber-500/80 mb-1.5 shadow" alt="마등">
            <div class="font-black text-xs text-white">9. 마등</div>
            <div class="text-[10px] text-teal-300 font-bold bg-teal-950/80 px-2 py-0.5 rounded border border-teal-600 mt-1">서량 (량주)</div>
          </div>
          <!-- 10. 조조 -->
          <div onclick="selectIntroRuler('조조', 13, 'caocao_retro')" class="intro-ruler-card p-2 rounded border-2 cursor-pointer transition flex flex-col items-center bg-blue-950/90 border-blue-700 hover:border-yellow-400" id="card-조조">
            <img id="intro-face-caocao_retro" class="w-16 h-20 object-cover rounded border border-amber-500/80 mb-1.5 shadow" alt="조조">
            <div class="font-black text-xs text-white">10. 조조</div>
            <div class="text-[10px] text-blue-300 font-bold bg-blue-950/80 px-2 py-0.5 rounded border border-blue-600 mt-1">낙양 (사례)</div>
          </div>
          <!-- 11. 여포 -->
          <div onclick="selectIntroRuler('여포', 6, 'lubu')" class="intro-ruler-card p-2 rounded border-2 cursor-pointer transition flex flex-col items-center bg-blue-950/90 border-blue-700 hover:border-yellow-400" id="card-여포">
            <img id="intro-face-lubu" class="w-16 h-20 object-cover rounded border border-amber-500/80 mb-1.5 shadow" alt="여포">
            <div class="font-black text-xs text-white">11. 여포</div>
            <div class="text-[10px] text-purple-300 font-bold bg-purple-950/80 px-2 py-0.5 rounded border border-purple-600 mt-1">복양 (연주)</div>
          </div>
          <!-- 12. 장노 -->
          <div onclick="selectIntroRuler('장노', 10, 'zhanglu')" class="intro-ruler-card p-2 rounded border-2 cursor-pointer transition flex flex-col items-center bg-blue-950/90 border-blue-700 hover:border-yellow-400" id="card-장노">
            <img id="intro-face-zhanglu" class="w-16 h-20 object-cover rounded border border-amber-500/80 mb-1.5 shadow" alt="장노">
            <div class="font-black text-xs text-white">12. 장노</div>
            <div class="text-[10px] text-green-300 font-bold bg-green-950/80 px-2 py-0.5 rounded border border-green-600 mt-1">한중 (익주)</div>
          </div>
        </div>
      </div>

      <!-- 하단 출진 버튼 -->
      <div class="border-t-2 border-amber-400 pt-3 flex items-center justify-between">
        <div class="text-xs text-slate-300">
          👑 선택한 군주로 천하 13주를 통일하고 한나라 황제에 즉위하십시오!
        </div>
        <button onclick="confirmIntroStart()" class="px-8 py-3 bg-gradient-to-r from-red-600 via-amber-600 to-red-600 hover:from-red-500 hover:to-amber-500 text-yellow-100 font-black text-sm rounded-lg border-2 border-yellow-300 shadow-2xl flex items-center gap-2 animate-pulse">
          <span>⚔️</span> 선택한 군주로 천하통일 출진!
        </button>
      </div>

    </div>
  </div>
"""

    # 4. 삼국지 5 헥스 전장 모달 컨테이너 HTML
    hex_battle_modal_html = f"""
  <!-- ==================== 🔥 삼국지 V (三國志 V) 헥스 전술 결전 모달 ==================== -->
  <div id="hex-battle-modal" class="fixed inset-0 modal-backdrop z-[99999] hidden flex flex-col items-center justify-center p-2 bg-black/90">
    <div class="koei-box w-full max-w-6xl p-2.5 rounded shadow-2xl border-4 border-yellow-500 max-h-[96vh] flex flex-col overflow-y-auto">
      
      <!-- 상단 헤더 및 후퇴 버튼 -->
      <div class="flex items-center justify-between border-b-2 border-yellow-600 pb-1.5 mb-2">
        <div class="flex items-center gap-2">
          <span class="text-xl">⚔️</span>
          <h2 id="hex-modal-title" class="text-base font-black text-yellow-300 text-pixel">
            [삼국지 V 헥스 전술 결전] 10턴 결전: 적 군량고 습격 & 일기토 대승 전략
          </h2>
        </div>
        <button onclick="closeHexBattle(false)" class="sam5-btn px-3 py-1 rounded text-xs bg-red-900 text-white font-bold border border-red-500">
          🏳️ 퇴각 (전장 이탈)
        </button>
      </div>

      <!-- 삼국지 5 실전 바디 임베딩 -->
      <div id="sam5-container" class="w-full flex-1">
        {sam5_body}
      </div>

    </div>
  </div>
"""

    # 5. 포로 처분 모달 (적장 등용 / 석방 / 참수)
    prisoner_modal_html = """
  <!-- ==================== 🔥 포로 처분 모달 (등용 / 석방 / 참수) ==================== -->
  <div id="prisoner-modal" class="fixed inset-0 modal-backdrop z-[999999] hidden flex items-center justify-center p-3 bg-black/85">
    <div class="koei-box w-full max-w-md p-4 rounded shadow-2xl border-4 border-amber-400 flex flex-col gap-3">
      <div class="flex items-center justify-between border-b-2 border-amber-400 pb-2">
        <div class="flex items-center gap-2">
          <span class="text-xl">⛓️</span>
          <h2 class="text-base font-black text-amber-300 text-pixel">[적장 생포] 포로 처분</h2>
        </div>
        <span class="px-2 py-0.5 rounded text-xs bg-red-950 border border-red-500 text-yellow-300 font-bold">생포 완료</span>
      </div>

      <!-- 포로 정보 카드 -->
      <div class="p-3 bg-blue-950/90 border border-amber-500/70 rounded-lg flex items-center gap-3">
        <div id="prisoner-icon" class="text-3xl p-2 bg-slate-900 rounded border border-amber-400">👤</div>
        <div class="space-y-1">
          <div id="prisoner-name" class="text-sm font-black text-yellow-200">적장</div>
          <div id="prisoner-stats" class="text-xs text-slate-300">무력: 95 | 지력: 70 | 통솔: 88</div>
          <div id="prisoner-title" class="text-[11px] text-cyan-300">적 군벌 주력 무장</div>
        </div>
      </div>

      <div class="text-xs text-slate-200 leading-relaxed bg-slate-900/80 p-2.5 rounded border border-blue-900">
        "주군, 전투에서 적장을 굴복시키고 생포하였습니다! 이 자를 어떻게 처분하시겠습니까?"
      </div>

      <div class="grid grid-cols-3 gap-2 pt-1">
        <button onclick="handlePrisonerRecruit()" class="py-2.5 rounded bg-gradient-to-b from-emerald-600 to-emerald-800 hover:from-emerald-500 hover:to-emerald-700 text-yellow-100 font-black text-xs shadow border border-emerald-400 flex flex-col items-center gap-0.5">
          <span>🤝 등 용</span>
          <span class="text-[10px] text-emerald-200 font-normal">(아군 장수 영입)</span>
        </button>
        <button onclick="handlePrisonerRelease()" class="py-2.5 rounded bg-gradient-to-b from-blue-700 to-blue-900 hover:from-blue-600 hover:to-blue-800 text-cyan-100 font-bold text-xs shadow border border-cyan-400 flex flex-col items-center gap-0.5">
          <span>🕊️ 석 방</span>
          <span class="text-[10px] text-cyan-200 font-normal">(민충·명성 +15)</span>
        </button>
        <button onclick="handlePrisonerExecute()" class="py-2.5 rounded bg-gradient-to-b from-rose-800 to-red-950 hover:from-rose-700 hover:to-red-900 text-red-200 font-black text-xs shadow border border-red-500 flex flex-col items-center gap-0.5">
          <span>⚔️ 참 수</span>
          <span class="text-[10px] text-red-300 font-normal">(적 전력 영구제거)</span>
        </button>
      </div>
    </div>
  </div>
"""

    # 6. 추가되는 통합 자바스크립트
    integrated_js = f"""
    // ==================== 🔥 삼국지 5 헥스 전술 전장 엔진 통합 ====================
    let hexBattleContext = {{
      targetProv: null,
      fromProv: null,
      capturedOfficer: null
    }};

    function openHexBattle(targetProv, fromProv) {{
      closeAllPopups();
      hexBattleContext.targetProv = targetProv;
      hexBattleContext.fromProv = fromProv;
      hexBattleContext.capturedOfficer = null;

      document.getElementById('hex-modal-title').innerText = `[삼국지 V 헥스 전술 결전] ${{fromProv.name}} ➔ ${{targetProv.name}} (${{gameState.rulerName}}군 vs ${{targetProv.ruler}}군)`;

      if (typeof restartBattle === 'function') {{
        restartBattle();
      }}

      openModal('hex-battle-modal');
      logMessage(`⚔️ [전술 결전 개시] ${{fromProv.name}}의 아군이 ${{targetProv.name}}의 ${{targetProv.ruler}}군을 상대로 10턴 헥스 결전에 돌입했습니다!`, 'text-yellow-300 font-black');
    }}

    function closeHexBattle(isVictory = false) {{
      closeModal('hex-battle-modal');
      if (isVictory && hexBattleContext.targetProv) {{
        onHexBattleVictory(hexBattleContext.targetProv);
      }}
    }}

    function onHexBattleVictory(targetProv) {{
      playSfx('victory');
      const prevRuler = targetProv.ruler;
      targetProv.ruler = gameState.rulerName;
      targetProv.leader = gameState.rulerName;
      targetProv.defense = 50;

      // 생포할 적장 결정
      const enemyList = ENEMY_OFFICERS_BY_RULER[prevRuler] || [
        {{ name: `${{prevRuler}}의 맹장`, war: 88, int: 65, lead: 84, icon: '🛡️', title: '적 수비대장' }}
      ];
      const captured = enemyList[Math.floor(Math.random() * enemyList.length)];
      hexBattleContext.capturedOfficer = captured;

      renderMapPins();
      updateRightPanel(targetProv.id);
      checkUnification();

      // 포로 처분 모달 띄우기
      showPrisonerModal(captured);
    }}

    // ==================== 🔥 포로 처분 (등용 / 석방 / 참수) ====================
    function showPrisonerModal(off) {{
      document.getElementById('prisoner-name').innerText = off.name;
      document.getElementById('prisoner-icon').innerText = off.icon || '👤';
      document.getElementById('prisoner-stats').innerText = `무력: ${{off.war}} | 지력: ${{off.int}} | 통솔: ${{off.lead || 80}}`;
      document.getElementById('prisoner-title').innerText = off.title || '적군 명장';
      openModal('prisoner-modal');
    }}

    function handlePrisonerRecruit() {{
      const off = hexBattleContext.capturedOfficer;
      closeModal('prisoner-modal');
      if (!off) return;

      const isLiuBei = (gameState.rulerName === '유비');
      const successChance = isLiuBei ? 0.80 : 0.65;

      if (Math.random() < successChance) {{
        MY_OFFICERS.push({{
          id: 'recruited_' + Date.now(),
          name: off.name,
          war: off.war,
          int: off.int,
          lead: off.lead || 80,
          icon: off.icon || '⚔️',
          title: `[등용] ${{off.title || '귀순 장수'}}`,
          hp: 100
        }});
        playSfx('victory');
        alert(`🎉 [등용 성공!]\\n${{off.name}}이 ${{gameState.rulerName}}의 큰 뜻과 인덕에 감복하여 충성을 맹세했습니다!\\n이제부터 아군 맹장으로 1:1 결투 및 전투에 출전시킬 수 있습니다!`);
        logMessage(`👑 [장수 등용] ${{off.name}}이 아군 진영에 합류했습니다! (보유 장수: ${{MY_OFFICERS.length}}명)`, 'text-yellow-300 font-black');
      }} else {{
        alert(`⚠️ ${{off.name}}이 끝내 고개를 저으며 등용을 거부하여 군감에 수감하였습니다.`);
        logMessage(`⛓️ ${{off.name}}이 등용을 거부하여 감옥에 가두었습니다.`, 'text-slate-400');
      }}
    }}

    function handlePrisonerRelease() {{
      const off = hexBattleContext.capturedOfficer;
      closeModal('prisoner-modal');
      if (!off) return;

      const myProv = getMyCapital();
      myProv.loyalty = Math.min(100, myProv.loyalty + 15);
      myProv.gold += 300;
      updateRightPanel(myProv.id);

      playSfx('build');
      alert(`🕊️ [석방]\\n${{off.name}}의 오랏줄을 풀어주고 후하게 대접하여 돌려보냈습니다.\\n주군의 고결한 인덕이 천하에 퍼져 민충이 15 올랐습니다! (명성 상승)`);
      logMessage(`🕊️ [석방] ${{off.name}}을 풀어주어 천하에 인덕을 떨쳤습니다! (민충 +15)`, 'text-cyan-300 font-bold');
    }}

    function handlePrisonerExecute() {{
      const off = hexBattleContext.capturedOfficer;
      closeModal('prisoner-modal');
      if (!off) return;

      playTone(180, 0.4, 'sawtooth', 0.3);
      alert(`⚔️ [참수]\\n${{off.name}}의 목을 베어 군문 앞에 효수하였습니다!\\n적 군벌의 주력 무장이 영구히 제거되었습니다.`);
      logMessage(`⚔️ [처형] 적장 ${{off.name}}을 참수하여 적의 기세를 꺾었습니다!`, 'text-red-400 font-black');
    }}

    // ==================== 🔥 인트로 12대 군주 선택 로직 ====================
    let selectedIntroRulerName = '유비';
    let selectedIntroProvId = 8;
    let selectedIntroKey = 'liubei';

    function selectIntroRuler(name, provId, key) {{
      selectedIntroRulerName = name;
      selectedIntroProvId = provId;
      selectedIntroKey = key;

      document.querySelectorAll('.intro-ruler-card').forEach(el => {{
        el.classList.remove('border-yellow-400', 'ring-2', 'ring-yellow-300', 'bg-blue-900');
        el.classList.add('border-blue-700');
      }});

      const targetCard = document.getElementById('card-' + name);
      if (targetCard) {{
        targetCard.classList.remove('border-blue-700');
        targetCard.classList.add('border-yellow-400', 'ring-2', 'ring-yellow-300', 'bg-blue-900');
      }}

      document.getElementById('selected-ruler-announce').innerText = `현재 선택: ${{name}} (${{PROVINCES.find(p=>p.id===provId)?.name || ''}} ${{provId}}번)`;
      playTone(520, 0.08, 'sine', 0.15);
    }}

    function setIntroDifficulty(level) {{
      setDifficulty(level);
      const bHard = document.getElementById('intro-diff-hard');
      const bNormal = document.getElementById('intro-diff-normal');
      const bEasy = document.getElementById('intro-diff-easy');
      if (bHard) bHard.className = (level==='hard') ? 'px-3 py-1 text-xs font-black rounded border-2 border-red-500 bg-red-900 text-yellow-200 shadow ring-2 ring-red-400' : 'px-3 py-1 text-xs font-bold rounded border border-red-900 bg-slate-900 text-slate-400';
      if (bNormal) bNormal.className = (level==='normal') ? 'px-3 py-1 text-xs font-black rounded border-2 border-blue-500 bg-blue-900 text-yellow-200 shadow ring-2 ring-blue-400' : 'px-3 py-1 text-xs font-bold rounded border border-blue-900 bg-slate-900 text-slate-400';
      if (bEasy) bEasy.className = (level==='easy') ? 'px-3 py-1 text-xs font-black rounded border-2 border-emerald-500 bg-emerald-900 text-yellow-200 shadow ring-2 ring-emerald-400' : 'px-3 py-1 text-xs font-bold rounded border border-emerald-900 bg-slate-900 text-slate-400';
    }}

    function confirmIntroStart() {{
      closeModal('intro-ruler-select-modal');
      changeRuler(selectedIntroRulerName, selectedIntroProvId, selectedIntroKey);
      playSfx('victory');
      logMessage(`👑 [거병 개시] 군주 '${{selectedIntroRulerName}}'으로 난세를 평정하기 위한 대장정에 올랐습니다!`, 'text-yellow-300 font-extrabold text-sm');
    }}

    function setupIntroFaces() {{
      const p = PORTRAITS;
      const setImg = (id, key) => {{ const el = document.getElementById(id); if (el && p[key]) el.src = p[key]; }};
      setImg('intro-face-gongsongzan', 'gongsongzan');
      setImg('intro-face-yuanshao_retro', 'yuanshao_retro');
      setImg('intro-face-gongyong', 'gongyong');
      setImg('intro-face-liuyao', 'liuyao');
      setImg('intro-face-sunce', 'sunce');
      setImg('intro-face-wanglang', 'wanglang');
      setImg('intro-face-yuanshu', 'yuanshu');
      setImg('intro-face-liubiao_retro', 'liubiao_retro');
      setImg('intro-face-mateng_retro', 'mateng_retro');
      setImg('intro-face-caocao_retro', 'caocao_retro');
      setImg('intro-face-lubu', 'lubu');
      setImg('intro-face-zhanglu', 'zhanglu');
    }}

    // ==================== 🔥 삼국지 5 헥스 전장 스크립트 임베딩 ====================
    {sam5_script}
"""

    # 7. openWarModal을 헥스 전장 호출로 전환
    war_modal_hex_replacement = """
      // 4. 전투 데이터 초기화
      battleData.targetProv = target;
      battleData.fromProv = myProv;
      battleData.turn = 1;
      battleData.myPower = 100;
      battleData.enemyPower = 100;
      battleData.mySoldiers = myProv.soldiers;
      battleData.enemySoldiers = target.soldiers;
      battleData.storageHp = gameState.storageHp;

      // 🔥 삼국지 5 헥스 전술 전장으로 즉시 진입!
      openHexBattle(target, myProv);
      return;
"""

    # 8. HTML 템플릿에 부품 결합
    # (A) CSS 주입
    html_template = html_template.replace("</style>", f"\n{sam5_css}\n</style>")

    # (B) 모달 HTML 주입
    modal_insert_marker = '<!-- ==================== 침공 목표 적 영지 선택 모달'
    modals_all = intro_modal_html + "\n" + hex_battle_modal_html + "\n" + prisoner_modal_html + "\n"
    if modal_insert_marker in html_template:
        html_template = html_template.replace(modal_insert_marker, modals_all + "\n" + modal_insert_marker)
    else:
        html_template = html_template.replace("</body>", modals_all + "\n</body>")

    # (C) JS 주입
    html_template = html_template.replace("</script>\n</body>", f"\n{integrated_js}\n</script>\n</body>")

    # (D) openWarModal 내부를 헥스 전장 호출로 전환
    pattern_open_battle = r"// 4\. 전투 데이터 초기화[\s\S]*?openModal\('battle-modal'\);"
    if re.search(pattern_open_battle, html_template):
        html_template = re.sub(pattern_open_battle, war_modal_hex_replacement.strip(), html_template)
        print("Successfully linked openWarModal to Hex Battle!")

    # (E) DOMContentLoaded 시 인트로 모달 띄우기 및 얼굴 세팅
    dom_hook = "window.addEventListener('DOMContentLoaded', () => {"
    dom_inject = """window.addEventListener('DOMContentLoaded', () => {
      setupIntroFaces();
      openModal('intro-ruler-select-modal');"""
    html_template = html_template.replace(dom_hook, dom_inject)

    # 9. 플레이스홀더 치환 (Map & Portraits Base64 완전 임베딩!)
    print("Replacing Map & Portrait Base64 placeholders...")
    final_html = html_template.replace("__MAP_B64__", map_b64)
    final_html = final_html.replace("__PORTRAITS_JSON__", portraits_json)
    final_html = final_html.replace("__LIUBEI_B64__", liubei_b64)

    # 10. 대상 파일들에 최종 배포
    target_paths = [
        r"C:\Users\LENOVO\Desktop\삼국지_황제의결단_웹게임.html",
        r"C:\Users\LENOVO\Desktop\sam3_update.html",
        r"g:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\samgukji.html",
        r"g:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\교육학\samgukji.html"
    ]

    for p in target_paths:
        try:
            with open(p, "w", encoding="utf-8") as f:
                f.write(final_html)
            print(f"Generated: {p} ({len(final_html):,} bytes)")
        except Exception as e:
            print(f"Failed {p}: {e}")

    print("=== 모든 궁극 마스터 HTML 빌드 완료! ===")

if __name__ == "__main__":
    build()
