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
    pg.wait_for_timeout(1200)

    # 1) Close intro modal
    pg.click('#liu-bei-intro-modal button:has-text("게임 시작")', timeout=3000)
    pg.wait_for_timeout(300)
    print('1. Intro closed. Errors:', errors)

    # 2) Training (1. 군사 -> 7. 훈련)
    pg.click('button.menu-btn:has-text("1. 군사")', timeout=3000)
    pg.wait_for_timeout(200)
    pg.click('#popup-military .koei-popup-item:has-text("7.")', timeout=3000)
    pg.wait_for_timeout(400)
    # If troop-promotion-modal opened, close it!
    promo_vis = pg.evaluate("""() => { const e = document.getElementById('troop-promotion-modal'); return e && getComputedStyle(e).display !== 'none'; }""")
    print('2. Training executed. Promotion modal visible:', promo_vis, 'Errors:', errors)
    if promo_vis:
        pg.click('#troop-promotion-modal button', timeout=3000)
        pg.wait_for_timeout(300)

    # 3) Rest (0. 휴양)
    month_before = pg.evaluate('() => gameState.month')
    pg.click('button.menu-btn:has-text("0. 휴양")', timeout=3000)
    pg.wait_for_timeout(500)
    # Close any modal opened during rest (e.g., invasion or promotion)
    open_modals = pg.evaluate("""() => [...document.querySelectorAll('[id$="-modal"]')].filter(e => getComputedStyle(e).display !== 'none').map(e => e.id)""")
    month_after = pg.evaluate('() => gameState.month')
    print(f'3. Rest executed -> month: {month_before} -> {month_after}, open_modals: {open_modals}, Errors: {errors}')
    for mid in open_modals:
        pg.evaluate(f"closeModal('{mid}')")

    # 4) Alliance (3. 외교 -> 1. 동맹체결: 유비-공손찬 동맹)
    pg.click('button.menu-btn:has-text("3. 외교")', timeout=3000)
    pg.wait_for_timeout(200)
    pg.click('#popup-diplomacy .koei-popup-item:has-text("1.")', timeout=3000)
    pg.wait_for_timeout(400)
    print('4. Alliance executed -> allies:', pg.evaluate('() => gameState.allies'), 'Errors:', errors)

    # 5) Attack (10. 익주 침공작전 개시)
    pg.evaluate('() => { gameState.selectedProvId = 10; updateRightPanel(10); }')
    pg.wait_for_timeout(300)
    pg.click('#province-context-action button', timeout=3000)
    pg.wait_for_timeout(500)
    open_modals_after_war = pg.evaluate("""() => [...document.querySelectorAll('[id$="-modal"]')].filter(e => getComputedStyle(e).display !== 'none').map(e => e.id)""")
    print('5. Attack executed -> open modals:', open_modals_after_war, 'Errors:', errors)
    print('   Dialogs:', dialogs)
    b.close()
