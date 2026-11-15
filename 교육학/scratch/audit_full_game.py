# -*- coding: utf-8 -*-
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

TARGET_FILE = r"C:\Users\LENOVO\Desktop\삼국지_황제의결단_웹게임.html"

with open(TARGET_FILE, "r", encoding="utf-8") as f:
    html = f.read()

print("="*60)
print("1. HTML 및 SCRIPT 구조 분석")
print("="*60)

scripts = re.findall(r"<script[\s\S]*?>([\s\S]*?)</script>", html, re.IGNORECASE)
print(f"Total script tags found: {len(scripts)}")

# 1. HTML 내 모든 id 추출
all_ids_in_html = set(re.findall(r'id=["\']([^"\']+)["\']', html))
print(f"Total HTML element IDs defined: {len(all_ids_in_html)}")

# 2. JS에서 getElementById로 참조하는 모든 ID 추출
all_get_ids = set()
for sc in scripts:
    matches = re.findall(r'document\.getElementById\(["\']([^"\']+)["\']\)', sc)
    all_get_ids.update(matches)

missing_ids = [gid for gid in all_get_ids if gid not in all_ids_in_html]
print(f"Total IDs accessed by getElementById: {len(all_get_ids)}")
if missing_ids:
    print(f"[!] MISSING IDs in HTML ({len(missing_ids)}): {missing_ids}")
else:
    print("[OK] All getElementById() target IDs exist perfectly in HTML!")

# 3. HTML onclick에서 호출하는 모든 함수 추출
onclick_calls = re.findall(r'onclick=["\']\s*([a-zA-Z0-9_]+)\s*\(', html)
all_onclick_funcs = set(onclick_calls)

# JS에서 정의된 모든 함수 이름 추출
defined_funcs = set()
for sc in scripts:
    fn_matches = re.findall(r'function\s+([a-zA-Z0-9_]+)\s*\(', sc)
    defined_funcs.update(fn_matches)

print(f"Total functions defined in scripts: {len(defined_funcs)}")
print(f"Total functions called via onclick: {len(all_onclick_funcs)}")

missing_onclick_funcs = [fn for fn in all_onclick_funcs if fn not in defined_funcs]
if missing_onclick_funcs:
    print(f"[!] MISSING onclick functions ({len(missing_onclick_funcs)}): {missing_onclick_funcs}")
else:
    print("[OK] All onclick functions are 100% defined in JavaScript!")

# 4. 삼국지 3 14대 메뉴 및 핵심 기능 함수 확인
essential_funcs = [
    "executeTraining", "executeRest", "nextTurn", "consumeActionPoint", "refundActionPoint",
    "openUnificationEnding", "checkUnification", "renderMapPins", "updateRightPanel",
    "handleHexClick", "selectUnit", "deselectUnit", "updateActionCommands", "disableAllCommands",
    "computeMovementRange", "executeSkillAction", "finishUnitAction", "endPlayerTurn",
    "calculateCombatDamage", "applyDamage", "getOfficerDuelWar", "openFormationModal",
    "onCmdAttack", "onCmdArchery", "onCmdFireSkill", "onCmdChaosSkill", "onCmdFlurry", "onCmdDuel", "onCmdWait"
]

missing_essentials = [fn for fn in essential_funcs if fn not in defined_funcs]
if missing_essentials:
    print(f"[!] MISSING Essential functions: {missing_essentials}")
else:
    print("[OK] All Essential Game & Battle functions are 100% present!")

print("="*60)
