# -*- coding: utf-8 -*-
"""
삼국지 3 (三國志 III) 마스터 에디션 빌더
- 13주 고화질 전도
- 유비 및 6대 군주 정식 초상화 Base64
- 10대 메뉴 (0.휴양, 1.군사, 2.인사, 3.외교, 4.정보, 5.개발, 6.계략, 7.상인, 8.특별, 9.기능)
- 금 100 정보 정찰 모달
- 출병 편성 창 (원작 복제)
- 공성전 배틀필드 (유닛 배치, 이동, 공격, 일제사격, 돌격, 일기토, 계략, 군량고 기습, 우측 실시간 전황판)
"""
import os
import json
import base64

def generate_master_game():
    brain_dir = r"C:\Users\LENOVO\.gemini\antigravity\brain\54a65f4d-a058-4307-83a1-d8dec8bb9bb0"
    assets_json = os.path.join(brain_dir, "samguk_b64_assets.json")

    with open(assets_json, "r", encoding="utf-8") as f:
        assets = json.load(f)

    map_b64 = assets["map_b64"]
    battlefield_b64 = assets["battlefield_b64"]
    liubei_b64 = assets["portraits"]["liubei"]
    portraits_json = json.dumps(assets["portraits"])

    html_template = r'''<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>삼국지 3 (三國志 III) 황제의 결단 - 13주 천하통일 & 공성전</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Serif+KR:wght@600;900&family=Nanum+Gothic+Coding:wght@700&display=swap');

    * {
      box-sizing: border-box;
      user-select: none;
    }

    body {
      font-family: 'Nanum Gothic Coding', 'Noto Serif KR', monospace, serif;
      background-color: #030712;
      color: #e2e8f0;
      overflow-x: hidden;
      margin: 0;
      padding: 0;
    }

    /* 삼국지 3 레트로 더블 골드 프레임 */
    .koei-frame {
      background: #000080;
      border: 3px double #d4af37;
      box-shadow: 0 0 12px rgba(0, 0, 0, 0.9), inset 0 0 8px rgba(0, 0, 0, 0.5);
    }
    .koei-subframe {
      border: 1px solid #c59b27;
      background: rgba(0, 0, 60, 0.9);
    }

    /* 상단 메뉴 버튼 */
    .menu-btn {
      background: #000080;
      border: 1.5px solid #d4af37;
      color: #ffffff;
      padding: 4px 9px;
      font-size: 13px;
      font-weight: 800;
      cursor: pointer;
      border-radius: 4px;
      transition: all 0.15s ease-in-out;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      letter-spacing: 0.5px;
      position: relative;
    }
    .menu-btn:hover {
      background: #1e3a8a;
      border-color: #fef08a;
      color: #fef08a;
    }
    .menu-btn:active {
      transform: translateY(1px);
    }

    /* 드롭다운 메뉴 */
    .dropdown-menu {
      position: absolute;
      top: 100%;
      left: 0;
      background: #000066;
      border: 2px double #d4af37;
      min-width: 150px;
      z-index: 100;
      display: none;
      box-shadow: 4px 4px 14px rgba(0, 0, 0, 0.95);
      padding: 4px 0;
    }
    .dropdown-menu.show {
      display: block;
    }
    .dropdown-item {
      padding: 5px 12px;
      font-size: 12.5px;
      color: #ffffff;
      cursor: pointer;
      display: flex;
      align-items: center;
      transition: background 0.15s;
      white-space: nowrap;
    }
    .dropdown-item:hover {
      background: #1e3a8a;
      color: #fde047;
    }
    .dropdown-item.highlight {
      color: #fb923c;
      font-weight: bold;
    }

    /* 청룡 / 황금 게이지 바 */
    .gauge-container {
      position: relative;
      background: #050b1a;
      border: 1px solid #1e293b;
      height: 13px;
      border-radius: 2px;
      overflow: hidden;
    }
    .gauge-dragon {
      height: 100%;
      background: linear-gradient(90deg, #0284c7 0%, #38bdf8 50%, #06b6d4 100%);
      box-shadow: 0 0 6px #38bdf8;
      transition: width 0.4s ease;
    }
    .gauge-gold {
      height: 100%;
      background: linear-gradient(90deg, #d97706 0%, #facc15 50%, #fef08a 100%);
      box-shadow: 0 0 6px #facc15;
      transition: width 0.4s ease;
    }

    /* 초상화 액자 */
    .portrait-box {
      border: 3px double #d4af37;
      background: #000033;
      padding: 2px;
      box-shadow: 0 0 10px rgba(0, 0, 0, 0.8);
      image-rendering: pixelated;
    }

    /* 지도 마커 */
    .map-pin {
      position: absolute;
      transform: translate(-50%, -50%);
      cursor: pointer;
      transition: all 0.2s;
      z-index: 10;
    }
    .map-pin:hover {
      transform: translate(-50%, -50%) scale(1.2);
      z-index: 30;
    }
    .pin-badge {
      padding: 3px 6px;
      border-radius: 4px;
      font-size: 11px;
      font-weight: 800;
      white-space: nowrap;
      border: 1.5px solid #fff;
      box-shadow: 0 2px 8px rgba(0,0,0,0.85);
      display: flex;
      align-items: center;
      gap: 3px;
    }
    .pin-selected {
      outline: 3px solid #facc15;
      box-shadow: 0 0 14px #facc15;
    }

    /* 배틀필드 유닛 마커 */
    .battle-unit {
      position: absolute;
      transform: translate(-50%, -50%);
      cursor: pointer;
      transition: all 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
      z-index: 25;
    }
    .battle-unit:hover {
      transform: translate(-50%, -50%) scale(1.15);
      z-index: 40;
    }
    .unit-badge {
      padding: 4px 8px;
      border-radius: 4px;
      font-size: 11px;
      font-weight: 900;
      border: 2px solid #ffffff;
      box-shadow: 0 3px 10px rgba(0, 0, 0, 0.9);
      display: flex;
      flex-direction: column;
      align-items: center;
      line-height: 1.1;
    }
    .unit-active {
      outline: 3px solid #facc15;
      box-shadow: 0 0 15px #facc15;
      animation: unitPulse 1.2s infinite;
    }
    @keyframes unitPulse {
      0%, 100% { transform: translate(-50%, -50%) scale(1.05); }
      50% { transform: translate(-50%, -50%) scale(1.18); }
    }

    /* 배치 타겟 스팟 (동심원) */
    .deploy-spot {
      position: absolute;
      transform: translate(-50%, -50%);
      width: 32px;
      height: 32px;
      border-radius: 50%;
      border: 2px dashed #facc15;
      background: rgba(250, 204, 21, 0.25);
      cursor: pointer;
      animation: spotBlink 1s infinite alternate;
      z-index: 20;
    }
    @keyframes spotBlink {
      from { transform: translate(-50%, -50%) scale(0.9); opacity: 0.6; }
      to { transform: translate(-50%, -50%) scale(1.2); opacity: 1; }
    }

    /* 모달 */
    .modal-backdrop {
      background: rgba(0, 0, 0, 0.8);
      backdrop-filter: blur(2px);
    }
    .text-pixel {
      text-shadow: 1px 1px 0 #000, -1px -1px 0 #000, 1px -1px 0 #000, -1px 1px 0 #000;
    }
  </style>
</head>
<body class="bg-gray-950 min-h-screen text-slate-100 flex flex-col justify-between">

  <!-- ==================== 상단 메뉴바 (삼국지 3 10대 메뉴) ==================== -->
  <header id="main-header" class="koei-frame px-2 py-1.5 border-b-2 border-amber-500 flex flex-wrap items-center justify-between gap-1 shadow-2xl relative z-40">
    <div class="flex items-center gap-1 flex-wrap">
      
      <!-- 0. 휴양 -->
      <div class="relative">
        <button id="btn-rest" onclick="executeRest()" class="menu-btn !bg-blue-900 border-yellow-400 text-yellow-300 font-black shadow-md hover:!bg-blue-700">
          <span>0. 휴양</span>
        </button>
      </div>

      <!-- 1. 군사 -->
      <div class="relative">
        <button onclick="toggleDropdown('military-menu')" class="menu-btn">
          <span>1. 군사 ▾</span>
        </button>
        <div id="military-menu" class="dropdown-menu">
          <div onclick="openMoveModal()" class="dropdown-item">1. 이 동</div>
          <div onclick="openTransportModal()" class="dropdown-item">2. 수 송</div>
          <div onclick="executeDefenseBoost()" class="dropdown-item highlight">3. 전쟁준비 (성방어력 향상)</div>
          <div onclick="openWarOrganizeModal()" class="dropdown-item highlight font-bold text-red-400 bg-red-950/40">4. 전 쟁 (실전 공성전 출병)</div>
          <div onclick="executeConscription()" class="dropdown-item">5. 징 병</div>
          <div onclick="executeRecruit()" class="dropdown-item">6. 모 병</div>
          <div onclick="executeTraining()" class="dropdown-item">7. 훈 련</div>
          <div onclick="openReorganizeModal()" class="dropdown-item">8. 재편성</div>
          <div onclick="executeShipBuilding()" class="dropdown-item">9. 선박건조</div>
        </div>
      </div>

      <!-- 2. 인사 -->
      <div class="relative">
        <button onclick="toggleDropdown('personnel-menu')" class="menu-btn">
          <span>2. 인사 ▾</span>
        </button>
        <div id="personnel-menu" class="dropdown-menu">
          <div onclick="executeSearchOfficer()" class="dropdown-item">1. 장수수색</div>
          <div onclick="executeHireOfficer()" class="dropdown-item highlight">2. 장수등용</div>
          <div onclick="executeReward()" class="dropdown-item">3. 포 상</div>
          <div onclick="executeRelief()" class="dropdown-item">4. 주민선정 (구호)</div>
          <div onclick="executeDelegate()" class="dropdown-item">5. 위 임</div>
          <div onclick="executeAppoint()" class="dropdown-item">6. 임 명</div>
          <div onclick="executeDirectOrder()" class="dropdown-item">7. 명 령</div>
          <div onclick="executeFireOfficer()" class="dropdown-item">8. 해 고</div>
          <div onclick="executeConfiscate()" class="dropdown-item">9. 몰 수</div>
        </div>
      </div>

      <!-- 3. 외교 -->
      <div class="relative">
        <button onclick="toggleDropdown('diplomacy-menu')" class="menu-btn">
          <span>3. 외교 ▾</span>
        </button>
        <div id="diplomacy-menu" class="dropdown-menu">
          <div onclick="executeAlliance()" class="dropdown-item highlight text-yellow-300 font-bold">1. 동맹체결 (쉬움 / 연합군 파병)</div>
          <div onclick="executeJointOperation()" class="dropdown-item">2. 공동작전</div>
          <div onclick="executeBreakAlliance()" class="dropdown-item text-red-400">3. 동맹파기</div>
          <div onclick="executeDiplomaticExchange()" class="dropdown-item">4. 물자교환</div>
        </div>
      </div>

      <!-- 4. 정보 (금 100 소모 장수 정찰) -->
      <div class="relative">
        <button id="btn-info" onclick="openInfoModal()" class="menu-btn !border-yellow-300 !text-yellow-200 ring-2 ring-yellow-400/50 shadow-lg">
          <span>4. 정보 (금 100)</span>
        </button>
      </div>

      <!-- 5. 개발 -->
      <div class="relative">
        <button onclick="toggleDropdown('develop-menu')" class="menu-btn">
          <span>5. 개발 ▾</span>
        </button>
        <div id="develop-menu" class="dropdown-menu">
          <div onclick="executeLandDev()" class="dropdown-item">1. 개 간 (농업 향상)</div>
          <div onclick="executeFloodControl()" class="dropdown-item">2. 치 수 (홍수 방비)</div>
          <div onclick="executeCommerceDev()" class="dropdown-item">3. 상업투자 (금 수입 증가)</div>
        </div>
      </div>

      <!-- 6. 계략 -->
      <div class="relative">
        <button onclick="toggleDropdown('stratagem-menu')" class="menu-btn !border-orange-400 !text-orange-200">
          <span>6. 계략 ▾</span>
        </button>
        <div id="stratagem-menu" class="dropdown-menu">
          <div onclick="executeStratagem(1)" class="dropdown-item">1. 매복의 독 (복병 침투)</div>
          <div onclick="executeStratagem(2)" class="dropdown-item highlight">2. 적중작적 (배신 유도)</div>
          <div onclick="executeStratagem(3)" class="dropdown-item highlight">3. 위서의심 (충성도 저하)</div>
          <div onclick="executeStratagem(4)" class="dropdown-item">4. 이호경식 (적 군벌 이간)</div>
          <div onclick="executeStratagem(5)" class="dropdown-item highlight">5. 구호탄랑 (태수 반란 유도)</div>
        </div>
      </div>

      <!-- 7. 상인 -->
      <div class="relative">
        <button onclick="toggleDropdown('merchant-menu')" class="menu-btn">
          <span>7. 상인 ▾</span>
        </button>
        <div id="merchant-menu" class="dropdown-menu">
          <div onclick="openTradeModal('sellFood')" class="dropdown-item">1. 군량매출 (쌀팔기)</div>
          <div onclick="openTradeModal('buyFood')" class="dropdown-item">2. 군량매입 (쌀사기)</div>
          <div onclick="openTradeModal('buyWeapons')" class="dropdown-item">3. 무기매입 (노궁/강노)</div>
          <div onclick="openTradeModal('buyHorses')" class="dropdown-item">4. 군마매입 (기병강화)</div>
        </div>
      </div>

      <!-- 8. 특별 -->
      <div class="relative">
        <button onclick="toggleDropdown('special-menu')" class="menu-btn">
          <span>8. 특별 ▾</span>
        </button>
        <div id="special-menu" class="dropdown-menu">
          <div onclick="executeWander()" class="dropdown-item">1. 방 랑</div>
          <div onclick="executeHeal()" class="dropdown-item highlight">2. 치 료</div>
          <div onclick="executeEmergencyTax()" class="dropdown-item">3. 임시징수</div>
          <div onclick="openTaxRateModal()" class="dropdown-item">4. 세율변경</div>
        </div>
      </div>

      <!-- 9. 기능 -->
      <div class="relative">
        <button onclick="toggleDropdown('config-menu')" class="menu-btn">
          <span>9. 기능 ▾</span>
        </button>
        <div id="config-menu" class="dropdown-menu">
          <div onclick="toggleBGM()" class="dropdown-item">1. BGM 음악 켜기/끄기</div>
          <div onclick="saveGame()" class="dropdown-item">2. 게임 저장하기</div>
          <div onclick="loadGame()" class="dropdown-item">3. 게임 불러오기</div>
          <div onclick="openRulerSelectModal()" class="dropdown-item text-yellow-300">4. 군주 변경하기</div>
          <div onclick="resetGame()" class="dropdown-item text-red-400">5. 새로 시작하기</div>
        </div>
      </div>

    </div>

    <!-- 우측 보조 컨트롤 바 -->
    <div class="flex items-center gap-1.5">
      <button id="bgm-btn" onclick="toggleBGM()" class="px-2 py-1 text-xs font-bold rounded bg-amber-700 hover:bg-amber-600 text-yellow-100 border border-yellow-400 flex items-center gap-1 shadow">
        <span id="bgm-icon">🎵</span> BGM: <span id="bgm-status">정지됨</span>
      </button>
      <button onclick="saveGame()" class="px-2 py-1 text-xs font-bold rounded bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-600">
        💾 저장
      </button>
      <button onclick="loadGame()" class="px-2 py-1 text-xs font-bold rounded bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-600">
        📂 로드
      </button>
      <button onclick="executeRest()" class="px-2.5 py-1 text-xs font-black rounded bg-red-800 hover:bg-red-700 text-white border border-red-400 shadow-md">
        ⌛ 턴 넘김
      </button>
    </div>
  </header>

  <!-- ==================== 메인 화면: 13주 전략 지도 모드 ==================== -->
  <main id="strategy-view" class="flex-1 p-2 sm:p-3 flex flex-col lg:flex-row gap-3 overflow-hidden">
    
    <!-- 좌측: 13주 고화질 지도 영역 -->
    <section class="flex-1 koei-frame p-2 flex flex-col relative overflow-hidden rounded shadow-2xl min-h-[540px]">
      
      <div class="flex items-center justify-between bg-blue-950/90 px-3 py-1.5 border border-amber-500/80 rounded mb-2 text-xs sm:text-sm font-bold z-20">
        <div class="flex items-center gap-2">
          <span class="text-amber-400">🗺️ 삼국지 3 전도 (13주 46군현)</span>
          <span class="text-slate-400">|</span>
          <span>선택: <strong id="map-selected-name" class="text-yellow-300">23. 신야 (형주)</strong></span>
        </div>
        <div class="flex items-center gap-3">
          <div class="flex items-center gap-1 text-emerald-400 bg-blue-950/90 px-2.5 py-0.5 rounded border border-emerald-500 shadow">
            <span>🏰 아군 보유 본거지:</span>
            <span id="my-provinces-count" class="font-extrabold text-yellow-300">1</span>개 <span class="text-[11px] text-red-300 font-normal">(모든 영지 피탈 시 멸망)</span>
          </div>
          <div class="text-emerald-400 hidden sm:inline-block">
            천하통일: <strong id="unify-progress" class="text-white">1 / 13주 (8%)</strong>
          </div>
        </div>
      </div>

      <!-- 지도 캔버스 -->
      <div id="map-container" class="relative flex-1 w-full h-[580px] bg-slate-950 rounded overflow-hidden border border-amber-600/60 flex items-center justify-center">
        <img id="samguk-map-img" src="__MAP_B64__" alt="13주 지도" class="w-full h-full object-cover sm:object-contain select-none pointer-events-none opacity-90 brightness-95">
        <div id="map-pins-layer" class="absolute inset-0"></div>

        <div id="weather-badge" class="absolute top-3 left-3 bg-blue-950/85 border border-amber-400 px-3 py-1 rounded text-xs font-bold shadow-lg z-20 flex items-center gap-2">
          <span id="season-text">🌸 208년 1월 (봄)</span>
          <span id="weather-text" class="text-cyan-300">🌤️ 맑음</span>
        </div>

        <div class="absolute bottom-2 left-3 right-3 bg-blue-950/90 border border-slate-700 px-3 py-1 rounded text-[11px] text-slate-300 flex items-center justify-between z-20">
          <span>* 거점을 클릭하고, <strong>[1. 군사 ➔ 4. 전쟁]</strong>으로 인접한 주를 공략하십시오.</span>
          <span class="text-amber-300 font-semibold">동맹국: 청색 표시 & 연합군 15,000 파병</span>
        </div>
      </div>
    </section>

    <!-- 우측: 원작 삼국지 3 3대 패널 (도시 상태창 + 시세창 + 유비 초상화) -->
    <aside class="w-full lg:w-[390px] flex flex-col gap-2.5">
      
      <!-- 1. 도시 정보창 -->
      <div class="koei-frame p-3 relative shadow-xl">
        <div class="flex items-center justify-between border-b border-amber-500/60 pb-1.5 mb-2.5">
          <div class="flex items-center gap-2">
            <span class="w-3.5 h-3.5 bg-emerald-500 border border-white inline-block"></span>
            <span id="panel-city-title" class="font-bold text-base text-white text-pixel tracking-wide">23. 신야</span>
          </div>
          <div class="text-sm font-bold">
            <span class="text-amber-400">군주</span> <span id="panel-ruler-name" class="text-orange-300 font-extrabold text-pixel">유비</span>
          </div>
        </div>

        <div class="flex items-center justify-between text-xs font-bold text-slate-200 mb-2 px-1">
          <div><span class="text-pink-400">태수</span> <span id="panel-governor" class="text-white">유비</span></div>
          <div><span class="text-emerald-400">군사</span> <span id="panel-advisor" class="text-white">관우</span></div>
          <div><span class="text-cyan-400">성 방어</span> <span id="panel-defense" class="text-amber-300 font-mono">65</span></div>
        </div>

        <div class="space-y-1.5 text-xs font-bold">
          <div class="flex items-center justify-between gap-2">
            <span class="text-cyan-300 w-10">인구</span>
            <div class="flex-1 gauge-container"><div id="bar-pop" class="gauge-dragon" style="width: 76%;"></div></div>
            <span id="val-pop" class="w-16 text-right font-mono text-white">382000</span>
          </div>
          <div class="flex items-center justify-between gap-2">
            <span class="text-cyan-300 w-10">금</span>
            <div class="flex-1 gauge-container"><div id="bar-gold" class="gauge-dragon" style="width: 48%;"></div></div>
            <span id="val-gold" class="w-16 text-right font-mono text-yellow-300">2400</span>
          </div>
          <div class="flex items-center justify-between gap-2">
            <span class="text-cyan-300 w-10">군량</span>
            <div class="flex-1 gauge-container"><div id="bar-food" class="gauge-dragon" style="width: 60%;"></div></div>
            <span id="val-food" class="w-16 text-right font-mono text-emerald-300">30000</span>
          </div>
          <div class="flex items-center justify-between gap-2">
            <span class="text-cyan-300 w-10">병사</span>
            <div class="flex-1 gauge-container"><div id="bar-sol" class="gauge-dragon" style="width: 57%;"></div></div>
            <span id="val-sol" class="w-16 text-right font-mono text-red-300">17200</span>
          </div>
          <div class="flex items-center justify-between gap-2">
            <span class="text-cyan-300 w-10">장수</span>
            <div class="flex-1 gauge-container"><div id="bar-off" class="gauge-dragon" style="width: 65%;"></div></div>
            <span id="val-off" class="w-16 text-right font-mono text-white">13</span>
          </div>
          <div class="flex items-center justify-between gap-2">
            <span class="text-yellow-400 w-10">민충</span>
            <div class="flex-1 gauge-container"><div id="bar-loy" class="gauge-gold" style="width: 60%;"></div></div>
            <span id="val-loy" class="w-16 text-right font-mono text-yellow-300">60</span>
          </div>
        </div>

        <div class="mt-2 pt-1.5 border-t border-blue-800 flex items-center justify-between text-[11px]">
          <div class="flex items-center gap-1">
            <span class="text-slate-300">🌾 주군량고:</span>
            <span id="food-storage-status" class="text-emerald-400 font-bold">내구 100% (안전)</span>
          </div>
          <button onclick="repairFoodStorage()" class="px-2 py-0.5 rounded bg-amber-700 hover:bg-amber-600 text-yellow-100 font-bold text-[10px] border border-yellow-400 shadow flex items-center gap-1">
            <span>🛠️</span> 창고 보수 (금 200)
          </button>
        </div>
      </div>

      <!-- 2. 시세창 & 3. 초상화 창 -->
      <div class="flex gap-2.5">
        <div class="w-1/2 koei-frame p-2.5 flex flex-col justify-between">
          <div class="text-center font-bold text-amber-300 border-b border-amber-500/50 pb-1 mb-1 text-xs">시 세</div>
          <div class="space-y-1 text-xs font-mono">
            <div class="flex justify-between"><span class="text-yellow-300 font-bold">쌀 팜</span><span id="rate-rice-sell" class="text-white font-bold">107</span></div>
            <div class="flex justify-between"><span class="text-yellow-300 font-bold">쌀 삼</span><span id="rate-rice-buy" class="text-white font-bold">59</span></div>
            <div class="flex justify-between"><span class="text-amber-200">노 궁</span><span id="rate-crossbow" class="text-white">57</span></div>
            <div class="flex justify-between"><span class="text-amber-200">강 노</span><span id="rate-heavy-bow" class="text-white">95</span></div>
            <div class="flex justify-between"><span class="text-amber-200">군 마</span><span id="rate-horse" class="text-white">49</span></div>
          </div>
          <div class="mt-1 text-[10px] text-slate-400 text-center">* 턴마다 시세 변동</div>
        </div>

        <!-- 군주 초상화 창 (유비 원본 도트 초상화 100% 임베딩) -->
        <div class="w-1/2 koei-frame p-2 flex flex-col items-center justify-between">
          <div class="text-[11px] font-bold text-amber-300 mb-1 text-center w-full border-b border-amber-500/40 pb-0.5">군주 초상화</div>
          <div class="portrait-box w-[95px] h-[115px] bg-blue-950 flex items-center justify-center overflow-hidden">
            <img id="main-ruler-face" src="__LIUBEI_B64__" alt="군주 얼굴" class="w-full h-full object-cover">
          </div>
          <div class="mt-1 text-center">
            <div id="portrait-ruler-name" class="text-xs font-extrabold text-yellow-300">군주 유비 (劉備)</div>
            <div class="text-[10px] text-slate-300">매력: 99 | 통솔: 78</div>
          </div>
        </div>
      </div>

      <!-- 로그 창 -->
      <div class="flex-1 koei-frame p-2.5 flex flex-col min-h-[130px]">
        <div class="flex items-center justify-between text-xs font-bold text-amber-300 border-b border-amber-500/40 pb-1 mb-1.5">
          <span>📜 천하 정세 로그</span>
          <button onclick="clearLogs()" class="text-[10px] text-slate-400 hover:text-white">지우기</button>
        </div>
        <div id="game-logs" class="flex-1 overflow-y-auto space-y-1 text-xs text-slate-200 pr-1 max-h-[140px] font-mono leading-relaxed">
          <div class="text-emerald-400 font-bold">👑 유비가 형주 신야에서 천하통일의 대업을 시작합니다!</div>
          <div class="text-cyan-300">💡 [안내] 4번 [정보]로 적군의 장수와 병력을 정찰할 수 있습니다.</div>
          <div class="text-yellow-300">⚔️ [군사] 1번 [군사 ➔ 4. 전쟁]으로 실전 공성전을 치르십시오!</div>
        </div>
      </div>

    </aside>
  </main>

  <!-- ==================== 배틀 필드 화면: 실전 공성전 모드 ==================== -->
  <main id="battlefield-view" class="flex-1 p-2 sm:p-3 flex flex-col lg:flex-row gap-3 overflow-hidden hidden">
    
    <!-- 좌측/중앙: 삼국지 3 실전 공성전 필드 (성곽, 해자 다리, 숲, 도로) -->
    <section class="flex-1 koei-frame p-2 flex flex-col relative overflow-hidden rounded shadow-2xl min-h-[560px]">
      
      <!-- 상단 전술 가이드 안내바 -->
      <div class="flex items-center justify-between bg-blue-950/90 px-3 py-1.5 border border-amber-500/80 rounded mb-2 text-xs sm:text-sm font-bold z-20">
        <div class="flex items-center gap-2">
          <span class="text-red-400 text-lg">⚔️</span>
          <span id="battle-guide-text" class="text-yellow-300 font-black animate-pulse">
            [배치 단계] 유비를 배치해 주세요 (상단 노란색 배치 구역 클릭)
          </span>
        </div>
        <div class="flex items-center gap-2">
          <div class="flex items-center gap-1 bg-blue-950 px-2 py-0.5 rounded border border-blue-600 text-xs">
            <span class="text-amber-300">🌾 창고 내구:</span>
            <span id="battle-storage-hp" class="text-emerald-400 font-bold font-mono">100%</span>
            <button onclick="emergencyRepairStorageInBattle()" class="ml-1 px-1.5 py-0.2 bg-amber-600 hover:bg-amber-500 text-white font-bold rounded text-[10px] border border-yellow-300">
              🛠️ 수리 (+30%)
            </button>
          </div>
          <span class="text-cyan-300 text-xs">성벽 내구: <strong id="battle-wall-hp" class="text-white font-mono">100/100</strong></span>
          <button onclick="retreatFromBattle()" class="px-2.5 py-0.5 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 border border-slate-600 text-xs font-bold">
            🏳️ 전군 퇴각
          </button>
        </div>
      </div>

      <!-- 배틀 필드 캔버스 컨테이너 (고화질 공성전 필드 배경 완전 임베딩) -->
      <div id="battle-field-container" class="relative flex-1 w-full h-[540px] bg-slate-950 rounded overflow-hidden border-2 border-red-500/80">
        <!-- 공성전 배경 이미지 (삼국지 3 원작) -->
        <img id="battlefield-bg-img" src="__BATTLEFIELD_B64__" alt="공성전 배틀필드" class="w-full h-full object-cover select-none pointer-events-none">

        <!-- 배치 동심원 스팟 레이어 (배치 단계에서 표시) -->
        <div id="deploy-spots-layer" class="absolute inset-0"></div>

        <!-- 유닛 부대 레이어 (아군 녹색, 적군 적색) -->
        <div id="battle-units-layer" class="absolute inset-0"></div>

        <!-- 전투 화염 및 이펙트 오버레이 레이어 -->
        <div id="battle-effects-layer" class="absolute inset-0 pointer-events-none"></div>

        <!-- 하단 전술 조작 명령 패널 (삼국지 3 원작 커맨드 바) -->
        <div id="battle-command-panel" class="absolute bottom-2 left-2 right-2 bg-blue-950/95 border-2 border-amber-400 p-2.5 rounded shadow-2xl flex flex-wrap items-center justify-between gap-2 z-30">
          <div class="flex items-center gap-2">
            <span class="text-xs text-amber-300 font-bold">선택 부대:</span>
            <span id="battle-current-unit-name" class="text-xs text-white font-black bg-blue-900 px-2 py-0.5 rounded border border-blue-500">유비 부대 (4,600명)</span>
          </div>

          <!-- 전략 전술 커맨드 버튼들 -->
          <div class="flex items-center gap-1.5 flex-wrap">
            <button onclick="battleCmdMove()" class="px-2.5 py-1 text-xs font-bold rounded bg-blue-800 hover:bg-blue-700 text-white border border-blue-400 shadow">
              🏃 이동 (진격)
            </button>
            <button onclick="battleCmdAttack()" class="px-2.5 py-1 text-xs font-black rounded bg-red-800 hover:bg-red-700 text-yellow-200 border border-red-400 shadow">
              ⚔️ 근접 공격
            </button>
            <button onclick="battleCmdArchery()" class="px-2.5 py-1 text-xs font-bold rounded bg-amber-800 hover:bg-amber-700 text-white border border-amber-400 shadow">
              🏹 일제사격 (노궁)
            </button>
            <button onclick="battleCmdCavalryCharge()" class="px-2.5 py-1 text-xs font-black rounded bg-purple-900 hover:bg-purple-800 text-yellow-200 border border-purple-400 shadow">
              🐎 기병 돌격!
            </button>
            <button onclick="battleCmdStratagemMenu()" class="px-2.5 py-1 text-xs font-bold rounded bg-emerald-800 hover:bg-emerald-700 text-emerald-200 border border-emerald-400 shadow">
              🧠 전술 계략 ▾
            </button>
            <button onclick="battleCmdDuel()" class="px-2.5 py-1 text-xs font-black rounded bg-orange-700 hover:bg-orange-600 text-white border border-yellow-300 shadow">
              🤺 일기토 신청!
            </button>
            <button onclick="battleCmdEndTurn()" class="px-3 py-1 text-xs font-black rounded bg-slate-800 hover:bg-slate-700 text-yellow-300 border border-yellow-400 shadow">
              ⏳ 턴 종료
            </button>
          </div>
        </div>

        <!-- 전술 계략 서브 팝업 -->
        <div id="battle-stratagem-popup" class="absolute bottom-16 right-24 bg-blue-950 border-2 border-amber-400 rounded p-2 z-40 hidden shadow-2xl space-y-1">
          <div onclick="executeBattleFire()" class="p-1.5 text-xs text-orange-300 hover:bg-blue-900 cursor-pointer rounded font-bold">🔥 화공 (성문/숲 방화)</div>
          <div onclick="executeBattleAmbush()" class="p-1.5 text-xs text-emerald-300 hover:bg-blue-900 cursor-pointer rounded font-bold">🌲 복병 (숲속 기습 매복)</div>
          <div onclick="executeBattleConfuse()" class="p-1.5 text-xs text-yellow-300 hover:bg-blue-900 cursor-pointer rounded font-bold">⚡ 혼란 (유인책)</div>
          <div onclick="executeBattleRaidStorage()" class="p-1.5 text-xs text-red-400 hover:bg-blue-900 cursor-pointer rounded font-black">🌾 주군량고 기습 탈취!</div>
        </div>

      </div>
    </section>

    <!-- 우측: 원작 삼국지 3 배틀필드 전황판 (양양, 날짜, 군세, 군량) -->
    <aside class="w-full lg:w-[360px] flex flex-col gap-2.5">
      
      <!-- 전황 스탯 박스 (원작 화면 100% 동일) -->
      <div class="koei-frame p-3 relative shadow-xl">
        <div class="border-b-2 border-amber-500 pb-2 mb-2.5 text-center">
          <h3 id="battle-panel-city" class="text-lg font-black text-white text-pixel tracking-wider">24 양양 (형주 공성전)</h3>
          <div class="flex items-center justify-center gap-3 text-xs font-bold text-slate-300 mt-1">
            <span id="battle-panel-date">208년 1월</span>
            <span class="text-amber-400">|</span>
            <span id="battle-panel-turn" class="text-pink-300 font-extrabold">1일째 아침</span>
            <span class="text-amber-400">|</span>
            <span id="battle-panel-weather" class="text-cyan-300">맑음</span>
          </div>
        </div>

        <!-- 유표군 VS 유비군 대진표 -->
        <div class="bg-blue-950/80 border border-blue-700 p-2 rounded mb-2.5 text-center">
          <div class="text-sm font-black text-cyan-300 mb-0.5">
            <span id="battle-defender-faction">유표군</span>
            <span class="text-yellow-400 px-2 font-mono text-base">VS</span>
            <span id="battle-attacker-faction" class="text-pink-300">유비군</span>
          </div>
          <div class="flex justify-around text-xs text-slate-300">
            <div>수: <strong id="battle-def-leader" class="text-white">유표</strong></div>
            <div>공: <strong id="battle-att-leader" class="text-white">유비</strong></div>
          </div>
        </div>

        <!-- 군사/자금/군량 대조표 -->
        <div class="space-y-2 text-xs font-mono">
          
          <!-- 총병사수 -->
          <div class="bg-blue-900/40 p-2 rounded border border-blue-800">
            <div class="text-amber-300 font-bold mb-1 flex justify-between">
              <span>총 병 사 수</span>
              <span class="text-slate-400 text-[10px]">수 / 공</span>
            </div>
            <div class="flex justify-between items-center text-sm font-bold">
              <span class="text-cyan-300">수: <span id="battle-def-soldiers" class="font-mono">8700</span></span>
              <span class="text-red-400">공: <span id="battle-att-soldiers" class="font-mono">12200</span></span>
            </div>
          </div>

          <!-- 군자금 -->
          <div class="bg-blue-900/40 p-2 rounded border border-blue-800">
            <div class="text-amber-300 font-bold mb-1 flex justify-between">
              <span>군 자 금</span>
              <span class="text-slate-400 text-[10px]">수 / 공</span>
            </div>
            <div class="flex justify-between items-center text-sm font-bold">
              <span class="text-yellow-300">수: <span id="battle-def-gold" class="font-mono">3000</span></span>
              <span class="text-yellow-300">공: <span id="battle-att-gold" class="font-mono">1000</span></span>
            </div>
          </div>

          <!-- 군량 -->
          <div class="bg-blue-900/40 p-2 rounded border border-blue-800">
            <div class="text-amber-300 font-bold mb-1 flex justify-between">
              <span>군 량</span>
              <span class="text-slate-400 text-[10px]">수 / 공</span>
            </div>
            <div class="flex justify-between items-center text-sm font-bold">
              <span class="text-emerald-300">수: <span id="battle-def-food" class="font-mono">58000</span></span>
              <span class="text-emerald-300">공: <span id="battle-att-food" class="font-mono">10000</span></span>
            </div>
          </div>

        </div>

        <!-- 승리 목표 알림 -->
        <div class="mt-3 p-2 bg-red-950/60 border border-red-700/80 rounded text-[11px] text-amber-200 space-y-0.5">
          <div class="font-bold text-red-300">🎯 승리 조건:</div>
          <div>1. 적 총대장 부대 괴멸 또는 성문 돌파</div>
          <div>2. 적 성내 <strong>주군량고 기습 점령 (일격 즉시 승리!)</strong></div>
        </div>
      </div>

      <!-- 실시간 전투 로그 창 -->
      <div class="flex-1 koei-frame p-2.5 flex flex-col min-h-[140px]">
        <div class="text-xs font-bold text-amber-300 border-b border-amber-500/40 pb-1 mb-1.5 flex justify-between">
          <span>⚔️ 실시간 교전 상황보</span>
          <span class="text-[10px] text-cyan-300 font-normal">턴제 배틀</span>
        </div>
        <div id="battle-logs" class="flex-1 overflow-y-auto space-y-1 text-xs text-slate-200 pr-1 max-h-[160px] font-mono leading-relaxed">
          <div class="text-yellow-300 font-bold">🚩 아군 공격 부대가 양양성 외곽에 도착했습니다!</div>
          <div class="text-cyan-300">💡 먼저 상단 진격로에 유비, 관우 부대를 배치하십시오.</div>
        </div>
      </div>

    </aside>
  </main>

  <!-- ==================== 출병 편성 모달 창 (원작 복제) ==================== -->
  <div id="war-organize-modal" class="fixed inset-0 modal-backdrop z-50 hidden flex items-center justify-center p-3">
    <div class="koei-frame w-full max-w-lg p-4 rounded shadow-2xl border-4 border-amber-400 max-h-[90vh] flex flex-col">
      <div class="flex items-center justify-between border-b-2 border-amber-400 pb-2 mb-3">
        <h2 class="text-lg font-black text-yellow-300 text-pixel">⚔️ 출병 부대 편성 (전쟁 준비)</h2>
        <button onclick="closeModal('war-organize-modal')" class="text-slate-400 hover:text-white font-bold text-lg px-2">✕</button>
      </div>

      <div class="space-y-3 text-xs">
        <div>
          <label class="block font-bold text-amber-300 mb-1">공격 목표 주 (인접한 적국만 선택 가능):</label>
          <select id="org-target-select" onchange="onWarTargetChange()" class="w-full bg-blue-950 border border-amber-400 rounded p-2 text-white font-bold">
            <!-- 동적 인접 주 목록 -->
          </select>
        </div>

        <!-- 출전 장수 목록 (원작 파란 박스 형태) -->
        <div class="bg-blue-950 border-2 border-blue-700 rounded p-2.5">
          <div class="text-amber-300 font-bold border-b border-blue-800 pb-1 mb-2 flex justify-between">
            <span>출전 장수 편성</span>
            <span>병과</span>
          </div>
          <div class="space-y-1.5 font-mono">
            <div class="flex items-center justify-between">
              <label class="flex items-center gap-1.5 cursor-pointer text-yellow-300 font-bold">
                <input type="checkbox" checked disabled class="accent-amber-500">
                <span>* 유비</span>
                <span class="text-slate-300 font-normal">4600</span>
              </label>
              <span class="text-cyan-300">보병</span>
            </div>
            <div class="flex items-center justify-between">
              <label class="flex items-center gap-1.5 cursor-pointer text-slate-200">
                <input type="checkbox" id="chk-guanyu" checked class="accent-amber-500">
                <span class="font-bold text-yellow-200">관우</span>
                <span class="text-slate-300">2400</span>
              </label>
              <span class="text-cyan-300">보병</span>
            </div>
            <div class="flex items-center justify-between">
              <label class="flex items-center gap-1.5 cursor-pointer text-slate-200">
                <input type="checkbox" id="chk-guanping" checked class="accent-amber-500">
                <span>관평</span>
                <span class="text-slate-300">2300</span>
              </label>
              <span class="text-cyan-300">보병</span>
            </div>
            <div class="flex items-center justify-between">
              <label class="flex items-center gap-1.5 cursor-pointer text-slate-200">
                <input type="checkbox" id="chk-zhaoyun" checked class="accent-amber-500">
                <span class="font-bold text-yellow-200">조운</span>
                <span class="text-slate-300">1500</span>
              </label>
              <span class="text-amber-300 font-bold">기병</span>
            </div>
            <div class="flex items-center justify-between">
              <label class="flex items-center gap-1.5 cursor-pointer text-slate-200">
                <input type="checkbox" id="chk-zhangfei" checked class="accent-amber-500">
                <span class="font-bold text-yellow-200">장비</span>
                <span class="text-slate-300">1600</span>
              </label>
              <span class="text-amber-300 font-bold">기병</span>
            </div>
          </div>
        </div>

        <!-- 군자금 및 군량 입력 (원작 삼국지 3 프롬프트 디자인) -->
        <div class="bg-blue-950 border border-amber-500 p-2.5 rounded font-mono space-y-2">
          <div class="flex justify-between text-slate-300">
            <span>금: <strong id="org-my-gold" class="text-yellow-300">2400</strong></span>
            <span>군량: <strong id="org-my-food" class="text-emerald-300">30000</strong></span>
            <span>보유병사: <strong id="org-my-soldiers" class="text-red-300">17200</strong></span>
          </div>
          <div class="border-t border-blue-800 pt-2">
            <label class="block text-amber-300 font-bold mb-1">군량을 얼마나 가지고 가겠습니까 (0-30000)?</label>
            <input type="number" id="org-food-input" value="10000" min="2000" max="30000" step="1000" class="w-full bg-blue-900 border border-yellow-400 rounded p-1.5 text-white font-bold">
          </div>
          <div>
            <label class="block text-amber-300 font-bold mb-1">군자금 (금):</label>
            <input type="number" id="org-gold-input" value="1000" min="200" max="2400" step="200" class="w-full bg-blue-900 border border-yellow-400 rounded p-1.5 text-white font-bold">
          </div>
        </div>

        <!-- 동맹 연합군 참전 알림 -->
        <div id="org-alliance-notice" class="bg-emerald-950/90 border border-emerald-400 p-2 rounded text-emerald-200 font-bold">
          🤝 동맹국 원군 15,000명이 연합 참전합니다! (+50% 추가 타격력)
        </div>
      </div>

      <div class="mt-3 pt-2 border-t border-amber-500/40 flex justify-end gap-2">
        <button onclick="closeModal('war-organize-modal')" class="px-3 py-1 bg-slate-700 hover:bg-slate-600 rounded font-bold">취소</button>
        <button onclick="startBattlefieldBattle()" class="px-5 py-1.5 bg-red-700 hover:bg-red-600 text-white font-black rounded border border-red-300 shadow-xl">
          ⚔️ 출병 확정! (실전 전장 진입)
        </button>
      </div>
    </div>
  </div>

  <!-- ==================== 4. 정보 모달 (금 100 소모 정찰 및 능력치 창) ==================== -->
  <div id="info-modal" class="fixed inset-0 modal-backdrop z-50 hidden flex items-center justify-center p-3">
    <div class="koei-frame w-full max-w-2xl p-4 rounded shadow-2xl border-4 border-amber-400 max-h-[90vh] flex flex-col">
      <div class="flex items-center justify-between border-b-2 border-amber-400 pb-2 mb-3">
        <div class="flex items-center gap-2">
          <span class="text-xl">📜</span>
          <h2 class="text-lg font-black text-yellow-300 text-pixel">
            [정보] <span id="info-target-name">형주</span> 군사 정보 및 장수 명부
          </h2>
        </div>
        <button onclick="closeModal('info-modal')" class="text-slate-400 hover:text-white font-bold text-lg px-2">✕</button>
      </div>

      <div class="bg-blue-950/80 border border-blue-600 px-3 py-1.5 rounded text-xs text-cyan-200 mb-3 flex items-center justify-between">
        <span>🕵️ 세작 정찰 보고 (금 100전 소모 완료): 적과 아군의 장수 상세 능력치와 군사력을 확인합니다.</span>
        <span class="text-amber-300 font-bold">신뢰도: 100%</span>
      </div>

      <!-- 3대 탭 버튼 -->
      <div class="flex gap-2 mb-3">
        <button id="tab-sol" onclick="switchInfoTab('sol')" class="px-3 py-1 rounded text-xs font-bold bg-blue-800 text-yellow-300 border border-yellow-400">
          장수명 / 병사 탭 (기본)
        </button>
        <button id="tab-charm" onclick="switchInfoTab('charm')" class="px-3 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300 border border-slate-600 hover:bg-slate-700">
          장수명 / 매력 탭
        </button>
        <button id="tab-stat" onclick="switchInfoTab('stat')" class="px-3 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300 border border-slate-600 hover:bg-slate-700">
          무력 / 지력 / 훈련도 탭
        </button>
      </div>

      <div class="flex-1 overflow-y-auto bg-blue-950 border-2 border-amber-500/70 rounded p-2">
        <table class="w-full text-xs font-mono text-left">
          <thead class="border-b border-amber-500/50 text-amber-300 bg-blue-900/60 sticky top-0">
            <tr>
              <th class="py-1 px-2 text-center w-12">번호</th>
              <th class="py-1 px-2">장수명</th>
              <th id="th-col1" class="py-1 px-2 text-right">병사 수</th>
              <th id="th-col2" class="py-1 px-2 text-right">훈련도</th>
              <th id="th-col3" class="py-1 px-2 text-right">사기</th>
              <th id="th-col4" class="py-1 px-2 text-right">충성도</th>
            </tr>
          </thead>
          <tbody id="info-officers-tbody" class="divide-y divide-blue-900/40 text-slate-200"></tbody>
        </table>
      </div>

      <div class="mt-3 pt-2 border-t border-amber-500/40 flex items-center justify-between text-xs">
        <span class="text-slate-300">총 주둔 병력: <strong id="info-total-soldiers" class="text-red-400">17,200</strong> 명 | 장수: <strong id="info-total-officers" class="text-white">13</strong> 명</span>
        <button onclick="closeModal('info-modal')" class="px-4 py-1 bg-amber-600 hover:bg-amber-500 text-white font-bold rounded">
          확 인
        </button>
      </div>
    </div>
  </div>

  <!-- 군주 선택 모달 -->
  <div id="ruler-select-modal" class="fixed inset-0 modal-backdrop z-50 hidden flex items-center justify-center p-3">
    <div class="koei-frame w-full max-w-2xl p-4 rounded shadow-2xl border-4 border-amber-400 max-h-[90vh] flex flex-col">
      <div class="flex items-center justify-between border-b-2 border-amber-400 pb-2 mb-3">
        <h2 class="text-lg font-black text-yellow-300 text-pixel">👑 플레이할 군주를 선택하십시오</h2>
        <button onclick="closeModal('ruler-select-modal')" class="text-slate-400 hover:text-white font-bold text-lg px-2">✕</button>
      </div>

      <div class="grid grid-cols-2 sm:grid-cols-3 gap-3 overflow-y-auto p-1">
        <div onclick="selectRuler('liubei')" class="koei-subframe p-2 rounded cursor-pointer hover:border-yellow-300 hover:scale-105 transition flex flex-col items-center">
          <div class="w-16 h-20 portrait-box mb-1"><img src="__LIUBEI_B64__" class="w-full h-full object-cover"></div>
          <span class="font-bold text-sm text-yellow-300">유비 (劉備)</span>
          <span class="text-[10px] text-slate-300">본거지: 형주 (신야)</span>
          <span class="text-[10px] text-emerald-400 font-semibold">특기: 인덕, 의병</span>
        </div>
        <div onclick="selectRuler('caocao')" class="koei-subframe p-2 rounded cursor-pointer hover:border-yellow-300 hover:scale-105 transition flex flex-col items-center">
          <div class="w-16 h-20 portrait-box mb-1"><img id="sel-caocao" src="" class="w-full h-full object-cover"></div>
          <span class="font-bold text-sm text-red-300">조조 (曹操)</span>
          <span class="text-[10px] text-slate-300">본거지: 연주 (허창)</span>
          <span class="text-[10px] text-cyan-400 font-semibold">특기: 패도, 기병</span>
        </div>
        <div onclick="selectRuler('sunquan')" class="koei-subframe p-2 rounded cursor-pointer hover:border-yellow-300 hover:scale-105 transition flex flex-col items-center">
          <div class="w-16 h-20 portrait-box mb-1"><img id="sel-sunquan" src="" class="w-full h-full object-cover"></div>
          <span class="font-bold text-sm text-emerald-300">손권 (孫權)</span>
          <span class="text-[10px] text-slate-300">본거지: 양주 (건업)</span>
          <span class="text-[10px] text-blue-400 font-semibold">특기: 수군, 수성</span>
        </div>
        <div onclick="selectRuler('yuanshao')" class="koei-subframe p-2 rounded cursor-pointer hover:border-yellow-300 hover:scale-105 transition flex flex-col items-center">
          <div class="w-16 h-20 portrait-box mb-1"><img id="sel-yuanshao" src="" class="w-full h-full object-cover"></div>
          <span class="font-bold text-sm text-amber-300">원소 (袁紹)</span>
          <span class="text-[10px] text-slate-300">본거지: 기주 (업)</span>
          <span class="text-[10px] text-yellow-400 font-semibold">특기: 명문, 대군</span>
        </div>
        <div onclick="selectRuler('mateng')" class="koei-subframe p-2 rounded cursor-pointer hover:border-yellow-300 hover:scale-105 transition flex flex-col items-center">
          <div class="w-16 h-20 portrait-box mb-1"><img id="sel-mateng" src="" class="w-full h-full object-cover"></div>
          <span class="font-bold text-sm text-purple-300">마등 (馬騰)</span>
          <span class="text-[10px] text-slate-300">본거지: 량주 (서량)</span>
          <span class="text-[10px] text-red-400 font-semibold">특기: 철기병, 돌격</span>
        </div>
        <div onclick="selectRuler('liubiao')" class="koei-subframe p-2 rounded cursor-pointer hover:border-yellow-300 hover:scale-105 transition flex flex-col items-center">
          <div class="w-16 h-20 portrait-box mb-1"><img id="sel-liubiao" src="" class="w-full h-full object-cover"></div>
          <span class="font-bold text-sm text-sky-300">유표 (劉表)</span>
          <span class="text-[10px] text-slate-300">본거지: 형주 (양양)</span>
          <span class="text-[10px] text-slate-400 font-semibold">특기: 학문, 안정</span>
        </div>
      </div>
    </div>
  </div>

  <!-- 상인 모달 -->
  <div id="trade-modal" class="fixed inset-0 modal-backdrop z-50 hidden flex items-center justify-center p-3">
    <div class="koei-frame w-full max-w-md p-4 rounded shadow-2xl border-4 border-amber-400">
      <div class="flex items-center justify-between border-b-2 border-amber-400 pb-2 mb-3">
        <h2 id="trade-modal-title" class="text-base font-black text-yellow-300 text-pixel">상인 교역소</h2>
        <button onclick="closeModal('trade-modal')" class="text-slate-400 hover:text-white font-bold text-lg px-2">✕</button>
      </div>
      <div class="space-y-3 text-xs">
        <div class="bg-blue-950 p-2.5 rounded border border-blue-700">
          <div class="flex justify-between mb-1"><span class="text-slate-300">현재 금:</span><span id="trade-gold-val" class="text-yellow-300 font-mono font-bold">2400</span></div>
          <div class="flex justify-between"><span class="text-slate-300">현재 군량:</span><span id="trade-food-val" class="text-emerald-300 font-mono font-bold">30000</span></div>
        </div>
        <div>
          <label class="block font-bold text-amber-300 mb-1">거래 수량 입력:</label>
          <input type="number" id="trade-input" value="1000" min="100" max="10000" step="100" class="w-full bg-blue-950 border border-amber-400 rounded p-2 text-white font-mono font-bold">
        </div>
      </div>
      <div class="mt-4 pt-2 border-t border-amber-500/40 flex justify-end gap-2">
        <button onclick="closeModal('trade-modal')" class="px-3 py-1 bg-slate-700 hover:bg-slate-600 rounded">취소</button>
        <button onclick="confirmTrade()" class="px-4 py-1 bg-amber-600 hover:bg-amber-500 text-white font-bold rounded">거래 체결</button>
      </div>
    </div>
  </div>

  <!-- 하단 상태 바 -->
  <footer class="bg-gray-900 border-t border-amber-600/60 px-3 py-1 text-[11px] text-slate-400 flex flex-wrap items-center justify-between">
    <div>
      <span class="text-amber-400 font-bold">三國志 III Master Battle Edition</span> | 공성전 & 13주 천하통일
    </div>
    <div class="flex items-center gap-3">
      <span>단축키: <strong>0</strong> (휴양) | <strong>4</strong> (정보정찰) | <strong>M</strong> (소리토글)</span>
    </div>
  </footer>

  <!-- ==================== 자바스크립트 삼국지 3 게임 & 배틀 엔진 ==================== -->
  <script>
    const PORTRAITS = __PORTRAITS_JSON__;

    const PROVINCES = [
      { id: 1, name: '유주', ruler: '공손찬', leader: '공손찬', advisor: '전주', pop: 280000, gold: 1800, food: 22000, soldiers: 12000, officers: 6, loyalty: 70, defense: 45, x: 74, y: 8, adj: [2, 12] },
      { id: 2, name: '기주', ruler: '원소', leader: '원소', advisor: '저수', pop: 450000, gold: 3500, food: 48000, soldiers: 28000, officers: 12, loyalty: 75, defense: 60, x: 65, y: 17, adj: [1, 3, 4, 12, 13] },
      { id: 3, name: '청주', ruler: '원소', leader: '원담', advisor: '신평', pop: 310000, gold: 2100, food: 25000, soldiers: 14000, officers: 7, loyalty: 65, defense: 40, x: 84, y: 19, adj: [2, 4, 5] },
      { id: 4, name: '연주', ruler: '조조', leader: '조조', advisor: '순욱', pop: 420000, gold: 4200, food: 45000, soldiers: 32000, officers: 15, loyalty: 88, defense: 75, x: 70, y: 26, adj: [2, 3, 5, 6, 13] },
      { id: 5, name: '서주', ruler: '조조', leader: '조인', advisor: '만총', pop: 350000, gold: 2500, food: 30000, soldiers: 18000, officers: 8, loyalty: 72, defense: 50, x: 82, y: 31, adj: [3, 4, 6, 7] },
      { id: 6, name: '예주', ruler: '조조', leader: '하후돈', advisor: '곽가', pop: 390000, gold: 3100, food: 36000, soldiers: 22000, officers: 10, loyalty: 80, defense: 55, x: 67, y: 36, adj: [4, 5, 7, 8, 13] },
      { id: 7, name: '양주', ruler: '손권', leader: '손권', advisor: '주유', pop: 510000, gold: 4800, food: 55000, soldiers: 35000, officers: 16, loyalty: 92, defense: 80, x: 76, y: 55, adj: [5, 6, 8, 9] },
      { id: 8, name: '형주', ruler: '유비', leader: '유비', advisor: '관우', pop: 382000, gold: 2400, food: 30000, soldiers: 17200, officers: 13, loyalty: 60, defense: 65, x: 47, y: 52, adj: [6, 7, 9, 10, 13] },
      { id: 9, name: '교주', ruler: '사섭', leader: '사섭', advisor: '사일', pop: 210000, gold: 1500, food: 18000, soldiers: 9000, officers: 5, loyalty: 85, defense: 35, x: 50, y: 78, adj: [7, 8, 10] },
      { id: 10, name: '익주', ruler: '유장', leader: '유장', advisor: '장송', pop: 480000, gold: 3800, food: 42000, soldiers: 25000, officers: 11, loyalty: 68, defense: 70, x: 20, y: 53, adj: [8, 9, 11, 13] },
      { id: 11, name: '량주', ruler: '마등', leader: '마등', advisor: '한수', pop: 260000, gold: 1900, food: 21000, soldiers: 19000, officers: 8, loyalty: 82, defense: 50, x: 19, y: 19, adj: [10, 12, 13] },
      { id: 12, name: '병주', ruler: '원소', leader: '고간', advisor: '곽원', pop: 240000, gold: 1600, food: 19000, soldiers: 11000, officers: 5, loyalty: 62, defense: 45, x: 44, y: 18, adj: [1, 2, 11, 13] },
      { id: 13, name: '사례교위부', ruler: '조조', leader: '조홍', advisor: '가후', pop: 560000, gold: 5200, food: 60000, soldiers: 38000, officers: 14, loyalty: 85, defense: 90, x: 46, y: 28, adj: [2, 4, 6, 8, 10, 11, 12] }
    ];

    const OFFICERS_DB = {
      '형주': [
        { no: 1, name: '유비', isLeader: true, soldiers: 4600, training: 85, morale: 90, loyalty: 100, charm: 99, war: 75, int: 78 },
        { no: 2, name: '관우', isLeader: true, soldiers: 2400, training: 95, morale: 98, loyalty: 100, charm: 96, war: 98, int: 84 },
        { no: 3, name: '관평', isLeader: true, soldiers: 2300, training: 80, morale: 85, loyalty: 95, charm: 75, war: 83, int: 72 },
        { no: 4, name: '간옹', isLeader: false, soldiers: 0, training: 50, morale: 70, loyalty: 92, charm: 79, war: 32, int: 75 },
        { no: 5, name: '주창', isLeader: false, soldiers: 1400, training: 78, morale: 80, loyalty: 98, charm: 58, war: 82, int: 45 },
        { no: 6, name: '손건', isLeader: false, soldiers: 0, training: 50, morale: 70, loyalty: 94, charm: 90, war: 34, int: 78 },
        { no: 7, name: '조운', isLeader: false, soldiers: 1500, training: 96, morale: 95, loyalty: 100, charm: 93, war: 97, int: 86 },
        { no: 8, name: '장달', isLeader: false, soldiers: 1000, training: 60, morale: 65, loyalty: 65, charm: 21, war: 55, int: 30 },
        { no: 9, name: '조통', isLeader: false, soldiers: 1400, training: 70, morale: 75, loyalty: 88, charm: 70, war: 74, int: 60 },
        { no: 10, name: '장비', isLeader: false, soldiers: 1600, training: 92, morale: 99, loyalty: 100, charm: 36, war: 99, int: 35 },
        { no: 11, name: '미방', isLeader: false, soldiers: 1000, training: 55, morale: 60, loyalty: 70, charm: 55, war: 60, int: 48 },
        { no: 12, name: '미축', isLeader: false, soldiers: 0, training: 50, morale: 70, loyalty: 96, charm: 86, war: 36, int: 76 },
        { no: 13, name: '유봉', isLeader: false, soldiers: 1400, training: 72, morale: 75, loyalty: 82, charm: 62, war: 78, int: 58 }
      ],
      '연주': [
        { no: 1, name: '조조', isLeader: true, soldiers: 8000, training: 95, morale: 95, loyalty: 100, charm: 96, war: 90, int: 94 },
        { no: 2, name: '하후돈', isLeader: true, soldiers: 6000, training: 90, morale: 92, loyalty: 100, charm: 84, war: 92, int: 70 },
        { no: 3, name: '장료', isLeader: false, soldiers: 5000, training: 96, morale: 95, loyalty: 95, charm: 88, war: 95, int: 85 },
        { no: 4, name: '순욱', isLeader: false, soldiers: 0, training: 50, morale: 70, loyalty: 100, charm: 94, war: 25, int: 97 }
      ]
    };

    function generateOfficersForProvince(prov) {
      if (OFFICERS_DB[prov.name]) return OFFICERS_DB[prov.name];
      const res = [];
      res.push({ no: 1, name: prov.leader, isLeader: true, soldiers: Math.floor(prov.soldiers * 0.4), training: 75, morale: 80, loyalty: 100, charm: 80, war: 78, int: 75 });
      res.push({ no: 2, name: prov.advisor, isLeader: false, soldiers: Math.floor(prov.soldiers * 0.2), training: 70, morale: 75, loyalty: 95, charm: 75, war: 50, int: 85 });
      for (let i = 3; i <= prov.officers; i++) {
        res.push({
          no: i, name: prov.name + '부장' + (i - 2), isLeader: false,
          soldiers: Math.floor((prov.soldiers * 0.4) / (prov.officers - 2)),
          training: 65, morale: 70, loyalty: 75, charm: 60, war: 65, int: 55
        });
      }
      return res;
    }

    let gameState = {
      year: 208,
      month: 1,
      currentRuler: 'liubei',
      rulerName: '유비',
      myCapitalId: 8,
      selectedProvId: 8,
      allies: [],
      baseLossCount: 0,
      rates: { riceSell: 107, riceBuy: 59, crossbow: 57, heavyBow: 95, horse: 49 },
      currentInfoTab: 'sol',
      bgmPlaying: false,
      audioCtx: null,
      bgmTimer: null
    };

    // ==================== 공성전 배틀필드 전용 상태 ====================
    let battleState = {
      active: false,
      targetProv: null,
      day: 1,
      timeOfDay: '아침', // 아침, 점심, 저녁
      weather: '맑음',
      defFaction: '유표군',
      attFaction: '유비군',
      defLeader: '유표',
      attLeader: '유비',
      defSoldiers: 8700,
      attSoldiers: 12200,
      defGold: 3000,
      attGold: 1000,
      defFood: 58000,
      attFood: 10000,
      wallHp: 100,
      storageCaptured: false,
      deployStep: 0, // 0: 유비배치, 1: 관우배치, 2: 배치완료
      units: [],
      selectedUnitId: null
    };

    // 초기화
    window.addEventListener('DOMContentLoaded', () => {
      renderMapPins();
      updateRightPanel(gameState.selectedProvId);
      setupRulerPortraits();
      bindKeyboardShortcuts();
      logMessage('🎮 삼국지 3 마스터 에디션이 기동되었습니다.', 'text-emerald-400 font-bold');
    });

    function setupRulerPortraits() {
      const p = PORTRAITS;
      const setImg = (id, key) => { const el = document.getElementById(id); if (el && p[key]) el.src = p[key]; };
      setImg('sel-caocao', 'caocao');
      setImg('sel-sunquan', 'sunquan');
      setImg('sel-yuanshao', 'yuanshao');
      setImg('sel-mateng', 'mateng');
      setImg('sel-liubiao', 'liubiao');
    }

    function renderMapPins() {
      const container = document.getElementById('map-pins-layer');
      container.innerHTML = '';

      PROVINCES.forEach(p => {
        const pin = document.createElement('div');
        pin.className = 'map-pin';
        pin.id = 'pin-' + p.id;
        pin.style.left = p.x + '%';
        pin.style.top = p.y + '%';

        const isMine = (p.ruler === gameState.rulerName);
        const isAlly = gameState.allies.includes(p.ruler);
        const isSelected = (p.id === gameState.selectedProvId);

        let badgeClass = 'bg-red-950/90 border-red-400 text-red-200';
        let icon = '⚔️';
        if (isMine) {
          badgeClass = 'bg-emerald-800 border-yellow-300 text-yellow-200';
          icon = '🚩';
        } else if (isAlly) {
          badgeClass = 'bg-sky-800 border-cyan-300 text-cyan-200';
          icon = '🤝';
        }
        if (isSelected) badgeClass += ' pin-selected ring-2 ring-yellow-400';

        pin.innerHTML = `
          <div class="pin-badge ${badgeClass}">
            <span>${icon}</span>
            <span>${p.id}. ${p.name}</span>
            <span class="text-[9px] opacity-80">(${p.ruler})</span>
          </div>
        `;
        pin.onclick = (e) => { e.stopPropagation(); selectProvince(p.id); };
        container.appendChild(pin);
      });
    }

    function selectProvince(provId) {
      gameState.selectedProvId = provId;
      renderMapPins();
      updateRightPanel(provId);
      const p = PROVINCES.find(x => x.id === provId);
      logMessage(`📍 [선택] ${p.id}. ${p.name} (${p.ruler} 영지, 방어력: ${p.defense})`, 'text-cyan-300');
    }

    function updateRightPanel(provId) {
      const p = PROVINCES.find(x => x.id === provId);
      if (!p) return;

      document.getElementById('map-selected-name').innerText = `${p.id}. ${p.name} (${p.ruler})`;
      document.getElementById('panel-city-title').innerText = `${p.id}. ${p.name}`;
      document.getElementById('panel-ruler-name').innerText = p.ruler;
      document.getElementById('panel-governor').innerText = p.leader;
      document.getElementById('panel-advisor').innerText = p.advisor;
      document.getElementById('panel-defense').innerText = p.defense;

      document.getElementById('val-pop').innerText = p.pop.toLocaleString();
      document.getElementById('val-gold').innerText = p.gold.toLocaleString();
      document.getElementById('val-food').innerText = p.food.toLocaleString();
      document.getElementById('val-sol').innerText = p.soldiers.toLocaleString();
      document.getElementById('val-off').innerText = p.officers;
      document.getElementById('val-loy').innerText = p.loyalty;

      document.getElementById('bar-pop').style.width = Math.min(100, (p.pop / 600000) * 100) + '%';
      document.getElementById('bar-gold').style.width = Math.min(100, (p.gold / 6000) * 100) + '%';
      document.getElementById('bar-food').style.width = Math.min(100, (p.food / 60000) * 100) + '%';
      document.getElementById('bar-sol').style.width = Math.min(100, (p.soldiers / 40000) * 100) + '%';
      document.getElementById('bar-off').style.width = Math.min(100, (p.officers / 20) * 100) + '%';
      document.getElementById('bar-loy').style.width = p.loyalty + '%';

      updateRulerPortraitDisplay(p.ruler);

      document.getElementById('rate-rice-sell').innerText = gameState.rates.riceSell;
      document.getElementById('rate-rice-buy').innerText = gameState.rates.riceBuy;
      document.getElementById('rate-crossbow').innerText = gameState.rates.crossbow;
      document.getElementById('rate-heavy-bow').innerText = gameState.rates.heavyBow;
      document.getElementById('rate-horse').innerText = gameState.rates.horse;

      // 천하통일 및 본거지 보유 수 달성률
      const myProvs = PROVINCES.filter(x => x.ruler === gameState.rulerName).length;
      document.getElementById('unify-progress').innerText = `${myProvs} / 13주 (${Math.round((myProvs / 13) * 100)}%)`;
      const myCountEl = document.getElementById('my-provinces-count');
      if (myCountEl) myCountEl.innerText = myProvs;

      // 만약 아군 영지가 0개가 되면 천하 멸망 (모든 본거지 피탈 시에만 게임 오버)
      if (myProvs === 0) {
        showGameOverModal();
      }
    }

    function updateRulerPortraitDisplay(ruler) {
      const faceImg = document.getElementById('main-ruler-face');
      const nameText = document.getElementById('portrait-ruler-name');
      const p = PORTRAITS;
      if (ruler === '유비') {
        faceImg.src = p['liubei_direct'] || p['liubei'];
        nameText.innerText = '군주 유비 (劉備)';
      } else if (ruler === '조조') {
        faceImg.src = p['caocao'] || p['liubei'];
        nameText.innerText = '군주 조조 (曹操)';
      } else if (ruler === '손권') {
        faceImg.src = p['sunquan'] || p['liubei'];
        nameText.innerText = '군주 손권 (孫權)';
      } else if (ruler === '원소') {
        faceImg.src = p['yuanshao'] || p['liubei'];
        nameText.innerText = '군주 원소 (袁紹)';
      } else if (ruler === '마등') {
        faceImg.src = p['mateng'] || p['liubei'];
        nameText.innerText = '군주 마등 (馬騰)';
      } else if (ruler === '유표') {
        faceImg.src = p['liubiao'] || p['liubei'];
        nameText.innerText = '군주 유표 (劉表)';
      } else {
        faceImg.src = p['liubei_direct'] || p['liubei'];
        nameText.innerText = `군주 ${ruler}`;
      }
    }

    // ==================== 0. 휴양 (턴 넘김) ====================
    function executeRest() {
      playSfx('rest');
      gameState.month++;
      if (gameState.month > 12) {
        gameState.month = 1;
        gameState.year++;
      }
      gameState.rates.riceSell = 90 + Math.floor(Math.random() * 35);
      gameState.rates.riceBuy = 45 + Math.floor(Math.random() * 25);
      gameState.rates.crossbow = 50 + Math.floor(Math.random() * 20);
      gameState.rates.heavyBow = 85 + Math.floor(Math.random() * 25);
      gameState.rates.horse = 40 + Math.floor(Math.random() * 25);

      const seasons = ['봄', '봄', '봄', '여름', '여름', '여름', '가을', '가을', '가을', '겨울', '겨울', '겨울'];
      const icons = ['🌸', '🌸', '🌸', '☀️', '☀️', '☀️', '🍁', '🍁', '🍁', '❄️', '❄️', '❄️'];
      const weathers = ['🌤️ 맑음', '☁️ 흐림', '🌧️ 비', '🌫️ 안개 (기습매복 최적)'];
      const curSeason = seasons[gameState.month - 1];
      const curIcon = icons[gameState.month - 1];
      const curWeather = weathers[Math.floor(Math.random() * weathers.length)];

      document.getElementById('season-text').innerText = `${curIcon} ${gameState.year}년 ${gameState.month}월 (${curSeason})`;
      document.getElementById('weather-text').innerText = curWeather;

      PROVINCES.forEach(p => {
        if (p.ruler === gameState.rulerName) {
          p.food = Math.max(0, p.food - Math.floor(p.soldiers * 0.05));
          if (gameState.month === 7) {
            const tax = Math.floor(p.pop * 0.015);
            p.gold += tax;
            logMessage(`💰 7월 세금 징수: ${p.name}에서 금 ${tax}전 수납`, 'text-yellow-300');
          }
          if (gameState.month === 10) {
            const harvest = Math.floor(p.pop * 0.08);
            p.food += harvest;
            logMessage(`🌾 10월 추수: ${p.name}에서 군량 ${harvest}석 수확`, 'text-emerald-300');
          }
        }
      });

      logMessage(`⌛ [휴양] ${gameState.year}년 ${gameState.month}월로 턴이 넘어갔습니다.`, 'text-yellow-200');
      updateRightPanel(gameState.selectedProvId);
    }

    // ==================== 1. 군사 & 출병 편성 모달 ====================
    // ==================== 식량저장창고 복구 (수리) 함수 ====================
    function repairFoodStorage() {
      const myProv = getMyCapital();
      if (myProv.gold < 200) {
        alert('주군량고(식량창고)를 보수하려면 금 200전이 필요합니다.');
        return;
      }
      playSfx('build');
      myProv.gold -= 200;
      myProv.defense = Math.min(100, myProv.defense + 15);
      
      // 내구도 100% 완전 복구!
      const statusEl = document.getElementById('food-storage-status');
      if (statusEl) {
        statusEl.innerText = '내구 100% (완전 복구됨)';
        statusEl.className = 'text-emerald-400 font-extrabold';
      }
      logMessage(`🛠️ [창고 완벽 보수] 금 200전으로 주군량고를 튼튼하게 수리하여 내구도를 100%로 완전 복구했습니다!`, 'text-emerald-300 font-bold');
      updateRightPanel(myProv.id);
    }

    function emergencyRepairStorageInBattle() {
      if (battleState.attGold < 200) {
        logBattleMessage('⚠️ 긴급 수리를 위한 군자금(금 200전)이 부족합니다!', 'text-red-400');
        return;
      }
      playSfx('build');
      battleState.attGold -= 200;
      const el = document.getElementById('battle-storage-hp');
      let cur = parseInt(el.innerText) || 100;
      cur = Math.min(100, cur + 30);
      el.innerText = cur + '%';
      logBattleMessage(`🛠️ [전장 긴급 수리] 군자금 200전을 투입하여 식량창고 내구도를 +30% 복구했습니다! (현재: ${cur}%)`, 'text-emerald-300 font-bold');
      updateBattlePanel();
    }

    // ==================== 게임 오버 (모든 본거지 피탈 시에만 발생) ====================
    function showGameOverModal() {
      alert('💀 적군에게 모든 본거지와 영지를 빼앗겨 천하의 뜻이 꺾였습니다! (보유 영지: 0개)');
      logMessage('💀 [천하 멸망] 모든 영지를 상실하여 군벌이 해체되었습니다.', 'text-red-500 font-black text-sm');
    }

    function openWarOrganizeModal() {
      closeAllDropdowns();
      const myProv = getMyCapital();
      const select = document.getElementById('org-target-select');
      select.innerHTML = '';

      // 주변(인접한 국경)만 공격 가능
      const adjTargets = PROVINCES.filter(p => myProv.adj.includes(p.id) && p.ruler !== gameState.rulerName);
      if (adjTargets.length === 0) {
        alert('현재 아군 본거지 주변에 맞닿아 있는 적의 영지가 없습니다!');
        return;
      }

      adjTargets.forEach(t => {
        const opt = document.createElement('option');
        opt.value = t.id;
        opt.innerText = `${t.id}. ${t.name} (군주: ${t.ruler}, 병력: ${t.soldiers.toLocaleString()}명)`;
        select.appendChild(opt);
      });

      document.getElementById('org-my-gold').innerText = myProv.gold.toLocaleString();
      document.getElementById('org-my-food').innerText = myProv.food.toLocaleString();
      document.getElementById('org-my-soldiers').innerText = myProv.soldiers.toLocaleString();

      const hasAlliance = gameState.allies.length > 0;
      const notice = document.getElementById('org-alliance-notice');
      if (hasAlliance) {
        notice.classList.remove('hidden');
        notice.innerText = `🤝 동맹국(${gameState.allies.join(', ')}) 원군 15,000명이 연합 참전합니다! (+50% 추가 타격력)`;
      } else {
        notice.classList.add('hidden');
      }

      openModal('war-organize-modal');
    }

    function onWarTargetChange() {}

    // ==================== 2단계: 실전 공성전 배틀필드 돌입 ====================
    function startBattlefieldBattle() {
      const myProv = getMyCapital();
      const targetId = parseInt(document.getElementById('org-target-select').value);
      const targetProv = PROVINCES.find(x => x.id === targetId);
      const foodTaken = parseInt(document.getElementById('org-food-input').value) || 5000;
      const goldTaken = parseInt(document.getElementById('org-gold-input').value) || 500;

      if (!targetProv) return;
      if (myProv.food < foodTaken || myProv.gold < goldTaken) {
        alert('보유 군량이나 군자금이 부족합니다!');
        return;
      }

      myProv.food -= foodTaken;
      myProv.gold -= goldTaken;

      closeModal('war-organize-modal');
      playSfx('war');

      // 배틀 상태 초기화
      battleState.active = true;
      battleState.targetProv = targetProv;
      battleState.day = 1;
      battleState.timeOfDay = '아침';
      battleState.weather = document.getElementById('weather-text').innerText;
      battleState.defFaction = targetProv.ruler + '군';
      battleState.attFaction = gameState.rulerName + '군';
      battleState.defLeader = targetProv.leader;
      battleState.attLeader = gameState.rulerName;
      battleState.defSoldiers = targetProv.soldiers;
      battleState.attSoldiers = 12200; // 편성 부대 총합
      battleState.defGold = targetProv.gold;
      battleState.attGold = goldTaken;
      battleState.defFood = targetProv.food;
      battleState.attFood = foodTaken;
      battleState.wallHp = targetProv.defense || 70;
      battleState.storageCaptured = false;
      battleState.deployStep = 0;

      // 아군 및 적군 유닛 구성
      battleState.units = [
        // 아군
        { id: 'att-1', name: '유비', type: 'infantry', isAttacker: true, soldiers: 4600, war: 75, int: 78, x: 0, y: 0, deployed: false, active: true },
        { id: 'att-2', name: '관우', type: 'infantry', isAttacker: true, soldiers: 2400, war: 98, int: 84, x: 0, y: 0, deployed: false, active: false },
        { id: 'att-3', name: '장비', type: 'cavalry', isAttacker: true, soldiers: 1600, war: 99, int: 35, x: 0, y: 0, deployed: false, active: false },
        { id: 'att-4', name: '조운', type: 'cavalry', isAttacker: true, soldiers: 1500, war: 97, int: 86, x: 0, y: 0, deployed: false, active: false },
        // 적군 (성내 및 성문 앞 배치)
        { id: 'def-1', name: targetProv.leader, type: 'infantry', isAttacker: false, soldiers: Math.floor(targetProv.soldiers * 0.5), war: 82, int: 75, x: 26, y: 55, deployed: true, active: true },
        { id: 'def-2', name: targetProv.advisor, type: 'archer', isAttacker: false, soldiers: Math.floor(targetProv.soldiers * 0.3), war: 60, int: 85, x: 40, y: 65, deployed: true, active: true },
        { id: 'def-3', name: '수비대장', type: 'cavalry', isAttacker: false, soldiers: Math.floor(targetProv.soldiers * 0.2), war: 75, int: 60, x: 18, y: 72, deployed: true, active: true }
      ];

      // 뷰 전환: 전략 지도 숨기고 배틀필드 표시
      document.getElementById('strategy-view').classList.add('hidden');
      document.getElementById('battlefield-view').classList.remove('hidden');

      // 전황판 갱신
      updateBattlePanel();
      setupDeploySpots();
      logBattleMessage(`🚩 ${targetProv.name} 공성전이 시작되었습니다! 유비군이 성문 외곽에 집결했습니다.`, 'text-yellow-300 font-extrabold');
      logBattleMessage(`💡 상단 진격로에 유비를 배치해 주십시오.`, 'text-cyan-300 font-bold');
    }

    // 배치 스팟 (원작 삼국지 3 동심원 타겟 위치들)
    const DEPLOY_COORDS = [
      { x: 48, y: 20 },
      { x: 55, y: 24 },
      { x: 62, y: 26 },
      { x: 70, y: 30 }
    ];

    function setupDeploySpots() {
      const container = document.getElementById('deploy-spots-layer');
      container.innerHTML = '';

      if (battleState.deployStep >= 4) return; // 배치 완료

      const names = ['유비', '관우', '장비', '조운'];
      const curName = names[battleState.deployStep];
      document.getElementById('battle-guide-text').innerText = `[배치 단계] ${curName}를 배치해 주세요 (노란색 원형 스팟 클릭)`;

      DEPLOY_COORDS.forEach((c, idx) => {
        const spot = document.createElement('div');
        spot.className = 'deploy-spot';
        spot.style.left = c.x + '%';
        spot.style.top = c.y + '%';
        spot.onclick = () => onDeploySpotClicked(c.x, c.y);
        container.appendChild(spot);
      });
    }

    function onDeploySpotClicked(x, y) {
      const attUnits = battleState.units.filter(u => u.isAttacker);
      const curUnit = attUnits[battleState.deployStep];
      if (!curUnit) return;

      curUnit.x = x;
      curUnit.y = y;
      curUnit.deployed = true;
      battleState.deployStep++;
      playSfx('rest');

      logBattleMessage(`📍 [배치 완료] ${curUnit.name} 부대가 진격로(${x}%, ${y}%)에 진을 쳤습니다.`, 'text-emerald-300');

      if (battleState.deployStep >= 4) {
        document.getElementById('deploy-spots-layer').innerHTML = '';
        document.getElementById('battle-guide-text').innerText = `⚔️ [전투 개시] 부대를 선택하여 이동/공격/계략 명령을 내리십시오!`;
        battleState.selectedUnitId = 'att-1';
        renderBattleUnits();
        updateBattleCommandPanel();
      } else {
        setupDeploySpots();
        renderBattleUnits();
      }
    }

    // 유닛 렌더링
    function renderBattleUnits() {
      const container = document.getElementById('battle-units-layer');
      container.innerHTML = '';

      battleState.units.forEach(u => {
        if (!u.deployed || u.soldiers <= 0) return;

        const el = document.createElement('div');
        el.className = 'battle-unit';
        el.id = 'unit-' + u.id;
        el.style.left = u.x + '%';
        el.style.top = u.y + '%';

        const isSelected = (u.id === battleState.selectedUnitId);
        let badgeClass = u.isAttacker ? 'bg-emerald-900 border-yellow-300 text-yellow-200' : 'bg-red-950 border-red-400 text-red-200';
        if (isSelected) badgeClass += ' unit-active ring-2 ring-yellow-400';

        const icon = (u.type === 'cavalry') ? '🐎' : (u.type === 'archer') ? '🏹' : '🛡️';

        el.innerHTML = `
          <div class="unit-badge ${badgeClass}">
            <div class="flex items-center gap-1">
              <span>${icon}</span>
              <span>${u.name}</span>
            </div>
            <span class="text-[9px] font-mono">${u.soldiers.toLocaleString()}</span>
          </div>
        `;

        el.onclick = (e) => {
          e.stopPropagation();
          if (u.isAttacker) {
            battleState.selectedUnitId = u.id;
            renderBattleUnits();
            updateBattleCommandPanel();
          } else {
            // 적군 클릭 시 근접 공격 시도
            targetEnemyUnit(u);
          }
        };

        container.appendChild(el);
      });
    }

    function updateBattleCommandPanel() {
      const u = battleState.units.find(x => x.id === battleState.selectedUnitId);
      if (!u) return;
      document.getElementById('battle-current-unit-name').innerText = `${u.name} 부대 (${u.soldiers.toLocaleString()}명, 무력:${u.war})`;
    }

    function updateBattlePanel() {
      const p = battleState.targetProv;
      document.getElementById('battle-panel-city').innerText = `${p.id}. ${p.name} (공성전)`;
      document.getElementById('battle-panel-turn').innerText = `${battleState.day}일째 ${battleState.timeOfDay}`;
      document.getElementById('battle-panel-weather').innerText = battleState.weather;
      document.getElementById('battle-defender-faction').innerText = battleState.defFaction;
      document.getElementById('battle-attacker-faction').innerText = battleState.attFaction;
      document.getElementById('battle-def-leader').innerText = battleState.defLeader;
      document.getElementById('battle-att-leader').innerText = battleState.attLeader;

      document.getElementById('battle-def-soldiers').innerText = battleState.defSoldiers.toLocaleString();
      document.getElementById('battle-att-soldiers').innerText = battleState.attSoldiers.toLocaleString();
      document.getElementById('battle-def-gold').innerText = battleState.defGold.toLocaleString();
      document.getElementById('battle-att-gold').innerText = battleState.attGold.toLocaleString();
      document.getElementById('battle-def-food').innerText = battleState.defFood.toLocaleString();
      document.getElementById('battle-att-food').innerText = battleState.attFood.toLocaleString();
      document.getElementById('battle-wall-hp').innerText = `${battleState.wallHp}/100`;
    }

    // ==================== 전략적 전투 커맨드 실행 ====================
    // 1. 이동
    function battleCmdMove() {
      const u = battleState.units.find(x => x.id === battleState.selectedUnitId);
      if (!u) return;
      playSfx('rest');

      // 성벽과 성문 쪽으로 전진 (대각선 쿼터뷰 좌표 이동)
      u.x = Math.max(15, u.x - 7);
      u.y = Math.min(80, u.y + 10);
      renderBattleUnits();

      logBattleMessage(`🏃 [진격] ${u.name} 부대가 성벽 앞 교전 지역으로 전진했습니다! (위치: ${u.x}%, ${u.y}%)`, 'text-cyan-300');
    }

    // 2. 근접 공격
    function battleCmdAttack() {
      const u = battleState.units.find(x => x.id === battleState.selectedUnitId);
      const enemy = battleState.units.find(x => !x.isAttacker && x.soldiers > 0);
      if (!u || !enemy) {
        logBattleMessage('⚠️ 공격할 적 부대가 없습니다.', 'text-slate-400');
        return;
      }
      playSfx('war');

      // 무력 및 상성 계산
      let dmg = Math.floor(u.soldiers * (u.war / 100) * 0.45);
      if (gameState.allies.length > 0) dmg = Math.floor(dmg * 1.5); // 동맹 연합군 보너스

      enemy.soldiers = Math.max(0, enemy.soldiers - dmg);
      battleState.defSoldiers = Math.max(0, battleState.defSoldiers - dmg);

      // 반격
      const counterDmg = Math.floor(enemy.soldiers * 0.15);
      u.soldiers = Math.max(0, u.soldiers - counterDmg);
      battleState.attSoldiers = Math.max(0, battleState.attSoldiers - counterDmg);

      logBattleMessage(`⚔️ [백병전] ${u.name} 부대가 ${enemy.name} 부대를 난타하여 ${dmg.toLocaleString()}명을 쓰러뜨렸습니다! (반격 피해: ${counterDmg}명)`, 'text-red-400 font-bold');

      renderBattleUnits();
      updateBattlePanel();
      checkBattleOutcome();
    }

    // 3. 원거리 일제사격
    function battleCmdArchery() {
      const u = battleState.units.find(x => x.id === battleState.selectedUnitId);
      const enemy = battleState.units.find(x => !x.isAttacker && x.soldiers > 0);
      if (!u || !enemy) return;
      playSfx('war');

      const dmg = Math.floor(u.soldiers * 0.28);
      enemy.soldiers = Math.max(0, enemy.soldiers - dmg);
      battleState.defSoldiers = Math.max(0, battleState.defSoldiers - dmg);

      logBattleMessage(`🏹 [화살비 일제사격] 노궁 부대가 성벽 위 ${enemy.name} 부대에 화살비를 퍼부어 ${dmg.toLocaleString()}명의 피해를 입혔습니다! (반격 없음)`, 'text-amber-300 font-bold');

      renderBattleUnits();
      updateBattlePanel();
      checkBattleOutcome();
    }

    // 4. 기병 돌격
    function battleCmdCavalryCharge() {
      const u = battleState.units.find(x => x.id === battleState.selectedUnitId);
      const enemy = battleState.units.find(x => !x.isAttacker && x.soldiers > 0);
      if (!u || !enemy) return;
      playSfx('war');

      const dmg = Math.floor(u.soldiers * 0.65);
      enemy.soldiers = Math.max(0, enemy.soldiers - dmg);
      battleState.defSoldiers = Math.max(0, battleState.defSoldiers - dmg);

      const rebound = Math.floor(dmg * 0.1);
      u.soldiers = Math.max(0, u.soldiers - rebound);
      battleState.attSoldiers = Math.max(0, battleState.attSoldiers - rebound);

      logBattleMessage(`🐎 [돌격!!] ${u.name}의 기병대가 적 진형을 짓밟고 돌파하여 ${dmg.toLocaleString()}명을 궤멸시켰습니다!`, 'text-yellow-300 font-extrabold');

      renderBattleUnits();
      updateBattlePanel();
      checkBattleOutcome();
    }

    // 5. 계략 메뉴 토글
    function battleCmdStratagemMenu() {
      const p = document.getElementById('battle-stratagem-popup');
      p.classList.toggle('hidden');
    }

    // 화공
    function executeBattleFire() {
      document.getElementById('battle-stratagem-popup').classList.add('hidden');
      playSfx('war');
      battleState.wallHp = Math.max(0, battleState.wallHp - 25);
      const enemy = battleState.units.find(x => !x.isAttacker && x.soldiers > 0);
      if (enemy) {
        enemy.soldiers = Math.max(0, enemy.soldiers - 800);
        battleState.defSoldiers = Math.max(0, battleState.defSoldiers - 800);
      }
      logBattleMessage(`🔥 [화공 적중!] 성문과 목책에 불을 질러 성벽 내구를 -25 깎고 적에게 800명의 화염 피해를 입혔습니다!`, 'text-orange-400 font-bold');
      renderBattleUnits();
      updateBattlePanel();
      checkBattleOutcome();
    }

    // 복병
    function executeBattleAmbush() {
      document.getElementById('battle-stratagem-popup').classList.add('hidden');
      playSfx('war');
      const enemy = battleState.units.find(x => !x.isAttacker && x.soldiers > 0);
      if (enemy) {
        enemy.soldiers = Math.max(0, enemy.soldiers - 1200);
        battleState.defSoldiers = Math.max(0, battleState.defSoldiers - 1200);
      }
      logBattleMessage(`🌲 [숲속 복병 기습!] 숲에 매복해있던 조운의 복병이 적의 측면을 덮쳐 1,200명을 혼란에 빠뜨렸습니다!`, 'text-emerald-300 font-bold');
      renderBattleUnits();
      updateBattlePanel();
      checkBattleOutcome();
    }

    // 혼란
    function executeBattleConfuse() {
      document.getElementById('battle-stratagem-popup').classList.add('hidden');
      logBattleMessage(`⚡ [적군 혼란] 위장 깃발로 적의 지휘 체계를 마비시켜 1턴간 조작 불능 상태로 만들었습니다!`, 'text-yellow-300 font-bold');
    }

    // 주군량고 기습 탈취! (일격 승리)
    function executeBattleRaidStorage() {
      document.getElementById('battle-stratagem-popup').classList.add('hidden');
      playSfx('victory');
      battleState.storageCaptured = true;
      battleState.defFood = 0;
      battleState.defSoldiers = 0;

      logBattleMessage(`🌾 [대성공!!] 성내 주군량고를 기습하여 적의 모든 군량을 전소시켰습니다! 적군 전원이 탈영하여 즉시 항복했습니다!`, 'text-yellow-300 font-black text-sm');
      setTimeout(concludeBattleVictory, 1200);
    }

    // 6. 일기토 (단기접전)
    function battleCmdDuel() {
      const u = battleState.units.find(x => x.id === battleState.selectedUnitId);
      const enemy = battleState.units.find(x => !x.isAttacker && x.soldiers > 0);
      if (!u || !enemy) return;

      playSfx('war');
      if (u.war >= enemy.war) {
        playSfx('victory');
        const capSoldiers = enemy.soldiers;
        enemy.soldiers = 0;
        battleState.defSoldiers = Math.max(0, battleState.defSoldiers - capSoldiers);
        logBattleMessage(`🤺 [일기토 승리!] ${u.name}(무력 ${u.war})이 적장 ${enemy.name}(무력 ${enemy.war})의 목을 베거나 생포했습니다! 적 부대 즉시 전멸!`, 'text-yellow-300 font-black');
      } else {
        u.soldiers = Math.max(0, u.soldiers - 1000);
        logBattleMessage(`⚠️ [일기토 무승부] ${u.name}과 ${enemy.name}이 80합을 겨루다 부상을 입고 말머리를 돌렸습니다.`, 'text-red-300 font-bold');
      }

      renderBattleUnits();
      updateBattlePanel();
      checkBattleOutcome();
    }

    // 7. 턴 종료
    function battleCmdEndTurn() {
      playSfx('rest');
      if (battleState.timeOfDay === '아침') battleState.timeOfDay = '점심';
      else if (battleState.timeOfDay === '점심') battleState.timeOfDay = '저녁';
      else {
        battleState.timeOfDay = '아침';
        battleState.day++;
        battleState.attFood = Math.max(0, battleState.attFood - 300);
        battleState.defFood = Math.max(0, battleState.defFood - 400);
      }

      // 적 AI 반격
      const att = battleState.units.find(x => x.isAttacker && x.soldiers > 0);
      const def = battleState.units.find(x => !x.isAttacker && x.soldiers > 0);
      if (att && def) {
        const aiDmg = Math.floor(def.soldiers * 0.12);
        att.soldiers = Math.max(0, att.soldiers - aiDmg);
        battleState.attSoldiers = Math.max(0, battleState.attSoldiers - aiDmg);
        logBattleMessage(`🛡️ [적군 턴] ${def.name} 부대가 반격을 가해 ${att.name} 부대에 ${aiDmg}명의 피해를 주었습니다.`, 'text-slate-300');
      }

      renderBattleUnits();
      updateBattlePanel();
      checkBattleOutcome();
    }

    function checkBattleOutcome() {
      if (battleState.defSoldiers <= 0 || battleState.wallHp <= 0) {
        setTimeout(concludeBattleVictory, 800);
      } else if (battleState.attSoldiers <= 0 || battleState.attFood <= 0) {
        setTimeout(concludeBattleDefeat, 800);
      }
    }

    function concludeBattleVictory() {
      playSfx('victory');
      const p = battleState.targetProv;
      p.ruler = gameState.rulerName;
      p.leader = gameState.rulerName;
      p.soldiers = 10000;
      p.defense = 50;

      alert(`🎉 [공성전 대승리!] ${p.name} 성을 완벽히 함락하고 영지로 흡수했습니다!`);
      exitBattlefield();
      checkUnification();
    }

    function concludeBattleDefeat() {
      alert(`⚠️ [패배] 아군 병력이 소진되어 퇴각합니다.`);
      exitBattlefield();
    }

    function retreatFromBattle() {
      if (confirm('전장에서 퇴각하시겠습니까? (군자금과 군량 일부 손실)')) {
        exitBattlefield();
      }
    }

    function exitBattlefield() {
      battleState.active = false;
      document.getElementById('battlefield-view').classList.add('hidden');
      document.getElementById('strategy-view').classList.remove('hidden');
      renderMapPins();
      updateRightPanel(gameState.selectedProvId);
    }

    function targetEnemyUnit(enemy) {
      logBattleMessage(`🎯 적군 [${enemy.name} 부대]를 타깃으로 지정했습니다. 공격 버튼을 누르십시오!`, 'text-yellow-300');
    }

    function logBattleMessage(msg, colorClass='text-slate-200') {
      const container = document.getElementById('battle-logs');
      if (!container) return;
      const div = document.createElement('div');
      div.className = colorClass;
      div.innerHTML = msg;
      container.appendChild(div);
      container.scrollTop = container.scrollHeight;
    }

    // ==================== 4. 정보 모달 (금 100 소모) ====================
    function openInfoModal() {
      closeAllDropdowns();
      const myProv = getMyCapital();
      if (myProv.gold < 100) { alert('금 100전이 필요합니다.'); return; }
      playSfx('info');
      myProv.gold -= 100;
      const targetProv = PROVINCES.find(x => x.id === gameState.selectedProvId);
      document.getElementById('info-target-name').innerText = `${targetProv.id}. ${targetProv.name} (${targetProv.ruler} 세력)`;
      renderInfoOfficersList(targetProv);
      openModal('info-modal');
      logMessage(`🕵️ [정보 정찰] 금 100전 소모: ${targetProv.name}의 장수 명부와 군사력을 정밀 정찰했습니다!`, 'text-yellow-300 font-bold');
      updateRightPanel(myProv.id);
    }

    function switchInfoTab(tab) {
      gameState.currentInfoTab = tab;
      document.getElementById('tab-sol').className = (tab === 'sol') ? 'px-3 py-1 rounded text-xs font-bold bg-blue-800 text-yellow-300 border border-yellow-400' : 'px-3 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300 border border-slate-600 hover:bg-slate-700';
      document.getElementById('tab-charm').className = (tab === 'charm') ? 'px-3 py-1 rounded text-xs font-bold bg-blue-800 text-yellow-300 border border-yellow-400' : 'px-3 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300 border border-slate-600 hover:bg-slate-700';
      document.getElementById('tab-stat').className = (tab === 'stat') ? 'px-3 py-1 rounded text-xs font-bold bg-blue-800 text-yellow-300 border border-yellow-400' : 'px-3 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300 border border-slate-600 hover:bg-slate-700';
      const targetProv = PROVINCES.find(x => x.id === gameState.selectedProvId);
      renderInfoOfficersList(targetProv);
    }

    function renderInfoOfficersList(prov) {
      const tbody = document.getElementById('info-officers-tbody');
      tbody.innerHTML = '';
      const officers = generateOfficersForProvince(prov);
      const tab = gameState.currentInfoTab;

      const th1 = document.getElementById('th-col1');
      const th2 = document.getElementById('th-col2');
      const th3 = document.getElementById('th-col3');
      const th4 = document.getElementById('th-col4');

      if (tab === 'sol') {
        th1.innerText = '병사 수'; th2.innerText = '훈련도'; th3.innerText = '사기'; th4.innerText = '충성도';
      } else if (tab === 'charm') {
        th1.innerText = '매 력'; th2.innerText = '통 솔'; th3.innerText = '직 책'; th4.innerText = '충성도';
      } else {
        th1.innerText = '무 력'; th2.innerText = '지 력'; th3.innerText = '훈련도'; th4.innerText = '충성도';
      }

      let totalSol = 0;
      officers.forEach(off => {
        totalSol += off.soldiers;
        const tr = document.createElement('tr');
        tr.className = 'hover:bg-blue-900/40 transition';

        let col1, col2, col3, col4;
        if (tab === 'sol') {
          col1 = `<span class="text-red-300 font-bold">${off.soldiers.toLocaleString()}</span>`;
          col2 = `<span class="text-cyan-300">${off.training}</span>`;
          col3 = `<span class="text-yellow-300">${off.morale}</span>`;
          col4 = `<span class="text-emerald-300">${off.loyalty}</span>`;
        } else if (tab === 'charm') {
          col1 = `<span class="text-pink-300 font-extrabold">${off.charm}</span>`;
          col2 = `<span class="text-blue-300">${off.war || 70}</span>`;
          col3 = `<span class="text-slate-300">${off.isLeader ? '군주/맹장' : '부장'}</span>`;
          col4 = `<span class="text-emerald-300">${off.loyalty}</span>`;
        } else {
          col1 = `<span class="text-red-400 font-bold">${off.war}</span>`;
          col2 = `<span class="text-cyan-400 font-bold">${off.int}</span>`;
          col3 = `<span class="text-yellow-300">${off.training}</span>`;
          col4 = `<span class="text-emerald-300">${off.loyalty}</span>`;
        }

        const mark = off.isLeader ? '<span class="text-amber-400">*</span>' : '';
        tr.innerHTML = `
          <td class="py-1 px-2 text-center text-slate-400">${off.no}</td>
          <td class="py-1 px-2 font-bold ${off.isLeader ? 'text-yellow-300' : 'text-slate-200'}">${off.name} ${mark}</td>
          <td class="py-1 px-2 text-right font-mono">${col1}</td>
          <td class="py-1 px-2 text-right font-mono">${col2}</td>
          <td class="py-1 px-2 text-right font-mono">${col3}</td>
          <td class="py-1 px-2 text-right font-mono">${col4}</td>
        `;
        tbody.appendChild(tr);
      });

      document.getElementById('info-total-soldiers').innerText = totalSol.toLocaleString();
      document.getElementById('info-total-officers').innerText = officers.length;
    }

    // ==================== 6. 계략 ====================
    function executeStratagem(type) {
      closeAllDropdowns();
      const myProv = getMyCapital();
      const targetProv = PROVINCES.find(x => x.id === gameState.selectedProvId);
      if (targetProv.ruler === gameState.rulerName) { alert('아군 영지에는 계략을 걸 수 없습니다.'); return; }
      if (myProv.gold < 150) { alert('금 150전이 필요합니다.'); return; }

      playSfx('stratagem');
      myProv.gold -= 150;

      if (type === 1) {
        targetProv.defense = Math.max(10, targetProv.defense - 15);
        logMessage(`🗡️ [매복의 독] ${targetProv.name}의 성내에 복병을 심어 방어력을 -15 깎았습니다!`, 'text-orange-400 font-bold');
      } else if (type === 2) {
        targetProv.loyalty = Math.max(10, targetProv.loyalty - 18);
        logMessage(`📜 [적중작적] ${targetProv.leader}에게 밀서를 보내 결전 시 배신 약속을 받아냈습니다!`, 'text-orange-400 font-bold');
      } else if (type === 3) {
        targetProv.loyalty = Math.max(10, targetProv.loyalty - 25);
        logMessage(`✉️ [위서의심] 적 군주에게 위조 서신을 보내 장수의 충성도를 -25 급락시켰습니다!`, 'text-orange-400 font-bold');
      } else if (type === 4) {
        logMessage(`🐯 [이호경식] ${targetProv.ruler} 세력과 주변 군벌 사이에 불화를 일으켰습니다!`, 'text-orange-400 font-bold');
      } else if (type === 5) {
        targetProv.soldiers = Math.floor(targetProv.soldiers * 0.75);
        logMessage(`🐺 [구호탄랑] 태수가 반란을 꾀해 내분이 일어나 적 병력 25%가 이탈했습니다!`, 'text-orange-400 font-bold');
      }
      updateRightPanel(targetProv.id);
    }

    // ==================== 3. 외교 ====================
    function executeAlliance() {
      closeAllDropdowns();
      const myProv = getMyCapital();
      const targetProv = PROVINCES.find(x => x.id === gameState.selectedProvId);
      if (targetProv.ruler === gameState.rulerName) { alert('자신과는 동맹을 맺을 수 없습니다.'); return; }
      if (gameState.allies.includes(targetProv.ruler)) { alert('이미 굳건한 동맹 관계입니다!'); return; }
      if (myProv.gold < 500) { alert('금 500전이 필요합니다.'); return; }

      playSfx('alliance');
      myProv.gold -= 500;
      if (Math.random() < 0.90) { // 90% 성립
        gameState.allies.push(targetProv.ruler);
        logMessage(`🤝 [동맹 체결] ${targetProv.ruler} 세력과 군사 동맹을 맺었습니다! 출병 시 15,000명의 연합군이 가세합니다!`, 'text-emerald-300 font-extrabold');
      } else {
        logMessage(`⚠️ [동맹 결렬] ${targetProv.ruler}이(가) 예물만 받고 결정을 유보했습니다.`, 'text-slate-300');
      }
      renderMapPins();
      updateRightPanel(myProv.id);
    }

    function executeBreakAlliance() {
      closeAllDropdowns();
      const targetProv = PROVINCES.find(x => x.id === gameState.selectedProvId);
      const idx = gameState.allies.indexOf(targetProv.ruler);
      if (idx !== -1) {
        gameState.allies.splice(idx, 1);
        logMessage(`⚡ [동맹 파기] ${targetProv.ruler}과의 동맹을 파기했습니다.`, 'text-red-400');
        renderMapPins();
      }
    }
    function executeJointOperation() { closeAllDropdowns(); alert('동맹군과 공동 작전을 모색 중입니다.'); }
    function executeDiplomaticExchange() { closeAllDropdowns(); alert('인접국과 물자를 교환했습니다.'); }

    // ==================== 2. 인사 / 5. 개발 / 7. 상인 / 8. 특별 ====================
    function executeSearchOfficer() {
      closeAllDropdowns();
      const names = ['제갈량', '방통', '황충', '위연', '강유', '마초', '법정'];
      const picked = names[Math.floor(Math.random() * names.length)];
      logMessage(`🔍 [인재 수색] 재야의 명장 [${picked}]의 은거지를 발견하였습니다!`, 'text-cyan-300 font-bold');
    }
    function executeHireOfficer() {
      closeAllDropdowns();
      const myProv = getMyCapital();
      myProv.officers++;
      logMessage(`📜 [등용 성공] 명망 높은 장수를 맞이했습니다! (장수 수: ${myProv.officers}명)`, 'text-emerald-300 font-bold');
      updateRightPanel(myProv.id);
    }
    function executeReward() {
      closeAllDropdowns();
      const myProv = getMyCapital();
      if (myProv.gold < 100) return;
      myProv.gold -= 100;
      logMessage(`🎁 [포상] 장수들에게 하사품을 내려 충성도를 100으로 높였습니다!`, 'text-yellow-300');
      updateRightPanel(myProv.id);
    }
    function executeRelief() {
      closeAllDropdowns();
      const myProv = getMyCapital();
      if (myProv.food < 1000) return;
      myProv.food -= 1000;
      myProv.loyalty = Math.min(100, myProv.loyalty + 15);
      logMessage(`🥣 [주민 구호] 백성들에게 곡식을 나누어주어 민충이 +15 상승했습니다!`, 'text-emerald-300 font-bold');
      updateRightPanel(myProv.id);
    }
    function executeLandDev() {
      closeAllDropdowns();
      const myProv = getMyCapital();
      if (myProv.gold < 200) return;
      myProv.gold -= 200;
      logMessage(`🚜 [개간] 농지를 개간하여 가을 추수량을 늘렸습니다!`, 'text-emerald-300');
      updateRightPanel(myProv.id);
    }
    function executeFloodControl() {
      closeAllDropdowns();
      const myProv = getMyCapital();
      if (myProv.gold < 200) return;
      myProv.gold -= 200;
      logMessage(`🌊 [치수] 제방을 정비하여 수해를 방비했습니다!`, 'text-cyan-300');
      updateRightPanel(myProv.id);
    }
    function executeCommerceDev() {
      closeAllDropdowns();
      const myProv = getMyCapital();
      if (myProv.gold < 200) return;
      myProv.gold -= 200;
      logMessage(`🏪 [상업 투자] 시장을 활성화하여 7월 세수 수입을 증대시켰습니다!`, 'text-yellow-300');
      updateRightPanel(myProv.id);
    }
    function executeTraining() {
      closeAllDropdowns();
      const myProv = getMyCapital();
      if (myProv.food < 500) return;
      myProv.food -= 500;
      logMessage(`⚔️ [훈련] 전군 훈련 실시로 사기와 훈련도를 대폭 향상시켰습니다!`, 'text-emerald-300');
      updateRightPanel(myProv.id);
    }
    function executeConscription() {
      closeAllDropdowns();
      const myProv = getMyCapital();
      myProv.soldiers += 2500;
      myProv.loyalty = Math.max(10, myProv.loyalty - 8);
      logMessage(`📢 [징병] 2,500명을 징집하였습니다. (민충 -8)`, 'text-slate-200');
      updateRightPanel(myProv.id);
    }
    function executeRecruit() {
      closeAllDropdowns();
      const myProv = getMyCapital();
      if (myProv.gold < 500) return;
      myProv.gold -= 500;
      myProv.soldiers += 3000;
      logMessage(`🎖️ [모병] 금 500전으로 정예 의용군 3,000명을 모집했습니다!`, 'text-yellow-300');
      updateRightPanel(myProv.id);
    }
    function executeShipBuilding() {
      closeAllDropdowns();
      const myProv = getMyCapital();
      if (myProv.gold < 300) return;
      myProv.gold -= 300;
      logMessage(`⛵ [선박건조] 도하용 누선 20척을 건조 완료했습니다!`, 'text-cyan-300');
      updateRightPanel(myProv.id);
    }

    let currentTradeType = '';
    function openTradeModal(type) {
      closeAllDropdowns();
      currentTradeType = type;
      const myProv = getMyCapital();
      document.getElementById('trade-gold-val').innerText = myProv.gold.toLocaleString();
      document.getElementById('trade-food-val').innerText = myProv.food.toLocaleString();
      const titles = { sellFood: '군량 매출 (쌀 팔기)', buyFood: '군량 매입 (쌀 사기)', buyWeapons: '무기 매입', buyHorses: '군마 매입' };
      document.getElementById('trade-modal-title').innerText = titles[type];
      openModal('trade-modal');
    }
    function confirmTrade() {
      const myProv = getMyCapital();
      const amt = parseInt(document.getElementById('trade-input').value) || 0;
      if (amt <= 0) return;
      if (currentTradeType === 'sellFood') {
        if (myProv.food < amt) { alert('군량이 부족합니다!'); return; }
        myProv.food -= amt;
        const earn = Math.floor((amt / 100) * gameState.rates.riceSell);
        myProv.gold += earn;
        logMessage(`🌾 [쌀 매각] 군량 ${amt.toLocaleString()}석 ➔ 금 ${earn.toLocaleString()}전 획득`, 'text-yellow-300 font-bold');
      } else if (currentTradeType === 'buyFood') {
        const cost = Math.floor((amt / 100) * gameState.rates.riceBuy);
        if (myProv.gold < cost) { alert('금이 부족합니다!'); return; }
        myProv.gold -= cost;
        myProv.food += amt;
        logMessage(`🌾 [쌀 매입] 금 ${cost.toLocaleString()}전 ➔ 군량 ${amt.toLocaleString()}석 구입`, 'text-emerald-300 font-bold');
      } else {
        alert('무기와 군마를 인수했습니다!');
      }
      closeModal('trade-modal');
      updateRightPanel(myProv.id);
    }

    function executeHeal() { closeAllDropdowns(); logMessage(`💊 [치료] 화타의 비방으로 부상병을 전원 치료했습니다!`, 'text-emerald-300 font-bold'); }
    function executeEmergencyTax() {
      closeAllDropdowns();
      const myProv = getMyCapital();
      myProv.gold += 1200;
      myProv.loyalty = Math.max(10, myProv.loyalty - 20);
      logMessage(`⚠️ [임시징수] 금 1,200전을 긴급 징수했습니다. (민충 -20)`, 'text-red-300');
      updateRightPanel(myProv.id);
    }
    function executeWander() { closeAllDropdowns(); alert('아직 유랑군으로 전환할 시기가 아닙니다.'); }
    function openTaxRateModal() { closeAllDropdowns(); alert('세율이 40%로 책정되어 있습니다.'); }
    function executeDelegate() { closeAllDropdowns(); alert('태수에게 위임 명령을 하달했습니다.'); }
    function executeAppoint() { closeAllDropdowns(); alert('군사와 태수를 정식 임명했습니다.'); }
    function executeDirectOrder() { closeAllDropdowns(); alert('장수들에게 특수 군령을 전파했습니다.'); }
    function executeFireOfficer() { closeAllDropdowns(); alert('장수를 해고 조치했습니다.'); }
    function executeConfiscate() { closeAllDropdowns(); alert('보물을 회수했습니다.'); }

    function openRulerSelectModal() { closeAllDropdowns(); openModal('ruler-select-modal'); }
    function selectRuler(rulerKey) {
      closeModal('ruler-select-modal');
      const map = { liubei: { name: '유비', id: 8 }, caocao: { name: '조조', id: 4 }, sunquan: { name: '손권', id: 7 }, yuanshao: { name: '원소', id: 2 }, mateng: { name: '마등', id: 11 }, liubiao: { name: '유표', id: 8 } };
      const info = map[rulerKey];
      if (!info) return;
      gameState.currentRuler = rulerKey;
      gameState.rulerName = info.name;
      gameState.myCapitalId = info.id;
      gameState.selectedProvId = info.id;
      renderMapPins();
      updateRightPanel(info.id);
      logMessage(`👑 플레이 군주가 [${info.name}]으로 변경되었습니다!`, 'text-yellow-300 font-extrabold');
    }

    // ==================== BGM & 사운드 ====================
    function toggleBGM() {
      closeAllDropdowns();
      if (gameState.bgmPlaying) stopBGM();
      else startBGM();
    }
    function startBGM() {
      try {
        if (!gameState.audioCtx) gameState.audioCtx = new (window.AudioContext || window.webkitAudioContext)();
        if (gameState.audioCtx.state === 'suspended') gameState.audioCtx.resume();
        gameState.bgmPlaying = true;
        document.getElementById('bgm-status').innerText = '재생 중';
        document.getElementById('bgm-icon').innerText = '🔊';
        document.getElementById('bgm-btn').className = 'px-2 py-1 text-xs font-bold rounded bg-emerald-700 text-yellow-100 border border-yellow-400 flex items-center gap-1 shadow';
        playRetroMelody();
      } catch (e) { console.error(e); }
    }
    function stopBGM() {
      gameState.bgmPlaying = false;
      if (gameState.bgmTimer) clearTimeout(gameState.bgmTimer);
      document.getElementById('bgm-status').innerText = '정지됨';
      document.getElementById('bgm-icon').innerText = '🎵';
      document.getElementById('bgm-btn').className = 'px-2 py-1 text-xs font-bold rounded bg-amber-700 text-yellow-100 border border-yellow-400 flex items-center gap-1 shadow';
    }
    function playRetroMelody() {
      if (!gameState.bgmPlaying || !gameState.audioCtx) return;
      const notes = [220, 261.6, 293.7, 329.6, 392.0, 440, 523.3, 587.3, 440, 392.0, 329.6, 293.7, 261.6, 220, 196.0, 220];
      let step = 0;
      function nextNote() {
        if (!gameState.bgmPlaying) return;
        playTone(notes[step % notes.length], 0.28, 'triangle', 0.12);
        step++;
        gameState.bgmTimer = setTimeout(nextNote, 320);
      }
      nextNote();
    }
    function playTone(freq, duration, type='sine', gain=0.1) {
      if (!gameState.audioCtx) return;
      const osc = gameState.audioCtx.createOscillator();
      const g = gameState.audioCtx.createGain();
      osc.type = type;
      osc.frequency.setValueAtTime(freq, gameState.audioCtx.currentTime);
      g.gain.setValueAtTime(gain, gameState.audioCtx.currentTime);
      g.gain.exponentialRampToValueAtTime(0.001, gameState.audioCtx.currentTime + duration);
      osc.connect(g);
      g.connect(gameState.audioCtx.destination);
      osc.start();
      osc.stop(gameState.audioCtx.currentTime + duration);
    }
    function playSfx(type) {
      if (!gameState.audioCtx) {
        try { gameState.audioCtx = new (window.AudioContext || window.webkitAudioContext)(); } catch(e){}
      }
      if (!gameState.audioCtx) return;
      if (type === 'rest') {
        playTone(330, 0.15, 'sine', 0.15);
        setTimeout(() => playTone(440, 0.25, 'sine', 0.15), 120);
      } else if (type === 'war') {
        playTone(110, 0.3, 'sawtooth', 0.25);
        setTimeout(() => playTone(90, 0.4, 'sawtooth', 0.25), 180);
      } else if (type === 'victory') {
        playTone(523.3, 0.2, 'triangle', 0.2);
        setTimeout(() => playTone(659.3, 0.2, 'triangle', 0.2), 150);
        setTimeout(() => playTone(784.0, 0.4, 'triangle', 0.25), 300);
      } else {
        playTone(440, 0.08, 'sine', 0.1);
      }
    }

    // 유틸
    function getMyCapital() { return PROVINCES.find(x => x.ruler === gameState.rulerName) || PROVINCES[7]; }
    function logMessage(msg, colorClass='text-slate-200') {
      const container = document.getElementById('game-logs');
      if (!container) return;
      const div = document.createElement('div');
      div.className = colorClass;
      div.innerHTML = msg;
      container.appendChild(div);
      container.scrollTop = container.scrollHeight;
    }
    function clearLogs() { document.getElementById('game-logs').innerHTML = ''; }
    function checkUnification() {
      const myCount = PROVINCES.filter(x => x.ruler === gameState.rulerName).length;
      if (myCount === 13) {
        alert('🎉 경축! 13주를 전면 평정하고 한나라 황제에 즉위하여 천하태평성대를 열었습니다!');
        logMessage('👑 [천하통일 달성] 13주 전 국토를 통일하여 황제의 자리에 올랐습니다!', 'text-yellow-300 font-extrabold');
      }
    }

    function toggleDropdown(id) {
      const el = document.getElementById(id);
      const isShowing = el.classList.contains('show');
      closeAllDropdowns();
      if (!isShowing) el.classList.add('show');
    }
    function closeAllDropdowns() {
      document.querySelectorAll('.dropdown-menu').forEach(m => m.classList.remove('show'));
    }
    window.onclick = function(e) {
      if (!e.target.closest('.relative')) closeAllDropdowns();
    };
    function openModal(id) { document.getElementById(id).classList.remove('hidden'); }
    function closeModal(id) { document.getElementById(id).classList.add('hidden'); }

    function bindKeyboardShortcuts() {
      window.addEventListener('keydown', (e) => {
        if (e.target.tagName === 'INPUT' || e.target.tagName === 'SELECT') return;
        if (e.key === '0') executeRest();
        if (e.key === '4') openInfoModal();
        if (e.key === 'm' || e.key === 'M') toggleBGM();
      });
    }

    function saveGame() {
      closeAllDropdowns();
      localStorage.setItem('samgukji3_save', JSON.stringify({ gameState, provinces: PROVINCES }));
      logMessage('💾 [저장 완료] 게임 상태가 브라우저에 저장되었습니다.', 'text-emerald-300');
    }
    function loadGame() {
      closeAllDropdowns();
      const raw = localStorage.getItem('samgukji3_save');
      if (!raw) { alert('저장된 게임 데이터가 없습니다.'); return; }
      try {
        const saved = JSON.parse(raw);
        gameState = saved.gameState;
        for (let i = 0; i < saved.provinces.length; i++) Object.assign(PROVINCES[i], saved.provinces[i]);
        renderMapPins();
        updateRightPanel(gameState.selectedProvId);
        logMessage('📂 [불러오기 완료] 세이브 데이터를 복원했습니다.', 'text-emerald-300');
      } catch (e) { alert('불러오기 실패: ' + e.message); }
    }
    function resetGame() {
      closeAllDropdowns();
      if (confirm('게임을 처음부터 다시 시작하시겠습니까?')) location.reload();
    }
  </script>
</body>
</html>'''

    print("Replacing placeholders in HTML template...")
    html_content = html_template.replace("__MAP_B64__", map_b64)
    html_content = html_content.replace("__BATTLEFIELD_B64__", battlefield_b64)
    html_content = html_content.replace("__PORTRAITS_JSON__", portraits_json)
    html_content = html_content.replace("__LIUBEI_B64__", liubei_b64)

    out_paths = [
        os.path.join(brain_dir, "samgukji_game.html"),
        r"C:\Users\LENOVO\Desktop\삼국지_황제의결단_웹게임.html",
        r"g:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\samgukji.html",
        r"g:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\교육학\samgukji.html"
    ]

    for p in out_paths:
        try:
            with open(p, "w", encoding="utf-8") as f:
                f.write(html_content)
            print(f"Generated: {p} ({len(html_content):,} bytes)")
        except Exception as e:
            print(f"Failed to write {p}: {e}")

if __name__ == "__main__":
    generate_master_game()
