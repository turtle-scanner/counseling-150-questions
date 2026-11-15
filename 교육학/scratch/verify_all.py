# -*- coding: utf-8 -*-
target_path = r'C:\Users\LENOVO\Desktop\삼국지_황제의결단_웹게임.html'
with open(target_path, 'r', encoding='utf-8') as f:
    html = f.read()

checks = {
    '1. Shishe in PORTRAITS': '"shishe": "data:image/jpeg;base64,' in html,
    '2. Shishe in updateRulerPortraitDisplay': "ruler === '사섭'" in html,
    '3. Officer deploy modal present': 'id="officer-deploy-modal"' in html,
    '4. Fatigue check logic': 'off.fatigue >= 70' in html,
    '5. Invasion attackerRuler pass to duel': 'openDuelSelectModal(fromProv ? fromProv.id : null, attackerRuler)' in html,
    '6. Dynamic hex battle units': 'initHexBattleUnits' in html,
    '7. Fatigue recovery on rest': '피로도가 35% 자연 회복' in html,
    '8. Fatigue recovery on reward': '피로도가 50% 대폭 회복' in html
}

for k, v in checks.items():
    print(f'{k}: {v}')
