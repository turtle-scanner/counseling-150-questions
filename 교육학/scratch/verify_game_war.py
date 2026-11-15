# -*- coding: utf-8 -*-
import os

target = r"C:\Users\LENOVO\Desktop\삼국지_황제의결단_웹게임.html"
with open(target, "r", encoding="utf-8") as f:
    html = f.read()

checks = {
    "openWarModal": "function openWarModal(targetProvId = null, fromProvId = null)" in html,
    "openWarTargetSelectModal": "function openWarTargetSelectModal()" in html,
    "war-target-modal": 'id="war-target-modal"' in html,
    "battleStartOfficerDuel": "function battleStartOfficerDuel()" in html,
    "duel_banner_in_battle": "장수 골라 1:1 진검승부 (일기토)!" in html,
    "panel-action-btn-container": 'id="panel-action-btn-container"' in html,
    "panel_btn_inject": "이 적 영지 즉시 침공 (전쟁 개시!)" in html,
    "duel_victory_patch": "battleData.targetProv" in html and "endBattleVictory()" in html,
    "popup_personnel": 'id="popup-personnel"' in html,
    "popup_military": 'id="popup-military"' in html,
}

print("=== 검증 결과 ===")
all_ok = True
for k, v in checks.items():
    print(f"[{'PASS' if v else 'FAIL'}] {k}")
    if not v:
        all_ok = False

print("전체 통과 여부:", all_ok)
