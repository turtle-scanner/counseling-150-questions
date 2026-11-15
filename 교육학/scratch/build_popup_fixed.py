# -*- coding: utf-8 -*-
import os
import json

def build_popup_fixed_game():
    brain_dir = r"C:\Users\LENOVO\.gemini\antigravity\brain\54a65f4d-a058-4307-83a1-d8dec8bb9bb0"
    assets_json = os.path.join(brain_dir, "samguk_b64_assets.json")

    with open(assets_json, "r", encoding="utf-8") as f:
        assets = json.load(f)

    map_b64 = assets["map_b64"]
    liubei_b64 = assets["portraits"]["liubei"]
    portraits_json = json.dumps(assets["portraits"])

    html_code = r'''<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>삼국지 3 (三國志 III) 황제의 결단 - 정통 팝업 에디션</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Serif+KR:wght@600;900&family=Nanum+Gothic+Coding:wght@700&display=swap');

    * { box-sizing: border-box; user-select: none; }
    body {
      font-family: 'Nanum Gothic Coding', 'Noto Serif KR', monospace;
      background-color: #030712;
      color: #f1f5f9;
      margin: 0;
      padding: 0;
      overflow-x: hidden;
    }

    /* 코에이 정통 더블 골드 프레임 */
    .koei-box {
      background: #000080;
      border: 3px double #d4af37;
      box-shadow: 0 0 14px rgba(0, 0, 0, 0.9), inset 0 0 8px rgba(0, 0, 0, 0.5);
    }

    /* 상단 메뉴바: 절대 overflow hidden/auto 걸지 않아 팝업이 자유롭게 튀어나오게 함 */
    #main-header {
      background: #000080;
      border-bottom: 2px solid #d4af37;
      overflow: visible !important;
      position: relative;
      z-index: 50;
    }
    .menu-bar-row {
      overflow: visible !important;
      position: relative;
    }

    /* 상단 메뉴 버튼 */
    .menu-btn {
      background: #000080;
      border: 1.5px solid #d4af37;
      color: #ffffff;
      padding: 5px 11px;
      font-size: 13px;
      font-weight: 800;
      cursor: pointer;
      border-radius: 3px;
      transition: all 0.15s;
      white-space: nowrap;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      position: relative;
    }
    .menu-btn:hover {
      background: #1e3a8a;
      border-color: #fef08a;
      color: #fef08a;
    }
    .menu-btn:active { transform: translateY(1px); }

    /* ==================== 원작 100% 동일 세로 팝업 윈도우 ==================== */
    .koei-popup-window {
      position: absolute;
      top: 100%;
      left: 0;
      background: #000066 !important;
      border: 2px solid #ffffff !important;
      box-shadow: 4px 6px 18px rgba(0, 0, 0, 0.95);
      min-width: 140px;
      width: max-content;
      z-index: 99999 !important;
      display: none;
      flex-direction: column;
      padding: 4px 0;
      margin-top: 2px;
    }
    .koei-popup-window.show {
      display: flex !important;
    }
    .koei-popup-item {
      padding: 4px 14px;
      font-size: 12.5px;
      color: #ffffff;
      cursor: pointer;
      white-space: nowrap;
      font-weight: bold;
      transition: background 0.12s;
      letter-spacing: 0.5px;
    }
    .koei-popup-item:hover {
      background: #1e3a8a;
      color: #fde047;
    }
    .koei-popup-item.orange {
      color: #fb923c !important;
    }

    /* 청룡 / 황금 게이지 */
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
      transition: width 0.3s;
    }
    .gauge-gold {
      height: 100%;
      background: linear-gradient(90deg, #d97706 0%, #facc15 50%, #fef08a 100%);
      box-shadow: 0 0 6px #facc15;
      transition: width 0.3s;
    }

    /* 초상화 액자 */
    .portrait-box {
      border: 3px double #d4af37;
      background: #000033;
      padding: 2px;
      box-shadow: 0 0 10px rgba(0, 0, 0, 0.8);
      image-rendering: pixelated;
    }

    /* 지도 마커 핀 */
    .map-pin {
      position: absolute;
      transform: translate(-50%, -50%);
      cursor: pointer;
      transition: all 0.2s cubic-bezier(0.34, 1.56, 0.64, 1);
      z-index: 20;
    }
    .map-pin:hover {
      transform: translate(-50%, -50%) scale(1.2);
      z-index: 35;
    }
    .pin-badge {
      padding: 3px 6px;
      border-radius: 4px;
      font-size: 11px;
      font-weight: 800;
      white-space: nowrap;
      border: 1.5px solid #fff;
      box-shadow: 0 2px 8px rgba(0,0,0,0.9);
      display: flex;
      align-items: center;
      gap: 3px;
    }
    .pin-selected {
      outline: 3px solid #facc15;
      box-shadow: 0 0 14px #facc15;
      animation: pinPulse 1.4s infinite;
    }
    @keyframes pinPulse {
      0%, 100% { transform: translate(-50%, -50%) scale(1.1); }
      50% { transform: translate(-50%, -50%) scale(1.22); }
    }

    .modal-backdrop {
      background: rgba(0, 0, 0, 0.82);
      backdrop-filter: blur(2px);
    }
    .text-pixel {
      text-shadow: 1px 1px 0 #000, -1px -1px 0 #000, 1px -1px 0 #000, -1px 1px 0 #000;
    }
  </style>
</head>
<body class="bg-gray-950 min-h-screen text-slate-100 flex flex-col justify-between">

  <!-- ==================== 1. 상단 메뉴바 (원작 팝업 윈도우 완벽 연동) ==================== -->
  <header id="main-header" class="px-3 py-1.5 flex items-center justify-between gap-2 shadow-2xl">
    
    <!-- 10대 메뉴 (가로 1줄 고정, 각 버튼 바로 아래에 하얀 테두리 팝업식 창이 뜸) -->
    <div class="menu-bar-row flex items-center gap-1.5 py-0.5">
      
      <!-- 0. 휴양 -->
      <div class="relative">
        <button onclick="executeRest()" class="menu-btn !bg-blue-900 border-yellow-400 text-yellow-300 font-black hover:!bg-blue-700 shadow">
          0. 휴양
        </button>
      </div>

      <!-- 1. 군사 (클릭 시 원작 팝업창 노출) -->
      <div class="relative">
        <button onclick="togglePopup('popup-military')" class="menu-btn">
          1. 군사
        </button>
        <div id="popup-military" class="koei-popup-window">
          <div onclick="openMoveModal()" class="koei-popup-item">1. 이 동</div>
          <div onclick="openTransportModal()" class="koei-popup-item orange">2. 수 송</div>
          <div onclick="repairFoodStorage()" class="koei-popup-item orange">3. 전쟁준비 (창고보수)</div>
          <div onclick="openWarModal()" class="koei-popup-item">4. 전 쟁</div>
          <div onclick="executeConscription()" class="koei-popup-item">5. 징 병</div>
          <div onclick="executeRecruit()" class="koei-popup-item">6. 모 병</div>
          <div onclick="executeTraining()" class="koei-popup-item">7. 훈 련</div>
          <div onclick="openReorganizeModal()" class="koei-popup-item">8. 재편성</div>
          <div onclick="executeShipBuilding()" class="koei-popup-item orange">9. 선박건조</div>
        </div>
      </div>

      <!-- 2. 인사 (클릭 시 원작 팝업창 노출) -->
      <div class="relative">
        <button onclick="togglePopup('popup-personnel')" class="menu-btn">
          2. 인사
        </button>
        <div id="popup-personnel" class="koei-popup-window">
          <div onclick="executeSearchOfficer()" class="koei-popup-item">1. 장수수색</div>
          <div onclick="executeHireOfficer()" class="koei-popup-item orange">2. 장수등용</div>
          <div onclick="executeReward()" class="koei-popup-item">3. 포 상</div>
          <div onclick="executeRelief()" class="koei-popup-item">4. 주민선정</div>
          <div onclick="executeDelegate()" class="koei-popup-item orange">5. 위 임</div>
          <div onclick="executeAppoint()" class="koei-popup-item">6. 임 명</div>
          <div onclick="executeDirectOrder()" class="koei-popup-item">7. 명 령</div>
          <div onclick="executeFireOfficer()" class="koei-popup-item">8. 해 고</div>
          <div onclick="executeConfiscate()" class="koei-popup-item">9. 몰 수</div>
        </div>
      </div>

      <!-- 3. 외교 (클릭 시 원작 팝업창 노출) -->
      <div class="relative">
        <button onclick="togglePopup('popup-diplomacy')" class="menu-btn">
          3. 외교
        </button>
        <div id="popup-diplomacy" class="koei-popup-window">
          <div onclick="executeAlliance()" class="koei-popup-item orange">1. 동맹체결 (쉬움)</div>
          <div onclick="executeJointOperation()" class="koei-popup-item">2. 공동작전</div>
          <div onclick="executeBreakAlliance()" class="koei-popup-item orange">3. 파 기</div>
          <div onclick="executeDiplomaticExchange()" class="koei-popup-item">4. 교 환</div>
        </div>
      </div>

      <!-- 4. 정보 (금 100 정찰) -->
      <div class="relative">
        <button onclick="openInfoModal()" class="menu-btn !border-yellow-300 !text-yellow-200 ring-2 ring-yellow-400/50 shadow">
          4. 정보 (금 100)
        </button>
      </div>

      <!-- 5. 개발 -->
      <div class="relative">
        <button onclick="togglePopup('popup-develop')" class="menu-btn">
          5. 개발
        </button>
        <div id="popup-develop" class="koei-popup-window">
          <div onclick="executeLandDev()" class="koei-popup-item">1. 개 간</div>
          <div onclick="executeFloodControl()" class="koei-popup-item orange">2. 치 수</div>
          <div onclick="executeCommerceDev()" class="koei-popup-item">3. 상업투자</div>
        </div>
      </div>

      <!-- 6. 계략 (클릭 시 원작 팝업창 노출 - 사용자가 올린 이미지 100% 동일) -->
      <div class="relative">
        <button onclick="togglePopup('popup-stratagem')" class="menu-btn !border-orange-400 !text-orange-200">
          6. 계략
        </button>
        <div id="popup-stratagem" class="koei-popup-window">
          <div onclick="executeStratagem(1)" class="koei-popup-item">1. 매복의 독</div>
          <div onclick="executeStratagem(2)" class="koei-popup-item orange">2. 적중작적</div>
          <div onclick="executeStratagem(3)" class="koei-popup-item orange">3. 위서의심</div>
          <div onclick="executeStratagem(4)" class="koei-popup-item">4. 이호경식</div>
          <div onclick="executeStratagem(5)" class="koei-popup-item orange">5. 구호탄랑</div>
        </div>
      </div>

      <!-- 7. 상인 (클릭 시 원작 팝업창 노출 - 사용자가 올린 이미지 100% 동일) -->
      <div class="relative">
        <button onclick="togglePopup('popup-merchant')" class="menu-btn">
          7. 상인
        </button>
        <div id="popup-merchant" class="koei-popup-window">
          <div onclick="openTradeModal('sellFood')" class="koei-popup-item">1. 군량매출</div>
          <div onclick="openTradeModal('buyFood')" class="koei-popup-item">2. 군량매입</div>
          <div onclick="openTradeModal('buyWeapons')" class="koei-popup-item">3. 무기매입</div>
          <div onclick="openTradeModal('buyHorses')" class="koei-popup-item">4. 군마매입</div>
        </div>
      </div>

      <!-- 8. 특별 (클릭 시 원작 팝업창 노출 - 사용자가 올린 이미지 100% 동일) -->
      <div class="relative">
        <button onclick="togglePopup('popup-special')" class="menu-btn">
          8. 특별
        </button>
        <div id="popup-special" class="koei-popup-window">
          <div onclick="executeWander()" class="koei-popup-item">1. 방 랑</div>
          <div onclick="executeHeal()" class="koei-popup-item orange">2. 치 료</div>
          <div onclick="executeEmergencyTax()" class="koei-popup-item">3. 임시징수</div>
          <div onclick="openTaxRateModal()" class="koei-popup-item">4. 세율변경</div>
        </div>
      </div>

      <!-- 9. 기능 -->
      <div class="relative">
        <button onclick="togglePopup('popup-config')" class="menu-btn">
          9. 기능
        </button>
        <div id="popup-config" class="koei-popup-window">
          <div onclick="toggleBGM()" class="koei-popup-item">1. 소 리 (BGM)</div>
          <div onclick="saveGame()" class="koei-popup-item">2. 저 장</div>
          <div onclick="loadGame()" class="koei-popup-item">3. 로 드</div>
          <div onclick="openRulerSelectModal()" class="koei-popup-item orange">4. 군주변경</div>
          <div onclick="resetGame()" class="koei-popup-item">5. 처음부터</div>
        </div>
      </div>

    </div>

    <!-- 우측 보조 컨트롤 바 -->
    <div class="flex items-center gap-1.5 flex-nowrap">
      <button id="bgm-btn" onclick="toggleBGM()" class="px-2.5 py-1 text-xs font-bold rounded bg-amber-700 hover:bg-amber-600 text-yellow-100 border border-yellow-400 flex items-center gap-1 shadow">
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

  <!-- ==================== 2. 메인 컨텐츠 영역 ==================== -->
  <main class="flex-1 p-2 sm:p-3 flex flex-col lg:flex-row gap-3 overflow-hidden items-start justify-center">
    
    <!-- 좌측: 13주 고화질 지도 영역 (정사각형 1:1 완벽 일치 박스) -->
    <section class="flex-1 koei-box p-2 flex flex-col w-full max-w-[720px] rounded shadow-2xl">
      
      <!-- 지도 헤더 안내판 -->
      <div class="flex items-center justify-between bg-blue-950/90 px-3 py-1.5 border border-amber-500/80 rounded mb-2 text-xs sm:text-sm font-bold">
        <div class="flex items-center gap-2">
          <span class="text-amber-400">🗺️ 삼국지 3 전도</span>
          <span class="text-slate-400">|</span>
          <span>선택: <strong id="map-selected-name" class="text-yellow-300">8. 형주 (유비)</strong></span>
        </div>
        <div class="flex items-center gap-2">
          <div class="flex items-center gap-1 text-emerald-400 bg-blue-950 px-2 py-0.5 rounded border border-emerald-500 text-xs">
            <span>🏰 보유 본거지:</span>
            <span id="my-provinces-count" class="font-black text-yellow-300">1</span>개
            <span class="text-[10px] text-slate-300 font-normal">(전 영지 피탈 시에만 멸망)</span>
          </div>
          <div class="text-cyan-300 text-xs hidden sm:inline-block">
            천하통일: <strong id="unify-progress" class="text-white">1 / 13주 (8%)</strong>
          </div>
        </div>
      </div>

      <!-- 지도 캔버스 박스 (지도의 가로세로 비율과 핀 레이어가 1:1로 정확히 겹침) -->
      <div class="relative w-full aspect-square max-h-[620px] bg-slate-950 rounded overflow-hidden border-2 border-amber-500/80 mx-auto flex items-center justify-center">
        <!-- 13주 고화질 지도 이미지 (Base64 완전 내장) -->
        <img id="samguk-map-img" src="__MAP_B64__" alt="13주 지도" class="w-full h-full object-cover pointer-events-none select-none">

        <!-- 13주 거점 핀 레이어 (각 주의 실제 한글 글자 바로 위에 100% 안착) -->
        <div id="map-pins-layer" class="absolute inset-0 pointer-events-auto"></div>

        <!-- 날씨/계절 오버레이 -->
        <div id="weather-badge" class="absolute top-2 left-2 bg-blue-950/85 border border-amber-400 px-2.5 py-1 rounded text-xs font-bold shadow-lg z-20 flex items-center gap-1.5">
          <span id="season-text">🌸 208년 1월 (봄)</span>
          <span id="weather-text" class="text-cyan-300">🌤️ 맑음</span>
        </div>

        <div class="absolute bottom-1.5 left-2 right-2 bg-blue-950/90 border border-slate-700 px-2.5 py-0.5 rounded text-[11px] text-slate-300 flex items-center justify-between z-20">
          <span>* 거점을 클릭하여 확인 후 <strong>[1. 군사 ➔ 4. 전 쟁]</strong>으로 인접한 주를 공략하십시오.</span>
          <span class="text-amber-300 font-semibold">동맹국: 청색 표시 & 연합군 15,000 파병</span>
        </div>
      </div>
    </section>

    <!-- 우측: 원작 삼국지 3 3대 패널 (도시 상태창 + 시세창 + 유비 초상화 창) -->
    <aside class="w-full lg:w-[380px] flex flex-col gap-2">
      
      <!-- 1. 도시 정보창 (식량저장창고 원클릭 100% 완전 복구 버튼 포함) -->
      <div class="koei-box p-3 relative shadow-xl">
        <div class="flex items-center justify-between border-b border-amber-500/60 pb-1.5 mb-2">
          <div class="flex items-center gap-2">
            <span class="w-3.5 h-3.5 bg-emerald-500 border border-white inline-block"></span>
            <span id="panel-city-title" class="font-bold text-base text-white text-pixel tracking-wide">8. 형주 (신야)</span>
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

        <!-- 식량창고 상태 & 원클릭 즉시 100% 완전 복구 버튼 -->
        <div class="mt-2.5 pt-2 border-t border-blue-800 flex items-center justify-between text-xs">
          <div class="flex items-center gap-1">
            <span class="text-slate-300">🌾 주군량고:</span>
            <span id="food-storage-status" class="text-emerald-400 font-black">내구 100% (완전 복구됨)</span>
          </div>
          <button onclick="repairFoodStorage()" class="px-2 py-0.5 rounded bg-amber-700 hover:bg-amber-600 text-yellow-100 font-bold text-[11px] border border-yellow-400 shadow flex items-center gap-1">
            <span>🛠️</span> 창고 보수 (금 200)
          </button>
        </div>
      </div>

      <!-- 2. 시세창 & 3. 군주 초상화 창 -->
      <div class="flex gap-2">
        <div class="w-1/2 koei-box p-2.5 flex flex-col justify-between">
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

        <!-- 군주 초상화 액자 (유비 원본 도트 초상화 100% 선명 노출) -->
        <div class="w-1/2 koei-box p-2 flex flex-col items-center justify-between">
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
      <div class="flex-1 koei-box p-2.5 flex flex-col min-h-[130px]">
        <div class="flex items-center justify-between text-xs font-bold text-amber-300 border-b border-amber-500/40 pb-1 mb-1.5">
          <span>📜 천하 정세 로그</span>
          <button onclick="clearLogs()" class="text-[10px] text-slate-400 hover:text-white">지우기</button>
        </div>
        <div id="game-logs" class="flex-1 overflow-y-auto space-y-1 text-xs text-slate-200 pr-1 max-h-[140px] font-mono leading-relaxed">
          <div class="text-emerald-400 font-bold">👑 유비가 형주 신야에서 천하통일의 대업을 시작합니다!</div>
          <div class="text-cyan-300">💡 [안내] 4번 [정보]로 적군의 장수와 병력을 정찰할 수 있습니다.</div>
          <div class="text-yellow-300">⚔️ [군사] 1번 [군사 ➔ 4. 전 쟁]으로 인접한 주를 공략하십시오!</div>
          <div class="text-emerald-300">🌾 [군량고] 창고 내구도는 [창고 보수] 버튼으로 언제든 100% 완전 복구됩니다.</div>
        </div>
      </div>

    </aside>
  </main>

  <!-- ==================== 실전 야전 배틀 모달 ==================== -->
  <div id="battle-modal" class="fixed inset-0 modal-backdrop z-50 hidden flex items-center justify-center p-3">
    <div class="koei-box w-full max-w-xl p-4 rounded shadow-2xl border-4 border-red-500 max-h-[90vh] flex flex-col">
      <div class="flex items-center justify-between border-b-2 border-red-500 pb-2 mb-3">
        <div class="flex items-center gap-2">
          <span class="text-xl">⚔️</span>
          <h2 id="battle-title" class="text-base font-black text-red-300 text-pixel">
            [야전 결전] 형주 vs 양양 (유비군 vs 유표군)
          </h2>
        </div>
        <div class="flex items-center gap-2 text-xs">
          <span id="battle-weather-badge" class="bg-blue-950 px-2 py-0.5 rounded border border-blue-600 text-cyan-300">☀️ 쾌청 (일반 야전)</span>
          <span id="battle-turn-count" class="bg-red-950 px-2 py-0.5 rounded border border-red-700 text-yellow-300 font-bold">턴: 1 / 10</span>
        </div>
      </div>

      <div class="space-y-3 text-xs">
        <div class="bg-blue-950/80 border-2 border-emerald-500/80 rounded p-2.5 space-y-1.5">
          <div class="flex items-center justify-between">
            <span class="font-extrabold text-emerald-300 text-sm">🚩 아군 (유비·제갈량)</span>
            <span id="battle-alliance-tag" class="text-yellow-300 font-bold bg-amber-950/80 px-2 py-0.5 rounded border border-amber-600">🤝 동맹연합군 참전 중 (+50% 타격)</span>
          </div>

          <div>
            <div class="flex justify-between mb-0.5 text-slate-300">
              <span>아군 전력: <strong id="battle-my-power-pct" class="text-emerald-400">100%</strong></span>
              <span>병력: <strong id="battle-my-soldiers-txt" class="text-white">17,200</strong>명</span>
            </div>
            <div class="gauge-container">
              <div id="battle-my-bar" class="gauge-dragon" style="width: 100%;"></div>
            </div>
          </div>

          <div class="bg-blue-900/40 p-2 rounded border border-blue-700 mt-2">
            <div class="flex items-center justify-between mb-1">
              <div class="flex items-center gap-1.5">
                <span class="text-amber-300 font-bold">🌾 식량저장창고:</span>
                <span id="battle-storage-pct" class="text-emerald-400 font-extrabold font-mono">100%</span>
                <span class="text-[10px] text-red-400">(0% 시 즉시 패배!)</span>
              </div>
              <button onclick="repairStorageInBattle()" class="px-2 py-0.5 bg-amber-600 hover:bg-amber-500 text-white font-extrabold rounded text-[11px] border border-yellow-300 shadow">
                🛠️ 창고 복구 (금 200 ➔ 100%)
              </button>
            </div>
            <div class="gauge-container">
              <div id="battle-storage-bar" class="gauge-gold" style="width: 100%;"></div>
            </div>
          </div>

          <div class="flex items-center justify-between pt-1">
            <span class="text-slate-300">작전 지휘관:</span>
            <span class="text-cyan-300 font-bold">제갈량 (지략 100) - 🔮 복병 함정 발동 가능</span>
          </div>
        </div>

        <div class="bg-blue-950/80 border-2 border-red-500/80 rounded p-2.5 space-y-1.5">
          <div class="flex items-center justify-between">
            <span id="battle-enemy-name" class="font-extrabold text-red-400 text-sm">⚔️ 적군 (유표 수비군)</span>
            <span id="battle-enemy-def-tag" class="text-slate-400 text-[11px]">성벽 방어력: 50</span>
          </div>
          <div>
            <div class="flex justify-between mb-0.5 text-slate-300">
              <span>적군 전력: <strong id="battle-enemy-power-pct" class="text-red-400">100%</strong></span>
              <span>병력: <strong id="battle-enemy-soldiers-txt" class="text-white">15,000</strong>명</span>
            </div>
            <div class="gauge-container">
              <div id="battle-enemy-bar" class="bg-red-600 h-full transition-all duration-300" style="width: 100%;"></div>
            </div>
          </div>
        </div>

        <div class="bg-blue-950 border border-blue-800 p-2 rounded max-h-[90px] overflow-y-auto text-xs font-mono text-slate-200 space-y-0.5" id="battle-modal-logs">
          <div class="text-yellow-300">🚩 결전이 시작되었습니다! 명령을 선택하십시오.</div>
        </div>

        <div class="grid grid-cols-4 gap-2 pt-1">
          <button onclick="battleActionAttack()" class="py-2 rounded bg-red-700 hover:bg-red-600 text-white font-extrabold text-xs shadow border border-red-400">
            ⚔️ 총공격
          </button>
          <button onclick="battleActionTrap()" class="py-2 rounded bg-blue-800 hover:bg-blue-700 text-cyan-200 font-bold text-xs shadow border border-blue-400">
            🧠 책사 함정
          </button>
          <button onclick="battleActionRaidStorage()" class="py-2 rounded bg-amber-700 hover:bg-amber-600 text-yellow-200 font-black text-xs shadow border border-yellow-400">
            🌾 창고 기습!
          </button>
          <button onclick="retreatFromBattleModal()" class="py-2 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-bold text-xs shadow border border-slate-600">
            🏳️ 퇴 각
          </button>
        </div>
      </div>
    </div>
  </div>

  <!-- ==================== 4. 정보 모달 (금 100) ==================== -->
  <div id="info-modal" class="fixed inset-0 modal-backdrop z-50 hidden flex items-center justify-center p-3">
    <div class="koei-box w-full max-w-2xl p-4 rounded shadow-2xl border-4 border-amber-400 max-h-[90vh] flex flex-col">
      <div class="flex items-center justify-between border-b-2 border-amber-400 pb-2 mb-3">
        <h2 class="text-base font-black text-yellow-300 text-pixel">
          📜 [정보] <span id="info-target-name">형주</span> 군사 정보 및 장수 명부
        </h2>
        <button onclick="closeModal('info-modal')" class="text-slate-400 hover:text-white font-bold text-lg px-2">✕</button>
      </div>

      <div class="bg-blue-950/80 border border-blue-600 px-3 py-1.5 rounded text-xs text-cyan-200 mb-3 flex items-center justify-between">
        <span>🕵️ 세작 정찰 보고 (금 100전 소모 완료): 적과 아군의 장수 상세 능력치와 군사력을 확인합니다.</span>
        <span class="text-amber-300 font-bold">신뢰도: 100%</span>
      </div>

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
        <button onclick="closeModal('info-modal')" class="px-4 py-1 bg-amber-600 hover:bg-amber-500 text-white font-bold rounded">확 인</button>
      </div>
    </div>
  </div>

  <!-- 군주 선택 모달 -->
  <div id="ruler-select-modal" class="fixed inset-0 modal-backdrop z-50 hidden flex items-center justify-center p-3">
    <div class="koei-box w-full max-w-2xl p-4 rounded shadow-2xl border-4 border-amber-400 max-h-[90vh] flex flex-col">
      <div class="flex items-center justify-between border-b-2 border-amber-400 pb-2 mb-3">
        <h2 class="text-base font-black text-yellow-300 text-pixel">👑 플레이할 군주를 선택하십시오</h2>
        <button onclick="closeModal('ruler-select-modal')" class="text-slate-400 hover:text-white font-bold text-lg px-2">✕</button>
      </div>
      <div class="grid grid-cols-2 sm:grid-cols-3 gap-2.5 overflow-y-auto p-1">
        <div onclick="selectRuler('liubei')" class="koei-box p-2 rounded cursor-pointer hover:border-yellow-300 hover:scale-105 transition flex flex-col items-center">
          <div class="w-16 h-20 portrait-box mb-1"><img src="__LIUBEI_B64__" class="w-full h-full object-cover"></div>
          <span class="font-bold text-xs text-yellow-300">유비 (劉備)</span>
          <span class="text-[10px] text-slate-300">형주 (신야)</span>
        </div>
        <div onclick="selectRuler('caocao')" class="koei-box p-2 rounded cursor-pointer hover:border-yellow-300 hover:scale-105 transition flex flex-col items-center">
          <div class="w-16 h-20 portrait-box mb-1"><img id="sel-caocao" src="" class="w-full h-full object-cover"></div>
          <span class="font-bold text-xs text-red-300">조조 (曹操)</span>
          <span class="text-[10px] text-slate-300">연주 (허창)</span>
        </div>
        <div onclick="selectRuler('sunquan')" class="koei-box p-2 rounded cursor-pointer hover:border-yellow-300 hover:scale-105 transition flex flex-col items-center">
          <div class="w-16 h-20 portrait-box mb-1"><img id="sel-sunquan" src="" class="w-full h-full object-cover"></div>
          <span class="font-bold text-xs text-emerald-300">손권 (孫權)</span>
          <span class="text-[10px] text-slate-300">양주 (건업)</span>
        </div>
        <div onclick="selectRuler('yuanshao')" class="koei-box p-2 rounded cursor-pointer hover:border-yellow-300 hover:scale-105 transition flex flex-col items-center">
          <div class="w-16 h-20 portrait-box mb-1"><img id="sel-yuanshao" src="" class="w-full h-full object-cover"></div>
          <span class="font-bold text-xs text-amber-300">원소 (袁紹)</span>
          <span class="text-[10px] text-slate-300">기주 (업)</span>
        </div>
        <div onclick="selectRuler('mateng')" class="koei-box p-2 rounded cursor-pointer hover:border-yellow-300 hover:scale-105 transition flex flex-col items-center">
          <div class="w-16 h-20 portrait-box mb-1"><img id="sel-mateng" src="" class="w-full h-full object-cover"></div>
          <span class="font-bold text-xs text-purple-300">마등 (馬騰)</span>
          <span class="text-[10px] text-slate-300">량주 (서량)</span>
        </div>
        <div onclick="selectRuler('liubiao')" class="koei-box p-2 rounded cursor-pointer hover:border-yellow-300 hover:scale-105 transition flex flex-col items-center">
          <div class="w-16 h-20 portrait-box mb-1"><img id="sel-liubiao" src="" class="w-full h-full object-cover"></div>
          <span class="font-bold text-xs text-sky-300">유표 (劉表)</span>
          <span class="text-[10px] text-slate-300">형주 (양양)</span>
        </div>
      </div>
    </div>
  </div>

  <!-- 상인 모달 -->
  <div id="trade-modal" class="fixed inset-0 modal-backdrop z-50 hidden flex items-center justify-center p-3">
    <div class="koei-box w-full max-w-md p-4 rounded shadow-2xl border-4 border-amber-400">
      <div class="flex items-center justify-between border-b-2 border-amber-400 pb-2 mb-3">
        <h2 id="trade-modal-title" class="text-sm font-black text-yellow-300 text-pixel">상인 교역소</h2>
        <button onclick="closeModal('trade-modal')" class="text-slate-400 hover:text-white font-bold text-lg px-2">✕</button>
      </div>
      <div class="space-y-2 text-xs">
        <div class="bg-blue-950 p-2 rounded border border-blue-700 flex justify-between font-mono">
          <span>금: <strong id="trade-gold-val" class="text-yellow-300">2400</strong></span>
          <span>군량: <strong id="trade-food-val" class="text-emerald-300">30000</strong></span>
        </div>
        <div>
          <label class="block font-bold text-amber-300 mb-1">거래 수량 입력:</label>
          <input type="number" id="trade-input" value="1000" min="100" max="10000" step="100" class="w-full bg-blue-950 border border-amber-400 rounded p-1.5 text-white font-mono font-bold">
        </div>
      </div>
      <div class="mt-3 pt-2 border-t border-amber-500/40 flex justify-end gap-2">
        <button onclick="closeModal('trade-modal')" class="px-3 py-1 bg-slate-700 hover:bg-slate-600 rounded text-xs">취소</button>
        <button onclick="confirmTrade()" class="px-4 py-1 bg-amber-600 hover:bg-amber-500 text-white font-bold rounded text-xs">거래 체결</button>
      </div>
    </div>
  </div>

  <!-- 하단 상태 바 -->
  <footer class="bg-gray-900 border-t border-amber-600/60 px-3 py-1 text-[11px] text-slate-400 flex flex-wrap items-center justify-between">
    <div>
      <span class="text-amber-400 font-bold">三國志 III Master Popup Edition</span> | 정통 코에이 팝업 시스템
    </div>
    <div class="flex items-center gap-3">
      <span>단축키: <strong>0</strong> (휴양) | <strong>4</strong> (정보정찰) | <strong>M</strong> (소리토글)</span>
    </div>
  </footer>

  <!-- ==================== 자바스크립트 엔진 ==================== -->
  <script>
    const PORTRAITS = __PORTRAITS_JSON__;

    const PROVINCES = [
      { id: 1, name: '유주', ruler: '공손찬', leader: '공손찬', advisor: '전주', pop: 280000, gold: 1800, food: 22000, soldiers: 12000, officers: 6, loyalty: 70, defense: 45, x: 71.0, y: 8.0, adj: [2, 12] },
      { id: 2, name: '기주', ruler: '원소', leader: '원소', advisor: '저수', pop: 450000, gold: 3500, food: 48000, soldiers: 28000, officers: 12, loyalty: 75, defense: 60, x: 63.5, y: 16.5, adj: [1, 3, 4, 12, 13] },
      { id: 3, name: '청주', ruler: '원소', leader: '원담', advisor: '신평', pop: 310000, gold: 2100, food: 25000, soldiers: 14000, officers: 7, loyalty: 65, defense: 40, x: 84.5, y: 19.0, adj: [2, 4, 5] },
      { id: 4, name: '연주', ruler: '조조', leader: '조조', advisor: '순욱', pop: 420000, gold: 4200, food: 45000, soldiers: 32000, officers: 15, loyalty: 88, defense: 75, x: 70.5, y: 25.5, adj: [2, 3, 5, 6, 13] },
      { id: 5, name: '서주', ruler: '조조', leader: '조인', advisor: '만총', pop: 350000, gold: 2500, food: 30000, soldiers: 18000, officers: 8, loyalty: 72, defense: 50, x: 81.5, y: 31.0, adj: [3, 4, 6, 7] },
      { id: 6, name: '예주', ruler: '조조', leader: '하후돈', advisor: '곽가', pop: 390000, gold: 3100, food: 36000, soldiers: 22000, officers: 10, loyalty: 80, defense: 55, x: 67.0, y: 36.5, adj: [4, 5, 7, 8, 13] },
      { id: 7, name: '양주', ruler: '손권', leader: '손권', advisor: '주유', pop: 510000, gold: 4800, food: 55000, soldiers: 35000, officers: 16, loyalty: 92, defense: 80, x: 78.5, y: 51.5, adj: [5, 6, 8, 9] },
      { id: 8, name: '형주', ruler: '유비', leader: '유비', advisor: '관우', pop: 382000, gold: 2400, food: 30000, soldiers: 17200, officers: 13, loyalty: 60, defense: 65, x: 48.5, y: 49.5, adj: [6, 7, 9, 10, 13] },
      { id: 9, name: '교주', ruler: '사섭', leader: '사섭', advisor: '사일', pop: 210000, gold: 1500, food: 18000, soldiers: 9000, officers: 5, loyalty: 85, defense: 35, x: 48.5, y: 73.0, adj: [7, 8, 10] },
      { id: 10, name: '익주', ruler: '유장', leader: '유장', advisor: '장송', pop: 480000, gold: 3800, food: 42000, soldiers: 25000, officers: 11, loyalty: 68, defense: 70, x: 21.0, y: 44.5, adj: [8, 9, 11, 13] },
      { id: 11, name: '량주', ruler: '마등', leader: '마등', advisor: '한수', pop: 260000, gold: 1900, food: 21000, soldiers: 19000, officers: 8, loyalty: 82, defense: 50, x: 22.0, y: 19.5, adj: [10, 12, 13] },
      { id: 12, name: '병주', ruler: '원소', leader: '고간', advisor: '곽원', pop: 240000, gold: 1600, food: 19000, soldiers: 11000, officers: 5, loyalty: 62, defense: 45, x: 45.0, y: 17.0, adj: [1, 2, 11, 13] },
      { id: 13, name: '사례교위부', ruler: '조조', leader: '조홍', advisor: '가후', pop: 560000, gold: 5200, food: 60000, soldiers: 38000, officers: 14, loyalty: 85, defense: 90, x: 45.5, y: 27.5, adj: [2, 4, 6, 8, 10, 11, 12] }
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
      storageHp: 100,
      rates: { riceSell: 107, riceBuy: 59, crossbow: 57, heavyBow: 95, horse: 49 },
      currentInfoTab: 'sol',
      bgmPlaying: false,
      audioCtx: null,
      bgmTimer: null
    };

    let battleData = {
      targetProv: null,
      turn: 1,
      myPower: 100,
      enemyPower: 100,
      mySoldiers: 17200,
      enemySoldiers: 15000,
      storageHp: 100
    };

    window.addEventListener('DOMContentLoaded', () => {
      renderMapPins();
      updateRightPanel(gameState.selectedProvId);
      setupRulerPortraits();
      bindKeyboardShortcuts();
      logMessage('🎮 삼국지 3 팝업 에디션이 완벽하게 가동되었습니다.', 'text-emerald-400 font-bold');
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

    // ==================== 팝업식 메뉴 토글 (핵심 개선) ====================
    function togglePopup(id) {
      const el = document.getElementById(id);
      const isShow = el.classList.contains('show');
      closeAllPopups();
      if (!isShow) {
        el.classList.add('show');
      }
    }

    function closeAllPopups() {
      document.querySelectorAll('.koei-popup-window').forEach(w => w.classList.remove('show'));
    }

    window.onclick = function(e) {
      if (!e.target.closest('.relative')) {
        closeAllPopups();
      }
    };

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

      const storageStatusEl = document.getElementById('food-storage-status');
      if (storageStatusEl) {
        storageStatusEl.innerText = `내구 ${gameState.storageHp}% (${gameState.storageHp >= 50 ? '안전' : '위험'})`;
        storageStatusEl.className = gameState.storageHp >= 50 ? 'text-emerald-400 font-black' : 'text-red-400 font-black';
      }

      const myProvs = PROVINCES.filter(x => x.ruler === gameState.rulerName).length;
      document.getElementById('unify-progress').innerText = `${myProvs} / 13주 (${Math.round((myProvs / 13) * 100)}%)`;
      const myCountEl = document.getElementById('my-provinces-count');
      if (myCountEl) myCountEl.innerText = myProvs;

      // 오직 모든 영지가 0개가 되었을 때만 멸망!
      if (myProvs === 0) {
        alert('💀 적군에게 모든 본거지와 영지를 빼앗겨 천하의 뜻이 꺾였습니다! (보유 영지: 0개)');
        logMessage('💀 [천하 멸망] 모든 영지를 상실하여 군벌이 해체되었습니다.', 'text-red-500 font-black');
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

    // ==================== 창고 원클릭 100% 완전 복구 ====================
    function repairFoodStorage() {
      closeAllPopups();
      const myProv = getMyCapital();
      if (myProv.gold < 200) {
        alert('주군량고를 보수하려면 금 200전이 필요합니다.');
        return;
      }
      playSfx('build');
      myProv.gold -= 200;
      myProv.defense = Math.min(100, myProv.defense + 15);
      gameState.storageHp = 100;

      logMessage(`🛠️ [창고 완벽 보수] 금 200전으로 주군량고를 튼튼히 보수하여 내구도를 100%로 완전 복구했습니다! (성 방어력 +15)`, 'text-emerald-300 font-bold');
      updateRightPanel(myProv.id);
      alert('🌾 주군량고(식량저장창고) 내구도가 100%로 완전 복구되었습니다!');
    }

    function repairStorageInBattle() {
      const myProv = getMyCapital();
      if (myProv.gold < 200) {
        alert('군자금 200전이 필요합니다!');
        return;
      }
      playSfx('build');
      myProv.gold -= 200;
      battleData.storageHp = 100;
      gameState.storageHp = 100;

      document.getElementById('battle-storage-pct').innerText = '100%';
      document.getElementById('battle-storage-bar').style.width = '100%';
      logBattleMsg('🛠️ [긴급 수리] 금 200전을 들여 식량창고 내구도를 100%로 완전 회복했습니다!', 'text-emerald-300 font-bold');
      updateRightPanel(myProv.id);
    }

    // ==================== 0. 휴양 ====================
    function executeRest() {
      closeAllPopups();
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

    // ==================== 1. 군사 & 야전 배틀 모달 ====================
    function openWarModal() {
      closeAllPopups();
      const myProv = getMyCapital();
      const targetProv = PROVINCES.find(x => x.id === gameState.selectedProvId);

      if (!myProv.adj.includes(targetProv.id) || targetProv.ruler === gameState.rulerName) {
        alert(`공격할 수 없습니다!\n본거지(${myProv.name})와 국경이 맞닿아 있는 인접한 적의 주만 출병할 수 있습니다.`);
        return;
      }

      playSfx('war');
      battleData.targetProv = targetProv;
      battleData.turn = 1;
      battleData.myPower = 100;
      battleData.enemyPower = 100;
      battleData.mySoldiers = myProv.soldiers;
      battleData.enemySoldiers = targetProv.soldiers;
      battleData.storageHp = gameState.storageHp;

      document.getElementById('battle-title').innerText = `[야전 결전] ${myProv.name} vs ${targetProv.name} (${gameState.rulerName}군 vs ${targetProv.ruler}군)`;
      document.getElementById('battle-enemy-name').innerText = `⚔️ 적군 (${targetProv.ruler} 수비군)`;
      document.getElementById('battle-enemy-def-tag').innerText = `성 방어력: ${targetProv.defense}`;
      document.getElementById('battle-my-soldiers-txt').innerText = myProv.soldiers.toLocaleString();
      document.getElementById('battle-enemy-soldiers-txt').innerText = targetProv.soldiers.toLocaleString();
      document.getElementById('battle-my-power-pct').innerText = '100%';
      document.getElementById('battle-enemy-power-pct').innerText = '100%';
      document.getElementById('battle-my-bar').style.width = '100%';
      document.getElementById('battle-enemy-bar').style.width = '100%';
      document.getElementById('battle-storage-pct').innerText = battleData.storageHp + '%';
      document.getElementById('battle-storage-bar').style.width = battleData.storageHp + '%';
      document.getElementById('battle-turn-count').innerText = `턴: 1 / 10`;

      const hasAlly = gameState.allies.length > 0;
      const tag = document.getElementById('battle-alliance-tag');
      if (hasAlly) {
        tag.classList.remove('hidden');
        tag.innerText = `🤝 동맹군(${gameState.allies.join(', ')}) 원군 15,000명 참전! (+50% 타격)`;
      } else {
        tag.classList.add('hidden');
      }

      document.getElementById('battle-modal-logs').innerHTML = `<div class="text-yellow-300 font-bold">🚩 ${targetProv.name} 공략전 개시! 전술 명령을 내리십시오.</div>`;
      openModal('battle-modal');
    }

    function battleActionAttack() {
      playSfx('war');
      const myProv = getMyCapital();
      const targetProv = battleData.targetProv;

      let myDmg = Math.floor(battleData.mySoldiers * 0.35);
      if (gameState.allies.length > 0) myDmg = Math.floor(myDmg * 1.5);

      const enemyDmg = Math.floor(battleData.enemySoldiers * 0.15);

      battleData.enemySoldiers = Math.max(0, battleData.enemySoldiers - myDmg);
      battleData.mySoldiers = Math.max(0, battleData.mySoldiers - enemyDmg);
      myProv.soldiers = battleData.mySoldiers;

      battleData.storageHp = Math.max(0, battleData.storageHp - 8);
      gameState.storageHp = battleData.storageHp;

      updateBattleModalUI();
      logBattleMsg(`⚔️ [총공격] 적군에게 ${myDmg.toLocaleString()}명의 타격을 입혔습니다! (아군 피해: ${enemyDmg.toLocaleString()}명, 창고내구 -8%)`, 'text-red-400 font-bold');
      nextBattleTurn();
    }

    function battleActionTrap() {
      playSfx('war');
      const trapDmg = Math.floor(battleData.enemySoldiers * 0.4);
      battleData.enemySoldiers = Math.max(0, battleData.enemySoldiers - trapDmg);

      updateBattleModalUI();
      logBattleMsg(`🧠 [책사 복병함정 적중!] 제갈량의 지략으로 적군이 혼란에 빠져 ${trapDmg.toLocaleString()}명이 궤멸되었습니다! (아군 무피해)`, 'text-cyan-300 font-bold');
      nextBattleTurn();
    }

    function battleActionRaidStorage() {
      playSfx('victory');
      battleData.enemySoldiers = 0;
      updateBattleModalUI();
      logBattleMsg(`🌾 [대성공!!] 적의 주군량고를 기습하여 전소시켰습니다! 적군 전원 탈영, 즉시 대승리!`, 'text-yellow-300 font-black text-sm');
      setTimeout(concludeBattleWin, 1000);
    }

    function nextBattleTurn() {
      battleData.turn++;
      document.getElementById('battle-turn-count').innerText = `턴: ${battleData.turn} / 10`;

      if (battleData.enemySoldiers <= 0) setTimeout(concludeBattleWin, 800);
      else if (battleData.mySoldiers <= 0 || battleData.storageHp <= 0) setTimeout(concludeBattleLoss, 800);
      else if (battleData.turn > 10) {
        alert('10턴이 경과하여 무승부로 퇴각합니다.');
        closeModal('battle-modal');
        updateRightPanel(gameState.selectedProvId);
      }
    }

    function updateBattleModalUI() {
      const myProv = getMyCapital();
      const targetProv = battleData.targetProv;
      const myPct = Math.round((battleData.mySoldiers / (myProv.soldiers + 1000)) * 100);
      const enemyPct = Math.round((battleData.enemySoldiers / (targetProv.soldiers + 1000)) * 100);

      document.getElementById('battle-my-soldiers-txt').innerText = battleData.mySoldiers.toLocaleString();
      document.getElementById('battle-enemy-soldiers-txt').innerText = battleData.enemySoldiers.toLocaleString();
      document.getElementById('battle-my-power-pct').innerText = myPct + '%';
      document.getElementById('battle-enemy-power-pct').innerText = enemyPct + '%';
      document.getElementById('battle-my-bar').style.width = Math.min(100, myPct) + '%';
      document.getElementById('battle-enemy-bar').style.width = Math.min(100, enemyPct) + '%';
      document.getElementById('battle-storage-pct').innerText = battleData.storageHp + '%';
      document.getElementById('battle-storage-bar').style.width = battleData.storageHp + '%';
    }

    function concludeBattleWin() {
      playSfx('victory');
      const targetProv = battleData.targetProv;
      targetProv.ruler = gameState.rulerName;
      targetProv.leader = gameState.rulerName;
      targetProv.soldiers = 12000;
      targetProv.defense = 50;

      closeModal('battle-modal');
      renderMapPins();
      updateRightPanel(targetProv.id);
      alert(`🎉 [대승리!] ${targetProv.name}을(를) 완벽히 점령하고 영지로 흡수했습니다!`);
      logMessage(`🏆 [대승리] ${targetProv.name}을(를) 평정하여 영토를 넓혔습니다!`, 'text-yellow-300 font-extrabold');
      checkUnification();
    }

    function concludeBattleLoss() {
      closeModal('battle-modal');
      alert(`⚠️ [패배] 아군 병력이 소진되었거나 식량창고가 피탈되어 퇴각합니다.`);
      updateRightPanel(gameState.selectedProvId);
    }

    function retreatFromBattleModal() {
      if (confirm('전장에서 안전하게 퇴각하시겠습니까?')) {
        closeModal('battle-modal');
        updateRightPanel(gameState.selectedProvId);
      }
    }

    function logBattleMsg(msg, color='text-slate-200') {
      const box = document.getElementById('battle-modal-logs');
      const div = document.createElement('div');
      div.className = color;
      div.innerText = msg;
      box.appendChild(div);
      box.scrollTop = box.scrollHeight;
    }

    // ==================== 4. 정보 모달 (금 100) ====================
    function openInfoModal() {
      closeAllPopups();
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
      closeAllPopups();
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
      closeAllPopups();
      const myProv = getMyCapital();
      const targetProv = PROVINCES.find(x => x.id === gameState.selectedProvId);
      if (targetProv.ruler === gameState.rulerName) { alert('자신과는 동맹을 맺을 수 없습니다.'); return; }
      if (gameState.allies.includes(targetProv.ruler)) { alert('이미 굳건한 동맹 관계입니다!'); return; }
      if (myProv.gold < 500) { alert('금 500전이 필요합니다.'); return; }

      playSfx('alliance');
      myProv.gold -= 500;
      if (Math.random() < 0.90) {
        gameState.allies.push(targetProv.ruler);
        logMessage(`🤝 [동맹 체결] ${targetProv.ruler} 세력과 군사 동맹을 맺었습니다! 출병 시 15,000명의 연합군이 가세합니다!`, 'text-emerald-300 font-extrabold');
      } else {
        logMessage(`⚠️ [동맹 결렬] ${targetProv.ruler}이(가) 결정을 유보했습니다.`, 'text-slate-300');
      }
      renderMapPins();
      updateRightPanel(myProv.id);
    }

    function executeBreakAlliance() {
      closeAllPopups();
      const targetProv = PROVINCES.find(x => x.id === gameState.selectedProvId);
      const idx = gameState.allies.indexOf(targetProv.ruler);
      if (idx !== -1) {
        gameState.allies.splice(idx, 1);
        logMessage(`⚡ [동맹 파기] ${targetProv.ruler}과의 동맹을 파기했습니다.`, 'text-red-400');
        renderMapPins();
      }
    }

    // ==================== 2. 인사 / 5. 개발 / 7. 상인 / 8. 특별 ====================
    function executeSearchOfficer() {
      closeAllPopups();
      const names = ['제갈량', '방통', '황충', '위연', '강유', '마초', '법정'];
      const picked = names[Math.floor(Math.random() * names.length)];
      logMessage(`🔍 [인재 수색] 재야의 명장 [${picked}]의 은거지를 발견하였습니다!`, 'text-cyan-300 font-bold');
    }
    function executeHireOfficer() {
      closeAllPopups();
      const myProv = getMyCapital();
      myProv.officers++;
      logMessage(`📜 [등용 성공] 명망 높은 장수를 맞이했습니다! (장수 수: ${myProv.officers}명)`, 'text-emerald-300 font-bold');
      updateRightPanel(myProv.id);
    }
    function executeReward() {
      closeAllPopups();
      const myProv = getMyCapital();
      if (myProv.gold < 100) return;
      myProv.gold -= 100;
      logMessage(`🎁 [포상] 장수들에게 하사품을 내려 충성도를 100으로 높였습니다!`, 'text-yellow-300');
      updateRightPanel(myProv.id);
    }
    function executeRelief() {
      closeAllPopups();
      const myProv = getMyCapital();
      if (myProv.food < 1000) return;
      myProv.food -= 1000;
      myProv.loyalty = Math.min(100, myProv.loyalty + 15);
      logMessage(`🥣 [주민 구호] 백성들에게 곡식을 나누어주어 민충이 +15 상승했습니다!`, 'text-emerald-300 font-bold');
      updateRightPanel(myProv.id);
    }
    function executeLandDev() {
      closeAllPopups();
      const myProv = getMyCapital();
      if (myProv.gold < 200) return;
      myProv.gold -= 200;
      logMessage(`🚜 [개간] 농지를 개간하여 가을 추수량을 늘렸습니다!`, 'text-emerald-300');
      updateRightPanel(myProv.id);
    }
    function executeFloodControl() {
      closeAllPopups();
      const myProv = getMyCapital();
      if (myProv.gold < 200) return;
      myProv.gold -= 200;
      logMessage(`🌊 [치수] 제방을 정비하여 수해를 방비했습니다!`, 'text-cyan-300');
      updateRightPanel(myProv.id);
    }
    function executeCommerceDev() {
      closeAllPopups();
      const myProv = getMyCapital();
      if (myProv.gold < 200) return;
      myProv.gold -= 200;
      logMessage(`🏪 [상업 투자] 시장을 활성화하여 7월 세수 수입을 증대시켰습니다!`, 'text-yellow-300');
      updateRightPanel(myProv.id);
    }
    function executeTraining() {
      closeAllPopups();
      const myProv = getMyCapital();
      if (myProv.food < 500) return;
      myProv.food -= 500;
      logMessage(`⚔️ [훈련] 전군 훈련 실시로 사기와 훈련도를 대폭 향상시켰습니다!`, 'text-emerald-300');
      updateRightPanel(myProv.id);
    }
    function executeConscription() {
      closeAllPopups();
      const myProv = getMyCapital();
      myProv.soldiers += 2500;
      myProv.loyalty = Math.max(10, myProv.loyalty - 8);
      logMessage(`📢 [징병] 2,500명을 징집하였습니다. (민충 -8)`, 'text-slate-200');
      updateRightPanel(myProv.id);
    }
    function executeRecruit() {
      closeAllPopups();
      const myProv = getMyCapital();
      if (myProv.gold < 500) return;
      myProv.gold -= 500;
      myProv.soldiers += 3000;
      logMessage(`🎖️ [모병] 금 500전으로 정예 의용군 3,000명을 모집했습니다!`, 'text-yellow-300');
      updateRightPanel(myProv.id);
    }
    function executeShipBuilding() {
      closeAllPopups();
      const myProv = getMyCapital();
      if (myProv.gold < 300) return;
      myProv.gold -= 300;
      logMessage(`⛵ [선박건조] 도하용 누선 20척을 건조 완료했습니다!`, 'text-cyan-300');
      updateRightPanel(myProv.id);
    }

    let currentTradeType = '';
    function openTradeModal(type) {
      closeAllPopups();
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

    function executeHeal() { closeAllPopups(); logMessage(`💊 [치료] 화타의 비방으로 부상병을 전원 치료했습니다!`, 'text-emerald-300 font-bold'); }
    function executeEmergencyTax() {
      closeAllPopups();
      const myProv = getMyCapital();
      myProv.gold += 1200;
      myProv.loyalty = Math.max(10, myProv.loyalty - 20);
      logMessage(`⚠️ [임시징수] 금 1,200전을 긴급 징수했습니다. (민충 -20)`, 'text-red-300');
      updateRightPanel(myProv.id);
    }

    function executeWander() { closeAllPopups(); alert('아직 유랑군으로 전환할 시기가 아닙니다.'); }
    function openTaxRateModal() { closeAllPopups(); alert('세율이 40%로 책정되어 있습니다.'); }
    function executeDelegate() { closeAllPopups(); alert('태수에게 위임 명령을 하달했습니다.'); }
    function executeAppoint() { closeAllPopups(); alert('군사와 태수를 정식 임명했습니다.'); }
    function executeDirectOrder() { closeAllPopups(); alert('장수들에게 특수 군령을 전파했습니다.'); }
    function executeFireOfficer() { closeAllPopups(); alert('장수를 해고 조치했습니다.'); }
    function executeConfiscate() { closeAllPopups(); alert('보물을 회수했습니다.'); }

    function openRulerSelectModal() { closeAllPopups(); openModal('ruler-select-modal'); }
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

    // ==================== BGM ====================
    function toggleBGM() {
      closeAllPopups();
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
        document.getElementById('bgm-btn').className = 'px-2.5 py-1 text-xs font-bold rounded bg-emerald-700 text-yellow-100 border border-yellow-400 flex items-center gap-1 shadow';
        playRetroMelody();
      } catch (e) { console.error(e); }
    }
    function stopBGM() {
      gameState.bgmPlaying = false;
      if (gameState.bgmTimer) clearTimeout(gameState.bgmTimer);
      document.getElementById('bgm-status').innerText = '정지됨';
      document.getElementById('bgm-icon').innerText = '🎵';
      document.getElementById('bgm-btn').className = 'px-2.5 py-1 text-xs font-bold rounded bg-amber-700 text-yellow-100 border border-yellow-400 flex items-center gap-1 shadow';
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
      closeAllPopups();
      localStorage.setItem('samgukji3_save', JSON.stringify({ gameState, provinces: PROVINCES }));
      logMessage('💾 [저장 완료] 게임 상태가 브라우저에 저장되었습니다.', 'text-emerald-300');
    }
    function loadGame() {
      closeAllPopups();
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
      closeAllPopups();
      if (confirm('게임을 처음부터 다시 시작하시겠습니까?')) location.reload();
    }
  </script>
</body>
</html>'''

    print("Replacing placeholders...")
    html_code = html_code.replace("__MAP_B64__", map_b64)
    html_code = html_code.replace("__PORTRAITS_JSON__", portraits_json)
    html_code = html_code.replace("__LIUBEI_B64__", liubei_b64)

    out_paths = [
        r"C:\Users\LENOVO\Desktop\sam3_update.html",
        r"C:\Users\LENOVO\Desktop\삼국지_황제의결단_웹게임.html",
        os.path.join(brain_dir, "samgukji_game.html"),
        r"g:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\samgukji.html",
        r"g:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\교육학\samgukji.html"
    ]

    for p in out_paths:
        try:
            with open(p, "w", encoding="utf-8") as f:
                f.write(html_code)
            print(f"Generated: {p} ({len(html_code):,} bytes)")
        except Exception as e:
            print(f"Failed {p}: {e}")

if __name__ == "__main__":
    build_popup_fixed_game()
