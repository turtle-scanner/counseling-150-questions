# -*- coding: utf-8 -*-
with open(r'C:\Users\LENOVO\Desktop\삼국지_황제의결단_웹게임.html', 'r', encoding='utf-8') as f:
    html = f.read()

checks = {
    '1. openWarModal calls openOfficerDeployModal': 'openOfficerDeployModal(target, myProv, false);' in html,
    '2. unification-ending-modal present': 'id="unification-ending-modal"' in html,
    '3. Ending story text present': '대망의 한나라 황제 즉위식' in html,
    '4. Regional maps present': 'REGIONAL_MAPS' in html,
    '5. Treasure discovery logic': 'checkTreasureDiscovery' in html,
    '6. Troop EXP gain logic': 'gainTroopExp' in html,
    '7. Golden difficulty balance': 'gameState.difficulty === \'hard\' ? 0.9' in html or 'gameState.difficulty === \'hard\'' in html,
    '8. CloseHexBattle defined': 'function closeHexBattle' in html
}

for k, v in checks.items():
    print(f"{k}: {v}")
