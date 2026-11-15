# -*- coding: utf-8 -*-
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='backslashreplace')
from playwright.sync_api import sync_playwright

URL = 'file:///C:/Users/LENOVO/Desktop/sam3_update.html'
errors = []
dialogs = []

with sync_playwright() as p:
    b = p.chromium.launch(headless=True)
    pg = b.new_page(viewport={'width': 1400, 'height': 900})
    pg.on('pageerror', lambda e: errors.append('PAGEERROR: ' + str(e)))
    pg.on('console', lambda m: errors.append('CONSOLE.' + m.type + ': ' + m.text) if m.type == 'error' else None)
    pg.on('dialog', lambda d: (dialogs.append(d.message.replace('\n', ' ')[:120]), d.accept()))
    pg.goto(URL)
    pg.wait_for_timeout(1500)

    print('1. Initial errors:', errors)
    print('   Visible modals at load:', pg.evaluate("""() => [...document.querySelectorAll('[id$="-modal"]')].filter(e => getComputedStyle(e).display !== 'none').map(e => e.id)"""))

    # 1) Click start button inside liu-bei-intro-modal
    pg.click('#liu-bei-intro-modal button:has-text("게임 시작")', timeout=3000)
    pg.wait_for_timeout(400)
    print('2. After start click -> visible modals:', pg.evaluate("""() => [...document.querySelectorAll('[id$="-modal"]')].filter(e => getComputedStyle(e).display !== 'none').map(e => e.id)"""))
    print('   Errors so far:', errors)

    # 2) Click 1. 군사 -> 7. 훈련
    pg.click('button.menu-btn:has-text("1. 군사")', timeout=3000)
    pg.wait_for_timeout(300)
    soldiers_before = pg.evaluate('() => getMyCapital().soldiers')
    exp_before = pg.evaluate('() => gameState.troopExp')
    pg.click('#popup-military .koei-popup-item:has-text("7.")', timeout=3000)
    pg.wait_for_timeout(400)
    soldiers_after = pg.evaluate('() => getMyCapital().soldiers')
    exp_after = pg.evaluate('() => gameState.troopExp')
    print(f'3. After Training click -> soldiers: {soldiers_before} -> {soldiers_after}, exp: {exp_before} -> {exp_after}')
    print('   Errors so far:', errors)

    # 3) Click 3. 외교 -> 1. 동맹체결 (유비-공손찬 동맹)
    pg.click('button.menu-btn:has-text("3. 외교")', timeout=3000)
    pg.wait_for_timeout(300)
    pg.click('#popup-diplomacy .koei-popup-item:has-text("1.")', timeout=3000)
    pg.wait_for_timeout(400)
    allies = pg.evaluate('() => gameState.allies')
    print('4. After Alliance click -> allies:', allies, 'dialogs:', dialogs[-1] if dialogs else None)
    print('   Errors so far:', errors)

    # 4) Select province 10 (익주) on map or call updateRightPanel(10), then click 침공작전 개시 button
    pg.evaluate('() => { gameState.selectedProvId = 10; updateRightPanel(10); }')
    pg.wait_for_timeout(300)
    pg.click('#province-context-action button', timeout=3000)
    pg.wait_for_timeout(500)
    vis_modals = pg.evaluate("""() => [...document.querySelectorAll('[id$="-modal"]')].filter(e => getComputedStyle(e).display !== 'none').map(e => e.id)""")
    hex_open = pg.evaluate("""() => { const el = document.getElementById('sam5-battle-modal') || document.getElementById('officer-deploy-modal') || document.getElementById('hex-battle-modal'); return el ? getComputedStyle(el).display : 'none'; }""")
    print('5. After Attack button click -> visible modals:', vis_modals, 'battle/deploy display:', hex_open)
    print('   Dialogs:', dialogs)
    print('   FINAL ERRORS:', errors)
    b.close()
