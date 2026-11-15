# -*- coding: utf-8 -*-
import sys
import re

def main():
    target_path = r'C:\Users\LENOVO\Desktop\삼국지_황제의결단_웹게임.html'
    with open(target_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # 사섭 base64 로드
    with open(r'g:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\교육학\scratch\shishe_b64.txt', 'r', encoding='utf-8') as f:
        shishe_b64 = f.read().strip()

    # 1. 중복된 레거시 인트로 블록 제거
    legacy_start = '<div class="text-right">\n          <span class="px-3 py-1 bg-blue-950 border border-blue-500 rounded text-xs text-cyan-300 font-bold">\n            1. 시나리오 : 2. 난세, 군웅 전토를 할거'
    legacy_end = '<button onclick="confirmIntroStart()" class="px-8 py-3 bg-gradient-to-r from-red-600 via-amber-600 to-red-600 hover:from-red-500 hover:to-amber-500 text-yellow-100 font-black text-sm rounded-lg border-2 border-yellow-300 shadow-2xl flex items-center gap-2 animate-pulse">\n          <span>⚔️</span> 선택한 군주로 천하통일 출진!\n        </button>\n      </div>\n\n    </div>\n  </div>'

    if legacy_start in html and legacy_end in html:
        idx1 = html.find(legacy_start)
        idx2 = html.find(legacy_end) + len(legacy_end)
        html = html[:idx1] + html[idx2:]
        print("중복된 레거시 인트로 모달 코드 완전 제거 성공!")
    else:
        print("경고: 레거시 인트로 블록 검색 실패, 정규식 시도...")
        pattern = re.compile(r'<div class="text-right">\s*<span[^>]*>\s*1\.\s*시나리오\s*:[^<]*</span>\s*</div>\s*</div>\s*<!-- 난이도 설정 바 -->[\s\S]*?<button onclick="confirmIntroStart\(\)"[^>]*>[\s\S]*?</div>\s*</div>', re.MULTILINE)
        m = pattern.search(html)
        if m:
            html = html[:m.start()] + html[m.end():]
            print("정규식으로 레거시 인트로 블록 제거 성공!")

    # 2. 인트로 군주 카드에 사섭(교주 9번) 추가 (총 12+1 군주)
    shishe_card = f"""
          <!-- 13. 사섭 (교주 군주) -->
          <div onclick="selectIntroRuler('사섭', 9, 'shishe')" class="intro-ruler-card p-2 rounded border-2 cursor-pointer transition flex flex-col items-center bg-blue-950/90 border-blue-700 hover:border-yellow-400 shadow" id="card-사섭">
            <img src="{shishe_b64}" class="w-16 h-20 object-cover rounded border border-amber-500/80 mb-1.5 shadow ring-1 ring-purple-500" alt="사섭">
            <div class="font-black text-xs text-white">13. 사섭 (위언)</div>
            <div class="text-[10px] text-purple-300 font-bold bg-purple-950/90 px-2 py-0.5 rounded border border-purple-600 mt-1">교주/남월 (9번)</div>
          </div>"""

    if 'id="card-사섭"' not in html:
        # 공융 카드 뒤에 삽입
        target_marker = '<div class="font-black text-xs text-white">12. 공융 (문거)</div>\n            <div class="text-[10px] text-lime-300 font-bold bg-lime-950/90 px-2 py-0.5 rounded border border-lime-600 mt-1">북해/청주 (3번)</div>\n          </div>'
        if target_marker in html:
            html = html.replace(target_marker, target_marker + "\n" + shishe_card)
            print("인트로에 사섭 카드 추가 성공!")

    # 3. 화면 상단에 v3.5 최신 업데이트 배너 탑재
    update_banner_html = """
  <!-- ==================== ✨ v3.5 최신 업데이트 완료 알림 배너 ==================== -->
  <div id="v35-update-banner" class="w-full bg-gradient-to-r from-red-950 via-amber-950 to-blue-950 border-b-2 border-yellow-400 py-1.5 px-3 flex items-center justify-between text-xs shadow-lg z-[999999] relative">
    <div class="flex items-center gap-2 overflow-x-auto">
      <span class="px-2 py-0.5 bg-red-600 text-white font-black rounded text-[10px] animate-pulse">v3.5 최신판</span>
      <span class="text-yellow-300 font-bold">✨ [최신 업데이트 완료]</span>
      <span class="text-slate-200">⚔️ 전쟁 출전 장수 3인 선발 | 💤 피로도 70% 출전제한 & 휴양/포상 회복 | 🏹 교주 사섭 초상화 매칭 | 🛡️ 손책군 침공 요격 일기토 버그 수리 완료!</span>
    </div>
    <button onclick="document.getElementById('v35-update-banner').style.display='none'" class="text-amber-300 hover:text-white font-mono text-xs px-2 py-0.5 border border-amber-600/60 rounded">
      ✕ 닫기
    </button>
  </div>
"""

    if 'id="v35-update-banner"' not in html:
        html = html.replace('<header id="main-header"', update_banner_html + '\n  <header id="main-header"')
        print("v3.5 최신 업데이트 배너 탑재 성공!")

    # 4. 저장 및 동기화
    with open(target_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print("데스크톱 파일 저장 완료!")

    for p in [r"C:\Users\LENOVO\Desktop\sam3_update.html",
              r"g:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\samgukji.html",
              r"g:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\교육학\samgukji.html"]:
        with open(p, 'w', encoding='utf-8') as f:
            f.write(html)
    print("모든 복사본 및 Git 파일 동기화 완료!")

if __name__ == "__main__":
    main()
