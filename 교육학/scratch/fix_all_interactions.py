# -*- coding: utf-8 -*-
import os
import re

def fix():
    print("=== 모든 상호작용 및 클릭 먹통 버그 완전 박멸 빌드 시작 ===")
    target_path = r"C:\Users\LENOVO\Desktop\삼국지_황제의결단_웹게임.html"
    with open(target_path, "r", encoding="utf-8") as f:
        html = f.read()

    # 1. openModal & closeModal 안전 가드 (Null pointer exception 완전 박멸!)
    old_modals = r'function openModal\(id\)\s*\{\s*document\.getElementById\(id\)\.classList\.remove\(\'hidden\'\);\s*\}\s*function closeModal\(id\)\s*\{\s*document\.getElementById\(id\)\.classList\.add\(\'hidden\'\);\s*\}'
    new_modals = """function openModal(id) {
      const el = document.getElementById(id);
      if (el) el.classList.remove('hidden');
    }
    function closeModal(id) {
      const el = document.getElementById(id);
      if (el) el.classList.add('hidden');
    }"""
    html = re.sub(old_modals, new_modals, html)

    # 2. changeRuler 안전 가드
    old_changeruler = r'function changeRuler\(name,\s*provId,\s*rulerKey\)\s*\{[\s\S]*?logMessage\(`👑 \[군주 변경\][\s\S]*?\}\s*\}'
    new_changeruler = """function changeRuler(name, provId, rulerKey) {
      closeModal('ruler-select-modal');
      closeModal('intro-ruler-select-modal');
      gameState.rulerName = name;
      gameState.myCapitalId = provId;
      gameState.currentRuler = rulerKey;
      gameState.selectedProvId = provId;
      renderMapPins();
      updateRightPanel(provId);
      logMessage(`👑 [군주 변경] 이제부터 '${name}'(으)로 천하통일을 지휘합니다!`, 'text-yellow-300 font-black');
    }"""
    html = re.sub(old_changeruler, new_changeruler, html)

    # 3. DOMContentLoaded 완벽 재정비 (안전한 초기화 순서)
    pattern_dom = r"window\.addEventListener\('DOMContentLoaded',\s*\(\)\s*=>\s*\{[\s\S]*?logMessage\('👑 \[유비 천하통일 출진\][\s\S]*?\}\s*\);"
    new_dom = """window.addEventListener('DOMContentLoaded', () => {
      try {
        gameState.rulerName = '유비';
        gameState.myCapitalId = 8;
        gameState.currentRuler = 'liubei';
        gameState.selectedProvId = 8;

        renderMapPins();
        updateRightPanel(8);
        setupRulerPortraits();
        updateTroopLevelUI();
        bindKeyboardShortcuts();
        updateDifficultyUI();
        logMessage('👑 [유비 천하통일 출진] 유비(현덕)가 형주(8번)에서 대의의 깃발을 올렸습니다! (관우·장비·조운 출진 대기)', 'text-yellow-300 font-extrabold text-sm');
      } catch (err) {
        console.error('Initialization error:', err);
      }
    });"""
    html = re.sub(pattern_dom, new_dom, html)

    # 4. 상단 메뉴 버튼 및 팝업 z-index 최상위 보장
    # 혹시 모를 오버레이 투명 레이어 차단
    css_fix = """
    /* 지도 핀 클릭 보장 및 z-index 최상위 */
    #map-pins-layer {
      position: absolute;
      inset: 0;
      pointer-events: auto !important;
      z-index: 50 !important;
    }
    .map-pin {
      position: absolute;
      cursor: pointer !important;
      pointer-events: auto !important;
      z-index: 60 !important;
      transform: translate(-50%, -50%);
    }
    .menu-btn {
      cursor: pointer !important;
      pointer-events: auto !important;
    }
    .koei-popup-window {
      z-index: 9999999 !important;
    }
    """
    html = html.replace("</style>", f"\n{css_fix}\n</style>")

    # 5. 대상 파일 4곳에 저장
    paths = [
        r"C:\Users\LENOVO\Desktop\삼국지_황제의결단_웹게임.html",
        r"C:\Users\LENOVO\Desktop\sam3_update.html",
        r"g:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\samgukji.html",
        r"g:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\교육학\samgukji.html"
    ]

    for p in paths:
        try:
            with open(p, "w", encoding="utf-8") as f:
                f.write(html)
            print(f"Generated: {p} ({len(html):,} bytes)")
        except Exception as e:
            print(f"Failed {p}: {e}")

    print("=== 모든 수정 완료! ===")

if __name__ == "__main__":
    fix()
