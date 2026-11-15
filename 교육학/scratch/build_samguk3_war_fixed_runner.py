# -*- coding: utf-8 -*-
import os
import json

def generate_samguk3_final_master():
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
  <title>삼국지 3 (三國志 III) 황제의 결단 - 정통 팝업 & 1:1 장수 결투 & 적군 침공 AI & 난이도 상중하</title>
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

    /* ==================== 최상단 메뉴바 (원작 100% 동일) ==================== */
    #main-header {
      background: #000080;
      border-top: 2px solid #d4af37;
      border-bottom: 2px solid #d4af37;
      overflow: visible !important;
      position: relative;
      z-index: 99999;
    }
    .menu-bar-row {
      overflow: visible !important;
      position: relative;
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      gap: 3px;
    }

    .menu-item-wrap {
      position: relative;
      display: inline-block;
      overflow: visible !important;
    }

    .menu-btn {
      background: #000080;
      border: 1.5px solid #d4af37;
      color: #ffffff;
      padding: 4px 9px;
      font-size: 13px;
      font-weight: 800;
      cursor: pointer;
      border-radius: 2px;
      transition: all 0.12s;
      white-space: nowrap;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      letter-spacing: 0.5px;
    }
    .menu-btn:hover {
      background: #1e3a8a;
      border-color: #fef08a;
      color: #fef08a;
    }
    .menu-btn:active { transform: translateY(1px); }

    /* ==================== 찰칵 떨어지는 원작 정통 세로 팝업 윈도우 ==================== */
    .koei-popup-window {
      position: absolute !important;
      top: calc(100% + 2px) !important;
      left: 0 !important;
      background: #000066 !important;
      border: 2px solid #ffffff !important;
      outline: 2px solid #000033 !important;
      box-shadow: 6px 10px 24px rgba(0, 0, 0, 0.95), inset 0 0 6px rgba(0,0,0,0.6) !important;
      min-width: 155px !important;
      width: max-content !important;
      z-index: 9999999 !important;
      display: none;
      flex-direction: column !important;
      padding: 4px 0 !important;
      margin: 0 !important;
      border-radius: 2px !important;
    }
    .koei-popup-window.show {
      display: flex !important;
      animation: popFade 0.1s ease-out;
    }
    @keyframes popFade {
      from { opacity: 0; transform: translateY(-4px); }
      to { opacity: 1; transform: translateY(0); }
    }
    .koei-popup-item {
      padding: 5px 14px !important;
      font-size: 13px !important;
      color: #ffffff !important;
      cursor: pointer !important;
      white-space: nowrap !important;
      font-weight: 700 !important;
      letter-spacing: 1px !important;
      border-bottom: 1px solid rgba(255, 255, 255, 0.08) !important;
      transition: background 0.1s, color 0.1s, padding-left 0.1s !important;
    }
    .koei-popup-item:last-child {
      border-bottom: none !important;
    }
    .koei-popup-item:hover {
      background: #1e3a8a !important;
      color: #fde047 !important;
      padding-left: 18px !important;
    }
    .koei-popup-item.orange {
      color: #fb923c !important;
    }
    .koei-popup-item.orange:hover {
      color: #fef08a !important;
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
      background: rgba(0, 0, 0, 0.86);
      backdrop-filter: blur(2px);
    }
    .text-pixel {
      text-shadow: 1px 1px 0 #000, -1px -1px 0 #000, 1px -1px 0 #000, -1px 1px 0 #000;
    }
  </style>
</head>
<body class="bg-gray-950 min-h-screen text-slate-100 flex flex-col justify-between">

  <!-- ==================== 1. 상단 메뉴바 (원작 팝업 윈도우 완벽 연동) ==================== -->
  <header id="main-header" class="px-2 sm:px-3 py-1 flex items-center justify-between gap-1 shadow-2xl">
    
    <!-- 10대 메뉴 (가로 1줄 고정, 각 버튼 클릭 시 바로 아래에 하얀 테두리 세로 팝업창 찰칵 노출) -->
    <div class="menu-bar-row">
      
      <!-- 0. 휴양 -->
      <div class="menu-item-wrap">
        <button onclick="executeRest()" class="menu-btn !bg-blue-900 border-yellow-400 text-yellow-300 font-black hover:!bg-blue-700 shadow">
          0. 휴양
        </button>
      </div>

      <!-- 1. 군사 (클릭 시 원작 팝업창 노출 - media_1793680516133_d2305157.jpg 100% 일치) -->
      <div class="menu-item-wrap">
        <button onclick="togglePopup(event, 'popup-military')" class="menu-btn">
          1. 군사 ▾
        </button>
        <div id="popup-military" class="koei-popup-window">
          <div onclick="openMoveModal()" class="koei-popup-item">1. 이  동</div>
          <div onclick="openTransportModal()" class="koei-popup-item orange">2. 수  송</div>
          <div onclick="repairFoodStorage()" class="koei-popup-item">3. 전쟁준비 (창고보수)</div>
          <div onclick="openWarModal()" class="koei-popup-item">4. 전  쟁</div>
          <div onclick="executeConscription()" class="koei-popup-item">5. 징  병</div>
          <div onclick="executeRecruit()" class="koei-popup-item">6. 모  병</div>
          <div onclick="executeTraining()" class="koei-popup-item">7. 훈  련</div>
          <div onclick="openReorganizeModal()" class="koei-popup-item">8. 재편성</div>
          <div onclick="executeShipBuilding()" class="koei-popup-item orange">9. 선박건조</div>
          <div onclick="openDuelSelectModal()" class="koei-popup-item !text-yellow-300 !font-extrabold bg-blue-950/80">⚔️ 장수 골라 1:1 결투!</div>
        </div>
      </div>

      <!-- 2. 인사 (클릭 시 원작 팝업창 노출) -->
      <div class="menu-item-wrap">
        <button onclick="togglePopup(event, 'popup-personnel')" class="menu-btn">
          2. 인사 ▾
        </button>
        <div id="popup-personnel" class="koei-popup-window">
          <div onclick="executeSearchOfficer()" class="koei-popup-item">1. 장수수색</div>
          <div onclick="executeHireOfficer()" class="koei-popup-item orange">2. 장수등용</div>
          <div onclick="executeReward()" class="koei-popup-item">3. 포  상</div>
          <div onclick="executeRelief()" class="koei-popup-item">4. 주민선정</div>
          <div onclick="executeDelegate()" class="koei-popup-item orange">5. 위  임</div>
          <div onclick="executeAppoint()" class="koei-popup-item">6. 임  명</div>
          <div onclick="executeDirectOrder()" class="koei-popup-item">7. 명  령</div>
          <div onclick="executeFireOfficer()" class="koei-popup-item">8. 해  고</div>
          <div onclick="executeConfiscate()" class="koei-popup-item">9. 몰  수</div>
        </div>
      </div>

      <!-- 3. 외교 (클릭 시 원작 팝업창 노출) -->
      <div class="menu-item-wrap">
        <button onclick="togglePopup(event, 'popup-diplomacy')" class="menu-btn">
          3. 외교 ▾
        </button>
        <div id="popup-diplomacy" class="koei-popup-window">
          <div onclick="executeAlliance()" class="koei-popup-item orange">1. 동맹체결</div>
          <div onclick="executeJointOperation()" class="koei-popup-item">2. 공동작전</div>
          <div onclick="executeBreakAlliance()" class="koei-popup-item orange">3. 파  기</div>
          <div onclick="executeDiplomaticExchange()" class="koei-popup-item">4. 교  환</div>
        </div>
      </div>

      <!-- 4. 정보 (금 100 정찰) -->
      <div class="menu-item-wrap">
        <button onclick="openInfoModal()" class="menu-btn !border-yellow-300 !text-yellow-200 ring-1 ring-yellow-400/50 shadow">
          4. 정보
        </button>
      </div>

      <!-- 5. 개발 -->
      <div class="menu-item-wrap">
        <button onclick="togglePopup(event, 'popup-develop')" class="menu-btn">
          5. 개발 ▾
        </button>
        <div id="popup-develop" class="koei-popup-window">
          <div onclick="executeLandDev()" class="koei-popup-item">1. 개  간</div>
          <div onclick="executeFloodControl()" class="koei-popup-item orange">2. 치  수</div>
          <div onclick="executeCommerceDev()" class="koei-popup-item">3. 상업투자</div>
        </div>
      </div>

      <!-- 6. 계략 (클릭 시 원작 팝업창 노출) -->
      <div class="menu-item-wrap">
        <button onclick="togglePopup(event, 'popup-stratagem')" class="menu-btn !border-orange-400 !text-orange-200">
          6. 계략 ▾
        </button>
        <div id="popup-stratagem" class="koei-popup-window">
          <div onclick="executeStratagem(1)" class="koei-popup-item">1. 매복의 독</div>
          <div onclick="executeStratagem(2)" class="koei-popup-item orange">2. 적중작적</div>
          <div onclick="executeStratagem(3)" class="koei-popup-item orange">3. 위서의심</div>
          <div onclick="executeStratagem(4)" class="koei-popup-item">4. 이호경식</div>
          <div onclick="executeStratagem(5)" class="koei-popup-item orange">5. 구호탄랑</div>
        </div>
      </div>

      <!-- 7. 상인 (클릭 시 원작 팝업창 노출) -->
      <div class="menu-item-wrap">
        <button onclick="togglePopup(event, 'popup-merchant')" class="menu-btn">
          7. 상인 ▾
        </button>
        <div id="popup-merchant" class="koei-popup-window">
          <div onclick="openTradeModal('sellFood')" class="koei-popup-item">1. 군량매출</div>
          <div onclick="openTradeModal('buyFood')" class="koei-popup-item">2. 군량매입</div>
          <div onclick="openTradeModal('buyWeapons')" class="koei-popup-item">3. 무기매입</div>
          <div onclick="openTradeModal('buyHorses')" class="koei-popup-item">4. 군마매입</div>
        </div>
      </div>

      <!-- 8. 특별 (클릭 시 원작 팝업창 노출) -->
      <div class="menu-item-wrap">
        <button onclick="togglePopup(event, 'popup-special')" class="menu-btn">
          8. 특별 ▾
        </button>
        <div id="popup-special" class="koei-popup-window">
          <div onclick="executeWander()" class="koei-popup-item">1. 방  랑</div>
          <div onclick="executeHeal()" class="koei-popup-item orange">2. 치  료</div>
          <div onclick="executeEmergencyTax()" class="koei-popup-item">3. 임시징수</div>
          <div onclick="openTaxRateModal()" class="koei-popup-item">4. 세율변경</div>
        </div>
      </div>

      <!-- 9. 기능 (5대 슬롯 저장/로드 연동) -->
      <div class="menu-item-wrap">
        <button onclick="togglePopup(event, 'popup-config')" class="menu-btn">
          9. 기능 ▾
        </button>
        <div id="popup-config" class="koei-popup-window">
          <div onclick="toggleBGM()" class="koei-popup-item">1. 소  리 (BGM)</div>
          <div onclick="openSaveModal()" class="koei-popup-item !text-emerald-300">2. 저  장 (5슬롯)</div>
          <div onclick="openLoadModal()" class="koei-popup-item !text-cyan-300">3. 로  드 (날짜/제목)</div>
          <div onclick="openDuelSelectModal()" class="koei-popup-item orange">4. 1:1 장수 결투</div>
          <div onclick="openRulerSelectModal()" class="koei-popup-item orange">5. 군주변경 (공손찬 등)</div>
          <div onclick="resetGame()" class="koei-popup-item">6. 처음부터</div>
        </div>
      </div>

      <!-- 🔥 게임레벨 : 상급 / 중급 / 초급 (원작 이미지 media_1793680463999_34cdcf7f.png 100% 동일) -->
      <div class="menu-item-wrap">
        <button onclick="togglePopup(event, 'popup-level')" class="menu-btn !bg-red-950 !border-red-400 !text-yellow-300 font-black shadow ring-1 ring-red-500">
          <span id="diff-badge-icon">🔥</span> <span id="diff-badge-text">3. 게임레벨 : 상급</span> ▾
        </button>
        <div id="popup-level" class="koei-popup-window">
          <div onclick="setDifficulty('hard')" class="koei-popup-item !text-red-400 font-black">🔥 3. 게임레벨 : 상급 (어려움 - 난세 패왕)</div>
          <div onclick="setDifficulty('normal')" class="koei-popup-item !text-yellow-300 font-bold">⚖️ 3. 게임레벨 : 중급 (보통 - 정통 실전)</div>
          <div onclick="setDifficulty('easy')" class="koei-popup-item !text-emerald-300 font-bold">🌱 3. 게임레벨 : 초급 (쉬움 - 초보자용)</div>
        </div>
      </div>

    </div>

    <!-- 우측 보조 컨트롤 바 -->
    <div class="flex items-center gap-1.5 flex-nowrap">
      <button onclick="openDuelSelectModal()" class="px-2 py-1 text-xs font-black rounded bg-red-700 hover:bg-red-600 text-yellow-100 border border-yellow-300 flex items-center gap-1 shadow animate-pulse">
        <span>⚔️</span> 장수 1:1 결투
      </button>
      <button id="bgm-btn" onclick="toggleBGM()" class="px-2 py-1 text-xs font-bold rounded bg-amber-700 hover:bg-amber-600 text-yellow-100 border border-yellow-400 flex items-center gap-1 shadow">
        <span id="bgm-icon">🎵</span> BGM
      </button>
      <button onclick="openSaveModal()" class="px-2 py-1 text-xs font-bold rounded bg-emerald-800 hover:bg-emerald-700 text-white border border-emerald-400 shadow">
        💾 저장
      </button>
      <button onclick="openLoadModal()" class="px-2 py-1 text-xs font-bold rounded bg-cyan-900 hover:bg-cyan-800 text-cyan-200 border border-cyan-400 shadow">
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
    <section class="flex-1 koei-box p-2 flex flex-col w-full max-w-[720px] rounded shadow-2xl relative">
      
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

        <!-- 날씨/계절 및 현재 레벨 오버레이 -->
        <div class="absolute top-2 left-2 flex flex-col gap-1 z-20">
          <div id="weather-badge" class="bg-blue-950/85 border border-amber-400 px-2.5 py-1 rounded text-xs font-bold shadow-lg flex items-center gap-1.5">
            <span id="season-text">🌸 208년 1월 (봄)</span>
            <span id="weather-text" class="text-cyan-300">🌤️ 맑음</span>
          </div>
          <div id="diff-map-tag" class="bg-red-950/90 border border-red-500 px-2 py-0.5 rounded text-[11px] font-black text-yellow-300 shadow">
            🔥 게임레벨 : 상급 (어려움 - 난세 패왕)
          </div>
        </div>

        <div class="absolute bottom-1.5 left-2 right-2 bg-blue-950/90 border border-slate-700 px-2.5 py-0.5 rounded text-[11px] text-slate-300 flex items-center justify-between z-20">
          <span>* 턴 넘김 시 <strong>적 군벌들도 서로를 맹렬히 침공</strong>합니다! ⚔️</span>
          <span class="text-amber-300 font-semibold">동맹국: 청색 표시 & 연합군 15,000 파병</span>
        </div>
      </div>
    </section>

    <!-- 우측: 원작 삼국지 3 3대 패널 (도시 상태창 + 시세창 + 군주 초상화 창) -->
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

        <!-- 🔥 영지 즉시 침공 / 출진 원클릭 액션 버튼 -->
        <div id="panel-action-btn-container" class="mt-2.5 pt-2 border-t border-blue-700/60">
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

      <!-- 2. 시세창 & 3. 군주 초상화 창 (공손찬, 조조, 원소 등 12군주 실시간 반영) -->
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

        <!-- 군주 초상화 액자 (공손찬 얼굴 및 12대 정통 픽셀 초상화 100% 선명 노출) -->
        <div class="w-1/2 koei-box p-2 flex flex-col items-center justify-between">
          <div class="text-[11px] font-bold text-amber-300 mb-1 text-center w-full border-b border-amber-500/40 pb-0.5">군주 초상화</div>
          <div class="portrait-box w-[100px] h-[120px] bg-blue-950 flex items-center justify-center overflow-hidden">
            <img id="main-ruler-face" src="__LIUBEI_B64__" alt="군주 얼굴" class="w-full h-full object-cover">
          </div>
          <div class="mt-1 text-center">
            <div id="portrait-ruler-name" class="text-xs font-extrabold text-yellow-300">군주 유비 (劉備)</div>
            <div id="portrait-ruler-stats" class="text-[10px] text-slate-300">매력: 99 | 통솔: 78</div>
          </div>
        </div>
      </div>

      <!-- 로그 창 (천하 전황 속보 실시간 출력) -->
      <div class="flex-1 koei-box p-2.5 flex flex-col min-h-[135px]">
        <div class="flex items-center justify-between text-xs font-bold text-amber-300 border-b border-amber-500/40 pb-1 mb-1.5">
          <span>📜 천하 정세 및 전쟁 속보</span>
          <button onclick="clearLogs()" class="text-[10px] text-slate-400 hover:text-white">지우기</button>
        </div>
        <div id="game-logs" class="flex-1 overflow-y-auto space-y-1 text-xs text-slate-200 pr-1 max-h-[145px] font-mono leading-relaxed">
          <div class="text-emerald-400 font-bold">👑 유비가 형주 신야에서 천하통일의 대업을 시작합니다!</div>
          <div class="text-yellow-300 font-bold">⚔️ [장수 1:1 결투] 아군 장수를 골라 적장과 1번씩 진검승부를 펼치십시오!</div>
          <div class="text-red-400 font-bold">🔥 [게임레벨 : 상급] 적 군벌들의 침공이 극도로 활발합니다!</div>
          <div class="text-cyan-300">💾 [5슬롯 저장] 날짜와 제목을 직접 지정하여 5개 슬롯에 안전 저장할 수 있습니다.</div>
        </div>
      </div>

    </aside>
  </main>

  <!-- ==================== 하단 원작 정통 대화 & 상태 프롬프트 창 ==================== -->
  <div class="bg-blue-950 border-t-2 border-amber-500/80 px-4 py-2 flex items-center justify-between text-xs font-mono shadow-2xl">
    <div class="flex items-center gap-3">
      <div class="px-3 py-1 bg-blue-900 border border-yellow-400 rounded text-yellow-300 font-extrabold">
        <span id="prompt-date">208년 봄 1월</span>
      </div>
      <div class="text-sm font-bold text-white tracking-wide">
        <span class="text-cyan-300">▶</span> <span id="prompt-text">무엇을 하겠습니까(0-9)? 상단 메뉴를 클릭하거나 단축키를 누르십시오.</span> <span class="animate-pulse">_</span>
      </div>
    </div>
    <div class="text-[11px] text-slate-400 hidden sm:inline-block">
      단축키: <strong>0</strong> (휴양) | <strong>1</strong> (군사) | <strong>4</strong> (정보) | <strong>M</strong> (소리)
    </div>
  </div>

  <!-- ==================== 🚨 적군 침공 긴급 요격/농성 모달 ==================== -->
  <div id="invasion-alert-modal" class="fixed inset-0 modal-backdrop z-50 hidden flex items-center justify-center p-3">
    <div class="koei-box w-full max-w-lg p-5 rounded shadow-2xl border-4 border-red-600 flex flex-col gap-3 animate-bounce">
      <div class="flex items-center gap-2 border-b-2 border-red-500 pb-2">
        <span class="text-3xl">🚨</span>
        <h2 class="text-lg font-black text-red-300 text-pixel">
          적군 침공 긴급 경보!
        </h2>
      </div>

      <div id="invasion-alert-msg" class="text-sm text-yellow-200 font-bold leading-relaxed bg-red-950/80 p-3 rounded border border-red-500">
        조조군 15,000 대군이 아군 영지(형주)로 진격해왔습니다!
      </div>

      <div class="text-xs text-slate-200">
        주군! 적의 기세를 꺾기 위해 장수를 골라 1:1 결투로 적장을 베거나, 성문을 닫고 농성전을 펼쳐야 합니다!
      </div>

      <div class="grid grid-cols-2 gap-3 pt-2">
        <button onclick="handleInvasionDuel()" class="py-3 bg-red-700 hover:bg-red-600 text-yellow-100 font-black text-xs rounded border-2 border-yellow-300 shadow flex items-center justify-center gap-1">
          <span>⚔️</span> 장수 출진 1:1 요격전!
        </button>
        <button onclick="handleInvasionDefend()" class="py-3 bg-blue-800 hover:bg-blue-700 text-cyan-100 font-bold text-xs rounded border-2 border-cyan-300 shadow flex items-center justify-center gap-1">
          <span>🛡️</span> 성벽 결사 농성!
        </button>
      </div>
    </div>
  </div>

  <!-- ==================== 1:1 장수 전략 결투 (일기토) 모달 ==================== -->
  <div id="duel-modal" class="fixed inset-0 modal-backdrop z-50 hidden flex items-center justify-center p-3">
    <div class="koei-box w-full max-w-2xl p-4 rounded shadow-2xl border-4 border-amber-400 flex flex-col gap-3">
      
      <!-- 결투 헤더 -->
      <div class="flex items-center justify-between border-b-2 border-amber-400 pb-2">
        <div class="flex items-center gap-2">
          <span class="text-2xl animate-bounce">⚔️</span>
          <h2 class="text-base sm:text-lg font-black text-yellow-300 text-pixel tracking-wide">
            삼국지 3 장수 1:1 진검승부 결투 (일기토)
          </h2>
        </div>
        <div class="flex items-center gap-2">
          <span id="duel-round-badge" class="bg-red-950 px-2.5 py-0.5 rounded border border-red-500 text-yellow-300 font-extrabold text-xs">
            제 1 합
          </span>
          <button onclick="closeModal('duel-modal')" class="text-slate-400 hover:text-white text-xs px-2 py-0.5 border border-slate-600 rounded">
            ✕ 닫기
          </button>
        </div>
      </div>

      <!-- 1:1 대결 장수 정보창 (좌측 아군 vs 우측 적장) -->
      <div class="grid grid-cols-2 gap-3 bg-blue-950/90 p-3 rounded border border-blue-600/80">
        
        <!-- 아군 장수 -->
        <div class="flex flex-col gap-1 border-r border-blue-700/60 pr-2">
          <div class="flex items-center justify-between">
            <span class="text-xs font-black text-emerald-400">🚩 [아군 출진 장수]</span>
            <span id="duel-my-stats" class="text-[11px] text-yellow-300 font-bold">무력: 98 | 지력: 84</span>
          </div>
          <div class="flex items-center gap-2 mt-1">
            <div class="w-14 h-16 bg-blue-900 border-2 border-emerald-400 rounded flex items-center justify-center text-3xl shadow overflow-hidden">
              <span id="duel-my-icon">🗡️</span>
            </div>
            <div class="flex-1">
              <div id="duel-my-name" class="text-sm font-black text-white text-pixel">관우 (운장)</div>
              <div class="flex justify-between text-[11px] text-slate-300 mt-1">
                <span>체력 (HP)</span>
                <span id="duel-my-hp-txt" class="text-emerald-400 font-bold">100 / 100</span>
              </div>
              <div class="gauge-container h-3 mt-0.5">
                <div id="duel-my-hp-bar" class="h-full bg-emerald-500 transition-all duration-300" style="width: 100%;"></div>
              </div>
            </div>
          </div>
        </div>

        <!-- 적군 장수 (여포, 허저, 공손찬 등) -->
        <div class="flex flex-col gap-1 pl-1">
          <div class="flex items-center justify-between">
            <span class="text-xs font-black text-red-400">⚔️ [적군 대적 장수]</span>
            <span id="duel-enemy-stats" class="text-[11px] text-yellow-300 font-bold">무력: 100 | 지력: 45</span>
          </div>
          <div class="flex items-center gap-2 mt-1">
            <div class="flex-1">
              <div id="duel-enemy-name" class="text-sm font-black text-white text-pixel text-right">여포 (봉선)</div>
              <div class="flex justify-between text-[11px] text-slate-300 mt-1">
                <span id="duel-enemy-hp-txt" class="text-red-400 font-bold">100 / 100</span>
                <span>체력 (HP)</span>
              </div>
              <div class="gauge-container h-3 mt-0.5">
                <div id="duel-enemy-hp-bar" class="h-full bg-red-600 transition-all duration-300" style="width: 100%;"></div>
              </div>
            </div>
            <div class="w-14 h-16 bg-red-950 border-2 border-red-500 rounded flex items-center justify-center text-3xl shadow overflow-hidden">
              <img id="duel-enemy-img" src="" class="w-full h-full object-cover hidden">
              <span id="duel-enemy-icon">👹</span>
            </div>
          </div>
        </div>

      </div>

      <!-- 실시간 결투 중계 컷신 로그 -->
      <div id="duel-combat-log" class="bg-blue-950 border-2 border-amber-500/70 p-3 rounded h-28 overflow-y-auto font-mono text-xs text-slate-100 space-y-1.5 shadow-inner">
        <div class="text-yellow-300 font-bold">⚔️ 두 장수가 말을 몰아 전장 중앙으로 맹렬히 돌진합니다!</div>
        <div class="text-slate-300">작전을 선택하여 적장의 빈틈을 노리거나 회심의 일격을 가하십시오.</div>
      </div>

      <!-- 5대 1:1 전략 커맨드 버튼 -->
      <div class="grid grid-cols-5 gap-2 pt-1">
        <button onclick="duelAction('quick')" class="py-2.5 px-1 bg-red-800 hover:bg-red-700 text-white font-extrabold text-xs rounded border border-red-400 shadow flex flex-col items-center">
          <span class="text-sm">⚔️</span>
          <span>쾌속 공격</span>
          <span class="text-[9px] text-slate-300 font-normal">명중률 90%</span>
        </button>
        <button onclick="duelAction('smash')" class="py-2.5 px-1 bg-amber-700 hover:bg-amber-600 text-yellow-100 font-black text-xs rounded border border-yellow-300 shadow flex flex-col items-center">
          <span class="text-sm">⚡</span>
          <span>필살 일격</span>
          <span class="text-[9px] text-yellow-200 font-normal">강타 / 60%</span>
        </button>
        <button onclick="duelAction('defend')" class="py-2.5 px-1 bg-blue-800 hover:bg-blue-700 text-cyan-100 font-bold text-xs rounded border border-blue-400 shadow flex flex-col items-center">
          <span class="text-sm">🛡️</span>
          <span>철벽 방어</span>
          <span class="text-[9px] text-cyan-200 font-normal">피해70%감소+반격</span>
        </button>
        <button onclick="duelAction('tactic')" class="py-2.5 px-1 bg-purple-800 hover:bg-purple-700 text-purple-100 font-bold text-xs rounded border border-purple-400 shadow flex flex-col items-center">
          <span class="text-sm">🧠</span>
          <span>계략 / 도발</span>
          <span class="text-[9px] text-purple-200 font-normal">혼란 유도</span>
        </button>
        <button onclick="duelAction('flee')" class="py-2.5 px-1 bg-slate-800 hover:bg-slate-700 text-slate-300 font-bold text-xs rounded border border-slate-600 shadow flex flex-col items-center">
          <span class="text-sm">🐎</span>
          <span>말머리 퇴각</span>
          <span class="text-[9px] text-slate-400 font-normal">안전 철수</span>
        </button>
      </div>

    </div>
  </div>

  <!-- ==================== 장수 선택 모달 (출진 장수 & 적장 선택) ==================== -->
  <div id="duel-select-modal" class="fixed inset-0 modal-backdrop z-50 hidden flex items-center justify-center p-3">
    <div class="koei-box w-full max-w-xl p-4 rounded shadow-2xl border-4 border-yellow-400 flex flex-col gap-3 max-h-[90vh]">
      <div class="flex items-center justify-between border-b-2 border-yellow-400 pb-2">
        <h2 class="text-base font-black text-yellow-300 text-pixel">
          ⚔️ 1:1 장수 선택 (장수를 골라 1번씩 대결!)
        </h2>
        <button onclick="closeModal('duel-select-modal')" class="text-slate-400 hover:text-white text-xs px-2 py-0.5 border border-slate-600 rounded">
          ✕
        </button>
      </div>

      <div class="text-xs text-slate-300">
        출전시킬 장수를 골라 적장과 1:1로 맞붙이십시오. 승리 시 적군 사기가 꺾이고 군자금을 노획합니다!
      </div>

      <!-- 아군 장수 목록 -->
      <div>
        <label class="block text-xs font-bold text-emerald-300 mb-1">1. 아군 출진 장수 선택:</label>
        <div id="duel-my-officer-list" class="grid grid-cols-2 sm:grid-cols-3 gap-2 max-h-40 overflow-y-auto p-1 bg-blue-950/80 rounded border border-blue-700">
          <!-- JS 렌더링 -->
        </div>
      </div>

      <!-- 적군 영지 및 적장 선택 -->
      <div class="grid grid-cols-2 gap-2">
        <div>
          <label class="block text-xs font-bold text-red-300 mb-1">2. 목표 적 영지:</label>
          <select id="duel-enemy-prov-select" onchange="updateEnemyOfficersList()" class="w-full bg-blue-950 border border-amber-400 rounded p-1.5 text-xs text-white font-bold">
            <!-- JS 렌더링 -->
          </select>
        </div>
        <div>
          <label class="block text-xs font-bold text-red-300 mb-1">3. 대전할 적장:</label>
          <select id="duel-enemy-officer-select" class="w-full bg-blue-950 border border-amber-400 rounded p-1.5 text-xs text-white font-bold">
            <!-- JS 렌더링 -->
          </select>
        </div>
      </div>

      <div class="mt-2 pt-2 border-t border-amber-500/40 flex justify-end gap-2">
        <button onclick="closeModal('duel-select-modal')" class="px-3 py-1.5 bg-slate-700 hover:bg-slate-600 rounded text-xs">취소</button>
        <button onclick="startDuelFight()" class="px-5 py-1.5 bg-red-700 hover:bg-red-600 text-white font-black rounded text-xs border border-yellow-300 shadow flex items-center gap-1">
          <span>⚔️</span> 결투 개시!
        </button>
      </div>
    </div>
  </div>

  <!-- ==================== 5대 슬롯 게임 저장 모달 ==================== -->
  <div id="save-modal" class="fixed inset-0 modal-backdrop z-50 hidden flex items-center justify-center p-3">
    <div class="koei-box w-full max-w-xl p-4 rounded shadow-2xl border-4 border-emerald-400 flex flex-col gap-3 max-h-[92vh]">
      <div class="flex items-center justify-between border-b-2 border-emerald-400 pb-2">
        <div class="flex items-center gap-2">
          <span class="text-xl">💾</span>
          <h2 class="text-base font-black text-emerald-300 text-pixel">
            삼국지 3 5대 세이브 슬롯 저장 (날짜 & 제목)
          </h2>
        </div>
        <button onclick="closeModal('save-modal')" class="text-slate-400 hover:text-white text-xs px-2 py-0.5 border border-slate-600 rounded">
          ✕
        </button>
      </div>

      <div class="text-xs text-slate-300">
        원하는 슬롯을 선택하고 저장 제목을 입력하여 현재 게임 상태를 보관하십시오.
      </div>

      <!-- 5대 슬롯 목록 -->
      <div id="save-slots-container" class="space-y-2 overflow-y-auto max-h-[50vh] pr-1">
        <!-- JS로 슬롯 1~5 렌더링 -->
      </div>

      <!-- 제목 입력 영역 (슬롯 선택 시 활성화) -->
      <div id="save-input-box" class="bg-blue-950/90 p-2.5 rounded border border-amber-400 flex flex-col gap-1.5">
        <div class="flex items-center justify-between text-xs font-bold text-amber-300">
          <span>선택된 슬롯: <strong id="selected-save-slot-label" class="text-yellow-200">슬롯 1</strong></span>
          <span class="text-slate-400 text-[11px]">제목을 직접 수정할 수 있습니다</span>
        </div>
        <input type="text" id="save-title-input" class="w-full bg-blue-900 border border-yellow-400 rounded px-2.5 py-1.5 text-xs text-white font-bold" placeholder="저장 제목을 입력하세요 (예: 208년 봄 유비 형주 방어전)">
      </div>

      <div class="pt-2 border-t border-emerald-500/40 flex justify-end gap-2">
        <button onclick="closeModal('save-modal')" class="px-3 py-1.5 bg-slate-700 hover:bg-slate-600 rounded text-xs">취소</button>
        <button onclick="confirmSaveSlot()" class="px-5 py-1.5 bg-emerald-700 hover:bg-emerald-600 text-white font-extrabold rounded text-xs border border-yellow-300 shadow flex items-center gap-1">
          <span>💾</span> 이 슬롯에 저장
        </button>
      </div>
    </div>
  </div>

  <!-- ==================== 5대 슬롯 게임 로드 모달 ==================== -->
  <div id="load-modal" class="fixed inset-0 modal-backdrop z-50 hidden flex items-center justify-center p-3">
    <div class="koei-box w-full max-w-xl p-4 rounded shadow-2xl border-4 border-cyan-400 flex flex-col gap-3 max-h-[92vh]">
      <div class="flex items-center justify-between border-b-2 border-cyan-400 pb-2">
        <div class="flex items-center gap-2">
          <span class="text-xl">📂</span>
          <h2 class="text-base font-black text-cyan-300 text-pixel">
            삼국지 3 5대 세이브 슬롯 불러오기 (날짜 & 제목)
          </h2>
        </div>
        <button onclick="closeModal('load-modal')" class="text-slate-400 hover:text-white text-xs px-2 py-0.5 border border-slate-600 rounded">
          ✕
        </button>
      </div>

      <div class="text-xs text-slate-300">
        저장된 날짜와 제목, 세력 현황을 확인한 후 불러올 슬롯을 선택하십시오.
      </div>

      <!-- 5대 로드 슬롯 목록 -->
      <div id="load-slots-container" class="space-y-2 overflow-y-auto max-h-[55vh] pr-1">
        <!-- JS로 슬롯 1~5 렌더링 -->
      </div>

      <div class="pt-2 border-t border-cyan-500/40 flex justify-end">
        <button onclick="closeModal('load-modal')" class="px-4 py-1.5 bg-slate-700 hover:bg-slate-600 rounded text-xs">닫기</button>
      </div>
    </div>
  </div>

  
  <!-- ==================== 침공 목표 적 영지 선택 모달 (인접 영지 공격 버그 완전 박멸) ==================== -->
  <div id="war-target-modal" class="fixed inset-0 modal-backdrop z-50 hidden flex items-center justify-center p-3">
    <div class="koei-box w-full max-w-2xl p-4 rounded shadow-2xl border-4 border-red-500 max-h-[88vh] flex flex-col">
      <div class="flex items-center justify-between border-b-2 border-red-500 pb-2 mb-3">
        <div class="flex items-center gap-2">
          <span class="text-xl">⚔️</span>
          <h2 class="text-base font-black text-red-300 text-pixel">
            [침공 목표 선택] 아군 영지와 국경이 맞닿은 적 영지
          </h2>
        </div>
        <button onclick="closeModal('war-target-modal')" class="text-slate-400 hover:text-white font-mono text-sm px-2 py-0.5 border border-slate-600 rounded">
          ✕ 닫기
        </button>
      </div>

      <div class="text-xs text-amber-200 mb-2 px-1 flex items-center justify-between">
        <span>🚩 침공할 적 영지를 선택하면 즉시 해당 영지로 대군이 출진합니다!</span>
        <span class="text-slate-400 text-[11px]">(국경 인접 영지만 공격 가능)</span>
      </div>

      <div id="war-target-list" class="space-y-2 overflow-y-auto max-h-[58vh] pr-1">
        <!-- 동적 렌더링 -->
      </div>

      <div class="pt-3 border-t border-red-900/80 flex items-center justify-between">
        <span class="text-[11px] text-slate-400">💡 지도에서 적 영지를 직접 클릭한 후 [이 적 영지 침공] 버튼을 눌러도 출진할 수 있습니다.</span>
        <button onclick="closeModal('war-target-modal')" class="px-3 py-1.5 bg-slate-700 hover:bg-slate-600 text-white font-bold text-xs rounded border border-slate-500">
          돌아가기
        </button>
      </div>
    </div>
  </div>

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
            <span id="battle-enemy-name" class="font-extrabold text-red-400 text-sm">⚔️ 적군 (수비군)</span>
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

        
        <!-- 🔥 장수 골라 1:1 결투 (일기토) 완벽 통합 배너 -->
        <div class="p-2.5 bg-gradient-to-r from-red-950 via-amber-950 to-red-950 border-2 border-amber-400 rounded-lg shadow-lg flex items-center justify-between">
          <div class="flex items-center gap-2.5">
            <span class="text-2xl animate-bounce">⚔️</span>
            <div>
              <div class="text-yellow-300 font-black text-xs flex items-center gap-1.5">
                <span>장수 골라 1:1 진검승부 (일기토)!</span>
                <span class="px-1.5 py-0.2 bg-red-800 text-[10px] text-yellow-100 rounded border border-yellow-400">적장 생포 시 즉시 함락</span>
              </div>
              <div class="text-slate-300 text-[11px]">아군 맹장(관우, 장비, 조운 등)을 골라 적장과 1:1로 맞붙습니다!</div>
            </div>
          </div>
          <button onclick="battleStartOfficerDuel()" class="px-3.5 py-2 bg-gradient-to-r from-red-600 to-amber-600 hover:from-red-500 hover:to-amber-500 text-white font-black text-xs rounded border-2 border-yellow-300 shadow-xl flex items-center gap-1 animate-pulse">
            <span>🗡️</span> 1:1 결투 개시!
          </button>
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
            🏳️ 퇴  각
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
          🔍 천하 13주 종합 정보 첩보 보고서 (소모: 금 100)
        </h2>
        <button onclick="closeModal('info-modal')" class="text-slate-400 hover:text-white text-xs px-2 py-0.5 border border-slate-600 rounded">
          ✕ 닫기
        </button>
      </div>

      <div class="flex gap-1.5 mb-2 text-xs">
        <button onclick="renderInfoTable('sol')" class="px-2.5 py-1 bg-blue-900 hover:bg-blue-800 rounded border border-blue-400 font-bold">1. 군사/병력</button>
        <button onclick="renderInfoTable('eco')" class="px-2.5 py-1 bg-amber-900 hover:bg-amber-800 rounded border border-amber-400 font-bold">2. 인구/금/식량</button>
        <button onclick="renderInfoTable('off')" class="px-2.5 py-1 bg-purple-900 hover:bg-purple-800 rounded border border-purple-400 font-bold">3. 장수/방어</button>
      </div>

      <div class="flex-1 overflow-y-auto max-h-[50vh] border border-blue-800 rounded bg-blue-950/80">
        <table class="w-full text-xs text-left text-slate-200">
          <thead class="bg-blue-900/90 text-amber-300 font-bold sticky top-0 border-b border-amber-500/50">
            <tr id="info-table-head"></tr>
          </thead>
          <tbody id="info-table-body" class="divide-y divide-blue-900/40 font-mono"></tbody>
        </table>
      </div>
      <div class="mt-2 text-right">
        <button onclick="closeModal('info-modal')" class="px-4 py-1.5 bg-slate-700 hover:bg-slate-600 rounded text-xs">확인 완료</button>
      </div>
    </div>
  </div>

  <!-- 상인 거래 모달 -->
  <div id="trade-modal" class="fixed inset-0 modal-backdrop z-50 hidden flex items-center justify-center p-3">
    <div class="koei-box w-full max-w-sm p-4 rounded shadow-2xl border-4 border-amber-400">
      <div class="flex items-center justify-between border-b-2 border-amber-400 pb-2 mb-3">
        <h2 id="trade-title" class="text-base font-black text-yellow-300 text-pixel">상인 거래</h2>
        <button onclick="closeModal('trade-modal')" class="text-slate-400 hover:text-white text-xs">✕</button>
      </div>
      <div class="space-y-2 text-xs">
        <div id="trade-info" class="text-slate-200"></div>
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

  <!-- ==================== 군주 선택 모달 (원작 코에이 12군주 초상화 완벽 탑재) ==================== -->
  <div id="ruler-select-modal" class="fixed inset-0 modal-backdrop z-50 hidden flex items-center justify-center p-3">
    <div class="koei-box w-full max-w-2xl p-4 rounded shadow-2xl border-4 border-yellow-400 max-h-[92vh] flex flex-col">
      <div class="flex items-center justify-between border-b-2 border-yellow-400 pb-2 mb-3">
        <div class="flex items-center gap-2">
          <span class="text-xl">👑</span>
          <h2 class="text-base font-black text-yellow-300 text-pixel">삼국지 3 12대 정통 군주 선택</h2>
        </div>
        <button onclick="closeModal('ruler-select-modal')" class="text-slate-400 hover:text-white text-xs px-2 py-0.5 border border-slate-600 rounded">✕</button>
      </div>

      <div class="text-xs text-slate-300 mb-2">
        플레이할 군주를 선택하십시오. 각 군주의 정통 도트 초상화와 본거지 거점이 연동됩니다.
      </div>

      <div class="grid grid-cols-3 sm:grid-cols-4 gap-2 text-xs text-center overflow-y-auto max-h-[60vh] p-1">
        
        <!-- 1. 공손찬 (북평/유주) - 사용자 요청 공손찬 정통 초상화 -->
        <div onclick="changeRuler('공손찬', 1, 'gongsongzan')" class="p-2 border-2 border-amber-400 bg-blue-950 rounded cursor-pointer hover:bg-blue-800 transition">
          <div class="w-16 h-20 mx-auto mb-1 bg-blue-900 border border-yellow-400 overflow-hidden portrait-box">
            <img id="sel-gongsongzan" src="" class="w-full h-full object-cover">
          </div>
          <div class="font-extrabold text-yellow-300">1. 공손찬</div>
          <div class="text-[10px] text-amber-300">유주 (북평)</div>
        </div>

        <!-- 2. 원소 (남피/기주) -->
        <div onclick="changeRuler('원소', 2, 'yuanshao_retro')" class="p-2 border border-slate-600 bg-blue-950 rounded cursor-pointer hover:bg-blue-800 transition">
          <div class="w-16 h-20 mx-auto mb-1 bg-blue-900 border border-yellow-400 overflow-hidden portrait-box">
            <img id="sel-yuanshao_retro" src="" class="w-full h-full object-cover">
          </div>
          <div class="font-bold text-white">2. 원소</div>
          <div class="text-[10px] text-yellow-200">기주 (남피)</div>
        </div>

        <!-- 3. 유비 (신야/형주) -->
        <div onclick="changeRuler('유비', 8, 'liubei')" class="p-2 border-2 border-emerald-400 bg-blue-950 rounded cursor-pointer hover:bg-blue-800 transition">
          <div class="w-16 h-20 mx-auto mb-1 bg-blue-900 border border-yellow-400 overflow-hidden portrait-box">
            <img src="__LIUBEI_B64__" class="w-full h-full object-cover">
          </div>
          <div class="font-extrabold text-emerald-300">3. 유비</div>
          <div class="text-[10px] text-emerald-400">형주 (신야)</div>
        </div>

        <!-- 4. 조조 (낙양/연주) -->
        <div onclick="changeRuler('조조', 4, 'caocao_retro')" class="p-2 border border-slate-600 bg-blue-950 rounded cursor-pointer hover:bg-blue-800 transition">
          <div class="w-16 h-20 mx-auto mb-1 bg-blue-900 border border-yellow-400 overflow-hidden portrait-box">
            <img id="sel-caocao_retro" src="" class="w-full h-full object-cover">
          </div>
          <div class="font-bold text-white">4. 조조</div>
          <div class="text-[10px] text-blue-300">연주 (낙양)</div>
        </div>

        <!-- 5. 손책 (노강/양주) -->
        <div onclick="changeRuler('손책', 7, 'sunce')" class="p-2 border border-slate-600 bg-blue-950 rounded cursor-pointer hover:bg-blue-800 transition">
          <div class="w-16 h-20 mx-auto mb-1 bg-blue-900 border border-yellow-400 overflow-hidden portrait-box">
            <img id="sel-sunce" src="" class="w-full h-full object-cover">
          </div>
          <div class="font-bold text-white">5. 손책</div>
          <div class="text-[10px] text-orange-400">양주 (노강)</div>
        </div>

        <!-- 6. 마등 (서량/량주) -->
        <div onclick="changeRuler('마등', 11, 'mateng_retro')" class="p-2 border border-slate-600 bg-blue-950 rounded cursor-pointer hover:bg-blue-800 transition">
          <div class="w-16 h-20 mx-auto mb-1 bg-blue-900 border border-yellow-400 overflow-hidden portrait-box">
            <img id="sel-mateng_retro" src="" class="w-full h-full object-cover">
          </div>
          <div class="font-bold text-white">6. 마등</div>
          <div class="text-[10px] text-cyan-300">량주 (서량)</div>
        </div>

        <!-- 7. 원술 (완/청주) -->
        <div onclick="changeRuler('원술', 3, 'yuanshu')" class="p-2 border border-slate-600 bg-blue-950 rounded cursor-pointer hover:bg-blue-800 transition">
          <div class="w-16 h-20 mx-auto mb-1 bg-blue-900 border border-yellow-400 overflow-hidden portrait-box">
            <img id="sel-yuanshu" src="" class="w-full h-full object-cover">
          </div>
          <div class="font-bold text-white">7. 원술</div>
          <div class="text-[10px] text-pink-400">청주 (완)</div>
        </div>

        <!-- 8. 유표 (양양/형주) -->
        <div onclick="changeRuler('유표', 8, 'liubiao_retro')" class="p-2 border border-slate-600 bg-blue-950 rounded cursor-pointer hover:bg-blue-800 transition">
          <div class="w-16 h-20 mx-auto mb-1 bg-blue-900 border border-yellow-400 overflow-hidden portrait-box">
            <img id="sel-liubiao_retro" src="" class="w-full h-full object-cover">
          </div>
          <div class="font-bold text-white">8. 유표</div>
          <div class="text-[10px] text-sky-300">형주 (양양)</div>
        </div>

        <!-- 9. 여포 (복양) -->
        <div onclick="changeRuler('여포', 6, 'lubu')" class="p-2 border border-red-500 bg-blue-950 rounded cursor-pointer hover:bg-blue-800 transition">
          <div class="w-16 h-20 mx-auto mb-1 bg-red-950 border border-red-400 overflow-hidden portrait-box">
            <img id="sel-lubu" src="" class="w-full h-full object-cover">
          </div>
          <div class="font-extrabold text-red-300">9. 여포</div>
          <div class="text-[10px] text-red-400">예주 (복양)</div>
        </div>

        <!-- 10. 장노 (한중/익주) -->
        <div onclick="changeRuler('장노', 10, 'zhanglu')" class="p-2 border border-slate-600 bg-blue-950 rounded cursor-pointer hover:bg-blue-800 transition">
          <div class="w-16 h-20 mx-auto mb-1 bg-blue-900 border border-yellow-400 overflow-hidden portrait-box">
            <img id="sel-zhanglu" src="" class="w-full h-full object-cover">
          </div>
          <div class="font-bold text-white">10. 장노</div>
          <div class="text-[10px] text-lime-300">익주 (한중)</div>
        </div>

        <!-- 11. 공융 (북해) -->
        <div onclick="changeRuler('공융', 5, 'gongyong')" class="p-2 border border-slate-600 bg-blue-950 rounded cursor-pointer hover:bg-blue-800 transition">
          <div class="w-16 h-20 mx-auto mb-1 bg-blue-900 border border-yellow-400 overflow-hidden portrait-box">
            <img id="sel-gongyong" src="" class="w-full h-full object-cover">
          </div>
          <div class="font-bold text-white">11. 공융</div>
          <div class="text-[10px] text-slate-300">서주 (북해)</div>
        </div>

        <!-- 12. 유요 (수춘) -->
        <div onclick="changeRuler('유요', 9, 'liuyao')" class="p-2 border border-slate-600 bg-blue-950 rounded cursor-pointer hover:bg-blue-800 transition">
          <div class="w-16 h-20 mx-auto mb-1 bg-blue-900 border border-yellow-400 overflow-hidden portrait-box">
            <img id="sel-liuyao" src="" class="w-full h-full object-cover">
          </div>
          <div class="font-bold text-white">12. 유요</div>
          <div class="text-[10px] text-slate-300">교주 (수춘)</div>
        </div>

      </div>

      <div class="mt-3 text-right">
        <button onclick="closeModal('ruler-select-modal')" class="px-4 py-1.5 bg-slate-700 hover:bg-slate-600 rounded text-xs">닫기</button>
      </div>
    </div>
  </div>

  <!-- 하단 상태 바 -->
  <footer class="bg-gray-900 border-t border-amber-600/60 px-3 py-1 text-[11px] text-slate-400 flex flex-wrap items-center justify-between">
    <div>
      <span class="text-amber-400 font-bold">三國志 III Master Final Edition</span> | 팝업식 메뉴 & 1:1 결투 & 적군 침공 AI & 난이도 상중하
    </div>
    <div class="flex items-center gap-3">
      <span>단축키: <strong>0</strong> (휴양) | <strong>1</strong> (군사) | <strong>4</strong> (정보정찰) | <strong>M</strong> (소리토글)</span>
    </div>
  </footer>

  <!-- ==================== 자바스크립트 엔진 ==================== -->
  <script>
    const PORTRAITS = __PORTRAITS_JSON__;

    const PROVINCES = [
      { id: 1, name: '유주', ruler: '공손찬', leader: '공손찬', advisor: '전주', pop: 280000, gold: 1800, food: 22000, soldiers: 12000, officers: 6, loyalty: 70, defense: 45, x: 71.0, y: 8.0, adj: [2, 12] },
      { id: 2, name: '기주', ruler: '원소', leader: '원소', advisor: '저수', pop: 450000, gold: 3500, food: 48000, soldiers: 28000, officers: 12, loyalty: 75, defense: 60, x: 63.5, y: 16.5, adj: [1, 3, 4, 12, 13] },
      { id: 3, name: '청주', ruler: '원술', leader: '기령', advisor: '신평', pop: 310000, gold: 2100, food: 25000, soldiers: 14000, officers: 7, loyalty: 65, defense: 40, x: 84.5, y: 19.0, adj: [2, 4, 5] },
      { id: 4, name: '연주', ruler: '조조', leader: '조조', advisor: '순욱', pop: 420000, gold: 4200, food: 45000, soldiers: 32000, officers: 15, loyalty: 88, defense: 75, x: 70.5, y: 25.5, adj: [2, 3, 5, 6, 13] },
      { id: 5, name: '서주', ruler: '조조', leader: '조인', advisor: '만총', pop: 350000, gold: 2500, food: 30000, soldiers: 18000, officers: 8, loyalty: 72, defense: 50, x: 81.5, y: 31.0, adj: [3, 4, 6, 7] },
      { id: 6, name: '예주', ruler: '여포', leader: '장료', advisor: '진궁', pop: 390000, gold: 3100, food: 36000, soldiers: 22000, officers: 10, loyalty: 80, defense: 55, x: 67.0, y: 36.5, adj: [4, 5, 7, 8, 13] },
      { id: 7, name: '양주', ruler: '손책', leader: '손책', advisor: '주유', pop: 510000, gold: 4800, food: 55000, soldiers: 35000, officers: 16, loyalty: 92, defense: 80, x: 78.5, y: 51.5, adj: [5, 6, 8, 9] },
      { id: 8, name: '형주', ruler: '유비', leader: '유비', advisor: '관우', pop: 382000, gold: 2400, food: 30000, soldiers: 17200, officers: 13, loyalty: 60, defense: 65, x: 48.5, y: 49.5, adj: [6, 7, 9, 10, 13] },
      { id: 9, name: '교주', ruler: '사섭', leader: '사섭', advisor: '사일', pop: 210000, gold: 1500, food: 18000, soldiers: 9000, officers: 5, loyalty: 85, defense: 35, x: 48.5, y: 73.0, adj: [7, 8, 10] },
      { id: 10, name: '익주', ruler: '장노', leader: '장노', advisor: '염포', pop: 480000, gold: 3800, food: 42000, soldiers: 25000, officers: 11, loyalty: 68, defense: 70, x: 21.0, y: 44.5, adj: [8, 9, 11, 13] },
      { id: 11, name: '량주', ruler: '마등', leader: '마등', advisor: '한수', pop: 260000, gold: 1900, food: 21000, soldiers: 19000, officers: 8, loyalty: 82, defense: 50, x: 22.0, y: 19.5, adj: [10, 12, 13] },
      { id: 12, name: '병주', ruler: '원소', leader: '고간', advisor: '곽원', pop: 240000, gold: 1600, food: 19000, soldiers: 11000, officers: 5, loyalty: 62, defense: 45, x: 45.0, y: 17.0, adj: [1, 2, 11, 13] },
      { id: 13, name: '사례교위부', ruler: '조조', leader: '조홍', advisor: '가후', pop: 560000, gold: 5200, food: 60000, soldiers: 38000, officers: 14, loyalty: 85, defense: 90, x: 45.5, y: 27.5, adj: [2, 4, 6, 8, 10, 11, 12] }
    ];

    // 주요 장수 DB (1:1 결투 및 군사 운용)
    const MY_OFFICERS = [
      { id: 'guan_yu', name: '관우 (운장)', war: 98, int: 84, lead: 97, icon: '🐉', title: '무성 (청룡언월도)', hp: 100 },
      { id: 'zhang_fei', name: '장비 (익덕)', war: 99, int: 35, lead: 88, icon: '⚡', title: '만인지적 (장팔사모)', hp: 100 },
      { id: 'zhao_yun', name: '조운 (자룡)', war: 97, int: 86, lead: 92, icon: '🛡️', title: '상산 조자룡 (일기당천)', hp: 100 },
      { id: 'huang_zhong', name: '황충 (한승)', war: 94, int: 68, lead: 87, icon: '🏹', title: '백발백중 노장', hp: 100 },
      { id: 'wei_yan', name: '위연 (문장)', war: 91, int: 70, lead: 84, icon: '🗡️', title: '한중태수 맹장', hp: 100 },
      { id: 'liu_bei', name: '유비 (현덕)', war: 75, int: 78, lead: 80, icon: '👑', title: '한실종친 군주 (쌍고검)', hp: 100 }
    ];

    const ENEMY_OFFICERS_BY_RULER = {
      '공손찬': [
        { name: '공손찬 (백규)', war: 84, int: 68, lead: 83, icon: '🐎', title: '백마의종 장군', faceKey: 'gongsongzan' },
        { name: '전예 (국양)', war: 76, int: 80, lead: 82, icon: '📜', title: '북방의 명장' }
      ],
      '조조': [
        { name: '허저 (중강)', war: 97, int: 38, lead: 84, icon: '🐻', title: '호치' },
        { name: '하후돈 (원양)', war: 92, int: 70, lead: 89, icon: '👁️', title: '독안룡' },
        { name: '장료 (문원)', war: 94, int: 84, lead: 95, icon: '⚡', title: '료래료래' },
        { name: '하후연 (묘재)', war: 91, int: 62, lead: 88, icon: '🏹', title: '신속명궁' },
        { name: '조인 (자효)', war: 88, int: 74, lead: 90, icon: '🛡️', title: '철벽의 맹장' }
      ],
      '여포': [
        { name: '여포 (봉선)', war: 100, int: 45, lead: 86, icon: '👹', title: '천하무쌍 비장', faceKey: 'lubu' },
        { name: '장료 (문원)', war: 94, int: 84, lead: 95, icon: '⚡', title: '팔건장 으뜸' },
        { name: '고순 (함진영)', war: 86, int: 60, lead: 88, icon: '🛡️', title: '함진영 대장' }
      ],
      '손책': [
        { name: '손책 (백부)', war: 92, int: 70, lead: 92, icon: '🐅', title: '소패왕', faceKey: 'sunce' },
        { name: '태사자 (자의)', war: 95, int: 72, lead: 86, icon: '🏹', title: '강동의 효웅' },
        { name: '감녕 (흥패)', war: 94, int: 76, lead: 87, icon: '🔔', title: '비단돛 방울장수' }
      ],
      '원소': [
        { name: '안량 (공석)', war: 93, int: 42, lead: 85, icon: '⚔️', title: '하북의 맹호' },
        { name: '문추 (자강)', war: 92, int: 35, lead: 84, icon: '🪓', title: '하북 으뜸장수' },
        { name: '원소 (본초)', war: 70, int: 75, lead: 80, icon: '👑', title: '맹주', faceKey: 'yuanshao_retro' }
      ],
      '마등': [
        { name: '마초 (맹기)', war: 97, int: 48, lead: 91, icon: '🦁', title: '서량의 금마초' },
        { name: '방덕 (영명)', war: 94, int: 70, lead: 86, icon: '⚰️', title: '백마장군' },
        { name: '마등 (수성)', war: 82, int: 60, lead: 84, icon: '🐎', title: '서량태수', faceKey: 'mateng_retro' }
      ],
      '유표': [
        { name: '문빙 (중업)', war: 84, int: 72, lead: 85, icon: '🛡️', title: '형주 수비명장' },
        { name: '황조 (원충)', war: 74, int: 50, lead: 70, icon: '🏹', title: '강하태수' },
        { name: '유표 (경승)', war: 55, int: 78, lead: 70, icon: '📜', title: '형주자사', faceKey: 'liubiao_retro' }
      ],
      '원술': [
        { name: '기령 (중달)', war: 84, int: 48, lead: 78, icon: '🔱', title: '삼첨도 대장' },
        { name: '원술 (공로)', war: 62, int: 65, lead: 65, icon: '👑', title: '중씨황제', faceKey: 'yuanshu' }
      ],
      '장노': [
        { name: '장위 (장로동생)', war: 78, int: 55, lead: 72, icon: '🗡️', title: '오두미 도위' },
        { name: '양백 (군사)', war: 65, int: 72, lead: 68, icon: '📜', title: '한중 부장' }
      ],
      '사섭': [
        { name: '사섭 (위언)', war: 62, int: 82, lead: 75, icon: '👑', title: '교지태수' },
        { name: '사휘 (영진)', war: 68, int: 55, lead: 65, icon: '🗡️', title: '남월의 장수' }
      ]
    };

    let gameState = {
      year: 208,
      month: 1,
      currentRuler: 'liubei',
      rulerName: '유비',
      myCapitalId: 8,
      selectedProvId: 8,
      allies: [],
      storageHp: 100,
      difficulty: 'hard', // 기본 난이도: 상급 (사용자가 너무 쉽지 않게 상급 요청!)
      rates: { riceSell: 107, riceBuy: 59, crossbow: 57, heavyBow: 95, horse: 49 },
      currentInfoTab: 'sol',
      bgmPlaying: false,
      audioCtx: null,
      bgmTimer: null
    };

    // 1:1 결투 진행 상태
    let duelState = {
      round: 1,
      myOfficer: null,
      enemyOfficer: null,
      myHp: 100,
      enemyHp: 100,
      enemyConfused: false,
      inDuel: false
    };

    let selectedSaveSlot = 1;
    let pendingInvasion = null;

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
      updateDifficultyUI();
      logMessage('🎮 삼국지 3 팝업 & 1:1 장수 결투 & 적군 침공 AI 에디션 가동!', 'text-emerald-400 font-bold');
    });

    function setupRulerPortraits() {
      const p = PORTRAITS;
      const setImg = (id, key) => { const el = document.getElementById(id); if (el && p[key]) el.src = p[key]; };
      setImg('sel-gongsongzan', 'gongsongzan');
      setImg('sel-yuanshao_retro', 'yuanshao_retro');
      setImg('sel-caocao_retro', 'caocao_retro');
      setImg('sel-sunce', 'sunce');
      setImg('sel-mateng_retro', 'mateng_retro');
      setImg('sel-yuanshu', 'yuanshu');
      setImg('sel-liubiao_retro', 'liubiao_retro');
      setImg('sel-lubu', 'lubu');
      setImg('sel-zhanglu', 'zhanglu');
      setImg('sel-gongyong', 'gongyong');
      setImg('sel-liuyao', 'liuyao');
    }

    // ==================== 🔥 게임레벨 : 상급, 중급, 초급 설정 ====================
    function setDifficulty(level) {
      closeAllPopups();
      gameState.difficulty = level;
      updateDifficultyUI();
      playSfx('build');

      const names = {
        hard: '상급 (어려움 - 난세 패왕 모드)',
        normal: '중급 (보통 - 정통 실전 모드)',
        easy: '초급 (쉬움 - 초보자용 모드)'
      };

      logMessage(`⚔️ [레벨 설정] 게임레벨이 '${names[level]}'으로 설정되었습니다!`, level === 'hard' ? 'text-red-400 font-black' : 'text-yellow-300 font-bold');
      alert(`⚔️ 게임레벨이 [${names[level]}]으로 변경되었습니다!`);
    }

    function updateDifficultyUI() {
      const iconEl = document.getElementById('diff-badge-icon');
      const textEl = document.getElementById('diff-badge-text');
      const mapTag = document.getElementById('diff-map-tag');

      if (gameState.difficulty === 'hard') {
        iconEl.innerText = '🔥';
        textEl.innerText = '3. 게임레벨 : 상급';
        mapTag.innerText = '🔥 게임레벨 : 상급 (어려움 - 난세 패왕)';
        mapTag.className = 'bg-red-950/90 border border-red-500 px-2 py-0.5 rounded text-[11px] font-black text-yellow-300 shadow';
      } else if (gameState.difficulty === 'normal') {
        iconEl.innerText = '⚖️';
        textEl.innerText = '3. 게임레벨 : 중급';
        mapTag.innerText = '⚖️ 게임레벨 : 중급 (보통 - 정통 실전)';
        mapTag.className = 'bg-blue-950/90 border border-blue-400 px-2 py-0.5 rounded text-[11px] font-bold text-cyan-200 shadow';
      } else {
        iconEl.innerText = '🌱';
        textEl.innerText = '3. 게임레벨 : 초급';
        mapTag.innerText = '🌱 게임레벨 : 초급 (쉬움 - 초보자용)';
        mapTag.className = 'bg-emerald-950/90 border border-emerald-500 px-2 py-0.5 rounded text-[11px] font-bold text-emerald-300 shadow';
      }
    }

    // ==================== 팝업식 메뉴 토글 (100% 독립 드롭다운) ====================
    function togglePopup(e, id) {
      if (e) e.stopPropagation();
      const el = document.getElementById(id);
      if (!el) return;
      const isShow = el.classList.contains('show');
      closeAllPopups();
      if (!isShow) {
        el.classList.add('show');
      }
    }

    function closeAllPopups() {
      document.querySelectorAll('.koei-popup-window').forEach(w => w.classList.remove('show'));
    }

    document.addEventListener('click', function(e) {
      if (!e.target.closest('.menu-item-wrap')) {
        closeAllPopups();
      }
    });

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
      document.getElementById('prompt-text').innerText = `${p.id}. ${p.name} (${p.ruler})을 선택했습니다. 명령을 내리십시오.`;
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

      // 12군주 초상화 및 공손찬 얼굴 실시간 정확 매핑
      updateRulerPortraitDisplay(p.ruler);

      document.getElementById('rate-rice-sell').innerText = gameState.rates.riceSell;
      document.getElementById('rate-rice-buy').innerText = gameState.rates.riceBuy;
      document.getElementById('rate-crossbow').innerText = gameState.rates.crossbow;
      document.getElementById('rate-heavy-bow').innerText = gameState.rates.heavyBow;
      document.getElementById('rate-horse').innerText = gameState.rates.horse;

      
      // 🔥 우측 패널 하단 원클릭 침공 / 출진 버튼 동적 렌더링
      const actionContainer = document.getElementById('panel-action-btn-container');
      if (actionContainer) {
        if (p.ruler !== gameState.rulerName) {
          actionContainer.innerHTML = `
            <button onclick="openWarModal(${p.id})" class="w-full py-2 bg-gradient-to-r from-red-700 to-rose-700 hover:from-red-600 hover:to-rose-600 text-yellow-100 font-black text-xs rounded border-2 border-yellow-300 shadow flex items-center justify-center gap-1.5 animate-pulse">
              <span>⚔️</span> 이 적 영지 즉시 침공 (전쟁 개시!)
            </button>
          `;
        } else {
          actionContainer.innerHTML = `
            <button onclick="openWarTargetSelectModal()" class="w-full py-2 bg-gradient-to-r from-blue-800 to-indigo-800 hover:from-blue-700 hover:to-indigo-700 text-cyan-100 font-bold text-xs rounded border border-cyan-300 shadow flex items-center justify-center gap-1.5">
              <span>🚩</span> 인접 적 영지 침공 작전 개시
            </button>
          `;
        }
      }

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

    // ==================== 12대 군주 초상화 완벽 매핑 (공손찬 100% 반영) ====================
    function updateRulerPortraitDisplay(ruler) {
      const faceImg = document.getElementById('main-ruler-face');
      const nameText = document.getElementById('portrait-ruler-name');
      const statsText = document.getElementById('portrait-ruler-stats');
      const p = PORTRAITS;

      if (ruler === '공손찬') {
        faceImg.src = p['gongsongzan'] || p['liubei'];
        nameText.innerText = '군주 공손찬 (公孫瓚)';
        statsText.innerText = '통솔: 84 | 무력: 84 | 백마의종';
      } else if (ruler === '유비') {
        faceImg.src = p['liubei_direct'] || p['liubei'];
        nameText.innerText = '군주 유비 (劉備)';
        statsText.innerText = '매력: 99 | 통솔: 78 | 덕망';
      } else if (ruler === '조조') {
        faceImg.src = p['caocao_retro'] || p['caocao'] || p['liubei'];
        nameText.innerText = '군주 조조 (曹操)';
        statsText.innerText = '통솔: 96 | 지력: 94 | 패도';
      } else if (ruler === '원소') {
        faceImg.src = p['yuanshao_retro'] || p['yuanshao'] || p['liubei'];
        nameText.innerText = '군주 원소 (袁紹)';
        statsText.innerText = '명망: 92 | 통솔: 80 | 하북맹주';
      } else if (ruler === '손책' || ruler === '손권') {
        faceImg.src = p['sunce'] || p['sunquan'] || p['liubei'];
        nameText.innerText = `군주 ${ruler} (孫氏)`;
        statsText.innerText = '무력: 92 | 통솔: 92 | 소패왕';
      } else if (ruler === '마등') {
        faceImg.src = p['mateng_retro'] || p['mateng'] || p['liubei'];
        nameText.innerText = '군주 마등 (馬騰)';
        statsText.innerText = '무력: 82 | 통솔: 84 | 서량기병';
      } else if (ruler === '유표') {
        faceImg.src = p['liubiao_retro'] || p['liubiao'] || p['liubei'];
        nameText.innerText = '군주 유표 (劉表)';
        statsText.innerText = '매력: 85 | 통솔: 70 | 형주자사';
      } else if (ruler === '원술') {
        faceImg.src = p['yuanshu'] || p['liubei'];
        nameText.innerText = '군주 원술 (袁術)';
        statsText.innerText = '야망: 95 | 통솔: 65 | 중씨황제';
      } else if (ruler === '여포') {
        faceImg.src = p['lubu'] || p['liubei'];
        nameText.innerText = '군주 여포 (呂布)';
        statsText.innerText = '무력: 100 | 천하무쌍 비장';
      } else if (ruler === '장노') {
        faceImg.src = p['zhanglu'] || p['liubei'];
        nameText.innerText = '군주 장노 (張魯)';
        statsText.innerText = '신망: 84 | 오두미교 교주';
      } else if (ruler === '공융') {
        faceImg.src = p['gongyong'] || p['liubei'];
        nameText.innerText = '군주 공융 (孔融)';
        statsText.innerText = '학식: 92 | 북해상 명사';
      } else if (ruler === '유요') {
        faceImg.src = p['liuyao'] || p['liubei'];
        nameText.innerText = '군주 유요 (劉繇)';
        statsText.innerText = '통솔: 68 | 양주자사';
      } else {
        faceImg.src = p['liubei_direct'] || p['liubei'];
        nameText.innerText = `군주 ${ruler}`;
        statsText.innerText = '통솔: 75 | 무력: 75';
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

    // ==================== 0. 휴양 (턴 넘김 & 난이도별 침공 시뮬레이션) ====================
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

      const seasonStr = `${curIcon} ${gameState.year}년 ${gameState.month}월 (${curSeason})`;
      document.getElementById('season-text').innerText = seasonStr;
      document.getElementById('weather-text').innerText = curWeather;
      document.getElementById('prompt-date').innerText = `${gameState.year}년 ${curSeason} ${gameState.month}월`;

      // 난이도별 군량 소모 가중치 (상: 0.07, 중: 0.05, 하: 0.03)
      let foodFactor = 0.05;
      if (gameState.difficulty === 'hard') foodFactor = 0.07;
      if (gameState.difficulty === 'easy') foodFactor = 0.03;

      PROVINCES.forEach(p => {
        if (p.ruler === gameState.rulerName) {
          p.food = Math.max(0, p.food - Math.floor(p.soldiers * foodFactor));
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
        } else {
          const bonus = (gameState.difficulty === 'hard') ? 800 : 400;
          p.soldiers = Math.min(50000, p.soldiers + Math.floor(Math.random() * 1000) + bonus);
          p.gold = Math.min(9000, p.gold + 300);
          p.food = Math.min(80000, p.food + 2500);
        }
      });

      logMessage(`⌛ [휴양] ${gameState.year}년 ${gameState.month}월로 턴이 넘어갔습니다.`, 'text-yellow-200');

      // 🔥 적 군벌들의 활기찬 상호 침공 및 아군 침공 시뮬레이션!
      simulateAIBattles();

      renderMapPins();
      updateRightPanel(gameState.selectedProvId);
    }

    // ==================== 🔥 적군 AI 침공 (난이도 상·중·하 정밀 연동) ====================
    function simulateAIBattles() {
      const warlords = ['조조', '원소', '손책', '마등', '공손찬', '여포', '유표', '원술'];
      
      let attackChance = 0.60;
      let targetPlayerWeight = 0.40;
      if (gameState.difficulty === 'hard') {
        attackChance = 0.85; // 상급: 매 턴 다발적 공격!
        targetPlayerWeight = 0.65; // 플레이어 집중 표적!
      } else if (gameState.difficulty === 'easy') {
        attackChance = 0.30;
        targetPlayerWeight = 0.15;
      }

      const activeAttackers = warlords.filter(() => Math.random() < attackChance);
      if (activeAttackers.length === 0 && gameState.difficulty === 'hard') {
        activeAttackers.push(warlords[Math.floor(Math.random() * warlords.length)]);
      }

      activeAttackers.forEach(attackerRuler => {
        const myProvs = PROVINCES.filter(p => p.ruler === attackerRuler && p.soldiers >= 7000);
        if (myProvs.length === 0) return;

        myProvs.sort((a, b) => b.soldiers - a.soldiers);
        const fromProv = myProvs[0];

        const targetProvs = PROVINCES.filter(p => fromProv.adj.includes(p.id) && p.ruler !== attackerRuler);
        if (targetProvs.length === 0) return;

        let targetProv = null;
        const playerProvTarget = targetProvs.find(p => p.ruler === gameState.rulerName);
        if (playerProvTarget && Math.random() < targetPlayerWeight) {
          targetProv = playerProvTarget;
        } else {
          targetProvs.sort((a, b) => (a.soldiers + a.defense * 80) - (b.soldiers + b.defense * 80));
          targetProv = targetProvs[0];
        }

        // 아군 영지 피습 시 ➔ 긴급 경보 모달 트리거!
        if (targetProv.ruler === gameState.rulerName) {
          const invasionForce = Math.floor(fromProv.soldiers * 0.4);
          fromProv.soldiers -= invasionForce;

          pendingInvasion = {
            attackerRuler: attackerRuler,
            fromProv: fromProv,
            targetProv: targetProv,
            invasionForce: invasionForce
          };

          // 침공 알림 모달 노출!
          document.getElementById('invasion-alert-msg').innerText = `🚨 [적군 침공!] ${attackerRuler}군 ${invasionForce.toLocaleString()}명이 아군 영지 '${targetProv.name}'으로 노도와 같이 진격해왔습니다!`;
          playSfx('war');
          openModal('invasion-alert-modal');
          logMessage(`🚨 [적군 침공 경보!] ${attackerRuler}군 ${invasionForce.toLocaleString()}명이 아군 영지 ${targetProv.name}을 급습했습니다!!`, 'text-red-400 font-black animate-pulse');
          return;
        }

        // 적들끼리의 상호 공격!
        const attackSoldiers = Math.floor(fromProv.soldiers * 0.4);
        fromProv.soldiers -= Math.floor(attackSoldiers * 0.4);

        const defPower = targetProv.soldiers + (targetProv.defense * 120);
        const attPower = attackSoldiers * (0.85 + Math.random() * 0.4);

        if (attPower > defPower * 1.05) {
          const oldRuler = targetProv.ruler;
          targetProv.ruler = attackerRuler;
          targetProv.soldiers = Math.floor(attackSoldiers * 0.6);
          targetProv.defense = Math.max(25, Math.floor(targetProv.defense * 0.6));
          targetProv.loyalty = 60;
          logMessage(`🔥 [천하 격변 속보!] ${attackerRuler}군이 ${oldRuler}의 ${targetProv.name}을 전격 함락하고 영지를 병합했습니다!`, 'text-yellow-300 font-black');
        } else {
          targetProv.soldiers = Math.max(2000, targetProv.soldiers - Math.floor(attackSoldiers * 0.3));
          targetProv.defense = Math.max(20, targetProv.defense - 4);
          logMessage(`⚔️ [전황 속보] ${attackerRuler}군이 ${targetProv.ruler}의 ${targetProv.name}을 공략했으나 견고한 수비벽에 막혀 퇴각했습니다.`, 'text-slate-300');
        }
      });
    }

    // 아군 침공 요격 처리
    function handleInvasionDuel() {
      closeModal('invasion-alert-modal');
      openDuelSelectModal();
      logMessage('⚔️ [장수 출진 요격] 적장을 1:1로 격파하여 침공군을 와해시키기 위해 결투를 개시합니다!', 'text-yellow-300 font-bold');
    }

    function handleInvasionDefend() {
      closeModal('invasion-alert-modal');
      if (!pendingInvasion) return;
      const { attackerRuler, targetProv, invasionForce } = pendingInvasion;
      
      const defensePower = targetProv.soldiers + (targetProv.defense * 140);
      if (defensePower >= invasionForce * 1.15) {
        const enemyCasualty = Math.floor(invasionForce * 0.6);
        const myCasualty = Math.floor(invasionForce * 0.15);
        targetProv.soldiers = Math.max(1000, targetProv.soldiers - myCasualty);
        targetProv.defense = Math.max(15, targetProv.defense - 5);
        playSfx('victory');
        logMessage(`🛡️ [아군 수성 대승!] ${targetProv.name}의 ${targetProv.leader} 장군이 결사항전하여 ${attackerRuler}군을 패퇴시켰습니다! (적 사상: ${enemyCasualty.toLocaleString()}명)`, 'text-emerald-300 font-extrabold');
        alert(`🛡️ [수성 대승!]\n${targetProv.name}의 성벽을 사수하여 ${attackerRuler}군의 공세를 물리쳤습니다!`);
      } else {
        const myLoss = Math.floor(targetProv.soldiers * 0.35);
        targetProv.soldiers = Math.max(500, targetProv.soldiers - myLoss);
        targetProv.defense = Math.max(10, targetProv.defense - 15);
        gameState.storageHp = Math.max(15, gameState.storageHp - 18);
        playSfx('war');
        logMessage(`⚠️ [영지 피해] ${attackerRuler}군의 맹공으로 ${targetProv.name}의 성벽이 파손되고 병사 ${myLoss.toLocaleString()}명을 잃었습니다! (창고 보수 요망)`, 'text-orange-400 font-bold');
        alert(`⚠️ [수성 피해 발생!]\n${attackerRuler}군의 파상 공세로 성벽과 창고가 파손되었습니다! [창고 보수]를 수행하십시오.`);
      }
      pendingInvasion = null;
      updateRightPanel(targetProv.id);
    }

    // ==================== 1:1 장수 전략 결투 (일기토) 시스템 ====================
    let selectedMyOfficerIdx = 0;

    function openDuelSelectModal() {
      closeAllPopups();
      const myContainer = document.getElementById('duel-my-officer-list');
      myContainer.innerHTML = '';
      MY_OFFICERS.forEach((off, idx) => {
        const item = document.createElement('div');
        item.className = `p-2 rounded border cursor-pointer text-xs flex flex-col justify-between transition ${idx === selectedMyOfficerIdx ? 'bg-amber-900 border-yellow-300 ring-2 ring-yellow-400' : 'bg-blue-900/60 border-blue-600 hover:bg-blue-800'}`;
        item.innerHTML = `
          <div class="flex items-center gap-1 font-bold text-white">
            <span>${off.icon}</span>
            <span>${off.name}</span>
          </div>
          <div class="text-[11px] text-yellow-300 mt-1">무력: <strong>${off.war}</strong> | 지력: ${off.int}</div>
          <div class="text-[10px] text-slate-300">${off.title}</div>
        `;
        item.onclick = () => {
          selectedMyOfficerIdx = idx;
          openDuelSelectModal();
        };
        myContainer.appendChild(item);
      });

      const provSelect = document.getElementById('duel-enemy-prov-select');
      provSelect.innerHTML = '';
      const enemies = PROVINCES.filter(p => p.ruler !== gameState.rulerName);
      enemies.forEach(p => {
        const opt = document.createElement('option');
        opt.value = p.id;
        opt.innerText = `${p.id}. ${p.name} (${p.ruler}령)`;
        provSelect.appendChild(opt);
      });

      updateEnemyOfficersList();
      openModal('duel-select-modal');
    }

    function updateEnemyOfficersList() {
      const provSelect = document.getElementById('duel-enemy-prov-select');
      const offSelect = document.getElementById('duel-enemy-officer-select');
      offSelect.innerHTML = '';
      const provId = parseInt(provSelect.value, 10);
      const prov = PROVINCES.find(p => p.id === provId);
      if (!prov) return;

      const list = ENEMY_OFFICERS_BY_RULER[prov.ruler] || [
        { name: prov.leader, war: 80, int: 70, lead: 80, icon: '⚔️', title: '영지 수비장군' }
      ];

      list.forEach((off, i) => {
        const opt = document.createElement('option');
        opt.value = i;
        opt.innerText = `${off.name} (무력 ${off.war} / 지력 ${off.int})`;
        offSelect.appendChild(opt);
      });
    }

    function startDuelFight() {
      closeModal('duel-select-modal');
      const provSelect = document.getElementById('duel-enemy-prov-select');
      const offSelect = document.getElementById('duel-enemy-officer-select');
      const provId = parseInt(provSelect.value, 10);
      const prov = PROVINCES.find(p => p.id === provId);

      const myOff = MY_OFFICERS[selectedMyOfficerIdx];
      const list = ENEMY_OFFICERS_BY_RULER[prov.ruler] || [
        { name: prov.leader, war: 80, int: 70, lead: 80, icon: '⚔️', title: '영지 수비장군' }
      ];
      const enemyOff = list[parseInt(offSelect.value, 10) || 0];

      duelState.round = 1;
      duelState.myOfficer = myOff;
      duelState.enemyOfficer = enemyOff;
      duelState.myHp = 100;
      duelState.enemyHp = 100;
      duelState.enemyConfused = false;
      duelState.inDuel = true;

      // 상급 난이도 시 적장 보정
      const enemyWar = (gameState.difficulty === 'hard') ? enemyOff.war + 10 : enemyOff.war;
      const enemyInt = (gameState.difficulty === 'hard') ? enemyOff.int + 8 : enemyOff.int;

      document.getElementById('duel-round-badge').innerText = '제 1 합';
      document.getElementById('duel-my-name').innerText = myOff.name;
      document.getElementById('duel-my-icon').innerText = myOff.icon;
      document.getElementById('duel-my-stats').innerText = `무력: ${myOff.war} | 지력: ${myOff.int}`;
      document.getElementById('duel-my-hp-txt').innerText = '100 / 100';
      document.getElementById('duel-my-hp-bar').style.width = '100%';

      document.getElementById('duel-enemy-name').innerText = enemyOff.name;
      document.getElementById('duel-enemy-stats').innerText = `무력: ${enemyWar} | 지력: ${enemyInt}`;
      document.getElementById('duel-enemy-hp-txt').innerText = '100 / 100';
      document.getElementById('duel-enemy-hp-bar').style.width = '100%';

      const enemyImg = document.getElementById('duel-enemy-img');
      const enemyIcon = document.getElementById('duel-enemy-icon');
      if (enemyOff.faceKey && PORTRAITS[enemyOff.faceKey]) {
        enemyImg.src = PORTRAITS[enemyOff.faceKey];
        enemyImg.classList.remove('hidden');
        enemyIcon.classList.add('hidden');
      } else {
        enemyImg.classList.add('hidden');
        enemyIcon.classList.remove('hidden');
        enemyIcon.innerText = enemyOff.icon || '👹';
      }

      const log = document.getElementById('duel-combat-log');
      log.innerHTML = `
        <div class="text-yellow-300 font-extrabold">🚩 [일기토 개전] ${myOff.name} vs ${enemyOff.name}!</div>
        <div class="text-cyan-200">두 장수가 창검을 맞부딪치며 제 1합의 공방에 돌입합니다! (${gameState.difficulty === 'hard' ? '🔥 상급 적장 무력/지력 보정 적용' : '표준 대결'})</div>
      `;

      playSfx('war');
      openModal('duel-modal');
    }

    function logDuel(msg, colorClass='text-slate-200') {
      const container = document.getElementById('duel-combat-log');
      if (!container) return;
      const d = document.createElement('div');
      d.className = colorClass;
      d.innerHTML = msg;
      container.appendChild(d);
      container.scrollTop = container.scrollHeight;
    }

    function duelAction(type) {
      if (!duelState.inDuel) return;
      const my = duelState.myOfficer;
      const enemy = duelState.enemyOfficer;

      duelState.round++;
      document.getElementById('duel-round-badge').innerText = `제 ${duelState.round} 합`;

      const enemyWar = (gameState.difficulty === 'hard') ? enemy.war + 10 : enemy.war;
      const enemyInt = (gameState.difficulty === 'hard') ? enemy.int + 8 : enemy.int;

      const enemyActions = ['attack', 'heavy', 'defend'];
      if (enemyInt >= 70) enemyActions.push('tactic');
      const enemyChoice = enemyActions[Math.floor(Math.random() * enemyActions.length)];

      let myDmg = 0;
      let enemyDmg = 0;

      // 1. 플레이어 행동 판정
      if (type === 'quick') {
        playTone(480, 0.12, 'sawtooth', 0.2);
        const hit = Math.random() < 0.90;
        if (hit) {
          myDmg = Math.floor((my.war * 0.22) + Math.random() * 10);
          logDuel(`⚔️ [쾌속 공격] ${my.name}의 정교한 공격 적중! (${enemy.name}에게 ${myDmg} 피해)`, 'text-yellow-300 font-bold');
        } else {
          logDuel(`💨 ${my.name}의 공격을 ${enemy.name}이 쳐냈습니다!`, 'text-slate-400');
        }
      } else if (type === 'smash') {
        playTone(320, 0.25, 'sawtooth', 0.3);
        const hit = Math.random() < 0.65;
        if (hit) {
          myDmg = Math.floor((my.war * 0.45) + Math.random() * 15);
          logDuel(`⚡ [필살 일격 작렬!] ${my.name}의 혼신의 일격이 적장의 갑주를 쪼갰습니다!! (${enemy.name}에게 ${myDmg} 치명타!)`, 'text-red-400 font-black animate-pulse');
        } else {
          logDuel(`💨 [필살 실패] ${my.name}의 큰 기술이 빗나가며 틈을 보였습니다!`, 'text-orange-400');
        }
      } else if (type === 'defend') {
        playTone(600, 0.1, 'sine', 0.15);
        logDuel(`🛡️ [철벽 방어] ${my.name}이 방패와 칼날로 방어 태세를 굳혔습니다!`, 'text-cyan-300 font-bold');
      } else if (type === 'tactic') {
        playTone(720, 0.15, 'triangle', 0.2);
        const diff = my.int - enemyInt;
        const success = Math.random() * 100 < (50 + diff);
        if (success) {
          duelState.enemyConfused = true;
          myDmg = 22;
          logDuel(`🧠 [심리 도발 성공!] ${my.name}의 호통에 ${enemy.name}이 혼란에 빠졌습니다! (혼란 피해 22)`, 'text-purple-300 font-black');
        } else {
          logDuel(`🗣️ 도발 실패! ${enemy.name}이 냉소를 머금고 반격합니다.`, 'text-slate-400');
        }
      } else if (type === 'flee') {
        duelState.inDuel = false;
        logDuel(`🐎 [퇴각] ${my.name}이 말머리를 돌려 본진으로 무사히 철수했습니다.`, 'text-slate-300 font-bold');
        logMessage(`🐎 [일기토 퇴각] ${my.name}이 부상을 입지 않고 무사히 귀환했습니다.`, 'text-slate-300');
        setTimeout(() => closeModal('duel-modal'), 1200);
        return;
      }

      // 2. 적 장수 행동 판정
      if (duelState.enemyConfused) {
        logDuel(`😵 [적 혼란] ${enemy.name}은 정신이 혼미하여 행동하지 못했습니다!`, 'text-purple-400');
        duelState.enemyConfused = false;
      } else {
        if (enemyChoice === 'heavy') {
          if (type === 'defend') {
            const counter = 18;
            myDmg += counter;
            logDuel(`🛡️⚡ [완벽한 방어 & 반격!] ${my.name}이 적장의 강타를 튕겨내며 ${counter}의 반격 피해를 입혔습니다!`, 'text-emerald-300 font-black');
          } else {
            enemyDmg = Math.floor((enemyWar * 0.38) + Math.random() * 12);
            logDuel(`💥 [적장의 맹공!] ${enemy.name}의 묵직한 칼날이 들이닥쳤습니다! (${my.name}에게 ${enemyDmg} 피해)`, 'text-red-400 font-bold');
          }
        } else if (enemyChoice === 'attack') {
          if (type === 'defend') {
            enemyDmg = Math.floor(((enemyWar * 0.22) + Math.random() * 5) * 0.3);
            logDuel(`🛡️ [피해 경감] 적의 공격을 방패로 막아내어 피해를 ${enemyDmg}로 최소화했습니다.`, 'text-cyan-300');
          } else {
            enemyDmg = Math.floor((enemyWar * 0.22) + Math.random() * 8);
            logDuel(`⚔️ ${enemy.name}의 검격! (${my.name}에게 ${enemyDmg} 피해)`, 'text-slate-300');
          }
        } else if (enemyChoice === 'defend') {
          logDuel(`🛡️ ${enemy.name}이 뒤로 물러나며 방어 태세를 취했습니다.`, 'text-slate-400');
          myDmg = Math.floor(myDmg * 0.5);
        } else {
          logDuel(`🗣️ ${enemy.name}: '네놈의 목숨줄도 오늘이 끝이다!'`, 'text-red-300');
        }
      }

      duelState.enemyHp = Math.max(0, duelState.enemyHp - myDmg);
      duelState.myHp = Math.max(0, duelState.myHp - enemyDmg);

      document.getElementById('duel-enemy-hp-txt').innerText = `${duelState.enemyHp} / 100`;
      document.getElementById('duel-enemy-hp-bar').style.width = `${duelState.enemyHp}%`;
      document.getElementById('duel-my-hp-txt').innerText = `${duelState.myHp} / 100`;
      document.getElementById('duel-my-hp-bar').style.width = `${duelState.myHp}%`;

      if (duelState.enemyHp <= 0) {
        duelState.inDuel = false;
        playSfx('victory');
        logDuel(`🎉🏆 [일기토 완전 승리!] ${my.name}이 ${enemy.name}을 말 아래로 낙마시키고 생포했습니다!!`, 'text-yellow-300 font-extrabold text-sm');
        logMessage(`👑 [일기토 대승] ${my.name}이 적장 ${enemy.name}과의 결투에서 대승을 거두었습니다! (금 500전 노획)`, 'text-yellow-300 font-black');

        if (battleData.targetProv) {
          logMessage(`🚩 [영지 점령] 적장이 일기토에서 격파되어 적군이 총붕괴했습니다! ${battleData.targetProv.name}을 점령했습니다!`, 'text-yellow-300 font-black');
          alert(`🎉🏆 [일기토 대승리!]
${my.name}이 적장 ${enemy.name}을 베어 적군이 총붕괴하고 패주했습니다!
${battleData.targetProv.name}을 완전히 점령하여 아군 영지로 편입했습니다!`);
          endBattleVictory();
        } else {
          const myProv = getMyCapital();
          myProv.gold += 500;
          updateRightPanel(myProv.id);
          alert(`🎉 [일기토 승리] ${my.name}이 적장 ${enemy.name}을 격파했습니다!
적군의 사기가 곤두박질치고 군자금 500전을 전리품으로 획득했습니다!
(다음 장수를 골라 또 대결할 수 있습니다)`);
        }
        setTimeout(() => closeModal('duel-modal'), 1800);
      } else if (duelState.myHp <= 0) {
        duelState.inDuel = false;
        logDuel(`💀 [패배] ${my.name}이 부상을 입고 휘하 장졸들의 호위를 받으며 긴급 철수했습니다!`, 'text-red-500 font-black');
        logMessage(`⚠️ [일기토 패배] ${my.name}이 결투 중 부상을 입고 후퇴했습니다.`, 'text-red-400');
        alert(`⚠️ ${my.name}이 부상을 입고 후퇴했습니다! 다른 장수를 골라 재도전하십시오.`);
        setTimeout(() => closeModal('duel-modal'), 1800);
      }
    }

    // ==================== 5대 세이브 슬롯 (저장 & 로드 & 날짜/제목) ====================
    function getSlotKey(slot) { return `samguk3_slot_${slot}`; }

    function getFormattedCurrentDate() {
      const now = new Date();
      const pad = n => String(n).padStart(2, '0');
      return `${now.getFullYear()}-${pad(now.getMonth()+1)}-${pad(now.getDate())} ${pad(now.getHours())}:${pad(now.getMinutes())}:${pad(now.getSeconds())}`;
    }

    function openSaveModal() {
      closeAllPopups();
      selectedSaveSlot = 1;
      renderSaveSlots();
      updateSaveTitleDefault();
      openModal('save-modal');
    }

    function renderSaveSlots() {
      const container = document.getElementById('save-slots-container');
      container.innerHTML = '';

      for (let s = 1; s <= 5; s++) {
        const raw = localStorage.getItem(getSlotKey(s));
        const data = raw ? JSON.parse(raw) : null;
        const isSelected = (s === selectedSaveSlot);

        const card = document.createElement('div');
        card.className = `p-3 rounded border-2 cursor-pointer transition flex items-center justify-between ${isSelected ? 'bg-emerald-950 border-yellow-400 ring-2 ring-yellow-400' : 'bg-blue-950/70 border-blue-700 hover:bg-blue-900/60'}`;
        card.onclick = () => {
          selectedSaveSlot = s;
          document.getElementById('selected-save-slot-label').innerText = `슬롯 ${s}`;
          renderSaveSlots();
          updateSaveTitleDefault();
        };

        if (data) {
          card.innerHTML = `
            <div class="flex-1">
              <div class="flex items-center gap-2">
                <span class="px-2 py-0.5 bg-emerald-800 text-yellow-200 font-black rounded text-[11px] border border-yellow-300">슬롯 ${s}</span>
                <span class="font-extrabold text-white text-xs text-pixel tracking-wide">${data.title}</span>
                <span class="text-[10px] bg-red-900 text-yellow-200 px-1.5 py-0.2 rounded border border-red-500 font-bold">${data.difficulty ? data.difficulty.toUpperCase() : 'HARD'}</span>
              </div>
              <div class="text-[11px] text-cyan-300 mt-1">🕒 저장 일시: <strong>${data.savedRealTime}</strong></div>
              <div class="text-[10px] text-slate-300">📅 게임 시점: ${data.gameDate} | 군주: ${data.ruler} (영지 ${data.territoriesCount}개) | 병사: ${data.soldiers.toLocaleString()}명</div>
            </div>
            <div class="text-right pl-2">
              <span class="text-xs text-yellow-300 font-bold bg-blue-900 px-2 py-1 rounded border border-blue-500">선택됨</span>
            </div>
          `;
        } else {
          card.innerHTML = `
            <div class="flex-1">
              <div class="flex items-center gap-2">
                <span class="px-2 py-0.5 bg-slate-800 text-slate-300 font-bold rounded text-[11px] border border-slate-600">슬롯 ${s}</span>
                <span class="font-bold text-slate-400 text-xs">[ 빈 슬롯 - 새로운 데이터 저장 가능 ]</span>
              </div>
              <div class="text-[11px] text-slate-500 mt-1">저장된 기록이 없습니다.</div>
            </div>
            <div class="text-right pl-2">
              <span class="text-xs text-slate-400">비어있음</span>
            </div>
          `;
        }
        container.appendChild(card);
      }
    }

    function updateSaveTitleDefault() {
      const input = document.getElementById('save-title-input');
      const myProv = getMyCapital();
      input.value = `${gameState.year}년 ${gameState.month}월 - ${gameState.rulerName}의 ${myProv.name} 평정기 (${gameState.difficulty.toUpperCase()})`;
      document.getElementById('selected-save-slot-label').innerText = `슬롯 ${selectedSaveSlot}`;
    }

    function confirmSaveSlot() {
      const input = document.getElementById('save-title-input');
      const title = input.value.trim() || `${gameState.year}년 ${gameState.month}월 세이브`;
      const myProv = getMyCapital();
      const myProvsCount = PROVINCES.filter(p => p.ruler === gameState.rulerName).length;

      const saveData = {
        slotId: selectedSaveSlot,
        title: title,
        savedRealTime: getFormattedCurrentDate(),
        gameDate: `${gameState.year}년 ${gameState.month}월`,
        difficulty: gameState.difficulty,
        ruler: gameState.rulerName,
        territoriesCount: myProvsCount,
        gold: myProv.gold,
        food: myProv.food,
        soldiers: myProv.soldiers,
        gameState: gameState,
        provinces: PROVINCES
      };

      localStorage.setItem(getSlotKey(selectedSaveSlot), JSON.stringify(saveData));
      playSfx('build');
      logMessage(`💾 [슬롯 ${selectedSaveSlot} 저장 완료] "${title}" (일시: ${saveData.savedRealTime})`, 'text-emerald-300 font-bold');
      alert(`💾 [슬롯 ${selectedSaveSlot} 저장 완료]\n제목: ${title}\n저장일시: ${saveData.savedRealTime}`);
      closeModal('save-modal');
    }

    function openLoadModal() {
      closeAllPopups();
      renderLoadSlots();
      openModal('load-modal');
    }

    function renderLoadSlots() {
      const container = document.getElementById('load-slots-container');
      container.innerHTML = '';

      for (let s = 1; s <= 5; s++) {
        const raw = localStorage.getItem(getSlotKey(s));
        const data = raw ? JSON.parse(raw) : null;

        const card = document.createElement('div');
        card.className = 'p-3 rounded border-2 bg-blue-950/80 border-blue-700 flex items-center justify-between gap-2';

        if (data) {
          card.innerHTML = `
            <div class="flex-1">
              <div class="flex items-center gap-2">
                <span class="px-2 py-0.5 bg-cyan-800 text-cyan-100 font-black rounded text-[11px] border border-cyan-400">슬롯 ${s}</span>
                <span class="font-black text-yellow-300 text-sm text-pixel">${data.title}</span>
                <span class="text-[10px] bg-red-900 text-yellow-200 px-1.5 py-0.2 rounded border border-red-500 font-bold">${data.difficulty ? data.difficulty.toUpperCase() : 'HARD'}</span>
              </div>
              <div class="text-[11px] text-cyan-200 mt-1">🕒 저장 일시: <strong class="text-white">${data.savedRealTime}</strong></div>
              <div class="text-[11px] text-slate-300 mt-0.5">📅 게임 시점: ${data.gameDate} | 군주: <strong>${data.ruler}</strong> (영지 ${data.territoriesCount}개)</div>
              <div class="text-[10px] text-amber-300">자원: 금 ${data.gold.toLocaleString()}전 | 군량 ${data.food.toLocaleString()}석 | 병사 ${data.soldiers.toLocaleString()}명</div>
            </div>
            <div class="flex items-center gap-1.5">
              <button onclick="confirmLoadSlot(${s})" class="px-3 py-1.5 bg-cyan-700 hover:bg-cyan-600 text-white font-extrabold rounded text-xs border border-cyan-300 shadow">
                📂 불러오기
              </button>
              <button onclick="deleteSlot(${s})" class="px-2 py-1.5 bg-red-900 hover:bg-red-800 text-red-200 rounded text-xs border border-red-600">
                🗑️
              </button>
            </div>
          `;
        } else {
          card.innerHTML = `
            <div class="flex-1 opacity-60">
              <div class="flex items-center gap-2">
                <span class="px-2 py-0.5 bg-slate-800 text-slate-400 font-bold rounded text-[11px] border border-slate-600">슬롯 ${s}</span>
                <span class="text-slate-400 text-xs">[ 빈 슬롯 - 저장된 데이터 없음 ]</span>
              </div>
              <div class="text-[11px] text-slate-500 mt-1">-</div>
            </div>
            <div>
              <span class="text-xs text-slate-500 px-3 py-1 border border-slate-700 rounded bg-slate-900">비어있음</span>
            </div>
          `;
        }
        container.appendChild(card);
      }
    }

    function confirmLoadSlot(slot) {
      const raw = localStorage.getItem(getSlotKey(slot));
      if (!raw) return;
      try {
        const saved = JSON.parse(raw);
        gameState = saved.gameState;
        for (let i = 0; i < saved.provinces.length; i++) {
          Object.assign(PROVINCES[i], saved.provinces[i]);
        }
        renderMapPins();
        updateRightPanel(gameState.selectedProvId);
        updateDifficultyUI();
        playSfx('rest');
        logMessage(`📂 [슬롯 ${slot} 로드 완료] "${saved.title}" (저장일시: ${saved.savedRealTime})`, 'text-cyan-300 font-extrabold');
        alert(`📂 [슬롯 ${slot} 불러오기 성공!]\n제목: ${saved.title}\n저장일시: ${saved.savedRealTime}\n군주: ${saved.ruler} | ${saved.gameDate}`);
        closeModal('load-modal');
      } catch (e) {
        alert('데이터 복원 실패: ' + e.message);
      }
    }

    function deleteSlot(slot) {
      if (confirm(`정말로 슬롯 ${slot}번의 저장 데이터를 영구 삭제하시겠습니까?`)) {
        localStorage.removeItem(getSlotKey(slot));
        renderLoadSlots();
        logMessage(`🗑️ [슬롯 ${slot} 삭제] 세이브 데이터가 삭제되었습니다.`, 'text-slate-400');
      }
    }

    // ==================== 야전 결전 모달 ====================
    
    // ==================== 🔥 인접 적 영지 침공 및 전쟁 시스템 (완전 개편) ====================
    function openWarModal(targetProvId = null, fromProvId = null) {
      closeAllPopups();

      // 1. 공격 목표 적 영지 결정
      let target = null;
      if (targetProvId) {
        target = PROVINCES.find(p => p.id === targetProvId);
      } else {
        const sel = PROVINCES.find(p => p.id === gameState.selectedProvId);
        if (sel && sel.ruler !== gameState.rulerName) {
          target = sel; // 유저가 지도에서 적 영지를 선택해둔 상태!
        }
      }

      // 목표 적 영지가 아직 지정되지 않은 경우(아군 영지 선택 또는 전체 전쟁 클릭) 목록 모달 오픈!
      if (!target) {
        openWarTargetSelectModal();
        return;
      }

      // 아군 영지를 대상으로 공격하려 한 경우
      if (target.ruler === gameState.rulerName) {
        alert('아군 영지는 공격할 수 없습니다! 적의 영지를 선택하십시오.');
        openWarTargetSelectModal();
        return;
      }

      // 2. 이 적 영지와 국경이 맞닿아 있는(인접한) 아군 영지들 찾기
      const adjMyProvs = PROVINCES.filter(p => p.ruler === gameState.rulerName && target.adj.includes(p.id));

      if (adjMyProvs.length === 0) {
        alert(`[공격 불가] ${target.id}. ${target.name} (${target.ruler})은(는) 아군 영지와 국경이 맞닿아 있지 않아 직접 공격할 수 없습니다!\n국경을 맞대고 있는 인접 적 영지를 먼저 공략하십시오.`);
        openWarTargetSelectModal();
        return;
      }

      // 3. 출진할 아군 영지 결정
      let myProv = null;
      if (fromProvId) {
        myProv = adjMyProvs.find(p => p.id === fromProvId);
      }
      if (!myProv) {
        const sel = PROVINCES.find(p => p.id === gameState.selectedProvId);
        if (sel && adjMyProvs.some(p => p.id === sel.id)) {
          myProv = sel;
        } else {
          // 인접 아군 영지 중 병력이 가장 많은 곳에서 출진!
          myProv = adjMyProvs.slice().sort((a, b) => b.soldiers - a.soldiers)[0];
        }
      }

      if (myProv.soldiers < 100) {
        alert(`출진할 ${myProv.name}의 병사가 부족합니다! (최소 100명 이상 필요)`);
        return;
      }

      // 4. 전투 데이터 초기화
      battleData.targetProv = target;
      battleData.fromProv = myProv;
      battleData.turn = 1;
      battleData.myPower = 100;
      battleData.enemyPower = 100;
      battleData.mySoldiers = myProv.soldiers;
      battleData.enemySoldiers = target.soldiers;
      battleData.storageHp = gameState.storageHp;

      // 5. 모달 UI 바인딩
      document.getElementById('battle-title').innerText = `[야전 결전] ${myProv.name} ➔ ${target.name} (${gameState.rulerName}군 vs ${target.ruler}군)`;
      document.getElementById('battle-enemy-name').innerText = `⚔️ 적군 (${target.ruler} 수비군: ${target.name})`;
      document.getElementById('battle-enemy-def-tag').innerText = `성벽 방어력: ${target.defense}`;
      document.getElementById('battle-my-soldiers-txt').innerText = myProv.soldiers.toLocaleString();
      document.getElementById('battle-enemy-soldiers-txt').innerText = target.soldiers.toLocaleString();
      document.getElementById('battle-storage-pct').innerText = `${gameState.storageHp}%`;
      document.getElementById('battle-storage-bar').style.width = `${gameState.storageHp}%`;

      document.getElementById('battle-enemy-power-pct').innerText = '100%';
      document.getElementById('battle-enemy-bar').style.width = '100%';
      document.getElementById('battle-my-power-pct').innerText = '100%';
      document.getElementById('battle-my-bar').style.width = '100%';

      document.getElementById('battle-modal-logs').innerHTML = `
        <div class="text-yellow-300 font-bold">🚩 [출진 개시] ${myProv.name}의 아군 ${myProv.soldiers.toLocaleString()}명이 ${target.name}(${target.ruler}군)을 향해 진격을 개시했습니다!</div>
        <div class="text-cyan-200">⚔️ 상단의 [1:1 결투 개시]를 눌러 장수를 골라 적장과 1번씩 맞붙거나, 아래 [총공격]으로 적군을 격멸하십시오!</div>
      `;

      playSfx('war');
      openModal('battle-modal');
    }

    // 침공 목표 적 영지 목록 모달
    function openWarTargetSelectModal() {
      closeAllPopups();
      const myProvs = PROVINCES.filter(p => p.ruler === gameState.rulerName);

      const attackableEnemyProvs = [];
      PROVINCES.forEach(p => {
        if (p.ruler !== gameState.rulerName) {
          const adjMine = myProvs.filter(myP => p.adj.includes(myP.id));
          if (adjMine.length > 0) {
            attackableEnemyProvs.push({
              prov: p,
              fromList: adjMine
            });
          }
        }
      });

      if (attackableEnemyProvs.length === 0) {
        alert('인접한 적의 영지가 없습니다! 영지를 이동하거나 턴을 넘기십시오.');
        return;
      }

      const listEl = document.getElementById('war-target-list');
      if (listEl) {
        listEl.innerHTML = attackableEnemyProvs.map(item => {
          const p = item.prov;
          const fromNames = item.fromList.map(m => `${m.id}.${m.name}(${m.soldiers.toLocaleString()}명)`).join(', ');
          return `
            <div class="p-2.5 rounded bg-blue-950/90 border border-amber-500/60 flex items-center justify-between hover:border-yellow-300 transition shadow">
              <div class="space-y-0.5">
                <div class="flex items-center gap-2">
                  <span class="text-red-400 font-black text-sm">${p.id}. ${p.name}</span>
                  <span class="px-2 py-0.5 rounded text-xs bg-red-900 text-yellow-200 border border-red-500 font-bold">${p.ruler} 군벌</span>
                  <span class="text-xs text-slate-300">병력: <b class="text-yellow-300">${p.soldiers.toLocaleString()}</b>명</span>
                  <span class="text-xs text-slate-300">성벽: <b class="text-cyan-300">${p.defense}</b></span>
                </div>
                <div class="text-[11px] text-emerald-300">
                  🚩 출진 가능 아군 영지: ${fromNames}
                </div>
              </div>
              <button onclick="closeModal('war-target-modal'); openWarModal(${p.id});" class="px-3.5 py-1.5 rounded bg-red-700 hover:bg-red-600 text-yellow-100 font-black text-xs border border-yellow-300 shadow flex items-center gap-1 animate-pulse">
                <span>⚔️</span> 침공 출진!
              </button>
            </div>
          `;
        }).join('');
      }

      openModal('war-target-modal');
    }

    // 야전 중 장수 1:1 일기토 출진 연결
    function battleStartOfficerDuel() {
      if (!battleData.targetProv) return;
      // 일기토 모달에서 해당 적 영지 적장과 맞붙도록 설정
      openDuelSelectModal();
      const provSelect = document.getElementById('duel-enemy-prov-select');
      if (provSelect) {
        provSelect.value = battleData.targetProv.id;
        updateEnemyOfficersList();
      }
    }


    function battleActionAttack() {
      if (!battleData.targetProv) return;
      playTone(220, 0.2, 'sawtooth', 0.25);
      battleData.turn++;
      document.getElementById('battle-turn-count').innerText = `턴: ${battleData.turn} / 10`;

      const myDamage = Math.floor(Math.random() * 25) + 15;
      battleData.enemyPower = Math.max(0, battleData.enemyPower - myDamage);
      battleData.enemySoldiers = Math.floor(battleData.targetProv.soldiers * (battleData.enemyPower / 100));

      const enemyDmg = (gameState.difficulty === 'hard') ? Math.floor(Math.random() * 24) + 14 : Math.floor(Math.random() * 18) + 10;
      battleData.myPower = Math.max(0, battleData.myPower - enemyDmg);
      const myProv = getMyCapital();
      battleData.mySoldiers = Math.floor(myProv.soldiers * (battleData.myPower / 100));

      if (Math.random() < 0.35) {
        battleData.storageHp = Math.max(10, battleData.storageHp - 10);
        document.getElementById('battle-storage-pct').innerText = `${battleData.storageHp}%`;
        document.getElementById('battle-storage-bar').style.width = `${battleData.storageHp}%`;
      }

      document.getElementById('battle-enemy-power-pct').innerText = `${battleData.enemyPower}%`;
      document.getElementById('battle-enemy-bar').style.width = `${battleData.enemyPower}%`;
      document.getElementById('battle-enemy-soldiers-txt').innerText = battleData.enemySoldiers.toLocaleString();

      document.getElementById('battle-my-power-pct').innerText = `${battleData.myPower}%`;
      document.getElementById('battle-my-bar').style.width = `${battleData.myPower}%`;
      document.getElementById('battle-my-soldiers-txt').innerText = battleData.mySoldiers.toLocaleString();

      logBattleMsg(`⚔️ 아군 총공격! 적군에게 ${myDamage}% 타격 입힘 (적 병력 잔여: ${battleData.enemySoldiers.toLocaleString()})`, 'text-yellow-300');

      if (battleData.enemyPower <= 0) {
        endBattleVictory();
      } else if (battleData.myPower <= 0) {
        endBattleDefeat();
      }
    }

    function battleActionTrap() {
      playTone(440, 0.25, 'triangle', 0.2);
      const success = Math.random() < 0.75;
      if (success) {
        const dmg = Math.floor(Math.random() * 30) + 20;
        battleData.enemyPower = Math.max(0, battleData.enemyPower - dmg);
        document.getElementById('battle-enemy-power-pct').innerText = `${battleData.enemyPower}%`;
        document.getElementById('battle-enemy-bar').style.width = `${battleData.enemyPower}%`;
        logBattleMsg(`🔮 제갈량의 복병 함정 성공! 적군이 대혼란에 빠져 ${dmg}% 궤멸!`, 'text-cyan-300 font-bold');
        if (battleData.enemyPower <= 0) endBattleVictory();
      } else {
        logBattleMsg(`⚠️ 적군이 매복을 간파하고 우회하였습니다!`, 'text-orange-400');
      }
    }

    function battleActionRaidStorage() {
      playTone(330, 0.2, 'sawtooth', 0.2);
      logBattleMsg(`🌾 적의 군량 수송대를 기습하여 적군 사기를 꺾었습니다!`, 'text-emerald-300 font-bold');
      battleData.enemyPower = Math.max(0, battleData.enemyPower - 20);
      document.getElementById('battle-enemy-power-pct').innerText = `${battleData.enemyPower}%`;
      document.getElementById('battle-enemy-bar').style.width = `${battleData.enemyPower}%`;
      if (battleData.enemyPower <= 0) endBattleVictory();
    }

    function endBattleVictory() {
      playSfx('victory');
      const target = battleData.targetProv;
      target.ruler = gameState.rulerName;
      target.leader = '관우';
      target.defense = 50;

      alert(`🎉 대승리! ${target.name}을 완전히 점령하여 본거지로 편입했습니다!`);
      logMessage(`👑 [점령 성공] ${target.name}을 정복하여 아군 영지가 되었습니다!`, 'text-yellow-300 font-black');
      closeModal('battle-modal');
      renderMapPins();
      updateRightPanel(target.id);
      checkUnification();
    }

    function endBattleDefeat() {
      alert('💀 아군 병력이 궤멸되어 퇴각하였습니다!');
      logMessage(`💀 [패전] 전투에서 패배하여 후퇴했습니다.`, 'text-red-400');
      closeModal('battle-modal');
      updateRightPanel(gameState.selectedProvId);
    }

    function retreatFromBattleModal() {
      if (confirm('전투에서 퇴각하시겠습니까?')) {
        closeModal('battle-modal');
        logMessage('🏳️ 군대를 수습하여 본진으로 퇴각하였습니다.', 'text-slate-400');
      }
    }

    function logBattleMsg(msg, colorClass) {
      const container = document.getElementById('battle-modal-logs');
      const div = document.createElement('div');
      div.className = colorClass;
      div.innerHTML = msg;
      container.appendChild(div);
      container.scrollTop = container.scrollHeight;
    }

    // ==================== 4. 정보 정찰 (금 100) ====================
    function openInfoModal() {
      closeAllPopups();
      const myProv = getMyCapital();
      if (myProv.gold < 100) {
        alert('정보 첩보를 입수하려면 금 100전이 필요합니다.');
        return;
      }
      playSfx('build');
      myProv.gold -= 100;
      updateRightPanel(myProv.id);
      renderInfoTable('sol');
      openModal('info-modal');
      logMessage('🔍 [정보 첩보] 금 100전을 들여 천하 13주의 최신 군사/경제 동향을 정찰했습니다.', 'text-yellow-300');
    }

    function renderInfoTable(type) {
      gameState.currentInfoTab = type;
      const thead = document.getElementById('info-table-head');
      const tbody = document.getElementById('info-table-body');
      tbody.innerHTML = '';

      if (type === 'sol') {
        thead.innerHTML = `
          <th class="p-2">주 번호 및 이름</th>
          <th class="p-2">지배 군주</th>
          <th class="p-2">수비 태수</th>
          <th class="p-2 text-right">상비군 (병력)</th>
          <th class="p-2 text-right">성벽 방어</th>
        `;
        PROVINCES.forEach(p => {
          const tr = document.createElement('tr');
          tr.className = p.ruler === gameState.rulerName ? 'bg-emerald-950/60 font-bold text-yellow-200' : 'hover:bg-blue-900/40';
          tr.innerHTML = `
            <td class="p-2">${p.id}. ${p.name}</td>
            <td class="p-2 font-bold">${p.ruler}</td>
            <td class="p-2 text-slate-300">${p.leader}</td>
            <td class="p-2 text-right text-red-300">${p.soldiers.toLocaleString()}명</td>
            <td class="p-2 text-right text-cyan-300">${p.defense}</td>
          `;
          tbody.appendChild(tr);
        });
      } else if (type === 'eco') {
        thead.innerHTML = `
          <th class="p-2">주 번호 및 이름</th>
          <th class="p-2">군주</th>
          <th class="p-2 text-right">인구수</th>
          <th class="p-2 text-right">보유 금</th>
          <th class="p-2 text-right">군량 (석)</th>
        `;
        PROVINCES.forEach(p => {
          const tr = document.createElement('tr');
          tr.className = p.ruler === gameState.rulerName ? 'bg-emerald-950/60 font-bold text-yellow-200' : 'hover:bg-blue-900/40';
          tr.innerHTML = `
            <td class="p-2">${p.id}. ${p.name}</td>
            <td class="p-2 font-bold">${p.ruler}</td>
            <td class="p-2 text-right text-white">${p.pop.toLocaleString()}</td>
            <td class="p-2 text-right text-yellow-300">${p.gold.toLocaleString()}</td>
            <td class="p-2 text-right text-emerald-300">${p.food.toLocaleString()}</td>
          `;
          tbody.appendChild(tr);
        });
      } else {
        thead.innerHTML = `
          <th class="p-2">주 번호 및 이름</th>
          <th class="p-2">군주</th>
          <th class="p-2">책사 군사</th>
          <th class="p-2 text-right">장수 수</th>
          <th class="p-2 text-right">민심 충성도</th>
        `;
        PROVINCES.forEach(p => {
          const tr = document.createElement('tr');
          tr.className = p.ruler === gameState.rulerName ? 'bg-emerald-950/60 font-bold text-yellow-200' : 'hover:bg-blue-900/40';
          tr.innerHTML = `
            <td class="p-2">${p.id}. ${p.name}</td>
            <td class="p-2 font-bold">${p.ruler}</td>
            <td class="p-2 text-cyan-300">${p.advisor}</td>
            <td class="p-2 text-right text-white">${p.officers}명</td>
            <td class="p-2 text-right text-yellow-300">${p.loyalty}</td>
          `;
          tbody.appendChild(tr);
        });
      }
    }

    // ==================== 계략 실행 ====================
    function executeStratagem(type) {
      closeAllPopups();
      const myProv = getMyCapital();
      if (myProv.gold < 150) {
        alert('계략을 실행하려면 군자금 150전이 필요합니다.');
        return;
      }
      playSfx('war');
      myProv.gold -= 150;
      updateRightPanel(myProv.id);

      const stratNames = ['', '매복의 독', '적중작적', '위서의심', '이호경식', '구호탄랑'];
      const targetProv = PROVINCES.find(p => p.ruler !== gameState.rulerName && p.ruler !== '미점령') || PROVINCES[3];

      const successRate = (gameState.difficulty === 'hard') ? 0.55 : 0.70;
      const success = Math.random() < successRate;
      if (success) {
        targetProv.loyalty = Math.max(20, targetProv.loyalty - 18);
        targetProv.defense = Math.max(20, targetProv.defense - 12);
        logMessage(`🔮 [계략 성공: ${stratNames[type]}] ${targetProv.name} (${targetProv.ruler})에 계략이 적중하여 민심(-18)과 방어력(-12)을 크게 와해시켰습니다!`, 'text-purple-300 font-bold');
        alert(`🔮 [${stratNames[type]} 성공!]\n${targetProv.name}의 적 진영에 내분이 일어나 수비 태세가 크게 무너졌습니다!`);
      } else {
        logMessage(`⚠️ [계략 간파] ${targetProv.name}의 적 군사가 계략을 사전에 간파하여 실패했습니다.`, 'text-orange-400');
        alert(`⚠️ 적 군사가 계략을 간파하여 무위로 돌아갔습니다.`);
      }
      updateRightPanel(targetProv.id);
    }

    // ==================== 외교 동맹 체결 ====================
    function executeAlliance() {
      closeAllPopups();
      const myProv = getMyCapital();
      const nonAllies = PROVINCES.filter(p => p.ruler !== gameState.rulerName && !gameState.allies.includes(p.ruler));
      if (nonAllies.length === 0) {
        alert('이미 천하의 모든 군벌과 동맹 관계이거나 적이 없습니다.');
        return;
      }
      const target = nonAllies[0];
      if (myProv.gold < 300) {
        alert('외교 동맹 예물로 금 300전이 필요합니다.');
        return;
      }
      myProv.gold -= 300;
      gameState.allies.push(target.ruler);
      playSfx('victory');
      logMessage(`🤝 [동맹 체결 성공] ${target.ruler}군과 피의 맹약을 맺었습니다! (전쟁 시 연합군 지원)`, 'text-cyan-300 font-extrabold');
      alert(`🤝 [동맹 체결]\n${target.ruler}과의 동맹이 성사되었습니다!\n이제 전장에 청색으로 표시되며 전쟁 시 연합군이 가세합니다.`);
      renderMapPins();
      updateRightPanel(myProv.id);
    }
    function executeJointOperation() { closeAllPopups(); alert('동맹군과 함께 협공할 목표 주를 지정하여 침공할 수 있습니다.'); }
    function executeBreakAlliance() { closeAllPopups(); gameState.allies = []; alert('모든 군벌과의 동맹을 파기했습니다.'); renderMapPins(); }
    function executeDiplomaticExchange() { closeAllPopups(); alert('사신을 파견하여 군마와 군량을 교환합니다.'); }

    // ==================== 개발 명령 ====================
    function executeLandDev() {
      closeAllPopups();
      const p = getMyCapital();
      if (p.gold < 100) { alert('개발 자금 100전이 필요합니다.'); return; }
      p.gold -= 100; p.food += 2500; p.loyalty = Math.min(100, p.loyalty + 3);
      playSfx('build');
      logMessage(`🌾 [개간 완료] ${p.name}의 농토를 확장하여 군량 2,500석 증가 (민심 +3)`, 'text-emerald-300 font-bold');
      updateRightPanel(p.id);
    }
    function executeFloodControl() {
      closeAllPopups();
      const p = getMyCapital();
      if (p.gold < 150) { alert('치수 자금 150전이 필요합니다.'); return; }
      p.gold -= 150; p.defense = Math.min(100, p.defense + 10);
      playSfx('build');
      logMessage(`🌊 [치수 완료] 제방을 정비하여 성벽 방어력 +10 상승!`, 'text-cyan-300 font-bold');
      updateRightPanel(p.id);
    }
    function executeCommerceDev() {
      closeAllPopups();
      const p = getMyCapital();
      if (p.gold < 120) { alert('상업 투자금 120전이 필요합니다.'); return; }
      p.gold -= 120; p.pop += 4000;
      playSfx('build');
      logMessage(`💰 [상업 투자] 저잣거리를 번영시켜 인구 4,000명 유입!`, 'text-yellow-300 font-bold');
      updateRightPanel(p.id);
    }

    // ==================== 군사 명령 ====================
    function executeConscription() {
      closeAllPopups();
      const p = getMyCapital();
      if (p.gold < 100) { alert('징병 자금 100전이 필요합니다.'); return; }
      p.gold -= 100; p.soldiers += 2500; p.loyalty = Math.max(10, p.loyalty - 6);
      playSfx('war');
      logMessage(`⚔️ [징병] 장정을 징집하여 병사 2,500명 확충 (민심 -6)`, 'text-red-300 font-bold');
      updateRightPanel(p.id);
    }
    function executeRecruit() {
      closeAllPopups();
      const p = getMyCapital();
      if (p.gold < 250) { alert('모병 자금 250전이 필요합니다.'); return; }
      p.gold -= 250; p.soldiers += 2000; p.loyalty = Math.min(100, p.loyalty + 2);
      playSfx('build');
      logMessage(`🚩 [모병] 의병을 모집하여 정예병 2,000명 합류 (민심 +2)`, 'text-emerald-300 font-bold');
      updateRightPanel(p.id);
    }
    function executeTraining() {
      closeAllPopups();
      const p = getMyCapital();
      p.defense = Math.min(100, p.defense + 5);
      playSfx('war');
      logMessage(`🛡️ [훈련] 전군 전투 훈련을 실시하여 부대 사기와 방어력을 다졌습니다.`, 'text-yellow-200');
      updateRightPanel(p.id);
    }
    function openMoveModal() { closeAllPopups(); alert('부대를 인접한 아군 영지로 이동시킵니다.'); }
    function openTransportModal() { closeAllPopups(); alert('금과 군량을 다른 본거지로 수송합니다.'); }
    function openReorganizeModal() { closeAllPopups(); alert('장수별 부대 편성을 변경합니다.'); }
    function executeShipBuilding() {
      closeAllPopups();
      const p = getMyCapital();
      if (p.gold < 300) { alert('선박 건조 자금 300전이 필요합니다.'); return; }
      p.gold -= 300;
      playSfx('build');
      logMessage(`⛵ [선박 건조] 대형 누선을 건조하여 수전 능력을 극대화했습니다.`, 'text-cyan-300 font-bold');
      updateRightPanel(p.id);
    }

    // ==================== 인사 명령 ====================
    function executeSearchOfficer() {
      closeAllPopups();
      playSfx('rest');
      const found = Math.random() < 0.65;
      if (found) {
        const pool = ['방통', '서서', '강유', '마속', '이엄', '황월영'];
        const name = pool[Math.floor(Math.random() * pool.length)];
        const p = getMyCapital();
        p.officers++;
        logMessage(`✨ [인재 발견!] 재야의 명사 '${name}'을 찾아내어 휘하로 맞이했습니다!`, 'text-yellow-300 font-black');
        alert(`✨ [인재 등용 성공!]\n재야의 인걸 '${name}'이 군주의 덕망에 감복하여 합류했습니다!`);
        updateRightPanel(p.id);
      } else {
        logMessage('🔍 천하를 수색하였으나 새로운 재야 인사를 찾지 못했습니다.', 'text-slate-400');
        alert('주변을 수색했으나 등용할 인재를 찾지 못했습니다.');
      }
    }
    function executeHireOfficer() { closeAllPopups(); alert('적국 장수를 회유하여 등용 공작을 펼칩니다.'); }
    function executeReward() {
      closeAllPopups();
      const p = getMyCapital();
      if (p.gold < 100) { alert('포상금 100전이 필요합니다.'); return; }
      p.gold -= 100;
      p.loyalty = Math.min(100, p.loyalty + 8);
      playSfx('build');
      logMessage(`🎁 [포상] 장수들에게 금과 보물을 하사하여 충성도를 높였습니다. (민심 +8)`, 'text-yellow-300');
      updateRightPanel(p.id);
    }
    function executeRelief() {
      closeAllPopups();
      const p = getMyCapital();
      if (p.food < 1000) { alert('구휼미 1000석이 필요합니다.'); return; }
      p.food -= 1000;
      p.loyalty = Math.min(100, p.loyalty + 10);
      playSfx('victory');
      logMessage(`🍚 [주민 구휼] 백성들에게 쌀을 나누어주어 민충이 크게 상승했습니다! (+10)`, 'text-emerald-300 font-bold');
      updateRightPanel(p.id);
    }
    function executeDelegate() { closeAllPopups(); alert('태수에게 영지 통치를 위임합니다.'); }
    function executeAppoint() { closeAllPopups(); alert('태수 및 군사를 새로 임명합니다.'); }
    function executeDirectOrder() { closeAllPopups(); alert('직속 명령을 하달합니다.'); }
    function executeFireOfficer() { closeAllPopups(); alert('신임하지 않는 장수를 해고합니다.'); }
    function executeConfiscate() { closeAllPopups(); alert('장수의 보물을 몰수합니다.'); }

    // ==================== 특별 명령 ====================
    function executeWander() { closeAllPopups(); if (confirm('영지를 버리고 방랑군이 되겠습니까?')) alert('방랑을 시작합니다.'); }
    function executeHeal() { closeAllPopups(); alert('명의 화타를 초빙하여 부상당한 장수를 치료합니다.'); }
    function executeEmergencyTax() {
      closeAllPopups();
      const p = getMyCapital();
      p.gold += 800; p.loyalty = Math.max(10, p.loyalty - 15);
      logMessage(`⚠️ [임시 징수] 긴급 세금 징수로 금 800전을 확보했으나 민심이 크게 하락했습니다! (-15)`, 'text-orange-400 font-bold');
      updateRightPanel(p.id);
    }
    function openTaxRateModal() { closeAllPopups(); alert('세율을 30% ~ 60% 사이로 조절합니다.'); }

    // ==================== 상인 거래 ====================
    let currentTradeType = 'sellFood';
    function openTradeModal(type) {
      closeAllPopups();
      currentTradeType = type;
      const titles = {
        sellFood: '군량 매출 (쌀 팔기)',
        buyFood: '군량 매입 (쌀 사기)',
        buyWeapons: '노궁/강노 매입',
        buyHorses: '군마 매입'
      };
      document.getElementById('trade-title').innerText = titles[type] || '상인 거래';
      const myProv = getMyCapital();
      let info = `현재 시세: 쌀 팜(${gameState.rates.riceSell}), 쌀 삼(${gameState.rates.riceBuy}), 군마(${gameState.rates.horse})<br>보유 금: <strong>${myProv.gold}전</strong> | 군량: <strong>${myProv.food}석</strong>`;
      document.getElementById('trade-info').innerHTML = info;
      openModal('trade-modal');
    }

    function confirmTrade() {
      const myProv = getMyCapital();
      const qty = parseInt(document.getElementById('trade-input').value, 10) || 1000;
      if (qty <= 0) return;

      if (currentTradeType === 'sellFood') {
        if (myProv.food < qty) { alert('보유 군량이 부족합니다.'); return; }
        myProv.food -= qty;
        const gain = Math.floor((qty / 100) * gameState.rates.riceSell);
        myProv.gold += gain;
        logMessage(`💰 [군량 판매] 군량 ${qty}석을 팔아 금 ${gain}전을 얻었습니다.`, 'text-yellow-300 font-bold');
      } else if (currentTradeType === 'buyFood') {
        const cost = Math.floor((qty / 100) * gameState.rates.riceBuy);
        if (myProv.gold < cost) { alert('군자금이 부족합니다.'); return; }
        myProv.gold -= cost;
        myProv.food += qty;
        logMessage(`🌾 [군량 구입] 금 ${cost}전으로 군량 ${qty}석을 매입했습니다.`, 'text-emerald-300 font-bold');
      } else if (currentTradeType === 'buyHorses') {
        const cost = Math.floor((qty / 10) * gameState.rates.horse);
        if (myProv.gold < cost) { alert('군자금이 부족합니다.'); return; }
        myProv.gold -= cost;
        p = myProv;
        p.defense = Math.min(100, p.defense + 8);
        logMessage(`🐎 [군마 구입] 군마를 확보하여 기병 전력을 강화했습니다! (방어력 +8)`, 'text-yellow-200 font-bold');
      }
      playSfx('build');
      closeModal('trade-modal');
      updateRightPanel(myProv.id);
    }

    // ==================== 군주 변경 ====================
    function openRulerSelectModal() { closeAllPopups(); openModal('ruler-select-modal'); }
    function changeRuler(name, provId, rulerKey) {
      closeModal('ruler-select-modal');
      gameState.rulerName = name;
      gameState.myCapitalId = provId;
      gameState.currentRuler = rulerKey;
      gameState.selectedProvId = provId;
      renderMapPins();
      updateRightPanel(provId);
      logMessage(`👑 [군주 변경] 이제부터 '${name}'으로 천하통일을 지휘합니다!`, 'text-yellow-300 font-black');
    }

    // ==================== 사운드 엔진 (Web Audio API) ====================
    function toggleBGM() {
      closeAllPopups();
      if (!gameState.audioCtx) {
        try { gameState.audioCtx = new (window.AudioContext || window.webkitAudioContext)(); } catch(e){}
      }
      gameState.bgmPlaying = !gameState.bgmPlaying;
      const statusEl = document.getElementById('bgm-status');
      const iconEl = document.getElementById('bgm-icon');

      if (gameState.bgmPlaying) {
        if (statusEl) statusEl.innerText = '재생 중';
        if (iconEl) iconEl.innerText = '🔊';
        document.getElementById('bgm-btn').className = 'px-2 py-1 text-xs font-bold rounded bg-emerald-700 hover:bg-emerald-600 text-yellow-100 border border-emerald-400 flex items-center gap-1 shadow';
        playRetroBgmLoop();
      } else {
        if (statusEl) statusEl.innerText = '정지됨';
        if (iconEl) iconEl.innerText = '🎵';
        document.getElementById('bgm-btn').className = 'px-2 py-1 text-xs font-bold rounded bg-amber-700 hover:bg-amber-600 text-yellow-100 border border-yellow-400 flex items-center gap-1 shadow';
        if (gameState.bgmTimer) { clearInterval(gameState.bgmTimer); gameState.bgmTimer = null; }
      }
    }

    function playRetroBgmLoop() {
      if (!gameState.audioCtx) return;
      const notes = [
        261.63, 293.66, 329.63, 392.00, 440.00, 523.25, 440.00, 392.00,
        329.63, 349.23, 392.00, 440.00, 523.25, 587.33, 659.25, 523.25
      ];
      let step = 0;
      gameState.bgmTimer = setInterval(() => {
        if (!gameState.bgmPlaying) return;
        playTone(notes[step % notes.length], 0.22, 'triangle', 0.12);
        if (step % 2 === 0) playTone(notes[(step + 4) % notes.length] / 2, 0.35, 'sine', 0.08);
        step++;
      }, 340);
    }

    function playTone(freq, duration, type='sine', gainVal=0.15) {
      if (!gameState.audioCtx) {
        try { gameState.audioCtx = new (window.AudioContext || window.webkitAudioContext)(); } catch(e){}
      }
      if (!gameState.audioCtx) return;
      const osc = gameState.audioCtx.createOscillator();
      const gain = gameState.audioCtx.createGain();
      osc.type = type;
      osc.frequency.setValueAtTime(freq, gameState.audioCtx.currentTime);
      gain.gain.setValueAtTime(gainVal, gameState.audioCtx.currentTime);
      gain.gain.exponentialRampToValueAtTime(0.001, gameState.audioCtx.currentTime + duration);
      osc.connect(gain);
      gain.connect(gameState.audioCtx.destination);
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
        r"C:\Users\LENOVO\Desktop\삼국지_황제의결단_웹게임.html",
        r"C:\Users\LENOVO\Desktop\sam3_update.html",
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
    generate_samguk3_final_master()
