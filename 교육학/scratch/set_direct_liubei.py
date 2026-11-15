# -*- coding: utf-8 -*-
import os
import re

def apply_direct_liubei():
    target_path = r"C:\Users\LENOVO\Desktop\삼국지_황제의결단_웹게임.html"
    with open(target_path, "r", encoding="utf-8") as f:
        html = f.read()

    # 1. intro-ruler-select-modal 을 처음에 숨김(hidden)으로 변경
    # 원래: <div id="intro-ruler-select-modal" class="fixed inset-0 modal-backdrop z-[999999] flex
    # 변경: <div id="intro-ruler-select-modal" class="fixed inset-0 modal-backdrop z-[999999] hidden flex
    html = html.replace(
        '<div id="intro-ruler-select-modal" class="fixed inset-0 modal-backdrop z-[999999] flex',
        '<div id="intro-ruler-select-modal" class="fixed inset-0 modal-backdrop z-[999999] hidden flex'
    )

    # 2. DOMContentLoaded 에서 intro modal 자동 팝업 제거하고, 곧바로 유비(형주 8번)로 세팅
    old_dom = """    window.addEventListener('DOMContentLoaded', () => {
      setupIntroFaces(); updateTroopLevelUI();
      openModal('intro-ruler-select-modal');"""

    new_dom = """    window.addEventListener('DOMContentLoaded', () => {
      // 🔥 사용자의 요청: 실행하자마자 바로 '유비'로 즉시 인게임 실행!
      changeRuler('유비', 8, 'liubei');
      updateTroopLevelUI();
      renderMapPins();
      updateRightPanel(8);
      setupRulerPortraits();
      bindKeyboardShortcuts();
      updateDifficultyUI();
      logMessage('👑 [유비 천하통일 출진] 유비(현덕)가 형주(8번)에서 대의의 깃발을 올렸습니다! (관우·장비·조운 출진 대기)', 'text-yellow-300 font-extrabold text-sm');"""

    if old_dom in html:
        html = html.replace(old_dom, new_dom)
        print("Successfully replaced DOMContentLoaded with direct Liu Bei launch!")
    else:
        # regex find
        pattern_dom = r"window\.addEventListener\('DOMContentLoaded',\s*\(\)\s*=>\s*\{[\s\S]*?openModal\('intro-ruler-select-modal'\);"
        if re.search(pattern_dom, html):
            html = re.sub(pattern_dom, new_dom.strip(), html)
            print("Successfully replaced DOMContentLoaded via regex!")

    # 3. 상단 메뉴 9. 기능에 [시나리오 / 군주 변경] 버튼 연결
    # openRulerSelectModal() 대신 openIntroModal()로 연결 가능하게
    menu_old = '<div onclick="openRulerSelectModal()" class="koei-popup-item orange">5. 군주변경 (공손찬 등)</div>'
    menu_new = '<div onclick="openModal(\'intro-ruler-select-modal\')" class="koei-popup-item !text-yellow-300 font-black">5. 시나리오/군주 선택창 열기</div>'
    if menu_old in html:
        html = html.replace(menu_old, menu_new)
        print("Successfully updated menu item for scenario/ruler select!")

    # 4. 대상 파일 4곳에 모두 저장
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
            print(f"Updated: {p} ({len(html):,} bytes)")
        except Exception as e:
            print(f"Failed {p}: {e}")

    print("=== 바로 유비 실행 설정 완료! ===")

if __name__ == "__main__":
    apply_direct_liubei()
