# -*- coding: utf-8 -*-
with open(r'C:\Users\LENOVO\Desktop\sam3_update.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

funcs = [
    'openMoveModal', 'openTransportModal', 'repairFoodStorage', 'openWarModal',
    'executeConscription', 'executeRecruit', 'executeTraining', 'openReorganizeModal',
    'executeShipBuilding', 'openDuelSelectModal', 'togglePopup', 'closeAllPopups',
    'executeRest', 'handleKeyPress', 'keydown'
]

print("=== FUNCTION EXISTENCE CHECK ===")
for fn in funcs:
    idx = text.find(f'function {fn}')
    if idx == -1:
        # Check if defined as const fn = or window.fn = or in addEventListener
        idx2 = text.find(f'{fn} =')
        if idx2 == -1:
            print(f"MISSING: {fn}")
        else:
            print(f"FOUND as assign: {fn} at {idx2}")
    else:
        print(f"FOUND as func: {fn} at {idx}")

# Check keydown event listener
pos_key = text.find("addEventListener('keydown'")
if pos_key == -1:
    pos_key = text.find('addEventListener("keydown"')
if pos_key == -1:
    pos_key = text.find('onkeydown')
print(f"\nKeydown listener found at: {pos_key}")
if pos_key != -1:
    print(text[pos_key:pos_key+800].encode('ascii', errors='backslashreplace').decode('ascii'))
