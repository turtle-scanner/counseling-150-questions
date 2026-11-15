# -*- coding: utf-8 -*-
with open(r'C:\Users\LENOVO\Desktop\sam3_update.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

funcs = [
    'openMoveModal', 'openTransportModal', 'repairFoodStorage', 'openWarModal',
    'executeConscription', 'executeRecruit', 'executeTraining', 'openReorganizeModal',
    'executeShipBuilding', 'openDuelSelectModal', 'togglePopup', 'closeAllPopups'
]

for fn in funcs:
    idx = text.find(f'function {fn}')
    if idx == -1:
        print(f"MISSING FUNCTION: function {fn} not found in JS!")
    else:
        end = text.find('}', idx)
        print(f"FOUND: function {fn}")
        snippet = text[idx:min(idx+200, len(text))].replace('\n', ' ')
        print(f"   {snippet[:100]}...")
