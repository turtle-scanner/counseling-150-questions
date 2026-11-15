# -*- coding: utf-8 -*-
with open(r'C:\Users\LENOVO\Desktop\삼국지_황제의결단_웹게임.html', 'r', encoding='utf-8') as f:
    html = f.read()

checks = {
    '1. closeHexBattle defined': 'function closeHexBattle(isVictory = false)' in html,
    '2. confirmExitBattleToMap defined': 'function confirmExitBattleToMap()' in html,
    '3. triggerVictory calls closeHexBattle(true)': 'closeHexBattle(true);' in html,
    '4. triggerDefeat calls closeHexBattle(false)': 'closeHexBattle(false);' in html,
    '5. checkMaxLoyaltyVolunteers defined': 'function checkMaxLoyaltyVolunteers(prov)' in html,
    '6. 8000 soldiers reward in code': 'rewardSoldiers = 8000;' in html,
    '7. loyalty hint in right panel': 'loyalty-volunteers-hint' in html,
    '8. executeRelief triggers checkMaxLoyaltyVolunteers': 'checkMaxLoyaltyVolunteers(myProv);' in html
}

for k, v in checks.items():
    print(f"{k}: {v}")
