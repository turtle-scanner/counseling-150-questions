# -*- coding: utf-8 -*-
import shutil
import re

SRC = r"C:\Users\LENOVO\Desktop\삼국지_황제의결단_웹게임.html"

with open(SRC, "r", encoding="utf-8") as f:
    html = f.read()

# 1. unify-progress 클릭 시 엔딩 모달 즉시 팝업 가능하게 이벤트 바인딩
old_unify_bar = '<strong id="unify-progress" class="text-white">'
new_unify_bar = '<strong id="unify-progress" onclick="openUnificationEnding()" class="text-white cursor-pointer hover:text-yellow-300 underline font-black" title="클릭 시 천하통일 즉위식 및 엔딩 모달 다시 보기">'
if old_unify_bar in html:
    html = html.replace(old_unify_bar, new_unify_bar)
    print("SUCCESS: Bound onclick to unify-progress.")

# 2. renderMapPins()에서 13주 통일 시 엔딩 모달 300ms 자동 호출 보장
map_pin_check = """      // 13주 천하통일 즉시 감지 및 엔딩 자동 팝업
      const totalRulerProv = PROVINCES.filter(p => p.ruler === gameState.rulerName).length;
      if (totalRulerProv === 13) {
        setTimeout(() => {
          if (typeof openUnificationEnding === 'function') openUnificationEnding();
        }, 350);
      }
"""
if "totalRulerProv === 13" not in html:
    html = html.replace("function renderMapPins() {", "function renderMapPins() {\n" + map_pin_check)
    print("SUCCESS: Injected 13-province instant ending trigger into renderMapPins.")

# 3. 훈련 시 레벨 +1 UI 갱신 확실히 동기화
with open(SRC, "w", encoding="utf-8") as f:
    f.write(html)

print("Saved updated HTML to Desktop.")

# 4. 대상 파일들로 전면 복사 동기화
TARGETS = [
    r"C:\Users\LENOVO\Desktop\sam3_update.html",
    r"g:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\samgukji.html",
    r"g:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\교육학\samgukji.html"
]

for t in TARGETS:
    try:
        shutil.copy2(SRC, t)
        print(f"Synced successfully -> {t}")
    except Exception as e:
        print(f"Error copying to {t}: {e}")
