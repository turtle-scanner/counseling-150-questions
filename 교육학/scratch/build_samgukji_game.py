import json, os

with open(r'C:\Users\LENOVO\.gemini\antigravity\brain\54a65f4d-a058-4307-83a1-d8dec8bb9bb0\samguk_b64_assets.json', 'r', encoding='utf-8') as f:
    b64_data = json.load(f)

map_b64 = b64_data['map_b64']
portraits_b64 = b64_data['portraits']
rulers_banner_b64 = b64_data['rulers_banner']

html_template = '''<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>삼국지 3 (三國志 III) 웹 에디션 - 13주 천하통일</title>
  <script src="https://www.gstatic.com/antigravity/web/dev/tailwindcss.min.js"></script>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Serif+KR:wght@600;900&family=Nanum+Gothic+Coding:wght@700&display=swap');

    body {
      font-family: 'Nanum Gothic Coding', 'Noto Serif KR', monospace, serif;
      background-color: #030712;
      color: #e2e8f0;
      user-select: none;
    }

    /* 삼국지 3 코에이 클래식 네이비 더블 골드 프레임 */
    .koei-box {
      background: #000080;
      border: 3px double #d4af37;
      box-shadow: 2px 2px 0px #000, inset 1px 1px 0px #ffd700;
    }

    .koei-header-btn {
      background: #000066;
      border: 1px solid #d4af37;
      color: #fef08a;
      transition: all 0.15s ease;
    }
    .koei-header-btn:hover {
      background: #1e3a8a;
      color: #ffffff;
      transform: translateY(-1px);
    }

    /* 13주 지도 위 인터랙티브 거점 핀 */
    .prov-pin {
      position: absolute;
      transform: translate(-50%, -50%);
      cursor: pointer;
      transition: all 0.2s ease;
      z-index: 20;
    }
    .prov-pin:hover {
      transform: translate(-50%, -50%) scale(1.15);
      z-index: 35;
      filter: drop-shadow(0 0 10px #f59e0b);
    }
    .prov-pin-active {
      transform: translate(-50%, -50%) scale(1.22);
      z-index: 40;
      filter: drop-shadow(0 0 14px #38bdf8);
    }

    /* 삼국지 3 고유의 청룡/물결 문양 게이지 바 */
    .dragon-gauge-bg {
      background: #0b1528;
      border: 1px solid #38bdf8;
      height: 12px;
      position: relative;
      overflow: hidden;
    }
    .dragon-gauge-fill {
      background: linear-gradient(90deg, #10b981 0%, #06b6d4 100%);
      height: 100%;
      transition: width 0.3s ease;
    }

    /* 드롭다운 군사 서브메뉴 */
    .submenu-box {
      background: #000080;
      border: 2px solid #d4af37;
      box-shadow: 4px 4px 0px #000;
      z-index: 50;
    }
    .submenu-item {
      padding: 5px 12px;
      cursor: pointer;
      transition: all 0.1s ease;
      border-bottom: 1px solid rgba(212, 175, 55, 0.2);
    }
    .submenu-item:last-child {
      border-bottom: none;
    }
    .submenu-item:hover {
      background: #1d4ed8;
      color: #ffffff;
      font-weight: bold;
    }

    @keyframes shake-anim {
      0%, 100% { transform: translate(0, 0); }
      20%, 60% { transform: translate(-8px, 5px); }
      40%, 80% { transform: translate(8px, -5px); }
    }
    .anim-shake { animation: shake-anim 0.35s ease-in-out; }
  </style>
</head>
<body class="min-h-screen flex flex-col items-center p-1 md:p-2 text-sm">

  <!-- ============================================================= -->
  <!-- 1. [상단 커맨드 메뉴 바] (0. 휴양 -> 턴넘김 / 1. 군사 -> 서브메뉴) -->
  <!-- ============================================================= -->
  <nav class="w-full max-w-6xl koei-box p-1.5 mb-2 relative flex flex-wrap items-center justify-between text-xs font-bold gap-1">
    <div class="flex flex-wrap items-center gap-1 relative">
      <!-- 0. 휴양: 클릭 시 바로 턴 넘김! -->
      <button onclick="cmdRest()" class="koei-header-btn px-2.5 py-1 rounded bg-amber-950 text-amber-200 border-amber-400">
        0. 휴양 (턴넘김)
      </button>
      
      <!-- 1. 군사: 클릭 시 삼국지 3 원작 서브메뉴 팝업! -->
      <div class="relative inline-block">
        <button onclick="toggleMilitarySubmenu()" id="btn-cmd-military" class="koei-header-btn px-2.5 py-1 rounded">
          1. 군사 ▼
        </button>

        <!-- ⭐️ 군사 서브메뉴 드롭다운 (원작 스크린샷 100% 매칭) -->
        <div id="military-submenu" class="hidden absolute left-0 top-full mt-1 w-44 submenu-box rounded text-xs py-1 font-mono text-yellow-200 shadow-2xl">
          <div onclick="execMilitarySub('move')" class="submenu-item">1. 이  동</div>
          <div onclick="execMilitarySub('transport')" class="submenu-item">2. 수  송</div>
          <div onclick="execMilitarySub('fortify')" class="submenu-item text-emerald-300 font-bold">3. 성 방어력 향상</div>
          <div onclick="execMilitarySub('attack')" class="submenu-item text-red-300 font-bold">4. 전  쟁 (공격)</div>
          <div onclick="execMilitarySub('recruit')" class="submenu-item">5. 징  병</div>
          <div onclick="execMilitarySub('hire')" class="submenu-item">6. 모  병</div>
          <div onclick="execMilitarySub('train')" class="submenu-item">7. 훈  련</div>
          <div onclick="execMilitarySub('reorg')" class="submenu-item">8. 재편성</div>
          <div onclick="execMilitarySub('ship')" class="submenu-item">9. 선박건조</div>
        </div>
      </div>

      <button onclick="cmdMenu('2')" class="koei-header-btn px-2 py-1 rounded">2. 인사</button>
      <button onclick="cmdMenu('3')" class="koei-header-btn px-2 py-1 rounded">3. 외교(동맹)</button>
      <button onclick="cmdMenu('4')" class="koei-header-btn px-2 py-1 rounded">4. 정보</button>
      <button onclick="cmdMenu('5')" class="koei-header-btn px-2 py-1 rounded">5. 개발</button>
      <button onclick="cmdMenu('6')" class="koei-header-btn px-2 py-1 rounded">6. 계략</button>
      <button onclick="cmdMenu('7')" class="koei-header-btn px-2 py-1 rounded">7. 상인</button>
      <button onclick="cmdMenu('8')" class="koei-header-btn px-2 py-1 rounded">8. 특별</button>
      <button onclick="cmdMenu('9')" class="koei-header-btn px-2 py-1 rounded">9. 기능</button>
    </div>

    <!-- 우측 보조 제어: 군주 선택, BGM, 저장, 로드, 턴 넘김 -->
    <div class="flex items-center gap-1.5">
      <button onclick="openRulerModal()" class="px-2 py-1 rounded bg-purple-900 hover:bg-purple-800 text-amber-200 border border-purple-400 font-bold flex items-center gap-1">
        👑 군주 선택
      </button>
      <button id="btn-bgm" onclick="toggleBgm()" class="px-2.5 py-1 rounded bg-amber-600 hover:bg-amber-500 text-slate-950 font-black flex items-center gap-1 shadow">
        <span id="bgm-icon">🎵</span> BGM: <strong id="bgm-status">재생중</strong>
      </button>
      <button onclick="saveGame()" class="koei-header-btn px-2 py-1 rounded">💾 저장</button>
      <button onclick="loadGame()" class="koei-header-btn px-2 py-1 rounded">📂 로드</button>
      <button onclick="nextTurn()" class="px-3 py-1 rounded bg-red-800 hover:bg-red-700 text-amber-200 border border-amber-400 font-black">
        ⌛ 턴 넘김
      </button>
    </div>
  </nav>

  <!-- ============================================================= -->
  <!-- 2. 메인 게임 화면: 삼국지 3 13주 고화질 지도 (좌측 65%) + 정통 UI창 (우측 35%) -->
  <!-- ============================================================= -->
  <main class="w-full max-w-6xl grid grid-cols-1 lg:grid-cols-12 gap-2 mb-2">
    
    <!-- [좌측 7열]: 사용자가 업로드한 13주(州) 실제 지도 배경 & 점령 맵 -->
    <div class="lg:col-span-7 koei-box p-2 relative flex flex-col justify-between overflow-hidden min-h-[540px]">
      
      <!-- 지도 상단 상태 바 -->
      <div class="flex justify-between items-center bg-slate-950/90 px-2.5 py-1 rounded border border-amber-500/40 text-xs font-mono mb-1 z-10">
        <div class="flex items-center gap-2">
          <span class="text-amber-300 font-bold">🗺️ 13주(州) 전도</span>
          <span class="text-slate-400">|</span>
          <span class="text-emerald-300">선택 주: <strong id="map-selected-name" class="text-yellow-300">서주 (유비 본거지)</strong></span>
        </div>
        
        <!-- ⭐️ 본거지 피탈 카운터 (3개 이상 피탈 시 멸망!) -->
        <div class="flex items-center gap-1.5 bg-red-950/90 px-2 py-0.5 rounded border border-red-500 text-red-200 font-bold">
          <span>🚨 본거지 피탈:</span>
          <strong id="badge-lost-bases" class="text-amber-300 text-sm">0 / 3</strong>
          <span class="text-[9px] text-red-300">(3회 피탈 시 멸망)</span>
        </div>
      </div>

      <!-- ⭐️⭐️⭐️ 13주 고화질 지도 컨테이너 (Base64 완전 임베딩!) ⭐️⭐️⭐️ -->
      <div id="map-container" class="relative w-full h-[470px] md:h-[510px] bg-slate-900 rounded border border-slate-700 overflow-hidden shadow-inner">
        <!-- 배경: 13주 고화질 지도 Base64 이미지 -->
        <img id="samguk3-13ju-img" src="__MAP_B64__" alt="삼국지 3 13주 지도" class="w-full h-full object-fill select-none pointer-events-none">

        <!-- 13주 인터랙티브 점령 핀들 (해당 주 위치에 정확히 배치) -->
        <div onclick="selectProvince('youju')" id="pin-youju" class="prov-pin" style="left: 73%; top: 8%;"></div>
        <div onclick="selectProvince('byeongju')" id="pin-byeongju" class="prov-pin" style="left: 44%; top: 16%;"></div>
        <div onclick="selectProvince('giju')" id="pin-giju" class="prov-pin" style="left: 66%; top: 18%;"></div>
        <div onclick="selectProvince('cheongju')" id="pin-cheongju" class="prov-pin" style="left: 84%; top: 19%;"></div>
        <div onclick="selectProvince('ryangju')" id="pin-ryangju" class="prov-pin" style="left: 22%; top: 19%;"></div>
        <div onclick="selectProvince('sarye')" id="pin-sarye" class="prov-pin" style="left: 45%; top: 28%;"></div>
        <div onclick="selectProvince('yeonju')" id="pin-yeonju" class="prov-pin" style="left: 69%; top: 26%;"></div>
        <div onclick="selectProvince('yeju')" id="pin-yeju" class="prov-pin" style="left: 67%; top: 36%;"></div>
        <div onclick="selectProvince('seoju')" id="pin-seoju" class="prov-pin" style="left: 81%; top: 31%;"></div>
        <div onclick="selectProvince('ikju')" id="pin-ikju" class="prov-pin" style="left: 22%; top: 52%;"></div>
        <div onclick="selectProvince('hyeongju')" id="pin-hyeongju" class="prov-pin" style="left: 48%; top: 52%;"></div>
        <div onclick="selectProvince('yangju')" id="pin-yangju" class="prov-pin" style="left: 76%; top: 56%;"></div>
        <div onclick="selectProvince('gyoju')" id="pin-gyoju" class="prov-pin" style="left: 48%; top: 78%;"></div>
      </div>

      <!-- 지도 하단 인접 규칙 안내 -->
      <div class="mt-1 flex justify-between items-center text-[10px] text-slate-400 font-mono">
        <span class="text-amber-300">⚠️ <strong>[인접 국경 규칙]</strong> 아군 영토와 국경이 맞닿은 주변 주만 공격할 수 있습니다.</span>
        <span class="text-emerald-300">천하통일 달성: <strong id="txt-conquest-pct">1 / 13 주 (8%)</strong></span>
      </div>

    </div>

    <!-- [우측 5열]: 삼국지 3 원작 스타일 도시 상태창 + 시세 + 군주 얼굴 (사용자 이미지 100% 매칭!) -->
    <div class="lg:col-span-5 flex flex-col space-y-2">
      
      <!-- 상단 그룹: 도시 정보창 (좌측) + 시세창 & 초상화 (우측) -->
      <div class="grid grid-cols-1 md:grid-cols-12 gap-2">
        
        <!-- [좌측 7칸]: ⭐️ 도시 상태창 (사용자 스크린샷 media_1793677285133_473c4932 100% 재현!) -->
        <div class="md:col-span-7 koei-box p-2.5 text-xs font-mono space-y-2 flex flex-col justify-between">
          
          <!-- 상단: ■ 23. 신야   군주 유비 -->
          <div class="flex justify-between items-center text-sm font-bold border-b border-yellow-500/50 pb-1">
            <div class="flex items-center gap-1.5">
              <span id="city-square-badge" class="w-3 h-3 bg-emerald-500 inline-block border border-white"></span>
              <span id="city-status-title" class="text-white font-black">23. 신야</span>
            </div>
            <div>
              <span class="text-red-400 font-bold">군주</span> <strong id="city-status-ruler" class="text-white font-bold">유비</strong>
            </div>
          </div>

          <!-- 태수 / 군사 -->
          <div class="flex justify-between items-center text-xs font-bold">
            <div>
              <span class="text-fuchsia-400">태수</span> <span id="city-status-gov" class="text-white">유비</span>
            </div>
            <div>
              <span class="text-emerald-400">군사</span> <span id="city-status-adv" class="text-white">관우</span>
            </div>
          </div>

          <!-- 인구 수치 & 청룡 게이지 -->
          <div>
            <div class="flex justify-between text-[11px]">
              <span class="text-cyan-300 font-bold">인구</span>
              <strong id="stat-pop" class="text-white font-bold">382,000</strong>
            </div>
            <div class="dragon-gauge-bg rounded-sm mt-0.5"><div id="gauge-pop" class="dragon-gauge-fill w-[75%]"></div></div>
          </div>

          <!-- 금 수치 & 청룡 게이지 -->
          <div>
            <div class="flex justify-between text-[11px]">
              <span class="text-cyan-300 font-bold">금</span>
              <strong id="stat-gold" class="text-white font-bold">5,000</strong>
            </div>
            <div class="dragon-gauge-bg rounded-sm mt-0.5"><div id="gauge-gold" class="dragon-gauge-fill w-[55%]"></div></div>
          </div>

          <!-- 군량 (식량저장창고) 수치 & 청룡 게이지 -->
          <div>
            <div class="flex justify-between text-[11px]">
              <span class="text-cyan-300 font-bold">군량(식량창고)</span>
              <strong id="stat-food" class="text-white font-bold">18,000석</strong>
            </div>
            <div class="dragon-gauge-bg rounded-sm mt-0.5"><div id="gauge-food" class="dragon-gauge-fill w-[65%]"></div></div>
          </div>

          <!-- 병사 수치 & 청룡 게이지 -->
          <div>
            <div class="flex justify-between text-[11px]">
              <span class="text-cyan-300 font-bold">병사</span>
              <strong id="stat-troops" class="text-white font-bold">22,000</strong>
            </div>
            <div class="dragon-gauge-bg rounded-sm mt-0.5"><div id="gauge-troops" class="dragon-gauge-fill w-[60%]"></div></div>
          </div>

          <!-- 민충 수치 & 황금 게이지 -->
          <div>
            <div class="flex justify-between text-[11px]">
              <span class="text-cyan-300 font-bold">민충</span>
              <strong id="stat-loyalty" class="text-white font-bold">85 / 100</strong>
            </div>
            <div class="dragon-gauge-bg rounded-sm mt-0.5"><div id="gauge-loyalty" class="bg-gradient-to-r from-yellow-400 to-amber-500 h-full w-[85%]"></div></div>
          </div>

        </div>

        <!-- [우측 5칸]: 시세창 + ⭐️ 군주 얼굴 초상화 (절대 안 깨지는 Base64!) -->
        <div class="md:col-span-5 flex flex-col justify-between space-y-2">
          
          <!-- ⭐️ 시세 (Market Prices) -->
          <div class="koei-box p-2 text-xs font-mono">
            <div class="text-center text-cyan-300 font-black tracking-widest border-b border-yellow-500/50 pb-0.5 mb-1 text-sm">
              시 세
            </div>
            <div class="space-y-0.5 text-[11px]">
              <div class="flex justify-between"><span class="text-yellow-300 font-bold">쌀 팜</span><strong id="market-rice-sell" class="text-white">107</strong></div>
              <div class="flex justify-between"><span class="text-yellow-300 font-bold">쌀 삼</span><strong id="market-rice-buy" class="text-white">59</strong></div>
              <div class="flex justify-between"><span class="text-yellow-300 font-bold">노 궁</span><strong id="market-bow1" class="text-white">57</strong></div>
              <div class="flex justify-between"><span class="text-yellow-300 font-bold">강 노</span><strong id="market-bow2" class="text-white">95</strong></div>
              <div class="flex justify-between"><span class="text-yellow-300 font-bold">군 마</span><strong id="market-horse" class="text-white">49</strong></div>
            </div>
          </div>

          <!-- ⭐️⭐️⭐️ 군주 얼굴 초상화 (사용자가 올린 사진과 100% 동일하게 바로 뜸!) ⭐️⭐️⭐️ -->
          <div class="koei-box p-1.5 flex flex-col items-center justify-center text-center">
            <div class="w-24 h-28 rounded border-2 border-yellow-400 overflow-hidden bg-slate-950 shadow-md relative flex items-center justify-center">
              <img id="ruler-portrait-img" src="__PORTRAIT_LIUBEI__" alt="군주 얼굴" class="w-full h-full object-cover">
            </div>
            <div id="ruler-portrait-label" class="text-yellow-300 font-black text-xs mt-1">
              군주: 유비 (劉備)
            </div>
          </div>

        </div>
      </div>

      <!-- 하단: 출병 작전 패널 (인접 검사 & 동맹 협공) -->
      <div class="koei-box p-2.5 text-xs font-mono space-y-1.5">
        <div class="flex justify-between items-center">
          <span class="text-slate-300 font-bold">선택 거점 국경 상태:</span>
          <span id="adjacency-status-badge" class="text-emerald-300 font-bold">아군 직할 본거지</span>
        </div>

        <div id="ally-assist-box" class="hidden p-1.5 bg-indigo-950 rounded border border-indigo-400">
          <label class="flex items-center gap-1.5 cursor-pointer text-indigo-200 font-bold">
            <input type="checkbox" id="chk-ally-assault" checked class="w-3.5 h-3.5 accent-indigo-500">
            <span>🤝 동맹군 연합 공격 (원군 15,000명 협공!)</span>
          </label>
        </div>

        <button onclick="handleCampaignBtn()" id="btn-campaign" class="w-full py-2.5 rounded bg-emerald-700 hover:bg-emerald-600 text-white font-black text-xs shadow-lg transition-all flex items-center justify-center gap-1 border border-yellow-400">
          <span>⚔️</span> <span id="btn-campaign-text">아군 본거지 내정</span>
        </button>
      </div>

    </div>
  </main>

  <!-- ============================================================= -->
  <!-- 3. [하단 대화창 & 시스템 메시지] -->
  <!-- ============================================================= -->
  <footer class="w-full max-w-6xl grid grid-cols-1 md:grid-cols-4 gap-2">
    <div class="koei-box p-2 text-center flex flex-col items-center justify-center">
      <span class="text-[10px] text-slate-300 font-mono">황력 (皇曆)</span>
      <div id="txt-calendar" class="text-base font-black text-yellow-300 font-serif">194년 봄 1월</div>
      <div class="text-[9px] text-emerald-300 font-mono mt-0.5">1월 상업 세금 징수의 달</div>
    </div>

    <div class="md:col-span-3 koei-box p-2.5 flex flex-col justify-between">
      <div id="dialogue-box" class="text-xs md:text-sm font-mono text-yellow-200 leading-relaxed min-h-[38px]">
        유비님, 13주 천하 지도에서 국경이 맞닿은 인접 주를 선택하여 정벌하십시오!
      </div>
      <div class="flex justify-between items-center text-[10px] text-slate-400 pt-1 border-t border-slate-700 mt-1">
        <span>키보드 0~9 번호키로 커맨드를 실행할 수 있습니다. (0번 휴양 시 바로 턴 넘김)</span>
        <span class="text-red-400 font-bold">⚠️ 본거지 3곳 이상 피탈 시 멸망!</span>
      </div>
    </div>
  </footer>

  <!-- ============================================================= -->
  <!-- ⭐️⭐️⭐️ [모달 0] 6대 군주 선택 모달 (Base64 배너 탑재!) ⭐️⭐️⭐️ -->
  <!-- ============================================================= -->
  <div id="rulerModal" class="fixed inset-0 bg-black/90 backdrop-blur-md z-50 flex items-center justify-center p-3 hidden">
    <div class="max-w-3xl w-full koei-box p-5 text-center shadow-2xl border-4 border-yellow-500">
      <div class="flex justify-between items-center pb-2 border-b border-yellow-500/50 mb-3">
        <h3 class="text-lg font-black text-yellow-300 tracking-wide">
          👑 삼국지 3: 군주를 선택하십시오!
        </h3>
        <button onclick="closeRulerModal()" class="text-slate-400 hover:text-white font-bold text-xl">✕</button>
      </div>

      <!-- 6대 군주 Base64 배너 이미지 -->
      <div class="mb-3 rounded-lg overflow-hidden border-2 border-yellow-400/80 shadow-lg bg-black flex justify-center">
        <img src="__RULERS_BANNER_B64__" alt="삼국지 3 군주 선택" class="w-full max-h-48 object-contain">
      </div>

      <!-- 6대 군주 선택 버튼 그리드 -->
      <div class="grid grid-cols-2 md:grid-cols-3 gap-2.5 text-xs text-left mb-3">
        <button onclick="selectRuler('yuanshao')" class="p-2.5 rounded bg-slate-900 hover:bg-slate-800 border-2 border-yellow-400 transition-all flex flex-col justify-between">
          <div class="flex justify-between items-center">
            <span class="font-black text-yellow-300 text-sm">1. 원소 (袁紹)</span>
            <span class="text-[9px] px-1.5 py-0.2 rounded bg-yellow-950 text-yellow-300 font-bold">기주 남피</span>
          </div>
          <div class="text-[10px] text-slate-300 mt-1">대장 안량·문추 | 금 7,000 / 25,000명</div>
          <div class="text-[9px] text-yellow-400 mt-0.5">명문 4세 5공의 풍부한 자금과 대군</div>
        </button>

        <button onclick="selectRuler('liubei')" class="p-2.5 rounded bg-slate-900 hover:bg-slate-800 border-2 border-emerald-400 transition-all flex flex-col justify-between ring-2 ring-emerald-500/50">
          <div class="flex justify-between items-center">
            <span class="font-black text-emerald-300 text-sm">2. 유비 (劉備)</span>
            <span class="text-[9px] px-1.5 py-0.2 rounded bg-emerald-950 text-emerald-200 font-bold">서주·신야</span>
          </div>
          <div class="text-[10px] text-slate-300 mt-1">관우·장비·제갈량 | 금 5,000 / 22,000명</div>
          <div class="text-[9px] text-emerald-300 mt-0.5">인덕과 대의, 지략 100 제갈량 함정 특화</div>
        </button>

        <button onclick="selectRuler('mateng')" class="p-2.5 rounded bg-slate-900 hover:bg-slate-800 border-2 border-cyan-400 transition-all flex flex-col justify-between">
          <div class="flex justify-between items-center">
            <span class="font-black text-cyan-300 text-sm">3. 마등 (馬騰)</span>
            <span class="text-[9px] px-1.5 py-0.2 rounded bg-cyan-950 text-cyan-200 font-bold">량주 서량</span>
          </div>
          <div class="text-[10px] text-slate-300 mt-1">금마초·방덕 | 금 4,500 / 20,000명</div>
          <div class="text-[9px] text-cyan-300 mt-0.5">서량 최강 돌격 철기병 군단</div>
        </button>

        <button onclick="selectRuler('sunquan')" class="p-2.5 rounded bg-slate-900 hover:bg-slate-800 border-2 border-orange-500 transition-all flex flex-col justify-between">
          <div class="flex justify-between items-center">
            <span class="font-black text-orange-400 text-sm">4. 손권 (孫權)</span>
            <span class="text-[9px] px-1.5 py-0.2 rounded bg-orange-950 text-orange-200 font-bold">양주 건업</span>
          </div>
          <div class="text-[10px] text-slate-300 mt-1">주유·태사자 | 금 6,000 / 22,000명</div>
          <div class="text-[9px] text-orange-300 mt-0.5">강동 천혜의 양쯔강 수군 무적</div>
        </button>

        <button onclick="selectRuler('caocao')" class="p-2.5 rounded bg-slate-900 hover:bg-slate-800 border-2 border-blue-500 transition-all flex flex-col justify-between">
          <div class="flex justify-between items-center">
            <span class="font-black text-blue-400 text-sm">5. 조조 (曹操)</span>
            <span class="text-[9px] px-1.5 py-0.2 rounded bg-blue-950 text-blue-200 font-bold">예주 허창</span>
          </div>
          <div class="text-[10px] text-slate-300 mt-1">하후돈·순욱 | 금 6,500 / 26,000명</div>
          <div class="text-[9px] text-blue-300 mt-0.5">중원의 패자, 지략과 무력의 조화</div>
        </button>

        <button onclick="selectRuler('liubiao')" class="p-2.5 rounded bg-slate-900 hover:bg-slate-800 border-2 border-sky-400 transition-all flex flex-col justify-between">
          <div class="flex justify-between items-center">
            <span class="font-black text-sky-300 text-sm">6. 유표 (劉表)</span>
            <span class="text-[9px] px-1.5 py-0.2 rounded bg-sky-950 text-sky-200 font-bold">형주 양양</span>
          </div>
          <div class="text-[10px] text-slate-300 mt-1">황충·채모 | 군량 35,000석 / 21,000명</div>
          <div class="text-[9px] text-sky-300 mt-0.5">형주의 방대한 곡창 지대와 군량</div>
        </button>
      </div>
    </div>
  </div>

  <!-- ============================================================= -->
  <!-- ⭐️ [모달 1] 외교 & 쉬운 동맹 체결 모달 -->
  <!-- ============================================================= -->
  <div id="diplomacyModal" class="fixed inset-0 bg-black/90 backdrop-blur-md z-50 flex items-center justify-center p-3 hidden">
    <div class="max-w-md w-full koei-box p-4 text-center">
      <div class="flex justify-between items-center pb-2 border-b border-yellow-500/50 mb-3">
        <h3 class="text-sm font-black text-yellow-300">
          🤝 외교 교섭 & 쉬운 동맹 체결
        </h3>
        <button onclick="closeDiplomacyModal()" class="text-slate-400 hover:text-white font-bold">✕</button>
      </div>

      <p class="text-xs text-slate-300 mb-3 leading-relaxed">
        선물(금 500전)을 보내면 <strong>85% 이상의 높은 확률로 쉽게 동맹</strong>을 맺을 수 있습니다.<br>
        동맹국은 서로 침공하지 않으며, 전장 출병 시 <strong>연합 공격(15,000명 협공)</strong>에 참전합니다!
      </p>

      <div id="alliance-target-list" class="space-y-2 text-xs text-left mb-3"></div>

      <button onclick="closeDiplomacyModal()" class="px-4 py-1.5 rounded bg-slate-800 hover:bg-slate-700 text-white font-bold text-xs">
        닫기
      </button>
    </div>
  </div>

  <!-- ============================================================= -->
  <!-- ⭐️ [모달 2] 실전 전술 전쟁터 (함정, 매복, 화계, 연합공격) -->
  <!-- ============================================================= -->
  <div id="battleModal" class="fixed inset-0 bg-black/90 backdrop-blur-md z-50 flex items-center justify-center p-2 hidden">
    <div class="max-w-3xl w-full koei-box p-4 relative overflow-hidden shadow-2xl">
      
      <div class="flex flex-wrap items-center justify-between pb-2 border-b border-yellow-500/40 mb-2 gap-2">
        <div class="flex items-center gap-2">
          <span class="text-xs bg-red-950 text-red-300 px-2.5 py-0.5 rounded border border-red-500 font-black">
            ⚔️ 실전 야전·공성 결전
          </span>
          <h3 id="battle-title" class="text-base font-black text-yellow-300">
            예주(허창) 정벌전
          </h3>
        </div>

        <div class="flex items-center gap-2">
          <span id="battle-weather-badge" class="px-2 py-0.5 rounded bg-indigo-950 border border-indigo-400 text-xs font-bold text-indigo-200 flex items-center gap-1">
            🌫️ 안개 (매복 기습 가능!)
          </span>
          <span class="text-xs font-mono text-amber-300 bg-slate-900 px-2 py-0.5 rounded border border-slate-700">
            교전 턴: <strong id="battle-turn-count">1</strong> / 10턴 내 결판!
          </span>
        </div>
      </div>

      <!-- 양군 진영 및 [식량저장창고] 현황판 -->
      <div class="grid grid-cols-2 gap-3 mb-2.5">
        
        <!-- 좌측: 아군 본대 & 아군 식량창고 -->
        <div class="bg-slate-900/90 border border-emerald-500/70 rounded p-2.5">
          <div class="flex justify-between items-center mb-1">
            <span id="battle-ally-title" class="text-xs font-bold text-emerald-300">🚩 아군 본대</span>
            <span id="battle-joint-badge" class="text-[9px] bg-indigo-900 text-indigo-200 px-1 rounded font-mono hidden">🤝동맹연합군 참전</span>
          </div>

          <div class="w-full bg-slate-950 rounded-full h-2.5 overflow-hidden border border-slate-700">
            <div id="ally-battle-hp-bar" class="bg-gradient-to-r from-emerald-500 to-cyan-400 h-full w-full transition-all duration-300"></div>
          </div>
          <div class="flex justify-between text-[10px] font-mono mt-0.5 text-slate-300">
            <span>아군 전력: <strong id="ally-battle-hp-text" class="text-emerald-300">100%</strong></span>
            <span>병력: <strong id="ally-battle-troops">22,000</strong></span>
          </div>

          <div class="mt-2 p-1.5 bg-slate-950 rounded border border-emerald-600/60 text-xs">
            <div class="flex justify-between items-center text-[10px]">
              <span class="text-amber-300 font-bold flex items-center gap-1">🌾 식량저장창고</span>
              <span class="text-red-400 font-mono font-bold">0% 시 즉시 패배!</span>
            </div>
            <div class="w-full bg-slate-900 rounded-full h-2 mt-1 overflow-hidden border border-slate-700">
              <div id="ally-depot-bar" class="bg-gradient-to-r from-amber-500 to-emerald-400 h-full w-full transition-all duration-300"></div>
            </div>
            <div class="flex justify-between text-[9px] font-mono mt-0.5 text-slate-400">
              <span>내구도: <strong id="ally-depot-hp" class="text-emerald-300">100</strong>%</span>
              <span>비축미: <strong id="battle-food-amt" class="text-emerald-300">18,000</strong>석</span>
            </div>
          </div>

          <div class="mt-1.5 flex items-center gap-1 text-[11px]">
            <span class="text-slate-400">지휘관:</span>
            <select id="sel-commander" onchange="changeCommander()" class="bg-slate-950 border border-slate-700 rounded px-1.5 py-0.5 text-amber-300 font-bold flex-1">
              <option value="zhuge" selected>제갈량 (지략 100) - 🕳️함정 절대성공</option>
              <option value="guan">관우 (무력 98, 지략 79) - 🕳️함정/청룡참</option>
              <option value="pang">방통 (지략 97) - 🕳️함정/화계</option>
              <option value="liu">군주 본인 (지략 70+) - 🕳️함정가능</option>
              <option value="zhang">장비 (무력 99, 지략 35) - ❌지략부족(함정불가)</option>
            </select>
          </div>
        </div>

        <!-- 우측: 적군 본대 & 적군 식량창고 -->
        <div class="bg-slate-900/90 border border-red-500/70 rounded p-2.5">
          <div class="flex justify-between items-center mb-1">
            <span id="enemy-battle-name" class="text-xs font-bold text-red-400">하후돈 (조조군)</span>
            <span id="enemy-status-badge" class="text-[9px] bg-red-950 text-red-300 px-1 rounded font-mono">정상</span>
          </div>

          <div class="w-full bg-slate-950 rounded-full h-2.5 overflow-hidden border border-slate-700">
            <div id="enemy-battle-hp-bar" class="bg-gradient-to-r from-red-500 to-rose-400 h-full w-full transition-all duration-300"></div>
          </div>
          <div class="flex justify-between text-[10px] font-mono mt-0.5 text-slate-300">
            <span>적 전력: <strong id="enemy-battle-hp-text" class="text-red-400">100%</strong></span>
            <span>병력: <strong id="enemy-battle-troops">25,000</strong></span>
          </div>

          <div class="mt-2 p-1.5 bg-slate-950 rounded border border-red-600/60 text-xs">
            <div class="flex justify-between items-center text-[10px]">
              <span class="text-red-300 font-bold flex items-center gap-1">🌾 적군 식량창고</span>
              <span class="text-amber-300 font-mono font-bold">파괴 시 적 즉각자멸!</span>
            </div>
            <div class="w-full bg-slate-900 rounded-full h-2 mt-1 overflow-hidden border border-slate-700">
              <div id="enemy-depot-bar" class="bg-gradient-to-r from-red-600 to-orange-400 h-full w-full transition-all duration-300"></div>
            </div>
            <div class="flex justify-between text-[9px] font-mono mt-0.5 text-slate-400">
              <span>적 창고 내구: <strong id="enemy-depot-hp" class="text-red-300">100</strong>%</span>
              <span class="text-amber-300">기습 목표</span>
            </div>
          </div>

          <div id="enemy-feature-desc" class="mt-1.5 p-1 bg-slate-950 rounded text-[10px] text-slate-400 font-mono">
            적군 수비대의 움직임을 주시하십시오.
          </div>
        </div>

      </div>

      <!-- 실시간 전장 브리핑 로그창 -->
      <div id="battleLog" class="bg-slate-950 rounded border border-yellow-500/40 p-2 text-xs font-mono text-amber-200 h-16 overflow-y-auto mb-2 leading-relaxed">
        ⚔️ 전장에 포진 완료! 군량고를 지키며 화계, 매복, 함정 등 고도의 전술로 5~10턴 안에 적을 격멸하십시오!
      </div>

      <!-- 전술 커맨드 버튼 그리드 -->
      <div id="battle-action-grid" class="space-y-1.5">
        <div class="grid grid-cols-3 gap-1.5">
          <button onclick="execTrapTactic()" id="btn-tactic-trap" class="p-2 rounded bg-cyan-950 hover:bg-cyan-900 border border-cyan-400 text-left transition-all">
            <div class="flex items-center justify-between">
              <span class="font-bold text-xs text-cyan-200">🕳️ 함정 유인</span>
              <span class="text-[9px] bg-cyan-900 text-cyan-300 px-1 rounded font-mono">지략 70+</span>
            </div>
            <div class="text-[9px] text-cyan-300/80 mt-0.5">적 혼란(2턴) + 병사 1/3 소멸!</div>
          </button>

          <button onclick="execAmbushTactic()" id="btn-tactic-ambush" class="p-2 rounded bg-indigo-950 hover:bg-indigo-900 border border-indigo-400 text-left transition-all">
            <div class="flex items-center justify-between">
              <span class="font-bold text-xs text-indigo-200">🥷 안개 매복</span>
              <span id="ambush-req-badge" class="text-[9px] bg-indigo-900 text-indigo-300 px-1 rounded font-mono">안개 전용</span>
            </div>
            <div class="text-[9px] text-indigo-300/80 mt-0.5">안개 속 기습! 적 병력 50% 절반 섬멸!</div>
          </button>

          <button onclick="execFireTactic()" class="p-2 rounded bg-red-950 hover:bg-red-900 border border-red-500 text-left transition-all">
            <div class="flex items-center justify-between">
              <span class="font-bold text-xs text-orange-300">🔥 맹렬한 화계</span>
              <span class="text-[9px] bg-red-900 text-orange-200 px-1 rounded font-mono">대화재</span>
            </div>
            <div class="text-[9px] text-orange-300/80 mt-0.5">적 진영 방화! 40~65 폭풍 화염 피해!</div>
          </button>
        </div>

        <div class="grid grid-cols-4 gap-1.5">
          <button onclick="execCounterTactic()" class="py-2 rounded bg-slate-800 hover:bg-slate-700 border border-slate-600 text-center">
            <div class="font-bold text-xs text-slate-200">🛡️ 방진 반격</div>
            <div class="text-[9px] text-cyan-300">피해 80% 차단+반격</div>
          </button>

          <button onclick="execAssaultTactic()" class="py-2 rounded bg-emerald-900 hover:bg-emerald-800 border border-emerald-400 text-center">
            <div class="font-bold text-xs text-emerald-200">🐉 청룡참 돌격</div>
            <div class="text-[9px] text-yellow-300">45~75 치명타</div>
          </button>

          <button onclick="execRaidEnemyDepot()" class="py-2 rounded bg-amber-800 hover:bg-amber-700 border border-amber-400 text-center">
            <div class="font-bold text-xs text-amber-200">🌾 적 창고 기습</div>
            <div class="text-[9px] text-yellow-300">오소 습격 ➔ 대승리!</div>
          </button>

          <button onclick="execDuelChallenge()" class="py-2 rounded bg-slate-800 hover:bg-slate-700 border border-yellow-500/50 text-center">
            <div class="font-bold text-xs text-amber-300">⚔️ 일기토 결투</div>
            <div class="text-[9px] text-slate-400">장수 1:1 대결</div>
          </button>
        </div>
      </div>

      <div id="battle-end-panel" class="hidden mt-2">
        <button onclick="closeBattleModal()" class="w-full py-2.5 rounded bg-emerald-700 hover:bg-emerald-600 text-white font-black text-xs shadow-xl">
          전투 결과 확인 및 영토 편입 (13주 천하 지도 복귀)
        </button>
      </div>

    </div>
  </div>

  <!-- ============================================================= -->
  <!-- 💀 [모달 3] GAME OVER (본거지 3곳 피탈 or 식량창고 점령) -->
  <!-- ============================================================= -->
  <div id="defeatModal" class="fixed inset-0 bg-black/95 backdrop-blur-xl z-50 flex items-center justify-center p-3 hidden">
    <div class="max-w-md w-full koei-box p-6 shadow-2xl text-center anim-shake">
      <div class="text-5xl mb-2">💀 🏴‍☠️ 🔥</div>
      <h2 id="defeat-title" class="text-xl font-black text-red-400 tracking-wide">
        비보(悲報)! 군주 멸망!
      </h2>
      <h3 id="defeat-subtitle" class="text-sm font-bold text-slate-300 mt-1">
        삼국지 3: 본거지 3개 이상 피탈로 천하의 뜻이 꺾였습니다!
      </h3>

      <div id="defeat-desc" class="my-4 p-3 bg-red-950/40 rounded border border-red-800 text-xs text-slate-300 leading-relaxed text-left font-serif">
        <p>
          "지켜야 할 3곳 이상의 주요 본거지를 적에게 빼앗기니 장수들은 흩어지고 백성들은 통곡하였습니다!"
        </p>
      </div>

      <div class="flex gap-2 justify-center">
        <button onclick="loadGame()" class="px-4 py-2 rounded bg-amber-600 hover:bg-amber-500 text-slate-950 font-black text-xs shadow">
          📂 저장 파일 불러오기
        </button>
        <button onclick="location.reload()" class="px-4 py-2 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-bold text-xs">
          🔄 처음부터 다시 도전
        </button>
      </div>
    </div>
  </div>

  <!-- ============================================================= -->
  <!-- 👑 [모달 4] 천하통일! 13주 제패 황제 즉위 태평성대 엔딩 -->
  <!-- ============================================================= -->
  <div id="endingModal" class="fixed inset-0 bg-black/95 backdrop-blur-xl z-50 flex items-center justify-center p-3 hidden">
    <div class="max-w-2xl w-full koei-box p-6 shadow-2xl text-center">
      <div class="text-5xl mb-2">👑 🎊 🕊️</div>
      <span class="text-xs bg-amber-500/20 text-amber-300 px-3 py-1 rounded-full border border-amber-500/50 font-black tracking-widest uppercase">
        삼국지 3 13주 완전 제패 : 太平聖代 (태평성대)
      </span>

      <h2 id="ending-ruler-title" class="text-2xl font-black text-amber-300 mt-3 tracking-wide">
        축하합니다! 13주 천하통일(天下統一) 완수!
      </h2>
      <h3 id="ending-ruler-subtitle" class="text-sm font-bold text-amber-100/90 mt-1">
        마침내 漢(한)나라의 정통 황제에 즉위하다!
      </h3>

      <div class="my-5 p-4 bg-slate-900/90 rounded border border-amber-500/40 text-xs text-stone-200 leading-relaxed text-left space-y-2 font-serif shadow-inner">
        <p>
          황건의 난 이후 이어진 수십 년간의 참혹한 전란이 마침내 종식되었습니다.<br>
          13개 주의 모든 군벌과 흉노, 남만의 맹획, 양쯔강의 해적까지 덕과 무용으로 평정하여 온 천하를 하나로 통일하였습니다.
        </p>
        <p class="text-amber-300 font-bold">
          📜 황제의 첫 번째 조서(詔書) :<br>
          "창칼을 녹여 쟁기와 보습을 만들고, 관고의 곡식을 모두 풀어 굶주린 백성들에게 나누어주라! 
          백성이 배부르고 편안하지 않다면 황제의 자리는 한낱 멍에에 불과하다."
        </p>
        <p>
          세금을 3년간 면제하고, 모든 이민족에게도 차별 없는 혜택을 베푸니, 
          백성들은 길가에서 춤을 추고 아이들의 웃음소리가 온 중원에 가득 찼습니다.<br>
          역사는 이 시대를 <strong>『영원히 기억될 태평성대의 황금기』</strong>라 기록하였습니다.
        </p>
      </div>

      <div class="flex justify-center gap-3">
        <button onclick="location.reload()" class="px-5 py-2.5 rounded bg-gradient-to-r from-amber-600 to-yellow-500 hover:brightness-110 text-slate-950 font-black text-xs shadow-xl">
          🔄 새로운 영웅으로 다시 시작하기
        </button>
        <button onclick="document.getElementById('endingModal').classList.add('hidden')" class="px-5 py-2.5 rounded bg-slate-800 hover:bg-slate-700 text-stone-300 font-bold text-xs border border-slate-700">
          계속 영토 다스리기
        </button>
      </div>
    </div>
  </div>

  <!-- ============================================================= -->
  <!-- 7. 자바스크립트 엔진 (군주선택 + 인접공격 + 동맹연합 + 13주 지도) -->
  <!-- ============================================================= -->
  <script>
    // -------------------------------------------------------------
    // Base64 초상화 데이터
    // -------------------------------------------------------------
    const PORTRAITS = __PORTRAITS_JSON__;

    // -------------------------------------------------------------
    // Web Audio API BGM 엔진
    // -------------------------------------------------------------
    let audioCtx = null;
    let isBgmPlaying = false;
    let bgmTimer = null;
    let bgmStep = 0;

    const melodyNotes = [
      293.66, 349.23, 392.00, 440.00, 523.25, 440.00, 392.00, 349.23,
      293.66, 392.00, 440.00, 523.25, 587.33, 523.25, 440.00, 392.00,
      349.23, 440.00, 392.00, 349.23, 293.66, 261.63, 293.66, 349.23,
      392.00, 440.00, 523.25, 440.00, 392.00, 349.23, 293.66, 293.66
    ];

    const bassNotes = [
      146.83, 146.83, 174.61, 196.00, 220.00, 196.00, 174.61, 146.83,
      146.83, 196.00, 220.00, 261.63, 293.66, 261.63, 220.00, 196.00,
      174.61, 220.00, 196.00, 174.61, 146.83, 130.81, 146.83, 174.61,
      196.00, 220.00, 261.63, 220.00, 196.00, 174.61, 146.83, 146.83
    ];

    function initAudio() {
      if (!audioCtx) audioCtx = new (window.AudioContext || window.webkitAudioContext)();
      if (audioCtx.state === 'suspended') audioCtx.resume();
    }

    function playNote(freq, dur, type = 'sine', vol = 0.1) {
      if (!audioCtx || !isBgmPlaying) return;
      try {
        const osc = audioCtx.createOscillator();
        const gain = audioCtx.createGain();
        osc.type = type;
        osc.frequency.setValueAtTime(freq, audioCtx.currentTime);
        gain.gain.setValueAtTime(vol, audioCtx.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + dur);
        osc.connect(gain);
        gain.connect(audioCtx.destination);
        osc.start();
        osc.stop(audioCtx.currentTime + dur);
      } catch(e){}
    }

    function bgmTick() {
      if (!isBgmPlaying) return;
      const melFreq = melodyNotes[bgmStep % melodyNotes.length];
      const basFreq = bassNotes[bgmStep % bassNotes.length];
      playNote(melFreq, 0.45, 'triangle', 0.12);
      if (bgmStep % 2 === 0) playNote(basFreq, 0.55, 'sine', 0.15);
      bgmStep++;
      bgmTimer = setTimeout(bgmTick, 350);
    }

    function toggleBgm() {
      initAudio();
      isBgmPlaying = !isBgmPlaying;
      const statusEl = document.getElementById('bgm-status');
      const iconEl = document.getElementById('bgm-icon');

      if (isBgmPlaying) {
        statusEl.textContent = '재생중';
        iconEl.textContent = '🎵';
        document.getElementById('btn-bgm').className = "px-2.5 py-1 rounded bg-amber-600 hover:bg-amber-500 text-slate-950 font-black flex items-center gap-1 shadow";
        bgmTick();
        setDialogue("🎵 삼국지 3 배경음악이 재생됩니다.");
      } else {
        statusEl.textContent = '음소거';
        iconEl.textContent = '🔇';
        document.getElementById('btn-bgm').className = "px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-bold flex items-center gap-1 border border-slate-700";
        if (bgmTimer) clearTimeout(bgmTimer);
      }
    }

    function playSfx(type) {
      initAudio();
      try {
        const now = audioCtx.currentTime;
        if (type === 'sword') {
          const osc = audioCtx.createOscillator();
          const g = audioCtx.createGain();
          osc.type = 'triangle';
          osc.frequency.setValueAtTime(1400, now);
          osc.frequency.exponentialRampToValueAtTime(300, now + 0.15);
          g.gain.setValueAtTime(0.25, now);
          g.gain.exponentialRampToValueAtTime(0.001, now + 0.18);
          osc.connect(g); g.connect(audioCtx.destination);
          osc.start(now); osc.stop(now + 0.2);
        } else if (type === 'fire') {
          const osc = audioCtx.createOscillator();
          const g = audioCtx.createGain();
          osc.type = 'sawtooth';
          osc.frequency.setValueAtTime(220, now);
          osc.frequency.linearRampToValueAtTime(120, now + 0.3);
          g.gain.setValueAtTime(0.3, now);
          g.gain.exponentialRampToValueAtTime(0.001, now + 0.35);
          osc.connect(g); g.connect(audioCtx.destination);
          osc.start(now); osc.stop(now + 0.35);
        } else if (type === 'trap') {
          const osc = audioCtx.createOscillator();
          const g = audioCtx.createGain();
          osc.type = 'square';
          osc.frequency.setValueAtTime(180, now);
          osc.frequency.exponentialRampToValueAtTime(40, now + 0.3);
          g.gain.setValueAtTime(0.4, now);
          g.gain.exponentialRampToValueAtTime(0.001, now + 0.35);
          osc.connect(g); g.connect(audioCtx.destination);
          osc.start(now); osc.stop(now + 0.4);
        } else if (type === 'ambush') {
          const osc = audioCtx.createOscillator();
          const g = audioCtx.createGain();
          osc.type = 'sawtooth';
          osc.frequency.setValueAtTime(600, now);
          osc.frequency.exponentialRampToValueAtTime(80, now + 0.25);
          g.gain.setValueAtTime(0.4, now);
          g.gain.exponentialRampToValueAtTime(0.001, now + 0.3);
          osc.connect(g); g.connect(audioCtx.destination);
          osc.start(now); osc.stop(now + 0.35);
        } else if (type === 'fanfare') {
          [523.25, 659.25, 783.99, 1046.5].forEach((freq, idx) => {
            const osc = audioCtx.createOscillator();
            const g = audioCtx.createGain();
            osc.type = 'triangle';
            osc.frequency.setValueAtTime(freq, now + idx * 0.12);
            g.gain.setValueAtTime(0.2, now + idx * 0.12);
            g.gain.exponentialRampToValueAtTime(0.001, now + idx * 0.12 + 0.3);
            osc.connect(g); g.connect(audioCtx.destination);
            osc.start(now + idx * 0.12); osc.stop(now + idx * 0.12 + 0.35);
          });
        }
      } catch(e){}
    }

    // -------------------------------------------------------------
    // 6대 군주 프로필
    // -------------------------------------------------------------
    const rulersData = {
      liubei: { key: 'liubei', name: '유비 (劉備)', capital: 'seoju', color: '#10b981', gold: 5000, food: 18000, troops: 22000, pop: 382000, loyalty: 85, portraitKey: 'liubei_classic', desc: '인덕과 대의, 지략 100 제갈량 함정 특화' },
      yuanshao: { key: 'yuanshao', name: '원소 (袁紹)', capital: 'giju', color: '#eab308', gold: 7000, food: 25000, troops: 25000, pop: 420000, loyalty: 75, portraitKey: 'yuanshao', desc: '명문 4세 5공의 풍부한 자금과 대군' },
      mateng: { key: 'mateng', name: '마등 (馬騰)', capital: 'ryangju', color: '#06b6d4', gold: 4500, food: 16000, troops: 20000, pop: 240000, loyalty: 86, portraitKey: 'mateng', desc: '서량 최강 돌격 철기병 군단' },
      sunquan: { key: 'sunquan', name: '손권 (孫權)', capital: 'yangju', color: '#f97316', gold: 6000, food: 22000, troops: 22000, pop: 410000, loyalty: 90, portraitKey: 'sunquan', desc: '강동 천혜의 양쯔강 수군 무적' },
      caocao: { key: 'caocao', name: '조조 (曹操)', capital: 'yeju', color: '#3b82f6', gold: 6500, food: 24000, troops: 26000, pop: 450000, loyalty: 88, portraitKey: 'caocao', desc: '중원의 패자, 지략과 무력의 조화' },
      liubiao: { key: 'liubiao', name: '유표 (劉表)', capital: 'hyeongju', color: '#38bdf8', gold: 5500, food: 35000, troops: 21000, pop: 390000, loyalty: 82, portraitKey: 'liubiao', desc: '형주의 방대한 곡창 지대와 군량' }
    };

    let curRulerKey = 'liubei';

    // 13주 인접 그래프 (주변만 공격 가능!)
    const adjGraph = {
      youju: ['byeongju', 'giju', 'cheongju'],
      byeongju: ['youju', 'giju', 'ryangju', 'sarye'],
      giju: ['youju', 'byeongju', 'cheongju', 'yeonju'],
      cheongju: ['youju', 'giju', 'yeonju', 'seoju'],
      ryangju: ['byeongju', 'sarye', 'ikju'],
      sarye: ['byeongju', 'ryangju', 'yeonju', 'yeju', 'hyeongju', 'ikju'],
      yeonju: ['giju', 'cheongju', 'sarye', 'yeju', 'seoju'],
      yeju: ['sarye', 'yeonju', 'seoju', 'hyeongju', 'yangju'],
      seoju: ['cheongju', 'yeonju', 'yeju', 'yangju'],
      hyeongju: ['sarye', 'yeju', 'yangju', 'ikju', 'gyoju'],
      yangju: ['yeju', 'seoju', 'hyeongju', 'gyoju'],
      ikju: ['ryangju', 'sarye', 'hyeongju', 'gyoju'],
      gyoju: ['ikju', 'hyeongju', 'yangju']
    };

    // 13주 데이터
    let provincesData = {
      seoju: { key: 'seoju', num: 23, name: '서주(신야·하비)', ruler: '유비', gov: '유비', adv: '관우', isPlayer: true, pop: 382000, troops: 22000, loyalty: 85, fort: 100, genWar: 98, genInt: 100, isAlliance: false },
      yeju: { key: 'yeju', num: 20, name: '예주(허창)', ruler: '조조', gov: '하후돈', adv: '순욱', isPlayer: false, pop: 450000, troops: 25000, loyalty: 88, fort: 90, genWar: 92, genInt: 95, isAlliance: false },
      yeonju: { key: 'yeonju', num: 10, name: '연주(복양·진류)', ruler: '조조군', gov: '조인', adv: '곽가', isPlayer: false, pop: 330000, troops: 20000, loyalty: 80, fort: 85, genWar: 88, genInt: 96, isAlliance: false },
      sarye: { key: 'sarye', num: 11, name: '사례(낙양·장안)', ruler: '여포', gov: '여포', adv: '진궁', isPlayer: false, pop: 520000, troops: 24000, loyalty: 70, fort: 95, genWar: 100, genInt: 89, isAlliance: false },
      giju: { key: 'giju', num: 3, name: '기주(업·남피)', ruler: '원소', gov: '안량', adv: '전풍', isPlayer: false, pop: 420000, troops: 22000, loyalty: 75, fort: 80, genWar: 90, genInt: 88, isAlliance: false },
      youju: { key: 'youju', num: 1, name: '유주(북평·계)', ruler: '공손찬', gov: '공손찬', adv: '관정', isPlayer: false, pop: 250000, troops: 14000, loyalty: 78, fort: 75, genWar: 85, genInt: 68, isAlliance: false },
      byeongju: { key: 'byeongju', num: 14, name: '병주(삭방·진양)', ruler: '흉노군', gov: '선우 어부라', adv: '좌현왕', isPlayer: false, pop: 180000, troops: 18000, loyalty: 90, fort: 85, genWar: 91, genInt: 62, isAlliance: false },
      cheongju: { key: 'cheongju', num: 9, name: '청주(북해·제남)', ruler: '공융군', gov: '태사자', adv: '공융', isPlayer: false, pop: 280000, troops: 12000, loyalty: 72, fort: 70, genWar: 92, genInt: 74, isAlliance: false },
      ryangju: { key: 'ryangju', num: 16, name: '량주(무위·천수)', ruler: '마등', gov: '마초', adv: '한수', isPlayer: false, pop: 240000, troops: 18000, loyalty: 86, fort: 80, genWar: 95, genInt: 60, isAlliance: false },
      hyeongju: { key: 'hyeongju', num: 24, name: '형주(양양·강하)', ruler: '유표', gov: '해적두목 감녕', adv: '괴월', isPlayer: false, pop: 390000, troops: 21000, loyalty: 82, fort: 85, genWar: 94, genInt: 72, isAlliance: false },
      yangju: { key: 'yangju', num: 34, name: '양주(건업·오)', ruler: '손권', gov: '손책/태사자', adv: '주유', isPlayer: false, pop: 410000, troops: 22000, loyalty: 90, fort: 88, genWar: 94, genInt: 96, isAlliance: false },
      ikju: { key: 'ikju', num: 41, name: '익주(성도·운남)', ruler: '남만맹획', gov: '남만왕 맹획', adv: '법정', isPlayer: false, pop: 480000, troops: 26000, loyalty: 85, fort: 90, genWar: 89, genInt: 42, isAlliance: false },
      gyoju: { key: 'gyoju', num: 46, name: '교주(남해·교지)', ruler: '사섭군', gov: '사섭', adv: '사일', isPlayer: false, pop: 190000, troops: 10000, loyalty: 70, fort: 60, genWar: 65, genInt: 78, isAlliance: false }
    };

    const generals = [
      { id: 'zhuge', name: '제갈량', war: 38, int: 100, lead: 98 },
      { id: 'guan', name: '관우', war: 98, int: 79, lead: 96 },
      { id: 'pang', name: '방통', war: 45, int: 97, lead: 86 },
      { id: 'liu', name: '유비', war: 74, int: 76, lead: 78 },
      { id: 'zhang', name: '장비', war: 99, int: 35, lead: 88 }
    ];

    let year = 194;
    let season = '봄';
    let month = 1;
    let gold = 5000;
    let food = 18000;
    let depotHp = 100;
    let lostBasesCount = 0;
    let selectedProvKey = 'seoju';

    // 전장 변수
    let battleTurn = 1;
    let battleMaxTurn = 10;
    let battleWeather = 'fog';
    let curCommander = generals[0];
    let allyBattleHp = 100;
    let enemyBattleHp = 100;
    let allyDepotHp = 100;
    let enemyDepotHp = 100;
    let enemyConfusion = 0;
    let isAmbushUsed = false;
    let battleTargetProvKey = 'yeju';
    let isJointAssault = false;

    function initGame() {
      renderMapPins();
      selectProvince(selectedProvKey);
      updateTopBar();
      updateCalendar();
    }

    // ⭐️ 0. 휴양: 바로 턴 넘기기!
    function cmdRest() {
      setDialogue("【0. 휴양】 유비와 장수들이 휴식을 취하며 다음 달로 턴을 넘깁니다.");
      nextTurn();
    }

    // ⭐️ 1. 군사 서브메뉴 토글
    function toggleMilitarySubmenu() {
      const sub = document.getElementById('military-submenu');
      sub.classList.toggle('hidden');
    }

    // 군사 서브메뉴 실행
    function execMilitarySub(action) {
      document.getElementById('military-submenu').classList.add('hidden');
      initAudio();
      playSfx('sword');

      const p = provincesData[selectedProvKey];

      if (action === 'move') {
        setDialogue(`【1. 이동】 아군 인접 거점으로 장수와 부대를 이동 배치합니다.`);
      } else if (action === 'transport') {
        setDialogue(`【2. 수송】 인접 본거지로 식량창고 군량미 2,000석과 군자금을 수송했습니다.`);
      } else if (action === 'fortify') {
        // ⭐️ 3. 성 방어력 향상!
        if (gold < 200) { alert("금이 부족합니다! (필요: 200전)"); return; }
        gold -= 200;
        p.fort = Math.min(100, p.fort + 15);
        depotHp = Math.min(100, depotHp + 15);
        updateTopBar();
        setDialogue(`🏰 【3. 성 방어력 향상】 성벽과 해자를 보수하여 성 방어력(+15)과 식량창고 내구도가 강화되었습니다! (현재 방어: ${p.fort})`);
      } else if (action === 'attack') {
        // ⭐️ 4. 전쟁 (공격)
        handleCampaignBtn();
      } else if (action === 'recruit') {
        // 5. 징병
        if (gold < 300) { alert("금이 부족합니다!"); return; }
        gold -= 300;
        p.troops += 1500;
        updateTopBar();
        selectProvince(selectedProvKey);
        setDialogue(`⚔️ 【5. 징병】 금 300전으로 정예 병사 1,500명을 추가 징집했습니다!`);
      } else if (action === 'hire') {
        setDialogue(`【6. 모병】 널리 방을 붙여 충성스러운 의용병을 모았습니다.`);
      } else if (action === 'train') {
        setDialogue(`🎯 【7. 훈련】 관우와 장비가 군사들을 맹훈련하여 전투 훈련도가 대폭 상승했습니다!`);
      } else if (action === 'reorg') {
        setDialogue(`【8. 재편성】 칭기즈칸 8대 특수 병과를 균형 있게 재편성했습니다.`);
      } else if (action === 'ship') {
        setDialogue(`⚓ 【9. 선박건조】 양쯔강 수전에 대비하여 몽동과 투함 전함을 건조했습니다.`);
      }
    }

    // 13주 지도 위 핀 렌더링
    function renderMapPins() {
      Object.keys(provincesData).forEach(k => {
        const p = provincesData[k];
        const pinEl = document.getElementById(`pin-${k}`);
        if (!pinEl) return;

        let badgeStyle = p.isPlayer 
          ? "bg-emerald-600 text-white border-2 border-yellow-300 font-black shadow-lg" 
          : (p.isAlliance ? "bg-indigo-700 text-indigo-100 border border-yellow-400" : "bg-slate-900/90 text-slate-200 border border-slate-600");

        let flagIcon = p.isPlayer ? "🚩" : (p.isAlliance ? "🤝" : "🏰");

        pinEl.innerHTML = `
          <div class="flex flex-col items-center">
            <span class="px-2 py-0.5 rounded-full text-[10px] ${badgeStyle} whitespace-nowrap">
              ${flagIcon} ${p.name.split('(')[0]} <span class="font-mono text-[9px]">(${p.ruler})</span>
            </span>
          </div>
        `;
      });
    }

    // 주 선택 시 인접성 검사 및 정통 UI 갱신
    function selectProvince(key) {
      selectedProvKey = key;
      const p = provincesData[key];
      if (!p) return;

      document.getElementById('map-selected-name').textContent = `${p.name} (${p.ruler})`;

      // ⭐️ 정통 삼국지 3 화면 데이터 갱신 (media_1793677285133_473c4932 100% 매칭!)
      document.getElementById('city-status-title').textContent = `${p.num}. ${p.name.split('(')[0]}`;
      document.getElementById('city-status-ruler').textContent = p.ruler;
      document.getElementById('city-status-gov').textContent = p.gov;
      document.getElementById('city-status-adv').textContent = p.adv;

      document.getElementById('stat-pop').textContent = p.pop.toLocaleString();
      document.getElementById('stat-troops').textContent = p.troops.toLocaleString();
      document.getElementById('stat-loyalty').textContent = `${p.loyalty} / 100`;

      // 핀 활성화
      document.querySelectorAll('.prov-pin').forEach(el => el.classList.remove('prov-pin-active'));
      const curPin = document.getElementById(`pin-${key}`);
      if (curPin) curPin.classList.add('prov-pin-active');

      const adjBadge = document.getElementById('adjacency-status-badge');
      const allyBox = document.getElementById('ally-assist-box');
      const btn = document.getElementById('btn-campaign');
      const btnText = document.getElementById('btn-campaign-text');

      if (p.isPlayer) {
        adjBadge.innerHTML = `<span class="text-emerald-400 font-bold">🚩 아군 직할 본거지 (방어력: ${p.fort})</span>`;
        allyBox.classList.add('hidden');
        btnText.textContent = "아군 본거지 내정 (성방어/훈련)";
        btn.className = "w-full py-2.5 rounded bg-emerald-700 hover:bg-emerald-600 text-white font-black text-xs shadow-lg border border-yellow-400";
        setDialogue(`[${p.name}]은(는) 아군 본거지입니다. 1. 군사 메뉴에서 성방어력 향상과 훈련을 실행할 수 있습니다.`);
      } else {
        // 인접성 검사
        const isAdj = checkAdjacency(key);
        const hasAlly = Object.values(provincesData).some(pr => pr.isAlliance);

        if (isAdj) {
          adjBadge.innerHTML = `<span class="text-yellow-300 font-bold">⚡ [인접 국경] 진격로 확보됨!</span>`;
          if (hasAlly) {
            allyBox.classList.remove('hidden');
          } else {
            allyBox.classList.add('hidden');
          }
          btnText.textContent = `⚔️ ${p.name.split('(')[0]} 정벌 총출병!`;
          btn.className = "w-full py-2.5 rounded bg-gradient-to-r from-red-700 via-orange-600 to-amber-600 hover:brightness-110 text-white font-black text-xs shadow-lg border border-yellow-400";
          setDialogue(`⚔️ [${p.name}]은(는) 아군 영토와 국경이 맞닿아 있습니다. 출병하여 정벌할 수 있습니다!`);
        } else {
          adjBadge.innerHTML = `<span class="text-red-400 font-bold">🔒 [원거리 불가] 국경 비인접</span>`;
          allyBox.classList.add('hidden');
          btnText.textContent = "🔒 인접 영토 점령 필요 (원거리 불가)";
          btn.className = "w-full py-2.5 rounded bg-slate-800 text-slate-500 font-bold text-xs cursor-not-allowed border border-slate-700";
          setDialogue(`⚠️ [${p.name}]은(는) 아군 영토와 국경이 닿지 않았습니다. 먼저 길목의 인접 주를 점령하십시오!`);
        }
      }
    }

    function checkAdjacency(targetKey) {
      const playerProvKeys = Object.keys(provincesData).filter(k => provincesData[k].isPlayer);
      for (let pk of playerProvKeys) {
        if (adjGraph[pk] && adjGraph[pk].includes(targetKey)) {
          return true;
        }
      }
      return false;
    }

    function setDialogue(msg) {
      document.getElementById('dialogue-box').innerHTML = `▶ ${msg}`;
    }

    function updateTopBar() {
      document.getElementById('stat-gold').textContent = gold.toLocaleString();
      document.getElementById('stat-food').textContent = `${food.toLocaleString()}석`;
      document.getElementById('badge-lost-bases').textContent = `${lostBasesCount} / 3`;
    }

    function updateCalendar() {
      document.getElementById('txt-calendar').textContent = `${year}년 ${season} ${month}월`;
    }

    // 0~9 번호키 지원
    function cmdMenu(cmd) {
      initAudio();
      playSfx('sword');
      if (cmd === '0') cmdRest();
      else if (cmd === '1') toggleMilitarySubmenu();
      else if (cmd === '2') setDialogue("【2. 인사】 충성스러운 맹장들과 지략가들이 황제를 보좌하고 있습니다.");
      else if (cmd === '3') openDiplomacyModal();
      else if (cmd === '4') {
        const myCount = Object.values(provincesData).filter(p => p.isPlayer).length;
        setDialogue(`【4. 정보】 현재 지배 13주 달성도: ${myCount} / 13 (피탈 본거지: ${lostBasesCount}/3).`);
      } else if (cmd === '5') {
        if (gold < 150) { setDialogue("금이 부족합니다! (필요: 150전)"); return; }
        gold -= 150;
        food += 800;
        updateTopBar();
        setDialogue("【5. 개발】 금 150을 들여 전답을 개간하여 식량저장창고에 800석을 입고했습니다!");
      } else if (cmd === '6') {
        setDialogue("【6. 계략】 전장에서 [지략 70이상 함정]과 [안개 속 매복]을 구사하십시오!");
      } else if (cmd === '7') {
        setDialogue("【7. 상인】 상인 방문: 쌀을 사거나 노궁/강노/군마를 거래할 수 있습니다.");
      } else if (cmd === '8') {
        setDialogue("【8. 특별】 칭기즈칸 8대 특수 병과가 군단에 배치되었습니다!");
      } else if (cmd === '9') {
        openRulerModal();
      }
    }

    window.addEventListener('keydown', (e) => {
      if (['0','1','2','3','4','5','6','7','8','9'].includes(e.key)) {
        cmdMenu(e.key);
      }
    });

    // ⭐️ 군주 선택
    function openRulerModal() { document.getElementById('rulerModal').classList.remove('hidden'); }
    function closeRulerModal() { document.getElementById('rulerModal').classList.add('hidden'); }

    function selectRuler(rulerKey) {
      const r = rulersData[rulerKey];
      if (!r) return;
      curRulerKey = rulerKey;

      Object.keys(provincesData).forEach(k => {
        provincesData[k].isPlayer = false;
        provincesData[k].isAlliance = false;
      });

      provincesData[r.capital].isPlayer = true;
      provincesData[r.capital].ruler = r.name.split(' ')[0];
      gold = r.gold;
      food = r.food;
      lostBasesCount = 0;
      selectedProvKey = r.capital;

      // ⭐️ 초상화 갱신
      const portraitImg = document.getElementById('ruler-portrait-img');
      if (PORTRAITS[r.portraitKey]) {
        portraitImg.src = PORTRAITS[r.portraitKey];
      }
      document.getElementById('ruler-portrait-label').textContent = `군주: ${r.name}`;

      closeRulerModal();
      renderMapPins();
      selectProvince(r.capital);
      updateTopBar();

      setDialogue(`👑 새로운 군주 [${r.name}]을(를) 선택하셨습니다! (${r.desc})`);
    }

    // 외교 모달
    function openDiplomacyModal() {
      const listEl = document.getElementById('alliance-target-list');
      listEl.innerHTML = '';

      const otherProvs = Object.keys(provincesData).filter(k => !provincesData[k].isPlayer);
      otherProvs.forEach(k => {
        const p = provincesData[k];
        const row = document.createElement('div');
        row.className = "flex items-center justify-between p-2 rounded bg-slate-900 border border-slate-700";
        
        let statusBtn = p.isAlliance
          ? `<span class="text-indigo-300 font-bold">🤝 동맹 체결됨</span>`
          : `<button onclick="makeAlliance('${k}')" class="px-2.5 py-1 rounded bg-amber-600 hover:bg-amber-500 text-slate-950 font-black text-xs shadow">동맹 체결 (금 500)</button>`;

        row.innerHTML = `
          <div>
            <span class="font-bold text-yellow-300">${p.name}</span>
            <div class="text-[10px] text-slate-400">군주: ${p.ruler} | 병력: ${p.troops.toLocaleString()}명</div>
          </div>
          <div>${statusBtn}</div>
        `;
        listEl.appendChild(row);
      });

      document.getElementById('diplomacyModal').classList.remove('hidden');
    }
    function closeDiplomacyModal() { document.getElementById('diplomacyModal').classList.add('hidden'); }

    function makeAlliance(key) {
      if (gold < 500) { alert("금이 부족합니다!"); return; }
      gold -= 500;
      updateTopBar();

      provincesData[key].isAlliance = true;
      playSfx('fanfare');
      alert(`🤝 [동맹 체결 성공!]\n${provincesData[key].ruler}과의 동맹이 성사되었습니다!\n전투 시 [연합 공격(원군 15,000명)]을 요청할 수 있습니다!`);
      closeDiplomacyModal();
      renderMapPins();
      selectProvince(selectedProvKey);
      setDialogue(`🤝 ${provincesData[key].ruler}과 굳건한 동맹을 맺었습니다. 이제 연합 공격이 가능합니다!`);
    }

    // 턴 넘김 처리 (적군 역습 AI)
    function nextTurn() {
      month++;
      if (month > 12) {
        month = 1;
        year++;
      }
      if (month <= 3) season = '봄';
      else if (month <= 6) season = '여름';
      else if (month <= 9) season = '가을';
      else season = '겨울';

      updateCalendar();

      if (month === 1) {
        gold += 2500;
        setDialogue("🎉 [1월 신년 세금] 상인들과 백성들이 세금 2,500전을 납부했습니다!");
      } else if (month === 7) {
        food += 8000;
        setDialogue("🌾 [7월 가을 추수] 햅쌀 8,000석을 식량저장창고에 입고했습니다!");
      }

      food = Math.max(0, food - 1200);
      if (food <= 0) {
        depotHp = Math.max(0, depotHp - 25);
        if (depotHp <= 0) {
          triggerDefeat("식량저장창고의 군량이 완전히 바닥나 전군이 굶주려 흩어졌습니다!", "보급선 단절 멸망");
          return;
        }
      }

      // 적군 역습
      const playerProvs = Object.keys(provincesData).filter(k => provincesData[k].isPlayer && k !== rulersData[curRulerKey].capital);
      if (playerProvs.length > 0 && Math.random() < 0.28) {
        const lostKey = playerProvs[Math.floor(Math.random() * playerProvs.length)];
        const lp = provincesData[lostKey];
        lp.isPlayer = false;
        lp.ruler = '적군탈환';
        lostBasesCount++;

        setDialogue(`🚨 <strong class="text-red-400">[비보! 본거지 피탈!]</strong> 적군이 기습하여 <strong>${lp.name}</strong>을 빼앗겼습니다! (현재 피탈: ${lostBasesCount}/3)`);

        if (lostBasesCount >= 3) {
          triggerDefeat("적군에게 3곳 이상의 본거지를 빼앗겨 군심이 와해되고 멸망하였습니다!", "삼국지 3: 본거지 3곳 이상 피탈 멸망");
          return;
        }
      }

      renderMapPins();
      updateTopBar();
      selectProvince(selectedProvKey);
    }

    // =============================================================
    // 실전 전술 전쟁 엔진
    // =============================================================
    function handleCampaignBtn() {
      const p = provincesData[selectedProvKey];
      if (p.isPlayer) {
        execMilitarySub('fortify');
        return;
      }

      if (!checkAdjacency(selectedProvKey)) {
        alert("⚠️ [공격 불가] 아군 영토와 국경이 맞닿은 주변 주만 공격할 수 있습니다!");
        return;
      }

      startWarBattle(selectedProvKey);
    }

    function startWarBattle(targetKey) {
      const target = provincesData[targetKey];
      battleTargetProvKey = targetKey;
      battleTurn = 1;
      allyBattleHp = 100;
      enemyBattleHp = 100;
      allyDepotHp = depotHp;
      enemyDepotHp = 100;
      enemyConfusion = 0;
      isAmbushUsed = false;

      const chkAlly = document.getElementById('chk-ally-assault');
      isJointAssault = chkAlly && chkAlly.checked;

      const jointBadge = document.getElementById('battle-joint-badge');
      if (isJointAssault) {
        jointBadge.classList.remove('hidden');
      } else {
        jointBadge.classList.add('hidden');
      }

      const weathers = ['fog', 'fog', 'fog', 'clear', 'wind', 'rain'];
      battleWeather = weathers[Math.floor(Math.random() * weathers.length)];
      updateBattleWeatherUI();

      document.getElementById('battle-title').textContent = `${target.name} 정벌전 (${target.ruler} 격파 작전)`;
      document.getElementById('enemy-battle-name').textContent = `${target.gov} (${target.ruler})`;
      document.getElementById('enemy-battle-troops').textContent = target.troops.toLocaleString();
      document.getElementById('battle-food-amt').textContent = `${food.toLocaleString()}석`;

      const eDesc = document.getElementById('enemy-feature-desc');
      if (targetKey === 'ikju') eDesc.textContent = "남만왕 맹획의 상아병 코끼리 부대! 함정과 화계가 필수적입니다.";
      else if (targetKey === 'byeongju') eDesc.textContent = "북방 흉노 철기병! 쾌속 기동으로 아군 후방을 유린하려 합니다.";
      else if (targetKey === 'sarye') eDesc.textContent = "무력 100 여포의 천하무쌍 부대! 함정 유인과 매복이 필요합니다.";
      else eDesc.textContent = "삼국지 3 정예 수비군! 지략과 전술을 구사하십시오.";

      updateBattleHpBars();
      document.getElementById('battle-turn-count').textContent = battleTurn;
      document.getElementById('battle-action-grid').classList.remove('hidden');
      document.getElementById('battle-end-panel').classList.add('hidden');

      let jointMsg = isJointAssault ? " <strong class='text-indigo-300'>[동맹군 15,000명 연합 협공 참전!]</strong>" : "";
      document.getElementById('battleLog').innerHTML = `
        🚩 <strong>${target.name} 정벌 작전 개시!</strong>${jointMsg} (날씨: ${getWeatherName(battleWeather)})<br>
        군량창고를 사수하며 5~10턴 안에 적을 격멸하십시오!
      `;

      document.getElementById('battleModal').classList.remove('hidden');
    }

    function getWeatherName(w) {
      if (w === 'fog') return '🌫️ 짙은 안개 (매복 기습 가능!)';
      if (w === 'wind') return '🌪️ 강풍 (화계 데미지 2배 폭발!)';
      if (w === 'rain') return '🌧️ 폭우 (화계 제한, 창병 강화)';
      return '☀️ 쾌청 (일반 야전)';
    }

    function updateBattleWeatherUI() {
      const wBadge = document.getElementById('battle-weather-badge');
      const ambushBtn = document.getElementById('btn-tactic-ambush');
      const ambushBadge = document.getElementById('ambush-req-badge');

      wBadge.textContent = getWeatherName(battleWeather);

      if (battleWeather === 'fog') {
        wBadge.className = "px-2 py-0.5 rounded bg-indigo-950 border border-indigo-400 text-xs font-bold text-indigo-200 flex items-center gap-1";
        ambushBtn.classList.remove('opacity-50', 'cursor-not-allowed');
        ambushBadge.textContent = "⚡발동가능";
        ambushBadge.className = "text-[9px] bg-indigo-900 text-indigo-200 px-1 rounded font-mono font-bold";
      } else {
        wBadge.className = "px-2 py-0.5 rounded bg-slate-800 border border-slate-600 text-xs font-bold text-cyan-300 flex items-center gap-1";
        ambushBtn.classList.add('opacity-50');
        ambushBadge.textContent = "안개 필요";
        ambushBadge.className = "text-[9px] bg-slate-900 text-slate-500 px-1 rounded font-mono";
      }
    }

    function changeCommander() {
      const val = document.getElementById('sel-commander').value;
      curCommander = generals.find(g => g.id === val);
      addBattleLog(`지휘관을 [${curCommander.name}]으로 변경했습니다. (지략: ${curCommander.int})`);
    }

    function addBattleLog(msg) {
      const log = document.getElementById('battleLog');
      log.innerHTML += `<br>▶ ${msg}`;
      log.scrollTop = log.scrollHeight;
    }

    function updateBattleHpBars() {
      document.getElementById('ally-battle-hp-bar').style.width = allyBattleHp + '%';
      document.getElementById('ally-battle-hp-text').textContent = allyBattleHp + '%';

      document.getElementById('enemy-battle-hp-bar').style.width = enemyBattleHp + '%';
      document.getElementById('enemy-battle-hp-text').textContent = enemyBattleHp + '%';

      document.getElementById('ally-depot-bar').style.width = allyDepotHp + '%';
      document.getElementById('ally-depot-hp').textContent = allyDepotHp;

      document.getElementById('enemy-depot-bar').style.width = enemyDepotHp + '%';
      document.getElementById('enemy-depot-hp').textContent = enemyDepotHp;

      const eBadge = document.getElementById('enemy-status-badge');
      if (enemyConfusion > 0) {
        eBadge.textContent = `🌀 혼란(${enemyConfusion}턴)`;
        eBadge.className = "text-[9px] bg-yellow-950 text-yellow-300 border border-yellow-600 px-1.5 py-0.5 rounded font-mono font-bold animate-pulse";
      } else {
        eBadge.textContent = "정상";
        eBadge.className = "text-[9px] bg-red-950 text-red-300 px-1 rounded font-mono";
      }
    }

    // 1. 함정 (지략 70 이상 전용)
    function execTrapTactic() {
      if (curCommander.int < 70) {
        alert(`[함정 불가] ${curCommander.name}의 지략은 ${curCommander.int}입니다.\n함정은 지략 70 이상인 지휘관만 시전할 수 있습니다!`);
        return;
      }
      playSfx('trap');
      const lostHp = Math.max(15, Math.floor(enemyBattleHp * 0.333));
      enemyBattleHp = Math.max(0, enemyBattleHp - lostHp);
      enemyConfusion = 2;

      const p = provincesData[battleTargetProvKey];
      const lostTroops = Math.floor(p.troops * 0.333);
      p.troops = Math.max(1000, p.troops - lostTroops);

      addBattleLog(`
        🕳️ <strong>[신산 함정 적중!]</strong> ${curCommander.name}(지략 ${curCommander.int})의 계책으로 적을 함정에 빠뜨렸습니다!<br>
        💥 <strong>적 병력 1/3(${lostTroops.toLocaleString()}명, HP -${lostHp}%) 즉시 소멸!</strong><br>
        🌀 적 진영이 <strong>혼란 상태(2턴간 행동 불능)</strong>에 빠졌습니다!
      `);

      updateBattleHpBars();
      checkBattleState();
      if (enemyBattleHp > 0) processEnemyTurn();
    }

    // 2. 안개 속 매복 기습 (50% 전멸)
    function execAmbushTactic() {
      if (battleWeather !== 'fog') {
        alert("전장에 [안개]가 끼어 있지 않아 매복할 수 없습니다!");
        return;
      }
      if (isAmbushUsed) {
        alert("매복 기습은 적이 경계하여 1회만 가능합니다!");
        return;
      }
      playSfx('ambush');
      isAmbushUsed = true;
      const lostHp = Math.max(25, Math.floor(enemyBattleHp * 0.5));
      enemyBattleHp = Math.max(0, enemyBattleHp - lostHp);

      const p = provincesData[battleTargetProvKey];
      const lostTroops = Math.floor(p.troops * 0.5);
      p.troops = Math.max(1000, p.troops - lostTroops);

      addBattleLog(`
        🥷 <strong>【안개 속 복병 기습 대성공!】</strong><br>
        자욱한 안개를 틈타 적의 배후를 단칼에 베어 갈랐습니다!<br>
        ⚡ <strong>적 병력 절반(50%, ${lostTroops.toLocaleString()}명 전멸! HP -${lostHp}%)!</strong>
      `);

      updateBattleHpBars();
      checkBattleState();
      if (enemyBattleHp > 0) processEnemyTurn();
    }

    // 3. 화계
    function execFireTactic() {
      playSfx('fire');
      const isWind = battleWeather === 'wind';
      let dmg = 38 + Math.floor(Math.random() * 25);
      if (isWind) dmg = Math.floor(dmg * 1.8);
      enemyBattleHp = Math.max(0, enemyBattleHp - dmg);

      let logMsg = `🔥 <strong>[화공(火攻) 전개!]</strong> 불화살과 기름으로 적진을 불태웠습니다! (피해: <strong>${dmg}</strong>)`;
      if (isWind) logMsg += `<br>🌪️ <strong>강풍을 타고 불길이 폭풍처럼 번져 대화재!</strong>`;
      addBattleLog(logMsg);

      updateBattleHpBars();
      checkBattleState();
      if (enemyBattleHp > 0) processEnemyTurn();
    }

    // 4. 방진 반격
    function execCounterTactic() {
      playSfx('sword');
      const counterDmg = 35 + Math.floor(Math.random() * 18);
      enemyBattleHp = Math.max(0, enemyBattleHp - counterDmg);

      addBattleLog(`🛡️ <strong>[철벽 방진 반격!]</strong> 적의 돌격을 80% 막아내고 역돌격으로 <strong>${counterDmg}</strong>의 치명타를 입혔습니다!`);
      updateBattleHpBars();
      checkBattleState();
      if (enemyBattleHp > 0) processEnemyTurn(true);
    }

    // 5. 청룡참 / 총돌격 (연합 공격 시 +50% 위력)
    function execAssaultTactic() {
      playSfx('sword');
      let dmg = 45 + Math.floor(Math.random() * 30);
      if (isJointAssault) {
        dmg = Math.floor(dmg * 1.5);
        addBattleLog(`🤝 <strong>[동맹군 연합 협공 돌격!]</strong> 아군과 동맹군이 양익에서 적을 포위 섬멸하여 <strong class="text-yellow-300">${dmg}</strong>의 폭풍 데미지를 입혔습니다!`);
      } else {
        addBattleLog(`🐉 <strong>[청룡참 & 8대 병종 돌격!]</strong> 적 본진을 짓밟아 <strong class="text-yellow-300">${dmg}</strong>의 폭풍 데미지를 입혔습니다!`);
      }
      enemyBattleHp = Math.max(0, enemyBattleHp - dmg);

      updateBattleHpBars();
      checkBattleState();
      if (enemyBattleHp > 0) processEnemyTurn();
    }

    // 6. 적 군량창고 기습
    function execRaidEnemyDepot() {
      playSfx('fire');
      const raidDmg = 45 + Math.floor(Math.random() * 30);
      enemyDepotHp = Math.max(0, enemyDepotHp - raidDmg);
      addBattleLog(`🌾 <strong>[오소 습격!]</strong> 적군 식량저장창고를 방화했습니다! (창고 내구: -${raidDmg}%)`);

      if (enemyDepotHp <= 0) {
        addBattleLog(`🔥 <strong>적군의 식량창고가 완전히 전소되었습니다! 적군이 군량 고갈로 일제히 자멸 투항합니다!</strong>`);
        enemyBattleHp = 0;
      }
      updateBattleHpBars();
      checkBattleState();
      if (enemyBattleHp > 0) processEnemyTurn();
    }

    // 7. 일기토
    function execDuelChallenge() {
      playSfx('sword');
      const p = provincesData[battleTargetProvKey];
      if (curCommander.war > p.genWar) {
        const dmg = 40 + (curCommander.war - p.genWar) * 2;
        enemyBattleHp = Math.max(0, enemyBattleHp - dmg);
        addBattleLog(`⚔️ [일기토 승리] ${curCommander.name}이 적장을 베어 적에게 <strong>${dmg}</strong>의 피해를 입혔습니다!`);
      } else {
        allyBattleHp = Math.max(0, allyBattleHp - 25);
        addBattleLog(`⚔️ [일기토 고전] 적장의 기세에 밀려 아군이 25의 피해를 입었습니다.`);
      }
      updateBattleHpBars();
      checkBattleState();
      if (enemyBattleHp > 0) processEnemyTurn();
    }

    // 적군 AI 턴
    function processEnemyTurn(isCounterMode = false) {
      battleTurn++;
      document.getElementById('battle-turn-count').textContent = battleTurn;

      if (enemyConfusion > 0) {
        enemyConfusion--;
        addBattleLog(`🌀 적군은 아직 <strong>혼란</strong>에 빠져 이번 턴 아무런 반격을 하지 못합니다!`);
        updateBattleHpBars();
        return;
      }

      const targetDepot = Math.random() < 0.4;
      if (targetDepot) {
        let depotDmg = 20 + Math.floor(Math.random() * 15);
        if (isCounterMode) depotDmg = Math.floor(depotDmg * 0.3);

        allyDepotHp = Math.max(0, allyDepotHp - depotDmg);
        addBattleLog(`🚨 <strong class="text-red-400">【적 별동대 군량창고 기습!】</strong> 아군 식량창고를 습격했습니다! (내구: -${depotDmg}% / 현재: ${allyDepotHp}%)`);

        if (allyDepotHp <= 0) {
          triggerDefeat("아군의 식량저장창고가 점령·방화당했습니다! 보급이 끊겨 멸망했습니다!", "식량저장창고 피탈 멸망");
          return;
        }
      } else {
        let allyLoss = 15 + Math.floor(Math.random() * 12);
        if (isCounterMode) allyLoss = Math.floor(allyLoss * 0.2);

        allyBattleHp = Math.max(0, allyBattleHp - allyLoss);
        addBattleLog(`⚔️ 적군 본대의 반격! 아군에게 <strong>${allyLoss}</strong>의 피해를 입혔습니다.`);

        if (allyBattleHp <= 0) {
          triggerDefeat("아군 본대가 전멸하여 전선이 무너졌습니다!", "아군 본대 전멸 멸망");
          return;
        }
      }

      if (battleTurn > battleMaxTurn) {
        if (allyBattleHp > enemyBattleHp) {
          addBattleLog(`⌛ 10턴이 경과했습니다. 우세한 아군 전력으로 적을 압박하여 거점을 수복했습니다!`);
          enemyBattleHp = 0;
          checkBattleState();
        } else {
          triggerDefeat("10턴 장기전으로 군량이 고갈되어 퇴각했습니다!", "군량 고갈 퇴각");
        }
      }

      updateBattleHpBars();
    }

    function checkBattleState() {
      if (enemyBattleHp <= 0) {
        handleBattleVictory();
      }
    }

    function handleBattleVictory() {
      playSfx('fanfare');
      document.getElementById('battle-action-grid').classList.add('hidden');
      document.getElementById('battle-end-panel').classList.remove('hidden');

      const p = provincesData[battleTargetProvKey];
      p.ruler = rulersData[curRulerKey].name.split(' ')[0];
      p.isPlayer = true;

      gold += 2500;
      food += 6000;

      addBattleLog(`
        🏆 <strong class="text-yellow-300 text-sm">【대승리! ${p.name} 완전 정복!】</strong><br>
        전술(함정, 매복, 화공)과 군량창고 사수로 적을 격멸했습니다!<br>
        🎉 <strong>적군 군량 6,000석 탈취 & 금 +2,500전 획득!</strong>
      `);

      checkUnificationProgress();
    }

    function triggerDefeat(reason, title = "비보(悲報)! 군주 멸망!") {
      document.getElementById('battleModal').classList.add('hidden');
      document.getElementById('defeat-title').textContent = title;
      document.getElementById('defeat-desc').innerHTML = `<p>${reason}</p>`;
      document.getElementById('defeatModal').classList.remove('hidden');
      setDialogue(`💀 [패배 비보] ${reason}`);
    }

    function closeBattleModal() {
      document.getElementById('battleModal').classList.add('hidden');
      depotHp = allyDepotHp;
      renderMapPins();
      updateTopBar();
      selectProvince(selectedProvKey);
    }

    function checkUnificationProgress() {
      const allKeys = Object.keys(provincesData);
      const conqueredCount = allKeys.filter(k => provincesData[k].isPlayer).length;
      const percent = Math.floor((conqueredCount / allKeys.length) * 100);

      document.getElementById('txt-conquest-pct').textContent = 
        `${conqueredCount} / ${allKeys.length} 주 (${percent}%)`;

      if (conqueredCount === allKeys.length) {
        setTimeout(() => {
          playSfx('fanfare');
          document.getElementById('ending-ruler-title').textContent = `축하합니다! ${rulersData[curRulerKey].name} 13주 천하통일 완수!`;
          document.getElementById('endingModal').classList.remove('hidden');
        }, 600);
      }
    }

    function saveGame() {
      const saveData = {
        curRulerKey, year, season, month, gold, food, depotHp, lostBasesCount, provincesData, selectedProvKey
      };
      localStorage.setItem('samgukji3_master_save_v3', JSON.stringify(saveData));
      alert(`💾 [삼국지 3 저장 완료]\n${year}년 ${season} ${month}월 시점의 천하 데이터가 저장되었습니다!`);
    }

    function loadGame() {
      const raw = localStorage.getItem('samgukji3_master_save_v3');
      if (!raw) {
        alert('저장된 데이터가 없습니다!');
        return;
      }
      try {
        const data = JSON.parse(raw);
        curRulerKey = data.curRulerKey || 'liubei';
        year = data.year;
        season = data.season;
        month = data.month;
        gold = data.gold;
        food = data.food;
        depotHp = data.depotHp || 100;
        lostBasesCount = data.lostBasesCount || 0;
        Object.assign(provincesData, data.provincesData);
        selectedProvKey = data.selectedProvKey;

        document.getElementById('defeatModal').classList.add('hidden');
        renderMapPins();
        updateTopBar();
        updateCalendar();
        selectProvince(selectedProvKey);
        checkUnificationProgress();
        alert(`📂 [삼국지 3 불러오기 완료]\n${year}년 ${season} ${month}월 시점으로 복귀했습니다!`);
      } catch(e) {
        alert('불러오기 중 오류가 발생했습니다.');
      }
    }

    window.onload = () => {
      initGame();
      window.addEventListener('click', () => initAudio(), { once: true });
    };
  </script>
</body>
</html>
'''

# 치환
html_content = html_template.replace('__MAP_B64__', map_b64)
html_content = html_content.replace('__RULERS_BANNER_B64__', rulers_banner_b64)
html_content = html_content.replace('__PORTRAIT_LIUBEI__', portraits_b64['liubei_classic'])
html_content = html_content.replace('__PORTRAITS_JSON__', json.dumps(portraits_b64))

out_path = r'C:\Users\LENOVO\.gemini\antigravity\brain\54a65f4d-a058-4307-83a1-d8dec8bb9bb0\samgukji_game.html'
with open(out_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print('Generated samgukji_game.html successfully! Size:', len(html_content) / 1024, 'KB')
