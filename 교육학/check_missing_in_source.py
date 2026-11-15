# -*- coding: utf-8 -*-
import os

source_file = r'G:\내 드라이브\ANTI GRAVITY\시험준비(패턴)\교육학\scratch\temp_script1.js'
with open(source_file, 'r', encoding='utf-8', errors='ignore') as f:
    code = f.read()

missing_list = [
  'battleActionAttack', 'battleActionRaidStorage', 'battleActionTrap', 'battleStartOfficerDuel',
  'clearLogs', 'confirmTrade', 'duelAction', 'executeAlliance', 'executeAppoint', 'executeBreakAlliance',
  'executeCommerceDev', 'executeConfiscate', 'executeDelegate', 'executeDirectOrder', 'executeEmergencyTax',
  'executeFireOfficer', 'executeFloodControl', 'executeHeal', 'executeHireOfficer', 'executeJointOperation',
  'executeLandDev', 'executeRelief', 'executeSearchOfficer', 'executeStratagem', 'executeTraining',
  'executeTreasureSearch', 'executeWander', 'handleInvasionDefend', 'handleInvasionDuel', 'handleInvasionHexBattle',
  'onCmdAmbushSkill', 'openDuelSelectModal', 'openInfoModal', 'openQuestModal', 'openReorganizeModal',
  'openTaxRateModal', 'openTradeModal', 'openTreasureModal', 'renderInfoTable', 'reorganizeSoldiers',
  'retreatFromBattleModal', 'selectScenario', 'toggleBGM'
]

found_in_src = []
not_found = []
for fn in missing_list:
    if f'function {fn}' in code or f'{fn} =' in code:
        found_in_src.append(fn)
    else:
        not_found.append(fn)

print(f"Found in temp_script1.js ({len(found_in_src)}): {found_in_src}")
print(f"Not found in temp_script1.js ({len(not_found)}): {not_found}")
