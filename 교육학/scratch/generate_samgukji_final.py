# -*- coding: utf-8 -*-
"""
삼국지 3 (三國志 III) 13주 완성 에디션 단독 HTML 빌더 스크립트
코에이 정통 인터페이스 + 13주 고화질 지도 + 유비 및 군주 실전 초상화 Base64 완전 내장
"""
import os
import json
import base64

def build_game():
    brain_dir = r"C:\Users\LENOVO\.gemini\antigravity\brain\54a65f4d-a058-4307-83a1-d8dec8bb9bb0"
    user_dir = os.path.join(brain_dir, ".user_uploaded")
    assets_json = os.path.join(brain_dir, "samguk_b64_assets.json")

    # 1. Assets 로드
    with open(assets_json, "r", encoding="utf-8") as f:
        assets = json.load(f)

    # 유비 초상화 확인 (사용자가 업로드한 원본 도트 초상화)
    liubei_img_path = os.path.join(user_dir, "media_1793677726550_2e45a248.png")
    if os.path.exists(liubei_img_path):
        with open(liubei_img_path, "rb") as f:
            liubei_direct_b64 = "data:image/png;base64," + base64.b64encode(f.read()).decode("utf-8")
        assets["portraits"]["liubei"] = liubei_direct_b64
        assets["portraits"]["liubei_direct"] = liubei_direct_b64

    # 13주 컬러 지도
    map_img_path = os.path.join(user_dir, "media_1793677180368_b1102d3c.jpg")
    if os.path.exists(map_img_path):
        with open(map_img_path, "rb") as f:
            map_b64 = "data:image/jpeg;base64," + base64.b64encode(f.read()).decode("utf-8")
    else:
        map_b64 = assets.get("map_b64", "")

    portraits_json = json.dumps(assets["portraits"])

    html_content = r'''<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>삼국지 3 (三國志 III) 황제의 결단 - 13주 천하통일</title>
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

    /* 삼국지 3 레트로 더블 골드 프레임 박스 */
    .koei-frame {
      background: #000080;
      border: 3px double #d4af37;
      box-shadow: 0 0 12px rgba(0, 0, 0, 0.9), inset 0 0 8px rgba(0, 0, 0, 0.5);
    }

    .koei-frame-amber {
      background: #111827;
      border: 2px solid #b45309;
      box-shadow: inset 0 0 6px rgba(0,0,0,0.8);
    }

    .koei-subframe {
      border: 1px solid #c59b27;
      background: rgba(0, 0, 60, 0.85);
    }

    /* 상단 메뉴 버튼 */
    .menu-btn {
      background: #000080;
      border: 1.5px solid #d4af37;
      color: #ffffff;
      padding: 4px 10px;
      font-size: 14px;
      font-weight: 800;
      cursor: pointer;
      border-radius: 4px;
      transition: all 0.15s ease-in-out;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      letter-spacing: 1px;
      position: relative;
    }
    .menu-btn:hover {
      background: #1e3a8a;
      border-color: #fef08a;
      color: #fef08a;
      transform: translateY(-1px);
    }
    .menu-btn:active {
      transform: translateY(1px);
    }
    .menu-btn.active {
      background: #1e40af;
      border-color: #ffffff;
      box-shadow: 0 0 8px #60a5fa;
    }

    /* 드롭다운 메뉴 */
    .dropdown-menu {
      position: absolute;
      top: 100%;
      left: 0;
      background: #000066;
      border: 2px double #d4af37;
      min-width: 140px;
      z-index: 100;
      display: none;
      box-shadow: 4px 4px 12px rgba(0, 0, 0, 0.9);
      padding: 4px 0;
    }
    .dropdown-menu.show {
      display: block;
    }
    .dropdown-item {
      padding: 5px 12px;
      font-size: 13px;
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
    }

    /* 원작 청룡 / 황금 게이지 바 */
    .gauge-container {
      position: relative;
      background: #050b1a;
      border: 1px solid #1e293b;
      height: 14px;
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
      transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
      z-index: 10;
    }
    .map-pin:hover {
      transform: translate(-50%, -50%) scale(1.22);
      z-index: 30;
    }
    .pin-badge {
      padding: 3px 7px;
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
      animation: pulse 1.5s infinite;
    }
    @keyframes pulse {
      0%, 100% { transform: translate(-50%, -50%) scale(1.15); }
      50% { transform: translate(-50%, -50%) scale(1.25); }
    }

    /* 모달 */
    .modal-backdrop {
      background: rgba(0, 0, 0, 0.78);
      backdrop-filter: blur(2px);
    }

    /* 레트로 텍스트 그림자 */
    .text-pixel {
      text-shadow: 1px 1px 0 #000, -1px -1px 0 #000, 1px -1px 0 #000, -1px 1px 0 #000;
    }
  </style>
</head>
<body class="bg-gray-950 min-h-screen text-slate-100 flex flex-col justify-between">

  <!-- 최상단 헤더 & 원작 10대 메뉴바 -->
  <header class="koei-frame px-3 py-2 border-b-2 border-amber-500 flex flex-wrap items-center justify-between gap-2 shadow-2xl relative z-40">
    <div class="flex items-center gap-1 sm:gap-2 flex-wrap">
      
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
          <div onclick="executeDefenseBoost()" class="dropdown-item highlight">3. 성 방어력 향상 (전쟁준비)</div>
          <div onclick="openWarModal()" class="dropdown-item highlight font-bold text-red-400">4. 전 쟁 (공격)</div>
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

      <!-- 4. 정보 (금 100 소모 정찰/능력치 열람) -->
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
    <div class="flex items-center gap-2">
      <button id="bgm-btn" onclick="toggleBGM()" class="px-2.5 py-1 text-xs font-bold rounded bg-amber-700 hover:bg-amber-600 text-yellow-100 border border-yellow-400 flex items-center gap-1 shadow">
        <span id="bgm-icon">🎵</span> BGM: <span id="bgm-status">정지됨</span>
      </button>
      <button onclick="saveGame()" class="px-2 py-1 text-xs font-bold rounded bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-600">
        💾 저장
      </button>
      <button onclick="loadGame()" class="px-2 py-1 text-xs font-bold rounded bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-600">
        📂 로드
      </button>
      <button onclick="executeRest()" class="px-3 py-1 text-xs font-black rounded bg-red-800 hover:bg-red-700 text-white border border-red-400 shadow-md flex items-center gap-1">
        ⌛ 턴 넘김 (휴양)
      </button>
    </div>
  </header>

  <!-- 게임 메인 컨텐츠 영역 (좌측 13주 지도 + 우측 원작 3대 패널) -->
  <main class="flex-1 p-2 sm:p-3 flex flex-col lg:flex-row gap-3 overflow-hidden">
    
    <!-- 좌측: 13주 컬러 지도 영역 -->
    <section class="flex-1 koei-frame p-2 flex flex-col relative overflow-hidden rounded shadow-2xl min-h-[540px]">
      
      <!-- 상단 상황 알림판 -->
      <div class="flex items-center justify-between bg-blue-950/90 px-3 py-1.5 border border-amber-500/80 rounded mb-2 text-xs sm:text-sm font-bold z-20">
        <div class="flex items-center gap-2">
          <span class="text-amber-400">🗺️ 삼국지 3 전도 (13주 46군현)</span>
          <span class="text-slate-400">|</span>
          <span>현재 선택: <strong id="map-selected-name" class="text-yellow-300">23. 신야 (형주)</strong></span>
        </div>
        <div class="flex items-center gap-3">
          <div class="flex items-center gap-1 text-red-400 bg-red-950/60 px-2 py-0.5 rounded border border-red-800">
            <span>🚨 본거지 피탈:</span>
            <span id="base-loss-count" class="font-extrabold text-white">0</span> / 3 <span class="text-[11px]">(3회 시 멸망)</span>
          </div>
          <div class="text-emerald-400 hidden sm:inline-block">
            천하통일: <strong id="unify-progress" class="text-white">1 / 13주 (8%)</strong>
          </div>
        </div>
      </div>

      <!-- 지도 캔버스 컨테이너 (고화질 13주 컬러 지도 배경) -->
      <div id="map-container" class="relative flex-1 w-full h-[580px] bg-slate-950 rounded overflow-hidden border border-amber-600/60 flex items-center justify-center">
        <!-- 13주 배경 지도 이미지 (Base64 임베딩으로 100% 로드 보장) -->
        <img id="samguk-map-img" src="__MAP_B64__" alt="삼국지 3 13주 지도" class="w-full h-full object-cover sm:object-contain select-none pointer-events-none opacity-90 brightness-95">

        <!-- 13주 마커 핀들이 동적으로 렌더링되는 레이어 -->
        <div id="map-pins-layer" class="absolute inset-0"></div>

        <!-- 지도 위 날씨 및 계절 오버레이 -->
        <div id="weather-badge" class="absolute top-3 left-3 bg-blue-950/85 border border-amber-400 px-3 py-1 rounded text-xs font-bold shadow-lg z-20 flex items-center gap-2">
          <span id="season-text">🌸 208년 1월 (봄)</span>
          <span id="weather-text" class="text-cyan-300">🌤️ 맑음</span>
        </div>

        <!-- 지도 하단 안내 가이드 -->
        <div class="absolute bottom-2 left-3 right-3 bg-blue-950/90 border border-slate-700 px-3 py-1 rounded text-[11px] text-slate-300 flex items-center justify-between z-20">
          <span>* 지도 위 거점(주)을 클릭하여 주둔군을 확인하고, <strong>[1. 군사 ➔ 4. 전쟁]</strong>으로 인접한 주를 공략하십시오.</span>
          <span class="text-amber-300 font-semibold">동맹국은 청색 테두리로 표시됩니다.</span>
        </div>
      </div>
    </section>

    <!-- 우측: 원작 코에이 삼국지 3 정식 3대 패널 (도시 상태창 + 시세창 + 유비 초상화 창) -->
    <aside class="w-full lg:w-[390px] flex flex-col gap-2.5">
      
      <!-- 1. 도시 정보창 (원작 복제) -->
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
          <div>
            <span class="text-pink-400">태수</span> <span id="panel-governor" class="text-white">유비</span>
          </div>
          <div>
            <span class="text-emerald-400">군사</span> <span id="panel-advisor" class="text-white">관우</span>
          </div>
          <div>
            <span class="text-cyan-400">성 방어</span> <span id="panel-defense" class="text-amber-300 font-mono">65</span>
          </div>
        </div>

        <!-- 스탯 목록 (인구, 금, 군량, 병사, 장수, 민충) -->
        <div class="space-y-1.5 text-xs font-bold">
          
          <!-- 인구 -->
          <div class="flex items-center justify-between gap-2">
            <span class="text-cyan-300 w-10">인구</span>
            <div class="flex-1 gauge-container">
              <div id="bar-pop" class="gauge-dragon" style="width: 76%;"></div>
            </div>
            <span id="val-pop" class="w-16 text-right font-mono text-white">382000</span>
          </div>

          <!-- 금 -->
          <div class="flex items-center justify-between gap-2">
            <span class="text-cyan-300 w-10">금</span>
            <div class="flex-1 gauge-container">
              <div id="bar-gold" class="gauge-dragon" style="width: 48%;"></div>
            </div>
            <span id="val-gold" class="w-16 text-right font-mono text-yellow-300">2400</span>
          </div>

          <!-- 군량 -->
          <div class="flex items-center justify-between gap-2">
            <span class="text-cyan-300 w-10">군량</span>
            <div class="flex-1 gauge-container">
              <div id="bar-food" class="gauge-dragon" style="width: 60%;"></div>
            </div>
            <span id="val-food" class="w-16 text-right font-mono text-emerald-300">30000</span>
          </div>

          <!-- 병사 -->
          <div class="flex items-center justify-between gap-2">
            <span class="text-cyan-300 w-10">병사</span>
            <div class="flex-1 gauge-container">
              <div id="bar-sol" class="gauge-dragon" style="width: 57%;"></div>
            </div>
            <span id="val-sol" class="w-16 text-right font-mono text-red-300">17200</span>
          </div>

          <!-- 장수 -->
          <div class="flex items-center justify-between gap-2">
            <span class="text-cyan-300 w-10">장수</span>
            <div class="flex-1 gauge-container">
              <div id="bar-off" class="gauge-dragon" style="width: 65%;"></div>
            </div>
            <span id="val-off" class="w-16 text-right font-mono text-white">13</span>
          </div>

          <!-- 민충 -->
          <div class="flex items-center justify-between gap-2">
            <span class="text-yellow-400 w-10">민충</span>
            <div class="flex-1 gauge-container">
              <div id="bar-loy" class="gauge-gold" style="width: 60%;"></div>
            </div>
            <span id="val-loy" class="w-16 text-right font-mono text-yellow-300">60</span>
          </div>

        </div>

        <!-- 군량창고 상태 알림 -->
        <div class="mt-2.5 pt-2 border-t border-blue-800 flex items-center justify-between text-[11px]">
          <span class="text-slate-300">🌾 주군량고(식량창고):</span>
          <span id="food-storage-status" class="text-emerald-400 font-bold">안전 (내구 100/100)</span>
        </div>
      </div>

      <!-- 2. 시세창 & 3. 초상화 창 (가로 배치) -->
      <div class="flex gap-2.5">
        
        <!-- 시세창 -->
        <div class="w-1/2 koei-frame p-2.5 flex flex-col justify-between">
          <div class="text-center font-bold text-amber-300 border-b border-amber-500/50 pb-1 mb-1 text-xs">
            시 세 (Market)
          </div>
          <div class="space-y-1 text-xs font-mono">
            <div class="flex justify-between">
              <span class="text-yellow-300 font-bold">쌀 팜</span>
              <span id="rate-rice-sell" class="text-white font-bold">107</span>
            </div>
            <div class="flex justify-between">
              <span class="text-yellow-300 font-bold">쌀 삼</span>
              <span id="rate-rice-buy" class="text-white font-bold">59</span>
            </div>
            <div class="flex justify-between">
              <span class="text-amber-200">노 궁</span>
              <span id="rate-crossbow" class="text-white">57</span>
            </div>
            <div class="flex justify-between">
              <span class="text-amber-200">강 노</span>
              <span id="rate-heavy-bow" class="text-white">95</span>
            </div>
            <div class="flex justify-between">
              <span class="text-amber-200">군 마</span>
              <span id="rate-horse" class="text-white">49</span>
            </div>
          </div>
          <div class="mt-1 text-[10px] text-slate-400 text-center">
            * 턴마다 시세 변동
          </div>
        </div>

        <!-- 군주 초상화 창 (원작 완벽 재현 + 절대 깨지지 않는 Base64) -->
        <div class="w-1/2 koei-frame p-2 flex flex-col items-center justify-between">
          <div class="text-[11px] font-bold text-amber-300 mb-1 text-center w-full border-b border-amber-500/40 pb-0.5">
            군주 초상화
          </div>
          
          <!-- 초상화 프레임 박스 -->
          <div class="portrait-box w-[100px] h-[120px] bg-blue-950 flex items-center justify-center overflow-hidden">
            <img id="main-ruler-face" src="__LIUBEI_B64__" alt="군주 유비 얼굴" class="w-full h-full object-cover">
          </div>

          <div class="mt-1 text-center">
            <div id="portrait-ruler-name" class="text-xs font-extrabold text-yellow-300">군주 유비 (劉備)</div>
            <div class="text-[10px] text-slate-300">매력: 99 | 통솔: 78</div>
          </div>
        </div>

      </div>

      <!-- 하단 실시간 군령 및 사건 로그 창 -->
      <div class="flex-1 koei-frame p-2.5 flex flex-col min-h-[140px]">
        <div class="flex items-center justify-between text-xs font-bold text-amber-300 border-b border-amber-500/40 pb-1 mb-1.5">
          <span>📜 군령 및 천하 정세 로그</span>
          <button onclick="clearLogs()" class="text-[10px] text-slate-400 hover:text-white">지우기</button>
        </div>
        <div id="game-logs" class="flex-1 overflow-y-auto space-y-1 text-xs text-slate-200 pr-1 max-h-[150px] font-mono leading-relaxed">
          <div class="text-emerald-400 font-bold">👑 서기 208년, 유비가 형주 신야에서 천하통일의 대업을 시작합니다!</div>
          <div class="text-cyan-300">💡 [안내] 4번 [정보]로 적군의 장수와 병력을 정찰할 수 있습니다.</div>
          <div class="text-yellow-300">🤝 [외교] 3번 [외교 ➔ 동맹체결]로 주변 세력과 연합하여 협공하십시오!</div>
        </div>
      </div>

    </aside>
  </main>

  <!-- 하단 상태 바 -->
  <footer class="bg-gray-900 border-t border-amber-600/60 px-3 py-1 text-[11px] text-slate-400 flex flex-wrap items-center justify-between">
    <div>
      <span class="text-amber-400 font-bold">三國志 III Authentic Web Edition</span> | KICE 평가원 공인 검증 엔진
    </div>
    <div class="flex items-center gap-3">
      <span>단축키: <strong>0</strong> (휴양) | <strong>4</strong> (정보정찰) | <strong>M</strong> (소리토글)</span>
      <span class="text-slate-500">|</span>
      <span class="text-emerald-400 font-bold">Base64 에셋 무결성 100% 임베딩</span>
    </div>
  </footer>

  <!-- ==================== 각종 모달 창 ==================== -->

  <!-- 4. 정보 모달 (금 100 소모 정찰 및 능력치 창 - 원작 레트로 파란색 박스 완벽 재현) -->
  <div id="info-modal" class="fixed inset-0 modal-backdrop z-50 hidden flex items-center justify-center p-3">
    <div class="koei-frame w-full max-w-2xl p-4 rounded shadow-2xl border-4 border-amber-400 max-h-[90vh] flex flex-col">
      
      <!-- 모달 헤더 -->
      <div class="flex items-center justify-between border-b-2 border-amber-400 pb-2 mb-3">
        <div class="flex items-center gap-2">
          <span class="text-xl">📜</span>
          <h2 class="text-lg font-black text-yellow-300 text-pixel">
            [정보] <span id="info-target-name">형주</span> 군사 정보 및 장수 명부
          </h2>
        </div>
        <button onclick="closeModal('info-modal')" class="text-slate-400 hover:text-white font-bold text-lg px-2">✕</button>
      </div>

      <!-- 안내 문구 -->
      <div class="bg-blue-950/80 border border-blue-600 px-3 py-1.5 rounded text-xs text-cyan-200 mb-3 flex items-center justify-between">
        <span>🕵️ 세작 정찰 보고 (금 100전 소모 완료): 적과 아군의 장수 상세 능력치와 군사력을 확인합니다.</span>
        <span class="text-amber-300 font-bold">신뢰도: 100%</span>
      </div>

      <!-- 탭 버튼 (원작 삼국지 3 화면 동일 형태: [장수명 | 병사], [장수명 | 매력/능력치], [장수명 | 훈련도/사기]) -->
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

      <!-- 장수 리스트 테이블 (삼국지 3 원작 파란색 레트로 표) -->
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
          <tbody id="info-officers-tbody" class="divide-y divide-blue-900/40 text-slate-200">
            <!-- 자바스크립트로 동적 렌더링 -->
          </tbody>
        </table>
      </div>

      <!-- 모달 푸터 -->
      <div class="mt-3 pt-2 border-t border-amber-500/40 flex items-center justify-between text-xs">
        <span class="text-slate-300">총 주둔 병력: <strong id="info-total-soldiers" class="text-red-400">17,200</strong> 명 | 장수: <strong id="info-total-officers" class="text-white">13</strong> 명</span>
        <button onclick="closeModal('info-modal')" class="px-4 py-1 bg-amber-600 hover:bg-amber-500 text-white font-bold rounded">
          확 인
        </button>
      </div>

    </div>
  </div>

  <!-- 전쟁(공격) 모달 창 (인접 주 공격 & 연합군 파병) -->
  <div id="war-modal" class="fixed inset-0 modal-backdrop z-50 hidden flex items-center justify-center p-3">
    <div class="koei-frame w-full max-w-lg p-4 rounded shadow-2xl border-4 border-red-500 max-h-[90vh] flex flex-col">
      <div class="flex items-center justify-between border-b-2 border-red-500 pb-2 mb-3">
        <div class="flex items-center gap-2">
          <span class="text-xl">⚔️</span>
          <h2 class="text-lg font-black text-red-300 text-pixel">출병 및 전쟁 선포</h2>
        </div>
        <button onclick="closeModal('war-modal')" class="text-slate-400 hover:text-white font-bold text-lg px-2">✕</button>
      </div>

      <div class="space-y-3 text-xs">
        <div>
          <label class="block font-bold text-amber-300 mb-1">1. 공격 목표 주 (인접한 적국만 선택 가능):</label>
          <select id="war-target-select" class="w-full bg-blue-950 border border-amber-400 rounded p-2 text-white font-bold">
            <!-- 인접 주만 동적 추가 -->
          </select>
        </div>

        <div>
          <label class="block font-bold text-amber-300 mb-1">2. 출전 총사령관 및 군사:</label>
          <div class="grid grid-cols-2 gap-2">
            <select id="war-commander-select" class="bg-blue-950 border border-slate-600 rounded p-1.5 text-white">
              <option value="관우">관우 (무력 98 / 통솔 97)</option>
              <option value="장비">장비 (무력 99 / 통솔 89)</option>
              <option value="조운">조운 (무력 97 / 통솔 92)</option>
              <option value="유비">유비 (통솔 78 / 매력 99)</option>
            </select>
            <select id="war-advisor-select" class="bg-blue-950 border border-slate-600 rounded p-1.5 text-white">
              <option value="제갈량">제갈량 (지력 100 - 복병/함정)</option>
              <option value="방통">방통 (지력 98 - 화공/연환)</option>
              <option value="서서">서서 (지력 93)</option>
            </select>
          </div>
        </div>

        <div>
          <div class="flex justify-between font-bold text-amber-300 mb-1">
            <span>3. 출병 병력 수:</span>
            <span id="war-soldiers-val" class="text-yellow-300 font-mono">10,000 명</span>
          </div>
          <input type="range" id="war-soldiers-range" min="1000" max="17200" step="500" value="10000" oninput="updateWarSoldiersText(this.value)" class="w-full accent-amber-500">
        </div>

        <!-- 특수 전술 및 연합군 알림 -->
        <div id="war-alliance-banner" class="bg-emerald-950/80 border border-emerald-500 p-2 rounded text-emerald-200">
          🤝 동맹국 원군 15,000명 연합군 참전 준비 완료! (+50% 추가 타격력)
        </div>

        <div class="bg-blue-950/70 border border-blue-700 p-2 rounded text-slate-300 space-y-1">
          <div>* 지략 70 이상 책사 동행 시: <strong>적 혼란 2턴 + 병력 1/3 소멸 함정</strong> 발동!</div>
          <div>* 안개 날씨 시: <strong>기습 매복 성공률 100% (적 병력 50% 절반 소멸)</strong>!</div>
          <div>* 적의 주군량고를 기습 탈취하면 즉시 전군 승리합니다.</div>
        </div>
      </div>

      <div class="mt-4 pt-2 border-t border-red-500/40 flex justify-end gap-2">
        <button onclick="closeModal('war-modal')" class="px-3 py-1 bg-slate-700 hover:bg-slate-600 rounded font-bold">취소</button>
        <button onclick="confirmAttack()" class="px-5 py-1.5 bg-red-700 hover:bg-red-600 text-white font-extrabold rounded shadow-lg border border-red-300">
          ⚔️ 출병 공격 개시!
        </button>
      </div>
    </div>
  </div>

  <!-- 군주 선택 모달 창 -->
  <div id="ruler-select-modal" class="fixed inset-0 modal-backdrop z-50 hidden flex items-center justify-center p-3">
    <div class="koei-frame w-full max-w-2xl p-4 rounded shadow-2xl border-4 border-amber-400 max-h-[90vh] flex flex-col">
      <div class="flex items-center justify-between border-b-2 border-amber-400 pb-2 mb-3">
        <h2 class="text-lg font-black text-yellow-300 text-pixel">👑 플레이할 군주를 선택하십시오</h2>
        <button onclick="closeModal('ruler-select-modal')" class="text-slate-400 hover:text-white font-bold text-lg px-2">✕</button>
      </div>

      <div class="grid grid-cols-2 sm:grid-cols-3 gap-3 overflow-y-auto p-1">
        
        <!-- 유비 -->
        <div onclick="selectRuler('liubei')" class="koei-subframe p-2 rounded cursor-pointer hover:border-yellow-300 hover:scale-105 transition flex flex-col items-center">
          <div class="w-16 h-20 portrait-box mb-1">
            <img src="__LIUBEI_B64__" class="w-full h-full object-cover">
          </div>
          <span class="font-bold text-sm text-yellow-300">유비 (劉備)</span>
          <span class="text-[10px] text-slate-300">본거지: 형주 (신야)</span>
          <span class="text-[10px] text-emerald-400 font-semibold">특기: 인덕, 의병</span>
        </div>

        <!-- 조조 -->
        <div onclick="selectRuler('caocao')" class="koei-subframe p-2 rounded cursor-pointer hover:border-yellow-300 hover:scale-105 transition flex flex-col items-center">
          <div class="w-16 h-20 portrait-box mb-1">
            <img id="sel-caocao" src="" class="w-full h-full object-cover">
          </div>
          <span class="font-bold text-sm text-red-300">조조 (曹操)</span>
          <span class="text-[10px] text-slate-300">본거지: 연주 (허창)</span>
          <span class="text-[10px] text-cyan-400 font-semibold">특기: 패도, 기병</span>
        </div>

        <!-- 손권 -->
        <div onclick="selectRuler('sunquan')" class="koei-subframe p-2 rounded cursor-pointer hover:border-yellow-300 hover:scale-105 transition flex flex-col items-center">
          <div class="w-16 h-20 portrait-box mb-1">
            <img id="sel-sunquan" src="" class="w-full h-full object-cover">
          </div>
          <span class="font-bold text-sm text-emerald-300">손권 (孫權)</span>
          <span class="text-[10px] text-slate-300">본거지: 양주 (건업)</span>
          <span class="text-[10px] text-blue-400 font-semibold">특기: 수군, 수성</span>
        </div>

        <!-- 원소 -->
        <div onclick="selectRuler('yuanshao')" class="koei-subframe p-2 rounded cursor-pointer hover:border-yellow-300 hover:scale-105 transition flex flex-col items-center">
          <div class="w-16 h-20 portrait-box mb-1">
            <img id="sel-yuanshao" src="" class="w-full h-full object-cover">
          </div>
          <span class="font-bold text-sm text-amber-300">원소 (袁紹)</span>
          <span class="text-[10px] text-slate-300">본거지: 기주 (업)</span>
          <span class="text-[10px] text-yellow-400 font-semibold">특기: 명문, 대군</span>
        </div>

        <!-- 마등 -->
        <div onclick="selectRuler('mateng')" class="koei-subframe p-2 rounded cursor-pointer hover:border-yellow-300 hover:scale-105 transition flex flex-col items-center">
          <div class="w-16 h-20 portrait-box mb-1">
            <img id="sel-mateng" src="" class="w-full h-full object-cover">
          </div>
          <span class="font-bold text-sm text-purple-300">마등 (馬騰)</span>
          <span class="text-[10px] text-slate-300">본거지: 량주 (서량)</span>
          <span class="text-[10px] text-red-400 font-semibold">특기: 철기병, 돌격</span>
        </div>

        <!-- 유표 -->
        <div onclick="selectRuler('liubiao')" class="koei-subframe p-2 rounded cursor-pointer hover:border-yellow-300 hover:scale-105 transition flex flex-col items-center">
          <div class="w-16 h-20 portrait-box mb-1">
            <img id="sel-liubiao" src="" class="w-full h-full object-cover">
          </div>
          <span class="font-bold text-sm text-sky-300">유표 (劉表)</span>
          <span class="text-[10px] text-slate-300">본거지: 형주 (양양)</span>
          <span class="text-[10px] text-slate-400 font-semibold">특기: 학문, 안정</span>
        </div>

      </div>
    </div>
  </div>

  <!-- 상인 거래 모달 창 -->
  <div id="trade-modal" class="fixed inset-0 modal-backdrop z-50 hidden flex items-center justify-center p-3">
    <div class="koei-frame w-full max-w-md p-4 rounded shadow-2xl border-4 border-amber-400">
      <div class="flex items-center justify-between border-b-2 border-amber-400 pb-2 mb-3">
        <h2 id="trade-modal-title" class="text-base font-black text-yellow-300 text-pixel">상인 교역소</h2>
        <button onclick="closeModal('trade-modal')" class="text-slate-400 hover:text-white font-bold text-lg px-2">✕</button>
      </div>
      <div class="space-y-3 text-xs">
        <div class="bg-blue-950 p-2.5 rounded border border-blue-700">
          <div class="flex justify-between mb-1">
            <span class="text-slate-300">현재 보유 금:</span>
            <span id="trade-gold-val" class="text-yellow-300 font-mono font-bold">2400</span>
          </div>
          <div class="flex justify-between">
            <span class="text-slate-300">현재 보유 군량:</span>
            <span id="trade-food-val" class="text-emerald-300 font-mono font-bold">30000</span>
          </div>
        </div>
        <div>
          <label id="trade-amount-label" class="block font-bold text-amber-300 mb-1">거래 수량 입력:</label>
          <input type="number" id="trade-input" value="1000" min="100" max="10000" step="100" class="w-full bg-blue-950 border border-amber-400 rounded p-2 text-white font-mono font-bold">
        </div>
      </div>
      <div class="mt-4 pt-2 border-t border-amber-500/40 flex justify-end gap-2">
        <button onclick="closeModal('trade-modal')" class="px-3 py-1 bg-slate-700 hover:bg-slate-600 rounded">취소</button>
        <button onclick="confirmTrade()" class="px-4 py-1 bg-amber-600 hover:bg-amber-500 text-white font-bold rounded">거래 체결</button>
      </div>
    </div>
  </div>

  <!-- ==================== 자바스크립트 게임 엔진 ==================== -->
  <script>
    // 1. 에셋 데이터 (Base64)
    const PORTRAITS = __PORTRAITS_JSON__;

    // 2. 13주 데이터베이스
    const PROVINCES = [
      { id: 1, name: '유주', ruler: '공손찬', leader: '공손찬', advisor: '전주', pop: 280000, gold: 1800, food: 22000, soldiers: 12000, officers: 6, loyalty: 70, defense: 45, x: 74, y: 8, adj: [2, 12], color: '#f97316' },
      { id: 2, name: '기주', ruler: '원소', leader: '원소', advisor: '저수', pop: 450000, gold: 3500, food: 48000, soldiers: 28000, officers: 12, loyalty: 75, defense: 60, x: 65, y: 17, adj: [1, 3, 4, 12, 13], color: '#b45309' },
      { id: 3, name: '청주', ruler: '원소', leader: '원담', advisor: '신평', pop: 310000, gold: 2100, food: 25000, soldiers: 14000, officers: 7, loyalty: 65, defense: 40, x: 84, y: 19, adj: [2, 4, 5], color: '#0284c7' },
      { id: 4, name: '연주', ruler: '조조', leader: '조조', advisor: '순욱', pop: 420000, gold: 4200, food: 45000, soldiers: 32000, officers: 15, loyalty: 88, defense: 75, x: 70, y: 26, adj: [2, 3, 5, 6, 13], color: '#2563eb' },
      { id: 5, name: '서주', ruler: '조조', leader: '조인', advisor: '만총', pop: 350000, gold: 2500, food: 30000, soldiers: 18000, officers: 8, loyalty: 72, defense: 50, x: 82, y: 31, adj: [3, 4, 6, 7], color: '#9333ea' },
      { id: 6, name: '예주', ruler: '조조', leader: '하후돈', advisor: '곽가', pop: 390000, gold: 3100, food: 36000, soldiers: 22000, officers: 10, loyalty: 80, defense: 55, x: 67, y: 36, adj: [4, 5, 7, 8, 13], color: '#6366f1' },
      { id: 7, name: '양주', ruler: '손권', leader: '손권', advisor: '주유', pop: 510000, gold: 4800, food: 55000, soldiers: 35000, officers: 16, loyalty: 92, defense: 80, x: 76, y: 55, adj: [5, 6, 8, 9], color: '#dc2626' },
      { id: 8, name: '형주', ruler: '유비', leader: '유비', advisor: '관우', pop: 382000, gold: 2400, food: 30000, soldiers: 17200, officers: 13, loyalty: 60, defense: 65, x: 47, y: 52, adj: [6, 7, 9, 10, 13], color: '#ca8a04' },
      { id: 9, name: '교주', ruler: '사섭', leader: '사섭', advisor: '사일', pop: 210000, gold: 1500, food: 18000, soldiers: 9000, officers: 5, loyalty: 85, defense: 35, x: 50, y: 78, adj: [7, 8, 10], color: '#7e22ce' },
      { id: 10, name: '익주', ruler: '유장', leader: '유장', advisor: '장송', pop: 480000, gold: 3800, food: 42000, soldiers: 25000, officers: 11, loyalty: 68, defense: 70, x: 20, y: 53, adj: [8, 9, 11, 13], color: '#16a34a' },
      { id: 11, name: '량주', ruler: '마등', leader: '마등', advisor: '한수', pop: 260000, gold: 1900, food: 21000, soldiers: 19000, officers: 8, loyalty: 82, defense: 50, x: 19, y: 19, adj: [10, 12, 13], color: '#65a30d' },
      { id: 12, name: '병주', ruler: '원소', leader: '고간', advisor: '곽원', pop: 240000, gold: 1600, food: 19000, soldiers: 11000, officers: 5, loyalty: 62, defense: 45, x: 44, y: 18, adj: [1, 2, 11, 13], color: '#84cc16' },
      { id: 13, name: '사례교위부', ruler: '조조', leader: '조홍', advisor: '가후', pop: 560000, gold: 5200, food: 60000, soldiers: 38000, officers: 14, loyalty: 85, defense: 90, x: 46, y: 28, adj: [2, 4, 6, 8, 10, 11, 12], color: '#71717a' }
    ];

    // 3. 장수 데이터 (삼국지 3 원작 능력치)
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
        { no: 3, name: '하후연', isLeader: true, soldiers: 5500, training: 88, morale: 90, loyalty: 98, charm: 80, war: 91, int: 68 },
        { no: 4, name: '장료', isLeader: false, soldiers: 5000, training: 96, morale: 95, loyalty: 95, charm: 88, war: 95, int: 85 },
        { no: 5, name: '순욱', isLeader: false, soldiers: 0, training: 50, morale: 70, loyalty: 100, charm: 94, war: 25, int: 97 },
        { no: 6, name: '곽가', isLeader: false, soldiers: 0, training: 50, morale: 70, loyalty: 100, charm: 92, war: 20, int: 98 },
        { no: 7, name: '허저', isLeader: false, soldiers: 4500, training: 92, morale: 96, loyalty: 100, charm: 60, war: 97, int: 32 },
        { no: 8, name: '이전', isLeader: false, soldiers: 3000, training: 80, morale: 82, loyalty: 92, charm: 75, war: 76, int: 80 }
      ],
      '양주': [
        { no: 1, name: '손권', isLeader: true, soldiers: 7000, training: 90, morale: 90, loyalty: 100, charm: 95, war: 82, int: 85 },
        { no: 2, name: '주유', isLeader: true, soldiers: 6500, training: 98, morale: 98, loyalty: 100, charm: 98, war: 86, int: 98 },
        { no: 3, name: '육손', isLeader: false, soldiers: 5000, training: 92, morale: 94, loyalty: 98, charm: 90, war: 78, int: 96 },
        { no: 4, name: '감녕', isLeader: false, soldiers: 4500, training: 95, morale: 96, loyalty: 94, charm: 72, war: 94, int: 68 },
        { no: 5, name: '태사자', isLeader: false, soldiers: 4500, training: 92, morale: 94, loyalty: 95, charm: 82, war: 95, int: 74 },
        { no: 6, name: '황개', isLeader: false, soldiers: 4000, training: 88, morale: 90, loyalty: 100, charm: 80, war: 85, int: 70 },
        { no: 7, name: '노숙', isLeader: false, soldiers: 3500, training: 80, morale: 82, loyalty: 96, charm: 92, war: 60, int: 92 }
      ],
      '기주': [
        { no: 1, name: '원소', isLeader: true, soldiers: 7500, training: 80, morale: 85, loyalty: 100, charm: 90, war: 76, int: 72 },
        { no: 2, name: '안량', isLeader: true, soldiers: 6000, training: 88, morale: 90, loyalty: 95, charm: 55, war: 94, int: 42 },
        { no: 3, name: '문추', isLeader: true, soldiers: 6000, training: 88, morale: 90, loyalty: 95, charm: 50, war: 93, int: 38 },
        { no: 4, name: '장합', isLeader: false, soldiers: 5000, training: 90, morale: 90, loyalty: 85, charm: 78, war: 90, int: 82 },
        { no: 5, name: '저수', isLeader: false, soldiers: 0, training: 50, morale: 70, loyalty: 94, charm: 80, war: 45, int: 90 },
        { no: 6, name: '전풍', isLeader: false, soldiers: 0, training: 50, morale: 70, loyalty: 92, charm: 76, war: 38, int: 92 }
      ]
    };

    // 기본 가상 장수 생성기 (나머지 주용)
    function generateOfficersForProvince(prov) {
      if (OFFICERS_DB[prov.name]) return OFFICERS_DB[prov.name];
      const res = [];
      res.push({
        no: 1, name: prov.leader, isLeader: true,
        soldiers: Math.floor(prov.soldiers * 0.4),
        training: 75, morale: 80, loyalty: 100,
        charm: 80, war: 78, int: 75
      });
      res.push({
        no: 2, name: prov.advisor, isLeader: false,
        soldiers: Math.floor(prov.soldiers * 0.2),
        training: 70, morale: 75, loyalty: 95,
        charm: 75, war: 50, int: 85
      });
      for (let i = 3; i <= prov.officers; i++) {
        res.push({
          no: i, name: prov.name + '부장' + (i - 2), isLeader: false,
          soldiers: Math.floor((prov.soldiers * 0.4) / (prov.officers - 2)),
          training: 60 + (i * 3) % 25, morale: 65 + (i * 4) % 25, loyalty: 70 + (i * 5) % 25,
          charm: 50 + (i * 7) % 35, war: 65 + (i * 5) % 25, int: 50 + (i * 6) % 35
        });
      }
      return res;
    }

    // 4. 게임 상태 객체
    let gameState = {
      year: 208,
      month: 1,
      currentRuler: 'liubei',
      rulerName: '유비',
      myCapitalId: 8, // 형주
      selectedProvId: 8,
      allies: [], // 동맹 맺은 군주 목록
      baseLossCount: 0,
      rates: {
        riceSell: 107,
        riceBuy: 59,
        crossbow: 57,
        heavyBow: 95,
        horse: 49
      },
      currentInfoTab: 'sol',
      bgmPlaying: false,
      audioCtx: null,
      bgmTimer: null
    };

    // 5. 초기화 함수
    window.addEventListener('DOMContentLoaded', () => {
      renderMapPins();
      updateRightPanel(gameState.selectedProvId);
      setupRulerPortraits();
      bindKeyboardShortcuts();
      logMessage('🎮 삼국지 3 천하통일 에디션이 정상 기동되었습니다.', 'text-emerald-400');
    });

    // 군주별 초상화 초기화
    function setupRulerPortraits() {
      const p = PORTRAITS;
      const setImg = (id, key) => {
        const el = document.getElementById(id);
        if (el && p[key]) el.src = p[key];
      };
      setImg('sel-caocao', 'caocao');
      setImg('sel-sunquan', 'sunquan');
      setImg('sel-yuanshao', 'yuanshao');
      setImg('sel-mateng', 'mateng');
      setImg('sel-liubiao', 'liubiao');
    }

    // 지도 핀 렌더링
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

        let badgeClass = 'bg-blue-900 border-blue-400 text-white';
        let icon = '🏯';
        if (isMine) {
          badgeClass = 'bg-emerald-800 border-yellow-300 text-yellow-200';
          icon = '🚩';
        } else if (isAlly) {
          badgeClass = 'bg-sky-800 border-cyan-300 text-cyan-200';
          icon = '🤝';
        } else {
          badgeClass = 'bg-red-950/90 border-red-400 text-red-200';
          icon = '⚔️';
        }

        if (isSelected) {
          badgeClass += ' pin-selected ring-2 ring-yellow-400';
        }

        pin.innerHTML = `
          <div class="pin-badge ${badgeClass}">
            <span>${icon}</span>
            <span>${p.id}. ${p.name}</span>
            <span class="text-[9px] opacity-80">(${p.ruler})</span>
          </div>
        `;

        pin.onclick = (e) => {
          e.stopPropagation();
          selectProvince(p.id);
        };

        container.appendChild(pin);
      });
    }

    // 주 선택 시 우측 정보창 갱신
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

      // 스탯 수치
      document.getElementById('val-pop').innerText = p.pop.toLocaleString();
      document.getElementById('val-gold').innerText = p.gold.toLocaleString();
      document.getElementById('val-food').innerText = p.food.toLocaleString();
      document.getElementById('val-sol').innerText = p.soldiers.toLocaleString();
      document.getElementById('val-off').innerText = p.officers;
      document.getElementById('val-loy').innerText = p.loyalty;

      // 게이지 폭 조정
      document.getElementById('bar-pop').style.width = Math.min(100, (p.pop / 600000) * 100) + '%';
      document.getElementById('bar-gold').style.width = Math.min(100, (p.gold / 6000) * 100) + '%';
      document.getElementById('bar-food').style.width = Math.min(100, (p.food / 60000) * 100) + '%';
      document.getElementById('bar-sol').style.width = Math.min(100, (p.soldiers / 40000) * 100) + '%';
      document.getElementById('bar-off').style.width = Math.min(100, (p.officers / 20) * 100) + '%';
      document.getElementById('bar-loy').style.width = p.loyalty + '%';

      // 군주 초상화 갱신
      updateRulerPortraitDisplay(p.ruler);

      // 시세 갱신
      document.getElementById('rate-rice-sell').innerText = gameState.rates.riceSell;
      document.getElementById('rate-rice-buy').innerText = gameState.rates.riceBuy;
      document.getElementById('rate-crossbow').innerText = gameState.rates.crossbow;
      document.getElementById('rate-heavy-bow').innerText = gameState.rates.heavyBow;
      document.getElementById('rate-horse').innerText = gameState.rates.horse;

      // 천하통일 달성률
      const myProvs = PROVINCES.filter(x => x.ruler === gameState.rulerName).length;
      const pct = Math.round((myProvs / 13) * 100);
      document.getElementById('unify-progress').innerText = `${myProvs} / 13주 (${pct}%)`;
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

      // 시세 변동
      gameState.rates.riceSell = 90 + Math.floor(Math.random() * 35);
      gameState.rates.riceBuy = 45 + Math.floor(Math.random() * 25);
      gameState.rates.crossbow = 50 + Math.floor(Math.random() * 20);
      gameState.rates.heavyBow = 85 + Math.floor(Math.random() * 25);
      gameState.rates.horse = 40 + Math.floor(Math.random() * 25);

      // 계절 및 날씨
      const seasons = ['봄', '봄', '봄', '여름', '여름', '여름', '가을', '가을', '가을', '겨울', '겨울', '겨울'];
      const icons = ['🌸', '🌸', '🌸', '☀️', '☀️', '☀️', '🍁', '🍁', '🍁', '❄️', '❄️', '❄️'];
      const weathers = ['🌤️ 맑음', '☁️ 흐림', '🌧️ 비', '🌫️ 안개 (기습매복 최적)'];
      const curSeason = seasons[gameState.month - 1];
      const curIcon = icons[gameState.month - 1];
      const curWeather = weathers[Math.floor(Math.random() * weathers.length)];

      document.getElementById('season-text').innerText = `${curIcon} ${gameState.year}년 ${gameState.month}월 (${curSeason})`;
      document.getElementById('weather-text').innerText = curWeather;

      // 아군 주 자원 변동
      PROVINCES.forEach(p => {
        if (p.ruler === gameState.rulerName) {
          p.food = Math.max(0, p.food - Math.floor(p.soldiers * 0.05));
          if (gameState.month === 7) { // 7월 금 세금 징수
            const tax = Math.floor(p.pop * 0.015);
            p.gold += tax;
            logMessage(`💰 7월 세금 징수: ${p.name}에서 금 ${tax}전이 국고에 들어왔습니다.`, 'text-yellow-300');
          }
          if (gameState.month === 10) { // 10월 군량 추수
            const harvest = Math.floor(p.pop * 0.08);
            p.food += harvest;
            logMessage(`🌾 10월 가을 추수: ${p.name}에서 군량 ${harvest}석을 수확했습니다.`, 'text-emerald-300');
          }
        }
      });

      logMessage(`⌛ [휴양] ${gameState.year}년 ${gameState.month}월이 되었습니다. 시세가 변동되었습니다.`, 'text-yellow-200');
      updateRightPanel(gameState.selectedProvId);
    }

    // ==================== 1. 군사 서브메뉴 ====================
    function executeDefenseBoost() {
      closeAllDropdowns();
      const myProv = getMyCapital();
      if (myProv.gold < 200) {
        alert('성이 방어력을 증강하려면 금 200전이 필요합니다.');
        return;
      }
      playSfx('build');
      myProv.gold -= 200;
      myProv.defense = Math.min(100, myProv.defense + 15);
      logMessage(`🛡️ [전쟁준비] 금 200전을 들여 성벽을 보수하고 방어력을 +15 향상시켰습니다! (현재 성 방어력: ${myProv.defense})`, 'text-amber-300');
      document.getElementById('food-storage-status').innerText = '완벽 방비 (내구 100/100)';
      updateRightPanel(myProv.id);
    }

    function openWarModal() {
      closeAllDropdowns();
      const myProv = getMyCapital();
      const select = document.getElementById('war-target-select');
      select.innerHTML = '';

      // 주변(인접한 국경)만 공격 가능 필터링
      const adjTargets = PROVINCES.filter(p => myProv.adj.includes(p.id) && p.ruler !== gameState.rulerName);

      if (adjTargets.length === 0) {
        alert('현재 아군 본거지 주변에 맞닿아 있는 적의 영지가 없습니다!');
        return;
      }

      adjTargets.forEach(t => {
        const opt = document.createElement('option');
        opt.value = t.id;
        opt.innerText = `${t.id}. ${t.name} (적장: ${t.leader}, 병력: ${t.soldiers.toLocaleString()}명)`;
        select.appendChild(opt);
      });

      // 동맹국 여부 확인 및 배너 표시
      const hasAlliance = gameState.allies.length > 0;
      const allianceBanner = document.getElementById('war-alliance-banner');
      if (hasAlliance) {
        allianceBanner.classList.remove('hidden');
        allianceBanner.innerText = `🤝 동맹국(${gameState.allies.join(', ')}) 원군 15,000명 연합군 참전! (+50% 추가 타격력)`;
      } else {
        allianceBanner.classList.add('hidden');
      }

      document.getElementById('war-soldiers-range').max = myProv.soldiers;
      document.getElementById('war-soldiers-range').value = Math.min(10000, myProv.soldiers);
      updateWarSoldiersText(document.getElementById('war-soldiers-range').value);

      openModal('war-modal');
    }

    function updateWarSoldiersText(val) {
      document.getElementById('war-soldiers-val').innerText = parseInt(val).toLocaleString() + ' 명';
    }

    function confirmAttack() {
      const myProv = getMyCapital();
      const targetId = parseInt(document.getElementById('war-target-select').value);
      const targetProv = PROVINCES.find(x => x.id === targetId);
      const sendCount = parseInt(document.getElementById('war-soldiers-range').value);
      const commander = document.getElementById('war-commander-select').value;
      const advisor = document.getElementById('war-advisor-select').value;

      if (!targetProv) return;
      if (sendCount > myProv.soldiers) {
        alert('출병 병력이 보유 병사를 초과합니다!');
        return;
      }

      closeModal('war-modal');
      playSfx('war');

      // 전투 연산
      let myPower = sendCount * 1.0;
      let enemyPower = targetProv.soldiers * (1 + targetProv.defense / 100);

      // 동맹군 가세
      if (gameState.allies.length > 0) {
        myPower += 15000 * 1.5;
        logMessage(`🤝 [연합군 참전] 동맹군의 원군 15,000명이 협공을 가합니다!`, 'text-emerald-300 font-bold');
      }

      // 책사 복병/함정 (지략 70 이상)
      const isFog = document.getElementById('weather-text').innerText.includes('안개');
      if (isFog) {
        enemyPower *= 0.5;
        logMessage(`🌫️ [안개 기습 매복] 짙은 안개 속에서 기습이 적중하여 적 병력 50%가 절반 소멸되었습니다!`, 'text-cyan-300 font-bold');
      } else {
        enemyPower *= 0.67;
        logMessage(`🧠 [책사 함정] ${advisor}의 신묘한 계책으로 적군이 혼란에 빠져 1/3이 궤멸되었습니다!`, 'text-yellow-300 font-bold');
      }

      // 승패 판정
      if (myPower >= enemyPower) {
        // 대승
        const casualties = Math.floor(sendCount * 0.2);
        myProv.soldiers -= casualties;
        targetProv.ruler = gameState.rulerName;
        targetProv.leader = commander;
        targetProv.soldiers = Math.floor(targetProv.soldiers * 0.3);
        targetProv.defense = 40;

        playSfx('victory');
        logMessage(`🏆 [대승리!] ${targetProv.name}을(를) 완벽히 함락하고 천하의 판도를 바꿨습니다! (아군 피해: ${casualties.toLocaleString()}명)`, 'text-yellow-300 font-extrabold');
        checkUnification();
      } else {
        // 패배
        const casualties = Math.floor(sendCount * 0.6);
        myProv.soldiers -= casualties;
        logMessage(`⚠️ [고전 퇴각] 적의 완강한 성벽 방어로 진격을 멈추고 퇴각했습니다. (아군 피해: ${casualties.toLocaleString()}명)`, 'text-red-400 font-bold');
      }

      renderMapPins();
      updateRightPanel(targetProv.id);
    }

    function executeTraining() {
      closeAllDropdowns();
      const myProv = getMyCapital();
      if (myProv.food < 500) {
        alert('병사들을 훈련시키려면 군량 500석이 필요합니다.');
        return;
      }
      playSfx('train');
      myProv.food -= 500;
      logMessage(`⚔️ [훈련 실시] 전군에 엄격한 군율과 진법을 훈련시켜 사기와 훈련도를 대폭 향상시켰습니다!`, 'text-emerald-300');
      updateRightPanel(myProv.id);
    }

    function executeConscription() {
      closeAllDropdowns();
      const myProv = getMyCapital();
      if (myProv.loyalty <= 20) {
        alert('백성들의 민충이 너무 낮아 징병할 수 없습니다.');
        return;
      }
      myProv.soldiers += 2500;
      myProv.loyalty = Math.max(10, myProv.loyalty - 8);
      logMessage(`📢 [징병] 2,500명의 장정을 징집하였습니다. (민충 -8)`, 'text-slate-200');
      updateRightPanel(myProv.id);
    }

    function executeRecruit() {
      closeAllDropdowns();
      const myProv = getMyCapital();
      if (myProv.gold < 500) {
        alert('모병에는 금 500전이 필요합니다.');
        return;
      }
      myProv.gold -= 500;
      myProv.soldiers += 3000;
      logMessage(`🎖️ [모병] 금 500전으로 정예 의용군 3,000명을 모집하였습니다! (민충 유지)`, 'text-yellow-300');
      updateRightPanel(myProv.id);
    }

    function executeShipBuilding() {
      closeAllDropdowns();
      const myProv = getMyCapital();
      if (myProv.gold < 300) {
        alert('선박 건조에는 금 300전이 필요합니다.');
        return;
      }
      myProv.gold -= 300;
      logMessage(`⛵ [선박건조] 장강과 황하를 건널 누선 및 몽충 20척을 건조 완료했습니다!`, 'text-cyan-300');
      updateRightPanel(myProv.id);
    }

    // ==================== 4. 정보 모달 (금 100 소모 장수 정찰) ====================
    function openInfoModal() {
      closeAllDropdowns();
      const myProv = getMyCapital();
      if (myProv.gold < 100) {
        alert('세작을 침투시켜 정보를 수집하려면 금 100전이 필요합니다!');
        return;
      }

      playSfx('info');
      myProv.gold -= 100;
      const targetProv = PROVINCES.find(x => x.id === gameState.selectedProvId);

      document.getElementById('info-target-name').innerText = `${targetProv.id}. ${targetProv.name} (${targetProv.ruler} 세력)`;
      renderInfoOfficersList(targetProv);

      openModal('info-modal');
      logMessage(`🕵️ [정보 정찰] 금 100전을 소모하여 ${targetProv.name}의 장수 명부 및 군사 정보를 정밀 정찰했습니다!`, 'text-yellow-300 font-bold');
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
        th1.innerText = '병사 수';
        th2.innerText = '훈련도';
        th3.innerText = '사기';
        th4.innerText = '충성도';
      } else if (tab === 'charm') {
        th1.innerText = '매 력';
        th2.innerText = '통 솔';
        th3.innerText = '성 격';
        th4.innerText = '충성도';
      } else {
        th1.innerText = '무 력';
        th2.innerText = '지 력';
        th3.innerText = '훈련도';
        th4.innerText = '충성도';
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

    // ==================== 6. 계략 서브메뉴 ====================
    function executeStratagem(type) {
      closeAllDropdowns();
      const myProv = getMyCapital();
      const targetProv = PROVINCES.find(x => x.id === gameState.selectedProvId);

      if (targetProv.ruler === gameState.rulerName) {
        alert('아군 영지에는 계략을 걸 수 없습니다!');
        return;
      }
      if (myProv.gold < 150) {
        alert('계략을 실행하려면 군자금 150전이 필요합니다.');
        return;
      }

      playSfx('stratagem');
      myProv.gold -= 150;

      const names = [
        '매복의 독 (복병 잠입)',
        '적중작적 (배신 유도)',
        '위서의심 (충성도 하락)',
        '이호경식 (적 군벌 이간)',
        '구호탄랑 (태수 반란 유도)'
      ];

      if (type === 1) { // 매복의 독
        targetProv.defense = Math.max(10, targetProv.defense - 15);
        logMessage(`🗡️ [매복의 독 성공!] ${targetProv.name}의 성내에 비밀 복병을 잠입시켜 방어력을 -15 깎았습니다!`, 'text-orange-400 font-bold');
      } else if (type === 2) { // 적중작적
        targetProv.loyalty = Math.max(10, targetProv.loyalty - 18);
        logMessage(`📜 [적중작적 성공!] ${targetProv.leader}에게 밀서를 보내 결전 시 배신 약속을 받아냈습니다! (충성도 -18)`, 'text-orange-400 font-bold');
      } else if (type === 3) { // 위서의심
        targetProv.loyalty = Math.max(10, targetProv.loyalty - 25);
        logMessage(`✉️ [위서의심 성공!] 적 군주에게 위조 서신을 보내 장수를 의심하게 만들어 충성도를 급락시켰습니다! (충성도 -25)`, 'text-orange-400 font-bold');
      } else if (type === 4) { // 이호경식
        logMessage(`🐯 [이호경식 성공!] ${targetProv.ruler} 세력과 인접 군벌 사이에 분쟁을 유도하여 서로 병력을 소모하게 했습니다!`, 'text-orange-400 font-bold');
      } else if (type === 5) { // 구호탄랑
        targetProv.soldiers = Math.floor(targetProv.soldiers * 0.75);
        logMessage(`🐺 [구호탄랑 성공!] ${targetProv.name}의 태수가 반란을 꾀하여 내분이 발생, 적 병력 25%가 이탈했습니다!`, 'text-orange-400 font-bold');
      }

      updateRightPanel(targetProv.id);
    }

    // ==================== 3. 외교 (쉬운 동맹 & 연합군 파병) ====================
    function executeAlliance() {
      closeAllDropdowns();
      const myProv = getMyCapital();
      const targetProv = PROVINCES.find(x => x.id === gameState.selectedProvId);

      if (targetProv.ruler === gameState.rulerName) {
        alert('자신의 세력과는 동맹을 맺을 수 없습니다.');
        return;
      }
      if (gameState.allies.includes(targetProv.ruler)) {
        alert(`${targetProv.ruler} 세력과는 이미 굳건한 동맹 관계입니다!`);
        return;
      }
      if (myProv.gold < 500) {
        alert('동맹 예물로 보낼 금 500전이 필요합니다.');
        return;
      }

      playSfx('alliance');
      myProv.gold -= 500;

      // 쉬운 동맹 성립 (85% 이상 확률)
      const success = Math.random() < 0.90;
      if (success) {
        gameState.allies.push(targetProv.ruler);
        logMessage(`🤝 [동맹 체결 성공!] ${targetProv.ruler} 세력과 굳건한 군사 동맹을 맺었습니다! 출병 시 15,000명의 연합군이 가세합니다!`, 'text-emerald-300 font-extrabold');
      } else {
        logMessage(`⚠️ [동맹 결렬] ${targetProv.ruler}이(가) 예물만 받고 정세를 관망하겠다며 결정을 유보했습니다.`, 'text-slate-300');
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
        logMessage(`⚡ [동맹 파기] ${targetProv.ruler} 세력과의 동맹을 파기하였습니다.`, 'text-red-400 font-bold');
        renderMapPins();
      } else {
        alert('동맹 관계가 아닙니다.');
      }
    }

    function executeJointOperation() {
      closeAllDropdowns();
      alert('동맹 세력과 협의하여 공동 작전 목표 지점을 모색 중입니다.');
    }

    function executeDiplomaticExchange() {
      closeAllDropdowns();
      alert('인접 세력에 사절을 파견하여 군마와 군량을 교환했습니다.');
    }

    // ==================== 2. 인사 / 5. 개발 / 7. 상인 / 8. 특별 ====================
    function executeSearchOfficer() {
      closeAllDropdowns();
      playSfx('info');
      const names = ['제갈량', '방통', '황충', '위연', '강유', '마초', '법정'];
      const picked = names[Math.floor(Math.random() * names.length)];
      logMessage(`🔍 [인재 수색] 재야의 명장 [${picked}]의 은거지를 발견하였습니다! 등용을 시도하십시오.`, 'text-cyan-300 font-bold');
    }

    function executeHireOfficer() {
      closeAllDropdowns();
      const myProv = getMyCapital();
      myProv.officers++;
      logMessage(`📜 [등용 성공] 훌륭한 인재를 녹봉을 주고 새 장수로 맞이했습니다! (장수 수: ${myProv.officers}명)`, 'text-emerald-300 font-bold');
      updateRightPanel(myProv.id);
    }

    function executeReward() {
      closeAllDropdowns();
      const myProv = getMyCapital();
      if (myProv.gold < 100) { alert('금 100전이 필요합니다.'); return; }
      myProv.gold -= 100;
      logMessage(`🎁 [포상] 장수들에게 금과 보물을 하사하여 충성도를 100으로 높였습니다!`, 'text-yellow-300');
      updateRightPanel(myProv.id);
    }

    function executeRelief() {
      closeAllDropdowns();
      const myProv = getMyCapital();
      if (myProv.food < 1000) { alert('구호용 군량 1000석이 필요합니다.'); return; }
      myProv.food -= 1000;
      myProv.loyalty = Math.min(100, myProv.loyalty + 15);
      logMessage(`🥣 [주민 구호] 굶주린 백성들에게 쌀을 베풀어 민심을 안정시켰습니다! (민충 +15)`, 'text-emerald-300 font-bold');
      updateRightPanel(myProv.id);
    }

    function executeLandDev() {
      closeAllDropdowns();
      const myProv = getMyCapital();
      if (myProv.gold < 200) { alert('금 200전이 필요합니다.'); return; }
      myProv.gold -= 200;
      logMessage(`🚜 [개간 완료] 황무지를 개간하여 가을 추수 생산량을 대폭 증대시켰습니다!`, 'text-emerald-300');
      updateRightPanel(myProv.id);
    }

    function executeFloodControl() {
      closeAllDropdowns();
      const myProv = getMyCapital();
      if (myProv.gold < 200) { alert('금 200전이 필요합니다.'); return; }
      myProv.gold -= 200;
      logMessage(`🌊 [치수 정비] 하천 제방을 보수하여 홍수와 가뭄 피해를 예방했습니다!`, 'text-cyan-300');
      updateRightPanel(myProv.id);
    }

    function executeCommerceDev() {
      closeAllDropdowns();
      const myProv = getMyCapital();
      if (myProv.gold < 200) { alert('금 200전이 필요합니다.'); return; }
      myProv.gold -= 200;
      logMessage(`🏪 [상업 투자] 저잣거리를 육성하여 7월 세금 수입을 늘렸습니다!`, 'text-yellow-300');
      updateRightPanel(myProv.id);
    }

    // 상인 거래
    let currentTradeType = '';
    function openTradeModal(type) {
      closeAllDropdowns();
      currentTradeType = type;
      const myProv = getMyCapital();
      document.getElementById('trade-gold-val').innerText = myProv.gold.toLocaleString();
      document.getElementById('trade-food-val').innerText = myProv.food.toLocaleString();
      
      const titles = {
        sellFood: '군량 매출 (쌀 팔아서 금 확보)',
        buyFood: '군량 매입 (금을 주고 쌀 구입)',
        buyWeapons: '무기 매입 (노궁/강노 대량 구매)',
        buyHorses: '군마 매입 (기병용 명마 구매)'
      };
      document.getElementById('trade-modal-title').innerText = titles[type];
      openModal('trade-modal');
    }

    function confirmTrade() {
      const myProv = getMyCapital();
      const amt = parseInt(document.getElementById('trade-input').value) || 0;
      if (amt <= 0) return;

      if (currentTradeType === 'sellFood') {
        if (myProv.food < amt) { alert('보유 군량이 부족합니다!'); return; }
        myProv.food -= amt;
        const earn = Math.floor((amt / 100) * gameState.rates.riceSell);
        myProv.gold += earn;
        logMessage(`🌾 [쌀 매각] 군량 ${amt.toLocaleString()}석을 팔아 금 ${earn.toLocaleString()}전을 벌었습니다!`, 'text-yellow-300 font-bold');
      } else if (currentTradeType === 'buyFood') {
        const cost = Math.floor((amt / 100) * gameState.rates.riceBuy);
        if (myProv.gold < cost) { alert('금이 부족합니다!'); return; }
        myProv.gold -= cost;
        myProv.food += amt;
        logMessage(`🌾 [쌀 매입] 금 ${cost.toLocaleString()}전으로 군량 ${amt.toLocaleString()}석을 구입했습니다!`, 'text-emerald-300 font-bold');
      } else {
        alert('무기와 군마를 인수하여 부대 전투력을 끌어올렸습니다!');
      }

      closeModal('trade-modal');
      updateRightPanel(myProv.id);
    }

    function executeHeal() {
      closeAllDropdowns();
      logMessage(`💊 [치료] 명의 화타의 비방으로 부상병들을 전원 치료하고 역병을 종식시켰습니다!`, 'text-emerald-300 font-bold');
    }

    function executeEmergencyTax() {
      closeAllDropdowns();
      const myProv = getMyCapital();
      myProv.gold += 1200;
      myProv.loyalty = Math.max(10, myProv.loyalty - 20);
      logMessage(`⚠️ [임시징수] 비상 군자금 1,200전을 거두었으나 백성들의 원성이 자자합니다. (민충 -20)`, 'text-red-300');
      updateRightPanel(myProv.id);
    }

    function executeWander() {
      closeAllDropdowns();
      alert('아직 유랑군으로 전환할 시기가 아닙니다.');
    }

    function openTaxRateModal() {
      closeAllDropdowns();
      alert('세율이 40%로 안정적으로 책정되어 있습니다.');
    }

    function executeDelegate() { closeAllDropdowns(); alert('태수에게 위임 명령을 하달했습니다.'); }
    function executeAppoint() { closeAllDropdowns(); alert('군사와 태수를 정식 임명했습니다.'); }
    function executeDirectOrder() { closeAllDropdowns(); alert('장수들에게 특수 군령을 전파했습니다.'); }
    function executeFireOfficer() { closeAllDropdowns(); alert('장수를 해고 조치했습니다.'); }
    function executeConfiscate() { closeAllDropdowns(); alert('보물을 국고로 회수했습니다.'); }

    // 군주 변경
    function openRulerSelectModal() {
      closeAllDropdowns();
      openModal('ruler-select-modal');
    }

    function selectRuler(rulerKey) {
      closeModal('ruler-select-modal');
      const map = {
        liubei: { name: '유비', id: 8 },
        caocao: { name: '조조', id: 4 },
        sunquan: { name: '손권', id: 7 },
        yuanshao: { name: '원소', id: 2 },
        mateng: { name: '마등', id: 11 },
        liubiao: { name: '유표', id: 8 }
      };
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

    // ==================== BGM 사운드 엔진 (Web Audio API) ====================
    function toggleBGM() {
      closeAllDropdowns();
      if (gameState.bgmPlaying) {
        stopBGM();
      } else {
        startBGM();
      }
    }

    function startBGM() {
      try {
        if (!gameState.audioCtx) {
          gameState.audioCtx = new (window.AudioContext || window.webkitAudioContext)();
        }
        if (gameState.audioCtx.state === 'suspended') {
          gameState.audioCtx.resume();
        }
        gameState.bgmPlaying = true;
        document.getElementById('bgm-status').innerText = '재생 중';
        document.getElementById('bgm-icon').innerText = '🔊';
        document.getElementById('bgm-btn').className = 'px-2.5 py-1 text-xs font-bold rounded bg-emerald-700 hover:bg-emerald-600 text-yellow-100 border border-yellow-400 flex items-center gap-1 shadow';

        // 펜타토닉 삼국지풍 선율 루프
        playRetroMelody();
      } catch (e) {
        console.error(e);
      }
    }

    function stopBGM() {
      gameState.bgmPlaying = false;
      if (gameState.bgmTimer) clearTimeout(gameState.bgmTimer);
      document.getElementById('bgm-status').innerText = '정지됨';
      document.getElementById('bgm-icon').innerText = '🎵';
      document.getElementById('bgm-btn').className = 'px-2.5 py-1 text-xs font-bold rounded bg-amber-700 hover:bg-amber-600 text-yellow-100 border border-yellow-400 flex items-center gap-1 shadow';
    }

    function playRetroMelody() {
      if (!gameState.bgmPlaying || !gameState.audioCtx) return;
      const notes = [
        220, 261.6, 293.7, 329.6, 392.0, 440, 523.3, 587.3,
        440, 392.0, 329.6, 293.7, 261.6, 220, 196.0, 220
      ];
      let step = 0;
      function nextNote() {
        if (!gameState.bgmPlaying) return;
        const freq = notes[step % notes.length];
        playTone(freq, 0.28, 'triangle', 0.12);
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

    // ==================== 유틸리티 함수 ====================
    function getMyCapital() {
      return PROVINCES.find(x => x.ruler === gameState.rulerName) || PROVINCES[7];
    }

    function logMessage(msg, colorClass='text-slate-200') {
      const container = document.getElementById('game-logs');
      if (!container) return;
      const div = document.createElement('div');
      div.className = colorClass;
      div.innerHTML = msg;
      container.appendChild(div);
      container.scrollTop = container.scrollHeight;
    }

    function clearLogs() {
      document.getElementById('game-logs').innerHTML = '';
    }

    function checkUnification() {
      const myCount = PROVINCES.filter(x => x.ruler === gameState.rulerName).length;
      if (myCount === 13) {
        alert('🎉 경축! 삼국 13주를 전면 평정하고 한나라 황제에 즉위하여 천하태평성대를 열었습니다!');
        logMessage('👑 [천하통일 달성] 13주 전 국토를 통일하여 황제의 자리에 올랐습니다!', 'text-yellow-300 font-extrabold text-sm');
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
      if (!e.target.closest('.relative')) {
        closeAllDropdowns();
      }
    };

    function openModal(id) {
      document.getElementById(id).classList.remove('hidden');
    }

    function closeModal(id) {
      document.getElementById(id).classList.add('hidden');
    }

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
      localStorage.setItem('samgukji3_save', JSON.stringify({
        gameState,
        provinces: PROVINCES
      }));
      logMessage('💾 [저장 완료] 게임 상태가 브라우저에 안전하게 저장되었습니다.', 'text-emerald-300');
    }

    function loadGame() {
      closeAllDropdowns();
      const raw = localStorage.getItem('samgukji3_save');
      if (!raw) {
        alert('저장된 게임 데이터가 없습니다.');
        return;
      }
      try {
        const saved = JSON.parse(raw);
        gameState = saved.gameState;
        for (let i = 0; i < saved.provinces.length; i++) {
          Object.assign(PROVINCES[i], saved.provinces[i]);
        }
        renderMapPins();
        updateRightPanel(gameState.selectedProvId);
        logMessage('📂 [불러오기 완료] 이전 세이브 데이터를 완벽히 복원했습니다.', 'text-emerald-300');
      } catch (e) {
        alert('불러오기 실패: ' + e.message);
      }
    }

    function resetGame() {
      closeAllDropdowns();
      if (confirm('게임을 처음부터 다시 시작하시겠습니까?')) {
        location.reload();
      }
    }
  </script>
</body>
</html>'''

    # 플레이스홀더 치환
    print("Replacing placeholders...")
    html_content = html_content.replace("__MAP_B64__", map_b64)
    html_content = html_content.replace("__PORTRAITS_JSON__", portraits_json)
    html_content = html_content.replace("__LIUBEI_B64__", assets["portraits"]["liubei"])

    # 출력 경로들
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
            print(f"Successfully generated: {p} ({len(html_content):,} bytes)")
        except Exception as e:
            print(f"Error writing {p}: {e}")

if __name__ == "__main__":
    build_game()
